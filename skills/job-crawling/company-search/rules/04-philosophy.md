# 기업이념 규칙

## 구조

`philosophy` 는 아래 4개 고정 키를 갖는다.

- `company_philosophy`
- `mission`
- `vision`
- `values_or_behavior`

각 키의 값은 `List<{title, content}>` 형식이다.

## OCR / 이미지

- 이념 텍스트가 이미지뿐이면 screenshot + Vision으로 읽는다.
- 외부 OCR 라이브러리 설치 금지
- `텍스트가 없어서 불가` 로 끝내지 않는다.

## 추출 규칙

1. `MISSION`, `VISION`, `VALUE`, `企業理念` 처럼 "이 아래 내용의 종류"를 알려주는 큰 제목은 `title` 로 저장하지 않는다.
2. 대표 이름, 직함, 서명처럼 내용이 아니라 말한 사람을 표시하는 정보는 제외한다.
3. 제목과 내용이 모두 있으면 둘 다 저장한다.
4. 내용만 있으면 `title=""`
5. 제목만 있으면 `content=""`
6. 정보가 없으면 `[]`
7. `title` 과 `content` 가 완전히 같으면 `title=""` 로 정규화한다.
8. 동일 키 안에서 같은 `title` 이 여러 번 나오면 1개로 합치고 `content` 를 줄바꿈(\n)으로 연결한다.
9. `第一章`, `3つの原則`, `○条` 같은 구조는 장 제목을 `title`, 그 아래 본문을 `content` 로 묶는다.

예시:

- `MISSION` / `VISION` / `企業理念` 같은 섹션명만 보이면 `title` 에 넣지 않는다.
- `Entertainment in Real Life`, `Try`, `Value` 처럼 항목 자체의 고유 이름이 있으면 `title` 에 넣는다.
- `대표이사 사장`, `CEO`, `야마다 타로` 같은 표기는 `content` 에 넣지 않는다.

## 보존 원칙

- 요약하지 않는다.
- 말줄임표로 줄이지 않는다.
- 원문을 가능한 한 그대로 유지한다.
