---
id: F-1
title: JavaScript
title_reading: ジャバスクリプト
category: term_tool
subtype: language
experience_level: partial
reader_level: 2
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - TypeScript
  - React
  - Node.js
  - HTML
  - CSS
status: ready
---

# JavaScript

## tagline

Web のインタラクション（操作反応）を実現するプログラミング言語で、略して JS（ジェイエス）と呼ばれます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ボタン反応・画面切り替え・入力チェックなど Web ページの動きを作るプログラミング言語です。ブラウザが直接解釈できる唯一の言語です。

## どこで出会うか

AI にフロントエンドの修正を頼むと「JavaScript で書きます」と返ってくる場面で出会います。Cursor や VS Code でも `.js` 拡張子として目にします。

## メイン図

### 図の狙い

JavaScript を中心に置き、言語を土台として成り立つ TypeScript・React・Next.js と、ブラウザ／サーバーという 2 つの実行環境との関係を概念図で見せます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: JavaScript（JS）
- 周辺の要素: TypeScript（上位互換の言語）／ React（UI ライブラリ）／ Next.js（フレームワーク）／ ブラウザ（実行環境①）／ Node.js（実行環境②、サーバー側）
- 関係の描き方: 中央に JS、上方向に TypeScript・React・Next.js の積み重ね矢印、下方向にブラウザと Node.js の 2 分岐

## 会話での使い方例

「その画面の動き、React ベースの JS ですか？Node.js で動いている部分もありますか？」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Web ページの動きを担うプログラミング言語です。

### 2. うれしさ

HTML・CSS と組み合わせるだけで動く画面を作れます。

### 3. 注意点

Java とは別物で、混同しないようにします。

### 4. どこで役立つか

AI にフロントエンド修正を頼む際、指示が的確になります。

### 5. はじめに

「Web の動きを JS が作る」「TypeScript の土台が JS」の 2 点。

### 6. 深掘り先

TypeScript（F-2）、React（F-10）、Node.js（F-80）。

## 開発フローでの位置（必須）

1. 要件の確認 — 「どんな動き（インタラクション）を作りたいか」を AI と合意する
2. コード生成 — AI に「JavaScript で書いて」と依頼し、`.js` ファイルを受け取る
3. ブラウザ確認 — 実行結果をブラウザで開き、動きが意図通りかチェックする
4. 修正・再依頼 — エラーメッセージや画面の違和感を AI に伝えて改善を繰り返す

## 関連用語

- TypeScript
- React
- Node.js
- HTML
- CSS


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Java と JavaScript が違うことも分かりづらく、「JS」ファイルは触れる気がしません。
- 「○○ JS」と付くライブラリが多くて何が何なのか分からなくなります。
-
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 触ることへの抵抗感がある。
- 👍 良い点: HTML の中に組み込めて挙動を確認できたり、用途がめちゃくちゃ広い。
- 👎 ダメな点: 普段の業務で積極的に触らない人からすると、ハードルが高い。
- 👥 誰向けか: 「実はみんな使っている」と意識したい人、まず色々やってみたい人。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「JS」ロゴ風の円、上方向に TypeScript・React・Next.js を積み木のように重ねる矢印、下方向にブラウザアイコンと Node.js アイコンへの 2 分岐矢印
- 登場人物: 非エンジニアの人物 1 人が AI チャット画面を見ながら「JS ってどこで動いてるの？」と思っている
- 吹き出し・心の声: 「ブラウザでもサーバーでも JS なんですね。TypeScript や React もここから来てるんですね」
- 中央に置くキーワード/ラベル: JavaScript（JS）
- Before / After の場合の対比ポイント: （概念図のため不要）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 吹き出し（AI と要件合意）
- Step 2 のアイコン/絵柄: コードファイル（.js ファイル生成）
- Step 3 のアイコン/絵柄: ブラウザウィンドウ（画面確認）
- Step 4 のアイコン/絵柄: 回転矢印（修正ループ）
- 矢印で示す流れの意図: 要件合意 → コード受け取り → 動作確認 → 改善ループ の 4 ステップ


## コミュニティ補完メモ

- TypeScript（F-2）との住み分け：JS に型（型＝データの種類の制約）を加えた上位互換が TypeScript。TypeScript 固有の話は F-2 へ。
- React（F-10）との住み分け：React は JS の上で動く UI ライブラリ。React のコンポーネント設計の話は F-10 へ。
- Next.js（F-11）との住み分け：Next.js は React をさらに包むフレームワーク。F-11 へ。
- ESLint（F-20）との住み分け：JS のコード品質チェックツール。F-20 へ。
- Node.js（F-80）との住み分け：サーバー側 JS のランタイム（実行環境）詳細は F-80 へ。本エントリでは「ブラウザ以外でも動く」という事実に触れる程度に留める。

## 出典メモ

- MDN Web Docs: JavaScript — <https://developer.mozilla.org/ja/docs/Web/JavaScript> — checked 2026-04-29
- ecma-international.org: ECMAScript 仕様 — <https://www.ecma-international.org/publications-and-standards/standards/ecma-262/> — checked 2026-04-29

## 備考

- Java と JavaScript は名前が似ているが無関係。Sun Microsystems（現 Oracle）の Java と、Netscape が開発した JavaScript は起源が別であり、非エンジニアが最も混乱しやすいポイントとして本エントリの注意点（見どころ 3）で明示した。
- ECMAScript（エクマスクリプト）は JavaScript の標準仕様で、バージョンが ES5・ES6（ES2015）・ES2023 のように更新される時変情報。本エントリはバージョン差分には踏み込まず、言語としての位置づけに絞った。
