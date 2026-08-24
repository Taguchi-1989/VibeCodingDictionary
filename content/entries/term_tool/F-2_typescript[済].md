---
id: F-2
title: TypeScript
title_reading: タイプスクリプト
category: term_tool
subtype: language
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - JavaScript
  - VS Code
  - Vite
  - Node.js
status: ready
---

# TypeScript

## tagline

JavaScript（JS）に静的型付けを加えた上位互換言語です。略して TS とも呼ばれます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

コードを書く時点で型（データの種類）のミスマッチを警告し、実行前にバグを検出します。コンパイル時に純粋な JS に変換されるため、ブラウザや Node.js（F-80）でそのまま動きます。

## どこで出会うか

VS Code（F-30）や Cursor でプロジェクトを開くと `.ts` ファイルや `tsconfig.json` として目に入ります。AI にコード生成を頼む場面でも「TypeScript で書きますか？」と確認されることがあります。

## メイン図

### 図の狙い

JS のコードに型注釈を足すだけで警告が出るようになる Before / After の対比を見せます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 型なしの JS、引数に何を渡してもエラーにならない
  - 視覚要素（コード）: `function add(a, b) { return a + b; }`
  - つまずき: `add("3", 2)` を渡しても実行時まで気づかない
- After
  - 状況: TS の型注釈を足した版
  - 視覚要素（コード）: `function add(a: number, b: number): number { return a + b; }`
  - うれしさ: `add("3", 2)` の時点でエディタが赤線を引いて警告してくれる

## 会話での使い方例

「TS の型を Claude に投げると、API の整合性まで一緒に直してもらえます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

JS に型チェックを加えて、実行前にバグを減らす言語拡張です。

### 2. うれしさ

型推論（type inference）で自動補完が効き、開発スピードが上がります。

### 3. 注意点

`any` 型に逃げると型の恩恵が消えるため、`unknown` で締める習慣が大切です。

### 4. どこで役立つか

複数人が触る業務 Web アプリや、長期保守するプロジェクトで特に効果的です。

### 5. はじめに

JS が書ければ型注釈を足すだけで始められ、`tsc` か Vite 経由で動かせます。

### 6. 深掘り先

JavaScript、型推論、tsconfig

## 開発フローでの位置（必須）

1. 環境準備 — `npm install typescript` で `tsc` コマンドを導入します
2. 設定 — `tsconfig.json` でコンパイル対象とオプションを決めます
3. 実装 — `.ts` ファイルで型注釈を付けながらコードを書きます
4. ビルド — `tsc` または Vite（F-41）経由で JS に変換して動作確認します


## 関連用語

- JavaScript
- VS Code
- Vite
- Node.js


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- JS すら難しいのに TS と言われてもマジで分からず、とっつきづらい。
- 「TS」と拡張子も変わるし、「上位互換」と言われてもピンと来ない。
- 概念だけ押さえれば充分。コードを読む力は大事で書く練習は後回しでよい。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 必要性も分からず辛かったですが、必須の道でした。
- 👍 良い点: 型定義が使えて、LLM 前提なら十分活かせます。
- 👎 ダメな点: 「JS の上位互換」がイメージしづらく初見の印象が悪いです。
- 👥 誰向けか: バイブコーディングで AI に長めのコードを書かせていく人。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左にエラーに気づかず困惑する開発者、右に赤線警告を見てうなずく開発者の対比
- 登場人物: 開発者 1 名（Before 側と After 側に各 1 コマ）
- 吹き出し・心の声: Before「なんで動かないんだろう…」/ After「型エラーが出た、すぐ直せる！」
- 中央に置くキーワード/ラベル: TypeScript の型注釈（`: number`）
- Before / After の対比ポイント: 実行前に気づけるかどうか

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: パッケージ箱（インストール）
- Step 2 のアイコン/絵柄: 設定ファイル（歯車）
- Step 3 のアイコン/絵柄: ペン（コーディング）
- Step 4 のアイコン/絵柄: ビルド矢印（JS への変換）
- 矢印で示す流れの意図: 型付き TS → ビルド → 純 JS の変換サイクル

## コミュニティ補完メモ

- F-1 JavaScript との住み分け：F-1 は「JS とは何か・ブラウザでどう動くか」を扱い、F-2 は「JS に型を足した TS の恩恵と使い始め方」にフォーカスします。両エントリで重複する JS の説明は最小限に抑えます。
- F-41 Vite との住み分け：Vite はビルドツール全般を扱うエントリで、TS との組み合わせ例は F-2 側から参照リンクを置くにとどめます。

## 出典メモ

- TypeScript 公式ドキュメント <https://www.typescriptlang.org/> — checked 2026-04-29
- Microsoft TypeScript GitHub <https://github.com/microsoft/TypeScript> — checked 2026-04-29


## 備考

- TypeScript は Microsoft が 2012 年に発表。Anders Hejlsberg（C# の設計者）が中心となって設計した。
- 採用例：VS Code（F-30）、Slack デスクトップ、Asana、Airbnb の型整備など業務系大規模 Web アプリでデファクト化。
- バイブコーディングでの意義：AI が生成したコードを型で受け止めると不整合を早期発見できる。Claude Code・Cursor も TS プロジェクトを得意とする。
- `any` 型は手っ取り早い逃げ道だが型の恩恵がゼロになるため、`unknown` や `never` で締める習慣を推奨する旨を注意点セルに凝縮した。
