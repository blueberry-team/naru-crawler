# 🍇 naru-crawler

나루 채용 플랫폼(naru-recruit.com) 공고 데이터 자동 적재 시스템

## 목적

기업 채용 사이트에서 공고를 수집 → 품질 검증 → 나루 DB에 DRAFT로 적재  
관리자가 어드민에서 검토 후 PUBLISHED로 전환

---

## 📁 구조

```
naru-crawler/
├── companies/           # 기업별 크롤러
│   ├── base.py          # 공통 추상 클래스 (매핑 룰 로직 포함)
│   └── hitachi.py       # 히타치 크롤러
├── rules/               # 매핑 규칙 (코드 없이 수정 가능)
│   ├── position_rules.json    # 직무 분류 키워드
│   ├── location_rules.json    # 근무지 매핑
│   └── experience_rules.json  # 경력 레벨 매핑
├── validators/
│   └── job_validator.py # 품질 검증
├── models/
│   └── job.py           # NaruJob 데이터 모델
├── api/
│   └── naru_client.py   # 나루 API 클라이언트
├── docs/
│   ├── COMMANDS.md      # 명령 기록
│   └── MISTAKES.md      # 실수 기록
├── runner.py            # CLI 실행
├── config.py            # 설정값
└── requirements.txt
```

---

## 🚀 실행

```bash
pip install -r requirements.txt

# 미리보기 (실제 적재 안 함)
python runner.py --company hitachi --limit 10 --dry-run

# 실제 적재 (50개)
python runner.py --company hitachi --limit 50

# 전체 실행
python runner.py --company hitachi

# 현재 DRAFT 현황 확인
python runner.py --company hitachi --report-only
```

---

## 📐 매핑 규칙

### position_rules.json

제목 + 카테고리 텍스트에서 키워드를 순서대로 매칭하여 포지션 분류

```json
{
  "position": "AI_ML",
  "keywords": ["AI", "機械学習", "生成AI", "LLM", ...]
}
```

**포지션 목록**:
| Enum | 설명 |
|------|------|
| AI_ML | AI/머신러닝 |
| DATA | 데이터 엔지니어링 |
| SECURITY | 보안 |
| DEVOPS | 인프라/클라우드/DevOps |
| BACKEND | 백엔드 개발 |
| FRONTEND | 프론트엔드 |
| MOBILE | 모바일 |
| EMBEDDED | 임베디드/제어시스템 |
| QA | 품질보증 |
| PRODUCT | 프로덕트/기획 |
| DESIGN | 디자인 |
| HR | 인사 |
| FINANCE | 재무/경리 |
| LEGAL | 법무 |
| BUSINESS | 영업/컨설팅/PM |
| OTHER | 기타 |

### location_rules.json

일본어 지명 → 나루 location enum 매핑

```json
{
  "location": "TOKYO",
  "keywords": ["東京", "渋谷", "品川", ...]
}
```

매칭 지명 없으면 `default: "OTHER_JAPAN"` 적용

### experience_rules.json

직급 키워드 → 경력 레벨 매핑

```json
{
  "level": "SENIOR",
  "keywords": ["主任", "主任クラス", "シニア", ...]
}
```

| Enum | 기준 |
|------|------|
| EXECUTIVE | 部長, 本部長 |
| MANAGER | 課長, マネージャー |
| LEAD | リーダー, アーキテクト |
| SENIOR | 主任, シニア |
| JUNIOR | 担当者, 第二新卒 |
| NEW_GRAD | 新卒 |
| MID | 기본값 (해당 없음) |

---

## ✅ 품질 기준

다음 조건을 모두 통과해야 DRAFT 적재됨:

| 항목 | 기준 |
|------|------|
| title | 5자 이상 |
| overview | 50자 이상 |
| tasks | 1개 이상 |
| position | 유효한 enum |
| locations | 1개 이상 (유효한 enum) |
| experienceLevel | 유효한 enum |

실패 시 ValidationError 반환 + 사유 로그 출력

---

## 🏭 새 기업 크롤러 추가 방법

1. `companies/{company_slug}.py` 생성
2. `BaseCrawler` 상속
3. 3개 메서드 구현:
   - `fetch_job_list()` → raw 공고 목록
   - `fetch_job_detail(job_id)` → raw 상세
   - `parse_job(raw)` → NaruJob 반환
4. `runner.py`의 `CRAWLERS` dict에 등록

```python
CRAWLERS = {
    "hitachi": lambda: HitachiCrawler(),
    "sony": lambda: SonyCrawler(),    # 추가
}
```

---

## 📚 문서

- [명령 기록](docs/COMMANDS.md) - 정우의 지시 및 처리 내역
- [실수 기록](docs/MISTAKES.md) - 실수 및 교훈
