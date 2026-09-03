---
id: J-82
title: 投機的デコード
title_reading: とうきてきデコード
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
  - KV Cache
  - LLM
  - Transformer
  - スループットとレイテンシ
  - Attention
status: ready
---

# 投機的デコード

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Speculative Decoding の略。小さく速いドラフトモデルに先のトークンを予想させ、大きい本命モデルが 1 回でまとめて検証することで、出力を変えずに生成を速くする推論高速化です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM（大規模言語モデル）の生成は自己回帰、つまり「1 トークン出す → それを入力に足してまた 1 トークン出す」を繰り返します。1 ステップで進めるのは必ず 1 トークンだけで、しかも大きいモデルは 1 ステップが重い——ここが生成の遅さ（レイテンシ）の正体です。GPU の演算能力はまだ余っているのに、メモリから巨大な重みを読み出す時間に律速され、1 トークンごとに「重みの全読み出し」を払い続けます。

投機的デコード（Speculative Decoding）は、この「1 ステップ 1 トークン」の縛りを実質的に緩めます。まず小さく速いドラフトモデル（draft model＝下書き役）に、先の数トークン（たとえば 4〜5 個）を一気に予想（投機）させます。次に大きい本命モデル（target model＝採点役）が、その候補列を**1 回の forward でまとめて検証**します。Transformer は系列を並列に処理できるので、4 トークンの検証は 1 トークンの生成とほぼ同じ時間で済みます。予想が当たっていればその列を一気に採用し、外れた箇所からは本命が出し直します。1 回の重い検証で複数トークンを確定できるぶん、重み読み出しの回数＝実質ステップ数が減り、速くなります。

決定的に重要なのは、**受理／棄却の確率設計によって出力分布が本命モデル単独と数学的に一致する**点です。各候補トークンを、本命の確率 p とドラフトの確率 q の比 min(1, p/q) で確率的に受理し、棄却したら補正分布 (p − q) の正の部分から引き直す——この棄却サンプリングにより、近似ではなく**本命と同じ分布**から引いたことになります。だから「速くなるが品質は落ちない」と言えます。

## どこで出会うか

API を叩く側からは投機的デコードは見えません。出会うのは「同じモデルなのに推論基盤を変えたら体感が速くなった」「TPS（Tokens Per Second＝毎秒トークン数）が上がったがコストは変わらない」といった、レイテンシの内訳を掘り下げたときです。

具体的には、vLLM・TensorRT-LLM・llama.cpp などの設定で `speculative` や `draft model`・`n-gram` といった項目を見たとき、「Medusa を入れて 2 倍速」「self-speculative decoding で追加モデル不要」といったリリースノートや論文、あるいは「ドラフトの的中率（acceptance rate）が低くてあまり速くならなかった」というチューニングの議論——このあたりで名前に出くわします。「メモリ帯域律速をどう逃れるか」という推論最適化の文脈では、KV Cache や量子化と並んで必ず候補に挙がる手法です。

## メイン図

### 図の狙い

「ドラフトが先のトークンを予想 → 本命が 1 回でまとめて検証 → 当たった列を一気に採用、外れた所から出し直し」という 1 サイクルを横に流して描き、なぜ重い本命モデルの呼び出し回数が減るのか（＝なぜ速いのか）と、出力は本命単独と一致する（＝品質は落ちない）ことを同時に掴んでもらう。

### A. 仕組み図（1 サイクルの流れ）

- 状況: ドラフトモデルが 4 トークン「the／cat／sat／on」を一気に予想する
- 検証: 本命モデルが 4 候補を 1 回の forward で並列採点。先頭から順に受理判定し、たとえば 3 個目で棄却が出たらそこで打ち切り
- 採用: 受理できた先頭 3 個（the／cat／sat）を確定し、棄却が出た位置は本命の補正分布から 1 個引き直す
- うれしさ: 本命の 1 回呼び出しで 3〜4 トークン進む（的中率が高いほど稼げる）。重い呼び出しの回数が減るので速い
- 不変条件: 受理／棄却の確率設計により、最終的な出力分布は本命を素直に 1 トークンずつ回したときと一致する

## 会話での使い方例

「投機的デコードはドラフトの的中率が命で、外れると本命を呼び直すぶん効きが鈍りますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

小さいドラフトモデルに先読みさせ、本命モデルが一括検証することで生成を速くする推論高速化です。

### 2. うれしさ

受理／棄却の確率設計により、出力分布を本命単独と一致させたまま速くできます（品質を落とさない）。

### 3. 注意点

効果はドラフトの的中率に依存し、外れが多いと本命の呼び直しが増えてほとんど速くなりません。

### 4. どこで役立つか

メモリ帯域に律速されるレイテンシ重視の生成、特に対話やコード補完で効きます。

### 5. はじめに

「予想して一括検証、外れたら出し直し。確率設計で出力は本命と同じ」が掴めれば十分です。

### 6. 深掘り先

