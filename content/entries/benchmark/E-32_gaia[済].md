---
id: E-32
title: GAIA
title_reading: ガイア
category: benchmark
subtype: agent
experience_level: research_only
reader_level: 3-4
importance: E
figure_type: comparison
page_layout: spread_v1
start_date: 2023-11-01
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - WebArena
  - AgentBench
  - OSWorld
  - AGI
status: ready
---

# GAIA

## tagline

General AI Assistants の略。人間が数分で解くタスクに AI がどこまで近づけるかを測るベンチマークです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Meta（C-4）と Hugging Face（C-7）が 2023 年末に公開した、AI エージェントの実用能力を測る問題集です。Web 検索・PDF 読解・画像理解など複数ツール協調が要る 466 問・Level 1〜3 です。

## どこで出会うか

AI エージェントのリリース記事や研究論文で「GAIA スコア」として登場します。公開時は GPT-4 約 15%・人間約 92%、2025 年には上位勢が 60% 台に到達しています。

## メイン図

### 図の狙い

GAIA の 3 難易度と代表スコアを並べ、AI と人間の差がどれだけ縮まったかを一目で示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: 研究者がエージェントの総合能力を他社モデルと比較するとき
- シーン2: AI ニュースで「GAIA Level 3 で人間に迫った」と報じられるとき
- シーン3: AGI 議論の参照指標として引用されるとき
- 並べる基準: 難易度別スコアの比較（AI vs 人間）

## 会話での使い方例

「GAIA Level 3 で Manus が人間に迫ったニュースを社内に共有しました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI エージェントの実世界タスク処理能力を測る問題集です。

### 2. うれしさ

人間基準との差が数値で見えるため、進化の速さを実感できます。

### 3. 注意点

同名の別プロジェクトが複数あり、本書では Meta + HF 版を指します。

### 4. どこで役立つか

エージェント導入の判断材料として比較評価の場面で参照されます。

### 5. はじめに

Level と問題数（466 問）と人間スコア（約 92%）が理解の起点です。

### 6. 深掘り先

WebArena、AgentBench、AGI

## 開発フローでの位置（必須）

1. 課題設定 — エージェントに「実世界で役立つか」を検証したいと考える
2. ベンチ選定 — Web 検索・ツール協調を測れる GAIA を評価指標に選ぶ
3. 評価実行 — Level 1〜3 の問題セットをエージェントに解かせてスコアを記録する
4. 比較分析 — 他モデル・人間スコアと並べて能力ギャップを可視化する
5. 改善反映 — 弱い Level の問題タイプをもとにプロンプトや設計を見直す

## 関連用語

- WebArena
- AgentBench
- OSWorld
- AGI


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 今回初めて知った語で、ベンチマークの存在自体が遠く感じられました。
- スコアが評価フレームワークで大きく変わり、単純比較が難しいです。
- AGI 議論の参照に使われるとはいえ、どこまで AGI 判断に直結するか不明です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回初めて存在を知り、人間との差を測る指標として面白いと感じました。
- 👍 良い点: モデルの賢さを定量的に比べられ、人間スコアと並列で見られる点が有用です。
- 👎 ダメな点: 評価フレーム次第でスコアが大きく動き、いつまで参照できるか見極めが要ります。
- 👥 誰向けか: AGI 議論やモデル選定で「賢さの相場」を語りたい人にとって押さえどころです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 横軸を難易度（Level 1 / 2 / 3）、縦軸をスコア（%）にした棒グラフ形式の比較図。「人間」と「AI（上位モデル）」の棒を並べて差を示す
- 登場人物（いれば）: 研究者風の人物 1 名。棒グラフをポインターで指して解説している構図
- 吹き出し・心の声: 「人間 92%、AI は今どこまで来てる？」
- 中央に置くキーワード/ラベル: GAIA スコア比較
- Before / After の場合の対比ポイント: なし（comparison）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（課題設定）
- Step 2 のアイコン/絵柄: チェックリスト（ベンチ選定）
- Step 3 のアイコン/絵柄: ロボット＋問題用紙（評価実行）
- Step 4 のアイコン/絵柄: 棒グラフ（比較分析）
- Step 5 のアイコン/絵柄: レンチ（改善反映）
- 矢印で示す流れの意図: 課題発見 → 評価 → 分析 → 改善の反復サイクル

## コミュニティ補完メモ

- WebArena（E-31）との住み分け：WebArena は Web ブラウザ操作タスクに特化。GAIA はマルチツール協調・PDF・画像など幅広い実世界タスクをカバーする総合型ベンチマーク
- AgentBench（E-33）との住み分け：AgentBench は OS・データベース・ゲームなど多環境での動作を評価。GAIA は人間難易度を基準に置く点が特徴的
- OSWorld（E-34）との住み分け：OSWorld はデスクトップ OS 上のタスクに特化。GAIA は Web/PDF/画像など外部ツール協調の複合タスクを対象とする
- 「GAIA」の名称衝突：Google の天文観測衛星プロジェクト（ESA Gaia）、各社フレームワーク等と同名。本書では Meta + Hugging Face 共同のベンチマークを指す

## 出典メモ

- Mialon et al., "GAIA: a benchmark for General AI Assistants" (2023) — arXiv:2311.12983 — checked 2026-04-30
- huggingface.co/datasets/gaia-benchmark/GAIA — checked 2026-04-30


## 備考

- 公開時スコア（2023 年末）：GPT-4 約 15%、人間約 92%
- 2025 年時点スコア：Claude 3.5 / GPT-4o などで 35〜40% 台、Manus 系エージェントで 60% 台（evaluation_date: 2026-04-30 時点の報告値）
- Level 3 は複数ツールを 5 ステップ以上組み合わせる問題が多く、現状でも AI にとって難易度が高いとされています
- AGI（J-1）議論の参照指標としても引用されることがあります
- **2026-05 時点のスコア状況**（評価フレームワークで大きく変動する点に注意）
  - 人間ベースライン: 約 92%
  - Princeton HAL（scaffold エージェント） + Claude Sonnet 4.5: 74.6%
  - BenchLM（モデル単体）: Claude Mythos Preview 52.3% / GPT-5.4 Pro 50.5%
  - Price Per Token（bare 評価）: GPT-5 Mini 44.8%
  - scaffold 有無で約 30 ポイント変動するため、モデル単体比較か agent 込みかを必ず明示する必要がある
