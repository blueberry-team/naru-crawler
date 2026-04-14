---
name: company-search
description: Playwright MCP로 일본 기업 공식 사이트를 탐색해 Company 엔티티에 맞는 회사 정보를 정리하고, 사용자에게 보여줄 텍스트를 한국어로 번역한 뒤, NARU companies API에 DRAFT로 저장한다. 회사 개요, 복리후생, 기업 이념, 평점, 검색 키워드, 출처 URL 수집이 필요할 때 사용한다.
disable-model-invocation: true
argument-hint: "<url>"
---

# company-search

이 스킬은 일본 기업 공식 사이트를 수집해서 회사 정보 DRAFT를 적재할 때 사용한다.

입력은 시작 URL 하나다.

```text
/company-search "https://example.com/recruit/"
```

실제 추출을 시작하기 전에 아래 파일을 순서대로 읽는다.

1. [`references/api-flow.md`](./references/api-flow.md)
2. [`references/payload-schema.md`](./references/payload-schema.md)
3. [`references/translation-generation.md`](./references/translation-generation.md)
4. [`references/checklist.md`](./references/checklist.md)
5. [`rules/01-navigation.md`](./rules/01-navigation.md)
6. [`rules/02-company-overview.md`](./rules/02-company-overview.md)
7. [`rules/03-benefits-worktype.md`](./rules/03-benefits-worktype.md)
8. [`rules/04-philosophy.md`](./rules/04-philosophy.md)
9. [`rules/05-company-rating.md`](./rules/05-company-rating.md)
10. [`rules/06-source-urls.md`](./rules/06-source-urls.md)
11. [`rules/07-tags-keywords-description.md`](./rules/07-tags-keywords-description.md)

필요하면 아래 예시도 읽는다.

- [`examples/good-output.md`](./examples/good-output.md)

## 실행 규칙

- Playwright MCP를 사용해 실제 사이트를 탐색한다.
- 외부 OCR 라이브러리를 설치하지 않는다.
- 이미지 텍스트는 `screenshot` 와 Vision으로 읽는다.
- 공식 사이트를 가장 우선하는 기준으로 본다.
- EDINET은 공식 사이트에 정확한 수치가 없을 때만 보조 소스로 사용한다.
- OpenWork는 평점 또는 공식 정보 완전 부재 시에만 제한적으로 사용한다.
- 추측으로 값을 채우지 않는다.
- 결측값은 `null`, `[]`, `{}`, `""` 규칙에 맞게 처리한다.
- 최종 결과는 회사 1건당 `1 payload = 1 POST` 다.
- bundle JSON 파일은 저장하지 않는다.

## 필수 작업 순서

1. 시작 URL을 Playwright MCP로 연다.
2. 회사 개요, 채용, 복리후생, 기업 이념, IR 관련 페이지를 탐색한다.
3. 공식 사이트에서 회사 기본 정보와 채용/복지 개요를 추출한다.
4. 기업 이념이 이미지일 경우 스크린샷과 Vision으로 읽는다.
5. 필요할 때만 EDINET과 OpenWork를 보조적으로 사용한다.
6. 규칙 문서를 기준으로 각 필드를 형식에 맞게 정리한다.
7. 사용자에게 보여줄 텍스트를 한국어로 번역해 최종 payload를 만든다.
8. [`references/payload-schema.md`](./references/payload-schema.md)와 [`references/checklist.md`](./references/checklist.md)를 기준으로 검증한다.
9. `POST /api/dev/companies` 로 `publishStatus: "DRAFT"` 제출한다.

## 최종 응답에는 아래 내용을 포함한다

- 회사명
- slug
- 제출에 사용한 payload 요약
- POST 성공 여부
- 사용한 주요 출처 페이지
- 누락되었거나 `null` 처리한 핵심 필드