棄却サンプリングの証明、Medusa、自己投機（self-speculative）、n-gram draft、EAGLE

## 開発フローでの位置（必須）

1. ドラフト確保 — 本命と同じ語彙・近い分布を持つ小型モデル、または Medusa ヘッドや n-gram 表を用意する
2. 投機（draft） — ドラフトが先の k トークンを一気に予想し、各位置の確率 q も記録する
3. 検証（verify） — 本命モデルが候補列を 1 回の forward で並列採点し、各位置の確率 p を得る
4. 受理／棄却 — 先頭から min(1, p/q) で受理、最初の棄却位置で打ち切り、そこは補正分布 (p−q)+ から 1 個引き直す
5. 反復 — 確定した列を入力に継ぎ足し、的中率を見ながら先読み長 k を調整して次サイクルへ

## 関連用語

- KV Cache
- LLM
- Transformer
- スループットとレイテンシ
- Attention

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「品質を変えずに速くなる」カラクリは納得感があった。
- 他の科学技術計算（Python 等）でも投機的な手法は知っていたので、"枯れた技術の LLM への展開"として腑に落ちた。
- 的中率のトレードオフは意識できているが、チューニングはモデル設計者に委ねている感じ。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 投機的実行という考え方自体は知っていたので「あ、それを LLM でもやるのか」とすんなり入った。
- 👍 良い点: 品質が変わらないという数学的保証があるのが面白い。枯れた技術の新展開という整理がしっくりくる。
- 👎 ダメな点: ドラフトモデルの的中率がどれくらいかは実際に使ってみないと感覚がつかめない。
- 👥 誰向けか: 「なぜ最近の LLM は速くなったのか」を技術的に理解したい人に良い。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左から右へ 1 サイクルを流す。①「ドラフト（小さい歯車）」が 4 枚の付箋「the/cat/sat/on」を一気に書き出す。②「本命（大きい歯車）」が 4 枚をまとめて 1 回でチェック（並列の採点矢印を 4 本まとめて 1 ストロークで描く）。③ 先頭 3 枚に緑のチェック、3 枚目の後に赤バツが付き、赤バツ位置は本命が新しい付箋を 1 枚引き直す。④ 確定した列が本文に連結される。比較用の小さなインセットで「素朴版＝本命が 1 枚ずつ重い呼び出しを繰り返す」を薄く添え、呼び出し回数の差を見せる。
- 登場人物（いれば）: 推論基盤を覗き込むエンジニア 1 名（著者の分身）。大きい歯車（本命）の 1 回の呼び出しで複数の付箋が確定する様子に注目している。
- 吹き出し・心の声: 「重いのは本命を呼ぶこと。だから下書きさせて 1 回でまとめて採点する。外れた所だけ本命が直せば、出てくる文章は本命単独と同じ——速いのに品質は変わらない」
- 中央に置くキーワード/ラベル: 「予想 → 一括検証 → 当たりは採用・外れは出し直し」「出力分布は本命と一致（min(1, p/q)）」
- 補足: CPU の投機的実行（分岐先を先に計算しておき、当たれば得・外れれば捨てる）との対応を小さな脚注アイコンで添えると名前の由来が伝わる。

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① 小歯車＋大歯車のペア、③ 的中率メーター（低いと効かない）を差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 小型ドラフトモデル（または本命に生えた複数の予測ヘッド＝Medusa）の準備
- Step 2 のアイコン/絵柄: ドラフトが k 枚の付箋を一気に書き出す（先読み）
- Step 3 のアイコン/絵柄: 本命が k 枚を 1 ストロークで並列採点（1 回の forward）
- Step 4 のアイコン/絵柄: 緑チェックと赤バツ＋補正分布から 1 枚引き直す min(1, p/q)
- Step 5 のアイコン/絵柄: 的中率メーターを見ながら先読み長 k を調整するダイヤル
- 矢印で示す流れの意図: 「下書き → 一括採点 → 受理／棄却 → 調整して反復」という、なぜ呼び出し回数が減るか・なぜ品質が保たれるかの縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: 投機的デコード（Speculative Decoding）
- visual_subject: 小さなドラフト歯車が4枚の付箋を一気に書き出し、大きな本命歯車が1回でまとめて採点し、緑チェックと赤バツで受理・棄却を決める「予想→一括検証→採用」の1サイクル
- supporting_subjects: 先頭3枚の緑チェック、3枚目以降の赤バツと補正分布からの引き直し付箋、確定した列が本文に連結される様子
- logo_subject: none
- excluded_subjects: カラフルなグラフ、絵文字、実在サービスのUI、赤・緑・黄の差し色（チェック・バツは白黒またはグレー系で表現）

