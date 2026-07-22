---
id: J-27
title: RoPE
title_reading: ロープ
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
  - Context Window
  - MLA
  - LLM
status: needs_review
---

# RoPE

<!--
バイブコーディング図鑑 スケルトン雛形 v1（2026-04-28 追加）
- 構造だけ先に置いた状態。本文は status を `drafting` に上げた段階で entry-writer が埋める
- validator は status: skeleton を archived/sample と同様にスキップする
- tagline には entry_candidates.md の「一言」を仮で流し込んでいる（本書きで磨き直す）

YAML 補足（本書きで埋める／見直す欄）:
- subtype: candidate.csv の subtype 列を流し込み済み（後で見直す）
- experience_level: hands_on / partial / research_only
- reader_level: 1〜6
- figure_type: before_after / structure / comparison / workflow / timeline（仮で structure を入れている）
- version_status: active / preview / deprecated（時変なら埋める）
- pricing_note: none / paid / freemium（時変なら埋める）
- related_terms: 3〜5 個目安
- status: skeleton → drafting → needs_review → ready
-->

## tagline

<!-- 25〜60 字（推奨 30〜38、略称展開を含む場合 35〜50）。
     タイトルが略称・ヌメロニム（MCP / a11y / LLM 等）なら冒頭に「{展開} の略。」を入れる（2026-04-28 追加）。
     例: `Model Context Protocol の略。LLM とツール・データをつなぐ標準規格です。` -->

Rotary Position Embedding の略。Query と Key を位置に応じて「回転」させ、相対位置を Attention に埋め込む位置エンコーディング方式です。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Transformer（J-13）の Attention（J-17）に「語順」を教える仕組みです。Attention はもともと、入力トークンを順序のない集合として見るため、単体では「猫が犬を追う」と「犬が猫を追う」を区別できません。そこで位置情報を別途注入する必要があります。

素朴な方法は、各位置に固有のベクトル（絶対位置エンコーディング）を作ってトークン埋め込みに足すやり方です。しかしこれは「3 番目」「100 番目」といった絶対座標を覚えさせるため、学習時に見た位置までしか効かず、それより長い文への一般化が弱いという弱点があります。

RoPE はまったく違うアプローチを取ります。位置ベクトルを「足す」のではなく、Query と Key のベクトルを、そのトークンの位置に比例した角度だけ「回転」させます。この回転を入れておくと、2 つのトークン間で計算する内積（＝ Attention スコア）が、両者の絶対位置ではなく **相対位置（位置の差）だけ** に依存するようになります。つまり「位置 m と位置 n」ではなく「m − n だけ離れている」という情報が、自然にスコアへ畳み込まれます。これが RoPE の核心です。

### 仕組みをもう一段（回転で相対位置が出る理由）

ベクトルの 2 次元ペア（x, y）を角度 θ だけ回す回転行列を R(θ) とします。位置 m の Query は角度 mθ だけ、位置 n の Key は角度 nθ だけ回します。回転後の内積を取ると、回転行列の性質 R(mθ)ᵀ R(nθ) = R((n − m)θ) により、内積の値は **(n − m)θ にのみ依存** する形に整理できます。絶対位置 m, n は打ち消し合い、差 n − m だけが残る——これが「回転で相対位置を埋め込む」の数学的な中身です。

実装では埋め込み次元を 2 つずつのペアに分け、ペアごとに異なる周波数 θ_i（低周波〜高周波）を割り当てます。低周波のペアは遠距離の位置差を、高周波のペアは近距離の位置差を表現し、複数の波長で位置を多重符号化します。複素数で書くと、各ペアを複素数 z とみなして e^{imθ} を掛ける（複素平面上の回転）操作と等価で、論文の式はこの複素表現で書かれています。

足し算ではなく回転なのでベクトルの長さ（ノルム）が変わらず、トークンの「意味」の大きさを保ったまま位置だけを乗せられる点も、絶対位置エンコーディングに対する利点です。


## どこで出会うか

オープンな大規模言語モデル（LLM, J-14）の構造を読むと、ほぼ必ず出てきます。Llama 系、Qwen 系、Mistral 系、DeepSeek 系など、近年の主要オープンモデルは位置エンコーディングに RoPE を採用しています。モデルカードや config.json に `rope_theta`（回転の基準周波数。10000 や 1000000 など）や `rope_scaling` といった項目が並んでいるのを見たら、それが RoPE のパラメータです。

