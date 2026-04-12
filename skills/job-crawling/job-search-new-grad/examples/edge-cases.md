# 엣지 케이스

## ATS 페이지가 지원 폼만 있는 경우

- 그 폼 페이지를 `jobSourceUrl` 로 쓰지 않는다.
- 실제 공고 상세가 있는 원래 페이지로 돌아간다.

## locations 가 불명확한 경우

- 도도부현을 확정할 수 없고 후보지 나열도 없다면:
  - `["UNKNOWN"]`
- `全国`, `国内各地` 만 있고 후보지가 없다면:
  - `["NATIONWIDE"]`

## workType 이 불명확한 경우

- 사무실 위치만 있고 remote / onsite / hybrid 정책이 없다면:
  - `UNKNOWN`

## joinDate fallback

- 명시적 입사 시기가 없고 졸업 규칙도 맞지 않으면:
  - `未定`

## salary 가 애매한 경우

- 연봉 수치가 명시돼 있으면 그대로 사용
- 월급만 있으면 보수적으로 환산
- 상한이 불명확하면 `salaryMax = null`
- 숫자 근거가 너무 애매하면 둘 다 `null`

## selectionProcess 가 없는 경우

- DOM과 이미지 어디에도 흐름 정보가 없으면:
  - `selectionProcess = null`

## 하나의 페이지에 공고가 여러 개인 경우

- 한 페이지에 유효한 트랙이 5개 있으면:
  - 공고 5개 추출
  - payload 5개 생성
  - POST 5번 호출
