---
id: D-44
title: Kimi
title_reading: キミ
category: model
subtype: open
experience_level: research_only
reader_level: 3
importance: D
figure_type: timeline
page_layout: spread_v1
start_date: 2023
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
last_audited: 2026-11-06
related_terms:
  - Moonshot AI
  - オープンウェイト
  - DeepSeek
  - Qwen
  - 長文 Context
status: ready
---

# Kimi

## tagline

中国 Moonshot AI が開発するモデル。超長文 Context（コンテキスト）と中国語対応が特徴です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Moonshot AI が開発するテキスト生成モデル群で、K2 はオープンウェイト（modified MIT）で公開されています。200 万 tokens 級の長文 Context 処理に強みがあります。

## どこで出会うか

中国 AI 動向記事やオープンモデルの比較表で名前が出ます。DeepSeek や Qwen と並んで「中国系モデル」として言及されます。

## メイン図

### 図の狙い

K1 から K2 への世代推移と、各世代の特色をタイムラインで示し、「中国発モデルがどう進化してきたか」を 1 枚で把握してもらいます。

### A. 時系列タイムライン（figure_type: timeline）

- K1（2023 年末〜）: Moonshot AI の初代モデル。長文 Context 処理を前面に打ち出す
- K1.5（2025 年初頭〜）: 推論能力を強化。思考連鎖（Chain-of-Thought）系の改良版
- K2（2025 年〜）: MoE（Mixture of Experts）構造で大規模化。modified MIT でオープンウェイト公開

## 会話での使い方例

「Kimi K2 はオープンウェイトなので、DeepSeek と同じ感覚で試せますよ。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

中国 Moonshot AI が開発する長文 Context 特化のモデル群です。

### 2. うれしさ

K2 がオープンウェイト公開のため、手元で動かして検証できます。

### 3. 注意点

中国企業製のためデータ規制や利用規約の確認が必要です。

### 4. どこで役立つか

長文の要約や翻訳タスクで 200 万 tokens 級の恩恵が出ます。

### 5. はじめに

K1→K2 の世代推移とオープン公開の有無が要点です。

### 6. 深掘り先

DeepSeek、Qwen、Moonshot AI

## 開発フローでの位置（必須）

1. モデルを選ぶ — K2 など用途に合う世代とサイズを確認する
2. ウェイトを取得 — Hugging Face の MoonshotAI リポジトリからダウンロード
3. ローカルで実行 — Ollama 等の対応ランタイムで起動して動作確認
4. API で試す — kimi.com の API エンドポイントを使うクラウド利用も選べる
5. 評価する — DeepSeek や Qwen と並べてタスク別の性能を比較する

## 関連用語

- Moonshot AI
- オープンウェイト
- DeepSeek
- Qwen
- 長文 Context

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 馴染みのないベンダーという印象があります
- 動かすときに相当なマシンパワーが必要です
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Opus 4.5 級と評判が良いオープンモデル
- 👍 良い点: Claude Code でエージェント自作に推奨される印象
- 👎 ダメな点: マシンパワーと情報漏洩でしょうか
- 👥 誰向けか: 自分でエージェントハーネスを組みたい人
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 横軸に時系列で「K1 → K1.5 → K2」を矢印で結ぶ。各世代の下に「長文 Context」「推論強化」「オープンウェイト公開」のラベルを添える
- 登場人物: 画面脇に研究者風の人物。K2 の箇所を指差して「これ手元で動かせます」と吹き出し
- 吹き出し・心の声: 「200 万 tokens って何ができるんだろう？」（読者の疑問を代弁）
- 中央に置くキーワード: Kimi ＝ 超長文 × オープンウェイトの中国系モデル

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: モデルカード（世代選択）
- Step 2 のアイコン/絵柄: ダウンロード矢印（Hugging Face）
- Step 3 のアイコン/絵柄: PC + 歯車（ローカル起動）
- Step 4 のアイコン/絵柄: クラウドアイコン（API 利用）
- Step 5 のアイコン/絵柄: スケール天秤（他モデルとの比較）
- 矢印で示す流れの意図: 選択 → 取得 → 起動 → 試用 → 評価 の一方通行


## コミュニティ補完メモ

- DeepSeek（D-46/D-47）との住み分け：DeepSeek は推論特化・R1 系が著名。Kimi は「超長文 Context」が独自色。同じ「中国系オープンモデル」として比較表に並ぶが、得意領域が異なる
- Qwen（D-43）との住み分け：Qwen は Alibaba Cloud 製で多言語・コード対応を前面に出す。Kimi は Moonshot AI 製で長文処理に的を絞る
- GLM（D-45）との住み分け：GLM は Tsinghua 大学発の系譜。Kimi は商用スタートアップ（Moonshot AI）発。どちらも中国語特化だが開発母体が異なる
- Moonshot AI（C-10）との関係：Kimi は Moonshot AI が提供するモデル・サービスの名称。会社エントリ（C-10 スケルトン）と役割を分けて参照し合う

## 出典メモ

- moonshot.cn — checked 2026-04-29
- kimi.com — checked 2026-04-29
- github.com/MoonshotAI — checked 2026-04-29
- Hugging Face: MoonshotAI/Kimi-K2-Instruct — checked 2026-04-29

## 備考

モデル名・ライセンス条件・公開範囲は時変情報です。K2 の modified MIT ライセンスは evaluation_date 2026-04-29 時点の情報であり、商用利用前に公式リポジトリを再確認します。kimi.com のチャットサービスは中国語が主軸ですが、英語インターフェースも提供されています。「200 万 tokens」はモデルによって上限が異なる可能性があるため、利用時は公式ドキュメントで確認が必要です。

**2026-11-06 鮮度監査（検索経由・一次未確認）**: 後継の **Kimi K3** が出ています。API は 2026-07-16、重みの公開は 2026-07-26〜27（報道で 1 日ずれ）。総パラメータ 2.8 兆、1 トークンあたりに動くのは 1,040 億の MoE で、配布サイズは約 1.5 TB と、個人の環境で動かせる大きさではありません。**ライセンスは K2 の modified MIT から独自の「Kimi K3 License」に変わり**、一定以上の売上がある商用推論や、モデルを API として提供する事業（MaaS）に別契約を求める条件がついたと報じられています。2026 年秋の各種比較記事ではオープンウェイトの上位候補に挙がる一方、Artificial Analysis の総合指標 v5（E-52）では、オープンウェイト勢と全体首位の差が広がったとされます。商用利用の前に Hugging Face（moonshotai/Kimi-K3）の LICENSE を必ず確認してください。
