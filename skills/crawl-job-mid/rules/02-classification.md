# 분류 규칙

## experienceLevel

- 이 스킬에서 수집하는 모든 공고의 `experienceLevel` 은 항상 `MID_CAREER`
- 신입, 인턴, 아르바이트, 업무위탁 전용 모집, 중도채용이 아닌 공고는 제외한다.

## position

신입용 `GRADUATE_*` enum 은 사용하지 않는다.

가능한 한 백엔드 `Position` enum 에 직접 매핑한다.
허용 enum 목록은 반드시 [`../references/enums.md`](../references/enums.md) 를 기준으로 확인한다.

대표 매핑 예시:

- `バックエンド`, `サーバーサイド`, `API開発` → `BACKEND`
- `フロントエンド`, `UI実装` → `FRONTEND`
- `フルスタック` → `FULLSTACK`
- `iOS` → `IOS`
- `Android` → `ANDROID`
- `インフラ` → `INFRA`
- `DevOps`, `SRE` → `DEVOPS`
- `クラウド` → `CLOUD`
- `セキュリティ` → `SECURITY`
- `QA`, `テスト` → `QA_TEST`
- `データエンジニア` → `DATA_ENGINEER`
- `データサイエンティスト` → `DATA_SCIENTIST`
- `機械学習`, `ML` → `ML_ENGINEER`
- `AI研究` → `AI_RESEARCH`
- `UI/UX` → `UX_UI`
- `プロダクトデザイン` → `PRODUCT_DESIGN`
- `プロダクトマネージャー`, `PdM`, `PO` → `PM_PO`
- `サービス企画` → `SERVICE_PLANNING`
- `事業企画` → `BUSINESS_STRATEGY`
- `経営企画` → `CORPORATE_STRATEGY`
- `新規事業` → `NEW_BUSINESS`
- `法人営業` → `B2B_SALES`
- `個人営業` → `B2C_SALES`
- `パートナー営業` → `PARTNER_SALES`
- `採用担当` → `RECRUITING`
- `HRBP` → `HRBP`
- `経理` → `ACCOUNTING`
- `財務` → `FINANCE`
- `法務` → `LEGAL_COUNSEL`

정확히 맞는 enum 이 없으면 해당 카테고리의 `*_OTHER` 를 사용한다.
문서에 없는 enum 이름을 새로 만들지 않는다.

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

`title` 은 공식 직무명 또는 포지션명이어야 한다.

규칙:

- 누락된 제목을 임의로 만들지 않는다.
- `正社員`, `契約社員`, `業務委託`, `マネージャー候補` 가 공식 명칭 일부면 유지한다.
- 제목이 이미지 안에만 있으면 Vision으로 읽는다.
- `【number】` prefix 는 제거한다.

아래 generic label은 단독으로 title 이 될 수 없다.

- `募集要項`
- `募集要件`
- `応募する`
- `マイページ`
- `中途採用`
- `キャリア採用`

title 추출 우선순위:

1. 표, 탭, 카드에 있는 직무명 / 포지션명
2. `機能名 + （職種名）` 형식일 때 괄호 안
3. hero heading `H1/H2`
4. role + grade + employment type 조합이 보이는 breadcrumb 또는 main heading
5. listing card name
6. 마지막 fallback 으로 browser title

최종 체크:

- title 이 generic function label이 아닌가
- title 과 `position` 이 모순되지 않는가
- 같은 회사 페이지 세트 안에서 중복되지 않는가
