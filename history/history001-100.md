# Deep Review History — Job #1 ~ #100

25개 평가 기준에 따른 공고별 상세 검증 결과.
평가 기준 상세: [docs/REVIEW_GUIDE.md](../docs/REVIEW_GUIDE.md)

---

## Job #1 ~ #11 — 존재하지 않음

| jobId | 상태 | 비고 |
|-------|------|------|
| 1 | 404 | DB에 존재하지 않음 |
| 2 | 404 | DB에 존재하지 않음 |
| 3 | 404 | DB에 존재하지 않음 |
| 4 | 404 | DB에 존재하지 않음 |
| 5 | 404 | DB에 존재하지 않음 |
| 6 | 404 | DB에 존재하지 않음 |
| 7 | 404 | DB에 존재하지 않음 |
| 8 | 404 | DB에 존재하지 않음 |
| 9 | 404 | DB에 존재하지 않음 |
| 10 | 404 | DB에 존재하지 않음 |
| 11 | 404 | DB에 존재하지 않음 |

API 확인: `GET /api/dev/jobs/{1~11}` 모두 404 응답. 초기 테스트 데이터 삭제 추정.
검증일: 2026-04-14

---

## Job #12 — DeNA | 2027년도 엔지니어직 본전형

**상태**: PUBLISHED | **소스**: https://dena.snar.jp/jobboard/detail.aspx?id=VzqdHIlOrLHIbVES5fPykA
**나루 공고**: https://www.naru-recruit.com/jobs/12
**어드민**: https://www.naru-recruit.com/admin/jobs/12?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 13:20 | 리뷰 | 22/25 ⚠️3 (A-2 salaryMax null, C-9 기업규모 미기재, D-12 요코하마 누락) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 연봉 500만엔~(월급 271,250엔~+직무급 116,250엔~). DB: salaryMin=5000000 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 상한 미기재("500万円~")이므로 정확하나, 상한 없음 표기가 맞는지 확인 필요 |
| A-3 | 통화·단위 | ✅ | 엔(만엔) 기준, 연봉 단위 정확 |
| B-4 | overview 발췌 | ✅ | 원본의 직무 설명("특정 영역에 머무르지 않고 다양한 사업 영역에서 새로운 가치 창출")과 일치. 오픈 포지션·입사 후 배치 확정 내용 정확 반영 |
| B-5 | tasks 일치 | ✅ | 6개 항목 모두 원본의 5개 엔지니어 트랙(소프트웨어/인프라/보안/데이터·MLOps/게임 클라이언트) 업무와 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave "2027년 4월 입사 가능(학력 불문)" = 원본 "2027年4月入社可能な方(就業経験の有無、年齢やいつ卒業したかに関わらず応募可)" 정확 |
| B-7 | selectionProcess 일치 | ✅ | "1차(서류·적성)→2차(면접)→3차→4차→최종→내정" 원본과 일치. 재도전 1회 가능 조건도 포함 |
| C-8 | 업종·사업 특성 | ✅ | overview에 "다양한 사업 영역에서 새로운 가치 창출" — DeNA의 멀티사업 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | overview에 기업 규모(직원수, 상장 여부 등) 미기재. 오픈 포지션·연수 후 배치 등 문화 특성은 반영됨 |
| C-10 | 기업명 정확성 | ✅ | "DeNA" (주식회사 디·엔·에이) 정확. 자회사 혼동 없음 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 신졸 엔지니어 오픈 포지션에 적합 |
| D-12 | locations 정확성 | ⚠️ | TOKYO만 기재. 원본에 "시부야 오피스(본사), 요코하마 오피스" 두 곳 명시. YOKOHAMA 누락이나 enum 부재 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD — 2027년 신졸 채용으로 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID — 원본 "리모트 워크가 인정된 장소" + 오피스 출근 = 하이브리드 정확 |
| E-15 | 필수 필드 누락 | ✅ | title, overview, tasks, position, locations, experienceLevel 모두 존재·유효 |
| E-16 | techStack 정확성 | ✅ | iOS/Android/Server/Web Front-end/Unity/Unreal Engine/GitHub Enterprise/JIRA/Slack/Circle CI — 원본 기술 스택과 일치 |
| E-17 | deadline 정확성 | ✅ | null — 원본에도 마감일 미기재 (수시 채용) |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월 (이전 입사 협의 가능)" — 원본과 정확 일치 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함. HTML 태그·깨진 문자 없음 |
| F-20 | 한국어 번역 | ✅ | 자연스러운 번역. 고유명사(DeNA, Unity 등) 적절 처리 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보에 집중됨. 과도한 기업 일반 소개 없음 |
| G-22 | source_url 접근 | ✅ | 200 응답. 정상 접근 가능 |
| G-23 | 채용 종료 키워드 | ✅ | 없음. Entry 버튼 활성 상태 |
| G-24 | 중복 공고 | ✅ | 동일 URL 중복 없음 |
| G-25 | 제목 일치 | ✅ | 원본 "2027年度 エンジニア職 本選考" → "2027년도 엔지니어직 본전형" 정확 |

**종합**: ✅ 22/25 통과, ⚠️ 3, ❌ 0
**판정**: PUBLISH 유지 적합. salaryMax null·요코하마 위치 누락·기업 규모 미기재는 경미한 이슈.
**Fix 액션**: 없음. A-2(salaryMax null)는 원본도 상한 미기재이므로 수정 불가. D-12(요코하마 누락)는 YOKOHAMA enum 부재로 AUTO-FIX 불가 → HOLD.
**Deadline 액션**: 없음. deadline=null(수시 채용), isDeadlinePassed=null, 원본 활성 확인(Entry 버튼 활성).

---

## Job #13 — DeNA | 2027년도 AI 스페셜리스트직 채용

