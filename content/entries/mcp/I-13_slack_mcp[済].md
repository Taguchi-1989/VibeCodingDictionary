---
id: I-13
title: Slack MCP
title_reading: スラックエムシーピー
category: mcp
subtype: reference
experience_level: hands_on
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2024-11
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - Notion MCP
  - AWS MCP
status: ready
---

# Slack MCP

## tagline

Slack ワークスペースを AI クライアントから操作できる、MCP の公式 reference server です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

チャンネル一覧取得・メッセージ取得・投稿・リアクション付与などの操作を、Claude などの AI クライアントから直接実行できます。Bot Token（xoxb-）を渡して起動するだけで連携が始まります。

## どこで出会うか

社内のやりとりを AI に要約させたいとき、会議メモをチャンネルへ自動投稿したいときに登場します。Claude の設定ファイルに接続情報を追加することで使えます。

## メイン図

### 図の狙い

AI クライアント → Slack MCP Server → Slack ワークスペースという接続の流れと、Bot Token が橋渡しをしていることを示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Slack MCP Server
- 周辺の要素: Claude（AI クライアント）／Bot Token（xoxb-）／チャンネル一覧取得／メッセージ投稿／Slack ワークスペース
- 関係の描き方: 左から右へ矢印。Claude → Slack MCP → Slack の 3 層構造

## 会話での使い方例

「昨日の #design チャンネルのやりとりを Slack MCP で要約させました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Slack を AI から操作する MCP の公式 reference server です。

### 2. うれしさ

チャンネル要約や自動投稿をコード不要で AI に任せられます。

### 3. 注意点

投稿スコープを bot に与えると、AI が誤投稿するリスクがあります。

### 4. どこで役立つか

議事録の自動共有や、複数チャンネルの情報収集に向いています。

### 5. はじめに

Slack App 作成と OAuth スコープの読み書き区別を把握します。

### 6. 深掘り先

MCP、MCP Server、Notion MCP

## 開発フローでの位置（必須）

1. Slack App 作成 — Slack API サイトで Bot Token を発行します
2. スコープ設定 — `channels:history` など必要な権限を付けます
3. サーバー起動 — Slack 用の MCP Server を起動します
4. Claude 設定 — 設定ファイルにトークンを環境変数として登録します
5. 動作確認 — まず閲覧だけで試し、投稿は後から足します


## 関連用語

- MCP
- MCP Server
- Notion MCP
- AWS MCP


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Teams をメインに使っているので、Slack は触ったことがありません。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Slack の方が便利そうですが、Teams 標準で評価は下がります。
- 👍 良い点: Slack の全域を横断検索できそうです（要確認）。
- 👎 ダメな点: Slack 有料プランでないと試せないかもしれません。
- 👥 誰向けか: Slack を日常的に使っているユーザー向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Claude（左）→ Slack MCP Server（中央）→ Slack ワークスペース（右）の 3 層フロー図
- 登場人物: 女性担当者が Claude に「昨日の #design チャンネルを要約して」と話しかけている
- 吹き出し・心の声: 担当者「会議後に手動でまとめるのが大変で…」→ Slack MCP 経由で自動要約が返ってくる様子
- 中央に置くキーワード/ラベル: Slack MCP Server／Bot Token（xoxb-）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: Slack App ロゴ + 鍵アイコン
- Step 2 のアイコン/絵柄: チェックリスト（スコープ一覧）
- Step 3 のアイコン/絵柄: ターミナル + npx コマンド
- Step 4 のアイコン/絵柄: 設定ファイル（JSON）
- Step 5 のアイコン/絵柄: Slack チャンネル + 虫眼鏡（閲覧確認）
- 矢印で示す流れの意図: 準備（認証）→ 起動（接続）→ 確認（安全運用）の段階を示す


## コミュニティ補完メモ

- I-1 MCP との住み分け：I-1 は規格の全体像。I-13 は Slack に特化した実装例
- I-2 MCP Server との住み分け：I-2 は server の概念と構造。I-13 は Slack の具体ユースケース
- I-30 Notion MCP との住み分け：同じ reference server 系。ドキュメント管理（Notion）かコミュニケーション（Slack）かで使い分ける
- OAuth スコープで迷う読者向け補足：`channels:history` が過去メッセージ取得、`chat:write` が投稿に相当。最初は `channels:history` + `channels:read` だけで要約確認ができる


## 出典メモ

- <https://github.com/modelcontextprotocol/servers/tree/main/src/slack> — checked 2026-04-29
- <https://modelcontextprotocol.io/introduction> — checked 2026-04-29


## 備考

- Bot Token（xoxb-）は User Token（xoxp-）と異なり、ワークスペース全体の bot として動作する
- 投稿スコープ（`chat:write`）は後から追加する運用が安全。閲覧確認が取れてから付与する
- `@modelcontextprotocol/server-slack` は TypeScript 実装の公式 reference server（2024-11 公開）
