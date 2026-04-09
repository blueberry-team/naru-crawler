---
name: job-crawling
description: 기업 채용 사이트에서 채용 공고를 크롤링하여 나루(naru-recruit.com) DB에 DRAFT 상태로 적재한다. 공고 단건 단위 추출·정규화·품질 검증·업로드를 담당한다.
---

# job-crawling — 공고 크롤링 스킬

## 무엇을 하는가

지정한 기업의 채용 페이지에서 **개별 채용 공고**를 수집하여 나루 백엔드 API로 전송, `status: DRAFT` 상태로 적재한다.

- 입력: 회사 식별자(slug) 또는 공고 URL 목록
- 처리: HTML/JSON 파싱 → 직무·근무지·경력 enum 매핑 → 필수 필드 검증
- 출력: 나루 백엔드의 새 DRAFT 공고 (관리자 검토 대기 큐로 적재)

이 스킬은 **공고 단건만 다룬다**. 기업 정보 등록·수정은 [`company-crawling`](../company-crawling/) 스킬을 사용한다.

---

## 전제 조건 (Setup)

이 스킬은 **다양한 사람이 Claude Desktop을 통해 처음 접근해서 실행하는 시나리오**를 가정한다. 따라서 처음 사용자는 아래 셋업을 한 번만 완료해야 한다.

### 1. 저장소 클론
```bash
git clone git@github.com:blueberry-team/naru-crawler.git
cd naru-crawler
```

### 2. Python 환경
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backup/requirements.txt    # 기존 의존성 재사용
```

### 3. 나루 어드민 토큰 등록
나루 백엔드는 `X-Admin-Token` 헤더로 인증한다. 토큰은 어드민에게 별도로 받아 환경변수에 저장한다.

```bash
export NARU_ADMIN_TOKEN="<발급받은_토큰>"
export NARU_API_BASE="https://api.naru-recruit.com"
```

쉘 종료 시 재설정이 귀찮으면 `~/.zshrc` 등에 추가하거나 Claude Desktop의 환경변수 설정 화면에 등록한다.

### 4. Claude Desktop 권한
이 스킬은 `Bash`, `WebFetch`, `Read`, `Write` 도구를 사용한다. Claude Desktop의 권한 모드가 `acceptEdits` 또는 `bypassPermissions`로 설정되어 있어야 자동 실행이 원활하다.

### 5. 첫 실행 점검
```bash
# DRAFT 목록 조회로 토큰·네트워크 정상 여부 확인
curl -s "$NARU_API_BASE/api/dev/jobs/drafts" -H "X-Admin-Token: $NARU_ADMIN_TOKEN" | head -c 200
```
JSON 응답이 돌아오면 셋업 완료.

---

## 사용 방법

Claude Desktop에서 다음과 같이 호출한다:

```
/job-crawling 회사=hitachi 개수=10 dry-run
/job-crawling URL=https://hrmos.co/pages/{company}/jobs/{id}
```

또는 자연어로:

> "naru-crawler로 GMO미디어 채용 페이지에서 백엔드 공고 5개 크롤링해서 드래프트로 올려줘"

### 워크플로우
1. **회사 식별** — 사용자가 지정한 slug 또는 URL에서 도메인 추출
2. **공고 목록 조회** — 회사별 어댑터(`backup/companies/{slug}.py`)로 raw 공고 리스트 가져오기
3. **상세 페이지 파싱** — 각 공고 URL을 fetch하여 제목/개요/자격/근무지 등 추출
4. **enum 매핑** — `backup/rules/*.json` 룰을 적용해 position/location/experienceLevel 결정
5. **품질 검증** — 필수 필드(title 5자+, overview 50자+, tasks 1개+, position/locations/experienceLevel 유효) 통과 확인
6. **DRAFT 적재** — `POST /api/dev/jobs` (`status: "DRAFT"`)로 업로드
7. **결과 보고** — 적재 성공/실패 건수와 jobId 목록을 반환

### 기존 자산 재사용
- 회사별 어댑터: `backup/companies/{slug}.py`
- enum 매핑 룰: `backup/rules/{position,location,experience}_rules.json`
- 모델 정의: `backup/models/job.py`
- API 클라이언트: `backup/api/naru_client.py`
- 검증기: `backup/validators/job_validator.py`

신규 회사를 추가하려면 `backup/companies/` 아래에 `BaseCrawler`를 상속한 모듈을 만들고 `runner.py`의 `CRAWLERS` dict에 등록한다.

---

## 출력 형식

```
✅ {company} 공고 크롤링 결과
- 시도: 10건
- DRAFT 적재 성공: 9건 (jobIds: [1153, 1154, ...])
- 검증 실패: 1건
  - https://...  →  overview 길이 부족 (32자, 최소 50자)

확인 링크: https://www.naru-recruit.com/admin?token=<TOKEN>
```

실패 시 사유를 상세히 출력하여 사용자가 룰을 수정할 수 있도록 한다.

---

## 주의 사항 (Do / Don't)

- ✅ 항상 **DRAFT 상태**로만 적재. 자동 PUBLISH 금지 — 검토는 [`draft-review-publish`](../draft-review-publish/) 스킬에서 수행한다.
- ✅ 외부 사이트에 과도한 부하를 주지 않도록 요청 간 delay (1~2초) 적용.
- ✅ User-Agent 헤더에 연락 가능한 식별자 포함.
- ❌ 쿠키·세션 토큰을 코드에 하드코딩하지 말 것. 환경변수 사용.
- ❌ 동일 source_url 중복 적재 방지 — 적재 전 기존 DRAFT 검색.
- ❌ 채용 사이트의 robots.txt를 무시하지 말 것.

---

## 관련 문서
- [`docs/REVIEW_GUIDE.md`](../../docs/REVIEW_GUIDE.md) — 품질 검증 기준
- [`docs/MISTAKES.md`](../../backup/docs/MISTAKES.md) — 과거 실수 기록
- [`backup/README.md`](../../backup/README.md) — 이전 README (구조·매핑 룰 상세)
