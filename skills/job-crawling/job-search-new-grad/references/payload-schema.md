# Payload 스키마

API 제출 시 이 스키마를 출력 형식의 기준으로 사용한다.

```json
{
  "companySlug": "string",
  "title": "string",
  "position": "GRADUATE_GENERAL | GRADUATE_ENGINEER | GRADUATE_TECHNICAL | GRADUATE_DESIGN | GRADUATE_SPECIALIST | GRADUATE_OTHER",
  "locations": ["TOKYO", "OSAKA"],
  "experienceLevel": "NEW_GRAD",
  "joinDate": "string",
  "workType": "REMOTE | ONSITE | HYBRID | UNKNOWN",
  "salaryMin": 5000000,
  "salaryMax": 7000000,
  "deadline": "2027-03-31",
  "overview": "string | null",
  "tasks": ["string"],
  "techStack": ["string"],
  "benefitDetail": {
    "복리후생": ["item 1", "item 2"],
    "주거": ["item 1"]
  },
  "targetAudience": "string",
  "selectionProcess": "string | null",
  "targetCandidate": {
    "mustHave": [],
    "niceToHave": [],
    "idealCandidate": [],
    "selectionPoints": [],
    "workingConditions": [],
    "notes": []
  },
  "jobSourceUrl": "string",
  "publishStatus": "DRAFT"
}
```

## 필수 검증 항목

- `companySlug` 가 있어야 한다
- `title` 은 비어 있으면 안 된다
- `position` 은 6개 graduate enum 중 하나여야 한다
- `locations` 는 빈 배열이면 안 된다
- `experienceLevel` 은 반드시 `NEW_GRAD`
- `joinDate` 는 null 또는 빈 문자열이면 안 된다
- `workType` 은 `REMOTE`, `ONSITE`, `HYBRID`, `UNKNOWN` 중 하나여야 한다
- `publishStatus` 는 반드시 `DRAFT`

## key 제약

- `camelCase` 사용
- extra key 추가 금지
- `selectionProcess` 는 `null` 가능
- `overview` 는 `null` 가능
- `tasks` 는 `[]` 가능
- `techStack` 는 `[]` 가능
- `benefitDetail` 은 `{}` 가능
- `targetCandidate` 내부 각 배열도 `[]` 가능
