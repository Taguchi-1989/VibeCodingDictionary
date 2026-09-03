---
id: F-154
title: OSS
title_reading: オーエスエス
category: term_tool
subtype: license
experience_level: research_only
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
  - Apache 2.0
  - GPL
  - Creative Commons
  - Mistral
status: ready
---

# OSS

## tagline

Open Source Software の略。ソースコードが公開され、再利用・改変・再配布が自由なソフトウェアです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ライセンス条件を守れば、誰でもソースコードを入手・改変・再配布できます。MIT / Apache 2.0（F-151）/ GPL（F-152）などが条件を定め、商用利用も原則可能です。


## どこで出会うか

GitHub のライブラリを npm や pip で入れるとき、たいてい OSS に触れています。Llama / Mistral などオープンウェイトモデルも OSS の仕組みで配布されています。


## メイン図

### 図の狙い

「無料 ＝ OSS」という誤解を解き、ソースコードの公開・改変自由という本質を掴んでもらう。


### C. 概念図（figure_type: structure）

- 中心に置く概念: OSS（Open Source Software）
- 周辺の要素: MIT ライセンス / Apache 2.0 / GPL / Linux カーネル / Python / Llama
- 関係の描き方: 中心から放射状に矢印、ライセンスと採用例を色分け


## 会話での使い方例

「この MCP server は OSS なので、社内向けに改造して動かしています。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ソースコードを公開し、自由な改変と再配布を認める仕組みです。

### 2. うれしさ

既存ライブラリを改造して使えるため、開発コストを抑えられます。

### 3. 注意点

無料と混同しがちですが、本質はソースコードの公開・自由改変です。

### 4. どこで役立つか

ローカル LLM の導入や社内ツール改造で実感しやすい仕組みです。

### 5. はじめに

ライセンス名と「改変・再配布の可否」を確認する習慣が入口です。

### 6. 深掘り先

Apache 2.0、GPL、Creative Commons


## 開発フローでの位置（必須）

1. 依存ライブラリ選定 — npm / pip で OSS ライブラリを探し、ライセンスを確認します
2. ライセンス確認 — MIT / Apache 2.0 / GPL の違いを見て商用・改変の可否を判断します
3. ローカル LLM 導入 — Llama / Mistral などオープンウェイトモデルをダウンロードして起動します
4. 社内改造・再配布 — ライセンス条件を守りながらフォーク・改変・社内展開を行います


## 関連用語

- Apache 2.0
- GPL
- Creative Commons
- Mistral


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- OSS という言葉を普段使っていても、開発していない人には全く伝わりません。
- 著作権感度がある人には通じても、課題認識のない人とは話がかみ合いません。
- 本当に OSS なのか、グレーな範囲の見分けが難しい場面があります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 自分のシステムが売れる可能性に繋がる仕組みだと知ってワクワクしました。
- 👍 良い点: 規約を守れば実際に商用利用でき、製品として売れる道が開けます。
- 👎 ダメな点: グレーな部分を踏むと損害賠償の話に発展する可能性があり、注意が要ります。
- 👥 誰向けか: アプリ開発する人には必須のリテラシーで、長い目で身につけたい知識です。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「OSS」ラベルを置き、左側にライセンス群（MIT / Apache 2.0 / GPL）、右側に採用ソフト群（Linux / Python / Llama）を放射状に配置
- 登場人物: 開発者（若い男性）が中央ラベルを指差している
- 吹き出し・心の声: 「ライセンス確認してから使おう」
- 中央に置くキーワード/ラベル: OSS（Open Source Software）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（ライブラリ検索）
- Step 2 のアイコン/絵柄: ドキュメント＋チェックマーク（ライセンス確認）
- Step 3 のアイコン/絵柄: ダウンロード矢印（モデル取得）
- Step 4 のアイコン/絵柄: レンチ（改造・展開）
- 矢印で示す流れの意図: 選定 → 確認 → 取得 → 展開の順序

## コミュニティ補完メモ

- Apache 2.0（F-151）との住み分け: F-151 は Apache ライセンスの条件詳細を扱う。本エントリは OSS 全体の概念と「無料≠OSS」の誤解解消が主眼。
- GPL（F-152）との住み分け: F-152 はコピーレフト条件（改変版も GPL 必須）の詳細を扱う。本エントリではライセンス種別の一例として列挙するにとどめる。
- Creative Commons（F-153）との住み分け: F-153 はドキュメント・画像・コンテンツ向けの CC ライセンスを扱う。本エントリでは「ドキュメント向けライセンスも存在する」という補足程度。
- Mistral（D-41）との住み分け: D-41 はモデルのスペック・性能を扱う。本エントリではオープンウェイト配布の「仕組み」文脈でのみ言及。


## 出典メモ

- Open Source Initiative — Open Source Definition — <https://opensource.org/osd> — checked 2026-04-30
- OSI Approved Licenses 一覧 — <https://opensource.org/licenses> — checked 2026-04-30


## 備考

- 「オープンウェイト」（Llama / Mistral 等）は厳密には OSS と区別されることもある。重みファイルは公開されるがライセンス条件が独自の場合も多い。誌面では「OSS の仕組みが基盤にある」と抽象的に表現し、厳密な差異は備考に留める。
- OSS の定義機関は Open Source Initiative（OSI）。FSF（Free Software Foundation）の「自由なソフトウェア」とは思想的に重なるが別組織。誌面ではスコープを絞り OSI の OSS 定義に統一。
