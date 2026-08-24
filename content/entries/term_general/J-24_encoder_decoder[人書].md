---
id: J-24
title: Encoder-Decoder
title_reading: エンコーダーデコーダー
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
  - Transformer
  - Attention
  - LLM
  - Whisper
  - VLM
status: needs_review
---

# Encoder-Decoder

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Encoder（符号化器）と Decoder（復号化器）の 2 部構成。入力系列を意味表現に畳み込む前半と、それを参照しながら出力系列を 1 トークンずつ生む後半に役割を分けた、系列変換（seq2seq）の古典的かつ原典 Transformer の骨格です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

「ある系列を別の系列に変換する」タスク——機械翻訳・要約・音声認識など——を、2 つの異なる役割の塔に分けて解きます。Encoder は入力（たとえば英文）を最初から最後まで双方向に読み込み、各トークンを「文全体の文脈を織り込んだ意味ベクトル」の列に変換します。ここでは未来のトークンも見てよい（masking なしの self-attention）ので、各単語を前後両方の文脈から理解できます。

Decoder は出力（たとえば訳した日本語）を 1 トークンずつ自己回帰的に生成します。このとき 2 種類の Attention（注意機構）を使うのが要点です。1 つは出力側の自己注意（causal self-attention、未来を見ないよう masking する）、もう 1 つが cross-attention（交差注意）で、Decoder の各位置が Encoder の出力した意味ベクトル列を「参照先」として引きます。Query は Decoder 側、Key・Value は Encoder 側から来る——これが「入力をどこに注目して訳すか」を担い、原典 Transformer が RNN を置き換えて成立した心臓部です。

## どこで出会うか

API を叩く側からは普段見えませんが、「入力と出力で性質が違う変換タスク」のモデルカードや論文を読むと必ず出てきます。代表は機械翻訳、T5（Text-to-Text Transfer Transformer、あらゆるタスクを系列変換に統一）、BART、そして音声認識の Whisper（D-71、音声特徴量を Encoder、テキストを Decoder で生成）。マルチモーダルでも「画像を Encoder、説明文を Decoder」という分業はこの構造の延長です。

逆に、いま話題の大規模 LLM（GPT 系・Claude 系）の多くは Decoder-only で、ここで Encoder-Decoder と対比されます。「なぜ Encoder を捨てたのか」「翻訳は Encoder-Decoder なのにチャットは Decoder-only なのはなぜか」という問いに踏み込むとき、この用語を起点に整理することになります。

## メイン図

### 図の狙い

左に Encoder の塔（双方向 self-attention で入力全体を意味表現に圧縮）、右に Decoder の塔（causal self-attention ＋ Encoder を引く cross-attention で出力を逐次生成）を並べ、両者をつなぐ cross-attention の矢印（Q は Decoder・K/V は Encoder）を太く描く。「入力を読む係」と「出力を書きながら入力を見に行く係」の分業を一目で掴んでもらう。

### 役割分担の構造図

- 左の塔: Encoder
  - 入力系列を全トークン一括で受け取り、masking なしの双方向 self-attention を N 層
  - 出力は「文脈を織り込んだ意味ベクトルの列」（固定の 1 ベクトルではなく系列のまま渡す点が RNN 時代との違い）
- 右の塔: Decoder
  - 下段: causal self-attention（生成済みの出力だけを見る、未来は masking）
  - 中段: cross-attention（Q=Decoder の状態、K・V=Encoder の出力）= ここで入力のどこに注目するか
  - 上段: 次トークンの確率分布を出し、1 個サンプリングしてまた下段へ戻る自己回帰ループ
- 対比の補助: 右下に小さく Decoder-only（Encoder の塔を消し、入力も出力も 1 本の系列として causal self-attention だけで処理）を併記

## 会話での使い方例

「翻訳や Whisper が Encoder-Decoder なのは入力と出力で見方を変えたいからで、cross-attention が入力の参照を担うのが効いていますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

入力を読む Encoder と出力を生む Decoder に分け、cross-attention で両者を橋渡しする系列変換の骨格です。

### 2. うれしさ

入力は双方向に深く理解し、出力は自己回帰で素直に生成できるので、翻訳・要約・音声認識のような変換タスクに自然に収まります。

### 3. 注意点

2 塔ぶんパラメータと実装が重く、入出力の性質が同じタスクでは Decoder-only より無駄が出やすい点に注意です。

### 4. どこで役立つか

機械翻訳・要約・音声認識（Whisper）・T5 系など、入力と出力で「読み方」を変えたい seq2seq で効きます。

### 5. はじめに

