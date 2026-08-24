---
id: B-22
title: Cloudflare
title_reading: クラウドフレア
category: service
subtype: hosting_cloud
experience_level: research_only
reader_level: 2-3
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - CDN
  - Workers
  - DNS
  - DDoS 対策
  - R2
status: ready
---

# Cloudflare

## tagline

Web サイトを高速・安全に届ける CDN（コンテンツ配信網）が中核のクラウドサービスです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

世界に分散したサーバーから、利用者に近い拠点でコンテンツを配信します。DDoS（分散型サービス妨害）の遮断、DNS（名前解決）管理、Workers でのエッジ実行、R2 ストレージも揃います。

## どこで出会うか

「Cloudflare が保護しています」の表示や DNS 画面のオレンジ色のアイコンが最初の接点になりがちです。AI でアプリを作った後に「Workers にデプロイ」と勧められる場面もあります。

## メイン図

### 図の狙い

Cloudflare が「Web の前に立つ傘」として CDN・DDoS 防御・Workers・R2 を一手に担う構造を示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Cloudflare（Web の前に立つ傘）
- 周辺の要素: CDN（高速配信）／DDoS 対策（攻撃遮断）／Workers（エッジ実行）／R2（ストレージ）／DNS（名前解決）
- 関係の描き方: 上部にインターネット、下部にオリジンサーバー、中間に Cloudflare の傘が広がる構図


## 会話での使い方例

「Cloudflare の Workers にデプロイすれば、サーバー不要でエッジから配信できます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Web トラフィックの前に立ち、配信・防御・実行を担います。

### 2. うれしさ

無料プランで CDN と DDoS 対策が使えます。

### 3. 注意点

Workers の実行環境は通常の Node.js と異なる点があります。

### 4. どこで役立つか

サイトの高速化やサーバーレス配信に向いています。

### 5. はじめに

CDN と DNS の役割を押さえると全体像が見えてきます。

### 6. 深掘り先

CDN、Workers、R2、Vercel、Netlify。

## 開発フローでの位置（必須）

1. ドメイン設定 — DNS を Cloudflare に向けてトラフィックを通します
2. CDN 有効化 — キャッシュとセキュリティが自動で機能します
3. Workers 開発 — エッジで動くコードを書いてデプロイします
4. R2 連携 — 画像や静的ファイルを S3 互換ストレージに置きます
5. 監視 — アクセスログや攻撃の遮断状況をダッシュボードで確認します


## 関連用語

- CDN
- Workers
- DNS
- DDoS 対策
- R2


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 管理画面が英語中心で取っ付きにくく、内部検索もトップから辿る前提で使いづらいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: CDN とドメイン管理を一括でやってくれる印象です。
- 👍 良い点: 提供範囲が広く価格も安め、信頼できるブランドです。
- 👎 ダメな点: 管理画面の検索機能の使い勝手はいまひとつです。
- 👥 誰向けか: 公開・運用まで通したいバイブコーダー向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 上から「インターネット（雲）」→「Cloudflare の傘」→「オリジンサーバー」の縦構造。傘の左右に CDN・DDoS 対策・Workers・R2・DNS のラベルが枝で伸びる
- 登場人物: 担当者（PC でサイト表示を確認する人）が手前に立ち、「サイトが速くなった」と見ている構図
- 吹き出し・心の声: 担当者「攻撃も防いでくれるのか…」「なぜか設定だけで速くなった」
- 中央に置くキーワード/ラベル: Cloudflare ＝ Web の前に立つ傘

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: DNS ゾーンアイコン（ドメイン設定）
- Step 2 のアイコン/絵柄: 盾アイコン（CDN・防御有効化）
- Step 3 のアイコン/絵柄: コードエディタ＋稲妻（Workers 開発）
- Step 4 のアイコン/絵柄: バケット＋ファイルアイコン（R2 連携）
- Step 5 のアイコン/絵柄: グラフ・ダッシュボードアイコン（監視）


## コミュニティ補完メモ

- Vercel（B-20）・Netlify（B-21）との住み分け：ホスティング軸では競合するが、Cloudflare の本来の強みは CDN・セキュリティ。Workers はエッジ実行に特化しており、フロントエンド特化の Vercel とは用途が異なります
- AWS（B-23）との住み分け：AWS は汎用クラウド全般、Cloudflare は「Web の前に立つ特化型」。S3 の代替として R2 を使うケースもある
- CDN の概念詳細は別エントリ候補。本エントリは Cloudflare が提供するサービス群の全体像に絞ります
- D1（SQLite ベース DB）は近年追加されたサービスだが、本エントリのスコープ外。備考に補足

## 出典メモ

- cloudflare.com — checked 2026-04-29
- developers.cloudflare.com/workers/ — checked 2026-04-29


## 備考

- Workers の実行環境は V8 ベースで、Node.js API の一部が使えない制約があります（時変情報）
- R2 は S3 互換のオブジェクトストレージで、Cloudflare 内からのアクセスは無料（エグレス料金なし）が特徴です
- D1（SQLite ベース DB）・Pages（静的サイトホスティング）も近年提供開始。本エントリでは主要 5 サービス（CDN・DDoS・Workers・R2・DNS）に絞りました
- 料金：無料プランあり、Pro／Business／Enterprise と拡張。pricing_note: freemium
