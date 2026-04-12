# API 엔드포인트

이 스킬에서 사용하는 API 엔드포인트를 정리한다.

## 인증

모든 `/api/dev/*` 요청에는 아래 헤더가 필요하다.

```
X-Admin-Token: {NARU_ADMIN_TOKEN}
```

## 조회

| 작업 | 메서드 | 엔드포인트 | 응답 |
|------|--------|-----------|------|
| DRAFT 목록 | GET | `/api/dev/jobs/drafts` | `List<AdminJobResponse>` |
| 단건 조회 (admin) | GET | `/api/dev/jobs/{id}` | `AdminJobResponse` |
| 단건 미리보기 | GET | `/api/dev/jobs/{id}/preview` | `JobDetailResponse` |
| PUBLISHED 목록 | GET | `/api/jobs?size=200` | `PageResponse<JobPreviewResponse>` |
| 회사 목록 | GET | `/api/companies?size=200` | 회사 목록 |

## 수정

| 작업 | 메서드 | 엔드포인트 | 요청 | 응답 |
|------|--------|-----------|------|------|
| 부분 수정 | PUT | `/api/dev/jobs/{id}` | `JobUpdateRequest` (변경 필드만) | 204 |
| DRAFT → PUBLISHED | PUT | `/api/dev/jobs/{id}/publish` | 없음 | 204 |
| PUBLISHED → DRAFT | PUT | `/api/dev/jobs/{id}/unpublish` | 없음 | 204 |
| 마감 표시 | PUT | `/api/dev/jobs/{id}/mark-deadline-passed` | 없음 | 204 |

## AdminJobResponse 필드

enum은 **name** (예: `BACKEND`, `TOKYO`) 으로 반환된다.

| 필드 | 타입 | 필수 | 비고 |
|------|------|------|------|
| `jobId` | Long | O | |
| `companyId` | Long | O | |
| `companySlug` | String | O | |
| `title` | String | O | |
| `position` | String (enum name) | O | Position enum 47개 |
| `locations` | List<String> (enum names) | O | Location enum 49개 |
| `experienceLevel` | String (enum name) | O | NEW_GRAD, MID_CAREER |
| `workType` | String (enum name) | O | REMOTE, ONSITE, HYBRID, UNKNOWN |
| `joinDate` | String | O | |
| `publishStatus` | String (enum name) | O | DRAFT, PUBLISHED |
| `salaryMin` | Integer | - | nullable |
| `salaryMax` | Integer | - | nullable |
| `deadline` | String (YYYY-MM-DD) | - | nullable |
| `techStack` | List<String> | - | nullable |
| `targetAudience` | String | - | nullable |
| `overview` | String | - | nullable |
| `tasks` | List<String> | - | nullable |
| `targetCandidate` | Map<String, List<String>> | - | nullable |
| `benefitDetail` | Map<String, List<String>> | - | nullable |
| `selectionProcess` | String | - | nullable |
| `jobSourceUrl` | String | - | nullable |
| `recruitmentType` | String (enum name) | - | nullable |
| `isDeadlinePassed` | Boolean | - | nullable |

## JobUpdateRequest 필드

모든 필드가 optional 이다. 전달한 필드만 업데이트되고 나머지는 유지된다.

필드 목록은 AdminJobResponse 와 동일하다. `jobId`, `companyId`, `createdAt`, `updatedAt` 은 제외.

## 절대 규칙

- DELETE 는 이 스킬에서 사용하지 않는다.
- PUT 으로 부분 수정만 한다.
- DELETE 후 재생성을 하지 않는다.
- 토큰을 로그나 출력에 노출하지 않는다.
