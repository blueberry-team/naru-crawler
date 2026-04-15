# HOLD 사례

## 사례 1: jobSourceUrl 404

```json
{
  "jobId": 1203,
  "companySlug": "sega",
  "title": "게임 시스템 프로그래머",
  "jobSourceUrl": "https://www.sega.co.jp/recruit/career/detail/gs-001"
}
```

검증: `jobSourceUrl` 접근 시 404 응답.

판정: **HOLD**
보고: "원본 URL 접근 불가 (404)"

---

## 사례 2: 채용 사이트 메인 페이지

```json
{
  "jobId": 1204,
  "companySlug": "rakuten",
  "title": "프론트엔드 엔지니어",
  "jobSourceUrl": "https://careers.rakuten.co.jp/"
}
```

검증: `jobSourceUrl` 접근 시 200 이지만, 페이지가 라쿠텐 채용 사이트 메인. 여러 공고가 나열된 목록이며 개별 공고 상세가 아님.

판정: **HOLD**
보고: "jobSourceUrl이 공고 상세가 아닌 채용 사이트 메인 페이지입니다"

---

## 사례 3: 채용 종료 키워드

```json
{
  "jobId": 1205,
  "companySlug": "mercari",
  "title": "SRE 엔지니어",
  "jobSourceUrl": "https://careers.mercari.com/job/sre-001"
}
```

검증: `jobSourceUrl` 접근 시 200 이지만, 페이지 본문에 "この募集は終了しました" 표시.

판정: **HOLD**
보고: "원본 페이지에서 채용 종료 키워드 발견: 募集は終了しました"

---

## 사례 4: PUBLISHED 중복

```json
{
  "jobId": 1206,
  "companySlug": "line",
  "title": "서버 사이드 엔지니어",
  "jobSourceUrl": "https://careers.linecorp.com/jobs/server-001"
}
```

검증: `GET /api/jobs?size=200` 에서 동일 `jobSourceUrl` 의 PUBLISHED 공고 발견 (ID=980).

판정: **HOLD**
보고: "이미 PUBLISHED 된 동일 공고 존재 (ID=980)"

---

## 사례 5: 리다이렉트 후 메인으로 이동

```json
{
  "jobId": 1207,
  "companySlug": "sony",
  "title": "AI 연구원",
  "jobSourceUrl": "https://www.sony.co.jp/recruit/career/ai-research-001"
}
```

검증: `jobSourceUrl` 접근 시 301 → 최종 도착 URL 이 `https://www.sony.co.jp/recruit/` (채용 메인).

판정: **HOLD**
보고: "리다이렉트 후 채용 메인으로 이동, 공고 만료 의심"

---

## 사례 6: jobSourceUrl 과 title 불일치

```json
{
  "jobId": 1208,
  "companySlug": "cyberagent",
  "title": "iOS 엔지니어",
  "jobSourceUrl": "https://www.cyberagent.co.jp/careers/detail/android-dev"
}
```

검증: `jobSourceUrl` 페이지의 직무 제목이 "Androidエンジニア" 이며 DB title "iOS 엔지니어" 와 불일치.

판정: **HOLD**
보고: "원본 페이지의 공고와 적재된 title이 일치하지 않습니다"
