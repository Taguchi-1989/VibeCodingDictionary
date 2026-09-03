---
id: J-94
title: 並列化戦略
title_reading: へいれつかせんりゃく
category: term_general
subtype: inference
experience_level: research_only
reader_level: 6
importance: E
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-06-22
related_terms:
  - バッチ推論
  - vLLM
  - MoE ルーティング
  - H100
  - GPU
status: ready
---

# 並列化戦略

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

1 つのモデルの計算を複数 GPU（クラスタ）に割って同時に回すための分割の流儀です。TP・PP・EP・DP の 4 軸を組み合わせ、巨大モデルを「載せる」「速く回す」を両立させます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

並列化戦略（Parallelism Strategy）は、1 つのモデルの推論計算を複数の GPU——多くは同一サーバや GPU クラスタ——にどう割り振るかを決める設計の総称です。ここで先に区別しておきたいのが、1 台の GPU の中で複数リクエストを束ねる **バッチ推論（J-84）** との違いです。バッチ推論は「1 台の中の話」、並列化戦略は「複数 GPU をまたぐ話」で、層が異なります。両者は排他ではなく、各 GPU の中ではバッチ推論が効き、その GPU 群をまたいで並列化戦略が効く、という二段構えで重なります。

動機は 2 つです。1 つは「載らない」問題。GLM-5.2 のような数千億パラメータの MoE（Mixture of Experts、J-89）モデルは、重みだけで数百 GB に達し、H100（J-72）1 枚の VRAM（80GB 級）には到底収まりません。もう 1 つは「速く回したい」。1 枚に収まる場合でも、計算を分担すれば 1 リクエストの応答も同時処理数も伸びます。そこで、何をどの GPU に割るかを決めるのが並列化戦略です。代表的な軸が次の 4 つで、それぞれ「何を分割するか」「通信がいつ・どれだけ走るか」「使いどころ」で性格が分かれます。

- **TP（Tensor Parallelism、テンソル並列）**: 1 つの行列演算（重み行列）を横に切り、複数 GPU で分担して計算し、その都度結果を集約します。層の内部で頻繁に通信が走るため、NVLink のような高速インターコネクトが事実上の前提です。Megatron-LM 由来。
- **PP（Pipeline Parallelism、パイプライン並列）**: モデルの層を前半・中盤・後半…と GPU ごとに分け、ベルトコンベヤ式に順送りします。素朴にやると後段 GPU が前段の完了を待って遊ぶ「気泡（パイプラインバブル）」が出るので、入力を小さく刻んだマイクロバッチを流し込んで隙間を埋めます。GPipe／PipeDream 由来。
- **EP（Expert Parallelism、専門家並列）**: MoE の専門家（J-89 のルーティングで選ばれる FFN 群）を GPU ごとに配置します。各トークンを担当の専門家がいる GPU へ送り、結果を戻す all-to-all 通信が肝で、ここが詰まると並列度を上げても伸びません。
- **DP（Data Parallelism、データ並列）**: モデルを丸ごと複製し、別々のリクエスト束を並列に処理してスループットを底上げします。推論では単独でなく、上の 3 つと組み合わせて使うのが普通です。

実際の大規模サービングは **TP × PP × EP ×（DP）を組み合わせ**ます。vLLM（J-83）や SGLang の `tensor_parallel_size` や `pipeline_parallel_size`、`expert_parallel_size` といった設定がまさにこれで、トポロジ（どの軸を何枚に割るか）を決める作業が運用の肝になります。ここに一本貫く原則は単純です——**分割するほど並列度は上がるが、その代わり GPU 間通信がボトルネックになる**。だから「速いリンクで結ばれた GPU 同士を通信の多い軸（TP・EP）に、遅いリンクをまたぐ箇所を通信の少ない軸（PP・DP）に」割り当てる、という配置がセオリーになります。

なお、学習時に出てくる ZeRO／FSDP は名前が似ていますが目的が違います。あちらは主に**学習**のオプティマイザ状態や勾配を分散して**メモリを削る**仕組みで、本エントリが扱う**推論**の計算分散とは狙いが別です。混同しないよう、ここでは推論側の並列化に話を絞ります。

## どこで出会うか

著者がこの言葉に出会うのは、クラウド API を呼ぶ側ではなく、巨大 OSS モデルを「自前のクラスタで動かす側」に回ったときです。「このモデル、80GB の H100 1 枚に載らない。何枚に、どう割れば動くのか」——この問いに答えるのが並列化戦略です。具体的には vLLM や SGLang、TensorRT-LLM の起動引数で `tensor_parallel_size 8`（8 枚で TP）のような値を決め、ベンチマークを取りながらトポロジを詰めていく場面で必ず触れます。

