"""
나루 Job 데이터 모델
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class NaruJob:
    """나루 DB에 적재할 공고 데이터"""
    company_slug: str
    title: str
    position: str                        # enum: BACKEND, FRONTEND, ...
    locations: List[str]                 # enum list: TOKYO, OSAKA, ...
    experience_level: str                # enum: JUNIOR, MID, SENIOR, ...
    overview: str                        # 직무 개요 (필수, 50자 이상)
    tasks: List[str]                     # 담당 업무 목록

    # 선택 필드
    join_date: Optional[str] = None      # 입사 시기 (예: 2026年4月)
    work_type: str = "ONSITE"           # ONSITE | HYBRID | REMOTE
    deadline: Optional[str] = None      # YYYY-MM-DD
    tech_stack: List[str] = field(default_factory=list)
    selection_process: Optional[str] = None
    salary: Optional[str] = None
    status: str = "DRAFT"

    # 크롤러 메타데이터 (적재 시 사용 안 함)
    source_id: Optional[str] = None     # 원본 공고 ID
    source_url: Optional[str] = None    # 원본 URL

    def to_api_payload(self) -> dict:
        """나루 API POST body로 변환"""
        payload = {
            "companySlug": self.company_slug,
            "title": self.title,
            "position": self.position,
            "locations": self.locations,
            "experienceLevel": self.experience_level,
            "overview": self.overview,
            "tasks": self.tasks,
            "workType": self.work_type,
            "status": self.status,
        }
        if self.join_date:
            payload["joinDate"] = self.join_date
        if self.deadline:
            payload["deadline"] = self.deadline
        if self.tech_stack:
            payload["techStack"] = self.tech_stack
        if self.selection_process:
            payload["selectionProcess"] = self.selection_process
        if self.salary:
            payload["salary"] = self.salary
        return payload
