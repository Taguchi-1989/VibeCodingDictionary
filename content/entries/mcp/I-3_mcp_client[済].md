---
id: I-3
title: MCP Client
title_reading: エムシーピークライアント
category: mcp
subtype: protocol
experience_level: hands_on
reader_level: 2
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2024-11
version_status: active
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - Claude Code
  - Cursor
  - Tool Use
status: ready
---

# MCP Client

## tagline

MCP 接続の「呼び出す側」です。LLM を抱えるホストが担う役割です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM を内蔵するアプリが MCP Server に接続するときの「呼び出し口」です。接続の確立・ツール一覧の取得・結果の受け取りをひとまとめに担います。

## どこで出会うか

Claude Code や Cursor など、AI を使うエディタやアプリが代表例です。設定ファイルに MCP Server の情報を書き足すと Client として機能し始めます。

## メイン図

### 図の狙い

「LLM ホスト（Client）が MCP Server を呼び出す」流れを 1 枚で示し、Server と Client の役割分担を視覚的に伝えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: MCP Client（LLM ホスト側の橋渡し役）
- 周辺の要素: LLM（推論）／MCP Client（接続管理）／MCP Server（GitHub, Filesystem 等）／External Service（実データ）
- 関係の描き方: 左に LLM、中央に MCP Client、右に MCP Server 群。左→中央→右と矢印を引き、Client が「呼び出す側」であることを明示

## 会話での使い方例

「Claude Code は MCP Client なので、Server を設定すれば外部ツールと話せます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

MCP Server を呼び出す「LLM ホスト側の接続窓口」です。

### 2. うれしさ

対応アプリに MCP Server を足すだけで、ツール連携が広がります。

### 3. 注意点

Client ごとに対応する MCP Server の範囲が異なることがあります。

### 4. どこで役立つか

エディタや AI アシスタントにツールを追加したいときに機能します。

### 5. はじめに

Claude Code や Cursor が Client の代表例という対応関係です。

### 6. 深掘り先

MCP Server、MCP Transport、Tool Use。

## 開発フローでの位置（必須）

1. ホストアプリを選ぶ — Claude Code や Cursor などを選びます
2. 使いたい Server を探す — 公式カタログで探します
3. 設定ファイルに書く — JSON で接続先を追記します
4. Client が Server に接続する — ツール一覧が自動で認識されます
5. LLM からツールを呼ぶ — 会話の中でツールが動きます

## 関連用語

- MCP
- MCP Server
- Claude Code
- Cursor
- Tool Use

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- クライアントとサーバーの方向が混乱します
- MCP は耳にしますが、Client は聞きなれません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: MCP の概念を AI ニュースで聞きました
- 👍 良い点: 正確に表していて、わかっています
- 👎 ダメな点: 通っぽく気取った感じになります
- 👥 誰向けか: 開発者のサービス連携向けです
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左に「LLM（Claude など）」、中央に「MCP Client」の太い帯、右に「MCP Server 群（GitHub / Filesystem 等）」。Client から Server への矢印を複数引き、「呼び出す側」を強調
- 登場人物: 開発者キャラクター 1 人が MCP Client（エディタ画面）を操作している
- 吹き出し・心の声: 「サーバーに接続するだけで、外のツールが全部使えます。」
- 中央に置くキーワード: MCP Client ＝ LLM ホスト側の接続窓口

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: アプリ選択アイコン（エディタ）
- Step 2 のアイコン/絵柄: 検索アイコン（カタログ）
- Step 3 のアイコン/絵柄: 設定ファイルアイコン（JSON）
- Step 4 のアイコン/絵柄: プラグインアイコン（接続確立）
- Step 5 のアイコン/絵柄: チャットアイコン（ツール呼び出し）
- 矢印で示す流れの意図: 選ぶ → 探す → 設定する → 繋がる → 使う

## コミュニティ補完メモ

- MCP プロトコル全体は I-1 で担当。本エントリは「Client 側の役割」に絞る。
- MCP Server（I-2）との対比が最重要。Server が「提供する側」、Client が「呼び出す側」。
- Claude Code（B-7）・Cursor（B-4）は MCP Client の代表例だが、それぞれのエントリで AI アシスタントとしての全体像を担う。本エントリは「Client という役割」視点で参照する形で住み分け。
- MCP Transport（通信方式）は I-1 または別エントリで詳述予定。本エントリでは言及しない。

## 出典メモ

- modelcontextprotocol.io/specification — checked 2026-04-29
- modelcontextprotocol.io/clients — checked 2026-04-29

## 備考

MCP のエコシステムは急成長中で、対応 Client・Server の一覧は数ヶ月で変化します。evaluation_date を必ず参照してください。
