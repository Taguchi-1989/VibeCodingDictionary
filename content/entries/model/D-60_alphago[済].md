---
# ── 識別・分類 ──
id: D-60
title: AlphaGo
title_reading: アルファゴ
category: model
subtype: historical

# ── 読者・体験 ──
experience_level: research_only
reader_level: 2-3
importance: C

# ── 誌面形式 ──
figure_type: timeline
page_layout: spread_v1

# ── 時変情報 ──
start_date: 2016-03-09
end_date:
version_status: deprecated
pricing_note: none
evaluation_date: 2026-04-30

# ── 関係 ──
related_terms:
  - Google DeepMind
  - Deep Learning
  - 強化学習
  - AlphaZero

# ── 制作状態 ──
status: ready
---

# AlphaGo

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

Google DeepMind が開発した囲碁 AI です。2016 年にトップ棋士を破り「AI が人間を超えた」と知られます。

## 何をしてくれるか

深層学習・強化学習・モンテカルロ木探索（MCTS）を組み合わせて囲碁を学習します。人間の棋譜で基礎を身につけ、自己対局を重ねて棋力を高めます。

## どこで出会うか

AI の歴史を説明する記事や書籍で頻繁に登場します。「2016 年 3 月の Lee Sedol 戦」は生成 AI ブームの起点として語られることが多く、業界の文脈を共有する場面で名前が出ます。

## メイン図

### 図の狙い

AlphaGo から AlphaZero・MuZero へと発展する系譜を時系列で示し、技術の連なりを掴んでもらう。

### C. 概念図（figure_type: timeline）

- 中心に置く概念: AlphaGo（2016）→ AlphaGo Zero（2017）→ AlphaZero（2018）→ MuZero（2019）
- 周辺の要素: DeepMind / 強化学習 / 自己対局 / MCTS
- 関係の描き方: 時系列の矢印で系譜をつなぐ

## 会話での使い方例

「AlphaGo の Lee Sedol 戦から数えると、生成 AI も同じくらいインパクトがありますね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

DeepMind の囲碁 AI 研究プロジェクトです。

### 2. うれしさ

強化学習と深層学習の組み合わせが実証されました。

### 3. 注意点

商用ツールではなく、現在は研究段階で終了しています。

### 4. どこで役立つか

AI の歴史文脈を説明する際に参照されます。

### 5. はじめに

2016 年の Lee Sedol 戦と DeepMind の名前を押さえます。

### 6. 深掘り先

AlphaZero、MuZero、Google DeepMind

## 開発フローでの位置（必須）

1. 棋譜学習 — 人間の棋譜データで基礎パターンを習得します
2. 自己対局 — AI 同士の対局を繰り返して棋力を強化します
3. 評価対局 — 人間のトップ棋士と対局し性能を検証します
4. 系譜継承 — AlphaGo Zero・AlphaZero へ手法を引き継ぎます


## 関連用語

- Google DeepMind
- Deep Learning
- 強化学習
- AlphaZero

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 名前は知っていても、どんな仕組みで動いているのかは難しいです。
- LLM などの現在の AI とどうつながっているのかが分かりにくいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: AI 史の象徴的な転換点の一つだと思います。
- 👍 良い点: 人類をある側面で超えたことが明確に語りやすいです。
- 👎 ダメな点: AlphaGo 自体は一般人が触れるサービスではなかった点です。
- 👥 誰向けか: AI の歴史を語りたい人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: AlphaGo → AlphaGo Zero → AlphaZero → MuZero の系譜を横一列の時系列で描く
- 登場人物: 棋士風の人物（Lee Sedol 役）と AI の対局シーンを左端に添える
- 吹き出し・心の声: 人物「これが AI に負けた瞬間…」／ AI「自己対局で強くなりました。」
- 中央に置くキーワード/ラベル: 「2016 Lee Sedol 戦」の吹き出しを起点に矢印で展開

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 棋譜データの束
- Step 2 のアイコン/絵柄: AI 同士が向かい合う碁盤
- Step 3 のアイコン/絵柄: 人間棋士と対局する場面
- Step 4 のアイコン/絵柄: AlphaZero へ向かう矢印
- 矢印で示す流れの意図: 学習 → 対局強化 → 実証 → 技術継承の流れ

## コミュニティ補完メモ

- C-3 Google DeepMind との住み分け：C-3 は組織全体（DeepMind の設立・事業・研究領域）を扱う。D-60 は AlphaGo という個別プロジェクトに絞り、技術手法と歴史的意義を中心とする
- C-52 Demis Hassabis との住み分け：C-52 は人物（Hassabis の経歴・思想）。D-60 では名前には触れず、プロジェクトの技術系譜を主軸にする
- J-11 Deep Learning との住み分け：J-11 は技術の原理を扱う。D-60 では「深層学習を応用した事例」として位置づける
- AlphaGo 自体は商用サービスとして提供されていない。「今も使える？」という読者の疑問は非エンジニアのつまずき欄に回す


## 出典メモ

- DeepMind 公式ブログ "AlphaGo" — checked 2026-04-30
- ドキュメンタリー映画『AlphaGo』（2017, Reel As Dirt）— checked 2026-04-30
- Nature 論文 "Mastering the game of Go with deep neural networks and tree search"（2016）— checked 2026-04-30


## 備考

- Lee Sedol 氏は 2019 年に囲碁プロ引退を表明。引退声明で AlphaGo を理由の一つに挙げた
- AlphaGo → AlphaGo Zero（2017、人間棋譜不要）→ AlphaZero（2018、チェス・将棋・囲碁を 1 手法で）→ MuZero（2019、ルール未知でも学習）という技術系譜
- バイブコーディング業界との直接的な技術的つながりは薄いが、「AI が人間を超えた象徴的事件」として業界文脈の共有に使われる
