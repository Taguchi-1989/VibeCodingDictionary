---
id: B-31
title: Excalidraw
title_reading: エクスカリドロー
category: service
subtype: saas_design
experience_level: hands_on
reader_level: 1-2
importance: D
figure_type: before_after
page_layout: spread_v1
start_date: 2020-01-01
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Mermaid
  - PlantUML
  - Figma
  - SVG
status: ready
---

# Excalidraw

## tagline

手書き風スタイルで素早くラフ図を描ける無料の作図ツールです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

フローチャートやアーキテクチャ図をブラウザだけで描けるツールです。ログイン不要で即起動でき、PNG や SVG へのエクスポートにも対応しています。

## どこで出会うか

AI に設計を相談する前の「整理メモ」として使われる場面が多いです。描いた図をスクリーンショットして Claude や ChatGPT に貼ると、図の意図ごと議論できます。

## メイン図

### 図の狙い

「ラフで描く → AI に貼る」という作業の流れを Before / After で示し、Excalidraw が何の入口になるかを伝えます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 設計の頭の中がまとまっていない
  - 視覚要素（コード or 概念）: 箇条書きのテキストメモのみ
  - つまずき: 何を AI に伝えればよいか分からない
- After
  - 状況: Excalidraw でラフ図を 5 分で描いた
  - 視覚要素: 手書き風のブロック図とフロー矢印
  - うれしさ: スクリーンショットを AI に渡して意図ごと議論できる

## 会話での使い方例

「Excalidraw でアーキテクチャをラフに描いて、Claude に説明させました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ブラウザで動く手書き風ラフ図ツールです。

### 2. うれしさ

ログイン不要で即使えて、AI への説明下書きになります。

### 3. 注意点

厳密な仕様書向けではなく、ラフを描く用途に限られます。

### 4. どこで役立つか

AI に設計を相談する前の図解整理に向いています。

### 5. はじめに

Web 版（excalidraw.com）でログイン不要の体験から始めます。

### 6. 深掘り先

Mermaid、Figma、PlantUML

## 開発フローでの位置（必須）

1. 頭出し — 設計の全体像をホワイトボード感覚でラフに描きます
2. AI 相談 — スクリーンショットを Claude や GPT に貼り付けて議論します
3. 修正 — AI のフィードバックを受けて図を手早く書き直します
4. 共有 — PNG または SVG でエクスポートして資料に貼り込みます
5. チーム協働 — Excalidraw+（SaaS 版）でリアルタイム共同編集できます

## 関連用語

- Mermaid
- PlantUML
- Figma
- SVG

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 手書き風の見た目が好みではなく、最初の見た目で離脱しがちです。
- 何のために起動するか分かりづらく、触る動機が湧きません。
- Mac ユーザーが好んで使うイメージがあり、自分の環境に馴染むか不安です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: AI 系の YouTuber が解説動画でよく画面に出していた印象が強かったです
- 👍 良い点: 無料でラフ図がブラウザ起動だけで描けるそうです
- 👎 ダメな点: Mermaid との差別化が掴めず使う動機が湧きません。
- 👥 誰向けか: AI 系の YouTuber や、手書き風の見た目が好きな人向けです
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左半分にテキストメモだけで困る人物、右半分に Excalidraw の手書き風ブロック図を描いた人物
- 登場人物（いれば）: 設計者（非エンジニア）が画面の前でメモを見ながら悩む左シーン、図を描いて AI に投げる右シーン
- 吹き出し・心の声: 左「何から説明すればいいんだろう…」、右「これで伝わりそう！」
- 中央に置くキーワード/ラベル: Excalidraw ロゴ風の手書き文字
- Before / After の対比ポイント: テキストのみ vs. 図付きで AI に相談できる状態

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ホワイトボード・ペン
- Step 2 のアイコン/絵柄: スクリーンショット・チャットバブル
- Step 3 のアイコン/絵柄: 矢印で修正を加える図
- Step 4 のアイコン/絵柄: PNG/SVG ファイルアイコン
- Step 5 のアイコン/絵柄: 複数人カーソル（協働編集）
- 矢印で示す流れの意図: 「ラフ描写 → AI 相談 → 修正 → 出力 → 共有」の一方向フロー

## コミュニティ補完メモ

- Figma（B-32）との住み分け：Figma はデザインシステム・高精度 UI 作成向け。Excalidraw は設計の初期ラフ・ホワイトボード向けで用途が異なります
- Mermaid（F-140）との住み分け：Mermaid はコードで図を生成するテキストベースのアプローチ。Excalidraw は手で直感的に描くビジュアルアプローチです。Excalidraw は Mermaid からの取り込みにも対応しているため、両方の入口になれます
- PlantUML（F-141）との住み分け：PlantUML は UML 図のコード生成向けで、厳密な仕様記述に向きます。Excalidraw はそこまで厳密さを求めない場面に向きます

## 出典メモ

- [excalidraw.com](https://excalidraw.com/) — checked 2026-04-30
- [github.com/excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) — checked 2026-04-30
- [plus.excalidraw.com](https://plus.excalidraw.com/) — checked 2026-04-30

## 備考

- Excalidraw はオープンソース（MIT ライセンス）。SaaS 版は Excalidraw+（チーム協働・有料）
- 開発者は Christopher Chedeau（元 Facebook）ら。公開は 2020 年
- ファイル形式 `.excalidraw` は JSON のため、Git で diff が取れる点が開発者に好まれる理由の一つ
- 「ちゃんとした図が作れない」という不満は用途のミスマッチ。製品仕様書や厳密な図には draw.io / Figma / PlantUML が向く
