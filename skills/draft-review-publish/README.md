---
name: draft-review-publish
description: 나루 백엔드의 DRAFT 상태 채용 공고를 샘플링·검증·수정한 후 PUBLISHED 상태로 전환한다. URL 유효성·채용 현행성·데이터 품질·중복 여부를 점검하고 PUT API로 결함을 부분 수정한 뒤 publish 한다.
---

# draft-review-publish — 드래프트 리뷰·퍼블리쉬 스킬

## 무엇을 하는가

크롤러가 적재한 DRAFT 공고를 사람·LLM이 함께 검토하여:

1. URL이 살아있는지 확인
2. 채용이 현재 진행 중인지 확인 (마감/종료 키워드 체크)
3. 데이터 품질 (필드 완성도, 분류 정확도, 텍스트 품질) 점검
4. 중복 공고 여부 확인
5. 결함이 있으면 PUT API로 부분 수정
6. 통과한 공고만 PUBLISHED 로 전환

이 스킬은 [`job-crawling`](../job-crawling/) 스킬이 적재한 결과를 다루며, 결과적으로 **나루 사용자에게 노출되는 공고를 결정**한다.

---

## 전제 조건 (Setup)

### 1. 저장소 클론
```bash
git clone git@github.com:blueberry-team/naru-crawler.git
cd naru-crawler
```

### 2. 환경 변수
```bash
export NARU_ADMIN_TOKEN="<발급받은_토큰>"
export NARU_API_BASE="https://api.naru-recruit.com"
```

### 3. Claude Desktop 권한
사용 도구: `Bash`, `WebFetch`, `Read`, `Edit`, `Write`. 권한 모드는 `acceptEdits` 권장.

수정 작업이 자동으로 PUT API를 호출하므로, 관리자급 토큰임을 인지한 사람이 운영해야 한다.

### 4. 첫 실행 점검
```bash
curl -s "$NARU_API_BASE/api/dev/jobs/drafts" \
  -H "X-Admin-Token: $NARU_ADMIN_TOKEN" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))"
```
DRAFT 개수가 출력되면 셋업 완료.

---

## 사용 방법

Claude Desktop에서 다음과 같이 호출한다:

```
/draft-review-publish 개수=5
/draft-review-publish jobIds=1153,1154,1155
/draft-review-publish company=hitachi 개수=10
```

또는 자연어:

> "DRAFT 공고 5개 샘플링해서 리뷰하고 문제 없으면 발행해줘"

### 워크플로우 (회차당)
1. **샘플링** — `GET /api/dev/jobs/drafts`로 DRAFT 목록 조회 → 회사·직군 다양성 고려해 N건 선택
2. **URL 검증** — 각 `jobSourceUrl`에 GET 요청
   - 200 → ✅ 통과
   - 404/410 → ❌ 원본 삭제 (publish 보류, 사용자에게 알림)
   - WAF 차단·카테고리 페이지 → ⚠️ DB 데이터 양호 시 통과
3. **채용 현행성 체크** — fetch한 본문에서 `募集終了`, `終了`, `締め切り`, `closed` 등 키워드 검색
4. **데이터 품질 검사** — `REVIEW_GUIDE.md` 기준으로 필드 완성도·분류 정확도·텍스트 품질 평가
5. **중복 검사** — 동일 source_url 또는 매우 유사한 title이 이미 PUBLISHED에 있는지 확인
6. **결함 수정** — 발견된 문제는 사용자 승인 없이 즉시 PUT으로 부분 수정 (예: position, locations)
   - **PUT만 사용. DELETE→재생성 금지.** PUT은 부분 업데이트, 변경 필드만 전송, 204 반환
7. **PUBLISH** — 모든 검증 통과 시 `PUT /api/dev/jobs/{id}/publish`
8. **로그 기록** — 회차별 표 형태로 결과 누적
9. **사용자 보고** — Discord 또는 콘솔로 회차 결과 요약 + 어드민 확인 링크 전송

### API 참고
| 작업 | 메서드 | 엔드포인트 |
|---|---|---|
| DRAFT 목록 | GET | `/api/dev/jobs/drafts` |
| 단건 조회 | GET | `/api/dev/jobs/{id}` |
| 부분 수정 | PUT | `/api/dev/jobs/{id}` (변경 필드만, 204 반환) |
| DRAFT → PUBLISH | PUT | `/api/dev/jobs/{id}/publish` |
| PUBLISH → DRAFT | PUT | `/api/dev/jobs/{id}/unpublish` |

---

## 출력 형식

```
📋 #N회차 리뷰 (M/total)

| jobId | 회사 | 제목 | 결과 | 비고 |
|-------|------|------|------|------|
| 1153  | GMO  | PHP 엔지니어 | ✅ →PUB | |
| 1154  | PayPay | DB 스페셜리스트 | 🔧 +OSAKA | |
| 1155  | SEGA | 시스템 프로그래머 | ❌ 404 | 보류 |

🔧 1154: https://www.naru-recruit.com/admin/jobs/1154?token=...
누적: ✅ N / 🔧 M / ❌ K
```

---

## history 기록 규칙

모든 리뷰·수정·발행 액션은 `history/` 폴더에 기록한다.

### 기록 대상
- Deep Review 25개 평가 결과 → `history/history001-100.md` (jobId 범위별)
- PUT 수정 내역 (수정 전후 비교) → 같은 파일의 해당 Job 섹션에 `[RE-REVIEW]` 추가
- PUBLISH 전환 기록 → 해당 Job의 **판정** 항목에 반영

### 파일 구조
```text
history/
├── history001-100.md     # jobId 1~100
├── history101-200.md     # jobId 101~200
└── ...
```

### 기록 시점
- 리뷰 완료 즉시 history md에 append
- Fix 실행 시 수정 내역 즉시 append
- PUBLISH 전환 시 판정 업데이트

---

## 주의 사항 (Do / Don't)

- ✅ **PUT 부분 업데이트만 사용**. 절대 DELETE 후 재생성하지 말 것.
- ✅ 결함은 묻지 말고 즉시 수정 후 사용자에게 보고. 단, **PUBLISH 전환은 신중**하게.
- ✅ 회차마다 결과를 `history/` md에 누적 기록. 패턴 발견 시 별도 섹션으로 분리.
- ✅ 위치/직군 enum 부재 등 **크롤러 결함**으로 분류된 케이스는 별도 패턴 누적 후 구조 개선 PR로 연결.
- ❌ 자동 PUBLISH가 위험한 공고 (404, 채용 종료 키워드 발견, 분류 모호) 는 보류.
- ❌ 토큰을 로그·커밋·Discord 메시지에 노출 금지.

---

