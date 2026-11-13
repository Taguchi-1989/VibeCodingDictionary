---
id: D-36
title: Muse 系
title_reading: ミューズ系
category: model
subtype: other_closed
experience_level: research_only
reader_level: 3
importance: B
figure_type: comparison
page_layout: spread_v1
start_date: 2026-04-08
version_status: active
pricing_note: paid
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - Llama 系
  - Meta AI
  - 蒸留
  - MoE
  - LLaMA のオープン化
status: needs_review
---

# Muse 系

## tagline

Meta が作る AI モデル群です。Llama に続く世代として登場しました。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

文字や画像をまとめて扱い、考えながらツールも使える Meta のモデル群です。Llama は重みを配るモデルでしたが、Muse は API で貸すのが基本で、一部の名前だけ重みも公開されています。

## どこで出会うか

Meta のアプリや、開発者向けの Meta Model API で使われます。記事では「Muse Spark」のように名前ごとに登場し、同じ Muse でも使える場所やライセンスが名前で違います。

## メイン図

### 図の狙い

Muse が「API で借りる名前」と「重みをもらえる名前」の 2 列に分かれることを見せます。Llama との違いが一目で分かるようにします。

### B. 比較図（figure_type: comparison）

- 左列「API で借りる」: Muse Spark、Muse Wonder、Muse Ember
- 右列「重みをもらえる」: Muse Glimmer（小型）、Muse Spark Open（大型）
- 例示ラベル: 「2026-11 時点」。ライセンスは名前ごとに違う

## 会話での使い方例

「Muse は Llama と違って、基本は API で借りる形ですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Meta が Llama の次に出したモデル群です。

### 2. うれしさ

用途に合わせて名前を選べ、小型は手元でも動かせます。

### 3. 注意点

同じ Muse でも名前ごとにライセンスが違います。

### 4. どこで役立つか

Meta 系モデルの選択肢を比べるときに役立ちます。

### 5. はじめに

「借りる名前」と「もらえる名前」を分けて覚えます。

### 6. 深掘り先

Llama 系、蒸留、MoE

## 開発フローでの位置（必須）

1. 用途を決める — 手元で動かすか、API で借りるかを決める
2. 名前を選ぶ — Spark や Glimmer など用途に合う名前を選ぶ
3. 条件を読む — 料金やライセンスを名前ごとに確認する
4. 試して比べる — 手元の仕事で他社モデルと比べる

## 関連用語

- Llama 系
- Meta AI
- 蒸留
- MoE
- LLaMA のオープン化

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

- 描く内容: 2 列の比較図。左に「API で借りる」棚（Spark・Wonder・Ember）、右に「重みをもらえる」棚（Glimmer・Spark Open）。左は貸出カウンター、右は持ち帰りの箱で表す
- 登場人物（いれば）: 読者キャラ（非エンジニア）と Meta 風の店員キャラ
- 吹き出し・心の声: 読者「Llama みたいに全部もらえるんじゃないの？」／店員「基本は貸出です。一部だけ持ち帰れます」
- 中央に置くキーワード/ラベル: 貸す／配る ／ 例示「2026-11 時点」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 分かれ道の標識（手元か API か）
- Step 2 のアイコン/絵柄: 名札が並ぶ棚
- Step 3 のアイコン/絵柄: 契約書と虫眼鏡
- Step 4 のアイコン/絵柄: 天秤

## コミュニティ補完メモ

- D-40 Llama 系との住み分け：Llama は重みを配るのが基本、Muse は貸すのが基本。経緯や世代の詳細は D-40 に任せ、ここは 1 文の対比にとどめる
- J-36 蒸留との関係：Muse Glimmer は Muse Spark からの蒸留とされる。蒸留の仕組みは J-36 へ
- J-18 MoE との関係：Muse Spark Open は MoE 構成とされる。仕組みは J-18 へ
- C-4 Meta AI との関係：C-4 は会社・サービス側の説明。本エントリはモデル側

## 出典メモ

- Meta 公式ブログ・CNBC・Axios（検索経由・二次情報を含む）— checked 2026-11-13
- Meta Model API のモデル一覧（検索経由）— checked 2026-11-13

## 備考

- **一次未確認**：Meta の公式サイトは環境のネットワーク制限で直接取得できず、すべて検索経由（二次情報を含む）です（2026-11-13 時点）
- 時系列（二次情報）：Muse Spark 2026-04-08／Muse Spark 1.1 2026-07-09（Meta Model API の公開プレビューと同時。文脈 100 万トークン、入力 $1.25・出力 $4.25 と報じられています）／Muse Glimmer 2026-08-10（Apache 2.0、30B 小型、Spark からの蒸留と報じられています）／Muse Spark Open 2026-10-15（816B／稼働 42B の MoE、独自の Muse Model License）
- API 提供の別名として Muse Wonder／Ember／Image／Voice Transcribe があるとされます。Muse Wonder（max）は Artificial Analysis の旧版指標で 52.4・12 位という記載があります（二次情報）
- 日付の食い違い：英語版 Wikipedia の一部は Muse Spark を 2026-07-09 とするが、Meta の発表は 2026-04-08（07-09 は 1.1 と API）。start_date は 04-08 を採用
- Muse Spark Open のライセンスには製品への表示義務や、一定売上以上の提供事業者への別契約があるとされます（二次情報）。利用前に原文確認が必要です
- 価格・版数は時変情報です。次回の鮮度監査で確認してください
