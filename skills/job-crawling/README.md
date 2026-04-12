---
name: job-crawling
description: Playwright MCP로 일본 채용 페이지를 수집하고, 공고 유형별 skill에서 필드 정규화와 번역을 수행한 뒤, 공고별로 NARU jobs API에 DRAFT payload를 적재한다.
---

# job-crawling

이 디렉터리는 일본 채용 공고 수집용 skill 문서를 관리한다.

현재 기준의 실제 운영 흐름은 아래와 같다.

- Playwright MCP로 실제 채용 사이트를 탐색한다.
- 공고 유형에 맞는 skill에서 상세 공고를 수집한다.
- 사용자 노출 텍스트를 일본어에서 한국어로 번역한다.
- payload를 검증한다.
- 공고별로 `POST /api/dev/jobs` 를 호출해 `publishStatus: "DRAFT"` 로 저장한다.

## 현재 기준 skill 구조

실제 실행은 분리된 Claude skill 구조를 기준으로 본다.

## 기본 원칙

- `Playwright MCP` 를 기본 브라우징 도구로 사용한다.
- `job-crawling` 아래에서는 공고 유형별 skill을 분리한다.
- 예: `new_grad`, `mid`
- 외부 채용 시스템으로 넘어가더라도 상세 공고가 있으면 계속 진행한다.
- 목록 페이지에 여러 트랙이 있으면 모두 수집한다.
- 한 페이지 안의 앵커 섹션도 공고 단위로 본다.
- `1공고 = 1 payload = 1 POST` 로 처리한다.
- bundle JSON 파일은 저장하지 않는다.
- 명시되지 않은 사실은 추측하지 않는다.
- `publishStatus` 는 항상 `DRAFT` 다.

## 스킬 구조

각 공고 유형은 분리된 Claude skill 디렉터리로 관리한다.

현재 구현된 예시는 아래 경로다.

- 메인 엔트리: [SKILL.md](/naru-crawler/skills/job-crawling/job-search-new-grad/SKILL.md)
- 규칙: [/naru-crawler/skills/job-crawling/job-search-new-grad/rules](/naru-crawler/skills/job-crawling/job-search-new-grad/rules)
- 참고 문서: [/naru-crawler/skills/job-crawling/job-search-new-grad/references](/naru-crawler/skills/job-crawling/job-search-new-grad/references)
- 예시: [/naru-crawler/skills/job-crawling/job-search-new-grad/examples](/naru-crawler/skills/job-crawling/job-search-new-grad/examples)

skill 디렉터리는 같은 레벨에서 유형별로 분리한다.

- `job-search-new-grad`
- `job-search-mid` 또는 이에 준하는 별도 skill

현재 예시 skill의 주요 참고 파일:

- payload 스키마: [payload-schema.md](/naru-crawler/skills/job-crawling/job-search-new-grad/references/payload-schema.md)
- 체크리스트: [checklist.md](/naru-crawler/skills/job-crawling/job-search-new-grad/references/checklist.md)
- 번역 glossary: [translation-glossary.md](/naru-crawler/skills/job-crawling/job-search-new-grad/references/translation-glossary.md)

## 입력

필수 입력:

- 시작 URL
- `companySlug`

호출 형식은 skill마다 다르지만, 보통 아래 두 값을 받는다.

현재 구현된 예시 skill 호출:

```text
/job-search-new-grad "https://www.softbank.jp/recruit/graduate/" softbank
```

한국어로 추가 조건을 붙여도 된다.

```text
/job-search-new-grad "https://www.softbank.jp/recruit/graduate/" softbank

API 호출은 하지 말고,
찾은 공고 수와 각 공고의 title, jobSourceUrl만 보여줘.
```

## 추천 테스트 순서

아래 순서는 공고 유형과 무관하게 공통으로 적용한다.

### 1. 수집 테스트

목적:

- 대상 채용 페이지 진입
- 외부 채용 시스템 이동 처리
- 공고 개수 인식
- 상세 URL 또는 앵커 URL 추출

예시:

