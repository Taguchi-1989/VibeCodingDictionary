---
id: G-48
title: Structured Outputs
title_reading: ストラクチャードアウトプット
category: term_llm
subtype: control
experience_level: partial
reader_level: 3-4
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-08-10
related_terms:
  - JSON Schema
  - Function Calling
  - Tool Use
  - JSON
status: ready
---

# Structured Outputs

## tagline

出力の形をスキーマで固定し、決まった構造の JSON を必ず返させる機能です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

出力の形を JSON Schema などのスキーマで指定し、その形どおりの応答を返させる機能です。「JSON で返して」とお願いするだけの方式と違い、必須項目の欠落や型の食い違いが起きません。

## どこで出会うか

Claude や ChatGPT などの API で、応答の形をスキーマで指定する設定として出会います。Anthropic は 2026 年 2 月に一般提供を開始しており、表を作る・分類する・書類から項目を抜き出すといった業務寄りの用途で使われます。

## メイン図

### 図の狙い

スキーマという型抜きを通すと、LLM の出力が決まった形の JSON にきっちり収まる様子を示す。

## 会話での使い方例

「Structured Outputs で必須項目や型のズレを防げます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

出力の形をスキーマで固定し、応答を強制する仕組みです。

### 2. うれしさ

必須項目の欠落や型ミスが起きにくくなります。

### 3. 注意点

実現方式が各社で違い、そのまま使い回せません。

### 4. どこで役立つか

表作成・分類・項目抽出など業務処理と相性が良いです。

### 5. はじめに

JSON Schema で出力の形を決める発想から始めます。

### 6. 深掘り先

JSON Schema、Function Calling、Tool Use。

## 開発フローでの位置（必須）

1. スキーマを設計する — 必須項目と型を JSON Schema で定義する
2. API リクエストに渡す — 出力形式としてスキーマを指定する
3. 構造化された応答を受け取る — 型どおりの JSON がそのまま返る
4. そのまま後続処理に回す — パースを挟まず値をすぐ使える

## 関連用語

- JSON Schema
- Function Calling
- Tool Use
- JSON

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- そもそも名前を初めて聞く。ここが最初のつまずき。
- 「JSON で返して」とお願いするのと何が違うのかが、言われないと分からない。
- 自分で設定するものなのか、ツール側が中でやってくれているものなのかが見えない。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回はじめて聞いた。決まった構造で出させるのがいいんだろうな、という感じ。
- 👍 良い点: 具体的な形で返ってくるのはいい。エンジニアリングの中でプロが実装してくれているところなので、便利に使えばいいと思う。
- 👎 ダメな点: 特にない、という感じ。
- 👥 誰向けか: ハーネスの原理原則のところまで行くと必要になる人向け。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: LLM の出力が四角い「型抜き（スキーマ）」を通り、決まった形の JSON になって出てくる様子
- 登場人物（いれば）: 左側に、自由形式の JSON を手にして困った顔をする人物。右側に、型抜きを通して整った表を受け取り安心する人物
- 吹き出し・心の声: 左の人物「あれ、必須のキーが抜けてる…」／右の人物「型どおりだから安心して使えます」
- 中央に置くキーワード/ラベル: スキーマ → 型どおりの JSON

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設計図を描く手（スキーマ設計）
- Step 2 のアイコン/絵柄: 送信矢印（API リクエスト）
- Step 3 のアイコン/絵柄: 型どおりに揃った JSON の箱（構造化された応答）
- Step 4 のアイコン/絵柄: そのまま流れ込む矢印（後続処理）


## コミュニティ補完メモ

- Function Calling（G-33）との住み分け：Function Calling は「関数を呼ぶための JSON 返却」という具体プロトコルに焦点を当てる。Structured Outputs は関数呼び出しに限らず、応答全体の形をスキーマで縛る話として書き分ける。
- JSON Schema（F-210）との住み分け：スキーマの書き方・仕様自体は F-210 に譲り、本エントリは「そのスキーマを LLM の出力制御に使う」場面に絞る。
- Tool Use（G-30）との住み分け：ツール呼び出しの仕組みそのものは G-30 に譲り、本エントリは通常の応答フォーマットを縛る用途を中心に扱う。


## 出典メモ

- Anthropic「Structured Outputs」 https://platform.claude.com/docs/en/build-with-claude/structured-outputs — checked 2026-08-10
- OpenAI「Structured Outputs」 https://developers.openai.com/api/docs/guides/structured-outputs — checked 2026-08-10


## 備考

- Anthropic は 2026 年 2 月に Structured Outputs の一般提供を開始した。実現方式は各社で異なり、生成時に形を強制する方式と、ツール呼び出しの仕組みを流用する方式がある。
