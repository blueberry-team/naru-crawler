---
name: job-search-new-grad
description: Playwright MCP로 일본 신입 채용 페이지를 크롤링하고, 명시된 정보만 추출한 뒤, 사용자 노출 텍스트를 일본어에서 한국어로 번역하고, 공고별로 NARU jobs API에 DRAFT payload를 제출한다.
disable-model-invocation: true
argument-hint: "<url> <companySlug>"
---

# job-search-new-grad

이 스킬은 일본 신입 채용 페이지를 크롤링해서 NARU에 DRAFT 공고로 적재할 때 사용한다.

이 스킬은 task형 워크플로우다. 시작 URL과 이미 존재하는 `companySlug`를 넘겨 직접 호출하는 것을 전제로 한다.

예시:

```text
/job-search-new-grad "https://example.com/recruit/newgrad" hitachi
```

실제 추출 작업을 시작하기 전에 아래 파일을 순서대로 읽는다.

1. [`references/api-flow.md`](./references/api-flow.md)
2. [`references/payload-schema.md`](./references/payload-schema.md)
3. [`references/translation-glossary.md`](./references/translation-glossary.md)
4. [`rules/01-navigation.md`](./rules/01-navigation.md)
5. [`rules/02-classification.md`](./rules/02-classification.md)
6. [`rules/03-join-date.md`](./rules/03-join-date.md)
7. [`rules/04-salary.md`](./rules/04-salary.md)
8. [`rules/05-target-audience.md`](./rules/05-target-audience.md)
9. [`rules/06-selection-process.md`](./rules/06-selection-process.md)
10. [`rules/07-content-fields.md`](./rules/07-content-fields.md)
11. [`rules/08-target-candidate.md`](./rules/08-target-candidate.md)

출력 형식이 흔들리지 않도록 필요하면 예시 파일도 읽는다.

- [`examples/good-output.md`](./examples/good-output.md)
- [`examples/edge-cases.md`](./examples/edge-cases.md)
- [`examples/bad-output.md`](./examples/bad-output.md)
- [`references/checklist.md`](./references/checklist.md)

## 실행 규칙

- Playwright MCP를 사용해 실제 사이트를 탐색한다.
- `NEW_GRAD` 공고만 수집한다.
- 각 공고는 반드시 상세 페이지까지 들어간다. 목록 페이지에서 끝내면 안 된다.
- `1공고 = 1 payload = 1 POST` 로 처리한다.
- bundle JSON 파일은 저장하지 않는다.
- 없는 사실을 만들어내지 않는다.
- 사용자 노출 텍스트만 한국어로 번역한다.
- enum, 날짜, 숫자, URL, slug 는 그대로 둔다.
- 모든 공고는 `publishStatus: "DRAFT"` 로 제출한다.

## 필수 워크플로우

1. 시작 URL을 Playwright MCP로 연다.
2. 신입 채용 동선을 따라간다. 외부 ATS 페이지라도 상세 공고가 있으면 계속 진행한다.
3. 페이지 안의 대상 트랙을 모두 찾는다.
4. 각 상세 페이지에 들어가 일본어 원문 사실을 추출한다.
5. rule 파일 기준으로 각 필드를 정규화한다.
6. glossary를 적용해 번역이 필요한 필드의 일본어를 한국어로 번역한다.
7. [`references/payload-schema.md`](./references/payload-schema.md)와 [`references/checklist.md`](./references/checklist.md)를 기준으로 payload를 검증한다.
8. 공고별로 `POST /api/dev/jobs` 를 호출한다.
9. 공고별 성공 / 실패를 보고한다.

## 최종 응답 요구사항

처리한 각 공고마다 아래를 보고한다.

- title
- jobSourceUrl
- POST 성공 여부
- 실패했다면 실패 원인

마지막에 아래 합계를 함께 보고한다.

- 시도 건수
- 성공 건수
- 실패 건수
