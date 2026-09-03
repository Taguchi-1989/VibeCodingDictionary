---
id: E-51
title: LMSYS Arena
title_reading: エルエムシスアリーナ
category: benchmark
subtype: general
experience_level: research_only
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2023
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Chatbot Arena
  - ELO レーティング
  - SWE-Bench Verified
  - Claude
status: ready
---

# LMSYS Arena

## tagline

Chatbot Arena を立ち上げた研究グループ、およびそのプラットフォームの総称です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

LMSYS が運営する人手投票型モデル評価基盤です。匿名 2 モデルに同じ質問を投げて好みの回答を選び、ELO レーティングでリーダーボードを公開します。

## どこで出会うか

新モデル記事で「LMSYS ランキングで上位」と紹介される場面が典型です。「LMSYS Arena」「LMArena」「Chatbot Arena」が混在しがちです。

## メイン図

### 図の狙い

「LMSYS という研究グループが立ち上げた Chatbot Arena が、LMArena として独立した」経緯を時系列で示します。

### B. 登場シーン（figure_type: structure）

- シーン1: LMSYS（2023 年）が Chatbot Arena を公開。UC Berkeley 発の研究基盤として注目を集める
- シーン2: Vision Arena・Copilot Arena など派生プラットフォームが追加される
- シーン3: 2024 年に LMArena として独立運営に移行。lmarena.ai が窓口になる
- 並べる基準: 時系列（設立 → 拡張 → 独立）

## 会話での使い方例

「LMSYS Arena で Gemini 2.5 Pro が 1 位に上がってきました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

人手投票の ELO でモデルの「体感品質」を順位化します。

### 2. うれしさ

数値ベンチと違い、実用文脈の印象がスコアに反映されます。

### 3. 注意点

LMSYS・Chatbot Arena・LMArena は別名で同系列のサービスです。

### 4. どこで役立つか

モデル選定時に「世間の体感評価」を一覧で確認できます。

### 5. はじめに

運営主体 LMSYS と Chatbot Arena（E-50）の関係を把握するのが出発点です。

### 6. 深掘り先

Chatbot Arena、ELO レーティング、SWE-Bench Verified

## 開発フローでの位置（必須）

1. 候補絞り込み — ランキングで体感評価を確認する
2. 名称照合 — 「LMSYS」「LMArena」「Chatbot Arena」は同系列と判断する
3. 派生 Arena — コーディングは Copilot Arena、画像は Vision Arena を参照
4. 自動ベンチ併用 — SWE-Bench Verified などと組み合わせて判断する

## 関連用語

- Chatbot Arena
- ELO レーティング
- SWE-Bench Verified
- Claude


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 順位は分かっても、点数差がモデル差にどれだけ効いているか掴めません。
- LMSYS・LMArena・Chatbot Arena など呼び名が混在して、同じ系列と気づきにくいです。
- 順位が週単位で入れ替わるため、最新を追わないと話題に乗り遅れます。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Chatbot Arena の時代から見ていて、統合や派生で動きが激しい印象です。
- 👍 良い点: 人の評価が入るため、定性的な使用感が反映されて選定の手がかりになります。
- 👎 ダメな点: 順位は分かっても点数差の意味が読み取りにくく、定量補完が要ります。
- 👥 誰向けか: 今どのモデルが強いか、最新の体感ランキングを追いたい人に向く指標です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左から「LMSYS（研究グループ）」→「Chatbot Arena（プラットフォーム）」→「LMArena（独立後）」という 3 段階の変遷を横並びで示す
- 登場人物: 研究者アイコン（LMSYS）1 名、画面を見るユーザー 1 名
- 吹き出し・心の声: 研究者「投票で体感を測ります」、ユーザー「同じ名前なのに URL が違う…」
- 中央に置くキーワード/ラベル: 「人手投票 × ELO」
- Before / After の場合の対比ポイント: 該当なし

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（ランキング確認）
- Step 2 のアイコン/絵柄: メモ帳＋名称ラベル（名称照合）
- Step 3 のアイコン/絵柄: 分岐矢印（派生 Arena 選択）
- Step 4 のアイコン/絵柄: グラフ 2 本（複数指標の比較）
- 矢印で示す流れの意図: ランキングで絞る → 名称混乱を解消 → 用途別 Arena を選ぶ → 自動採点と合わせて判断


## コミュニティ補完メモ

- E-50 Chatbot Arena との住み分け: E-50 は「仕組み（匿名対戦 → ELO → ランキング）」を中心に説明。E-51 は「運営主体の LMSYS、名称変遷（→ LMArena）、派生 Arena の存在」を補う。読者が両方を読めば全体像が揃う構成。
- 「LMSYS」の正式名は Large Model Systems Organization（UC Berkeley 主導の研究グループ）。本文では「UC Berkeley などの研究者が集まる LMSYS」に留め、正式組織名の展開は備考に移す。
- Copilot Arena はコーディング補完モデルの評価に特化した派生版。バイブコーディング読者に関連が高いため開発フロー Step 3 で言及。


## 出典メモ

- lmarena.ai — checked 2026-04-30
- LMSYS Org ブログ（lmsys.org/blog）— checked 2026-04-30
- arXiv:2403.04132（Chatbot Arena 原論文）— checked 2026-04-30


## 備考

- LMSYS の正式名: Large Model Systems Organization。本文では略称のまま使用し、ここに補記。
- 2024 年の独立分離は「LMSYS という研究グループの活動と、商業運営のプラットフォームを切り分ける」目的で行われた。本文ではこの経緯を 1 行に縮め、詳細はここに留める。
- 個別モデルの順位は時変情報のため本文に記載しない。
- **2026-05 時点のランキング状況**
  - Text 部門 #1: Claude Opus 4.6（Elo 1504）
  - 上位は Gemini 3.1 Pro Preview と Claude Opus 4.6 Thinking が 95% CI で同率タイ
  - 数学・推論カテゴリ: GPT-5 が Elo 1561 で最高
  - GPQA Diamond: Claude Mythos Preview 94.6% でハードサイエンス首位
  - フロンティア帯: GPT-5 / Claude Opus 4.6 / Gemini 3.1 Pro / Grok 4 / DeepSeek V3.2（Elo 1450-1561）
  - 投票数 600 万 + で運用。順位は週次で入れ替わるため、引用時は必ず日付を併記
  - Preview タグのモデルは CI が広く、Elo が 20-40 ポイント揺れることがあるため絶対視は避ける
