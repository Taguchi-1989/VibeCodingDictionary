---
id: I-50
title: AWS MCP
title_reading: エーダブリューエスエムシーピー
category: mcp
subtype: cloud
experience_level: hands_on
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2024-12
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - AWS
  - Amazon Bedrock
status: ready
---

# AWS MCP

## tagline

AWS リソースを AI クライアントから操作できる AWS 公式の MCP Server 群です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

AWS 公式の MCP Server 群の総称です。CDK 操作・CloudFormation 検証・Bedrock 検索など用途別に Server が用意されています。

## どこで出会うか

Claude Code など MCP 対応ツールで「インフラ作業を AI に任せたい」場面で登場します。必要な Server だけを個別に起動して使います。

## メイン図

### 図の狙い

MCP を経由して Claude と AWS の各サービスがつながる構造を示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: AWS MCP（MCP Server 群）
- 周辺の要素: Claude Code（MCP Client）/ CDK / CloudFormation / Bedrock KB / S3 / EC2
- 関係の描き方: Claude Code から AWS MCP へ矢印、AWS MCP から各 AWS サービスへ矢印（扇状）


## 会話での使い方例

「AWS MCP で CDK スタックの差分を確認してから本番に流しました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI から AWS リソースを操作・参照するための公式 MCP Server 群。

### 2. うれしさ

CLI を手打ちせず自然言語で CDK 差分確認や S3 設定参照ができます。

### 3. 注意点

本番アカウントへの直接接続は事故の元で、読み取り専用ロールが安全です。

### 4. どこで役立つか

インフラ構築・運用補助と Bedrock RAG 検索のテストに向いています。

### 5. はじめに

必要な Server だけを選び、認証に AWS CLI プロファイルを使う点を確認します。

### 6. 深掘り先

MCP、MCP Server、Amazon Bedrock

## 開発フローでの位置（必須）

1. 認証準備 — 読み取り専用の IAM ロールを認証情報に設定します
2. Server 起動 — 用途別の AWS 用 MCP Server を起動します
3. MCP 登録 — MCP Client の設定に接続先を追加します
4. AI で操作 — 「このスタックの差分を要約して」と自然言語で頼みます
5. 確認・反映 — 出力を確認してから本番に反映し、事故を防ぎます


## 関連用語

- MCP
- MCP Server
- AWS
- Amazon Bedrock


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- AWS 自体の初期設定で、MCP に到達する前につまずきそうです
- AWS のやりたい概念が分からないと、MCP の提案も判断できません
- MCP の前に AWS 自体の学習が必要になりそうです
<!-- user-input:end key="stumble" -->


<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: AI エージェントと対話で要件を詰めれば使えそうです
- 👍 良い点: 画面のポチポチ操作をせずに済みそうです
- 👎 ダメな点: AWS 自体の知識が多少必要になります
- 👥 誰向けか: 企業で AWS 環境を構築する人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Claude Code を操作する人物から AWS MCP を経由して AWS 各サービスへ矢印が伸びる構成図
- 登場人物: ノートPC を操作するエンジニア風の人物（Claude と話しかける吹き出し付き）
- 吹き出し・心の声: 「CDK スタックの差分を見て」→ AWS MCP → 各サービスに扇状にアクセス
- 中央に置くキーワード/ラベル: AWS MCP（awslabs/mcp）
- Before / After の場合の対比ポイント: -

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 鍵マーク（IAM 認証）
- Step 2 のアイコン/絵柄: サーバー起動アイコン
- Step 3 のアイコン/絵柄: プラグイン接続アイコン
- Step 4 のアイコン/絵柄: チャット吹き出し（AI 指示）
- Step 5 のアイコン/絵柄: チェックマーク（確認・反映）
- 矢印で示す流れの意図: 認証 → 起動 → 登録 → 操作 → 確認 の順で事故を防ぐ流れ


## コミュニティ補完メモ

- I-1 MCP との住み分け：MCP は規格の概念解説、AWS MCP は AWS 向け実装の具体例。両者はセットで読むと理解が深まります
- I-2 MCP Server との住み分け：MCP Server は「Server とは何か」の概念エントリ。AWS MCP はその具体例の 1 つで、複数の Server 群を指す集合概念として扱います
- B-30 Amazon Bedrock との住み分け：Bedrock は AI サービス自体の解説、AWS MCP の `bedrock-kb-retrieval-mcp-server` はそこへ MCP でアクセスする手段です
- 用途別 Server（CDK / CloudFormation / Bedrock KB など）が増え続けているため、評価日時点の一覧は出典メモの公式リポジトリを参照してください


## 出典メモ

- <https://github.com/awslabs/mcp> — checked 2026-04-29


## 備考

- 認証は AWS CLI と同様に `~/.aws/credentials` のプロファイルか IAM ロールを利用
- transport は stdio。Server ごとに個別起動が必要（1 コマンド = 1 Server）
- 本番アカウントに直接繋ぐと意図しない変更が起きる可能性があるため、読み取り専用ロールから始めるのが安全
- `awslabs/mcp` は 2024 年 12 月頃から公開が始まったリポジトリで、収録 Server は増加中（時変情報）
