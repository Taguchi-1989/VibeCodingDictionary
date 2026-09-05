---
id: I-1
title: MCP
title_reading: モデルコンテキストプロトコル
category: mcp
subtype: protocol
experience_level: hands_on
reader_level: 2
importance: B
figure_type: structure
page_layout: spread_v1
start_date: 2024-11
version_status: active
evaluation_date: 2026-09-05
related_terms:
  - MCP Server
  - MCP Client
  - MCP Transport
  - Tool Use
  - Claude Code
status: ready
---

# MCP

## tagline

Model Context Protocol の略。LLM とツールをつなぐ「AI の USB-C」と呼ばれる標準規格です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM とツールを共通方式で接続する規格です。2024 年に Anthropic が提案し、2025 年 12 月に Agentic AI Foundation へ寄贈されました。いまは 1 社が仕様を握らない形です。

## どこで出会うか

Claude Code や Cursor の「拡張カタログ」規格です。1 つ入れるだけで GitHub 操作や社内 DB 連携ができ、MCP 前提のエージェント設計が広がっています。

## メイン図

### 図の狙い

LLM ⇔ MCP Client ⇔ MCP Server ⇔ External Service の 4 段構造を、1 枚の概念図で見せます。「個別連携」から「共通プロトコル」への構造変化が視覚で伝わるようにします。

### C. 概念図（figure_type: structure）

- 中心に置く概念: MCP Protocol（LLM とツールの間に立つ共通規格）
- 周辺の要素（4〜5 個）: LLM（Claude など）／MCP Client（Claude Code など）／MCP Server（GitHub MCP など）／External Service（GitHub 本体）／Transport（通信方式 stdio/SSE/HTTP）
- 関係の描き方: 左に LLM、右に外部サービス、中央に MCP Protocol を太く描く。両側の矢印は MCP Protocol を介して流れる
- Before/After 対比のヒント: 左下に「Before: 個別連携でバラバラ」の小さい概念図、右下に「After: MCP で統一」の概念図を添える

## 会話での使い方例

「Claude Code に MCP を足せば外部ツールに横展開できますね、AI の USB-C なので。」

## この用語の見どころ

### 1. 役割

LLM とツールをつなぐ共通コネクタです。

### 2. うれしさ

一度書けば、MCP 対応のどの LLM からも同じように使えます。

### 3. 注意点

仕様とエコシステムが急成長中で、数ヶ月で状況が変わります。

### 4. どこで役立つか

エージェントのツール拡張、データ連携、社内システムとの橋渡し。

### 5. はじめに

Server／Client／Transport の 3 役と共通コネクタの発想。

### 6. 深掘り先

MCP SDK、各種 MCP（GitHub／Playwright／Notion）、自作 MCP のテンプレ。

## 開発フローでの位置（必須）

1. 欲しい外部連携を見つける — 何のツール・データと繋ぎたいか
2. 既存の MCP があるか探す — 公式／コミュニティ／商用
3. 無ければ自作、あれば設定 — SDK または設定ファイル
4. MCP Client から呼び出して実行 — Claude Code や Cursor の中で使う

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 関連用語

- MCP Server
- MCP Client
- MCP Transport
- Tool Use
- Claude Code

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 何の略で何の役に立つかピンと来ず、「AI の USB-C」もイメージが結びつきません
- Server と Client のどちらが自分側か混乱しやすく、設定時に迷います
- 入れた MCP の安全性（権限・データ漏れ）の判断が難しく、追加に不安を感じます
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 名前のキャッチーさが先行している印象です。
- 👍 良い点: LLM からのソフトウェア操作が容易になります。
- 👎 ダメな点: 入れすぎるとコンテキストを圧迫します。
- 👥 誰向けか: エージェントユースを試したい人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「MCP Protocol」の太い帯。左側に LLM（Claude のロゴ風）＋ MCP Client（Claude Code ターミナル）、右側に MCP Server 群（GitHub／Playwright／Notion）＋ External Service。矢印が MCP Protocol 帯を通って両側を繋ぐ
- 登場人物: LLM 側に開発者キャラクター 1 人、外部サービス側に「つなぎ先」アイコン群
- 吹き出し・心の声: 「MCP があれば、同じやり方でどこにも繋がる」
- 中央に置くキーワード: MCP ＝ LLM とツールの共通コネクタ
- 追加: 左下に小さく「Before: バラバラ連携」／右下に「After: MCP で統一」の対比を添える

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 探索アイコン（欲しい連携を見つける）
- Step 2: カタログアイコン（既存 MCP を探す）
- Step 3: 組み立て or ダウンロードアイコン（自作 or 設定）
- Step 4: 実行アイコン（Client から呼び出し）
- 矢印: 見つける → 探す → 用意する → 呼ぶ

## コミュニティ補完メモ

個別 MCP（I-10 Filesystem、I-11 GitHub、I-20 Playwright、I-30 Notion など）は別エントリで深掘り。本エントリは「プロトコル自体の総論」に絞ります。

## 出典メモ

- Anthropic "Introducing the Model Context Protocol"（2024-11）— checked 2026-04-23
- modelcontextprotocol.io — checked 2026-09-05
- Anthropic "Donating the Model Context Protocol and establishing of the Agentic AI Foundation"（2025-12-09）— checked 2026-09-05
- https://blog.modelcontextprotocol.io/posts/ — checked 2026-09-05

## 備考

MCP の仕様・エコシステムは動きが速いので、evaluation_date を必ず持たせて時変情報として扱います。

2026-09-05 の当て直しで確認した点（2026-04-23 版からの差分）:

- **統治が移りました**。2025-12-09 に Anthropic が MCP を **AAIF（Agentic AI Foundation、Linux Foundation 傘下の directed fund）** へ寄贈。Anthropic・Block・OpenAI が共同創設者で、AWS・Google・Microsoft・Cloudflare・Bloomberg などがプラチナメンバーです。**J-132 A2A も 2026-08 に同じ財団のホストプロジェクトになりました**（2 つのプロトコルが同じ傘の下に並んだ、というのが 2026 年の構図）
- **仕様は 2026-07-28 版が最新**（プロトコル公開以来で最大の更新。プロトコル層のセッション管理を外して stateless 化したため、以前のサーバーとの後方互換が完全ではありません）。誌面ではバージョン番号までは出さず、「1 社が握らない形になった」ところまでに留めています
