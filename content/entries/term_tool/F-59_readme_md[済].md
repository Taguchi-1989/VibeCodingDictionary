---
id: F-59
title: README.md
title_reading: リードミー ドット エムディー
category: term_tool
subtype: git
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - git
  - GitHub
  - Markdown
  - CLAUDE.md
status: ready
---

# README.md

## tagline

リポジトリの玄関に置く説明ファイルです。プロジェクトの目的・使い方・規約をまとめます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

プロジェクトの概要・インストール手順・使い方・ライセンスを 1 ファイルに集約します。GitHub ではリポジトリを開いたときにトップページへ自動表示されます。

## どこで出会うか

GitHub でリポジトリを開くとコード一覧のすぐ下に表示されます。AI エージェントも「最初に読むファイル」として参照するため、渡す前に整備しておくと効果的です。

## メイン図

### 図の狙い

README.md がリポジトリ・人間・AI の 3 者をつなぐ「玄関」であることを示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: README.md ファイル
- 周辺の要素: リポジトリ本体 / GitHub トップ表示 / AI エージェント / 開発者 / ライセンス / バッジ
- 関係の描き方: 矢印（README.md から各要素へ情報提供）


## 会話での使い方例

「README.md を整えてから AI に渡すと、最初の挙動の精度が上がります。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

プロジェクトの目的・手順・規約を一元化する説明ファイルです。

### 2. うれしさ

整備すると AI が初回から文脈を把握し、指示の精度が上がります。

### 3. 注意点

概要を書かず手順だけ列挙すると、何のプロジェクトか伝わりません。

### 4. どこで役立つか

共同開発・AI エージェントへの引き渡し・OSS 公開時に効果があります。

### 5. はじめに

ファイル名は大文字 `README.md` が慣習で、GitHub が自動認識します。

### 6. 深掘り先

CLAUDE.md、Markdown、git

## 開発フローでの位置（必須）

1. リポジトリ作成 — git init 直後にルートへ README.md を置きます
2. 概要記入 — 何のプロジェクトかを冒頭 1 文で書きます
3. 手順整備 — インストール・使い方・開発手順を Markdown で記述します
4. AI 引き渡し — Claude Code 等に渡す前に README.md を最新化します
5. 継続更新 — 仕様変更のたびに内容を同期して鮮度を保ちます


## 関連用語

- git
- GitHub
- Markdown
- CLAUDE.md


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 英語ベースで読む気になれず .md の拡張子にも最初は抵抗がありました。
- 書くべき箇所とそうでない箇所の境界が最初は微妙に分かりにくかったです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 最初に読むものだけど、ドキュメントだけでは読む気がしない。
- 👍 良い点: エージェントが作ってくれるので自分で触らずに済みます。
- 👎 ダメな点: バージョン管理が甘いと古い情報が残りがちで管理が課題です。
- 👥 誰向けか: アプリを作る人・使う人どちらにも関係します。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: README.md を中心に、GitHub 画面・AI エージェント・開発者が矢印でつながる構造図
- 登場人物: 開発者（スマホで GitHub を開いている）、AI エージェント（ロボット的アイコン）
- 吹き出し・心の声: 開発者「何のプロジェクトか一発でわかる」、AI「ここを読んで動き方を決めます」
- 中央に置くキーワード/ラベル: README.md

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: フォルダ＋プラスマーク（リポジトリ作成）
- Step 2 のアイコン/絵柄: テキスト入力画面（概要記入）
- Step 3 のアイコン/絵柄: 箇条書き書類（手順整備）
- Step 4 のアイコン/絵柄: AI ロボットへ手渡しする人物（AI 引き渡し）
- 矢印で示す流れの意図: 作成から AI 活用まで一筆書きの流れ


## コミュニティ補完メモ

- CLAUDE.md（G-20）との住み分け: README.md はプロジェクト全体の人間向け説明。CLAUDE.md は Claude Code 専用の AI 向け指示書。両者は別ファイルで役割が異なります。
- Markdown（F-6）との住み分け: Markdown は書式の記法そのもの。README.md はその Markdown を使って書くファイルです。
- git（F-50）との住み分け: git はバージョン管理の仕組み全体。README.md は git リポジトリのルートに置く説明ファイルです。

## 出典メモ

- GitHub Docs "About READMEs" — checked 2026-04-29
- [GitHub Docs: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)


## 備考

- ファイル名は `README.md` 大文字が慣習ですが、`readme.md` も GitHub は認識します。大文字を推奨。
- `README.rst`（reStructuredText）形式も一部プロジェクトで使われますが、現在は Markdown が主流です。
- バッジ（ビルド状態・ライセンス・npm バージョン等）は Shields.io で画像 URL として埋め込む慣習です。誌面では深掘り要素として扱い、本文では言及を省いています。
