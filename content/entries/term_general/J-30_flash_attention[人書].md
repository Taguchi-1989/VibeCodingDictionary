---
id: J-30
title: Flash Attention
title_reading: フラッシュアテンション
category: term_general
subtype: inference
experience_level: research_only
reader_level: 6
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-06-22
related_terms:
  - Attention
  - KV Cache
  - Transformer
  - H100
  - VRAM
status: needs_review
---

# Flash Attention

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Attention の計算を「メモリ階層を意識して（IO-aware）」組み直し、n×n のスコア行列を一度も全部メモリに書き出さずに、厳密な（近似でない）Attention を高速・省メモリで計算する手法です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Attention（注意機構）の素朴な実装は、長さ n の系列に対して n×n のスコア行列 S = QKᵀ を作り、softmax を取り、それを V に掛けます。問題は S の置き場所です。GPU には演算ユニットに近い高速だが小容量の SRAM（オンチップメモリ、数十 MB）と、大容量だが遅い HBM（VRAM 本体、数十 GB）の二層があり、素朴版は n×n の S を HBM に丸ごと書き出してから読み戻します。系列が長いと、計算そのものより「この巨大な中間行列を HBM と往復させる帯域（IO）」が律速になります。つまり GPU は暇なのにメモリの出し入れで待たされる、メモリ帯域ボトルネックです。

Flash Attention は、この n×n 行列を一度も全部はメモリに書かないのが核心です。Q・K・V をブロックに分割（タイリング）し、ブロックの組を SRAM 上に載せて部分的な Attention を計算し、ブロックをずらしながら結果を積み上げます。softmax は系列全体を見ないと正規化できないように見えますが、online softmax（逐次的に最大値とスケールを更新しながら和を繋ぐ手法）を使うことで、ブロックごとの部分結果を数学的に厳密なまま合成できます。出てくる答えは素朴版と完全に同一で、近似ではありません。効果は、HBM 上の中間メモリが O(n²) → O(n) に落ち、IO 削減で実時間（壁時計時間）が大きく短縮されること。「IO を意識した厳密 Attention」という一言が、この手法のすべてを言い表します。

## どこで出会うか

普段はライブラリや推論基盤の奥に隠れていて、API を叩く側からは見えません。出会うのは「同じ GPU なのにライブラリを更新したら学習・推論が目に見えて速くなった」「長い文脈を入れても以前ほどメモリが爆発しなくなった」といった性能の理由を掘り下げたときです。

具体的には、PyTorch の `scaled_dot_product_attention`（内部で Flash 実装を選択）、`flash-attn` パッケージ、vLLM や TensorRT-LLM の「FlashAttention-2 / FlashAttention-3 をバックエンドに採用」というリリースノート、H100 の Tensor Core や非同期コピー機能を前提にした最適化の記述——このあたりで Flash Attention という言葉に出くわします。長文脈モデルが現実的なメモリで動く背景には、ほぼ必ずこの手法があります。

## メイン図

### 図の狙い

「n×n のスコア行列を HBM に丸ごと書き出してから読み戻す素朴版（IO が律速）」と「行列を作らずブロック単位で SRAM 上に計算し online softmax で繋ぐ Flash 版（HBM への中間書き出しゼロ）」を上下に並べ、削っているのは計算量ではなく『メモリの出し入れ（IO）』だ、という肝を面積と矢印の本数で掴んでもらう。

### A. Before / After（律速がどこかのトレードオフ）

- Before（素朴な Attention）
  - 状況: S = QKᵀ の n×n 行列を計算して HBM に書き出し、softmax のために読み戻し、また書き、V と掛けるためにまた読む
  - 視覚要素（概念）: 演算ユニット ⇄ HBM を何往復もする太い矢印。SRAM はほぼ空。中央に巨大な n×n マス目（HBM 上に常駐）
  - つまずき: 系列が長いほど n×n の往復データ量が増え、GPU の演算ユニットは暇なのに帯域待ちで遅くなる。中間メモリ O(n²)
- After（Flash Attention）
  - 状況: Q・K・V をブロックに割り、ブロックの組だけ SRAM に載せて部分 Attention を計算、online softmax でスケールを更新しながら出力に足し込む
  - 視覚要素: SRAM 上で小さなブロックが順に光り、HBM への矢印は入力読み込みと最終出力書き出しの細い 2 本だけ。n×n のマス目は「作られない（点線で消す）」
  - うれしさ: HBM 上の中間メモリ O(n) に激減、IO 往復が減って実時間が短縮。答えは素朴版と完全一致（厳密）

## 会話での使い方例

「Flash Attention は n×n を HBM に書かずタイリングと online softmax で繋ぐ厳密版なので、速さの正体は計算じゃなく IO 削減ですよね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Attention をメモリ階層に最適化して組み直し、n×n 行列を書き出さずに厳密計算する高速化手法です。

