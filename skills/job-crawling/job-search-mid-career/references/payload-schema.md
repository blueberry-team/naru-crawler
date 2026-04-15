# Payload 스키마

API 제출 시 이 스키마를 출력 형식의 기준으로 사용한다.

```json
{
  "companySlug": "string",
  "title": "string",
  "position": "BACKEND | FRONTEND | FULLSTACK | IOS | ANDROID | INFRA | CLOUD | DEVOPS | SECURITY | QA_TEST | DATA_ENGINEER | DATA_SCIENTIST | ML_ENGINEER | PM_PO | SERVICE_PLANNING | BUSINESS_STRATEGY | B2B_SALES | RECRUITING | ACCOUNTING | ...",
  "locations": ["TOKYO", "OSAKA"],
  "experienceLevel": "MID_CAREER",
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
- `position` 은 백엔드 `Position` enum 중 하나여야 한다
- 신입 전용 `GRADUATE_*` enum 은 사용하지 않는다
- `locations` 는 빈 배열이면 안 된다
- `experienceLevel` 은 반드시 `MID_CAREER`
- `joinDate` 는 null 또는 빈 문자열이면 안 된다
- `workType` 은 `REMOTE`, `ONSITE`, `HYBRID`, `UNKNOWN` 중 하나여야 한다
- `publishStatus` 는 반드시 `DRAFT`

정확한 enum 목록은 [`enums.md`](./enums.md) 를 기준으로 본다.

## key 제약

- `camelCase` 사용
- extra key 추가 금지
- `selectionProcess` 는 `null` 가능
- `overview` 는 `null` 가능
- `tasks` 는 `[]` 가능
- `techStack` 는 `[]` 가능
- `benefitDetail` 은 `{}` 가능
- `targetCandidate` 내부 각 배열도 `[]` 가능

## position 초안 규칙

- 가능한 한 백엔드의 세부 enum 에 직접 매핑한다.
- 정확한 세부 enum 이 없으면 가장 가까운 카테고리의 `*_OTHER` 를 사용한다.
- `GRADUATE_*` enum 은 금지한다.
- enum 이름을 추측하지 않는다. 허용값은 [`enums.md`](./enums.md) 에 있는 값만 사용한다.

예시:

- `バックエンドエンジニア` → `BACKEND`
- `フロントエンドエンジニア` → `FRONTEND`
- `インフラエンジニア` → `INFRA`
- `クラウドエンジニア` → `CLOUD`
- `データエンジニア` → `DATA_ENGINEER`
- `データサイエンティスト` → `DATA_SCIENTIST`
- `プロダクトマネージャー` → `PM_PO`
- `サービス企画` → `SERVICE_PLANNING`
- `法人営業` → `B2B_SALES`
- `採用担当` → `RECRUITING`
- `経理` → `ACCOUNTING`

## joinDate 초안 규칙

- `joinDate` 는 필수 문자열이다.
- 명시된 입사 가능 시기만 저장한다.
- 예시:
  - `2026年7月` → `2026년 7월`
  - `入社時期応相談` → `입사 시기 협의`
  - `できるだけ早く` → `가능한 한 빠르게`
  - `未定` → `미정`
