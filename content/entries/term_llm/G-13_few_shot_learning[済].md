---
id: G-13
title: Few-shot Learning
title_reading: フューショットラーニング
category: term_llm
subtype: technique
experience_level: partial
reader_level: 3
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Prompt Engineering
  - Zero-shot
  - One-shot
  - Context Engineering
  - Fine-tuning
status: ready
---

# Few-shot Learning

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

数個の例示を渡すだけで AI の出力を意図した形に近づける手法です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM への入力に、入出力の例を数件そのまま添える方法です。モデルを再学習させずに、望む形式やスタイルへ出力を寄せられます。

## どこで出会うか

ChatGPT や Claude に「以下の形式で答えてください。例1…例2…」と伝えるときが典型例です。Context Engineering の代表的な実装として紹介されます。

## メイン図

### 図の狙い

Zero-shot・One-shot・Few-shot の 3 パターンを横に並べ、例示の数が増えるほど出力が整うことを視覚的に伝える。

### B. 登場シーン（figure_type: comparison）

- シーン1（Zero-shot）: 例なしで「ポジティブかネガティブか答えて」と入力する人物。AI が形式不定の返答をする
- シーン2（One-shot）: 1 件の例を添えて送る人物。AI が例に沿った形式で返す
- シーン3（Few-shot）: 3 件の例を添えて送る人物。AI が安定してラベルのみを返す
- 並べる基準: 例示の件数と出力の安定度の対比

## 会話での使い方例

「Few-shot で例を 3 件渡したら、出力形式がきれいに揃いますよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

例示をプロンプトに含めて、LLM の出力形式やスタイルを誘導します。

### 2. うれしさ

モデルの重みを変えずに挙動を調整できるため、手軽さとコスト効率が両立します。

### 3. 注意点

例示が偏ると出力も偏るため、例の質と多様性が精度を左右しやすいです。

### 4. どこで役立つか

定型フォーマットの分類・抽出タスクで効果が出やすいです。

### 5. はじめに

Zero-shot との対比で「例あり・なし」の差を試すと効果を体感できます。

### 6. 深掘り先

Prompt Engineering、Context Engineering、Zero-shot

## 開発フローでの位置（必須）

1. タスク定義 — 期待する入出力の形式をゴールとして整理する
2. 例の準備 — 実際の入出力ペアを 2〜5 件選び、質と多様性を確認
3. プロンプトに組み込む — 例示を指示の冒頭に配置する
4. 出力を評価 — Zero-shot との比較で例示の効果を確認する
5. 例数を調整 — Token 消費を踏まえて必要最小数に絞る

## 関連用語

- Zero-shot / One-shot
- Prompt / Context Engineering

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- チャットで初めて認識した程度で、チューニング的な概念と捉えています
- 自分の仕事に効くのか、実用に持っていけるかが難しいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回初めてちゃんと見たかも。
- 👍 良い点: Claude や GPT の応答をその場で調整できる点が良さそうです。
- 👎 ダメな点: Gemini など回答が過去に引っ張られ、エコーチェンバー化しやすいです。
- 👥 誰向けか: AI の出力をメタ的に扱っていく人向け。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左から右へ「Zero-shot／One-shot／Few-shot」の 3 列を並べた対比図。列ごとにプロンプト欄と AI の返答欄を示す
- 登場人物: ノート PC に向かうビジネスパーソン（1 人）。3 列とも同じ人物が例示の数だけ異なる入力をする演出
- 吹き出し・心の声: Zero-shot 列「形式がバラバラ…」、Few-shot 列「毎回同じ形式で返ってくる！」
- 中央に置くキーワード/ラベル: 「例示の数が精度を決める」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ゴールと出力形式を付箋に書く人
- Step 2 のアイコン/絵柄: 入出力ペアのカードを選ぶ手
- Step 3 のアイコン/絵柄: プロンプト欄に例を貼り付けるキーボード操作
- Step 4 のアイコン/絵柄: Zero-shot と Few-shot の出力を並べて見るルーペ
- Step 5 のアイコン/絵柄: 不要な例を削るハサミ
- 矢印で示す流れの意図: 「定義 → 例の選定 → 組み込み → 評価 → 最適化」の順で進む

## コミュニティ補完メモ

- G-10 Prompt Engineering との住み分け：Few-shot は Prompt Engineering の中核技術の 1 つ。本エントリは「例示を使う」という操作に絞る。指示文全体の設計原則は G-10 へ誘導する
- G-11 Context Engineering との住み分け：Few-shot は Context に例を置く実装手段。Context 全体の設計思想は G-11 へ誘導する
- G-6 One-shot との住み分け：One-shot は例示が 1 件の特殊ケース。Few-shot（複数例）との連続性を示す兄弟エントリ
- J-16 Fine-tuning との違い：Few-shot は重みを変えず例示で誘導。Fine-tuning はモデルの重みを更新する別アプローチ

## 出典メモ

- arXiv:2005.14165 "Language Models are Few-Shot Learners"（GPT-3 論文）— checked 2026-04-29
- docs.anthropic.com（Anthropic プロンプトガイド） — checked 2026-04-29
- platform.openai.com/docs/guides/prompt-engineering — checked 2026-04-29

## 備考

- Few-shot の「few」は文脈により 2〜10 件程度を指すことが多いが、明確な定義はなく、One-shot（1 件）・Zero-shot（0 件）との連続体として理解するのが自然
- 例示の件数が増えると Token を消費するため、長い文書タスクでは件数と Context 長のトレードオフが生じる
