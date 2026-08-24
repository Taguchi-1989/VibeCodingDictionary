---
# ── 識別・分類 ──
id: F-140
title: Mermaid
title_reading: マーメイド
category: term_tool
subtype: diagram

# ── 読者・体験 ──
experience_level: partial
reader_level: 2-3
importance: C

# ── 誌面形式 ──
figure_type: before_after
page_layout: spread_v1

# ── 時変情報 ──
start_date: 2014-01-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-30

# ── 関係 ──
related_terms:
  - Markdown
  - PlantUML
  - GitHub
  - SVG

# ── 制作状態 ──
status: needs_review
---

# Mermaid

## tagline

テキストでフローチャートや構成図を生成できる記法です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Markdown のコードブロックに `mermaid` と指定するだけでフローチャートやシーケンス図をブラウザ上で描画します。図のソースがテキストなので Git 差分管理ができます。

## どこで出会うか

GitHub や Notion のドキュメントで見かけます。AI に「Mermaid で構成図を出して」と頼むと README や PR にそのまま貼れる形で返ってきます。

## メイン図

### 図の狙い

テキスト数行から図が生まれる流れを Before / After で示し、手書きや画像編集が不要になる感覚を掴んでもらいます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 構成図を画像として描いてドキュメントに貼っていた
  - 視覚要素（コード or 概念）: スクリーンショットや PNG ファイルを毎回更新する手間
  - つまずき: 図を変更するたびに画像を作り直して貼り替える必要がある
- After
  - 状況: Mermaid の記法でテキストを編集するだけで図が更新される
  - 視覚要素: `graph TD; A-->B; B-->C;` の 1 行が即座に矢印図になる
  - うれしさ: Git の差分でどこを変えたか分かり、AI にも頼みやすい

## 会話での使い方例

「Mermaid で構成図を Claude に書いてもらって、PR にそのまま貼りました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

テキストから図を自動生成する軽量な記法です。

### 2. うれしさ

図がテキストなので Git 管理でき、AI にも生成を頼めます。

### 3. 注意点

細かいレイアウト調整は苦手で、複雑な図には不向きです。

### 4. どこで役立つか

README・PR・仕様書など、テキスト主体のドキュメントで役立ちます。

### 5. はじめに

GitHub でのレンダリングと `graph TD` の基本構文を把握するところから始めます。

### 6. 深掘り先

PlantUML、Excalidraw、Markdown

## 開発フローでの位置（必須）

1. 設計・議論 — システム構成や処理の流れを Mermaid でテキスト化して共有します
2. ドキュメント作成 — README や仕様書に記法をそのまま埋め込みます
3. AI への依頼 — 「Mermaid で書いて」と指示すると図のテキストが返ってきます
4. レビュー・更新 — テキスト差分だけで図の変更が分かり、PR レビューが楽になります

## 関連用語

- Markdown
- PlantUML
- GitHub
- SVG


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 昔は AI 生成のクセが強く、図を整えるのに相当苦労した記憶があります。
- AI 利用者には自然な選択肢でも、それ以外の人には認知度が低く通じません。
- どこまで描けるのか、無料と有料の範囲の違いが分かりにくいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: フローチャートをテキストでさっと描けると知り、便利さに驚きました。
- 👍 良い点: 動的に更新できるため、即興で図を起こせる手軽さが嬉しいです。
- 👎 ダメな点: 大きな図だと文字が小さくなり、構文エラーか描画失敗かの判別も難しいです。
- 👥 誰向けか: 今後さらに広がりそうな記法で、全ての人にとって触る価値があります。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に「PNG を差し替える人（困り顔）」、右に「3 行テキストから矢印図が自動生成される画面」
- 登場人物: ノートPCを前に苦笑いしている人物（左 Before）と、スッキリした顔でテキストを入力している人物（右 After）
- 吹き出し・心の声: Before「また画像貼り替えだ…」/ After「テキスト変えるだけで更新できた！」
- 中央に置くキーワード/ラベル: `graph TD; A-->B;` → 矢印図
- Before / After の対比ポイント: 画像管理の手間 vs テキスト 1 行の即時反映

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 吹き出し（設計議論）
- Step 2 のアイコン/絵柄: ドキュメントアイコン
- Step 3 のアイコン/絵柄: AI ロボット（依頼）
- Step 4 のアイコン/絵柄: Git の差分アイコン
- 矢印で示す流れの意図: 設計 → 文書化 → AI 生成 → レビューの一方向フロー


## コミュニティ補完メモ

- PlantUML（F-141）との住み分け：Mermaid は手軽さと GitHub ネイティブ対応が強み。PlantUML は複雑なシーケンス図や厳密な UML が必要な場面向き。
- Excalidraw（B-31）との住み分け：Excalidraw は手書き風の自由なキャンバス。Mermaid はテキスト管理・AI 連携向き。
- SVG（F-9）との関係：Mermaid のレンダリング出力は SVG 形式で書き出せる。

## 出典メモ

- https://mermaid.js.org/intro/ — checked 2026-04-30
- https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/ — checked 2026-04-30


## 備考

- GitHub の Mermaid サポートは 2022 年 2 月に正式対応（Markdown のコードブロックで自動レンダリング）。
- Notion は Mermaid コードブロックをネイティブ表示（2023 年以降）。対応状況はアプリのバージョンによって異なる場合があります。
- 細かいノード位置の指定は Mermaid の仕様上難しい。レイアウトをコントロールしたい場合は Graphviz や D2 が選択肢になります。
