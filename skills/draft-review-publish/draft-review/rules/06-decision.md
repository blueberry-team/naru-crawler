# 최종 판정 + 액션

01~05 규칙의 검증 결과를 종합하여 공고별로 판정을 내린다.

## 판정 분류

### PUBLISH

모든 검증을 통과한 공고.

액션:
1. `PUT /api/dev/jobs/{id}/publish`
2. 결과 테이블에 "PUBLISH" 기록

### FIX+PUBLISH

경미한 결함만 있어서 수정 후 발행 가능한 공고.

액션:
1. `PUT /api/dev/jobs/{id}` 로 결함 필드 수정 (변경 필드만 전송)
2. 수정 완료 확인 (204 응답)
3. `PUT /api/dev/jobs/{id}/publish`
4. 결과 테이블에 "FIX+PUB" 기록 + 수정 내역

FIX 가능한 항목:
- `position`, `locations`, `experienceLevel`, `workType` 재분류
- `recruitmentType` 설정
- `overview`, `tasks`, `selectionProcess` 텍스트 수정
- `targetCandidate`, `benefitDetail` 구조 정리, 중복 제거
- `targetAudience` 수정
- `title` prefix 제거
- `salaryMin`/`salaryMax` 공개 데이터 기반 추가 또는 이상치 수정
- `deadline` 갱신 (원본에서 새 마감일 확인된 경우)
- `techStack` 오탐 항목 제거
- HTML 태그 잔여물 제거
- 일본어 미번역 텍스트 번역
- 어색한 표현 수정

### HOLD

심각한 문제가 있어서 자동 수정이 불가능하거나 위험한 공고. DRAFT 상태를 유지하고 사용자에게 보고한다.

액션:
1. 수정하지 않는다
2. DRAFT 상태를 유지한다
3. 결과 테이블에 "HOLD" 기록 + 사유

HOLD 사유 목록:

| 사유 | 보고 메시지 |
|------|------------|
| jobSourceUrl 빈 값 | "jobSourceUrl이 비어있습니다" |
| jobSourceUrl 404/410/5xx | "원본 URL 접근 불가 ({상태코드})" |
| jobSourceUrl 이 목록/메인 페이지 | "jobSourceUrl이 공고 상세가 아닌 채용 사이트 페이지입니다" |
| jobSourceUrl 이 지원서 페이지 | "jobSourceUrl이 지원서 페이지입니다. 공고 상세 URL로 수정 필요" |
| jobSourceUrl 페이지와 title 불일치 | "원본 페이지의 공고와 적재된 title이 일치하지 않습니다" |
| 리다이렉트 후 메인으로 이동 | "리다이렉트 후 채용 메인으로 이동, 공고 만료 의심" |
| 로그인 필요 | "jobSourceUrl 접근에 로그인이 필요합니다" |
| WAF 차단 (재시도 후에도) | "WAF 차단으로 원본 페이지 접근 불가" |
| 채용 종료 키워드 발견 | "원본 페이지에서 채용 종료 키워드 발견: {키워드}" |
| 원본 목록에서 제거됨 | "원본 채용 페이지 목록에서 해당 공고가 제거되었습니다" |
| companySlug DB에 없음 | "companySlug '{slug}'가 DB에 존재하지 않습니다" |
| PUBLISHED 에 동일 jobSourceUrl | "이미 PUBLISHED 된 동일 공고 존재 (ID={id})" |
| 동일 회사 유사 title PUBLISHED | "동일 회사에 유사한 제목의 PUBLISHED 공고 존재 (ID={id})" |
| DRAFT 간 jobSourceUrl 중복 | "동일 jobSourceUrl 의 DRAFT 가 복수 존재 (ID={ids})" |
| title 5자 미만 또는 의미 없음 | "title이 부실합니다" |
| publishStatus 가 DRAFT 가 아님 | "publishStatus 이상: {값}" |

## 출력 형식

```
#N회차 리뷰 결과

| jobId | 회사 | 제목 | 판정 | 비고 |
|-------|------|------|------|------|
| 1153  | GMO  | PHP 엔지니어 | PUBLISH | |
| 1154  | PayPay | DB 스페셜리스트 | FIX+PUB | locations: [] → [OSAKA] |
| 1155  | SEGA | 시스템 프로그래머 | HOLD | jobSourceUrl 404 |

수정 내역:
- 1154: PUT locations=[OSAKA], position BACKEND → DATA_ENGINEER

HOLD 사유:
- 1155: 원본 URL 응답 404, 채용 종료 가능성

합계: 리뷰 3건 / PUBLISH 1건 / FIX+PUB 1건 / HOLD 1건
```

## 절대 규칙

- HOLD 판정 공고는 절대 PUBLISH 하지 않는다.
- HOLD 판정 공고를 수정하지 않는다.
- FIX 시 DELETE 후 재생성하지 않는다. PUT 부분 수정만 사용한다.
- 판정이 모호할 때는 HOLD 로 처리한다. 안전한 쪽으로 판단한다.
- 사용자가 HOLD 공고에 대해 별도 지시를 내릴 때까지 대기한다.
