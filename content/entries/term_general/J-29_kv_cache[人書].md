---
id: J-29
title: KV Cache
title_reading: ケーブイキャッシュ
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
  - Attention
  - Transformer
  - Flash Attention
  - MLA
  - vLLM
status: needs_review
---

# KV Cache

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Key（鍵）と Value（値）の略。自己回帰生成で過去トークンの K・V を保存し、毎ステップの再計算を省くことで、長い生成を実用速度に乗せる推論の心臓部です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Transformer（トランスフォーマー）が文章を 1 トークンずつ生成するとき、各層の Attention（注意機構）は「いま見ている全トークンの Key と Value」を必要とします。素直に実装すると、新しいトークンを 1 個出すたびに過去すべてのトークンの K・V を再計算するので、n トークン目の生成に O(n) の計算がかかり、全体では O(n²) に膨らみます。

KV Cache は、一度計算した過去トークンの K・V を GPU メモリに置いておき、次のステップでは「新しく増えた 1 トークンぶんの K・V だけ」を計算して継ぎ足す仕組みです。これにより各生成ステップは O(n) に、しかも実体は「行列を 1 行追記して 1 回の Attention を回すだけ」に落ち、長文生成が現実的な速度になります。Q（Query）はステップごとに新しく作り直しますが、K と V は過去ぶんを使い回せる——ここが「K と V だけをキャッシュする」名前の由来です。

## どこで出会うか

普段はライブラリの内側に隠れていて、API を叩く側からは見えません。出会うのは「長い文脈を入れたら急に GPU メモリが足りなくなった」「同時リクエスト数（バッチサイズ）を上げたら OOM（Out Of Memory）した」といった運用のボトルネックを掘り下げたときです。

具体的には、vLLM や TensorRT-LLM のログ、`max_model_len` や `gpu_memory_utilization` といった設定項目、「PagedAttention で KV キャッシュの断片化を解消した」というリリースノート、MQA/GQA/MLA が「KV キャッシュを削るための工夫」として紹介される技術記事——このあたりで KV Cache という言葉に出くわします。推論コストの議論はほぼ必ずここに帰着します。

## メイン図

### 図の狙い

「過去トークンの K・V を毎回作り直す素朴版（O(n²)）」と「キャッシュに 1 行ずつ追記する KV Cache 版（各ステップ O(n)）」を上下に並べ、なぜ計算量が落ちるか・代わりにメモリを食うか、という交換条件（トレードオフ）を一目で掴んでもらう。

### A. Before / After（計算とメモリのトレードオフ）

- Before（KV Cache なし）
  - 状況: トークンを 1 個生成するたびに、過去全トークンの K・V をゼロから再計算
  - 視覚要素（概念）: ステップが進むほど三角形に膨らむ再計算ブロック。総計算量 O(n²)
  - つまずき: 系列が長くなると生成が二乗で重くなり、長文生成が非現実的になる
- After（KV Cache あり）
  - 状況: 過去の K・V はメモリに保持、新トークンぶんの K・V だけ計算して追記
  - 視覚要素: 縦に伸びていく KV テーブルに 1 行ずつ append、Attention は最新 Q × 全 K
  - うれしさ: 各ステップ O(n)、生成全体が線形オーダーに。代償として KV テーブルのぶんだけ GPU メモリを常時占有する

## 会話での使い方例

「長文脈で OOM するのは KV Cache がトークン数ぶん線形に膨らむからで、GQA や PagedAttention で削るのが定石ですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

自己回帰生成で過去トークンの K・V を保存し、毎ステップの Attention 再計算を省く推論最適化です。

### 2. うれしさ

各生成ステップの計算量を O(n²) 相当から O(n) に落とし、長文生成を実用速度に乗せます。

### 3. 注意点

速度の代償に GPU メモリを食い、消費量は「系列長 × 層数 × ヘッド数 × 2(K と V) × 精度」に比例して伸びます。

### 4. どこで役立つか

長文脈チャット・大規模バッチ推論・スループット最適化など、メモリと速度のせめぎ合う場面で効きます。

### 5. はじめに

