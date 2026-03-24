"""
크롤러 기본 추상 클래스
새 기업 추가 시 이 클래스를 상속받아 구현
"""
import json
import re
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional

from models.job import NaruJob
from config import CRAWL_DELAY

# rules 디렉토리 경로
RULES_DIR = Path(__file__).parent.parent / "rules"


class BaseCrawler(ABC):
    """모든 기업 크롤러의 베이스 클래스"""

    def __init__(self, company_slug: str):
        self.company_slug = company_slug
        self._position_rules = self._load_rules("position_rules.json")
        self._location_rules = self._load_rules("location_rules.json")
        self._experience_rules = self._load_rules("experience_rules.json")

    def _load_rules(self, filename: str) -> dict:
        path = RULES_DIR / filename
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def _sleep(self):
        """크롤링 딜레이 (서버 부하 방지)"""
        time.sleep(CRAWL_DELAY)

    def classify_position(self, text: str) -> str:
        """
        제목/카테고리 텍스트로 포지션 분류
        rules/position_rules.json 기준
        """
        for rule in self._position_rules["rules"]:
            for keyword in rule["keywords"]:
                if keyword.lower() in text.lower():
                    return rule["position"]
        return "OTHER"

    def classify_locations(self, text: str) -> List[str]:
        """
        텍스트에서 근무지 추출
        rules/location_rules.json 기준
        """
        found = []
        text_lower = text.lower()
        for rule in self._location_rules["rules"]:
            for keyword in rule["keywords"]:
                if keyword in text:  # 일본어는 lower() 불필요
                    loc = rule["location"]
                    if loc not in found:
                        found.append(loc)
                    break  # 같은 location은 한 번만
        return found if found else [self._location_rules.get("default", "OTHER_JAPAN")]

    def classify_experience(self, text: str) -> str:
        """
        텍스트에서 경력 수준 분류
        rules/experience_rules.json 기준
        """
        for rule in self._experience_rules["rules"]:
            for keyword in rule["keywords"]:
                if keyword in text:
                    return rule["level"]
        return self._experience_rules.get("default", "MID")

    def detect_work_type(self, text: str) -> str:
        """근무 형태 감지"""
        if any(k in text for k in ["フルリモート", "完全在宅", "完全リモート"]):
            return "REMOTE"
        if any(k in text for k in ["ハイブリッド", "リモート", "在宅", "テレワーク"]):
            return "HYBRID"
        return "ONSITE"

    def extract_tech_stack(self, text: str) -> List[str]:
        """텍스트에서 기술 스택 키워드 추출"""
        tech_keywords = [
            "Java", "Python", "Go", "Ruby", "PHP", "C#", "C++", "Scala", "Kotlin", "Swift",
            "JavaScript", "TypeScript", "React", "Vue", "Angular", "Node.js",
            "Spring", "Django", "Rails", "FastAPI",
            "AWS", "Azure", "GCP", "Kubernetes", "Docker", "Terraform", "Ansible",
            "PostgreSQL", "MySQL", "MongoDB", "Redis", "Elasticsearch",
            "SAP", "Salesforce", "ServiceNow",
            "TensorFlow", "PyTorch", "scikit-learn",
            "Spark", "Hadoop", "Kafka",
        ]
        found = []
        for tech in tech_keywords:
            if tech.lower() in text.lower():
                found.append(tech)
        return found

    @abstractmethod
    def fetch_job_list(self, limit: Optional[int] = None) -> List[dict]:
        """공고 목록 가져오기 (raw 데이터)"""
        pass

    @abstractmethod
    def fetch_job_detail(self, job_id: str) -> Optional[dict]:
        """공고 상세 정보 가져오기 (raw 데이터)"""
        pass

    @abstractmethod
    def parse_job(self, raw: dict) -> Optional[NaruJob]:
        """raw 데이터 → NaruJob 변환"""
        pass

    def crawl(self, limit: Optional[int] = None) -> List[NaruJob]:
        """
        전체 크롤링 실행
        목록 → 상세 → 파싱 → NaruJob 반환
        """
        print(f"[{self.company_slug}] 공고 목록 수집 중...")
        raw_list = self.fetch_job_list(limit=limit)
        print(f"[{self.company_slug}] 총 {len(raw_list)}개 공고 발견")

        jobs = []
        for i, raw in enumerate(raw_list):
            job_id = raw.get("id", "unknown")
            try:
                detail = self.fetch_job_detail(str(job_id))
                if detail:
                    raw.update(detail)

                job = self.parse_job(raw)
                if job:
                    jobs.append(job)
                    print(f"  [{i+1}/{len(raw_list)}] ✅ {job.title[:40]}")
                else:
                    print(f"  [{i+1}/{len(raw_list)}] ⚠️  파싱 실패: job_id={job_id}")
            except Exception as e:
                print(f"  [{i+1}/{len(raw_list)}] ❌ 에러 (job_id={job_id}): {e}")

            self._sleep()

        print(f"[{self.company_slug}] 파싱 완료: {len(jobs)}/{len(raw_list)}개")
        return jobs
