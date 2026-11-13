---
id: D-84
title: Doubao 系
title_reading: ドウバオ系
category: model
subtype: other_closed
experience_level: research_only
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date: 2026-02-14
version_status: active
pricing_note: freemium
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - ByteDance
  - Seedance
  - DeepSeek
  - Alibaba
  - Qwen 系
status: needs_review
---

# Doubao 系

## tagline

ByteDance の対話アプリ Doubao の中身にあたるモデル群です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ByteDance の Seed チームが作る、文章やコード向けのモデル群です。2026-02 公開の Doubao-Seed-2.0 は Pro・Lite・Mini の 3 段と Code があります。重みは公開されていません。

## どこで出会うか

対話アプリ Doubao（豆包）と、企業向けクラウド Volcano Engine の API で出会います。中国勢のモデルを比べる話題で、DeepSeek や Qwen と並んで名前が出ます。

## メイン図

### 図の狙い

「アプリの名前は Doubao、作るチームは Seed、貸す窓口は Volcano Engine」という 3 つの名前の関係を整理し、版が見えにくい理由を掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Doubao-Seed（モデル）
- 周辺の要素: アプリ Doubao、開発チーム Seed、API 窓口 Volcano Engine、Pro／Lite／Mini の 3 段
- 関係の描き方: 中央のモデルから、アプリと API の 2 本の出口を描く

## 会話での使い方例

「Doubao は ByteDance の対話アプリで、中身は Seed チームのモデルですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ByteDance 製の、重み非公開のモデル群です。

### 2. うれしさ

Pro・Lite・Mini から用途に合う大きさを選べます。

### 3. 注意点

同じモデル名のまま更新され、版が見えにくいです。

### 4. どこで役立つか

中国勢モデルの動向の把握や比較です。

### 5. はじめに

アプリ名とチーム名の違いから整理します。

### 6. 深掘り先

ByteDance、Seedance、Qwen 系

## 開発フローでの位置（必須）

1. 名前を整理 — Doubao・Seed・Volcano Engine の関係を知る
2. 段を選ぶ — Pro・Lite・Mini から用途に合うものを選ぶ
3. 窓口を確認 — 使えるのは API かアプリかを確かめる
4. 並べて試す — DeepSeek や Qwen と同じ課題で比べる
5. 更新を追う — 同名のまま変わる版を公式で確認する

## 関連用語

- ByteDance
- Seedance
- DeepSeek
- Alibaba
- Qwen 系

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 
- 
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 
- 👍 良い点: 
- 👎 ダメな点: 
- 👥 誰向けか: 
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Seed チーム」の人物が作るモデルの箱。そこからスマホのアプリ（Doubao）と、企業ビルへ向かう API の 2 本の出口が出る
- 登場人物（いれば）: 読者キャラ（非エンジニア）と、Seed チームの開発者キャラ
- 吹き出し・心の声: 読者「名前が 3 つあって混乱する」／開発者「アプリは Doubao、作るのは Seed、貸す窓口は Volcano Engine」
- 中央に置くキーワード/ラベル: Doubao-Seed ／ Pro・Lite・Mini ／ Volcano Engine ／ 2026-02 公開

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 3 つの名札
- Step 2 のアイコン/絵柄: 大中小の 3 つの箱
- Step 3 のアイコン/絵柄: アプリと API の分かれ道
- Step 4 のアイコン/絵柄: 並んだ 2 つの結果と天秤
- Step 5 のアイコン/絵柄: 更新を示す回転矢印


## コミュニティ補完メモ

- C-24 ByteDance との住み分け：会社の沿革・TikTok は C-24 側。本エントリは LLM の Doubao 系に絞る
- D-56 Seedance との住み分け：動画生成は Seedance 側に任せる。同じ Seed チームの別系統
- D-43 Qwen 系・C-16 DeepSeek との関係：中国勢の比較対象として並べるが、重みを公開する両者と違い、Doubao 系は非公開

## 出典メモ

- ByteDance Seed・Volcano Engine の公式ページの検索結果（二次情報を含む）— checked 2026-11-13
- 技術系報道の検索結果（二次情報）— checked 2026-11-13

## 備考

- **一次未確認（検索経由）**：本エントリの事実はすべて検索経由で、公式ページの直接取得はしていません（2026-11-13 時点）。Artificial Analysis（AA）への掲載そのものも未確認で、主要な LLM 開発元として立てています
- Doubao-Seed-2.0 の公開日は 2026-02-14（検索経由）。Seed 2.1（2026-06-23、Pro／Turbo、文脈 256K）が公開されたと報じられています（二次情報）。本文には書かず、ここで保持
- Volcano Engine の API は同じモデル ID のまま週 1 回以上更新されるとされ、版を特定しにくい点に注意
- `pricing_note: freemium` はアプリの無料利用と API の従量課金が併存するという意味づけで、具体的な単価は未確認です
