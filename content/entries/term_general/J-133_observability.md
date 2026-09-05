---
id: J-133
title: オブザーバビリティ
title_reading:
category: term_general
subtype: agent_ops
experience_level: research_only
reader_level: 4
importance: C
figure_type: workflow
page_layout: spread_v1
start_date:
end_date:
version_status: preview
pricing_note: none
evaluation_date: 2026-09-05
related_terms:
  - Evals
  - Token
  - Tool Use
  - デバッグ
  - モデルルーティング
status: needs_review
---

# オブザーバビリティ

## tagline

AI が何をどう処理したかを、後から追える状態にしておくことです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

AI が何にどれだけ時間とお金を使ったかを、トレースという記録として残す考え方です。呼び出したモデル・叩いたツール・使ったトークン数・待ち時間まで、1 回のやり取り単位で後から追えるようにします。

## どこで出会うか

エージェントが途中で止まったり、費用が急に増えたりしたときの原因調査で出会います。Langfuse・LangSmith・Arize といった監視ツールの画面や、OpenTelemetry を使った計装の話として登場します。

## メイン図

### 図の狙い

1 回の依頼が「モデル → ツール → モデル」と渡り歩く様子を、時間軸のトレースとして描き、どこで詰まったかを指させることを伝えます。

## 会話での使い方例

「トレース見たら、どのツール呼び出しで時間が溶けてるか一目でわかりますよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

処理の流れを記録し、後から追跡できる状態にします。

### 2. うれしさ

「なんとなく不調」で終わらせず、原因を指させます。

### 3. 注意点

OpenTelemetry の GenAI 規約はまだ実験段階です。

### 4. どこで役立つか

失敗調査や費用の内訳確認で役立ちます。

### 5. はじめに

1 回のやり取りの記録＝トレースから理解します。

### 6. 深掘り先

OpenTelemetry、GenAI セマンティック規約、トレース

## 開発フローでの位置（必須）

1. 計装する — モデル呼び出しやツール呼び出しに記録を仕込みます
2. トレースを集める — OTLP 対応の監視ツールへ送ります
3. 失敗を追う — 詰まった箇所やコストの内訳を確認します
4. 評価へつなぐ — 集めた記録を Evals の材料に回します

## 関連用語

- Evals
- Token
- Tool Use
- デバッグ
- モデルルーティング

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

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 1 回の依頼が「人 → エージェント → モデル → ツール → モデル → 人」と渡り歩く時間軸のトレース。各矢印に所要時間・トークン数の小さなラベルを添える
- 登場人物（いれば）: エージェントを運用する担当者（画面のトレース表示を見ている）
- 吹き出し・心の声: 「このツール呼び出しだけ 8 秒かかってる……ここが原因か」
- 中央に置くキーワード/ラベル: トレース

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: コードに計測用のタグを埋め込む手つき
- Step 2 のアイコン/絵柄: 記録がダッシュボードへ流れ込む矢印
- Step 3 のアイコン/絵柄: 赤く光る詰まり箇所を指差す
- Step 4 のアイコン/絵柄: 集めた記録が Evals の箱へ積まれる

## コミュニティ補完メモ

- G-50 Evals との住み分け：オブザーバビリティは「記録を残す」側、Evals は「その記録を使って良し悪しを測る」側。トレースは評価データの原料という位置づけで J-133 側から G-50 へ橋渡しする
- J-109 モデルルーティングとの関係：どのモデルにいくら払ったかの内訳を見る場面で接続する
- F-46 デバッグとの違い：デバッグはコードの不具合を追う一般的な行為、オブザーバビリティは AI の処理過程を継続的に可視化する仕組み

## 出典メモ

- https://openobserve.ai/blog/opentelemetry-for-llms/ — checked 2026-09-05
- https://langfuse.com/integrations/native/opentelemetry — checked 2026-09-05
- https://www.marktechpost.com/2026/08/09/top-llm-observability-and-evaluation-platforms-in-2026-langfuse-langsmith-braintrust-arize-and-more-compared/ — checked 2026-09-05

## 備考

OpenTelemetry の GenAI セマンティック規約は 2026 年 3 月時点で大半が experimental（実験段階）で、`gen_ai.*` 属性の多くに Development の安定性バッジが付いています。メジャーバージョンを上げずに属性名が変わる可能性があるため、`version_status: preview` としています。ツール名（Langfuse・LangSmith・Arize・Braintrust・AWS Bedrock AgentCore・Datadog）は本文では例示に留め、優劣の比較はしません。
