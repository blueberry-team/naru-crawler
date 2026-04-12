# 분류 규칙

## experienceLevel

- 이 스킬에서 수집하는 모든 공고의 `experienceLevel` 은 항상 `NEW_GRAD`
- 경력직, experienced hire, 아르바이트, 신입이 아닌 공고는 제외한다.

## position

아래 6개 enum 만 사용한다.

- `GRADUATE_GENERAL`
- `GRADUATE_ENGINEER`
- `GRADUATE_TECHNICAL`
- `GRADUATE_DESIGN`
- `GRADUATE_SPECIALIST`
- `GRADUATE_OTHER`

매핑 규칙:

- `総合職`, `ビジネス`, `企画`, `営業`, `コーポレート` → `GRADUATE_GENERAL`
- `エンジニア`, `ソフトウェア`, `開発`, `IT` → `GRADUATE_ENGINEER`
- `技術職`, `研究`, `製造`, `電気`, `機械`, `ハード` → `GRADUATE_TECHNICAL`
- `デザイン`, `UI/UX` → `GRADUATE_DESIGN`
- `法務`, `会計`, `税務`, `人事`, `労務` → `GRADUATE_SPECIALIST`
- 그 외 → `GRADUATE_OTHER`

`BACKEND`, `FRONTEND` 같은 비신입 상세 enum 은 사용하지 않는다.

## locations

`locations` 는 비어 있지 않은 도도부현 enum 배열이다.

예시:

- 도쿄만 있음: `["TOKYO"]`
- 여러 지역: `["TOKYO","OSAKA","FUKUOKA"]`
- 불명확: `["UNKNOWN"]`

규칙:

1. 명시된 도도부현을 모두 저장한다.
2. 배치 미정이어도 같은 단락 / 표 / 그림 안에 후보지가 나열돼 있으면 `UNKNOWN` 대신 후보지를 저장한다.
3. 도시명이나 거점명만 있을 때는 도도부현이 확실할 때만 매핑한다.
4. 페이지에 `全国`, `各拠点`, `国内各地` 만 있고 구체 후보지가 없으면 `["NATIONWIDE"]`
5. 추출 실패 시 `["UNKNOWN"]`

안전한 도시 → 도도부현 매핑:

- 渋谷 / 新宿 / 品川 / 六本木 / 秋葉原 / 池袋 → `TOKYO`
- 横浜 / 川崎 → `KANAGAWA`
- 名古屋 → `AICHI`
- 札幌 → `HOKKAIDO`
- 仙台 → `MIYAGI`
- 梅田 / 難波 → `OSAKA`
- 神戸 → `HYOGO`
- 京都 → `KYOTO`
- 博多 / 福岡市 → `FUKUOKA`
- 那覇 → `OKINAWA`

안전 매핑 목록 밖은 추측하지 않는다.

## workType

근무 형태가 명시된 경우에만 분류한다.

탐색 대상 섹션:

- `募集要項`
- `勤務形態`
- `働き方`
- `勤務制度`
- `勤務時間`
- `福利厚生`
- `制度`
- `社内制度`
- `働く環境`
- `FAQ`
- `よくある質問`
- footnote와 작은 글씨
- 이미지, 배너, 차트, alt text

매핑:

- `フルリモート`, `完全在宅`, `完全リモート`, `全国から勤務可`, `Full Remote`, `Fully Remote` → `REMOTE`
- `リモート可`, `在宅勤務可`, `テレワーク可`, `一部リモート`, `出社と在宅併用`, `ハイブリッド`, `週◯日出社`, `出社＋リモート` → `HYBRID`
- `出社必須`, `原則出社`, `オフィス勤務`, `常駐`, `対面勤務`, `在宅不可` → `ONSITE`
- 불명확하면 `UNKNOWN`

사무실 위치만으로 `ONSITE` 를 추론하지 않는다.

## title

`title` 은 공식 트랙명 또는 코스명이어야 한다.

규칙:

- 누락된 제목을 임의로 만들지 않는다.
- `本選考`, `早期選考`, `インターン`, `エントリー` 가 공식 명칭 일부면 유지한다.
- 제목이 이미지 안에만 있으면 Vision으로 읽는다.
- `【number】` prefix 는 제거한다.

아래 generic label은 단독으로 title 이 될 수 없다.

- `募集要項`
- `選考フロー`
- `応募受付期間`
- `採用基本情報`
- `エントリー`
- `マイページ`
- `新卒採用`

title 추출 우선순위:

1. 표, 탭, 카드에 있는 코스명 / 직무명
2. `機能名 + （職種/コース名）` 형식일 때 괄호 안
3. hero heading `H1/H2`
4. year + track + selection type 조합이 보이는 breadcrumb 또는 main heading
5. listing card name
6. 마지막 fallback 으로 browser title

최종 체크:

- title 이 generic function label이 아닌가
- title 과 `position` 이 모순되지 않는가
- 같은 회사 페이지 세트 안에서 중복되지 않는가
