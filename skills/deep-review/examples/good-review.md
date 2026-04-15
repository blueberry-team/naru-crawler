# 정상 리뷰 → PUBLISH 사례

## 입력 상태

```json
{
  "jobId": 1201,
  "companySlug": "freee",
  "title": "백엔드 엔지니어 (결제 플랫폼)",
  "position": "BACKEND",
  "locations": ["TOKYO"],
  "experienceLevel": "MID_CAREER",
  "workType": "HYBRID",
  "joinDate": "수시 채용",
  "overview": "freee의 결제 플랫폼 팀에서 마이크로서비스 기반 결제 시스템의 설계·개발·운영을 담당합니다. 대규모 트랜잭션 처리와 높은 가용성이 요구되는 환경에서 기술적 도전을 경험할 수 있습니다.",
  "tasks": [
    "결제 시스템 API 설계 및 개발",
    "마이크로서비스 아키텍처 설계 및 운영",
    "대규모 트랜잭션 처리 성능 최적화",
    "결제 관련 외부 서비스 연동"
  ],
  "targetCandidate": {
    "mustHave": ["웹 애플리케이션 개발 경력 3년 이상", "Java 또는 Go 실무 경험"],
    "niceToHave": ["결제/금융 도메인 경험", "마이크로서비스 설계 경험"],
    "idealCandidate": ["기술적 도전을 즐기는 분", "팀과 함께 성장하고 싶은 분"],
    "workingConditions": ["도쿄 본사 (시부야)", "주 3일 출근 + 2일 리모트"],
    "selectionPoints": ["기술 과제 + 면접에서 설계 능력 평가"],
    "notes": ["비자 스폰서 가능"]
  },
  "benefitDetail": {
    "복리후생": ["교통비 전액 지급", "자기개발비 연 10만엔"],
    "근무환경": ["자유 복장", "유연 근무제"]
  },
  "selectionProcess": "서류 전형 → 기술 과제 → 면접 (2~3회) → 최종 합격",
  "jobSourceUrl": "https://jobs.freee.co.jp/recruitments/001",
  "salaryMin": 6000000,
  "salaryMax": 10000000,
  "deadline": null,
  "techStack": ["Java", "Go", "Kubernetes", "AWS"],
  "targetAudience": "결제/핀테크 분야에 관심 있는 백엔드 엔지니어",
  "recruitmentType": "ROLLING",
  "publishStatus": "DRAFT"
}
```

## 검증 결과

| 항목 | 결과 |
|------|------|
| jobSourceUrl 접근 | 200, 공고 상세 페이지 확인 |
| title 일치 | 원문 "バックエンドエンジニア（決済プラットフォーム）" 과 의미 일치 |
| 채용 현행성 | 종료 키워드 없음, deadline null (수시 채용) |
| enum 정합성 | position=BACKEND, locations=[TOKYO], experienceLevel=MID_CAREER, workType=HYBRID 모두 유효 |
| 분류 정확도 | 원문과 일치 |
| 필수 필드 | 모두 존재 |
| 텍스트 품질 | HTML 잔여물 없음, 일본어 잔존 없음, 자연스러운 한국어 |
| 중복 | PUBLISHED 에 동일 URL/title 없음 |

## 판정

**PUBLISH**

액션: `PUT /api/dev/jobs/1201/publish`
