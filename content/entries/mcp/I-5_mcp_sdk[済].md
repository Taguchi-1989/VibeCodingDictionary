---
id: I-5
title: MCP SDK
title_reading: エムシーピーエスディーケー
category: mcp
subtype: protocol
experience_level: hands_on
reader_level: 4-5
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
  - MCP Client
  - 自作 MCP
status: ready
---

# MCP SDK

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

MCP サーバ・クライアントを自作するための公式開発キットです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

MCP サーバ／クライアントを実装するとき、JSON-RPC 通信とライフサイクル管理を SDK が担います。Tool・Resource・Prompt の各機能は register 関数で宣言するだけで動きます。

## どこで出会うか

社内 API を Claude から呼びたい場面や自作 MCP（I-80）を書く場面で登場します。TypeScript 版・Python 版それぞれに公式サンプルが揃っています。

## メイン図

### 図の狙い

SDK が担う通信レイヤと、開発者が宣言するだけでよいサーバ機能の関係を示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: MCP SDK
- 周辺の要素（3〜6個）: Tool 登録 / Resource 登録 / Prompt 登録 / JSON-RPC 処理 / ライフサイクル管理
- 関係の描き方（矢印・包含）: SDK が通信を内包し、開発者の宣言を受け取る矢印で示す


## 会話での使い方例

「社内 API を MCP 化したいなら、Python SDK のサンプルから始めるのが一番早いです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

MCP サーバ・クライアント自作の基盤ライブラリです。

### 2. うれしさ

通信処理を書かずに Tool 登録だけに集中できます。

### 3. 注意点

MCP の概念を先に把握しないと初期設定で詰まりやすいです。

### 4. どこで役立つか

組織内 API や DB を LLM に繋ぐ自作サーバを作る場面です。

### 5. はじめに

TypeScript か Python を選び、公式サンプルで tools/list を動かします。

### 6. 深掘り先

MCP Server（I-2）、MCP Client（I-3）、自作 MCP（I-80）

## 開発フローでの位置（必須）

1. 概念把握 — MCP（I-1）でサーバとクライアントの関係を理解します
2. SDK 導入 — TypeScript か Python の SDK を入れます
3. Tool 宣言 — 呼び出せる関数を登録します
4. 動作確認 — tools/list でツールが認識されたか見ます
5. 接続テスト — MCP Client（I-3）から tools/call を発行して確かめます


## 関連用語

- MCP
- MCP Server
- MCP Client
- 自作 MCP

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- SDK というものに馴染みがありません
- ユーザー側が意識することは少ないです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:社内システムに応答させるのに使えそうです
- 👍 良い点:自作のロジックを公開できます
- 👎 ダメな点:リテラシーがないと概念すら厳しいです
- 👥 誰向けか:社内サービスを AI に代行させたい開発者向け
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「MCP SDK」のボックスを置き、上から「Tool 登録」「Resource 登録」「Prompt 登録」の 3 つが矢印で流れ込む。SDK の下からは「JSON-RPC」「ライフサイクル管理」が伸びてサーバ・クライアント間の通信を担う
- 登場人物: 開発者（エンジニア）が SDK に向かってコードを書いている姿
- 吹き出し・心の声: 「JSON-RPC はお任せ！あとは Tool を登録するだけです」
- 中央に置くキーワード/ラベル: MCP SDK

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 本（概念把握）
- Step 2 のアイコン/絵柄: ターミナル（パッケージ導入）
- Step 3 のアイコン/絵柄: コードエディタ（Tool 宣言）
- Step 4 のアイコン/絵柄: チェックマーク（動作確認）
- 矢印で示す流れの意図: SDK 導入からサーバ公開までの一連の手順

## コミュニティ補完メモ

- MCP（I-1）との住み分け：I-1 は概念・規格の説明。I-5 は「実際に実装するとき使うライブラリ」の話
- MCP Server（I-2）との住み分け：I-2 はサーバの役割・動き方の概念。I-5 はそのサーバを作る道具
- 自作 MCP（I-80）との住み分け：I-80 は自作する理由・ユースケース中心。I-5 は実装手段の説明

## 出典メモ

- [MCP Tools ドキュメント](https://modelcontextprotocol.io/docs/concepts/tools) — checked 2026-04-29
- [Python SDK（GitHub）](https://github.com/modelcontextprotocol/python-sdk) — checked 2026-04-29
- [TypeScript SDK（GitHub）](https://github.com/modelcontextprotocol/typescript-sdk) — checked 2026-04-29


## 備考

- TypeScript SDK パッケージ名：`@modelcontextprotocol/sdk`（npm）
- Python SDK パッケージ名：`mcp`（PyPI）
- ライフサイクルの 3 フェーズ：initialize / tools/list / tools/call
- サーバが提供できる機能種別：Tool・Resource・Prompt の 3 種類
