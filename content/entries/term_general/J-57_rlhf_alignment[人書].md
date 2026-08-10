---
id: J-57
title: RLHF・アラインメント
title_reading: アラインメント
category: term_general
subtype: ethics_law
experience_level: partial
reader_level: 3-4
importance: B
figure_type: flow
page_layout: spread_v1
start_date: 2022-03
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-08-10
related_terms:
  - LLM
  - Fine-tuning
  - Hallucination
  - Sycophancy
status: needs_review
---

# RLHF・アラインメント

<!--
バイブコーディング図鑑 スケルトン雛形 v1（2026-04-28 追加）
- 構造だけ先に置いた状態。本文は status を `drafting` に上げた段階で entry-writer が埋める
- validator は status: skeleton を archived/sample と同様にスキップする
- tagline には entry_candidates.md の「一言」を仮で流し込んでいる（本書きで磨き直す）

YAML 補足（本書きで埋める／見直す欄）:
- subtype: candidate.csv の subtype 列を流し込み済み（後で見直す）
- experience_level: hands_on / partial / research_only
- reader_level: 1〜6
- figure_type: before_after / structure / comparison / workflow / timeline（仮で structure を入れている）
- version_status: active / preview / deprecated（時変なら埋める）
- pricing_note: none / paid / freemium（時変なら埋める）
- related_terms: 3〜5 個目安
- status: skeleton → drafting → needs_review → ready
-->

## tagline

<!-- 25〜60 字（推奨 30〜38、略称展開を含む場合 35〜50）。
     タイトルが略称・ヌメロニム（MCP / a11y / LLM 等）なら冒頭に「{展開} の略。」を入れる（2026-04-28 追加）。
     例: `Model Context Protocol の略。LLM とツール・データをつなぐ標準規格です。` -->

人間のフィードバックによる強化学習の略。人間の評価を報酬に AI の振る舞いを整える手法です。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

<!-- 60〜200 字（推奨 80〜150）。役割と仕組みを 2〜4 文で。本書きで埋める。 -->

アラインメント（AI の振る舞いを人間の意図や価値観に合わせる取り組み）の代表的な手法です。人が複数の回答を比べて順位をつけ、その評価を報酬として学習させることで、望ましい応答に近づけます。

## どこで出会うか

<!-- 60〜200 字（推奨 80〜150）。読者が遭遇する具体シーン。本書きで埋める。 -->

2022 年の InstructGPT で効果が示され、ChatGPT のような対話 AI が実用的になった転機とされます。人の代わりに AI が評価する Constitutional AI や、手順を簡略化した DPO なども広く使われています。


## メイン図

### 図の狙い

<!-- 1〜2 文。この図で読者に何を掴んでもらうか。本書きで埋める。 -->

素直な受け答えが「人の評価を学習した結果」であることを、評価する人と学習後の AI の対比で示します。

## 会話での使い方例

<!-- 25〜50 字（推奨 30〜40）、1 文。本書きで埋める。 -->

「RLHF のおかげで ChatGPT は素直に指示へ従うようになったんですよね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

<!-- 15〜40 字、1 文。本書きで埋める。 -->

AI の振る舞いを人間の意図に合わせる学習手法です。

### 2. うれしさ

<!-- 15〜40 字、1 文。本書きで埋める。 -->

対話 AI が指示に素直に従いやすくなります。

### 3. 注意点

<!-- 15〜40 字、1 文。本書きで埋める。 -->

評価者の偏りがそのまま挙動に反映されます。

### 4. どこで役立つか

<!-- 15〜40 字、1 文。本書きで埋める。 -->

チャット AI の使い勝手や応答の質を左右します。

### 5. はじめに

<!-- 15〜40 字、1 文。本書きで埋める。 -->

ChatGPT が急に使いやすくなった理由の一つと知ること。

### 6. 深掘り先

<!-- 15〜50 字、1〜3 語をカンマ区切り。本書きで埋める。 -->

Constitutional AI、DPO、RLAIF


## 開発フローでの位置（必須）

<!-- 4〜5 ステップ。本書きで埋める。 -->

1. 事前学習 — 大量のテキストで基礎的な言語能力を身につけます。
2. 教師ありファインチューニング — 手本となる回答例で受け答えの形を整えます。
3. RLHF — 人の評価を報酬にして望ましい応答へ近づけます。
4. リリース後の観測 — 迎合や偏りが出ていないか継続的に確認します。
5. 利用者の検証 — 出力を鵜呑みにせず自分でも確かめる習慣を持ちます。


## 関連用語

<!-- 3〜5 個。本書きで埋める。YAML の related_terms と一致させる。 -->

- LLM
- Fine-tuning
- Hallucination
- Sycophancy


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

### メイン図（左ページ中段 / figure_type: flow）

- 描く内容: 左に「複数の AI 回答を見比べて順位をつける評価者」、右に「素直な受け答えを返す学習後の AI」の流れ図。矢印で「評価 → 報酬 → 学習」の循環を示す
- 登場人物: 腕組みして 2 つの回答を見比べる評価者（人物）と、吹き出しで応答する AI アイコン
- 吹き出し・心の声: 評価者「こっちの答え方のほうが親切だな」／AI アイコン「その評価、覚えておきます」
- 中央に置くキーワード/ラベル: RLHF（人の評価で学習）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 本の山（事前学習）
- Step 2 のアイコン/絵柄: お手本カード（教師ありファインチューニング）
- Step 3 のアイコン/絵柄: 星の評価（RLHF）
- Step 4 のアイコン/絵柄: 虫眼鏡＋グラフ（リリース後の観測）
- Step 5 のアイコン/絵柄: チェックマークを持つ人物（利用者の検証）


## コミュニティ補完メモ

- J-52 Sycophancy との住み分け：J-52 は RLHF が引き起こす副作用（迎合しすぎる挙動）の解説に特化。本エントリは RLHF・アラインメントという手法・目的そのものの説明に絞り、副作用の詳細は J-52 へ誘導する
- J-50 AI 倫理（未執筆）との住み分け：AI 倫理は設計・社会的影響を含む広い枠組み。本エントリはそのうちモデルの学習段階で使われる具体的な技術に絞る
- J-51 Hallucination との住み分け：Hallucination は事実と異なる生成という別現象。RLHF は挙動全般を整える手法であり、Hallucination を完全には防げない点は「注意点」で軽く触れるに留める
- G-10 Prompt Engineering との接続：ユーザー側の工夫（プロンプト）と、モデル側の学習（RLHF）は補完関係にある。詳細は G-10 へ譲る

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Ouyang et al., "Training language models to follow instructions with human feedback" (InstructGPT), arXiv:2203.02155 — checked 2026-08-10
- Anthropic「Constitutional AI: Harmlessness from AI Feedback」<https://www.anthropic.com/news/claudes-constitution> — checked 2026-08-10


## 備考

- InstructGPT の論文提出は 2022 年 3 月。ChatGPT（2022 年 11 月公開、H-53）の直接の前身にあたる研究として start_date に採用した
- DPO（Direct Preference Optimization）・RLAIF（AI フィードバックによる強化学習）は「深掘り先」止まりとし、手法の詳細解説は別エントリの候補として残す
- Sycophancy（迎合、J-52）の原因説明は RLHF 側でも軽く触れているが、詳しい現象解説は J-52 に委ねてスコープの重複を避けた
