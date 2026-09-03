---
id: F-120
title: PostgreSQL
title_reading: ポストグレスキューエル
category: term_tool
subtype: database
experience_level: partial
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - SQLite
  - Prisma
  - ORM
  - Supabase
  - pgvector
status: ready
---

# PostgreSQL

## tagline

オープンソースのリレーショナルデータベース（RDB）です。業務データの格納先として広く選ばれています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

表形式でデータを管理し、SQL で読み書きできる OSS の RDB です。標準 SQL への準拠度が高く、JSON 型や全文検索、pgvector（ベクトル検索）など拡張機能が豊富です。


## どこで出会うか

SaaS（B-43）の本番 DB や Supabase（B-29）の中核として名前が出ます。AWS・Azure・GCP のマネージドサービスでも選べ、LLM に渡す業務データの格納先として登場します。


## メイン図

### 図の狙い

PostgreSQL が「データを受け取る箱」であることと、pgvector で RAG にも使える二刀流の立ち位置を伝えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: PostgreSQL（データベース本体）
- 周辺の要素: SQL クエリ / JSON・JSONB / pgvector / Supabase / ORM / LLM
- 関係の描き方: 矢印（データが流れ込む方向）＋ pgvector からベクトル検索への出力


## 会話での使い方例

「Postgres に pgvector を入れて Embedding の格納先にしました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

業務データを表形式で保存し、SQL で取り出せる RDB です。

### 2. うれしさ

OSS で無料、拡張機能で RAG 向けベクトル検索にも対応できます。

### 3. 注意点

SQLite と違いサーバー起動が必要で、初期構築に手間がかかります。

### 4. どこで役立つか

業務データの格納・検索基盤として SaaS 開発で役立ちます。

### 5. はじめに

テーブル・行・SQL の基本と RDB である点を押さえれば十分です。

### 6. 深掘り先

pgvector、Supabase、ORM


## 開発フローでの位置（必須）

1. DB 選定 — データ規模と拡張性を見て PostgreSQL を選びます
2. スキーマ設計 — テーブルと列を決め ORM（F-123）で反映します
3. データ投入 — API や Supabase 経由で INSERT します
4. クエリ & RAG — SQL 検索や pgvector で Embedding を扱います
5. 運用 — RDS / Cloud SQL などでバックアップを自動化します


## 関連用語

- SQLite
- Prisma
- ORM
- Supabase


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- そもそも読み方が分からず、PostgreSQL の正しい呼び方に迷います。
- データベースや SQL も分からないのに、拡張機能まで重なって理解が追いつきません。
- データの中身がどんな構造で並んでいるのか、イメージしづらいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: SQL 系の中ではデフォルト的に使われている良さげな存在、と感じました。
- 👍 良い点: オープンソースで標準的な選択肢として扱われている安心感があります。
- 👎 ダメな点: データベース自体のハードルが高く、知らない人には敷居がきついです。
- 👥 誰向けか: しっかりとサイトを作っていく人向けで、ここまで使えると強いです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: PostgreSQL サーバーを中心に、左から SQL クエリを投げる開発者、右上に pgvector でベクトルを取り出す LLM、下に Supabase・ORM が並ぶ構成図
- 登場人物: 開発者（ノートPC 持参）、LLM ロボット（ベクトルを受け取る）
- 吹き出し・心の声: 開発者「Postgres に全部まとめてる」、LLM「Embedding ちょうだい」
- 中央に置くキーワード/ラベル: PostgreSQL

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 天秤（選定）
- Step 2 のアイコン/絵柄: 設計図・テーブル
- Step 3 のアイコン/絵柄: データ投入の矢印
- Step 4 のアイコン/絵柄: LLM ＋ 虫めがね
- Step 5 のアイコン/絵柄: 歯車（運用・クラウド）

## コミュニティ補完メモ

- SQLite（F-121）との住み分け: SQLite はサーバー不要の組み込み向け軽量 DB。PostgreSQL は本番・複数接続・拡張機能が必要な場合に選ぶ
- Supabase（B-29）との住み分け: Supabase は PostgreSQL を BaaS（バックエンド・アズ・ア・サービス）としてラップしたサービス。PostgreSQL はその下層エンジン
- MySQL との差異: MySQL も OSS RDBMS だが、PostgreSQL は JSON・配列型・拡張機能の豊富さで差別化される。本図鑑では MySQL 単独エントリは現時点で未収録


## 出典メモ

- [postgresql.org/about](https://www.postgresql.org/about/) — checked 2026-04-29
- [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) — checked 2026-04-29


## 備考

- 通称「Postgres」は公式 FAQ でも認められた略称。正式名称は PostgreSQL
- 料金: OSS 本体は無料。クラウドマネージド（RDS 等）は従量課金
- pgvector は extension として後付けで有効化する（`CREATE EXTENSION vector;`）