「Encoder は双方向で読む、Decoder は未来を隠して書く、つなぎ目が cross-attention（Q は Decoder・K/V は Encoder）」が掴めれば十分です。

### 6. 深掘り先

Decoder-only との比較、cross-attention の仕組み、T5、BART、Whisper の音声 Encoder

## 開発フローでの位置（必須）

1. 入力エンコード — 入力系列を Encoder に一括投入し、双方向 self-attention で各トークンを文脈つき意味ベクトルに変換する（並列計算できるので高速）
2. 意味表現の受け渡し — Encoder 出力（系列のままの K・V 素材）を Decoder の cross-attention 層に橋渡しする。ここが 2 塔をつなぐ接点
3. 自己回帰デコード — Decoder が causal self-attention で生成済み出力を見つつ、cross-attention で入力を参照し、次の 1 トークンを予測する
4. 逐次ループ — 出した 1 トークンを入力末尾に足してまた Decoder を回す。終端トークンが出るまで繰り返す（KV Cache が効く場面）
5. 構造の選択 — 入出力で読み方を変えたいなら Encoder-Decoder、汎用チャット・事前学習のスケールを優先するなら Decoder-only、と設計時に分岐する

## 関連用語

- Transformer
- Attention
- LLM
- Whisper
- VLM

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Encoder-Decoder → Decoder-only の流れは、ディープラーニング黎明期（画像認識ブレイクスルー）からの地続きとして理解している。
- self-attention と cross-attention の2種類があること自体がまだ曖昧。言葉では何となく掴めてきたが、絵で見た方が確実に腹落ちする感じ。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 歴史の流れ（画像認識 → DL → Transformer → Decoder-only）として捉えると大きな絵が掴めた。
- 👍 良い点: 「読む係と書く係を分けた」という役割の整理は分かりやすい。
- 👎 ダメな点: cross-attention と self-attention の違いは図なしには頭に定着しない。ポンチ絵が必須。
- 👥 誰向けか: LLM の歴史的な変遷（なぜ今 Decoder-only が主流なのか）を理解したい人に良い。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央で向き合う 2 つの塔。左 = Encoder（入力「I love AI」を 3 トークンまとめて受け取り、双方向の両向き矢印で self-attention を回し、上に意味ベクトルの列を吐く）。右 = Decoder（下から「私 は AI が」と生成済みトークンが積み上がり、causal self-attention は未来を斜線でマスク、その上に Encoder の意味ベクトル列へ伸びる太い cross-attention 矢印、最上段で次トークン「好き」の確率分布）。2 塔の間を結ぶ cross-attention の太矢印に「Q=Decoder / K・V=Encoder」のラベル。右下隅に小さく Decoder-only 版（塔が 1 本だけ）を点線枠で対比。
- 登場人物（いれば）: 翻訳の現場を覗き込むエンジニア 1 名（著者の分身）。左の塔を指して「こっちは全文を一気に読む係」、右の塔を指して「こっちは書きながら左を見に行く係」と分担を確認している。
- 吹き出し・心の声: 「読む係と書く係を分けた。書く側が cross-attention で読む側を参照する——だから入力と出力で読み方を変えられる」
- 中央に置くキーワード/ラベル: 「Encoder=双方向に読む / Decoder=未来を隠して書く」「橋渡し = cross-attention（Q:Decoder, K/V:Encoder）」
- 比較（Decoder-only）の対比ポイント: 2 塔 vs 1 塔。入力と出力を別扱い vs 1 本の系列に連結。翻訳・音声認識向き vs 汎用チャット・事前学習スケール向き。

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① 2 つの塔と橋アイコン、⑤ cross-attention の矢印だけ差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 入力全文を一括で炉に通す Encoder のバッチ矢印（双方向）
- Step 2 のアイコン/絵柄: Encoder の出力ベクトル列が Decoder へ渡る橋（受け渡し）
- Step 3 のアイコン/絵柄: Decoder が cross-attention で左の塔を参照しつつ 1 トークン予測
- Step 4 のアイコン/絵柄: 出力トークンを足して回す自己回帰ループ矢印
- Step 5 のアイコン/絵柄: 分岐の道標（左 = Encoder-Decoder / 右 = Decoder-only）
- 矢印で示す流れの意図: 入力を読む → 橋で渡す → 参照して書く → ループ → 構造を選ぶ、という「2 塔がどう連携し、なぜ Decoder-only と分かれるか」の縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: Encoder-Decoder
- visual_subject: 入力を読む Encoder 塔と出力を書く Decoder 塔が cross-attention の矢印でつながる 2 塔の分業構造
- supporting_subjects: cross-attention の Q/K/V ラベル、Decoder-only の対比（点線枠の 1 塔）、次トークン生成の自己回帰ループ
- logo_subject: none
- excluded_subjects: カラフルな注意マップ、ヒートマップ、実際のUIスクリーンショット、虹色グラフ、絵文字

