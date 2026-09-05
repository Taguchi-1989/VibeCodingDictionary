---
id: J-95
title: 半導体サプライチェーン
title_reading: ハンドウタイサプライチェーン
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 6
importance: B
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-06-23
related_terms:
  - HBM
  - CoWoS
  - ASML
  - TSMC
  - GPU
status: ready
---

# 半導体サプライチェーン

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

「GPU が出ない理由」を遡ると、チップ→装置→材料→原料の4層が直列でつながっていて、各層に別々の独占企業が張り付いています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

「AI チップが足りない」という話は、GPU（画像処理装置）の生産だけの問題ではありません。GPU に積む HBM（High Bandwidth Memory、高帯域幅メモリ）を作る装置、その装置に使う材料、さらに材料の原料と、チップ→装置→材料→原料の4層が直列でつながっており、どの層の1社が詰まっても GPU は出てきません。このエントリはその4層の全体像と「直列ボトルネック」の構造を俯瞰します。個別の装置・材料・鉱物は J-96〜J-99 に譲り、ここは地図として機能することを目的にしています（2026年6月時点の情報にもとづきます）。

## どこで出会うか

「AI バブルの真の受益者は GPU メーカーではなく、ツルハシを売る装置メーカーだ」という言い回しで、投資家・半導体アナリストのレポートによく登場します。AI 開発を進める立場では「なぜ H100 の納期が延びるのか」「なぜ HBM の値段が上がり続けるのか」を理解しようとすると、自然にこの4層の話に行き着きます。EUV（Extreme Ultraviolet、極端紫外線）露光・CoWoS（Chip on Wafer on Substrate、先端パッケージ技術）・HBM といった語が同時に出てくる記事やポッドキャストが、最初の接触点になることが多いです。

## メイン図

### 図の狙い

4層の縦積み構造と「直列ボトルネック」の流れを1枚で示し、どの層でも1社詰まれば GPU が止まることを視覚的に掴んでもらいます。

### 4層の入れ子構造

```
【チップ層】  GPU: NVIDIA（米）  HBM: SK Hynix（韓）  製造: TSMC（台）
      ↑
【装置層】  露光: ASML（蘭 / EUV 100%独占）  薄化: DISCO（日 / 世界独占）
          接合: ASMPT（星）・BESI（蘭）  検査: KLA（米）  光学: Zeiss（独）
      ↑
【材料層】  ABF 基板フィルム: 味の素（日 / 95%）  RDL 絶縁: 旭化成（日）
          EUV フォトレジスト: JSR・東京応化・信越化学（日 / 90%超）
          シリコンウェハ: 信越化学・SUMCO（日 / 過半）
      ↑
【原料層】  石化系（樹脂・溶剤）→ 日本の合成ノウハウ
          元素系（Ga・Ge・希ガス・レアアース）→ 中国の精錬（90%前後）
```

直列ボトルネック: EUV（ASML）→ HBM（SK Hynix ＋ DISCO 薄化）→ CoWoS（TSMC ＋ 接合 ＋ 味の素 ABF ＋ 旭化成 Pimel）。このどれか1つが詰まれば GPU が出ません。

## 会話での使い方例

「GPU 不足の根はチップではなくて CoWoS や HBM の直列ボトルネックにあって、装置と材料まで遡らないと全体像が見えないですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

GPU が届くまでのチップ→装置→材料→原料の4層全体の構造と、直列ボトルネックの位置を示す地図です。

### 2. うれしさ

「なぜ AI チップの供給が増えにくいのか」を、個別企業の話でなく構造として掴めます。

### 3. 注意点

シェア・価格・逼迫度は時期で大きく動くため、この4層構造は安定していても数字は2026年6月時点のスナップショットです。

### 4. どこで役立つか

AI インフラの調達・投資判断・地政学リスクを考えるときに、視野を GPU 1社から4層全体へ広げる起点になります。

### 5. はじめに

「直列ボトルネック」と「各層に別々の独占企業が1社ずつ張り付く入れ子寡占」の2点を押さえれば芯は掴めます。

### 6. 深掘り先

CoWoS（J-96）、半導体製造装置（J-97）、電子材料（J-98）、重要鉱物の地政学（J-99）

