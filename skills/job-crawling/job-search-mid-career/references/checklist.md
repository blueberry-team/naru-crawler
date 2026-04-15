# 체크리스트

각 공고를 POST 하기 전에 아래 항목을 반드시 확인한다.

## 공고 대상

- 중도채용 공고인가
- 신입 / 아르바이트 / 단순 지원 폼 / 비대상 공고가 섞이지 않았는가
- 목록 페이지가 아니라 상세 페이지까지 들어갔는가

## URL

- `jobSourceUrl` 이 실제 상세 공고 URL 인가
- 지원 폼 URL이 아닌가
- 외부 ATS로 이동했더라도 상세 공고 기준 URL을 잡았는가

## title / 분류

- `title` 이 기능명만으로 끝나지 않는가
- `【番号】` prefix 를 제거했는가
- `position` 이 백엔드 `Position` enum 중 하나인가
- `position` 이 [`enums.md`](./enums.md) 에 있는 실제 enum 값인가
- `GRADUATE_*` enum 을 쓰지 않았는가
- `experienceLevel` 이 `MID_CAREER` 인가

## locations / workType

- `locations` 가 빈 배열이 아닌가
- 도도부현 근거가 없으면 `UNKNOWN` 규칙을 지켰는가
- `workType` 을 근거 없이 추측하지 않았는가
- 근거 없으면 `UNKNOWN` 으로 두었는가

## joinDate / deadline

- `joinDate` 가 비어 있지 않은가
- 입사 가능 시기 규칙을 적용할 수 있으면 적용했는가
- 그래도 불명확하면 `미정` 으로 넣었는가
- `deadline` 은 명시된 경우만 `YYYY-MM-DD` 인가
- `随時`, `通年`, `未定` 를 `null` 로 처리했는가

## salary

- 연봉 명시가 있으면 그 값을 그대로 사용했는가
- 수당 포함 여부를 임의로 조정하지 않았는가
- 월급 환산 시 급여성 항목만 합산했는가
- 상한이 불명확하면 `salaryMax = null` 인가
- 숫자 파싱이 `万`, `千円`, `円` 규칙을 지켰는가

## 번역

- 사용자 노출 텍스트가 한국어인가
- 일본어 원문을 그대로 남기지 않았는가
- glossary forbidden 표현이 남아 있지 않은가
- 번역 금지 필드를 바꾸지 않았는가

번역 금지 필드:

- `companySlug`
- `position`
- `locations`
- `experienceLevel`
- `workType`
- `salaryMin`
- `salaryMax`
- `deadline`
- `jobSourceUrl`
- `publishStatus`

## content fields

- `overview` 는 설명문 중심인가
- `tasks` 는 실제 업무인가
- `techStack` 은 명시된 기술만 들어갔는가
- `benefitDetail` 은 같은 공고 페이지의 정보만 반영했는가
- `selectionProcess` 에 단계 순서가 명확히 드러나는가

## targetAudience / targetCandidate

- `targetAudience` 에 경력 연차 / 직무축 / 레벨 같은 상단 요약만 들어갔는가
- 상세 조건은 `targetCandidate` 로 분리했는가
- `targetCandidate` 구조가 고정 key 를 모두 갖고 있는가

필수 key:

- `mustHave`
- `niceToHave`
- `idealCandidate`
- `selectionPoints`
- `workingConditions`
- `notes`

## API payload

- `camelCase` 를 사용했는가
- 불필요한 extra key 가 없는가
- `publishStatus` 가 반드시 `DRAFT` 인가
- `1공고 = 1payload = 1POST` 규칙을 지켰는가
