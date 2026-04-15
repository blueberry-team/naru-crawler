# 중복 검증

## 대상 목록 조회

`GET /api/jobs?size=200` 으로 현재 PUBLISHED 공고 목록을 가져온다.

## 검증 항목

### 1. jobSourceUrl 중복

리뷰 대상 DRAFT 의 `jobSourceUrl` 과 PUBLISHED 목록의 `jobSourceUrl` 을 대조한다.

- 완전 일치하는 PUBLISHED 공고가 있으면:
  - HOLD — "이미 PUBLISHED 된 동일 공고 존재 (ID={id})"

### 2. title 유사도

리뷰 대상 DRAFT 의 `title` 과 같은 `companySlug` 를 가진 PUBLISHED 공고의 `title` 을 대조한다.

- 같은 회사에 거의 동일한 제목의 공고가 이미 PUBLISHED 되어 있으면:
  - HOLD — "동일 회사에 유사한 제목의 PUBLISHED 공고 존재 (ID={id}, title='{title}')"

유사도 판단 기준:
- 제목에서 직무명 핵심어가 동일하고 부가 정보(지역, 연차 등)만 다른 경우는 중복이 아님
- 제목이 사실상 같은 직무를 가리키면 중복

### 3. DRAFT 간 중복

같은 리뷰 배치 안에서 DRAFT 끼리 `jobSourceUrl` 이 겹치는 경우도 확인한다.

- 겹치면 하나만 리뷰하고 나머지는 HOLD — "동일 jobSourceUrl 의 DRAFT 가 복수 존재 (ID={ids})"
