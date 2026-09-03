---
id: J-25
title: Tokenizer・BPE
title_reading: トークナイザー・ビーピーイー
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
  - Token
  - LLM
  - Transformer
  - パラメータ数の単位
  - Context Window
status: ready
---

# Tokenizer・BPE

## tagline

Tokenizer は文字列をトークンに刻む器、BPE（Byte Pair Encoding、バイト対符号化）はその刻み方を統計的に決める手法です。LLM は文字でも単語でもなく「サブワード単位のトークン」で世界を見ます。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Tokenizer（トークナイザ）は、私たちが書いた文字列を LLM が処理できる「トークン」という単位に分割する前処理装置です。LLM の本体（Transformer）は数値ベクトルしか扱えないため、まず文字列を整数 ID の列に変換する必要があり、その変換規則を担うのが Tokenizer です。

このとき問題になるのが「どの単位で刻むか」です。素朴には 2 つの極端が考えられます。

- **単語単位**で刻む案：人間には自然ですが、語彙が爆発します。英語だけで数十万語、活用形や複合語、固有名詞を入れれば際限なく増え、学習時に見なかった単語（未知語、Out-of-Vocabulary）が必ず出ます。未知語は `<UNK>` という 1 つの記号に潰すしかなく、情報が失われます。
- **文字単位**で刻む案：未知語は原理的に消えます（どんな単語も文字の列に分解できる）が、今度は系列が長くなりすぎます。`internationalization` が 1 トークンではなく 20 トークンになり、Transformer の計算量は系列長の 2 乗で効くため、文字単位は計算が重く、また 1 トークンあたりの意味が薄くなって学習効率も落ちます。

この 2 つの折衷が**サブワード（subword）単位**です。頻出する塊（`the`, `ing`, `tion` など）は 1 トークンにまとめ、珍しい単語は小さな断片や最終的には文字・バイトまで分解する。「頻度が高いものほど大きく、低いものほど細かく」刻むことで、語彙サイズを数万程度（GPT-4 系の `o200k_base` で約 20 万、GPT-3.5/4 の `cl100k_base` で約 10 万）に抑えつつ、未知語をゼロにできます。

**BPE（Byte Pair Encoding）**は、このサブワード語彙を**コーパスから自動的に育てる**アルゴリズムです。手順は貪欲法（greedy）で、概略は次の通りです。

1. まず全テキストを最小単位（文字、または後述するバイト）に分解する。
2. コーパス全体を走査し、**隣り合うペアのうち最も出現回数が多い組**を 1 つ見つける。
3. そのペアを 1 つの新しいトークンとして語彙に追加し、コーパス中の全該当箇所をマージする。
4. 語彙が目標サイズ（例：10 万語）に達するまで 2〜3 を繰り返す。

具体例で見ます。コーパスに `low` が 5 回、`lower` が 2 回、`newest` が 6 回、`widest` が 3 回あるとします。最初は全部バラバラの文字（`l o w`, `l o w e r`, …）です。隣接ペアを数えると `e s`（newest と widest に登場）や `e r`（lower に登場）が多く出ます。最頻ペアが `e s` ならまずこれをマージして `es` というトークンが生まれ、次に `es t` がマージされて `est` が生まれ……という具合に、頻出の語尾 `est` や `er` が**学習データの統計だけから自然に切り出されます**。人間が「`-est` は最上級の接尾辞だ」と教えたわけではなく、ただ「よく隣り合うから」まとめられた結果が、たまたま意味のある形態素に近づくのが BPE の面白いところです。

実際の LLM では、文字ではなく**バイト単位の BPE（byte-level BPE）**が主流です。Unicode 文字をそのまま単位にすると、絵文字や CJK（漢字・かな）まで含めて単位の種類が膨大になり、また学習データにない文字で再び未知語問題が起きます。そこで一段下の **UTF-8 バイト列**（0〜255 の 256 種類）を最小単位に取ると、世界中のどんな文字・絵文字・記号も必ず表現でき、原理的に未知語が消えます。日本語の「猫」は UTF-8 で 3 バイトなので、まず 3 つのバイトに分解され、頻度が高ければマージされて 1〜2 トークンにまとまります。これが「日本語は英語より多くトークンを食いがち」になる根の理由です。英語は概ね 1 単語が 1 バイト×数文字で頻出マージも効きますが、日本語は 1 文字 3 バイトから始まるうえ学習コーパス上の頻度も英語ほど高くないため、マージが進みきらず、1 文字が 1〜3 トークンに散りやすいのです。


## どこで出会うか

