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
