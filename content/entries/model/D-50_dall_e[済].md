---
id: D-50
title: DALL-E
title_reading: ダリ
category: model
subtype: image_video
experience_level: partial
reader_level: 2
importance: C
figure_type: timeline
page_layout: spread_v1
start_date: 2021
version_status: deprecated
pricing_note: freemium
evaluation_date: 2026-04-29
last_audited: 2026-11-13
related_terms:
  - OpenAI
  - ChatGPT
  - 拡散モデル
  - Stable Diffusion
  - GPT Image 系
status: ready
---

# DALL-E

## tagline

OpenAI の画像生成モデルです。2025 年 3 月に ChatGPT では GPT Image へ交代しました。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

テキストの指示文（プロンプト）を送ると画像を生成します。拡散モデル（Diffusion Model）という仕組みで、ノイズから目的の画像を段階的に作り出します。

## どこで出会うか

2023 年 10 月から 2025 年 3 月まで、ChatGPT で絵を頼むと DALL-E 3 が動いていました。以降は GPT Image 系が動きます。画像生成の歴史や比較の文脈で名前を目にすることがあります。

## メイン図

### 図の狙い

DALL-E 1（2021）→ DALL-E 2（2022）→ DALL-E 3（2023）の 3 世代と、2025 年 3 月の GPT Image への交代を時系列で示し、DALL-E の位置づけを 1 枚で把握できるようにします。

### タイムライン（figure_type: timeline）

- DALL-E 1（2021年1月）：テキストから画像生成の概念実証。品質はまだ荒削り
- DALL-E 2（2022年4月）：解像度と写実性が大幅に向上。インペインティング（部分修正）も対応
- DALL-E 3（2023年10月）：ChatGPT との統合。プロンプトの読み取り精度が向上し、指示通りの画像が出やすくなりました
- 2025年3月：ChatGPT の画像生成が GPT Image（D-28）に交代。以降 ChatGPT で DALL-E 3 は動きません

## 会話での使い方例

「DALL-E は ChatGPT の絵を担った画像モデルで、今は GPT Image に交代しました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

テキスト指示から画像を生成する OpenAI の画像モデルです。

### 2. うれしさ

文章だけで画像が作れるので、デザイン素材を素早く試せます。

### 3. 注意点

生成画像の著作権・商用利用のルールは利用規約で都度確認が必要です。

### 4. どこで役立つか

資料の挿絵や SNS 投稿用素材の下書き作成に使えます。

### 5. はじめに

今の入口は GPT Image 系で、DALL-E は歴史として読みます。

### 6. 深掘り先

GPT Image 系、拡散モデル、Stable Diffusion

## 開発フローでの位置（必須）

1. 用途を決める — 挿絵・アイコン・背景など目的を絞る
2. プロンプトを書く — 画風・構図・色味を文章で指示する
3. 生成・確認 — ChatGPT 画面または API で画像を受け取る
4. 修正指示 — 気に入らない箇所を追加プロンプトで調整する
5. 利用規約を確認 — 商用利用の可否を OpenAI の規約で確認する

## 関連用語

- OpenAI
- ChatGPT
- 拡散モデル
- Stable Diffusion
- GPT Image 系

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 良いものができても、少し修正しようとするとすぐに絵が崩れます。
- 出力の絵柄が一定のクセに偏りやすいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 自分の絵より上手くて結構感動しました。
- 👍 良い点: 一定品質のものをたくさん作れる点が良いです。
- 👎 ダメな点: AI っぽさが出やすく、確率的な均一感が気になります。
- 👥 誰向けか: Midjourney から次のツールを探している人向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 横軸に「2021 DALL-E 1」→「2022 DALL-E 2」→「2023 DALL-E 3」を矢印で結び、末尾に「2025-03 GPT Image へ交代」の分岐矢印を足す（2026-11-13 追記）。各世代の代表的な変化（荒削り→高解像度→ChatGPT 統合）を吹き出しで添える
- 登場人物: 画面脇に人物キャラクター（著者）が DALL-E 3 の時系列を指差している
- 吹き出し・心の声: DALL-E 3 の箇所に「ChatGPT から直接指示できます」と吹き出し
- 中央に置くキーワード: テキスト → 画像

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 目標アイコン（用途を決める）
- Step 2 のアイコン/絵柄: 鉛筆アイコン（プロンプトを書く）
- Step 3 のアイコン/絵柄: 画像フレームアイコン（生成・確認）
- Step 4 のアイコン/絵柄: ループ矢印（修正指示）
- 矢印で示す流れの意図: 一方向の流れ＋修正ループを示す

## コミュニティ補完メモ

- Stable Diffusion（D-54）との住み分け：D-54 はオープンソースで自前環境構築・細かいパラメータ制御が中心。DALL-E は ChatGPT 経由で気軽に試せる「入口」として位置づける
- Imagen（D-51）との住み分け：D-51 は Google のモデル。本エントリは OpenAI 系の文脈で書く
- GPT Image 系（D-28）との住み分け（2026-11-13 追記）：2025-03 以降の ChatGPT の画像生成は D-28。本エントリは DALL-E 1〜3 の歴史に絞る
- Sora（D-52）との住み分け：D-52 は動画生成。本エントリは静止画のみ扱う
- 拡散モデル（J-23）の詳細な仕組みは J-23 に委ねる。本エントリでは「ノイズから段階的に生成」の一句に留める

## 出典メモ

- openai.com/dall-e-3 — checked 2026-04-29
- OpenAI blog "DALL-E 3 is now available in ChatGPT Plus" — checked 2026-04-29
- OpenAI の GPT Image に関する発表・報道（検索経由）— checked 2026-11-13
- Stage 16 ブリーフ 追補 5（ledgers/stage16_briefs_2026-11.md）— checked 2026-11-13

## 備考

モデル名・提供形態・商用利用条件は時変情報です。商用利用前に利用規約を確認してください。

- **2026-11-13 鮮度監査**：ChatGPT の画像生成は 2025-03 に GPT Image 1（GPT-4o ベース）へ交代しており、「ChatGPT で頼むと DALL-E が動く」は 2025-03 以降は当てはまらないため、本文を過去の話として時点を固定した（一次未確認・検索経由）。旧備考の「評価日時点では ChatGPT 統合が主な利用経路」は上書き
- `version_status` は active → deprecated に変更。D-14 Claude Mythos Preview が後継登場後に deprecated へ変えた前例に合わせ、「後継に交代済みで、新規に勧めない」状態を deprecated と判断した。DALL-E の API の最終提供終了日は未確認
- 著者の「私のコメント」は 2026-04 時点の印象のため触れていない