### scene brief（日本語）
左の Encoder 塔（入力トークンを双方向に読む両向き矢印）と右の Decoder 塔（causal self-attention の斜線マスク＋上段の cross-attention 矢印）を中央で対比して描く。2 塔をつなぐ太い cross-attention 矢印に「Q=Decoder / K・V=Encoder」のラベルを添える。右下隅には点線枠の Decoder-only 1 塔を小さく並べ、2 塔 vs 1 塔の対比を示す。著者の分身エンジニア（左の塔を指さしながら）が吹き出しで「読む係と書く係を分けた。書く側が cross-attention で読む側を参照する」と語る。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background; a single engineer character (author's alter ego) pointing at the left tower with a speech bubble reading "reading side vs writing side"; two vertical towers center stage — left tower labeled Encoder with bidirectional self-attention arrows (no masking), right tower labeled Decoder with a diagonal-masked causal self-attention block below and a thick cross-attention arrow pointing leftward to the Encoder labeled "Q=Decoder / K·V=Encoder" in deep navy; small dotted-border single-tower diagram in lower-right corner labeled Decoder-only for contrast; flat, clean, consistent series style; minimal text, only the key labels "Encoder=双方向に読む", "Decoder=未来を隠して書く", "cross-attention"; 2:1 horizontal composition. No yellow, green, red, purple, orange, rainbow colors, colorful UI, or brand colors.

## コミュニティ補完メモ

- 同じ Lv6 シェルフ・近接エントリとの住み分け:
  - Transformer（J-13）: 原典 Transformer はこの Encoder-Decoder 構成だった。J-13 は「Transformer とは何か（Attention で RNN を置き換えた）」を担い、本エントリは「その 2 部構成の役割分担と Decoder-only への分岐」を深掘りする位置。
  - Attention（J-17）: self-attention / cross-attention / causal masking の数理は J-17 に譲り、本エントリは「どの Attention をどの塔で使うか」の配置に集中する。
  - LLM（J-14）: 現代 LLM の主流が Decoder-only である理由（事前学習のスケールしやすさ・タスク汎用性・next-token 予測の単純さ）の総論は J-14 側。本エントリでは Encoder-Decoder との対比に限って触れる。
  - Whisper（D-71）: Encoder-Decoder の実例（音声 Encoder ＋ テキスト Decoder）。本エントリは構造の一般論、D-71 は製品としての音声認識。
  - VLM（J-15）: 画像 Encoder ＋ 言語 Decoder という分業が Encoder-Decoder の発想の延長であること。マルチモーダルの総論は J-15。
- スコープ境界: 本エントリは「Encoder-Decoder とは何か・なぜ役割を分けるか・Decoder-only とどう違い、なぜ主流が後者に寄ったか」までを担う。各 Attention の数式と各製品の詳細は関連エントリに譲る。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Vaswani et al., "Attention Is All You Need" (2017) https://arxiv.org/abs/1706.03762 — checked 2026-06-22（原典 Transformer の Encoder-Decoder 構成、cross-attention、self-attention の一次出典）
- Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (T5, 2020) https://arxiv.org/abs/1910.10683 — checked 2026-06-22（あらゆるタスクを text-to-text の seq2seq に統一した Encoder-Decoder の代表例）
- Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision" (Whisper, 2022) https://arxiv.org/abs/2212.04356 — checked 2026-06-22（音声 Encoder ＋ テキスト Decoder という Encoder-Decoder の実装例）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- Decoder-only が主流になった理由の補足: ①事前学習が next-token 予測 1 本でスケールしやすい ②in-context learning でタスクを統一でき、タスクごとに Encoder を作り分けなくてよい ③実装が単純（塔 1 本）でスループット最適化（KV Cache 等）が効きやすい。一方、翻訳・音声認識のように「入力を双方向で深く読みたい／入出力の性質が明確に違う」タスクでは Encoder-Decoder が今も自然で有利。両者は優劣ではなくタスク適合の問題、という整理を誌面では採る。
- 用語注: 原典の "encoder" / "decoder" は通信・信号処理の符号化器・復号化器の比喩。系列を別表現に「畳み込む」「展開する」役割分担を指し、可逆な符号化を意味するわけではない点に留意。