**상태**: PUBLISHED | **소스**: https://student.dena.com/job/aispecialist
**나루 공고**: https://www.naru-recruit.com/jobs/13
**어드민**: https://www.naru-recruit.com/admin/jobs/13?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 13:20 | 리뷰 | 21/25 ⚠️4 (A-1 연봉출처 불명, A-2 범위, D-11 position 모호, D-12 위치) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=6000000. 원본 랜딩페이지에 연봉 미기재. 별도 snar.jp 지원 포털에서 확인 필요. 출처 불명확 |
| A-2 | 연봉 범위 일치 | ⚠️ | 원본 랜딩페이지에 연봉 정보 없음. salaryMin 600만엔의 근거 확인 불가 (DeNA AI 스페셜리스트 일반 수준과 부합하지만 원본 발췌 아님) |
| A-3 | 통화·단위 | ✅ | 엔 단위, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "AI 올인 전략", "스포츠, 게임, 라이브 스트리밍, 헬스케어" 등 원본 페이지의 핵심 메시지와 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 원본의 AI 엔지니어/데이터 사이언티스트/풀스택 3개 부문 업무 반영. LLM·생성형 AI, Kaggle 등 구체적 |
| B-6 | targetCandidate 일치 | ✅ | mustHave "AI 전문성·응용력·열정 + 2027년 4월 입사(학력불문)" — 원본 취지와 일치 |
| B-7 | selectionProcess 일치 | ✅ | Job #12와 동일 전형 프로세스. DeNA 공통 전형 구조 |
| C-8 | 업종·사업 특성 | ✅ | "스포츠, 게임, 라이브 스트리밍, 헬스케어" — DeNA 핵심 사업 영역 명시 |
| C-9 | 기업 규모·문화 차별화 | ✅ | "AI 올인 전략" — DeNA의 AI 투자 방향성 차별화 포인트 반영 |
| C-10 | 기업명 정확성 | ✅ | DeNA 정확 |
| D-11 | position 정확성 | ⚠️ | GRADUATE_ENGINEER — AI 스페셜리스트인데 일반 엔지니어와 동일 분류. AI_ML 또는 ML_ENGINEER가 더 정확할 수 있으나 신졸 특화 enum이라 수용 가능 |
| D-12 | locations 정확성 | ⚠️ | TOKYO만 기재. Job #12와 동일하게 요코하마 오피스 가능성 있으나 랜딩페이지에 위치 미기재 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD — 2027년 신졸 채용 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID — Job #12와 동일 근무 체계 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | LLM/생성형AI/LLMOps/AI Agent/컴퓨터비전/MLOps/Python — AI 스페셜리스트에 적합한 스택 |
| E-17 | deadline 정확성 | ✅ | null — 원본에도 마감일 미기재 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답. 랜딩페이지 정상 |
| G-23 | 채용 종료 키워드 | ✅ | 없음. Entry 링크 활성 (2027/2028 입사 모두) |
| G-24 | 중복 공고 | ✅ | Job #12와 별도 트랙 (엔지니어 vs AI 스페셜리스트). 중복 아님 |
| G-25 | 제목 일치 | ✅ | 원본 "AIスペシャリスト" → "AI 스페셜리스트직 채용" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 4, ❌ 0
**판정**: PUBLISH 유지 적합. 연봉 출처 불명확(A-1, A-2)이 가장 큰 이슈 — 원본 랜딩페이지에 연봉 미기재인데 DB에 600만엔 설정됨. 별도 확인 필요.
**Fix 액션**: 없음. A-1/A-2(연봉 출처 불명확)는 SEMI-AUTO — snar.jp 포털에서 별도 확인 필요 → HOLD. D-12/D-11은 구조적 한계.
**Deadline 액션**: 없음. deadline=null(수시), 원본 활성(Entry 링크 2027/2028 모두 활성).

---

## Job #14 — DeNA | 2027년도 비즈니스직 본전형

**상태**: PUBLISHED | **소스**: https://dena.snar.jp/jobboard/detail.aspx?id=L7eq4XI5cPU5t6K5rHapeQ
**나루 공고**: https://www.naru-recruit.com/jobs/14
**어드민**: https://www.naru-recruit.com/admin/jobs/14?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 13:30 | 리뷰 | 23/25 ⚠️2 (A-2 salaryMax null, D-12 요코하마 누락) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 연봉 500만엔~(월급 271,250엔~+직무급 116,250엔~). DB: salaryMin=5000000 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 상한 미기재("500万円~")이므로 정확하나 상한 없음 |
| A-3 | 통화·단위 | ✅ | 엔(만엔) 기준, 연봉 단위 정확 |
| B-4 | overview 발췌 | ✅ | "난이도 높은 미션", "사업 리더 또는 스페셜리스트", "전략 입안~마케팅~경영 기획" — 원본 취지와 일치 |
| B-5 | tasks 일치 | ✅ | 7개 항목(사업추진/PM/조직관리/마케팅/커뮤니티/대외협력/CS) — 원본의 비즈니스 직군 업무 범위와 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave "2027년 4월 입사(학력·경력 불문)" 원본과 정확 일치 |
| B-7 | selectionProcess 일치 | ✅ | "엔트리→WEB테스트·ES→면접 4회→최종→내정" — 원본 전형 플로우와 일치. 재도전 가능 조건 포함 |
| C-8 | 업종·사업 특성 | ✅ | "정답이 없는 길을 개척하며 DeNA 사업의 근간을 지탱" — 비즈니스직 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ✅ | workingConditions에 "셰이크핸즈 제도(사내 전직), 크로스잡 제도(사내 부업)" — DeNA 고유 제도 반영 |
| C-10 | 기업명 정확성 | ✅ | DeNA 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 신졸 비즈니스/종합직에 적합 |
| D-12 | locations 정확성 | ⚠️ | TOKYO만 기재. 원본에 "시부야 본사, 요코하마 오피스" 두 곳 명시. YOKOHAMA 누락 (enum 부재) |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID — "리모트 워크가 인정된 장소" + 오피스 = 하이브리드 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재·유효 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 비즈니스직이므로 기술 스택 없음이 정확 |
| E-17 | deadline 정확성 | ✅ | null — 원본에도 마감일 미기재 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월 (이전 입사 협의 가능)" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "셰이크핸즈", "크로스잡" 등 고유 제도명 적절 표기 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답, Entry 버튼 활성 |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ✅ | Job #12(엔지니어), #13(AI)과 별도 트랙 |
| G-25 | 제목 일치 | ✅ | 원본 "2027年度 ビジネス職 本選考" → "2027년도 비즈니스직 본전형" 정확 |

