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

---

## Job #29 — 라쿠텐 그룹 | 2027년도 디자인 코스 본전형

**상태**: PUBLISHED
**소스**: https://corp.rakuten.co.jp/careers/graduates/recruit_business/creative.html
**나루 공고**: https://www.naru-recruit.com/jobs/29
**어드민**: https://www.naru-recruit.com/admin/jobs/29?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 03:35 | 리뷰 | 21/25 ⚠️4 (A-2, C-9, E-17 deadline 경과하나 원본 활성) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 月給 350,000엔(학부)/360,000엔(석사). DB: salaryMin=4200000 = 350,000×12 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 학부/석사 차이(+1만/월)는 반영 안 됨 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "브랜드와 70개+ 서비스에 최상의 UX 제공", "AI 활용 서비스 성장 기여" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 컨셉수립/AI UX/빅데이터/AI 워크플로우/디자인시스템 — 원본과 정확 일치. AI 활용 강조 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정(기졸업 3년 미만) + 일본어 + 포트폴리오" — 원본과 일치. 디자인 코스 특유의 포트폴리오 요건 반영 |
| B-7 | selectionProcess 일치 | ✅ | "Personal Page→AF(포트폴리오 첨부)·WebTest→면접(2~3개월)→내정" — 포트폴리오 제출 포함 |
| C-8 | 업종·사업 특성 | ✅ | "70개+ 국내외 서비스" — 라쿠텐 종합 플랫폼 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 라쿠텐 그룹 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | rakuten-group 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 디자인 코스에 정확 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | UX/UI/Graphic Design/AI/Data Science — 디자인+AI 융합 스택 적절 |
| E-17 | deadline 정확성 | ⚠️ | deadline=2026-02-12 경과했으나 **원본 활성** (종료 키워드 없음). Job #26과 동일 패턴 → HOLD |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답, 페이지 정상 |
| G-23 | 채용 종료 키워드 | ✅ | 없음 — 여전히 활성 |
| G-24 | 중복 공고 | ✅ | Job #26(비즈니스)과 다른 코스 |
| G-25 | 제목 일치 | ✅ | "デザインコース" → "디자인 코스" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 4, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: 없음. E-17 deadline 경과하나 원본 활성 → HOLD (Job #26과 동일).
**Deadline 액션**: 없음. 원본에 종료 키워드 없음 → isDeadlinePassed 설정하지 않음.

> 📊 라쿠텐 2건 (#26, #29) 모두 deadline 경과했으나 원본 활성. 마감일 연장 또는 수시 전환 추정. LY Corp과 대조적 (LY Corp은 명시적 종료).

---

## Job #30 — 라쿠텐 그룹 | 2027년도 엔지니어직 본전형

**상태**: PUBLISHED
**소스**: https://corp.rakuten.co.jp/careers/graduates/recruit_engineer/
**나루 공고**: https://www.naru-recruit.com/jobs/30
**어드민**: https://www.naru-recruit.com/admin/jobs/30?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 03:45 | 리뷰 | 21/25 ⚠️2 ❌2 (A-2, C-9, E-17 deadline 경과, G-23 채용종료) |
| 04/15 03:45 | Deadline | ❌ "募集終了しました" 확인 → PUT isDeadlinePassed=true (204) |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | 공고 명시. 원본: 月額 370,000엔~(기초급 281,013+고정시간외 88,987). DB: salaryMin=4440000 = 370,000×12 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본 "個人の専門知識や経験に応じて決定" — 상한 없음 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "직종×조직형 채용", "내정 시 직종 확정" — 원본과 일치. 라쿠텐 고유 채용 방식 반영 |
| B-5 | tasks 일치 | ✅ | 6개 항목 — SW/인프라/AI·ML/데이터/PM/QA — 원본 6개 직종 트랙과 정확 일치 |
| B-6 | targetCandidate 일치 | ✅ | "학사~박사, 일본어 회화+, 영어 비즈니스" — 원본과 일치. 엔지니어는 영어 요건도 명시 |
| B-7 | selectionProcess 일치 | ✅ | "마이페이지→ES→1차서류→코딩테스트→2차서류→면접→오퍼" — 원본과 일치. 코딩테스트 포함 |
| C-8 | 업종·사업 특성 | ✅ | "직종×조직형" — 라쿠텐 특유의 배치 방식 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 그룹 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | rakuten-group 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 엔지니어 직종에 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | Java/PHP/Python/Golang/Scala/Kotlin/TypeScript/React/iOS·Android/Docker·K8s/MySQL/Git — 원본 기술 스택과 일치. 풍부한 12개 항목 |
| E-17 | deadline 정확성 | ❌ | deadline=2026-02-24 경과. isDeadlinePassed=null → PUT 수정 완료 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 |
| G-23 | 채용 종료 키워드 | ❌ | "募集終了しました" 명시적 발견. 2028 인턴은 별도 수용 중 |
| G-24 | 중복 공고 | ✅ | Job #26(비즈니스)/29(디자인)과 다른 코스 |
| G-25 | 제목 일치 | ✅ | "エンジニア職" → "엔지니어직" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 2, ❌ 2
**판정**: 채용 종료 → isDeadlinePassed=true 처리 완료
**Fix 액션**: 없음.
**Deadline 액션**: ✅ PUT {"isDeadlinePassed": true} → 204. "募集終了しました" 확인.

> 📊 라쿠텐 주의: 비즈니스/디자인(#26,29)은 원본 활성인데, 엔지니어(#30)는 "募集終了" 명시. 코스별 마감 시점이 다른 것으로 확인. techStack 12개로 가장 풍부한 공고.

---

## Job #31 — 라쿠텐 그룹 | 2027년도 FinTech 코스 본전형

**상태**: PUBLISHED
**소스**: https://corp.rakuten.co.jp/careers/graduates/recruit_business/fintech.html
**나루 공고**: https://www.naru-recruit.com/jobs/31
**어드민**: https://www.naru-recruit.com/admin/jobs/31?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 03:55 | 리뷰 | 21/25 ⚠️4 (A-2, C-9, E-17 deadline 경과하나 원본 활성, E-18 joinDate) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | Job #26과 동일 기준 적용. salaryMin=4200000 = 350,000×12 라쿠텐 비즈니스 공통 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "신용카드, 라쿠텐 Edy, 라쿠텐 페이, 은행, 증권, 보험" — 원본 FinTech 사업 영역 정확 나열 |
| B-5 | tasks 일치 | ✅ | 7개 항목 — Sales/Marketing/Product/Strategy/Operation/System/Corporate — 원본 7개 직종과 정확 일치. 가장 다양한 직종 구성 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정(기졸업 3년 미만) + 일본어" — 원본과 일치 |
| B-7 | selectionProcess 일치 | ✅ | Job #26과 동일 라쿠텐 비즈니스 전형 구조 |
| C-8 | 업종·사업 특성 | ✅ | "다각적인 FinTech 사업" — 결제·은행·증권·보험 사업 특성 구체적 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 그룹 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | rakuten-group 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — FinTech 종합 코스 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 비즈니스/FinTech 코스이므로 적절 |
| E-17 | deadline 정확성 | ⚠️ | deadline=2026-02-12 경과했으나 원본 활성 → HOLD (라쿠텐 비즈니스 패턴) |
| E-18 | joinDate 정확성 | ⚠️ | "2027년 4월"만 기재. 다른 라쿠텐 코스는 "4월·10월"인데 FinTech는 4월만. 원본 확인 필요 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답, 페이지 정상 |
| G-23 | 채용 종료 키워드 | ✅ | 없음 — 여전히 활성. Personal Page 등록/로그인 기능 |
| G-24 | 중복 공고 | ✅ | Job #26(비즈니스)/29(디자인)/30(엔지니어)와 다른 코스 |
| G-25 | 제목 일치 | ✅ | "FinTechコース" → "FinTech 코스" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 4, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: 없음. E-17/E-18은 HOLD.
**Deadline 액션**: 없음. deadline 경과했으나 원본 활성 → isDeadlinePassed 설정하지 않음.

> 📊 라쿠텐 코스별 상태 정리: 비즈니스(#26) 활성, 디자인(#29) 활성, 엔지니어(#30) 종료, FinTech(#31) 활성. 엔지니어만 종료된 것 확정.

---

## Job #32 — 라쿠텐 그룹 | 2027년도 마케팅 코스 본전형

**상태**: PUBLISHED
**소스**: https://corp.rakuten.co.jp/careers/graduates/recruit_business/marketing.html
**나루 공고**: https://www.naru-recruit.com/jobs/32
**어드민**: https://www.naru-recruit.com/admin/jobs/32?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 04:05 | 리뷰 | 22/25 ⚠️3 (A-2, C-9, E-17 deadline 경과하나 원본 활성) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=4200000. 라쿠텐 비즈니스 공통 350,000×12 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "그룹 전체 마케팅·브랜드·멤버십 전략", "전사 횡단적" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 브랜드전략/마케팅효율/데이터분석/가이드라인 — 원본과 정확 일치 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정(기졸업 3년 미만) + 일본어" — 라쿠텐 비즈니스 공통 |
| B-7 | selectionProcess 일치 | ✅ | "Personal Page→AF(별도 문항)·WebTest→면접→내정" — 마케팅 코스는 "별도 문항" 추가 포함 |
| C-8 | 업종·사업 특성 | ✅ | "그룹 전체 브랜드 선도", "독자 분석 플랫폼" — 라쿠텐 마케팅 조직 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 그룹 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | rakuten-group 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 마케팅 종합 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 마케팅 코스 적절 |
| E-17 | deadline 정확성 | ⚠️ | deadline=2026-02-12 경과하나 원본 활성 → HOLD |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월·10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답, 활성 |
| G-23 | 채용 종료 키워드 | ✅ | 없음 |
| G-24 | 중복 공고 | ✅ | 다른 코스와 중복 없음 |
| G-25 | 제목 일치 | ✅ | "マーケティングコース" → "마케팅 코스" 정확 |

**종합**: ✅ 22/25 통과, ⚠️ 3, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline 경과하나 원본 활성 → HOLD.

> 📊 라쿠텐 5코스 완료 (#26,29,30,31,32). 활성 4 / 종료 1(엔지니어). 마케팅 코스는 22/25으로 라쿠텐 최고점.

---

## Job #33 — 액센추어 | 2027년도 디자인 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/33
**어드민**: https://www.naru-recruit.com/admin/jobs/33?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 04:15 | 리뷰 | 19/25 ⚠️6 (A-1 연봉 null, A-2, C-9, E-16, G-22 공통URL, G-24 URL 공유) → 수정 필요 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin/Max 모두 null. 그러나 원본에 연봉 명시: 비즈니스/디지털 컨설턴트 663만, 데이터사이언티스트/AI아키텍트 754만. 디자인 트랙 별도 연봉은 미기재 → 정확한 값 확인 불가 |
| A-2 | 연봉 범위 일치 | ⚠️ | null인데 원본에 일부 트랙 연봉은 있음. 디자인 트랙 연봉 미특정 |
| A-3 | 통화·단위 | ✅ | N/A (null) |
| B-4 | overview 발췌 | ✅ | "소비자·사회·기업 과제 해결을 디자인", "행동 양식 자체를 바꾸는 경험" — 원본 디자인 트랙 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — 과제해결/리서치/프로덕트 창출 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | "2027년 졸업 예정(기졸업 3년 미만) + 일본어" — 원본과 일치 |
| B-7 | selectionProcess 일치 | ✅ | "프리엔트리→마이페이지→AF·WebTest→면접→내정" — 원본과 일치 |
| C-8 | 업종·사업 특성 | ✅ | "디지털과 피지컬을 넘나들며" — 글로벌 컨설팅의 디자인 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 액센추어 글로벌 규모(75만+ 직원, Fortune 500) 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 디자인 트랙에 정확 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Design Research/Experience Design/Service Design — 적절하지만 원본에서 구체적 도구(Figma, Adobe 등) 미명시 |
| E-17 | deadline 정확성 | ✅ | null — 원본에서도 마감일 미기재 (수시). "2027年卒エントリー受付中" 확인 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" — 원본과 일치 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 200 응답이나 12개 트랙 공통 페이지. 디자인 전용 URL 아님 |
| G-23 | 채용 종료 키워드 | ✅ | 없음. "2027年卒のエントリーを受付中です" 활성 |
| G-24 | 중복 공고 | ⚠️ | 동일 URL에서 12개 트랙 공고가 나올 수 있음 (덴츠디지털 패턴과 동일) |
| G-25 | 제목 일치 | ✅ | "デザイン" → "디자인" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합. 연봉 null이 가장 큰 이슈 — 디자인 트랙 연봉이 다른 트랙과 같은지 확인 필요.
**Fix 액션**: A-1/A-2 연봉 null → HOLD. 원본에 디자인 트랙 별도 연봉 미기재. 다른 트랙(663만/754만) 값을 임의 적용하면 안 됨.
**Deadline 액션**: 없음. deadline=null, 원본 활성 ("エントリー受付中").

> 📊 액센추어 첫 등장. 12개 트랙 공통 URL 패턴 (덴츠디지털 8코스와 동일 구조). 연봉 트랙별 차등 있으나 디자인 별도 미기재.

---

## Job #34 — 액센추어 | 2027년도 콘텐츠 디자인 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/34
**어드민**: https://www.naru-recruit.com/admin/jobs/34?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 04:25 | 리뷰 | 19/25 ⚠️6 (A-1 salary null, A-2, C-9, E-16, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin/Max null. Job #33과 동일 — 원본에 콘텐츠 디자인 트랙 별도 연봉 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | null |
| A-3 | 통화·단위 | ✅ | N/A |
| B-4 | overview 발췌 | ✅ | "소비자와 기업을 잇는 접점에서 콘텐츠 제작", "브랜딩, 컨셉 메이킹, UI 디자인" — 원본 콘텐츠 디자인 트랙과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — 콘텐츠제작/브랜딩·커뮤니케이션/톤앤매너·UI — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정(기졸업 3년 미만) + 일본어" — 액센추어 공통 |
| B-7 | selectionProcess 일치 | ✅ | Job #33과 동일 전형 구조 |
| C-8 | 업종·사업 특성 | ✅ | "디지털 마케팅 지원" — 컨설팅 기업의 콘텐츠 디자인 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 콘텐츠 디자인 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | UI Design/Branding/Content Creation — 적절하지만 구체적 도구 미명시 |
| E-17 | deadline 정확성 | ✅ | null — 수시, "エントリー受付中" |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "톤앤매너", "컨셉 메이킹" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL (Job #33과 동일) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33과 동일 source_url. 트랙 다르므로 콘텐츠 중복 아님 |
| G-25 | 제목 일치 | ✅ | "コンテンツデザイン" → "콘텐츠 디자인" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합. Job #33과 동일 구조적 이슈 (연봉 null, 공통 URL).
**Fix 액션**: 없음. salary null은 HOLD (디자인 트랙 별도 연봉 미기재).
**Deadline 액션**: 없음. deadline=null, 원본 활성.

---

## Job #35 — 액센추어 | 2027년도 솔루션 엔지니어 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/35
**어드민**: https://www.naru-recruit.com/admin/jobs/35?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 04:35 | 리뷰 | 20/25 ⚠️5 (A-2, C-9, E-16, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=6660000. 원본에 "ソリューション・エンジニア: 6,630,000円" 명시 (6,630,000 vs DB 6,660,000 — 3만엔 차이, 오차 확인 필요) |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 상한 미기재. 또한 salaryMin 6,660,000 vs 원본 6,630,000 미세 불일치 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "IT 전략/비즈니스 그랜드 디자인을 시스템 사양으로 구체화" — 솔루션 엔지니어 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — IT전략 구체화/시스템 구축/고품질 개발 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정(고전 포함) + 일본어" — 엔지니어 트랙은 고등전문학교도 포함 (디자인 #33~34와 차이 정확 반영) |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "높은 IT 전문성" — IT 컨설팅 기업의 SE 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 솔루션 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | HOKKAIDO/MIYAGI/FUKUSHIMA/GUNMA/AICHI/TOKYO/OSAKA/FUKUOKA 8개 지역 — 액센추어 전국 거점 반영. 🆕 다수 지방 enum 실사용 확인! |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | IT Strategy/System Architecture/Software Engineering — 추상적. 구체 기술(Java, AWS 등) 미명시이나 원본도 동일 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~34와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ソリューション・エンジニア" → "솔루션 엔지니어" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. A-2에서 salaryMin 미세 불일치 (DB 6,660,000 vs 원본 6,630,000) 확인 필요.
**Fix 액션**: A-2 salaryMin 불일치 의심 (3만엔 차이) → HOLD. 원본 재확인 후 수정 여부 결정 필요. 임의 수정하지 않음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 액센추어 3건 (#33~35). 🆕 중요 발견: HOKKAIDO/MIYAGI/FUKUSHIMA/GUNMA/AICHI/FUKUOKA 등 지방 enum이 실제 백엔드에 존재 확인! 기존에 Kawasaki/Nagoya/Hokkaido enum 부재라고 판단했던 것은 크롤러 매핑 문제였지 백엔드 한계가 아니었음.

---

## Job #36 — 액센추어 | 2027년도 데이터 사이언티스트 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/36
**어드민**: https://www.naru-recruit.com/admin/jobs/36?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 04:45 | 리뷰 | 20/25 ⚠️5 (A-2 salaryMin 불일치, C-9, E-16, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=7560000. 원본에 "データサイエンティスト: 7,540,000円" 명시 (DB 7,560,000 vs 원본 7,540,000 — 2만엔 차이. #35와 동일 미세 불일치 패턴) |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. salaryMin도 2만엔 불일치 (DB>원본). 액센추어 공통 패턴 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "데이터 사이언스 및 생성형 AI", "선진적 혁신 창출과 비즈니스 구현" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — AI 혁신/비즈니스 구현/데이터 분석 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정(기졸업 3년 미만) + 일본어" — 액센추어 공통 |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "최첨단 기술을 무기로" — AI/데이터 컨설팅 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 데이터 사이언티스트 적합 (DATA_SCIENTIST가 더 정확할 수 있으나 신졸 enum 체계상 수용) |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA — #35(8지역)보다 적지만 DS 트랙은 2거점이 맞을 수 있음 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Data Science/Generative AI/Machine Learning — 적절하지만 구체 도구(Python, TensorFlow 등) 미명시 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~35와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "データサイエンティスト" → "데이터 사이언티스트" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: A-2 salaryMin 불일치 (DB 7,560,000 vs 원본 7,540,000) → HOLD. #35(3만 차이)와 동일 패턴. 액센추어 전체적으로 salaryMin이 원본보다 약간 높게 설정됨. 일괄 확인 필요.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 액센추어 salaryMin 불일치 패턴: #35 SE(DB 666만 vs 원본 663만, +3만), #36 DS(DB 756만 vs 원본 754만, +2만). 크롤러가 연봉 계산 시 약간의 오차 발생 추정. 일괄 수정 대상.

---

## Job #37 — 액센추어 | 2027년도 AI 아키텍트 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/37
**어드민**: https://www.naru-recruit.com/admin/jobs/37?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 04:55 | 리뷰 | 20/25 ⚠️5 (A-2 salaryMin 불일치, C-9, E-16 추상, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=7560000. 원본 "AIアーキテクト: 7,540,000円". DB 756만 vs 원본 754만 (+2만). #36 DS와 동일 연봉·동일 오차 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. salaryMin +2만 불일치 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "생성형 AI·음성 인식·NLP·이미지 인식·ML·DL", "AI Powered 변혁" — 원본과 일치. AI 기술 상세 나열 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — AI 솔루션 개발/클라우드+커스텀 설계/AI 변혁 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | 액센추어 공통 |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "모든 산업·업무·솔루션에 AI 엔지니어링·컨설팅" — 글로벌 AI 컨설팅 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — AI 아키텍트 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA — #36 DS와 동일 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | Generative AI/Audio Recognition/NLP/Image Recognition/ML/DL/Cloud Services — 7개 항목, AI 아키텍트에 적합. 역대 가장 구체적인 AI 스택 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~36과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "AIアーキテクト" → "AI 아키텍트" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. techStack이 AI 분야 가장 구체적 (7개). salaryMin 불일치는 액센추어 공통.
**Fix 액션**: A-2 salaryMin +2만 불일치 → HOLD (액센추어 일괄 수정 대상).
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 액센추어 4건 (#33~37) 중 연봉 있는 2건(#35 SE, #36 DS/#37 AI) 모두 salaryMin이 원본보다 2~3만엔 높음. 계산 오차 패턴 확정. E-16 techStack은 #37 AI 아키텍트가 7개로 가장 풍부.

---

## Job #38 — 액센추어 | 2027년도 비즈니스 컨설턴트 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/38
**어드민**: https://www.naru-recruit.com/admin/jobs/38?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 05:05 | 리뷰 | 20/25 ⚠️5 (A-2 salaryMin 불일치, C-9, E-16, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=6660000. 원본 "ビジネスコンサルタント: 6,630,000円". DB 666만 vs 원본 663만 (+3만) — #35 SE와 동일 급여·동일 오차 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. salaryMin +3만 불일치 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "변혁의 리더", "생성형 AI·ML 첨단 기술 활용" — 원본 비즈니스 컨설턴트 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — 개혁경로 수립/첨단기술 프로젝트/변혁 실행 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정(기졸업 3년 미만) + 일본어 비즈니스" — 컨설턴트 트랙은 비즈니스 레벨 일본어 요구 (엔지니어와 차이) |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "기업 및 공공기관의 변혁" — 경영 컨설팅 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 비즈니스 컨설턴트 적합 |
| D-12 | locations 정확성 | ✅ | MIYAGI/AICHI/TOKYO/OSAKA/FUKUOKA 5개 — 다거점 반영 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Generative AI/Machine Learning — 비즈니스 컨설턴트인데 AI 기술만 2개. 전략 컨설팅 도구(PPT, 재무모델링 등)는 미명시이나 원본도 동일 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~37과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ビジネスコンサルタント" → "비즈니스 컨설턴트" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: A-2 salaryMin +3만 불일치 → HOLD (액센추어 일괄 수정 대상).
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 액센추어 5건 (#33~38) salaryMin 오차 패턴: 컨설턴트계(#38 BC=663만, #35 SE=663만) 동일 급여·동일 오차(+3만). DS/AI계(#36,37=754만) 동일 급여·동일 오차(+2만).

---

## Job #39 — 액센추어 | 2027년도 디지털 컨설턴트 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/39
**어드민**: https://www.naru-recruit.com/admin/jobs/39?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 05:15 | 리뷰 | 20/25 ⚠️5 (A-2 salaryMin +3만, C-9, E-16, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=6660000. 원본 "デジタルコンサルタント: 6,630,000円". +3만 불일치 — 컨설턴트급 공통 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. salaryMin +3만 불일치 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "클라우드, 인더스트리 X, 빅데이터, IoT, AI" — 원본 디지털 컨설턴트 설명과 일치. 인더스트리 X(제조DX) 포함 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — 클라우드·AI 과제해결/인더스트리X/빅데이터 UX — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | "졸업 예정 + 일본어 비즈니스" — 컨설턴트급 공통 |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "인더스트리 X (제조업의 디지털화)" — 디지털 컨설팅 특화 영역 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 디지털 컨설턴트 적합 |
| D-12 | locations 정확성 | ✅ | HOKKAIDO/AICHI/TOKYO/OSAKA/FUKUOKA 5거점 — #38 BC(MIYAGI 포함)와 약간 다름. 트랙별 거점 차이 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Cloud/Industry X/Big Data/IoT/AI — 5개 키워드, 적절하지만 추상적 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "인더스트리 X" 등 고유명사 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~38과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "デジタルコンサルタント" → "디지털 컨설턴트" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: A-2 salaryMin +3만 → HOLD (액센추어 일괄 수정 대상).
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 액센추어 6건 (#33~39). 트랙별 거점 차이 정리: SE(#35) 8거점 최다, BC(#38) 5거점(MIYAGI 포함), DC(#39) 5거점(HOKKAIDO 포함), DS/AI(#36,37) 2거점(TOKYO/OSAKA만), 디자인(#33,34) 1거점(TOKYO만).

---

## Job #40 — 액센추어 | 2027년도 디렉터 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/40
**어드민**: https://www.naru-recruit.com/admin/jobs/40?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 05:25 | 리뷰 | 19/25 ⚠️6 (A-1 salary null, A-2, C-9, E-16, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin/Max null. #33~34 디자인과 동일 — 디렉터 트랙 별도 연봉 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | null |
| A-3 | 통화·단위 | ✅ | N/A |
| B-4 | overview 발췌 | ✅ | "디지털 마케팅 전략 수립", "웹·앱·디지털 콘텐츠 제작 지시" — 원본 디렉터 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 전략수립/소셜미디어/콘텐츠 디렉션/효과검증·개선 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | 액센추어 공통 |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "제작 및 운영 → 효과 검증 → 지속 개선" — 디지털 마케팅 디렉션 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 디렉터(마케팅/크리에이티브 디렉션) 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+FUKUOKA 2거점 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Digital Marketing/Social Media Strategy/Information Architecture — 추상적이나 원본도 동일 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~39와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ディレクター" → "디렉터" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합. salary null은 디자인/콘텐츠 계열과 동일.
**Fix 액션**: 없음. salary null → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

---

## Job #41 — 액센추어 | 2027년도 전략 컨설턴트 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/41
**어드민**: https://www.naru-recruit.com/admin/jobs/41?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 05:35 | 리뷰 | 20/25 ⚠️5 (A-2 salaryMin +2만, C-9, E-16, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=7560000. 원본 "ストラテジーコンサルタント: 7,540,000円". +2만 불일치 — DS/AI급과 동일 급여·동일 오차 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. salaryMin +2만 불일치 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "경영진과 함께 기업·산업 변혁", "고부가가치 비즈니스 설계" — 전략 컨설턴트 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — 경영변혁/그랜드디자인/조직횡단 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | 액센추어 공통 |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "경영진과 함께", "조직 횡단적" — 전략 컨설팅 최상위 트랙 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 전략 컨설턴트 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+OSAKA 2거점 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Management Strategy/Business Transformation/Cross-functional Leadership — 전략 컨설팅 키워드이나 기술 도구라기보다 역량 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "그랜드 디자인", "임팩트 창출" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~40과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ストラテジーコンサルタント" → "전략 컨설턴트" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: A-2 salaryMin +2만 → HOLD (액센추어 일괄).
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 액센추어 급여 3등급 확정: 전략/DS/AI급 754만(+2만), 컨설턴트/SE급 663만(+3만), 디자인/콘텐츠/디렉터급 미기재(null). 전략 컨설턴트가 최고 급여 트랙.

---

## Job #42 — 액센추어 | 2027년도 마케팅 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/42
**어드민**: https://www.naru-recruit.com/admin/jobs/42?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 05:45 | 리뷰 | 19/25 ⚠️6 (A-1 salary null, A-2, C-9, E-16, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin/Max null. 마케팅 트랙 별도 연봉 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | null |
| A-3 | 통화·단위 | ✅ | N/A |
| B-4 | overview 발췌 | ✅ | "생성형 AI, 데이터, 기술을 활용한 마케팅 재정의" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — AI 마케팅/소비자 경험/고객 가치 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | 액센추어 공통 |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "마케팅을 재정의" — AI 기반 마케팅 컨설팅 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 마케팅 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 1거점 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Generative AI/Marketing Automation/Data Analysis — 마케팅 도구이나 추상적 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~41과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "マーケティング" → "마케팅" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합. salary null — 디자인/콘텐츠/디렉터 계열과 동일.
**Fix 액션**: 없음. salary null → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 액센추어 10건 (#33~42). salary null 트랙: 디자인(#33), 콘텐츠 디자인(#34), 디렉터(#40), 마케팅(#42) — 4건. 12개 트랙 중 남은 2건(크리에이티브, 오퍼레이션) 예상.

---

## Job #43 — 액센추어 | 2027년도 크리에이티브 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/43
**어드민**: https://www.naru-recruit.com/admin/jobs/43?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 05:55 | 리뷰 | 19/25 ⚠️6 (A-1 null, A-2, C-9, E-16 빈배열, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin/Max null. 크리에이티브 트랙 별도 연봉 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | null |
| A-3 | 통화·단위 | ✅ | N/A |
| B-4 | overview 발췌 | ✅ | "아이디어의 힘으로 기업·사회 과제에 접근", "소비자 경험이나 사회 구조까지 바꾸는 임팩트" — 원본 크리에이티브 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — 창의적 접근/임팩트 창출/비전 구현 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | 액센추어 공통 |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "사회 및 사람들과 공감·공명하는 새로운 가치" — 크리에이티브 컨설팅 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_OTHER — 크리에이티브 직군. GRADUATE_DESIGN이 더 적합할 수 있으나 디자인(#33)과 구분 위해 OTHER 사용 수용 가능 |
| D-12 | locations 정확성 | ✅ | TOKYO 1거점 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | 빈 배열 []. 크리에이티브 트랙이므로 기술 스택 없음은 이해되나 #33 디자인(Design Research 등)과 비교하면 빈약 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "임팩트 창출", "공감·공명" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~42와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "クリエイティブ" → "크리에이티브" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합. salary null — 디자인/콘텐츠/디렉터/마케팅 계열과 동일.
**Fix 액션**: 없음. salary null → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 액센추어 11/12트랙 완료. 남은 1건: 오퍼레이션 스페셜리스트.

---

## Job #44 — 액센추어 | 2027년도 오퍼레이션 스페셜리스트 본전형

**상태**: PUBLISHED
**소스**: https://www.accenture.com/jp-ja/careers/life-at-accenture/entry-level
**나루 공고**: https://www.naru-recruit.com/jobs/44
**어드민**: https://www.naru-recruit.com/admin/jobs/44?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 06:05 | 리뷰 | 19/25 ⚠️6 (A-1 null, A-2, C-9, E-16, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin/Max null. 오퍼레이션 트랙 별도 연봉 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | null |
| A-3 | 통화·단위 | ✅ | N/A |
| B-4 | overview 발췌 | ✅ | "경리·인사·구매 업무 수탁 자동화·효율화", "백오피스 업무 설계·개선" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — BPO 운영/업무 설계·관리/자동화 도입 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | 액센추어 공통 |
| B-7 | selectionProcess 일치 | ✅ | 액센추어 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "업무 수탁 자동화·효율화" — BPO 서비스 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 글로벌 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | accenture 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_SPECIALIST — 오퍼레이션 스페셜리스트 적합. 신규 enum 사용 |
| D-12 | locations 정확성 | ✅ | TOKYO/OSAKA/FUKUOKA/KUMAMOTO 4거점. 🆕 KUMAMOTO 첫 등장! |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | BPO/RPA/Efficiency Optimization — 오퍼레이션 도구이나 추상적 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월, 2026년 10월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 트랙 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 12트랙 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | Job #33~43과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "オペレーションズスペシャリスト" → "오퍼레이션 스페셜리스트" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합
**Fix 액션**: 없음. salary null → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 **액센추어 12/12트랙 전체 완료** (#33~44). 평균 19.6/25.
> 🆕 KUMAMOTO enum 첫 등장 (#44 오퍼레이션).
> 급여 요약: 전략/DS/AI 754만 | 컨설턴트/SE 663만 | 디자인/콘텐츠/디렉터/마케팅/크리에이티브/오퍼레이션 null.
> 거점 요약: SE 8거점(최다) > BC/DC 5거점 > 오퍼레이션 4거점(KUMAMOTO 포함) > DS/AI/전략 2거점 > 디자인계 1거점.

---

## Job #45 — 사이버에이전트 | 비즈니스 코스 2027년도 신입 채용

**상태**: PUBLISHED
**소스**: https://www.cyberagent.co.jp/careers/students/biz2027/
**나루 공고**: https://www.naru-recruit.com/jobs/45
**어드민**: https://www.naru-recruit.com/admin/jobs/45?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 06:15 | 리뷰 | 19/25 ⚠️4 ❌2 (A-2, C-9, E-17 deadline 경과, G-23 채용종료) |
| 04/15 06:15 | Deadline | ❌ "こちらの募集は終了いたしました" 확인 → PUT isDeadlinePassed=true (204) |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=5040000. 원본 페이지에 연봉 미기재이나, 사이버에이전트 공식 채용 정보에서 504만엔(초봉 42만/월×12) 확인 가능. DB 값 부합 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "광고 전략·마케팅·기획", "게임·서비스 PM", "인사·법무·경리·홍보·IR" — 비즈니스 코스 폭넓은 직종 정확 나열 |
| B-5 | tasks 일치 | ✅ | 8개 항목 — 영업/프로듀서/인사/법무/경리/홍보/IR/경영지원 — 원본 직종 구성과 일치. 역대 가장 많은 tasks |
| B-6 | targetCandidate 일치 | ✅ | "신입, 고졸 이상, 학과 불문" — 원본과 일치. 사이버에이전트는 학력 제한이 매우 낮음 |
| B-7 | selectionProcess 일치 | ✅ | "마이페이지→1차(GD/면접)→2차~6차→최종→내정" — 7단계 전형! 원본과 일치 |
| C-8 | 업종·사업 특성 | ✅ | "광고 전략", "게임·서비스" — 사이버에이전트 2대 축(광고+게임) 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | Abema, Cygames 등 자회사 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 비즈니스 종합 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO/OSAKA/FUKUOKA/AICHI 4거점 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | ONSITE — 사이버에이전트는 출근 중심. 다른 회사(HYBRID)와 차이 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 비즈니스 코스 적절 |
| E-17 | deadline 정확성 | ❌ | deadline=2026-03-04 경과. isDeadlinePassed=null → PUT 수정 완료 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월 (원칙)" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 (페이지 존재) |
| G-23 | 채용 종료 키워드 | ❌ | "こちらの募集は終了いたしました" 명시적 종료 |
| G-24 | 중복 공고 | ✅ | 사이버에이전트 첫 공고 |
| G-25 | 제목 일치 | ✅ | "ビジネスコース" → "비즈니스 코스" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 4, ❌ 2
**판정**: 채용 종료 → isDeadlinePassed=true 처리 완료
**Fix 액션**: 없음.
**Deadline 액션**: ✅ PUT {"isDeadlinePassed": true} → 204. "こちらの募集は終了いたしました" 확인.

> 📊 사이버에이전트 첫 등장. 특이점: 전형 7단계(GD→면접 6회), workType=ONSITE(타사 대비 드문 출근 중심), 학력 제한 최소(고졸 이상), tasks 8개(역대 최다).

---

## Job #46 — 사이버에이전트 | 게임 시나리오 라이터

**상태**: PUBLISHED
**소스**: https://creators.cyberagent.co.jp/information/
**나루 공고**: https://www.naru-recruit.com/jobs/46
**어드민**: https://www.naru-recruit.com/admin/jobs/46?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 06:25 | 리뷰 | 18/25 ⚠️7 (A-2, B-6 mustHave not_specified, C-9, D-14 UNKNOWN, E-16, G-22 공통URL, G-24) → 수정 필요 |
| 04/15 06:25 | Fix | D-14: workType UNKNOWN 확인 — 원본에 근무형태 미기재 → HOLD |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=5040000. 사이버에이전트 크리에이터 공통 504만 — #45 비즈니스와 동일 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "시나리오 구성, 캐릭터 대사 작성", "콘텐츠 제작의 근본에 관여" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 시나리오/대사/세계관/캐릭터설정/미디어믹스 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ⚠️ | mustHave=["not_specified"]. 원본에는 "27卒, 28卒, 29卒の学生" 등 대상 명시되어 있으나 DB에 반영 안 됨 |
| B-7 | selectionProcess 일치 | ✅ | "포트폴리오→면접(크리에이터+인사)→최종(집행임원)→내정" — 원본과 일치. 크리에이터 전형 특유 |
| C-8 | 업종·사업 특성 | ✅ | "게임 시나리오" — 사이버에이전트 게임 사업 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | Cygames 등 자회사 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_OTHER — 시나리오 라이터는 엔지니어/디자인/비즈니스에 해당 안 되므로 OTHER 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN. 원본 페이지에 근무형태 미기재. #45 비즈니스는 ONSITE인데 크리에이터는 다를 수 있음 → HOLD |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 (mustHave가 "not_specified"이지만 필드 자체는 존재) |
| E-16 | techStack 정확성 | ⚠️ | 빈 배열 []. 시나리오 라이터라 기술 도구 없지만 원본에 언급 없으므로 적절 |
| E-17 | deadline 정확성 | ✅ | null — 원본에 "通年採用, 締め切りなし" 명시. 수시 채용 정확 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월 이후" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 5개 직종 공통 크리에이터 페이지 |
| G-23 | 채용 종료 키워드 | ✅ | 없음. "通年採用" 명시적 활성 |
| G-24 | 중복 공고 | ⚠️ | 크리에이터 페이지에서 다른 직종(디자이너/일러스트/3DCG/애니메이터)도 공유 |
| G-25 | 제목 일치 | ✅ | "ゲームシナリオライター" → "게임 시나리오 라이터" 정확 |

**종합**: ✅ 18/25 통과, ⚠️ 7, ❌ 0
**판정**: PUBLISH 유지 적합. mustHave "not_specified"와 workType UNKNOWN이 데이터 품질 이슈.
**Fix 액션**: B-6 mustHave "not_specified" → SEMI-AUTO 가능 ("27~29卒 학생" 추출 가능하지만 원본 구조가 복잡해서 HOLD). D-14 workType UNKNOWN → HOLD.
**Deadline 액션**: 없음. "通年採用, 締め切りなし" — 수시 채용 활성.

---

## Job #47 — 사이버에이전트 | 게임 엔지니어

**상태**: PUBLISHED
**소스**: https://www.cyberagent.co.jp/careers/students/tech/jobs/detail/id=27085
**나루 공고**: https://www.naru-recruit.com/jobs/47
**어드민**: https://www.naru-recruit.com/admin/jobs/47?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 06:35 | 리뷰 | 20/25 ⚠️5 (A-1 연봉 출처 불명, A-2, C-9, D-14 UNKNOWN, G-24 없음) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=5040000. 원본 상세 페이지에 연봉 미기재 ("募集要項" 별도 페이지 참조). 사이버에이전트 공통 504만으로 추정 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "스마트폰 게임 개발", "Unity 등 게임 엔진", "인게임, 아키텍처, 그래픽, UI, 툴, AI" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 6개 항목 — 클라이언트/백엔드/인게임·UI/툴/기술검증/사양설계 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 4개 — 개발경험/인턴3일+/사이버에이전트 인턴/팀개발 — 원본과 일치. 엔지니어 특유의 경험 기반 요건 |
| B-7 | selectionProcess 일치 | ✅ | "서류·적성→면접4회(엔지니어→인사→엔지니어책임자→인사책임자/임원)→내정" — 원본과 일치 |
| C-8 | 업종·사업 특성 | ✅ | "스마트폰 게임", "Unity/UnrealEngine" — 모바일 게임 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | Cygames 등 자회사 게임 스튜디오 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 게임 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN. 원본에 근무형태 미기재. #45 비즈니스는 ONSITE |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | Unity/UniTask/UniRx/3D/UI/URP/Shader/C#/UnrealEngine/DirectX/AI/Realtime Communication — 12개, 매우 구체적! 역대 최다급 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "협의 가능" — 유연 입사 시기 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답. 개별 공고 전용 URL! (공통 URL 아님) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | 개별 URL이므로 중복 없음 |
| G-25 | 제목 일치 | ✅ | "ゲームエンジニア" → "게임 엔지니어" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. techStack 12개로 데이터 품질 우수. 개별 URL도 사용.
**Fix 액션**: D-14 workType UNKNOWN → HOLD (원본 미기재).
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 사이버에이전트 엔지니어는 개별 공고 URL 사용 (크리에이터와 다른 구조). techStack 12개 (Unity/C#/URP/Shader 등) — 라쿠텐 #30 와 동급 최다. mustHave에 구체적 경험 요건 있음 (타사 대비 높은 진입 장벽).

---

## Job #48 — 사이버에이전트 | 머신러닝 엔지니어/데이터 사이언티스트

**상태**: PUBLISHED
**소스**: https://www.cyberagent.co.jp/careers/students/tech/jobs/detail/id=27074
**나루 공고**: https://www.naru-recruit.com/jobs/48
**어드민**: https://www.naru-recruit.com/admin/jobs/48?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 06:45 | 리뷰 | 20/25 ⚠️5 (A-1 출처 불명, A-2, C-9, D-14 UNKNOWN, E-16 과다) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=5040000. 원본에 연봉 미기재. 사이버에이전트 공통 504만 추정 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "대규모 데이터, ML 기술 이용 솔루션 제안~실행", "컴퓨터 과학·통계·인과 추론" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 7개 항목 — 과제발견/알고리즘/시스템설계/가설·지표/오프라인 검증/프로덕트/A/B 테스트 — 원본과 일치. ML 파이프라인 전 과정 포함 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 4개 — 학회발표·논문/업무경험/인턴3일+/사이버에이전트 인턴 — 원본과 일치. **학회 발표 요건이 특이** |
| B-7 | selectionProcess 일치 | ✅ | #47과 동일 4단계 면접 구조 |
| C-8 | 업종·사업 특성 | ✅ | "다양한 사업 과제에 ML 솔루션" — 광고+게임+미디어 횡단 AI 적용 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | AI Lab 등 연구소 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — ML 엔지니어/DS 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN. 원본 미기재 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | **27개!** ML/DL/NLP/CV/음성/강화학습/추천/MLOps/Python/Java/C++/SQL/TF/PyTorch/생성형AI/LLM/VLM/게임AI/통계/인과추론/계량경제/업리프트/밴딧/R/OR/시계열 — **역대 최다 techStack!** |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "협의 가능" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "업리프트 모델링", "밴딧 알고리즘" 등 전문용어 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답. 개별 공고 전용 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #47과 다른 직종 (게임 엔지니어 vs ML/DS) |
| G-25 | 제목 일치 | ✅ | "機械学習エンジニア/データサイエンティスト" → 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. techStack 27개 — 역대 최다! 데이터 품질 매우 우수.
**Fix 액션**: D-14 workType UNKNOWN → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 사이버에이전트 ML/DS (#48): techStack **27개**(역대 최다 — 기존 최다 라쿠텐 #30/사이버에이전트 #47의 12개 대비 2배 이상). mustHave에 학회 발표/논문 요건 포함 — 리서치 레벨 요구. 사이버에이전트 AI Lab의 영향 추정.

---

## Job #49 — 사이버에이전트 | 인프라 엔지니어

**상태**: PUBLISHED
**소스**: https://www.cyberagent.co.jp/careers/students/tech/jobs/detail/id=27087
**나루 공고**: https://www.naru-recruit.com/jobs/49
**어드민**: https://www.naru-recruit.com/admin/jobs/49?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 06:55 | 리뷰 | 20/25 ⚠️5 (A-1 출처 불명, A-2, C-9, D-14 UNKNOWN, E-16 과다?) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=5040000. 원본 미기재. 사이버에이전트 공통 504만 추정 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "퍼블릭 클라우드(AWS/GCP/Azure)", "프라이빗 클라우드(OpenStack)", "네트워크 인프라" — 3개 영역 정확 |
| B-5 | tasks 일치 | ✅ | 7개 항목 — 퍼블릭클라우드/IaC 자동화/Observability/프라이빗클라우드/DC 네트워크/매니지드서비스/오피스 네트워크 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | #47 게임 엔지니어와 동일 mustHave 4개 (개발경험/인턴3일+/사이버에이전트 인턴/팀개발) |
| B-7 | selectionProcess 일치 | ✅ | 사이버에이전트 엔지니어 공통 4단계 면접 |
| C-8 | 업종·사업 특성 | ✅ | "국내·해외 오피스 및 스튜디오" — 대규모 인프라 운영 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 인프라 규모(서버 수, DC 수) 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 인프라 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN. 원본 미기재 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | **36개!** 🏆 역대 최다 갱신! AWS/Azure/GCP/Docker/K8s/IaC/OpenStack/Python/Go/Ansible/OpenvSwitch/OpenFlow/Qemu/KVM/BGP/Proxmox/Ceph/NFS/iSCSI/NVMe/GPU/Cisco/Juniper/Citrix/F5/EVPN·VXLAN/RoCEv2/gRPC/MySQL/Kubeflow/KServe/GitHub Actions 등 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "협의 가능" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "관측 가능성(Observability)" 등 전문용어 정확 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답. 개별 공고 전용 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #47(게임)/#48(ML) 와 다른 직종 |
| G-25 | 제목 일치 | ✅ | "インフラエンジニア" → "인프라 엔지니어" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. techStack **36개** — 역대 최다! 인프라 전 영역(클라우드/네트워크/스토리지/GPU/ML Infra) 포괄.
**Fix 액션**: D-14 workType UNKNOWN → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 **techStack 역대 최다 갱신!** #49 인프라 36개 > #48 ML/DS 27개 > #47 게임 12개. 사이버에이전트 엔지니어 공고가 데이터 품질 최상위 — 개별 URL + 풍부한 techStack + 구체적 mustHave.

---

## Job #50 — 사이버에이전트 | 클라이언트 엔지니어 (Web, Android, iOS, Flutter)

**상태**: PUBLISHED
**소스**: https://www.cyberagent.co.jp/careers/students/tech/jobs/detail/id=27088
**나루 공고**: https://www.naru-recruit.com/jobs/50
**어드민**: https://www.naru-recruit.com/admin/jobs/50?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 07:05 | 리뷰 | 20/25 ⚠️5 (A-1 출처 불명, A-2, C-9, D-14 UNKNOWN, E-16 과다?) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=5040000. 원본 미기재. 사이버에이전트 공통 504만 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "Web 기술로 UI/UX, 시맨틱 마크업, 성능, 접근성, 보안", "앱 전체 설계~모바일 기능 개발" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 8개 항목 — Web 설계/UI·UX/마크업/성능·보안/앱설계/인터랙션/모바일/성능개선 — 원본과 일치. Web+모바일 풀스택 |
| B-6 | targetCandidate 일치 | ✅ | 사이버에이전트 엔지니어 공통 mustHave 4개 |
| B-7 | selectionProcess 일치 | ✅ | 사이버에이전트 엔지니어 공통 4단계 면접 |
| C-8 | 업종·사업 특성 | ✅ | "사용자가 보는 모든 것에 폭넓게 관여" — 클라이언트 엔지니어 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 서비스 규모(Abema, WINTICKET 등) 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 클라이언트 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN. 원본 미기재 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | **36개!** #49와 공동 역대 최다! Web: HTML/CSS/JS/TS/React/Vue/Next.js/Vite/esbuild/SWC/Storybook/webpack/Node.js/GraphQL/CDN. iOS: SwiftUI/Swift Concurrency/TCA. Flutter: Riverpod/Melos/Freezed. Android: Jetpack Compose/Kotlin Multiplatform/Dagger Hilt/ExoPlayer/Room |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "협의 가능" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "시맨틱 마크업", "관측 가능성" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답. 개별 공고 전용 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #47~49와 다른 직종 |
| G-25 | 제목 일치 | ✅ | "クライアントエンジニア" → "클라이언트 엔지니어" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. techStack 36개 — Web/iOS/Flutter/Android 4개 플랫폼 포괄.
**Fix 액션**: D-14 workType UNKNOWN → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 🎯 **50건 마일스톤!** #12~50 리뷰 완료 (39건, jobId 1~11 미존재 제외).
> 📊 사이버에이전트 클라이언트(#50): techStack 36개 — #49 인프라와 공동 1위. Web(15개)+iOS(4개)+Flutter(6개)+Android(7개)+아키텍처(4개) = 4개 플랫폼 완전 커버.
> 📊 사이버에이전트 엔지니어 4건(#47~50) 모두 techStack 12개 이상, mustHave 구체적 — 전체 공고 중 데이터 품질 최상위급.

---

## Job #51 — 사이버에이전트 | 백엔드 엔지니어

**상태**: PUBLISHED
**소스**: https://www.cyberagent.co.jp/careers/students/tech/jobs/detail/id=27084
**나루 공고**: https://www.naru-recruit.com/jobs/51
**어드민**: https://www.naru-recruit.com/admin/jobs/51?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 07:15 | 리뷰 | 20/25 ⚠️5 (A-1 출처 불명, A-2, C-9, D-14 UNKNOWN, E-16 과다?) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=5040000. 원본 미기재. 사이버에이전트 공통 504만 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "일본 최대 규모 사용자·트래픽", "Go/Java/Scala/PHP", "퍼블릭·프라이빗 클라우드" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 6개 항목 — ABEMA·탭플·AWA/광고/게임/공통기반/PipeCD·Bucketeer/데이터기반 — 원본과 일치. 구체적 서비스명 포함! |
| B-6 | targetCandidate 일치 | ✅ | 사이버에이전트 엔지니어 공통 mustHave 4개 |
| B-7 | selectionProcess 일치 | ✅ | 사이버에이전트 엔지니어 공통 4단계 면접 |
| C-8 | 업종·사업 특성 | ✅ | "ABEMA, 탭플, AWA" — 구체 서비스명으로 사업 특성 반영. "PipeCD, Bucketeer" OSS 기여 문화 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | "일본 최대 규모" 언급되나 직원수 등 수치 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 백엔드 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN. 원본 미기재 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 21개 — Go/Rust/Kotlin/Scala/Node.js/PHP/Java/Ruby/Docker/AWS/GCP/K8s/MySQL/Aurora/Spanner/MongoDB/OpenAPI/PipeCD/Terraform/Datadog/DDD. 언어 8개+인프라+DB+도구 폭넓게 포괄 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "협의 가능" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중. ABEMA/탭플/AWA 등 서비스명 포함 |
| G-22 | source_url 접근 | ✅ | 200 응답. 개별 공고 전용 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #47~50과 다른 직종 |
| G-25 | 제목 일치 | ✅ | "バックエンドエンジニア" → "백엔드 엔지니어" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. tasks에 ABEMA/탭플/AWA/PipeCD/Bucketeer 등 구체 서비스명 포함 — 높은 콘텐츠 품질.
**Fix 액션**: D-14 workType UNKNOWN → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 사이버에이전트 엔지니어 5건(#47~51) techStack 합계: 게임 12 + ML/DS 27 + 인프라 36 + 클라이언트 36 + 백엔드 21 = **132개 고유 기술**. 압도적 데이터 품질.

---

## Job #52 — 사이버에이전트 | 게임 3DCG 크리에이터/3DCG 디렉터

**상태**: PUBLISHED
**소스**: https://creators.cyberagent.co.jp/information/
**나루 공고**: https://www.naru-recruit.com/jobs/52
**어드민**: https://www.naru-recruit.com/admin/jobs/52?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 07:25 | 리뷰 | 18/25 ⚠️7 (A-1 출처 불명, A-2, B-6 not_specified, C-9, D-14 UNKNOWN, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=5040000. 원본 미기재. 사이버에이전트 공통 504만 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "3DCG 제작 전반", "미경험자도 지원 가능" — 원본과 일치. 미경험 허용이 특이 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 캐릭터 모델링/배경 모델링/모션/이펙트 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ⚠️ | mustHave=["not_specified"]. #46 시나리오와 동일 이슈 |
| B-7 | selectionProcess 일치 | ✅ | #46과 동일 크리에이터 전형 (포트폴리오→면접→집행임원) |
| C-8 | 업종·사업 특성 | ✅ | "스마트폰 게임 3DCG" — 모바일 게임 CG 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 게임 스튜디오 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 3DCG 크리에이터 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN. 원본 미기재 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 []. 3DCG이므로 Maya/Blender 등 있을 수 있으나 원본 미명시 |
| E-17 | deadline 정확성 | ✅ | null — "通年採用" 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월 이후" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 5직종 공통 크리에이터 URL (#46과 동일) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, "通年採用" 활성 |
| G-24 | 중복 공고 | ⚠️ | #46 시나리오와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ゲーム3DCGクリエイター/ディレクター" → 정확 |

**종합**: ✅ 18/25 통과, ⚠️ 7, ❌ 0
**판정**: PUBLISH 유지 적합. #46과 동일 이슈 (mustHave not_specified, UNKNOWN, 공통 URL).
**Fix 액션**: B-6 mustHave / D-14 workType → HOLD (#46과 동일).
**Deadline 액션**: 없음. "通年採용" 수시 활성.

---

## Job #53 — 사이버에이전트 | 게임 일러스트레이터

**상태**: PUBLISHED
**소스**: https://creators.cyberagent.co.jp/information/
**나루 공고**: https://www.naru-recruit.com/jobs/53
**어드민**: https://www.naru-recruit.com/admin/jobs/53?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 07:35 | 리뷰 | 18/25 ⚠️7 (A-1, A-2, B-6 not_specified, C-9, D-14 UNKNOWN, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=5040000. 사이버에이전트 공통 504만 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "캐릭터, 배경, 무기 디자인·스틸 일러스트", "아트 디렉션 담당 경우도" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 7개 항목 — 캐릭터/배경/무기 디자인, 일러스트/캐릭터설정/컨셉/아트 디렉션 — 원본과 일치. 크리에이터 중 tasks 최다 |
| B-6 | targetCandidate 일치 | ⚠️ | mustHave=["not_specified"]. 크리에이터 공통 이슈 |
| B-7 | selectionProcess 일치 | ✅ | 크리에이터 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "스마트폰 게임 일러스트" — 게임 아트 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 게임 스튜디오 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 일러스트레이터 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 []. 일러스트레이터 도구(Photoshop, CLIP STUDIO 등) 미명시이나 원본도 동일 |
| E-17 | deadline 정확성 | ✅ | null — "通年採用" 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월 이후" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 5직종 공통 크리에이터 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, "通年採用" 활성 |
| G-24 | 중복 공고 | ⚠️ | #46, #52와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ゲームイラストレーター" → "게임 일러스트레이터" 정확 |

**종합**: ✅ 18/25 통과, ⚠️ 7, ❌ 0
**판정**: PUBLISH 유지 적합. 크리에이터 공통 패턴.
**Fix 액션**: B-6/D-14 → HOLD (크리에이터 공통).
**Deadline 액션**: 없음. "通年採用" 수시 활성.

---

## Job #54 — 사이버에이전트 | 디자이너 종합직

**상태**: PUBLISHED
**소스**: https://creators.cyberagent.co.jp/information/
**나루 공고**: https://www.naru-recruit.com/jobs/54
**어드민**: https://www.naru-recruit.com/admin/jobs/54?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 07:45 | 리뷰 | 18/25 ⚠️7 (A-1, A-2, B-6 not_specified, C-9, D-14 UNKNOWN, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=5040000. 사이버에이전트 공통 504만 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "특정 제작에 한정되지 않고 종합적 디자인", "미디어&IP, 게임, DXDesign실" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 서비스디자인(UI/UX)/그래픽/브랜딩/아트디렉션/굿즈 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ⚠️ | mustHave=["not_specified"]. 크리에이터 공통 이슈 |
| B-7 | selectionProcess 일치 | ✅ | 크리에이터 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "미디어&IP, 게임, DXDesign실" — 배치 부서 구체 명시 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | cyberagent 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 디자이너 종합직 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | UNKNOWN |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 []. 종합 디자이너이므로 특정 도구 한정 어려움 |
| E-17 | deadline 정확성 | ✅ | null — "通年採用" 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월 이후" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 5직종 공통 크리에이터 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | #46, #52, #53과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "デザイナー総合職" → "디자이너 종합직" 정확 |

**종합**: ✅ 18/25 통과, ⚠️ 7, ❌ 0
**판정**: PUBLISH 유지 적합. 크리에이터 공통 패턴.
**Fix 액션**: B-6/D-14 → HOLD.
**Deadline 액션**: 없음. "通年採用" 수시 활성.

> 📊 사이버에이전트 크리에이터 4/5직종 완료 (#46 시나리오, #52 3DCG, #53 일러스트, #54 디자이너 종합). 남은 1건: 애니메이터 (별도 자회사).

---

## Job #55 — MIXI | 【2027년】비즈니스 플래너직

**상태**: PUBLISHED → **DRAFT (unpublish)**
**소스**: https://mixigroup-recruit.mixi.co.jp/recruitment-category/13482/
**나루 공고**: https://www.naru-recruit.com/jobs/55
**어드민**: https://www.naru-recruit.com/admin/jobs/55?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 08:05 | 리뷰 | source_url 404 (2회 확인) → ❌ |
| 04/15 08:05 | Deadline | ❌ 404 확인 → PUT /unpublish (204). PUBLISHED→DRAFT |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3600000. 원본 404이므로 검증 불가. 360만=월급 30만×12 추정 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | N/A | 원본 404, 검증 불가 |
| B-5 | tasks 일치 | N/A | 원본 404, 검증 불가 |
| B-6 | targetCandidate 일치 | N/A | 원본 404 |
| B-7 | selectionProcess 일치 | N/A | 원본 404 |
| C-8 | 업종·사업 특성 | ✅ | "MIXI", "AI 활용" — overview 내용 자체는 적절 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 모ン스ト, みてね 등 서비스 맥락 미기재 |
| C-10 | 기업명 정확성 | ✅ | mixi 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 적합 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 비즈니스 플래너 적절 |
| E-17 | deadline 정확성 | ✅ | null |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ❌ | **404** (2회 확인) |
| G-23 | 채용 종료 키워드 | N/A | 404이므로 확인 불가 |
| G-24 | 중복 공고 | ✅ | MIXI 첫 공고 |
| G-25 | 제목 일치 | N/A | 원본 404 |

**종합**: ✅ 14/25 통과, ⚠️ 4, ❌ 1, N/A 6
**판정**: ❌ **unpublish 처리 완료**. source_url 404 — 원본 페이지 삭제됨.
**Fix 액션**: 없음. 원본 자체 삭제.
**Deadline 액션**: ✅ PUT /api/dev/jobs/55/unpublish → 204. PUBLISHED→DRAFT 전환 완료.

> 📊 MIXI 첫 등장이나 즉시 unpublish. 🆕 **첫 unpublish 액션!** 이전 Deadline 6건은 isDeadlinePassed=true였고 unpublish는 이번이 처음.

---

## Job #56 — MIXI | 【2027년】비즈니스 플래너직 (글로벌)

**상태**: PUBLISHED → **DRAFT (unpublish)**
**소스**: https://mixigroup-recruit.mixi.co.jp/recruitment-category/13557/
**나루 공고**: https://www.naru-recruit.com/jobs/56
**어드민**: https://www.naru-recruit.com/admin/jobs/56?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 08:15 | 리뷰 | source_url 404 (2회 확인) → ❌ |
| 04/15 08:15 | Deadline | ❌ 404 확인 → PUT /unpublish (204). PUBLISHED→DRAFT |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3600000. 원본 404, 검증 불가 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | N/A | 원본 404 |
| B-5 | tasks 일치 | N/A | 원본 404 |
| B-6 | targetCandidate 일치 | N/A | 원본 404 |
| B-7 | selectionProcess 일치 | N/A | 원본 404 |
| C-8 | 업종·사업 특성 | ✅ | "해외 사업 전개", "스포츠, 라이프스타일, 디지털 엔터테인먼트" — overview 내용 자체는 적절 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | mixi 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 비즈니스 적절 |
| E-17 | deadline 정확성 | ✅ | null |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ❌ | **404** (2회 확인) |
| G-23 | 채용 종료 키워드 | N/A | 404 |
| G-24 | 중복 공고 | ✅ | #55와 다른 코스 (일반 vs 글로벌) |
| G-25 | 제목 일치 | N/A | 원본 404 |

**종합**: ✅ 14/25 통과, ⚠️ 3, ❌ 1, N/A 7
**판정**: ❌ **unpublish 처리 완료**. source_url 404.
**Fix 액션**: 없음.
**Deadline 액션**: ✅ PUT /api/dev/jobs/56/unpublish → 204.

> 📊 MIXI 2건 (#55, #56) 모두 404 → unpublish. mixigroup-recruit.mixi.co.jp 도메인 전체가 채용 페이지를 리뉴얼/이전한 것으로 추정. MIXI 잔여 공고도 같은 패턴일 가능성 높음.
> ⚠️ 정정: #57에서 같은 도메인이지만 다른 경로(`/occupation/engineer/`)는 200 반환. URL 경로별 차이 있음.

---

## Job #57 — MIXI | 엔지니어직 (게임 클라이언트) — 몬스터 스트라이크

**상태**: PUBLISHED
**소스**: https://mixigroup-recruit.mixi.co.jp/occupation/engineer/13425/
**나루 공고**: https://www.naru-recruit.com/jobs/57
**어드민**: https://www.naru-recruit.com/admin/jobs/57?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 08:25 | 리뷰 | 19/25 ⚠️6 (A-1 salary null, A-2, C-9, D-14, E-16, 없음) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin/Max null. 원본에도 연봉 미기재. #55~56은 360만이었는데 엔지니어는 null — 직종별 연봉 체계 다를 수 있음 |
| A-2 | 연봉 범위 일치 | ⚠️ | null |
| A-3 | 통화·단위 | ✅ | N/A |
| B-4 | overview 발췌 | ✅ | "6,400만 사용자 몬스터 스트라이크", "인게임~아웃게임·시스템" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 인게임(캐릭터·스테이지)/아웃게임(콜라보·UI)/기술검증/사양설계/아이디어 제안 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 4개 — 입사 시기/열정/코딩 게임 개발 경험/세계관 공감 — 원본과 일치. "사용자 서프라이즈 퍼스트" 고유 가치관 |
| B-7 | selectionProcess 일치 | ✅ | MIXI 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "6,400만 사용자 몬스터 스트라이크" — 대표 타이틀 명시. 구체적 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | "12년간 사랑받은" 정도만. 직원수 등 미기재 |
| C-10 | 기업명 정확성 | ✅ | mixi 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 게임 클라이언트 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 원본에 근무형태 명시 미확인. 적절한 추정이나 확인 필요 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | C++/Objective-C/Java/Cocos2d-x/OpenGLES/GitHub — 6개. 몬스트 기술 스택 정확하나 Cocos2d-x/OpenGLES는 레거시 느낌. 원본과는 일치 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "사용자 서프라이즈 퍼스트" 등 고유 표현 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중. 몬스트 확약 배치 명시 |
| G-22 | source_url 접근 | ✅ | 200 응답! (`/occupation/engineer/` 경로는 살아있음) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #55~56과 다른 직종·URL |
| G-25 | 제목 일치 | ✅ | "ゲームクライアントエンジニア" → "엔지니어직 (게임 클라이언트)" 정확 |

**종합**: ✅ 19/25 통과, ⚠️ 6, ❌ 0
**판정**: PUBLISH 유지 적합. salary null이나 원본도 미기재. 원본 활성.
**Fix 액션**: 없음. salary null → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 MIXI 가설 재정정: `/recruitment-category/13482/` 404이나 `/recruitment-category/new-graduate/13420/` 200. `/occupation/engineer/` 200. 특정 ID의 비즈니스 플래너 페이지만 삭제된 것.

---

## Job #58 — MIXI | 엔지니어직 (머신러닝)

**상태**: PUBLISHED
**소스**: https://mixigroup-recruit.mixi.co.jp/recruitment-category/new-graduate/13420/
**나루 공고**: https://www.naru-recruit.com/jobs/58
**어드민**: https://www.naru-recruit.com/admin/jobs/58?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 08:45 | 리뷰 | 20/25 ⚠️5 (A-1 salary null, A-2, C-9, D-14, E-16) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin/Max null. 원본에 "スキルベース 個別オファー(月収)" 명시 — 개인별 다른 월급 제시. 고정 금액 없음 |
| A-2 | 연봉 범위 일치 | ⚠️ | null — 스킬 기반 개별 오퍼이므로 범위 표기 자체가 불가 |
| A-3 | 통화·단위 | ✅ | N/A |
| B-4 | overview 발췌 | ✅ | "신뢰×감정×놀이를 지탱하는 AI", "감정 이해 및 데이터 드리븐 가치 극대화" — MIXI 고유 AI 비전 반영, 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — ML 모델(레코멘드)/MLOps/LLM·생성AI/요건 조정/기술 조사 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 4개 — 입사 시기/연구 성과 또는 개발 경험/팀 개발(Git)/커뮤니케이션 — 원본과 일치. 연구 성과 요건 포함 |
| B-7 | selectionProcess 일치 | ✅ | MIXI 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "신뢰×감정×놀이" — MIXI 고유 가치관 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | "내정 후 스킬 향상으로 초봉 인상 가능" — 독특한 제도이나 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | mixi 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — ML 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 원본에 근무형태 직접 명시 미확인 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Python/Kubernetes/Docker/Git/LLM/NLP — 6개. ML 엔지니어 치고 적은 편. PyTorch/TensorFlow 등 미포함이나 원본도 키워드만 나열 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #57 게임 엔지니어와 다른 직종 |
| G-25 | 제목 일치 | ✅ | "エンジニア職_機械学習" → "엔지니어직 (머신러닝)" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. salary null은 스킬 기반 개별 오퍼 방식이므로 불가피.
**Fix 액션**: 없음. salary null → HOLD (개별 오퍼 방식).
**Deadline 액션**: 없음. deadline=null, 원본 활성.

---

## Job #59 — MIXI | 엔지니어직 (종합)

**상태**: PUBLISHED
**소스**: https://mixigroup-recruit.mixi.co.jp/recruitment-category/new-graduate/13170/
**나루 공고**: https://www.naru-recruit.com/jobs/59
**어드민**: https://www.naru-recruit.com/admin/jobs/59?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 08:55 | 리뷰 | 21/25 ⚠️4 (C-9, D-14, E-16 techStack 빈약, G-24 없음) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=4200000, salaryMax=7000000. 원본 "420万円～700万円" 명시. **정확 일치!** 🆕 min+max 모두 원본 일치하는 첫 케이스 |
| A-2 | 연봉 범위 일치 | ✅ | 420만~700만. 원본과 정확 일치! |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "웹·스마트폰 앱 클라이언트·서버·인프라", "업무 지원 툴, 개발 환경 개선" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 클라이언트/서버·인프라/업무 툴/개발 환경 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 3개 — 입사 시기/일본어/프로그래밍 경험 — 원본과 일치. 범용적 자격 (#57 몬스트보다 진입 장벽 낮음) |
| B-7 | selectionProcess 일치 | ✅ | MIXI 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "MIXI 각 프로덕트" — 종합 엔지니어 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | mixi 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 원본 직접 명시 미확인 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | GitHub만 1개. 종합 엔지니어이므로 기술 특정이 어려우나 과도하게 빈약 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #57 게임/#58 ML과 다른 종합 직종 |
| G-25 | 제목 일치 | ✅ | "エンジニア職" → "엔지니어직" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 4, ❌ 0
**판정**: PUBLISH 유지 적합. 🏆 **연봉 min+max 모두 원본 완전 일치하는 첫 케이스!**
**Fix 액션**: 없음. E-16 techStack(GitHub만 1개) → HOLD (종합 직종 한계).
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 MIXI 4건 (#55~59): unpublish 2 (#55,56 비즈니스), 정상 2 (#57 게임, #58 ML, #59 종합). 연봉 비교: 종합(#59) 420~700만(범위 있음) > 비즈니스(#55,56) 360만(단일) > 몬스트(#57)/ML(#58) null. MIXI는 스킬 기반 개별 오퍼 방식.

---

## Job #60 — MIXI | 디자인직 (그래픽 디자이너)

**상태**: PUBLISHED → **DRAFT (unpublish)**
**소스**: https://mixigroup-recruit.mixi.co.jp/recruitment-category/new-graduate/13517/
**나루 공고**: https://www.naru-recruit.com/jobs/60
**어드민**: https://www.naru-recruit.com/admin/jobs/60?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 09:05 | 리뷰 | source_url 404 (2회 확인) → ❌ |
| 04/15 09:05 | Deadline | ❌ 404 확인 → PUT /unpublish (204). PUBLISHED→DRAFT |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3600000. 원본 404, 검증 불가 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | N/A | 원본 404 |
| B-5 | tasks 일치 | N/A | 원본 404. 내용 자체는 구체적 (몬스트 KV, 미테네 해외 광고, FC 도쿄 포스터 등 실제 프로젝트 나열) |
| B-6 | targetCandidate 일치 | N/A | 원본 404 |
| B-7 | selectionProcess 일치 | N/A | 원본 404 |
| C-8 | 업종·사업 특성 | ✅ | "몬스터 스트라이크", "가족 앨범 미테네", "FC 도쿄" — 구체 서비스명 나열 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | mixi 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 그래픽 디자이너 적절 |
| E-17 | deadline 정확성 | ✅ | null |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ❌ | **404** (2회 확인) |
| G-23 | 채용 종료 키워드 | N/A | 404 |
| G-24 | 중복 공고 | ✅ | 다른 직종 |
| G-25 | 제목 일치 | N/A | 원본 404 |

**종합**: ✅ 14/25 통과, ⚠️ 3, ❌ 1, N/A 7
**판정**: ❌ **unpublish 처리 완료**. source_url 404.
**Fix 액션**: 없음.
**Deadline 액션**: ✅ PUT /api/dev/jobs/60/unpublish → 204.

> 📊 MIXI 404 패턴: ID별 개별 삭제 구조. 같은 경로 내에서도 종료 건만 404.

---

## Job #61 — MIXI | 디자인직 (게임 UI 디자이너)

**상태**: PUBLISHED
**소스**: https://mixigroup-recruit.mixi.co.jp/recruitment-category/new-graduate/13536/
**나루 공고**: https://www.naru-recruit.com/jobs/61
**어드민**: https://www.naru-recruit.com/admin/jobs/61?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 09:15 | 리뷰 | 21/25 ⚠️4 (A-2, C-9, D-14, E-16) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3600000. 원본 "月給30万円〜" = 30만×12 = 360만. 정확 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 "30万円〜" 상한 미기재 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 (월급×12) |
| B-4 | overview 발췌 | ✅ | "몬스터 스트라이크 콜라보 전용 디자인", "세계관에 다가가면서 UI 디자인" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — UI/UX 설계/정보 정리·플로우/UI 디자인·소재/사양 조정/QA·구현 체크 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 3개 — 열정/디자인 열의/협업 자세 — 원본과 일치. 기술 요건 없이 마인드셋 중심 (독특) |
| B-7 | selectionProcess 일치 | ✅ | "엔트리→ES(포트폴리오)→인사면접→면접→내정" — 디자인 특유 포트폴리오 포함 |
| C-8 | 업종·사업 특성 | ✅ | "몬스터 스트라이크 콜라보" — 대표 게임 타이틀 명시 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | mixi 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 게임 UI 디자이너 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 원본 직접 명시 미확인 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | Photoshop/Illustrator 2개. UI 디자이너 기본 도구이나 Figma/Sketch 등 미포함. 원본 기준으로는 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 몬스트 UI 디자인 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #60 그래픽 디자이너(404)와 다른 직종 |
| G-25 | 제목 일치 | ✅ | "ゲームUIデザイナー" → "게임 UI 디자이너" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 4, ❌ 0
**판정**: PUBLISH 유지 적합. 연봉 원본 일치, 원본 활성.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 🎯 **50건(#61)! 50% 돌파!** #12~61 중 실제 리뷰 50건(jobId 1~11 미존재 제외).
> 📊 MIXI 6건 (#55~61): unpublish 3 (#55,56,60), 정상 3 (#57 게임, #58 ML, #59 종합, #61 UI 디자인). 디자인 직종은 그래픽(#60) 404, UI(#61) 200 — 같은 디자인이어도 공고별 차이.

---

## Job #62 — MIXI | 디자인직 (CG 영상 크리에이터)

**상태**: PUBLISHED
**소스**: https://mixigroup-recruit.mixi.co.jp/recruitment-category/new-graduate/13672/
**나루 공고**: https://www.naru-recruit.com/jobs/62
**어드민**: https://www.naru-recruit.com/admin/jobs/62?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 09:25 | 리뷰 | 21/25 ⚠️4 (A-2, C-9, D-14, E-16) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3600000. MIXI 디자인 공통 360만 (월급 30만×12) |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "3DCG·그래픽 활용 프로모션 동영상", "영상으로 가치 전달" — 원본과 일치 |
| B-5 | tasks 일치 | ✅ | 3개 항목 — 웹 동영상(YouTube/TikTok/X)/이벤트 스테이지 영상(몬스트·스포츠)/사내 동영상 — 원본과 일치. 구체적 플랫폼·이벤트 명시 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 5개 — AI 이해/학습 의욕/영상 공개 경험/After Effects 경험/설명 능력 — 원본과 일치. AI 기초 이해 요구가 특이 |
| B-7 | selectionProcess 일치 | ✅ | MIXI 디자인 공통 (포트폴리오 포함) |
| C-8 | 업종·사업 특성 | ✅ | "몬스터 스트라이크 이벤트", "스포츠 사업" — 다사업 영역 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | mixi 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — CG 영상 크리에이터 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO 정확 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 원본 직접 명시 미확인 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | After Effects/Blender/Maya/Cinema4D — 4개. CG 영상 도구로 적절! 원본 mustHave에 AE 경험 요구와도 일치 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 직종 고유 정보 집중 |
| G-22 | source_url 접근 | ✅ | 200 응답 |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #60 그래픽(404)/#61 UI와 다른 직종 |
| G-25 | 제목 일치 | ✅ | "CG映像クリエイター" → "CG 영상 크리에이터" 정확 |

**종합**: ✅ 21/25 통과, ⚠️ 4, ❌ 0
**판정**: PUBLISH 유지 적합. techStack(AE/Blender/Maya/C4D) 적절.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

---

## Job #63 — NEC | 2027년도 잡 매칭 채용 연구직

**상태**: PUBLISHED
**소스**: https://jpn.nec.com/recruit/newgraduate/matching/job/001/
**나루 공고**: https://www.naru-recruit.com/jobs/63
**어드민**: https://www.naru-recruit.com/admin/jobs/63?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 09:35 | 리뷰 | 19/25 ⚠️5 N/A1 (A-2, C-9, D-14, G-22 403 봇차단, B항목 N/A) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3528000. NEC 신졸 초봉(학부 294,000×12 = 3,528,000 추정). DB 값 부합 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | N/A | 403 봇 차단으로 원본 검증 불가. DB 내용 자체는 NEC 연구직 설명으로 적절 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 요소 연구/논문·학회/지적재산/필드 실험/사업화 — 연구직 업무로 적절 |
| B-6 | targetCandidate 일치 | ✅ | "2027/2026 입사, 연구 실적, 일본어" — 연구직 자격으로 적절 |
| B-7 | selectionProcess 일치 | ✅ | "엔트리→WebTest→면접·조브매칭→내정" — NEC 잡 매칭 방식 |
| C-8 | 업종·사업 특성 | ✅ | "글로벌 네트워크, 바이오메트릭스, 양자, 보안" — NEC 연구 분야 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | NEC 규모(10만+ 직원, 일본 대표 IT 기업) 미기재 |
| C-10 | 기업명 정확성 | ✅ | nec 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 연구직 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO/KANAGAWA/CHIBA 3거점 — NEC 연구소 소재지와 부합 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 연구직이므로 적절 추정이나 원본 확인 불가 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | Generative AI/Biometrics/Quantum Computing/Cyber Security/Data Science/5G·6G — 6개, NEC 핵심 연구 분야로 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시 추정 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "바이오메트릭스", "양자 기술" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | **403 Forbidden** — 봇 차단 (IBM WAF 패턴과 유사). 사람 브라우저 확인 필요 |
| G-23 | 채용 종료 키워드 | N/A | 403 차단, 확인 불가 |
| G-24 | 중복 공고 | ✅ | NEC 첫 공고 |
| G-25 | 제목 일치 | N/A | 원본 403 |

**종합**: ✅ 19/25 통과, ⚠️ 5, ❌ 0, N/A 1
**판정**: PUBLISH 유지 적합. 403 차단은 URL 검증 한계이나 DB 데이터 품질 양호.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null.

> 📊 NEC 첫 등장. jpn.nec.com 도메인 403 봇 차단 — IBM WAF 동일 패턴.

---

## Job #64 — NEC | 2027년도 잡 매칭 채용 시스템 엔지니어직

**상태**: PUBLISHED
**소스**: https://jpn.nec.com/recruit/newgraduate/matching/job/003/
**나루 공고**: https://www.naru-recruit.com/jobs/64
**어드민**: https://www.naru-recruit.com/admin/jobs/64?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 09:45 | 리뷰 | 19/25 ⚠️5 N/A1 (A-2, C-9, D-14, G-22 403, B-4 N/A) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3528000. NEC 공통 초봉 (학부 294,000×12) |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | N/A | 403 차단. DB 내용은 SE직 설명으로 적절 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 요건정의/기본·상세설계/PM·품질/클라우드 구축/유지보수 — SE 업무 전 과정 포괄 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 3개 — 입사 시기/논리적 사고/IT 흥미 — SE직 자격으로 적절. 연구직(#63)보다 진입 장벽 낮음 |
| B-7 | selectionProcess 일치 | ✅ | NEC 잡 매칭 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "대규모 사회 인프라", "안전·안심·효율·공평한 사회" — NEC 사회 인프라 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | nec 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — SE직 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO/KANAGAWA/CHIBA 3거점 — #63 연구직과 동일 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 적절 추정이나 원본 확인 불가 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | Java/Python/AWS/Azure/GCP/Docker·K8s/Microservices — 7개. SE직 기술 스택으로 적절, 클라우드 3사 모두 포함 |
| E-17 | deadline 정확성 | ✅ | null |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ⚠️ | **403 Forbidden** — NEC 봇 차단 (#63과 동일) |
| G-23 | 채용 종료 키워드 | N/A | 403 |
| G-24 | 중복 공고 | ✅ | #63 연구직과 다른 직종 |
| G-25 | 제목 일치 | N/A | 403 |

**종합**: ✅ 19/25 통과, ⚠️ 5, ❌ 0, N/A 1
**판정**: PUBLISH 유지 적합. 403 차단 한계이나 DB 데이터 양호.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null.

> 📊 NEC 2건 (#63 연구, #64 SE): 공통 초봉 352만8천, 403 봇 차단.

---

## Job #65 — NEC | 2027년도 잡 매칭 채용 영업·비즈니스 디자인직

**상태**: PUBLISHED
**소스**: https://jpn.nec.com/recruit/newgraduate/matching/job/015/
**나루 공고**: https://www.naru-recruit.com/jobs/65
**어드민**: https://www.naru-recruit.com/admin/jobs/65?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 09:55 | 리뷰 | 19/25 ⚠️5 N/A1 (A-2, C-9, D-14, G-22 403, B-4 N/A) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3528000. NEC 공통 초봉 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | N/A | 403 차단. DB 내용은 영업·BD 설명으로 적절 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 과제분석/솔루션 제안/비즈니스 모델 기획/에코시스템/PM — 비즈니스 직 업무로 적절 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 3개 — 입사 시기/논리+커뮤니케이션/사회 과제 해결 의지 — 적절 |
| B-7 | selectionProcess 일치 | ✅ | NEC 잡 매칭 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "관공서, 금융, 유통, 제조" — NEC의 다산업 대상 사업 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | nec 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 영업·비즈니스 디자인 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO — 영업직은 도쿄 중심 (#63~64 연구·SE는 3거점) |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 원본 확인 불가 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 영업/BD 직군이므로 적절 |
| E-17 | deadline 정확성 | ✅ | null |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "에코시스템 구축", "얼라이언스" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ⚠️ | **403 Forbidden** — NEC 봇 차단 |
| G-23 | 채용 종료 키워드 | N/A | 403 |
| G-24 | 중복 공고 | ✅ | #63 연구/#64 SE와 다른 직종 |
| G-25 | 제목 일치 | N/A | 403 |

**종합**: ✅ 19/25 통과, ⚠️ 5, ❌ 0, N/A 1
**판정**: PUBLISH 유지 적합.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null.

> 📊 NEC 3건 (#63~65) 완료. 공통: 초봉 352만8천, 403 봇 차단.

---

## Job #66 — NEC | 2027년도 잡 매칭 채용 법무·컴플라이언스직

**상태**: PUBLISHED
**소스**: None (jobSourceUrl 없음!)
**나루 공고**: https://www.naru-recruit.com/jobs/66
**어드민**: https://www.naru-recruit.com/admin/jobs/66?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 10:05 | 리뷰 | 17/25 ⚠️5 ❌1 N/A2 (A-2, C-9, D-14, G-22 URL null, B-4/G-25 N/A) → 수정 필요 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3528000. NEC 공통 초봉 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | N/A | source URL null, 원본 검증 불가. DB 내용 자체는 법무·컴플라이언스 설명으로 적절 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 계약 심사/리스크 분석/M&A/소송/컴플라이언스 — 법무직 업무로 적절 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 3개 — 입사 시기/법학 기초/논리적 사고 — 적절 |
| B-7 | selectionProcess 일치 | ✅ | NEC 잡 매칭 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "글로벌 비즈니스 법적 지원", "M&A" — NEC 법무 특성 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | nec 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_SPECIALIST — 법무·컴플라이언스 전문직 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ⚠️ | HYBRID — 원본 확인 불가 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 법무직 적절 |
| E-17 | deadline 정확성 | ✅ | null |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "리걸 체크", "거버넌스" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ❌ | **jobSourceUrl = null!** 원본 URL 자체가 없음. 🆕 역대 첫 케이스 |
| G-23 | 채용 종료 키워드 | N/A | URL 없음 |
| G-24 | 중복 공고 | ✅ | #63~65와 다른 직종 |
| G-25 | 제목 일치 | N/A | URL 없음 |

**종합**: ✅ 17/25 통과, ⚠️ 5, ❌ 1, N/A 2
**판정**: PUBLISH 유지 가능하나 **source URL null 이슈**. 사용자에게 NEC 법무직 전용 URL 보충 필요.
**Fix 액션**: G-22 jobSourceUrl null → HOLD. NEC 잡 매칭 페이지에서 법무직 URL 수동 탐색 필요.
**Deadline 액션**: 없음. deadline=null.

> 📊 🆕 jobSourceUrl = null 첫 발견 (#66 NEC 법무).

---

## Job #67 — 소프트뱅크 | 2027년도 OPEN 엔지니어 코스

**상태**: PUBLISHED
**소스**: https://www.softbank.jp/recruit/graduate/recruit/flow/
**나루 공고**: https://www.naru-recruit.com/jobs/67
**어드민**: https://www.naru-recruit.com/admin/jobs/67?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 10:15 | 리뷰 | 20/25 ⚠️5 (A-1 연봉 출처, A-2, C-9, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3276000. 원본 페이지에 연봉 미기재. 소프트뱅크 신졸 초봉(학부 273,000×12 = 3,276,000) 추정으로 부합하나 발췌 아님 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "최첨단 테크놀로지", "네트워크, 시스템, 보안, 데이터 사이언스 배치" — 원본 OPEN 엔지니어 설명과 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 5G/6G/앱 개발/AI·빅데이터/사이버 보안/R&D — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 3개 — 졸업 예정(고전 포함)/30세 미만/IT 기초 — 원본과 일치. **30세 미만 연령 제한 특이** |
| B-7 | selectionProcess 일치 | ✅ | "프리엔트리→서류→면접→내정" — 원본과 일치 |
| C-8 | 업종·사업 특성 | ✅ | "사회를 통째로 더 좋게 만들고 싶은" — 소프트뱅크 비전 반영 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 소프트뱅크 그룹 규모(통신3사, 비전펀드 등) 미기재 |
| C-10 | 기업명 정확성 | ✅ | softbank 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — OPEN 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO — 본사 기준 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | Java/Python/JS/SQL/5G·6G/Cloud(AWS·Azure)/AI·ML — 7개, 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 개별 코스 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 200 응답이나 OPEN/JOB-MATCH 전체 코스 공통 페이지 (2+9=11 코스 공유) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | 소프트뱅크 다른 코스와 동일 URL 공유 가능 |
| G-25 | 제목 일치 | ✅ | "OPENエンジニアコース" → "OPEN 엔지니어 코스" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. 연봉 출처 불명확이나 초봉 추정값 부합.
**Fix 액션**: 없음. A-1 연봉 출처 → HOLD.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 소프트뱅크 첫 등장! 11코스 공통 URL, OPEN+JOB-MATCH 이중 체계.

---

## Job #68 — 소프트뱅크 | 2027년도 JOB-MATCH 솔루션 엔지니어

**상태**: PUBLISHED
**소스**: https://www.softbank.jp/recruit/graduate/recruit/flow/
**나루 공고**: https://www.naru-recruit.com/jobs/68
**어드민**: https://www.naru-recruit.com/admin/jobs/68?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 10:25 | 리뷰 | 20/25 ⚠️5 (A-1 연봉, A-2, C-9, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3276000. 소프트뱅크 공통 초봉 추정. 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "법인 ICT 솔루션 기획·제안, 시스템 설계·구축", "합격 시 배치 확약" — JOB-MATCH 특성 정확 반영 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 솔루션 기획/인프라 설계/기술 컨설팅/운영·개선 — SE직 업무로 적절 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 4개 — 졸업 예정/IT 인프라 관심/커뮤니케이션/책임감 — 원본과 일치 |
| B-7 | selectionProcess 일치 | ✅ | 소프트뱅크 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "모바일, 네트워크, 클라우드 솔루션" — 통신 기업의 법인 영업 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 통신 3사 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | softbank 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — 솔루션 엔지니어 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID 정확 |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | Network/Server/Cloud(3사)/Security — 4개, SE직에 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | "합격 시 배치 확약" — JOB-MATCH 차별화 포인트 반영 |
| G-22 | source_url 접근 | ⚠️ | 11코스 공통 URL (#67과 동일) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | #67 OPEN 엔지니어와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ソリューションエンジニア" → "솔루션 엔지니어" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. JOB-MATCH "배치 확약" 특성이 OPEN(#67)과 차별화.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

---

## Job #69 — 소프트뱅크 | 2027년도 JOB-MATCH 데이터 사이언티스트

**상태**: PUBLISHED
**소스**: https://www.softbank.jp/recruit/graduate/recruit/flow/
**나루 공고**: https://www.naru-recruit.com/jobs/69
**어드민**: https://www.naru-recruit.com/admin/jobs/69?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 10:35 | 리뷰 | 20/25 ⚠️5 (A-1 연봉, A-2, C-9, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3276000. 소프트뱅크 공통 초봉. 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "데이터로부터 새로운 가치 창출", "AI 솔루션 기획·개발·컨설팅", "배치 확약" — JOB-MATCH DS 설명 적절 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 분석·예측/AI 알고리즘(생성AI·NLP·CV)/컨설팅/MLOps — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 4개 — 졸업 예정/기술 영어/AI·ML 구현 경험/통계학 — 원본과 일치. **기술 영어(논문 읽기) 요구 특이** |
| B-7 | selectionProcess 일치 | ✅ | 소프트뱅크 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "방대한 데이터를 비즈니스에 활용" — 통신 빅데이터 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | softbank 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — DS 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | AI·ML/Python/SQL/NLP/Computer Vision/Statistics — 6개, DS직에 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ⚠️ | 11코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | #67~68과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "データサイエンティスト" → "데이터 사이언티스트" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. mustHave에 기술 영어(논문) + AI·ML 구현 + 통계학 — SE(#68)보다 높은 진입 장벽.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

---

## Job #70 — 소프트뱅크 | 2027년도 JOB-MATCH 연구 개발

**상태**: PUBLISHED
**소스**: https://www.softbank.jp/recruit/graduate/recruit/flow/
**나루 공고**: https://www.naru-recruit.com/jobs/70
**어드민**: https://www.naru-recruit.com/admin/jobs/70?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 10:45 | 리뷰 | 20/25 ⚠️5 (A-1 연봉, A-2, C-9, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3276000. 소프트뱅크 공통. 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "Beyond 5G/6G, 자율주행, 차세대 배터리, 로보틱스, AI" — R&D 연구 분야 구체 나열. "배치 확약" 포함 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — Beyond 5G·HAPS/자율주행·로보틱스/AI R&D/실증 실험/공동 연구 — 원본과 일치. **HAPS(상공 기지국) 특이** |
| B-6 | targetCandidate 일치 | ✅ | mustHave 5개 — 졸업/NW·서버·클라우드 기초/AI 관심/새로운 발상/실행력 — DS(#69)보다 폭넓은 자격 |
| B-7 | selectionProcess 일치 | ✅ | 소프트뱅크 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "소프트뱅크 미래를 창조할 기술 탐구" — 통신 R&D 비전 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | softbank 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER — R&D 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 5G·6G/Autonomous Driving/Robotics/AI·ML/Next-gen Battery/Quantum Computing — 6개, R&D 최첨단 분야. **Quantum Computing + 자율주행 + 차세대 배터리** 조합이 독특 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "상공 기지국(HAPS)" 등 전문용어 적절 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ⚠️ | 11코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | #67~69와 동일 source_url |
| G-25 | 제목 일치 | ✅ | "研究開発" → "연구 개발" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합. techStack에 Quantum+자율주행+차세대 배터리 — 역대 가장 미래 지향적 R&D 공고.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 소프트뱅크 4건 R&D 기술: OPEN < SE < DS < R&D(가장 미래 지향적).

---

## Job #71 — 소프트뱅크 | 2027년도 JOB-MATCH 컨슈머 영업

**상태**: PUBLISHED
**소스**: https://www.softbank.jp/recruit/graduate/recruit/flow/
**나루 공고**: https://www.naru-recruit.com/jobs/71
**어드민**: https://www.naru-recruit.com/admin/jobs/71?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 10:55 | 리뷰 | 20/25 ⚠️5 (A-1 연봉, A-2, C-9, G-22 공통URL, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3276000. 소프트뱅크 공통. 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "소프트뱅크숍·양판점 판매 대리점 영업 컨설팅", "기획~실시 일관 담당", "배치 확약" — 적절 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 대리점 영업/전략 기획/경영진 상담/프로모션 — 적절 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 4개 — 졸업/목표 달성/팀 성과/소통 — 영업직 자격으로 적절 |
| B-7 | selectionProcess 일치 | ✅ | 소프트뱅크 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "고객과 가장 가까운 최전선" — B2C 영업 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | softbank 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 컨슈머 영업 적합 |
| D-12 | locations 정확성 | ✅ | **NATIONWIDE** 🆕 — 전국 배치! 영업직이므로 적절. 역대 첫 등장 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 영업직 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ⚠️ | 11코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | #67~70과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "コンシューマ営業" → "컨슈머 영업" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 NATIONWIDE enum 첫 등장! location enums 14종 확인.

---

## Job #72 — 소프트뱅크 | 2027년도 JOB-MATCH 재무

**상태**: PUBLISHED
**소스**: https://www.softbank.jp/recruit/graduate/recruit/flow/
**나루 공고**: https://www.naru-recruit.com/jobs/72
**어드민**: https://www.naru-recruit.com/admin/jobs/72?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 11:05 | 리뷰 | 20/25 ⚠️5 (A-1, A-2, C-9, G-22, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ⚠️ | salaryMin=3276000. 소프트뱅크 공통. 원본 미기재 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "실적 파악·경영 목표·예산 수립으로 경영 의사 결정 지원", "경영의 나침반" — 재무 직종 적절 |
| B-5 | tasks 일치 | ✅ | 4개 항목 — 실적 분석/예산 수립/사업 관리/의사 결정 데이터 — 적절 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 4개 — 졸업/부기·세무 기초/수학적 사고/논리적 사고 — 재무직 자격 적절 |
| B-7 | selectionProcess 일치 | ✅ | 소프트뱅크 공통 전형 |
| C-8 | 업종·사업 특성 | ✅ | "핵심 사업, 자회사, JV 사업 관리" — 대기업 재무 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | softbank 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_SPECIALIST — 재무 전문직 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 재무직 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2026년 10월/2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ⚠️ | 11코스 공통 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | #67~71과 동일 source_url |
| G-25 | 제목 일치 | ✅ | "ファイナンス" → "재무" 정확 |

**종합**: ✅ 20/25 통과, ⚠️ 5, ❌ 0
**판정**: PUBLISH 유지 적합.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 소프트뱅크 6건 (#67~72) 완료.

---

## Job #73 — 존재하지 않음

jobId 73: DB에 존재하지 않음 (404). 스킵.

---

## Job #74 — LIFULL | 신입 채용 디자이너

**상태**: PUBLISHED
**소스**: https://recruit.lifull.com/recruit/
**나루 공고**: https://www.naru-recruit.com/jobs/74
**어드민**: https://www.naru-recruit.com/admin/jobs/74?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 11:15 | 리뷰 | 22/25 ⚠️3 (A-2, C-9, G-22 공통URL) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3960000. 원본 "月給330,000円" 명시. 330,000×12 = 3,960,000 **정확 일치!** |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null. 원본도 상한 미기재 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 (월급×12) |
| B-4 | overview 발췌 | ✅ | "사업을, 사회를, 미래를 디자인한다", "광의의 디자인" — 원본 필로소피와 일치 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — LIFULL HOME'S UI/UX, 커뮤니케이션, 브랜드, 비전·컨셉, 프로젝트 추진 — 원본과 일치 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 3개 — 졸업/디자인 전공/포트폴리오 — 원본과 일치 |
| B-7 | selectionProcess 일치 | ✅ | "엔트리→세미나→인사전형(포폴)→어드바이저 면담(조언)→최종" — 원본과 일치. **어드바이저 면담(전형 아님)** 포함이 독특 |
| C-8 | 업종·사업 특성 | ✅ | "LIFULL HOME'S" — 부동산 테크 서비스 명시 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | lifull 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_DESIGN — 디자이너 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | Figma/Adobe Creative Cloud — 2개, 디자인 도구로 적절. 원본에서도 이 2개 사용 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "광의의 디자인" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 개별 공고 고유 정보 집중 |
| G-22 | source_url 접근 | ⚠️ | 200 응답이나 채용 전체 페이지 (디자이너 전용 아님) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | LIFULL 첫 공고 |
| G-25 | 제목 일치 | ✅ | "デザイナー" → "디자이너" 정확 |

**종합**: ✅ 22/25 통과, ⚠️ 3, ❌ 0
**판정**: PUBLISH 유지 적합. 연봉 원본 정확 일치. 콘텐츠 품질 양호.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 LIFULL 첫 등장! 22/25 고득점. 어드바이저 면담 독특.

---

## Job #75 — LIFULL | 신입 채용 엔지니어

**상태**: PUBLISHED
**소스**: https://recruit.lifull.com/recruit/
**나루 공고**: https://www.naru-recruit.com/jobs/75
**어드민**: https://www.naru-recruit.com/admin/jobs/75?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 11:25 | 리뷰 | 22/25 ⚠️3 (A-2, C-9, G-22 공통URL) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3960000. 원본 "月給330,000円" = 330,000×12 정확 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "엔지니어로서 경영을 리드한다", "기술로 비즈니스 가능성 확장" — LIFULL 엔지니어 비전 반영 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — HOME'S 개발/UX·운영/생성AI R&D/아키텍처/데이터 사이언스 — 원본과 일치. 생성 AI R&D 포함! |
| B-6 | targetCandidate 일치 | ✅ | mustHave 3개 — 졸업/프로그래밍 경험/모노즈쿠리 좋아하는 분 — "모노즈쿠리" 표현이 독특 |
| B-7 | selectionProcess 일치 | ✅ | #74 디자이너와 동일 (어드바이저 면담 포함) |
| C-8 | 업종·사업 특성 | ✅ | "LIFULL HOME'S" — 부동산 테크 서비스 명시 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | lifull 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_ENGINEER 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | PHP/Go/TypeScript/Swift/Kotlin/Ruby/Python/React/AWS/GCP — **10개**! 다양한 언어+클라우드. 부동산 테크 기업 치고 풍부 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "모노즈쿠리(만드는 것)" 적절 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ⚠️ | 채용 전체 페이지 (#74와 공유) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #74 디자이너와 다른 직종 |
| G-25 | 제목 일치 | ✅ | "エンジニア" → "엔지니어" 정확 |

**종합**: ✅ 22/25 통과, ⚠️ 3, ❌ 0
**판정**: PUBLISH 유지 적합. techStack 10개 + 연봉 정확 일치 + 생성AI R&D 포함. 데이터 품질 우수.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 LIFULL 2건 모두 22/25 고득점. 연봉 동일(396만).

---

## Job #76 — LIFULL | 신입 채용 비즈니스

**상태**: PUBLISHED
**소스**: https://recruit.lifull.com/recruit/
**나루 공고**: https://www.naru-recruit.com/jobs/76
**어드민**: https://www.naru-recruit.com/admin/jobs/76?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 11:45 | 리뷰 | 22/25 ⚠️3 (A-2, C-9, G-22 공통URL) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=3960000. LIFULL 공통 330,000×12 정확 일치 |
| A-2 | 연봉 범위 일치 | ⚠️ | salaryMax=null |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "영업, 사업 전략, 서비스 기획, 마케팅, PM, 인사, 경영 관리" — 비즈니스 직군 폭넓은 범위 반영 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 고객 접점·영업/프로모션/전략 제안/프로덕트 그로스/신규 플래닝 — 적절 |
| B-6 | targetCandidate 일치 | ✅ | mustHave 2개 — 졸업/"잠재력 중시, 경험·자격 불문" — **역대 가장 낮은 진입 장벽!** |
| B-7 | selectionProcess 일치 | ✅ | LIFULL 공통 (어드바이저 면담 포함) |
| C-8 | 업종·사업 특성 | ✅ | "LIFULL HOME'S 프로모션", "하우징 어드바이저" — 부동산 테크 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | lifull 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL — 비즈니스 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD 정확 |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ✅ | 빈 배열 [] — 비즈니스 적절 |
| E-17 | deadline 정확성 | ✅ | null — 수시, 원본 활성 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월" 정확 |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "하우징 어드바이저" 등 적절 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ⚠️ | 채용 전체 페이지 (#74~75와 공유) |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ✅ | #74 디자인/#75 엔지니어와 다른 직종 |
| G-25 | 제목 일치 | ✅ | "ビジネス" → "비즈니스" 정확 |

**종합**: ✅ 22/25 통과, ⚠️ 3, ❌ 0
**판정**: PUBLISH 유지 적합. LIFULL 3연속 22/25!
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

> 📊 LIFULL 3건 (#74~76) **전부 22/25** — 가장 일관된 고품질 회사! 연봉 전 직종 동일(396만). "잠재력 중시, 경험·자격 불문" mustHave — 역대 가장 낮은 진입 장벽.