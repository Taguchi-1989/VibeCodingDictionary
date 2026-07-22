---
id: J-85
title: スループットとレイテンシ
title_reading: スループットとレイテンシ
category: term_general
subtype: inference
experience_level: research_only
reader_level: 6
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-06-22
related_terms:
  - バッチ推論
  - KV Cache
  - vLLM
  - 投機的デコード
  - Token
status: needs_review
---

# スループットとレイテンシ

## tagline

LLM 推論性能を測る 2 つの物差しです。スループット（単位時間に捌けるトークン数）はシステムの効率、レイテンシ（1 リクエストの体感速度）はユーザーの待ち時間を表し、両者はしばしば綱引きの関係になります。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LLM 推論を運用するとき、「速い／遅い」を一語で語ると判断を誤ります。スループットとレイテンシは、その「速さ」を 2 つの独立した軸に分解する物差しです。

**スループット（Throughput）** はシステム視点の指標で、単位時間あたりに捌けるトークン数やリクエスト数を表します。代表的には 1 秒あたりの出力トークン数（tokens/sec）やリクエスト数（requests/sec, RPS）。GPU を遊ばせず詰め込むほど高くなり、運用コスト（1 トークンあたりの単価）に直結します。

**レイテンシ（Latency）** はユーザー視点の指標で、1 つのリクエストが返ってくるまでの体感速度を表します。LLM ではこれをさらに 3 つに分けて測るのが要点です。

- **TTFT（Time To First Token）**: 最初の 1 文字が出るまでの時間。入力プロンプト全体を一度に処理する **prefill フェーズ** に律速されます。入力が長いほど、また同時に他リクエストが詰まっているほど伸びます。「送信ボタンを押してから画面に何か出るまでの沈黙」がこれです。
- **TPOT / ITL（Time Per Output Token / Inter-Token Latency）**: 2 文字目以降、1 トークンを刻む間隔。1 トークンずつ自己回帰的に生成する **decode フェーズ** に律速されます。「文字がパラパラと流れてくる速さ」がこれです。
- **エンドツーエンドレイテンシ**: 1 リクエストが完了するまでの総時間。おおむね `TTFT + 出力トークン数 × TPOT` で近似できます。出力が長い処理では第 2 項が支配的になります。

この分解が効くのは、prefill と decode で**ボトルネックの性質が違う**からです。prefill は入力トークンを行列演算でまとめて流すため計算（演算器）律速になりやすく、decode は 1 トークンずつ進めながら毎ステップ全パラメータと KV Cache をメモリから読むため**メモリ帯域律速**になりやすい。だから「TTFT を縮める手」と「TPOT を縮める手」は別物で、一緒くたに「速くする」と言うと打ち手を見失います。

## どこで出会うか

自分でモデルをホストする側に回った瞬間に、この 2 軸は必ず立ちはだかります。vLLM や TGI（Text Generation Inference）のベンチマーク結果を読むと、必ず「throughput」と「TTFT / TPOT」が別々のグラフで並んでいます。クラウドの推論 API でも、料金表は 1M トークン単価（≒ 提供側のスループット効率の裏返し）で書かれ、SLA には p50 / p99 レイテンシが書かれます。

実務で綱引きが顕在化するのは**バッチサイズを決めるとき**です。同時に処理するリクエストをたくさん束ねるほど GPU の演算器が埋まりスループットは上がりますが、1 つ 1 つのリクエストは順番待ちと演算の混雑で TTFT・TPOT が悪化します。逆にバッチを小さくすれば 1 件は速く返るが、GPU が遊んでスループット（≒ コスト効率）が落ちます。「チャット UI で 1 人を速く返したいのか」「夜間に大量文書を一括要約したいのか」で、どちらの軸を捨てるかが変わります。

## メイン図

### 図の狙い

「速さ」が 1 本の物差しではなく直交する 2 軸（縦：スループット／横：レイテンシの良さ）であること、そしてバッチを大きくすると右下（高スループット・高レイテンシ＝遅い）へ、小さくすると左上（低スループット・低レイテンシ＝速い）へ動く綱引きの関係を、運用者が天秤で悩む姿として一目で掴ませます。

## 会話での使い方例

