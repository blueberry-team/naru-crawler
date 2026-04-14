---
name: published-deadline-cleanup
description: 나루 백엔드의 PUBLISHED 채용 공고를 마감일·원본 상태·데이터 품질 기준으로 정기 점검하여, 마감·종료·불량 공고를 정리하고 살아있는 공고의 정보를 최신화한다.
---

# published-deadline-cleanup — 퍼블리쉬 공고 마감·품질 정리 스킬

## 무엇을 하는가

나루 사용자에게 노출 중인 PUBLISHED 공고를 주기적으로 점검:

1. `deadline` 필드가 오늘 기준 지난 공고 식별
2. 원본 채용 페이지가 아직 살아있고 채용 중인지 재검증
3. 마감되었거나 원본이 사라진 공고는 **unpublish** 처리
4. 살아있는 공고의 deadline·salary·locations 등이 변경된 경우 PUT으로 업데이트
5. 25개 평가 기준 중 핵심 항목 빠른 재검증 (간이 Deep Review)
6. 결과를 로그에 기록하고 Discord로 보고

이 스킬은 **서비스 신뢰성 유지의 핵심**으로, 사용자에게 dead-link / stale / 부정확한 공고가 노출되지 않도록 한다.

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

이 스킬은 사용자 노출 공고를 비공개로 전환하는 작업이라, **잘못 실행되면 노출 손실**이 발생한다.

### 4. 첫 실행 점검
```bash
curl -s "$NARU_API_BASE/api/jobs" | python3 -c "
import json, sys
items = json.load(sys.stdin).get('items', [])
print(f'PUBLISHED 총 {len(items)}건')"
```

---

## 사용 방법

```text
/published-deadline-cleanup
/published-deadline-cleanup dry-run
/published-deadline-cleanup company=hitachi
/published-deadline-cleanup days-overdue=7
/published-deadline-cleanup --full-check
```

또는 자연어:

> "퍼블리쉬된 공고 중에 마감일 지난 것들 정리해줘"
> "PUBLISHED 전체 URL 살아있는지 점검해줘"

---

## 점검 항목 (10개 핵심 체크)

### Tier 1: 즉시 조치 (자동)

| # | 점검 항목 | 판정 기준 | 액션 |
|---|----------|----------|------|
| 1 | **deadline 경과** | `deadline < today` | `PUT {"isDeadlinePassed": true}` (PUBLISHED 유지, 마감 표시) |
| 2 | **source_url 404/410** | HTTP 404/410 응답 | `PUT /unpublish` (DRAFT로 되돌림) |
| 3 | **채용 종료 키워드** | `募集終了`/`受付終了`/`closed` 발견 | `PUT {"isDeadlinePassed": true}` |
| 4 | **응모 버튼 비활성** | 원본에서 応募する 버튼 없거나 disabled | `PUT {"isDeadlinePassed": true}` |

### Tier 2: 업데이트 (자동)

| # | 점검 항목 | 판정 기준 | 액션 |
|---|----------|----------|------|
| 5 | **deadline 변경** | 원본 마감일이 DB와 다름 | PUT deadline 갱신 |
| 6 | **연봉 변경** | 원본 연봉이 DB와 다름 | PUT salaryMin/Max 갱신 |
| 7 | **근무지 변경** | 원본 근무지가 DB와 다름 | PUT locations 갱신 |
| 8 | **근무형태 변경** | 원본 리모트/하이브리드 변경 | PUT workType 갱신 |

### Tier 3: 플래그 (보고만)

| # | 점검 항목 | 판정 기준 | 액션 |
|---|----------|----------|------|
| 9 | **WAF/봇 차단** | 200이나 빈 콘텐츠/challenge 페이지 | ⚠️ 플래그, 사람 확인 필요 |
| 10 | **공고 내용 대폭 변경** | 원본 제목/직무가 DB와 다름 | ⚠️ 플래그, 재크롤 필요 |

---

## 워크플로우

```text
[1] PUBLISHED 목록 조회
     │
     ├── GET /api/jobs (전체) 또는
     └── 특정 회사/기간 필터
     ↓
[2] Tier 1 점검 (즉시 조치)
     │
     ├── deadline 경과 체크 (DB만으로 판별 가능)
     │    └── PUT {"isDeadlinePassed": true} (PUBLISHED 유지, 마감 표시)
     ├── source_url WebFetch
     │    ├── 404/410 → unpublish (DRAFT로 되돌림)
     │    ├── 200 + 종료 키워드 → isDeadlinePassed=true
     │    └── 200 + 정상 → Tier 2로
     ├── 404 후보 목록 → 전체 점검 끝난 후 재시도 (대기 없이 자연 간격)
     │    ├── 여전히 404 → unpublish 확정
     │    └── 이번엔 200 → 일시적 오류, 정상 유지
     └── 마감/unpublish 대상 일괄 처리
     ↓
[3] Tier 2 점검 (업데이트)
     │
     ├── 원본에서 deadline/salary/locations/workType 추출
     ├── DB 값과 비교
     ├── 차이 있으면 PUT /api/dev/jobs/{id} (변경 필드만)
     └── 204 응답 확인
     ↓
[4] Tier 3 점검 (플래그)
     │
     ├── WAF/봇 차단 감지
     ├── 제목/직무 변경 감지
     └── 플래그 목록 생성
     ↓
[5] dry-run 분기
     │
     ├── dry-run=true → 보고만 (PUT 미실행)
     └── dry-run=false → 실제 PUT 실행
     ↓
[6] 로그 기록
     │
     └── history/cleanup-log.md에 회차별 결과 append
          ├── unpublish 건: jobId, 사유, 이전 상태
          ├── 갱신 건: jobId, 변경 필드, 이전값→신규값
          └── 플래그 건: jobId, 사유
     ↓
[7] Discord 보고
```