```text
/job-search-new-grad "https://www.softbank.jp/recruit/graduate/" softbank

API 호출은 하지 말고,
찾은 공고 수와 각 공고의 title, jobSourceUrl만 보여줘.
```

### 2. payload 테스트

목적:

- 필드 정규화 확인
- 일본어 -> 한국어 번역 확인
- schema / checklist 기준 검증 확인

예시:

```text
/job-search-new-grad "https://www.softbank.jp/recruit/graduate/" softbank

API 호출은 하지 말고,
첫 번째 공고 1건만 최종 payload JSON으로 보여줘.
```

### 3. 실제 DRAFT 적재

목적:

- 공고별 `POST /api/dev/jobs` 실행
- 성공 / 실패 보고

예시:

```text
/job-search-new-grad "https://www.softbank.jp/recruit/graduate/" softbank

이 페이지의 대상 공고를 모두 수집하고,
공고별로 1건씩 DRAFT로 저장해줘.
```

## 워크플로우

1. 시작 URL을 Playwright MCP로 연다.
2. 선택한 skill의 규칙에 따라 대상 공고 동선을 찾는다.
3. 외부 채용 시스템으로 이동했더라도 상세 공고가 있으면 계속 진행한다.
4. 공고 목록, 카드, 탭, 페이지 내 앵커 섹션에서 공고 단위를 식별한다.
5. 각 공고 상세에서 원문 사실을 추출한다.
6. 규칙 문서 기준으로 `title`, `position`, `locations`, `joinDate`, `salaryMin`, `salaryMax`, `selectionProcess`, `targetCandidate`, `benefitDetail` 등을 정규화한다.
7. 번역이 필요한 필드만 한국어로 번역한다.
8. [payload-schema.md](/naru-crawler/skills/job-crawling/job-search-new-grad/references/payload-schema.md) 와 [checklist.md](/naru-crawler/skills/job-crawling/job-search-new-grad/references/checklist.md) 기준으로 payload를 검증한다.
9. 적재 단계라면 공고별로 `POST /api/dev/jobs` 를 호출한다.

## payload 핵심 규칙

- `companySlug` 는 기존 회사 slug 를 사용한다.
- `experienceLevel` 은 선택한 skill의 대상 유형에 맞춰 채운다.
- `publishStatus` 는 항상 `DRAFT`
- `workType` 은 `REMOTE | ONSITE | HYBRID | UNKNOWN`
- `locations` 는 빈 배열이면 안 된다.
- `joinDate` 는 null 이면 안 된다.
- `selectionProcess` 는 근거가 없을 때만 `null`
- `benefitDetail` 과 `targetCandidate` 는 서로 중복 저장하지 않는다.

전체 구조는 [payload-schema.md](/naru-crawler/skills/job-crawling/job-search-new-grad/references/payload-schema.md) 를 따른다.

## 탐색 원칙

- 프롬프트 안의 탐색 키워드는 사이트 원문 기준으로 적는다.
- 예: `新卒`, `募集要項`, `選考フロー`, `Graduate`
- 이유는 실제 채용 페이지의 메뉴, 버튼, 섹션명이 일본어 또는 영어로 표시되기 때문이다.
- 즉 이 문자열들은 결과 출력용이 아니라 페이지 탐색용 navigation 규칙이다.

## 번역 원칙

- 최종 결과의 사용자 노출 텍스트는 모두 한국어로 번역한다.
- 최종 결과에는 일본어가 남으면 안 된다.
- enum, 숫자, URL, slug, payload key 는 번역하지 않는다.

## 하지 않는 것

- JSON 파일 번들 저장을 하지 않는다.
- 회사 전체 복지 페이지까지 불필요하게 확장 수집하지 않는다.
- 일반적인 채용 절차를 상상해서 `selectionProcess` 를 보강하지 않는다.
- 공고에 없는 정보를 추측으로 채우지 않는다.

## 관련 문서

- 현재 예시 skill: [SKILL.md](/naru-crawler/skills/job-crawling/job-search-new-grad/SKILL.md)
