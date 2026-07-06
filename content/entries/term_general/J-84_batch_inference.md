---
id: J-84
title: バッチ推論
title_reading: バッチすいろん
category: term_general
subtype: inference
experience_level: research_only
reader_level: 6
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-06-22
related_terms:
  - スループットとレイテンシ
  - KV Cache
  - vLLM
  - GPU
  - LLM
status: drafting
---

# バッチ推論

## tagline

複数のリクエストを束ねて GPU に一度に流し、ハードを使い切ってスループットを引き上げる推論のやり方です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

バッチ推論（Batch Inference）は、複数の推論リクエストを 1 つの大きな行列計算にまとめ、GPU に一度に流す手法です。GPU は数千の演算器（コア）を並べて「同じ計算を大量のデータに一斉適用する（SIMD/SIMT）」のが得意なハードです。ここに 1 リクエストだけを流すと、行列のサイズが小さく演算器の大半が遊び、さらに重み（モデルのパラメータ）を VRAM から読み出すコストばかりが目立つメモリ帯域律速の状態になります。

そこで複数リクエストの入力を縦に積んで「行数の多い 1 つの行列 ×（共有する）重み行列」に変形すると、重みを 1 回読むだけで多数のリクエストを処理できます。重み読み出しという固定コストが頭数で割り勘になり、GPU の演算ユニット（テンソルコア）も埋まるため、単位時間あたりに捌けるリクエスト数＝スループットが跳ね上がります。これがバッチ推論の核心です。

ただし無条件で速くなるわけではありません。バッチを組むには「ある程度リクエストが揃うのを待つ」必要があり、待たされたリクエストから見れば応答までの時間＝レイテンシは悪化しえます。バッチサイズを大きくするほどスループットは上がるがレイテンシは伸びる、という **スループット ↔ レイテンシの綱引き**（J-85）が、バッチ推論の設計を貫く基本トレードオフです。

## どこで出会うか

著者がこの言葉に出会うのは、自社で LLM を「動かす側」に回ったとき、つまり API を呼ぶのではなく vLLM（J-83）や TensorRT-LLM のような推論サーバを GPU 上に立てて運用するときです。GPU は 1 枚あたり時間課金で高価なので、「同じ GPU で 1 秒あたり何件捌けるか」が運用コストに直結します。ここで設定する `max_num_seqs`（同時に処理する系列数の上限）や `max_num_batched_tokens` といったパラメータが、まさにバッチの大きさを決めるツマミです。

クラウドの LLM API（ChatGPT や Claude）を使うだけの読者には見えませんが、その API の裏側では必ずこのバッチングが効いており、料金の安さと速さを支えています。OpenAI などが提供する「Batch API」（24 時間以内に返す代わりに半額）も、レイテンシを犠牲にスループットを最大化する、この綱引きを商品化したものです。

## メイン図

### 図の狙い

1 リクエストずつ流すと GPU の演算器が大半遊ぶ様子と、複数リクエストを束ねると同じハードが埋まりスループットが跳ね上がる様子を左右に並べ、「待つ代償にレイテンシが伸びる」綱引きまでを一目で掴んでもらう。

## 会話での使い方例

「GPU 遊ばせず捌くにはバッチ推論が要りますが、待つぶんレイテンシは伸びますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

複数リクエストを束ねて GPU を埋め、スループットを稼ぐ推論手法です。

### 2. うれしさ

重み読み出しを頭数で割り勘でき、GPU 1 枚あたりの処理数とコスト効率が上がります。

### 3. 注意点

バッチが揃うまで待つため、個々のレイテンシは悪化しえます。

### 4. どこで役立つか

LLM を自前の GPU で運用し、スループットとコストを最適化する場面です。

### 5. はじめに

静的バッチングの無駄と Continuous batching の差を掴むと腑に落ちます。

### 6. 深掘り先

Continuous batching, prefill/decode の律速差, KV Cache のメモリ制約

## 開発フローでの位置（必須）

1. リクエスト到着 — 推論サーバのキューに複数リクエストが溜まる
2. バッチ編成 — 揃った系列を 1 つの行列に束ね、prefill（入力一括処理）を実行
3. 逐次デコード — 1 トークンずつ生成。Continuous batching なら終わった枠に次を詰める
4. KV Cache 管理 — 各系列のキャッシュで VRAM を消費し、バッチサイズの上限が決まる
5. 応答返却 — 完了した系列から順に返し、空いた枠へ新規リクエストを流し込む

## 関連用語