## 開発フローでの位置（必須）

1. チップ層の把握 — GPU（NVIDIA）・HBM（SK Hynix 62%寡占）・製造（TSMC）の3社構造を掴む。HBM は2026年分完売・2027年まで逼迫（2026年6月時点）
2. 装置層の把握 — 各製造工程に1社ずつ独占・寡占企業が張り付く。EUV 露光は ASML 100%、ウェハ薄化は DISCO 世界独占、接合は ASMPT・BESI が首位
3. 材料層の把握 — 装置が動くための電子材料は日本企業に集中。ABF フィルム（味の素 95%）・EUV レジスト（日本3社で 90%超）・ウェハ（信越・SUMCO で過半）
4. 原料層の把握 — 材料の原料はさらに二分される。石化系（樹脂・溶剤）は日本の合成ノウハウ、元素系（ガリウム・ゲルマニウム等）は中国が精錬を握る
5. 直列ボトルネックの特定 — EUV → HBM → CoWoS の3か所が現在の直列ボトルネック。NVIDIA はその全層を先行予約で押さえている

## 関連用語

- HBM
- CoWoS
- ASML
- TSMC
- GPU

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 半導体は工程が複雑な分、サプライチェーンもかなり複層的になっている。どこが本当に技術力があって代替不可能なのか、逆にどこが代替可能なのかを見極めるのが難しい。
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: サプライチェーンの複層性が、LLM のアーキテクチャとどう結びついていくのかが難しくもあり面白い。
- 👍 良い点: どこに本当の技術力（代替不可能性）があるのかを見極める視点が持てる。
- 👎 ダメな点: 後工程が特にそうですが、非常に緻密で精密な連なりになっています。どこか一か所がダメージを受けると全体に影響が出るので、ダメというより脆いという感じです。
- 👥 誰向けか: かなりマニアックな内容。株好きな人が AI 銘柄を勉強する文脈で掘り下げそう。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 4層の縦積み図を中央に据える。最下層【原料】から上に向かって【材料】→【装置】→【チップ】と積み上げ、各層の枠内にキー企業名（国旗アイコン付き）を配置。層と層の間に上向き矢印を入れ「どの矢印が詰まっても上に届かない」を示す。右下隅に「直列ボトルネック」として EUV → HBM → CoWoS を赤系の点線ループで囲み強調する。
- 登場人物: AI エンジニア（著者の分身）が図の右横に立ち、4層図を見上げながら各層のつながりを指差している。
- 吹き出し・心の声: 「GPU が足りない理由を遡ったら、チップより下の層が全部つながっていた」
- 中央に置くキーワード/ラベル: 「チップ → 装置 → 材料 → 原料」「直列ボトルネック（EUV / HBM / CoWoS）」「各層に別々の独占企業」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（積み上げ層のミニ図を差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チップ（GPU ダイ）のシルエット ＋ HBM の積層イメージ
- Step 2 のアイコン/絵柄: 露光装置（ASML EUV）の外形シルエット ＋ ウェハ薄化の工程矢印
- Step 3 のアイコン/絵柄: 味の素 ABF フィルムのロール ＋ フォトレジストのボトル（素材感）
- Step 4 のアイコン/絵柄: 元素記号（Ga / Ge）と鉱山 / 精錬炉の概念アイコン
- Step 5 のアイコン/絵柄: 直列ボトルネック3か所を点線で繋いだ「どこか1か所が詰まる」ダイアグラム
- 矢印で示す流れの意図: 原料→材料→装置→チップという「下から積み上がる依存関係」と、どこか1か所が詰まると上流に影響が伝播する「直列の弱さ」を縦方向の矢印で表現する

## コミュニティ補完メモ

