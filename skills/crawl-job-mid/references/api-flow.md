# API 플로우

이 스킬은 로컬 추출로 끝나지 않는다. 최종 단계는 API 요청이다.

## 기본 모델

- 하나의 페이지 안에는 여러 트랙이 있을 수 있다.
- 한 페이지에 유효한 중도채용 공고가 5개 있으면 5개 모두 처리한다.
- 각 트랙은 하나의 정규화된 payload가 된다.
- 각 payload마다 POST 요청을 1번씩 보낸다.

## 필수 순서

1. 시작 URL 접속
2. 중도채용 섹션 진입
3. 각 공고 상세 페이지 진입
4. 일본어 원문 수집
5. 모든 필드 정규화
6. 한국어 번역
7. payload 검증
8. `/api/dev/jobs` POST

## 절대 규칙

- bundle JSON 파일을 만들지 않는다.
- payload 생성에서 멈추지 않는다.
- 배열 payload 하나로 여러 공고를 보내지 않는다.
- 여러 공고를 하나의 객체로 합치지 않는다.
- 지원 폼 URL을 `jobSourceUrl` 로 쓰지 않는다.
- `publishStatus` 를 빼먹지 않는다.

## API 엔드포인트

- Method: `POST`
- Path: `/api/dev/jobs`
- Headers:
  - `Content-Type: application/json`
  - `X-Admin-Token: {NARU_ADMIN_TOKEN}`

## 출력 모델

- `1 상세 공고 = 1 payload = 1 POST`
- 한 공고가 검증이나 POST에서 실패해도, 사용자가 중단을 요구하지 않았다면 나머지는 계속 처리하되 결과를 분리해서 보고한다.
