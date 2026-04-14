# Company payload 형식

`POST /api/dev/companies` 제출 시 아래 구조를 기준으로 사용한다.

```json
{
  "name": "주식회사 샘플",
  "slug": "sample",
  "industry": "MEDIA_ADVERTISING",
  "location": "TOKYO",
  "workType": "HYBRID",
  "flexTime": true,
  "logoUrl": "https://img.logo.dev/example.com",
  "employeesGroup": 1148,
  "employeesEntity": 676,
  "tags": ["엔터테인먼트", "스마트폰 게임", "플렉스타임"],
  "description": "스마트폰 게임을 중심으로 콘솔 게임, XR, 블록체인 게임까지 전개하는 엔터테인먼트 기업이다.",
  "ceo": "야마다 타로",
  "companyType": "MID",
  "establishedDate": "2008-10-01",
  "revenue": 25933000000,
  "website": "https://example.com/",
  "address": "일본 도쿄도 미나토구 ...",
  "benefitDetail": {
    "근무 방식": ["재택근무와 출근을 병행한다."],
    "복리후생": ["선택형 복리후생 제도를 운영한다."]
  },
  "philosophy": {
    "company_philosophy": [{ "title": "", "content": "일상을 더 즐겁게 만든다." }],
    "mission": [{ "title": "Entertainment in Real Life", "content": "기술과 아이디어로 새로운 경험을 만든다." }],
    "vision": [],
    "values_or_behavior": [{ "title": "", "content": "변화를 두려워하지 않고 도전한다." }]
  },
  "companyRating": 3.0,
  "ratingSource": "OpenWork",
  "searchKeywords": ["株式会社サンプル", "Sample Inc.", "주식회사 샘플", "샘플"],
  "companySourceUrls": {
    "홈": ["https://example.com/"],
    "회사개요": ["https://example.com/company"],
    "채용": ["https://example.com/recruit"],
    "모집요강·복리후생": ["https://example.com/recruit/welfare"],
    "기업이념": ["https://example.com/philosophy"],
    "IR": ["https://example.com/ir"]
  },
  "publishStatus": "DRAFT"
}
```

## 필수 필드

- `name`
- `slug`
- `industry`
- `location`
- `address`
- `workType`
- `companyType`
- `publishStatus`

나머지는 `null`, `[]`, `{}` 허용 범위에 맞춰 채운다.

## 필드별 형태

### 기본 필드

- `name`: 한국어 회사명 문자열
- `slug`: 영문 slug
  - 수집 대상 회사의 공식 영어 회사명을 기준으로 만든다.
  - 푸터 영어 회사명은 보조 근거로 쓸 수 있지만, 모회사명이나 그룹명인지 확인해야 한다.
  - 법인을 제거하고 소문자 + `-` 형식으로 정리한다.
- `description`: 한국어 소개문 문자열 또는 `null`
- `tags`: 한국어 태그 배열, 최대 10개
- `website`: 공식 사이트 루트 URL
- `logoUrl`: `https://img.logo.dev/{domain}` 형식
- `address`: 한국어 주소 문자열. 공식 주소가 없을 때만 예외 규칙 적용
- `ceo`: 한국어 인명 문자열 또는 `null`

### 수치 / 날짜 필드

- `employeesGroup`: 연결 기준 종업원 수 정수 또는 `null`
- `employeesEntity`: 개별 기준 종업원 수 정수 또는 `null`
- `revenue`: 엔 단위 `int64` 또는 `null`
  - 수집 대상 회사 자체의 연결 매출이 있으면 우선 사용한다.
  - 수집 대상 회사 자체의 단독 매출만 있으면 그 값을 사용한다.
  - 모회사나 그룹 전체 매출만 보이는 경우에는 사용하지 않는다.
  - 자회사를 수집 중인데 모회사 그룹 연결 매출만 보이면 `null` 로 둔다.
- `establishedDate`: `YYYY-MM-DD` 또는 `null`
- `companyRating`: 소수점 평점 또는 `null`
- `ratingSource`: 현재는 `OpenWork` 또는 `null`

### 구조형 필드

- `benefitDetail`: `Map<String, List<String>>`
  - 키는 한국어 섹션명
  - 값은 자연스러운 한국어 문장 배열
  - 각 요소는 복지나 제도를 설명하는 의미 단위 1개
  - 정보가 없으면 `{}`
- `philosophy`
  - 고정 키 4개를 모두 포함한다.
  - `company_philosophy`
  - `mission`
  - `vision`
  - `values_or_behavior`
  - 각 값은 `[{ "title": string, "content": string }]` 배열이다.
  - 정보가 없으면 해당 배열은 `[]`
- `companySourceUrls`: `Map<String, List<String>>`
  - 최종 payload에서는 한국어 키만 사용한다.
  - 허용 키: `홈`, `회사개요`, `채용`, `모집요강·복리후생`, `기업이념`, `IR`, `기타`
  - 값은 공식 URL 배열이다.
  - OpenWork URL은 넣지 않는다.
