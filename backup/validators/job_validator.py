"""
나루 공고 품질 검증기
적재 전 모든 공고는 여기서 검증을 통과해야 함
"""
from typing import Tuple, List
from models.job import NaruJob
from config import QUALITY_MIN_TITLE_LEN, QUALITY_MIN_OVERVIEW_LEN, QUALITY_MIN_TASKS

# 유효한 enum 값 목록
VALID_POSITIONS = {
    # 신졸
    "GRADUATE_GENERAL", "GRADUATE_ENGINEER", "GRADUATE_TECHNICAL", "GRADUATE_DESIGN",
    "GRADUATE_SPECIALIST", "GRADUATE_OTHER",
    # IT/개발
    "BACKEND", "FRONTEND", "FULLSTACK", "ANDROID", "IOS", "CROSS_PLATFORM",
    "DEVOPS", "CLOUD", "INFRA", "SECURITY", "QA_TEST", "DBA", "IT_DEV_OTHER",
    # AI/데이터
    "DATA_ANALYST", "DATA_ENGINEER", "ML_ENGINEER", "AI_RESEARCH", "MLOPS",
    "BI_ANALYTICS", "DATA_SCIENTIST", "NLP", "COMPUTER_VISION", "DATA_GOVERNANCE", "AI_DATA_OTHER",
    # 게임
    "GAME_CLIENT", "GAME_SERVER", "GAME_ENGINE", "GAME_GRAPHICS", "GAME_PLANNER",
    "GAME_QA", "GAME_OPERATION", "GAME_SECURITY", "GAME_OTHER",
    # 디자인
    "UX_UI", "GRAPHIC", "BRAND", "PRODUCT_DESIGN", "ILLUSTRATION", "MOTION",
    "EDITORIAL", "DESIGN_SYSTEM", "DESIGN_OTHER",
    # 기획/전략
    "PM_PO", "SERVICE_PLANNING", "BUSINESS_STRATEGY", "CORPORATE_STRATEGY", "NEW_BUSINESS",
    "OPERATION_PLANNING", "POLICY_PLANNING", "PLANNING_STRATEGY_OTHER",
    # 마케팅
    "PERFORMANCE_MARKETING", "BRAND_MARKETING", "CONTENT_MARKETING", "SEO",
    "CRM_MARKETING", "SOCIAL_MARKETING", "AD_PLANNING", "MARKETING_AD_OTHER",
    # 영업
    "KEY_ACCOUNT", "INSIDE_SALES", "SALES_ENGINEER", "PARTNER_SALES", "SALES_OTHER",
    # 물류
    "EXPORT_IMPORT", "LOGISTICS_OPERATION", "FORWARDING", "WAREHOUSE", "SCM",
    "CUSTOMS", "TRADE_LOGISTICS_OTHER",
    # 법무/HR/재무
    "LEGAL_COUNSEL", "COMPLIANCE", "CONTRACT_REVIEW", "IP_PATENT", "PRIVACY", "LEGAL_COMPLIANCE_OTHER",
    "RECRUITING", "HRD", "HRBP", "PAYROLL", "GENERAL_AFFAIRS", "LABOR_RELATIONS", "HR_GENERAL_AFFAIRS_OTHER",
    "ACCOUNTING", "TAX", "FINANCE", "MANAGEMENT_ACCOUNTING", "IR", "FPNA", "ACCOUNTING_TAX_FINANCE_OTHER",
    # 엔지니어링
    "MECHANICAL", "ELECTRICAL_ELECTRONICS", "EMBEDDED", "ROBOTICS", "MATERIALS",
    "QA_QC", "ENGINEERING_RD_OTHER",
    # 기타
    "MANUFACTURING", "MAINTENANCE", "CUSTOMER_SUPPORT_TM_OTHER", "SERVICE_OTHER",
}

VALID_LOCATIONS = {
    # 일본 도도부현 전체
    "NATIONWIDE", "HOKKAIDO", "AOMORI", "IWATE", "MIYAGI", "AKITA", "YAMAGATA", "FUKUSHIMA",
    "IBARAKI", "TOCHIGI", "GUNMA", "SAITAMA", "CHIBA", "TOKYO", "KANAGAWA",
    "NIIGATA", "TOYAMA", "ISHIKAWA", "FUKUI", "YAMANASHI", "NAGANO",
    "GIFU", "SHIZUOKA", "AICHI", "MIE", "SHIGA", "KYOTO", "OSAKA", "HYOGO", "NARA",
    "WAKAYAMA", "TOTTORI", "SHIMANE", "OKAYAMA", "HIROSHIMA", "YAMAGUCHI",
    "TOKUSHIMA", "KAGAWA", "EHIME", "KOCHI",
    "FUKUOKA", "SAGA", "NAGASAKI", "KUMAMOTO", "OITA", "MIYAZAKI", "KAGOSHIMA", "OKINAWA",
    "OVERSEAS", "REMOTE",
}

VALID_EXPERIENCE_LEVELS = {
    "NEW_GRAD", "MID_CAREER"
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
