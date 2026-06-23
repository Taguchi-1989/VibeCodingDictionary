---
id: J-86
title: GQA
title_reading: ジーキューエー
category: term_general
subtype: ml_basic
experience_level: research_only
reader_level: 6
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-06-22
related_terms:
  - KV Cache
  - MLA
  - Attention
  - Transformer
  - GLM
status: drafting
---

# GQA

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Grouped-Query Attention の略。クエリヘッドをいくつかのグループに分け、グループごとに 1 組の Key・Value を共有することで、KV キャッシュのメモリを大きく削りつつ品質劣化を最小限に抑える注意機構です。MHA と MQA の「ほどよい中間」にあたる実務的な落としどころです。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Transformer（トランスフォーマー）の標準的な MHA（Multi-Head Attention、多頭注意）は、すべての Attention ヘッドがそれぞれ独自の Key（鍵）と Value（値）を持ちます。表現力は高いのですが、自己回帰生成のとき過去トークンの K・V を保存する KV キャッシュ（J-29）のメモリが「ヘッド数ぶん」まるごと必要になり、長文脈・大バッチでボトルネックになります。

正反対の極端が MQA（Multi-Query Attention、多クエリ注意）です。全ヘッドで K・V を「たった 1 組」だけ共有してしまうので、KV キャッシュは劇的に減りますが、共有が強すぎて品質が落ちやすいという弱点があります。

GQA（Grouped-Query Attention、グループ化クエリ注意）は、この両極の中間を取ります。クエリヘッドをいくつかのグループに束ね、グループごとに 1 組だけ K・V を共有します。たとえば 64 個のクエリヘッドを 8 グループに分ければ、K・V ヘッドは 8 組で済みます（MHA なら 64 組、MQA なら 1 組）。KV キャッシュは K・V ヘッド数に比例するので、64 組 → 8 組で約 8 分の 1 に削れます。それでいて「グループ数ぶん」の表現の自由度は残るため、MQA まで削ったときのような品質劣化を避けられる——これが「ほどよい共有」の落としどころです。

## どこで出会うか

普段の API 利用では見えません。出会うのは、Llama 2 / 3、Mistral、GLM-4.5 / GLM-5 系など主要 LLM のアーキテクチャ解説や技術レポートで「Attention は GQA を採用」と書かれている箇所、推論基盤（vLLM など）の設定で `num_key_value_heads` がクエリヘッド数より小さい値になっているのを見つけたとき、そして MHA / MQA / GQA / MLA を「KV キャッシュを削る手法の系譜」として並べて比較している技術記事です。

近年の主要なオープンモデルは、ほぼ標準で GQA を採用しています。「なぜ最近のモデルは長文脈をあの推論コストで回せるのか」を掘り下げると、まず最初に出てくる定番の工夫が GQA です。

## メイン図

### 図の狙い

KV を削る 3 段階——MHA（ヘッドごとにフルの K・V）/ GQA（グループで K・V を共有）/ MQA（全ヘッドで K・V を 1 組共有）——を横並びにし、「GQA はその中間で、メモリと品質のバランスを取る落としどころ」であることを、共有されていく K・V ヘッドの本数で一目で掴んでもらう。

### A. Before / After（K・V ヘッドの共有度）

- Before（MHA / MQA の両極）
  - 状況: MHA は K・V ヘッドをクエリと同数だけフルに持ち（メモリ最大・品質最良）、MQA は全クエリで K・V を 1 組だけ共有する（メモリ最小・品質劣化リスク大）
  - 視覚要素: 左に「8 Q ＝ 8 K・V」の MHA、右に「8 Q → 1 K・V」の MQA。両極を矢印の両端に置く
  - つまずき: MHA はメモリを食い、MQA は削りすぎて品質が落ちやすい。どちらも一長一短
- After（GQA）
  - 状況: クエリヘッドをグループに束ね、グループごとに 1 組の K・V を共有する（例: 8 Q を 2 グループにし K・V は 2 組）
  - 視覚要素: 8 本の Q が 2 グループに色分けされ、各グループが 1 組の K・V を共有する束ね線。中央に配置して両極の「間」を示す
  - うれしさ: KV キャッシュをグループ数ぶんに削りつつ、グループ単位の表現は残るので品質劣化が小さい。メモリと品質の妥協点

## 会話での使い方例

「GQA は Q ヘッドをグループ化して K・V を共有するので、MQA まで削らずに KV キャッシュを抑えて品質も保てるのが効いていますよね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

クエリヘッドをグループに束ね、グループごとに 1 組の K・V を共有して KV キャッシュを削る注意機構です。

### 2. うれしさ

KV ヘッドをグループ数まで間引いてメモリを大幅削減しつつ、MQA ほど削らないので品質劣化を最小に抑えられます。

### 3. 注意点

グループ数が共有の強さを決めるハイパーパラメータで、減らしすぎると MQA と同様に品質が落ちます。

### 4. どこで役立つか

