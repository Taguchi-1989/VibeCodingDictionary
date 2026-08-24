---
id: F-60
title: GitHub
title_reading: ギットハブ
category: term_tool
subtype: github
experience_level: partial
reader_level: 2
importance: B
figure_type: structure
page_layout: spread_v1
start_date: 2008-04-10
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - git
  - Pull Request
  - GitHub Actions
  - リポジトリ
  - Issue
status: ready
---

# GitHub

## tagline

git のコードをクラウドで管理し、チームで共有・レビューできるホスティングサービスです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

git（ギット）の変更履歴をネット上に保存し、チーム全員が同じリポジトリにアクセスできます。コードレビュー・Issue（課題管理）・CI/CD もここに集まります。

## どこで出会うか

「GitHub にコードを上げておいて」「PR（Pull Request）を送って」というチーム開発の日常会話に登場します。OSS の参照先 URL としても頻出します。

## メイン図

### 図の狙い

GitHub が提供するリポジトリ・Issue・PR・Actions の 4 機能を傘の構造で示し、「コードを起点に開発のやり取り全体がここに集まる」ことを伝えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: GitHub リポジトリ
- 周辺の要素（4 個）: Issue（課題管理）／Pull Request（変更レビュー）／GitHub Actions（自動テスト・デプロイ）／GitHub Copilot（AI 補完・B-5）
- 関係の描き方: 中心のリポジトリから各機能が放射状に伸びる構造図。人物がリポジトリを囲んで作業している様子を添える

## 会話での使い方例

「コードは GitHub に上げてあるので、Issue で修正依頼をもらえれば PR で対応できます。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

git リポジトリをクラウドで共有し、レビューと自動化を一箇所にまとめます。

### 2. うれしさ

変更の経緯が残り、PR でレビューして取り込む流れが自然に整います。

### 3. 注意点

git の操作ミスはそのまま履歴に残るため、push 前の確認が大切です。

### 4. どこで役立つか

チーム開発・OSS 貢献・AI ツールの設定共有のどれでも拠点になります。

### 5. はじめに

リポジトリの作成・push・PR の 3 操作が最初の壁です。

### 6. 深掘り先

Pull Request（F-61）、GitHub Actions（F-62）、git（F-50）

## 開発フローでの位置（必須）

1. リポジトリを作成 — GitHub 上に新しいリポジトリを作り、git と紐づけます
2. コードを push — ローカルの変更を `git push` でリモートリポジトリへ送ります
3. PR を作成 — 変更を本線へ取り込む提案を出し、チームにレビューを依頼します
4. Issue・Actions で管理 — 課題を Issue に記録し、Actions で自動テストを走らせます

## 関連用語

- git
- Pull Request
- GitHub Actions
- リポジトリ
- Issue

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 社内導入時に相当な抵抗があり、英語画面で操作に慣れるまで時間がかかりました。
- GitHub エコシステムの強さは動かさないと分からず認識にハードルがある。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: エンジニアが良いと言っていても最初は良さが分かりませんでした
- 👍 良い点: 無料範囲が広くプライベートと公開を分けて使えて超便利です
- 👎 ダメな点: とっかかりが少し難しいです。
- 👥 誰向けか: エージェントワークをする人にはほぼ全員向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「GitHub リポジトリ」のアイコン（オクトキャット風の雲）を置き、上下左右に Issue・PR・Actions・Copilot の 4 機能が伸びる傘型の構造図
- 登場人物: 開発者 2〜3 名がリポジトリを囲んで作業している様子。1 人はコードを push し、もう 1 人は PR をレビューしている
- 吹き出し・心の声: 「PR 送っておきました」「Issue にコメントしておきます」
- 中央に置くキーワード/ラベル: GitHub リポジトリ（コードの拠点）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 雲＋プラス — リポジトリ作成
- Step 2 のアイコン/絵柄: 上矢印＋クラウド — push
- Step 3 のアイコン/絵柄: 吹き出し＋矢印 — PR レビュー
- Step 4 のアイコン/絵柄: チェックリスト＋歯車 — Issue・Actions 管理
- 矢印で示す流れの意図: コードを上げる → レビューされる → 管理される、という開発ループ


## コミュニティ補完メモ

- git（F-50）との住み分け：git はバージョン管理の仕組みそのもの。GitHub は git リポジトリをクラウドでホストするサービス（Microsoft 傘下）。本エントリは「GitHub というサービス上で何ができるか」に絞ります
- Pull Request（F-61）との住み分け：PR は GitHub の代表機能の 1 つですが、仕組みと使い方は F-61 で深掘りします。本エントリでは登場シーンの紹介にとどめます
- GitHub Actions（F-62）との住み分け：CI/CD 自動化の詳細は F-62 で扱います。本エントリでは「自動テストもここに集まる」の一言だけ触れます
- GitHub Copilot（B-5）との住み分け：Copilot は GitHub の AI 補完サービス。本エントリは Copilot ではなくリポジトリ管理・レビュー機能を主眼とします
- GitLab・Bitbucket 等の競合：同様のホスティングサービスとして存在しますが、本エントリのスコープ外です。深掘り先として注記するにとどめます
- GitHub MCP（I-11）：GitHub の MCP 統合は別エントリで扱います

## 出典メモ

- github.com — checked 2026-04-29
- docs.github.com — checked 2026-04-29

## 備考

- 料金：個人向け Free / Pro（月 $4）/ Team（月 $4/ユーザー）/ Enterprise の多段プランがあり時変性が高いため、本文では触れず evaluation_date で管理します
- 2008-04 にローンチ。2018-06 に Microsoft（マイクロソフト）が買収。現在も独立ブランドで運営されています
- git と GitHub は別物ですが、初学者が混同しやすい組み合わせです。F-50 の備考にも同様の注記があります
