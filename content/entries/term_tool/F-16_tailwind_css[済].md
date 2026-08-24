---
id: F-16
title: Tailwind CSS
title_reading: テールウィンド シーエスエス
category: term_tool
subtype: framework
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: before_after
page_layout: spread_v1
start_date: 2017-01-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - CSS
  - shadcn/ui
  - React
  - Prettier
status: ready
---

# Tailwind CSS

## tagline

HTML の class に小さなクラスを並べてスタイルを組む CSS フレームワークです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`flex p-4 text-sm` のように用途別の小さなクラスを並べて UI を組みます。別途 CSS ファイルを書かず、HTML の class 属性だけでスタイルが整います。

## どこで出会うか

v0（B-9）や Bolt.new（B-11）が生成する UI コードに多く使われます。shadcn/ui（F-15）も前提採用しており、AI の出力を読む場面で登場します。

## メイン図

### 図の狙い

カスタム CSS を書く従来手法と、クラスを並べる Tailwind 手法の対比を 1 画面で示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 別ファイルの CSS を書いてクラス名を管理する
  - 視覚要素（コード or 概念）: `.card { padding: 1rem; font-size: 0.875rem; }`
  - つまずき: クラス名を考えて CSS ファイルを往復する手間がある
- After
  - 状況: HTML の class 属性に Tailwind クラスを直接並べる
  - 視覚要素: `<div class="p-4 text-sm rounded shadow">`
  - うれしさ: CSS ファイルを開かずに HTML だけでスタイルが完結する


## 会話での使い方例

「v0 が吐く UI コードはほぼ Tailwind なので、最低限の作法を押さえると読みやすいです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

HTML の class にユーティリティを並べてスタイルを組む CSS フレームワークです。

### 2. うれしさ

CSS ファイルやクラス名の管理が要らず、AI 出力のコードも読みやすくなります

### 3. 注意点

class 属性が長くなりがちで、放置すると可読性が下がることがあります。

### 4. どこで役立つか

AI 生成 UI の読解や、shadcn/ui を使う React プロジェクトで役立ちます。

### 5. はじめに

`p` `m` `flex` `text` `bg` など、よく使うクラスの命名ルールを把握するところから始めます。

### 6. 深掘り先

CSS, shadcn/ui, Prettier

## 開発フローでの位置（必須）

1. 初期設定 — `npm install tailwindcss` で導入し設定ファイルを置きます
2. クラスを記述 — `flex gap-4 p-6` のように class 属性で組みます
3. AI 出力を読む — v0・Bolt.new の出力も多くが Tailwind です
4. 整理 — Prettier プラグインで整列し `@apply` でまとめます
5. ビルド — 未使用クラスを削った軽量 CSS が出ます


## 関連用語

- CSS
- shadcn/ui
- React
- Prettier


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 使い所を考えないと画一的なデザインになりやすくテンプレ感が出ます。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: かっこいい CSS が書けるのかな、という期待がありました。
- 👍 良い点: AI コードのベストプラクティスとして定着し、学習リソースも豊富です。
- 👎 ダメな点: デザインがテンプレ感になりやすい点が気になります。
- 👥 誰向けか: AI エージェントでアプリを作る人はほぼ全員触ることになります。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に CSS ファイルとのやり取り（行き来する人）、右に HTML の class 属性だけでスタイルが完結している様子
- 登場人物（いれば）: 開発者（非エンジニアを想定した普段着の人物）
- 吹き出し・心の声: Before「CSS ファイルどこだっけ…」After「class に書くだけで完結しました！」
- 中央に置くキーワード/ラベル: `class="p-4 text-sm flex"`
- Before / After の場合の対比ポイント: CSS ファイルを往復する手間がなくなる点

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設定ファイルとターミナル
- Step 2 のアイコン/絵柄: HTML タグと class 属性
- Step 3 のアイコン/絵柄: AI チャット画面と出力コード
- Step 4 のアイコン/絵柄: Prettier のフォーマットアイコン
- Step 5 のアイコン/絵柄: ビルド後の軽量 CSS ファイル
- 矢印で示す流れの意図: 「インストール → 記述 → 読解 → 整理 → 出力」の循環を示す


## コミュニティ補完メモ

- CSS（F-5）との住み分け: F-5 は CSS 言語の概念・構文全般を扱う。F-16 はそのユーティリティクラス活用という「書き方の流儀」に絞る
- shadcn/ui（F-15）との住み分け: F-15 はコンポーネント集、F-16 はそのスタイリング基盤。F-15 を使うためには F-16 の作法が必要になる
- Prettier（F-21）との住み分け: F-21 はコード整形全般、`prettier-plugin-tailwindcss` は Tailwind クラスの並び順整列という限定的な連携


## 出典メモ

- <https://tailwindcss.com/> — checked 2026-04-30
- <https://tailwindcss.com/docs/upgrade-guide> （v4 アップグレードガイド）— checked 2026-04-30


## 備考

- v3（2021）→ v4（2024）で JIT（Just-In-Time）コンパイルがデフォルトになり新エンジンに移行。v4 以降は設定ファイル構造も変化しているため、記事を参照する際はバージョンに注意。
- Adam Wathan が 2017 年に公開。当初は「class が汚くなる」と批判されたが、現在は業界標準の地位を確立している。
- 「なぜ CSS を書かないのか」という疑問は非エンジニアに特に起きやすい。非エンジニアのつまずき欄に追記を推奨。
