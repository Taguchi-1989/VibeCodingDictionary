---
id: D-81
title: MiMo
title_reading: ミモ
category: model
subtype: open
experience_level: research_only
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2026-09-21
version_status: active
pricing_note: freemium
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - Xiaomi
  - MoE
  - MIT ライセンス
  - Kimi
  - DeepSeek V4
status: needs_review
---

# MiMo

## tagline

Xiaomi の LLM です。MIT ライセンスで重みが公開されています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Xiaomi（シャオミ）が作る汎用モデルです。2026-09 公開の MiMo-V2.6-Pro は約 1.02 兆パラメータの MoE（専門家の一部だけを動かす構造）で、文字・画像・動画・音声を扱い、文脈は 100 万トークンと報じられています。

## どこで出会うか

重みを配る大型モデルの比較で、Kimi や DeepSeek V4 と並んで名前が出ます。MIT ライセンスで、軽量の Flash 版も同時に公開されました。

## メイン図

### 図の狙い

「家電メーカーが出した、自由に使える大型モデル」という位置づけと、Pro と Flash の大きさの違いを掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: スマホ・家電の会社から出た大型モデル（Pro）と軽量版（Flash）
- 周辺の要素: Pro 約 1.02 兆／稼働約 42B、Flash 309B、文脈 100 万トークン、4 種類の入力（文字・画像・動画・音声）、MIT ライセンスの札
- 関係の描き方: スマホと家電の箱を背にした大小 2 体の人型シルエット。光る部分が動く部分

## 会話での使い方例

「MiMo は MIT ライセンスで重みが出ている MoE だと聞きます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Xiaomi が作る、重みを配る汎用モデルです。

### 2. うれしさ

MIT ライセンスで、商用でも使いやすい条件です。

### 3. 注意点

順位の数字は発表元ごとに食い違うことがあります。

### 4. どこで役立つか

重みを配る大型モデルの比較や、自前運用の検討です。

### 5. はじめに

Pro と Flash の大きさの違いから見ます。

### 6. 深掘り先

Xiaomi、MoE、MIT ライセンス

## 開発フローでの位置（必須）

1. 話題を知る — ニュースや順位表で MiMo の名前を見る
2. 版を選ぶ — 大型の Pro か軽量の Flash かを決める
3. 重みを取得 — 配布先から入手する
4. 数字を確認 — 順位とライセンスを公式で再確認する
5. 使い方を決める — 自前運用か API 利用かを比べる

## 関連用語

- Xiaomi
- MoE
- MIT ライセンス
- Kimi
- DeepSeek V4

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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: スマホ・家電の箱を背にした大小 2 体の人型シルエット（Pro と Flash）。光る部分が 1 トークンで動く部分。胸に MIT ライセンスの札
- 登場人物（いれば）: 読者キャラ（非エンジニア）が、2 体を見上げて驚いている
- 吹き出し・心の声: 読者「スマホの会社が、こんな大きなモデルを配っているの？」／Pro「約 1.02 兆のうち動くのは約 42B」／Flash「こちらは 309B」
- 中央に置くキーワード/ラベル: 総パラメータ 約 1.02 兆 ／ 動く部分 約 42B ／ 文脈 100 万トークン ／ MIT ライセンス（2026-11 時点・報道ベース）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 新聞（ニュース）
- Step 2 のアイコン/絵柄: 大小 2 つの箱（Pro / Flash）
- Step 3 のアイコン/絵柄: ダウンロード矢印
- Step 4 のアイコン/絵柄: 虫眼鏡と公式ページ
- Step 5 のアイコン/絵柄: 分かれ道（自前運用か API か）


## コミュニティ補完メモ

- C-20 Xiaomi（会社）との住み分け：会社の創業・事業は C-20 に任せ、本エントリはモデル（MiMo）に絞る
- D-44 Kimi・D-48 DeepSeek V4 との比較：同じく重みを配る大型 MoE。順位の入れ替わりは E-52 Artificial Analysis Intelligence Index 側の読み方に任せる
- J-18 MoE：総パラメータと稼働パラメータの解説は J-18 側に任せる

## 出典メモ

- Xiaomi の MiMo-V2.6-Pro 発表に関する報道・解説記事（検索経由・二次情報）— checked 2026-11-13
- Artificial Analysis に関する記事（検索経由・二次情報）— checked 2026-11-13

## 備考

- **一次未確認（検索経由）**：公開日（2026-09-21 または 22 と記事で割れる。start_date は前者）、約 1.02 兆／稼働約 42B の MoE、Flash 309B、高速版 UltraSpeed の存在、文脈 100 万トークン、4 種類の入力、MIT ライセンスは、すべて二次情報で公式未確認です（2026-11-13 時点）
- Xiaomi は「Artificial Analysis Intelligence Index で 46 点、重みを入手できるモデルで最高」と発表しましたが、同点で Kimi K3.1 Pro を首位とする記事もあり、時点で入れ替わります。点数は本文に書いていません。自社の比較表でも Claude Opus 5 には多くの項目で及ばないとされます
- `pricing_note: freemium` は重みの入手（無料）と API 利用が併存する意味づけ。API 価格は未確認
- 関連用語に「オープンモデル」の項目は entries.csv に無いため入れていません
