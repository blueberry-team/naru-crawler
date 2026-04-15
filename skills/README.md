# 나루 크롤러 Skills

나루 채용 플랫폼의 데이터 운영을 위한 Claude Desktop 스킬 모음.

---

## 작업 선택

### (1) 신졸 채용 정보 데이터 추가

새로운 신졸(新卒) 채용 공고를 크롤링하여 나루 DB에 DRAFT로 적재합니다.

**사용 스킬**: [`crawl-job-newgrad`](crawl-job-newgrad/)

**흐름**:
1. Playwright MCP로 대상 기업 채용 페이지 탐색
2. 신졸 공고 목록에서 개별 공고 상세 수집
3. 필드 정규화 + 일본어→한국어 번역
4. payload 검증 후 `POST /api/dev/jobs` (DRAFT)

**실행 예시**:
```text
/crawl-job-newgrad "https://www.softbank.jp/recruit/graduate/" softbank
```

---

### (2) 중도 채용 정보 데이터 추가

경력직(中途/キャリア) 채용 공고를 크롤링하여 나루 DB에 DRAFT로 적재합니다.

**사용 스킬**: [`crawl-job-mid`](crawl-job-mid/)

**흐름**:
1. Playwright MCP로 대상 기업 경력 채용 페이지 탐색
2. 경력직 공고 목록에서 개별 공고 상세 수집
3. 필드 정규화 + 일본어→한국어 번역
4. payload 검증 후 `POST /api/dev/jobs` (DRAFT)

**실행 예시**:
```text
/crawl-job-mid "https://hrmos.co/pages/simplex/jobs" simplex
```

---

### (3) 새로운 기업 정보 데이터 추가

아직 나루에 등록되지 않은 기업의 메타데이터를 수집하여 Company DB에 적재합니다.

**사용 스킬**: [`crawl-company`](crawl-company/)

**흐름**:
1. Playwright MCP로 기업 공식 사이트 / 채용 페이지 탐색
2. 회사명, 산업, 직원수, 복리후생, 경영철학 등 메타 추출
3. 로고 URL 수집, 태그 생성
4. payload 검증 후 `POST /api/dev/companies` (DRAFT)

**실행 예시**:
```text
/crawl-company "https://www.cybozu.co.jp/" cybozu
```

---

### (4) 퍼블리쉬된 공고 리뷰 및 정리하기

이미 PUBLISHED된 공고를 25개 평가 기준으로 Deep Review하고, 문제를 수정하며, 마감된 공고를 정리합니다.

**사용 스킬** (3개를 순서대로):

| 순서 | 스킬 | 역할 |
|------|------|------|
| 1 | [`deep-review`](deep-review/) | 동일한 채용공고 원본을 크롤링하여 25개 기준 Deep Review 진행 |
| 2 | [`fix-reviewed`](fix-reviewed/) | 리뷰에서 발견된 ⚠️/❌ 항목을 수정 (PUT API) + 재리뷰 |
| 3 | [`cleanup-deadline`](cleanup-deadline/) | 마감일 경과 / 원본 삭제 공고 정리 (isDeadlinePassed / unpublish) |

**흐름**:
1. **딥 리뷰**: 공고의 source URL을 WebFetch → 원본과 DB 데이터 25개 항목 대조
2. **수정**: 분류 오류(position/locations), 연봉 오차, 텍스트 품질 등 수정
3. **마감 정리**: deadline 경과 → `isDeadlinePassed=true`, 원본 404 → `unpublish`
4. 모든 결과를 `history/` 폴더에 기록

**실행 예시**:
```text
DRAFT 공고 5개 샘플링해서 딥 리뷰하고 문제 있으면 수정해줘
마감일 지난 PUBLISHED 공고 정리해줘
```

---

## 스킬 폴더 구조

각 스킬은 동일한 구조를 따릅니다:

```text
skills/{동사}-{명사}/
├── SKILL.md          # 스킬 정의 (프롬프트 + 규칙 요약)
├── rules/            # 상세 규칙 (번호별 분리)
├── examples/         # 입출력 예시 (good/bad/edge-cases)
└── references/       # 참고 자료 (API 스펙, enum, 체크리스트)
```

## 공통 원칙

- **Playwright MCP**를 기본 브라우징 도구로 사용 (crawl-* 스킬)
- `1공고 = 1 payload = 1 POST`
- `publishStatus`는 항상 `DRAFT` (크롤링 시)
- 명시되지 않은 사실은 추측하지 않음
- 회사 전체 정보와 개별 공고 정보를 구분 ([상세](../docs/REVIEW_GUIDE.md))
- 모든 작업 결과는 `history/` 폴더에 기록
