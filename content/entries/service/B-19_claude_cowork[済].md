---
id: B-19
title: Claude Cowork
title_reading: クロード コワーク
category: service
subtype: collaboration_service
experience_level: partial
reader_level: 2-3
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2025-01-01
version_status: active
pricing_note: paid
evaluation_date: 2026-04-30
related_terms:
  - Claude
  - Anthropic
  - Claude Code
  - Claude の料金プラン
status: ready
---

<!-- バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠） -->

## tagline

Claude.ai のチーム協働機能です。Workspace と Project で組織内の Claude を共有できます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

複数メンバーが同じ Project に入り、プロンプトやナレッジ・会話履歴を共有できます。Connectors で GitHub や Drive を繋ぎ社内情報を読み込ませる使い方もできます。

## どこで出会うか

Claude.ai の Team・Enterprise プランで「Workspaces」「Projects」として現れます。プロンプト統一や議事録共有の話題で名前が出ます。

## メイン図

### 図の狙い

個人向け Claude.ai と、チームで使う Claude Cowork の構造の違いを示します。

### B. 登場シーン（figure_type: structure）

- シーン1: PM が Workspace を作成し、メンバー全員にシステムプロンプトを配布
- シーン2: エンジニアが Connectors で GitHub リポジトリを接続し Claude に参照させる
- シーン3: 非エンジニアが共有 Project の Artifacts から議事録ドラフトを受け取る
- 並べる基準: 役割別（管理者・開発者・非エンジニア）の利用シーン

## 会話での使い方例

「Claude Cowork の Project に Drive を繋いで議事録を共有しました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

組織内で Claude の文脈・プロンプトを一元管理する協働機能です。

### 2. うれしさ

メンバー全員が同じ設定の Claude を使えるため、出力がブレにくくなります。

### 3. 注意点

Team・Enterprise プランが必要で、個人の無料プランには含まれません。

### 4. どこで役立つか

社内プロンプト管理や Connectors による業務システム連携で効果が出ます。

### 5. はじめに

Claude.ai・Claude Code・Claude Cowork の 3 つは別物と押さえておきます。

### 6. 深掘り先

Claude、Anthropic、Claude の料金プラン

## 開発フローでの位置（必須）

1. プラン確認 — Team か Enterprise で Workspace を開設します
2. Project 作成 — 用途別に Project を切りプロンプトを設定します
3. Connectors 接続 — GitHub や Drive を知識源として繋ぎます
4. メンバー招待 — 共有 Project で協働を始めます
5. Artifacts 活用 — 生成物を共有してチームに配布します

## 関連用語

- Claude
- Anthropic
- Claude Code
- Claude の料金プラン

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Claude Code との違いが実感しにくく、開発者向けと一般向けで評価が割れています。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Claude Code を一般人向けにした感じです。
- 👍 良い点: MCP が使えない場面でも Computer Use で力技が効きます。
- 👎 ダメな点: トークン消費が大きく、Plus プランだとコスパが見えにくいです。
- 👥 誰向けか: 一般タスクを Claude に任せたい人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Claude Cowork」のロゴ枠を置き、左に「個人 Claude.ai」、右に「チーム Workspace / Project」を並べる構造図
- 登場人物: 左に 1 人（個人利用者）、右に 3 人（PM・エンジニア・非エンジニア）
- 吹き出し・心の声: 個人「会話がバラバラだな」→ チーム PM「同じプロンプトで統一できた！」
- 中央に置くキーワード/ラベル: Workspace / Project / Connectors
- Before / After の場合の対比ポイント: 個人バラバラ運用 → チーム一元管理

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: クレジットカード・プランバッジ
- Step 2 のアイコン/絵柄: フォルダ＋歯車（Project 設定）
- Step 3 のアイコン/絵柄: プラグ・接続ケーブル（Connectors）
- Step 4 のアイコン/絵柄: 人物グループ（招待）
- 矢印で示す流れの意図: プラン開設からチーム本格稼働までの順番

## コミュニティ補完メモ

- Claude（B-2）との住み分け：B-2 は Claude というモデル・サービス全体を扱う。B-19 はその中のチーム協働機能に限定
- Claude Code（B-7）との住み分け：B-7 は CLI/IDE で動くコーディングエージェント。B-19 は Web UI ベースの組織共有機能。名称が似るが用途が異なる点を「非エンジニアのつまずき」欄の素材にできる
- Claude の料金プラン（B-50）との住み分け：B-50 でプラン体系全体を扱い、B-19 は Team/Enterprise プランの機能詳細に絞る

## 出典メモ

- [Anthropic Teams 発表](https://www.anthropic.com/news/claude-teams) — checked 2026-04-30
- [Claude Teams ページ](https://claude.ai/teams) — checked 2026-04-30

## 備考

- 「Claude Cowork」は Anthropic 公式の機能ブランド名としての正式確認が未完。スケルトンの notes に「要確認: 正式名称」とあるため、出版前に Anthropic 公式ページで名称を再確認する
- Connectors の対応サービス（GitHub・Google Drive 等）は時変情報のため evaluation_date 以降に変更される可能性がある
- 競合: ChatGPT Team（OpenAI Workspaces 系）、Gemini for Google Workspace との比較は B-50 の料金プランエントリか、別途比較エントリで扱う
