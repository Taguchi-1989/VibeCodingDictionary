---
id: D-11
title: Claude 3.5 系
title_reading: クロード サンテンゴ系
category: model
subtype: anthropic
experience_level: hands_on
reader_level: 2-3
importance: B
figure_type: timeline
page_layout: spread_v1
version_status: deprecated
evaluation_date: 2026-04-25
related_terms:
  - Claude 4 系
  - Anthropic
  - Sonnet
  - Artifacts
  - Computer use
status: ready
---

# Claude 3.5 系

## tagline

バイブコーディング普及前夜の主力。Sonnet 3.5 でコード適性が跳ねた世代です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

文章・コード生成と画像理解を担うモデル群です。Sonnet 3.5 でコーディング適性が大きく向上し、Artifacts や Computer use もこの世代で先行公開されました。

## どこで出会うか

現在は 4 系が主力のため、過去の記事で「Sonnet 3.5 で試した」という記述を見かける場面が出会いの入口です。どの版・ティアか把握すると 4 系への移行比較に役立ちます。

## メイン図

### 図の狙い

3.5 系の登場順（3.5 Sonnet → 3.5 Haiku → 3.5 Sonnet v2 → 3.7 Sonnet）を時系列で示し、各版でどんな変化があったかを 1 枚で掴んでもらいます。

### C. 概念図（figure_type: timeline）

- リリース順の 4 つのノード:
  - **3.5 Sonnet**（2024-06）: Sonnet ティアでコーディング適性が大きく跳ねた転換点
  - **3.5 Haiku**（2024-10）: 軽量・高速。小さなタスク向けの廉価帯
  - **3.5 Sonnet v2**（2024-10）: 初代 Sonnet 3.5 を改訂。精度・命令追従を向上
  - **3.7 Sonnet**（2025-02）: 公称番号は 3.7 だが 3.5 系の最終形。Extended Thinking を先行搭載
- 横軸: 2024-06 → 2025-02 の時間軸
- 縦軸方向に Sonnet / Haiku の 2 ティアを薄く引く

## 会話での使い方例

「Sonnet 3.5 でコード適性が跳ねた頃から、AI コーディングの空気が変わりましたね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

3.5 Sonnet がコード適性の転換点になった、4 系登場前の主力世代です。

### 2. うれしさ

Sonnet／Haiku の 2 段構成でタスク規模に応じた使い分けができました。

### 3. 注意点

現在は deprecated 扱い。API 提供は要確認です。

### 4. どこで役立つか

過去記事の再現確認や、3.5 系プロンプトの 4 系移行比較に役立ちます。

### 5. はじめに

3.5 Sonnet が転換点、3.7 Sonnet が 3.5 系の最終形という流れです。

### 6. 深掘り先

Artifacts、Computer use、Claude 4 系。

## 開発フローでの位置（必須）

1. モデル世代を把握する — 4 系（現行）か 3.5 系（過去）かを記事・設定で確認
2. 版・ティアを確認する — Sonnet（中間）か Haiku（軽量）か、また初代か v2 か
3. コードや指示を実行する — Claude.ai / API / Claude Code 経由
4. 結果を評価して移行判断 — 4 系で同等以上が期待できるなら乗り換えを検討

## 関連用語

- Claude 4 系
- Anthropic
- Sonnet
- Artifacts
- Computer use


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 3.5 Sonnet に初代と v2 があり、どちらの話か分かりにくいです。
- 古い LLM が「最新は 3.5 Sonnet」と返し現役把握がずれます。
- Opus が最上位と思われがちですが 3.5 系は Sonnet が先行。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 文章が達者で、実直な印象を受けました。
- 👍 良い点: コーディングタスクに向いていた印象です。
- 👎 ダメな点: 計算の正確性や賢さでは際立った印象はありませんでした。
- 👥 誰向けか: コーディング補助として使う人に向いていましたが、今は後継に譲る印象です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 横軸に時間軸（2024-06 → 2025-02）を引き、4 つのノード（3.5 Sonnet / 3.5 Haiku / 3.5 Sonnet v2 / 3.7 Sonnet）を矢印でつなぐ。3.5 Sonnet の位置に★マーク＋「コード適性が跳ねた」ラベル。3.7 Sonnet の末端に「3.5 系の最終形」注記
- 登場人物: 画面脇に小さく著者キャラクター。3.5 Sonnet ノードを指差して「ここで変わった」と吹き出し
- 吹き出し・心の声: 「バイブコーディング前夜、これで試してた」（過去を振り返る口調）
- 中央に置くキーワード: 3.5 系＝コード適性の転換点、4 系への橋渡し
- 縦方向に Sonnet / Haiku の 2 段レーンを薄く引き、各ノードがどのティアに属するかをドットで示す

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 虫眼鏡アイコン（世代を把握する）
- Step 2: バッジ × 2（Sonnet／Haiku）
- Step 3: 歯車アイコン（実行）
- Step 4: 矢印＋乗り換えマーク（4 系移行を検討）
- 矢印: 把握 → 選ぶ → 実行 → 評価 の一方向フロー


## コミュニティ補完メモ

- 現行主力の 4 系総論は D-12 で扱います。本エントリは「3.5 系」という過去の世代を歴史・移行文脈で整理します。
- 3.7 Sonnet は公称上 3.7 ですが 3.5 系の延長として扱い、本エントリでカバーします。別立てはしません。
- Artifacts / Computer use の詳細は各専門エントリへ誘導します。
- 4.5 系の詳細は D-13 へ。

## 出典メモ

- https://www.anthropic.com/news/claude-3-5-sonnet — checked 2026-04-25
- https://www.anthropic.com/news/claude-3-5-haiku — checked 2026-04-25
- https://www.anthropic.com/news/claude-3-7-sonnet — checked 2026-04-25
- https://docs.anthropic.com/en/docs/about-claude/models/overview — checked 2026-04-25

## 備考

- 3.7 Sonnet は番号こそ 3.7 ですが、Anthropic は 3.5 系からの継続発展として位置づけており、本エントリにまとめています。4 系とは別世代です。
- モデルの API 提供継続状況・価格は時変情報です。本番運用前に公式ページで最新状況を確認してください（evaluation_date: 2026-04-25）。
