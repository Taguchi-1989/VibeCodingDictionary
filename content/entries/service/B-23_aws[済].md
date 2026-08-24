---
id: B-23
title: AWS
title_reading: アマゾンウェブサービス
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
  - EC2
  - S3
  - Lambda
  - Amazon Bedrock
  - Google Cloud
status: ready
---

# AWS

## tagline

Amazon Web Services の略。EC2・S3・Lambda など多数のサービスを傘下に持つクラウド基盤です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

EC2・S3・Lambda などのインフラをクラウドで提供します。AI モデル呼び出しには Amazon Bedrock を使います。

## どこで出会うか

サービスの裏側で動いていることが多く、設定画面や請求書で「AWS」の文字を目にします。開発チームから「デプロイ先は AWS」「S3 に置いています」と聞いたときが最初の接触点です。

## メイン図

### 図の狙い

AWS という傘の下に EC2・S3・Lambda・Bedrock が並ぶ構造を示し、「どのサービスが何をしているか」を 1 枚で掴めるようにします。

### C. 概念図（figure_type: structure）

- 中心に置く概念: AWS（Amazon Web Services）
- 周辺の要素: EC2（仮想サーバー）／S3（ストレージ）／Lambda（サーバーレス実行）／Amazon Bedrock（AI モデル呼び出し）／RDS（データベース）
- 関係の描き方: 中央に AWS ロゴ、4 方向に各サービスが枝として伸びる。非エンジニアの担当者が「うちのサービスの裏側」を見ている構図


## 会話での使い方例

「本番環境は AWS の EC2 で動いているので、S3 のバケット権限も確認しておきます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

クラウド上でインフラを一式提供するサービス群です。

### 2. うれしさ

初期設備投資なしに、必要なときだけリソースを使えます。

### 3. 注意点

サービスが多く、どれを使うか選択に迷うことがあります。

### 4. どこで役立つか

Web サービスの構築・ファイル管理・AI 組み込みに使えます。

### 5. はじめに

EC2・S3・Lambda の 3 つが入口として理解しやすいです。

### 6. 深掘り先

Amazon Bedrock、Google Cloud、Azure。

## 開発フローでの位置（必須）

1. インフラ設計 — AWS の中から必要なサービスを選定します
2. 環境構築 — EC2 や Lambda を立ち上げ、S3 に置き場を作ります
3. アプリデプロイ — コードを AWS 上に載せて公開できる状態にします
4. AI 機能の追加 — Bedrock 経由でモデルを呼び出しアプリに組み込みます

## 関連用語

- EC2
- S3
- Lambda
- Amazon Bedrock
- Google Cloud


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- カード登録でエラーが出やすく、会員登録の画面が混み入っています
- 200 ドル無料枠はアカウント紐づけで、放置アカウントだと再取得しにくいです
- EC2・S3・Lambda は名前から中身が想像しづらく、辞書なしでは判別できません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 「クラウドといえばここ」という印象で、何でもできそうに見えました
- 👍 良い点: 幅が広く、LLM に設定を任せられます。閉域網で守れる点も心強いです
- 👎 ダメな点: 使い方によっては料金が嵩み、コスト感が読めない不安があります
- 👥 誰向けか: 企業システムを本格的に組む人向け。無骨な命名に慣れる人向きです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「AWS」のロゴノード。四方向に枝が伸び、EC2（サーバーのアイコン）・S3（バケットアイコン）・Lambda（稲妻アイコン）・Bedrock（脳／AI アイコン）が並ぶ。手前に非エンジニアの担当者が「これがうちのサービスを動かしてるのか…」と眺めている構図
- 登場人物: 非エンジニアの担当者（ノート PC を持って AWS コンソールを眺める人）
- 吹き出し・心の声: 「これがうちのサービスの裏側か…」「EC2 ってサーバーのことか」
- 中央に置くキーワード/ラベル: AWS ＝ クラウドの傘

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設計図アイコン — インフラ設計
- Step 2 のアイコン/絵柄: サーバー＋バケットアイコン — 環境構築
- Step 3 のアイコン/絵柄: ロケット／デプロイアイコン — アプリデプロイ
- Step 4 のアイコン/絵柄: 脳／AI アイコン＋矢印 — Bedrock で AI 追加
- 矢印で示す流れの意図: 設計 → 構築 → デプロイ → AI 追加 の開発の進行


## コミュニティ補完メモ

- Amazon Bedrock（AI モデルの呼び出し）は B-30 で個別に扱います。本エントリは「AWS 全体の傘と代表サービス」に絞ります
- Google Cloud（B-24）・Azure（B-25）との対比は各エントリに任せ、本エントリでは言及を最小限にします
- EC2・S3・Lambda の詳細仕様は本エントリのスコープ外。「何をするサービスか」の一言紹介に留めます
- 料金体系は複雑なため本文に入れず、pricing_note: paid の明示に留めます


## 出典メモ

- https://aws.amazon.com — checked 2026-04-29
- https://aws.amazon.com/what-is-aws/ — checked 2026-04-29


## 備考

- モデル・料金・提供状況は時変情報です。evaluation_date: 2026-04-29 を持たせます
- AWS は experience_level: research_only（著者はインフラ管理者ではなく、利用側の立場）
- 略称 AWS は Amazon Web Services の頭字語。title_reading には「英単語をカタカナで並べた読み」として アマゾンウェブサービス を入れています（2026-04-29）
