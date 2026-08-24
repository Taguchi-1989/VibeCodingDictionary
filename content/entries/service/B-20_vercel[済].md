---
id: B-20
title: Vercel
title_reading: バーセル
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
  - Next.js
  - デプロイ
  - Preview URL
  - CI/CD
status: ready
---

# Vercel

## tagline

Git（ギット）に push するだけで Web サイトが公開される、フロントエンド特化のホスティングサービスです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Git リポジトリに push すると自動でビルド・デプロイし、Preview URL を発行します。Next.js の開発元が運営するためフロントエンド向け設定が最初から整っています。

## どこで出会うか

AI に「Web アプリを作って」と頼むと出力に Vercel への公開手順が含まれます。GitHub 連携で本番 URL が数十秒で出るので試作品の社外共有でも名前が出ます。

## メイン図

### 図の狙い

「コードを push したら URL が出る」という 3 段の流れを 1 枚に収め、Vercel が間に何をしているかを掴んでもらいます。

### B. 登場シーン（figure_type: structure）

- シーン1: 開発者がローカルで変更を加え、GitHub に push する
- シーン2: Vercel が自動検知してビルド — Preview URL が発行される
- シーン3: 問題なければ確認後に Production（本番）URL に昇格
- 並べる基準: push → Preview → Production の時系列


## 会話での使い方例

「PR ごとに Preview URL が出るので、デザイナーにもすぐ確認してもらえます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

push をトリガーにビルド・デプロイ・URL 発行を自動化します。

### 2. うれしさ

設定なしで Next.js が動き、URL が即日もらえます。

### 3. 注意点

フロントエンド特化のため、バックエンド処理は別途用意が必要です。

### 4. どこで役立つか

試作品の外部共有や、PR ごとの確認 URL 配布に便利です。

### 5. はじめに

push で URL が出る流れとプレビュー・本番の 2 段階を押さえます。

### 6. 深掘り先

Next.js、CI/CD、デプロイ、v0（ブイゼロ）。

## 開発フローでの位置（必須）

1. コード編集 — ローカルで変更を加え、動作を確認する
2. Git push — GitHub にコードを送ると Vercel が自動で検知する
3. Preview 確認 — 発行された Preview URL でステークホルダーがレビューする
4. 本番リリース — 問題がなければ Production URL に昇格して公開完了


## 関連用語

- Next.js
- デプロイ
- Preview URL
- CI/CD


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Pro に上げたら無料分が消えた感覚で、課金の境目が分かりづらいです。
- Hobby は個人限定で商用は Pro（月 20 ドル〜）必須。ビルドが増えると毎月溶けます。
- 環境変数のダッシュボード設定に慣れるまでローカルとの差で戸惑います。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Web アプリ作成で Next.js のデプロイ先として真っ先に勧められます。
- 👍 良い点: 環境変数を入れれば外部サービス連携も完結します。
- 👎 ダメな点: Pro 以上の従量課金が高くつき、ビルドだけで月の予算が溶けがちです。
- 👥 誰向けか: 自分の Web アプリを公開してみたいバイブコーディング中級者向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左から「Git push」「Vercel 自動ビルド」「Preview URL 発行」「Production 公開」の 3 段フローを矢印でつなぐ
- 登場人物: 開発者（ノート PC で push する人）とレビュアー（スマホで Preview URL を開く人）の 2 名
- 吹き出し・心の声: 開発者「push しました！」、レビュアー「URL すぐ来た、確認できます」
- 中央に置くキーワード/ラベル: push → Preview → Production

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ノート PC ＋ 鉛筆（コード編集）
- Step 2 のアイコン/絵柄: 矢印付き Git ブランチ（push）
- Step 3 のアイコン/絵柄: スマホ画面にチェックマーク（Preview 確認）
- Step 4 のアイコン/絵柄: ロケット（本番リリース）
- 矢印で示す流れの意図: push 1 回で公開まで完結する速さを強調


## コミュニティ補完メモ

- Next.js の機能詳細（Pages Router / App Router 等）は F-11 で扱います。本エントリは「Vercel でホスティングする」流れに絞ります
- v0（AI でフロントエンドを生成するサブサービス）は B-9 で独立扱いです。本エントリでは名称のみ触れる範囲とします
- CI/CD の概念一般は別エントリ候補です。本エントリは Vercel 固有の自動デプロイに絞ります


## 出典メモ

- https://vercel.com — checked 2026-04-29


## 備考

- 料金プラン（Hobby 無料 / Pro / Enterprise）は時変情報です。evaluation_date を必ず持たせます
- Next.js を作った会社（Vercel 社）がホスティングサービスも提供している点は、読者が混乱しやすいポイントのため「何をしてくれるか」に明示しました
