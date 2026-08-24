---
id: F-4
title: HTML
title_reading: エイチティーエムエル
category: term_tool
subtype: language
experience_level: partial
reader_level: 2
importance: B
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - CSS
  - JavaScript
  - Markdown
  - ブラウザ
  - DOM
status: ready
---

# HTML

## tagline

HyperText Markup Language の略。Web ページの骨格を作るマークアップ言語です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

テキストや画像・リンクを「タグ（tag）」で囲み、ページの構造を定義します。`<h1>` で見出し、`<p>` で段落を意味し、ブラウザがその構造を表示します。

## どこで出会うか

AI にランディングページを依頼すると出力に HTML ファイルが含まれます。VS Code でも `.html` ファイルとして目にします。

## メイン図

### 図の狙い

HTML タグが「構造の骨格」として機能し、CSS（スタイル）と JavaScript（動き）がその上に乗る 3 層関係を概念図で示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: HTML（骨格・構造）
- 周辺の要素: CSS（見た目・色・レイアウト）／ JavaScript（動き・インタラクション）／ ブラウザ（表示する実行環境）
- 関係の描き方: HTML を土台の層、CSS を中間層、JavaScript を上位層とした積み重ねの図。右にブラウザウィンドウのアイコンを置き、3 層が合わさってページとして出力されることを示す矢印

## 会話での使い方例

「この HTML の `<div>` タグ、CSS でスタイルを当てたいのですが構造として合っていますか？」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Web ページの骨格を作るマークアップ言語で、CSS・JS の土台です。

### 2. うれしさ

タグで囲むだけで構造の意味が決まり、AI への指示が通りやすくなります。

### 3. 注意点

HTML だけでは見た目を整えられず、スタイルは CSS に任せます。

### 4. どこで役立つか

AI が返した HTML の構造を読む場面で役立ちます。

### 5. はじめに

`<html>` `<head>` `<body>` の 3 タグと `<h1>` `<p>` が出発点です。

### 6. 深掘り先

CSS（F-5）、JavaScript（F-1）、DOM（F-160）。

## 開発フローでの位置（必須）

1. 構造の指示 — AI に「HTML でページの骨格を作って」と頼み、`.html` を受け取る
2. ブラウザ確認 — ブラウザで開き、見出しや段落の並びが意図通りか確かめる
3. CSS 追加 — AI に見た目の調整を頼み、スタイルを当ててもらう
4. JavaScript 追加 — 動きが必要なら AI に JS を加えてもらう
5. 修正・再依頼 — 崩れやタグの誤りを AI に伝えて改善します

## 関連用語

- CSS
- JavaScript
- Markdown
- ブラウザ
- DOM


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- CSS や JS を中に書き込むと責任範囲が分かりにくくなります。
- タグの読み解きが辛く、使い方を覚えるのに時間がかかりました。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Web で使われる言語という認識でした。
- 👍 良い点: 単一ファイルで配布すれば軽く動くものが作れます。
- 👎 ダメな点: 「どこまで HTML に含めるか」という設計判断が難しいです。
- 👥 誰向けか: ファイルを受け渡して確認する人に最も扱いやすい形式です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 3 層積み重ねの図。下から「HTML（骨格）」「CSS（見た目）」「JavaScript（動き）」の層を積み上げ、右側にブラウザウィンドウを配置して矢印でつなぐ
- 登場人物: 非エンジニアの人物 1 人がソースコードを見ながら「この `<div>` ってどこに出るんだろう？」と首をかしげている
- 吹き出し・心の声: 「タグで囲むと意味が決まるんですね。CSS で色を付けるのはその次なんだ」
- 中央に置くキーワード/ラベル: HTML（骨格・構造）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チャット吹き出し（AI への依頼）
- Step 2 のアイコン/絵柄: ブラウザウィンドウ（確認）
- Step 3 のアイコン/絵柄: 塗りつぶしブラシ（CSS 追加）
- Step 4 のアイコン/絵柄: 稲妻（JS で動きを追加）
- Step 5 のアイコン/絵柄: 回転矢印（修正ループ）
- 矢印で示す流れの意図: 骨格生成 → 確認 → スタイル → 動き → 改善ループ の 5 ステップ


## コミュニティ補完メモ

- CSS（F-5）との住み分け：HTML がタグで構造を決め、CSS がその構造に見た目を当てます。色・フォント・レイアウトの話は F-5 CSS へ。
- JavaScript（F-1）との住み分け：ボタン反応・画面切り替えなどの動きは JS の担当です。本エントリは「構造の定義」に絞ります。
- Markdown（F-6）との住み分け：Markdown は HTML に変換されることが多いですが、書き方は別物です。Markdown 独自の書式は F-6 へ。
- DOM（F-160）との住み分け：HTML タグがブラウザ上でオブジェクトのツリーになる「DOM（Document Object Model）」の概念は F-160 へ委ねます。
- HTML5・WHATWG・W3C の規格史：深掘り先レベルの情報です。本エントリでは言語としての基本的な役割に絞ります。

## 出典メモ

- MDN Web Docs: HTML（HyperText Markup Language）— <https://developer.mozilla.org/ja/docs/Web/HTML> — checked 2026-04-29

## 備考

- HTML のバージョン史（HTML4 → XHTML → HTML5）は時変情報を含みますが、現在は HTML5（WHATWG の HTML Living Standard として継続更新）が事実上の標準です。本エントリではバージョン差分には踏み込まず、言語としての役割に絞りました。
- CSS・JS との 3 層関係は本エントリの核心です。それぞれのスタイル・動きの詳細は F-5・F-1 に委ねます。
