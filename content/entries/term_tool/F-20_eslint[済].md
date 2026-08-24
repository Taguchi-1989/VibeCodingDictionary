---
id: F-20
title: ESLint
title_reading: イーエスリント
category: term_tool
subtype: linter
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: before_after
page_layout: spread_v1
start_date: 2013-07-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - JavaScript
  - TypeScript
  - Prettier
  - VS Code
status: ready
---

# ESLint

## tagline

JS / TS コードを静的解析し、バグや書き方の不統一を警告するリンターです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

未使用変数・未定義変数・`==` と `===` の混在・セミコロン抜けなどをルールベースで検出します。プラグインを追加すれば React・TypeScript・アクセシビリティ領域の規約にも対応できます。

## どこで出会うか

VS Code でコードを書くと赤い波線や警告パネルとして現れます。CI（継続的インテグレーション）に組み込めば、プルリクエスト時に自動チェックが走り、レビュー前に問題を拾えます。

## メイン図

### 図の狙い

ESLint を導入する前後で、コード品質とレビュー負荷がどう変わるかを対比で示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: ESLint なし。`==` 混在・未使用変数がそのまま残る
  - 視覚要素（コード or 概念）: `if (x == null)` `const unused = 1`
  - つまずき: 動くが壊れやすく、レビューで毎回指摘される
- After
  - 状況: ESLint 導入。保存時に波線が出て `--fix` で大半が自動修正される
  - 視覚要素: `if (x === null)` ＋ 未使用変数エラー削除済み
  - うれしさ: AI が出したコードも ESLint が機械的に弾くので品質が安定する


## 会話での使い方例

「ESLint のルールを共有してから Claude に書かせると、コミット前の指摘が激減します。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

JS／TS のコードを静的解析して品質問題を検出するリンターです。

### 2. うれしさ

`--fix` オプションで警告の多くが自動修正され、手直しが減ります。

### 3. 注意点

Prettier（整形担当）と役割が違い、両者を併用するのが一般的です。

### 4. どこで役立つか

AI 生成コードの品質チェックに使うと回帰を抑えられます。

### 5. はじめに

「赤い波線 → `--fix` で直す」の流れを体験するところから始まります。

### 6. 深掘り先

Prettier、TypeScript、CI/CD


## 開発フローでの位置（必須）

1. コード生成 — Claude Code・Cursor などが JS／TS コードを出力する
2. 静的解析 — ESLint がルールに照らして警告・エラーを列挙する
3. 自動修正 — `eslint --fix` で直せるルールを一括修正する
4. レビュー — 残った警告を開発者が確認してコミットの判断をする
5. CI チェック — プルリクエスト時に ESLint が再実行され品質ゲートとして機能する


## 関連用語

- JavaScript
- TypeScript
- Prettier
- VS Code

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- JS なのになぜ ES という略称なのか最初は分かりませんでした。「リント」の意味を掴むまでも時間がかかりました。
- チェックを厳しくすると `any` 型だらけになって収拾がつかなくなるジレンマを経験しました。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: チェックしてくれるなら良いツールだろうと感じました。
- 👍 良い点: 機械的にチェックできる仕組みは必須です。今や入れておくべきツールです。
- 👎 ダメな点: AI エージェントと組み合わせると設定が崩れやすくなります。
- 👥 誰向けか: AI エージェントにかなりの部分を任せていきたい人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に ESLint なしのコード（`==` 混在・未使用変数）、右に `--fix` 後のきれいなコード
- 登場人物: 開発者（非エンジニア）がエディタを見て頭を抱えている → 修正後に笑顔になる
- 吹き出し・心の声: Before「赤い波線だらけ…」/ After「`--fix` 一発で片付いた！」
- 中央に置くキーワード/ラベル: `eslint --fix`
- Before / After の対比ポイント: 波線の有無とコードの変化（`==` → `===`）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ロボット（AI エージェント）がコードを書いている絵
- Step 2 のアイコン/絵柄: 虫眼鏡（静的解析）
- Step 3 のアイコン/絵柄: レンチ（自動修正）
- Step 4 のアイコン/絵柄: 人のアイコン（人間レビュー）
- Step 5 のアイコン/絵柄: チェックマーク（CI パス）
- 矢印で示す流れの意図: AI 生成 → 機械チェック → 人間判断 の流れを示す

## コミュニティ補完メモ

- Prettier（F-21）との住み分け：ESLint は「コードの正しさ・品質（`==` vs `===`、未使用変数など）」を検出、Prettier は「インデント・改行・クォートの統一（整形）」を担当。両者は役割が重ならず、通常は `eslint-config-prettier` プラグインで衝突を回避しながら併用する。
- TypeScript（F-2）との関係：`@typescript-eslint` プラグインを追加することで TS 固有の型チェックルールも ESLint で扱える。ただし型チェック本体は tsc が担当するため完全な代替ではない。
- VS Code（F-30）との関係：ESLint 拡張機能をインストールすると保存時に自動実行され、波線がリアルタイムに表示される。

## 出典メモ

- <https://eslint.org/docs/latest/> — checked 2026-04-29
- <https://github.com/eslint/eslint> — checked 2026-04-29


## 備考

- ESLint は 2013 年に Nicholas C. Zakas が開始し、現在は OpenJS Foundation 配下のオープンソースプロジェクト（Apache-2.0 ライセンス）。
- `eslint --fix` で自動修正できるルールとできないルールが混在する。初学者は「赤い波線が全部消えるわけではない」点でつまずきやすい。
- pricing_note: none（OSS、無料）。
- 旧 3 桁 ID（303）と連携。旧ファイルが存在する場合は status: archived に落とし、本エントリで引き継ぐ。
