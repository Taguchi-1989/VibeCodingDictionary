---
id: C-7
title: Hugging Face
title_reading: ハギングフェイス
category: person_org
subtype: company
experience_level: partial
reader_level: 2-3
importance: B
figure_type: structure
page_layout: spread_v1
start_date: 2016
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - オープンモデル
  - transformers
  - Spaces
  - Llama
  - Mistral
status: ready
---

# Hugging Face

## tagline

AI モデルとデータセットを誰でも共有できるプラットフォームです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

オープンモデル・データセット・デモアプリを集めた共有基盤です。Models / Datasets / Spaces / transformers ライブラリの 4 本柱で構成され、「AI の GitHub」と呼ばれます。

## どこで出会うか

Llama や Mistral などのオープンモデルを探すとき、最初に行き着く場所です。transformers ライブラリは Python で AI を扱う事実上の標準で、コードサンプルを検索すると高頻度で登場します。

## メイン図

### 図の狙い

Hugging Face が「1 つのプラットフォームに何を束ねているか」を 4 本柱で示します。会社名より「場所」として覚えてもらうのが目的です。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Hugging Face（2016 年設立）
- 周辺の要素（4 個）: Models（公開モデル置き場）／Datasets（学習データ置き場）／Spaces（デモホスティング）／transformers（Python ライブラリ）
- 関係の描き方: 中央に HF ロゴ、四方に 4 本柱アイコンを配置し、包含の丸で囲む

## 会話での使い方例

「Llama はまず Hugging Face で配布モデルを確認してから使うのが定番です。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

オープンモデルとデータセットの中心的な流通基盤です。

### 2. うれしさ

無料で最新モデルをすぐ試せ、Spaces でデモも確認できます。

### 3. 注意点

モデルの品質はまちまちで、ライセンスは個別に確認が必要です。

### 4. どこで役立つか

自前で AI を動かしたい人がモデル選定と動作確認をするとき。

### 5. はじめに

Models 検索と transformers ライブラリの関係をまず把握します。

### 6. 深掘り先

transformers、Llama、Mistral、Gradio。

## 開発フローでの位置（必須）

1. モデルを探す — huggingface.co の Models でキーワード検索し候補を絞る
2. ライセンス確認 — 商用利用可否を README と Model Card で確認する
3. Spaces で試す — Gradio デモで動作を確認してから導入を判断する
4. ローカルに取得 — transformers でモデルをダウンロードして推論を実行する
5. データセット活用 — Datasets からファインチューニング用データを取得する

## 関連用語

- オープンモデル
- transformers
- Spaces
- Llama
- Mistral


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 商用利用可能なのか単なるテスト用なのかの区別がつきづらいです。
- 悪意の有無も含め、個人情報を入力するのには抵抗があります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: AI ニュースで実装されたと耳にしました。
- 👍 良い点: AI モデルのデファクトスタンダードな置き場です。
- 👎 ダメな点: 著作権や機密の扱いが不安で、デプロイもコールドスタートが起きました。
- 👥 誰向けか: AI を活用する側より提供する側向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に HF のロゴ（抱き合うロボットのアイコン）を置き、四方に 4 本柱を示すアイコンを配置。Models（モデルの箱）、Datasets（テーブルアイコン）、Spaces（ブラウザ画面アイコン）、transformers（Python ヘビアイコン）
- 登場人物: 若い研究者（20 代男性）がラップトップで HF のモデル検索ページを見ている
- 吹き出し・心の声: 「Llama がここで全部揃う！モデルもデータもデモも」
- 中央に置くキーワード/ラベル: Hugging Face = AI モデルの流通ハブ

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 検索アイコン（モデルを探す）
- Step 2 のアイコン/絵柄: 書類・ライセンスアイコン（ライセンス確認）
- Step 3 のアイコン/絵柄: 再生ボタン（Spaces で試す）
- Step 4 のアイコン/絵柄: ダウンロード矢印（ローカルに取得）
- Step 5 のアイコン/絵柄: データベースアイコン（データセット活用）
- 矢印で示す流れの意図: 「探す → 確認 → 試す → 取得 → 活用」の導入サイクル


## コミュニティ補完メモ

- Llama（D-40）との住み分け：Llama はモデル自体の解説、Hugging Face（C-7）はその配布先・流通プラットフォームとして扱います
- Mistral（D-41）も同様の位置づけです
- transformers ライブラリは Hugging Face 社が開発した Python（F-3）向けライブラリです。個別エントリが立つ場合は F 系で扱い、C-7 は「ライブラリの提供元」の説明に留めます
- Spaces は Gradio / Streamlit ベースのデモホスティング機能。Gradio 個別エントリとの重複を避けるため、C-7 では「デモ確認の場所」程度の言及に留めます
- GitHub（I-11）との住み分け：コードのバージョン管理は GitHub、AI モデル・データセットの共有は Hugging Face と整理します

## 出典メモ

- <https://huggingface.co> — checked 2026-04-29
- <https://huggingface.co/docs/transformers> — checked 2026-04-29

## 備考

- 2016 年設立、本社はニューヨーク。当初はチャットボット会社として出発し、のちに AI コミュニティプラットフォームへ転換しました
- 無料 / Pro / Enterprise の 3 段階プランがあり、料金は変動することがあります。evaluation_date を参照してください
- 「Hugging Face」の社名は、テキストのニュアンスをとらえる NLP 技術への親しみを表した名前です（顔文字の :hugging_face: に由来）
- Enterprise Hub などの法人向け機能は時変情報のため本文では触れていません
