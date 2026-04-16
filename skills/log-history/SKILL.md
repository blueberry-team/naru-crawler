---
name: log-history
description: 나루 공고 리뷰/수정/마감정리 작업을 history/ 폴더의 md 파일에 기록할 때 따르는 공통 포맷. deep-review, fix-reviewed, cleanup-deadline 등에서 공유.
---

# log-history — 리뷰 히스토리 기록 포맷

## 원칙

한 공고 = **하나의 섹션**. 여러 라운드 리뷰/수정이 반복돼도 기존 섹션에 append하지 말고 **기존 섹션의 "리뷰 이력" 테이블에 한 줄 추가**한다. 메타데이터(소스/링크 등) 중복 금지.

## 섹션 구조

```markdown
## Job #{id} — {회사명} | {title}

**상태**: PUBLISHED / DRAFT
**소스**: {jobSourceUrl}
**나루 공고**: https://www.naru-recruit.com/jobs/{id}
**어드민**: https://www.naru-recruit.com/admin/jobs/{id}?token=jungwoo_naru_server_password_0129

### 리뷰 이력 (시간순)
| 시각 | 액션 | 상세 |
|------|------|------|
| MM/DD HH:mm | 리뷰 | N/25 ⚠️X ❌Y → 판정 |
| MM/DD HH:mm | Fix | 필드명 변경내용 PUT 204 |
| MM/DD HH:mm | 재검증 | Playwright 확인 — 근거 |

### 원문 현황 (최신)
- **勤務地**: 원문 발췌
- **給与**: 원문 발췌
- **모집상태**: 활성 / 종료 / (리다이렉트 정보)

### 평가 상세 (필요 시, 최종 한 번만)
| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅/⚠️/❌ | ... |

**최종 판정**: PUBLISH / Fix+PUBLISH / HOLD / DRAFT 유지
```

## 작성 규칙

### 1. 섹션 중복 금지

- `[RE-REVIEW]`, `[RE-RE-REVIEW]` 같은 별도 헤더로 공고 섹션을 반복 추가하지 않는다.
- 이미 파일에 `## Job #{id}` 섹션이 있으면 **그 섹션 내부 "리뷰 이력" 테이블에 한 줄만 추가**한다.
- "원문 현황" 블록은 최신 확인 내용으로 **덮어쓴다**(과거 값은 리뷰 이력에만 남음).

### 2. 신규 섹션 추가 시

파일에 해당 공고 섹션이 없으면 파일 끝에 `---` 구분선과 함께 새 섹션 생성.

### 3. 리뷰 이력 테이블 엔트리

- `시각`: `MM/DD HH:mm` (JST)
- `액션`: `리뷰` / `Fix` / `재검증` / `마감Fix` / `Unpublish` / `Revert`
- `상세`: 1~2 문장. 수치/필드명/PUT 응답코드/Playwright 확인 근거 간결 기재

### 4. 평가 상세 테이블

- 25개 기준 전체 테이블은 **최초 리뷰** 또는 **변동 있는 회차**만 작성.
- 변경 없는 재검증에서는 생략 (리뷰 이력 한 줄로 충분).

### 5. 불필요 정보 금지

- 같은 회사/URL을 여러 공고가 공유할 때 "#N과 동일" 표현 사용, 내용 복붙 금지.
- 이전 회차의 판정/근거를 반복 서술하지 않는다. "이전 #NN 판정 유지" 한 줄로 충분.

## 편집 흐름

```bash
# 1. 기존 섹션 존재 여부
grep -n "^## Job #${id} —" history/historyXXX-YYY.md

# 2-A. 있으면: "리뷰 이력" 테이블 끝에 한 줄 추가 (python/awk)
# 2-B. 없으면: 파일 끝에 --- + 새 섹션 append

# 3. "원문 현황" 블록이 있으면 업데이트, 없으면 추가

# 4. git add/commit/push
```

## 예시: 여러 라운드를 하나로 압축

**Before (중복 섹션)**
```markdown
## Job #13 — DeNA | AI Specialist
[메타...]
...리뷰 테이블...

## Job #13 [RE-REVIEW] — DeNA | AI Specialist
[메타 중복...]
...동일 평가 반복...

## Job #13 [RE-RE-REVIEW] — DeNA | AI Specialist
[메타 중복 또...]
```

**After (통합 섹션)**
```markdown
## Job #13 — DeNA | AI Specialist

**상태**: PUBLISHED
**소스**: https://student.dena.com/aispecialist/
...

### 리뷰 이력
| 04/14 13:20 | 리뷰 | 22/25 ⚠️2 → PUBLISH 유지 |
| 04/15 15:05 | Fix | locations +KANAGAWA PUT 204 |
| 04/15 18:20 | 재검증 | Playwright 재확인, 3건 불일치 발견 |
| 04/15 18:36 | Fix | URL/locations/salaryMin 3건 PUT 204 |

### 원문 현황 (최신)
- 勤務地: 渋谷(東京)+横浜(神奈川)
- 給与: 7,000,000 (2026-03-06 改定後)

**최종 판정**: Fix+PUBLISH
```

---

## 자동화 힌트

append-only 스크립트로는 한계가 있다. 섹션 업데이트를 자동화할 때는:

1. `grep -n "^## Job #${id} —"` 로 섹션 시작 행 찾기
2. 다음 `^## Job ` 또는 `^---$` 까지가 해당 섹션
3. 섹션 내 "리뷰 이력" 테이블 `| ... |` 마지막 행 뒤에 삽입
4. "원문 현황" 블록은 전체 교체

Python `re.sub`나 `awk` 로 블록 단위 편집 권장. 순수 `cat >>` 는 신규 공고 섹션 추가 시에만 사용.
