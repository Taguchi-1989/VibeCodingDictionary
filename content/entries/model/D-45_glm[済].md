---
id: D-45
title: GLM
title_reading: ジーエルエム
category: model
subtype: open_weight_llm
experience_level: research_only
reader_level: 3-4
importance: D
figure_type: comparison
page_layout: spread_v1
start_date: 2023-03-01
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Z.ai
  - DeepSeek V3
  - Qwen
  - Kimi
status: ready
---

# GLM

## tagline

General Language Model の略。Z.ai（中国）が開発するオープンウェイト LLM 群です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

中国語と英語の両言語に強い LLM（大規模言語モデル）を提供します。コーディング特化の CodeGeeX や画像入力対応の GLM-4V など派生モデルも多く、用途に合わせて選べます。

## どこで出会うか

Hugging Face でオープンウェイト版が公開されており、ローカル GPU で動かす構成を試みる際に名前を見かけます。Cursor や Roo Code などのエディタ連携でも GLM-4.6 が選択肢として挙がります。

## メイン図

### 図の狙い

GLM ファミリーの系譜と派生モデルの広がりを一覧で示し、「どのバージョンが何に向くか」を掴んでもらいます。

### B. 登場シーン（figure_type: comparison）

- シーン1: 開発者がローカル環境で GLM-4.6 をセットアップし、社内チャットを試作している
- シーン2: Cursor の設定画面でモデル一覧を開き、GLM-4.6 を選んでコード補完を確認している
- シーン3: Hugging Face の GLM-4V ページで画像入力デモを動かしている
- 並べる基準: 利用環境（ローカル／エディタ統合／ウェブデモ）の違い

## 会話での使い方例

「GLM-4.6 をローカル GPU で動かして、社内チャットを試作しました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Z.ai が提供する中国語・英語対応のオープンウェイト LLM です。

### 2. うれしさ

ローカルで動かせるためデータを外部送信せずに利用できます。

### 3. 注意点

統計分野の GLM（一般化線形モデル）と同名で混同しやすいです。

### 4. どこで役立つか

中国語を含む文書処理やローカル LLM 構成での検討に向きます。

### 5. はじめに

Z.ai 開発・Hugging Face 公開・派生モデルの種類を把握します。

### 6. 深掘り先

DeepSeek V3、Qwen、CodeGeeX

## 開発フローでの位置（必須）

1. モデル選定 — Hugging Face で GLM のバージョンと量子化形式を確認します
2. ローカル環境構築 — GPU ドライバと推論ライブラリ（llama.cpp 等）を準備します
3. エディタ連携 — Cursor や Roo Code にエンドポイントを設定してコード補完を試みます
4. 用途別派生選択 — コードなら CodeGeeX、画像入力なら GLM-4V を選びます

## 関連用語

- Z.ai
- DeepSeek V3
- Qwen
- Kimi


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 一般認知度がかなり低く、知らない人には「何それ？」となります。
- API 利用時に中国系モデルゆえの情報漏洩リスクが気になります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: YouTuber が推していて名前を知った印象です。
- 👍 良い点: 以前は API 料金が安くてコスパが良いと評判でした。
- 👎 ダメな点: 最近値上げしたという話もあります。
- 👥 誰向けか: LLM をコスパで選びたい人向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: GLM ファミリーの系譜を縦に並べた比較図。ChatGLM → GLM-4 → GLM-4.5/4.6 の流れと、CodeGeeX・GLM-4V・GLM-4-Voice の派生ラインを枝分かれで示す
- 登場人物（いれば）: エンジニア風の人物が Hugging Face のモデルカードを見ながら「どれを使おう」と考えている
- 吹き出し・心の声: 「中国語も英語もいけるのか」「ローカルで動くのが魅力」
- 中央に置くキーワード/ラベル: GLM-4.6

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡で Hugging Face ページを検索
- Step 2 のアイコン/絵柄: GPU サーバーにインストール中の画面
- Step 3 のアイコン/絵柄: エディタのモデル選択ドロップダウン
- Step 4 のアイコン/絵柄: コード補完と画像入力の 2 つのアイコンを並置
- 矢印で示す流れの意図: モデル選定から実利用まで 4 段階で進む流れ


## コミュニティ補完メモ

- Z.ai（C-11）との住み分け：C-11 は企業・開発元の説明、D-45 はモデルファミリーの技術的特性を扱います
- DeepSeek V3（D-46）との住み分け：同じ中国系オープンウェイト勢だが、DeepSeek は深度求（DeepSeek 社）、GLM は Z.ai と開発元が異なります
- Qwen（D-43）との住み分け：Qwen はアリババ系、GLM は清華大学発スピンアウト Z.ai 系で、言語特性のターゲットが一部重なります
- 統計分野の GLM（一般化線形モデル、Generalized Linear Model）とは別物。本書では Z.ai の LLM ファミリーを指します

## 出典メモ

- <https://huggingface.co/THUDM> — GLM モデル一覧 checked 2026-04-30
- <https://zhipuai.cn> — Z.ai 公式（旧 Zhipu AI） checked 2026-04-30


## 備考

- GLM-4.5 は 2025 年中盤にエージェンティック性能を強化したバージョン
- GLM-4.6 は 2025 年後半に公開、Cursor・Roo Code 等エディタ連携を意識した設計
- 統計の GLM（Generalized Linear Model）とは別物。読者への注意を「非エンジニアのつまずき」欄に残す想定
- pricing_note: freemium（Hugging Face 公開のオープンウェイト版は無償、Z.ai の API 版は有償プランあり）
