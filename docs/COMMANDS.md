# 📋 명령 기록 (Command Log)

정우의 지시 사항과 처리 내역을 시간순으로 기록합니다.

---

## 2026-03-24

### [09:00] 레포지토리 확인
- **명령**: 깃헙 `blueberry_team` 레포 중 `blueberry_naru` 존재 확인
- **처리**: `gh repo list blueberry-team` → `blueberry-team/blueberry_naru` 확인
- **결과**: ✅ private repo, Engineer 팀 maintain 권한

### [09:10] 레포 클론
- **명령**: `blueberry_naru`를 Documents 안에 클론
- **처리**: `gh repo clone blueberry-team/blueberry_naru ~/Documents/blueberry_naru`
- **결과**: ✅ Nuxt.js + Spring Boot 프로젝트 확인

### [09:15] 서비스 파악
- **명령**: "공고에 대해서 꾸준히 데이터 적재가 필요한 서비스"
- **파악**: 한국/일본 채용 플랫폼 naru-recruit.com, Job 엔티티 PostgreSQL 저장

### [09:20] DRAFT 기능 확인
- **명령**: pull 후 드래프트 가능한지 확인
- **처리**: `feature/publish-status` 브랜치 확인 → DRAFT/PUBLISHED 상태 구조 파악
- **결과**: ✅ `POST /api/dev/jobs` + `"status": "DRAFT"` 으로 적재 가능

### [09:25] API 토큰 수신 및 테스트 적재
- **명령**: 토큰 `jungwoo_naru_server_password_0129` 공유, 임시 데이터 적재 테스트
- **처리**: jsol 기업 슬러그로 테스트 공고 생성 (ID: 465)
- **실수 1**: 정우가 확인하기 전에 바로 삭제 → 재생성 요청
- **재처리**: 동일 데이터로 재생성 (ID: 465) → 삭제 안 함
- **결과**: ✅ DRAFT 적재/조회 흐름 검증 완료

### [09:30] publish-status 브랜치 머지 확인
- **명령**: 머지 완료 후 확인
- **처리**: `git pull` → PublishStatus 전체 확장 확인
- **결과**: ✅ Job/Company/Event/Mentoring 전부 DRAFT 지원

### [09:35] 기업/공고 현황 분석
- **명령**: 기업 리스트 + 공고 정보 분석, 매일 보고
- **처리**:
  - 122개 기업, 437개 공고 수집
  - 공고 0개 기업 45개 추출 (크롤링 우선순위)
  - `scripts/naru_daily_report.py` 생성
  - HEARTBEAT.md에 매일 1회 보고 등록
- **결과**: ✅ 첫 리포트 Discord #일상-봇 전송

### [09:40] 히타치 크롤러 구축
- **명령**: "히타치만 먼저 해보자 공고 품질을 보고 싶어서"
- **처리**:
  - hitachi.jposting.net JS 렌더링 우회
  - `jscudp.jcareers.com` API 발견
  - 705개 공고 수집 확인
- **결과**: ✅ API 구조 파악 완료

### [09:45] 크롤러 시스템 구축
- **명령**: "품질이 완벽해야해, 제대로 된 규칙과 롤을 만들어야 하고, 내가 파악할 수 있어야 해"
- **처리**:
  - `naru-crawler/` 프레임워크 설계 및 구현
  - position/location/experience 매핑 룰 JSON
  - 품질 검증기 (ValidationError)
  - runner.py CLI (`--dry-run`, `--limit`, `--report-only`)
- **결과**: ✅ 이 레포 생성

### [09:50] GitHub 프라이빗 레포 생성
- **명령**: "깃헙 프라이빗 레포지토리로 만들어서 올려줘 + 명령/실수 기록 문서도 넣어줘"
- **처리**: `blueberry-team/naru-crawler` 프라이빗 레포 생성 및 push
- **결과**: ✅ (진행중)
