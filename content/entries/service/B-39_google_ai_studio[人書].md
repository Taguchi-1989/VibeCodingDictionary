---
id: B-39
title: Google AI Studio
title_reading: グーグルエーアイスタジオ
category: service
subtype: ai_assistant
experience_level: hands_on
reader_level: 2-3
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
  - API
  - API キー
  - Vertex AI
status: needs_review
---

# Google AI Studio

## tagline

Gemini をブラウザで無料で試せる、Google の開発者向け入口です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Google アカウントさえあれば無料で Gemini を試せるブラウザ画面です。プロンプトを打ち込んで応答を確認したり、画像や音声を使った入力を試したりできます。専門知識がなくても操作できる作りです。

## どこで出会うか

自分のアプリや外部ツールに Gemini を組み込みたいとき、最初に開く画面として名前が挙がります。この画面から API キーを発行でき、非エンジニアが「まず触ってみる」入口としても使われます。

## メイン図

### 図の狙い

Google AI Studio の画面を 1 枚に見立て、プロンプト入力欄・応答表示・API キー発行ボタンという 3 つの要素がひと続きになっている様子を掴んでもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Google AI Studio の画面（左にプロンプト入力、右に応答、下に API キー発行ボタン）
- 周辺の要素（3〜6個）: プロンプト入力欄、応答表示、画像・音声の添付、API キー発行ボタン、無料枠の表示
- 関係の描き方（矢印・包含・比較）: 入力欄から応答表示へ試す矢印、画面下部から API キー発行ボタンへ分かれる持ち出す矢印

## 会話での使い方例

「まず Google AI Studio で試してから、API キーを取りましょう。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Gemini を無料で試せる Google 公式の実験場です。

### 2. うれしさ

クレジットカード登録なしで今すぐ触れます。

### 3. 注意点

本格的な商用利用では Vertex AI への移行を検討します。

### 4. どこで役立つか

自分のアプリに Gemini を組み込む最初の一歩に向きます。

### 5. はじめに

プロンプトを打って応答を見るところから始めます。

### 6. 深掘り先

API キー、Vertex AI、Gemini。

## 開発フローでの位置（必須）

1. アカウント準備 — Google アカウントでログインします
2. API キー発行 — 発行ボタンから取得します
3. プロンプト試作 — 入力と応答を繰り返し確認します
4. コードに接続 — 取得したキーを自分のアプリに設定します

## 関連用語

- Gemini
- API
- API キー
- Vertex AI

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 登録やお金まわりの手続きが必要なところです。使い始める前に登録が要るので、そこが最初の壁になります。

<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: なんでもできる環境だな、というのが第一印象でした。
- 👍 良い点: なんでもできて、しかも無料で試せるところです。2024 年ごろであれば、とてもいい環境だったと思います。
- 👎 ダメな点: いまは、同じことをやるなら Claude Code や Codex を使ったほうがいいと思います。無料で使える部分はありますが、継続的に使える枠ではなく、新しい機能を少しずつ試せる場という位置づけです。実装で本当にできることのほうがどんどん進んでいるので、組織の役割としてここに置いてある感があり、Google は時間の面で遅れている印象です。いまは微妙だと感じています。
- 👥 誰向けか: 
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: ノート PC 画面いっぱいに Google AI Studio の編集画面（左にプロンプト入力欄、右に応答表示、画面下に「Get API key」ボタン）
- 登場人物: 非エンジニアの企画職の人物 1 人（PC の前で身を乗り出している）
- 吹き出し・心の声: 「無料でここまで触れるんですね。このキーをコピーして自分のツールに貼ろう」
- 中央に置くキーワード/ラベル: Google AI Studio ＝ 試して、キーを持ち出す場所

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ログインアイコン（アカウント準備）
- Step 2 のアイコン/絵柄: 鍵アイコン（API キー発行）
- Step 3 のアイコン/絵柄: チャット吹き出し（プロンプト試作）
- Step 4 のアイコン/絵柄: プラグ接続アイコン（コードに接続）

## コミュニティ補完メモ

- F-214 API キーとの住み分け：本エントリは「どこでキーを発行するか」という入口の役割に絞り、キーの安全な扱い方・漏えい対応・ローテーションなどキーの管理そのものは F-214 に譲ります。
- B-27 Vertex AI との住み分け：個人が無料で試す Google AI Studio と、企業向け・本番運用の Vertex AI は別サービスです。本エントリでは Vertex AI への移行が選択肢としてある、という 1 点だけ触れます。
- B-1 Gemini との住み分け：Gemini というブランド全体の説明は B-1 に譲り、本エントリは「開発者向けの試用画面」という 1 つの入口に絞ります。

## 出典メモ

- Google AI Studio — <https://aistudio.google.com/> — checked 2026-08-10
- Gemini API ドキュメント「API キーの取得」— <https://ai.google.dev/gemini-api/docs/api-key> — checked 2026-08-10

## 備考

- モデル・料金・提供状況は時変情報です。evaluation_date を必ず確認します。
- 個人向け Google AI Studio と企業向け Vertex AI の違いは B-27 Vertex AI を参照してください。
