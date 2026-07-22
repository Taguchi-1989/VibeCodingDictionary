---
id: J-99
title: CoWoS
title_reading: コウオス
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 6
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-06-23
related_terms:
  - HBM
  - TSMC
  - GPU
  - 半導体サプライチェーン
  - ハイブリッドボンディング
status: needs_review
---

# CoWoS

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Chip-on-Wafer-on-Substrate の略。GPU ダイと HBM（High Bandwidth Memory）スタックを 1 枚の基板に物理統合する TSMC の先端パッケージ技術です。2026 年 6 月時点、CoWoS こそが AI GPU 供給の最大ボトルネックとされています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

CoWoS は、GPU の製造を「前工程」と「後工程」の 2 段階に分けたときの後工程を担います。前工程では TSMC の 3nm / 2nm プロセスと ASML の EUV（Extreme Ultraviolet、極端紫外線）露光装置で GPU ダイそのものを作ります。後工程の CoWoS では、出来上がった GPU ダイと HBM スタックを同じシリコンインターポーザ（中継基板）の上に並べ、数千本の極細配線で直結して 1 パッケージに仕上げます。

この統合によって GPU コアと HBM の距離が数百マイクロメートルに縮まり、PCIe（Peripheral Component Interconnect Express）で別ボードを繋ぐ場合と比べて桁違いの帯域（数 TB/s）を引き出せます。HBM の広帯域はここで初めて有効になります。

## どこで出会うか

NVIDIA の H100 / H200 / B200 といった AI 学習・推論向けデータセンター GPU は、すべて TSMC CoWoS で後工程を仕上げています。「GPU が足りない」「AI チップの供給が逼迫している」という報道の裏側には、CoWoS の生産能力がそのまま上限として効いています。

2026 年 6 月時点の状況は次の通りです。NVIDIA が TSMC の CoWoS 能力の 50〜60% を単独予約し、TSMC は月産 3.5 万枚（2024 年末）から月産 13 万枚（2026 年末目標）へ約 4 倍の増産を進めています。それでも需要に追いつかず、Amkor や ASE といった外部パッケージングメーカーにも発注が広がっています。分析各社は「ボトルネックは HBM から CoWoS に移動した」と指摘しており、HBM を増産しても CoWoS が詰まれば GPU は増えません。

## メイン図

### 図の狙い

「GPU ダイと HBM スタックがどのように CoWoS で統合されるか」を断面図スタイルで見せ、なぜ帯域が跳ね上がり、なぜここが供給のボトルネックになるのかを一目で掴んでもらいます。

### A. CoWoS パッケージ断面（レイヤー構造）

- 最下層: ABF（Ajinomoto Build-up Film）基板。味の素製の絶縁フィルムが世界シェア 95%。
- 中層: シリコンインターポーザ（CoWoS の「WoS」部分）。微細配線（RDL）で上層のダイ間を高密度に結ぶ
- 上層左: GPU ダイ（TSMC 3nm で製造。「CoW」の Chip-on-Wafer 部分に相当）
- 上層右: HBM スタック × 複数個（SK Hynix / Micron / Samsung がダイを TSMC に持ち込み、CoWoS で GPU に接合）
- 矢印: GPU ダイ ↔ HBM スタック 間を走る高密度配線（帯域数 TB/s を視覚化）

## 会話での使い方例

「H100 が足りないのは CoWoS のキャパが詰まっているからで、HBM が増えても意味がないんですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

GPU ダイと HBM を 1 枚の基板に物理統合し、数 TB/s の帯域を実現する後工程パッケージ技術です。

### 2. うれしさ

チップ間の距離を数百マイクロメートルに縮め、PCIe 接続では得られない極大帯域を引き出せます。

### 3. 注意点

製造は TSMC しか量産できず、NVIDIA が能力の 50〜60% を予約するため他社の確保が難しい状況です（2026 年 6 月時点）。

### 4. どこで役立つか

