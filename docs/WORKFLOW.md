# 나루 공고 적재 워크플로우

> **원칙**: 기존 DB는 절대 수정/삭제 금지. 추가만 허용.
> 모든 적재는 정우의 검토·승인 후 단건(1개)씩 진행.

---

## ⛔ 절대 규칙 — 어떤 상황에서도 예외 없음

### DB 조작
| 작업 | 허용 여부 |
|------|----------|
| 공고 추가 (POST) | ✅ 단, 승인 후 단건씩만 |
| 공고 수정 (PUT) | ⚠️ 정우 허락 받은 후에만 |
| 공고 삭제 (DELETE) | ❌ 직접 실행 절대 금지 — 반드시 정우에게 먼저 물어볼 것 |
| 기업 생성 | ⚠️ slug 확인 후 없을 때만, 정우 보고 후 |
| 기업 수정/삭제 | ❌ 절대 금지 |

### 적재 프로세스
- **승인 없이 POST 금지** — 원문 + 번역 + payload 전부 보여주고 OK 받을 것
- **단건씩** — 무더기 적재 금지
- **모든 텍스트 한국어** — 일본어 원문 그대로 적재 금지
- **publishStatus 항상 `"DRAFT"`** — `"status"` 필드명 절대 금지
- **dry-run 먼저** — 크롤러 실행 시 반드시 dry-run → 보고 → 승인 → 실행 순서

### 과거 반복 실수 — 절대 재발 금지
- slug 확인 없이 새 회사 생성 → DB 오염
- `"status": "DRAFT"` 사용 → 전체 PUBLISHED 자동 등록
- 승인 받기 전에 혼자 적재 실행
- 일본어 원문 그대로 적재
- 삭제하겠다고 선언 후 바로 실행 (삭제는 항상 되물을 것)

---

## 액션 0 — 과거 실수 리뷰 (매 적재 전 필수)

`docs/MISTAKES.md` 를 반드시 먼저 읽고 동일 실수 반복 방지.

**주요 반복 금지 실수:**
- [ ] 기업 slug 확인 없이 새 회사 생성 (DB 오염 원인)
- [ ] `publishStatus` 아닌 `status` 필드명 사용 → 자동 PUBLISHED됨
- [ ] `entry.phtml` (지원서 페이지) URL을 jobSourceUrl로 사용
- [ ] 제목에 【번호】 prefix 그대로 남김
- [ ] salary null로 방치 (공개 데이터 조사 없이 포기)
- [ ] ExperienceLevel/Position enum 실제 배포 버전 확인 없이 추측
- [ ] 승인 없이 혼자 적재 실행
- [ ] 일본어 원문 그대로 적재
- [ ] 삭제 선언 후 바로 실행 (항상 되물을 것)

---

## 액션 1 — 기업 존재 여부 확인

```
GET /api/companies?size=200
```

- 기존 등록 회사 slug 목록에서 해당 기업 있는지 탐색
- **있으면**: 해당 slug 사용, 절대 새 회사 생성 금지
- **없으면**: 정우에게 먼저 보고 후 지시 대기

보고 형식:
```
🔍 기업 확인: [회사명]
→ DB 존재: ✅ slug=hitachi (ID=22) / ❌ 없음
```

---

## 액션 2 — 중복 공고 확인

```
GET /api/dev/jobs/drafts   (DRAFT 목록)
GET /api/jobs?size=200     (PUBLISHED 목록)
```

- `jobSourceUrl` 또는 제목으로 동일 공고 이미 있는지 확인
- 있으면 → 적재 스킵, 정우에게 보고

보고 형식:
```
🔍 중복 확인: [공고명]
→ DRAFT: ❌ 없음 / ✅ ID=492 중복 존재
```

---

## 액션 3 — 원문 수집 + 날짜/우선순위 분석

### 출처 URL
- 상세 페이지: `https://hitachi.jposting.net/u/job.phtml?job_code={ID}` ✅
- 지원서 페이지: `entry.phtml` ❌ (사용 금지)

### 날짜 확인 항목
| 항목 | 확인 방법 | 우선순위 영향 |
|------|----------|------------|
| **마감일** (deadline) | 원문 페이지에서 탐색 | 마감 임박 → 높은 우선순위 |
| **게재일** (공고 등록일) | API 응답의 `is_new`, 날짜 필드 | 최신 공고 우선 |
| **수시 채용 여부** | 原文 "随時", "通年" 등 | 마감일 null 처리 |