直接「Tokenizer を設定する」場面は、自分でモデルを学習・ファインチューニングする人を除けばほとんどありません。ですが**結果としては毎日出会っています**。

最もはっきり出会うのは**課金とコンテキスト長**です。OpenAI や Anthropic の API 料金は「1M トークンあたり ◯ ドル」で、Context Window（コンテキスト窓、G-5）の上限も「128K トークン」のようにトークンで表されます。つまり Tokenizer は**課金メーターであり、入力できる長さの物差し**そのものです。同じ「だいたい 1 ページ」の文章でも、英語より日本語のほうがトークン数が多くなり、料金もコンテキスト消費も増えます。これは品質の差ではなく、純粋に Tokenizer の刻み方の差です。

もう 1 つは**モデル間の比較や乗り換え**です。GPT-3.5/4 系（`cl100k_base`）と GPT-4o 系（`o200k_base`）ではトークナイザが違い、同じ日本語でも後者のほうがトークン数が少なく済みます。モデルを変えると「同じプロンプトなのにコンテキスト消費が変わった」ことが起きるのは、本体だけでなく Tokenizer も入れ替わったからです。OpenAI の `tiktoken`、Hugging Face の `tokenizers`、Google の SentencePiece などを使うと、実際に何トークンになるかを手元で数えられます。コードや JSON を大量に投げるエージェント開発では、この「トークン会計」が地味に効いてきます。


## メイン図

### 図の狙い

同じ一文が「単語単位／文字単位／サブワード（BPE）単位」で刻まれるとトークンの粒度と本数がどう変わるかを横並びで見せ、BPE が「頻出は大きく・珍しいは細かく」の折衷であることを一目で掴んでもらう。


## 会話での使い方例

「日本語はバイト単位 BPE で刻まれるので、英語より多くトークンを食いますよね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

文字列を LLM が読める整数 ID 列（トークン）に変換する入口の前処理装置です。

### 2. うれしさ

サブワード単位なので語彙爆発を抑えつつ未知語をゼロにでき、系列長も抑えられます。

### 3. 注意点

トークン数は課金とコンテキスト消費の単位で、日本語は英語より多く食いがちです。

### 4. どこで役立つか

API のコスト見積もり、コンテキスト長の管理、モデル乗り換え時の消費量の予測に効きます。

### 5. はじめに

`tiktoken` や Hugging Face `tokenizers` で自分の文章が何トークンか数えてみるのが入口です。

### 6. 深掘り先

byte-level BPE、SentencePiece／Unigram、Transformer の埋め込み層


## 開発フローでの位置（必須）

1. 入力受け取り — ユーザーやファイルから生の文字列（UTF-8）を受け取る
2. トークン化 — Tokenizer が BPE 規則で文字列をサブワードのトークン列に刻む
3. ID 化・埋め込み — 各トークンを整数 ID にし、Transformer の埋め込み層でベクトル化する
4. 推論 — モデルが次トークンの確率を計算し、トークン単位で生成する
5. デトークン化 — 生成されたトークン ID 列を文字列に復元して出力する


## 関連用語

- Token
- LLM
- Transformer
- パラメータ数の単位
- Context Window


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 日本語は1文字≒1トークンになりがちで同じ内容でも英語より多くなる、という感覚は早い段階から掴めた。
- 最近「クレジット」という別単位が出てきており（Microsoft 系など）、トークンと混在してややこしい。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 昔の携帯のパケット料金みたいなイメージ。インプットとアウトプットで料金が違う点も含めて、わりと早い段階から掴めた。
- 👍 良い点: このモデルは高い・安いという感覚が分かるようになる。さらに「自社でモデルを持たないベンダーは API を借りて利益を上乗せしないといけないから原理的に不利」というのが見えてくる。お金・通貨と同じ感覚で持てる。
- 👎 ダメな点: その感覚を人に説明しづらい。
- 👥 誰向けか: 結構誰にでも開示していい内容。みんなトークンあたりいくらという感覚を持てるといいと思う。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 1 つの英文（例 "the newest widest"）と 1 つの日本語文（例「猫がいます」）を、横 3 レーン（①単語単位 ②文字/バイト単位 ③サブワード=BPE）に分けて、それぞれトークンの区切りをブロックで可視化。①は箱が大きいが未知語に弱い、②は箱が極小で本数が多い、③は頻出語尾 est/er が 1 箱にまとまる中庸、と本数差が一目で分かるように。日本語レーンでは「猫」が UTF-8 の 3 バイト箱に割れる様子を添える。
- 登場人物（いれば）: トークン数を数えている開発者 1 名（電卓またはメーターを持つ）。
- 吹き出し・心の声: 「同じ意味なのに、日本語のほうがトークン箱が多い…！」「BPE は頻度でちょうどいい大きさに刻んでくれるのか」
- 中央に置くキーワード/ラベル: 「頻出は大きく・珍しいは細かく ＝ サブワード（BPE）」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 生テキスト（吹き出し or ドキュメント）
- Step 2 のアイコン/絵柄: テキストがブロックに割れる（ハサミ＋ブロック列）
- Step 3 のアイコン/絵柄: ブロックに番号が振られ→格子状ベクトルへ
- Step 4 のアイコン/絵柄: 確率分布から次トークンが 1 つ点灯（生成）／Step5 で文字列に戻る矢印

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: Tokenizer・BPE
- visual_subject: 同じ文が「単語単位・文字単位・BPE サブワード単位」でどう異なる粒度に刻まれるかを横 3 レーンで並べた比較図
- supporting_subjects: 電卓（コスト計算）を持つ開発者 1 名、日本語「猫」が UTF-8 3 バイトに割れる補足
- logo_subject: none
- excluded_subjects: カラフルなトークン色分け、実在サービスのUI、ヒートマップ、絵文字、虹色バー

