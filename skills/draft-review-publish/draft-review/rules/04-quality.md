# 데이터 품질 검증

DB에서 가져온 AdminJobResponse 의 모든 필드를 전수 검사한다.

## 1. enum 실존 검증

각 enum 필드의 값이 `references/enums.md` 의 목록에 실제로 존재하는지 대조한다.

| 필드 | 허용 값 | 실패 시 |
|------|---------|--------|
| `position` | Position enum 47개 중 하나 | FIX — 원문 대조 후 재분류 |
| `locations` | 배열 내 모든 값이 Location enum 49개 중 하나 | FIX — 유효하지 않은 값 제거, 원문 기반 재매핑 |
| `experienceLevel` | `NEW_GRAD`, `MID_CAREER` | FIX — 원문 대조 후 수정 |
| `workType` | `REMOTE`, `ONSITE`, `HYBRID`, `UNKNOWN` | FIX — 원문 대조 후 수정 |
| `recruitmentType` | `NEW_GRADUATE`, `OPEN_RECRUITMENT`, `ROLLING`, null | FIX — 원문 기반 설정 |
| `publishStatus` | `DRAFT` 여야 함 | 이상 시 HOLD |

존재하지 않는 값이 들어있으면 원본 페이지를 참고하여 올바른 enum 으로 PUT 수정한다.

## 2. 분류 정확도 (원문 대조)

enum 값이 실존하더라도, 원문과 일치하는지 교차 검증한다.

| 검증 | 방법 | 예시 |
|------|------|------|
| `position` vs 원문 직무명 | 페이지의 직무 제목/카테고리와 대조 | "프론트엔드 개발자" 인데 `BACKEND` → FIX |
| `locations` vs 원문 근무지 | 勤務地/勤務場所/勤務先 섹션과 대조 | 오사카 근무인데 `TOKYO` → FIX |
| `experienceLevel` vs 원문 대상 | 新卒/中途/경력 키워드 대조 | 신졸 공고인데 `MID_CAREER` → FIX |
| `workType` vs 원문 근무형태 | リモート/在宅/出社/テレワーク 키워드 대조 | 풀리모트인데 `ONSITE` → FIX |

## 3. 필수 필드 검증

서버의 `@NotNull`/`@NotBlank` 기준과 품질 기준을 함께 적용한다.

| 필드 | 검증 | 실패 시 |
|------|------|--------|
| `title` | 비어있지 않음, 5자 이상, 의미 있는 직무명 포함 | HOLD |
| `position` | 위 enum 검증 참고 | FIX |
| `locations` | 빈 배열이 아님 | FIX — 원문에서 근무지 추출 |
| `experienceLevel` | 위 enum 검증 참고 | FIX |
| `joinDate` | 비어있지 않음 | FIX — 원문에서 입사 시기 추출, 불명확하면 "미정" |
| `workType` | 위 enum 검증 참고 | FIX |
| `companySlug` | `GET /api/companies?size=200` 에서 존재 확인 | HOLD — "companySlug '{slug}'가 DB에 존재하지 않습니다" |

## 4. 권장 필드 품질 검증

| 필드 | 검증 | 실패 시 |
|------|------|--------|
| `overview` | 50자 이상, 실제 직무 설명, 보일러플레이트가 아님 | FIX — 원문에서 보강 |
| `tasks` | 1개 이상, 각 항목이 구체적 업무 | FIX — 원문에서 추출 |
| `targetCandidate` | Map 키가 의미 있는 한국어, 값 배열이 비어있지 않음 | FIX |
| `benefitDetail` | `targetCandidate` 와 내용 중복 없음 | FIX — 중복 항목 제거 |
| `selectionProcess` | 자연스러운 한국어, "복수 회" 사용 금지 | FIX — 표현 수정 |
| `jobSourceUrl` | 비어있지 않음 (02-url-validation 에서 이미 검증) | HOLD |
| `salaryMin`/`salaryMax` | 있으면 상식적 범위 (연봉 200만~5000만엔) | FIX — 이상치 제거 또는 null |
| `salaryMin`/`salaryMax` | 둘 다 null 이면 공개 데이터 조사 시도 | FIX 가능하면 추가, 불가능하면 유지 |
| `deadline` | 있으면 미래 날짜인지 확인 (03-freshness 와 연계) | FIX 또는 HOLD |
| `targetAudience` | 한국어, 모집 대상 한 문장 | FIX |
| `techStack` | 있으면 실제 기술명인지 (HTML ruby 오탐 등 체크) | FIX — 잘못된 항목 제거 |
| `recruitmentType` | 원문 채용 유형과 일치 | FIX |

## 5. 텍스트 품질 검증

모든 텍스트 필드에 대해 수행한다: `title`, `overview`, `tasks` 각 항목, `selectionProcess`, `targetAudience`, `targetCandidate` 의 모든 값, `benefitDetail` 의 모든 값.

| 검증 | 예시 | 실패 시 |
|------|------|--------|
| HTML 태그 잔여물 | `<br>`, `&nbsp;`, `<p>`, `</div>` | FIX — 태그 제거 |
| 깨진 문자 (mojibake) | `ã‚¢`, `â€"` | FIX — 원문에서 재번역 |
| 일본어 미번역 | 히라가나/카타카나/한자가 사용자 노출 필드에 잔존 | FIX — 한국어로 번역 |
| 제목 prefix 잔존 | `【15】`, `[A-001]` 등 | FIX — prefix 제거 |
| 어색한 표현 | "복수 회", "수차례에 걸쳐" 등 | FIX — 자연스러운 한국어로 수정 |
| 과도한 줄바꿈/공백 | 연속 빈 줄, 불필요 들여쓰기 | FIX — 정리 |
