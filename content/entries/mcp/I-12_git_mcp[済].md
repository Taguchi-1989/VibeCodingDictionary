---
id: I-12
title: Git MCP
title_reading: ギットエムシーピー
category: mcp
subtype: reference
experience_level: partial
reader_level: 3-4
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-09-05
related_terms:
  - MCP
  - MCP Server
  - GitHub MCP
  - git
status: ready
---

# Git MCP

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

ローカルの git 操作を AI が直接呼び出せる MCP 公式 reference server です。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`git status` / `git diff` / `git log` / `git commit` など主要な操作を Claude が「git 専用ツール群」として呼び出せます。Python 製で `mcp-server-git` として公開されています。

## どこで出会うか

Bash 全権限を渡せない職場や CI 環境で git 操作だけ MCP 経由に絞りたいときに登場します。`uvx mcp-server-git` で起動して使います。

## メイン図

### 図の狙い

Bash 全許可と Git MCP 利用の権限範囲の違いを示し、なぜ Git MCP が選ばれるかを掴んでもらいます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Claude に Bash ツールで git を叩かせている
  - 視覚要素: Claude → Bash（全権限）→ git / rm / curl など
  - つまずき: 権限が広すぎてセキュリティポリシーに引っかかる
- After
  - 状況: Git MCP で git 専用ツール群だけ渡す
  - 視覚要素: Claude → Git MCP（git 操作のみ）→ ローカルリポジトリ
  - うれしさ: 権限を絞り込んだまま commit まで自動化できる


## 会話での使い方例

「Bash を切っている環境でも、Git MCP を使えば commit まで任せられます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

git 操作専用の MCP ツール群を Claude に提供します。

### 2. うれしさ

Bash 許可なしで commit・branch が自動化できます。

### 3. 注意点

I-11 GitHub MCP とは別物で、ローカル操作専用です。

### 4. どこで役立つか

権限を厳しく管理する職場や CI 環境で効果があります。

### 5. はじめに

MCP の基本（I-1）と GitHub MCP との違いを先に押さえます。

### 6. 深掘り先

MCP Server、GitHub MCP、git


## 開発フローでの位置（必須）

1. 環境準備 — `uvx mcp-server-git` をインストールして起動設定を書きます
2. 接続確認 — Claude が git ツール一覧を認識しているか確認します
3. 操作委任 — status・diff・log を Claude に呼ばせて動作を検証します
4. commit 自動化 — add / commit を AI に任せて変更を記録します
5. branch 運用 — 作成・切り替えまで任せて開発を回します


## 関連用語

- MCP
- MCP Server
- GitHub MCP
- git


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 全権委任して致命的な破壊行為をされました（Sonnet 4 時代）
- 面倒で全権委任したくなりますが、事前の権限見極めが必要です
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: ローカル承認の回数が減って楽になりそうです
- 👍 良い点: エージェントのトークン数が下がりそうです
- 👎 ダメな点: 権限設定を怠ると致命的な操作が起こり得ます
- 👥 誰向けか: コーディングをする人全般に向いています
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に「Bash 全権限」の広い矢印、右に「Git MCP のみ」の細い矢印。権限の絞り込みを視覚化する
- 登場人物: 開発者（30 代、腕組みして画面を見ている）
- 吹き出し・心の声: Before「git 以外も全部触れてしまう…」After「git だけ渡せば安心です。」
- 中央に置くキーワード/ラベル: 「権限スコープ」
- Before / After の対比ポイント: 許可ツールの範囲（広い vs 狭い）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ターミナルと設定ファイル
- Step 2 のアイコン/絵柄: チェックマーク・接続確認
- Step 3 のアイコン/絵柄: 虫眼鏡・diff 確認
- Step 4 のアイコン/絵柄: コミットアイコン（git ブランチマーク）
- 矢印で示す流れの意図: 環境構築 → 確認 → 委任 → 自動化の段階的な信頼構築


## コミュニティ補完メモ

- I-11 GitHub MCP との住み分け：GitHub MCP はリモートの GitHub API（Issue・PR・Repository 操作）を担い、Git MCP はローカルリポジトリの git コマンド操作を担います。「GitHub = リモート、Git MCP = ローカル」が最短の区別です
- F-50 git との住み分け：F-50 は git コマンド自体の概念解説。I-12 は git を MCP 経由で AI に使わせる運用方法の話です
- I-2 MCP Server との関係：I-12 は MCP Server の具体例の 1 つ。MCP Server の仕組みを知りたい読者は I-2 へ誘導します


## 出典メモ

- https://github.com/modelcontextprotocol/servers/tree/main/src/git — checked 2026-04-29
- MCP 公式ドキュメント（modelcontextprotocol.io） — checked 2026-04-29


## 備考

- `mcp-server-git` は Python 製。`uvx` コマンド（uv ツール）で手軽にインストールできます
- transport は stdio のみ（2026-09-05 時点）
- Claude Code はデフォルトで Bash 経由の git 操作が可能なため、Git MCP が必要になるのは「Bash 許可を絞り込んだ環境」に限られます。一般的なバイブコーディング環境では Claude Code の Bash ツールで十分なケースが多いです
- **2026-09-05 の当て直し**: 2025 年 5 月に参照サーバー 14 本がアーカイブへ移された際、Git は書き直された版が現役の保守対象として残りました。**いま Anthropic が保守している参照サーバーは Everything / Fetch / Filesystem / Git / Memory / Sequential Thinking / Time の 7 本**です。本エントリの「公式 reference server」という説明は 2026-09-05 時点でも有効です。出典: <https://github.com/modelcontextprotocol/servers> — checked 2026-09-05
