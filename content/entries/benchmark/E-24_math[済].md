---
id: E-24
title: MATH
title_reading: マス
category: benchmark
subtype: reasoning
experience_level: research_only
reader_level: 3-4
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - GSM8K
  - AIME
  - MMLU-Pro
  - Thinking モデル
status: ready
---

# MATH

## tagline

競技数学レベルの推論を測るベンチマークです。難問 12,500 問でモデルの数学力を評価します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

2021 年公開の数学ベンチマークです。代数・幾何・数論・確率など 7 分類 12,500 問を収録し、最終回答を照合して正答率を算出します。


## どこで出会うか

新モデルの発表資料で「MATH スコア 90%超」のように登場します。GSM8K（小学校算数レベル）より格段に難しく、Level 5 はいまも伸び代が残っています。


## メイン図

### 図の狙い

GSM8K と MATH の難易度帯の違いを並べて、MATH が競技数学域に位置することを示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: 研究者・エンジニアがモデルのリリースノートで MATH スコアを確認する
- シーン2: 複数モデルを比較した表で GSM8K と MATH の列が並ぶ
- シーン3: 社内ツール選定でデータ分析モデルの実力を参考指標として引用する
- 並べる基準: 難易度の低い GSM8K → 難易度の高い MATH の順で対比


## 会話での使い方例

「MATH の Level 5 に強いモデルなら、社内のデータ分析でも詰まりにくいですね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

モデルの競技数学レベルの推論力を正答率で定量化します。

### 2. うれしさ

難易度 Level 別のスコアで、モデルの得意・不得意を細かく比べられます。

### 3. 注意点

途中の計算過程ではなく、最終回答の一致だけを採点する仕様です。

### 4. どこで役立つか

数値計算や論理推論が求められる業務ツール選定の参考になります。

### 5. はじめに

GSM8K との難易度差と、スコアが何を意味するかを押さえれば十分です。

### 6. 深掘り先

GSM8K、AIME、Thinking モデル


## 開発フローでの位置（必須）

1. モデル選定 — 発表資料で MATH スコアを確認し、数学推論力の目安にします
2. 難易度確認 — Level 1〜5 の内訳を見て、業務要件に近い難度帯を絞り込みます
3. 比較評価 — GSM8K スコアと並べて、易〜難の推論力バランスを把握します
4. 採用判断 — Hard サブセット（Level 5）の成績をデータ分析用途の判断基準にします


## 関連用語

- GSM8K
- AIME
- MMLU-Pro
- Thinking モデル


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Level 5 が他ベンチマークでどの位置かイメージしにくいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:今回初めて知りました
- 👍 良い点:段階別なので 1 つで能力を幅広く測れるのが良いです
- 👎 ダメな点:難易度の感覚がつかみにくいです
- 👥 誰向けか:結構マニアックな層向けかなと思います
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 縦軸に難易度（低→高）、横軸に代表ベンチマーク名（GSM8K / MATH Level1〜5）を並べた帯グラフ
- 登場人物: エンジニア風の人物が棒グラフを指差しながら比較している
- 吹き出し・心の声: 「GSM8K はもう 99% 出るのに、MATH Level 5 はまだ伸び代がある！」
- 中央に置くキーワード/ラベル: MATH Level 5（難問帯）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡とスコア表
- Step 2 のアイコン/絵柄: レベルメーター（1〜5）
- Step 3 のアイコン/絵柄: 2 本棒グラフの比較
- Step 4 のアイコン/絵柄: チェックマークと採用ラベル
- 矢印で示す流れの意図: 発表資料確認 → 難度帯絞り込み → 他ベンチと比較 → 採用判断の一連の流れ

## コミュニティ補完メモ

- GSM8K（E-23）との住み分け: GSM8K は小学校算数レベルで飽和気味、MATH は競技数学級でまだ伸び代がある点を軸に分ける
- AIME（E-25）との住み分け: AIME は MATH の上位互換として位置づけ、E-25 で扱う
- MMLU-Pro（E-21）との住み分け: MMLU-Pro は多分野の知識幅、MATH は数学推論の深さで役割が異なる
- タイトル注意: `MATH` は一般語と紛らわしいが、ベンチ名そのもの。論文タイトル「Measuring Mathematical Problem Solving With the MATH Dataset」を覚えると検索しやすい


## 出典メモ

- Hendrycks et al. "Measuring Mathematical Problem Solving With the MATH Dataset" (2021) [arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874) — checked 2026-04-30
- MATH Leaderboard (Papers With Code) [paperswithcode.com/sota/math-word-problems-on-math](https://paperswithcode.com/sota/math-word-problems-on-math) — checked 2026-04-30

## 備考

- MATH スコアはモデル世代ごとに更新されるため時変情報として扱う（evaluation_date 参照）
- 正答率の評価方式: 最終回答のみ照合（Chain of Thought の途中式は対象外）
- Level 5（Hard サブセット）は 2025〜2026 時点でもトップモデルが 90% 台前半にとどまることがある
