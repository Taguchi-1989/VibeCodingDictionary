---
id: B-28
title: Render
title_reading: レンダー
category: service
subtype: hosting_cloud
experience_level: partial
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2018-01-01
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Vercel
  - GitHub
  - デプロイ
  - Heroku
status: ready
---

# Render

## tagline

GitHub（ギットハブ）に push するだけでアプリ・DB をまとめて公開できる汎用 PaaS です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Web サービス・静的サイト・API サーバ・バックグラウンドワーカー・Cron Job・PostgreSQL（ポストグレスキューエル）・Redis（レディス）を 1 つの管理画面で扱えます。

## どこで出会うか

AI が書いたサンプルアプリを世界に公開する手順を調べると名前が出てきます。Heroku（ヘロク）より安価な代替として個人開発コミュニティでも紹介されることがあります。

## メイン図

### 図の狙い

「GitHub への push 1 回でアプリと DB が公開状態になる」流れと、Render が引き受けるサービス群を 1 枚で掴んでもらいます。

### B. 登場シーン（figure_type: structure）

- シーン1: 開発者が GitHub に push → Render が自動でビルド・デプロイを実行する
- シーン2: PR を出すとプレビュー環境が自動生成され、URL が届く
- シーン3: PostgreSQL や Redis も同じ管理画面でプロビジョニングして接続する
- 並べる基準: push → プレビュー → 本番 + DB 追加の時系列


## 会話での使い方例

「Claude が書いた API を Render にデプロイして、フロントは Vercel にしました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Web サービスから DB まで一元管理できる汎用ホスティング基盤です。

### 2. うれしさ

push するだけで本番 URL が出て、DB も同じ画面で用意できます。

### 3. 注意点

無料プランは一定時間で休止し、常時稼働には有料プランが必要です。

### 4. どこで役立つか

AI 生成の API を素早く公開したい個人開発に向いています。

### 5. はじめに

Vercel はフロント特化、Render はバックエンド・DB まで含む汎用 PaaS です。

### 6. 深掘り先

Vercel、GitHub、Heroku、デプロイ。

## 開発フローでの位置（必須）

1. コード編集 — AI の助けでアプリ・API コードをローカルで作成する
2. GitHub push — コードを push すると Render が自動でビルドを開始する
3. プレビュー確認 — PR ごとに発行される URL で動作を確認する
4. 本番リリース — マージ後に本番 URL に自動昇格して公開完了


## 関連用語

- Vercel
- GitHub
- デプロイ
- Heroku


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 環境変数の設定場所が分かりづらく、本番だけ落ちることがあります。
- フロントと分けると複雑になるので本体ごと Render に入れる方が楽です。
- 管理画面がとっつきにくく、最初はどのメニューを開けばよいか迷います。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: LLM が「Render がいい」と勧めてくる候補です。
- 👍 良い点: FastAPI / Flask を無料でデプロイできます。
- 👎 ダメな点: 無料プランはコールドスタートで 30 秒かかりストレスです。
- 👥 誰向けか: Python バックを無料で公開したい個人開発者向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左から「GitHub push」「Render 自動ビルド」「本番 URL 発行」の矢印フローを中央に置き、右側に「PostgreSQL・Redis」のアイコンを同じ管理画面内として囲む
- 登場人物: 開発者（ノート PC を操作する人）1 名
- 吹き出し・心の声: 開発者「push したら API も DB もまとめて動いた」
- 中央に置くキーワード/ラベル: push → ビルド → 公開

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ノート PC ＋ AI アシスタント（コード生成）
- Step 2 のアイコン/絵柄: 矢印付き Git ブランチ（push）
- Step 3 のアイコン/絵柄: スマホ画面にチェックマーク（プレビュー確認）
- Step 4 のアイコン/絵柄: ロケット（本番リリース）
- 矢印で示す流れの意図: push 1 回でアプリと DB が同時に立ち上がる速さを強調


## コミュニティ補完メモ

- Vercel（B-20）との住み分け：Vercel は Next.js など SSR/SSG フロントエンドに最適化、Render はバックエンド API・Worker・DB まで含む汎用 PaaS。組み合わせて使う構成が多い
- Netlify（B-21）との住み分け：Netlify も静的サイトに強いが、Render は PostgreSQL・Redis などバックエンドリソースを同一管理画面で扱える点で異なる
- Heroku との比較は読者がよく気にするため「どこで出会うか」に 1 句入れた。Heroku 詳細は独立エントリ候補


## 出典メモ

- <https://render.com> — checked 2026-04-30
- <https://render.com/pricing> — checked 2026-04-30


## 備考

- 無料プランは一定時間アクセスがないとインスタンスが休止する仕様（スピンダウン）。起動に数十秒かかることがある。常時稼働には Starter（$7/月）以上が必要
- 料金：無料プラン / Starter $7/月 / Standard $25/月（2026-04-30 時点）。時変情報のため evaluation_date を付けた
- Heroku は 2022 年に無料プランを廃止したことで Render への移行が広まった経緯がある
