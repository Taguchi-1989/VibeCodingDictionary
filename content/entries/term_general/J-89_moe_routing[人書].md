---
id: J-89
title: MoE ルーティング
title_reading: モーイールーティング
category: term_general
subtype: ml_basic
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
  - MoE
  - Transformer
  - LLM
  - DeepSeek V3
  - GLM
status: needs_review
---

# MoE ルーティング

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

MoE（Mixture of Experts、混合専門家）で「各トークンをどの専門家に振り分けるか」を決めるルーター（ゲーティングネットワーク）の仕組みです。スコア化・top-k 選択・負荷分散が核で、ここの設計が品質と計算効率を左右します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

MoE（J-18）は、1 つの巨大な FFN（Feed-Forward Network、全結合層）を持つ代わりに、小さな FFN を「専門家（expert）」として多数並べ、各トークンにつき少数だけを選んで使うことで、総パラメータ数を増やしながら 1 トークンあたりの計算量（活性パラメータ）を抑える仕組みです。この「どの専門家を選ぶか」を毎トークン決める役が**ルーター（ゲーティングネットワーク）**です。

ルーターの基本動作は 3 段です。(1) トークンの隠れ表現 h に小さな線形層（ゲート行列 W_g）をかけ、専門家 N 個ぶんのスコア（ロジット）を出す。(2) スコアの高い上位 k 個（top-k、典型的には k=2 や 8）を選ぶ。(3) 選ばれた専門家の出力を、スコアから作ったゲート重みで加重合算して次層へ渡す——という流れです。

スコアの作り方には 2 系統あります。一つは全専門家にまたがる **softmax gating**（N 個のスコアを softmax で正規化してから top-k を取る）。もう一つは DeepSeek-V3 や GLM 系が採る **sigmoid gating** で、各専門家のスコアを sigmoid で**独立に**評価し、「選ぶ尺度」と「重みの正規化」を分離します。専門家数 N が数百に増えると softmax の相互競合が扱いにくくなるため、独立評価しやすい sigmoid 系が大規模 MoE で好まれます。

## どこで出会うか

普段の API 利用では一切見えません。出会うのは、DeepSeek-V3 / R1、GLM-4.5、Mixtral、Qwen-MoE といった MoE モデルの技術レポートや、「総パラメータ 6710 億・活性 370 億」のように**総 vs 活性パラメータ**の差を説明する記事です。この差を作っているのが、毎トークン少数の専門家だけを起動するルーティングだからです。

より深掘りすると、「ある専門家にトークンが集中して残りが死ぬ（routing collapse、ルーティング崩壊）」「補助損失（auxiliary loss）が品質を削る」「DeepSeek-V3 が補助損失なし負荷分散（loss-free balancing）を導入した」といった、ルーター設計そのものを論じる記事・arXiv 論文に出会います。MoE の「速くて賢い」が実は**ルーターの出来**に強く依存している、と気づいたあたりで必ず立ち止まる用語です。

## メイン図

### 図の狙い

1 本のトークンがルーターに入り、全専門家のスコアが出て top-k だけが起動し、加重合算されて出ていく——という「振り分けの 1 サイクル」を縦に描く。あわせて、素朴に学習すると人気専門家にトークンが偏る（routing collapse）こと、それを bias 項で均す loss-free balancing が「損失を汚さず選択だけ調整する」ことを対比で掴んでもらう。

### A. Before / After（負荷分散のあるなし）

- Before（素朴なルーティング）
  - 状況: スコアの高い専門家にトークンが自然に集中し、一部の専門家ばかり使われ、残りが学習されず死ぬ
  - 視覚要素: 8 人の専門家のうち 2 人だけにトークンの矢印が殺到し、6 人が手持ち無沙汰（点線）。GPU 配置図では混んだデバイスが赤く律速
  - つまずき: 容量の偏りで一部 GPU がボトルネック化し、死んだ専門家ぶんのパラメータが無駄になる
