---
id: G-20
title: CLAUDE.md
title_reading: クロードエムディー
category: tool_agent
subtype: config_file
experience_level: hands_on
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
last_audited: 2026-11-13
related_terms:
  - Claude Code
  - AGENTS.md
  - Memory
  - CLAUDE.md に書くことの変遷
status: ready
---

# CLAUDE.md

## tagline

Claude Code（略称 CC）がセッション開始時に自動で読む、プロジェクト専用の指示書です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

プロジェクトのルートや `~/.claude/` に置くと、CC がセッション開始時に読み込みます。コードから分からない規約や注意事項を書いておけば、毎回手入力しなくても CC が文脈を把握した状態で動き始めます。

## どこで出会うか

CC を初めて使うときに紹介される場面が多いです。本書プロジェクトもルートに置いており、規約が毎セッション CC に伝わります。チームで使う場合は Git に入れて共有します。

## メイン図

### 図の狙い

CLAUDE.md が置かれる場所（ルート・サブディレクトリ・グローバル）と CC の読み込み順を示し、「どこに書けばどこに届くか」を掴んでもらう。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Claude Code（セッション開始時に読み込む）
- 周辺の要素: `~/.claude/CLAUDE.md`（全プロジェクト共通）／プロジェクトルート `CLAUDE.md`（このプロジェクト専用）／サブディレクトリ `CLAUDE.md`（特定フォルダ専用）
- 関係の描き方: 外から内へ矢印。グローバル → ルート → サブディレクトリの順に CC が読む。合計が Context Window 内に収まる点線枠を添える

## 会話での使い方例

「CLAUDE.md にプロジェクト規約を書いておくと、毎回 CC に説明しなくて済みます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

CC がセッション開始時に読む、プロジェクト専用の記憶ファイルです。

### 2. うれしさ

規約を一度書けば毎セッション CC が把握した状態で始まります。

### 3. 注意点

毎回読まれるため、長いと注意が散ります。短く保つのが公式の勧めです。

### 4. どこで役立つか

チームで CC を使うとき、コード規約を全員に共有する場面で効果的です。

### 5. はじめに

置く場所（ルート / グローバル）と読み込まれる順番の 2 点が基本です。

### 6. 深掘り先

AGENTS.md、Memory、CLAUDE.md に書くことの変遷

## 開発フローでの位置（必須）

1. 規約を整理 — コードから分からないことだけを選んで箇条書きにする
2. CLAUDE.md を作成 — プロジェクトルートに置き、規約や注意点を記述する
3. CC が読み込む — セッション開始時に CC がプロジェクトの文脈を把握する
4. 変更時に更新 — チームの合意を得てファイルを修正し Git でレビューする
5. 肥大化を防ぐ — 200 行未満を目安に削り、手順はスキルへ移す

## 関連用語

- Claude Code
- AGENTS.md
- Memory
- CLAUDE.md に書くことの変遷

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- どこに置けばよいか、何を書けばよいかが最初は分かりません
- 全部書き込むとコンテキストが膨らみ、モデルの賢さが下がりがちです
- そもそも「.md」というファイル形式自体に馴染みがありません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: ここに書けば Claude に伝わる、楽だなという印象でした
- 👍 良い点: 方針・ルールをファイルに切り出して Claude に運用させられます
- 👎 ダメな点: 詰め込みすぎると逆効果で、委任体系の設計が必要になります
- 👥 誰向けか: バイブコーディングをする人、特に CC を使う人には必修の概念です
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 3 段の階層図。上段に `~/.claude/CLAUDE.md`（雲アイコン＝グローバル）、中段にプロジェクトルートの `CLAUDE.md`（フォルダアイコン）、下段にサブディレクトリの `CLAUDE.md`（小フォルダ）。それぞれから Claude Code の箱へ矢印が流れる。Context Window の点線枠で全体を囲む
- 登場人物: フォルダの横に人物（開発者）が CLAUDE.md を書いている姿。CC の箱のそばに「セッション開始！」の吹き出し
- 吹き出し・心の声: 「毎回説明しなくていい」「どこに書けばどこに届く？」
- 中央に置くキーワード/ラベル: CLAUDE.md ＝ プロジェクトの記憶

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 付箋に規約を書く人
- Step 2 のアイコン/絵柄: フォルダにファイルを置く人
- Step 3 のアイコン/絵柄: CC が自動で本を開いて読むアイコン
- Step 4 のアイコン/絵柄: チームで Git のブランチをレビューする人たち
- Step 5 のアイコン/絵柄: ハサミでファイルを整理する人
- 矢印で示す流れの意図: 「整理 → 記述 → 自動読込 → 更新 → 管理」の循環

## コミュニティ補完メモ

- AGENTS.md（G-21）との住み分け：CLAUDE.md は Claude Code 専用。AGENTS.md は OpenAI Codex / Gemini CLI など複数エージェントに対応する汎用版。CC のみを使うなら CLAUDE.md で十分。
- SKILL.md（G-22）との住み分け：CLAUDE.md はプロジェクト全体の記憶。SKILL.md はエージェントが参照するスキル・手順書単位のファイル。役割分担が異なる。
- .claude/settings.json（G-23）との住み分け：設定ファイルで権限・ツール・Hook を制御し、CLAUDE.md は自然言語で文脈・規約を伝える。両者は補完関係。
- Hook（G-31）/ Slash Command（G-32）は CLAUDE.md 内で言及されることが多いが、別エントリで詳細を扱う。
- Memory（別エントリ候補）との住み分け：CLAUDE.md は人が書くファイルベースの記憶。Memory（auto memory）は CC が実行中に自分でメモを書く仕組み。
- H-65 CLAUDE.md に書くことの変遷への導線：「昔はいろいろ書け → スキルへ分けろ → 今は短く、コードから分からないことだけ」という推奨の移り変わりは H-65 に任せる。本エントリは 2026-11 時点の公式ガイドに沿った現在形の説明にとどめる
- 手順はスキル（G-22）へ、例外なしのルールはフック・deny ルールへ、という振り分けが 2026-11 の公式ガイド。`/doctor` が削れる箇所を提案する

## 出典メモ

- docs.anthropic.com/en/docs/claude-code/memory — checked 2026-04-29
- code.claude.com（best-practices / memory）— checked 2026-11-13
- claude.com/blog「Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents」（2026-06-18）— checked 2026-11-13

## 備考

- CLAUDE.md の読み込み順はグローバル（`~/.claude/CLAUDE.md`）→ プロジェクトルート → サブディレクトリの順。優先度はより具体的（内側）なほど高い。
- ファイルが大きくなると Context Window を圧迫するため、定期的な整理が推奨される。2026-11 の公式ガイド（一次確認済み）：毎セッション読み込まれるので短く保つ／コードから読み取れないことだけ書く／1 ファイル 200 行未満が目安／手順はスキルへ／例外なしのルールはフックへ／`/doctor` が削れる箇所を提案（`/doctor prompt-audit` は古いモデル向けの指示や矛盾を指摘）。2026-11-13 に本文の「規約を何でも書く」寄りの記述を改めた。
- 本書プロジェクト自身が CLAUDE.md を持っている（`C:\Users\user\Desktop\Vibecodingカタログ\CLAUDE.md`）ため、自己言及の実例として扱いやすい。
