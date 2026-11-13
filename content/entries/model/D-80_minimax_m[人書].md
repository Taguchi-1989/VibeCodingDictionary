---
id: D-80
title: MiniMax M 系
title_reading: ミニマックス エム系
category: model
subtype: open
experience_level: research_only
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2026-06
version_status: active
pricing_note: freemium
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - MiniMax
  - MoE
  - Kimi
  - Hugging Face
status: needs_review
---

# MiniMax M 系

## tagline

MiniMax の文章・コーディング向けモデル群です。M3 は重みが公開されています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

MiniMax が作る文章・コーディング向けのモデル群です。M3 は 2026-06 に公開された MoE（専門家の一部だけを動かす構造）で、文脈は 100 万トークン、画像・動画の入力や PC 操作にも対応すると報じられています。

## どこで出会うか

重みを配る大型モデルの比較や、Artificial Analysis のリーダーボードで名前が出ます。重みは独自の MiniMax Community License で公開され、商用では表示が要るとされます。

## メイン図

### 図の狙い

M 系の「体の大きさ」と「動く部分」、そして MiniMax 内での役割分担（文章・コーディングの M 系と、動画の Hailuo）を一枚で掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: M3 の総パラメータ（体）と、1 トークンで動く部分（光る部分）
- 周辺の要素: ルーター、文脈 100 万トークン、画像・動画入力、PC 操作、ライセンスの札、別系統の Hailuo
- 関係の描き方: 大きな人型シルエットの一部だけ光らせ、横に別部屋として Hailuo を小さく置く

## 会話での使い方例

「MiniMax M3 は重みが公開された MoE で、ライセンスの確認が要りますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

MiniMax の文章・コーディング向けモデル群です。

### 2. うれしさ

重みが公開され、自前で動かす選択肢になります。

### 3. 注意点

ライセンスは独自で、商用利用の条件の確認が要ります。

### 4. どこで役立つか

重みを配る大型モデルの比較や、自前運用の検討です。

### 5. はじめに

M2.7 から M3 への流れと、動画の Hailuo との違いから。

### 6. 深掘り先

MiniMax、MoE、Kimi

## 開発フローでの位置（必須）

1. 話題を知る — ニュースや順位表で M 系の名前を見る
2. 版を選ぶ — M2.7 と M3 の違いを確かめる
3. 条件を確認 — 独自ライセンスと表示の要件を読む
4. 重みを取得 — Hugging Face などの配布先から入手する
5. 使い方を決める — 自前運用か API 利用かを比べる

## 関連用語

- MiniMax
- MoE
- Kimi
- Hugging Face

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

- 描く内容: 大きな人型シルエット（M3）。体全体が総パラメータ、光る部分が 1 トークンで動く部分。横に小さな別部屋として動画制作の Hailuo
- 登場人物（いれば）: 読者キャラ（非エンジニア）が、光る部分と別部屋を指さして見比べている
- 吹き出し・心の声: 読者「文章の M と、動画の Hailuo は別の系統なんだ」／M3「428B のうち動くのは約 23B」
- 中央に置くキーワード/ラベル: 総パラメータ 428B ／ 動く部分 約 23B ／ 文脈 100 万トークン ／ MiniMax Community License（2026-11 時点・報道ベース）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 新聞（ニュース）
- Step 2 のアイコン/絵柄: 2 つの箱（M2.7 と M3）
- Step 3 のアイコン/絵柄: 契約書と虫眼鏡
- Step 4 のアイコン/絵柄: ダウンロード矢印
- Step 5 のアイコン/絵柄: 分かれ道（自前運用か API か）


## コミュニティ補完メモ

- C-19 MiniMax（会社）との住み分け：会社の創業・上場などは C-19 に任せ、本エントリはモデル（M 系）に絞る
- D-44 Kimi・D-48 DeepSeek V4 との関係：同じく中国発で重みを配る大型 MoE。ライセンスの種類がそれぞれ違う（MIT／独自など）ので、使う前に各条文を確認する
- J-18 MoE：総パラメータと稼働パラメータの数値の解説は J-18 側に任せる
- 動画生成の Hailuo は別系統で、本エントリでは扱わない

## 出典メモ

- Artificial Analysis の比較ページ・記事見出し（検索結果）— checked 2026-11-13
- MiniMax-M3 に関する報道・解説記事（検索経由・二次情報）— checked 2026-11-13

## 備考

- **一次未確認（検索経由）**：公開時期（2026-06）、428B／稼働約 23B の MoE、文脈 100 万トークン、画像・動画入力と PC 操作への対応、重み公開、MiniMax Community License（商用で「Built with MiniMax M3」の表示が要るとされる点）は、すべて二次情報で公式未確認です（2026-11-13 時点）。本文は「報じられています」「とされます」で弱めています
- Artificial Analysis には M2.7・M3 が総合 10〜20 位台に載ると報じられています（順位は時点で動くため本文には書かない）
- `pricing_note: freemium` は重みの入手（無料）と API 利用（従量課金）が併存する意味づけ。API 価格は未確認
- 関連用語に「オープンモデル」の項目は entries.csv に無いため入れていません
