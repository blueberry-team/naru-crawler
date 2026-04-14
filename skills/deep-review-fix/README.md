---
name: deep-review-fix
description: Deep Review에서 발견된 ⚠️/❌ 항목을 자동 수정(PUT API)하고, 재리뷰하여 history md에 수정 전후 비교를 기록한다. 수정 불가 건은 사용자 판단 대기로 분류한다.
---

# deep-review-fix — 리뷰 결과 기반 자동 수정·재리뷰 스킬

## 무엇을 하는가

Deep Review(25개 평가 기준)에서 ⚠️/❌로 판정된 항목을 분석하여:

1. **자동 수정 가능한 건** → PUT API로 즉시 수정
2. **수정 후 재리뷰** → 동일 25개 기준으로 재평가
3. **수정 전후 비교** → history md에 `[RE-REVIEW]` 섹션 추가
4. **수정 불가 건** → 사용자 판단 대기(`HOLD`) 표시

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

PUT API를 호출하므로 관리자급 토큰이 필요하다.

### 4. 첫 실행 점검
```bash
# Deep Review 파일이 존재하는지 확인
ls history/history*.md
```

---

## 사용 방법

```text
/deep-review-fix history/history001-100.md
/deep-review-fix jobId=13
/deep-review-fix --all-warnings
```

또는 자연어:

> "history001-100.md에서 ⚠️ 있는 공고 찾아서 수정하고 재리뷰해줘"

---

## 수정 가능 항목 분류 (Action Matrix)

### 자동 수정 가능 (AUTO-FIX)

| 평가 항목 | 문제 유형 | 수정 액션 |
|----------|----------|----------|
| A-1 | 연봉 출처 불명확 | WebFetch로 snar.jp/hrmos 등 지원 포털 재확인 → salaryMin/Max PUT |
| A-2 | 연봉 범위 불일치 | 원본 확인 후 salaryMin/salaryMax PUT |
| D-11 | position 오분류 | 원본 직무 내용 대조 → position PUT (enum 존재 시) |
| D-12 | locations 누락/오류 | 원본 근무지 확인 → locations PUT (enum 존재 시) |
| D-13 | experienceLevel 오류 | 원본 자격 요건 확인 → experienceLevel PUT |
| D-14 | workType 오류 | 원본 근무 형태 확인 → workType PUT |
| E-16 | techStack 누락/오류 | 원본 기술 스택 확인 → techStack PUT |
| E-17 | deadline 오류 | 원본 마감일 확인 → deadline PUT |
| E-18 | joinDate 오류 | 원본 입사일 확인 → joinDate PUT |
| F-19 | HTML 잔여물 | 텍스트 정제 → overview/tasks PUT |
| G-25 | 제목 불일치 | 원본 제목 재확인 → title PUT |

### 반자동 수정 (SEMI-AUTO) — 확인 후 수정

| 평가 항목 | 문제 유형 | 수정 액션 |
|----------|----------|----------|
| B-4 | overview 원본과 불일치 | WebFetch로 원본 재수집 → overview 재작성 → PUT |
| B-5 | tasks 누락/불일치 | 원본 재수집 → tasks 재구성 → PUT |
| B-6 | targetCandidate 불일치 | 원본 재수집 → targetCandidate 재구성 → PUT |
| B-7 | selectionProcess 불일치 | 원본 재수집 → selectionProcess PUT |
| F-20 | 번역 부자연스러움 | 원본 대조 후 재번역 → PUT |
| F-21 | 보일러플레이트 과다 | overview 정제 → PUT |

### 수정 불가 (HOLD) — 사용자 판단 필요

| 평가 항목 | 문제 유형 | 사유 |
|----------|----------|------|
| A-1/A-2 | 연봉 원본에도 미기재 | 정보 자체가 없음. 사용자가 기업 평균 추정치 사용 여부 결정 |
| C-8 | 업종 특성 미반영 | overview 전면 재작성 필요 — 자동화 리스크 |
| C-9 | 기업 문화 미반영 | 추가 리서치 필요 |
| D-11 | position enum 부재 | DESIGNER, SALES_ENGINEER 등 enum 추가 필요 — 백엔드 변경 |
| D-12 | locations enum 부재 | KAWASAKI, NAGOYA, HOKKAIDO 등 enum 추가 필요 — 백엔드 변경 |
| G-22 | source_url 404 | 원본 삭제됨. 공고 유지 여부 사용자 결정 |
| G-22 | source_url WAF 차단 | 자동 검증 불가. 사람이 브라우저로 확인 필요 |

---

## 워크플로우

