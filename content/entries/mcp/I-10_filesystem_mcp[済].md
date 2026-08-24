---
id: I-10
title: Filesystem MCP
title_reading: ファイルシステムエムシーピー
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
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - Claude Code
  - Tool Use
  - MCP Client
status: ready
---

# Filesystem MCP

## tagline

LLM がローカルファイルを読み書きするための MCP（Model Context Protocol）実装です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM からの指示でローカルファイルを読む・書く・一覧取得する操作を提供します。MCP 公式サーバー実装で、許可するディレクトリを設定ファイルで限定できます。

## どこで出会うか

MCP の入門例として公式ドキュメントや GitHub に掲載されています。「LLM にローカルファイルを触らせてみたい」と思ったとき、最初に試す MCP として紹介されることが多いです。

## メイン図

### 図の狙い

Claude Code などの MCP Client からの操作が Filesystem MCP を経由してローカルディスクに届く流れを 1 枚で示します。「許可ディレクトリのみ」という制限が視覚で伝わるようにします。

### C. 概念図（figure_type: workflow）

- 中心に置く概念: Filesystem MCP Server（許可ディレクトリのゲート役）
- 周辺の要素: MCP Client（Claude Code）／read ・ write ・ list の 3 操作／許可ディレクトリ（例: ~/projects）／ブロックされる領域（例: /etc、/home 外）
- 関係の描き方: 左から MCP Client → Filesystem MCP → 許可ディレクトリへの矢印、ブロック領域には × を添える

## 会話での使い方例

「Filesystem MCP を入れると、Client からローカルのファイルを直接読み書きできます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM にローカルファイルの読み書き権限を渡す MCP です。

### 2. うれしさ

設定ファイル 1 つでアクセス範囲を絞り、安全に連携できます。

### 3. 注意点

Claude Code は同等機能を内蔵するため、用途が限定されます。

### 4. どこで役立つか

Claude Code 以外の MCP Client でファイル操作を試す場面です。

### 5. はじめに

許可ディレクトリの設定と read / write / list の 3 操作の把握。

### 6. 深掘り先

MCP、MCP Server、GitHub MCP、Playwright MCP。

## 開発フローでの位置（必須）

1. Client を用意する — Claude Code や Cursor などを選びます
2. Filesystem MCP を入れる — npm や公式リポジトリから取得します
3. 許可ディレクトリを設定する — 触れるパスを設定ファイルで指定します
4. LLM から呼び出す — read / write / list でファイルを扱います
5. 結果を確認する — 実際のファイルに反映されたか確かめます

## 関連用語

- MCP
- MCP Server
- Claude Code
- Tool Use
- MCP Client

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 普段目にも耳にもしません
- 自分で構築すべきものなのか分かりません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回はじめて試してみました
- 👍 良い点: Claude Code に任せれば意識せず色々できます
- 👎 ダメな点: 権限設定をミスすると大変です
- 👥 誰向けか: 自作のハーネスを組む人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左に「Claude Code（MCP Client）」のターミナルアイコン、中央に「Filesystem MCP」のゲート役ボックス（鍵マーク付き）、右に「許可ディレクトリ（~/projects）」のフォルダアイコン。ブロックされるパス（/etc など）には × を描く
- 登場人物: 開発者キャラクター 1 人が左で「このファイル読んで」と指示を出している
- 吹き出し・心の声: 「許可ディレクトリ内ならOK、外はブロック」
- 中央に置くキーワード/ラベル: Filesystem MCP ＝ ファイル操作のゲート

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: クライアント選択アイコン（Claude Code ロゴ）
- Step 2 のアイコン/絵柄: ダウンロードアイコン（インストール）
- Step 3 のアイコン/絵柄: 設定ファイルアイコン（鍵付きフォルダ）
- Step 4 のアイコン/絵柄: 操作アイコン（read / write / list の 3 矢印）
- Step 5 のアイコン/絵柄: チェックマーク（確認）
- 矢印で示す流れの意図: 準備 → 設定 → 実行 → 確認の流れ


## コミュニティ補完メモ

- MCP 全体（I-1）との住み分け：I-1 はプロトコルの総論。I-10 は「ファイル操作」という最もシンプルな具体 MCP の紹介に絞る
- MCP Server（I-2）との住み分け：I-2 は MCP Server の概念・仕組み。I-10 は Filesystem MCP という実装例
- GitHub MCP（I-11）・Playwright MCP（I-20）との住み分け：いずれも兄弟エントリ。Filesystem MCP は「ローカルファイル」特化、外部サービスとの連携は他エントリで扱う
- Claude Code との関係：Claude Code は Filesystem MCP と同等のファイル操作機能を内蔵している。Claude Code を使っている場合、Filesystem MCP を別途導入する必要はほぼない。Claude Code 以外の MCP Client を使う場面での活用を注意点として明示した

## 出典メモ

- modelcontextprotocol.io/examples — checked 2026-04-29
- github.com/modelcontextprotocol/servers — checked 2026-04-29

## 備考

Filesystem MCP は MCP の公式サンプル実装の 1 つで、構造がシンプルなため入門リソースとして多く紹介されています。Claude Code ユーザーには重複機能になる点を注意事項として明記しています。evaluation_date つきの時変情報として管理します。
