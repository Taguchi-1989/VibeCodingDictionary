---
id: B-34
title: NotebookLM
title_reading: ノートブックエルエム
category: service
subtype: ai_assistant
experience_level: hands_on
reader_level: 1-2
importance: B
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-08-10
related_terms:
  - Gemini
  - RAG
  - Context
  - Google AI Studio
status: ready
---

# NotebookLM

<!--
バイブコーディング図鑑 スケルトン雛形 v1（2026-04-28 追加）
- 構造だけ先に置いた状態。本文は status を `drafting` に上げた段階で entry-writer が埋める
- validator は status: skeleton を archived/sample と同様にスキップする
- tagline には entry_candidates.md の「一言」を仮で流し込んでいる（本書きで磨き直す）

YAML 補足（本書きで埋める／見直す欄）:
- subtype: candidate.csv の subtype 列を流し込み済み（後で見直す）
- experience_level: hands_on / partial / research_only
- reader_level: 1〜6
- figure_type: before_after / structure / comparison / workflow / timeline（仮で structure を入れている）
- version_status: active / preview / deprecated（時変なら埋める）
- pricing_note: none / paid / freemium（時変なら埋める）
- related_terms: 3〜5 個目安
- status: skeleton → drafting → needs_review → ready
-->

## tagline

アップロードした資料だけを根拠に答える、Google のノートツールです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

PDF や Google ドキュメント、Web ページ、YouTube 動画などをソースとして登録すると、その範囲だけを根拠に要約や質問応答をしてくれます。回答には引用元が示されるので、出どころを確認しながら使えます。

## どこで出会うか

配布資料や論文、議事録を大量に読み込んで要点をつかみたい調査・学習の場面で使われます。音声概要が SNS で話題になり、耳から資料を確認する使い方も広がっています。

## メイン図

### 図の狙い

資料を登録すると、その範囲だけを根拠にした回答が返ってくる「閉じた情報源」の仕組みを掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: NotebookLM（登録した資料の集合＝ノートブック）
- 周辺の要素（3〜6個）: PDF・Google ドキュメント・Web ページ・YouTube 動画（入力側）／要約・質問応答・引用元・音声概要（出力側）
- 関係の描き方（矢印・包含・比較）: 資料が中心に集まり、そこから回答や音声が外へ出ていく一方向の矢印

## 会話での使い方例

「NotebookLM は資料を全部読ませてから要約させると安心感が違います。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

PDF や動画などの資料を読み込ませ、その範囲だけで回答するノート AI です。

### 2. うれしさ

回答に引用元が示され、出どころを確認しながら使えます。

### 3. 注意点

登録した資料以外の一般知識には、基本的に答えません。

### 4. どこで役立つか

論文や議事録の要点整理、資料の下読みに向いています。

### 5. はじめに

資料をアップロードして質問してみる、この 1 サイクルです。

### 6. 深掘り先

RAG、Gemini、Google AI Studio

## 開発フローでの位置（必須）

1. ソース登録 — PDF・Web ページ・動画などを資料として登録します。
2. 要約・質問 — 登録済みの資料だけを根拠に要約や質問に答えてもらいます。
3. 引用確認 — 回答に付いた引用元をたどって、出どころを確かめます。
4. 音声化 — Audio Overview で資料を会話形式の音声に変換します。

## 関連用語

- Gemini
- RAG
- Context
- Google AI Studio

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 非エンジニアとしてつまずくところは特にありませんでした。設定なしで勝手に使えます。

<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 話題になっていたので触りました。YouTube などを根拠として引っ張ってこられるのがいいなと感じました。
- 👍 良い点: Google 系のサービスがオールインワンで使えるところです。YouTube などを根拠に指定して、それをもとに回答させる簡易的な RAG が作れますし、そこからインフォグラフィックや音声生成、簡単な動画生成、プレゼン資料の作成までつながります。ひとつのパッケージになっているのが非常にいいと思います。
- 👎 ダメな点: Google の統制が取れていないな、とすごく感じます。NotebookLM のチームとメインの Gemini のチームの統合がとても遅かったからです。出て話題になってから年単位かかっていて、そこに内部の政治を感じてしまいます。
- 👥 誰向けか: 簡易的に共有したい人にはいいと思います。ただ、いいところはあるけれど、ずっと使い続けるかというとそうでもない、というのが正直なところです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: PDF・Web ページ・動画のアイコンが漏斗状に中央の「NotebookLM ノート」へ集まり、そこから回答の吹き出しと音声波形が外へ出ていく構造図
- 登場人物（いれば）: 資料を読み込ませて安心した表情で結果を眺めているリサーチャー風の人物
- 吹き出し・心の声: 「渡した資料の範囲でしか答えないから安心できる」
- 中央に置くキーワード/ラベル: NotebookLM／ソースに忠実な回答

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: PDF・Web ページ・動画アイコンの束
- Step 2 のアイコン/絵柄: ノートと虫眼鏡
- Step 3 のアイコン/絵柄: 引用マークの付いた吹き出し
- Step 4 のアイコン/絵柄: ヘッドフォンと音声波形

## コミュニティ補完メモ

- Gemini（B-1）との住み分け：Gemini は一般知識も使う汎用の会話 AI。NotebookLM は登録した資料の範囲だけに回答を限定する専用ツール
- RAG（G-15）との住み分け：RAG は「手元の資料を検索して回答に使う」仕組み一般の説明。NotebookLM はその仕組みを使った具体的な製品の 1 つ
- Google AI Studio（B-39）との住み分け：Google AI Studio は開発者がモデルを試す検証ツール。NotebookLM は資料整理をしたい一般利用者向けの完成品サービス

## 出典メモ

- NotebookLM 公式サイト (https://notebooklm.google.com/) — checked 2026-08-10
- Google NotebookLM ヘルプ (https://support.google.com/notebooklm) — checked 2026-08-10

## 備考

無料版と有料版でノートブック数・ソース数・1 日の質問回数の上限が異なります（具体的な数値は変わりやすいため本文では省略）。まとめ記事に出る改称に関する話は公式で確認できないため、本エントリでは扱っていません。
