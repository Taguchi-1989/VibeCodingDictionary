---
id: F-110
title: Lighthouse
title_reading: ライトハウス
category: term_tool
subtype: quality
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - a11y
  - GitHub Actions
  - Core Web Vitals
  - JavaScript
status: needs_review
---

# Lighthouse

## tagline

Google が提供する Web ページ品質の自動診断ツールです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Performance・Accessibility・SEO など複数項目を 0〜100 点で評価します。Chrome の DevTools から即使え、CLI や CI にも組み込めます。

## どこで出会うか

Chrome の DevTools の「Lighthouse」タブを押すと診断が始まります。AI で書いたコードの品質確認や、PR ごとの自動計測でも使われます。

## メイン図

### 図の狙い

5 つのカテゴリそれぞれにスコアが出る構造を示し、数字が何を意味するかを一目で分かるようにします。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Lighthouse スコアレポート
- 周辺の要素: Performance / Accessibility / Best Practices / SEO / PWA の 5 スコア円
- 関係の描き方: 中央のレポート画面から 5 本の線が各スコアへ伸びる放射状


## 会話での使い方例

「Lighthouse スコアを Claude に渡したら、画像の遅延読み込みまで提案してもらえました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Web ページの品質を 5 カテゴリ・100 点満点で数値化します。

### 2. うれしさ

AI 生成コードの品質を人の目に頼らず機械的に確認できます。

### 3. 注意点

スコアはネットワーク環境や計測タイミングで変動することがあります。

### 4. どこで役立つか

CI に組み込むと PR ごとにスコア低下を自動検出できます。

### 5. はじめに

DevTools の Lighthouse タブと LCP 2.5 秒基準を押さえるのが第一歩です。

### 6. 深掘り先

Core Web Vitals、a11y（F-111）、GitHub Actions（F-62）


## 開発フローでの位置（必須）

1. 手動計測 — DevTools の Lighthouse タブで初回スコアを確認します。
2. 課題特定 — LCP・INP・CLS など Core Web Vitals の低い値を読みます。
3. AI へ依頼 — レポートを渡し、画像最適化などを提案してもらいます。
4. CI で自動化 — Lighthouse CI を GitHub Actions に組み込みます。
5. 基準値の保持 — LCP 2.5 秒など閾値で低下を防ぎます。


## 関連用語

- a11y
- GitHub Actions
- Core Web Vitals
- JavaScript


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 仕組みは分からないまま点数が出てきて、その数字が何を意味するか掴めません。
- 高い方が良いのは分かっても、どう定義されたスコアか説明がしづらいです。
- 改善ヒントが英語で書かれていて、どう直せばよいかさっぱり分かりません。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: F12 で開いて点数まで出る機能があると知って感動しました。
- 👍 良い点: 無料で自分のサイトを評価でき、他人のサイトの採点で遊べるのも楽しいです。
- 👎 ダメな点: 計測に時間がかかり、ローカル環境やユーザー体験までは担保しきれません。
- 👥 誰向けか: 自分の Web サイトを作る人や、ベンチマーク遊びをしたい人に向きます。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Lighthouse レポート画面の模式図。中央にスコア表示パネル、外周に 5 カテゴリのスコア円を放射状に並べる
- 登場人物: 画面を眺めるエンジニア風の人物（横顔）
- 吹き出し・心の声: 「Performance 65 点…画像が重いのか」と考えている
- 中央に置くキーワード/ラベル: Lighthouse Report

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ブラウザ画面（虫眼鏡）
- Step 2 のアイコン/絵柄: スコアゲージ（低得点を指す針）
- Step 3 のアイコン/絵柄: AI チャット吹き出し
- Step 4 のアイコン/絵柄: GitHub ワークフロー矢印
- 矢印で示す流れの意図: 手動確認 → 課題特定 → AI 改善 → 自動監視 の順で品質を守る循環


## コミュニティ補完メモ

- a11y（F-111）との住み分け: F-110 は Lighthouse というツール全体、F-111 は Accessibility（a11y）という概念。Lighthouse は a11y スコアを計測する手段の一つ。
- Core Web Vitals との関係: LCP / INP / CLS は Lighthouse の Performance カテゴリに含まれる指標。別エントリとして詳細を扱う想定。
- GitHub Actions（F-62）との住み分け: F-62 は CI/CD の基盤、F-110 は品質計測ツール。Lighthouse CI は F-62 の上で動くアプリケーションの位置付け。


## 出典メモ

- [Chrome for Developers: Lighthouse overview](https://developer.chrome.com/docs/lighthouse/overview) — checked 2026-04-30
- [web.dev: LCP](https://web.dev/articles/lcp) — checked 2026-04-30


## 備考

- LCP（Largest Contentful Paint）の基準値: 2.5 秒以下 Good / 2.5〜4 秒 Needs Improvement / 4 秒超 Poor。初心者がつまずきやすいため読者のつまずき例として記録。
- Lighthouse CI は Google が提供するオープンソースの npm パッケージで、GitHub Actions などに組み込む形で使う。
