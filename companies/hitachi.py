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

    # job_items: 목록 API에서 추가로 요청할 필드
    JOB_ITEMS = [
        ("job_items[]", "description"),   # 직무 상세 설명
        ("job_items[]", "location"),      # 근무지
        ("job_items[]", "requirement"),   # 지원 자격
        ("job_items[]", "positions"),     # 포지션 태그
    ]

    def fetch_job_list(self, limit: Optional[int] = None) -> List[dict]:
        """
        히타치 전체 공고 목록 + 상세 필드 한 번에 수집
        job_items[] 파라미터로 description 등 포함 → 상세 API 개별 호출 불필요
        """
        params = [("job_list", "1")] + self.JOB_ITEMS
        resp = self.session.get(HITACHI_API_BASE, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        raw_jobs = []
        self._extract_jobs_recursive(data, raw_jobs, seen_ids=set())

        # job ID 기준 중복 제거
        seen = set()
        jobs = []
        for j in raw_jobs:
            jid = str(j.get("id", ""))
            if jid and jid not in seen:
                seen.add(jid)
                jobs.append(j)

        if limit:
            jobs = jobs[:limit]
        return jobs

    def _extract_jobs_recursive(self, obj, result: list, seen_ids: set, category: str = ""):
        """JSON 트리에서 job 항목 재귀적으로 추출 (중복 제거)"""
        if not isinstance(obj, dict):
            return
        for key, value in obj.items():
            if key.startswith("job_category") and isinstance(value, dict):
                cat_name = value.get("name", category)
                self._extract_jobs_recursive(value, result, seen_ids, cat_name)
            elif key == "job" and isinstance(value, dict):
                for _, job_data in value.items():
                    if isinstance(job_data, dict) and "name" in job_data:
                        job_id = str(job_data.get("id", ""))
                        if job_id and job_id in seen_ids:
                            continue  # 중복 스킵
                        seen_ids.add(job_id)
                        job_data["_category"] = category
                        result.append(job_data)
            elif isinstance(value, dict):
                self._extract_jobs_recursive(value, result, seen_ids, category)

    # ──────────────────────────────────────────
    # 공고 상세 수집
    # ──────────────────────────────────────────

    def fetch_job_detail(self, job_id: str) -> Optional[dict]:
        """
        개별 상세 API 호출 불필요 — fetch_job_list에서 job_items[]로 이미 수집
        BaseCrawler 인터페이스 충족을 위해 None 반환
        """
        return None

    def _find_job_detail(self, data: dict, job_id: str) -> Optional[dict]:
        """상세 API 응답에서 특정 job_id의 데이터 추출"""
        if not isinstance(data, dict):
            return None
        for key, value in data.items():
            if isinstance(value, dict):
                # job_id가 정확히 일치하는 항목 찾기
                if str(value.get("id", "")) == str(job_id) and "name" in value:
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
        job_id   = str(raw.get("id", ""))
        title    = self._clean_text(raw.get("name", ""))
        category = raw.get("_category", "")
        location_text = raw.get("location", "") or ""

        if not title:
            return None

        # ── 분류 ──────────────────────────────────────
        classify_text = f"{title} {category}"
        position   = self.classify_position(classify_text)
        locations  = self.classify_locations(location_text or title)
        experience = self.classify_experience(title)

        # ── description 파싱 ──────────────────────────
        desc_raw  = raw.get("description", "") or ""
        req_raw   = raw.get("requirement", "") or ""

        desc      = self._clean_html(desc_raw)
        req       = self._clean_html(req_raw)

        # overview: description이 충분하면 사용, 아니면 title+category로 보충
        if len(desc) >= 50:
            overview = desc
        else:
            overview = f"【{category}】\n\n{title}\n\n{desc}".strip()

        if req:
            overview += f"\n\n【応募資格】\n{req}"

        # ── tasks 파싱 ────────────────────────────────
        # description에서 업무 항목 추출 (・▶ 등 불릿 기준)
        tasks = []
        for line in desc.split("\n"):
            line = line.strip().lstrip("・•●▶︎▼■□◆◇→▷").strip()
            if line and len(line) > 5:
                tasks.append(line)
        # tasks가 너무 많으면 앞 10개만
        tasks = tasks[:10] if tasks else [title]

        # ── 근무 형태 ─────────────────────────────────
        work_type = self.detect_work_type(desc)

        # ── 기술 스택 ─────────────────────────────────
        tech_stack = self.extract_tech_stack(f"{title} {desc} {req}")

        return NaruJob(
            company_slug=COMPANY_SLUG,
            title=title,
            position=position,
            locations=locations,
            experience_level=experience,
            overview=overview,
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
        """HTML → 일반 텍스트 변환 (ruby 태그 등 불필요한 태그 제거)"""
        if not html_text:
            return ""
        soup = BeautifulSoup(html_text, "html.parser")
        # <ruby>, <rt>, <rp> 태그 제거 (후리가나 — 기술스택 오탐 방지)
        for tag in soup.find_all(["ruby", "rt", "rp"]):
            tag.decompose()
        # <br>, <p>, <li> → 개행
        for tag in soup.find_all(["br", "p", "li", "div"]):
            tag.insert_after("\n")
        text = soup.get_text()
        # 연속 개행 정리
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        return text
