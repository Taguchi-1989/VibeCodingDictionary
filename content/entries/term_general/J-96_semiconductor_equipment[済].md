---
id: J-96
title: 半導体製造装置
title_reading: ハンドウタイセイゾウソウチ
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 6
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-06-23
related_terms:
  - ASML
  - HBM
  - CoWoS
  - TSMC
  - 半導体サプライチェーン
status: ready
---

# 半導体製造装置

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

AI バブルの本当の受益者は「ツルハシを売る人」です。各工程を別々の企業が独占し、競合せず需要を分け合う「入れ子寡占」の構造を持ちます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

半導体製造装置とは、シリコンウェハ（半導体の素材）に回路を焼き付け、積み重ね、検査するための専用機械群です。GPU や HBM（High Bandwidth Memory、高帯域メモリ）を作るには、露光・薄化・接合・エッチング・成膜・検査という工程ごとに専用装置が必要で、どの工程も 1〜2 社しか作れません。AI ブームで GPU 需要が急増するほど、これらの装置メーカーへの発注も連動して増えます。結果として、AI 企業ではなく装置メーカーが安定した需要増の恩恵を受ける構造になっています。

## どこで出会うか

「なぜ AI チップは品薄になるのか」「NVIDIA はなぜ半導体を自社で作らないのか」「ASML（エイエスエムエル）とはどんな会社か」という問いを掘り下げたとき、この世界に入ります。HBM の寡占が崩れにくい理由を調べると、TSV（Through-Silicon Via、シリコン貫通電極）工程でのウェハ薄化（30μm 以下）や接合精度（10nm）の難しさが本質であり、それを可能にするのが DISCO（日本・ウェハ薄化・世界独占）や BESI（オランダ・ハイブリッドボンディング）などの装置メーカーだと分かります。株式投資の文脈でも「AI 関連銘柄としての装置メーカー」として KLA（過去 5 年 +571%）、Lam Research（同 +381%）、BESI（同 +332%）などが注目されています（2026 年 6 月時点のスナップショット、一次情報で要再確認）。

## メイン図

### 図の狙い

「AI チップが出来上がるまでの工程」を縦の流れで示し、各工程に独占企業が張り付く「入れ子寡占」の構造を一目で掴んでもらう。

### A. 工程ごとの独占企業（縦積み構造図）

- 工程 1: EUV 露光（極端紫外線リソグラフィ） — ASML（オランダ）100% 独占。世界でここしか作れない
- 工程 2: ウェハ薄化（30μm 以下に削る） — DISCO（日本）世界独占。ホコリ 1 粒で数千ドルの不良になる精密加工
- 工程 3: ハイブリッドボンディング（ダイの接合） — BESI（オランダ）/ ASMPT（シンガポール）が首位
- 工程 4: エッチング・成膜（TSV の穴あけ・銅埋め） — Lam Research（米）/ 東京エレクトロン / Applied Materials が寡占
- 工程 5: 検査・計測（歩留まり管理） — KLA（米）/ Lasertec（日）が寡占
- 各工程に「その会社のロゴ＋国旗」を小さく添え、「競合が別工程を担い競合せず需要を分け合う」矢印を横に引く

## 会話での使い方例

「AI 株で一番安定しているのは装置メーカーで、ASML と KLA は工程独占ですから需要が逃げないんですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

GPU・HBM を作る各工程に特化した専用機械を供給し、チップ量産を支える縁の下の力持ちです。

### 2. うれしさ

AI 需要が増えるほど装置需要も増え、かつ代替が効かないため安定した需要増が続きます。

### 3. 注意点

株価は時変情報で変動が大きく、2026 年 6 月のスナップショットは一次情報で随時再確認が必要です。

### 4. どこで役立つか

HBM 寡占の原因・AI チップの供給制約・装置銘柄の理解に直結します。

### 5. はじめに

ASML（EUV 独占）と DISCO（薄化独占）の 2 社を押さえると「なぜ誰も追いつけないか」の骨格が見えます。

### 6. 深掘り先

TSV、HBM、CoWoS、EUV リソグラフィ、半導体サプライチェーン

## 開発フローでの位置（必須）

