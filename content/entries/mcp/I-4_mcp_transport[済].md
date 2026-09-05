---
id: I-4
title: MCP Transport
title_reading: エムシーピートランスポート
category: mcp
subtype: protocol
experience_level: partial
reader_level: 3-4
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-09-05
related_terms:
  - MCP
  - MCP Server
  - MCP Client
  - MCP SDK
status: ready
---

# MCP Transport

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

AI クライアントと MCP Server をつなぐ通信路の規格。stdio と HTTP の 2 系統が基本です。

## 何をしてくれるか

クライアントとサーバがメッセージをやり取りする経路を定めた仕組みです。ローカルには stdio、リモートには Streamable HTTP を使います。旧来の HTTP+SSE は非推奨になりました。

## どこで出会うか

設定ファイルに MCP Server を追加するとき、`command`（stdio）か `url`（HTTP）かで Transport が決まります。動かないときの最初の切り分けポイントです。

## メイン図

### 図の狙い

stdio（ローカル子プロセス起動）と HTTP（リモート接続）の 2 系統を並べて、どちらをいつ選ぶかが一目でわかるようにする。

### B. 登場シーン（figure_type: comparison）

- シーン1: ローカル MCP — `node` や `uvx` でプロセスを起動、stdio で JSON-RPC をやり取り
- シーン2: リモート MCP — クラウドサービスが提供する URL に Streamable HTTP で接続
- 並べる基準: ローカル vs リモートの Transport 選択軸

## 会話での使い方例

「この MCP Server は stdio なので、ローカルで `node` を起動しないと動きません。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Client・サーバ間の通信経路を stdio / HTTP の 2 系統から選ぶ仕組み。

### 2. うれしさ

Transport を把握すると MCP Server が動かない原因を素早く切り分けられます。

### 3. 注意点

stdio 専用サーバに HTTP の URL を設定しても接続できません。

### 4. どこで役立つか

MCP Server 導入時の設定記述形式を選ぶ場面。

### 5. はじめに

stdio＝ローカル起動、HTTP＝リモート URL 接続の 2 区分が要点。

### 6. 深掘り先

MCP Server、JSON-RPC、Streamable HTTP

## 開発フローでの位置（必須）

1. Server を選ぶ — stdio 専用か HTTP 対応かを確認します
2. 設定ファイルに書く — stdio なら `command`、HTTP なら `url` を書きます
3. クライアントが起動する — stdio では子プロセスとして立ち上げます
4. 通信が始まる — JSON-RPC が選んだ Transport を流れます
5. つまずいたら確認する — 種別の取り違えがないか設定を見直します

## 関連用語

- MCP
- MCP Server
- MCP Client
- MCP SDK


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- エージェントがやってくれると特に意識することはありません
- 切り分けに使うところまでいかず、チャットで聞いて従うことになりそうです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回初めてです
- 👍 良い点: MCP の解像度が上がります
- 👎 ダメな点: 二系統の理解が難しいです
- 👥 誰向けか: 開発者向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左列に stdio（ローカル）、右列に Streamable HTTP（リモート）の 2 系統を並べた比較図
- 登場人物: 開発者が設定ファイルを見ながら「どっちで動くんだ？」と首をかしげている
- 吹き出し・心の声: 左「node で起動 → stdio 接続」、右「URL 貼るだけ → HTTP 接続」
- 中央に置くキーワード/ラベル: Transport

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: サーバのアイコン（種類確認）
- Step 2 のアイコン/絵柄: 設定ファイル・鉛筆
- Step 3 のアイコン/絵柄: コンピューター・起動矢印
- Step 4 のアイコン/絵柄: 双方向矢印（通信）
- 矢印で示す流れの意図: 選択 → 設定 → 起動 → 通信の一連の流れ


## コミュニティ補完メモ

- I-1 MCP との住み分け：MCP はプロトコル全体。本エントリは通信路の種別に絞ったスコープ
- I-2 MCP Server との住み分け：サーバ側の機能・設定方法は I-2 へ。本エントリは「どの Transport を使うか」の選択と設定記述に絞る
- I-3 MCP Client との住み分け：クライアント側の実装詳細は I-3 へ

## 出典メモ

- <https://modelcontextprotocol.io/docs/concepts/transports> — checked 2026-09-05
- <https://docs.anthropic.com/en/docs/claude-code/mcp> — checked 2026-04-29

## 備考

- **2026-09-05 の当て直し**: Streamable HTTP は「策定が進んでいる後継」ではなく、**すでに現行の標準**です。旧 HTTP+SSE は **2025-03-26 の仕様で非推奨**になり、後方互換のための猶予も **2026-06-30 で終了**しました。新規に HTTP+SSE のサーバーを作る理由はもうありません
- 2026-07-28 の仕様更新でプロトコル層のセッション管理が外れ、stateless 化しました。誌面では細部に踏み込まず「ローカルは stdio、リモートは Streamable HTTP」の 2 択に絞っています
- stdio 専用サーバと HTTP 対応サーバを混在させた設定は可能（設定ファイル内で複数エントリを持てる）
