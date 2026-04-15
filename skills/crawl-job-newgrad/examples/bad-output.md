# 나쁜 출력 예시

아래 예시는 “이렇게 하면 안 된다”를 보여주기 위한 샘플이다.

## 예시 1: 여러 공고를 한 배열로 묶어 저장

```json
[
  {
    "companySlug": "hitachi",
    "title": "2027年度 エンジニア職コース 本選考"
  },
  {
    "companySlug": "hitachi",
    "title": "2027年度 ビジネス職コース 本選考"
  }
]
```

문제:

- `1공고 = 1payload = 1POST` 규칙 위반
- 배열 payload 사용 금지

## 예시 2: 번역 금지 필드를 번역함

```json
{
  "companySlug": "히타치",
  "position": "신입 엔지니어",
  "locations": ["도쿄"],
  "experienceLevel": "신입",
  "workType": "하이브리드"
}
```

문제:

- `companySlug` 번역 금지
- `position` enum 훼손
- `locations` enum 훼손
- `experienceLevel` enum 훼손
- `workType` enum 훼손

## 예시 3: title 을 기능명으로 저장

```json
{
  "title": "募集要項"
}
```

문제:

- 기능명만 저장함
- 실제 직종명 / 코스명 아님

## 예시 4: 지원 폼 URL을 jobSourceUrl 로 사용

```json
{
  "jobSourceUrl": "https://example.com/entry/form"
}
```

문제:

- 상세 공고 URL이 아님
- 지원 폼 URL 사용 금지

## 예시 5: 근거 없이 workType 추측

```json
{
  "workType": "ONSITE"
}
```

문제:

- 사무실 주소만 보고 출근형으로 추정했을 가능성
- 명시 근거 없으면 `UNKNOWN` 이어야 함

## 예시 6: joinDate 누락

```json
{
  "joinDate": null
}
```

문제:

- `joinDate` null 금지
- 규칙에 따라 `YYYY年4月`, `YYYY年10月`, 또는 `未定` 으로 채워야 함

## 예시 7: salaryMax 를 근거 없이 복사

```json
{
  "salaryMin": 5000000,
  "salaryMax": 5000000
}
```

문제:

- 원문이 단일 연봉 명시가 아닌데 임의로 상한을 복사했을 수 있음
- 상한이 불명확하면 `salaryMax = null`

## 예시 8: 일본어 원문 그대로 적재

```json
{
  "overview": "大規模データ基盤の開発を担当します。",
  "tasks": ["Webアプリケーションを開発する"]
}
```

문제:

- 사용자 노출 텍스트는 한국어로 번역해야 함

## 예시 9: selectionProcess 를 순서 없이 붙여넣음

```json
{
  "selectionProcess": "書類選考、面接、適性検査、内定"
}
```

문제:

- 순서가 명확하지 않음
- 가능하면 `→` 형식으로 복원해야 함

## 예시 10: 근거 없이 상세 조건을 targetAudience 에 넣음

```json
{
  "targetAudience": "2027졸 대상, Java 경험자, 영어 가능자"
}
```

문제:

- `targetAudience` 에는 졸업 시기 / 졸업 연도 / 기졸 가능만 들어가야 함
- 기술, 어학, 상세 자격은 `targetCandidate` 로 보내야 함
