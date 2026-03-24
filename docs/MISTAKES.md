# ⚠️ 실수 기록 (Mistakes Log)

AI가 저지른 실수와 개선 사항을 기록합니다.

---

## 2026-03-24

### MISTAKE-001: 확인 전 테스트 데이터 삭제
- **상황**: DRAFT 테스트 공고(ID 464) 생성 후 정우가 어드민에서 확인하기 전에 바로 삭제
- **원인**: "테스트 데이터니까 삭제할게요"라고 독단적으로 판단
- **정우 반응**: "왜 바로 삭제하는데;; 내가 확인을 해야지"
- **교훈**: 사용자가 확인/승인하기 전에는 데이터를 삭제하거나 변경하지 말 것
- **개선**: 이후 재생성(ID 465) 후 삭제하지 않고 보존

---

### MISTAKE-002: fetch_job_detail이 잘못된 job 데이터 반환
- **상황**: 상세 API(`?job_code1=N`) 호출 시 응답 JSON에서 "description" 있는 첫 dict 반환 → 항상 job 15 덮어씌움
- **원인**: `_find_job_detail`이 job_id 일치 검사 없이 description 있는 첫 항목 반환
- **증상**: limit=5로 실행 시 5개 공고가 모두 같은 job (ID=15) 표시
- **해결**: 상세 API 호출 자체를 제거하고 목록 API `job_items[]` 파라미터로 통합

### MISTAKE-003: 위치 오탐 (東京都 → KYOTO)
- **상황**: "東京都"가 "京都" 키워드와 substring 매칭 → TOKYO + KYOTO 동시 반환
- **원인**: 단순 `keyword in text` 매칭, 더 긴 지명 우선 처리 미흡
- **해결**: "京都" → "京都府/京都市/京都駅/京都勤務"로 변경 (전체 지명 명시)

### MISTAKE-004: HTML ruby 태그 기술스택 오탐
- **상황**: description HTML의 `<ruby>` 태그(일본어 후리가나)가 plain text 변환 후 "ruby" 남아 Ruby(언어)로 오탐
- **해결**: `_clean_html()` 에서 `<ruby>`, `<rt>`, `<rp>` 태그 먼저 제거

---

### MISTAKE-005: 기업 slug 사전 확인 없이 새 회사 생성 → DB 오염
- **상황**: `hitachi` slug가 이미 ID=22로 등록돼 있었는데 확인 없이 새 회사(ID=144~147) 생성
- **결과**: 동일 slug 중복, JPA 캐시 오염, `/api/dev/companies/names` 500 에러 유발
- **규칙**: 공고 적재 전 반드시 `GET /api/companies?size=200` 으로 기존 slug 확인

### MISTAKE-006: `status` vs `publishStatus` 필드명 혼동 → 전체 PUBLISHED 자동 등록
- **상황**: payload에 `"status": "DRAFT"` 전송 → JobCreateRequest에 없는 필드 → 무시됨
- **결과**: 기본값 `PublishStatus.PUBLISHED` 적용, 20개 공고 즉시 공개
- **규칙**: 반드시 `"publishStatus": "DRAFT"` 사용

### MISTAKE-007: `entry.phtml` (지원서 페이지)를 jobSourceUrl로 사용
- **상황**: `entry.phtml?job_code1=15` → 클릭 시 지원서 페이지로 직행
- **해결**: `job.phtml?job_code=15` 가 공고 상세 페이지 (파라미터도 `job_code1` → `job_code`)

### MISTAKE-008: 제목에 【번호】 prefix 그대로 적재
- **상황**: `【15】多種大量なデータ...` 를 그대로 제목으로 사용
- **규칙**: `re.sub(r'^【\d+】\s*', '', title)` 으로 번호 제거 후 한국어 번역 적용

### MISTAKE-009: salary null 방치 (조사 없이 포기)
- **상황**: 히타치 원문에 "협의"라고만 써있어서 null로 적재
- **규칙**: OpenWork, 취업 에이전시 등 공개 데이터로 보수적 추정. 확신 없으면 min만 넣고 max는 null

---

## 앞으로 지켜야 할 원칙

1. **데이터 생성 후 삭제는 명시적 지시 후에만**
2. **품질 실패 공고도 로그에 남길 것** (silent fail 금지)
3. **DRY RUN 먼저, 실제 적재는 확인 후에**
4. **API 토큰 등 민감 정보는 config.py에만, 문서에는 마스킹**