AI データセンター GPU（H100/H200/B200 系）はすべて CoWoS 経由。AI 供給制約を読み解く鍵です。

### 5. はじめに

「前工程＝ダイ製造、後工程＝CoWoS 統合」の 2 段階構造と、ボトルネックが HBM から CoWoS に移った経緯を押さえると芯が掴めます。

### 6. 深掘り先

HBM、TSMC 3D Fabric Alliance、ハイブリッドボンディング、ABF 基板、半導体サプライチェーン

## 開発フローでの位置（必須）

1. 前工程（ダイ製造） — TSMC 3nm/2nm + ASML EUV で GPU ダイを焼く。歩留まりが GPU 単価の大半を決める
2. HBM 製造 — SK Hynix / Micron / Samsung が DRAM ダイを TSV（Through Silicon Via）で縦積みし HBM スタックを作る
3. CoWoS 接合 — TSMC がシリコンインターポーザ上に GPU ダイと HBM スタックを搭載。ASMPT / BESI のボンディング装置で接合し、Camtek / KLA で検査する
4. ABF 基板実装 — CoWoS パッケージを Unimicron / Ibiden 等が作る ABF 基板に実装。基板稼働率 90% 逼迫（2026 年 6 月時点）
5. 出荷 → AI インフラ — 完成 GPU がデータセンターへ。CoWoS のキャパが月産 GPU 上限をそのまま決める

## 関連用語

- HBM
- TSMC
- GPU
- 半導体サプライチェーン
- ハイブリッドボンディング

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- CoWoS はGPUの物理的なアーキテクチャ（高速接続）の話で、データを超高速でやり取りするための鍵になっている、というのが最初の腹落ちどころだった。
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: ハードとソフト、どちらも大事。ハード側の代表がTSMC、ソフト側の代表がNVIDIA（CUDAなど）。ハード側の方がむしろ競争力の源泉になっているのではないか。
- 👍 良い点: ハードはサプライチェーンごと組み上げる必要があって時間がかかる分、参入障壁になっている。一方でソフト側は、従来は積み重ねられた研究開発が参入障壁だったが、その設計自体を LLM を使ってできるようになってきていて、この障壁が崩れつつあるのではないか。
- 👎 ダメな点: これはつまり、自分たち（AI/ソフト産業）が作った LLM によって、自分たちの産業構造の強みが自己破壊されていく、という皮肉な動きになるのではないかという気がしている。
- 👥 誰向けか: 
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: CoWoS パッケージの断面図を縦 3 層で描く。最下層に ABF 基板（「味の素製」ラベル付き）、中層にシリコンインターポーザ（高密度配線の格子模様）、上層に GPU ダイ（左）と HBM スタック 4 本（右）を並べる。GPU ダイと HBM スタック間に「数 TB/s」ラベルの太矢印を入れる。右端に隣の PCIe ケーブルの細矢印を並べ「数十 GB/s」と書いて帯域差を対比する。
- 登場人物: エンジニア（著者の分身）1 名が断面図の横に立ち、インターポーザ中層の配線格子を指差している。
- 吹き出し・心の声: 「GPU もう無いんじゃなくて CoWoS が詰まってるんだ——ここが増えないと何も増えない」
- 中央に置くキーワード/ラベル: 「CoWoS＝GPU＋HBM を 1 枚に統合」「ボトルネックはここ」「月産上限 = CoWoS 上限」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出: 断面積み上げ図の小アイコンを 1 と 3 に添える）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: TSMC ファブのシルエット＋ EUV 露光の光芒
- Step 2 のアイコン/絵柄: HBM スタックの縦積み（DRAM ダイが重なる断面）
- Step 3 のアイコン/絵柄: インターポーザ上に GPU ダイと HBM を並べてボンディング装置が接合する様子
- Step 4 のアイコン/絵柄: ABF 基板にパッケージを実装するリフロー炉のイメージ
- Step 5 のアイコン/絵柄: データセンターのラックに GPU サーバが収まるシルエット
- 矢印で示す流れの意図: 前工程 → HBM 製造 → CoWoS 統合 → 基板実装 → AI インフラという「GPU 1 枚が完成するまでの縦の流れ」と、CoWoS が中央で全体を律速する位置にあることを強調する

