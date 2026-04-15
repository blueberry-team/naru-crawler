# Company Rating Rules

## source

- OpenWork 검색 리스트 페이지를 직접 사용한다.
- URL:
  - `https://www.openwork.jp/company_list?field=&pref=&src_str={企業名}&sort=1`

## 규칙

- 상세 페이지로 들어가지 않는다.
- 목록에서 해당 기업의 종합 평가 점수를 읽는다.
- 소수점 첫째 자리 반올림
- 가져오지 못하면:
  - `companyRating = null`
  - `ratingSource = null`
- `0` 으로 채우지 않는다.

## 금지

- OpenWork 홈을 경유해 불필요한 랭킹 데이터를 읽지 않는다.
- OpenWork URL을 `companySourceUrls` 에 넣지 않는다.
