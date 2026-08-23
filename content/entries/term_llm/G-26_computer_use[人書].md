---
id: G-26
title: Computer Use
title_reading: コンピューターユース
category: term_llm
subtype: control
experience_level: research_only
reader_level: 3-4
importance: C
figure_type: workflow
page_layout: spread_v1
start_date: 2024-10-22
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-08-10
related_terms:
  - AI エージェント
  - Tool Use
  - Claude Cowork
  - Permission
status: needs_review
---

# Computer Use

## tagline

AIにスクリーンショットを見せ、マウスとキーボードで画面操作させる使い方です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

AI が画面のスクリーンショットを見ながら、人と同じようにクリックやドラッグ、文字入力を自分で判断して行います。API 連携がない古いシステムの操作にも向いています。

## どこで出会うか

AI エージェント（G-49）の使い方の1つです。Claude Code や Claude Cowork から Mac・Windows の画面操作を任せる場面で出会います。

## メイン図

### 図の狙い

画面を見て操作を返す「観察→操作」のループを 1 枚で見せる。

## 会話での使い方例

「Computer Use を使えば、古い社内システムも操作を任せられます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

画面を見て人と同じように操作を代行します。

### 2. うれしさ

専用の API がない古いソフトも自動化できます。

### 3. 注意点

誤操作や情報持ち出しのリスクがあります。

### 4. どこで役立つか

入力フォームが多い定型作業の自動化で役立ちます。

### 5. はじめに

操作範囲を絞った環境で小さく試すことです。

### 6. 深掘り先

AI エージェント、Permission、Claude Cowork


## 開発フローでの位置（必須）

1. 環境を用意する — 操作範囲を絞った仮想環境やブラウザを用意します。
2. 画面を読み取る — スクリーンショットで現在の画面状態を確認します。
3. 操作を実行する — マウス操作とキー入力を出力し、実際に操作します。
4. 結果を確認する — 次のスクリーンショットを見て次の行動を判断します。
5. 重要操作は承認する — ファイル削除や送信など重い操作は人が確認します。


## 関連用語

- AI エージェント
- Tool Use
- Claude Cowork
- Permission


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

### メイン図（左ページ中段 / figure_type: flow）

- 描く内容: 画面のスクリーンショットを AI が見て、マウス操作の指示を返し、また次のスクリーンショットを確認する円環のフロー
- 登場人物（いれば）: 画面の前で AI の操作を手を出さずに見守る利用者
- 吹き出し・心の声: 利用者「クリックする場所まで自分で見つけてくれるんだ」／AI「次はこのボタンを押します」
- 中央に置くキーワード/ラベル: スクリーンショット → 判断 → クリック/入力

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 仮想デスクトップの枠アイコン
- Step 2 のアイコン/絵柄: カメラ/スクリーンショットアイコン
- Step 3 のアイコン/絵柄: マウスカーソルとキーボードアイコン
- Step 4 のアイコン/絵柄: 虫眼鏡で画面を確認するアイコン
- Step 5 のアイコン/絵柄: 承認ボタンを押す手


## コミュニティ補完メモ

- G-49 AI エージェントとの住み分け: 本エントリはエージェントが「画面を見て操作する」という具体的な操作手段の 1 つに絞る。自律ループ自体の定義や一般論は G-49 に譲る。
- G-39 Permission との住み分け: 操作範囲を絞る・重要操作を人が承認するという運用は Permission の仕組みを前提とし、設定方法の詳細は G-39 に譲る。
- G-30 Tool Use との住み分け: マウス・キーボード操作に特化したツール呼び出しという位置づけで、ツール呼び出し全般の仕組みは G-30 に譲る。
- B-19 Claude Cowork との住み分け: Cowork というサービス自体の機能紹介は B-19 に譲り、本エントリは Computer Use という操作方式の説明に絞る。


## 出典メモ

- Anthropic「Introducing Claude 3.5 Sonnet with computer use」— <https://www.anthropic.com/news/3-5-models-and-computer-use> — checked 2026-08-10
- Anthropic Docs「Computer use」— <https://docs.anthropic.com/en/docs/agents-and-tools/computer-use> — checked 2026-08-10


## 備考

- Anthropic が 2024 年 10 月に Claude 3.5 Sonnet で Computer Use を公開したのが最初の大きな一歩です。2026 年には Claude Cowork や Claude Code からも macOS・Windows の画面操作に使えるようになりました。
- 操作範囲を絞った仮想環境やサンドボックス、重要操作の人手承認と組み合わせて使うのが基本的な運用です。
