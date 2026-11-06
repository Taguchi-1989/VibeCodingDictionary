---
id: G-52
title: Fast mode
title_reading: ファストモード
category: term_llm
subtype: control
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-11-06
last_audited: 2026-11-06
related_terms:
  - effort レベル
  - Prompt Caching
  - Claude Code
  - Claude 5.5 系
status: needs_review
---

# Fast mode

## tagline

同じモデルを、高い単価で速く動かす設定です。頭は良くならず、速くなります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Fast mode（高速モード）は、同じモデルを速さ優先の構成で動かす設定です。Claude Code の Opus では最大 2.5 倍速になり、品質や能力は変わらず、そのぶん単価が上がります。

## どこで出会うか

Claude Code で /fast と入力して切り替えます。オン中はプロンプトの横に ↯ が出ます。速さを追加料金で買う同様の仕組みは、2026 年秋に他社でも並びました。

## メイン図

### 図の狙い

同じモデルが通常レーンと有料の高速レーンを走る対比で、「速くなるが賢くはならず、料金が上がる」ことを掴んでもらう。

### B. 登場シーン（figure_type: comparison）

- シーン1（通常レーン）: 同じ車（モデル）が普通のペースで走る
- シーン2（高速レーン）: 入口の料金所を通って、同じ車が速く走る
- 並べる基準: 車（モデル）は同一で、速さと料金だけが違う

## 会話での使い方例

「素早く試したい場面だけ Fast mode にして、effort は下げずに使います。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

同じモデルを高い単価で速く動かします。

### 2. うれしさ

質を保ったまま、待ち時間が短くなります。

### 3. 注意点

会話の途中でオンにすると高くつきます。

### 4. どこで役立つか

素早い試行錯誤やその場のデバッグです。

### 5. はじめに

使うなら会話の最初から /fast でオンにします。

### 6. 深掘り先

effort レベル、Prompt Caching

## 開発フローでの位置（必須）

1. 会話の最初に決める — 速さが要る作業か見極めます。
2. /fast でオンにする — プロンプト横の ↯ で状態を確認します。
3. 素早く試行錯誤する — その場のデバッグなどに使います。
4. 終わったらオフに戻す — 長い自律作業では費用を抑えます。

## 関連用語

- effort レベル
- Prompt Caching
- Claude Code
- Claude 5.5 系

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 上下 2 本の道路。上は通常レーン、下は高速レーンで入口に料金所。同じ車（モデル）が両方に描かれ、下のほうが速度線つき
- 登場人物: ノート PC に向かう非エンジニアのビジネスパーソン。料金所のメーターを気にしている
- 吹き出し・心の声: 通常レーン「ふつうの速さで十分」、高速レーン「速い。でも料金所を通ったぶん高いな」
- 中央に置くキーワード/ラベル: 「頭は良くならない。速くなるだけ」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 会話の最初のメッセージ欄
- Step 2 のアイコン/絵柄: /fast を打つ手と ↯ マーク
- Step 3 のアイコン/絵柄: 次々に返ってくる応答
- Step 4 のアイコン/絵柄: スイッチをオフに戻す手

## コミュニティ補完メモ

- G-9 effort レベルとの住み分け：effort を下げると考える量が減って速くなるが質が落ちることがある。Fast mode は質を保ったまま速くなるが高い。両者は組み合わせられる。
- G-19 Prompt Caching との関係：会話の途中でオンにすると、それまでの文脈全体を Fast mode の単価でキャッシュなしに読み直すぶん課金される。通常速度とはキャッシュも別。
- D-17 Claude 5.5 系との関係：Opus 5.5 が Fast mode の対象（Sonnet・Haiku では使えない）。

## 出典メモ

- Claude Code 公式「Fast mode」 https://code.claude.com/docs/en/fast-mode — checked 2026-11-06
- OpenAI（Ultrafast mode）・xAI（Grok 4.7 Fast）分は検索経由の二次情報 — checked 2026-11-06

## 備考

- 価格（100 万トークンあたり、2026-11 時点）: Opus 5.5 は $8 / $40（通常の 2 倍）、Opus 5 と Opus 4.8 は $10 / $50（研究プレビュー）。誌面本文には出さずメイン図のラベルのみ。
- Claude Code での提供状況（2026-11-06 時点）: 対象は Opus のみ。Opus 4.8 の Fast mode は 2026-10-30 に非推奨、2026-11-30 に廃止。Amazon Bedrock・Google Cloud・Microsoft Foundry では使えない。
- 課金: サブスクリプション（Pro / Max / Ultra / Team / Enterprise）ではプランの利用枠ではなく利用クレジットから引かれる。Team / Enterprise はオーナーが有効化するまで使えない。
- 他社の同様の仕組み: OpenAI の GPT-6.1 Sol の Ultrafast mode（2026-10-08、API）、xAI の Grok 4.7 Fast（約 2 倍の価格）。これらは検索経由で一次未確認。
- 向かない用途: 長い自律タスク・バッチ処理・費用重視の作業。
