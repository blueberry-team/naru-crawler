---
name: company-crawling
description: 기업의 공식 채용 사이트·코퍼레이트 페이지에서 회사 정보를 크롤링하여 나루(naru-recruit.com)의 Company DB에 DRAFT로 적재한다. 회사명·로고·산업·인원수·복지·경영철학·태그 등 메타데이터 수집을 담당한다.
---

# company-crawling — 기업 크롤링 스킬

## 무엇을 하는가

지정한 기업의 공식 사이트와 채용 페이지에서 **회사 메타데이터**를 수집하여 나루 백엔드의 Company 엔티티로 적재한다. 채용 공고 단건은 [`job-crawling`](../job-crawling/) 스킬에서 별도로 처리한다.

- 입력: 회사명, 도메인, 또는 기업 정보 페이지 URL
- 처리: 회사 페이지/위키피디아/CSR 페이지 등에서 메타 추출 → 산업·기업유형·근무형태 enum 매핑
- 출력: 나루 백엔드의 새 Company DRAFT (관리자 검토 대기)

---

## 전제 조건 (Setup)

이 스킬은 **다양한 사람이 Claude Desktop을 통해 처음 접근해서 실행하는 시나리오**를 가정한다. 처음 사용자는 아래를 한 번만 완료한다.

### 1. 저장소 클론
```bash
git clone git@github.com:blueberry-team/naru-crawler.git
cd naru-crawler
```

### 2. Python 환경
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backup/requirements.txt
```

### 3. 필수 환경 변수
```bash
export NARU_ADMIN_TOKEN="<발급받은_토큰>"
export NARU_API_BASE="https://api.naru-recruit.com"
# 로고 이미지 호스팅 토큰 (선택)
export LOGO_DEV_TOKEN="<logo.dev_pk_token>"
```

`LOGO_DEV_TOKEN`이 없으면 로고 URL은 빈 값으로 적재된다.

### 4. Claude Desktop 권한
사용 도구: `Bash`, `WebFetch`, `WebSearch`, `Read`, `Write`. 권한 모드는 `acceptEdits` 권장.

### 5. 첫 실행 점검
```bash
curl -s "$NARU_API_BASE/api/companies" | python3 -c "import json,sys; print(len(json.load(sys.stdin).get('items',[])))"
```
숫자가 출력되면 셋업 완료.

---

## 사용 방법

Claude Desktop에서 다음과 같이 호출한다:

```
/company-crawling 도메인=hitachi.co.jp
/company-crawling 회사명="아빔 컨설팅"
```

또는 자연어:

> "freee 회사 정보 크롤링해서 나루 드래프트로 등록해줘"

### 워크플로우
1. **회사 식별** — 사용자 입력에서 도메인 또는 회사명 추출, 위키/공식 사이트 검색
2. **공식 페이지 fetch** — 회사 소개·CSR·IR 페이지에서 다음 정보 추출:
   - 회사명 (KO/JA/EN)
   - 본사 위치 (도쿄/오사카/지방)
   - 산업 분류 (IT·통신·인터넷, 컨설팅, 금융 등)
   - 기업 유형 (대기업, 중견, 스타트업, 외국계)
   - 직원 수 (그룹·단체)
   - 설립 연도, 매출, 상장 여부
   - 경영철학·핵심가치
   - 복리후생 키워드
3. **로고 URL 수집** — `https://img.logo.dev/{domain}?token=$LOGO_DEV_TOKEN`
4. **태그 생성** — 산업·기술·키워드 5~10개 추출
5. **enum 매핑** — `backup/rules/`의 매핑 룰 또는 LLM 기반 분류
6. **DRAFT 적재** — `POST /api/dev/companies` (`publishStatus: "DRAFT"`)
7. **결과 보고** — companyId 와 어드민 링크 반환

### 중복 방지
적재 전 `GET /api/companies?slug={slug}`로 동일 slug 존재 여부 확인. 이미 있으면 사용자에게 업데이트 여부를 물어본다.

---

## 출력 형식

```
✅ 회사 크롤링 결과
- 회사명: 주식회사 freee
- slug: freee
- companyId: 130
- 산업: IT·통신·인터넷
- 직원 수: 1,722명
- 태그: SaaS, 회계, 핀테크, 클라우드, 자동화, ...

확인 링크: https://www.naru-recruit.com/admin/companies/130?token=<TOKEN>
```

---

## 주의 사항 (Do / Don't)

- ✅ 항상 **DRAFT** 상태로만 적재. 사람이 검토 후 PUBLISH.
- ✅ 다국어 명칭(KO/JA/EN) 모두 수집 시도.
- ✅ `description`은 원본 언어 그대로가 아니라 한국어로 정리.
- ❌ 자동 번역기에 의존한 부정확한 한글화 금지 — 번역 전 사람 검증 권장 필드는 별도 표시.
- ❌ 위키피디아의 구버전 직원수 등 stale 데이터 주의. 가능하면 IR/유가증권보고서의 최신값 사용.
- ❌ 공식 로고를 무단으로 호스팅에 업로드하지 말 것. logo.dev 등 라이선스가 명확한 서비스 사용.

---

## 관련 문서
- [`docs/REVIEW_GUIDE.md`](../../docs/REVIEW_GUIDE.md) — 회사 메타 검증 기준
- [`backup/README.md`](../../backup/README.md) — 이전 구조
