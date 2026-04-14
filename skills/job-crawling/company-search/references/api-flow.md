# API 처리 흐름

이 스킬은 파일 저장이 아니라 Company DRAFT 저장을 목표로 한다.

## 출력 목표

- 회사 1건당 `POST /api/dev/companies` 1회
- 최종 payload에서 사용자에게 보여줄 텍스트는 한국어로 채운다.
- `publishStatus: "DRAFT"` 로 제출

## 생성 순서

1. 공식 사이트 탐색
2. 회사 기본 정보 추출
3. 채용 / 복리후생 / 기업 이념 / IR 정보 추출
4. 필요 시 EDINET 보조 사용
5. 필요 시 OpenWork로 평점 수집
6. 추출한 정보를 필드 형식에 맞게 정리
7. 한국어 번역 규칙에 따라 최종 payload 생성
8. [`payload-schema.md`](./payload-schema.md) 와 [`checklist.md`](./checklist.md)를 기준으로 검증
9. `POST /api/dev/companies` 로 DRAFT 제출

## 우선순위

1. 공식 사이트
2. EDINET
3. OpenWork

공식 사이트에 근거가 있으면 외부 소스로 덮어쓰지 않는다.