また、技術ブログや論文を読むときの語彙としても頻出します。「671B のモデルをノード内 TP、ノードまたぎ PP で配置」「MoE は EP で専門家を分散し all-to-all がボトルネック」といった記述は、この 4 軸の組み合わせを述べているにすぎません。クラウドの LLM API を使うだけの読者には見えませんが、その裏側では必ずこの並列化戦略が組まれており、巨大モデルがそもそも応答できること自体を支えています。GPU の枚数・接続トポロジ（NVLink／InfiniBand）と並列化の割り当てがかみ合って初めて、想定どおりの速度が出ます。

## メイン図

### 図の狙い

1 枚に載らない巨大モデルを、4 つの軸（TP は行列を横割り／PP は層を縦割り／EP は専門家を配置／DP は丸ごと複製）でどう GPU クラスタに割り付けるかを 1 枚で俯瞰し、「分割するほど並列度は上がるが GPU 間通信がボトルネックになる」というトレードオフ——速いリンクは通信の多い軸、遅いリンクは通信の少ない軸へ——を一目で掴んでもらう。

## 会話での使い方例

「巨大 MoE は 1 枚に載らないので、TP×PP×EP で割って all-to-all 通信が詰まらないトポロジに寄せますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

1 つのモデルの推論計算を複数 GPU に分割し、巨大モデルを「載せる」「速く回す」を両立させる設計です。

### 2. うれしさ

1 枚に載らないモデルが動き、計算分担で応答も同時処理数も伸ばせます。

### 3. 注意点

分割するほど GPU 間通信がボトルネックになり、並列度を上げても頭打ちになりえます。

### 4. どこで役立つか

巨大 OSS モデルを自前クラスタでサービングし、トポロジを詰める場面で活きます。

### 5. はじめに

TP（行列横割り）・PP（層縦割り）・EP（専門家配置）・DP（丸ごと複製）の 4 軸の違いを掴むのが起点です。

### 6. 深掘り先

all-to-all 通信, パイプラインバブル, NVLink/InfiniBand トポロジ, 学習側の ZeRO/FSDP との違い

## 開発フローでの位置（必須）

1. 載るか試算 — モデルの重み量と GPU の VRAM を突き合わせ、何枚必要かと分割の要否を見積もる
2. 軸を選ぶ — TP・PP・EP・DP のどれをどれだけ使うか、モデル構造（MoE か否か）に合わせて決める
3. トポロジ配置 — 通信の多い軸（TP・EP）を NVLink で、またぐ軸（PP・DP）を低速リンク側に割り当てる
4. 起動設定 — vLLM/SGLang の `tensor_parallel_size` 等に落とし込み、クラスタへデプロイする
5. 計測と調整 — スループット・レイテンシ・通信待ちを計測し、all-to-all やバブルのボトルネックを潰す

## 関連用語

