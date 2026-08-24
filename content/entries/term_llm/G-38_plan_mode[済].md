---
id: G-38
title: Plan Mode
title_reading: プラン モード
category: term_llm
subtype: control
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: before_after
page_layout: spread_v1
start_date: 2025-01-01
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Claude Code
  - Permission
  - Slash Command
  - Auto Mode
status: ready
---

# Plan Mode

## tagline

実装前に計画を提示して承認を待つモードです。いきなりの書き換えを防ぎます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Claude Code が搭載するモードで Shift+Tab で切り替えます。ファイルは編集せず実装計画だけを提示し、Approve（承認）で初めて実装に進みます。

## どこで出会うか

大規模リファクタや設計変更を依頼するときに使われます。Claude Code を日常的に使うと、変更規模に応じて Plan Mode と Auto Mode を使い分ける運用が定着しがちです。


## メイン図

### 図の狙い

「計画提示 → 承認 → 実装」の 3 ステップを対比することで、いきなり書き換えるリスクをどこで止めるかを伝える。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Auto Mode でそのまま実行
  - 視覚要素: ファイルが次々と書き換わっていく画面
  - つまずき: 「意図と違う変更が広がってしまった」
- After
  - 状況: Plan Mode で計画を確認してから承認
  - 視覚要素: 「計画テキスト → Approve ボタン → 実装開始」の 3 ステップ
  - うれしさ: 「方針がずれていたらここで止められる」


## 会話での使い方例

「リファクタ前は Plan Mode で計画レビューしてから走らせるようにしました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

実装前に計画だけを提示し、承認を待つ合意形成ステップです。

### 2. うれしさ

意図と違う変更が広がる前に方針を確認できます。

### 3. 注意点

小さな修正まで毎回通すと作業が遅くなりがちです。

### 4. どこで役立つか

大規模リファクタやチームでの方針共有前に効果的です。

### 5. はじめに

Shift+Tab で切り替え、Approve で実装開始する流れを押さえます。

### 6. 深掘り先

Permission, Auto Mode, Slash Command


## 開発フローでの位置（必須）

1. タスク入力 — Claude Code に変更内容や目標を指示します
2. Plan Mode 切り替え — Shift+Tab でモードを切り替えます
3. 計画確認 — CC が計画テキストを提示し、ファイルは変更しません
4. Approve — 内容に問題がなければ承認し、実装フェーズに進みます
5. 実装完了 — 承認済みの計画に沿ってコード変更が実行されます


## 関連用語

- Claude Code
- Permission
- Slash Command
- Auto Mode


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「いい感じにやってほしい」と思っていると、プランが面倒くさく感じます。
- 手戻り経験がないと重要性を肌感覚で理解しにくいです。
-
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: モードの切り替えが面倒くさい。
- 👍 良い点: 計画に時間を使うことで最終的に時短になり質が上がります。
- 👎 ダメな点: 重要性を肌感覚で理解するのが難しいです。
- 👥 誰向けか: AI にタスクを委ねる人すべて。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: Auto Mode で「ファイルが次々書き換わる」画面と、Plan Mode で「計画テキストを読んでいる人」の 2 コマ対比
- 登場人物: 画面を覗き込む開発者（非エンジニア想定）
- 吹き出し・心の声: Before「え、もう書き換えてる！」/ After「ここで確認できた、助かった」
- 中央に置くキーワード/ラベル: 「Approve」「Plan Mode」
- Before / After の対比ポイント: 実装が始まるタイミングを「承認前」か「いきなり」かで分ける

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チャット入力アイコン
- Step 2 のアイコン/絵柄: Shift+Tab キー表示
- Step 3 のアイコン/絵柄: 計画テキスト（リスト）
- Step 4 のアイコン/絵柄: Approve ボタン（チェックマーク）
- 矢印で示す流れの意図: 承認というゲートを経て実装に進む流れを強調

## コミュニティ補完メモ

- Cursor（B-4）の Composer Preview との住み分け：Cursor は UI プレビュー確認が主目的、Plan Mode はコード変更計画の合意形成が主目的。機能の意図が異なる
- Devin（B-10）との住み分け：Devin はレビュー段階を PR で行うエージェント型、Plan Mode は実装前の対話型承認ステップ
- Permission（G-39）との関係：Permission はツール実行の許可設定、Plan Mode は計画提示という別レイヤーの安全機構。両方を使い分けることで多段防御になる
- Auto Mode は Plan Mode の対概念。小さな修正は Auto Mode、大きな変更は Plan Mode という使い分けが定石

## 出典メモ

- Claude Code 公式ドキュメント（Anthropic） — checked 2026-04-30
- <https://docs.anthropic.com/en/docs/claude-code/overview> — checked 2026-04-30


## 備考

- Plan Mode は 2025 年に Claude Code に導入された機能。evaluation_date は 2026-04-30
- Aider の `/architect` モードも類似の「設計先行・実装後」フローを持つが、インタラクション方式が異なる
- 「毎回 Plan Mode を通す必要があるか」というつまずきに対しては、変更規模で使い分けるのが現実的な答え
