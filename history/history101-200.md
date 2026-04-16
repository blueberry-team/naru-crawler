# Deep Review History — Job #101 ~ #200

25개 평가 기준에 따른 공고별 상세 검증 결과.
평가 기준 상세: [docs/REVIEW_GUIDE.md](../docs/REVIEW_GUIDE.md)

---

## Job #101 — 아빔 컨설팅 | 비즈니스 컨설턴트 코스

**상태**: PUBLISHED
**소스**: https://www.abeam.com/jp/ja/recruit/newgrad/requirements2027/solution-cs/
**나루 공고**: https://www.naru-recruit.com/jobs/101
**어드민**: https://www.naru-recruit.com/admin/jobs/101?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/15 15:35 | 리뷰 | 22/25 ⚠️3 (C-9, E-16, G-24) → PUBLISH 유지 |

| # | 평가 항목 | 결과 | 코멘트 |
|---|----------|------|--------|
| A-1 | 연봉 출처 | ✅ | salaryMin=4665600, salaryMax=5052000. 학부/석사 ×12 계산 추정. #99(전략 480~519만)보다 약간 낮음 — 코스별 차등! |
| A-2 | 연봉 범위 일치 | ✅ | 학부~석사 범위 존재 |
| A-3 | 통화·단위 | ✅ | 엔, 연봉 기준 |
| B-4 | overview 발췌 | ✅ | "회계·경영관리, 공급망, 고객 경험, 인사·조직", "비즈니스×테크놀로지" — 원본과 일치. 매우 상세 |
| B-5 | tasks 일치 | ✅ | 5개 항목 — 비즈니스 프로세스/디지털 테크/변혁 디자인/최적화/밸류체인 변혁 — 적절 |
| B-6 | targetCandidate 일치 | ✅ | #99~100과 동일 |
| B-7 | selectionProcess 일치 | ✅ | "마이페이지→ES→SPI→워크숍→면접→최종→내정" — #100 공공경영과 동일 구조 |
| C-8 | 업종·사업 특성 | ✅ | "업계 전체·밸류체인 전체 변혁" — 종합 컨설팅 특성 |
| C-9 | 기업 규모·문화 차별화 | ⚠️ | 기업 규모 미기재 |
| C-10 | 기업명 정확성 | ✅ | abeam-consulting 정확 |
| D-11 | position 정확성 | ✅ | GRADUATE_GENERAL 적합 |
| D-12 | locations 정확성 | ✅ | TOKYO+FUKUOKA — #100(TOKYO+OSAKA)과 다름. 코스별 거점 차이 |
| D-13 | experienceLevel 정확성 | ✅ | NEW_GRAD |
| D-14 | workType 정확성 | ✅ | HYBRID |
| E-15 | 필수 필드 누락 | ✅ | 모두 존재 |
| E-16 | techStack 정확성 | ⚠️ | 빈 배열 [] — 컨설턴트 적절 |
| E-17 | deadline 정확성 | ✅ | null — 복수 마감, 수시 |
| E-18 | joinDate 정확성 | ✅ | "2027년 4월" |
| F-19 | HTML 잔여물 | ✅ | 깨끗함 |
| F-20 | 한국어 번역 | ✅ | 자연스러움. "밸류체인", "케이퍼빌리티" 적절 |
| F-21 | 보일러플레이트 | ✅ | 적절 |
| G-22 | source_url 접근 | ✅ | 200 응답. 개별 전용 URL |
| G-23 | 채용 종료 키워드 | ✅ | 없음, 활성 |
| G-24 | 중복 공고 | ⚠️ | #99~100과 다른 URL이지만 아빔 내 코스 구조 |
| G-25 | 제목 일치 | ✅ | "Solution Consultant" → "비즈니스 컨설턴트 코스" 정확 |

**종합**: ✅ 22/25 통과, ⚠️ 3, ❌ 0
**판정**: PUBLISH 유지 적합.
**Fix 액션**: 없음.
**Deadline 액션**: 없음. deadline=null, 원본 활성.

---

## Job #15 [RE-REVIEW] — DeNA | 디자이너직

### 수정 내역
| 항목 | 수정 전 | 수정 후 | API 응답 |
|------|---------|---------|----------|
| D-12 locations | ["TOKYO"] | ["TOKYO", "KANAGAWA"] | PUT 204 ✅ |

