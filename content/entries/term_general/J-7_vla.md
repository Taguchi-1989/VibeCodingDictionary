---
id: J-7
title: VLA
title_reading: ビジョンランゲージアクション
category: term_general
subtype: ai_concept
experience_level: research_only
reader_level: 4-5
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-09-05
related_terms:
  - VLM
  - 世界モデル
  - フィジカル AI
  - LLM
status: drafting
---

# VLA

## tagline

Vision-Language-Action の略。視覚・言語・行動を 1 モデルでつなぎ、ロボットを動かす枠組みです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

VLM（視覚と言語を扱うモデル）に「行動」を足した仕組みです。カメラ映像と指示文を受け取り、関節の動きなど実際のロボット操作を出力します。

## どこで出会うか

フィジカル AI やヒューマノイドロボットの記事で、RT-2 や GR00T N1 といったモデル名とセットで登場します。J-15 VLM の発展形として紹介される場面が多いです。

## メイン図

### 図の狙い

視覚・言語の理解に「行動の生成」が加わることで、チャットで終わらず現実の動作に到達する流れを示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: VLA（Vision-Language-Action）
- 周辺の要素: カメラ映像 / 指示文（言語）/ VLM 部 / 行動トークン・Diffusion Transformer / モーター動作
- 関係の描き方: 矢印（視覚+言語 → VLM で理解 → 行動生成部 → ロボットの動き）


## 会話での使い方例

「VLA モデルなら、VLM の理解をそのままロボットの動作に変換できますね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

視覚・言語の理解を行動の出力にまでつなげます。

### 2. うれしさ

指示文だけでロボットに具体的な動作を任せられます。

### 3. 注意点

どのモデルが優れているかの比較は誌面では扱いません。

### 4. どこで役立つか

ヒューマノイドや産業用ロボットの操作生成に使われます。

### 5. はじめに

「VLM に行動出力を足したもの」で入門として十分です。

### 6. 深掘り先

VLM、フィジカル AI、世界モデル

## 開発フローでの位置（必須）

1. 視覚入力 — カメラや LiDAR で周囲の状況を捉える
2. 言語指示 — 「これを掴んで」などの自然言語を受け取る
3. VLM で理解 — 画像と指示をトークン化しモデルに渡す
4. 行動生成 — Diffusion Transformer 等が関節の動きを出力する
5. ロボット実行 — 出力に従いハードウェアが実際に動く


## 関連用語

- VLM
- 世界モデル
- フィジカル AI
- LLM


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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: カメラ映像と吹き出し指示文が VLM ブロックに入り、行動生成部を経てロボットアームが動く一連の流れ
- 登場人物: ロボットアームの前に立つ研究者（男性）が「これを棚に置いて」と話しかけている
- 吹き出し・心の声: ロボット「映像と言葉を読んで、次はこの角度で腕を動かします。」
- 中央に置くキーワード/ラベル: VLA
- Before / After の場合の対比ポイント: なし（構造図）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: カメラ・LiDAR アイコン
- Step 2 のアイコン/絵柄: 吹き出し（自然言語指示）
- Step 3 のアイコン/絵柄: VLM ブロック（画像＋指示のトークン化）
- Step 4 のアイコン/絵柄: Diffusion Transformer の格子模様
- Step 5 のアイコン/絵柄: ロボットアームが動くイラスト
- 矢印で示す流れの意図: 「見て・読んで・動く」の一直線の流れを示す


## コミュニティ補完メモ

- J-15 VLM との住み分け：VLM は「視覚＋言語」の理解まで。VLA はそこに「行動」の出力を足した発展形として書き分ける。
- J-6 フィジカル AI との住み分け：フィジカル AI はセンサー〜ハードウェアまでを含む全体システムの語。VLA はその中で判断を担うモデル単体を指す語として整理する。
- 代表モデル（RT-2 / π0 / GR00T N1）の優劣比較はブリーフの方針どおり書かない。


## 出典メモ

- https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/ — checked 2026-09-05
- https://arxiv.org/pdf/2503.14734 （GR00T N1）— checked 2026-09-05
- https://arxiv.org/pdf/2507.01925 （VLA サーベイ）— checked 2026-09-05


## 備考

- 代表的なモデルとして RT-2（Google DeepMind, 2023）、π0（Physical Intelligence）、GR00T N1（NVIDIA, 2025）がある。GR00T N1 の公開版 GR00T-N1-2B は合計 2.2B パラメータ（うち VLM 部が 1.34B）で、VLM が画像と指示をトークン化し、Diffusion Transformer が motor action を出す二段構え。
- どのモデルが最強かの比較やベンチマーク順位は本エントリでは扱わない。
