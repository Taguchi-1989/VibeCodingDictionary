---
id: I-20
title: Playwright MCP
title_reading: プレイライトエムシーピー
category: mcp
subtype: dev_automation
experience_level: hands_on
reader_level: 3
importance: C
figure_type: workflow
page_layout: spread_v1
start_date: 2024-11
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - Claude Code
  - Playwright
  - E2E テスト
status: ready
---

# Playwright MCP

## tagline

LLM が実ブラウザを直接操作できる MCP です。クリック・入力・スクショをコードなしで実行します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Microsoft が公開する MCP Server で、LLM にブラウザ操作ツールを提供します。Accessibility ツリーベースでセマンティックに操作するため、要素を正確に特定できます。

## どこで出会うか

Claude Code の設定に追加すると、チャットで「フォームを入力して送信して」と頼むだけで実ブラウザが動きます。E2E テスト・UI レビュー・Web スクレイピングで名前を見かけます。

## メイン図

### 図の狙い

Claude Code → Playwright MCP → 実ブラウザ の 3 段構造を示し、「指示を打つだけでブラウザが動く」流れを視覚で伝えます。

### C. 概念図（figure_type: workflow）

- 中心に置く概念: Playwright MCP（LLM とブラウザの橋渡し）
- 周辺の要素: Claude Code（LLM）／Playwright MCP Server／実ブラウザ（Chromium など）／操作結果（スクショ・DOM）
- 関係の描き方: 左に Claude Code、中央に Playwright MCP、右に実ブラウザを配置し、左→中→右の矢印で操作フローを示す

## 会話での使い方例

「Playwright MCP を入れると Claude Code からブラウザを動かせて、E2E が楽です。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM にブラウザ操作ツールを渡す MCP Server です。

### 2. うれしさ

コードを書かず自然言語でブラウザを動かせます。

### 3. 注意点

アクセシビリティツリーがない要素は操作が難しいです。

### 4. どこで役立つか

E2E テスト、UI 確認、Web スクレイピングに使えます。

### 5. はじめに

MCP の仕組みと Playwright の役割を先に押さえます。

### 6. 深掘り先

Playwright、MCP Server、E2E テスト。

## 開発フローでの位置（必須）

1. Playwright MCP を設定に追加する — Claude Code の設定ファイルに Server を登録します
2. LLM に操作したいページと手順を伝える — チャットで URL と操作内容を指示します
3. Playwright MCP がブラウザを操作する — クリック・入力・スクロールをセマンティックに実行します
4. 結果を受け取る — スクリーンショットや DOM の状態が LLM に返ります

## 関連用語

- MCP
- MCP Server
- Claude Code
- Playwright
- E2E テスト


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 普通に仕事をしていたら名前を聞かないです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:確認が非常に楽になって最高です
- 👍 良い点:実際の操作を代行してくれて使い方が現代的です
- 👎 ダメな点:ペルソナを設定しても網羅は難しい点に注意です
- 👥 誰向けか:バイブコーディングをする人すべてに向きます
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左に開発者キャラクターがチャット画面で指示を打つ様子、中央に「Playwright MCP」のボックス、右に実ブラウザのウィンドウ（フォームが入力されている画面）を配置。左→中→右の矢印でフローを示す
- 登場人物: 開発者 1 人（チャット画面を見ている）
- 吹き出し・心の声: 「フォームを入力して送信して」という指示の吹き出しと、ブラウザ側に「操作完了！スクショ返します」の応答
- 中央に置くキーワード/ラベル: Playwright MCP ＝ LLM とブラウザの橋渡し

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設定ファイルのアイコン（歯車）
- Step 2 のアイコン/絵柄: チャット吹き出しのアイコン
- Step 3 のアイコン/絵柄: ブラウザ操作のアイコン（カーソル）
- Step 4 のアイコン/絵柄: スクリーンショットのアイコン（カメラ）
- 矢印で示す流れの意図: 設定 → 指示 → 操作 → 確認


## コミュニティ補完メモ

- MCP プロトコル全体は I-1、MCP Server の仕組みは I-2 で扱う。本エントリは「ブラウザ操作に特化した具体的 MCP」に絞ります
- Puppeteer MCP（I-21）との住み分け：Playwright MCP は Accessibility ツリーベースのセマンティック操作、Puppeteer MCP は DOM 直接操作が中心。どちらも「LLM がブラウザを動かす」点は同じですが、操作の方式が異なります
- Chrome DevTools MCP（I-22）とは：DevTools プロトコル経由のデバッグ・ネットワーク検査が主で、ブラウザ UI 操作とは目的が異なります
- Filesystem MCP（I-10）・GitHub MCP（I-11）と兄弟エントリ。「具体的な MCP の使われ方」シリーズとして位置づけ

## 出典メモ

- github.com/microsoft/playwright-mcp（Microsoft 公式）— checked 2026-04-29
- playwright.dev — checked 2026-04-29

## 備考

Playwright MCP の仕様・対応ブラウザは更新中です。evaluation_date を持たせて時変情報として扱います。Microsoft 公式リポジトリの README が最新の動作確認として信頼できます。
