---
id: F-141
title: PlantUML
title_reading: プラントユーエムエル
category: term_tool
subtype: diagram
experience_level: partial
reader_level: 3-4
importance: E
figure_type: structure
page_layout: spread_v1
start_date: 2009-01-01
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Mermaid
  - Markdown
  - SVG
  - VS Code
status: ready
---

# PlantUML

## tagline

テキストで UML 図を描くオープンソースツールです。クラス図・シーケンス図などを記法で表現します。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`@startuml` と `@enduml` で囲んだ記述から、シーケンス図やクラス図などの UML 図を自動生成します。テキストで書けるため、Git でバージョン管理できます。

## どこで出会うか

AI に業務フローや設計を依頼すると PlantUML の記法で返ってくる場面があります。VS Code 拡張や公式 Web（PlantUML Server）でそのまま描画できます。

## メイン図

### 図の狙い

テキスト記法と生成される図の対応関係を示し、「書いたら図になる」という感覚を掴んでもらいます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 手で図を描いており、仕様変更のたびに描き直しが必要
  - 視覚要素（コード or 概念）: PowerPoint の図、修正が煩雑
  - つまずき: 図の更新が面倒で古い設計図が放置される
- After
  - 状況: PlantUML の記法をテキストで書いて図を自動生成
  - 視覚要素: `Alice -> Bob: 承認依頼` の 1 行でシーケンスが表示される
  - うれしさ: テキスト修正だけで図が最新状態を保てます


## 会話での使い方例

「複雑な業務フローは PlantUML を Claude に書かせると意外ときれいです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

テキスト記法から UML 図を自動生成するツールです。

### 2. うれしさ

テキストで管理できるので Git での差分管理が可能です。

### 3. 注意点

ローカル描画には Java と Graphviz の両方が必要です。

### 4. どこで役立つか

業務システムの設計書や仕様共有の場面に向きます。

### 5. はじめに

まず PlantUML Server の Web 描画から試すと導入が楽です。

### 6. 深掘り先

Mermaid、VS Code 拡張、Graphviz


## 開発フローでの位置（必須）

1. 設計意図を整理する — 図にしたい構造や処理の流れを決めます
2. AI に記法を生成させる — Claude などに PlantUML で書くよう指示します
3. Web または拡張で描画する — PlantUML Server か VS Code 拡張で確認します
4. テキストを Git で管理する — 仕様変更は記法を修正するだけで図に反映されます


## 関連用語

- Mermaid
- Markdown
- SVG
- VS Code


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Mermaid より表現力は高いものの、AI の学習量が少なくエラーが頻発します。
- 間違った構文が返ってきて、修正地獄になることがあります。
- 学習量や GitHub の対応差から、日常用途は Mermaid に寄せたほうが楽です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 表現力が高く、図のアーティストに出会ったような感動がありました。
- 👍 良い点: アーキテクトとして使い込みたくなる機能がたくさん揃っています。
- 👎 ダメな点: マイナーで AI 学習量が少なく、任せきりにできず手直しが必要です。
- 👥 誰向けか: どうしても PlantUML を使いたい人向けで、AI 任せは難しいです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左に PlantUML テキスト記法、右に生成されたシーケンス図。矢印でつなぐ
- 登場人物: エンジニアが画面を見ている人物（1名）
- 吹き出し・心の声: 「テキスト書いたら図になった！」
- 中央に置くキーワード/ラベル: PlantUML

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: メモ帳アイコン（設計整理）
- Step 2 のアイコン/絵柄: AI チャットアイコン（記法生成）
- Step 3 のアイコン/絵柄: ブラウザ／エディタアイコン（描画確認）
- Step 4 のアイコン/絵柄: Git ブランチアイコン（バージョン管理）
- 矢印で示す流れの意図: テキスト起点で図が生まれ、そのまま管理に乗る流れ


## コミュニティ補完メモ

- Mermaid（F-140）との住み分け：Mermaid はブラウザだけで動く手軽さが強み。PlantUML は要素数・属性量が多い複雑な業務系図に向く。AI 出力で両方出てくるため、読者は「どちらを選ぶか」を知れれば十分
- VS Code（F-30）との関係：PlantUML 拡張を入れると VS Code 上でプレビューが可能。拡張の詳細は F-30 に委ねる

## 出典メモ

- [plantuml.com](https://plantuml.com/) — checked 2026-04-30
- [VS Code 拡張 jebbs.plantuml](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml) — checked 2026-04-30

## 備考

- ローカル実行の前提：Java（JRE 8 以上）と Graphviz が必要。導入コストがあるため、初学者には [PlantUML Server](https://www.plantuml.com/plantuml/uml/) から始めることを薦める
- Graphviz 不要な図種：シーケンス図・アクティビティ図（新構文）・マインドマップは Graphviz なしで描画できる場合がある（バージョン依存）
- **2026-05 時点の状況メモ**：Mermaid は GitHub・Notion のネイティブレンダリング対応で日常用途の優位が深まっており、LLM の学習量も Mermaid のほうが多く一発成功率が高めとされる傾向。PlantUML は本格 UML や複雑な企業システム設計では依然有効で、用途で選び分けるのが現実的。AI 構文精度の差は両者とも改善が続いているため、半年〜1 年ごとに再評価が必要
