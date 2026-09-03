---
id: F-90
title: Docker
title_reading: ドッカー
category: term_tool
subtype: container
experience_level: partial
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - コンテナ
  - イメージ
  - Dockerfile
  - Docker Compose
  - WSL
status: ready
---

# Docker

## tagline

環境差異を封じ込めるコンテナ型仮想化ツールです。「私のマシンでは動く」問題の定番解決策。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

アプリの実行環境をコンテナ（Container）という軽量な箱にまとめ、どの OS でも同じ状態で動かせます。Dockerfile からイメージ（Image・配布用の雛形）を作り、チームや本番へ渡せます。

## どこで出会うか

AI ツールのローカル実行や開発環境を揃える場面で「Docker で動かしてください」と案内されます。WSL（Windows Subsystem for Linux）と合わせれば Windows でも Linux コンテナが動きます

## メイン図

### 図の狙い

Dockerfile → イメージ → コンテナという 3 段階の流れを 1 枚で見せ、「どの環境でも同じ箱が動く」ことを伝えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: コンテナ（どこでも同じ箱）
- 周辺の要素: Dockerfile（設計図）→ Image（雛形）→ Container（実行）、Mac / Windows / Linux / クラウドの各 OS
- 関係の描き方: 左から右への矢印で Dockerfile → Image → Container を並べ、Container から各 OS 環境への「動く」矢印を出す

## 会話での使い方例

「Dockerfile を書いておけば、環境差異を気にせずチームに配れますよ。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

実行環境をコンテナに封じ込め、どこでも再現できるようにします。

### 2. うれしさ

環境差異を封じ込め、どこでも再現できる環境を配布できます。

### 3. 注意点

初回はイメージのビルド時間がかかります。

### 4. どこで役立つか

AI ツールのローカル実行やチームの環境統一に役立ちます。

### 5. はじめに

Dockerfile・イメージ・コンテナの 3 語の関係が入口になります。

### 6. 深掘り先

Docker Compose、Kubernetes、レジストリ（Docker Hub）。

## 開発フローでの位置（必須）

1. Dockerfile を書く — 使うミドルウェアや設定を 1 ファイルに記述する
2. `docker build` — Dockerfile からイメージを生成する
3. `docker run` — イメージからコンテナを起動し、アプリが動く状態にする
4. イメージを配布 — チームやクラウドへ渡してどこでも同じ環境を再現する

## 関連用語

- コンテナ
- イメージ
- Dockerfile
- Docker Compose
- WSL


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- ローカルでは無料でも会社で使うと利用人数で課金が増え、戸惑います。
- なんでも Docker に乗せようとすると、容量が大きくなり同時並行が大変です。
- VS Code との連携が途中で切れたり、プロセスが死んだりして詰まります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Docker 化すると別の PC でも動かせて安心、という話を聞いて気になりました。
- 👍 良い点: 個人環境を丸ごと別の PC に移して動かせる再現性が魅力です。
- 👎 ダメな点: 一人開発だと過剰になりやすく、動かすリソースもかつかつになります。
- 👥 誰向けか: チーム開発の人向けです。多少のコストを必要経費にできる規模が前提です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左に「Dockerfile（設計図アイコン）」→ 中央に「Image（箱の雛形）」→ 右に「Container（実行中の箱）」を矢印でつなぐ。Container の下に Mac・Windows・Linux・クラウドのロゴを並べ、同じ箱が乗っている絵
- 登場人物: 開発者（1 名）が左端で Dockerfile をパソコンに打ち込んでいる
- 吹き出し・心の声: 開発者「Dockerfile 1 枚書いたら、どこでも同じ環境が動いた」／右端「私のマシンでは動く、を卒業」
- 中央に置くキーワード/ラベル: Dockerfile → Image → Container → どこでも動く

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 設計図アイコン（Dockerfile を書く）
- Step 2 のアイコン/絵柄: ハンマー・ビルドアイコン（docker build）
- Step 3 のアイコン/絵柄: 再生ボタン（docker run）
- Step 4 のアイコン/絵柄: 配布・シェアアイコン（イメージを配る）
- 矢印で示す流れの意図: 設計 → 生成 → 実行 → 共有 のループ


## コミュニティ補完メモ

- Docker Compose（複数コンテナの管理）は本エントリでは深掘り先として 1 語の言及のみ。詳細は別エントリ候補。
- Kubernetes（コンテナオーケストレーション）は規模が大きく別エントリ候補。本エントリは単体 Docker の概念に絞る。
- WSL（F-82）は組み合わせシーンとして「どこで出会うか」に言及。Windows ユーザーへの入口として有効。

## 出典メモ

- docker.com — checked 2026-04-29
- docs.docker.com — checked 2026-04-29

## 備考

- Docker Desktop は個人利用は無料、企業利用は有料プラン（pricing_note: freemium）。2026-04-29 時点。
- OCI（Open Container Initiative）準拠のコンテナランタイムとして Podman なども存在するが、入門語彙として Docker を代名詞として扱う。