---

## 출력 형식

```text
🧹 #N회차 PUBLISHED 정리

📊 점검 대상: 45건
━━━━━━━━━━━━━━━━━━━━━

🛑 마감 처리 (Tier 1): 3건
  - #305 SCSK 인프라 엔지니어 — 募集終了 → isDeadlinePassed=true
  - #312 Capcom VFX 엔지니어 — deadline 경과 → isDeadlinePassed=true
  - #301 SEGA 시스템 프로그래머 — 404 (2회 확인) → unpublish (DRAFT)

🔄 갱신 (Tier 2): 5건
  - #401 Hitachi AI 엔지니어 — deadline 2026-06-30→2026-09-30
  - #402 SMBC PM — salaryMin 5000000→5500000
  - #403 DeNA 엔지니어 — locations +YOKOHAMA

⚠️ 플래그 (Tier 3): 2건
  - #501 IBM 컨설턴트 — WAF 차단, 사람 확인 필요
  - #502 NTT Data 엔지니어 — 제목 변경 감지

✅ 정상 유지: 35건
```

---

## 로그 기록 형식

### history/cleanup-log.md

```markdown
## #1회차 (2026-04-14)

| jobId | 회사 | 구분 | 사유 | 액션 | 결과 |
|-------|------|------|------|------|------|
| 301 | SEGA | unpublish | 404 (2회 확인) | PUT /unpublish → DRAFT | 204 ✅ |
| 305 | SCSK | 마감 | 募集終了 | PUT isDeadlinePassed=true | 204 ✅ |
| 312 | Capcom | 마감 | deadline 경과 | PUT isDeadlinePassed=true | 204 ✅ |
| 401 | Hitachi | 갱신 | deadline 변경 | PUT deadline | 204 ✅ |
| 501 | IBM | 플래그 | WAF | — | 사람 확인 대기 |

합계: 마감 2 / unpublish 1 / 갱신 1 / 플래그 1 / 정상 40
```

---

## 실행 빈도 권장

| 모드 | 빈도 | 설명 |
|------|------|------|
| deadline 체크 | 매일 1회 | DB deadline 필드만 확인 (API 호출 최소) |
| URL 재검증 | 주 1회 | 전체 PUBLISHED의 source_url WebFetch |
| 전체 점검 | 월 1회 | Tier 1~3 전체 + 연봉/위치 변경 체크 |

### cron 예시
```text
# 매일 오전 9시 deadline 체크
0 9 * * * /published-deadline-cleanup --deadline-only

# 매주 월요일 전체 URL 재검증
0 10 * * 1 /published-deadline-cleanup --full-check dry-run

# 매월 1일 전체 점검 (dry-run 먼저)
0 10 1 * * /published-deadline-cleanup --full-check
```

---

## 주의 사항 (Do / Don't)

- ✅ **dry-run 우선**. 처음 운영하는 사람은 반드시 dry-run으로 영향 확인 후 실제 실행.
- ✅ 일시적 네트워크 오류와 진짜 404 구분 — 1회 실패한 URL은 **404 후보 목록**에 넣고, 전체 점검 끝난 후 재시도 (대기 없이 자연 간격 확보).
- ✅ deadline이 NULL인 공고도 정기 재검증 대상 (원본이 영구적이라는 전제는 위험).
- ✅ 로그에 jobId·이전 상태·새 상태·근거를 **모두 기록** (감사 추적용).
- ✅ unpublish 전에 **현재 PUBLISHED 총 건수 확인** — 대량 unpublish로 서비스 공고가 급감하면 안 됨.
- ✅ 갱신 시 **변경 전 값을 로그에 기록** 후 PUT.
- ❌ DELETE 절대 금지. 마감은 `isDeadlinePassed=true`, 원본 삭제는 `unpublish` 사용.
- ❌ 한 번에 **20건 이상 상태 변경 시 사용자 승인** 필요 (대량 실수 방지).
- ❌ WAF 차단 건을 자동 unpublish 하지 말 것 — 사람 확인 필요.
- ❌ Discord·로그에 토큰 노출 금지.

---

## 관련 문서
- [`docs/REVIEW_GUIDE.md`](../../docs/REVIEW_GUIDE.md) — 25개 평가 기준
- [`skills/deep-review-fix/`](../deep-review-fix/) — Deep Review 후 수정 스킬
- [`history/`](../../history/) — Deep Review 결과 + cleanup 로그
