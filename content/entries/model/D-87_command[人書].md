---
id: D-87
title: Command 系
title_reading: コマンド系
category: model
subtype: open
experience_level: research_only
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2024
version_status: active
pricing_note: freemium
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - Cohere
  - RAG
  - Embedding
  - Transformer 論文
  - MoE
status: needs_review
---

# Command 系

## tagline

Cohere が企業向けに作る AI モデル群です。社内に置いて動かす用途を想定しています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

自社の環境に置いて動かす前提で作られた、Cohere の言語モデル群です。検索した資料をもとに答える RAG（検索拡張生成）の用途に強いとされ、2026 年には重みも公開されました。

## どこで出会うか

企業の社内検索や問い合わせ対応で、Cohere の API や自社環境の形で使われます。記事では Command R、Command A、Command A+ のように名前ごとに登場します。

## メイン図

### 図の狙い

Command が「会社の中に置いて動かす」ことを前提にした作りで、検索用の部品と組み合わせて使われる姿を見せます。

### A. 構造図（figure_type: structure）

- 中央「Command（Cohere のモデル）」
- 左: 社内の資料（Embed・Rerank で探す）
- 右: 社内の環境（手元・プライベートクラウド）で回答
- 例示ラベル: 「2026-11 時点」。Command A+ は Apache 2.0 での重み公開と報じられています

## 会話での使い方例

「Command は社内に置いて RAG で使う、企業向けのモデルですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

企業の社内で動かす前提の言語モデル群です。

### 2. うれしさ

資料を外に出さず、検索と組み合わせて使えます。

### 3. 注意点

名前ごとに提供形態とライセンスが違います。

### 4. どこで役立つか

社内検索や問い合わせ対応の設計で役立ちます。

### 5. はじめに

R、A、A+ の順に世代が進んだと覚えます。

### 6. 深掘り先

RAG、Embedding、Cohere

## 開発フローでの位置（必須）

1. 用途を決める — 社内資料への質問応答かを見極める
2. 資料を整える — Embedding で検索できる形にする
3. モデルを選ぶ — Command R や A など用途に合う名前を選ぶ
4. 置き場所を決める — API か自社環境かを選ぶ
5. 試して比べる — 手元の資料で他社モデルと比べる

## 関連用語

- Cohere
- RAG
- Embedding
- Transformer 論文
- MoE

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

- 描く内容: 会社のビルの中に Command の箱が置かれ、横に書類棚（Embed・Rerank）がつながる図。ビルの外へ資料が出ない矢印を描く
- 登場人物（いれば）: 読者キャラ（非エンジニア）と社内担当者キャラ
- 吹き出し・心の声: 読者「社内の資料を外に出さずに使えるの？」／担当者「自社の環境に置いて動かせる前提のモデルです」
- 中央に置くキーワード/ラベル: 社内で動かす ／ 例示「2026-11 時点」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 質問の吹き出し
- Step 2 のアイコン/絵柄: 書類が棚に整列
- Step 3 のアイコン/絵柄: 名札が並ぶ棚
- Step 4 のアイコン/絵柄: ビルとクラウドの分かれ道
- Step 5 のアイコン/絵柄: 天秤

## コミュニティ補完メモ

- C-27 Cohere との住み分け：C-27 は会社・事業側の説明。本エントリはモデル側
- G-15 RAG／G-16 Embedding との関係：Command は RAG の「答える役」、Embed／Rerank は「探す役」。仕組みは G-15・G-16 へ
- H-58 Transformer 論文との関係：創業者の Aidan Gomez 氏は論文の共著者のひとり。経緯は C-27 と H-58 に任せる

## 出典メモ

- Cohere 公式発表・技術系ニュース記事（検索経由・二次情報を含む）— checked 2026-11-13
- ブリーフ ledgers/stage16_briefs_2026-11.md 追補 3 — checked 2026-11-13

## 備考

- **一次未確認（検索経由）**：Cohere の公式サイトは環境のネットワーク制限で直接取得できず、二次情報を含みます（2026-11-13 時点）。基礎情報は一般知識にもとづきます
- 時系列：Command R／R+ 2024／Command A 2025-03／Command A+ 2026-05-20（MoE、48 言語、少ないハードウェアで動くことを重視。Cohere 初の Apache 2.0 での重み公開と Gomez 氏が投稿したと報じられています）。音声認識の Cohere Transcribe（2026-03、Apache 2.0）は別エントリ候補
- Command R 系の重みは従来、非商用の別ライセンスで公開されていた（一般知識）。A+ の条件との違いは利用前に原文確認が必要です
- Artificial Analysis（AA）への掲載そのものは未確認です。主要な LLM 開発元として立てています
- 価格・版数は時変情報です。次回の鮮度監査で確認してください
