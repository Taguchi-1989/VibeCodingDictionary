---
id: D-82
title: Inkling
title_reading: インクリング
category: model
subtype: open
experience_level: research_only
reader_level: 3
importance: C
figure_type: comparison
page_layout: spread_v1
start_date: 2026-07-15
version_status: active
pricing_note: freemium
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - Thinking Machines Lab
  - MoE
  - Apache 2.0
  - Fine-tuning
status: needs_review
---

# Inkling

## tagline

Thinking Machines Lab が出した最初の公開モデルです。重みは公開されています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

2026-07-15 に公開された汎用モデルです。975B の MoE（専門家の一部だけを動かす構造）で、重みは Apache 2.0 で公開されました。自社向けに作り替える土台として出されています。

## どこで出会うか

Artificial Analysis の比較ページや、重みを配るモデルの話題で名前が出ます。07-31 には小型版の Inkling Small が続きました。

## メイン図

### 図の狙い

大型の Inkling と小型の Inkling Small を並べ、大きさが違っても近い性能という点と、「土台として作り替える」位置づけを掴んでもらいます。

### C. 比較図（figure_type: comparison）

- 左列「Inkling」: 975B の MoE／稼働 41B／文脈 100 万トークン／Apache 2.0
- 右列「Inkling Small」: 276B の MoE／稼働 12B／文脈 256K／Apache 2.0
- 下に共通の矢印: 「自社向けに作り替える土台（Tinker）」
- 比較の軸: 大きさ、動く部分、文脈の長さ

## 会話での使い方例

「Inkling は Apache 2.0 で重みが出ていて、土台として使う前提ですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

作り替えの土台として出された、重み公開の汎用モデルです。

### 2. うれしさ

Apache 2.0 で、自社向けに調整しやすい条件です。

### 3. 注意点

学習データと学習コードは公開されていません。

### 4. どこで役立つか

重みを配る大型モデルの比較や、作り替えの検討です。

### 5. はじめに

Inkling と Inkling Small の大きさの違いから見ます。

### 6. 深掘り先

Thinking Machines Lab、MoE、Fine-tuning

## 開発フローでの位置（必須）

1. 話題を知る — ニュースや順位表で Inkling を見る
2. 版を選ぶ — 大型の Inkling か小型の Small かを決める
3. 重みを取得 — 配布先から入手する
4. 作り替える — 自社のデータで調整する形を検討する
5. 使い方を決める — 自前運用か API 利用かを比べる

## 関連用語

- Thinking Machines Lab
- MoE
- Apache 2.0
- Fine-tuning

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

- 描く内容: 左右 2 列。左に大きな人型シルエット（Inkling）、右に一回り小さな人型（Inkling Small）。どちらも光る部分が動く部分。2 体の足元に「Tinker で作り替える土台」と書かれた作業台
- 登場人物（いれば）: 読者キャラ（非エンジニア）が 2 体を見比べ、作業台の道具を手に取っている
- 吹き出し・心の声: 読者「小さいほうでも点数が近いの？」／Inkling「975B のうち動くのは 41B」／Small「276B のうち動くのは 12B」
- 中央に置くキーワード/ラベル: 土台 ／ Apache 2.0 ／ 文脈 100 万トークン／256K（2026-11 時点・報道ベース）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 新聞（ニュース）
- Step 2 のアイコン/絵柄: 大小 2 つの箱（Inkling / Small）
- Step 3 のアイコン/絵柄: ダウンロード矢印
- Step 4 のアイコン/絵柄: 工具と作業台
- Step 5 のアイコン/絵柄: 分かれ道（自前運用か API か）


## コミュニティ補完メモ

- C-21 Thinking Machines Lab（会社）との住み分け：創業・調達・人員などは C-21 に任せ、本エントリはモデル（Inkling）に絞る
- Tinker（自社向けに作り替える基盤）は C-21 側で扱う。本エントリは土台としての位置づけだけ書く
- J-16 Fine-tuning：作り替えの手法の解説は J-16 側に任せる
- J-18 MoE：総パラメータと稼働パラメータの解説は J-18 側に任せる
- Apache 2.0 のエントリとの関係：「重みは Apache 2.0、学習データと学習コードは非公開」という区別は本エントリで一言だけ触れる

## 出典メモ

- Artificial Analysis の Inkling・Inkling Small に関する比較ページ／記事見出し（検索結果）— checked 2026-11-13
- Thinking Machines Lab の Inkling に関する報道・解説記事（検索経由・二次情報）— checked 2026-11-13

## 備考

- **一次未確認（検索経由）**：公開日（2026-07-15、Small は 07-31）、975B／稼働 41B、276B／稼働 12B、文脈 100 万／256K、Apache 2.0、学習データ・コード非公開、「最高性能ではない」という会社自身の発言は、すべて二次情報で公式未確認です（2026-11-13 時点）
- AA は Inkling Small を「3 分の 1 以下の大きさで Inkling と 1 点差以内」と記事にしましたが、点数と順位は時点で動くため本文には書いていません
- `pricing_note: freemium` は重みの入手（無料）と、Tinker・API の有償利用が併存する意味づけ。価格は未確認
- 関連用語に「オープンモデル」の項目は entries.csv に無いため入れていません