### scene brief（日本語）
推論基盤を覗き込むエンジニア1名（著者の分身）が、大きな歯車（本命）の1回の呼び出しで複数の付箋が確定する様子に注目している場面。左から右へ1サイクルを流す。①小さな歯車（ドラフト）が4枚の付箋「the/cat/sat/on」を一気に書き出す。②大きな歯車（本命）が4枚をまとめて並列採点（4本の採点矢印を1ストロークで束ねる）。③先頭3枚にチェックマーク、4枚目にバツ印が付き、バツ位置は本命が新しい付箋を1枚引き直す。④確定した列が右の本文に連結される。エンジニアの吹き出し：「重いのは本命を呼ぶこと。だから下書きさせて1回でまとめて採点する。外れた所だけ本命が直せば、出てくる文章は本命単独と同じ——速いのに品質は変わらない」。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, flat light gray fills, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background. A single engineer character (author avatar, male, standing right side) observing the cycle with a speech bubble: "One big call, multiple tokens confirmed." Left-to-right horizontal flow: a small gear labeled "Draft" emitting four sticky-note cards ("the", "cat", "sat", "on") simultaneously; a large gear labeled "Target" receiving all four cards in a single parallel verification stroke (four arrows bundled as one sweep); the first three cards marked with checkmarks in #8DB7E8, the fourth card marked with a cross (×) in #6B7280; a new replacement card being drawn from a small correction pile by the large gear; the confirmed tokens flowing right into a growing text strip. Small inset in bottom-left corner (lighter, smaller): naive decoding showing the large gear being called four separate times with heavy individual arrows, labeled "×4 calls". No colorful charts, no brand logos, no yellow/green/red/purple, no emoji. The contrast between one bundled verification sweep and four separate heavy calls is the visual core. Flat, clean, consistent series style; minimal text, only key labels. 2:1 horizontal composition.

## コミュニティ補完メモ

- 削る対象が違う近接語との住み分け（ここが本エントリの肝）:
  - KV Cache（J-29）/ Flash Attention（J-30）: これらは「1 ステップ（1 トークン）の処理を軽くする」最適化。投機的デコードは「ステップ数（本命の呼び出し回数）を実質減らす」最適化。削る対象が直交するので併用でき、実際の推論基盤では両方同時に効かせる。
  - 量子化（重みのビット削減）: 1 ステップの重み読み出し量を減らす方向。これも投機的デコードと直交し、ドラフトモデル自体を量子化して速くする使い方もある。
  - スループットとレイテンシ（J-85）: 投機的デコードは主に**レイテンシ（1 リクエストの応答速度）**を下げる手法。一方バッチを大きくする最適化はスループット重視で、両者はトレードオフになることがある（投機の検証はバッチ内で計算を食うため、満杯バッチでは旨味が減る）。
  - バッチ推論（J-84）/ vLLM（J-83）: 投機的デコードを実装する側の基盤。受理されたトークン数が可変になるため、バッチ管理や KV Cache の扱いが素朴版より複雑になる。
- 派生・関連手法（深掘り先）:
  - Medusa: 別モデルを用意せず、本命に複数の予測ヘッドを追加してドラフト列を作る。デプロイが簡単。
  - 自己投機（self-speculative decoding）: 本命の一部の層だけ通した「浅い自分」をドラフトに使い、追加モデル不要にする。
  - n-gram draft（prompt lookup decoding）: 入力中に既出の語列をそのままドラフトに使う。要約・コード補完など「入力からの引用が多い」タスクで的中率が高い。
  - EAGLE 系: 特徴量レベルで次トークンを予測し的中率を上げた改良。
- スコープ境界: 本エントリは「投機的デコードとは何か・なぜ出力が一致するか・KV Cache 系とどう削る対象が違うか」までを担う。棄却サンプリングの完全な証明や各派生手法の数理は深掘り先に譲る。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Leviathan, Kalman, Matias, "Fast Inference from Transformers via Speculative Decoding" (Google, 2022) https://arxiv.org/abs/2211.17192 — checked 2026-06-22（受理／棄却の確率設計で出力分布が target と一致することを示した一次出典）
- Chen et al., "Accelerating Large Language Model Decoding with Speculative Sampling" (DeepMind, 2023) https://arxiv.org/abs/2302.01318 — checked 2026-06-22（大規模モデルでの speculative sampling の定式化と棄却サンプリングの証明）
- Cai et al., "Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads" (2024) https://arxiv.org/abs/2401.10774 — checked 2026-06-22（別ドラフトモデルを使わず複数ヘッドで投機する派生手法）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- 計算量の表現について: 厳密には「実質ステップ数」は受理トークン数の期待値で決まり、的中率 α・先読み長 k のとき 1 サイクルあたり期待受理数は (1−α^(k+1))/(1−α) で近似される（Leviathan et al. 2022）。誌面では混乱を避け「本命の呼び出し回数が減る＝速い、的中率が低いと効かない」に表現を寄せた。
- 名前の由来: CPU の投機的実行（speculative execution）との対応——分岐先を確定前に先回りで計算し、当たれば時間を稼ぎ、外れれば捨てる。投機的デコードも「先回りで予想し、外れたら捨てる」点で同じ発想。
