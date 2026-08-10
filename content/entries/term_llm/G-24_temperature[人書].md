---
id: G-24
title: Temperature
title_reading: テンパラチャー
category: term_llm
subtype: basic
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-08-10
related_terms:
  - LLM
  - Context
  - System Prompt
  - Prompt Engineering
status: needs_review
---

# Temperature

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

出力のばらつきを決める数値設定です。低いほど手堅く、高いほど多様になります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM が次の単語をどれだけ大胆に選ぶかを調整します。値を低くすると確率の高い単語を選びやすく、手堅い答えになります。値を高くすると表現の幅は広がりますが、話が逸れることもあります。

## どこで出会うか

ChatGPT や Claude、Gemini の API 設定画面や詳細設定メニューで目にします。要約やコード生成は低め、アイデア出しは高めにする使い分けが定番です。

## メイン図

### 図の狙い

同じ質問を投げても、Temperature の高低で回答の顔つきが変わることを、低め・高めの 2 コマで見せる。

### B. 登場シーン（figure_type: comparison）

- シーン1（低め設定）: 資料の要約を頼んだ人物、AI が毎回ほぼ同じ手堅い要約を返す
- シーン2（高め設定）: キャッチコピー案を頼んだ人物、AI が回答のたびに違う案を返す
- 並べる基準: 同じ依頼を Temperature の値だけ変えて実行した対比

## 会話での使い方例

「要約は Temperature を低めにして、事実からブレないようにしています。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

出力の多様性とランダム性の強さを決める調整つまみです。

### 2. うれしさ

毎回似た答えか、意外な答えかを選べます。

### 3. 注意点

高くしすぎると答えが破綻することがあります。

### 4. どこで役立つか

アイデア出しやコピー案作りで高めに使います。

### 5. はじめに

要約や分類はまず低めの値から試します。

### 6. 深掘り先

Top-p、サンプリング、System Prompt

## 開発フローでの位置（必須）

1. プロンプトを送る — まず要件や質問を LLM に渡して送信します。
2. Temperature を設定する — 用途に応じて低めか高めかを選びます。
3. 出力を確認する — ばらつきの度合いが目的に合っているか見ます。
4. 必要なら値を調整し直す — 高すぎ・低すぎなら変えて再実行します。

## 関連用語

- LLM
- Context
- System Prompt
- Prompt Engineering

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左右 2 コマの対比。左は「Temperature 低め」のメーター表示とノート PC に向かう人物、右は「Temperature 高め」のメーター表示と同じ人物
- 登場人物: 非エンジニアのビジネスパーソン（男女どちらでも可）が同じ人物として左右に登場
- 吹き出し・心の声: 左「今日もいつも通りの要約だ」、右「お、今日は違う案が出た」
- 中央に置くキーワード/ラベル: 「同じ質問、違う顔つき」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: キーボードで質問を打つ人
- Step 2 のアイコン/絵柄: メーターのつまみを動かす手
- Step 3 のアイコン/絵柄: 出力を読み比べるルーペ
- Step 4 のアイコン/絵柄: つまみを再調整する手
- 矢印で示す流れの意図: 「送る → 設定する → 確認する → 直す」の反復サイクル

## コミュニティ補完メモ

- G-8 決定論的／非決定論的（本文ファイル未作成）との住み分け：G-8 は「同じ入力でも結果が変わりうる」という性質そのものを扱う予定。本エントリはその性質を左右する具体的な設定値（Temperature）に絞る。G-8 が本書きされたら、本エントリの「注意点」あたりから軽く誘導してよい。
- G-10 Prompt Engineering との住み分け：指示文の書き方は G-10、出力の生成パラメータ調整は本エントリ、と役割を分ける。

## 出典メモ

- Anthropic API リファレンス（Messages, temperature パラメータ） <https://docs.anthropic.com/en/api/messages> — checked 2026-08-10
- Gemini API ドキュメント（Text generation, temperature） <https://ai.google.dev/gemini-api/docs/text-generation> — checked 2026-08-10

## 備考

サービスによって Temperature の取りうる範囲が 0〜1 や 0〜2 など異なります。数値の意味は「相対的に低い・高い」で捉えるのが安全です。