長文脈化（Context Window, G-5 の拡張）の話題でも頻出します。「学習は 4K トークンでしたが 32K まで使えます」といった context length extension は、RoPE が相対位置ベースで外挿しやすい性質を土台にしています。回転の周波数をスケールして長距離に対応させる NTK-aware スケーリングや、周波数帯ごとに扱いを変える YaRN は、いずれも RoPE の角度設計をいじる手法です。これらの名前を追っていくと、必ず RoPE の理解が前提になります。


## メイン図

### 図の狙い

「絶対位置を足す」旧方式と「Query / Key を位置の角度だけ回す」RoPE を左右に並べ、回転後の内積が位置の差 (n − m) だけで決まる——つまり相対位置が自然に出る——という核心を一目で掴んでもらう図です。


## 会話での使い方例

「RoPE は位置を足さず Query と Key を回すので、相対位置で効いて外挿しやすいんですよね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Attention に語順を教える位置エンコーディング。位置を足さず Query / Key を回転させます。

### 2. うれしさ

回転後の内積が相対位置（位置の差）だけで決まり、長文への外挿がしやすくなります。

### 3. 注意点

回転周波数の設計次第で、学習長を超える文脈では精度が落ちることがあります。

### 4. どこで役立つか

長文脈化（context length extension）。NTK スケーリングや YaRN の土台になります。

### 5. はじめに

