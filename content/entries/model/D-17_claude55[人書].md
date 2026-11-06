---
id: D-17
title: Claude 5.5 系
title_reading: クロード ゴテンゴ系
category: model
subtype: anthropic
experience_level: hands_on
reader_level: 2-3
importance: A
figure_type: comparison
page_layout: spread_v1
start_date: 2026-09-22
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-11-06
last_audited: 2026-11-06
related_terms:
  - effort レベル
  - Fast mode
  - Claude Fable / Mythos
  - Claude 5 系
status: needs_review
---

# Claude 5.5 系

## tagline

Claude 第 5.5 世代。3 モデルが 2026 年秋に出そろいました。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Opus 5.5・Sonnet 5.5・Haiku 5.5 の 3 段で、同じ性能帯を安く、速く使えます。文脈は 3 モデル共通で 100 万トークンです。考える量の強弱（effort）も選べます。

## どこで出会うか

Claude Code や Claude.ai、API で出会う世代です。2026-09-22 から 10-07 にかけて 3 段がそろい、公式は「迷ったらまず Opus 5.5」と案内しています。Opus が最上位ではなく、出発点になりました。

## メイン図

### 図の狙い

公開日順に 3 枚のカードを並べ、短期間で 3 段がそろったことと、価格・速さの違いを掴んでもらいます。

### B. 登場シーン（figure_type: comparison）

- シーン1: Opus 5.5（2026-09-22 公開）— 入力 $4 / 出力 $20。Fast mode は $8 / $40（2026-11 時点）
- シーン2: Sonnet 5.5（2026-09-28 公開）— 入力 $2 / 出力 $10。Sonnet 5 より 30% 以上速い
- シーン3: Haiku 5.5（2026-10-07 公開）— 入力 $0.10 / 出力 $0.50（プロンプト 10 万トークンまで）
- 共通値: 文脈 100 万トークン・出力上限 12.8 万トークン
- 並べる基準: 公開日順

## 会話での使い方例

「Sonnet 5.5 は effort の既定が high ですが、Opus 5.5 は medium です。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Opus・Sonnet・Haiku の 3 段が出そろった世代です。

### 2. うれしさ

同じ性能帯が、安く速く使えるようになりました。

### 3. 注意点

effort の既定値がモデルごとに違います。

### 4. どこで役立つか

Claude Code の日常作業から軽い振り分けまでです。

### 5. はじめに

迷ったらまず Opus 5.5 から試します。

### 6. 深掘り先

effort レベル、Fast mode、Claude Code

## 開発フローでの位置（必須）

1. 仕事の重さを見る — 難しい設計か、軽い振り分けかを判断します
2. 段を選ぶ — 迷ったらまず Opus 5.5 から始めます
3. effort を決める — 既定値がモデルごとに違う点に注意します
4. 速さが要るなら — Opus に限り Fast mode を検討します
5. 結果を見て調整 — 足りなければ Fable（D-16）へ進みます

## 関連用語

- effort レベル
- Fast mode
- Claude Fable / Mythos
- Claude 5 系

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 横に 3 枚のカード（Opus 5.5／Sonnet 5.5／Haiku 5.5）を公開日順に並べ、日付（2026-09-22／09-28／10-07）と価格（2026-11 時点）を注記。Opus カードには「Fast mode 最大 2.5 倍速」の高速レーン札。下部に共通値（文脈 100 万トークン）の帯
- 登場人物: 著者キャラクターが 3 枚のカードの前で、effort のダイヤルを回している
- 吹き出し・心の声: 著者「迷ったらまず Opus 5.5。軽い仕事は Haiku に回そう」
- 中央に置くキーワード/ラベル: Claude 5.5 系＝2026 年秋にそろった 3 段

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 天秤アイコン（重さを見る）
- Step 2: 3 つのバッジ（Opus／Sonnet／Haiku）
- Step 3: effort ダイヤル（low〜max）
- Step 4: 高速レーンの料金所（Fast mode）
- Step 5: 上向き矢印（Fable への切り上げ）

## コミュニティ補完メモ

- 前の世代は D-15 Claude 5 系、Opus の上の段は D-16 Claude Fable / Mythos が担当します。本エントリは 5.5 世代の 3 モデルに絞ります。
- effort は G-9、Fast mode は G-52 が担当します。本エントリでは「既定値がモデルごとに違う」点だけを書きます。
- preserved thinking（Opus 5.5 から）は J-152 蒸留攻撃が担当します。
- Artificial Analysis Intelligence Index（E-52）での位置づけも同エントリを参照してください。

## 出典メモ

- Anthropic「Claude Opus 5.5」https://www.anthropic.com/claude-opus-5-5 — checked 2026-11-06
- Anthropic「Claude Sonnet 5.5」https://www.anthropic.com/claude-sonnet-5-5 — checked 2026-11-06
- Anthropic「Claude Haiku 5.5」https://www.anthropic.com/claude-haiku-5-5 — checked 2026-11-06
- Anthropic「Models overview」https://platform.claude.com/docs/en/about-claude/models/overview — checked 2026-11-06

## 備考

モデル名・価格・提供状況は時変情報です。Opus 5.5 は公式が「ほとんどの仕事で Fable 5.1 と同等の水準、Opus 5 より約 40% 安く回せる」と説明し、キャッシュ読み出しは $0.20、Fast mode は最大 2.5 倍速で $8 / $40、effort は low / medium / high / xhigh / max の 5 段で既定は medium、思考は常時オンで無効化できません。Sonnet 5.5 は Sonnet 5 とトークン単価が同じで、少ないトークンで済むため 1 タスクあたり最大 30% 安く、知識労働の評価 GDPval-AA では Opus 5.5 とほぼ並ぶ（Elo 1844 対 1846）と説明され、effort の既定は high です。Haiku 5.5 はプロンプト 10 万トークンを超えると $0.50 / $2.50 になり、Haiku 4.5（$1 / $5）より平均約 75% 安く、Haiku で初めて effort を調整でき、既定は medium です。3 モデル共通で、信頼できる知識の終点は 2026-06 です。2026-10-12 の蒸留対策で導入された preserved thinking は Fable 5.1 と Opus 5.5 から対象です。Artificial Analysis Intelligence Index v5（2026-11 初旬）では Opus 5.5（max）が 59 で 2 位と報じられています（二次情報、E-52 参照）。後続世代の固有名は、次回の世代交代時に追記します。なお、ブリーフは「3 週間で 3 段がそろった」と記していましたが、公開日（2026-09-22〜10-07）から数えると約 2 週間のため、本文は日付で記述しています。
