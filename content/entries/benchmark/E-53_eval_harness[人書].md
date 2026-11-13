---
id: E-53
title: 評価ハーネス
title_reading: ひょうかハーネス
category: benchmark
subtype: general
experience_level: research_only
reader_level: 3
importance: C
figure_type: workflow
page_layout: spread_v1
version_status: active
pricing_note: free
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - Terminal-Bench
  - effort レベル
  - ハーネスエンジニアリング
  - Evals
status: needs_review
---

# 評価ハーネス

## tagline

ベンチマークを動かして採点する実行基盤です。問題集とは別物です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

モデルやエージェントに問題を渡し、隔離した環境で動かして、採点と記録までを行う仕組みです。Harbor や Inspect AI が代表例で、問題集そのものではなく試験会場にあたります。

## どこで出会うか

ベンチマークの公式手順に「Harbor で実行」などと書かれています。ツールの有無や考える量の設定で点が変わるため、発表記事のスコア注記でも目にします。

## メイン図

### 図の狙い

問題集と試験会場（ハーネス）は別物で、会場の設定が変わると同じモデルでも点が動くことを見せます。

### C. 概念図（figure_type: workflow）

- 左から右へ: 問題集 → ハーネス（隔離環境で実行）→ 採点 → 順位表
- ハーネスの箱に設定ダイヤル（ツール／effort／時間・メモリ）を付ける
- 下に例示ラベル「2026-11 時点: Terminal-Bench 4.0 は Harbor 上で実行」

## 会話での使い方例

「Terminal-Bench は Harbor で走らせるので、設定で点が動きますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

問題を渡して動かし、採点して記録します。

### 2. うれしさ

誰でも同じ手順で試験を再現しやすくなります。

### 3. 注意点

設定が違うと、同じモデルでも点が変わります。

### 4. どこで役立つか

スコア記事を読むとき、条件の確認に役立ちます。

### 5. はじめに

点数の横にある「ツールあり／なし」を読むことです。

### 6. 深掘り先

Terminal-Bench、effort レベル、ハーネスエンジニアリング

## 開発フローでの位置（必須）

1. 問題集を選ぶ — 測りたい力に合う試験を決める
2. 会場を整える — ハーネスで隔離環境と設定を用意する
3. 実行する — モデルやエージェントに問題を解かせる
4. 採点・記録 — 結果とログを同じ形式で残す
5. 条件と一緒に読む — 点数を設定とセットで比べる

## 関連用語

- Terminal-Bench
- effort レベル
- ハーネスエンジニアリング
- Evals

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 
- 
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 
- 👍 良い点: 
- 👎 ダメな点: 
- 👥 誰向けか: 
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 左から問題集の本、会場の建物（ハーネス）、採点の赤ペン、順位表の板。会場の屋根に設定ダイヤル 3 つ（ツール／effort／時間・メモリ）
- 登場人物（いれば）: 読者キャラ（非エンジニア）が会場の外から順位表を見ている
- 吹き出し・心の声: 読者「同じモデルなのに、会場が違うと点が違う？」／ダイヤル脇「設定で点が変わるよ」
- 中央に置くキーワード/ラベル: 問題集 ≠ 試験会場 ／ 例示「2026-11 時点: Terminal-Bench 4.0 は Harbor 上で実行」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 問題集の本棚
- Step 2 のアイコン/絵柄: 箱（隔離環境）とダイヤル
- Step 3 のアイコン/絵柄: 走るロボット
- Step 4 のアイコン/絵柄: 赤ペンとログ
- Step 5 のアイコン/絵柄: 点数に付く注釈タグ


## コミュニティ補完メモ

- E-3 Terminal-Bench との住み分け：Terminal-Bench は問題集、Harbor はそれを動かす会場。4.0 は Harbor の上に作られたとされる
- E-52 Artificial Analysis Intelligence Index との関係：合成点を読むときも、どの設定で測ったかが前提になる
- G-9 effort レベルとの関係：考える量の設定そのものが、ハーネス側の条件として点に効く
- J-106 ハーネスエンジニアリングとの住み分け：J-106 は AI エージェントを動かす器の設計。こちらは「測る」ための器。同じ「ハーネス」でも用途が違う
- G-50 Evals との住み分け：Evals は自分の仕事向けの評価をつくる話。こちらは公開ベンチマークを走らせる道具

## 出典メモ

- tbench.ai／harborframework.com（検索経由・二次情報を含む）— checked 2026-11-13
- Inspect AI（英国 AI Security Institute 公開の評価フレームワーク、検索経由）— checked 2026-11-13

## 備考

- **一次未確認**：Harbor・Inspect AI・Terminal-Bench 4.0 の情報は環境のネットワーク制限で直接取得できず、検索経由です（2026-11-13 時点）
- Harbor：コンテナ環境でエージェントやモデルを評価・改善する枠組み。Terminal-Bench 4.0 は `harbor run -d terminal-bench/terminal-bench@4.0.0` で実行するとされる
- Inspect AI の互換ラッパー（`inspect_harbor`）経由でベンチマークを読み込む研究例がある
- Terminal-Bench 4.0（2026-08-28）は課題ごとの時間・CPU・メモリを較正し直した版とされる。Humanity's Last Exam が「ツールあり」「ツールなし」で別の数字になる例もある
- Anthropic の Claude Code 文書も、考える側（モデル）と実行する側（Claude Code 本体＝ハーネス）を分けて説明している
- 本文は「会場」の比喩で統一。具体的な製品の版・コマンドは時変情報のため誌面に出さない