```text
[1] history md 스캔
     ↓
[2] ⚠️/❌ 항목 추출 → 분류 (AUTO-FIX / SEMI-AUTO / HOLD)
     ↓
[3] AUTO-FIX 실행
     │
     ├── 원본 URL WebFetch (최신 정보 확인)
     ├── 수정 값 결정
     ├── PUT /api/dev/jobs/{id} (변경 필드만)
     └── 204 응답 확인
     ↓
[4] SEMI-AUTO 실행
     │
     ├── 원본 재수집·대조
     ├── 수정 초안 작성
     ├── PUT 실행
     └── 204 응답 확인
     ↓
[5] 재리뷰 (수정된 항목만)
     │
     ├── API에서 수정 후 데이터 재조회
     ├── 해당 항목 재평가
     └── 결과 기록
     ↓
[6] history md 업데이트
     │
     ├── 기존 리뷰 아래에 [RE-REVIEW] 섹션 추가
     ├── 수정 전후 비교 테이블
     └── 최종 판정 업데이트
     ↓
[7] HOLD 목록 정리
     │
     ├── 수정 불가 사유 명시
     └── 사용자 액션 요청 목록 생성
     ↓
[8] Discord 보고
```

---

## 재리뷰 기록 형식

```markdown
## Job #13 — DeNA | AI 스페셜리스트직 [RE-REVIEW]

**수정 일시**: 2026-04-14 14:30
**수정 항목**: A-1, A-2, D-12

### 수정 내역

| 항목 | 수정 전 | 수정 후 | API 응답 |
|------|---------|---------|----------|
| A-1 salaryMin | 6000000 (출처 불명) | 6000000 (snar.jp 확인) | — (값 변경 없음, 출처 확인만) |
| D-12 locations | ["TOKYO"] | ["TOKYO", "YOKOHAMA"] | 204 ✅ |

### 재평가 결과

| # | 평가 항목 | 수정 전 | 수정 후 | 코멘트 |
|---|----------|---------|---------|--------|
| A-1 | 연봉 출처 | ⚠️ | ✅ | snar.jp 포털에서 600만엔~ 확인 완료 |
| A-2 | 연봉 범위 | ⚠️ | ⚠️ | salaryMax 여전히 null (원본도 상한 미기재) |
| D-12 | locations | ⚠️ | ✅ | YOKOHAMA 추가 완료 |

**수정 전**: ✅ 21/25, ⚠️ 4, ❌ 0
**수정 후**: ✅ 23/25, ⚠️ 2, ❌ 0
**최종 판정**: PUBLISH 유지 적합 (개선됨)
```

---

## HOLD 목록 형식

```markdown
## HOLD 목록 — 사용자 판단 필요

| jobId | 회사 | 항목 | 문제 | 필요 액션 |
|-------|------|------|------|----------|
| 886 | DTS | D-11 | SALES_ENGINEER enum 부재 | 백엔드 enum 추가 후 재분류 |
| 910 | SMBC | D-11 | DESIGNER enum 부재 | 백엔드 enum 추가 후 재분류 |
| 853 | Leverages | D-12 | NAGOYA enum 부재 | 백엔드 enum 추가 후 재분류 |
| 950 | SEGA | G-22 | source_url 404 | 공고 유지/삭제 결정 |
```

---

## 주의 사항 (Do / Don't)

- ✅ **PUT 부분 업데이트만 사용**. DELETE 절대 금지.
- ✅ 수정 전 반드시 원본 URL을 **WebFetch로 최신 정보 재확인** 후 수정.
- ✅ 수정 내역을 history md에 **수정 전후 비교와 함께 기록**. 추적 가능해야 함.
- ✅ AUTO-FIX라도 PUT 전에 **변경될 값을 로그에 먼저 기록**.
- ✅ 한 번에 수정하는 건수는 **10건 이하**. 대량 수정 시 사용자 승인 필요.
- ❌ overview 전면 재작성은 AUTO-FIX로 하지 말 것 — SEMI-AUTO 이상.
- ❌ 원본에 없는 정보를 추측으로 채우지 말 것 (예: 연봉 추정치 임의 설정).
- ❌ HOLD 건을 사용자 승인 없이 수정하지 말 것.
- ❌ 토큰을 로그·커밋·Discord에 노출 금지.

---

## 관련 문서
- [`docs/REVIEW_GUIDE.md`](../../docs/REVIEW_GUIDE.md) — 25개 평가 기준
- [`history/`](../../history/) — Deep Review 결과 아카이브
- [`skills/draft-review-publish/`](../draft-review-publish/) — 기존 리뷰·퍼블리쉬 스킬