**종합**: ✅ 23/25 통과, ⚠️ 2, ❌ 0
**판정**: PUBLISH 유지 적합. salaryMax null·요코하마 누락은 경미.
**Fix 액션**: 없음. A-2/D-12 모두 구조적 한계 (enum 부재/원본 상한 미기재).
**Deadline 액션**: 없음. deadline=null(수시), 원본 활성.

---

## Job #15 — DeNA | 2027년도 디자이너직 채용

**상태**: PUBLISHED | **소스**: https://student.dena.com/job/designer
**나루 공고**: https://www.naru-recruit.com/jobs/15
**어드민**: https://www.naru-recruit.com/admin/jobs/15?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 13:30 | 리뷰 | 21/25 ⚠️4 (A-1 연봉출처, A-2 범위, D-12 위치, G-22 URL 혼합) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4500000. 원본 랜딩페이지에는 디자이너직 연봉 직접 기재 없음. snar.jp 지원 포털 별도 확인 필요. 다른 트랙(AI 600만)과 구분되는 450만 설정의 근거 불명확 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본에서 디자이너직 상한 확인 불가 |
| A-3 | 통화·단위 | ✅ | 엔 단위, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "엔터테인먼트부터 사회의 미래까지", "프로덕트/커뮤니케이션/게임 서비스 디자인 세 영역" — 원본 페이지 메시지와 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 프로덕트 디자인, 커뮤니케이션 디자인, 게임 서비스 디자인, AI 활용 크리에이티비티 — 원본 3개 디자인 트랙 + AI 활용 반영 |
| B-6 | targetCandidate 일치 | ✅ | mustHave "2027년 4월 입사(학력불문) + 포트폴리오 제출" — 디자이너직 특유의 포트폴리오 요건 정확 반영 |
| B-7 | selectionProcess 일치 | ✅ | "1차(서류·포트폴리오 심사)→면접 3회→최종→내정" — 디자이너직은 포트폴리오 심사가 1차에 포함, 엔지니어와 차별화 |
| C-8 | 업종·사업 특성 | ✅ | "세계를 열광시키는 새로운 가치 창출" — DeNA 디자인 비전 반영 |
| C-9 | 기업 규모·문화 차별화 | ✅ | workingConditions에 "마사지룸, CHO실(건강관리)" — DeNA 복지 특성 반영 |
| C-10 | 기업명 정확성 | ✅ | DeNA 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 신졸 디자이너직에 정확 |
| D-12 | locations 정확성 | ⚠️ | TOKYO만 기재. 요코하마 오피스 가능성 있으나 디자이너 랜딩페이지에 위치 상세 미기재 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | AI/Figma/Adobe Creative Cloud/Unity — 디자이너 도구로 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시 채용 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 200 응답이나 랜딩페이지가 다른 트랙(AI 제너럴리스트) 정보도 혼합 표시. 디자이너 전용 상세가 분리되지 않음 |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ✅ | Job #12~14와 별도 트랙 |
| G-25 | 제목 일치 | ✅ | "デザイナー" → "디자이너직 채용" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 4, ❌ 0
**판정**: PUBLISH 유지 적합. 연봉 출처 불명확(A-1,A-2)과 source URL 혼합 표시(G-22)가 주요 이슈.
**Fix 액션**: 없음. A-1/A-2(연봉 출처)는 SEMI-AUTO → HOLD. G-22(URL 혼합)는 원본 구조적 한계.
**Deadline 액션**: 없음. deadline=null(수시), 원본 활성.

---

## Job #16 — 덴츠디지털 | 크리에이티브/아트(CR) 2027년도 본전형

**상태**: PUBLISHED | **소스**: https://dd.dentsudigital.co.jp/recruit/newrec/course/
**나루 공고**: https://www.naru-recruit.com/jobs/16
**어드민**: https://www.naru-recruit.com/admin/jobs/16?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 13:40 | 리뷰 | 20/25 ⚠️5 (A-1 연봉, A-2 범위, C-9 기업맥락, G-22 URL공유, G-24 중복URL) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4394700. 원본 코스 페이지에 연봉 미기재. 별도 채용 요강 페이지에서 확인 필요. 439만 4700엔은 덴츠디지털 신졸 초봉 수준과 부합하지만 이 페이지에서 발췌 아님 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본에 연봉 범위 미기재 |
| A-3 | 통화·단위 | ✅ | 엔 단위, 연봉 기준. 439만 4700엔 = 월급 기반 연 환산으로 추정 |
| B-4 | overview 발췌 | ✅ | "크리에이티브와 기술의 힘으로 사람의 마음을 움직이는 일", "광고의 틀에 얽매이지 않고" — 원본 CR 코스 설명과 의미 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — WebCM/배너/캠페인, 크리에이티브+기술 과제해결, 비즈니스 창출, 서비스 개발 — 원본 CR 코스 업무 범위와 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 3월 졸업 예정 + 일본어 소통 + 포트폴리오" — 원본의 CR 코스 자격과 정확 일치 |
| B-7 | selectionProcess 일치 | ✅ | "프리엔트리→코스선택→전형(포트폴리오·실무과제)→내정" — 원본의 CR 전형 특징(실무과제) 반영 |
| C-8 | 업종·사업 특성 | ✅ | "광고의 틀에 얽매이지 않고" — 덴츠디지털의 디지털 종합 광고 + 사업개발 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 덴츠그룹 산하 디지털 전문회사라는 맥락 미기재. 기업 개요 부족 |
| C-10 | 기업명 정확성 | ✅ | "덴츠디지털(dentsu-digital)" 정확. 덴츠 본사와 구분됨 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 크리에이티브/아트 직군에 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA — 덴츠디지털은 도쿄·오사카 양 거점 운영, 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID — 덴츠디지털 근무 형태와 부합 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 크리에이티브/아트 직군이므로 특정 기술 스택 없음 정확 |
| E-17 | deadline 정확성 | ✅ | null — 원본에도 마감일 미기재 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" — 원본 입사 시기와 일치 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 200 응답이나 8개 코스 공통 페이지. CR 코스 전용 URL이 아니라 전체 코스 소개 페이지 → Job #16~#17 등 여러 공고가 동일 URL 공유 |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ⚠️ | Job #17(DS 코스)과 동일 source_url. URL 기준 중복이나 코스가 다르므로 콘텐츠 중복은 아님 |
| G-25 | 제목 일치 | ✅ | 원본 "クリエイティブ/アート(CR)" → "크리에이티브/아트(CR)" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. 연봉 출처 불명확, 기업 맥락 부족, source_url 공유(8코스 1페이지)가 주요 이슈. source_url은 구조적 한계(코스별 개별 URL 미제공).
**Fix 액션**: 없음. 덴츠디지털 공통 구조적 한계 (연봉·기업맥락·URL공유). AUTO-FIX 대상 없음.
**Deadline 액션**: 없음. deadline=null(수시), 원본 활성.

