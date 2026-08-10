---
id: J-116
title: TPU
title_reading: テンソルプロセッシングユニット
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 3-4
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-08-10
related_terms:
  - GPU
  - H100
  - Google Cloud
  - Vertex AI
status: needs_review
---

# TPU

## tagline

Tensor Processing Unit の略。Google 独自の AI 計算専用チップです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

AI の学習・推論で頻出する行列演算に絞って設計された専用チップです。汎用の GPU と違い用途を絞り込むことで、電力あたりの処理効率を高めています。

## どこで出会うか

Google 検索や Gemini など自社サービスの裏側で使われるほか、Google Cloud の Vertex AI 経由で外部の開発者も借りて使えます。学習ニュースでは NVIDIA GPU と並んで名前が挙がります。

## メイン図

### 図の狙い

NVIDIA の GPU（汎用設計）と TPU（AI 専用設計）を並べ、設計思想の違いを一目で見せます。

### B. 登場シーン（figure_type: comparison）

- シーン1: 左側に GPU — 汎用設計で幅広い演算に対応する
- シーン2: 右側に TPU — AI の行列演算だけに絞った専用設計
- シーン3: 下段に「用途」ラベル。GPU は画像処理・ゲーム・AI 全般、TPU は AI の学習・推論に特化
- 並べる基準: 設計思想（汎用 vs 専用）の対比

## 会話での使い方例

「TPU なら Vertex AI 経由で GPU より安く回せることがあります。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI 計算に特化した Google 独自の専用チップです。

### 2. うれしさ

GPU より電力あたりの処理効率が高いことがあります。

### 3. 注意点

自社サービス中心で外部への供給は限定的です。

### 4. どこで役立つか

Google Cloud 経由の大規模な学習・推論で使われます。

### 5. はじめに

GPU との違いは専用設計かどうかという点です。

### 6. 深掘り先

GPU、H100、Vertex AI

## 開発フローでの位置（必須）

1. 用途を選ぶ — 学習か推論かで GPU と TPU のどちらが向くか判断します
2. 環境を確保する — Google Cloud や Vertex AI で TPU インスタンスを申し込みます
3. ジョブを実行する — 用意した TPU 上で学習・推論の処理を走らせます
4. 効率を確認する — 処理速度と電力あたりのコストを他の環境と比べます

## 関連用語

- GPU
- H100
- Google Cloud
- Vertex AI

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 
- 
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 
- 👍 良い点: 
- 👎 ダメな点: 
- 👥 誰向けか: 
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左に GPU（形の違うブロックを何でもこなす汎用装置）、右に TPU（同じ形のブロックだけを高速に処理する専用装置）を並べた対比図
- 登場人物（いれば）: GPU 側に「なんでもできるけど専門はない」という顔の人物、TPU 側に「AI の計算だけならこっちが速い」という顔の人物
- 吹き出し・心の声: GPU「画像処理もゲームも何でもこなします」、TPU「AI の行列演算だけならこっちが得意です」
- 中央に置くキーワード/ラベル: 汎用設計 vs 専用設計

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡 + 天秤（用途を比べて選ぶ）
- Step 2 のアイコン/絵柄: クラウドのアイコン（Google Cloud / Vertex AI で確保）
- Step 3 のアイコン/絵柄: チップが光るアイコン（ジョブ実行）
- Step 4 のアイコン/絵柄: メーター・ゲージ（効率確認）


## コミュニティ補完メモ

- GPU（J-77）との住み分け：J-77 は GPU 全般の概念エントリ。本エントリは「Google が自社で作った、もう一つの選択肢」という TPU 固有の位置づけに絞る
- H100（J-72）・Blackwell（J-73）との住み分け：どちらも NVIDIA の特定 GPU 製品。TPU は同じ役割（AI 計算）を担う NVIDIA 以外の選択肢として対比的に置く
- NPU・AI PC（J-115）との住み分け：J-115 は手元の PC に載る省電力チップ。本エントリは Google のデータセンター向け大規模チップに絞り、規模感を分ける
- Google Cloud（B-24）・Vertex AI（B-27）との住み分け：TPU を借りる具体的な手順・料金の説明はそちらに譲り、本エントリはチップ自体の役割説明に絞る


## 出典メモ

- Google Cloud TPU 公式ページ <https://cloud.google.com/tpu> — checked 2026-08-10
- Google Cloud Blog「Introducing Ironwood TPUs」<https://cloud.google.com/blog/products/compute/introducing-ironwood-tpus> — checked 2026-08-10


## 備考

- 2026-08 時点で最新世代は第 7 世代の Ironwood で、一般提供が進んでいる段階です。世代名・世代数は今後も更新される時変情報のため、本文では固有の世代名を断定せず evaluation_date 時点の情報として扱っています。
- 市場全体では NVIDIA の GPU が大きなシェアを占め、TPU は「自社で作る」路線の代表例という位置づけです。
