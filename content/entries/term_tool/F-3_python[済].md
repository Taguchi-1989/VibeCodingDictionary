---
id: F-3
title: Python
title_reading: パイソン
category: term_tool
subtype: language
experience_level: partial
reader_level: 2-3
importance: B
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note:
evaluation_date: 2026-04-29
related_terms:
  - JavaScript
  - NumPy
  - pip
  - Jupyter
  - PyTorch
status: ready
---

# Python

## tagline

英語に近い書き味を持つプログラミング言語で、AI／ML 分野の事実上の標準です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

データ分析・機械学習・自動化を短いコードで書けるプログラミング言語で、豊富なライブラリがそのまま使えます。

## どこで出会うか

AI にコードを頼むと「Python で書きます」と出力される場面が多く、バイブコーディングで最初に触れる言語になることがあります。

## メイン図

### 図の狙い

Python を中心に据え、データ分析・機械学習・自動化という 3 つの用途と、その外側に広がるライブラリ群の位置を概念図で見せます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Python（言語本体）
- 周辺の要素: データ分析（NumPy / pandas）／ 機械学習（PyTorch / scikit-learn）／ 自動化スクリプト（標準ライブラリ）／ パッケージ管理（pip）／ 対話環境（Jupyter）
- 関係の描き方: 中心から 3 本の矢印（用途別）、各矢印の先にライブラリ名ラベルを添える

## 会話での使い方例

「pip でインストールして Jupyter で確かめると、NumPy も pandas もすぐ試せます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

データ処理・機械学習・自動化の 3 領域をカバーする汎用言語です。

### 2. うれしさ

文法がシンプルで AI が書いたコードを人が読んで理解しやすいです。

### 3. 注意点

JavaScript など Web 系の言語とは別物で用途と環境が異なります。

### 4. どこで役立つか

AI の出力コードを読む・動かす場面やデータ整形の自動化に役立ちます。

### 5. はじめに

変数・ループ・関数の 3 つと pip によるライブラリ追加の手順が出発点です。

### 6. 深掘り先

NumPy、pandas、PyTorch、pip、Jupyter。

## 開発フローでの位置（必須）

1. 環境構築 — Python をインストールし、pip で必要なライブラリを追加する
2. コード生成 — AI に「Python で書いて」と依頼し、スクリプトを受け取る
3. 実行・確認 — Jupyter（ジュピター）やターミナルで動作を確かめる
4. 修正・再依頼 — エラーや出力を AI に貼り、改善を繰り返す

## 関連用語

- JavaScript
- NumPy
- pip
- Jupyter
- PyTorch


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 読むことはできても、書こうとするとエラーが出やすい印象があります。
- 形式や領域によって使い方が違い、「Python」でもレベル感がバラバラです。
- TS で書くか Python で書くかを迷う場面が結構あります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 機械学習で使われる言語というイメージでした。
- 👍 良い点: LLM との相性が良く、Excel 代替にも使えます。
- 👎 ダメな点: Excel に比べ視覚的でなく操作への慣れが必要。
- 👥 誰向けか: LLM でデータ分析・科技計算をする人は全員触っておきたい。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Python」ロゴ風の円、外側に 3 方向の矢印と用途ラベル（データ分析・機械学習・自動化）、各矢印の先にライブラリ名の小ラベル
- 登場人物: 非エンジニアの人物 1 人が画面を見ている。画面に「Python で書いて」と入力している
- 吹き出し・心の声: 「AI が Python で書いてくれた。pip で入れて動かしてみよう」
- 中央に置くキーワード/ラベル: Python
- Before / After の場合の対比ポイント: （概念図のため不要）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ダウンロード矢印（環境構築）
- Step 2 のアイコン/絵柄: チャット吹き出し（AI にコード依頼）
- Step 3 のアイコン/絵柄: 再生ボタン（実行・確認）
- Step 4 のアイコン/絵柄: 回転矢印（修正・再依頼のループ）
- 矢印で示す流れの意図: 環境整備 → AI 活用 → 実行確認 → 改善ループ の 4 ステップ


## コミュニティ補完メモ

NumPy（数値計算）・pandas（表データ操作）・PyTorch（機械学習フレームワーク）は別エントリに譲ります。本エントリは Python 言語本体のスコープ（特徴・用途・エコシステムの全体像）に絞ります。pip（パッケージ管理）や Jupyter（対話環境）はそれぞれ別エントリ候補として深掘りします。JavaScript（F-1）との住み分け：Web フロントエンドは JavaScript、データ・AI 処理は Python が主戦場です。

## 出典メモ

- https://www.python.org — checked 2026-04-29

## 備考

Python のバージョン（3.x 系が現行主流、2.x 系は 2020 年にサポート終了）は時変情報ですが、本エントリでは言語の特性・用途に絞るため version_status: active とし、バージョン差分には踏み込みません。AI/ML での主流性も現時点の状況であり、将来変化する可能性があります。
