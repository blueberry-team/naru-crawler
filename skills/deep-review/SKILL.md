---
name: deep-review
description: 나루 백엔드의 DRAFT/PUBLISHED 공고를 Playwright MCP로 원본 페이지를 직접 확인하여, 25개 평가 기준으로 Deep Review를 수행하고, 결함 수정 또는 PUBLISH 또는 HOLD 판정을 내린다.
disable-model-invocation: true
argument-hint: "개수=5 | jobIds=1153,1154 | company=hitachi 개수=10"
---

# deep-review

이 스킬은 공고를 원본 채용 페이지와 대조하여 25개 기준으로 Deep Review할 때 사용한다.

이 스킬은 task형 워크플로우다. 샘플링 조건을 넘겨 직접 호출하는 것을 전제로 한다.

예시:

```text
/draft-review 개수=5
/draft-review jobIds=1153,1154,1155
/draft-review company=hitachi 개수=10
```

실제 리뷰를 시작하기 전에 아래 파일을 순서대로 읽는다.

1. [`references/api-endpoints.md`](./references/api-endpoints.md)
2. [`references/enums.md`](./references/enums.md)
3. [`references/checklist.md`](./references/checklist.md)
4. [`rules/01-sampling.md`](./rules/01-sampling.md)
5. [`rules/02-url-validation.md`](./rules/02-url-validation.md)
6. [`rules/03-freshness.md`](./rules/03-freshness.md)
7. [`rules/04-quality.md`](./rules/04-quality.md)
8. [`rules/05-duplicate.md`](./rules/05-duplicate.md)
9. [`rules/06-decision.md`](./rules/06-decision.md)

출력 형식이 흔들리지 않도록 필요하면 예시 파일도 읽는다.

- [`examples/good-review.md`](./examples/good-review.md)
- [`examples/fix-and-publish.md`](./examples/fix-and-publish.md)
- [`examples/hold.md`](./examples/hold.md)

## 전제 조건: Playwright MCP 설정

원본 채용 페이지 확인 시 **Playwright MCP를 기본으로 사용**한다.
WebFetch는 사용하지 않는다.

### Playwright MCP 설정 방법

Claude Desktop의 MCP 설정 파일에 추가:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-playwright"]
    }
  }
}
```

설치 확인:
```bash
npx @anthropic-ai/mcp-playwright --version
```

### 왜 Playwright MCP인가

| 방식 | 장점 | 한계 |
|------|------|------|
Deep Review에서 원본 확인은 **정확성이 최우선**이므로 Playwright MCP만 사용한다.

### Playwright MCP 사용 시 주의

- 勤務地, 給与, 仕事内容 등 **개별 공고의 해당 섹션만** 확인
- 회사 전체 정보와 개별 공고 정보를 혼동 금지 ([상세](../../docs/REVIEW_GUIDE.md))
- 페이지 로딩 후 충분히 대기 (SPA 등 동적 렌더링 고려)

## 실행 규칙

- `GET /api/dev/jobs/drafts` 로 DRAFT 목록을 가져온다.
- 각 공고마다 `GET /api/dev/jobs/{id}` 로 전체 필드를 조회한다.
- 각 공고의 `jobSourceUrl` 에 **Playwright MCP로 접근**하여 원본 페이지를 확인한다.
- rules 파일 순서대로 검증을 수행한다.
- 검증 결과에 따라 PUBLISH, FIX+PUBLISH, HOLD 를 판정한다.
- FIX 항목은 `PUT /api/dev/jobs/{id}` 로 즉시 수정한다.
- PUBLISH 판정 공고는 `PUT /api/dev/jobs/{id}/publish` 로 전환한다.
- HOLD 판정 공고는 DRAFT 상태를 유지하고 사용자에게 사유를 보고한다.
- 판정 결과를 수정하거나 추측하지 않는다.

## 필수 워크플로우

1. DRAFT 목록 조회 → 샘플링 규칙에 따라 N건 선택
2. 공고별 전체 필드 조회 (`GET /api/dev/jobs/{id}`)
3. jobSourceUrl 접근 → URL 유효성 검증 (02-url-validation)
4. 원본 페이지 내용으로 채용 현행성 검증 (03-freshness)
5. 전체 필드 품질 검증 — enum 실존, 필수 필드, 텍스트 품질 (04-quality)
6. PUBLISHED 목록과 중복 검증 (05-duplicate)
7. 종합 판정 (06-decision)
8. FIX 대상 → PUT 수정
9. PUBLISH 대상 → PUT publish
10. HOLD 대상 → 사유 기록
11. 결과 보고

## 최종 응답 요구사항

처리한 각 공고마다 아래를 보고한다.

- jobId
- 회사명
- title
- 판정 (PUBLISH / FIX+PUBLISH / HOLD)
- 수정 내역 (FIX인 경우)
- HOLD 사유 (HOLD인 경우)

마지막에 아래 합계를 함께 보고한다.

- 리뷰 건수
- PUBLISH 건수
- FIX+PUBLISH 건수
- HOLD 건수
