---
id: J-87
title: QK-Norm
title_reading: キューケーノルム
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
  - Attention
  - Transformer
  - RoPE
  - GLM
  - LLM
status: needs_review
---

# QK-Norm

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Query-Key Normalization（クエリ・キー正規化）の略。Attention スコアを取る前に Query と Key をそれぞれ正規化し、attention logit が膨らみすぎて softmax が飽和するのを防ぐことで、大規模・高学習率の事前学習を安定させるテクニックです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Attention（注意機構）のスコアは、Query（クエリ、問い合わせベクトル）と Key（キー、鍵ベクトル）の内積で決まります。具体的には `softmax(QKᵀ / √d)` という形で、各トークンが他のどのトークンにどれだけ注目するかを表す確率分布をつくります。問題は、学習が進むにつれて Q と K のノルム（ベクトルの長さ）がじわじわ膨らんでいくことです。ノルムが大きくなると内積（attention logit、注意ロジット）も極端に大きくなり、softmax の入力に巨大な値が混ざります。

softmax は入力差が大きいほど 1 つの要素へ確率を集中させるので、logit が膨らむと「ほぼ 1 つのトークンだけに確率が張り付く」飽和状態になります。これは attention entropy collapse（注意エントロピーの崩壊）と呼ばれ、勾配がほとんど流れなくなって学習が不安定化し、loss spike（損失の急なはね上がり）や発散を招くことがあります。

QK-Norm は、内積を取る前に Q と K をそれぞれ正規化（典型的には RMSNorm か LayerNorm をヘッド次元に対して適用）して、logit のスケールを構造的に抑え込む手法です。正規化によって Q・K の長さが一定範囲に保たれるため、学習がどれだけ進んでも logit が青天井に膨らむことがなくなり、softmax が飽和しません。結果として、大規模モデルを高い学習率で回しても安定して収束するようになります。

## どこで出会うか

普段の API 利用や推論側からは一切見えません。出会うのは、大規模 LLM（大規模言語モデル）の「事前学習をどう安定させたか」を掘り下げたときです。

具体的には、大規模モデルの技術報告で「attention logit を安定化させるために QK-Norm を採用した」と書かれている箇所、loss spike 対策・学習安定化テクの系譜（z-loss、logit soft-cap、QK-Norm などが並ぶ文脈）、Transformer のアーキテクチャ図で Q・K の経路に正規化層が挿入されている図——このあたりです。直近では GLM-4.5 系が attention logit 安定化のために QK-Norm を採用していることが技術報告で触れられており、ViT-22B（22B パラメータの Vision Transformer）の学習安定化でも使われた、よく知られた一手です。

「大規模・高学習率で学習が発散する → どう抑えるか」を追いかけ始めると、必ず名前が出てくる用語です。

## メイン図

### 図の狙い

「正規化なし（学習が進むと Q・K のノルムが膨らみ、logit が爆発して softmax が 1 トークンに飽和＝entropy collapse）」と「QK-Norm あり（Q・K を正規化して長さを抑え、logit のスケールが一定に保たれ、softmax が健全な分布を維持）」を上下に並べ、なぜ正規化が学習を安定させるのかを一目で掴んでもらう。

### A. Before / After（logit の暴走を抑える）

- Before（QK-Norm なし）
  - 状況: 学習ステップが進むほど Q・K のノルムが膨張し、内積 QKᵀ が極端に大きくなる
  - 視覚要素（概念）: 右肩上がりに伸びる Q・K のノルム曲線と、それに連動して尖っていく softmax 分布（1 本の棒だけが天井に張り付く）
  - つまずき: softmax が飽和して entropy が崩壊し、勾配が消えて loss spike・発散が起きる
- After（QK-Norm あり）
  - 状況: 内積の前に Q・K をそれぞれ正規化し、ベクトルの長さを一定範囲に固定する
  - 視覚要素: Q・K の経路にそれぞれ正規化ブロックが挿入され、ノルム曲線が水平に保たれる。softmax 分布はなだらかな山を保つ
  - うれしさ: logit が青天井に膨らまないので softmax が飽和せず、大規模・高学習率でも安定して収束する