- After（loss-free balancing）
  - 状況: 専門家ごとに動的な bias 項をスコアに足し引きし、混みすぎた専門家のスコアを下げ、空いた専門家を選ばれやすくする
  - 視覚要素: 各専門家の上に「+b / −b」の調整つまみ。矢印が 8 人へほぼ均等に分散し、GPU が均等な緑になる
  - うれしさ: 言語モデリング損失そのものには罰則を足さない（綱引きが起きない）ので、均等化と品質を両立できる

## 会話での使い方例

「MoE の肝はルーターで、DeepSeek-V3 は補助損失なしで bias を動かして負荷分散するから品質を削らずに均せるのが効いていますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

各トークンをどの専門家に振り分けるかを、スコア化と top-k 選択で毎トークン決めるゲーティング機構です。

### 2. うれしさ

少数の専門家だけ起動するので、総パラメータを増やしつつ 1 トークンの計算量を抑えられます。

### 3. 注意点

素朴に学習すると人気専門家にトークンが集中し（routing collapse）、残りが死んで負荷も偏ります。

### 4. どこで役立つか

DeepSeek-V3・GLM-4.5・Mixtral など、活性パラメータを抑えて巨大化する大規模 MoE の中核で効きます。

### 5. はじめに

「スコア → top-k 選択 → 加重合算、そして偏りを均す負荷分散が要る」が掴めれば入口は十分です。

### 6. 深掘り先

MoE（J-18）、補助損失 vs loss-free balancing、sigmoid gating、fine-grained / shared experts、DeepSeek-V3・GLM 技術報告

## 開発フローでの位置（必須）

1. スコア化（gating） — トークン表現にゲート行列をかけ、専門家 N 個のスコアを出す。softmax か sigmoid（独立評価）かを選ぶ
2. top-k 選択 — スコア上位 k 個の専門家だけを起動対象にし、ゲート重みを正規化する（活性パラメータを決める段）
3. 加重合算 — 選ばれた専門家の出力をゲート重みで足し合わせ、次層へ渡す。共有専門家があれば常時加える
4. 負荷分散 — routing collapse を防ぐため均等化する。従来は補助損失、DeepSeek-V3 / GLM は loss-free balancing（bias 調整）
5. 容量・配置調整 — 各専門家の capacity factor（受け入れ上限）とトークン溢れ（drop）、GPU 間の expert parallelism を調整する

## 関連用語

