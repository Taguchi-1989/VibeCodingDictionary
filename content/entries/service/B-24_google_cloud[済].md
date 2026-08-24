---
id: B-24
title: Google Cloud
title_reading: グーグルクラウド
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
  - Vertex AI
  - BigQuery
  - Cloud Run
  - AWS
  - Firebase
status: ready
---

# Google Cloud

## tagline

GCP（Google Cloud Platform）とも呼ばれる Google のクラウド基盤です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Compute Engine・Cloud Run・BigQuery・Vertex AI など、仮想サーバーからデータ分析・AI まで一式をクラウドで提供します。

## どこで出会うか

開発チームから「GCS にファイルを置いています」「BigQuery でログを見ています」と聞くときが最初の接点になりがちです。AI 機能の話題では Vertex AI の名前が出ます。

## メイン図

### 図の狙い

Google Cloud という傘の下に主要サービスが並ぶ構造を示し、「どのサービスが何をしているか」を 1 枚で掴めるようにします。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Google Cloud
- 周辺の要素: Compute Engine（仮想サーバー）／Cloud Run（コンテナ実行）／BigQuery（大規模データ分析）／Vertex AI（AI プラットフォーム）／Cloud Storage（ストレージ）
- 関係の描き方: 中央に Google Cloud ロゴ、4〜5 方向に各サービスが枝として伸びる。非エンジニアの担当者が「うちのデータはここにあるのか」と眺めている構図


## 会話での使い方例

「分析用データは BigQuery に置いているので、Google Cloud から確認できます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Google のインフラとサービスをクラウドで提供する基盤です。

### 2. うれしさ

BigQuery によるデータ分析の強さが独自の強みです。

### 3. 注意点

サービスの種類が多く、選択と料金の把握に慣れが必要です。

### 4. どこで役立つか

データ分析や AI 機能を組み込む開発に向いています。

### 5. はじめに

Cloud Storage・BigQuery・Vertex AI の 3 つが入口です。

### 6. 深掘り先

Vertex AI、BigQuery、AWS。

## 開発フローでの位置（必須）

1. インフラ設計 — Google Cloud の中から必要なサービスを選定します
2. 環境構築 — Cloud Run や Compute Engine を立ち上げ、Cloud Storage に置き場を作ります
3. アプリデプロイ — コードを Google Cloud 上に載せて公開できる状態にします
4. AI 機能の追加 — Vertex AI 経由でモデルを呼び出しアプリに組み込みます

## 関連用語

- Vertex AI
- BigQuery
- Cloud Run
- AWS
- Firebase


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- GCP という名前が分かりにくく、データの流れや安全な使い方が掴みにくいです。
- Vertex AI も実例はあっても自分で使うときの手順が分かりにくいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: API 経由で Gemini を安全に使えるなら助かるな、という印象です
- 👍 良い点: セキュアに使える前提が整っているとされています
- 👎 ダメな点: 手順が分かりにくく、他社 API との併用も面倒な場面があります。
- 👥 誰向けか: API でセキュアに開発したい人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Google Cloud」のロゴノード。四方向に枝が伸び、Compute Engine（サーバーアイコン）・Cloud Run（コンテナアイコン）・BigQuery（データベースアイコン）・Vertex AI（脳／AI アイコン）・Cloud Storage（バケットアイコン）が並ぶ
- 登場人物: 非エンジニアの担当者（ノート PC を持って Google Cloud コンソールを眺める人）
- 吹き出し・心の声: 「うちのデータはここにあるのか…」「BigQuery ってこれか」
- 中央に置くキーワード/ラベル: Google Cloud ＝ クラウドの傘

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設計図アイコン — インフラ設計
- Step 2 のアイコン/絵柄: サーバー＋バケットアイコン — 環境構築
- Step 3 のアイコン/絵柄: ロケット／デプロイアイコン — アプリデプロイ
- Step 4 のアイコン/絵柄: 脳／AI アイコン＋矢印 — Vertex AI で AI 追加
- 矢印で示す流れの意図: 設計 → 構築 → デプロイ → AI 追加 の開発の進行


## コミュニティ補完メモ

- Vertex AI（B-27）は Google Cloud の AI／ML プラットフォームとして別エントリで扱います。本エントリは「Google Cloud 全体の傘と代表サービス」に絞ります
- Firebase は別エントリ候補。モバイル／Web 開発向けの BaaS として独立した位置づけです
- AWS（B-23）・Azure（B-25）との対比は各エントリに任せ、本エントリでは「3 大クラウドの一角」という言及にとどめます
- BigQuery によるデータ分析の強みが AWS・Azure との独自色。本文にはその一点だけ言及します
- GCP は旧称。現在の正式表記は「Google Cloud」で、本書もそれに従います


## 出典メモ

- <https://cloud.google.com> — checked 2026-04-29
- <https://cloud.google.com/products> — checked 2026-04-29


## 備考

- モデル・料金・提供状況は時変情報です。evaluation_date: 2026-04-29 を持たせます
- experience_level: research_only（著者はインフラ管理者ではなく、利用側の立場）
- GCP は Google Cloud Platform の略称。本書では「Google Cloud」を正式表記として使用します
