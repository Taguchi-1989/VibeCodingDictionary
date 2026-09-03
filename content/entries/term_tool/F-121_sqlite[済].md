---
id: F-121
title: SQLite
title_reading: エスキューライト
category: term_tool
subtype: database
experience_level: partial
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2000-08-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - PostgreSQL
  - Prisma
  - ORM
  - SQLite MCP
status: ready
---

# SQLite

## tagline

サーバ不要で動く組込み型リレーショナルデータベースです。1 つの `.db` ファイルにテーブルとデータがまるごと収まります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ライブラリとしてファイルを直接読み書きするため、常駐プロセスの起動が不要です。SQL でデータを扱いつつ、準備はファイル 1 つで済みます。

## どこで出会うか

iOS・Android・Chrome の内部で採用されています。ローカル開発で「サーバなしで DB を試したい」場面や、SQLite MCP 経由で AI が SQL を実行する場面でも使われます。

## メイン図

### 図の狙い

「ファイル 1 つ＝DB 1 つ」という構造を、PostgreSQL などのサーバ型 DB との対比で示します。

### B. 登場シーン（figure_type: structure）

- シーン1: 開発者がローカル環境で `.db` ファイルをそのままアプリに渡す
- シーン2: スマートフォンアプリが端末内の SQLite ファイルにデータを保存する
- シーン3: AI ツールが SQLite MCP 経由でファイルを直接クエリする
- 並べる基準: 「ファイル直アクセス」という共通点で 3 シーンを並置


## 会話での使い方例

「ちょっとしたデータ集計なら SQLite を 1 ファイル作るだけで済みます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

テーブルとデータを `.db` ファイル 1 つにまとめる組込み DB エンジンです。

### 2. うれしさ

サーバ起動ゼロで SQL が使えるため、試作や小規模アプリの立ち上げが速いです。

### 3. 注意点

ネットワーク越しの同時書き込みに弱く、大量同時アクセスには向きません。

### 4. どこで役立つか

ローカル開発・テスト環境・モバイルアプリの設定保存で役立ちます。

### 5. はじめに

「ファイル 1 つが DB 1 つ」という概念と、SQL で操作できる点を押さえましょう。

### 6. 深掘り先

PostgreSQL（F-120）、Prisma（F-122）、SQLite MCP（I-41）


## 開発フローでの位置（必須）

1. 設計 — データ構造を決め `.db` ファイルを作成する
2. ローカル開発 — SQL でテーブルを作りアプリから読み書きする
3. テスト — ファイルをコピーするだけで環境を複製できる
4. 本番移行判断 — 同時アクセスが増えたら PostgreSQL 等へ切り替えを検討する


## 関連用語

- PostgreSQL
- Prisma
- ORM
- SQLite MCP


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- そもそも読み方が分からず、PostgreSQL との違いも掴みづらいです。
- SQL 自体のハードルもあり、何のソフトで中身を見ればよいか分かりません。
- ローカルにあると言われても、実態がどこに置かれているのかが見えづらいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: ローカルで完結する点に魅力を感じ、軽さに惹かれました。
- 👍 良い点: サーバを立てずに 1 ファイルで DB が使える手軽さが嬉しいです。
- 👎 ダメな点: どこに実体があるか馴染みが薄く、慣れるまで分かりづらいです。
- 👥 誰向けか: 開発者向けで、ローカル試作やテスト用途で力を発揮します。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左に「SQLite」＝ファイルアイコン 1 つ、右に「PostgreSQL」＝サーバラック図で対比
- 登場人物: 開発者（男性・カジュアル）がノートPCの前に座っている
- 吹き出し・心の声: 「サーバ立てなくていいの？楽だ！」
- 中央に置くキーワード/ラベル: `.db ファイル = DB 本体`

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ファイル作成アイコン
- Step 2 のアイコン/絵柄: SQL コード片（CREATE TABLE）
- Step 3 のアイコン/絵柄: ファイルコピーの矢印
- Step 4 のアイコン/絵柄: 分岐サイン（小規模 ← → 大規模）
- 矢印で示す流れの意図: ローカル完結から本番判断までの自然な流れ


## コミュニティ補完メモ

- PostgreSQL（F-120）との住み分け：SQLite はサーバ不要の小規模・ローカル向け、PostgreSQL はネットワーク越しの同時接続が必要な本番向け。「小さく始めて PostgreSQL に乗り換える」流れとして隣接エントリで補完する
- Prisma（F-122）との住み分け：Prisma は ORM レイヤーで、SQLite を背後の DB として使える。セットとして紹介可能
- SQLite MCP（I-41）との住み分け：I-41 は「AI が SQLite を操作する手段」の説明に集中する。SQLite 本体の解説は本エントリで完結させる


## 出典メモ

- [sqlite.org](https://www.sqlite.org/index.html) — checked 2026-04-29
- [sqlite.org/mostdeployed](https://www.sqlite.org/mostdeployed.html)（世界で最も使われている DB の根拠） — checked 2026-04-29


## 備考

- SQLite の開発は D. Richard Hipp が 2000 年に開始。現在もオープンソースとして活発に継続中
- バージョン 3 系（SQLite3）が現行標準。Python 標準ライブラリにも `sqlite3` モジュールとして同梱されている
- ロック方式はデータベースファイル全体にかかる（WAL モードで緩和可）。大量同時書き込みが必要な本番環境では PostgreSQL / MySQL への切り替えを検討する