- バッチ推論
- vLLM
- MoE ルーティング
- H100
- GPU

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- TP/PP/EP/DP の4つが最初は全然区別できなかった。「何を割るか」（お客/計算そのもの/層/専門家）に対応させる例え（レジ増設・4人で分担・組立ライン・専門医配置）を通したら一気に分かった。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 「エージェントの並列」を語るとき、人によってパイプライン視点とエキスパート視点のどちらを指しているかがズレていると気づいた。自分はパイプラインで見ていたが、エキスパート視点の人もいて、どちらも正解だが抽象度（階層）が違う話をしていただけだった。
- 👍 良い点: パイプラインが上位の骨組みで、その中にエキスパートやテンソル分担が入れ子になっている、という階層構造が分かると腹落ちする。
- 👎 ダメな点: 言葉（並列・エージェント）だけで話すと、どの階層の話か定義がずれたまま議論が噛み合わなくなる。
- 👥 誰向けか: 大規模モデルの推論基盤を設計する人、複数GPUで分散処理を組む人向け。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「1 枚に載らない巨大モデル」のブロック（数百 GB のラベル付き）を置き、そこから 4 本の矢印が 4 つの分割パターンへ枝分かれする俯瞰図。① TP＝1 枚の大きな重み行列を縦の点線で複数 GPU に横割りし「層内で都度集約（通信多）」の双方向矢印。② PP＝モデルの層スタックを前半 / 中盤 / 後半の帯に区切り、各帯を別 GPU に乗せてベルトコンベヤ状に順送り、後段に「待ち＝気泡（バブル）」のグレー帯と、それを埋めるマイクロバッチの小ブロック列。③ EP＝MoE の専門家（FFN）アイコンを GPU ごとに配置し、トークンが担当 GPU へ飛ぶ all-to-all の交差した矢印束（ここが詰まりやすい、と赤で注記）。④ DP＝同じモデル箱を丸ごと 2〜3 個複製し、別々のリクエスト束が並列に入る。下辺に「速いリンク（NVLink）＝通信の多い軸 TP/EP」「遅いリンク（InfiniBand）＝通信の少ない軸 PP/DP」の対応バーを敷き、配置原則を色で結ぶ。
- 登場人物（いれば）: クラスタを運用するインフラエンジニア 1 名（著者の分身）。GPU ラックの前で配置図を見ながら、4 軸の組み合わせ表（TP8×PP2×EP… のような）を指でなぞっている。
- 吹き出し・心の声: 「1 枚に載らないなら割るしかない。でも割るほど GPU 同士のおしゃべりが増える——速いリンクは通信の多い軸へ、遅いリンクはまたぐ軸へ。そこの噛み合わせが速度を決めるのか」
- 中央に置くキーワード/ラベル: 「TP＝行列を横割り」「PP＝層を縦割り」「EP＝専門家を配置」「DP＝丸ごと複製」「分割↑＝並列度↑だが通信↑（トレードオフ）」
- 補足: バッチ推論（J-84）との層の違いを示すため、各 GPU の箱の中に小さく「束ねたリクエスト＝バッチ（1 台内）」を添え、それを「またぐ＝並列化戦略（複数台）」と外枠で囲んで二段構えを表す。

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（① モデルを 4 軸へ枝分かれさせる分配器、② NVLink/InfiniBand のリンク束、を差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: モデルの重み量メーターと GPU の VRAM 容器を天秤にかける（載る / 載らない判定）
- Step 2 のアイコン/絵柄: TP・PP・EP・DP の 4 枚カードから組み合わせを選ぶ手
- Step 3 のアイコン/絵柄: GPU ラックの配線図。NVLink を太線、InfiniBand を細線で描き、軸を割り当てる
- Step 4 のアイコン/絵柄: `vllm serve --tensor-parallel-size 8` のターミナル＋クラスタへのデプロイ矢印
- Step 5 のアイコン/絵柄: スループット / レイテンシ / 通信待ちの計測ダッシュボードと、all-to-all・バブルを潰すレンチ
- 矢印で示す流れの意図: 試算 → 軸選定 → トポロジ配置 → 起動設定 → 計測調整、という「巨大モデルをクラスタに載せて速度を出すまで」の縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: 並列化戦略（TP・PP・EP・DP の 4 軸）
- visual_subject: 1 枚に載らない巨大モデルが 4 軸で GPU クラスタに割り付けられる俯瞰図——分割するほど通信がボトルネックになるトレードオフ
- supporting_subjects: TP（行列を横割り）・PP（層を縦割り）・EP（専門家を配置）・DP（丸ごと複製）の 4 ブロック、NVLink（太線）・InfiniBand（細線）の配線、著者の分身エンジニアが GPU ラック前で配置図を指でなぞる
- logo_subject: none
- excluded_subjects: カラフルなグラフ、実在ブランドUI・ロゴ（NVIDIA等）、赤い警告アイコン、絵文字

