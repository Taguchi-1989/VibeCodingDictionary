---
id: E-4
title: HumanEval
title_reading: ヒューマンイーバル
category: benchmark
subtype: coding
experience_level: research_only
reader_level: 2
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2021
version_status: active
evaluation_date: 2026-04-29
related_terms:
  - pass@k
  - SWE-Bench
  - MBPP
  - Codex
  - Python
status: ready
---

# HumanEval

## tagline

AI が Python の関数を正しく書ける割合を測る古典ベンチマークです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

164 個の Python 関数生成課題で構成され、AI が書いたコードが隠しテストを通るかどうかで採点します。合格率は pass@1（1 回の出力で通る確率）という指標で表します。

## どこで出会うか

新モデルの発表記事や論文で「HumanEval スコア XX%」という形で登場します。上位モデルでは 90% 以上も多く飽和気味で、他ベンチとの比較で読むのが現実的です。

## メイン図

### 図の狙い

「問題文（docstring）を与えると AI が関数本体を埋める」という仕組みと、pass@1 の評価ループを 1 枚で示します。「点数が高いほど良い、でも飽和している」という読み方も添えます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: 関数の穴埋め → テスト実行 → pass@1 スコア
- 周辺の要素（3〜6 個）: docstring（問題文）／AI 生成コード／隠しテストケース／合否判定／164 問という規模感
- 関係の描き方: 左から右への一本線フロー。右端に「最新モデルは 90%+ 帯」のスコアバーを小さく添える

## 会話での使い方例

「HumanEval は飽和気味なので、SWE-Bench も合わせて見るのが現実的です。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI のコード生成力を pass@1 で数値化する基準です。

### 2. うれしさ

164 問という規模で、モデル間の比較が簡単にできます。

### 3. 注意点

Python 限定で、上位モデルでは 90%+ に達し飽和しています。

### 4. どこで役立つか

モデル選定の最初の足場、比較の共通言語として。

### 5. はじめに

pass@1 の意味と、164 問・Python 限定というスコープ。

### 6. 深掘り先

SWE-Bench、MBPP、pass@k

## 開発フローでの位置（必須）

1. モデル発表を確認 — HumanEval スコアが提示されることが多い
2. スコアの文脈を読む — Python 限定・飽和傾向を念頭に置く
3. 他ベンチと比較する — SWE-Bench や MBPP と並べて総合判断
4. 自分のタスクに近いか評価 — 関数単位か、リポジトリ規模かを区別する
5. 採用モデルを決める — 単一指標に頼らず複数スコアで判断

## 関連用語

- pass@k
- SWE-Bench
- MBPP
- Codex
- Python

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Python 評価なのに名前に Python が入らず分かりづらいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回調べていて初めて見ました
- 👍 良い点: Python コードを点数で評価できる点が良いです
- 👎 ダメな点: 飽和気味で、今の最低限が分かる程度でしょうか
- 👥 誰向けか: モデルの強さを最低限把握したい人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左から「問題文（docstring）アイコン」→「AI（ロボット頭部）が関数を書く」→「隠しテスト実行（✓/✗）」→「pass@1 スコア」の一本線フロー。右端にスコアバーを置き、90%+ 帯に「最新モデルが集まる帯」を斜線で示す
- 登場人物: AI エージェントの簡略アイコン 1 体、エンジニアが課題を渡す手のひら
- 吹き出し・心の声: AI の頭上に「この関数、こう書けばいいですね。」、テスト段階で「✓ 通過 / ✗ 不合格」を両方描く
- 中央に置くキーワード/ラベル: pass@1、164 問、Python 限定

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 吹き出し＋数字（モデル発表）
- Step 2 のアイコン/絵柄: 拡大鏡（スコアの文脈を読む）
- Step 3 のアイコン/絵柄: 比較表（他ベンチと並べる）
- Step 4 のアイコン/絵柄: ふるい（自分のタスクに近いか）
- Step 5 のアイコン/絵柄: ✓ チェック（採用モデル決定）
- 矢印: 発表 → 読む → 比較 → 評価 → 決定

## コミュニティ補完メモ

- SWE-Bench（E-1）との住み分け：HumanEval は「単一関数の穴埋め」、SWE-Bench は「実リポジトリへのパッチ作成」。難度・スコープともに別物として読む
- MBPP は HumanEval の後継候補として登場した別セット。両者の違いは問題数・難度・出典の違い（Google Research 製）
- Codex（OpenAI の初期コード特化モデル）の評価用に作られた経緯が背景知識として重要。2021 年発表の古典という位置づけ

## 出典メモ

- github.com/openai/human-eval — checked 2026-04-29
- arXiv:2107.03374 "Evaluating Large Language Models Trained on Code" — checked 2026-04-29

## 備考

- HumanEval は 2021 年発表の古典ベンチで、Codex 評価のために作られた
- 最新モデルでは 90%+ を達成するものが多く、「飽和」が議論される段階にある
- Python 限定という制約が実務評価の参考値としての限界でもある
- 後継として MBPP、難度の高い実務向けとして SWE-Bench が存在する
