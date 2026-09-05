---
id: I-11
title: GitHub MCP
title_reading: ギットハブエムシーピー
category: mcp
subtype: reference
experience_level: hands_on
reader_level: 3
importance: D
figure_type: workflow
page_layout: spread_v1
start_date: 2024-11
version_status: active
pricing_note: none
evaluation_date: 2026-09-05
related_terms:
  - MCP
  - MCP Server
  - GitHub
  - Claude Code
  - Tool Use
status: ready
---

# GitHub MCP

## tagline

GitHub 公式が提供する MCP Server です。AI から Issue・PR・コードを直接操作できます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

MCP Client から GitHub の Issue 作成・PR 作成・コード検索・ブランチ操作を呼び出せる公式 MCP Server です。

## どこで出会うか

「Issue を AI に作らせたい」と調べると出てきます。自分の環境で動かす形と、GitHub がホストする形の 2 通りがあり、設定ファイルに追記すればエージェントが GitHub を操作できます。

## メイン図

### 図の狙い

Claude Code から GitHub MCP を経由して GitHub API にリクエストが流れ、Issue や PR が操作される一連の流れを見せます。「AI が直接 GitHub を動かす」経路を視覚で伝えます。

### C. 概念図（figure_type: workflow）

- 中心に置く概念: GitHub MCP Server（AI と GitHub API の仲介役）
- 周辺の要素（4〜5 個）: Claude Code（MCP Client）／GitHub MCP Server／GitHub API／Issue・PR・コード／ブランチ
- 関係の描き方: 左に Claude Code、中央に GitHub MCP Server、右に GitHub API と操作対象を並べる。矢印は左から右へ流れる

## 会話での使い方例

「GitHub MCP を入れると、Claude Code から PR を直接作れて便利ですね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI から GitHub を操作するための公式 MCP Server です。

### 2. うれしさ

Issue や PR の作成をエージェントに任せられます。

### 3. 注意点

GitHub Token の権限設定を誤ると意図しない操作が起きます。

### 4. どこで役立つか

Issue 整理や PR 作成を自動化したい開発フローで役立ちます。

### 5. はじめに

GitHub Token の取得と MCP 設定ファイルへの追記が出発点です。

### 6. 深掘り先

MCP Server、GitHub API、Tool Use。

## 開発フローでの位置（必須）

1. GitHub Token を取得する — 操作に必要な権限スコープを設定します
2. MCP 設定ファイルに追記する — GitHub MCP Server のエンドポイントを登録します
3. Claude Code から呼び出す — Issue 作成や PR 操作を指示します
4. 結果を GitHub 上で確認する — AI が操作した内容を実際のリポジトリで確かめます

## 関連用語

- MCP
- MCP Server
- GitHub
- Claude Code
- Tool Use

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- アクセストークン取得の手順でつまずきやすく、意味も分かりにくいです。
- たまに接続が切れることがあります。
- トークンに有効期限があり、気づかず失効していることがあります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Claude Code から GitHub 操作を自動でやってくれて便利です。
- 👍 良い点: GitHub へのデータ転送を Claude Code から直接できます。
- 👎 ダメな点: 仕組みの理解は難しく、権限設定には注意が必要です。
- 👥 誰向けか: コーディングをする人全般向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左から「Claude Code（ターミナル画面）」→「GitHub MCP Server（六角形バッジ）」→「GitHub API（クラウドアイコン）」→「Issue / PR / コード（カードアイコン群）」の横並びフロー図
- 登場人物: 左端に開発者キャラクター 1 人。「PR 作って」と吹き出しを出している
- 吹き出し・心の声: 開発者「GitHub に頼まなくていいんだ」／Claude Code「わかりました、PR を作ります」
- 中央に置くキーワード/ラベル: GitHub MCP ＝ AI と GitHub をつなぐ公式仲介役

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 鍵アイコン（Token 取得）
- Step 2 のアイコン/絵柄: 設定ファイルアイコン（追記）
- Step 3 のアイコン/絵柄: ターミナルアイコン（呼び出し）
- Step 4 のアイコン/絵柄: GitHub ロゴ（確認）
- 矢印で示す流れの意図: 準備 → 設定 → 実行 → 確認

## コミュニティ補完メモ

- GitHub 本体（F-60）との住み分け：F-60 は GitHub というサービス全体を扱う。I-11 は GitHub を AI から操作する MCP Server の役割に絞る
- MCP プロトコル全体（I-1）との住み分け：I-1 は「プロトコルの総論」。I-11 は GitHub という具体的な MCP Server の 1 例
- MCP Server 総論（I-2）との住み分け：I-2 は MCP Server の設計・構造。I-11 は GitHub MCP という既製品の使い方
- I-10 Filesystem MCP・I-20 Playwright MCP と兄弟エントリ。3 件とも「具体的 MCP の使い方」として構造を揃えている

## 出典メモ

- github.com/github/github-mcp-server — checked 2026-04-29
- modelcontextprotocol.io/examples — checked 2026-04-29

## 備考

GitHub MCP は GitHub 公式がメンテナンスしており、機能追加が活発です。evaluation_date を必ず持たせて時変情報として扱います。Token の権限スコープは操作内容に応じて最小権限を原則とします。

**2026-09-05 の当て直し**: 現行は `github/github-mcp-server`（GitHub 公式）。Anthropic との協業で **Go に書き直された**もので、**ホスト型（リモート）とローカル（Docker / Go バイナリ）の 2 通り**の使い方があります。一方、MCP の参照サーバー側にあった旧 GitHub server は **2025 年 5 月にアーカイブへ移りました**（I-13 / I-21 / I-41 と同じ整理）。混同しやすいので、指す先は GitHub 公式の方です。出典: <https://github.com/github/github-mcp-server> ／ <https://github.blog/changelog/2025-04-04-github-mcp-server-public-preview/> — checked 2026-09-05
