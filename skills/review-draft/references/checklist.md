# 리뷰 체크리스트

각 DRAFT 공고를 판정하기 전에 아래 항목을 반드시 확인한다.

## URL

- `jobSourceUrl` 이 비어있지 않은가
- 접근 시 200 응답을 받는가
- 응답 페이지가 개별 공고 상세인가 (채용 사이트 메인/목록이 아닌가)
- 페이지의 직무 제목이 DB의 `title` 과 의미적으로 일치하는가
- 리다이렉트 후 채용 메인으로 빠지지 않는가

## 채용 현행성

- 원본 페이지에 마감/종료 키워드가 없는가
- `deadline` 이 오늘 이전이 아닌가
- 원본 사이트의 공고 목록에 아직 존재하는가

## enum 정합성

- `position` 이 Position enum 47개 중 하나인가
- `locations` 의 모든 값이 Location enum 49개 중 하나인가
- `locations` 가 빈 배열이 아닌가
- `experienceLevel` 이 `NEW_GRAD` 또는 `MID_CAREER` 인가
- `workType` 이 `REMOTE`, `ONSITE`, `HYBRID`, `UNKNOWN` 중 하나인가
- `recruitmentType` 이 유효한 값 또는 null 인가
- `publishStatus` 가 `DRAFT` 인가

## 분류 정확도

- `position` 이 원문 직무명/카테고리와 일치하는가
- `locations` 가 원문 근무지와 일치하는가
- `experienceLevel` 이 원문 대상 (新卒/中途) 과 일치하는가
- `workType` 이 원문 근무 형태와 일치하는가

## 필수 필드

- `title` 이 5자 이상이고 의미 있는 직무명을 포함하는가
- `joinDate` 가 비어있지 않은가
- `companySlug` 가 DB에 실제 존재하는가

## 권장 필드 품질

- `overview` 가 50자 이상이고 실제 직무 설명인가
- `tasks` 가 1개 이상이고 구체적 업무인가
- `targetCandidate` 의 키가 의미 있는 한국어이고 값 배열이 비어있지 않은가
- `benefitDetail` 이 `targetCandidate` 와 내용 중복이 아닌가
- `selectionProcess` 가 자연스러운 한국어인가
- `salaryMin`/`salaryMax` 가 있으면 상식적 범위인가

## 텍스트 품질

- HTML 태그 잔여물이 없는가 (`<br>`, `&nbsp;`, `<p>` 등)
- 깨진 문자(mojibake)가 없는가
- 일본어가 번역되지 않고 그대로 남아 있지 않은가
- `title` 에 불필요한 prefix (번호, 코드 등)가 남아있지 않은가
- `selectionProcess` 에 "복수 회" 같은 어색한 표현이 없는가

## 중복

- 동일 `jobSourceUrl` 로 이미 PUBLISHED 된 공고가 없는가
- 매우 유사한 `title` 의 PUBLISHED 공고가 없는가
