"""
나루 크롤러 설정값
"""

# 나루 API
NARU_API_BASE = "https://api.naru-recruit.com"
NARU_ADMIN_TOKEN = "jungwoo_naru_server_password_0129"

# 크롤링 딜레이 (초) - 서버 부하 방지
CRAWL_DELAY = 1.0

# 히타치 API
HITACHI_API_BASE = "https://jscudp.jcareers.com/hitachi/u/jobs.phtml"
HITACHI_REFERER = "https://hitachi.jposting.net/"

# 품질 기준
QUALITY_MIN_TITLE_LEN = 5
QUALITY_MIN_OVERVIEW_LEN = 50
QUALITY_MIN_TASKS = 1
