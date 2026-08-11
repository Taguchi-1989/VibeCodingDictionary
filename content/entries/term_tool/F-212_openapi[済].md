---
id: F-212
title: OpenAPI
title_reading: オープンエーピーアイ
category: term_tool
subtype: api_contract
experience_level: partial
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note:
evaluation_date: 2026-08-10
related_terms:
  - API
  - JSON Schema
  - YAML
  - Zod
status: ready
---

# OpenAPI

## tagline

API の仕様を YAML/JSON で機械可読に書く業界標準の記述形式です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

API のエンドポイントやパラメータ、レスポンスの形をひとつのファイルにまとめて定義します。ここから API ドキュメントの自動生成、クライアントコードの生成、モックサーバーの用意までが機械的に行えます。

## どこで出会うか

API を提供する側が入出力や認証の形を YAML/JSON で公開する場面で見かけます。Swagger UI などの画面で仕様書として表示され、旧称は Swagger です。

## メイン図

### 図の狙い

OpenAPI ファイルを中心に置き、そこから仕様書・生成コード・モックサーバーが枝分かれして生まれる様子を見せます。

## 会話での使い方例

「OpenAPI があれば API 仕様書からコードを自動生成できますよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

API の仕様を YAML/JSON で書き表す記述形式です。

### 2. うれしさ

ドキュメントやコードが仕様書から自動で作れます。

### 3. 注意点

現行版は 3.2.0 で、4.0 はまだ設計段階です。

### 4. どこで役立つか

API ドキュメント生成やコード自動生成の場面で使います。

### 5. はじめに

まずはひとつのエンドポイントを YAML で書いてみます。

### 6. 深掘り先

JSON Schema、Swagger UI、コード生成。

## 開発フローでの位置（必須）

1. 仕様書を書く — エンドポイントや入出力を YAML/JSON で記述する
2. ドキュメント生成 — Swagger UI などで仕様書を見やすく表示する
3. コード生成 — 仕様書からクライアントやサーバーのひな形を作る
4. モック・テスト — 仕様書をもとにモックサーバーで先行開発する
5. 保守・更新 — 実装との差分が出ないよう仕様書を更新し続ける

## 関連用語

- API
- JSON Schema
- YAML
- Zod

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 名前が OpenAI と似すぎていて、頭の中で毎回ぶつかる。まずここ。
- 規約の細かいところまでは正直読み切れない。そこは LLM に任せてしまえばいいと思ってしまう。
- バージョンをいくつに合わせるか、更新にどう追従するか、という判断が要ることに気づかない。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: OpenAPI と OpenAI が名前でめちゃくちゃコンフリクトする、というのが第一印象。
- 👍 良い点: API の標準形式なので、それに従っていればいい。細かいところは LLM に書かせられる。
- 👎 ダメな点: やっぱり名前が分かりづらい。混同する。
- 👥 誰向けか: AI フレンドリーにするならここを必ず通ることになる。規格があるから通すべきという判断や、バージョンをどれに合わせるか、更新にどう追従するかまで含めて考える人向け。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に 1 枚の YAML ファイル（OpenAPI 仕様書）を置き、そこから 3 方向に矢印が伸びて「ドキュメント画面」「生成されたコード」「モックサーバー」が生まれる構造図
- 登場人物（いれば）: ファイルを見つめるエンジニア風の人物 1 人
- 吹き出し・心の声: 「この 1 枚を書けば、あとは自動で揃う。」
- 中央に置くキーワード/ラベル: OpenAPI 仕様書（YAML/JSON）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 鉛筆とファイル（仕様書を書く）
- Step 2 のアイコン/絵柄: ブラウザ画面（ドキュメント生成）
- Step 3 のアイコン/絵柄: 歯車とコード片（コード生成）
- Step 4 のアイコン/絵柄: 模擬サーバーの箱（モック・テスト）


## コミュニティ補完メモ

- F-213 API との住み分け：「API とは何か」は F-213 に譲り、本エントリは「API の仕様を機械可読な形式で書く」という記述の話に絞る。
- F-210 JSON Schema との住み分け：値の形の検証ルールそのものは F-210 に譲り、OpenAPI はその上に乗る「API 全体の取扱説明書」として扱う。
- F-7 YAML との住み分け：YAML 自体の書き方は F-7 に譲り、OpenAPI は YAML/JSON を使う代表的な用途のひとつとして触れるにとどめる。
- F-211 Zod との住み分け：TypeScript 側でのスキーマ記述は F-211 に譲る。両者を連携させて型と仕様書を一致させる運用があるが、深掘りはしない。

## 出典メモ

- OpenAPI Initiative 公式サイト — https://www.openapis.org/ — checked 2026-08-10
- OpenAPI Specification 3.2.0 — https://spec.openapis.org/oas/latest.html — checked 2026-08-10
- Moonwalk SIG（次期 4.0 の検討リポジトリ）— https://github.com/OAI/sig-moonwalk — checked 2026-08-10

## 備考

- 2026-08 時点の現行版は 3.2.0（2025-09 リリース）。次期メジャー版 4.0 は「Project Moonwalk」として設計が進んでいる段階で、まだリリースされていない。「4.0 が出た」とは書かないこと。
- 旧称は Swagger。仕様自体の名称は OpenAPI に変わったが、Swagger UI など一部ツール名には今も名残がある。
