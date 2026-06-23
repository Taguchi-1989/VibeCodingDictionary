---
id: J-28
title: MLA
title_reading: エムエルエー
category: term_general
subtype: ml_basic
experience_level: research_only
reader_level: 6
importance: E
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-06-22
related_terms:
  - KV Cache
  - Attention
  - RoPE
  - DeepSeek V3
  - Transformer
status: drafting
---

# MLA

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Multi-Head Latent Attention の略。Key と Value を低ランクの潜在ベクトルに圧縮してキャッシュし、使うとき各ヘッドへ復元することで、KV キャッシュのメモリを大きく削りつつ品質劣化を抑える注意機構です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

長文脈・大バッチ推論では、過去トークンの Key（鍵）と Value（値）を保存する KV キャッシュ（J-29）が GPU メモリの最大のボトルネックになります。先行する MQA（Multi-Query Attention）/ GQA（Grouped-Query Attention）は「K・V ヘッドの本数を減らして共有する」ことでキャッシュを削りますが、表現の自由度を捨てるぶん品質が落ちがちでした。

MLA（Multi-Head Latent Attention、多頭潜在注意）は、DeepSeek-V2 / V3 が導入した手法です。各トークンの K・V を、ヘッドごとにそのまま持つのではなく、まず低次元の「潜在ベクトル」1 本に圧縮（ダウンプロジェクション）してキャッシュします。Attention を計算するときに、その潜在ベクトルから各ヘッドの K・V を線形変換で復元（アッププロジェクション）します。

つまり「ヘッドの本数を減らす（MQA/GQA）」のではなく「ヘッドはフル本数のまま、保存する中身を低ランクに畳む」発想です。キャッシュするのは潜在ベクトル（と後述の RoPE 用の小さな成分）だけなので、KV キャッシュ量を GQA より大きく削りつつ、復元後はヘッドごとの表現を取り戻せるため品質劣化を抑えられる——これが MLA の位置づけです。

## どこで出会うか

普段の API 利用では一切見えません。出会うのは、DeepSeek-V2 / V3 / R1 系の技術レポートやアーキテクチャ解説、「なぜ DeepSeek は長文脈をあの推論コストで回せるのか」を掘り下げた記事、推論基盤（vLLM など）が MLA 対応を入れたというリリースノート、そして MQA / GQA / MLA を「KV キャッシュを削る手法の系譜」として並べて比較する技術記事です。

「KV キャッシュが重い → ヘッドを共有して削る（MQA/GQA）か、潜在表現に圧縮して削る（MLA）か」という設計判断を追いかけ始めたときに、必ず名前が出てくる用語です。

## メイン図

### 図の狙い

KV を削る 3 手法——MHA（素朴な多頭注意）/ GQA（ヘッド共有）/ MLA（低ランク圧縮）——を横並びにし、「MQA/GQA は本数を減らす」「MLA は本数を保ったまま中身を畳む」という削り方の違いと、それが品質とメモリのトレードオフにどう効くかを一目で掴んでもらう。

### A. Before / After（何をキャッシュするかの違い）

- Before（GQA まで）
  - 状況: K・V ヘッドの本数そのものを減らして複数の Q ヘッドで共有する
  - 視覚要素: 8 本の Q ヘッドに対し、K・V は 2 本に束ねられている（本数を間引く絵）
  - つまずき: 削るほどメモリは減るが、共有された K・V は表現が粗くなり品質が落ちやすい
- After（MLA）
  - 状況: K・V はフル本数ぶん必要だが、キャッシュには低次元の潜在ベクトル 1 本だけを保存し、計算時に各ヘッドへ復元する
  - 視覚要素: 太い K・V の束が細い潜在ベクトル 1 本に絞られ（圧縮）、使うときに再び 8 本へ展開される（復元）矢印
  - うれしさ: 保存量は GQA より小さくできるのに、復元後はヘッドごとの表現を取り戻せるので品質劣化が小さい

## 会話での使い方例

「DeepSeek の MLA は KV を潜在ベクトルに圧縮して持つので、GQA よりメモリを削りつつ品質も保てるのが効いていますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

K・V を低ランクの潜在ベクトルに圧縮してキャッシュし、計算時に各ヘッドへ復元する注意機構です。

### 2. うれしさ

KV キャッシュを GQA より大きく削りつつ、ヘッドを間引かないので品質劣化を抑えられます。

### 3. 注意点

復元の行列演算が増え、RoPE（回転位置埋め込み）との両立に専用の設計が要ります。

### 4. どこで役立つか

長文脈・大バッチで KV メモリが律速になる、DeepSeek 系のような大規模モデルの推論で効きます。