## コミュニティ補完メモ

- 半導体サプライチェーン（J 章・別エントリ候補）との住み分け: 本エントリは CoWoS という後工程の 1 技術に特化。チップ→装置→材料→原料の 4 層全体俯瞰は別エントリに譲る。
- HBM（J 章・別エントリ候補）との住み分け: HBM はメモリ製品（SK Hynix / Micron / Samsung が製造）、CoWoS はそれを GPU に「接合する工程」。「HBM が出来ても CoWoS が詰まれば GPU に載らない」の上下関係を本文で明示済み。
- GPU（G 章系エントリ）との住み分け: GPU の演算仕様・AI 学習用途は GPU エントリが担う。本エントリは「その GPU がどう作られるか・なぜ供給が逼迫するか」の製造サイドに立つ。
- ハイブリッドボンディング（別エントリ候補）との住み分け: ハイブリッドボンディングは HBM スタック内の DRAM ダイ同士の接合技術（BESI/Applied Materials 等が担う）。CoWoS はその HBM スタックを GPU ダイに繋ぐ上位の統合工程。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- CoWoS Not HBM Is the Real AI Supply Bottleneck (Medium) https://medium.com/@Elongated_musk/cowos-not-hbm-is-the-real-ai-supply-bottleneck-d0ae8f3f7ce4 — checked 2026-06-23（「ボトルネックが HBM から CoWoS に移動した」の一次論拠）
- Advanced Packaging: Nvidia Secures 60% of CoWoS Capacity (Astute Group) https://www.astutegroup.com/news/industrial/advanced-packaging-demand-soars-nvidia-secures-60-of-cowos-capacity/ — checked 2026-06-23（NVIDIA の CoWoS 50〜60% 予約・TSMC 月産 3.5 万→13 万枚増産）
- TSMC 3D Fabric Alliance Substrate Partners (Asia Business Daily) https://www.asiae.co.kr/en/article/2026043014033228020 — checked 2026-06-23（TSMC 3D Fabric Alliance の接合・検査・ABF 基板・HBM 各社の役割分担）
- ABF 基板の需要逼迫・味の素 95% シェア (BigGo Finance) https://finance.biggo.com/news/ZU2KJZ4BpwxG186NIOsE — checked 2026-06-23（ABF 基板稼働率 90% 逼迫・30% 値上げ）
- ledgers/inference_hardware_landscape_2026.md §11（NVIDIA→TSMC ライン・CoWoS こそ真のボトルネック） — checked 2026-06-23（本調査ノートの一次整理）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- 時変情報: NVIDIA の CoWoS 予約比率（50〜60%）・TSMC 月産能力（13 万枚目標）・ABF 基板稼働率（90%）はいずれも 2026 年 6 月時点のスナップショット。書籍化前に一次情報で再確認すること。
- CoWoS の「CoW」部分: Chip-on-Wafer の略で、GPU ダイをインターポーザウェハに直接搭載する工程を指す。「WoS」は Wafer-on-Substrate でインターポーザを ABF 基板に実装する工程。2 段階を合わせて CoWoS と呼ぶ。
- TSMC 3D Fabric Alliance の主要タッグ相手: 接合（ASMPT 星・BESI 蘭）、検査（KLA 米・Camtek イスラエル・Onto 米）、ABF 基板（Unimicron 台・Ibiden / Shinko / Toppan 日・Samsung 電機 韓）、HBM 物理統合（SK Hynix / Micron / Samsung）。
- 用語の整理: 「ボトルネックが HBM から CoWoS に移動した」は「HBM は十分増産できるようになったが、それを GPU に搭載する CoWoS 工程が追いつかない」という意味。ボトルネックは潰すと次が顔を出す、という連鎖の現在地。
