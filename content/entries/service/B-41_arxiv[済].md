---
id: B-41
title: arXiv
title_reading: アーカイヴ
category: service
subtype: info_source
experience_level: research_only
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 1991-08-14
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Transformer 論文
  - Deep Learning
  - Reddit
  - Papers With Code
status: ready
---

## tagline

査読前の論文を無料で公開するプレプリントサーバです。AI 分野の新手法はここで先に出ます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

物理・数学・情報科学などの論文を、査読（専門家によるチェック）の前に無料で公開するサーバです。研究者は成果をすぐ共有でき、読者は掲載を待たずに内容を確認できます。

## どこで出会うか

Transformer 論文（J-13）や GPT・DeepSeek 系の技術報告など、話題の論文の出所として名前を見かけます。Hugging Face Papers や Papers With Code 経由で個別論文に辿り着くことも多いです。

## メイン図

### 図の狙い

arXiv が研究者・AI サービス・実務者をどうつなぐかを 1 枚で示します。

### 登場シーン

- シーン1: 研究者が新モデルの論文を arXiv に投稿し、翌日には世界中で読まれる
- シーン2: エンジニアが「DeepSeek-R1」を検索し、論文 PDF を Claude に貼り付けて要約依頼
- シーン3: 非エンジニアが Hugging Face Papers の「今週の注目」リンクから arXiv 論文に到達
- 並べる基準: 読者が arXiv に辿り着くルートの違い

## 会話での使い方例

「arXiv の DeepSeek 論文を Claude に要約させて、再現計画を立てました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI 分野の研究成果を、査読前に無料で届ける一次情報源です。

### 2. うれしさ

新手法の詳細をジャーナル掲載より数か月早く確認できます。

### 3. 注意点

査読前のため、主張が後で覆されることがあります。

### 4. どこで役立つか

手法の仕組みを原著から確認したいときに役立ちます。

### 5. はじめに

arxiv.org でタイトルを検索し PDF を開く操作だけで使えます。

### 6. 深掘り先

Papers With Code、Hugging Face Papers、Semantic Scholar

## 開発フローでの位置（必須）

1. モデル名を検索 — Twitter や Hugging Face の投稿に arXiv リンクがよく貼られます
2. PDF を開く — abstract（要旨）だけで概要が掴めます
3. AI に要約依頼 — Claude や ChatGPT に貼り「3 行で要約」と頼みます
4. 実装例を探す — Papers With Code で GitHub リポジトリを辿ります
5. 引用を辿る — 関連論文で背景知識を補います

## 関連用語

- Transformer 論文
- Deep Learning
- Reddit
- Papers With Code

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 査読前も混じっていて玉石混交なので、サイト内検索だけで探すのはしんどいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 最先端の論文が無料で置いてある点に魅力を感じます
- 👍 良い点: AI の検索・要約と組み合わせ、引用数で注目論文を追えます
- 👎 ダメな点: 主張に幅がある論文も多く、全部見ようとすると時間が足りません
- 👥 誰向けか: AI 経由で研究動向を素早く追いたい人向けです
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「arXiv」ロゴ文字ラベルを置き、左から研究者が PDF をアップロード、右側に「Claude」「エンジニア」「非エンジニア」が矢印で受け取る構造図
- 登場人物: 研究者（投稿側）1 名 ／ 読み手として非エンジニア会社員 1 名
- 吹き出し・心の声: 研究者「論文を公開しました」／非エンジニア「AI に要約してもらおう」
- 中央に置くキーワード/ラベル: arXiv（プレプリントサーバ）
- Before / After の場合の対比ポイント: 該当なし（structure 図）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（検索）
- Step 2 のアイコン/絵柄: PDF ファイルアイコン
- Step 3 のアイコン/絵柄: AI チャット吹き出し
- Step 4 のアイコン/絵柄: GitHub ロゴ
- Step 5 のアイコン/絵柄: 連鎖する論文リンク
- 矢印で示す流れの意図: 話題を知る → 原著を読む → AI で補助 → 実装を探す → 深掘りする

## コミュニティ補完メモ

- B-40 Reddit との住み分け：Reddit は議論・感想・実験報告の場。arXiv は論文の一次公開場所。「Reddit で話題になった arXiv 論文を読む」という順序が典型的な使い方です。
- J-13 Transformer との住み分け：J-13 は Transformer という技術概念のエントリ。B-41 arXiv は「論文が公開される場所」として Transformer 論文（"Attention Is All You Need"）を例として参照する関係です。

## 出典メモ

- <https://arxiv.org/about> — checked 2026-04-30
- <https://info.arxiv.org/about/history.html> — checked 2026-04-30
- <https://paperswithcode.com> — checked 2026-04-30

## 備考

- 1991 年、Paul Ginsparg（コーネル大学）が物理学プレプリント共有のために立ち上げ。後に数学・コンピュータサイエンス・統計・電気工学などへ拡張。
- cs.CL（自然言語処理）/ cs.AI（人工知能）/ cs.LG（機械学習）の 3 カテゴリが AI 業界では特によく参照されます。
- 査読なし公開のリスク：再現性・主張の確からしさは GitHub での追試や後続論文の引用数でも補完するとよいです。
