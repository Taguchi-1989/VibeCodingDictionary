---
id: D-86
title: Hunyuan 系
title_reading: フンユェン系
category: model
subtype: open
experience_level: research_only
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2023-09
version_status: active
pricing_note: freemium
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - Tencent
  - Alibaba
  - Qwen 系
  - MoE
status: needs_review
---

# Hunyuan 系

## tagline

Tencent が作る AI モデル群で、重みも公開されています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

WeChat やゲームで知られる Tencent の大規模言語モデル群です。2023 年に初公開され、2026 年には MoE（専門家の組み合わせ）構成の Hy3 の重みが公開されました。

## どこで出会うか

Tencent の対話アプリ Yuanbao（元宝）などの中身として使われます。海外向けには「Hy」の名で呼ばれ、記事では Hy3 のように名前ごとに登場します。

## メイン図

### 図の狙い

Hunyuan が Tencent の手持ちのアプリに組み込まれ、同時に重みも配られる、2 つの出口を持つことを見せます。

### A. 構造図（figure_type: structure）

- 中央「Hunyuan（混元）／海外名 Hy」
- 上へ: Yuanbao・CodeBuddy・ima（Tencent のアプリ）
- 下へ: 重み公開の Hy3（295B／稼働 21B の MoE と報じられています）
- 例示ラベル: 「2026-11 時点」。ライセンスは記事で食い違い

## 会話での使い方例

「Hunyuan は Tencent のアプリに入りつつ、重みも公開されていますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Tencent が自社アプリ向けに育てるモデル群です。

### 2. うれしさ

重みが公開された版は、自分の環境で試せます。

### 3. 注意点

ライセンスの記述が資料によって食い違います。

### 4. どこで役立つか

中国発モデルの選択肢を比べるときに役立ちます。

### 5. はじめに

「Hunyuan」と海外名「Hy」を同じものと覚えます。

### 6. 深掘り先

Tencent、Qwen 系、MoE

## 開発フローでの位置（必須）

1. 候補を知る — 中国発の公開モデルとして名前を押さえる
2. 版を確かめる — Hy3 など使いたい名前の版を確認する
3. 条件を読む — ライセンスの原文を自分で読む
4. 試して比べる — 手元の仕事で他社モデルと比べる

## 関連用語

- Tencent
- Alibaba
- Qwen 系
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

- 描く内容: 中央に「Hunyuan」の箱。上の矢印は Tencent のアプリ群（Yuanbao・CodeBuddy・ima）、下の矢印は「重みを配る」箱（Hy3）
- 登場人物（いれば）: 読者キャラ（非エンジニア）と Tencent 風の案内役キャラ
- 吹き出し・心の声: 読者「Hunyuan と Hy は別のもの？」／案内役「同じ系統です。海外向けの名前が Hy です」
- 中央に置くキーワード/ラベル: 混元／Hy ／ 例示「2026-11 時点」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 地図に立てる旗
- Step 2 のアイコン/絵柄: 版数が並ぶ名札
- Step 3 のアイコン/絵柄: 契約書と虫眼鏡
- Step 4 のアイコン/絵柄: 天秤

## コミュニティ補完メモ

- C-26 Tencent との住み分け：C-26 は会社・アプリ側の説明。本エントリはモデル側
- D-43 Qwen 系（Alibaba）との関係：同じ中国発の重み公開モデル。比較の観点は D-43 に任せ、ここは名前の紹介にとどめる
- J-18 MoE との関係：Hy3 は MoE 構成とされる。仕組みは J-18 へ

## 出典メモ

- Tencent 公式発表・技術系ニュース記事（検索経由・二次情報を含む）— checked 2026-11-13
- ブリーフ ledgers/stage16_briefs_2026-11.md 追補 3 — checked 2026-11-13

## 備考

- **一次未確認（検索経由）**：Tencent の公式サイトは環境のネットワーク制限で直接取得できず、二次情報を含みます（2026-11-13 時点）。基礎情報は一般知識にもとづきます
- 時系列（二次情報）：2023-09 初公開／Hy3 preview 2026-04-23（295B の MoE、稼働 21B、文脈 256K、重み公開）／Hy3 正式版 2026-07-06
- **ライセンスの食い違い**：Apache 2.0 とする記事と、独自ライセンスとする記事があり未確定です。利用前に原文確認が必要です
- **Hy4 の記載（2026-11-04）**が 1 件ありましたが、裏が取れないため本文には書いていません
- Artificial Analysis（AA）への掲載そのものは未確認です。主要な LLM 開発元として立てています
- 価格・版数は時変情報です。次回の鮮度監査で確認してください
