# 결함 수정 후 PUBLISH 사례

## 입력 상태

```json
{
  "jobId": 1202,
  "companySlug": "paypay",
  "title": "【A-003】데이터베이스 스페셜리스트",
  "position": "BACKEND",
  "locations": [],
  "experienceLevel": "MID_CAREER",
  "workType": "UNKNOWN",
  "joinDate": "수시 채용",
  "overview": "PayPayのデータベース基盤チームで、大規模RDBおよびNoSQLの設計・運用を担当します。",
  "tasks": [
    "대규모 데이터베이스 설계 및 운용",
    "쿼리 성능 튜닝"
  ],
  "selectionProcess": "서류 전형 → 면접 (복수 회) → 최종 합격",
  "jobSourceUrl": "https://about.paypay.ne.jp/career/positions/db-specialist",
  "salaryMin": null,
  "salaryMax": null,
  "publishStatus": "DRAFT"
}
```

## 검증 결과

| 항목 | 결과 | 문제 |
|------|------|------|
| jobSourceUrl 접근 | 200, 공고 상세 확인 | |
| title | prefix 잔존 | `【A-003】` 제거 필요 |
| position | 원문은 DB 전문가 | `BACKEND` → `DATA_ENGINEER` |
| locations | 빈 배열 | 원문 勤務地: 東京都港区 → `[TOKYO]` |
| workType | 원문에 "フルリモート可" 기재 | `UNKNOWN` → `REMOTE` |
| overview | 일본어 미번역 | 한국어로 번역 필요 |
| selectionProcess | "복수 회" 사용 | "2~3회" 로 수정 |
| salaryMin | null | OpenWork 기준 PayPay DB 전문가 추정: 8,000,000 |

## 수정 내역

```
PUT /api/dev/jobs/1202
{
  "title": "데이터베이스 스페셜리스트",
  "position": "DATA_ENGINEER",
  "locations": ["TOKYO"],
  "workType": "REMOTE",
  "overview": "PayPay의 데이터베이스 기반 팀에서 대규모 RDB 및 NoSQL의 설계·운용을 담당합니다.",
  "selectionProcess": "서류 전형 → 면접 (2~3회) → 최종 합격",
  "salaryMin": 8000000
}
```

## 판정

**FIX+PUBLISH**

액션:
1. `PUT /api/dev/jobs/1202` (위 수정 사항)
2. `PUT /api/dev/jobs/1202/publish`

보고:
```
| 1202 | PayPay | 데이터베이스 스페셜리스트 | FIX+PUB | title prefix 제거, position BACKEND→DATA_ENGINEER, locations []→[TOKYO], workType UNKNOWN→REMOTE, overview 번역, selectionProcess 표현 수정, salaryMin 추가 |
```
