"""
나루 API 클라이언트
DRAFT 공고 적재, 조회, 삭제 등
"""
from typing import List, Optional
import requests

from config import NARU_API_BASE, NARU_ADMIN_TOKEN
from models.job import NaruJob

HEADERS = {
    "Content-Type": "application/json",
    "X-Admin-Token": NARU_ADMIN_TOKEN,
}


class NaruClient:
    """나루 API 클라이언트"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def create_job(self, job: NaruJob) -> dict:
        """
        공고 생성 (DRAFT 상태로)
        성공: {"jobId": ..., "status": "DRAFT"}
        실패: requests.HTTPError
        """
        payload = job.to_api_payload()
        resp = self.session.post(f"{NARU_API_BASE}/api/dev/jobs", json=payload)
        resp.raise_for_status()
        return resp.json() if resp.text else {"status": "created"}

    def get_drafts(self) -> List[dict]:
        """현재 DRAFT 공고 목록"""
        resp = self.session.get(f"{NARU_API_BASE}/api/dev/jobs/drafts")
        resp.raise_for_status()
        return resp.json()

    def delete_job(self, job_id: int) -> bool:
        """공고 삭제 (테스트용)"""
        resp = self.session.delete(f"{NARU_API_BASE}/api/dev/jobs/{job_id}")
        return resp.status_code == 204

    def get_company_by_slug(self, slug: str) -> Optional[dict]:
        """slug로 기업 조회"""
        try:
            resp = self.session.get(f"{NARU_API_BASE}/api/dev/companies/{slug}")
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return None
