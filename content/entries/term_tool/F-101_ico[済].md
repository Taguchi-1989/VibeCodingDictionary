---
id: F-101
title: .ico
title_reading: ドット アイコ
category: term_tool
subtype: file_format
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - SVG
  - PNG
  - favicon
  - ImageMagick
status: ready
---

# .ico

## tagline

Windows やブラウザで表示されるアイコン専用の画像形式です。複数サイズを 1 ファイルに束ねられます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

16×16 から 256×256 まで異なるサイズのビットマップ画像を 1 ファイルに格納できる形式です。OS やブラウザが表示先の大きさに合わせて最適なサイズを自動で選びます。


## どこで出会うか

Web サイトを作ると `favicon.ico` をルートに置くよう求められます。AI に「favicon を用意して」と頼むと `.ico` 生成を提案されます。Windows のショートカットアイコンにも使われます。


## メイン図

### 図の狙い

1 つの `.ico` ファイルが複数サイズを内包し、表示先によって使い分けられる仕組みを示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: ブラウザタブに 16×16 が表示される
- シーン2: Windows デスクトップのショートカットに 48×48 が表示される
- シーン3: 高解像度ディスプレイで 256×256 が選ばれる
- 並べる基準: 表示先（ブラウザ・OS）ごとのサイズ自動選択


## 会話での使い方例

「favicon は AI に SVG で作らせて、`.ico` は ImageMagick で変換しました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

複数サイズのアイコン画像を 1 ファイルに束ねる形式です。

### 2. うれしさ

OS が表示先に合わせて最適サイズを自動選択してくれます。

### 3. 注意点

現代の Web では PNG や SVG でも favicon に使えます。

### 4. どこで役立つか

Windows アプリや IE 対応が必要なサイトで今も必要です。

### 5. はじめに

`favicon.ico` はサイトのルートに置くブラウザタブ用アイコンです。

### 6. 深掘り先

SVG、PNG、ImageMagick


## 開発フローでの位置（必須）

1. デザイン素材を用意 — PNG や SVG でアイコン原案を作ります
2. サイズ展開 — 16×16 / 32×32 / 48×48 などを書き出します
3. `.ico` に変換 — ImageMagick などで複数サイズを 1 ファイルに束ねます
4. favicon として配置 — サイトルートに `favicon.ico` として置き、`<link>` タグで参照します


## 関連用語

- SVG
- PNG
- favicon
- ImageMagick


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 画像生成で作ったものをアイコンのところに設定しようと思うと、この拡張子を変えるだけではダメで、特別な処理をかけないといけないというところを知らなかったのが1つ目です。
- もう1つは、何も設定しないままになってしまって、毎回同じものが出てしまうというところです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Web ページの上に出ているアイコンって、PNG とか JPEG じゃないんだ、というところでした。ICO というファイル形式を知りませんでした。
- 👍 良い点: 非常に軽量で、特徴を伝えられるので、自分のサイトを作ったときに何かを識別する手段になります。
- 👎 ダメな点: Web 制作などをしないと、そもそもこの拡張子の名前すら知らないままです。
- 👥 誰向けか: 自分でサイトを作ってデプロイする人向けです。社内システムを作る人も、バニラのままではなく設定してほしいなと思います。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 1 つの `.ico` ファイルから複数サイズが取り出される様子。ファイルアイコンを中央に置き、左にブラウザタブ（16px）、右にデスクトップショートカット（48px）、上に高解像度表示（256px）を矢印で接続する
- 登場人物: Web 制作者が PC 画面を指さしながら「なんで 3 種類あるの？」と首をかしげているポーズ
- 吹き出し・心の声: 「全部 `.ico` 1 個でいいんだ！」
- 中央に置くキーワード/ラベル: `.ico` ファイル（多サイズ内包）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 鉛筆アイコン（デザイン）
- Step 2 のアイコン/絵柄: 拡大縮小矢印（サイズ展開）
- Step 3 のアイコン/絵柄: コンバートアイコン（変換）
- Step 4 のアイコン/絵柄: フォルダ＋ブラウザ（配置）
- 矢印で示す流れの意図: PNG/SVG から `.ico` を経由してサイトに組み込むまでの一方向の流れ


## コミュニティ補完メモ

- SVG（F-9）との住み分け：SVG はベクター形式でスケーラブルだが、IE や一部 Windows 環境では `.ico` の方が確実に表示される。現代の Web では `<link rel="icon" href="icon.svg">` で SVG を使いつつ、旧環境向けに `favicon.ico` を併置するパターンが多い
- PNG との関係：PNG 単体でも `<link rel="icon" type="image/png">` で favicon に使えるが、ブラウザ互換性や複数サイズ自動選択の点で `.ico` が依然有利な場面がある


## 出典メモ

- MDN Web Docs: favicon — <https://developer.mozilla.org/ja/docs/Glossary/Favicon> — checked 2026-04-30
- Microsoft Docs: ICO ファイル形式 — <https://docs.microsoft.com/en-us/windows/win32/uxguide/vis-icons> — checked 2026-04-30


## 備考

- IE 対応が不要な場合は SVG または PNG の favicon で十分なケースが多い
- `favicon.ico` をルートに置くと `<link>` タグ不要でブラウザが自動取得する慣例がある