1. 前工程（露光） — ASML の EUV 装置でシリコンウェハに回路パターンを焼き付ける。代替不可で世界 1 社
2. 前工程（エッチ・成膜） — Lam Research / 東京エレクトロン / AMAT が TSV の穴あけと銅埋めを担う
3. 後工程（薄化・切断） — DISCO がウェハを 30μm 以下に削り個片化。精度のズレが歩留まりを直撃する
4. 後工程（接合） — BESI / ASMPT がダイを 10nm 精度でハイブリッドボンディング。HBM の積層を実現する
5. 検査 — KLA / Lasertec が各工程の欠陥を計測し歩留まりを管理。ここが甘いと全工程の損失が出る

## 関連用語

- ASML
- HBM
- CoWoS
- TSMC
- 半導体サプライチェーン

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 半導体製造装置というと真っ先に出てくるのがオランダの露光装置メーカー ASML（EUV 露光装置）。超高価・超ニッチな技術で、台数の問題ではなく、サプライチェーン上のクリティカルパス（ここが止まると全体が止まる急所）になっている。
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 台数ではなく、代替の効かない急所（クリティカルパス）を握っているかどうかが強さの正体だと感じた。
- 👍 良い点: どの工程が独占されているかを見ると、サプライチェーンの脆さがどこにあるか読める。
- 👎 ダメな点: この分野で日本メーカーがなかなか存在感を出せなくなってしまったのが気になる。
- 👥 誰向けか: 半導体サプライチェーンや AI 銘柄をマニアックに追いたい人向け。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 縦一列の工程フロー図（露光 → エッチ/成膜 → 薄化/切断 → 接合 → 検査）。各工程ブロックの右側に独占企業名と国旗アイコンを配置。工程間を下向き矢印でつなぎ「どれか 1 つが詰まれば GPU が出ない」という直列構造を可視化する
- 登場人物: 投資家・エンジニア兼用の「調べている人」1 名（著者の分身）。図の左端に立ち、縦の工程ラインを指差しながら目を丸くしている
- 吹き出し・心の声: 「AI チップを作る各工程、全部別の会社が独占してる——競合しないで需要を分け合う構造なんだ」
- 中央に置くキーワード/ラベル: 「入れ子寡占」「各工程に 1〜2 社しかいない」「AI 需要 ∝ 装置需要」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（装置の歯車アイコンを差し色で演出）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: EUV 露光機の外観スケッチ（ASML ラベル付き）
- Step 2 のアイコン/絵柄: エッチング装置（穴あきウェハ断面）
- Step 3 のアイコン/絵柄: 薄いウェハの断面（30μm ラベル）
- Step 4 のアイコン/絵柄: 積層ダイの接合イメージ（HBM タワー）
- Step 5 のアイコン/絵柄: 検査装置のビーム照射と欠陥マーク

## 画像生成プロンプト

<!-- 自動下書き 2026-06-23 / 人の視点（使う人がどう感じるか）を主役に。白・黒・グレー・青系のみ。手書き風線画。 -->

### subject_stack
- entry_subject: 半導体製造装置（入れ子寡占）
- visual_subject: 工程ごとに独占企業が張り付く縦積みフロー図
- supporting_subjects: 調べている人（著者の分身）、工程ブロック×5段、国旗アイコン、「競合しない」横矢印
- logo_subject: none
- excluded_subjects: 実在ロゴマーク、カラフルなダッシュボード、グリーン/レッド/イエロー警告色

### scene brief（日本語）
縦一列に 5 段の工程ブロック（露光・エッチ/成膜・薄化・接合・検査）を並べ、各ブロック右に国旗アイコン＋企業名ラベルを添える。工程間は下向き矢印でつなぎ「直列ボトルネック」の構造を示す。画面左端に「調べている人」を立たせ、縦フローを指差しながら「競合しないで需要を分け合ってる」と吹き出しを出す。下方に「入れ子寡占」ラベルを大きめに配置。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration, 2:1 horizontal composition; monochrome plus blue palette only, white background. Five vertically stacked process blocks (EUV lithography → Etch/Deposit → Thinning → Bonding → Inspection) connected by downward arrows representing a serial bottleneck. Each block has a small flag icon and company-name label on the right side. A single character (researcher/author figure) stands to the left, pointing at the flow with a speech bubble saying the key idea about non-competing monopolies. Key label "入れ子寡占" placed prominently at the bottom. Flat, clean, consistent series style; no brand logos, no yellow/green/red/purple/orange, no colorful UI.

