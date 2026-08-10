---
id: F-47
title: フロントエンド／バックエンド
title_reading:
category: term_tool
subtype: architecture
experience_level: partial
reader_level: 1-2
importance: B
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status:
pricing_note:
evaluation_date: 2026-08-10
related_terms:
  - API
  - React
  - Next.js
  - Supabase
  - デプロイ
status: needs_review
---

# フロントエンド／バックエンド

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

画面を作る役割と、データや処理を支える役割に分けた開発の呼び方です。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

フロントエンドは利用者が見て触る画面側を担当し、バックエンドはサーバー側でデータの保存・計算・認証などの裏方を担当します。両者はAPIでつながり、画面側から情報を頼んで受け取ります。

## どこで出会うか

AIに開発を頼むとき、フロントエンドの見た目の話かバックエンドの処理の話かを分けて伝えると意図が通ります。個人開発ではSupabaseのように裏側をまるごと任せる選択もあります。

## メイン図

### 図の狙い

画面側と裏側が別の役割で、境界にAPIという窓口があることを一目で伝えます。


## 会話での使い方例

「その機能はフロントエンドの見た目、それともバックエンドの処理ですか？」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

画面側の役割と、データを扱う裏側の役割を分けて呼ぶ言葉です。


### 2. うれしさ

担当範囲がはっきりし、AIへの依頼も分担しやすくなります。


### 3. 注意点

境界のAPI設計を誤ると、両者の連携がずれます。


### 4. どこで役立つか

画面設計や機能実装をAIに相談するときに使います。


### 5. はじめに

自分が触る画面はどちら側かを意識してみます。


### 6. 深掘り先

API、フルスタック、Supabase


## 開発フローでの位置（必須）

1. 要件整理 — 画面機能と裏側のデータ処理を分けて洗い出します。
2. フロントエンド実装 — 画面のレイアウトや操作感を作り込みます。
3. バックエンド実装 — データの保存・計算・認証を用意します。
4. API接続確認 — 画面と裏側のやり取りが動くか確かめます。


## 関連用語

- API
- React
- Next.js
- Supabase
- デプロイ


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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 画面（左＝フロントエンド）とサーバー（右＝バックエンド）を左右に対比配置し、中央の境界線上に「API」という橋・窓口のアイコンを描く。左右の色や質感を変えて役割の違いを視覚化する
- 登場人物: 左側でボタンを押す利用者、右側でデータを管理するサーバー役のキャラクター（擬人化 or エンジニア）
- 吹き出し・心の声: 利用者「このデータちょうだい」→ 中央の API を通って → サーバー役「はい、これです」と返す。境界が API であることが吹き出しの経路で分かるようにする
- 中央に置くキーワード/ラベル: 「API」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: メモ・付箋で要件を左右に仕分けるイラスト
- Step 2 のアイコン/絵柄: 画面・ボタンのワイヤーフレーム
- Step 3 のアイコン/絵柄: サーバー・データベースのアイコン
- Step 4 のアイコン/絵柄: 左右をつなぐ矢印と API のラベル


## コミュニティ補完メモ

- F-213 API との住み分け：本エントリは境界としての API に触れるだけで、リクエスト/レスポンスの形式やエンドポイントの詳細は F-213 に譲る
- F-18 フレームワーク／ライブラリ との住み分け：F-18 はツールの種類の軸、本エントリは役割分担の軸で、直交する整理として並べられる
- B-29 Supabase との住み分け：本エントリは「裏側を任せる選択肢がある」という位置づけの一言に留め、機能詳細は B-29 に譲る

## 出典メモ

- MDN「Web 標準の学習を始める」https://developer.mozilla.org/ja/docs/Learn_web_development/Getting_started/Web_standards — checked 2026-08-10
- MDN「サーバーサイドの学習」https://developer.mozilla.org/ja/docs/Learn_web_development/Extensions/Server-side — checked 2026-08-10


## 備考

API（F-213）の説明は最小限に留め、詳細は F-213 側に委ねています。
