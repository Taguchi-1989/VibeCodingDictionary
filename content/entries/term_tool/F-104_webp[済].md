---
id: F-104
title: .webp
title_reading: ドット ウェッピー
category: term_tool
subtype: file_format
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - SVG
  - .ico
  - Lighthouse
  - HTML
status: ready
---

# .webp

## tagline

Web 向けの軽量画像フォーマットです。JPEG・PNG より小さく、同等の画質を保ちます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

画像ファイルを小さく保ちながら、可逆・非可逆の両圧縮、透明度（アルファチャンネル）、アニメーション表示に対応します。同等画質で JPEG 比 25〜35%、PNG 比 26% のサイズ削減が見込めます。

## どこで出会うか

Lighthouse（ライトハウス）のパフォーマンス診断で「次世代フォーマットを使用してください」と表示されたとき、候補として名前が出ます。AI が生成した PNG を `.webp` に変換する場面でも登場します。

## メイン図

### 図の狙い

PNG・JPEG と `.webp` のファイルサイズを Before / After で比較し、変換前後の違いを直感的に伝えます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: PNG 形式のまま Web に配置している
  - 視覚要素: ファイルアイコン「image.png 800 KB」
  - つまずき: ページ読み込みが遅く、Lighthouse スコアが低い
- After
  - 状況: `.webp` に変換して配置した
  - 視覚要素: ファイルアイコン「image.webp 560 KB」（約 30% 削減）
  - うれしさ: 同じ画質のまま転送量が減り、表示が速くなります


## 会話での使い方例

「PNG を `.webp` に変換したら Lighthouse のスコアが 10 点上がりました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Web 向けに画像を圧縮する軽量フォーマットです。

### 2. うれしさ

JPEG・PNG より小さく、表示速度と転送コストが改善されます。

### 3. 注意点

IE 11 は非対応でしたが、IE 11 自体がサポート終了済みです。

### 4. どこで役立つか

ブログや EC サイトの画像最適化と Lighthouse 改善に有効です。

### 5. はじめに

主要ブラウザは 2020 年以降対応済みと知れば導入の障壁はありません。

### 6. 深掘り先

Lighthouse、HTML の `<picture>` 要素、SVG


## 開発フローでの位置（必須）

1. 画像を用意する — AI 生成や撮影で PNG・JPEG を取得します
2. フォーマットを変換する — ツールやスクリプトで `.webp` に変換します
3. HTML に組み込む — `<img>` タグや `<picture>` 要素で参照します
4. Lighthouse で確認する — パフォーマンス項目のスコア変化を確認します


## 関連用語

- SVG
- .ico
- Lighthouse
- HTML


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 名前を見ても画像ファイルとは分からず、初見では何の拡張子か掴めません。
- LLM に「この形式にすると軽くなる」と言われても、仕組みが分からず不安です。
- AI に任せて変換すると、たまに画像が劣化して困ることがあります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: PNG や JPEG で重くなる悩みを相談した時に紹介された印象です。
- 👍 良い点: 画質を保ったままかなり容量を削減でき、表示が軽くなります。
- 👎 ダメな点: 圧縮の仕方で劣化し、AI 任せの変換だと壊れてしまうこともあります。
- 👥 誰向けか: 画像をたくさん載せる Web サイトを作る人に向いています。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: PNG ファイルと `.webp` ファイルを横並びで比較。ファイルサイズの数値を大きく表示する
- 登場人物: Web 担当者（20 代、パソコンの前で Lighthouse レポートを見ている）
- 吹き出し・心の声: Before「ページが重い…」→ After「30% 小さくなった！スコア上がった」
- 中央に置くキーワード/ラベル: `.webp` 変換
- Before / After の対比ポイント: PNG 800 KB → .webp 560 KB、Lighthouse スコア例示

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 画像ファイル（PNG/JPEG アイコン）
- Step 2 のアイコン/絵柄: 変換ツール（歯車＋矢印）
- Step 3 のアイコン/絵柄: HTML ファイル（コードエディタ）
- Step 4 のアイコン/絵柄: Lighthouse スコアメーター
- 矢印で示す流れの意図: 取得 → 変換 → 組み込み → 検証という直線フロー

## コミュニティ補完メモ

- F-9 SVG との住み分け：SVG はベクター（図形・アイコン）、`.webp` はラスター（写真・スクショ）。用途が異なるため競合しない
- F-101 .ico との住み分け：`.ico` はファビコン専用。`.webp` は通常の Web 画像向け
- F-110 Lighthouse との住み分け：Lighthouse は診断ツール、`.webp` はその改善手段の 1 つ


## 出典メモ

- <https://developers.google.com/speed/webp> — checked 2026-04-30
- <https://caniuse.com/webp> — checked 2026-04-30


## 備考

- IE 11 は `.webp` 非対応だったが、Microsoft による IE 11 サポートは 2022-06-15 に終了済み。現時点での実用上の制約はほぼない
- アニメーション対応は GIF の代替として使えるが、動画コンテンツには MP4 等の動画フォーマットが適している場合もある
