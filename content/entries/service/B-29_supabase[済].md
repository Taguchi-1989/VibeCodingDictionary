---
id: B-29
title: Supabase
title_reading: スーパーベース
category: service
subtype: baas
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2020-01-01
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - PostgreSQL
  - Vercel
  - OAuth
  - v0
status: ready
---

# Supabase

## tagline

OSS の BaaS（Backend as a Service）です。PostgreSQL を中核に据えた Firebase 代替です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

DB・認証・ストレージ・Edge Functions・Realtime を 1 サービスで提供します。PostgreSQL ベースで型生成対応 SDK から操作できます。


## どこで出会うか

v0 や Bolt.new がフルスタック雛形を出すとき DB ＋ Auth に選ばれます。「Supabase のプロジェクト URL を教えて」と AI に聞かれたら出会うサインです。


## メイン図

### 図の狙い

Supabase が提供する機能群とフロントエンドの接続関係を 1 枚で示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Supabase（Postgres）
- 周辺の要素（4個）: Auth / Storage / Edge Functions / Realtime
- 関係の描き方（矢印・包含・比較）: 中心から外に向かう放射状の矢印


## 会話での使い方例

「Supabase に Auth と DB をまとめて、フロントは Claude に書かせたら 1 日で動きました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

DB・認証・ストレージを 1 サービスで担う BaaS です。

### 2. うれしさ

PostgreSQL の SQL 構文と型生成で安全に開発できます。

### 3. 注意点

RLS（行レベルセキュリティ）の設定漏れが認可抜けにつながります。

### 4. どこで役立つか

MVP・中規模 SaaS の初期バックエンド構築で役立ちます。

### 5. はじめに

Firebase との違い（OSS・SQL・RLS）を押さえると入りやすいです。

### 6. 深掘り先

PostgreSQL、Row Level Security、pgvector


## 開発フローでの位置（必須）

1. プロジェクト作成 — ダッシュボードで DB と Auth を初期化します
2. スキーマ設計 — SQL エディタでテーブルを定義します
3. SDK 接続 — TypeScript クライアントから CRUD を呼びます
4. 認証設定 — OAuth（B-130）と RLS ポリシーを追加します
5. デプロイ連携 — Vercel（B-20）に URL とキーを渡します


## 関連用語

- PostgreSQL
- Vercel
- OAuth
- v0


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- DB＋認証が一括で乗る利点が最初はピンと来ませんでした。
- SQL エディタの挙動もデータベース概念なしでは理解が難しい部分です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: LLM に「無料 DB ならここ」と紹介されたサイトです。
- 👍 良い点: 慣れれば比較的楽で、AI への委任もしやすい環境です。
- 👎 ダメな点: 初学者にとっての取っ付きにくさはあります。
- 👥 誰向けか: 個人サイトや小〜中規模サービスを運用したい人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Supabase を中心に Auth・Storage・Edge Functions・Realtime が放射状に広がる構成図
- 登場人物（いれば）: スタートアップ開発者（1名）がノートPC を操作している
- 吹き出し・心の声: 「DB も認証もこれ 1 つで足りる」
- 中央に置くキーワード/ラベル: Supabase（Postgres）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ダッシュボードのブラウザ画面
- Step 2 のアイコン/絵柄: テーブル設計の SQL コード断片
- Step 3 のアイコン/絵柄: TypeScript の関数呼び出し
- Step 4 のアイコン/絵柄: 鍵マーク（認証・RLS）
- Step 5 のアイコン/絵柄: Vercel ロゴと矢印

## コミュニティ補完メモ

- Firebase との住み分け：Firebase（Google・NoSQL・Firestore 中心）と Supabase（OSS・PostgreSQL・SQL 中心）は対照的な選択肢。B-29 は SQL を扱いたいケースに絞って説明し、Firebase との比較は「注意点」の補足として備考へ逃がす。
- B-20 Vercel との関係：Vercel はフロントエンドのホスティング、Supabase はバックエンドの DB ＋ Auth 担当として住み分け。

## 出典メモ

- [supabase.com/docs](https://supabase.com/docs) — checked 2026-04-30
- [supabase.com/pricing](https://supabase.com/pricing) — checked 2026-04-30


## 備考

- Firebase との違いは読者がつまずきやすい点。Firebase は NoSQL（Firestore）中心、Supabase は PostgreSQL（SQL）中心。セルフホストも可（Apache 2.0）。
- RLS（Row Level Security）はテーブル単位の認可制御で、設定漏れが致命的なセキュリティ穴になるため注意点に明記した。
- pgvector 拡張を使うと RAG（Retrieval Augmented Generation）に必要なベクトル検索が Postgres 内で完結する（Deep 読者向け補足）。
- pricing_note: freemium（Free プランあり、Pro $25/月〜。evaluation_date: 2026-04-30 時点）。
