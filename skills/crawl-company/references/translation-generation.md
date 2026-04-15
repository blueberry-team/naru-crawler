# 번역 및 생성 규칙

이 문서는 `company_search.yml`의 번역 및 생성 관련 세부 제약을 옮긴 기준 문서다.

## 기본 순서

1. 기업 공식 사이트에서 필요한 정보를 추출한다.
2. 추출한 정보를 필드 형식에 맞게 정리한다.
3. 최종 payload에서 사용자에게 보여줄 텍스트를 한국어로 번역한다.
4. `POST /api/dev/companies` 에 `publishStatus: "DRAFT"` 로 제출한다.

## 결측값 규칙

- 정보가 없으면 타입에 따라 `null`, `[]`, `{}`, `""` 를 사용한다.
- 아래 같은 설명문을 값으로 넣지 않는다.
  - `공식 사이트에 기재 없음`
  - `정보 없음`
  - `N/A`

세부 규칙:

- null 허용 필드는 설명문 대신 반드시 `null`을 우선 사용
- null 비허용 문자열 필드는 정보가 없으면 `""`
- 단 `address` 는 예외
  - 공식 정보가 없으면 모델 기존 지식으로 보완 가능
  - 그래도 불가능할 때만 `""`

## 번역 대상 필드

값이 있을 때만 자연스러운 한국어로 번역한다. 직역은 금지한다.

- `name`
- `ceo`
- `description`
- `address`
- `benefitDetail`
- `philosophy`
- `tags`

추가 규칙:

- 최종 payload의 사용자 노출 텍스트에는 일본어가 남으면 안 된다.
- `benefitDetail` 안의 의미가 분명한 제도명은 한국어 뜻으로 풀어 쓴다.
- 회사가 붙인 고유 브랜드형 제도명은 한국어 표기로 적을 수 있다.
- 고유 제도명을 쓸 때도 제도명만 단독으로 남기지 말고, 페이지에 적힌 의미나 조건을 함께 한국어로 설명한다.

## 번역 금지 / 그대로 유지할 필드

아래는 원문 값을 그대로 유지한다.

### ID / URL

- `slug`
- `website`
- `logoUrl`

### 수치 데이터

- `revenue`
- `employeesGroup`
- `employeesEntity`
- `companyRating`
- `establishedDate`

### Enum

- `industry`
- `location`
- `workType`
- `companyType`
- `flexTime`

### 기타

- `searchKeywords`
- `publishStatus`

## searchKeywords 제약

- `searchKeywords` 는 번역 금지
- 요소 변환, 치환, 순서 변경, 추가, 삭제 금지
- 서비스명 / 제품명 / 브랜드명 / 일반명사 금지
- 대소문자만 다른 변형 금지
- 영어명은 `기본형 1개 + 공백 변형` 만 허용
  - 예: `CyberAgent`, `Cyber Agent`
  - 금지: `cyberagent`, `CYBERAGENT`

## logoUrl

- `logoUrl` 는 `https://img.logo.dev/{domain}` 형식으로 생성한다.
- `www.` 는 제거한다.

## revenue

- `integer(64)` 형식
- 엔 단위 저장
- 변환 규칙:
  - `兆` → `10^12`
  - `億` → `10^8`
  - `万` → `10^4`
  - `千` → `10^3`
- 콤마와 공백은 제거한다.
- 수집 대상 회사 자체의 연결 매출이 있으면 우선 사용
- 수집 대상 회사 자체의 단독 매출만 있으면 그 값을 사용
- 모회사나 그룹 전체 매출만 보이고 수집 대상 회사의 매출이 아니면 사용 금지
- 자회사 페이지에서 모회사 그룹 연결 매출만 확인되면 넣지 않음
- 매출의 적용 범위가 불명확하면 `null`
- 정보 없음 또는 계산 불가면 `null`

예시:

- `1億円` → `100000000`
- `7,097億円` → `709700000000`
- `3兆5,574億円` → `3557400000000`
- `5,000万円` → `50000000`

## companyType

- `FOREIGN` 판정을 최우선한다.
- 종업원 수 판정보다 우선한다.

아래 중 하나라도 공식 소스에서 확인되면 `FOREIGN`:

1. `日本法人`, `日本支社`, `日本拠点` 등 해외 본사 기업의 일본 법인 표기
2. `[해외기업명]의 일원`, `part of [global company]` 같은 모회사 귀속 표현
3. Headquarters 가 일본 국외
4. 일본 법인이어도 모회사가 해외 법인이라는 공식 표기

`FOREIGN` 이 아니라면 종업원 수 기준으로 판정한다.

- `employeesEntity` 우선, 없으면 `employeesGroup`
- `>= 2000` → `LARGE`
- `300-1999` → `MID`
- `< 300` → `SMALL`
- 둘 다 `null` → `UNKNOWN`

## companyRating

- 취득 불가면 `null`
- `0` 으로 채우지 않는다.
- 취득 가능하면 소수점 첫째 자리 반올림

## philosophy 공통 생성 규칙

- 4개 고정 키를 모두 만든다.
  - `company_philosophy`
  - `mission`
  - `vision`
  - `values_or_behavior`
- 각 키 값은 `List<{title, content}>`
- `MISSION`, `VISION`, `企業理念` 처럼 섹션 종류를 알려주는 큰 제목은 `title` 로 저장하지 않는다.
- 대표 이름, 직함, 서명처럼 본문 내용이 아닌 표기는 제외한다.
- 정보가 없으면 `[]`
- `title` 과 `content` 가 같으면 `title=""` 로 정리
- 같은 `title` 이 반복되면 1개 요소로 합치고 `content` 를 줄바꿈으로 연결

## 최종 제출

- `POST /api/dev/companies`
- `publishStatus` 는 반드시 `DRAFT`
