---
id: G-14
title: Thinking モデル
title_reading: シンキングモデル
category: term_llm
subtype: technique
experience_level: partial
reader_level: 3
importance: B
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - o1 系
  - Extended Thinking
  - Reasoning
  - LLM
  - プロンプト
status: ready
---

# Thinking モデル

## tagline

回答前に内部で推論を重ね、複雑な問いに粘り強く向き合うモデルの総称です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

プロンプトを受け取った後、すぐ出力せず内部で思考ステップを積んでから回答します。論理・数学・コード最適化など一発で答えが出にくい問題で精度が上がります。

## どこで出会うか

ChatGPT（B-3）のモデル選択欄や API のモデル名に「o1」「o3」「Gemini Thinking」「Extended Thinking」と出てきます。応答が遅い場面で「なぜ時間がかかるのか」が最初のつまずきになりがちです。

## メイン図

### 図の狙い

通常モデルと Thinking モデルを人物の吹き出しで対比し、「考える時間の違い」を直感的に掴んでもらいます。

### B. 登場シーン（figure_type: comparison）

- シーン1: 通常モデル — 人物がプロンプトを入れると即座に吹き出しで「はい！」と回答する
- シーン2: Thinking モデル — 人物が同じプロンプトを入れると、モデルが「…考え中…」と思考バブルを出した後に回答する
- 並べる基準: 同じ入力・異なる内部処理時間の対比

## 会話での使い方例

「難しいロジックは Thinking モデルに投げると、時間はかかりますが精度が上がることがあります。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

回答前に内部推論を重ねる、精度重視型のモデルです。

### 2. うれしさ

複雑な論理・数学で通常モデルより正確になることがあります。

### 3. 注意点

内部推論のぶん応答が遅く、料金も高くなりがちです。

### 4. どこで役立つか

バグ特定・数式検証・多段階ロジックの問題に向きます。

### 5. はじめに

各社で呼び方が違う点と、速さとのトレードオフを把握します。

### 6. 深掘り先

o1 系、o3 系、推論時スケーリング（J-130）

## 開発フローでの位置（必須）

1. 問題の難易度を判断する — 論理・数学・複雑なコードかどうか確認します
2. モデル種別を選ぶ — 通常か Thinking モデルかをコストと精度で選択します
3. バリアントを絞る — 各社の軽量版・上位版から用途に合うものを選びます
4. 実行と評価 — 応答時間・品質・料金を確認し、必要なら切り替えます

## 関連用語

- o1 系
- Extended Thinking
- Reasoning
- LLM
- プロンプト


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 昔はプロンプトで誘導していたが、Thinking Model なら自動でやってくれます
- 「Thinking Model」と「Reasoning Model」の違いが結構難しいです
- 速さより精度がほしいときは、基本これを選ぶことになります
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: o1 登場でベンチマークスコアがぐっと伸びたのが記憶に残っています
- 👍 良い点: 今のモデルを使う人なら知らず知らず使っているくらい当たり前です
- 👎 ダメな点: 速度が遅いので、ファストモデルとの使い分けも考えたいです
- 👥 誰向けか: 最近は頭出しもしてくれるので、幅広く使いやすくなりました
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左列「通常モデル」、右列「Thinking モデル」を横並び対比。入力は同じプロンプト、出力のタイミングだけが異なる
- 登場人物: 中央に人物キャラクター、左右を交互に指差しながら「どっちにする？」と吹き出し
- 吹き出し・心の声: 通常モデル側「すぐ答えます！」、Thinking モデル側に「…じっくり考え中…」の思考バブル → その後に回答
- 中央に置くキーワード/ラベル: 速さ vs 深さ

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 天秤アイコン（難易度判断）
- Step 2 のアイコン/絵柄: 分岐矢印（通常 or Thinking）
- Step 3 のアイコン/絵柄: バッジ複数（軽量版・上位版）
- Step 4 のアイコン/絵柄: メーター＋時計アイコン（応答時間・料金の評価）
- 矢印で示す流れの意図: 「判断 → 選択 → 絞り込み → 評価」の 4 段階


## コミュニティ補完メモ

- o1 系（D-22）は OpenAI の代表的 Thinking モデル実装。本エントリは「Thinking モデル」という概念・総称を扱い、各社固有の実装には踏み込みません。
- o3 系（D-23）は o1 系の進化形。いずれも本エントリの「深掘り先」として名前を出すにとどめます。
- Claude の Extended Thinking（D-13 関連）、Gemini の Deep Think（D-2 関連）も同概念ですが、各社名称が違う点をコミュニティ補完で説明します。
- 「各社で呼び方が違う（reasoning model / thinking model / extended thinking）が、本書では Thinking モデルで統一」という整理を備考にも残します。


## 出典メモ

- https://docs.anthropic.com/ja/docs/build-with-claude/extended-thinking — checked 2026-04-29
- https://openai.com/index/learning-to-reason-with-llms — checked 2026-04-29
- https://ai.google.dev/gemini-api/docs/thinking — checked 2026-04-29


## 備考

本書では「Thinking モデル」に統一。各社の呼称は reasoning model（OpenAI）、extended thinking（Anthropic）、Deep Think（Google）など異なります。応答速度と料金は時変情報です。evaluation_date: 2026-04-29 時点の情報をもとにしています。