- `searchKeywords`
  - 일본어, 영어, 한국어 회사명 변형이 함께 들어갈 수 있다.
  - 회사명 변형만 넣는다.
  - 서비스명, 제품명, 브랜드명은 넣지 않는다.

## Enum

### industry

- `FINANCE`
- `CONSULTING_PROFESSIONAL`
- `IT_TELECOM_INTERNET`
- `INFRA_TRANSPORT_REAL_ESTATE_CONSTRUCTION`
- `MANUFACTURING_TRADING`
- `HEALTHCARE`
- `MEDIA_ADVERTISING`
- `SERVICE_RETAIL_FOOD`
- `PUBLIC_NPO`
- `OTHER`
- `UNKNOWN`

### location

- `NATIONWIDE`
- `HOKKAIDO`
- `AOMORI`
- `IWATE`
- `MIYAGI`
- `AKITA`
- `YAMAGATA`
- `FUKUSHIMA`
- `IBARAKI`
- `TOCHIGI`
- `GUNMA`
- `SAITAMA`
- `CHIBA`
- `TOKYO`
- `KANAGAWA`
- `NIIGATA`
- `TOYAMA`
- `ISHIKAWA`
- `FUKUI`
- `YAMANASHI`
- `NAGANO`
- `GIFU`
- `SHIZUOKA`
- `AICHI`
- `MIE`
- `SHIGA`
- `KYOTO`
- `OSAKA`
- `HYOGO`
- `NARA`
- `WAKAYAMA`
- `TOTTORI`
- `SHIMANE`
- `OKAYAMA`
- `HIROSHIMA`
- `YAMAGUCHI`
- `TOKUSHIMA`
- `KAGAWA`
- `EHIME`
- `KOCHI`
- `FUKUOKA`
- `SAGA`
- `NAGASAKI`
- `KUMAMOTO`
- `OITA`
- `MIYAZAKI`
- `KAGOSHIMA`
- `OKINAWA`
- `UNKNOWN`

### workType

- `REMOTE`
- `ONSITE`
- `HYBRID`
- `UNKNOWN`

### companyType

- `LARGE`
- `MID`
- `SMALL`
- `FOREIGN`
- `UNKNOWN`

## Nullability

- `flexTime`: `boolean | null`
- `logoUrl`: `string | null`
- `description`: `string | null`
- `employeesGroup`: `integer | null`
- `employeesEntity`: `integer | null`
- `tags`: `[]` 가능
- `ceo`: `string | null`
- `establishedDate`: `YYYY-MM-DD | null`
- `revenue`: `int64 | null`
- `website`: `string | null`
- `benefitDetail`: `{}` 가능
- `philosophy`: 4개 고정 키 필수, 각 값은 `[]` 가능
- `companySourceUrls`: `{}` 가능
- `companyRating`: `number | null`
- `ratingSource`: `string | null`
- `searchKeywords`: `[]` 가능

결측값 보충 규칙:

- 설명문으로 결측값을 메우지 않는다.
- `공식 사이트에 기재 없음`, `정보 없음`, `N/A` 같은 문자열 금지
- null 허용 필드는 반드시 `null`을 우선 사용
- null 비허용 문자열 필드는 정보가 없으면 `""`
- 단 `address` 는 모델이 이미 알고 있는 정보로 보완을 허용하고, 그래도 모르면 `""`

## companySourceUrls 키

최종 payload에서는 아래 한국어 키만 사용한다.

- `홈`
- `회사개요`
- `채용`
- `모집요강·복리후생`
- `기업이념`
- `IR`
- `기타`

OpenWork URL은 값에 넣지 않는다.

## 번역 규칙

최종 payload에서 사용자에게 보여줄 텍스트는 한국어여야 한다.

한국어 번역 대상:

- `name`
- `ceo`
- `description`
- `address`
- `benefitDetail`
- `philosophy`
- `tags`
- `companySourceUrls` 의 한국어 키

번역 금지:

- `slug`
- `industry`
- `location`
- `workType`
- `companyType`
- `flexTime`
- `logoUrl`
- `employeesGroup`
- `employeesEntity`
- `establishedDate`
- `revenue`
- `website`
- `companyRating`
- `ratingSource`
- `searchKeywords`
- `publishStatus`

추가 규칙:

- 최종 payload에서 사용자에게 보여줄 텍스트에는 일본어가 남으면 안 된다.
- `searchKeywords` 는 번역으로 새 값을 만들지 않는다.
- `searchKeywords` 는 회사명 변형만 유지하고, 서비스명이나 제품명은 넣지 않는다.
- `logoUrl` 는 `https://img.logo.dev/{domain}` 형식을 사용하고 `www.` 는 제거한다.

## 제출 규칙

- 최종 제출은 `POST /api/dev/companies`
- `publishStatus` 는 반드시 `DRAFT`