「TTFT が悪いのは prefill 律速だから、バッチ詰め込みよりまず投機的デコードを試したいですね」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM 推論の「速さ」を効率（スループット）と体感（レイテンシ）の 2 軸に分けて測る物差しです。

### 2. うれしさ

prefill 律速の TTFT と decode 律速の TPOT を分けて見ることで、打ち手を正しく選べます。

### 3. 注意点

バッチを大きくするとスループットは上がるがレイテンシは悪化しやすく、両立はトレードオフです。

### 4. どこで役立つか

自前ホスティングのベンチ評価、バッチサイズ設計、推論コストと体感速度の折り合いをつける場面。

### 5. はじめに

「速い」を 1 語で語らず、スループット・TTFT・TPOT の 3 つを別々に測るところから始めます。

### 6. 深掘り先

連続バッチング、投機的デコード、KV Cache、Flash Attention

## 開発フローでの位置（必須）

1. 要件の見極め — チャット（TTFT 重視）かバッチ処理（スループット重視）か、優先軸を先に決める
2. ベースライン計測 — 単一リクエストで TTFT・TPOT・エンドツーエンドを測り素の性能を把握する
3. バッチ条件で再計測 — 同時実行数を上げながら、スループット向上とレイテンシ悪化の曲線を取る
4. 打ち手の選択 — TTFT は投機的デコード／prefill 最適化、TPOT は KV Cache・Flash Attention、効率は連続バッチングで攻める
5. SLA で線引き — p99 レイテンシの上限を守れる最大バッチサイズに固定し、コストと体感を両立させる

## 関連用語

- バッチ推論
- KV Cache
- vLLM
- 投機的デコード
- Token

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 普段はクラウド（API）経由なので「速い/遅い」くらいの感覚で、TTFT/TPOT を意識してこなかった。
- ローカルでモデルを動かすようになると、この2つの違いが急に気になり始める。TPOT は「後から1文字ずつ参加してくる速さ」というイメージで掴んだ。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: モデルの性能に「そんな違いがあるんだ」と初めて知った。
- 👍 良い点: 性能を単純な速い/遅いで済ませず、TTFT/TPOT で分けて見られるようになるところ。
- 👎 ダメな点: 特にない。
- 👥 誰向けか: API のレスポンスやユーザーインターフェースを設計している人向け。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 縦軸＝スループット（tokens/sec）、横軸＝レイテンシの速さ（左が速い）の 2 次元平面。平面上に右下がりの曲線を 1 本引き、「バッチ大→右下（速度を犠牲に効率）」「バッチ小→左上（効率を犠牲に速度）」の矢印を添える。曲線上に「チャット向けゾーン（左上寄り）」「バッチ処理向けゾーン（右下寄り）」の 2 領域を薄く色分け。脇に小さく「レイテンシ＝TTFT＋出力長×TPOT」の式札を置く。
- 登場人物（いれば）: 推論サーバを運用するエンジニア 1 人が、左右に皿の付いた天秤を前に腕組みして悩んでいる。天秤の左皿に「速さ（体感）」、右皿に「効率（コスト）」の重り。
- 吹き出し・心の声: 運用者の心の声「バッチを増やせば安くなる…けど 1 人ずつは遅くなるんだよな」。曲線上に小さく「ここが両立の限界（p99 SLA）」のラベル。
- 中央に置くキーワード/ラベル: 「スループット ⇄ レイテンシ は綱引き」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チャット吹き出し と 書類の山を天秤にかける絵（優先軸を選ぶ）
- Step 2 のアイコン/絵柄: ストップウォッチ 1 個（単発計測）
- Step 3 のアイコン/絵柄: 右肩上がり＆右肩下がりの 2 本の曲線グラフ
- Step 4 のアイコン/絵柄: 工具箱から KV Cache・投機的デコードのタグが出ている絵
- Step 5 のアイコン/絵柄: p99 のラインを引いた定規


## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: スループットとレイテンシ
- visual_subject: 縦軸スループット・横軸レイテンシの2次元平面上を右下がりの曲線が走り、エンジニアが天秤を前に悩む姿
- supporting_subjects: 天秤（左皿「速さ」・右皿「効率」）、右下がりトレードオフ曲線、チャット向けゾーンとバッチ処理向けゾーンの薄い塗り分け、p99 SLA ライン
- logo_subject: none
- excluded_subjects: カラフルなグラフ・実在UIスクリーンショット・他社ロゴ・緑/赤/黄の警告色