### 2. うれしさ

中間メモリが O(n²) → O(n) に落ち、IO 往復が減って実時間が短縮します。答えは近似ではなく厳密です。

### 3. 注意点

削っているのは計算量ではなく『メモリの出し入れ（IO）』であり、ボトルネックが演算側なら効果は薄い点に注意です。

### 4. どこで役立つか

長文脈の学習・推論、Transformer の Attention がメモリ帯域で律速になる場面全般で効きます。

### 5. はじめに

「n×n を作らず、SRAM 上でブロック計算し online softmax で繋ぐ。だから省メモリかつ厳密」が掴めれば十分です。

### 6. 深掘り先

online softmax、タイリング、SRAM と HBM の帯域差、FlashAttention-2 / 3、H100 の非同期コピー

## 開発フローでの位置（必須）

1. 律速の特定 — Attention が「演算待ち」か「メモリ帯域待ち」かを見極める。長系列ほど後者（IO ボトルネック）に寄る
2. タイリング — Q・K・V をブロックに分割し、ブロックの組を SRAM に載せて部分 Attention を計算する。n×n 全体は作らない
3. online softmax で合成 — ブロックごとの部分結果を、最大値とスケールを逐次更新しながら厳密に繋ぐ。HBM への中間書き出しをゼロにする
4. バックエンド選択 — FlashAttention-2（並列化・work 分割の改善）、FlashAttention-3（H100 の非同期コピーと FP8 を活用）など、GPU 世代に合う実装を選ぶ
5. 効果測定 — メモリ消費の低下と壁時計時間の短縮を確認。出力が素朴版と一致する（厳密）ことも合わせて検証する

## 関連用語

- Attention
- KV Cache
- Transformer
- H100
- VRAM


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「書き出さずに次へ渡す」というイメージは何となくある。IO ＝ メモリへの書き込み時間を減らす方向感も掴めている。
- ただ「SRAM の中でタイル計算し続ける」という具体的な絵はまだ曖昧。
- HBM という言葉が馴染みなく、SRAM（高速・揮発）との2段構造は難しく感じた。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 「書き出さないから速い」という名前と効果のイメージは掴めた。
- 👍 良い点: KV Cache（再計算しない）とセットで理解すると2つの効率化の違いが整理できる。
- 👎 ダメな点: SRAM / HBM のメモリ階層が分からないと、なぜ速いかの理由が繋がらない。
- 👥 誰向けか: GPU のメモリ構造を少し知っている人が「なぜ H100 で速いのか」を掘り下げるのに良い。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 上段に「素朴な Attention」、下段に「Flash Attention」の 2 段比較。共通の舞台として GPU の二層メモリ（左に小さな高速 SRAM、右に大きな遅い HBM）を描く。上段は中央に巨大な n×n マス目を HBM 上に置き、演算ユニットと HBM を行き来する太い矢印を 4 往復ぶん（書く→読む→書く→読む）描いて「データの出し入れで詰まる」さまを表す。下段は SRAM 上で小さなブロックが順番に光り（タイリング）、online softmax のスケール更新を曲線矢印で示し、n×n マス目は点線で「作られない」と消す。HBM への矢印は入力読み込みと最終出力の細い 2 本だけ。
- 登場人物（いれば）: GPU の中を覗き込むエンジニア 1 名（著者の分身）。上段では HBM を往復する太い矢印に「ここで待たされる」と顔をしかめ、下段では SRAM 上の光るブロックを指して納得顔。
- 吹き出し・心の声: 「遅いのは計算じゃない。n×n をメモリに出し入れする往復だ。だったら——行列を作らずにブロックで済ませればいい」
- 中央に置くキーワード/ラベル: 「中間メモリ O(n²) → O(n)」「削るのは計算量じゃなく IO」「答えは厳密（近似ではない）」「SRAM 速い小さい / HBM 遅い大きい」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（① メモリ階層の二層、③ 太い往復矢印に「IO」ラベルだけ差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: GPU が「演算待ち」か「帯域待ち」かを見分ける天秤（律速の特定）
- Step 2 のアイコン/絵柄: 大きな行列を格子に切り分けてブロックを取り出す（タイリング）
- Step 3 のアイコン/絵柄: ブロックの部分結果を逐次つなぐ波線＋スケール更新の数式 m, ℓ（online softmax）
- Step 4 のアイコン/絵柄: GPU 世代バッジ（FA-2 / FA-3 / H100）を選ぶスイッチ
- Step 5 のアイコン/絵柄: メモリゲージ↓と時計↓、出力一致チェックマーク（効果測定）
- 矢印で示す流れの意図: 律速を見極める → 行列を作らずブロック計算 → 厳密に合成 → GPU に合う実装を選ぶ → 省メモリと高速を確認、という「なぜ速いか・何を削ったか」の縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: Flash Attention
- visual_subject: SRAM上でブロックが順番に光りながら部分Attentionを計算し、HBMへの往復矢印が細い2本だけになる「IO削減」の対比構造
- supporting_subjects: 素朴版の太い往復矢印×4、n×nマス目（点線で「作られない」と消す）、GPUの二層メモリ（小さな高速SRAM・大きな遅いHBM）
- logo_subject: none
- excluded_subjects: カラフルなグラフ、絵文字、実在サービスのUI、赤・緑・黄の差し色