長文脈・大バッチ推論で KV メモリが律速になる、Llama / Mistral / GLM 系のような主流モデルで広く効きます。

### 5. はじめに

「MHA（全ヘッド独自）と MQA（全ヘッド 1 組共有）の中間で、グループ単位に K・V を共有する」が掴めれば十分です。

### 6. 深掘り先

KV Cache、MHA / MQA、MLA、num_key_value_heads、Llama / GLM の技術レポート

## 開発フローでの位置（必須）

1. 動機の確認 — 長文脈・大バッチで KV キャッシュが GPU メモリを食い潰すボトルネックを把握する
2. 両極の整理 — MHA はメモリ最大で品質最良、MQA はメモリ最小だが品質劣化リスク大、という両極を押さえる
3. グループ設計 — クエリヘッドを何グループに束ねるか決める。グループ数 = K・V ヘッド数が共有の強さを支配する
4. 学習・変換 — 既存の MHA チェックポイントから、K・V ヘッドを平均して束ねる uptraining で GQA モデルへ安く変換する
5. 評価と採用 — KV メモリ削減量と品質を MHA / MQA と比較し、バランス点を選んで本番モデルに採用する

## 関連用語

- KV Cache
- MLA
- Attention
- Transformer
- GLM


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- MHA / GQA / MQA の三文字略称が最初は分かりにくかった。
- Multi と Attention（M・A）が共通と分かると、残りの G（Grouped）や Q（Query）が何を意味するか予測できるようになり、覚えやすくなった。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 三文字略称がずらっと並んでいてとっつきにくかった。
- 👍 良い点: KV キャッシュが課題というところに対して、ヘッド共有でちゃんとアプローチしているのが分かる。
- 👎 ダメな点: バニラ（MHA）からどんどん複雑になっていくので、パッと全体像が掴めない。
- 👥 誰向けか: 技術の進化の流れを理解したい人向け。「なぜ進歩したか」を答えられると手の内に技術がある感じがする。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 横並び 3 段の比較。左に MHA（8 本の Q ヘッドそれぞれに専用の K・V が 1 本ずつ＝計 8 組、KV キャッシュが一番太い）、右に MQA（8 本の Q がすべて 1 組の K・V を共有＝計 1 組、キャッシュは一番細いが「共有が強すぎて品質↓」の注記）、中央に GQA（8 本の Q を 2 グループに色分けし、各グループが 1 組ずつ K・V を共有＝計 2 組）。下に「KV キャッシュに保存する K・V ヘッド数」を高さで示すバーを 3 本並べ、MHA=8、GQA=2、MQA=1 と段階的に減るのを見せる。GQA のバーに「メモリ↓・品質ほぼ維持」の吹き出し。
- 登場人物（いれば）: 推論基盤のメモリ図を覗き込むエンジニア 1 名（著者の分身）。中央 GQA の「グループで K・V を共有」する束ね線を指差している。
- 吹き出し・心の声: 「全部独自（MHA）だと重い、全部 1 組（MQA）だと品質が落ちる。グループで共有する“ほどよい間”を取るのが GQA——だからメモリは軽いのに表現は粗くならない」
- 中央に置くキーワード/ラベル: 「MHA（独自）→ GQA（グループ共有）→ MQA（全共有）」「KV ヘッド数 = グループ数 ∝ キャッシュ量」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（① 8 本 → 2 組に束ねる「グループ化」の括り矢印、③ グループ数を増減させるスライダー＝共有の強さ調整、だけ差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: KV キャッシュで膨らむメモリゲージ（ボトルネックの提示）
- Step 2 のアイコン/絵柄: 左に MHA（メモリ大）、右に MQA（品質↓）の両極を天秤の両端に置く図
- Step 3 のアイコン/絵柄: 8 本の Q ヘッドを 2 グループに色分けして束ねる括り（グループ設計）
- Step 4 のアイコン/絵柄: MHA の K・V ヘッドを平均して束ね GQA へ変換する uptraining の集約矢印
- Step 5 のアイコン/絵柄: MHA / GQA / MQA の 3 本を「メモリ」と「品質」の 2 軸でプロットし GQA のバランス点を丸で囲む
- 矢印で示す流れの意図: ボトルネック → 両極の限界 → グループ設計 → 安い変換 → バランス評価、という「なぜ GQA が要るか・どう中間点を選ぶか」の縦の流れ


## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: GQA
- visual_subject: MHA（8組独立）・GQA（2グループ共有）・MQA（1組共有）を横3列に並べ KV ヘッド本数が段階的に減るバー比較
- supporting_subjects: 推論基盤のメモリ図を覗き込みGQAの束ね線を指差すエンジニア、KV ヘッド数を高さで示す3本のバー、クエリヘッドからKVへの束ね矢印
- logo_subject: none
- excluded_subjects: カラフルなニューラルネットワーク図・実在UIスクリーンショット・他社ロゴ・緑/赤/黄の警告色・虹色のAttentionヒートマップ

