---
id: B-21
title: Netlify
title_reading: ネットリファイ
category: service
subtype: hosting_cloud
experience_level: partial
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
  - デプロイ
  - CI/CD
  - Jamstack
  - サーバレス
  - GitHub
status: ready
---

# Netlify

## tagline

Git push で静的サイトが自動公開される、Jamstack（ジャムスタック）対応のホスティングサービスです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Git リポジトリに push すると自動でビルド・デプロイし、グローバル CDN でサイトを配信します。フォームや認証などの周辺機能も追加できます。

## どこで出会うか

個人ブログや社内ドキュメントを無料で公開したい場面で登場します。AI に静的サイトの公開方法を尋ねると GitHub との連携手順が示されます。

## メイン図

### 図の狙い

「push したらサイトが世界に届く」という流れを 3 段で示し、Netlify がどこで動いているかを掴んでもらいます。

## 会話での使い方例

「Netlify は GitHub に push するだけで静的サイトが公開できます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

push をトリガーにビルド・デプロイ・CDN 配信を自動化します。

### 2. うれしさ

無料枠で個人サイトが立ち、設定ファイルも最小限で済みます。

### 3. 注意点

動的処理は Functions（サーバレス）利用で、制限があります。

### 4. どこで役立つか

ブログや LP など静的サイトの公開・共有に向いています。

### 5. はじめに

GitHub 連携と自動デプロイの流れを最初に押さえます。

### 6. 深掘り先

Jamstack、CI/CD、サーバレス、Vercel（バーセル）。

## 開発フローでの位置（必須）

1. コード編集 — ローカルでサイトの内容を変更し、動作を確認する
2. Git push — GitHub にコードを送ると Netlify が自動で検知する
3. 自動ビルド — Netlify がビルドを実行し、成果物を生成する
4. CDN 配信 — グローバル CDN にデプロイされ、URL でアクセスできる状態になる


## 関連用語

- デプロイ
- CI/CD
- Jamstack
- サーバレス
- GitHub


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- index.html の配置やフォルダ命名のお作法で苦労しました。今は AI エージェントに任せれば困らない領域です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 自分のブログをネットに公開できる感動がありました。
- 👍 良い点: 無料から始められて操作も比較的簡単です。
- 👎 ダメな点: お作法はあり、初心者は AI に伴走してもらわないと詰まりやすいです。
- 👥 誰向けか: ブログや自分のメディアを発信したい人向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左から「Git push」「Netlify 自動ビルド」「CDN 配信」の 3 段フローを矢印でつなぐ
- 登場人物: 開発者（ノート PC で push する人）とサイト閲覧者（スマホでサイトを開く人）の 2 名
- 吹き出し・心の声: 開発者「push しました！」、閲覧者「もう公開されてる、早いですね」
- 中央に置くキーワード/ラベル: push → ビルド → CDN 配信

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ノート PC ＋ 鉛筆（コード編集）
- Step 2 のアイコン/絵柄: 矢印付き Git ブランチ（push）
- Step 3 のアイコン/絵柄: 歯車（自動ビルド）
- Step 4 のアイコン/絵柄: 地球儀＋矢印（CDN 配信）


## コミュニティ補完メモ

- Vercel（B-20）との住み分け：Vercel は Next.js 親和性が高くフロントエンド特化。Netlify は Jamstack 全般に対応し Forms / Identity / Edge Functions などの周辺機能も持つ
- Cloudflare Pages（B-22）との住み分け：Cloudflare は CDN・セキュリティ機能が強み。Netlify は Forms や Identity など独自機能で差別化している
- Forms / Identity / Edge Functions などの周辺機能は本エントリでは名称のみに留め、詳細は各機能エントリへ


## 出典メモ

- netlify.com — checked 2026-04-29


## 備考

- 料金プラン（Starter 無料 / Pro / Enterprise）は時変情報です。evaluation_date を必ず持たせます
- 2010 年代後半に Jamstack という用語の普及とともに広まったサービスです