---

## Job #17 — 덴츠디지털 | 데이터 사이언스(DS) 2027년도 본전형

**상태**: PUBLISHED | **소스**: https://dd.dentsudigital.co.jp/recruit/newrec/course/
**나루 공고**: https://www.naru-recruit.com/jobs/17
**어드민**: https://www.naru-recruit.com/admin/jobs/17?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 13:40 | 리뷰 | 19/25 ⚠️6 (A-1, A-2, C-9, D-11 position 모호, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4394700. Job #16과 동일. 원본 페이지에 연봉 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본 미기재 |
| A-3 | 통화·단위 | ✅ | 엔 단위, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "데이터와 AI/머신러닝 활용을 통한 비즈니스 가치 창출", "통계·머신러닝 고도 분석" — 원본 DS 코스 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 솔루션 기획/개발, 고도 분석, 컨설팅, AI 자동화 — DS 코스 업무와 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 3월 졸업 예정 + 일본어 소통" — 원본과 일치. CR과 달리 포트폴리오 불요 (정확) |
| B-7 | selectionProcess 일치 | ✅ | "프리엔트리→코스선택→전형(개발 지식·기술 확인)→내정" — DS 코스 특징(개발 지식 확인) 반영 |
| C-8 | 업종·사업 특성 | ✅ | "마케팅 커뮤니케이션 영역에서의 독자적 솔루션" — 광고 데이터 분석 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | Job #16과 동일 — 덴츠그룹 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | 덴츠디지털 정확 |
| D-11 | position 정확성 | ⚠️ | GRADUATE_ENGINEER — DS 코스인데 일반 엔지니어 분류. GRADUATE_DATA 또는 DATA_SCIENTIST가 더 정확할 수 있으나 신졸 enum 체계상 수용 가능 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | AI/Machine Learning/통계학 — DS 코스에 적합. 다소 추상적이나 원본도 구체 기술 미기재 |
| E-17 | deadline 정확성 | ✅ | null — 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | Job #16과 동일 URL 공유 (8코스 1페이지) |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ⚠️ | Job #16과 동일 source_url. 코스 다르므로 콘텐츠 중복 아님 |
| G-25 | 제목 일치 | ✅ | "データサイエンス(DS)" → "데이터 사이언스(DS)" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합. Job #16과 동일 구조적 이슈(연봉 출처, 기업 맥락, URL 공유). position 분류가 약간 모호(GRADUATE_ENGINEER vs DS 특화).
**Fix 액션**: 없음. D-11(position GRADUATE_ENGINEER vs DS 특화)는 신졸 enum 체계상 수용 가능 → HOLD.
**Deadline 액션**: 없음. deadline=null(수시), 원본 활성.

---

## Job #18 — 덴츠디지털 | 소프트웨어/AI 시스템 엔지니어링(EG) 2027년도 본전형

