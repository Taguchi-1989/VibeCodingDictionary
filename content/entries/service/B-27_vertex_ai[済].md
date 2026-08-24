---
id: B-27
title: Vertex AI
title_reading: バーテックス エーアイ
category: service
subtype: managed_ai
experience_level: partial
reader_level: 3-4
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2021-05-18
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-30
related_terms:
  - Google Cloud
  - Gemini
  - Azure OpenAI
  - Amazon Bedrock
status: ready
---

# Vertex AI

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

Google Cloud（B-24）の AI・機械学習向けフルマネージドプラットフォームです。

## 何をしてくれるか

Gemini や Llama・Claude などのモデルを API で呼び出せます。Model Garden でモデルを選び、Vertex AI Studio でプロンプトを試作してそのまま本番 API に接続できます。

## どこで出会うか

業務システムに AI を組み込む場面で、Google Cloud を使う組織の選択肢として登場します。BigQuery や Cloud Storage と直接つながり、データ基盤が Google Cloud にある場合に選ばれます。

## メイン図

### 図の狙い

Vertex AI がモデルの「選ぶ・試す・使う」3 ステップを 1 プラットフォームで完結させる構造を示す。

### B. 登場シーン（figure_type: structure）

- シーン1: エンジニアが Model Garden で Gemini と Claude を並べて精度比較する
- シーン2: プロダクトマネージャーが Vertex AI Studio でプロンプトを試作し、API に昇格させる
- シーン3: データエンジニアが BigQuery のデータを Vertex AI Pipelines に流して推論バッチを動かす
- 並べる基準: 職種別の利用シーン

## 会話での使い方例

「Vertex AI で Gemini と Claude を切り替えて精度比較しました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Google Cloud 上で AI モデルを選定・試作・運用する基盤です。

### 2. うれしさ

複数モデルを 1 画面で比較し、同じ API 形式で切り替えられます。

### 3. 注意点

個人向け Google AI Studio と混同しやすく、用途と料金が異なります。

### 4. どこで役立つか

Google データ基盤を持つ企業が AI を業務に組み込む場面に向きます。

### 5. はじめに

個人向け Google AI Studio との違い（本番サービス）を押さえます。

### 6. 深掘り先

Model Garden、Vertex AI Studio、BigQuery ML

## 開発フローでの位置（必須）

1. 要件整理 — AI に任せるタスクと必要なデータを洗い出す
2. モデル選定 — Model Garden で候補モデルを比較・試作する
3. プロンプト調整 — Vertex AI Studio で入出力を繰り返し確認する
4. API 接続 — 本番システムから Vertex AI のエンドポイントを呼び出す
5. 監視・更新 — Pipelines でバッチ実行を管理しモデルを差し替える


## 関連用語

- Google Cloud
- Gemini
- Azure OpenAI
- Amazon Bedrock


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- ビッグデータ文脈で知りましたが、今は Gemini の GCP ルートが主戦場で「難しい人向け」のイメージが強いです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: ビッグデータ解析の記事で初めて見ました。
- 👍 良い点: クラウドで重い計算を回せてローカルマシンを軽くできます。
- 👎 ダメな点: 契約形態・機密管理・社内規約の整理まで必要で運用設計が重いです。
- 👥 誰向けか: Google 基盤でビッグデータ解析を活用したい人向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Vertex AI を中心に、左から「モデル群（Gemini / Claude / Llama）」、上に「Model Garden（選ぶ）」、右に「Vertex AI Studio（試す）」、下に「BigQuery / API エンドポイント（使う）」が放射状に配置された構造図
- 登場人物: 企業のエンジニアが画面を指差している様子、背後に Google Cloud のロゴ入りサーバー棚
- 吹き出し・心の声: 「どのモデルが合うか、ここで全部試せます」
- 中央に置くキーワード/ラベル: Vertex AI

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: クリップボードに要件メモを書く人
- Step 2 のアイコン/絵柄: モデルカードを並べて比較する画面
- Step 3 のアイコン/絵柄: プロンプト入力ボックスと出力結果
- Step 4 のアイコン/絵柄: API の矢印がシステムに刺さる図
- Step 5 のアイコン/絵柄: パイプライン監視ダッシュボード


## コミュニティ補完メモ

- Azure OpenAI（B-26）との住み分け：Azure OpenAI は Microsoft Azure 上で OpenAI モデル（GPT 系）を使う。Vertex AI は Google Cloud 上で Google モデル＋パートナーモデルを使う。組織のクラウド基盤がどちらかで選ばれることが多い
- Amazon Bedrock（B-30）との住み分け：Bedrock は AWS 上で複数モデルを API 呼び出しする。三者は「クラウド経由で LLM を呼ぶ」三本柱として並べて説明可能
- Google AI Studio との混同注意：Google AI Studio は個人が Gemini を無料で試す画面。Vertex AI は企業向けの有料 Cloud サービスで、本番運用・アクセス制御・SLA あり


## 出典メモ

- <https://cloud.google.com/vertex-ai> — checked 2026-04-30
- <https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform> — checked 2026-04-30


## 備考

- Vertex AI は 2021-05-18 に GA（General Availability）。旧 Google AI Platform と AutoML を統合した後継サービス
- 料金は使ったモデル・リクエスト数・Pipelines 実行時間などで変わる従量課金。evaluation_date での確認を推奨
- Codey（コード補完 API）も Vertex AI 経由で呼び出せるが、Gemini 1.5 以降は Gemini コード機能に統合されつつある（2026-04 時点）