- MoE
- Transformer
- LLM
- DeepSeek V3
- GLM

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- routing collapse（偏り）が「何が悪いのか」が最初ピンと来なかった。偏ると分業の意味がなくなりGPU負荷も集中するとわかって腹落ちした。
- sigmoid gating を統計の4パラメータ sigmoid（立ち上がり・傾き・上限・下限）と混同していてつまずいた。MoE では 1/(1+e^−x) の1本だけと分かってクリアになった。
- 「使う/使わない」の判定がある気はしていたが、Top-K との組み合わせまでは分かっていなかった。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: sigmoid gating を仕事関数とのアナロジーでイメージしようとしたが、統計の4パラメータ版の背景が強くそこで混乱した。
- 👍 良い点: 線形でもバイナリな発火（0/1）でもなく、確率として滑らかに表現できる（畳み込める）のが良い。
- 👎 ダメな点: まだ曖昧な部分が残っていてよく分からない。
- 👥 誰向けか: ちゃんと理解したい人向け。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に 1 本のトークン h が下から入る。ルーター（ゲート行列の小箱）を通ると、横一列に並んだ 8 人の専門家（FFN）それぞれへスコア（数値バッジ）が割り振られる。上位 2 人（top-k=2）だけがハイライトされ起動、その出力がゲート重みで加重合算されて上へ抜ける。左半分に Before（素朴：2 人に矢印が殺到、6 人は点線で死亡、GPU 配置が一部赤く律速）、右半分に After（loss-free balancing：各専門家に「+b / −b」の調整つまみ、矢印が 8 人へ均等分散、GPU が均等な緑）を対比で並べる。右端に小さく「共有専門家（shared expert）」を常時通る別レーンを添える。
- 登場人物（いれば）: ルーティング盤を覗き込むエンジニア 1 名（著者の分身）。混んだ専門家の「+b/−b」つまみを回して矢印を散らしている。
- 吹き出し・心の声: 「スコアで上位 2 人を選ぶだけ。でも放っておくと人気の専門家に殺到する——bias を足し引きして、損失を汚さずに均すのが loss-free balancing」
- 中央に置くキーワード/ラベル: 「スコア化 → top-k → 加重合算」「routing collapse を bias で均す（補助損失なし）」「総パラメータ大 / 活性パラメータ小」
- Before / After の場合の対比ポイント: Before は矢印が一部に殺到し専門家が死ぬ（偏り）。After は bias 調整で均等分散。罰則を損失に足すか（綱引き発生）、bias で選択だけ動かすか（綱引きなし）の差を、損失グラフの有無で対比。

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① 分岐する振り分け矢印、③ 一点に殺到する collapse 警告、④ 専門家が横並びの MoE ブロックだけ差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ゲート行列の小箱から N 個のスコアバッジが噴き出す（softmax / sigmoid の二択タブ）
- Step 2 のアイコン/絵柄: スコア順に並んだ専門家から上位 k 個だけ点灯（top-k のスポットライト）
- Step 3 のアイコン/絵柄: 点灯した専門家の出力を重み付きで合流させる加算ノード（＋共有専門家の常時レーン）
- Step 4 のアイコン/絵柄: 偏った棒グラフに「+b/−b」つまみが効いて平らになる（loss-free balancing）。隣に綱引きする補助損失版を×印で対比
- Step 5 のアイコン/絵柄: 各専門家の容量バケツが溢れる drop と、GPU 間に専門家を分散配置する expert parallelism のネットワーク図
- 矢印で示す流れの意図: スコア化 → 選択 → 合算 → 負荷分散 → 容量/配置、という「どう振り分け、どう偏りを均し、どうハードに載せるか」の縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: MoE ルーティング（ゲーティングネットワーク）
- visual_subject: 1 本のトークンが 8 人の専門家へスコアで振り分けられる Before / After ——routing collapse（偏り）vs loss-free balancing（均等分散）
- supporting_subjects: ルーター（ゲート行列の小箱）、スコアバッジ付きの専門家（FFN）8 人、top-k ハイライト、+b/−b の調整つまみ、共有専門家の常時レーン
- logo_subject: none
- excluded_subjects: カラフルなグラフ、実在ブランドUI、赤い警告アイコン、DeepSeek・GLMのロゴ、絵文字