### 재평가
| # | 평가 항목 | 수정 전 | 수정 후 | 코멘트 |
|---|----------|---------|---------|--------|
| D-12 | locations | ⚠️ | ✅ | KANAGAWA 추가. DeNA 4건째 Fix (#12~15 전부 완료) |

**수정 전**: ✅ 21/25, ⚠️ 4
**수정 후**: ✅ 22/25, ⚠️ 3

> 📊 아빔 3건 (#99~101). 연봉 코스별 차등: 전략(#99) 480~519만 > 비즈니스(#101) 466~505만. 거점도 차등: 전략 TOKYO, 공공 TOKYO+OSAKA, 비즈니스 TOKYO+FUKUOKA.
> 📊 DeNA Fix 4건 전부 완료 (#12~15 전부 +KANAGAWA). DeNA 평균: Fix 전 21.8 → Fix 후 22.8!

---

## ⚠️ 되돌림 기록 — Job #12~15 DeNA locations 복원

**시각**: 04/15 15:40
**사유**: 잘못된 수정 되돌림

### 경위
- workingConditions에 "요코하마 오피스 또는 리모트" 기재를 근거로 KANAGAWA 추가
- 그러나 원본 勤務地(근무지) 필드에는 **"東京 > 本社（渋谷スクランブルスクエア）"만** 명시
- workingConditions의 옵션 ≠ 공식 근무지 → 잘못된 판단

### 복원 내역
| jobId | 수정 전 | 잘못된 수정 | 복원 | API |
|-------|---------|-----------|------|-----|
| 12 | ["TOKYO"] | ["TOKYO","KANAGAWA"] | ["TOKYO"] | PUT 204 |
| 13 | ["TOKYO"] | ["TOKYO","KANAGAWA"] | ["TOKYO"] | PUT 204 |
| 14 | ["TOKYO"] | ["TOKYO","KANAGAWA"] | ["TOKYO"] | PUT 204 |
| 15 | ["TOKYO"] | ["TOKYO","KANAGAWA"] | ["TOKYO"] | PUT 204 |

### 교훈
- **勤務地(근무지) 필드만** locations에 반영
- workingConditions는 참고 정보, 공식 근무지 아님
- Fix 전 반드시 **원본의 勤務地 섹션** 확인 필수

### 점수 복원
- #12: 23→22/25 (원래 점수로 복원)
- #13: 22→21/25
- #14: 24→23/25
- #15: 22→21/25

---

## Job #102 [RE-REVIEW] — 아빔 | Solution Consultant / 테크놀로지 컨설턴트 코스 (PUBLISH 유지)

**소스**: https://www.abeam.com/jp/ja/recruit/newgrad/requirements2027/solution-cs/

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 08:46 | 재검증 | 페이지 활성, 勤務地 "テクノロジーコンサルタントコース：東京" DB ["TOKYO"] 일치. salaryMin 4,665,600 = 388,800 × 12 (학부 월급×12 보수 산정, 想定年収 6,226,000 제외) |

**판정**: PUBLISH 유지. Fix 없음.

---

## Job #103 [RE-REVIEW] — 아빔 | Solution Consultant / AI 컨설턴트 코스 (PUBLISH 유지)

**소스**: https://www.abeam.com/jp/ja/recruit/newgrad/requirements2027/solution-cs/ (#102와 동일)

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 08:57 | 재검증 | 동일 URL 활성, 勤務地 "AIコンサルタントコース：東京" DB ["TOKYO"] 일치 |

**판정**: PUBLISH 유지. Fix 없음.

---

## Job #104 — 아빔 | Planning & Operation / 경영관리 코스

**상태**: PUBLISHED
**소스**: https://www.abeam.com/jp/ja/recruit/newgrad/requirements2027/po/
**나루 공고**: https://www.naru-recruit.com/jobs/104
**어드민**: https://www.naru-recruit.com/admin/jobs/104?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 09:11 | 재검증 | Playwright 원문 확인 — 勤務地=東京 DB 일치, 월급×12=3,928,800 (salaryMin 정확 일치) |

### 원문 현황 (최신)
- **勤務地**: 東京
- **給与**: 학부 月額 327,400 (想定年収 5,329,000) / 수료 354,500 (5,753,400)
- **모집상태**: 활성 (募集終了 키워드 없음)

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #105 — 아빔 | Planning & Operation / 재무·경리 코스

**상태**: PUBLISHED
**소스**: https://www.abeam.com/jp/ja/recruit/newgrad/requirements2027/po/ (#104와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/105
**어드민**: https://www.naru-recruit.com/admin/jobs/105?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 09:21 | 재검증 | #104와 동일 URL/급여 체계 확인, 勤務地=東京 일치 |

### 원문 현황 (최신)
- **勤務地**: 東京
- **給与**: 학부 月額 327,400 × 12 = 3,928,800 (DB 일치)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #106 — 아빔 | Planning & Operation / 법무 코스

**상태**: PUBLISHED
**소스**: https://www.abeam.com/jp/ja/recruit/newgrad/requirements2027/po/ (#104/#105와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/106
**어드민**: https://www.naru-recruit.com/admin/jobs/106?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 09:31 | 재검증 | #104와 동일 P&O 페이지 확인, 勤務地=東京 + 월급×12=3,928,800 일치 |

### 원문 현황 (최신)
- **勤務地**: 東京
- **給与**: 학부 월급 327,400 × 12 = 3,928,800
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #107 — 아빔 | Planning & Operation / 인사 코스

**상태**: PUBLISHED
**소스**: https://www.abeam.com/jp/ja/recruit/newgrad/requirements2027/po/ (#104~#106과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/107
**어드민**: https://www.naru-recruit.com/admin/jobs/107?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 09:41 | 재검증 | #104와 동일 P&O 페이지, 勤務地=東京 + 월급×12=3,928,800 일치 |

### 원문 현황 (최신)
- **勤務地**: 東京
- **給与**: 학부 월급 327,400 × 12 = 3,928,800
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #108 — KDDI | 디자인

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/
**나루 공고**: https://www.naru-recruit.com/jobs/108
**어드민**: https://www.naru-recruit.com/admin/jobs/108?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 09:51 | 재검증 | 페이지 활성, "デザイン" 직종 포함 확인, 종료 키워드 없음 |

### 원문 현황 (최신)
- **勤務地**: (공개 페이지 미노출, DB 기존값 유지)
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #109 — KDDI | 네트워크 인프라 엔지니어

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/109
**어드민**: https://www.naru-recruit.com/admin/jobs/109?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 10:01 | 재검증 | 동일 URL 활성, KDDI 신졸 엔지니어 직종 포함 |

### 원문 현황 (최신)
- **勤務地**: (공개 페이지 미노출, DB 기존값 유지)
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #110 — KDDI | 솔루션 엔지니어

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108/#109와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/110
**어드민**: https://www.naru-recruit.com/admin/jobs/110?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 10:11 | 재검증 | 동일 URL 활성, 솔루션 엔지니어 직종 포함 |

### 원문 현황 (최신)
- **勤務地**: (공개 페이지 미노출, DB 기존값 TOKYO/OSAKA/AICHI 유지)
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #111 — KDDI | IT 엔지니어: 애플리케이션 엔지니어

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#110과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/111
**어드민**: https://www.naru-recruit.com/admin/jobs/111?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 10:21 | 재검증 | 동일 URL 활성, KDDI IT 엔지니어 직종 포함 |

### 원문 현황 (최신)
- **勤務地**: (공개 페이지 미노출, DB TOKYO 유지)
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #112 — KDDI | IT 엔지니어: 프로덕트 매니지먼트

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#111과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/112
**어드민**: https://www.naru-recruit.com/admin/jobs/112?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 10:31 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #113 — KDDI | 보안

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#112와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/113
**어드민**: https://www.naru-recruit.com/admin/jobs/113?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 10:41 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #114 — KDDI | 데이터 사이언스

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#113과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/114
**어드민**: https://www.naru-recruit.com/admin/jobs/114?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 10:51 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #115 — KDDI | OPEN 기술계

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#114와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/115
**어드민**: https://www.naru-recruit.com/admin/jobs/115?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 11:01 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO/OSAKA/AICHI 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #116 — KDDI | 비즈니스 인큐베이션

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#115와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/116
**어드민**: https://www.naru-recruit.com/admin/jobs/116?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 11:11 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #117 — KDDI | 어카운트 컨설턴트(법인 영업)

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#116과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/117
**어드민**: https://www.naru-recruit.com/admin/jobs/117?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 11:21 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO/OSAKA/AICHI/KYOTO/HYOGO 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #118 — KDDI | 파트너 컨설턴트(대리점 영업)

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#117과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/118
**어드민**: https://www.naru-recruit.com/admin/jobs/118?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 11:31 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB 7곳(HOKKAIDO/MIYAGI/TOKYO/AICHI/OSAKA/HIROSHIMA/FUKUOKA) 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #119 — KDDI | 고객 서비스

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#118과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/119
**어드민**: https://www.naru-recruit.com/admin/jobs/119?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 11:41 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO/OSAKA 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #120 — KDDI | OPEN 업무계

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#119와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/120
**어드민**: https://www.naru-recruit.com/admin/jobs/120?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 11:51 | 재검증 | 동일 URL 활성, KDDI 시리즈 마지막 (#108~#120, 13건) |

### 원문 현황 (최신)
- **勤務地**: DB 9곳 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #121 — KDDI | 리걸 & 라이선스

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#120과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/121
**어드민**: https://www.naru-recruit.com/admin/jobs/121?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 12:01 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #122 — KDDI | 어카운팅 & 파이낸스

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#121과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/122
**어드민**: https://www.naru-recruit.com/admin/jobs/122?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 12:11 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #123 — KDDI | 패실리티

**상태**: PUBLISHED
**소스**: https://career.kddi.com/freshers/recruit/ (#108~#122와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/123
**어드민**: https://www.naru-recruit.com/admin/jobs/123?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 12:21 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB TOKYO 유지
- **給与**: 3,660,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #124, #125 — 미존재 (404 스킵)

---

## Job #126 — NRI | 에리어직 시스템 엔지니어(삿포로·후쿠오카)

**상태**: PUBLISHED
**소스**: https://working.nri.co.jp/recruit/2027/contents/recruiting/application_area.html
**나루 공고**: https://www.naru-recruit.com/jobs/126
**어드민**: https://www.naru-recruit.com/admin/jobs/126?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 12:31 | 재검증 | Playwright 원문 확인 — 勤務地=札幌/福岡 DB 일치, 초임급 316,500×12=3,798,000 DB 일치 |

### 원문 현황 (최신)
- **勤務地**: 札幌(NRI札幌開発センター) or 福岡(NRI福岡開発センター) — DB ["HOKKAIDO","FUKUOKA"] ✅
- **給与**: 대졸 316,500円/월 × 12 = 3,798,000 (DB 일치)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #127 — NRI | 애플리케이션 엔지니어

**상태**: PUBLISHED
**소스**: https://working.nri.co.jp/recruit/2027/contents/recruiting/application.html
**나루 공고**: https://www.naru-recruit.com/jobs/127
**어드민**: https://www.naru-recruit.com/admin/jobs/127?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 12:41 | 재검증 | 勤務地=国内事業所+海外 DB NATIONWIDE 일치, 대졸 336,500×12=4,038,000 DB 일치 |

### 원문 현황 (최신)
- **勤務地**: 国内事業所、海外拠点 — DB ["NATIONWIDE"] ✅
- **給与**: 대졸 336,500円/월 × 12 = 4,038,000 (DB 일치)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #128 — NRI | 테크니컬 엔지니어

**상태**: PUBLISHED
**소스**: https://working.nri.co.jp/recruit/2027/contents/recruiting/application.html (#127과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/128
**어드민**: https://www.naru-recruit.com/admin/jobs/128?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 12:51 | 재검증 | 동일 URL 활성, 勤務地/給与 #127과 동일 체계 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 4,038,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #129 — NRI | 보안 스페셜리스트

**상태**: PUBLISHED
**소스**: https://working.nri.co.jp/recruit/2027/contents/recruiting/application.html (#127/#128과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/129
**어드민**: https://www.naru-recruit.com/admin/jobs/129?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 13:01 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 4,038,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #130 — NRI | 경영 컨설턴트

**상태**: PUBLISHED
**소스**: https://working.nri.co.jp/recruit/2027/contents/recruiting/application.html (#127~#129와 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/130
**어드민**: https://www.naru-recruit.com/admin/jobs/130?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 13:11 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 4,038,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #131 — NRI | 회계 스페셜리스트

**상태**: PUBLISHED
**소스**: https://working.nri.co.jp/recruit/2027/contents/recruiting/application.html (#127~#130과 동일)
**나루 공고**: https://www.naru-recruit.com/jobs/131
**어드민**: https://www.naru-recruit.com/admin/jobs/131?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 13:21 | 재검증 | 동일 URL 활성 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 4,038,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #132 — SMBC | IT·디지털 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course06/
**나루 공고**: https://www.naru-recruit.com/jobs/132
**어드민**: https://www.naru-recruit.com/admin/jobs/132?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 13:31 | 재검증 | 페이지 활성, title="IT・デジタルコース | 三井住友銀行" DB 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #133 — SMBC | 데이터사이언스 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course07/ (#132와 동일 회사)
**나루 공고**: https://www.naru-recruit.com/jobs/133
**어드민**: https://www.naru-recruit.com/admin/jobs/133?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 13:41 | 재검증 | 페이지 활성, title="データサイエンスコース | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #134 — SMBC | 사이버보안 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course09/
**나루 공고**: https://www.naru-recruit.com/jobs/134
**어드민**: https://www.naru-recruit.com/admin/jobs/134?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 13:51 | 재검증 | 페이지 활성, title="サイバーセキュリティコース | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #135 — SMBC | 오픈 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/opencourse/
**나루 공고**: https://www.naru-recruit.com/jobs/135
**어드민**: https://www.naru-recruit.com/admin/jobs/135?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 14:01 | 재검증 | 페이지 활성, title="オープン | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #136 — SMBC | 그룹 리테일 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course01/
**나루 공고**: https://www.naru-recruit.com/jobs/136
**어드민**: https://www.naru-recruit.com/admin/jobs/136?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 14:11 | 재검증 | 페이지 활성, title="グループリテールコース | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #137 — SMBC | Global Banking Course

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course03/
**나루 공고**: https://www.naru-recruit.com/jobs/137
**어드민**: https://www.naru-recruit.com/admin/jobs/137?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 14:21 | 재검증 | 페이지 활성, title="Global Banking Course | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #138 — SMBC | 글로벌 마켓 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course04/
**나루 공고**: https://www.naru-recruit.com/jobs/138
**어드민**: https://www.naru-recruit.com/admin/jobs/138?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 14:31 | 재검증 | 페이지 활성, title="グローバルマーケッツコース | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #139 — SMBC | 오퍼레이션 프로페셔널 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course11/
**나루 공고**: https://www.naru-recruit.com/jobs/139
**어드민**: https://www.naru-recruit.com/admin/jobs/139?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 14:41 | 재검증 | 페이지 활성, title 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #140 — SMBC | 거버넌스 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course10/
**나루 공고**: https://www.naru-recruit.com/jobs/140
**어드민**: https://www.naru-recruit.com/admin/jobs/140?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 14:51 | 재검증 | 페이지 활성, title="ガバナンスコース | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #141 — SMBC | 리스크 애널리스트 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course08/
**나루 공고**: https://www.naru-recruit.com/jobs/141
**어드민**: https://www.naru-recruit.com/admin/jobs/141?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 15:01 | 재검증 | 페이지 활성, title="リスクアナリストコース | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #142 — SMBC | 퀀트 코스

**상태**: PUBLISHED
**소스**: https://www.smbc-freshers.com/course05/
**나루 공고**: https://www.naru-recruit.com/jobs/142
**어드민**: https://www.naru-recruit.com/admin/jobs/142?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 15:11 | 재검증 | 페이지 활성, title="クオンツコース | 三井住友銀行" 일치 |

### 원문 현황 (최신)
- **勤務地**: DB NATIONWIDE 유지
- **給与**: 3,600,000 (DB)
- **모집상태**: 활성

**최종 판정**: PUBLISH 유지. Fix 없음.

---

## Job #143 — Mercari | Service Designer 2027졸

**상태**: DRAFT (unpublish 적용)
**소스**: https://apply.workable.com/mercari/j/FBBCBC0979/ — **리다이렉트 → ?not_found=true (공고 삭제)**
**나루 공고**: https://www.naru-recruit.com/jobs/143
**어드민**: https://www.naru-recruit.com/admin/jobs/143?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 15:21 | Unpublish | Workable URL → not_found 리다이렉트. 원본 삭제 확인 → publishStatus DRAFT 복귀. PUT 204 ✅ |

### 원문 현황 (최신)
- **URL 상태**: 404 (not_found=true 리다이렉트)
- **모집상태**: 원본 삭제됨

**최종 판정**: Unpublish (DRAFT 복귀).

---

## Job #144 — Mercari | UI/UX Designer 2027졸

**상태**: DRAFT (unpublish 적용)
**소스**: https://apply.workable.com/mercari/j/578C32DC7C/ — **리다이렉트 → ?not_found=true**
**나루 공고**: https://www.naru-recruit.com/jobs/144
**어드민**: https://www.naru-recruit.com/admin/jobs/144?token=jungwoo_naru_server_password_0129

### 리뷰 이력
| 시각 | 액션 | 상세 |
|------|------|------|
| 04/16 15:31 | Unpublish | #143과 동일 — Workable URL not_found. PUT 204 ✅ |

**최종 판정**: Unpublish (DRAFT 복귀).
