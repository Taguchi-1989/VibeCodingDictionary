---
id: J-21
title: LoRA
title_reading: ローラ
category: term_general
subtype: data_learning
experience_level: partial
reader_level: 4-5
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Fine-tuning
  - QLoRA
  - Stable Diffusion
  - パラメータ数
status: ready
---

# LoRA

## tagline

Low-Rank Adaptation の略。元モデルを凍結し差分行列だけを学習する微調整手法です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Fine-tuning は全パラメータを更新しますが、LoRA は各層に差分行列を足してそこだけ学習します。差分ファイルは数 MB〜数百 MB に収まり、メモリと学習時間を抑えられます。

## どこで出会うか

Stable Diffusion（D-54）の画像生成コミュニティでは「キャラクター LoRA」「画風 LoRA」として流通しています。SaaS が顧客別チューニングを裏で提供する際にも使われます。

## メイン図

### 図の狙い

元モデルを凍結したまま「差分だけ」を取り扱うイメージを対比で示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Full Fine-tuning でモデル全体を再学習中
  - 視覚要素: 大きなモデル全体が更新マークで赤く染まる
  - つまずき: GPU メモリが足りず途中で止まる
- After
  - 状況: LoRA で差分行列だけを学習
  - 視覚要素: 元モデルは灰色（凍結）、薄い青の差分レイヤーだけが点灯
  - うれしさ: 消費メモリが激減し、手元の GPU でも動く

## 会話での使い方例

「社内ロゴを覚えさせる LoRA を Stable Diffusion で作りました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

元モデルを凍結したまま差分行列だけを学習する微調整手法です。

### 2. うれしさ

フル Fine-tuning の数十分の一のメモリで追加学習ができます。

### 3. 注意点

LoRA はファイル形式ではなく学習手法と差分の保存形式です。

### 4. どこで役立つか

画像生成や LLM の用途別チューニングに役立ちます。

### 5. はじめに

「元モデルは変えず差分だけ保存できる」仕組みを押さえると理解が早いです。

### 6. 深掘り先

QLoRA、Fine-tuning（J-16）、パラメータ数（J-22）

## 開発フローでの位置（必須）

1. ベースモデルを選定 — 凍結して学習対象外にするモデルを決めます
2. 学習データを準備 — 追加したいスタイル・ドメインの例を集めます
3. LoRA を学習 — 差分行列だけを GPU で数時間〜数日かけて訓練します
4. 差分ファイルを配布 — 数 MB 単位の LoRA ファイルを用途別に保存します
5. 推論時に重ね合わせ — 元モデルに LoRA を合成して出力を得ます

## 関連用語

- Fine-tuning
- QLoRA
- Stable Diffusion
- パラメータ数

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「LoRA で微調整する」という話を聞いたとき、何となく分かったようで分かっていない感覚でした。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 名前が可愛らしい用語、という印象です。
- 👍 良い点: フル Fine-tuning より少ないリソースで個人 PC でも調整できます。
- 👎 ダメな点: 元モデルが入れ替わると調整がやり直しになりがちです。
- 👥 誰向けか: 画像生成で自分好みに調整したい個人ユーザー向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左側に「全パラメータが赤く更新されるフル Fine-tuning」、右側に「元モデル（灰色・凍結）＋薄青の差分レイヤーだけが光る LoRA」の対比
- 登場人物: エンジニア風の人物が左では困り顔（GPU メモリ不足）、右では笑顔
- 吹き出し・心の声: 左「全部更新して GPU が死にそう…」／右「差分だけで十分でした！」
- 中央に置くキーワード/ラベル: 「ΔW（差分行列）」
- Before / After の対比ポイント: 更新対象のパラメータ数の差

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 冷凍庫マーク（凍結）
- Step 2 のアイコン/絵柄: フォルダ・データ収集
- Step 3 のアイコン/絵柄: GPU・学習中
- Step 4 のアイコン/絵柄: 小さいファイルアイコン（数 MB）
- Step 5 のアイコン/絵柄: レイヤー重ね合わせ
- 矢印で示す流れの意図: ベースモデルを起点に差分が積み重なる流れ

## コミュニティ補完メモ

- Fine-tuning（J-16）との住み分け：J-16 は「全パラメータ更新」の手法全般を扱う。J-21 LoRA は PEFT の代表手法として J-16 の手段の 1 つ。詳細比較は J-16 に委ねる。
- QLoRA（J-22 近辺）との住み分け：QLoRA は LoRA ＋ 4bit 量子化の組み合わせ。量子化については量子化エントリ（J-19 近辺）に委ねる。
- パラメータ数（J-22）との住み分け：J-22 は「なぜパラメータ数が多いと重いか」を解説。LoRA が「全パラメータを触らなくて済む理由」の背景知識として参照先にする。

## 出典メモ

- Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", arXiv 2021 — checked 2026-04-29
- Hugging Face PEFT ドキュメント — checked 2026-04-29

## 備考

- QLoRA（4bit 量子化との組み合わせ）や DoRA・GaLore など派生手法が存在するが、本エントリでは LoRA 本体の概念に絞る。派生は深掘り先として言及するにとどめる。
- Stable Diffusion コミュニティでは「LoRA ファイル」と呼ばれることが多く、ファイル形式と混同されやすい。「学習手法＋差分保存形式」という正確な定義を「注意点」で強調する。