### scene brief（日本語）
横並び3列の比較図を中心に据える。左列「MHA」は8本のQヘッドそれぞれに独立したKVが1本ずつ伸び、下に高いバー（KVキャッシュ量が最大）。右列「MQA」は8本のQが1本のKVへ一斉に集まり、下に一番低いバーと小さく「品質↓」の注記。中央列「GQA」は8本のQが2グループ（色分けした括り線）にまとまり各グループから1本のKVが伸びる、下に中程度のバーに「メモリ↓・品質ほぼ維持」の吹き出し。画面右端にエンジニア（著者の分身）がGQAの束ね線を指差し、心の声「全部独自だと重い、全部1組だと品質が落ちる——グループで共有する"ほどよい間"がGQA」を添える。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration, 2:1 horizontal composition (1254x627); monochrome plus blue palette only (#1A1A1A linework, neutral grays #6B7280, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background. Three-column comparison: left column "MHA" shows 8 query lines each connecting to its own separate KV pair, plus a tall bar below indicating large KV cache; right column "MQA" shows 8 query lines all converging to one shared KV pair, plus a very short bar and a small note "quality ↓"; center column "GQA" shows 8 query lines grouped into two color-coded brackets each sharing one KV pair, plus a medium-height bar with callout "memory ↓ / quality ≈ preserved". A single male engineer stands at the right, pointing at the GQA grouping brackets, with a thought bubble conveying the "just right middle ground" insight. Flat, clean, consistent series style; minimal text, only the three column labels and two callout tags; no yellow, green, red, purple, orange, rainbow, colorful attention heatmaps, or brand marks.

## コミュニティ補完メモ

- 同じ Lv6 シェルフの近接語との住み分け:
  - KV Cache（J-29）: 「何を・なぜキャッシュするか」と「それがボトルネックになる理由」を担う上位概念。GQA はその「構造的削減」ステップの代表的な一手段（ヘッド共有）を深掘りする位置。
  - MLA（J-28）: 同じく KV を削るが、アプローチが異なる。GQA は「K・V ヘッドの本数を減らして共有する」、MLA は「ヘッド本数は保ったまま中身を低ランクに圧縮する」。MHA → GQA → MQA が「本数を削る系譜」、MLA はそこから分岐した「次元を畳む系譜」と整理する。
  - Attention（J-17）: Q/K/V と多頭注意の基礎。GQA は Attention の K・V ヘッドの「持ち方」を変える派生なので J-17 が前提。
  - Transformer（J-13）: GQA が載る土台のアーキテクチャ。
  - GLM（D-45）: GQA を採用する代表モデル群。GLM-4.5 / GLM-5 系、GLM-5.2 も GQA を採用している。「どのモデルが採用したか」は D-45 側、「GQA という仕組みそのもの」は本エントリ。
- KV を削る手法の系譜（本シェルフ内の地図）: MHA（独自・重い）→ GQA（グループ共有・主流）→ MQA（全共有・軽いが品質↓）が「本数を削る」一直線。MLA（J-28）は「本数ではなく次元を低ランクに畳む」別軸の分岐。
- スコープ境界: 本エントリは「GQA とは何か・MHA/MQA との位置関係・なぜ品質を保てるか・どう安く変換するか」までを担う。具体の uptraining 手順や各モデルの採用詳細は出典・各モデルエントリに譲る。


## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints" (2023) https://arxiv.org/abs/2305.13245 — checked 2026-06-22（GQA の原論文。MHA/MQA の中間としてのグループ共有の定義、既存 MHA チェックポイントからの uptraining、品質とメモリのトレードオフ）
- Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need" (MQA, 2019) https://arxiv.org/abs/1911.02150 — checked 2026-06-22（GQA の片極にあたる MQA の一次出典。全ヘッドで K・V を 1 組共有する起点）
- Touvron et al., "Llama 2: Open Foundation and Fine-Tuned Chat Models" (2023) https://arxiv.org/abs/2307.09288 — checked 2026-06-22（GQA を主要オープンモデルが標準採用した代表例。大規模実モデルでの効果報告）


## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- 「ほどよい共有」の直観: K・V は表現の冗長性が高く、全ヘッドで完全に独自である必要は薄い。一方で MQA のように 1 組まで削ると、異なる Q ヘッドが見るべき「鍵の射影」の多様性まで失われ品質が落ちる。GQA はグループ数というつまみで「どこまで共有を許すか」を連続的に選べるのが本質。グループ数 = 1 が MQA、グループ数 = ヘッド数が MHA で、GQA は両者を内包する一般化と整理できる。
- KV キャッシュ削減率: キャッシュ量は K・V ヘッド数（= グループ数）に比例する。クエリヘッド 64・グループ 8 なら 64 → 8 で約 1/8。Llama 2 70B はクエリヘッド 64・KV ヘッド 8（8 グループ）の構成が知られる。
- GLM-5.2 への言及: GLM-5 系（GLM-5.2 含む）も Attention に GQA を採用している。最新の採用状況は各モデルの技術レポートで確認すること（時変情報のため evaluation_date 基準）。
