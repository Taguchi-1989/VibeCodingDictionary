---
id: I-30
title: Notion MCP
title_reading: ノーションエムシーピー
category: mcp
subtype: collab
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
  - Slack MCP
  - AWS MCP
status: ready
---

# Notion MCP

## tagline

Notion ワークスペースを AI クライアントから操作できる MCP server です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ページ検索・取得・子ページ作成・データベース問い合わせ・コメント投稿など Notion API の操作を AI クライアントのツールとして提供します。

## どこで出会うか

仕様書を Notion で管理している組織で、Claude Code に「このページの要件を読んで実装して」と渡すときに登場します。議事録の自動書き出しにも使えます。

## メイン図

### 図の狙い

AI クライアント → Notion MCP Server → Notion ワークスペースという 3 層の接続と、Integration Token が橋渡しになっていることを示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Notion MCP Server
- 周辺の要素: Claude（AI クライアント）／Internal Integration Token／ページ検索・取得／コメント投稿／Notion ワークスペース
- 関係の描き方: 左から右への矢印。Claude → Notion MCP → Notion の 3 層構造

## 会話での使い方例

「Notion MCP で要件ページを拾わせて、そのまま Claude Code に実装させました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Notion ワークスペースを AI から操作する MCP server。

### 2. うれしさ

仕様書の読み込みやページ作成を AI に任せられます。

### 3. 注意点

Integration をページに「招待」しないとアクセスできません。

### 4. どこで役立つか

仕様管理を Notion で行う組織での AI 連携に向いています。

### 5. はじめに

Internal Integration Token の発行とページへの招待手順が必要です。

### 6. 深掘り先

MCP、MCP Server、Slack MCP

## 開発フローでの位置（必須）

1. Integration 作成 — Notion の設定画面でトークンを発行します
2. ページに招待 — 対象のページやデータベースに接続（招待）します
3. サーバー起動 — Notion 公式の MCP Server を起動します
4. Claude 設定 — 設定ファイルにトークンを環境変数として登録します
5. 動作確認 — まず検索・取得のみ試し、書き込みは権限を確認してから使います


## 関連用語

- MCP
- MCP Server
- Slack MCP
- AWS MCP


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- ネイティブな Notion ユーザーではないので、正直なところ何とも言えません
- どこにどう整理すればよいかが、触っていないため判断できません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Notion に MCP があるのは便利そうです
- 👍 良い点: MCP 経由なので効率が高いのではないでしょうか
- 👎 ダメな点: 使ってみないと使い心地が想像できません
- 👥 誰向けか: Notion のアクティブユーザー向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Claude（左）→ Notion MCP Server（中央）→ Notion ワークスペース（右）の 3 層フロー図
- 登場人物: 男性担当者が Claude に「この仕様ページを読んで実装して」と話しかけている
- 吹き出し・心の声: 担当者「Notion の要件をコピペしなくて済む！」→ Notion MCP 経由で仕様が自動で渡される様子
- 中央に置くキーワード/ラベル: Notion MCP Server／Internal Integration Token

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: Notion ロゴ + 鍵アイコン（Token 発行）
- Step 2 のアイコン/絵柄: ページアイコン + プラスボタン（招待）
- Step 3 のアイコン/絵柄: ターミナル + npx コマンド
- Step 4 のアイコン/絵柄: 設定ファイル（JSON）
- Step 5 のアイコン/絵柄: Notion ページ + 虫眼鏡（読み取り確認）
- 矢印で示す流れの意図: 認証準備 → 権限付与 → 起動 → 接続 → 確認の段階を示す

## コミュニティ補完メモ

- I-1 MCP との住み分け：I-1 は規格の全体像。I-30 は Notion に特化した実装例
- I-2 MCP Server との住み分け：I-2 は server の概念と構造。I-30 は Notion の具体ユースケース
- I-13 Slack MCP との住み分け：同じ reference server 系。ドキュメント管理（Notion）かコミュニケーション（Slack）かで使い分ける
- I-50 AWS MCP との住み分け：I-50 はクラウドインフラ操作。I-30 はドキュメント管理・知識ベース連携
- 公式（`@notionhq/notion-mcp-server`）とコミュニティ製が並立しているが、本エントリは公式を主体として扱う
- URL から Page ID を取り出す方法（末尾の 32 文字）は「読者のつまずき」の典型。ブロック ID と混同しやすい点を備考に記載


## 出典メモ

- <https://github.com/makenotion/notion-mcp-server> — checked 2026-04-29
- <https://developers.notion.com/docs/create-a-notion-integration> — checked 2026-04-29
- <https://modelcontextprotocol.io/introduction> — checked 2026-04-29


## 備考

- Internal Integration Token は `secret_` で始まる。External Integration（OAuth）とは別物
- ページ ID は Notion の URL 末尾の 32 文字（ハイフンを除く）。ブロック ID と形式が同じなので、URL のどの部分を使うかで混乱しやすい
- `@notionhq/notion-mcp-server` は 2024 年後半に Notion 公式がリリース。コミュニティ製（`notion-mcp` 等）も複数存在するが、公式が推奨される
- Integration をページに「招待」しないと「Could not find page with ID」や「No access」エラーになる。エラーメッセージだけでは原因が判断しづらいため注意
