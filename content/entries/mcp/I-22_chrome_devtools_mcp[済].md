---
id: I-22
title: Chrome DevTools MCP
title_reading: クロームデブツールズエムシーピー
category: mcp
subtype: dev_automation
experience_level: hands_on
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - Playwright MCP
  - VS Code
status: ready
---

# Chrome DevTools MCP

## tagline

Chrome 専用の MCP Server です。ログ取得やパフォーマンス計測を AI から操作できます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Google 公式の `chrome-devtools-mcp` が CDP でブラウザを操作します。コンソールログとパフォーマンストレースを AI の指示で取得できます。

## どこで出会うか

フロントエンドのバグ調査や LCP（最大コンテンツ描画）計測を AI に任せる場面です。`npx chrome-devtools-mcp@latest` で起動し CDP で接続します。

## メイン図

### 図の狙い

AI エージェントが Chrome DevTools MCP を通じて Chrome を操作し、計測結果を受け取る流れを示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Chrome DevTools MCP（仲介役）
- 周辺の要素: AI エージェント / Chrome ブラウザ / DevTools Protocol（CDP）/ コンソールログ・パフォーマンストレース
- 関係の描き方: AI → MCP → CDP → Chrome の矢印で接続


## 会話での使い方例

「LCP の遅さを Chrome DevTools MCP で計測してもらえると助かります。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Chrome を AI から操作し、低レベルな計測データを取得する仲介役です。

### 2. うれしさ

パフォーマンストレースやコンソールログを AI が自動収集できます。

### 3. 注意点

Chrome 専用のため、Firefox や Safari の動作確認には使えません。

### 4. どこで役立つか

フロントエンドの速度改善やバグ調査の作業で役立ちます。

### 5. はじめに

Playwright MCP との違いは「クロスブラウザか Chrome 特化計測か」です。

### 6. 深掘り先

MCP Server、Playwright MCP、Chrome DevTools Protocol

## 開発フローでの位置（必須）

1. 環境準備 — `npx chrome-devtools-mcp@latest` でサーバーを起動します
2. 接続確立 — 実行中の Chrome または自動起動した Chrome に CDP で接続します
3. AI に指示 — コンソールログ取得・パフォーマンス計測などを AI エージェントへ依頼します
4. 結果受け取り — トレースデータやスクリーンショットを確認して改善策を検討します
5. 修正と再計測 — コード修正後に同じ手順で再計測して効果を確かめます


## 関連用語

- MCP
- MCP Server
- Playwright MCP
- VS Code


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Playwright との差分が分かりにくく、どちらを使うか判断が難しいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:Playwright と並ぶブラウザ操作役で便利そうです
- 👍 良い点:Chrome のパフォーマンス計測も任せられるようです
- 👎 ダメな点:Chrome 専用で Firefox や Safari は使えません
- 👥 誰向けか:Chrome だけ対応させたい人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: AI エージェントが Chrome DevTools MCP 経由で Chrome ブラウザを操作する構造図
- 登場人物（いれば）: フロントエンド開発者がノート PC の前に座り、AI チャット画面を見ている
- 吹き出し・心の声: 「LCP が遅い原因を調べてください」→ MCP が Chrome に接続 → 「3.2 秒です。画像が原因です」
- 中央に置くキーワード/ラベル: Chrome DevTools MCP

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ターミナルアイコン（npx 起動）
- Step 2 のアイコン/絵柄: 接続プラグアイコン（CDP 接続）
- Step 3 のアイコン/絵柄: AI チャットアイコン（指示）
- Step 4 のアイコン/絵柄: グラフ・スクリーンショットアイコン（結果）
- 矢印で示す流れの意図: 起動 → 接続 → 計測依頼 → 結果確認 → 改善の PDCA


## コミュニティ補完メモ

I-20 Playwright MCP との住み分け：Playwright MCP はクロスブラウザ（Chrome・Firefox・Safari）の自動化と E2E テスト向け。Chrome DevTools MCP は Chrome に特化し、Performance タブ相当の低レベル計測（LCP・FCP・トレース取得）に強みがある。「ブラウザを動かしたいだけ」なら Playwright MCP、「Chrome の計測データを AI に分析させたい」なら Chrome DevTools MCP を選ぶ。

I-1 MCP・I-2 MCP Server との関係：Chrome DevTools MCP は MCP のプロトコルに則って作られた具体的な Server 実装の 1 つ。MCP の仕組みを理解してからこのエントリを読むと理解しやすい。

## 出典メモ

- <https://github.com/ModelContextProtocol/servers> — checked 2026-04-29
- <https://developer.chrome.com/docs/devtools/protocol> — checked 2026-04-29


## 備考

- `chrome-devtools-mcp` は Google 公式提供の OSS（2026-04-29 時点で active）
- 起動オプションで「実行中の Chrome に接続」か「自動で headed Chrome を起動」かを選べる（時変情報あり、evaluation_date で管理）
- CDP は Chrome DevTools Protocol の略称
