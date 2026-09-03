---
id: F-80
title: Node.js
title_reading: ノードジェイエス
category: term_tool
subtype: runtime
experience_level: partial
reader_level: 2-3
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2009-05-27
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - JavaScript
  - npm
  - pnpm
  - TypeScript
status: ready
---

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
- 左ページ：読者が初めて読む側。短い段落で物語的に書く。
- 右ページ：辞書引き側。6視点の見どころ → つまずき／私のコメント → 開発フロー → 関連用語 → 参考 URL。
- 「非エンジニアのつまずき」「私のコメント」は著者本人が記入する欄。AI は原則触らない。
-->

## tagline

JavaScript（F-1）をブラウザの外で動かすランタイムです。サーバや CLI ツールの基盤として広く使われています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Chrome の V8 エンジンを内蔵し、JavaScript をサーバや CLI で実行できます。非同期 I/O ライブラリ（libuv）と組み合わせて、多数のリクエストを効率よく捌けます。

## どこで出会うか

AI ツール CLI を導入するときに `npx claude` のようなコマンドで登場します。MCP サーバや Vite（F-41）も Node.js 上で動くため、README やエラーで名前を見かけます。

## メイン図

### 図の狙い

「ブラウザの外でも JS が動く」という構造を、ランタイムと実行対象の関係で示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Node.js ランタイム
- 周辺の要素（3〜6個）: V8 エンジン / libuv / npm パッケージ / サーバアプリ / CLI ツール / MCP サーバ
- 関係の描き方（矢印・包含・比較）: Node.js が中心にあり、各用途へ矢印で展開する包含図

## 会話での使い方例

「Node.js さえあれば `npx` で AI ツールをすぐ動かせます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

JavaScript をサーバや CLI で実行するランタイムです。

### 2. うれしさ

`npx` 1 行で AI ツールの CLI をすぐ試せます。

### 3. 注意点

ブラウザ専用 API（`window` 等）は使えません。

### 4. どこで役立つか

AI ツール CLI の導入やビルドツールの実行で役立ちます。

### 5. はじめに

LTS（偶数番号）が安定版で、現行は v22 です。

### 6. 深掘り先

npm（F-40）、pnpm（F-44）、TypeScript（F-2）

## 開発フローでの位置（必須）

1. 環境準備 — Node.js をインストールして実行基盤を整える
2. パッケージ導入 — npm や pnpm で依存ライブラリを追加する
3. ツール実行 — `npx` コマンドで AI ツール CLI を起動する
4. サーバ構築 — バックエンドや MCP サーバの実行環境として利用する
5. ビルド処理 — Vite 等のビルドツールを Node.js 上で走らせる

## 関連用語

- JavaScript
- npm
- pnpm
- TypeScript

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- JavaScript の JS なんだろうけど、ノードって何？となります。
- Claude Code を入れる時に Node.js も求められ、JS の裏の巨大さに驚きました。
- バージョンの考え方が難しく、別の PC ではずれて動かないこともあります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 「なんだこれ」と思いましたが、よく見かけるので少しずつ馴染んできました。
- 👍 良い点: この上で Claude Code が動く基盤だと分かると見え方が変わります。
- 👎 ダメな点: 更新タイミングや英語の説明が分かりにくく、PC 間でバージョンがずれます。
- 👥 誰向けか: バイブコーディングをする人は誰しも一度は通る基礎だと思います。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に Node.js のロゴと「ランタイム」ラベルを置き、周囲に V8 / libuv / npm / CLI ツール / MCP サーバ / Web サーバを配置した包含図
- 登場人物（いれば）: 非エンジニアの人物が端末の前に座り、`npx claude` を打鍵している様子
- 吹き出し・心の声: 「これだけで動くの？」という驚き
- 中央に置くキーワード/ラベル: Node.js ランタイム
- Before / After の場合の対比ポイント: （構造図のため不要）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: インストール（ダウンロード矢印）
- Step 2 のアイコン/絵柄: パッケージ箱
- Step 3 のアイコン/絵柄: ターミナル画面
- Step 4 のアイコン/絵柄: サーバラック
- Step 5 のアイコン/絵柄: 歯車（ビルド）
- 矢印で示す流れの意図: 導入から実行・構築まで順方向で進む

## コミュニティ補完メモ

- JavaScript（F-1）との住み分け：F-1 は「言語仕様（ECMAScript）」を扱い、F-80 は「ブラウザ外の実行環境」を扱う。`window`/`document` 等のブラウザ API は Node.js では使えない点が最大の分岐点。
- npm（F-40）との住み分け：F-80 はランタイム本体、F-40 はパッケージ管理ツール。Node.js に同梱されているが概念は別。
- Deno・Bun との関係：Node.js の代替ランタイムとして Deno / Bun が存在するが、業界シェアでは Node.js が依然主流。備考に記載。

## 出典メモ

- [nodejs.org/en/about](https://nodejs.org/en/about) — checked 2026-04-29
- [github.com/nodejs/node](https://github.com/nodejs/node) — checked 2026-04-29

## 備考

- 2026-04 時点の LTS は Node.js 22。LTS は偶数番号のリリースが担当し、約 30 か月のサポート期間がある。
- Deno（Ryan Dahl が Node.js の反省を踏まえて開発）や Bun（高速を売りにした新興ランタイム）が存在するが、現時点では AI ツール CLI の多くが Node.js を前提としている。
- `npx` は Node.js に同梱の npm 経由で動く実行コマンド。パッケージをインストールせずにワンショット実行できる点が AI ツール導入のハードルを下げている。
