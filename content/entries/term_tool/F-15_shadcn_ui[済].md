---
id: F-15
title: shadcn/ui
title_reading: シャドシーエヌ ユーアイ
category: term_tool
subtype: framework
experience_level: hands_on
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2023-01-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - React
  - Tailwind CSS
  - v0
  - Radix UI
status: ready
---

# shadcn/ui

## tagline

React 用の UI コンポーネント集です。npm 配布ではなく CLI でコードを直接コピーする方式です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Radix UI と Tailwind CSS（F-16）を組み合わせたコンポーネントを提供します。1 コマンドでコードがプロジェクトにコピーされるため、そのまま自由にカスタマイズできます。

## どこで出会うか

Next.js（F-11）や Astro（F-17）で UI を組み立てる場面で登場します。AI アシスタントに「shadcn/ui で作って」と伝えると対応できるため、バイブコーディングでも定番の指定です。

## メイン図

### 図の狙い

「npm パッケージではなくコードコピー」という独自配布方式と、コンポーネントがプロジェクトに取り込まれる流れを示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: shadcn/ui CLI
- 周辺の要素（3〜5個）: Radix UI（プリミティブ）、Tailwind CSS（スタイル）、自プロジェクトのコード、npx コマンド
- 関係の描き方（矢印・包含・比較）: CLI が Radix + Tailwind を合成したコードを自プロジェクトへ「コピー」する矢印


## 会話での使い方例

「shadcn の Button を `add` してから画面を組んでいくと早いです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

React 向け UI コンポーネントをコピー方式で提供します。

### 2. うれしさ

コードが自分のリポジトリに入るので自由に改変できます。

### 3. 注意点

npm 依存ではないためバージョン追従は手動になります。

### 4. どこで役立つか

React で UI を素早く組みたい場面に向きます。

### 5. はじめに

コピー配布方式の意味を押さえると使い方が掴めます。

### 6. 深掘り先

Radix UI、Tailwind CSS、v0


## 開発フローでの位置（必須）

1. プロジェクト初期化 — Next.js や Vite で React 環境を立ち上げます
2. shadcn/ui 導入 — `npx shadcn@latest init` で設定を生成します
3. コンポーネント追加 — `add button` でパーツをコピーします
4. カスタマイズ — 取り込まれたコードを直接編集します
5. AI との連携 — Claude や v0 に「shadcn/ui で」と指定して生成します


## 関連用語

- React
- Tailwind CSS
- v0
- Radix UI


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 名前の読み方が分からず AI に勧められるたびに調べ直していました。使ってはいたけどよく分かっていなかったというのが正直なところです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 謎の呪文のような名前で最初は全く分かりませんでした。
- 👍 良い点: コンポーネントをまとめて管理できベストプラクティスとして定着しています。
- 👎 ダメな点: 
- 👥 誰向けか: AI エージェントを使ってアプリを作る人は、ほぼ全員が通ることになると思います。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 開発者が CLI コマンドを打つとコンポーネントのコードが自プロジェクトへ飛んでくるイメージ図
- 登場人物（いれば）: ノートPC前の開発者1名
- 吹き出し・心の声: 「`add button` したらもうコードが入ってる！」
- 中央に置くキーワード/ラベル: shadcn/ui CLI
- Before / After の場合の対比ポイント: なし（構造図）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: フォルダ作成
- Step 2 のアイコン/絵柄: 設定ファイル生成
- Step 3 のアイコン/絵柄: コンポーネントコピー
- Step 4 のアイコン/絵柄: コード編集
- 矢印で示す流れの意図: 1コマンドでコードが手元に来て、そのまま編集できる流れ


## コミュニティ補完メモ

- Tailwind CSS（F-16）との住み分け：F-16 はスタイルの仕組みを扱う。F-15 はそれを前提にしたコンポーネント集として分担
- v0（B-9）との住み分け：v0 は Vercel が提供する UI 生成 AI ツール。shadcn/ui をベースに出力するため、v0 の出力物の前提知識として F-15 が機能する
- React（F-11）との住み分け：F-11 は React 自体の説明。shadcn/ui は React 生態圏の UI ライブラリとして分担


## 出典メモ

- [shadcn/ui 公式サイト](https://ui.shadcn.com/) — checked 2026-04-29
- [shadcn-ui/ui GitHub](https://github.com/shadcn-ui/ui) — checked 2026-04-29


## 備考

- コピー配布方式のため、shadcn/ui 本体のバージョンアップが自プロジェクトに自動適用されない点は利点でも注意点でもある
- 個人開発者（shadcn）が 2023 年に開始、Vercel が支援・関連プロジェクトとして拡大（2026-04-29 時点）
- Radix UI はアクセシビリティ対応のプリミティブを提供するライブラリで、shadcn/ui の基盤