- J-96 CoWoS: GPU と HBM を1枚に統合する先端パッケージ技術の詳細。本エントリでは「直列ボトルネックの最終段」として位置づけ、詳細は J-96 に譲る
- J-97 半導体製造装置: ASML・DISCO・KLA ほか装置ベンダー各社のキー技術と市場独占の詳細。本エントリは「装置層全体」を俯瞰し、J-97 が各社を深掘りする
- J-98 電子材料: 味の素 ABF・旭化成 Pimel・EUV レジストなど日本企業が握る材料層の詳細。本エントリは材料層の「日本集中」という事実だけを指摘し、J-98 が仕組みと意味を掘り下げる
- J-99 重要鉱物の地政学: ガリウム・ゲルマニウム・希ガス等の元素系原料と中国の精錬支配・輸出規制の詳細。本エントリは「原料層に中国が集中」という位置づけだけを担う
- スコープ境界: 本エントリは4層構造の地図（俯瞰）に徹し、各層の内部構造・企業の詳細・数値の深掘りはすべて J-96〜J-99 に分担する

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Why is HBM so Hard to Manufacture (Vik's Newsletter) https://www.viksnewsletter.com/p/why-is-hbm-so-hard-to-manufacture — checked 2026-06-23（HBM 製造難易度・TSV 技術・SK Hynix 寡占構造の確認）
- ASML EUV Dominance (TrendForce) https://www.trendforce.com/insights/asml-euv — checked 2026-06-23（ASML EUV 100%独占の確認）
- DISCO Corporation World Leader (SemiAnalysis) https://semianalysis.com/2022/07/19/disco-corporation-the-world-leader/ — checked 2026-06-23（DISCO ウェハ薄化・世界独占の確認）
- Advanced Packaging: Nvidia Secures 60% of CoWoS (Astute Group) https://www.astutegroup.com/news/industrial/advanced-packaging-demand-soars-nvidia-secures-60-of-cowos-capacity/ — checked 2026-06-23（NVIDIA が CoWoS 能力の50-60%を単独予約している点の確認）
- CoWoS Not HBM Is the Real Bottleneck (Medium) https://medium.com/@Elongated_musk/cowos-not-hbm-is-the-real-ai-supply-bottleneck-d0ae8f3f7ce4 — checked 2026-06-23（直列ボトルネックが HBM から CoWoS へ移動しつつある指摘）
- Ajinomoto 95% ABF, 30% price hike (BigGo Finance) https://finance.biggo.com/news/ZU2KJZ4BpwxG186NIOsE — checked 2026-06-23（味の素 ABF の95%シェアと2026Q3価格引き上げの確認）
- Asahi Kasei Pimel PSPI for Advanced Packaging (Asahi Kasei) https://www.asahi-kasei.com/news/2026/e260521 — checked 2026-06-23（旭化成 Pimel の HBM/CoWoS RDL 絶縁への必須性の確認）
- Japanese Lock on Photolithography (Private Markets News) https://privatemarketsnews.substack.com/p/the-japanese-lock-on-photolithography — checked 2026-06-23（EUV フォトレジストにおける日本3社の90%超シェアの確認）
- Beyond Rare Earths: China's Gallium (CSIS) https://www.csis.org/analysis/beyond-rare-earths-chinas-growing-threat-gallium-supply-chains — checked 2026-06-23（ガリウム精錬の中国集中・輸出規制の武器化の確認）
- Hybrid Bonding: SK Hynix/Applied Materials/BESI (Counterpoint) https://counterpointresearch.com/en/insights/Hybrid-Bonding-Expands-from-Logic-to-Memory-SK-Hynix-Applied-Materials-BESI-Drive-Co-optimization-to-Scale-Next-gen-HBM — checked 2026-06-23（接合工程における ASMPT・BESI の首位確認）
- SK Hynix: The Memory Bottleneck (Longyield) https://longyield.substack.com/p/sk-hynix-the-memory-bottleneck-powering — checked 2026-06-23（HBM の2026年分完売・2027年逼迫予測の確認）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- シェア・価格・在庫逼迫度は時変情報。本文の「2026年6月時点」の明記と evaluation_date: 2026-06-23 を根拠とし、書籍化前に一次情報で再確認すること。
- 4層構造の枠組みは比較的安定しているが、ボトルネックの主役（HBM→CoWoS→次は何か）は動きうる。
- 素材の一次情報は ledgers/inference_hardware_landscape_2026.md の §9〜§14 にまとめてある。
- 本エントリは俯瞰（地図）に徹する。各層の数値・深掘りは J-96（CoWoS）・J-97（装置）・J-98（材料）・J-99（原料・地政学）に分担させること。
