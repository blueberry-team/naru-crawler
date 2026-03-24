"""
히타치(日立製作所) 크롤러
jscudp.jcareers.com API 사용
"""
import re
import html
from typing import List, Optional

import requests
from bs4 import BeautifulSoup

from companies.base import BaseCrawler
from models.job import NaruJob
from config import HITACHI_API_BASE, HITACHI_REFERER

COMPANY_SLUG = "hitachi"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Referer": HITACHI_REFERER,
    "Accept": "application/json",
}


class HitachiCrawler(BaseCrawler):
    """히타치 채용 공고 크롤러"""

    def __init__(self):
        super().__init__(COMPANY_SLUG)
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    # ──────────────────────────────────────────
    # 공고 목록 수집
    # ──────────────────────────────────────────

    def fetch_job_list(self, limit: Optional[int] = None) -> List[dict]:
        """히타치 전체 공고 목록 API에서 수집"""
        resp = self.session.get(HITACHI_API_BASE, params={"job_list": 1})
        resp.raise_for_status()
        data = resp.json()

        jobs = []
        self._extract_jobs_recursive(data, jobs)

        if limit:
            jobs = jobs[:limit]
        return jobs

    def _extract_jobs_recursive(self, obj, result: list, category: str = ""):
        """JSON 트리에서 job 항목 재귀적으로 추출"""
        if not isinstance(obj, dict):
            return
        for key, value in obj.items():
            if key.startswith("job_category") and isinstance(value, dict):
                cat_name = value.get("name", category)
                self._extract_jobs_recursive(value, result, cat_name)
            elif key == "job" and isinstance(value, dict):
                for _, job_data in value.items():
                    if isinstance(job_data, dict) and "name" in job_data:
                        job_data["_category"] = category
                        result.append(job_data)
            elif isinstance(value, dict):
                self._extract_jobs_recursive(value, result, category)

    # ──────────────────────────────────────────
    # 공고 상세 수집
    # ──────────────────────────────────────────

    def fetch_job_detail(self, job_id: str) -> Optional[dict]:
        """개별 공고 상세 API 호출"""
        try:
            resp = self.session.get(HITACHI_API_BASE, params={"job_code1": job_id})
            resp.raise_for_status()
            data = resp.json()
            # 상세 응답에서 job 항목 찾기
            return self._find_job_detail(data, job_id)
        except Exception as e:
            print(f"    상세 fetch 실패 (id={job_id}): {e}")
            return None

    def _find_job_detail(self, data: dict, job_id: str) -> Optional[dict]:
        """상세 API 응답에서 job 데이터 추출"""
        if not isinstance(data, dict):
            return None
        for key, value in data.items():
            if isinstance(value, dict):
                if "description" in value or "duty_description" in value:
                    return value
                result = self._find_job_detail(value, job_id)
                if result:
                    return result
        return None

    # ──────────────────────────────────────────
    # 파싱: raw 데이터 → NaruJob
    # ──────────────────────────────────────────

    def parse_job(self, raw: dict) -> Optional[NaruJob]:
        """히타치 raw 데이터를 NaruJob으로 변환"""
        job_id = str(raw.get("id", ""))
        title = self._clean_text(raw.get("name", ""))
        category = raw.get("_category", "")
        location_text = raw.get("location", "") or ""

        if not title:
            return None

        # 분류
        classify_text = f"{title} {category}"
        position = self.classify_position(classify_text)
        locations = self.classify_locations(f"{title} {location_text}")
        experience = self.classify_experience(title)
        work_type = self.detect_work_type(title + " " + (raw.get("description", "") or ""))
        tech_stack = self.extract_tech_stack(title)

        # overview 구성 (상세 있으면 우선)
        desc = self._clean_html(raw.get("description", "") or "")
        duty = self._clean_html(raw.get("duty_description", "") or "")
        requirement = self._clean_html(raw.get("requirement", "") or "")

        overview = desc or f"【{category}】{title}"
        if requirement:
            overview += f"\n\n【応募資格】\n{requirement}"

        # tasks 구성
        tasks = []
        if duty:
            # 개행으로 분리
            for line in duty.split("\n"):
                line = line.strip().lstrip("・•●▶︎▼■").strip()
                if line and len(line) > 3:
                    tasks.append(line)
        if not tasks:
            tasks = [title]  # 최소 1개 보장

        # 기술 스택 보강
        if not tech_stack:
            tech_stack = self.extract_tech_stack(overview + " " + duty)

        return NaruJob(
            company_slug=COMPANY_SLUG,
            title=title,
            position=position,
            locations=locations,
            experience_level=experience,
            overview=overview if len(overview) >= 50 else f"{title}\n\n{category} 부문의 채용 공고입니다.\n\n{overview}",
            tasks=tasks,
            work_type=work_type,
            tech_stack=tech_stack,
            source_id=job_id,
            source_url=f"https://hitachi.jposting.net/u/entry.phtml?job_code1={job_id}",
        )

    # ──────────────────────────────────────────
    # 유틸리티
    # ──────────────────────────────────────────

    def _clean_text(self, text: str) -> str:
        """텍스트 정리"""
        if not text:
            return ""
        # HTML 엔티티 디코딩
        text = html.unescape(text)
        # 불필요한 공백 제거
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def _clean_html(self, html_text: str) -> str:
        """HTML → 일반 텍스트 변환"""
        if not html_text:
            return ""
        soup = BeautifulSoup(html_text, "html.parser")
        # <br>, <p>, <li> → 개행
        for tag in soup.find_all(["br", "p", "li"]):
            tag.insert_after("\n")
        text = soup.get_text()
        # 연속 개행 정리
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        return text
