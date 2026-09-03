---
id: F-160
title: DOM
title_reading: ディーオーエム
category: term_tool
subtype: web_foundation
experience_level: partial
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - JavaScript
  - HTML
  - React
  - SVG
status: ready
---

# DOM

## tagline

Document Object Model の略。HTML をツリー化して JavaScript から操作する規格です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ブラウザが HTML を解析すると各タグがツリー構造になります。JavaScript から `querySelector()` などで表示中のページを書き換えられます。


## どこで出会うか

AI にフロントエンドを頼むと `getElementById()` や `addEventListener()` が現れます。「ボタンを押したら動く」の舞台が DOM です。


## メイン図

### 図の狙い

HTML テキストと DOM ツリーの対応を示し、「HTML と DOM は別物」という読者の混乱を解消する。

### C. 概念図（figure_type: structure）

- 中心に置く概念: DOM ツリー（html → head / body → 各タグのノード階層）
- 周辺の要素: HTML テキスト（入力）／ブラウザの解析処理／JavaScript の操作 API／画面表示（出力）
- 関係の描き方: HTML テキストからブラウザが DOM ツリーを生成し、JS が操作して画面が更新される流れを矢印で示す


## 会話での使い方例

「`document.querySelector` で書いてもらったコードがそのまま動きました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ブラウザが HTML からツリー構造を生成し JS が操作する接点です。

### 2. うれしさ

JS の一行でボタン追加やテキスト書き換えができます。

### 3. 注意点

HTML はテキスト、DOM はメモリ上のオブジェクトで別物です。

### 4. どこで役立つか

AI 生成コードのデバッグ時に DOM ツリーの構造を読む場面です。

### 5. はじめに

`document.querySelector` でノードを取得する基本操作から入ります。

### 6. 深掘り先

Virtual DOM、Shadow DOM、Web Components


## 開発フローでの位置（必須）

1. HTML 記述 — タグで文書構造を書く
2. ブラウザ読み込み — HTML が解析され DOM ツリーが生成される
3. JS による操作 — querySelector や createElement でノードを取得・追加する
4. 画面更新 — DOM の変更がブラウザに即時反映される
5. フレームワーク活用 — React 等が Virtual DOM で差分だけ効率的に適用する


## 関連用語

- JavaScript
- HTML
- React
- SVG


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- AI エージェントの裏側で重要と言われても、初見ではチンプンカンプンになります。
- 整備されていないレガシーアプリだと触りづらく、もどかしくなります。
- 「DOM」という三文字自体は見かけても、最初は意味を掴むのに時間がかかります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: DOM という文字は出てくるのに、意味を掴むまで時間がかかりました。
- 👍 良い点: AI エージェントがテキストで触れるため、画像認識に頼らず成功率が上がります。
- 👎 ダメな点: 同じ土台に立たないと会話が通じず、重要性の共有が難しいです。
- 👥 誰向けか: なぜ動くかの仕組みを理解して応用したい、深く踏み込みたい人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左側に HTML テキスト（`<html><body><p>Hello</p></body></html>` 数行）、右側に DOM ツリー図（html ノードが根、body・p などが枝葉）、中央にブラウザのアイコンと「解析」の矢印
- 登場人物: 開発者（男性 or 女性）がブラウザの前に座り、画面を指さしている
- 吹き出し・心の声: 「HTML を書いたのに、JS で触るのはツリーなんですね」
- 中央に置くキーワード/ラベル: DOM ツリー

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: テキストファイル（HTML）
- Step 2 のアイコン/絵柄: ブラウザアイコン＋歯車（解析）
- Step 3 のアイコン/絵柄: ツリー図＋JS ロゴ
- Step 4 のアイコン/絵柄: 画面（更新後）
- 矢印で示す流れの意図: HTML → 解析 → DOM 操作 → 画面反映の一方向の流れ


## コミュニティ補完メモ

- F-1 JavaScript との住み分け：F-1 は JS 言語全体を扱う。DOM は JS がブラウザ内で操作する対象（API）の概念として独立させる
- F-4 HTML との住み分け：F-4 は HTML の書き方・タグの意味を扱う。DOM は HTML を読み込んだ後のメモリ上の表現として区別する
- F-11 React との住み分け：F-11 は React フレームワーク全体を扱う。Virtual DOM は DOM のここで簡潔に言及し、詳細は F-11 に誘導する

## 出典メモ

- MDN Web Docs「Document Object Model (DOM)」<https://developer.mozilla.org/ja/docs/Web/API/Document_Object_Model> — checked 2026-04-30
- WHATWG DOM Living Standard <https://dom.spec.whatwg.org/> — checked 2026-04-30

## 備考

- HTML はテキスト形式の「文書のソース」、DOM はそれをブラウザが解析してメモリ上に展開したオブジェクトツリー。同じ内容を指しているが形が異なる点が読者の混乱の主因
- Shadow DOM（Web Components のスコープ分離）と Virtual DOM（React / Vue の差分計算最適化）は派生概念として深掘り先に記載。詳細は別エントリに委ねる
