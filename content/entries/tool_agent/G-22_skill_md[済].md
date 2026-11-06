---
id: G-22
title: SKILL.md
title_reading: スキルエムディー
category: tool_agent
subtype: config_file
experience_level: hands_on
reader_level: 4
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
last_audited: 2026-11-06
related_terms:
  - CLAUDE.md
  - Claude Code
  - Slash Command
  - Skills
  - AGENTS.md
status: ready
---

# SKILL.md

## tagline

Claude が必要と判断したときに読み込む、呼び出し可能な手順書ファイルです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`.claude/skills/<スキル名>/SKILL.md` に手順を書いておくと、Claude が会話の流れから必要性を判断して自動で読み込みます。CLAUDE.md と異なり、必要な場面でだけ参照される点が特徴です。

## どこで出会うか

Claude Code の Skills（スキルズ）機能を調べたとき、または `docs.claude.com` で「再利用可能な手順書を定義する」という説明を読んだ場面で出会います。

## メイン図

### 図の狙い

SKILL.md が置かれる場所と、Claude が「今この手順が要る」と判断して読み込む流れを示し、CLAUDE.md との役割の違いを掴んでもらう。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Claude（必要な場面で SKILL.md を読み込む）
- 周辺の要素: `.claude/skills/write-entry/SKILL.md`（執筆手順）／`.claude/skills/import-comments/SKILL.md`（取り込み手順）／CLAUDE.md（常時読まれるプロジェクト記憶）
- 関係の描き方: CLAUDE.md から Claude へは常時矢印。SKILL.md からは「必要なときだけ」の点線矢印。2 本の矢印の違いで役割差を可視化

## 会話での使い方例

「SKILL.md に手順を書いておくと、Claude が必要な場面で自動で読んでくれます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

必要なときだけ Claude が呼び出す、手順書単位のファイルです。

### 2. うれしさ

手順を一度書けば Claude が都度判断して再利用してくれます。

### 3. 注意点

CLAUDE.md と混同しやすく、配置場所とタイミングが異なります。

### 4. どこで役立つか

繰り返し発生する作業を手順化して Claude に委ねる場面に向きます。

### 5. はじめに

Skills 機能の存在と `.claude/skills/` への配置場所が最初の要点です。

### 6. 深掘り先

CLAUDE.md、Slash Command、AGENTS.md

## 開発フローでの位置（必須）

1. 手順を整理する — 繰り返す作業をステップに分解する
2. SKILL.md を作成する — `.claude/skills/<名前>/SKILL.md` に記述する
3. Claude が判断する — 会話の流れから該当スキルを読み込む
4. 手順が実行される — SKILL.md に沿って Claude が作業を進める
5. 手順を更新する — 作業内容が変わったらファイルを書き直す

## 関連用語

- CLAUDE.md
- Claude Code
- Slash Command
- Skills
- AGENTS.md

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- SKILL.md と CLAUDE.md の切り分けが難しく、最初は迷いが出ます。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: なぜこれを別ファイルとして使い分けるのか、最初はあまり理解できませんでした
- 👍 良い点: 必要な手順だけ読み込まれ、文脈をコンパクトに保てる点が良いです。
- 👎 ダメな点: メンテしないと複雑化しやすく、作りっぱなしには向きません。
- 👥 誰向けか: バイブコーディングをある程度自動化させたい人の必修概念です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左側に CLAUDE.md（常時矢印で Claude へ）、右側に複数の SKILL.md ファイルアイコン（点線矢印で Claude へ）。Claude の箱を中央に配置し、2 種類の矢印の違いで読み込みタイミングの差を表す
- 登場人物: Claude の箱の横に人物（開発者）が「今これが必要」と思っている様子。吹き出しで Claude が「スキル読みます」と応じる
- 吹き出し・心の声: 「いつも読むの？」→「必要なときだけ読みます」、「手順を一度書けば使い回せる」
- 中央に置くキーワード/ラベル: SKILL.md ＝ 必要なときだけ読まれる手順書

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 付箋に手順を整理する人
- Step 2 のアイコン/絵柄: フォルダ構造にファイルを配置する人
- Step 3 のアイコン/絵柄: Claude が会話を読んで判断するアイコン
- Step 4 のアイコン/絵柄: Claude が手順書を開いて作業するアイコン
- Step 5 のアイコン/絵柄: ファイルを更新する人
- 矢印で示す流れの意図: 「整理 → 配置 → 判断 → 実行 → 更新」の繰り返しサイクル

## コミュニティ補完メモ

- CLAUDE.md（G-20）との住み分け：CLAUDE.md はセッション開始時に常時読まれるプロジェクト全体の指示書。SKILL.md は Skills 機能で Claude が必要と判断したときだけ読まれる手順書単位のファイル。読み込みタイミングが根本的に異なる。
- AGENTS.md（G-21）との住み分け：AGENTS.md は OpenAI Codex や Gemini CLI など複数エージェントに対応する汎用設定。SKILL.md は Claude Code の Skills 機能に特化したファイル。
- Slash Command（G-32）との住み分け：Slash Command はユーザーが明示的に呼び出すコマンド。SKILL.md は Claude 自身が必要性を判断して読み込む点が異なる。両者を組み合わせることもできる。
- 本書プロジェクト自身が `skills/write-entry.md` と `skills/import-comments.md` を持っているため、自己言及の実例として示しやすい。

## 出典メモ

- docs.claude.com（Claude Skills ドキュメント）— checked 2026-04-29
- anthropic.com — checked 2026-04-29

## 備考

- Skills 機能は Claude Code の比較的新しい機能で、仕様が変わる可能性がある。evaluation_date で鮮度を管理する。
- **2026-11-06 鮮度監査（Anthropic 公式で確認）**: Agent Skills は 2025-10 に登場し、2025-12 にオープン標準として公開された。**2026-10-22、Anthropic は Agent Skills の標準（名称・ロゴ・GitHub 組織・agentskills.io ドメイン）を Agentic AI Foundation（AAIF、Linux Foundation 傘下）に寄贈**した。MCP（I-1）・A2A（J-132）と同じ財団の下に並んだことになる。Anthropic・Google・OpenAI などの技術者が個人の立場で保守し、版管理・提案プロセス・セキュリティ指針を整える予定。SKILL.md は特定の 1 社の機能ではなく、業界共通の形式に向かっている
- `.claude/skills/<skill-name>/SKILL.md` の配置ルールは、ディレクトリ名がスキルの識別子になる点に注意。
- 本書プロジェクトの `skills/` ディレクトリ（`skills/write-entry.md` 等）は Claude Code の Skills 機能そのものではなく、人間と Claude が参照する手順書として機能している。混同を避けるためコミュニティ補完メモに記載。