### 5. はじめに

「本数を減らす GQA」対「中身を低ランクに畳む MLA」の対比が掴めれば入口は十分です。

### 6. 深掘り先

KV Cache、MQA / GQA、低ランク分解、RoPE、DeepSeek-V2/V3 技術レポート

## 開発フローでの位置（必須）

1. 動機の確認 — 長文脈・大バッチで KV キャッシュが GPU メモリを食い潰すボトルネックを把握する
2. 先行手法の限界 — MQA/GQA は K・V ヘッドを減らして削るが、品質劣化と引き換えになる点を押さえる
3. 圧縮（ダウンプロジェクション） — 各トークンの K・V を低次元の潜在ベクトル 1 本に畳み、それだけをキャッシュする
4. 復元（アッププロジェクション） — Attention 計算時に潜在ベクトルから各ヘッドの K・V を線形変換で復元する
5. RoPE 両立と評価 — 回転位置成分を分離して持つ工夫を入れ、メモリ削減量と品質を GQA と比較評価する

## 関連用語

- KV Cache
- Attention
- RoPE
- DeepSeek V3
- Transformer

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- GQA の "G"（Grouped）の意味がすぐに出てこない。「グループで共有する」イメージが定着しにくい。
- MLA の「低ランク圧縮」と GQA の「ヘッド共有」の違い——「まとめる」vs「圧縮する」がどう違うのかが曖昧だった。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: DeepSeek など最先端が採用しているという事実から「今のトップはここまで来ているのか」という感じ。
- 👍 良い点: 「本数を減らす（GQA）vs 折りたたんで小さくする（MLA）」の例えで整理できた。
- 👎 ダメな点: 低ランク圧縮の数理（なぜ圧縮しても情報が保てるのか）まではまだ曖昧。
- 👥 誰向けか: GQA を理解した上で「もう一段深い削減」を知りたい人。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 横並び 3 段の比較。左に MHA（Q・K・V がそれぞれ 8 本フルにあり、KV キャッシュが一番太い）、中央に GQA（Q 8 本に対し K・V を 2 本へ束ね、本数を間引いてキャッシュを細くする）、右に MLA（K・V はフル 8 本ぶん使うが、キャッシュには細い潜在ベクトル 1 本だけ＝太い束 → 細い 1 本 → 計算時に再び 8 本へ展開、という「畳んで→展開」矢印）。下に「キャッシュに保存する量」を高さで示すバーを 3 本並べ、MLA が最も低いことを示す。
- 登場人物（いれば）: 推論基盤のメモリ図を覗き込むエンジニア 1 名（著者の分身）。MLA の「太い束 → 細い 1 本」の圧縮矢印を指差している。
- 吹き出し・心の声: 「ヘッドは減らさない。保存する中身を低ランクに畳んで、使うとき展開し直す——だからメモリは軽いのに表現は粗くならない」
- 中央に置くキーワード/ラベル: 「本数を減らす（GQA）vs 中身を畳む（MLA）」「圧縮（down）→ キャッシュ → 復元（up）」
- Before / After の場合の対比ポイント: GQA は「K・V の本数」を間引く（横方向に細る）。MLA は「保存する次元」を低ランクに畳む（保存量だけ縮み、ヘッド本数は保つ）。削る軸が違うことを矢印の向きで対比。

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① 圧縮 → 展開の二段矢印、③ RoPE 成分を別に持つ「分離」マークだけ差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: KV キャッシュで膨らむメモリゲージ（ボトルネックの提示）
- Step 2 のアイコン/絵柄: 8 本 → 2 本に間引かれる K・V ヘッド（GQA）に「品質↓」の注記
- Step 3 のアイコン/絵柄: 太い K・V 束が細い潜在ベクトル 1 本に絞られる漏斗（ダウンプロジェクション）
- Step 4 のアイコン/絵柄: 潜在ベクトルから 8 本の K・V が再展開される逆漏斗（アッププロジェクション）
- Step 5 のアイコン/絵柄: 位置回転（RoPE）成分を別レーンで持つ分岐＋メモリと品質の天秤
- 矢印で示す流れの意図: ボトルネック → 先行手法の限界 → 圧縮 → 復元 → RoPE 両立、という「なぜ MLA が要るか・どう実現するか」の縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: MLA（Multi-Head Latent Attention）
- visual_subject: K・V の太い束が細い潜在ベクトル1本に圧縮され、計算時に再び各ヘッドへ展開される「圧縮→キャッシュ→復元」の流れ
- supporting_subjects: MHA・GQA・MLAの3手法のキャッシュ量比較バー、ダウンプロジェクション漏斗、アッププロジェクション逆漏斗
- logo_subject: none
- excluded_subjects: カラフルなグラフ、絵文字、実在サービスのUI、赤・緑・黄の差し色

