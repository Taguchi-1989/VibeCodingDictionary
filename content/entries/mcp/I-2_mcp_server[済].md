---
id: I-2
title: MCP Server
title_reading: エムシーピーサーバー
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
  - MCP Client
  - Tool Use
  - Filesystem MCP
  - GitHub MCP
status: ready
---

# MCP Server

## tagline

ツールやデータを LLM に提供する「橋の向こう側」の役割です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Client のリクエストを受け、外部サービスやファイルシステムを操作して結果を返します。GitHub・Slack など連携先ごとに 1 つ用意され、LLM は Server を呼ぶだけで個別実装を意識しません。

## どこで出会うか

`claude_desktop_config.json` などで MCP Server を登録するときに登場します。目的ごとに個別の Server（Filesystem MCP・GitHub MCP 等）が存在します。

## メイン図

### 図の狙い

MCP Client ⇔ MCP Server ⇔ External Service の 3 層構造を見せ、Server が「橋渡し役」として中央に立つことを伝えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: MCP Server（橋渡し役）
- 周辺の要素: MCP Client（Claude Code など）／External Service（GitHub, Filesystem, Slack）／MCP Protocol（通信規格）／Tool（操作できる機能）
- 関係の描き方: 左に MCP Client、右に External Service 群を並べ、中央の MCP Server が両者を仲介する矢印で繋ぐ

## 会話での使い方例

「GitHub MCP も MCP Server の一種で、Client から呼ぶだけで PR 操作ができます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Client のリクエストを受け、外部サービスを操作して返す橋渡し役。

### 2. うれしさ

1 つ用意すれば MCP 対応のどの Client からも呼び出せます。

### 3. 注意点

ローカル動作とリモート動作で信頼範囲が変わります。

### 4. どこで役立つか

ファイル操作・API 連携・DB 参照を LLM に渡したい場面。

### 5. はじめに

「Client を受け外部に繋ぐ橋渡し役」の 1 点が理解の核心です。

### 6. 深掘り先

MCP Client、Filesystem MCP、GitHub MCP、MCP Transport

## 開発フローでの位置（必須）

1. 連携先を決める — GitHub や Slack など、つなぎたいサービスを選びます
2. 対応する Server を探す — 公式やコミュニティのカタログで探します
3. 設定ファイルに登録する — Server の起動方法を書きます
4. Client から呼び出す — Client が Server に Tool 要求を送ります
5. 結果が LLM に返る — 処理結果が Client 経由で LLM に渡ります

## 関連用語

- MCP
- MCP Client
- Tool Use
- Filesystem MCP
- GitHub MCP

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 具体例がどちらか分かりにくいです。ユーザー側ではなくサービス側でしょうか。
- 似たような単語が多くて辛いです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: キャッチーな感じです。
- 👍 良い点: LLM のエージェントユースが捗り、精度が上がります。
- 👎 ダメな点: セキュリティ的に危ないものもあります。
- 👥 誰向けか: エージェントユース向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左に「MCP Client（Claude Code）」の端末アイコン、中央に「MCP Server」の大きめブロック（橋の欄干風）、右に External Service 群（GitHub・Filesystem・Slack のアイコン）を並べ、双方向の矢印で繋ぐ
- 登場人物: 左側に開発者キャラクター 1 人（「呼ぶ側」）、右側に「データ持ってる側」のサーバーアイコン
- 吹き出し・心の声: 「MCP Server が橋渡しするから、LLM は外部を直接知らなくていい」
- 中央に置くキーワード/ラベル: MCP Server ＝ ツール・データを提供する橋渡し役

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 外部サービス選択（チェックアイコン）
- Step 2 のアイコン/絵柄: カタログ検索（虫眼鏡）
- Step 3 のアイコン/絵柄: 設定ファイル（歯車 or ファイルアイコン）
- Step 4 のアイコン/絵柄: 呼び出し矢印（Client → Server）
- Step 5 のアイコン/絵柄: 結果が返る矢印（Server → LLM）

## コミュニティ補完メモ

- MCP プロトコル全体（I-1）との住み分け：I-1 はプロトコルの総論。I-2 は「提供する側（Server）」の役割に絞る。
- MCP Client（I-3）との対比：Client が「呼ぶ側」、Server が「応える側」。セットで読むと理解が深まる。
- 個別 Server（I-10 Filesystem MCP / I-11 GitHub MCP / I-20 Playwright MCP）：具体的な実装例として参照。本エントリでは「Server とは何か」の構造説明に集中する。
- OpenAPI との類比：Server が外部に公開する Tool 定義は OpenAPI の operationId に近い発想。エンジニア向けの補足として備考に記載。

## 出典メモ

- modelcontextprotocol.io/specification — checked 2026-04-29
- anthropic.com/news/model-context-protocol — checked 2026-04-29

## 備考

- MCP Server はローカル（stdio 通信）とリモート（SSE / HTTP 通信）の両方の動作モードがあります。ローカルは開発機内のみで動き、リモートは外部ホスト上に置けます。信頼範囲が変わるため注意点として 3. に記載しました。
- OpenAPI に近い役割という観点は本文には入れず、エンジニア向け補足としてここに留めています。
- MCP エコシステムは急成長中。evaluation_date を更新しながら追跡が必要です。
