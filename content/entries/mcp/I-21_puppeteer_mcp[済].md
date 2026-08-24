---
id: I-21
title: Puppeteer MCP
title_reading: パペティア エムシーピー
category: mcp
subtype: dev_automation
experience_level: partial
reader_level: 3-4
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Playwright MCP
  - Chrome DevTools MCP
  - MCP Server
  - JavaScript
status: ready
---

# Puppeteer MCP

## tagline

Chrome のブラウザ自動操作を MCP 経由で呼び出せるサーバーです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Google 製の Chrome 自動操作ライブラリ Puppeteer を MCP Server として公開し、AI がページ遷移・クリック・フォーム入力・スクリーンショット・JS 実行をツール呼び出しでこなせます。

## どこで出会うか

MCP 公式 reference server として Claude Desktop / Code の設定画面で参照する場面に出てきます。Web 自動テストや PDF 量産の選択肢として紹介されます。


## メイン図

### 図の狙い

Playwright MCP・Chrome DevTools MCP との 3 者を並べ、「Chrome 特化のシンプル操作」という Puppeteer MCP の位置を掴んでもらう。

### B. 登場シーン（figure_type: comparison）

- シーン1: Chrome/Chromium 限定でよく、API がシンプルな自動テスト
- シーン2: Web ページの PDF 生成・スクリーンショット量産
- シーン3: クロスブラウザ不要な既存 Web アプリの操作自動化
- 並べる基準: 用途・ブラウザ範囲・学習コストの 3 軸


## 会話での使い方例

「Puppeteer MCP で Chrome を動かして、申請画面の PDF を 50 件まとめて出力しました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Chrome 自動操作を AI エージェントのツールとして提供します。

### 2. うれしさ

スクリプト不要で AI 指示だけでブラウザ操作が完結します。

### 3. 注意点

Chrome / Chromium 専用で Firefox・Safari は非対応です。

### 4. どこで役立つか

PDF 量産・スクリーンショット・フォーム自動入力の場面。

### 5. はじめに

MCP Server（I-2）の仕組みと起動コマンドが前提知識です。

### 6. 深掘り先

Playwright MCP、Chrome DevTools MCP、MCP Server


## 開発フローでの位置（必須）

1. MCP 設定 — `npx -y @modelcontextprotocol/server-puppeteer` を設定ファイルに追加します
2. ブラウザ起動 — AI がツール呼び出しで Chrome を headless 起動します
3. 操作実行 — クリック・フォーム入力・スクリーンショットなどを逐次実行します
4. 結果取得 — 画像や HTML・コンソールログを AI が受け取り、次の操作に使います


## 関連用語

- Playwright MCP
- Chrome DevTools MCP
- MCP Server
- JavaScript


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- PDF を作りたいだけなのに、できることが多すぎて何を任せればよいか迷います
- 依存関係が見えづらく、どこまで指示を細かく書くべきか判断しにくいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:何でもできすぎて、PDF 周りでもよく分かりません
- 👍 良い点:PDF 生成もできるので、出版関係では使わない手はないです
- 👎 ダメな点:機能が多く初見は難しい。文字化けや LaTeX に注意
- 👥 誰向けか:PDF で受け渡しをする人すべてに向きます
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 3 列の比較表。Puppeteer MCP / Playwright MCP / Chrome DevTools MCP を横に並べ、「対応ブラウザ」「API の複雑さ」「主な用途」を行で比べる
- 登場人物（いれば）: 担当者（開発者）が 3 列を眺めて Puppeteer MCP を指差している
- 吹き出し・心の声: 「Chrome だけでいいからシンプルで十分です」
- 中央に置くキーワード/ラベル: Puppeteer MCP（中列をハイライト）
- Before / After の場合の対比ポイント: なし（comparison 形式）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設定ファイルにコマンドを書き込む手のアイコン
- Step 2 のアイコン/絵柄: Chrome ブラウザが起動するアイコン
- Step 3 のアイコン/絵柄: マウスカーソル＋キーボードのアイコン（操作実行）
- Step 4 のアイコン/絵柄: PDF・スクリーンショット・ログが積み重なるアイコン
- 矢印で示す流れの意図: 設定 → 起動 → 操作 → 結果取得の一方向フロー

## コミュニティ補完メモ

- Playwright MCP（I-20）との住み分け：クロスブラウザ（Chrome/Firefox/Safari）が必要なら Playwright MCP、Chrome 特化でシンプルに済ませたいなら Puppeteer MCP。
- Chrome DevTools MCP（I-22）との住み分け：パフォーマンス計測・低レベルな DevTools プロトコル操作は Chrome DevTools MCP へ。Puppeteer MCP はページ操作・スクリーンショット・PDF 生成などの高レベル操作に集中。
- MCP Server（I-2）が前提知識。MCP の仕組みを知らない読者は I-2 を先に読む。


## 出典メモ

- [modelcontextprotocol/servers: puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) — checked 2026-04-30
- [MCP Debugging Tools](https://modelcontextprotocol.io/docs/tools/debugging) — checked 2026-04-30


## 備考

- Puppeteer MCP は MCP 公式 reference server のひとつ（2024 年 11 月 MCP 公開時から収録）。
- headless モードで動作するため、サーバー環境でも利用可能。GUI が不要な自動化シナリオに向く。
- 起動後は Chrome のユーザーデータを残さないクリーンセッションが基本。永続ログインが必要な場合は別途設定が必要。
