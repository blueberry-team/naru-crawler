# naru-crawler

Claude Desktop을 활용하여 일정 시간 단위로 나루(naru-recruit.com) 프로젝트의 채용 데이터를 추가·검토하기 위한 크롤러.

---

## 스킬 구성

| 스킬 | 설명 |
|------|------|
| [company-crawling](skills/company-crawling/) | 기업 공식 사이트에서 회사 메타데이터를 수집하여 DRAFT로 적재 |
| [job-crawling](skills/job-crawling/) | 기업 채용 페이지에서 개별 공고를 수집하여 DRAFT로 적재 |
| [draft-review-publish](skills/draft-review-publish/) | DRAFT 공고를 검증·수정한 후 PUBLISHED로 전환 |
| [published-deadline-cleanup](skills/published-deadline-cleanup/) | PUBLISHED 공고 중 마감된 것을 CLOSED로 정리 |

---

## 작업 요청 → 스킬 매핑

| 요청 예시 | 사용할 스킬 |
|----------|------------|
| "○○ 회사 등록해줘", "회사 정보 크롤링" | `company-crawling` |
| "○○ 공고 크롤링해줘", "채용 공고 추가해줘" | `job-crawling` |
| "드래프트 검토해줘", "공고 퍼블리쉬해줘" | `draft-review-publish` |
| "마감 공고 정리해줘", "만료된 공고 처리해줘" | `published-deadline-cleanup` |

---

## 문서

| 문서 | 내용 |
|------|------|
| [WORKFLOW.md](WORKFLOW.md) | 적재 워크플로우 및 절대 규칙 |
| [REVIEW_GUIDE.md](REVIEW_GUIDE.md) | 공고 품질 검증 기준 |
| [MISTAKES.md](MISTAKES.md) | 과거 실수 기록 및 재발 방지 |