「K と V だけ使い回し、Q は毎回新規。だから二乗が線形に落ち、代わりにメモリを常時占有する」が掴めれば十分です。

### 6. 深掘り先

PagedAttention（vLLM）、MQA/GQA、MLA、量子化、Flash Attention

## 開発フローでの位置（必須）

1. プロンプト投入 — 入力（プロンプト）全体を 1 回まとめて通す prefill。ここで初期の K・V を一括計算してキャッシュへ格納する
2. 逐次生成（decode） — 1 トークン出すごとに、新トークンの K・V をキャッシュに追記し、最新 Q × 全 K で次トークンを予測する
3. メモリ管理 — 系列が伸びるほど KV テーブルが線形に肥大。PagedAttention で固定長ブロックに分割し断片化を抑える
4. 構造的削減 — MQA/GQA で K・V ヘッドを共有、MLA で K・V を低次元に圧縮、量子化で 1 要素あたりのビット数を削り、キャッシュ容量そのものを縮める
5. スループット調整 — 削れたメモリぶんバッチサイズを上げ、同時リクエスト数とレイテンシ（応答遅延）のバランスを取る

## 関連用語

- Attention
- Transformer
- Flash Attention
- MLA
- vLLM

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- K・V という言葉がカチッとハマるまでは入ってこなかった。何度か聞くうちに腹落ちした。
- キャッシュ＝使い回す、という感覚は掴めると一気に繋がる。
- 文脈が長くなると重たくなる体感（CLAUDE.md・エージェント）はあるが、「キャッシュがメモリを食うから速くなる」という方向感はまだ曖昧。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 論文解説を読んで K/V という言葉がハマった瞬間に「これか」となった。
- 👍 良い点: プロンプトキャッシュ（長文脈を使い回す）という実用と直結して理解できた。
- 👎 ダメな点: メモリ消費と速度向上のトレードオフの方向感がまだ曖昧に残っている。
- 👥 誰向けか: LLM のコスト・速度を気にし始めた人が「なぜ長い会話は重いのか」を理解するのに良い。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 上段に「KV Cache なし」、下段に「KV Cache あり」の 2 段比較。上段はステップ t=1,2,3… が進むたび、過去全トークンを覆う再計算ブロックが三角形に肥大していく様子（総和が O(n²) であることを面積で示す）。下段は縦に並んだ KV テーブルに、ステップごとに新しい 1 行（K_t, V_t）だけが青で追記され、最新の Q_t が全 K と内積を取る矢印を 1 本だけ描く。
- 登場人物（いれば）: 推論基盤を覗き込むエンジニア 1 名（著者の分身）。下段の追記される 1 行を指差している。
- 吹き出し・心の声: 「過去の K・V は作り直さない。増えた 1 行だけ足せばいい——だからメモリは食うが速い」
- 中央に置くキーワード/ラベル: 「O(n²) → 各ステップ O(n)」「Q は毎回新規 / K・V は使い回し」
- Before / After の場合の対比ポイント: 計算量（再計算量）の三角形 vs メモリ（KV テーブル）の縦長。速度とメモリのトレードオフを面積と高さで対比。

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① キャッシュ箱、③ メモリゲージが満タンに近づく演出だけ差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: プロンプト全文を一括で炉に通す prefill のバッチ矢印
- Step 2 のアイコン/絵柄: 1 行ずつ積み上がる KV テーブル＋ループ矢印（decode）
- Step 3 のアイコン/絵柄: ページ分割されたメモリブロック（PagedAttention）
- Step 4 のアイコン/絵柄: 圧縮・共有を示す 4 ヘッド→1 ヘッドの集約（GQA/MLA）と量子化のビット削減
- Step 5 のアイコン/絵柄: バッチを並べてスループット↑・レイテンシのバランスを取る天秤
- 矢印で示す流れの意図: prefill → decode ループ → メモリが膨らむ → 削る工夫 → スループット最適化、という「ボトルネックがどこで生まれ、どう削られるか」の縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: KV Cache
- visual_subject: KVテーブルに新しい1行（K_t, V_t）だけを青で追記し、最新QがKと内積を取る「1行足すだけ」の追記構造
- supporting_subjects: KV Cacheなし版の再計算三角形（O(n²)の面積）との対比、縦に伸びるKVテーブル
- logo_subject: none
- excluded_subjects: カラフルなグラフ、絵文字、実在サービスのUI、赤・緑・黄の差し色