### scene brief（日本語）
中央に横 3 レーンの比較図を置く。上段に同じ英文（例 "the newest widest"）を、①単語単位（大きなブロック、少ない）、②文字単位（極小ブロック、大量）、③BPE サブワード（中サイズ、"est"/"er" が 1 ブロック）の 3 パターンで並べる。下段に「猫」が 3 バイト箱に割れる日本語レーンを添える。右側に電卓かメーターを持つ開発者（著者の分身）が吹き出しで「同じ意味なのに、日本語のほうがトークン箱が多い…！」と語る。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background; a single developer character holding a calculator or meter gauge with a speech bubble; three horizontal token lanes center stage — top lane shows large word-unit blocks, middle lane shows tiny character-unit blocks (many more boxes), bottom lane shows medium subword BPE blocks where common suffixes are merged into single boxes highlighted in pale blue #EAF1FB; a small annotation below showing a Japanese character split into three byte-boxes; flat, clean, consistent series style; minimal text labels only "Word", "Char", "BPE", "頻出は大きく·珍しいは細かく"; 2:1 horizontal composition. No yellow, green, red, purple, orange, rainbow colors, colorful UI, or brand colors.

## コミュニティ補完メモ

- Token（G-2）との住み分け: G-2 は「トークン＝課金・長さの単位」という読者向けの説明。本エントリ J-25 は「そのトークンを誰がどう作っているか（Tokenizer のアルゴリズム＝BPE）」という一段内部の技術解説。重複を避け、J-25 は仕組み（貪欲マージ・byte-level）に寄せる。
- Context Window（G-5）との住み分け: G-5 は「窓の広さと使い切りの話」。本エントリは「窓の目盛り＝トークンを刻む側」。日本語が窓を早く食う理由を J-25 が供給する。
- SentencePiece / WordPiece / Unigram は BPE の兄弟手法。誌面に載せると発散するため本文では byte-level BPE までに留め、深掘り先と備考に逃がした。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Sennrich, Haddow, Birch "Neural Machine Translation of Rare Words with Subword Units" (ACL 2016, arXiv:1508.07909) — BPE をサブワード分割に応用した原典 — checked 2026-06-22
- OpenAI tiktoken (https://github.com/openai/tiktoken) — cl100k_base / o200k_base の実装と byte-level BPE の挙動 — checked 2026-06-22
- Hugging Face NLP Course "Byte-Pair Encoding tokenization" (https://huggingface.co/learn/nlp-course/chapter6/5) — BPE の学習手順とマージの具体例 — checked 2026-06-22

## 備考

- reader_level: 6（著者の自己学習シェルフ・刊行スコープ外、docs/level_policy.md §2-6）。今季の本には載せない深掘り技術ノート。
- 字数は Lv6 ノート共通ルールにより制限を外し、腹落ち優先で本文を厚めにした。
- 本文では byte-level BPE までを扱い、SentencePiece の Unigram 言語モデル方式（BPE とは別系統の確率的分割）や WordPiece（BERT 系）は深掘り先・コミュニティ補完メモに退避した。
- 語彙サイズ（cl100k_base ≈ 10 万、o200k_base ≈ 20 万）は 2026-06 時点の OpenAI 公開実装に基づく時変情報。モデル更新で変わり得る。
