---
id: F-61
title: Pull Request
title_reading: プルリクエスト
category: term_tool
subtype: git_workflow
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: workflow
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - git
  - GitHub
  - GitHub Actions
  - branch
status: ready
---

# Pull Request

## tagline

作業ブランチを本流に取り込んでもらう依頼です。コードレビューの中心の場になります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

作業ブランチの差分を main などの本流へ統合してもらう依頼の仕組みです。タイトル・差分・CI の結果・レビュアーのコメントが 1 画面に集まります。

## どこで出会うか

GitHub のリポジトリの「Pull requests」タブから作成します。チーム開発では承認フローの入口になり、1 人開発でも変更履歴として残ります。

## メイン図

### 図の狙い

PR が「依頼 → レビュー → マージ」の流れを担う中継点であることを示します。

### C. 概念図（figure_type: workflow）

- 中心に置く概念: Pull Request（取り込み依頼）
- 周辺の要素: 作業ブランチ、main ブランチ、レビュアー、CI チェック、マージ
- 関係の描き方: 作業ブランチから PR を出し、レビュアーと CI を通過してから main に合流する矢印


## 会話での使い方例

「PR の本文を Claude に書かせると、レビュアーが Why から読めて助かります。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

作業ブランチを本流へ取り込む依頼と、レビューの場を兼ねます。

### 2. うれしさ

変更の意図・差分・CI 結果が 1 画面に集まり、判断が速くなります。

### 3. 注意点

本文に「何を直したか」だけ書き「なぜ直したか」が抜けがちです。

### 4. どこで役立つか

チーム開発のレビューだけでなく、1 人開発の変更履歴管理にも使えます。

### 5. はじめに

PR を作る手順と、タイトル・本文の基本構成を押さえれば始められます。

### 6. 深掘り先

GitHub Actions、コードレビュー、branch


## 開発フローでの位置（必須）

1. ブランチ作成 — git（F-50）で feature ブランチを切ります
2. コミット & プッシュ — 変更を commit してリモートへ push します
3. PR 作成 — Why / What / テスト計画を本文に書いて依頼します
4. レビュー & CI — コメントと GitHub Actions（F-62）の自動チェックを通します
5. マージ — 承認条件を満たしたら main へ取り込んで完了です


## 関連用語

- git
- GitHub
- GitHub Actions
- branch


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 名前が悪くて分かりづらいです。「承認依頼」と理解していますが名前からは結びつきません。
- git のプル・プッシュのリクエストと説明すると理解できますが、日本語でそのまま扱うのは難しいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 名前から動作が想像できません。
- 👍 良い点: 監査の仕組みとしてバイブコーダーには絶対必要なものです。
- 👎 ダメな点: 名前が分かりづらく概念理解に時間がかかります。
- 👥 誰向けか: バイブコーダー全員が押さえるべきです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左に作業者が feature ブランチでコードを書いている様子、中央に「Pull Request」のカード（タイトル・本文・CI バッジが並ぶ）、右にレビュアーが承認してから main ブランチへ矢印でマージされる流れ
- 登場人物: 作業者（コード書いている人）、レビュアー（コメントしている人）
- 吹き出し・心の声: 作業者「なぜ直したかを書いておこう」、レビュアー「Why がわかると判断が楽です」
- 中央に置くキーワード/ラベル: Pull Request
- Before / After の場合の対比ポイント: （workflow のため省略）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ブランチ分岐の図
- Step 2 のアイコン/絵柄: 上矢印（push）
- Step 3 のアイコン/絵柄: PR カード
- Step 4 のアイコン/絵柄: チェックマーク（CI ＋ レビュアー）
- Step 5 のアイコン/絵柄: ブランチ合流（マージ）
- 矢印で示す流れの意図: feature → PR → レビュー通過 → main 合流の一連の流れ

## コミュニティ補完メモ

- F-60 GitHub との住み分け：GitHub はホスティングプラットフォーム全体、F-61 PR はその中の「変更取り込み依頼」機能。GitHub の説明の中で PR に触れるが、本エントリはレビューフロー・本文の書き方・承認条件を中心に扱う
- F-53 branch との住み分け：branch は作業の分岐を作る概念、PR はその branch の成果物を本流へ取り込む依頼の手続き。セットで説明するが別エントリ
- GitLab の Merge Request（MR）は同義だが、本エントリでは GitHub の慣習 PR を主軸に説明し、MR は備考で補足する


## 出典メモ

- GitHub Docs "About pull requests" — checked 2026-04-29
- GitHub Docs "Creating a pull request" — checked 2026-04-29


## 備考

- GitLab では同等機能を Merge Request（MR）と呼ぶ。Bitbucket も PR と呼ぶ
- PR テンプレート（`.github/pull_request_template.md`）を整備すると、本文の Why / What / Test plan が自動で挿入されてチーム全体の品質が揃う
- Claude Code・Cursor など AI ツールが PR の本文を自動生成する使い方が広まっており、CI 失敗時の修正提案まで担うケースもある
