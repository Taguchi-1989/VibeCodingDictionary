---
id: I-41
title: SQLite MCP
title_reading: エスキューライトエムシーピー
category: mcp
subtype: data
experience_level: hands_on
reader_level: 3
importance: D
figure_type: workflow
page_layout: spread_v1
start_date: 2024-11
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - Python
  - AWS MCP
status: ready
---

# SQLite MCP

## tagline

SQLite データベースを AI クライアントから自然言語で操作できる MCP Server です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`mcp-server-sqlite` が `.db` ファイルへの SQL 実行を提供します。コードを書かずに「売上を集計して」と自然言語で指示できます。

## どこで出会うか

「Claude に DB を集計させたい」と思ったとき MCP 公式ドキュメントで紹介されています。`uvx mcp-server-sqlite` の 1 行で使い始められます。

## メイン図

### 図の狙い

AI クライアントが SQLite MCP を経由してローカル `.db` ファイルを操作する流れを示し、「AI に DB を渡す」イメージを具体化します。

### C. 概念図（figure_type: workflow）

- 中心に置く概念: SQLite MCP Server（`.db` ファイルへのゲート役）
- 周辺の要素: AI クライアント（Claude など）／自然言語指示／SQL 変換／`.db` ファイル／結果（表・CSV）
- 関係の描き方: 左から AI クライアント → SQLite MCP → `.db` ファイルへの矢印。read-only モード時は書き込み矢印に × を添える

## 会話での使い方例

「SQLite MCP で集計して CSV に書き出してもらいました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ローカル `.db` ファイルを AI が SQL で操作する窓口。

### 2. うれしさ

自然言語の指示だけでデータ集計やマイグレーションができます。

### 3. 注意点

書き込み操作はバックアップ必須で、read-only モードが安全です。

### 4. どこで役立つか

ローカル在庫 DB や売上ログを AI で即席分析したい場面に向きます。

### 5. はじめに

`.db` ファイルを用意し `uvx` コマンドで起動できれば試せます。

### 6. 深掘り先

MCP Server、MCP、Filesystem MCP

## 開発フローでの位置（必須）

1. DB 準備 — `.db` ファイルを用意し、必要ならコピーを取ります
2. Server 起動 — `mcp-server-sqlite` に DB のパスを渡して起動します
3. クライアント接続 — 設定ファイルにパスを登録して接続します
4. 自然言語で操作 — 「このテーブルを集計して」と指示するだけです
5. 結果確認 — SELECT 結果や変更後のスキーマを AI が返してくれます


## 関連用語

- MCP
- MCP Server
- Python
- AWS MCP


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- SQL と SQLite（SQL ライト）の関係が分かりづらいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: SQL を操作できる MCP なのかな
- 👍 良い点: ローカル完結で DB を叩いてくれて便利そうです
- 👎 ダメな点: PostgreSQL との互換性まわりがハードル
- 👥 誰向けか: ローカル完結の小規模システムを作る人向け
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: AI クライアントが SQLite MCP を介してローカル `.db` を操作する 3 段構造（AI → MCP → DB）
- 登場人物: ノートPC前の人物（「集計して」と話しかけている）
- 吹き出し・心の声: 人物「先月の売上だけ出して」／MCP「SELECT で拾います」
- 中央に置くキーワード/ラベル: SQLite MCP
- Before / After の場合の対比ポイント: （不使用）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: DB ファイルアイコン（コピーマーク付き）
- Step 2 のアイコン/絵柄: ターミナル画面（uvx コマンド）
- Step 3 のアイコン/絵柄: 設定ファイル（json アイコン）
- Step 4 のアイコン/絵柄: チャット吹き出し（自然言語指示）
- 矢印で示す流れの意図: 準備 → 起動 → 接続 → 操作の順序を示す


## コミュニティ補完メモ

- I-1 MCP との住み分け：MCP はプロトコル全体の定義。SQLite MCP は MCP の具体的な実装例（data 操作特化）
- I-2 MCP Server との住み分け：MCP Server は概念・仕組みの説明。SQLite MCP はその具体サーバーの 1 つ
- I-10 Filesystem MCP との住み分け：Filesystem MCP はファイル読み書き全般。SQLite MCP は `.db` ファイル内を SQL で操作する点が異なる
- I-50 AWS MCP との住み分け：AWS MCP はクラウドリソース操作。SQLite MCP はローカル DB 専用
- PostgreSQL や MySQL 向け MCP（postgres / mysql）が公式・コミュニティで存在するが、それらは別エントリ扱い


## 出典メモ

- https://github.com/modelcontextprotocol/servers — checked 2026-04-29
- https://modelcontextprotocol.io/docs — checked 2026-04-29


## 備考

- read-only モードはブリーフ記載の安心材料。起動オプションでの制御なので、正確なフラグ名は公式 README で要確認（時変情報）
- SQLite は Python 標準ライブラリに含まれるため、`mcp-server-sqlite` の Python 実装との相性が自然
- PostgreSQL・MySQL 向けには別 MCP server が存在するが、本エントリのスコープはローカル SQLite のみ