### scene brief（日本語）
GPUの中を覗き込むエンジニア1名（著者の分身）が上下2段の比較図を見ている場面。共通の舞台として左に小さなSRAM・右に大きなHBMを描く。上段（素朴な Attention）：中央に巨大なn×nマス目をHBM上に置き、演算ユニットとHBMを行き来する太い矢印を4往復ぶん描いてボトルネックを表現。エンジニアはここで顔をしかめる。下段（Flash Attention）：SRAM上で小さなブロックが順番に#8DB7E8で光り（タイリング）、n×nマス目は点線で「作られない」と消す。HBMへの矢印は入力と出力の細い2本だけ。エンジニアは下段のブロックを指差し納得顔。吹き出し：「遅いのは計算じゃない。n×nをメモリに出し入れする往復だ。だったら——行列を作らずにブロックで済ませればいい」。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, flat light gray fills, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background. A single engineer character (author avatar, male, standing) shown twice: upper half frowning at thick bidirectional arrows, lower half pointing with a satisfied expression at glowing SRAM tiles. GPU memory layout: a small labeled box "SRAM (fast, small)" on the left and a large labeled box "HBM (slow, large)" on the right, drawn in both halves. Upper half (labeled "Naive Attention"): a large n×n grid sitting inside HBM, with four thick double-headed arrows between compute unit and HBM; label "O(n²) memory". Lower half (labeled "Flash Attention"): SRAM box contains small tiles highlighted in #8DB7E8 cycling in sequence; n×n grid shown as dashed outline labeled "never materialized"; only two thin arrows to/from HBM for input read and output write; label "O(n) memory". No colorful charts, no brand logos, no yellow/green/red/purple, no emoji. The contrast between four thick arrows and two thin arrows is the visual core. Flat, clean, consistent series style; minimal text, only key labels. 2:1 horizontal composition.

## コミュニティ補完メモ

- 同じ Lv6 シェルフの近接語との住み分け:
  - KV Cache（J-29）: 「再計算を省く」最適化。過去トークンの K・V を保存して作り直さない。Flash Attention は「中間行列 n×n の書き出しを省く」最適化。削っている対象が違う（再計算 vs IO）。直交するので併用される——Flash 実装は KV キャッシュ上の K・V を入力に取って動く。
  - Attention（J-17）: Flash Attention が最適化している演算そのものの定義（Q/K/V と softmax）。Flash は数学的に同一の答えを返すので、Attention の理解が前提になる。
  - Transformer（J-13）: Attention を積み重ねた本体。長文脈化の現実性は Flash Attention の省メモリに支えられている。
  - H100（J-72）/ VRAM（J-70）: Flash の効果を決めるハードウェア側。VRAM(HBM) の帯域が律速を生み、H100 の非同期コピー・Tensor Core を FlashAttention-3 が活用する。
- スコープ境界: 本エントリは「Flash Attention とは何か・なぜ速いか（IO 削減）・KV Cache と何が違うか」までを担う。online softmax の数式展開や FA-2/3 のカーネル実装詳細は深掘り先に譲る。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" (2022) https://arxiv.org/abs/2205.14135 — checked 2026-06-22（タイリング＋online softmax で n×n を書き出さず厳密 Attention を実現する一次出典。IO-aware の定義と O(n) メモリの主張）
- Dao, "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning" (2023) https://arxiv.org/abs/2307.08691 — checked 2026-06-22（並列化と work 分割の改善で FA-1 を高速化した続報）
- Shah et al., "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision" (2024) https://arxiv.org/abs/2407.08608 — checked 2026-06-22（H100 の非同期コピーと FP8 低精度を活用した最新世代）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- 「KV Cache との違い」を最重要の腹落ちポイントとして本文・見どころ・補完メモの 3 箇所で押さえた: KV Cache は「再計算（過去トークンの K・V）を省く」、Flash Attention は「中間行列（n×n スコア）の書き出しを省く」。削減対象が異なり、直交・併用される。
- 「近似ではなく厳密」は誤解の生まれやすい点なので tagline・何をしてくれるか・見どころ 2/5 で繰り返し明記した。計算順序を変えただけで数学的に同一の出力を返す。
- メモリ階層の容量はおおよその目安（SRAM 数十 MB / HBM 数十 GB）。世代で変動するため数値は概数として扱う。
