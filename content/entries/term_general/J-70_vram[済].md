---
id: J-70
title: VRAM
title_reading: ブイラム
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 3-4
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - GPU
  - パラメータ数
  - 量子化
  - H100
status: ready
---

# VRAM

## tagline

Video RAM の略。GPU に直結した高速メモリで、LLM 推論時にモデルパラメータを格納します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

GPU が計算に使うデータを保持するメモリです。LLM 推論ではモデルパラメータ・中間活性・KV キャッシュをここに置きます。容量が不足するとモデルが動きません。

## どこで出会うか

ローカル LLM を試すときに最初にぶつかる制約です。「このモデルは VRAM 何 GB 必要？」という確認から始めることになります。

## メイン図

### 図の狙い

RAM（システムメモリ）と VRAM の役割分担を横並びで示し、LLM 推論が VRAM だけに依存する構造を掴んでもらう。

### B. 登場シーン（figure_type: comparison）

- シーン1: CPU + RAM でプログラム全般を処理、GPU + VRAM でモデル推論を処理
- シーン2: 70B モデル fp16 → 約 140GB 必要、4bit 量子化 → 約 35GB に圧縮
- シーン3: Apple Silicon は CPU/GPU 統合メモリ（Unified Memory）で VRAM 相当を大容量確保
- 並べる基準: VRAM 容量とモデルサイズの対応関係（読者が試せるかどうか）


## 会話での使い方例

「RTX 5090 の 32GB VRAM だと、4bit 量子化の 70B モデルがギリ動く感じです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

GPU が推論に使うパラメータ・KV キャッシュを保持します。

### 2. うれしさ

容量を把握すれば、動かせるモデルの上限を事前に計算できます。

### 3. 注意点

CPU のシステムメモリ（RAM）とは独立した GPU 専用領域です。

### 4. どこで役立つか

ローカル LLM の選定や、API 利用か自前推論かの判断に使います。

### 5. はじめに

「モデルサイズ × 量子化精度 = 必要 VRAM」の目安計算を押さえます。

### 6. 深掘り先

GPU（J-77）、パラメータ数（J-22）、量子化（J-19）

## 開発フローでの位置（必須）

1. モデル選定 — 試したいモデルのパラメータ数と量子化精度を確認します
2. VRAM 試算 — パラメータ数 × 精度バイト数で必要 VRAM を概算します
3. 環境確認 — 手元の GPU や Apple Silicon の搭載 VRAM を調べます
4. 実行判断 — 不足時は量子化（J-19）を下げるか API に切り替えます
5. 推論実行 — llama.cpp 等でロードし VRAM 使用量を確認します


## 関連用語

- GPU（J-77）
- パラメータ数（J-22）
- 量子化（J-19）
- H100（J-72）


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- コンシューマー GPU だとフロンティアモデルが載りきらない理由がここに集約されます。
- Mac 開発者が多いのは RAM と VRAM を共通化してコスパが良いからです。
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: メモリにも色々あるんだな、と知る入口でした
- 👍 良い点: GPU の性能を「動くかどうか」で単純に評価できる指標になる点
- 👎 ダメな点: そもそも動かない、という制約はやはり厳しいです
- 👥 誰向けか: ローカル llm 試す人は必須かな
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左に「CPU + RAM」ボックス、右に「GPU + VRAM」ボックスを並べ、VRAM 内に「パラメータ」「KV キャッシュ」「中間活性」のラベルを積み上げる
- 登場人物: 手元 PC を前にしてローカル LLM を試そうとしている人
- 吹き出し・心の声: 「VRAM 24GB… 70B モデルは fp16 だと無理か。4bit にしよう」
- 中央に置くキーワード/ラベル: VRAM（GPU 専用）
- Before / After の場合の対比ポイント: fp16（140GB 必要・不足）vs 4bit 量子化（35GB・収まる）の 2 列比較も右側に添えるとわかりやすい

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: モデルカードを見ている人
- Step 2 のアイコン/絵柄: 電卓・計算式（サイズ × バイト数）
- Step 3 のアイコン/絵柄: GPU チップと VRAM バー
- Step 4 のアイコン/絵柄: 分岐矢印（量子化を下げる／API に切り替える）
- 矢印で示す流れの意図: VRAM チェックが Go/No-go の判断点になる構造を可視化する


## コミュニティ補完メモ

- H100（J-72）との住み分け：J-72 はデータセンター向け GPU カード全体の解説。VRAM はその中のメモリ容量の概念に絞った説明。数値の例（H100=80GB 等）は備考に置き、J-72 エントリで詳述。
- GPU（J-77）との住み分け：J-77 は GPU ハードウェア全体。VRAM は GPU の一部として存在するメモリ容量の話に特化。
- 量子化（J-19）との住み分け：J-19 は量子化の仕組み・手法の解説。VRAM エントリでは「量子化で必要 VRAM が減る」という関係性だけに触れ、詳細は J-19 に委ねる。

## 出典メモ

- NVIDIA GPU 仕様ページ（RTX 4090/5090/H100/H200/B200）— checked 2026-04-29
- llama.cpp GitHub README（VRAM 要件の目安計算）— checked 2026-04-29
- Apple Silicon Unified Memory 公式説明 — checked 2026-04-29


## 備考

- 容量例は 2026-04 時点。RTX 5090=32GB、H100=80GB、H200=141GB、B200=192GB は時変情報のため evaluation_date を参照。
- Apple Silicon の Unified Memory は CPU と GPU が同一メモリプールを共有する点が独特。他のディスクリート GPU とは構造が異なるため、単純比較に注意。
- 「必要 VRAM の目安」：70B モデル fp16=約 140GB、int8=約 70GB、int4=約 35GB（パラメータ数 × バイト数の概算。KV キャッシュや中間活性は含まない）。
