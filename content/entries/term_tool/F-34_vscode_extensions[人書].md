---
id: F-34
title: VS Code 拡張機能
title_reading: ブイエスコード拡張機能
category: term_tool
subtype: editor_ext
experience_level: hands_on
reader_level: 1-2
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-08-23
related_terms:
  - VS Code
  - GitHub Copilot
  - Claude Code
  - Git Graph
status: needs_review
---

# VS Code 拡張機能

## tagline

VS Code に機能を足すプラグインの仕組みで、AI 支援の多くもこの形で配られます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

VS Code に後から機能を足す仕組みで、公式マーケットプレイスから検索してインストールします。言語サポートや整形、Linter、Git 連携など役割は多様で、AI コーディング支援の多くもこの形で配られています。

## どこで出会うか

VS Code の拡張機能タブ（パズルピースのアイコン）から検索して見つかります。GitHub Copilot などの AI 拡張を導入する記事でもよく登場します。

## メイン図

### 図の狙い

VS Code 本体を中心に複数の拡張機能がつながる様子を見せ、AI コーディング支援も同じ仕組みの一部だと伝えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: VS Code 拡張機能（マーケットプレイス）
- 周辺の要素: GitHub Copilot 拡張 / Claude Code 拡張 / Linter 拡張 / テーマ拡張 / Git 連携拡張
- 関係の描き方: 中央のマーケットプレイス棚から各拡張カードが差し込まれるハブ＆スポーク構造

## 会話での使い方例

「Claude Code も拡張機能として VS Code に入れられますよ。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

VS Code に後から機能を足すプラグインの仕組みです。

### 2. うれしさ

必要な機能だけ選んで、自分好みの環境に育てられます。

### 3. 注意点

ローカルのファイルに触れるため提供元を確認して選びます。

### 4. どこで役立つか

AI 補完や整形など目的別に環境を整えたいときに使います。

### 5. はじめに

まずは公式マーケットプレイスで検索するところから始めます。

### 6. 深掘り先

GitHub Copilot、Git Graph、Markdown All in One

## 開発フローでの位置（必須）

1. 拡張機能タブを開く — 左側のパズルピースアイコンから検索します。
2. 提供元を確認 — インストール前に発行元やレビューを確かめます。
3. インストール — ボタン 1 つで追加され、自動で有効になります。
4. 使ってみる — 補完やフォーマットなど機能をすぐ試せます。


## 関連用語

- VS Code
- GitHub Copilot
- Claude Code
- Git Graph


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に VS Code のパズルピースアイコン（拡張機能マーケットプレイス）を置き、そこから複数の拡張カードが差し込まれる構造。カードには AI 拡張・Linter・テーマなどのアイコンを添える
- 登場人物（いれば）: PC 画面を見ながら「これ入れてみよう」と拡張カードを選ぶ人物
- 吹き出し・心の声: 「この提供元、大丈夫かな」と確認しながら選ぶひとこと
- 中央に置くキーワード/ラベル: 拡張機能（マーケットプレイス）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: パズルピース — 拡張機能タブ
- Step 2 のアイコン/絵柄: 虫眼鏡 — 提供元の確認
- Step 3 のアイコン/絵柄: ダウンロード矢印 — インストール
- Step 4 のアイコン/絵柄: 鉛筆 — 使ってみる


## コミュニティ補完メモ

- F-30 VS Code との住み分け：VS Code 本体の機能・エコシステム全体は F-30 に譲り、本エントリは「拡張機能」という仕組み自体（マーケットプレイス・インストール・注意点）に絞ります
- F-35 / F-36 / F-37 / F-38（個別拡張）との住み分け：個々の拡張の使い方・詳細は各エントリに任せ、本エントリは代表例として名前を挙げる程度にとどめます
- B-5 GitHub Copilot・B-7 Claude Code との住み分け：AI 拡張そのものの使い方は各エントリで扱い、本エントリは「拡張機能として配られる」という位置づけの説明にとどめます

## 出典メモ

- VS Code 公式「Extension Marketplace」<https://code.visualstudio.com/docs/editor/extension-marketplace> — checked 2026-08-23

## 備考

- 拡張機能ごとに価格・提供状況は異なります（無料のものが多い一方、GitHub Copilot のように有料プランが必要なものもあります）。個別の料金は各拡張のエントリを参照してください。