### scene brief（日本語）
2次元プロット平面を画面中央に大きく配置する。縦軸「スループット（tokens/sec）」、横軸「レイテンシの速さ（左が速い）」。右下がりの曲線を1本引き、左上寄りに薄青の「チャット向け」ゾーン、右下寄りにグレーの「バッチ処理向け」ゾーンを描く。曲線上に「バッチ大→」「←バッチ小」の小矢印。下端に「p99 SLA」の定規線。画面左端にエンジニア（著者の分身）が天秤を両手で持って立ち、心の声「バッチを増やせば安くなる…けど1人ずつは遅くなるんだよな」の吹き出し。ラベルは「スループット ⇄ レイテンシ は綱引き」1本のみ。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration, 2:1 horizontal composition (1254x627); monochrome plus blue palette only (#1A1A1A linework, neutral grays #6B7280, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background. A 2D trade-off plot occupies the center: vertical axis labeled "Throughput", horizontal axis labeled "Latency (fast ←)"; one downward-sloping curve in deep navy; pale blue zone in the upper-left ("chat use-case") and gray zone in the lower-right ("batch use-case"); small arrows along the curve for "larger batch →" and "← smaller batch"; a dashed "p99 SLA" threshold line near the bottom. A single male engineer stands at the left holding a balance scale, with a thought bubble conveying the trade-off dilemma. One label banner: "Throughput ⇄ Latency: trade-off". Flat, clean, consistent series style; minimal text, only axis names, zone names, and the one label; no yellow, green, red, purple, orange, rainbow, colorful UI, or brand marks.

## コミュニティ補完メモ

- バッチ推論（J-84）との住み分け: J-84 は「複数リクエストをまとめて GPU に流す技法」そのものを説明する。本エントリは、その技法がスループットとレイテンシの 2 軸のどこを動かすか（綱引きの理由）を扱う。連続バッチング（continuous batching）の仕組みの詳細は J-84 に寄せ、本稿では「スループットを上げレイテンシ悪化を抑える手」として 1 句触れるに留める。
- KV Cache（J-29）・Flash Attention（J-30）・投機的デコード（J-82）・vLLM（J-83）との住み分け: これら個別技法は「何をするものか」を各エントリで深掘りする。本エントリは「それぞれが TTFT / TPOT / スループットのどこを改善する手なのか」を一枚に位置づけるハブとして機能させる（KV Cache＝decode のメモリ帯域節約で TPOT・スループット、Flash Attention＝attention の I/O 削減で prefill の TTFT と長文 decode、投機的デコード＝1 ステップ複数トークンで TPOT、連続バッチング＝GPU 占有率向上でスループット）。
- Token（G-2）: スループットの単位「tokens/sec」やレイテンシの式「出力長×TPOT」がトークン単位であることの前提語。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- NVIDIA 技術ブログ「LLM Inference Benchmarking: Fundamental Concepts」（TTFT / TPOT / ITL / throughput の定義）https://developer.nvidia.com/blog/llm-inference-benchmarking-fundamental-concepts/ — checked 2026-06-22
- vLLM ドキュメント「Performance and Tuning」「Optimization and Tuning」（throughput とレイテンシのトレードオフ、バッチング設定）https://docs.vllm.ai/en/latest/ — checked 2026-06-22
- Databricks ブログ「LLM Inference Performance Engineering: Best Practices」（prefill/decode 律速、メモリ帯域とレイテンシの関係）https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices — checked 2026-06-22

## 備考

reader_level: 6（著者の自己学習シェルフ・刊行スコープ外）。docs/level_policy.md §2-6 に従い、字数制限・ですます・著者欄チェックは validator で緩和される前提で、腹落ち優先で各節を厚めに書いた。文体はですます維持。図は figure_type: comparison（2 軸平面＋天秤）。本エントリは個別最適化技法（J-29/J-30/J-82/J-83/J-84）を 2 軸上に位置づけるハブとして設計している。
