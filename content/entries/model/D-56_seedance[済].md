---
id: D-56
title: Seedance
title_reading: シードダンス
category: model
subtype: video_generation
experience_level: partial
reader_level: 3-4
importance: D
figure_type: comparison
page_layout: spread_v1
start_date: 2025-06-01
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Sora
  - Veo
  - Kling
  - fal.ai
  - 拡散モデル
status: ready
---

# Seedance

## tagline

ByteDance（中国）が開発する動画生成モデル。テキスト・画像から最大 1080p の短尺動画を生成します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

テキストや画像を入力すると、5〜10 秒前後の動画を生成します。表情の細やかさやカメラ移動、物理的な自然さが評価され、広告素材やコンテ確認など短尺動画の試作に使われます。

## どこで出会うか

中国では Doubao（豆包）や Jimeng（即梦）アプリ経由で利用できます。海外では fal.ai や Replicate などの MaaS（モデルアズアサービス）経由で API が公開されており、コスト比較の場面でよく名前が挙がります。

## メイン図

### 図の狙い

Seedance がテキスト・画像から動画を出力するまでの流れと、競合モデルとのコスト・品質の位置づけを示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: マーケターが fal.ai で 6 秒広告素材を試作する
- シーン2: クリエイターが Sora／Veo と画質・価格を横比較する
- シーン3: 開発者が API を呼んで動画生成をプロトタイプに組み込む
- 並べる基準: 用途（試作／比較／組み込み）

## 会話での使い方例

「Seedance Pro で広告 6 秒動画を試作したら、Veo より安く出ました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

テキスト・画像から短尺動画を生成するモデルです。

### 2. うれしさ

表情やカメラ移動の自然さをコスパよく得られます。

### 3. 注意点

生成できるのは 10 秒前後の短尺動画が中心です。

### 4. どこで役立つか

広告・SNS 向け短尺素材の試作フェーズに向いています。

### 5. はじめに

ByteDance が開発し、fal.ai 経由で試せることを押さえましょう。

### 6. 深掘り先

Sora, Veo, Kling

## 開発フローでの位置（必須）

1. 企画・構成 — 動画の尺・カット・セリフをテキストで整理します
2. プロンプト入力 — fal.ai 等で Seedance にテキストや参照画像を送ります
3. 生成・確認 — 出力動画の表情・動き・物理感を目視でチェックします
4. 比較・採用判断 — Sora や Veo と品質・コストを比べて素材を選定します

## 関連用語

- Sora
- Veo
- Kling
- fal.ai
- 拡散モデル

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 中国国内向けのアナウンスがあり、ニュースベースでしか目にしていません。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Sora との優劣は不明ですが、良い動画が作れる印象です。
- 👍 良い点: ベンチマークが高いです。
- 👎 ダメな点: 中華系ならではの警戒感があり、映画レベルはまだ先の印象です。
- 👥 誰向けか: テレビや映画関係者向けかなと思います。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: テキスト入力 → Seedance → 動画出力の流れと、Sora・Veo・Kling との比較表（品質 / コスト）
- 登場人物（いれば）: マーケター担当者がスマホで広告動画を確認している様子
- 吹き出し・心の声: 「Veo より安くできた！」「表情の動きが自然ですね」
- 中央に置くキーワード/ラベル: Seedance 1.0 Pro

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 企画メモ・テキスト
- Step 2 のアイコン/絵柄: fal.ai の入力画面
- Step 3 のアイコン/絵柄: 動画再生プレビュー
- Step 4 のアイコン/絵柄: Sora / Veo との比較スコア
- 矢印で示す流れの意図: 試作から採用判断までの一連のサイクル

## コミュニティ補完メモ

- Sora（D-52）との住み分け：Sora は OpenAI 製で品質面が先行するが価格が高い。Seedance はコスパ比較の文脈で登場することが多い
- Veo（D-53）との住み分け：Veo は Google DeepMind 製。Seedance と Veo はともに「Sora 対抗」として英語圏で比較される
- Kling（Kuaishou 製）との住み分け：同じ中国系動画生成モデル。Kling との比較がコミュニティで頻出する
- Doubao・Jimeng との関係：ByteDance の総合 AI ブランドが Doubao。Jimeng は画像・動画特化アプリ。Seedance はその動画生成モデル名

## 出典メモ

- fal.ai Seedance モデルページ — checked 2026-04-30
- ByteDance Seedance 1.0 公式アナウンス — checked 2026-04-30

## 備考

- Seedance 1.0 / 1.0 Pro が 2025 年中盤に公開。Pro は高品質版
- 中国本土向けは Doubao・Jimeng 経由、海外向けは Volcano Engine / fal.ai / Replicate で API 提供
- 生成動画の最大解像度は 1080p、尺は 5〜10 秒前後（evaluation_date: 2026-04-30 時点）