- スループットとレイテンシ
- KV Cache
- vLLM
- GPU
- LLM

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- スループットとレイテンシの「綱引き」がピンと来なかった。
- レストランの厨房（即1皿ずつ出す vs まとめて10皿作る）の例えで「あちらを立てればこちらが立たず」が腹落ちした。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 綱引き（スループット↔レイテンシ）が抽象的でピンと来なかったが、厨房の例えで腹落ちした。
- 👍 良い点: チャットは応答速度優先、夜間の大量処理はスループット優先、と使い分けの判断軸として効くのが分かる。
- 👎 ダメな点: 言葉だけだと「あちらを立てればこちらが立たず」の関係が伝わりにくい。具体例が要る。
- 👥 誰向けか: LLM をサービスとして提供する側、コストと応答速度のバランスを設計する人向け。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左右 2 パネルの対比図。左「1 件ずつ流す」＝大きな GPU の格子（演算器）のうち 1 マスだけ点灯、残りはグレーアウトで「遊休」。右「束ねて流す」＝同じ格子がほぼ全マス点灯し、入口で 4〜5 本のリクエスト矢印が 1 本の太い帯にまとまって GPU へ突入。右下に小さく「待ち時間 = レイテンシ↑」の砂時計を添えて綱引きを示唆。
- 登場人物（いれば）: 推論サーバを運用するエンジニア 1 人（GPU ラックの前で計器を見ている）。
- 吹き出し・心の声: 左パネルのエンジニア「1 件ずつだと GPU がスカスカで、もったいない…」／右パネルのエンジニア「束ねたら一気に捌けた。でも待たせた人のレイテンシは伸びるな」
- 中央に置くキーワード/ラベル: 「スループット↑ ↔ レイテンシ↑（綱引き）」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: キューに積まれた封筒（リクエスト）の列
- Step 2 のアイコン/絵柄: 封筒が 1 本の太い帯に束ねられ GPU へ入る
- Step 3 のアイコン/絵柄: トークンが 1 個ずつ出る歯車。空いた枠に次の封筒が滑り込む（Continuous batching）
- Step 4 のアイコン/絵柄: VRAM メーターと KV Cache のブロックが積み上がり上限に迫る

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: バッチ推論
- visual_subject: 1件ずつでは GPU 演算器がスカスカ、複数を束ねるとほぼ全マス点灯する左右対比
- supporting_subjects: 推論サーバを運用するエンジニア、GPU 演算格子のタイル、束ねリクエスト矢印、砂時計（レイテンシ↑の示唆）
- logo_subject: none
- excluded_subjects: カラフルな GPU ダッシュボード・実在UIスクリーンショット・他社ロゴ・緑/赤/黄の警告色

### scene brief（日本語）
左右2パネルの対比図を中心に据える。左パネルは大きな GPU 演算格子のうち1マスだけ青く点灯し、残りはグレーアウトで「遊休」。左端のエンジニアが小さく「1件ずつだと GPU がスカスカで、もったいない…」の吹き出し。右パネルは同じ格子がほぼ全マス点灯し、入口で4本のリクエスト矢印が1本の太い帯にまとまって GPU へ突入。右下の小さな砂時計に「待ち時間 = レイテンシ↑」のラベルを添えて綱引きを示唆。パネル中央に大きく「スループット↑ ↔ レイテンシ↑（綱引き）」のラベル1本のみ。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration, 2:1 horizontal composition (1254x627); monochrome plus blue palette only (#1A1A1A linework, neutral grays #6B7280, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background. Left panel: a large GPU compute grid where only one cell is lit in pale blue and the rest are gray (idle); a single male engineer stands at the left with a thought bubble indicating waste. Right panel: the same grid with nearly all cells lit in pale blue; four request arrows merge into one thick band entering the GPU; a small hourglass at the bottom-right carries the label "latency ↑". One central label banner: "Throughput ↑ ↔ Latency ↑". Flat, clean, consistent series style; minimal text, only the one label and the hourglass tag; no yellow, green, red, purple, orange, rainbow, colorful UI, or brand marks.

## コミュニティ補完メモ

- J-85（スループットとレイテンシ）との住み分け: J-85 は 2 指標そのものの定義・綱引きの一般論を扱う。本エントリは「その綱引きを操作する具体手段＝リクエストを束ねる」に寄せる。
- J-83（vLLM）との住み分け: vLLM は Continuous batching と PagedAttention を実装した代表的な推論サーバ製品。本エントリはバッチングという一般概念を扱い、vLLM はその実装例として参照する。
- J-29（KV Cache）との住み分け: KV Cache はキャッシュの仕組みそのもの。本エントリでは「KV Cache の VRAM 消費がバッチサイズの上限を決める制約」としてのみ触れ、深掘りは J-29 に委ねる。
- 補足（誌面には出さない深掘り）: prefill は入力トークン全体を一括で行列演算するため演算律速（compute-bound）になりやすく、バッチを大きくしても線形には伸びにくい。一方 decode は 1 トークンずつ重みを読み直すためメモリ帯域律速（memory-bound）で、ここをバッチで割り勘するのが効く。だから「prefill と decode を分けてスケジュールする（disaggregated serving / chunked prefill）」という設計が近年の主流になっている。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Orca: A Distributed Serving System for Transformer-Based Generative Models (Yu et al., OSDI 2022) — continuous/iteration-level batching の原典 — checked 2026-06-22
- vLLM ドキュメント（docs.vllm.ai）Optimization and Tuning / continuous batching・max_num_seqs の説明 — checked 2026-06-22
- NVIDIA Technical Blog "Mastering LLM Techniques: Inference Optimization"（in-flight batching, prefill/decode の律速差） — checked 2026-06-22

## 備考

- reader_level: 6（自己学習シェルフ・刊行スコープ外）。docs/level_policy.md §2-6 に基づき、モデル内部・推論基盤の深掘り技術として今季は刷らず原稿として残す。
- 静的バッチング（static batching）= 全リクエストを揃えて開始し全員終わるまで次を入れない方式。生成長がバラバラだと長い 1 件に引きずられて GPU が遊ぶ。これを Continuous/in-flight batching が「終わった枠に即次を詰める」ことで解消した、という歴史的な流れが理解の軸。
