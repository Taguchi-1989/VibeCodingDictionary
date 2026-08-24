---
id: B-25
title: Azure
title_reading: マイクロソフトアジュール
category: service
subtype: hosting_cloud
experience_level: research_only
reader_level: 2-3
importance: B
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-29
related_terms:
  - AWS
  - Google Cloud
  - Azure OpenAI
  - Microsoft 365
  - App Service
status: ready
---

# Azure

## tagline

Microsoft Azure の略称。VM や App Service など多数のサービスを束ねるクラウド基盤です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

VM（仮想マシン）・App Service（Web アプリ）・Functions（サーバーレス）など、インフラをクラウドで提供します。AI モデルの呼び出しには Azure OpenAI を使います。

## どこで出会うか

Microsoft 365・Active Directory と統合しやすく、同製品が多い企業で選ばれます。開発チームから「App Service に載せています」と聞いたときが接触点です。

## メイン図

### 図の狙い

Azure という傘の下に VM・App Service・Functions・Azure OpenAI が並ぶ構造を示し、「どのサービスが何をしているか」を 1 枚で掴めるようにします。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Azure（Microsoft Azure）
- 周辺の要素: VM（仮想サーバー）／App Service（Web アプリ実行）／Functions（サーバーレス実行）／Azure OpenAI（AI モデル呼び出し）／Cosmos DB（データベース）
- 関係の描き方: 中央に Azure ロゴ、4 方向に各サービスが枝として伸びる。非エンジニアの担当者が「うちのサービスの裏側」を見ている構図


## 会話での使い方例

「App Service で動いているので、Azure OpenAI の設定も確認しておきます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

クラウド上でインフラを一式提供するサービス群です。

### 2. うれしさ

Microsoft 365 や Active Directory との連携が得意です。

### 3. 注意点

サービスが多く、どれを選ぶか迷うことがあります。

### 4. どこで役立つか

Web 運用・AI 組み込み・企業認証基盤に使えます。

### 5. はじめに

VM・App Service・Functions の 3 つが入口です。

### 6. 深掘り先

Azure OpenAI、AWS、Google Cloud。

## 開発フローでの位置（必須）

1. インフラ設計 — Azure の中から必要なサービスを選定します
2. 環境構築 — VM や App Service を立ち上げ、Cosmos DB に置き場を作ります
3. アプリデプロイ — コードを Azure 上に載せて公開できる状態にします
4. AI 機能の追加 — Azure OpenAI 経由でモデルを呼び出しアプリに組み込みます

## 関連用語

- AWS
- Google Cloud
- Azure OpenAI
- Microsoft 365
- App Service


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「Azure というクラウド上で動いている」という前提を共有できておらず会話で躓きやすいです。読み方「アジュール」も初見には伝わりにくいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Microsoft エコシステムに統合されている点が良さそうと感じました。
- 👍 良い点: クラウドとして出来は悪くなく、評価も上がってきています。
- 👎 ダメな点: ChatGPT MCP と Microsoft MCP がコンフリクトするなど組み合わせの見極めが大変です。
- 👥 誰向けか: 業務で Microsoft ソフトを使っている人は押さえておくと良いです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Azure」のロゴノード。四方向に枝が伸び、VM（サーバーアイコン）・App Service（Web アイコン）・Functions（稲妻アイコン）・Azure OpenAI（脳／AI アイコン）が並ぶ。手前に非エンジニアの担当者が「これがうちの会社のシステムか…」と眺めている構図
- 登場人物: 非エンジニアの担当者（ノート PC を持って Azure ポータルを眺める人）
- 吹き出し・心の声: 「これがうちのサービスの裏側か…」「Microsoft のだから設定がつながってる」
- 中央に置くキーワード/ラベル: Azure ＝ クラウドの傘

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設計図アイコン — インフラ設計
- Step 2 のアイコン/絵柄: サーバー＋DB アイコン — 環境構築
- Step 3 のアイコン/絵柄: ロケット／デプロイアイコン — アプリデプロイ
- Step 4 のアイコン/絵柄: 脳／AI アイコン＋矢印 — Azure OpenAI で AI 追加
- 矢印で示す流れの意図: 設計 → 構築 → デプロイ → AI 追加 の開発の進行


## コミュニティ補完メモ

- Azure OpenAI（AI モデルの呼び出し）は B-26 で個別に扱います。本エントリは「Azure 全体の傘と代表サービス」に絞ります
- AWS（B-23）・Google Cloud（B-24）との対比は各エントリに任せ、本エントリでは言及を最小限にします
- Microsoft 365 との統合は Azure の独自色として 1 文だけ「どこで出会うか」で触れ、詳細は本エントリのスコープ外とします
- Microsoft AI（C-8）・Microsoft Copilot（B-15）との住み分け: Azure はインフラ基盤、Copilot は AI アシスタント体験、Azure OpenAI は企業向けモデル API と役割が異なります
- AKS（Azure Kubernetes Service）・Cosmos DB・Active Directory 連携などの詳細は本文に入れず、誌面ポンチ絵の補足候補として備考に保存します

## 出典メモ

- [azure.microsoft.com](https://azure.microsoft.com) — checked 2026-04-29
- [azure.microsoft.com/ja-jp/overview/](https://azure.microsoft.com/ja-jp/overview/) — checked 2026-04-29


## 備考

- モデル・料金・提供状況は時変情報です。evaluation_date: 2026-04-29 を持たせます
- Azure は experience_level: research_only（著者はインフラ管理者ではなく、利用側の立場）
- 正式名称は Microsoft Azure。略称「Azure」が一般的。title_reading には「英単語をカタカナで並べた読み」としてマイクロソフトアジュールを入れています（2026-04-29）
- 3 大クラウド（AWS・Azure・Google Cloud）の一角として位置づけ、エンタープライズ・Microsoft 製品ユーザー層に強みを持つ点が B-23 / B-24 との差分