### scene brief（日本語）
推論基盤を覗き込むエンジニア1名（著者の分身）が、縦に伸びるKVテーブルに追記される1行を指差している場面。画面を上下2段に割り、上段は「KV Cacheなし」でステップが進むほど再計算ブロックが三角形に肥大する様子（O(n²)を面積で示す）をグレーで描く。下段は「KV Cacheあり」で縦長のKVテーブルに1行ずつ新しい行が#D6E6FAで追記され、最新のQ_tから全Kへ1本の矢印だけが伸びる。エンジニアが下段の追記行を指差し、吹き出し：「過去の K・V は作り直さない。増えた1行だけ足せばいい——だからメモリは食うが速い」。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, flat light gray fills, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background. A single engineer character (author avatar, male, standing) pointing to a KV table row being appended, with a speech bubble: "Just add one row — no recompute." Upper half of diagram (labeled "Without KV Cache"): a growing triangle of gray recalculation blocks stacking up as time steps increase, annotated "O(n²)". Lower half (labeled "With KV Cache"): a tall narrow KV table with rows stacking vertically; the newest row highlighted in #D6E6FA, a single arrow from "Q_t" pointing across to the full K column. No colorful charts, no brand logos, no yellow/green/red/purple, no emoji. The contrast between the expanding triangle and the simple append arrow is the visual core. Flat, clean, consistent series style; minimal text, only key labels. 2:1 horizontal composition.

## コミュニティ補完メモ

- 同じ Lv6 シェルフの近接語との住み分け:
  - Flash Attention（J-30）: Attention の計算そのものを I/O 効率良く再構成する話。KV Cache が「何を保存するか」なら、Flash Attention は「保存した K・V とどう速く計算するか」。直交する最適化で併用される。
  - MLA（J-28）: KV Cache を低ランクの潜在ベクトルに圧縮してメモリを削る具体手法。本エントリの「構造的削減」ステップの一つを深掘りする位置。
  - vLLM（J-83）: KV Cache を OS のページングのように固定長ブロックで管理する PagedAttention の実装基盤。本エントリの「メモリ管理」ステップの実体。
  - バッチ推論（J-84）/ スループットとレイテンシ（J-85）: KV Cache のメモリ節約がそのままバッチサイズ＝同時処理数の上限を決める、という下流の話。
  - 投機的デコード（J-82）: ドラフトモデルで複数トークンを先読みし decode 回数を減らす別軸の高速化。KV Cache とは独立だが併用される。
- スコープ境界: 本エントリは「KV Cache とは何か・なぜ効くか・どこがボトルネックか」までを担う。個別の削減手法（MLA, PagedAttention）の数理は各エントリに譲る。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Vaswani et al., "Attention Is All You Need" (2017) https://arxiv.org/abs/1706.03762 — checked 2026-06-22（Attention の Q/K/V の定義と Transformer のデコーダ構造の一次出典）
- Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (vLLM, 2023) https://arxiv.org/abs/2309.06180 — checked 2026-06-22（KV キャッシュの断片化問題と PagedAttention による解決）
- Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need" (MQA, 2019) https://arxiv.org/abs/1911.02150 — checked 2026-06-22（KV ヘッド共有によるキャッシュ削減の起点。GQA/MLA の前段）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- 計算量について: 「各ステップ O(n)・全体 O(n²)」はキャッシュありでも変わらない（n トークン生成すれば Σ O(t) = O(n²)）。本エントリで言う改善は「キャッシュなしの O(n²) per step 相当の再計算（全体 O(n³)）」ではなく、「per step を O(n²)→O(n) に落とし、無駄な再計算をゼロにする」点。誌面では混乱を避け「毎ステップの再計算を省く＝各ステップ O(n)」に表現を寄せた。
