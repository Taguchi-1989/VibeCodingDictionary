---
id: F-181
title: WebGL
title_reading: ウェブジーエル
category: term_tool
subtype: graphics_api
experience_level: partial
reader_level: 3-4
importance: E
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - OpenGL
  - three.js
  - JavaScript
  - GPU
status: ready
---

# WebGL

## tagline

Web Graphics Library の略。ブラウザ上で 3D 描画を行う JavaScript API です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

GPU（グラフィックス処理ユニット）を使い、ブラウザ内で 3D を描画します。JavaScript から呼び出せる低レベル API で、頂点座標やシェーダ（描画プログラム）を直接指定する仕組みです。

## どこで出会うか

Google Maps の 3D 表示、AI モデルのデモ、ブラウザゲームなどで内部的に使われています。three.js（F-14）や Babylon.js といった高レベルライブラリが WebGL を呼び出す構造です。

## メイン図

### 図の狙い

JavaScript → three.js → WebGL → GPU という層の積み重ねを示し、WebGL が低レベル API であることを把握してもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: WebGL API
- 周辺の要素: JavaScript コード / three.js / GPU / ブラウザ
- 関係の描き方: 上から下への呼び出し階層（包含・矢印）


## 会話での使い方例

「WebGL でシェーダを直接書くより、three.js を Claude に書かせる方が早いです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ブラウザ上で GPU を使った 3D 描画を可能にする API です。

### 2. うれしさ

プラグインなしで 3D コンテンツをどのブラウザでも動かせます。

### 3. 注意点

低レベル API のため直接書くコード量が多く、学習コストがあります。

### 4. どこで役立つか

3D ビジュアライゼーションや AI デモをブラウザで提供する場面に向きます。

### 5. はじめに

WebGL は基盤で、実務では three.js 経由で使う層と理解できれば十分です。

### 6. 深掘り先

three.js（F-14）、OpenGL（F-180）、WebGPU

## 開発フローでの位置（必須）

1. 要件確認 — ブラウザで 3D 表示が必要かどうかを確かめます。
2. ライブラリ選定 — three.js など WebGL を抽象化したライブラリを選びます。
3. AI コード生成 — Claude や Cursor に three.js コードを書かせます。
4. 動作確認 — ブラウザで GPU レンダリングの結果を確認します。


## 関連用語

- OpenGL
- three.js
- JavaScript
- GPU


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 中身の仕組みを知らないと難しく感じ、入口で身構えてしまいます。
- 実は three.js などで簡単に動かせる、と気づくまでに時間がかかります。
- ブラウザで 3D が動く仕組みとして登場するため、出会う場面が限られます。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 「こんなの自作できるんだ」と感動した、すごい体験になりました。
- 👍 良い点: 「おっ、すごい」と言わせるものが、思ったより簡単に作れるところです。
- 👎 ダメな点: 直接書くと大変で、three.js などの上位ライブラリを介す必要があります。
- 👥 誰向けか: ブラウザで 3D を使って遊んだり見せたい人にとっての入口になります。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: JavaScript → three.js → WebGL → GPU の呼び出し階層を縦に積んだ図
- 登場人物（いれば）: 開発者（非エンジニア寄り）がラップトップで three.js を書いているシーン
- 吹き出し・心の声: 「three.js に頼めば WebGL の細かい仕組みは知らなくていい！」
- 中央に置くキーワード/ラベル: WebGL API

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 画面イメージ（要件確認）
- Step 2 のアイコン/絵柄: ライブラリ積み木（three.js ロゴ）
- Step 3 のアイコン/絵柄: AI チャット画面（コード生成）
- Step 4 のアイコン/絵柄: ブラウザ上の 3D オブジェクト
- 矢印で示す流れの意図: 「WebGL 直書きを避けて three.js + AI で済ませる」実践フローを示す


## コミュニティ補完メモ

- OpenGL（F-180）との住み分け：OpenGL はデスクトップ・ネイティブアプリ向けの元祖、WebGL はそれをブラウザ向けに派生させた API。スコープは「ブラウザ上」の有無で区切ります。
- three.js（F-14）との住み分け：WebGL は低レベル API、three.js はその上位抽象化ライブラリ。階層が異なるため重複しません。three.js エントリで「WebGL を使っている」と参照する形が適切です。
- WebGPU との住み分け：WebGPU は WebGL の後継として 2023 年に主要ブラウザで使えるようになった次世代 API（Vulkan / Metal / DirectX 12 を抽象化）。WebGL は当面併存します。WebGPU は別エントリ扱いが望ましいです。


## 出典メモ

- Khronos Group WebGL 仕様 — <https://www.khronos.org/webgl/> — checked 2026-04-30
- MDN Web Docs: WebGL API — <https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API> — checked 2026-04-30


## 備考

- WebGL 1.0 は 2011 年、WebGL 2.0 は 2017 年に Khronos Group が仕様化。
- 後継の WebGPU は 2023 年に Chrome で GA。WebGL は Safari や旧環境の互換性のため当面存続。
- バイブコーディング文脈では「WebGL を直接書く」より「three.js を AI に書かせる」パターンが主流。