## コミュニティ補完メモ

- 半導体サプライチェーン全体（4 層入れ子の俯瞰・直列ボトルネック）: 本エントリは「装置層」だけを担う。チップ層（GPU/HBM）は別エントリ、材料層（味の素 ABF / EUV レジスト）・原料層（ガリウム等）はさらに別エントリに分担
- HBM（J 章）との住み分け: HBM は「何が高帯域メモリか・なぜ寡占か」の概念側。本エントリは「その HBM を作る装置群」の具体側。重なりは §9 の TSV 難易度部分のみ、本エントリでは製造難易度の入口として触れ、詳細は HBM エントリに譲る
- CoWoS との住み分け: CoWoS は GPU と HBM を 1 枚に統合する後工程パッケージング技術。本エントリの「接合」ステップがその上流工程に相当。CoWoS エントリでは ASMPT/BESI の接合装置を再参照する形で住み分ける
- ASML エントリとの住み分け: ASML は EUV 露光に特化した深掘りエントリ。本エントリは ASML を「工程の 1 例」として紹介するにとどめ、光学系・EUV 光源・レジストの詳細は ASML エントリに譲る

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Why is HBM so Hard to Manufacture (Vik's Newsletter) https://www.viksnewsletter.com/p/why-is-hbm-so-hard-to-manufacture — checked 2026-06-23（TSV 難易度・30μm 薄化・歩留まり・資本$15B 超・10 年累積ノウハウの根拠）
- DISCO Corporation World Leader (SemiAnalysis) https://semianalysis.com/2022/07/19/disco-corporation-the-world-leader/ — checked 2026-06-23（DISCO のウェハ薄化・切断工程の世界独占）
- Hybrid Bonding: SK Hynix/Applied Materials/BESI (Counterpoint) https://counterpointresearch.com/en/insights/Hybrid-Bonding-Expands-from-Logic-to-Memory-SK-Hynix-Applied-Materials-BESI-Drive-Co-optimization-to-Scale-Next-gen-HBM — checked 2026-06-23（ハイブリッドボンディング工程・BESI/ASMPT の役割）
- ASML EUV Dominance (TrendForce) https://www.trendforce.com/insights/asml-euv — checked 2026-06-23（ASML の EUV 100% 独占）
- Advanced Packaging: Nvidia Secures 60% of CoWoS (Astute Group) https://www.astutegroup.com/news/industrial/advanced-packaging-demand-soars-nvidia-secures-60-of-cowos-capacity/ — checked 2026-06-23（CoWoS ボトルネック・TSMC 増産計画）
- 装置各社の株価（KLA +571% / Lam +381% / BESI +332% 等）は 2026-06 時点スナップショット（ledgers/inference_hardware_landscape_2026.md §10 より転記）。エントリ化前に一次情報で再確認すること — checked 2026-06-23

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- **株価は時変情報**。`evaluation_date: 2026-06-23` を付けているが、数値は `ledgers/inference_hardware_landscape_2026.md §10` の検索ベーススナップショットであり、書籍化前に証券会社データ等の一次情報で必ず再確認すること。
- 工程の独占度・各社シェアも変化しうる（例: 中国 CXMT が 2026 年末に国産 HBM3 を狙うが先頭から 3〜4 年遅れ＋EUV 使えず歩留まり苦戦見込み）。出典付きで更新する。
- 本エントリは「装置層」のみを担う。チップ（GPU/HBM）・材料（ABF/EUV レジスト）・原料（ガリウム等）は別エントリ群に分担する（ledgers/inference_hardware_landscape_2026.md §14「エントリ化メモ」参照）。
- 競合関係の補足: ASML・DISCO・BESI・KLA 等は工程が別々のため直接競合しない。各社が異なるボトルネックを握り、どれか 1 社でも滞ると GPU の出荷が遅れる直列構造。「入れ子寡占」という表現はこの構造を指す。
