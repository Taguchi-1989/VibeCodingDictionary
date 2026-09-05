---
id: G-50
title: Evals
title_reading: エバルス
category: term_llm
subtype: evaluation
experience_level: partial
reader_level: 3
importance: C
figure_type: workflow
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-09-05
related_terms:
  - LLM-judge
  - SWE-Bench
  - オブザーバビリティ
  - HITL
  - ハルシネーション
status: needs_review
---

# Evals

## tagline

evaluations の略。AI の出来を自分の仕事の基準で測るしくみです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

モデルやプロンプトの出来を、決めた基準で繰り返し測るしくみです。決定的な判定・統計的な判定・LLM-as-a-judge（G-51）の 3 種を、安く確実な順に使い分けます。

## どこで出会うか

AI に仕事を任せる前に、合格ラインを 5 個書き出すような場面で使います。プロンプトを変えるたび毎回目で確認するのは大変なので、決めた基準で自動的に測り直す土台として使われます。

## メイン図

### 図の狙い

「良し悪しの基準を書き出して残す」作業が、良し悪しをその場の感覚で判断するのとどう違うかを見せる図です。

## 会話での使い方例

「まず合格ラインを5個書き出して、evalsとして残しておきましょう。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

仕事の合格基準を、自分で決めて測る物差しです。

### 2. うれしさ

感覚ではなく数字で良し悪しを判断できます。

### 3. 注意点

指標を先に決めると本番の失敗を見落とします。

### 4. どこで役立つか

AI に仕事を任せる前の合否ラインづくりに向きます。

### 5. はじめに

まず失敗例を 5 個集めて基準にします。

### 6. 深掘り先

LLM-as-a-judge、ゴールデンデータセット

## 開発フローでの位置（必須）

1. 失敗例を集める — 本番ログから典型的な失敗を拾います。
2. 基準を書き出す — 合格ラインを具体的な項目として言語化します。
3. 評価器を選ぶ — 決定的・統計的・AI 採点の順で試します。
4. 繰り返し測る — 基準を変えず、プロンプト変更のたび測り直します。

## 関連用語

- LLM-judge
- SWE-Bench
- オブザーバビリティ
- HITL
- ハルシネーション

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

- 描く内容: 「合格ライン」を書いたチェックリストを手に持つ人が、AI の出力を横に並べて 1 項目ずつ照らし合わせている様子
- 登場人物（いれば）: チェックリストを持つ担当者、画面から出てくる AI の出力
- 吹き出し・心の声: 担当者「なんとなく良さそう、じゃなくて。ここが基準」
- 中央に置くキーワード/ラベル: 合格ライン／決定的・統計的・LLM-as-a-judge

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ログの束から失敗例を拾い上げる虫眼鏡
- Step 2 のアイコン/絵柄: チェックリストに項目を書き足すペン
- Step 3 のアイコン/絵柄: 決定的・統計的・AI 採点の 3 レーン分岐
- Step 4 のアイコン/絵柄: 同じ基準を何度も当てる矢印のループ

## コミュニティ補完メモ

- G-51 LLM-as-a-judge との住み分け：G-50 は evals 全体（決定的・統計的・LLM-as-a-judge の 3 種を束ねる考え方）、G-51 は判定役を AI にするやり方の詳細です。数字（一致率の目安など）は G-51 側に置きます
- E 章（ベンチマーク）との住み分け：ベンチマークは「業界共通の物差し」、evals は「自分の仕事に合わせて自分で作る物差し」。E-1 SWE-Bench は他人が作った点数の読み方の代表例として関連用語に置きます
- J-133 オブザーバビリティとの接続：本番のトレースは evals 用データの原料になります（bottom-up 設計の出発点）
- J-134 Human-in-the-loop（HITL）との接続：evals で拾いきれない境界事例を人の判断に回す先として関連づけます

## 出典メモ

- https://deepeval.com/blog/llm-as-a-judge — checked 2026-09-05
- https://galtea.ai/blog/llm-evaluation-complete-guide — checked 2026-09-05
- https://www.getmaxim.ai/articles/building-a-golden-dataset-for-ai-evaluation-a-step-by-step-guide/ — checked 2026-09-05

## 備考

先に指標を決めてからデータを作る（top-down）と本番で転びやすく、先に実際の失敗を集めてから指標を設計する（bottom-up）方が本番の壊れ方を当てやすい、という整理が 2026 年時点の実務側の共通見解です。特定の評価 SaaS 名（Braintrust / Arize / Langfuse 等）は本文では挙げていません。