### scene brief（日本語）
中央に「1 枚に載らない巨大モデル（数百 GB）」のブロックを置き、そこから 4 本の矢印が 4 つの分割パターンへ枝分かれする俯瞰図。① TP：大きな重み行列を縦の点線で複数 GPU に横割りし、双方向の通信矢印を「通信多」と示す。② PP：層スタックを前半・中盤・後半の帯に区切り、ベルトコンベヤ状に順送り、後段に「気泡（バブル）」のグレー帯と、それを埋めるマイクロバッチの小ブロック列。③ EP：専門家（FFN）アイコンを GPU ごとに配置し、トークンが担当 GPU へ飛ぶ all-to-all の交差矢印束（「ここが詰まりやすい」と注記）。④ DP：同じモデル箱を 2〜3 個複製し、別々のリクエスト束が並列に入る。下辺に「NVLink（太線）＝通信の多い軸 TP/EP」「InfiniBand（細線）＝通信の少ない軸 PP/DP」の対応バー。著者の分身エンジニア 1 名が GPU ラックの前に立ち、配置図を指でなぞりながら吹き出しで「割るほど速くなる、でも通信が詰まる——速いリンクは通信の多い軸へ」と語る。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background; a single infrastructure-engineer character (author's stand-in) standing in front of a GPU rack diagram and tracing a placement chart with one finger, thought bubble reading "split = faster, but more talk between GPUs"; center: a large "huge model (hundreds GB)" block with four arrows branching to four panels — TP panel: a weight matrix sliced vertically across multiple GPU boxes with two-headed communication arrows labeled "frequent sync"; PP panel: model layer stack divided into front/middle/back bands on separate GPUs in conveyor style, a gray "bubble" gap with small micro-batch blocks filling it; EP panel: expert-FFN icons placed on separate GPUs with crossing all-to-all arrows annotated "bottleneck here"; DP panel: two identical model copies receiving separate request batches in parallel; bottom bar: thick line labeled "NVLink = TP/EP (high communication)", thin line labeled "InfiniBand = PP/DP (low communication)"; key labels "TP row-split", "PP layer-split", "EP expert-place", "DP full-copy"; flat, clean, consistent series style; 2:1 horizontal composition. Color rule: strictly #FFFFFF background, #1A1A1A lines, grays, and the five approved blues only — no yellow, green, red, purple, orange, rainbow colors, colorful UI, or emoji.

## コミュニティ補完メモ

- 同じ Lv6 シェルフの近接語との住み分け:
  - バッチ推論（J-84）: 「1 台の GPU 内で複数リクエストを束ねる」概念。本エントリは「複数 GPU をまたいで 1 モデルの計算を割る」概念で層が異なる。各 GPU の中ではバッチ推論、その GPU 群をまたいで並列化戦略、という二段構えで重なる関係を本文・図で崩さない。
  - vLLM（J-83）: 並列化戦略を `tensor_parallel_size` 等の設定で実装する代表的なサービングエンジン。概念は本エントリ、それを動かす道具が J-83。
  - MoE ルーティング（J-89）: EP（専門家並列）が分散する対象＝専門家の選び方そのもの。ルーティングの仕組みは J-89、その専門家を GPU に配ってトークンを all-to-all で送る分散側が本エントリ。
  - H100（J-72）/ GPU（J-77）: 並列化が割り付ける先のハード。1 枚の VRAM 上限が「割る必要」を生み、NVLink 等の接続トポロジが「どう割るか」を縛る。ハードの素性は J-72/J-77、それを束ねて使う戦略が本エントリ。
- スコープ境界: 本エントリは「なぜ割るか・4 軸は何を割るか・組み合わせとトレードオフ」までを担う。Megatron-LM の行列分割の数式、all-to-all の集団通信アルゴリズム、学習側 ZeRO/FSDP の段階分けは各深掘りに譲る（ZeRO/FSDP は推論ではなく学習のメモリ削減なので、本エントリでは「目的が違う」と区別する程度に留める）。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism" arXiv:1909.08053 https://arxiv.org/abs/1909.08053 — checked 2026-06-22（テンソル並列（TP）の一次出典。Transformer の行列演算を GPU 間で分割する手法）
- Huang et al., "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism" arXiv:1811.06965 https://arxiv.org/abs/1811.06965 — checked 2026-06-22（パイプライン並列（PP）の一次出典。層分割とマイクロバッチによるバブル削減）
- vLLM 公式ドキュメント Distributed Inference and Serving https://docs.vllm.ai/en/latest/serving/distributed_serving.html — checked 2026-06-22（`tensor_parallel_size`・`pipeline_parallel_size` 等で TP×PP を組み合わせるサービング設定の確認）
- SGLang ドキュメント（分散・並列の設定） https://docs.sglang.ai/ — checked 2026-06-22（MoE の expert parallelism を含む並列化設定の確認）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- 用語の整理: TP/EP は「層内・トークン単位で頻繁に通信する＝高速リンク（NVLink）前提」、PP/DP は「またぐ箇所が少ない＝低速リンク（InfiniBand）でも耐える」という性格の差が配置原則の核。「分割↑＝並列度↑だが通信↑」というトレードオフを軸に据えること。
- 区別の要点: ①バッチ推論（J-84）＝1 台内、本エントリ＝複数台またぎ。②ZeRO/FSDP＝学習のメモリ削減、本エントリ＝推論の計算分散。この 2 つの混同を本文・図で防ぐ。
- 設定名（`tensor_parallel_size` 等）や対応軸はエンジンのバージョンで変わるため時変情報として扱う。