### 우선순위 기준
1. 마감일 있는 공고 (임박할수록 높음)
2. AI/데이터/연구직 (플랫폼 타겟과 일치)
3. 최근 게재 공고

보고 형식:
```
📋 원문 출처: https://hitachi.jposting.net/u/job.phtml?job_code=15
📅 마감일: 없음 (수시 채용)
📅 게재일: 확인 불가 (is_new: false)
⚡ 우선순위: 중 (수시 + AI연구직)
```

---

## 액션 4 — 번역 + payload 작성 및 보고

### 필드 작성 기준

| 필드 | 기준 |
|------|------|
| `title` | 한국어 번역, 【번호】 prefix 완전 제거 |
| `position` | 실제 배포 enum 사용 (Position.java 확인) |
| `experienceLevel` | `NEW_GRAD` 또는 `MID_CAREER` 둘 중 하나만 |
| `workType` | `REMOTE` / `ONSITE` / `HYBRID` / `UNKNOWN` |
| `joinDate` | 한국어 (예: `수시 채용`, `2026년 4월`) |
| `overview` | 職務概要 섹션 → 한국어 번역 |
| `tasks` | 職務詳細 불릿 → 한국어 배열 (최대 7개) |
| `targetAudience` | 모집 대상 → 한국어 한 문장 |
| `targetCandidate` | 아래 구조 한국어로 채움 |
| `selectionProcess` | 선발 단계 → 한국어. "복수 회" 사용 금지 → "2~3회" 또는 "여러 차례" |
| `jobSourceUrl` | `job.phtml?job_code=` 형식 |
| `salaryMin` | 공개 데이터 보수적 추정. 불명확하면 null |
| `salaryMax` | 확신 없으면 null |
| `deadline` | 마감일 있으면 `YYYY-MM-DD`, 수시채용이면 null |
| `publishStatus` | 항상 `"DRAFT"` |

### targetCandidate 구조
```json
{
  "notes": ["공고 특이사항, 지원 절차 안내 등"],
  "mustHave": ["필수 요건"],
  "niceToHave": ["우대 요건"],
  "idealCandidate": ["이런 분을 찾습니다"],
  "selectionPoints": ["평가 포인트"],
  "workingConditions": ["근무지, 근무 형태, 팀 규모 등"]
}
```

### 급여 추정 기준 (히타치 기준, 공개 데이터 기반)
| 포지션 태그 | salaryMin | salaryMax |
|------------|----------|----------|
| 主任クラス (S6) | 6,500,000 | 7,500,000 (또는 null) |
| 上級主任 (S5) | 8,000,000 | null |
| 経験者・専門職 | 5,000,000 | null |
| 담당자クラス | 4,500,000 | null |
| 不明 / 協議 | null | null |

### 보고 형식 (정우 승인용)
```
【원문】
■ 職務概要: (일본어 원문)

【번역】
■ overview: (한국어 번역)

【최종 payload】
{ ... JSON ... }
```

---

## 액션 5 — 승인 후 단건 적재

정우 OK 받은 후:
1. `POST /api/dev/jobs` 단 1건만 적재
2. 201 응답 확인
3. `GET /api/dev/jobs/{id}/preview` 로 전 필드 재검증
4. 보고:
```
✅ DRAFT 적재 완료 ID=512
title: 대규모 다종 데이터 관리 및 처리 기술 연구개발
company: 주식회사 히타치제작소
salary: 6,500,000 ~ 7,500,000엔
jobSourceUrl: https://...
```

---

## 액션 6 — 피드백 반영

- 수정 요청 → `PUT /api/dev/jobs/{id}` 해당 필드만 수정 (절대 삭제 금지)
- 동일 수정이 크롤러 로직에도 해당하면 → 코드 수정 + `docs/MISTAKES.md` 업데이트 + commit/push

---

## 요약 체크리스트

```
□ 0. MISTAKES.md 읽기
□ 1. 기업 slug 기존 DB에서 확인
□ 2. 중복 공고 없는지 DRAFT/PUBLISHED 탐색
□ 3. 원문 수집 + 마감일/게재일 확인 + 우선순위 판단
□ 4. 원문↔번역 대조 + 전체 payload → 정우에게 보고
□ 5. 승인 후 단건 POST (publishStatus: DRAFT)
□ 6. 적재 결과 검증 + 피드백 반영
```