## 会話での使い方例

「学習で attention logit が爆発して loss spike するのは、QK-Norm で Q・K を正規化して logit のスケールを抑えれば防げますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

内積の前に Query と Key を正規化し、attention logit のスケールを抑えて softmax の飽和を防ぐ手法です。

### 2. うれしさ

大規模・高学習率でも logit が暴走せず、loss spike や発散を抑えて事前学習を安定させられます。

### 3. 注意点

固定係数 1/√d とは違い、QK-Norm は学習を通じてノルムそのものを制御する点が本質です。

### 4. どこで役立つか

数十億〜数千億パラメータの LLM 事前学習など、attention logit が膨らんで不安定化しやすい場面で効きます。

### 5. はじめに

「Q・K のノルムが膨らむ → logit 爆発 → softmax 飽和 → 学習崩壊。それを正規化で根元から抑える」が掴めれば十分です。

### 6. 深掘り先

attention entropy collapse、RMSNorm / LayerNorm、RoPE との適用順序、logit soft-cap、GLM-4.5 技術報告

## 開発フローでの位置（必須）

1. 不安定の検知 — 大規模・高学習率の事前学習で loss spike や発散が起き、attention logit が異常に大きいことを掴む
2. 原因の特定 — 学習が進むほど Q・K のノルムが膨らみ、softmax が 1 トークンに飽和（entropy collapse）していると突き止める
3. 正規化の挿入 — 内積 QKᵀ を取る直前に、Q と K へそれぞれ RMSNorm / LayerNorm をヘッド次元で適用する
4. RoPE との順序調整 — 位置回転（RoPE）を「正規化の前か後か」を設計し、回転と正規化が干渉しないよう適用順を決める
5. 安定性の確認 — logit のスケールが頭打ちになり、loss spike が消え、高学習率でも収束することを検証する

## 関連用語

- Attention
- Transformer
- RoPE
- GLM
- LLM

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 実際にどうやって正規化するのか（どのタイミングで・どの範囲に丸め込むのか）が掴めなかった。
- 従来の 1/√d スケーリング（単純に値を小さくする）との違いがどこにあるのかが分かりにくかった。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 大暴走させないだろうな、という感覚はある。
- 👍 良い点: 内積の暴走というボトルネックにちゃんと手当てをしていて、複雑な計算を可能にしているところ。
- 👎 ダメな点: 基本原則からの発展が積み重なっていて、どこで何をしているのか分かりにくくなってくる。
- 👥 誰向けか: 中の仕組みを深く考える人。この仕組みがどんなハードウェアを必要とするか、まで考えたい人。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 上段に「QK-Norm なし」、下段に「QK-Norm あり」の 2 段比較。上段は左に「学習ステップ→」を横軸にした Q・K ノルムの右肩上がり曲線、その先に「QKᵀ / √d」の内積ブロックが赤く膨れ上がり、右端の softmax 分布は 1 本の棒だけが天井に張り付く尖った形（entropy collapse）。さらにその下に「loss」曲線がギザギザに跳ねる loss spike を小さく添える。下段は同じ流れだが、Q の経路と K の経路にそれぞれ「Norm」ブロック（正規化層）を挿入し、ノルム曲線が水平に保たれ、内積ブロックは赤くならず、softmax 分布はなだらかな山、loss 曲線は滑らかに下る。
- 登場人物（いれば）: 学習ダッシュボードの loss 曲線を睨むエンジニア 1 名（著者の分身）。上段の跳ねた loss spike を指差して困り顔、下段の滑らかな曲線を見て安堵している。
- 吹き出し・心の声: 「Q・K のノルムが青天井に伸びて logit が爆発する。正規化で長さを抑えれば、softmax は飽和しないし loss も跳ねない」
- 中央に置くキーワード/ラベル: 「ノルム膨張 → logit 爆発 → softmax 飽和（entropy collapse）」「内積の前に Q・K を正規化」
- Before / After の場合の対比ポイント: 上段は「右肩上がりのノルム曲線 ＋ 尖った softmax ＋ ギザギザの loss」、下段は「水平なノルム曲線 ＋ なだらかな softmax ＋ 滑らかな loss」。正規化ブロックの有無が三つの曲線すべての形を変えることを対比。

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（① Q・K の経路に挟まる Norm ブロック、③ 固定係数 1/√d と学習制御の違いを示す「固定 vs 可変」マークだけ差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ギザギザに跳ねる loss 曲線（loss spike）と赤い警告マーク
- Step 2 のアイコン/絵柄: 右肩上がりの Q・K ノルム曲線＋尖った softmax（entropy collapse の提示）
- Step 3 のアイコン/絵柄: Q の経路と K の経路それぞれに挿入される Norm ブロック（内積の直前）
- Step 4 のアイコン/絵柄: RoPE の回転矢印と Norm ブロックの適用順（前後）を示す分岐レーン
- Step 5 のアイコン/絵柄: 水平に頭打ちになる logit スケールゲージ＋滑らかに下る loss 曲線（安定収束）
- 矢印で示す流れの意図: 不安定検知 → 原因特定 → 正規化挿入 → RoPE 両立 → 安定確認、という「なぜ logit が暴走し、どこに正規化を入れて止めるか」の縦の流れ

## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: QK-Norm（Query-Key Normalization）
- visual_subject: attention logit 爆発の Before / After ——正規化なしで loss spike、正規化ありで安定収束
- supporting_subjects: Q・K のノルム曲線（右肩上がり vs 水平）、softmax 分布（尖った vs なだらか）、loss 曲線（ギザギザ vs 滑らか）、Norm ブロック（Q・K 経路に挿入）
- logo_subject: none
- excluded_subjects: カラフルなグラフ、赤い警告アイコン、絵文字、実在する DL フレームワーク UI、ブランドカラー

### scene brief（日本語）
上下 2 段の Before / After 比較図。上段（QK-Norm なし）は、学習が進むにつれて Q・K のノルム曲線が右肩上がりに伸び、その先の softmax 分布が 1 本の棒だけ天井に張り付く尖った形（entropy collapse）で、loss 曲線はギザギザに跳ねている。下段（QK-Norm あり）は、Q・K の経路それぞれに Norm ブロックが挿入され、ノルム曲線は水平に保たれ、softmax はなだらかな山を維持し、loss は滑らかに下る。画面右端に学習ダッシュボードを睨む著者の分身エンジニア 1 名を配置し、上段で困り顔（loss spike を指差す）、下段で安堵している様子を吹き出しで示す。中央ラベルは「Q・K のノルム膨張 → logit 爆発 → softmax 飽和（entropy collapse）」「内積の前に Q・K を正規化」。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background; a single engineer character (author's stand-in) at the right edge — frowning and pointing at a jagged loss-spike curve in the top half, relaxed with a thought bubble showing a smooth descending loss curve in the bottom half; top panel labeled "No QK-Norm": Q and K norm curves rise steeply to the right, the attention softmax bar chart shows one bar spiking to the ceiling (entropy collapse), the loss curve zigzags; bottom panel labeled "QK-Norm": small "Norm" blocks are inserted in both the Q path and K path before the dot-product box, norm curves remain flat, softmax shows a gentle hill, loss curve descends smoothly; key labels "norm explosion → logit burst → softmax saturation" (top) and "normalize Q & K before dot product" (bottom) in minimal text; flat, clean, consistent series style; 2:1 horizontal composition. Color rule: strictly #FFFFFF background, #1A1A1A lines, grays, and the five approved blues only — no yellow, green, red, purple, orange, rainbow colors, colorful UI, or emoji.

## コミュニティ補完メモ

- 同じ Lv6 シェルフの近接語との住み分け:
  - Attention（J-17）: Q/K/V と softmax(QKᵀ/√d) の基礎。QK-Norm はその内積の「直前」に正規化を挟む派生なので、J-17 が前提。
  - Transformer（J-13）: 層の積み重ねと残差・正規化の置き場所（Pre-LN / Post-LN）の基礎。QK-Norm は「どこに何の正規化を置くか」という設計議論の一支流として位置づく。
  - RoPE（J-27）: 位置情報を Q・K の回転で入れる手法。QK-Norm と RoPE はどちらも Q・K に作用するため適用順序（回転の前に正規化するか後か）が論点になる。順序設計の詳細は J-27 と本エントリで分担。
  - GLM（D-45）: QK-Norm を attention logit 安定化のために採用した代表的なモデル系列。「どのモデルが・なぜ採ったか」は D-45 側、「QK-Norm という仕組みそのもの」は本エントリ。
  - LLM（J-14）: 大規模事前学習の安定化という文脈の上位概念。loss spike / z-loss / logit soft-cap など安定化テク全体の地図は J-14 側、QK-Norm 単体の深掘りは本エントリ。
- スコープ境界: 本エントリは「QK-Norm とは何か・なぜ logit が暴走するか・正規化でどう止まるか・1/√d スケーリングとの違い・RoPE との順序が論点になる点」までを担う。RMSNorm/LayerNorm の数式詳細や各モデルの実装差は出典の技術報告に譲る。
- 1/√d との違いを明確に: softmax 直前の `/√d` は内積の期待スケールを次元 d に対して固定で割る定数項で、学習開始時点のスケールを整えるだけ。QK-Norm は学習が進んでも Q・K のノルムが膨らまないよう「実行時のベクトル長そのもの」を正規化で制御する。前者は静的な係数、後者は動的なノルム制御、という対比が肝。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Henry et al., "Query-Key Normalization for Transformers" (2020) https://arxiv.org/abs/2010.04245 — checked 2026-06-22（QK-Norm の初出。Q・K を正規化して内積スケールを抑える定式化と効果の報告）
- Dehghani et al., "Scaling Vision Transformers to 22 Billion Parameters" (ViT-22B, 2023) https://arxiv.org/abs/2302.05442 — checked 2026-06-22（大規模学習の安定化に QK-Norm を採用した代表例。attention logit の発散対策としての位置づけ）
- Zeng et al., "GLM-4.5: ..." Technical Report (2025) https://arxiv.org/abs/2508.06471 — checked 2026-06-22（GLM-4.5 系が attention logit 安定化のために QK-Norm を採用していることの一次情報）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- attention entropy collapse の機序: softmax 入力（logit）の最大値と他の差が大きいほど出力が one-hot に近づき、確率分布のエントロピーが 0 へ落ちる。one-hot に近い分布は softmax のヤコビアンが極小（p_i(1-p_i) がほぼ 0）になり勾配が消えるため、その層の学習が止まって全体の最適化が崩れる。Q・K のノルム膨張はこの logit 増大の主因なので、ノルムを正規化で頭打ちにすれば entropy collapse を根元から防げる、という因果。
- RoPE との適用順序: RoPE は Q・K に位置依存の回転をかける。回転はノルムを保存する直交変換なので「正規化 → 回転」でも「回転 → 正規化」でもノルム制御の効果自体は保たれるが、実装上は正規化を回転の前に置く構成が一般的。誌面・本文では深入りせず「順序が設計論点になる」に留める。
- 近縁の安定化テクとの整理: logit soft-cap（tanh で logit に上限を被せる、Gemma 系）は出力側で logit を抑える対症療法、QK-Norm は入力側で Q・K の長さを抑える予防策、という違い。z-loss は softmax の正規化項を罰則として加える別軸。これらは排他でなく併用されることもある。
