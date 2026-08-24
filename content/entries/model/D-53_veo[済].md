---
id: D-53
title: Veo
title_reading: ヴェオ
category: model
subtype: video_generation
experience_level: research_only
reader_level: 2-3
importance: D
figure_type: comparison
page_layout: spread_v1
start_date: 2024-05-14
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Sora
  - Flow
  - Google DeepMind
  - Gemini
status: ready
---

# Veo

## tagline

Google DeepMind が開発する動画生成 AI モデルです。テキストや画像を入力するだけで、映像を出力します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

テキスト・画像・既存動画を入力として、リアルな質感とカメラワークを持つ動画を生成します。Veo 3（2025 年）では環境音・対話・効果音まで含む音声付き動画を出力できます。

## どこで出会うか

Gemini アプリ・Google AI Studio・Vertex AI として利用できます。映像制作ツール Flow の基盤モデルでもあり、広告・コンテンツ制作で名前が挙がります。

## メイン図

### 図の狙い

Veo という基盤モデルと、それを使う各クライアント（Flow・Gemini アプリ・Vertex AI）の関係を整理する。

### B. 登場シーン（figure_type: comparison）

- シーン1: クリエイターが Gemini アプリで広告動画のたたきをテキスト入力から生成する
- シーン2: 開発者が Vertex AI の API 経由で Veo を呼び出し、自社サービスに動画生成を組み込む
- シーン3: 映像ディレクターが Flow で Veo を使いながらカメラワークを指定してシーンを作る
- 並べる基準: 利用者の職種・接触インターフェース別


## 会話での使い方例

「Veo 3 で広告動画のたたきを作って、ナレーションは ElevenLabs に差し替えました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

テキスト・画像から動画を生成する Google の基盤モデルです。

### 2. うれしさ

Veo 3 は音声まで同時生成でき、制作工程を短縮できます。

### 3. 注意点

Veo 本体は API で、利用には Flow や Gemini アプリが必要です。

### 4. どこで役立つか

広告・SNS 動画の初稿やプロトタイプ制作に向いています。

### 5. はじめに

Veo はモデル名、Flow と Gemini は利用窓口と覚えると整理しやすいです。

### 6. 深掘り先

Sora、Flow、Google DeepMind


## 開発フローでの位置（必須）

1. 企画 — 作りたい映像のシーンや雰囲気をテキストで言語化する
2. 生成 — Gemini アプリや Flow にプロンプトを入力し Veo で動画を出力する
3. 確認 — カメラワーク・質感・尺を確認し、再生成やパラメータ調整を行う
4. 仕上げ — 音声を ElevenLabs 等に差し替えたり字幕を追加して完成版にする
5. 展開 — SNS・広告・プレゼン資料に組み込み、必要に応じてリテイクを回す


## 関連用語

- Sora
- Flow
- Google DeepMind
- Gemini


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Whisk から動画を生成できましたが、思ったようなシーンの切り替えになりません
- Gemini からやっても思った通りの感じにならず、結局使えませんでした
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: ベンチマークでほぼ 1 位だったので、すごいと思いました
- 👍 良い点: Google のサブスク範囲内で無料で使えたところです
- 👎 ダメな点: 指示追従性が低く、今考えると使いづらいです
- 👥 誰向けか: 昔のモデルを試してみたい人向けかなと思います
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 中央に「Veo」と書いた箱を置き、左から「テキスト」「画像」「既存動画」の矢印が刺さる。右側に「Gemini アプリ」「Flow」「Vertex AI」の 3 つの出口が並ぶ
- 登場人物: クリエイター女性（Gemini アプリ画面を見ている）とエンジニア男性（API コードを打っている）
- 吹き出し・心の声: クリエイター「テキストだけで動画ができた！」/ エンジニア「API で自社サービスに組み込める」
- 中央に置くキーワード/ラベル: Veo（基盤モデル）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: メモ帳・鉛筆（企画）
- Step 2 のアイコン/絵柄: 動画クリップ・再生ボタン（生成）
- Step 3 のアイコン/絵柄: 虫眼鏡・チェックマーク（確認）
- Step 4 のアイコン/絵柄: ハサミ・ミキサー（仕上げ）
- 矢印で示す流れの意図: 企画からリリースまでの一方向の流れ


## コミュニティ補完メモ

- Sora（D-52）との住み分け：Sora は OpenAI の動画生成モデル、Veo は Google DeepMind の動画生成モデル。競合関係にあり、比較記事・比較動画が多い。本エントリは Veo の特徴と利用経路に集中し、比較はコメント欄・参考記事に委ねる
- Flow（D-57）との住み分け：Flow は Veo を使った映像制作向けクライアントツール。Veo がエンジン、Flow がハンドルというイメージ
- Google DeepMind（C-3）との住み分け：C-3 は DeepMind の組織エントリ。Veo の開発元として言及するに留め、詳細は C-3 へ


## 出典メモ

- Google DeepMind Veo 公式ページ — checked 2026-04-30
- Google I/O 2024 Veo 発表記事 — checked 2026-04-30
- Veo 3 発表ブログ（Google DeepMind）— checked 2026-04-30


## 備考

- Veo 1 は 2024 年 5 月 Google I/O で発表。Veo 2 は 2024 年末に最大 4K・最大 2 分の動画生成に対応。Veo 3 は 2025 年にネイティブ音声合成対応
- 一般向け利用は Gemini アプリ（Gemini Advanced 等）、開発者向けは Google AI Studio／Vertex AI
- 競合: OpenAI Sora / Runway Gen / Pika / Kling
- pricing_note: freemium（Gemini の有料プランに含まれる機能として提供）