### scene brief（日本語）
左右 2 列の Before / After 比較。左（Before：routing collapse）は、横一列に並んだ 8 人の専門家のうち 2 人だけに矢印が殺到し、残り 6 人は点線で「使われていない」状態。右（After：loss-free balancing）は、各専門家の上に「+b / −b」の調整つまみが付き、矢印が 8 人へほぼ均等に分散している。中央上部にルーター（ゲート行列の小箱）から専門家 8 人へスコアバッジが割り振られ、top-2 だけがハイライト点灯する「振り分けの 1 サイクル」を小さく描く。右端に著者の分身エンジニア 1 名が「+b/−b」つまみを回している様子で立ち、吹き出しに「損失を汚さずに bias だけ動かして均す——routing collapse を防ぐのが肝」と語る。下辺に「スコア化 → top-k → 加重合算」「bias で選択だけ調整（補助損失なし）」のラベル。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background; a single engineer character (author's stand-in) at the right edge turning a "+b/−b" dial; left panel "Before (routing collapse)": a router box at top sends score badges to 8 expert-FFN figures in a row, but 6 experts are shown in dashed gray (idle), only 2 receive solid arrows (overloaded); right panel "After (loss-free balancing)": each of 8 experts has a small "+b/−b" adjustment knob above them, solid arrows spread evenly to all 8; a small top-center inset shows the one-cycle flow: router → score badges → top-2 highlighted → weighted sum → output; key labels "routing collapse" (left), "loss-free balancing" (right), "score → top-k → weighted sum" (bottom); flat, clean, consistent series style; 2:1 horizontal composition. Color rule: strictly #FFFFFF background, #1A1A1A lines, grays, and the five approved blues only — no yellow, green, red, purple, orange, rainbow colors, colorful UI, or emoji.

## コミュニティ補完メモ

- 同じ Lv6 シェルフ／近接エントリとの住み分け:
  - MoE（J-18）: 「MoE とは何か・なぜ総 vs 活性パラメータを分けられるか」という浅い概要を担う上位エントリ。本エントリ（J-89）はその companion で、「どのトークンをどの専門家に振るか＝ルーティング機構」だけに絞る。専門家そのものの構造や MoE 全体のメリットは J-18 に譲り、本エントリは重複させない。
  - Transformer（J-13）: MoE は Transformer の FFN 層を置き換える形で入る。ルーターが差し込まれる位置（各ブロックの FFN）の前提は J-13。
  - LLM（J-14）: MoE ルーティングが効く対象は大規模言語モデル。なぜ大規模化で活性パラメータ抑制が要るかの動機は J-14 側。
  - DeepSeek V3（D-46）: loss-free balancing ＋ sigmoid gating ＋ fine-grained/shared experts を大規模実装した代表モデル。「どのモデルが・なぜ採ったか」は D-46、「ルーティング機構そのもの」は本エントリ。
  - GLM（D-45）: GLM-4.5/4.6 系も loss-free balance routing ＋ sigmoid gates を採用。モデル固有の話は D-45、共通機構は本エントリ。
- スコープ境界: 本エントリは「ルーターの仕組み（スコア化・top-k・加重合算）／負荷分散の必要性（routing collapse）／補助損失とその副作用／loss-free balancing（bias 調整）／fine-grained・shared experts の設計」までを担う。容量係数の具体数値や expert parallelism の通信最適化の実装詳細は出典の技術レポートに譲る。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- DeepSeek-AI, "DeepSeek-V3 Technical Report" (2024) https://arxiv.org/abs/2412.19437 — checked 2026-06-22（補助損失なし負荷分散 loss-free balancing の bias 調整、sigmoid gating、fine-grained / shared experts の設計と理由）
- GLM-4.5 Team / Zhipu AI, "GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models" (2025) https://arxiv.org/abs/2508.06471 — checked 2026-06-22（loss-free balance routing ＋ sigmoid gates の採用。大規模 MoE のルーティング設計の一次情報）
- Fedus et al., "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity" (2021) https://arxiv.org/abs/2101.03961 — checked 2026-06-22（top-k=1 ルーティング、capacity factor とトークン drop、補助損失による負荷分散の古典的定式化）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- softmax vs sigmoid gating の直観: softmax は N 個のスコアを互いに競合させて確率化するため、専門家数が増えるほど 1 個あたりの確率が薄まり、勝者総取りの不安定さや微妙なスコア差の扱いが難しくなる。sigmoid は各専門家を独立に [0,1] 評価し、「選ぶ尺度（どれが妥当か）」と「合算時の重み正規化」を分離できるので、数百専門家の fine-grained MoE と相性が良い。DeepSeek-V3 / GLM がこちらを採るのはこの拡張性が理由。
- loss-free balancing が「損失を汚さない」意味: 従来の補助損失は「均等から外れたら罰」を本来の言語モデリング損失に足すため、勾配が品質方向と均等方向で綱引きになり、強くかけるほど品質が落ちる。DeepSeek-V3 はルーティング**スコア**に専門家ごとの bias 項を足し、過負荷な専門家は bias を下げ、低負荷な専門家は bias を上げる、という勾配を介さない動的更新で均す。bias は top-k の**選択**にだけ効かせ、最終的なゲート重みには元スコアを使うため、選択は均しつつ重みは歪めない設計になっている。
- fine-grained / shared experts: fine-grained experts は専門家 1 個を細かく分割して数を増やし（例: 1 個を 4 分割）、より細かい専門分化と組み合わせ自由度を稼ぐ。shared experts は全トークンが常に通る共通専門家を少数置き、共通知識をそこに集約させて、ルーティング対象の専門家には差分・専門知識を学ばせる分業。両者は DeepSeek-V3 のルーティング設計の要で、負荷分散と専門分化のバランスを取る。
