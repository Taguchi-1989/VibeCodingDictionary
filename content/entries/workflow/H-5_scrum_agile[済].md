---
id: H-5
title: Scrum / Agile
title_reading: スクラム アジャイル
category: workflow
subtype: methodology
experience_level: partial
reader_level: 2-3
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - TDD
  - コードレビュー
  - Git Flow
  - DevOps
status: ready
---

# Scrum / Agile

## tagline

短い反復で動くソフトを届け続ける開発の価値観と型です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Agile は短い反復・変化への追従を柱とする価値観です。Scrum はその代表的な型で、Sprint 単位で動くものを届ける枠組みを指します。

## どこで出会うか

チームの朝会（Daily Stand-up）や Sprint Review の案内・Backlog 管理ツールで目にします。AI ツール導入でも「1 Sprint 試して Retrospective で評価する」使い方と相性が良いです。

## メイン図

### 図の狙い

Agile が上位概念（価値観）で Scrum がその具体的な型の 1 つである、という包含関係を示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Agile（価値観・宣言）
- 周辺の要素（3〜6個）: Scrum / Kanban / XP / SAFe
- 関係の描き方（矢印・包含・比較）: Agile を大きな円で囲み、Scrum・Kanban・XP を内包する小円として配置。SAFe は Scrum の外に「大規模版」として接続


## 会話での使い方例

「Sprint 単位で AI を試し、Retrospective で振り返ると納得感が高いです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

短い反復で動くものを届け、変化に追従する開発の型です。

### 2. うれしさ

Sprint ごとに成果を確認でき、方向修正が早くできます。

### 3. 注意点

Agile と Scrum は別物で、Scrum は Agile の型の 1 つです。

### 4. どこで役立つか

要件が変わりやすいプロダクト開発や AI 導入の実験に有効です。

### 5. はじめに

Agile が上位概念、Scrum はその具体的な実装の型と押さえます。

### 6. 深掘り先

Kanban、XP、SAFe、DevOps


## 開発フローでの位置（必須）

1. Sprint 計画 — Backlog から今回届けるものを選び、Sprint 目標を決めます。
2. 開発と Daily Stand-up — 毎日 15 分の朝会で進捗と詰まりを共有します。
3. Sprint Review — Sprint 終了時に動くものをステークホルダーに見せます。
4. Retrospective — チームで振り返り、次の Sprint の改善点を決めます。


## 関連用語

- TDD
- コードレビュー
- Git Flow
- DevOps


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- ひとり開発だとそのまま当てはめづらい概念です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: SE の人が組織で回すやり方、という印象です
- 👍 良い点: 従来のエンジニアリングスタイルだと、進め方の効率が上がっていく仕組みです
- 👎 ダメな点: AI エージェントで自動化できる工程を人手で回す必要が薄い印象です。
- 👥 誰向けか: AI エージェントを前提に置かない、従来型のチーム開発をする人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: Agile を大きな円として中心に置き、その中に Scrum・Kanban・XP の 3 つの小円を並べる。SAFe は Scrum の円の外に接続線で「大規模スケーリング版」として示す。
- 登場人物（いれば）: チームメンバー 1 名（ホワイトボードの前に立つ人物）
- 吹き出し・心の声: 「Scrum は Agile の型の 1 つ、上下関係じゃなくて包含関係です」
- 中央に置くキーワード/ラベル: Agile / Scrum

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: カレンダー＋リスト（Sprint 計画）
- Step 2 のアイコン/絵柄: 人物 3 名が輪になる（Daily Stand-up）
- Step 3 のアイコン/絵柄: モニター画面（Sprint Review）
- Step 4 のアイコン/絵柄: 矢印が円を描く（Retrospective）
- 矢印で示す流れの意図: 4 ステップが循環することを示す


## コミュニティ補完メモ

- H-1 TDD との住み分け: TDD はコードレベルの品質実践、Scrum / Agile はチーム・プロセス全体の枠組みで重複しない。「TDD を Scrum の Sprint の中で行う」という関係。
- H-6 Git Flow との住み分け: Git Flow はブランチ戦略、Scrum はチームの進め方の型。両立できる。
- H-8 DevOps との住み分け: DevOps は開発と運用の継続的連携、Agile はチーム内の反復開発の価値観。補完関係。
- Kanban は Agile の別実装として軽く触れるにとどめる（別エントリで扱う場合の準備）。


## 出典メモ

- Agile Manifesto（agilemanifesto.org）— checked 2026-04-30
- Scrum Guide 2020（scrumguides.org）— checked 2026-04-30


## 備考

- Agile と Scrum の上下関係（包含関係）は非エンジニアが最も混乱する点。tagline と 5. はじめに で意識的に繰り返した。
- SAFe（Scaled Agile Framework）は大規模組織向けのスケーリング枠組みで詳細は別エントリ候補。
- Scrumban（Scrum + Kanban の組み合わせ）は本エントリのスコープ外で、コミュニティ補完メモに記載。
