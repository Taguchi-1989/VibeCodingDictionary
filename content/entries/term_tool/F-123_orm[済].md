---
# ── 識別・分類 ──
id: F-123
title: ORM
title_reading: オーアールエム
category: term_tool
subtype: orm

# ── 読者・体験 ──
experience_level: partial
reader_level: 2-3
importance: D

# ── 誌面形式 ──
figure_type: before_after
page_layout: spread_v1

# ── 時変情報 ──
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29

# ── 関係 ──
related_terms:
  - PostgreSQL
  - Prisma
  - TypeScript
  - Python

# ── 制作状態 ──
status: ready
---

# ORM

## tagline

Object-Relational Mapping の略。DB のテーブルをクラスとして扱い、SQL なしで操作する仕組みです。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`User.findById(1)` のような書き方で DB を操作できます。型補完が効き、スキーマ変更もコードに反映されやすく、SQL 直書きより扱いやすいです。


## どこで出会うか

Prisma や TypeORM（TypeScript）、SQLAlchemy（Python）、Active Record（Rails）などのライブラリ名で登場します。AI がスキーマから API を生成する際も ORM 前提が多いです。


## メイン図

### 図の狙い

生 SQL と ORM 記法の対比を示し、「どちらも同じ DB 操作だが書き方が異なる」点を掴んでもらう。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 生 SQL でユーザーを取得する
  - 視覚要素（コード）: `SELECT * FROM users WHERE id = 1;`
  - つまずき: タイプミスや型の不一致がランタイムまで気づけない
- After
  - 状況: ORM 経由で同じ操作
  - 視覚要素: `User.findById(1)`
  - うれしさ: 型補完が効き、スキーマと同期したまま操作できる


## 会話での使い方例

「ORM を使うと、AI がスキーマから API まで一気に書いてくれます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

DB のテーブルとコードのクラスを対応付ける橋渡し役です。

### 2. うれしさ

型補完が効き、スキーマ変更をコードに反映しやすくなります。

### 3. 注意点

複雑なクエリは生 SQL のほうが読みやすい場合があります。

### 4. どこで役立つか

AI がスキーマから API を一気に書く場面で役立ちます。

### 5. はじめに

クラス＝テーブル、オブジェクト＝行という対応関係が基本です。

### 6. 深掘り先

Prisma、SQLAlchemy、N+1 問題


## 開発フローでの位置（必須）

1. スキーマ定義 — DB のテーブル構造をモデルクラスとして記述する
2. マイグレーション — スキーマ変更を DB に適用してテーブルを更新する
3. クエリ記述 — メソッド呼び出しでデータの取得・更新・削除を行う
4. API 実装 — ORM のクエリ結果をそのまま API レスポンスに組み込む


## 関連用語

- PostgreSQL
- Prisma
- TypeScript
- Python


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- table と class の対応や、SQL なしで操作できる仕組みがピンと来ません。
- Prisma など個別実装と ORM という概念名が混ざって登場し、整理がつきません。
- 理解より先に Claude へスキーマ生成を任せて済ませてしまうことが多いです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 名前を見ても何の略か分からず、難しい語だと身構えました。
- 👍 良い点: 楽に DB を扱えるらしい、というところまでは想像できます。
- 👎 ダメな点: 自分の中で噛み砕けておらず、現時点では勉強中の概念です。
- 👥 誰向けか: しっかり理解したい人向けです。私自身もまだ追いついていません。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に生 SQL 文、右に ORM のメソッド呼び出しを並べた Before/After 対比
- 登場人物（いれば）: エンジニア風の人物が左側で SQL を眺めて首をかしげ、右側でコード補完に「おっ」と反応している
- 吹き出し・心の声: Before「型間違えた…」／After「補完が効いて楽です。」
- 中央に置くキーワード/ラベル: ORM
- Before / After の対比ポイント: SQL 直書き vs メソッド呼び出し

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: テーブル定義書
- Step 2 のアイコン/絵柄: 矢印付きのデータベースシリンダー
- Step 3 のアイコン/絵柄: コードエディタ
- Step 4 のアイコン/絵柄: API エンドポイント
- 矢印で示す流れの意図: スキーマ → DB 同期 → クエリ → API の直線的な流れ


## コミュニティ補完メモ

- F-122 Prisma との住み分け：Prisma は ORM の代表実装（TypeScript 向け）。ORM はその上位概念なので、「ORM とは何か」の理解を本エントリで済ませ、Prisma での具体操作は F-122 へ誘導する。
- F-120 PostgreSQL との住み分け：PostgreSQL は ORM が内部で接続する DB 本体。ORM は DB の種類に関わらず同じ書き方を提供する層である点を補足。

## 出典メモ

- Prisma ORM 公式ドキュメント <https://www.prisma.io/docs> — checked 2026-04-29
- SQLAlchemy 公式ドキュメント <https://docs.sqlalchemy.org/> — checked 2026-04-29


## 備考

- N+1 問題（関連データを 1 件ずつ追加クエリしてしまう問題）は ORM 使用時の典型的パフォーマンス罠。開発中はクエリログを有効にすることで早期発見できる。
- Prisma / TypeORM / Drizzle ORM（TypeScript）、Sequelize（JS/TS）、SQLAlchemy（Python）、Hibernate（Java）、Active Record（Ruby）が代表実装。
