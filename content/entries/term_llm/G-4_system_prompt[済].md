---
id: G-4
title: System Prompt
title_reading: システムプロンプト
category: term_llm
subtype: basic
experience_level: partial
reader_level: 2
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Context
  - Prompt Engineering
  - Few-shot
  - Context Window
status: ready
---

# System Prompt

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

AI の役割・前提を会話前にあらかじめ仕込む指示の下層です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ユーザーの発言より先に LLM（大規模言語モデル）へ渡す指示層です。役割や制約をここに書けば、会話ごとに同じ指示を繰り返さずに済みます。

## どこで出会うか

Claude や ChatGPT の API の `system` フィールドがこれにあたります。「カスタム指示」「プロジェクト指示」も同じ仕組みで、役割や出力形式の統一に使います。

## メイン図

### 図の狙い

System Prompt が「会話の土台層」として User Prompt の下に敷かれる二層構造を示し、「あらかじめ仕込む層」と「毎回入れる層」の違いを伝えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: LLM への入力が二層に分かれる構造
- 周辺の要素: System Prompt 層（役割・制約・前提）、User Prompt 層（毎回の指示・質問）、LLM（応答を生成する箱）
- 関係の描き方: 下段に System Prompt の板、上段に User Prompt の板、それが重なって LLM に流れ込む矢印。System Prompt 板に「役割 / 制約 / 前提」の小ラベルを入れる

## 会話での使い方例

「System Prompt に制約を書けば、毎回同じ指示を送らずに済みます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

会話全体に共通する役割・制約を LLM にあらかじめ伝える層です。

### 2. うれしさ

一度書けば毎回の指示が不要になり、応答の一貫性が保てます。

### 3. 注意点

User Prompt と矛盾した内容を書くと出力が不安定になります。

### 4. どこで役立つか

チームで同じ AI を使うとき、出力形式や言語を統一する場面で効きます。

### 5. はじめに

System と User の二層構造と、System が先に読まれる順序の把握。

### 6. 深掘り先

Context, Prompt Engineering, Few-shot

## 開発フローでの位置（必須）

1. 役割・制約を決める — 担わせたいペルソナと守らせたい制約を整理する
2. System Prompt を書く — 役割・出力形式・禁止事項を簡潔にまとめる
3. User Prompt と動作確認 — 会話を何件か試し、矛盾や抜けを潰す
4. 改善・再固定 — 出力が安定したらテンプレとして保存する
5. 運用・更新 — タスクや対象が変わるたびに見直す

## 関連用語

- Context
- Prompt Engineering
- Few-shot
- Context Window

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「プロンプト」と一括りで呼ぶことが多く、何のプロンプトかが解像度低めで伝わります。
- 普段ユーザーとして意識する場面が少なく、作る側に回らないと触れません。
- どこまでをデフォルトに書くかの判断が難しく、設計の勉強が要ります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回まとめる中で初めて、ちゃんと理解できた語でした。
- 👍 良い点: デフォルトで仕込んでおけるので、回答の質を底上げできるところです。
- 👎 ダメな点: User Prompt とコンフリクトすると出力が不安定で、設計が難しいです。
- 👥 誰向けか: ユーザー側ではなく、AI のシステムを設計する側の人に必要な語です。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 二層の板が重なる断面図。下段が「System Prompt」（紺色板・役割 / 制約 / 前提のラベル付き）、上段が「User Prompt」（白板・質問や指示）、二枚が合わさって LLM の箱に流れ込む矢印
- 登場人物: 左端に開発者キャラクターが System Prompt 板を「あらかじめ」敷いている姿
- 吹き出し・心の声: 「毎回書かなくていい！」「土台だから変わらない」
- 中央に置くキーワード/ラベル: 「仕込み層 vs 会話層」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 付箋にペルソナ・制約を書く人
- Step 2 のアイコン/絵柄: テキストエディタで System Prompt を組む人
- Step 3 のアイコン/絵柄: 吹き出しを往復させてチェックする人
- Step 4 のアイコン/絵柄: 保存アイコン（テンプレとして固定）
- Step 5 のアイコン/絵柄: カレンダーと鉛筆（定期見直し）
- 矢印で示す流れの意図: 「決める → 書く → 確認 → 固定 → 更新」のサイクル

## コミュニティ補完メモ

- G-1 Context との住み分け：Context は「LLM に渡す情報全体」を指す上位概念。System Prompt はその中の一要素（下層の指示層）。G-1 では System Prompt を Context の構成要素の 1 つとして言及している。
- G-10 Prompt Engineering との住み分け：Prompt Engineering は指示文設計の技術全般。System Prompt はその設計対象の 1 つ（下層）であり、User Prompt 設計と対になる概念として本エントリで独立して扱う。
- G-20 CLAUDE.md との関係：CLAUDE.md はプロジェクト固有の指示をリポジトリに置く仕組みで、Claude Code における System Prompt の拡張形。詳細は G-20 へ。
- G-11 Context Engineering との関係：Context 全体を動的に設計する技術。System Prompt はその静的な土台部分にあたる。

## 出典メモ

- docs.anthropic.com/en/docs/build-with-claude/prompt-engineering — checked 2026-04-29
- platform.openai.com/docs/guides/text-generation — checked 2026-04-29

## 備考

- System Prompt の扱い（フィールド名・挙動）は API プロバイダによって微妙に異なるが、「ユーザー発言より先に読まれる指示層」という役割は共通。
- 「カスタム指示」（ChatGPT）「プロジェクト指示」（Claude）など UI 名称が異なる場合も、仕組みとして System Prompt にあたることを備考として明記。
