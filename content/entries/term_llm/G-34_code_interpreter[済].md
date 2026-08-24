---
id: G-34
title: Code Interpreter
title_reading: コード インタプリタ
category: term_llm
subtype: code_execution
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: before_after
page_layout: spread_v1
start_date: 2023-07-01
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Tool Use
  - Function Calling
  - Python
  - Deep Research
status: ready
---

# Code Interpreter

## tagline

LLM がサンドボックス内で Python コードを実行して結果を返す機能です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

自然言語で「この CSV を分析して」と頼むと、AI が裏で Python コードを書いて実行し、グラフや数値結果を画面に返してくれます。コードを読む必要はありません。

## どこで出会うか

ChatGPT にファイルをアップロードしたときや、Claude の code execution 機能として登場します。「売上データを分析して」と話しかけると自動で動きます。

## メイン図

### 図の狙い

「自然言語で頼む → AI が Python を書いて実行 → 結果が返る」という一連の流れを、コードを書かずに使える体験として示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 表計算ソフトで手動グラフを作っている
  - 視覚要素（コード or 概念）: CSV ファイルと格闘するビジネスパーソン
  - つまずき: Python を知らないと自動化できない
- After
  - 状況: Code Interpreter に CSV を投げて「月別グラフを出して」と入力
  - 視覚要素: チャットに折れ線グラフが表示される
  - うれしさ: コードを書かずに分析結果が手に入る

## 会話での使い方例

「Code Interpreter で売上 CSV を投げたら、月別グラフまで自動で出ました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI が Python コードを書いて実行し、結果を返す機能です。

### 2. うれしさ

コードを書かずにデータ分析やグラフ作成ができます。

### 3. 注意点

コードを「書く」だけの機能ではなく「実行」まで行います。

### 4. どこで役立つか

営業・マーケターがデータを素早く可視化したい場面です。

### 5. はじめに

「AI が裏で Python を動かしている」と覚えれば十分です。

### 6. 深掘り先

Tool Use、Function Calling、Python

## 開発フローでの位置（必須）

1. ファイル準備 — CSV・Excel・画像ファイルをチャットにアップロードします
2. 自然言語で依頼 — 「月別集計してグラフ化して」と入力します
3. AI がコード生成・実行 — サンドボックス内で Python が自動実行されます
4. 結果を受け取る — グラフや数値・変換ファイルが画面に表示されます


## 関連用語

- Tool Use
- Function Calling
- Python
- Deep Research


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「LLM は計算できない」と思っている人が、このパラダイムに苦労しがちです
- Python が裏で走っていると伝えるのが難しく、説明が長くなりがちです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 革命的だと思いました
- 👍 良い点: Python が動くので計算が得意で、今は特に強いです
- 👎 ダメな点: 結果確認に図などの仕組みを合わせないと効率が上がりません
- 👥 誰向けか: 科学技術計算から Excel まで、幅広いデータ作業をする人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に CSV ファイルを持って困るビジネスパーソン、右にチャット画面でグラフが出た様子
- 登場人物: 営業職風の人物（スーツ、表計算ソフトの前）
- 吹き出し・心の声: Before「Python 書けないと無理か…」、After「送っただけでグラフになった！」
- 中央に置くキーワード/ラベル: Code Interpreter
- Before / After の場合の対比ポイント: コードを書く手間 vs チャットで完結

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ファイルアップロードアイコン
- Step 2 のアイコン/絵柄: チャット吹き出し
- Step 3 のアイコン/絵柄: 歯車（実行中）
- Step 4 のアイコン/絵柄: グラフ・チャートアイコン
- 矢印で示す流れの意図: ユーザー入力から自動実行・結果返却までのシンプルな一方向フロー


## コミュニティ補完メモ

- Tool Use（G-30）との住み分け：Tool Use は LLM がツールを呼び出す仕組みの総称。Code Interpreter はその中でもコード実行に特化した具体的な機能の呼び名。
- Function Calling（G-33）との住み分け：Function Calling は外部 API を呼ぶ機構で、Code Interpreter は Python 実行環境に特化。概念は近いが用途が異なる。
- Deep Research（G-35）との住み分け：Deep Research は検索・情報収集の自律実行。Code Interpreter はデータ処理・可視化に特化。

## 出典メモ

- OpenAI Blog "ChatGPT Code Interpreter" — checked 2026-04-30
- OpenAI Help "Advanced data analysis" — checked 2026-04-30


## 備考

- 2023-07 ChatGPT Plus に「Code Interpreter」として登場。その後「Advanced Data Analysis」に改名されたが、2024 年以降は再び Code Interpreter / Python tool と呼ばれるようになった。
- 名称は提供サービスによって異なる：ChatGPT では「Python tool」、Claude では「code execution」、Gemini では「Code Execution」。
