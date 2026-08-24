---
id: I-23
title: Serena MCP
title_reading: セレーナエムシーピー
category: mcp
subtype: dev_automation
experience_level: hands_on
reader_level: 3-4
importance: E
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - LSP
  - Context Engineering
  - VS Code
status: ready
---

# Serena MCP

## tagline

LSP（Language Server Protocol）でシンボル操作を LLM に提供する MCP Server です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

シンボルの定義位置や参照先を LSP 経由で正確に取得し、LLM が「必要箇所だけ参照・書き換え」できるようにします。Oraios AI 公開のオープンソース Server です。

## どこで出会うか

大規模リポジトリでリファクタや影響範囲調査を行うときに名前が出ます。`uvx` コマンドで起動して MCP Client 設定に登録するだけで使え、Python・TypeScript・Rust・Go など多言語に対応しています。

## メイン図

### 図の狙い

grep による全文検索と LSP 経由のシンボル解析の違いを対比し、Serena がコンテキスト消費を抑えながら精度を上げる仕組みを伝えます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Claude が grep でリポジトリ全体を検索
  - 視覚要素: 大量のファイルが赤くハイライトされたコンテキスト枠
  - つまずき: 関係ないファイルまで読み込み、コンテキストが圧迫される
- After
  - 状況: Serena MCP 経由でシンボル参照を取得
  - 視覚要素: 対象の関数定義と参照箇所だけが青くピックアップされた図
  - うれしさ: 必要箇所だけ取得でき、型情報込みの精度の高い参照が得られる

## 会話での使い方例

「Serena で `parseJSON` の参照を全部洗ってから修正箇所を絞り込みました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LSP 経由でシンボル情報を LLM に渡す MCP Server です。

### 2. うれしさ

grep より正確な参照解析で影響範囲を素早く把握できます。

### 3. 注意点

LSP が対応する言語でないと動作しない点に注意が必要です。

### 4. どこで役立つか

大規模リポジトリの関数改名や依存関係調査で効果が出やすいです。

### 5. はじめに

MCP と LSP の基本的な役割を押さえると理解が早まります。

### 6. 深掘り先

MCP Server、LSP、Context Engineering

## 開発フローでの位置（必須）

1. 環境構築 — `uvx` で Serena を起動し、MCP Client の設定に登録します
2. シンボル参照 — 調べたい関数名やクラス名を指定し、定義位置と呼び出し箇所を取得します
3. 影響範囲の確認 — そのシンボルを参照する箇所を一覧で確認します
4. 安全な書き換え — 影響範囲を把握した上で、関数単位で安全にコードを修正します
5. 動作確認 — 修正後に再度参照を引き、取り残しがないか確かめます

## 関連用語

- MCP
- MCP Server
- LSP
- Context Engineering
- VS Code

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「すごくいい、トークン効率が上がる」と言われますが、原理がまったく分かりません
- 入れたはいいものの、ちゃんと起動しているのかも分かっていません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: バイブコーダーの人がかなりおすすめしたいやつなのでしょう
- 👍 良い点: 確かにトークンの使用効率は下がった気がします
- 👎 ダメな点: 最近のものだともういらないのかな？ 区別がつかず分かりません
- 👥 誰向けか: 少し昔のエージェントツールを使っている人向けでしょうか
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に「Claude が grep で大量ファイルを読む」図、右に「Serena MCP 経由でシンボルだけ取得」図を並べた Before/After
- 登場人物: 画面の前で困り顔のエンジニア（Before）と、すっきりした表情で必要箇所だけ見ているエンジニア（After）
- 吹き出し・心の声: Before「また関係ないファイルまで読んでる…」 After「`parseJSON` の参照だけ全部出た！」
- 中央に置くキーワード/ラベル: Serena MCP（LSP 経由）
- Before / After の対比ポイント: コンテキスト枠の占有量（Before=赤く満杯 / After=青く必要箇所のみ）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ターミナルアイコン（起動・設定）
- Step 2 のアイコン/絵柄: 虫眼鏡アイコン（シンボル参照）
- Step 3 のアイコン/絵柄: ネットワーク図アイコン（影響範囲）
- Step 4 のアイコン/絵柄: 鉛筆アイコン（書き換え）
- Step 5 のアイコン/絵柄: チェックマークアイコン（動作確認）
- 矢印で示す流れの意図: 「設定 → 調査 → 把握 → 修正 → 確認」という安全なリファクタの順序

## コミュニティ補完メモ

- I-1 MCP との住み分け：I-1 は MCP という規格・概念全体の解説。Serena MCP はその規格を使った具体的なコード解析ツールの紹介。
- I-2 MCP Server との住み分け：I-2 は「MCP Server とは何か（構造・役割）」の総論。Serena MCP はその具体例の 1 つ。
- G-11 Context Engineering との住み分け：G-11 はコンテキスト設計の考え方全体。Serena はコンテキスト消費の削減手段として補完的に参照される。
- 「Claude Code が grep すれば良くない？」という読者の疑問については、LSP 経由の型情報付き参照と grep の全文検索では精度が根本的に異なることを備考に補足。

## 出典メモ

- [oraios/serena GitHub リポジトリ](https://github.com/oraios/serena) — checked 2026-04-29

## 備考

- Serena MCP は Oraios AI（スイス）が公開するオープンソースプロジェクト。
- grep との違い：grep はテキストマッチのため同名の変数や文字列リテラルも拾う。LSP 経由の参照は言語の型情報と構文木を利用するため、「本当にその関数を呼んでいる箇所」だけを正確に抽出できる。
- 対応言語は Python / TypeScript / JavaScript / Java / Kotlin / Rust / Go / C / C++ など（2026-04-29 時点）。
