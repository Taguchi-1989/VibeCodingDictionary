---
id: C-11
title: Z.ai
title_reading: ズィー エーアイ
category: person_org
subtype: company
experience_level: research_only
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2019-01-01
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - GLM
  - Moonshot AI
  - Hugging Face
  - Anthropic
status: ready
---

# Z.ai

## tagline

旧称 Zhipu AI（智譜 AI）。清華大学発の中国 AI 企業です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

GLM（大規模言語モデルの一系列）を開発・提供する中国の AI 企業です。テキスト・コード・画像に対応したモデルをそろえ、API とオープンウェイト（重みを公開した形式）で利用できます。

## どこで出会うか

Hugging Face で GLM モデルを検索するとヒットします。中国系 LLM 記事では「六小虎」の一角として登場します。2025 年 1 月に米国制裁リスト（Entity List）へ追加されており、規制報道にも出ます。

## メイン図

### 図の狙い

Z.ai（旧 Zhipu AI）が提供するモデルファミリーの構成と、各モデルがどの用途に対応するかを整理して示します。

### B. 登場シーン（figure_type: structure）

- シーン1: 研究者が Hugging Face で GLM-4 の重みをダウンロードしてローカルで推論する
- シーン2: 開発者が CodeGeeX API をコーディング補完用途で組み込む
- シーン3: AI 業界ニュースで「中国 LLM 六小虎の一角」として企業名が挙がる
- 並べる基準: 用途（チャット／コーディング／画像／音声／エージェント）別


## 会話での使い方例

「Z.ai の GLM-4.6、ローカルで動かすと意外と速いです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

清華大学発、GLM 系 LLM を開発する中国の AI 企業です。

### 2. うれしさ

オープンウェイト公開が多く、ローカル実行で試せます。

### 3. 注意点

米国の制裁リスト入りにより、米国企業との直接取引が制限されます。

### 4. どこで役立つか

中国語対応や多言語 LLM の選択肢を比較する場面で参照します。

### 5. はじめに

旧社名 Zhipu AI と Z.ai が同一企業を指すと把握するだけで十分です。

### 6. 深掘り先

GLM、CodeGeeX、AutoGLM

## 開発フローでの位置（必須）

1. モデル選定 — GLM-4 系をローカルまたは API で利用するか検討する
2. 重み取得 — Hugging Face から GLM のオープンウェイトをダウンロードする
3. 環境構築 — ローカル推論環境（vLLM など）を用意してモデルを読み込む
4. 実行・評価 — チャット・コーディング・画像などタスク別に出力を確認する


## 関連用語

- GLM
- Moonshot AI
- Hugging Face
- Anthropic


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 旧称 Zhipu AI と現名 Z.ai が混在し、同一企業と気付きづらいです
- GLM / CodeGeeX 等が D-45 と交差し、どちらで読むかの線引きが難しいです
- 制裁リスト入りで取引制限がある点がニュースを断片的に追うだけでは掴みにくいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: GLM の開発企業として名前をちらっと見た記憶があります。
- 👍 良い点: 安価でオープンという点が魅力だと感じます。
- 👎 ダメな点: 中国系特有の情報漏洩への不安が拭えません。
- 👥 誰向けか: フロンティアモデルからコストを削減したい人向けではないでしょうか。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Z.ai」ロゴ、周囲に 5 つのモデル（ChatGLM・CodeGeeX・GLM-4V・GLM-4-Voice・AutoGLM）を放射状に配置する構成図
- 登場人物: 開発者キャラクターが Hugging Face のページを見ながら「どれを選ぼう」と考えている様子
- 吹き出し・心の声: 「ローカルで動くの？」「API と両方ある！」
- 中央に置くキーワード/ラベル: Z.ai（旧 Zhipu AI）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（モデル選定）
- Step 2 のアイコン/絵柄: ダウンロード矢印（重み取得）
- Step 3 のアイコン/絵柄: サーバー（環境構築）
- Step 4 のアイコン/絵柄: チェックリスト（実行・評価）
- 矢印で示す流れの意図: 選定 → 取得 → 構築 → 評価の一方向フロー


## コミュニティ補完メモ

- C-10 Moonshot AI との住み分け: C-10 はキャラクター AI やチャットサービスが主軸。C-11 Z.ai は LLM 研究開発・オープンウェイト公開が軸で、コーディング（CodeGeeX）やエージェント（AutoGLM）用途のモデルファミリーが特徴
- D-45 GLM との住み分け: D-45 は GLM モデルシリーズ自体（アーキテクチャ・バージョン展開）を扱うエントリ。C-11 は GLM を提供する企業としての Z.ai に焦点を当てる
- 「六小虎」の他メンバー（Moonshot / MiniMax / Baichuan / 01.AI / StepFun）については各エントリ側で言及し、C-11 では Z.ai 固有の情報に絞る

## 出典メモ

- Z.ai 公式サイト <https://z.ai/> — checked 2026-04-30
- Zhipu AI GitHub <https://github.com/THUDM> — checked 2026-04-30
- 米国財務省 Entity List 追加報道（2025 年 1 月）— checked 2026-04-30
- Hugging Face GLM モデルページ <https://huggingface.co/THUDM> — checked 2026-04-30


## 備考

- 社名リブランド: 2025 年に「Zhipu AI（智譜 AI）」から「Z.ai」に改称。ニュース・論文では Zhipu 表記が残り、製品サイトでは Z.ai 表記が主流。読者混乱を避けるため tagline に「旧称 Zhipu AI」を明記した
- 制裁リストの影響: 米国財務省の制裁（2025 年 1 月追加）により、米国企業が Z.ai と直接取引する際に制限が生じる。オープンウェイトの利用自体が直ちに禁止されるわけではないが、商用契約・投資は影響を受ける可能性がある（出版前に最新規制状況を要確認）
- バージョン展開: GLM-4 → GLM-4.5 → GLM-4.6 と进化中。評価日時点の最新は GLM-4.6（2026-04-30 評価）
