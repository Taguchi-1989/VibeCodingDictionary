---
id: F-85
title: SuperClaude Framework
title_reading: スーパークロードフレームワーク
category: term_tool
subtype: framework
experience_level: hands_on
reader_level: 4-5
importance: E
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Claude Code
  - Slash Command
  - Subagent
  - AGENTS.md
status: ready
---

# SuperClaude Framework

## tagline

Claude Code をコミュニティが拡張した非公式 OSS フレームワークです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`/architect` `/refactor` などのスラッシュコマンドと専門ペルソナを Claude Code に追加し、工程ごとの動作を短いコマンドで呼び出せます。

## どこで出会うか

GitHub で公開されており、`pip` でインストールします。導入後は `.claude/` 配下に定義が追加され、Claude Code の起動時から使えます。

## メイン図

### 図の狙い

SuperClaude を入れる前後で Claude Code の呼び出し方がどう変わるかを示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Claude Code をそのまま起動している
  - 視覚要素（コード or 概念）: 汎用チャット欄のみ
  - つまずき: 設計・テスト・レビューを都度プロンプトで指示しなければならない
- After
  - 状況: SuperClaude 導入済みの Claude Code を起動
  - 視覚要素: `/architect` `/security` など専用コマンドが並ぶ一覧
  - うれしさ: 工程に合ったペルソナが自動で切り替わり、指示が短くなる


## 会話での使い方例

「SuperClaude を入れたら `/architect` で設計レビューを任せられました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Claude Code に工程別コマンドとペルソナを追加する拡張です。

### 2. うれしさ

設計・テスト・レビューを短いコマンドで呼び出せます。

### 3. 注意点

Anthropic 非公式のコミュニティ製で、破壊的変更が入ることがあります。

### 4. どこで役立つか

Claude Code を日常的に使う個人開発・小規模チームに向いています。

### 5. はじめに

Claude Code の基本操作を理解してから導入するのが確実です。

### 6. 深掘り先

Claude Code、Slash Command、AGENTS.md


## 開発フローでの位置（必須）

1. インストール — `pip install superclaude` で `.claude/` に展開します
2. ペルソナ選択 — architect / frontend / qa など工程に合うものを指定
3. コマンド実行 — `/architect` `/refactor` で Claude に作業を依頼
4. 出力確認 — 生成されたコードやレビューを取り込みます


## 関連用語

- Claude Code
- Slash Command
- Subagent
- AGENTS.md


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- OSS の非公式拡張なので、自分で探す手間と信頼性の見極めが必要になります。
- スラッシュコマンドや専門ペルソナを覚えてキータイプするのが面倒に感じます。
- 公式に同等機能が来たら陳腐化するので、メンテの見極めが大変です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 「むきむきのクロード」みたいで、ポケモンのマッシブーンを思い浮かべました。
- 👍 良い点: 認知リソースを節約し、工程ごとに最適な配慮を呼び出せる価値があります。
- 👎 ダメな点: 公式に取り込まれたら陳腐化するため、見極めとメンテが難しいです。
- 👥 誰向けか: 認知リソースを節約しながら Claude Code を使い込みたい人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Claude Code の画面を中心に、左側に「素の Claude Code（チャット欄のみ）」、右側に「SuperClaude 導入後（/architect /security などのコマンド一覧）」を並べた Before/After 構成
- 登場人物（いれば）: 開発者（1 名）がターミナルを操作している様子
- 吹き出し・心の声: Before「毎回長いプロンプトを書かないと…」／After「`/architect` で一発です。」
- 中央に置くキーワード/ラベル: SuperClaude
- Before / After の場合の対比ポイント: コマンド入力の手間と Claude の専門性

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: パッケージインストール（箱に矢印）
- Step 2 のアイコン/絵柄: ペルソナ切り替え（人型アイコン×複数）
- Step 3 のアイコン/絵柄: スラッシュコマンド実行（ターミナル）
- Step 4 のアイコン/絵柄: 成果物取り込み（フォルダへの矢印）
- 矢印で示す流れの意図: インストールから実際の開発作業までの直線的な流れ

## コミュニティ補完メモ

- Claude Code（B-7）との住み分け：B-7 は Anthropic 公式の CLI ツール本体。F-85 はその上に乗るコミュニティ製拡張。Claude Code を知らずに SuperClaude だけ読んでも理解しにくいため、B-7 を先に参照させる。
- Slash Command（G-32）との住み分け：G-32 はスラッシュコマンドの概念全般を扱う。F-85 の `/architect` 等はその具体的実装例として位置付ける。
- AGENTS.md（G-21）との住み分け：G-21 はエージェント動作を指示するファイル形式の解説。SuperClaude はインストール時に AGENTS.md 系ファイルを `.claude/` に生成するため関連が深い。


## 出典メモ

- GitHub NomenAK/SuperClaude <https://github.com/NomenAK/SuperClaude> — checked 2026-04-30


## 備考

- SuperClaude はコミュニティ OSS のため、バージョンアップで仕様が変わることがある。コマンド名・ペルソナ名は出版前に要確認。
- 「Anthropic 公式では？」という読者の誤解を防ぐため、tagline と注意点で非公式である点を明示している。
