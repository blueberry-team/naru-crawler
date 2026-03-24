"""
나루 공고 품질 검증기
적재 전 모든 공고는 여기서 검증을 통과해야 함
"""
from typing import Tuple, List
from models.job import NaruJob
from config import QUALITY_MIN_TITLE_LEN, QUALITY_MIN_OVERVIEW_LEN, QUALITY_MIN_TASKS

# 유효한 enum 값 목록
VALID_POSITIONS = {
    "BACKEND", "FRONTEND", "FULLSTACK", "MOBILE", "DEVOPS",
    "DATA", "AI_ML", "SECURITY", "EMBEDDED", "QA",
    "PRODUCT", "DESIGN", "BUSINESS", "HR", "FINANCE", "LEGAL", "OTHER"
}

VALID_LOCATIONS = {
    "TOKYO", "OSAKA", "NAGOYA", "FUKUOKA", "SAPPORO", "SENDAI",
    "HIROSHIMA", "KYOTO", "YOKOHAMA", "KANAGAWA", "REMOTE",
    "OTHER_JAPAN", "OVERSEAS"
}

VALID_EXPERIENCE_LEVELS = {
    "NEW_GRAD", "JUNIOR", "MID", "SENIOR", "LEAD", "MANAGER", "EXECUTIVE"
}

VALID_WORK_TYPES = {"ONSITE", "HYBRID", "REMOTE"}


class ValidationError(Exception):
    """검증 실패 에러"""
    def __init__(self, reasons: List[str]):
        self.reasons = reasons
        super().__init__(f"검증 실패: {', '.join(reasons)}")


def validate(job: NaruJob) -> Tuple[bool, List[str]]:
    """
    공고 품질 검증
    Returns: (통과 여부, 실패 사유 목록)
    """
    errors = []

    # 제목 검증
    if not job.title or len(job.title.strip()) < QUALITY_MIN_TITLE_LEN:
        errors.append(f"title이 너무 짧음 (최소 {QUALITY_MIN_TITLE_LEN}자, 현재: {len(job.title or '')}자)")

    # 개요 검증
    if not job.overview or len(job.overview.strip()) < QUALITY_MIN_OVERVIEW_LEN:
        errors.append(f"overview가 너무 짧음 (최소 {QUALITY_MIN_OVERVIEW_LEN}자, 현재: {len(job.overview or '')}자)")

    # 담당 업무 검증
    if not job.tasks or len(job.tasks) < QUALITY_MIN_TASKS:
        errors.append(f"tasks가 없음 (최소 {QUALITY_MIN_TASKS}개 필요)")

    # position enum 검증
    if job.position not in VALID_POSITIONS:
        errors.append(f"유효하지 않은 position: '{job.position}'")

    # location 검증
    if not job.locations:
        errors.append("locations가 비어있음")
    else:
        invalid_locs = [loc for loc in job.locations if loc not in VALID_LOCATIONS]
        if invalid_locs:
            errors.append(f"유효하지 않은 location: {invalid_locs}")

    # experienceLevel 검증
    if job.experience_level not in VALID_EXPERIENCE_LEVELS:
        errors.append(f"유효하지 않은 experienceLevel: '{job.experience_level}'")

    # workType 검증
    if job.work_type not in VALID_WORK_TYPES:
        errors.append(f"유효하지 않은 workType: '{job.work_type}'")

    # companySlug 검증
    if not job.company_slug or len(job.company_slug.strip()) == 0:
        errors.append("companySlug가 비어있음")

    return len(errors) == 0, errors
