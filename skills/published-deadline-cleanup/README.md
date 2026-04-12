---
name: published-deadline-cleanup
description: 나루 백엔드의 PUBLISHED 채용 공고를 마감일 기준으로 정기 점검하여, 마감일이 지났거나 원본이 종료된 공고를 CLOSED(또는 unpublish) 상태로 정리한다.
---

# published-deadline-cleanup — 퍼블리쉬 공고 마감 정리 스킬

## 무엇을 하는가

나루 사용자에게 노출 중인 PUBLISHED 공고를 주기적으로 점검:

1. `deadline` 필드가 오늘 기준 지난 공고 식별
2. 원본 채용 페이지가 아직 살아있고 채용 중인지 재검증
3. 마감되었거나 원본이 사라진 공고는 **CLOSED 상태로 전환** (또는 unpublish)
4. 살아있는 공고의 deadline이 갱신된 경우 PUT으로 업데이트
5. 결과 보고

이 스킬은 신뢰성 유지의 핵심으로, 사용자에게 dead-link / stale 공고가 노출되지 않도록 한다.

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

이 스킬은 사용자 노출 공고를 비공개로 전환하는 작업이라, **잘못 실행되면 노출 손실**이 발생한다. 운영 전 dry-run으로 검증하기를 권장.

### 4. 첫 실행 점검
```bash
curl -s "$NARU_API_BASE/api/jobs" | python3 -c "
import json, sys
items = json.load(sys.stdin).get('items', [])
print(f'PUBLISHED 총 {len(items)}건')"
```

---

## 사용 방법

Claude Desktop에서 다음과 같이 호출한다:

```
/published-deadline-cleanup
/published-deadline-cleanup dry-run
/published-deadline-cleanup company=hitachi
/published-deadline-cleanup days-overdue=7
```

또는 자연어:

> "퍼블리쉬된 공고 중에 마감일 지난 것들 정리해줘"

### 워크플로우
1. **PUBLISHED 목록 조회** — `GET /api/jobs?status=PUBLISHED&limit=...`
2. **마감일 필터** — `deadline < today` 또는 `deadline IS NULL`인 공고 추출
3. **재검증** — 각 `jobSourceUrl` GET 요청
   - **HTTP 404 / 410** → 원본 삭제 → **CLOSED 전환**
   - **본문에 `募集終了`/`受付終了`/`closed` 등 키워드 포함** → CLOSED 전환
   - **여전히 active** → deadline 갱신 시도 (페이지에서 새 마감일 추출)
4. **상태 전환**
   - 옵션 A: `PUT /api/dev/jobs/{id}` `{"publishStatus": "CLOSED"}`
   - 옵션 B: `PUT /api/dev/jobs/{id}/unpublish` (DRAFT 로 되돌림)
   - 백엔드에 CLOSED enum이 없다면 옵션 B 사용
5. **deadline 갱신** — 살아있는 공고는 `PUT /api/dev/jobs/{id}` `{"deadline": "YYYY-MM-DD"}`
6. **로그 기록** — 회차별 결과 누적 기록
7. **사용자 보고** — 회차 결과 (정리·갱신·보류 건수) Discord/콘솔로 전송

### dry-run 모드
실제 PUT 호출 없이 분류만 수행하고 보고만 한다. 운영 전 반드시 dry-run으로 영향 범위 확인.

---

## 출력 형식

```
🧹 #N회차 정리 (PUBLISHED 점검)
- 점검 대상 (deadline 지남): 23건
- ✅ 여전히 active (deadline 갱신): 15건
- 🛑 CLOSED 전환: 7건
- ⚠️ 보류 (모호): 1건

🛑 CLOSED 전환 jobIds: [301, 305, 312, 318, 322, 327, 333]
✅ deadline 갱신: ...
```

---

## 주의 사항 (Do / Don't)

- ✅ **dry-run 우선**. 처음 운영하는 사람은 반드시 dry-run으로 영향 확인 후 실제 실행.
- ✅ 일시적 네트워크 오류와 진짜 404 구분 — 1회 실패한 URL은 5분 후 재시도하여 확신 후 처리.
- ✅ deadline이 NULL인 공고도 정기 재검증 대상 (원본이 영구적이라는 전제는 위험).
- ✅ 로그에 jobId·이전 상태·새 상태·근거를 모두 기록 (감사 추적용).
- ❌ DELETE 절대 금지. 항상 `unpublish` 또는 `publishStatus` 변경.
- ❌ 한 번에 100건 이상 일괄 처리 시, 사용자에게 사전 승인을 받을 것 (대량 실수 시 복구 비용 큼).
- ❌ Discord·로그에 토큰 노출 금지.

---