**상태**: PUBLISHED | **소스**: https://dd.dentsudigital.co.jp/recruit/newrec/course/
**나루 공고**: https://www.naru-recruit.com/jobs/18
**어드민**: https://www.naru-recruit.com/admin/jobs/18?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 13:50 | 리뷰 | 19/25 ⚠️6 (A-1, A-2, C-9, E-16 techStack 추상, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4394700. Job #16~17과 동일 — 원본 코스 페이지에 연봉 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본 미기재 |
| A-3 | 통화·단위 | ✅ | 엔 단위, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "디지털 광고 영역 앱 개발", "생성형 AI·예측 AI" — 원본 EG 코스 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 앱 개발, 클라우드 인프라, AI 시스템, 운영 — EG 코스 업무 정확 반영 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 3월 졸업(고전·전문학교 포함) + 일본어" — 원본과 일치. EG는 고전·전문학교도 지원 가능 (CR/MC와 차이) |
| B-7 | selectionProcess 일치 | ✅ | "프리엔트리→코스선택→전형→내정" — 원본 구조와 일치 |
| C-8 | 업종·사업 특성 | ✅ | "디지털 광고 영역", "클라이언트에게 가치 제공" — 광고 테크 회사 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 덴츠그룹 맥락 미기재 (Job #16~17과 동일 이슈) |
| C-10 | 기업명 정확성 | ✅ | 덴츠디지털 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — SW/AI 엔지니어링 직군에 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | "Software Development/Cloud Infrastructure/AI System Engineering" — 추상적. 구체 기술(Python, AWS, GCP 등) 미기재이나 원본도 구체 기술 미명시 |
| E-17 | deadline 정확성 | ✅ | null — 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | Job #16~17과 동일 — 8코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ⚠️ | Job #16~17과 동일 source_url. 코스 다르므로 콘텐츠 중복 아님 |
| G-25 | 제목 일치 | ✅ | "ソフトウェア/AIシステムエンジニアリング(EG)" → 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합. 덴츠디지털 공통 구조적 이슈(연봉·기업맥락·URL공유·techStack 추상). Job #16~17과 동일 패턴.
**Fix 액션**: 없음. E-16(techStack 추상)는 원본도 구체 기술 미명시 → 수정 불가.
**Deadline 액션**: 없음. deadline=null(수시), 원본 활성.

---

## Job #19 — 덴츠디지털 | 마케팅 커뮤니케이션(MC) 2027년도 본전형

**상태**: PUBLISHED | **소스**: https://dd.dentsudigital.co.jp/recruit/newrec/course/
**나루 공고**: https://www.naru-recruit.com/jobs/19
**어드민**: https://www.naru-recruit.com/admin/jobs/19?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 13:50 | 리뷰 | 20/25 ⚠️5 (A-1, A-2, C-9, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4394700. 원본 미기재, 덴츠디지털 공통 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔 단위, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "Google, Instagram, TikTok, X, Amazon 등 플랫폼 활용", "온오프라인 통합 마케팅" — 원본 MC 코스 설명과 일치. 구체적 플랫폼 명시가 좋음 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 광고 전략, 화제성 창출, 통합 마케팅, 이커머스 시책 — MC 코스 업무와 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 3월 졸업(대학원·대학) + 일본어" — 원본과 일치. MC는 고전·전문학교 미포함 (EG와 차이 정확 반영) |
| B-7 | selectionProcess 일치 | ✅ | 원본 구조와 일치 |
| C-8 | 업종·사업 특성 | ✅ | 디지털 마케팅·광고 특성 구체적으로 반영 (플랫폼 나열) |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 덴츠그룹 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | 덴츠디지털 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 마케팅/비즈니스 직군으로 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — MC 직군이므로 기술 스택 없음 정확 |
| E-17 | deadline 정확성 | ✅ | null — 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 8코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ⚠️ | Job #16~18과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "マーケティングコミュニケーション(MC)" → 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. 덴츠디지털 공통 패턴. overview의 플랫폼 나열(Google/Instagram/TikTok/X/Amazon)이 구체적이어서 콘텐츠 품질 양호.
**Fix 액션**: 없음. 덴츠디지털 공통 구조적 한계.
**Deadline 액션**: 없음. deadline=null(수시), 원본 활성.

---

## Job #20 — 덴츠디지털 | 마케팅 DX(DX) 2027년도 본전형

**상태**: PUBLISHED | **소스**: https://dd.dentsudigital.co.jp/recruit/newrec/course/
**나루 공고**: https://www.naru-recruit.com/jobs/20
**어드민**: https://www.naru-recruit.com/admin/jobs/20?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 14:00 | 리뷰 | 20/25 ⚠️5 (A-1, A-2, C-9, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4394700. 덴츠디지털 공통 — 원본 코스 페이지에 연봉 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "마케팅 DX·가치 창출 DX", "프로덕트 변혁, 온드 미디어 변혁, 로열티 변혁" — 원본 DX 코스 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — DX 지원, 미디어 변혁, 1to1 마케팅, 커머스 변혁 — DX 코스 업무와 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 3월 졸업(대학원·대학) + 일본어" — 원본과 일치 |
| B-7 | selectionProcess 일치 | ✅ | 덴츠디지털 공통 전형 구조 |
| C-8 | 업종·사업 특성 | ✅ | "IT 지식과 커뮤니케이션의 종합적 능력" — DX 컨설팅 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 덴츠그룹 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | 덴츠디지털 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — DX 컨설턴트로 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — DX 컨설턴트 직군이므로 특정 기술 없음 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 8코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ⚠️ | Job #16~19와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "マーケティングDX(DX)" → 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: 없음 (AUTO-FIX 대상 없음. 연봉·기업맥락·URL공유는 구조적 한계)
**Deadline 액션**: 없음 (deadline=null, isDeadlinePassed=null, 수시 채용, 원본 활성)

---

## Job #21 — 덴츠디지털 | 글로벌(GL) 2027년도 본전형

**상태**: PUBLISHED | **소스**: https://dd.dentsudigital.co.jp/recruit/newrec/course/
**나루 공고**: https://www.naru-recruit.com/jobs/21
**어드민**: https://www.naru-recruit.com/admin/jobs/21?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 14:00 | 리뷰 | 20/25 ⚠️5 (A-1, A-2, C-9, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4394700. 덴츠디지털 공통 — 원본 코스 페이지에 연봉 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "글로벌 기업 디지털 마케팅", "해외 거점 포함 덴츠 그룹 연계", "외자계·일본계 양방향" — 원본 GL 코스 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 글로벌 프로듀싱, 외자계→일본, 일본계→해외, 디지털화 — GL 코스 업무와 일치 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정 + 일본어 + TOEIC 750점" — GL 코스 특유의 영어 요건 정확 반영. 다른 코스와 차별화됨 |
| B-7 | selectionProcess 일치 | ✅ | "영어 실력 확인 포함" — GL 코스 전형 특징 반영 |
| C-8 | 업종·사업 특성 | ✅ | "해외 거점 포함 덴츠 그룹 연계" — 글로벌 광고 네트워크 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 덴츠그룹 전체 규모·해외 거점 수 등 미기재 |
| C-10 | 기업명 정확성 | ✅ | 덴츠디지털 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 글로벌 마케팅/비즈니스 직군으로 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — GL 직군이므로 기술 스택 없음 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "외자계 기업", "프로듀싱" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 8코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ⚠️ | Job #16~20과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "グローバル(GL)" → "글로벌(GL)" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: 없음 (덴츠디지털 공통 구조적 한계)
**Deadline 액션**: 없음 (deadline=null, isDeadlinePassed=null, 수시 채용, 원본 활성)

---

## Job #22 — 덴츠디지털 | 비즈니스 프로듀스(BP) 2027년도 본전형

**상태**: PUBLISHED
**소스**: https://dd.dentsudigital.co.jp/recruit/newrec/course/
**나루 공고**: https://www.naru-recruit.com/jobs/22
**어드민**: https://www.naru-recruit.com/admin/jobs/22?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 14:10 | 리뷰 | 20/25 ⚠️5 (A-1, A-2, C-9, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4394700. 덴츠디지털 공통 — 원본 코스 페이지에 연봉 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "사내외 최전선에서 클라이언트 과제에 직면하는 세일즈 프로듀서", "전문가 팀 빌딩", "수지 관리" — 원본 BP 코스 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 과제해결, 팀빌딩, 프로세스설계, 안건 획득 — BP 코스 업무와 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 3월 졸업(대학원·대학) + 일본어" — 원본과 일치 |
| B-7 | selectionProcess 일치 | ✅ | 덴츠디지털 공통 전형 구조 |
| C-8 | 업종·사업 특성 | ✅ | "폭넓은 사업 영역을 강점으로" — 종합 디지털 광고 회사의 BP 직군 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 덴츠그룹 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | 덴츠디지털 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 세일즈 프로듀서/비즈니스 직군으로 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA — workingConditions에 "시오도메(도쿄), 간사이(오사카)" 명시. 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — BP 직군이므로 기술 스택 없음 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "수지 관리", "안건 획득" 등 비즈니스 용어 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 8코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ⚠️ | Job #16~21과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ビジネスプロデュース(BP)" → "비즈니스 프로듀스(BP)" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: 없음. 덴츠디지털 공통 구조적 한계 (연봉·기업맥락·URL공유). AUTO-FIX 대상 없음.
**Deadline 액션**: 없음. deadline=null(수시), isDeadlinePassed=null, 원본 활성.

---

## Job #23 — 덴츠디지털 | 오픈 포지션(OP) 2027년도 본전형

**상태**: PUBLISHED
**소스**: https://dd.dentsudigital.co.jp/recruit/newrec/course/
**나루 공고**: https://www.naru-recruit.com/jobs/23
**어드민**: https://www.naru-recruit.com/admin/jobs/23?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/14 14:10 | 리뷰 | 19/25 ⚠️6 (A-1, A-2, B-5 tasks 1개, C-9, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=4394700. 덴츠디지털 공통 — 원본 코스 페이지에 연봉 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "강점과 가치관 이해하고 최적 포지션 배치" — 원본 OP 코스 설명과 일치 |
| B-5 | tasks 일치 | ⚠️ | 1개 항목만 존재("최적 포지션 배치 후 업무"). OP 특성상 불가피하나 데이터 빈약 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정 + 일본어 + 학창시절 높은 성과 경험" — OP 코스 특유 자격 정확 반영 |
| B-7 | selectionProcess 일치 | ✅ | 덴츠디지털 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "서비스 영역과 경영 기반 중 최적 포지션" — OP 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 덴츠그룹 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | 덴츠디지털 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — OP(오픈포지션)으로 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 (tasks 1개뿐이지만 존재는 함) |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — OP이므로 기술 미정 정확 |
| E-17 | deadline 정확성 | ✅ | null — 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 8코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ⚠️ | Job #16~22와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "オープンポジション(OP)" → "오픈 포지션(OP)" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: 없음. B-5(tasks 1개)는 OP 특성상 불가피. 나머지는 덴츠 공통 구조적 한계.
**Deadline 액션**: 없음. deadline=null(수시), isDeadlinePassed=null, 원본 활성.

> 📊 덴츠디지털 8코스 전체 완료 (#16~23). 평균 19.6/25. 공통 ⚠️: 연봉 출처(A-1/A-2), 기업 맥락(C-9), URL 공유(G-22/G-24). 코스별 차별화(포트폴리오/영어/기술확인/성과 경험)는 정확 반영됨.

---

## Job #24 — LY Corp (LINE야후) | Software Engineering Specialist

**상태**: PUBLISHED
**소스**: https://www.lycorp.co.jp/ja/recruit/newgrads/engineer/jd0001/
**나루 공고**: https://www.naru-recruit.com/jobs/24
**어드민**: https://www.naru-recruit.com/admin/jobs/24?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 02:45 | 리뷰 | 19/25 ⚠️5 ❌1 (A-2, E-16, E-17 deadline 경과, G-23 채용종료) |
| 04/15 02:46 | Deadline | ❌ 채용 종료 확인 → PUT isDeadlinePassed=true (204) |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 月額 434,000엔~, 연봉 651만엔~. DB: salaryMin=6510000 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 "651万円~"으로 상한 미기재 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "각종 서비스와 기반 시스템 설계·개발·운용", "보안 품질 향상" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 웹앱/백엔드, 프런트엔드/SDK, iOS/Android, 데이터, ML — 원본 5개 전문 분야와 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년도 입사(4월/10월), 학력 불문, 정규직 경험 없는 분" — 원본과 정확 일치 |
| B-7 | selectionProcess 일치 | ✅ | "지원→코딩테스트→면접(복수회)→내정" — 원본과 일치 |
| C-8 | 업종·사업 특성 | ✅ | LINE야후의 대규모 서비스 개발 맥락 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | LINE야후 규모(직원수 등) 미기재. "폭넓은 기술 스택 경험" 문화는 반영됨 |
| C-10 | 기업명 정확성 | ✅ | ly-corp (LY Corporation = LINE야후) 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 신졸 SW 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO — 원본 "東京" 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID — 원본 "ハイブリッドワーク" 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | 빈 배열 []. 원본에 구체 기술은 명시 안 됐지만 5개 전문 분야(서버/프런트/모바일/데이터/ML)로 볼 때 일부 기술 추출 가능했음 |
| E-17 | deadline 정확성 | ❌ | deadline=2026-02-02이나 isDeadlinePassed=null이었음. 이미 경과 → PUT으로 수정 완료 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월/10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 (페이지 존재) |
| G-23 | 채용 종료 키워드 | ❌ | "2027年度新卒採用エントリー受付は終了しました" 발견 → 채용 종료 확인 |
| G-24 | 중복 공고 | ✅ | 중복 없음 |
| G-25 | 제목 일치 | ✅ | "Software Engineering Specialist" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 3, ❌ 2
**판정**: 채용 종료 → isDeadlinePassed=true 처리 완료
**Fix 액션**: 없음 (E-16 techStack 빈 배열은 SEMI-AUTO → HOLD)
**Deadline 액션**: ✅ PUT {"isDeadlinePassed": true} → 204. 원본에 "エントリー受付は終了しました" 확인. deadline=2026-02-02 이미 경과.

---

## Job #25 — LY Corp (LINE야후) | Infra Engineering Expert

**상태**: PUBLISHED
**소스**: https://www.lycorp.co.jp/ja/recruit/newgrads/engineer/jd0002/
**나루 공고**: https://www.naru-recruit.com/jobs/25
**어드민**: https://www.naru-recruit.com/admin/jobs/25?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 02:55 | 리뷰 | 20/25 ⚠️3 ❌2 (A-2, C-9, E-17 deadline 경과, G-23 채용종료) |
| 04/15 02:55 | Deadline | ❌ 채용 종료 확인 → PUT isDeadlinePassed=true (204) |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 月額 487,000엔~(기초급 377,377+고정시간외 109,623), 연봉 730만5천엔~. DB: salaryMin=7305000 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 "730万円~" 상한 미기재 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "방대한 트래픽을 지탱하는 기반 구축·운용", "국내 손꼽히는 규모의 인프라" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 6개 항목 — 물리서버 설계/OS Provisioning/서버관리 시스템/네트워크/자동화/프라이빗 클라우드 — 원본 6개 업무와 정확 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 입사(4월/10월), 학력 불문, 정규직 경험 없는 분" — 원본과 일치 |
| B-7 | selectionProcess 일치 | ✅ | "지원→코딩테스트→면접(복수회)→내정" — Job #24와 동일 구조 |
| C-8 | 업종·사업 특성 | ✅ | "수십만 대 물리 서버", "국내 손꼽히는 규모" — LINE야후 인프라 규모 강조 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 직원수 등 기업 개요 미기재. 인프라 규모 강조는 차별화 포인트 |
| C-10 | 기업명 정확성 | ✅ | ly-corp (LY Corporation) 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 신졸 인프라 엔지니어. INFRA가 더 정확할 수 있으나 신졸 enum 체계상 수용 가능 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | OpenStack/Kubernetes — 원본 명시 기술과 일치. 핵심 2개만이라 다소 적지만 원본도 이 2개만 명시 |
| E-17 | deadline 정확성 | ❌ | deadline=2026-02-02 이미 경과 (오늘 2026-04-15). isDeadlinePassed=null이었음 → PUT으로 수정 완료 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월/10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 |
| G-23 | 채용 종료 키워드 | ❌ | "2027年度新卒採用エントリー受付は終了しました" 발견 |
| G-24 | 중복 공고 | ✅ | Job #24와 동일 회사지만 다른 전문 분야 (SW vs Infra) |
| G-25 | 제목 일치 | ✅ | "Infra Engineering Expert" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 3, ❌ 2
**판정**: 채용 종료 → isDeadlinePassed=true 처리 완료
**Fix 액션**: 없음.
**Deadline 액션**: ✅ PUT {"isDeadlinePassed": true} → 204. Job #24와 동일 — LY Corp 2027 신졸 채용 전체 종료 확인.

> 📊 LY Corp 2건 (#24~25) 모두 채용 종료. 동일 deadline(2026-02-02), 동일 종료 메시지. LY Corp 잔여 공고(#26~?)도 같은 패턴일 가능성 높음.

---

## Job #26 — 라쿠텐 그룹 | 2027년도 비즈니스 종합 코스 본전형

**상태**: PUBLISHED
**소스**: https://corp.rakuten.co.jp/careers/graduates/recruit_business/business.html
**나루 공고**: https://www.naru-recruit.com/jobs/26
**어드민**: https://www.naru-recruit.com/admin/jobs/26?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 03:05 | 리뷰 | 21/25 ⚠️4 (A-2, C-9, E-17 deadline 경과하나 원본 활성, G-24 없음) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 月給 350,000엔(학부)/360,000엔(석사), 40시간 고정 시간외 포함. DB: salaryMin=4200000 = 350,000×12 정확 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 학부/석사 차이 있으나 상한은 미기재 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 (월급 ×12로 환산) |
| B-4 | overview 발췌 | ✅ | "약 70개 이상의 서비스", "초기 배치는 적성과 희망 고려" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 컨설팅영업/기획/마케팅/크리에이티브/코퍼레이트 — 원본 배치 대상 직종과 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 3월 졸업 예정 + 기졸업 3년 미만 + 비즈니스 일본어" — 원본과 정확 일치 |
| B-7 | selectionProcess 일치 | ✅ | "Personal Page 등록→AF 제출·Web Test→온라인 면접(2~3개월)→내정" — 원본과 일치 |
| C-8 | 업종·사업 특성 | ✅ | "인터넷, FinTech, 디지털 콘텐츠, 통신" — 라쿠텐 종합 사업 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 라쿠텐 그룹 규모(직원수, 글로벌 진출 등) 미기재. "70개+ 서비스"는 언급됨 |
| C-10 | 기업명 정확성 | ✅ | rakuten-group 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 비즈니스 종합 코스에 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO — 원본에 "勤務地: 本社および国内外の事業所" 중 본사 도쿄 기준 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 비즈니스 종합 코스이므로 기술 스택 없음 적절 |
| E-17 | deadline 정확성 | ⚠️ | deadline=2026-02-12 경과했으나 **원본 페이지에 종료 키워드 없음**. 마감일 연장 또는 수시 전환 추정. deadline 갱신 또는 삭제 필요 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답, 페이지 정상 |
| G-23 | 채용 종료 키워드 | ✅ | 없음 — 원본 여전히 활성 |
| G-24 | 중복 공고 | ✅ | 중복 없음 |
| G-25 | 제목 일치 | ✅ | "ビジネス総合コース" → "비즈니스 종합 코스" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 4, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: E-17 deadline=2026-02-12 경과했으나 원본 활성 → deadline null로 PUT 가능하지만 원본에서 새 마감일 미확인. HOLD (사용자 판단 필요: deadline 삭제 vs 유지).
**Deadline 액션**: 없음. deadline 경과했으나 원본에 종료 키워드 없음 → isDeadlinePassed 설정하지 않음. 원본이 활성이므로 마감 처리 부적절.

---

## Job #27 — LY Corp (LINE야후) | 비즈니스 컨설턴트

**상태**: PUBLISHED
**소스**: https://www.lycorp.co.jp/ja/recruit/newgrads/business-consultant/
**나루 공고**: https://www.naru-recruit.com/jobs/27
**어드민**: https://www.naru-recruit.com/admin/jobs/27?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 03:15 | 리뷰 | 20/25 ⚠️3 ❌2 (A-2, C-9, E-17 deadline 경과, G-23 채용종료) |
| 04/15 03:15 | Deadline | ❌ 채용 종료 확인 → PUT isDeadlinePassed=true (204) |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 月額 314,000엔~(기초급 242,459+고정시간외 71,541), 연봉 471만엔~. DB: salaryMin=4710000 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 "471万円~" 상한 미기재 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "방대한 데이터와 자산 활용", "컨설팅 세일즈", "매출 극대화" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — 컨설팅세일즈, 데이터활용 과제해결, 매출극대화 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 입사, 학력 불문, 정규직 경험 없는 분" + 상세 자질 요건 7개 — 원본과 정확 일치 |
| B-7 | selectionProcess 일치 | ✅ | "지원→ES·SPI→면접(복수)→내정, 면접 일본어" — 원본과 일치 |
| C-8 | 업종·사업 특성 | ✅ | "LINE야후의 데이터와 자산" — 플랫폼 기업의 B2B 컨설팅 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | ly-corp 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 비즈니스 컨설턴트 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA+FUKUOKA — 원본에 다거점 명시 시 3개 지역 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 비즈니스 직군이므로 적절 |
| E-17 | deadline 정확성 | ❌ | deadline=2026-02-17 이미 경과. isDeadlinePassed=null이었음 → PUT으로 수정 완료 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월/10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 |
| G-23 | 채용 종료 키워드 | ❌ | "2027年度新卒採用エントリー受付は終了しました" 발견 |
| G-24 | 중복 공고 | ✅ | Job #24~25(엔지니어)와 다른 직군 (비즈니스) |
| G-25 | 제목 일치 | ✅ | "ビジネスコンサルタント" → "비즈니스 컨설턴트" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 3, ❌ 2
**판정**: 채용 종료 → isDeadlinePassed=true 처리 완료
**Fix 액션**: 없음.
**Deadline 액션**: ✅ PUT {"isDeadlinePassed": true} → 204. LY Corp 2027 신졸 3건째 종료 확인.

> 📊 LY Corp 3건 (#24~25, #27) 모두 채용 종료. FUKUOKA enum이 실제 사용됨 — 기존 TOKYO/OSAKA 외 지방 enum 존재 확인.

---

## Job #28 — LY Corp (LINE야후) | 프로덕트 플래너

**상태**: PUBLISHED
**소스**: https://www.lycorp.co.jp/ja/recruit/newgrads/product-planner/
**나루 공고**: https://www.naru-recruit.com/jobs/28
**어드민**: https://www.naru-recruit.com/admin/jobs/28?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 03:25 | 리뷰 | 20/25 ⚠️3 ❌2 (A-2, C-9, E-17 deadline 경과, G-23 채용종료) |
| 04/15 03:25 | Deadline | ❌ 채용 종료 확인 → PUT isDeadlinePassed=true (204) |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 月額 336,000엔~(기초급 259,616+고정시간외 76,384), 연봉 504만엔~. DB: salaryMin=5040000 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 상한 미기재 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "수천만 규모 서비스부터 신규 사업", "사용자 퍼스트", "경험의 변화를 구상·구현" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 6개 항목 — 리서치/기획/UX설계/디렉션/AI 활용/사업전략 — 원본과 정확 일치. 생성AI·AI에이전트 활용도 포함 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 입사, 학력 불문" + 자질 요건 4개 — 원본과 일치 |
| B-7 | selectionProcess 일치 | ✅ | "지원→ES·SPI→면접(복수)→내정, 면접 일본어" — Job #27과 동일 구조 |
| C-8 | 업종·사업 특성 | ✅ | "수천만 규모 서비스" — LINE야후 대규모 플랫폼 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | ly-corp 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 프로덕트 플래너 적합. PM_PO도 가능하나 신졸 enum 체계상 수용 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 프로덕트 플래너이므로 적절 |
| E-17 | deadline 정확성 | ❌ | deadline=2026-02-17 이미 경과. isDeadlinePassed=null → PUT 수정 완료 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월/10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 |
| G-23 | 채용 종료 키워드 | ❌ | "2027年度新卒採用エントリー受付は終了しました" 발견. 인턴2026은 별도 수용 중 |
| G-24 | 중복 공고 | ✅ | Job #24~27과 다른 직군 |
| G-25 | 제목 일치 | ✅ | "プロダクトプランナー" → "프로덕트 플래너" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 3, ❌ 2
**판정**: 채용 종료 → isDeadlinePassed=true 처리 완료
**Fix 액션**: 없음.
**Deadline 액션**: ✅ PUT {"isDeadlinePassed": true} → 204. LY Corp 2027 신졸 4건째 종료.

> 📊 LY Corp 누적 4건 (#24, #25, #27, #28) 전부 채용 종료. 연봉 범위: 471만~730만5천엔 (직군별 차등). 전 직군 "エントリー受付は終了しました" 동일 메시지.