回転行列 R(mθ)ᵀR(nθ) = R((n−m)θ で相対位置が出る、という 1 本の式から入ると掴めます。

### 6. 深掘り先

NTK-aware スケーリング, YaRN, ALiBi（別系統の相対位置手法）


## 開発フローでの位置（必須）

1. 動機を確認 — Attention は集合扱いで語順を区別できない、と腹に落とす
2. 旧方式の限界 — 絶対位置を足す方式は学習長を超えると外挿が弱い
3. RoPE の核 — Query / Key を位置の角度だけ回し、内積を相対位置依存にする
4. 数理を確認 — R(mθ)ᵀR(nθ)=R((n−m)θ で絶対位置が打ち消える、を式で追う
5. 長文脈化へ展開 — rope_theta / rope_scaling を調整し NTK・YaRN へ進む


## 関連用語

- Attention
- Transformer
- Context Window
- MLA
- LLM


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「直線的な加算ではなくベクトルを回転させる」という発想は極座標のイメージで何となく掴めた。
- 回転行列は演算上扱いやすい（ノルムが変わらない等）のではという数学的な直感はある。
- 長文脈との繋がりと YaRN は未知。「回転角のスケールを調整すると文脈長を伸ばせる」という説明で繋がったが、自分からは出てこなかった。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 極座標・回転行列の発想で「ああそういうことか」となった。機械系の素養があると入りやすい。
- 👍 良い点: 絶対位置ではなく相対位置で埋め込む、という方向転換の理由が数学的に納得できた。
- 👎 ダメな点: YaRN など長文脈拡張との繋がりは説明なしには出てこない。
- 👥 誰向けか: 行列・ベクトルの基礎知識がある人が「なぜ今の LLM は長文に強いのか」を掘るのに良い。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 画面を左右 2 分割。左＝旧「絶対位置を足す」方式（トークンベクトルに位置ベクトルを + で足すイメージ、足し算の記号と「位置 3」「位置 100」ラベル）。右＝RoPE（同じ 2 つのトークンの Query / Key を矢印の向きとして描き、それぞれを位置に比例した角度 mθ・nθ だけ回した様子）。右下に内積の吹き出しで「結果は (n−m)θ だけで決まる ＝ 相対位置」と注記。
- 登場人物（いれば）: モデルの中身を覗き込む学習者（著者本人のイメージ）。右側の回転矢印を指さしている。
- 吹き出し・心の声: 学習者「足すんじゃなくて、回すのか…」／回転矢印のそばに「絶対位置 m, n は打ち消えて、差 n−m だけ残る」
- 中央に置くキーワード/ラベル: 「足す → 回す」「相対位置 = n − m」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 集合（順序なしの点の塊）に「?」
- Step 2 のアイコン/絵柄: 位置ベクトルを足す図に赤い注意マーク
- Step 3 のアイコン/絵柄: くるりと回る回転矢印
- Step 4 のアイコン/絵柄: R(mθ)ᵀR(nθ)=R((n−m)θ の式札
- Step 5 のアイコン/絵柄: 長い帯（長文脈）と rope_scaling のつまみ


## 画像生成プロンプト

<!-- 自動下書き 2026-06-22 / docs/ponchi_prompt_pipeline.md・ponchi_image_generation_rules.md 準拠。色は白・黒・グレー・青系のみ。手書き風線画。人の視点（使う人がどう感じるか）を主役に。後で画像生成に流す素案。 -->

### subject_stack
- entry_subject: RoPE（Rotary Position Embedding）
- visual_subject: 旧「位置ベクトルを足す」方式（左）と「Query/Key を位置の角度だけ回す」RoPE（右）の左右対比、回転後の内積が相対位置 (n−m) だけで決まることを示す矢印図
- supporting_subjects: 回転矢印を指さす学習者（著者の分身）、相対位置の吹き出しラベル
- logo_subject: none
- excluded_subjects: カラフルな注意ヒートマップ、虹色の位置エンコーディング波形、実在サービスのUI、絵文字

### scene brief（日本語）
画面を左右 2 分割する。左側は旧方式（絶対位置エンコーディング）として、トークンベクトルに位置ベクトルを「＋」で足す図に「位置 3」「位置 100」ラベルを添え、グレーで描く。右側は RoPE として、2 つのトークンの Query/Key ベクトルをそれぞれ mθ・nθ だけ回転させた矢印図を描き、回転後の内積の吹き出しに「結果は (n−m)θ だけで決まる ＝ 相対位置」を濃紺で注記する。中央右寄りに学習者が回転矢印を指さして「足すんじゃなくて、回すのか…」と吹き出しで語る。

### prompt（English / 画像生成用）
Hand-drawn editorial line illustration; monochrome plus blue palette only (#1A1A1A linework, neutral grays, pale blues #EAF1FB/#D6E6FA/#8DB7E8, deep navy #123E82 accent), white background; canvas split left/right — left panel (gray tone) shows absolute position encoding as a vector-plus-position-vector addition diagram labeled "位置 3" and "位置 100"; right panel shows RoPE as two token vectors being rotated by angles mθ and nθ with curved rotation arrows in pale blue #8DB7E8, and a speech bubble or annotation in deep navy #123E82 reading "(n−m)θ = 相対位置"; a single learner character in the center-right pointing at the rotation arrows with a speech bubble; flat, clean, consistent series style; minimal text labels only "足す → 回す" and "相対位置 = n − m"; 2:1 horizontal composition. No yellow, green, red, purple, orange, rainbow colors, colorful heatmaps, or brand colors.

## コミュニティ補完メモ

- Attention（J-17）: 「なぜ位置情報が要るのか（集合として見る性質）」は J-17 側の本筋。RoPE は「その位置情報をどう注入するか」の一手法として住み分ける。
- MLA（J-28）: KV キャッシュ圧縮の文脈で RoPE との相互作用（decoupled RoPE）が論点になる。数理の深掘りは J-28 側に寄せ、本エントリは「相対位置を回転で埋める」一点に絞る。
- Context Window（G-5）: 「長文脈をなぜ扱えるか」の読者向け説明は G-5。RoPE は外挿の技術的土台として参照される側。
- ALiBi など別系統の相対位置手法は本文では深掘りせず「深掘り先」に名前出しのみ。


## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- Su et al., "RoFormer: Enhanced Transformer with Rotary Position Embedding" (arXiv:2104.09864) — checked 2026-06-22
- bloc97, "NTK-Aware Scaled RoPE" (Reddit / GitHub gist で公開された context extension 手法) — checked 2026-06-22
- Peng et al., "YaRN: Efficient Context Window Extension of Large Language Models" (arXiv:2309.00071) — checked 2026-06-22


## 備考

- reader_level: 6（著者の自己学習シェルフ・刊行スコープ外）。docs/level_policy.md §2-6 に基づき、モデル内部の数理に踏み込む深掘り技術として 6 に置く。今季は刷らない。
- 数式は回転行列・複素表現の直感までに留め、厳密証明は載せていない。腹落ち優先。
- 実装上の `rope_theta` / `rope_scaling` は config 値であり時変情報を含むため出典メモを必須化（モデルごと・バージョンごとに値が異なる）。