### scene brief（日本語）
推論基盤のメモリ図を覗き込むエンジニア1名（著者の分身）が、MLA の圧縮矢印を指差している場面。画面左から右へ、太いK・V束が漏斗状に細い潜在ベクトル1本に絞られ（ダウンプロジェクション）、キャッシュに格納された後、逆漏斗で再び8本のヘッドへ展開される（アッププロジェクション）流れを大きく描く。下部には MHA・GQA・MLA のキャッシュ量を高さで示す3本バーを並べ、MLA が最も低いことを示す。エンジニアの吹き出し：「ヘッドは減らさない。保存する中身を低ランクに畳んで、使うとき展開し直す——だからメモリは軽いのに表現は粗くならない」。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, flat light gray fills, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background. A single engineer character (author avatar, male, standing) pointing at a compression funnel in the center of the diagram, with a speech bubble: "Store the latent, expand on demand." Main diagram: a wide bundle of K/V arrows on the left narrows through a funnel (down-projection) into a single slim latent vector stored as a cache cylinder, then expands back through an inverted funnel (up-projection) into 8 separate K/V head arrows on the right. Below the main flow, three vertical bars labeled MHA, GQA, MLA show decreasing KV cache height left to right, with MLA bar shortest and highlighted in #8DB7E8. Small labels: "compress (down)" above the funnel, "restore (up)" above the inverted funnel. No n×n grids, no colorful charts, no brand logos, no yellow/green/red/purple. Flat, clean, consistent series style; minimal text, only key labels. 2:1 horizontal composition.

## コミュニティ補完メモ

- 同じ Lv6 シェルフの近接語との住み分け:
  - KV Cache（J-29）: 「何を・なぜキャッシュするか」と「それがボトルネックになる理由」を担う上位概念。MLA はその「構造的削減」ステップの一手段を深掘りする位置。
  - Attention（J-17）: Q/K/V と多頭注意の基礎。MLA は Attention の K・V の「持ち方」を変える派生なので、J-17 が前提。
  - RoPE（J-27）: 位置情報を K・Q の回転で入れる手法。MLA の圧縮表現と回転位置の相性が問題になり、DeepSeek は位置成分を分離して持つ「decoupled RoPE」を採用した。両立の工夫の詳細は J-27 と本エントリで分担。
  - DeepSeek V3（D-46）: MLA を実装・スケールさせた代表モデル。MLA を「どのモデルが・なぜ採用したか」は D-46 側、「MLA という仕組みそのもの」は本エントリ。
  - MQA/GQA: KV を削る系譜の前段（本数を減らす手法）。本書では独立エントリを立てず、本エントリと J-29 内で対比して扱う。
- スコープ境界: 本エントリは「MLA とは何か・MQA/GQA との削り方の違い・なぜ低ランクで効くか・RoPE 両立に工夫が要る点」までを担う。具体の行列分解の式変形や DeepSeek の実装詳細は出典の技術レポートに譲る。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- DeepSeek-AI, "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model" (2024) https://arxiv.org/abs/2405.04434 — checked 2026-06-22（MLA の初出。低ランク KV 圧縮と decoupled RoPE の定義、GQA/MQA との比較）
- DeepSeek-AI, "DeepSeek-V3 Technical Report" (2024) https://arxiv.org/abs/2412.19437 — checked 2026-06-22（MLA を大規模にスケールさせた実装。KV キャッシュ削減量と品質の報告）
- Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints" (2023) https://arxiv.org/abs/2305.13245 — checked 2026-06-22（MLA が比較対象とする GQA の一次出典。ヘッド共有によるKV削減の系譜）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- 「低ランクで効く」直観: K・V 行列はヘッド間・次元間に冗長性が高く、特異値の大半が小さい（実効ランクが低い）ことが多い。だから少数の潜在次元で大半の情報を保てる、というのが圧縮の根拠。MQA/GQA の「ヘッド共有」も低ランク近似の特殊形と見なせるが、MLA はランクの取り方をより柔軟にした一般化と整理できる。
- RoPE 両立の論点: 素朴に K を潜在ベクトルへ畳むと、位置依存の回転（RoPE）を後段でかけ直せず吸収できない。DeepSeek は K を「圧縮してキャッシュする内容成分」と「位置回転をかける小さな専用成分（decoupled RoPE）」に分け、後者だけ別に持つことで両立させた。誌面では深入りせず「分離して持つ工夫が要る」に留める。
