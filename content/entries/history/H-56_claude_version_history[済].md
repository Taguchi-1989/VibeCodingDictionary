---
id: H-56
title: Claude のバージョン史
category: history
subtype: timeline
experience_level: research_only
reader_level: 2-3
importance: C
figure_type: timeline
page_layout: spread_v1
start_date: 2023-03
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Claude
  - Anthropic
  - Claude 3 系
  - Claude 4 系
  - Extended Thinking
status: ready
---

# Claude のバージョン史

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

Anthropic が 2023 年以降リリースしてきた Claude シリーズの版数と命名変遷をまとめます。

## 何をしてくれるか

Claude のバージョン史を知ると各世代の特徴を整理できます。Haiku／Sonnet／Opus という命名体系は 3 系以降で定着しました。

## どこで出会うか

API のモデル名や料金表を見るときに、世代の違いが気になります。モデル選定の資料づくりや社内の相談でも、版数の話題がよく出ます。

## メイン図

### 図の狙い

2023 年から 2026 年へ続く横軸タイムラインで、各バージョンの登場時期と命名ルールを一覧できるようにします。

## 会話での使い方例

「Extended Thinking は 3.7 Sonnet から搭載されました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Claude 各世代の登場時期と特徴を年表でまとめます。

### 2. うれしさ

モデル名を見たとき世代と能力の見当がつきます。

### 3. 注意点

版数は増え続けるため、評価日以降の追加リリースは未反映です。

### 4. どこで役立つか

API のモデル選定や社内ツール更新の判断材料になります。

### 5. はじめに

Haiku／Sonnet／Opus の三段構えと世代番号の読み方が起点です。

### 6. 深掘り先

Claude 3 系、Claude 4 系、Extended Thinking

## 開発フローでの位置（必須）

1. 要件整理 — 処理量・速度・コスト感から世代と tier を絞ります
2. モデル選定 — Haiku（速・安）か Sonnet（主力）か Opus（推論重視）かを決めます
3. API 呼び出し — `claude-sonnet-4-6` のようにモデル名を文字列で指定します
4. 評価・切り替え — 新バージョンが出たら性能比較して乗り換えを検討します

## 関連用語

- Claude
- Anthropic
- Claude 3 系
- Claude 4 系
- Extended Thinking


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Opus は料金が高く、Max まで踏み込まないと実力感をつかみにくいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Sonnet 3.5 が「そこそこ賢いモデル」として話題になっていた印象です
- 👍 良い点: Opus 4.5 系はコーディング用途でかなり手応えがありました
- 👎 ダメな点: Sonnet 4 は計画を立てるのに実装精度が追いつかず台パンしたくなりました
- 👥 誰向けか: 過去バージョンの実力感を把握したい人に向いています
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 2023-03 から 2026-04 までの横軸タイムラインに各バージョンを並べる
- 登場人物: メガネをかけたエンジニア風の人物が年表を指差している
- 吹き出し・心の声:「3.5 Sonnet がコーディングで話題になったんだ」
- 中央に置くキーワード/ラベル: Claude 1 / 2 / 3 / 3.5 / 3.7 / 4 系

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チェックリスト
- Step 2 のアイコン/絵柄: 天秤（コスト vs 性能）
- Step 3 のアイコン/絵柄: コードエディタ画面
- Step 4 のアイコン/絵柄: 比較グラフ


## コミュニティ補完メモ

- B-2 Claude はサービス全体の紹介。本エントリはバージョン変遷の年表に特化
- D-10 Claude 3 系は各ファミリーの詳細スペックを扱う
- D-11 Claude 3.5 系は Artifacts や Extended Thinking の詳細を扱う
- D-12 Claude 4 系は Claude Code GA 以降の詳細を扱う
- C-2 Anthropic は会社・理念の紹介。本エントリはモデル史のみ

2025-05 の Claude 4 系（Opus 4 / Sonnet 4）と Claude Code の同時 GA は D-12 が詳細を持つ。本エントリでは「登場時期と命名ルール」の年表視点のみ記述。

## 出典メモ

- Anthropic News (anthropic.com/news) — checked 2026-04-30
- Anthropic Docs: Models (docs.anthropic.com/en/docs/about-claude/models) — checked 2026-04-30

## 備考

- 2023-03: Claude 1（API 限定、100K コンテキストが当時の目玉）
- 2023-07: Claude 2（一般向け claude.ai 開始）
- 2024-03: Claude 3 ファミリー（Haiku / Sonnet / Opus 三段構え、200K コンテキスト）
- 2024-06: Claude 3.5 Sonnet（コーディング・推論で GPT-4o と話題に）、Artifacts 同時投入
- 2024-10: Claude 3.5 Haiku（軽量化）
- 2025-02: Claude 3.7 Sonnet（Extended Thinking 内蔵）
- 2025-05: Claude 4 系（Opus 4 / Sonnet 4）、Claude Code 同時 GA
- 2025-09: Claude 4.5 Sonnet、2025-11: Claude 4.6 Sonnet、2026-04: Claude 4.7 Opus
- 評価日以降の新リリースは反映されていないため、現時点の情報は Anthropic 公式ページで確認が必要
