---
id: B-4
title: Cursor
title_reading: カーソル
category: service
subtype: ai_assistant
experience_level: partial
reader_level: 2-3
importance: B
figure_type: before_after
page_layout: spread_v1
start_date: 2023-01-01
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - VS Code
  - GitHub Copilot
  - Composer
  - バイブコーディング
  - Tab 補完
status: ready
---

# Cursor

<!--
バイブコーディング図鑑 エントリー v2（spread_v1 準拠）
-->

## tagline

VS Code をフォークした AI 常駐エディタです。チャット・補完・マルチファイル編集を 1 つの画面に統合しています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

コード生成・チャット・先読み補完の 3 つを 1 画面でこなします。Cmd-K でインライン生成、Cmd-L でチャット、Tab で補完受け入れが基本セットです。

## どこで出会うか

GitHub Copilot との比較記事やバイブコーディング入門記事でよく名前が出ます。「エディタ自体に AI を入れた」サービスとして紹介されます。

## メイン図

### 図の狙い

VS Code 単体で手打ちしていた状態と、Cursor で AI が常駐した状態を対比し、同じエディタ環境で何が変わるかを示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: VS Code 単体で作業。AI は外部タブで別に開く
  - 視覚要素（コード or 概念）: エディタウィンドウ横に別ブラウザタブで ChatGPT を開いた図
  - つまずき: コードとチャットを行き来するたびにコピーペーストが発生する
- After
  - 状況: Cursor でエディタ内に AI が常駐。Tab で補完、Cmd-L でチャット、Cmd-K でインライン編集
  - 視覚要素: 同じウィンドウ内にサイドチャットとインライン提案が同居する図
  - うれしさ: コードを離れずに AI と対話でき、編集・確認がその場で完結します

## 会話での使い方例

「Cursor の Composer でマルチファイルをまとめて直してもらったら早かったです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI 補完・チャット・インライン編集を統合したコードエディタです。

### 2. うれしさ

エディタを離れずに AI と往復でき、コピペの手間がなくなります。

### 3. 注意点

無料枠に月あたりの使用上限があり超過すると有料プランが必要です。

### 4. どこで役立つか

新規生成より既存ファイルの修正・リファクタリング場面で効果が出やすいです。

### 5. はじめに

cursor.com からインストールし VS Code 設定を引き継いで起動できます。

### 6. 深掘り先

Composer（D-35）、VS Code（F-30）、GitHub Copilot（B-5）

## 開発フローでの位置（必須）

1. インストール — cursor.com から入手し、VS Code 設定を引き継いで起動します
2. Cmd-K で生成 — 選択範囲にその場でコードを書いてもらいます
3. Cmd-L でチャット — ファイルを参照して修正方針を確認します
4. Tab で補完 — 次行の続きを Tab で受け入れて進めます
5. Composer で横断編集 — 複数ファイルの変更を一括指示します

## 関連用語

- VS Code
- GitHub Copilot
- Composer
- バイブコーディング
- Tab 補完


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Cursor を入れても VS Code との違いがよくわかりませんでした。
- 学習に使われると聞き、会社で使っていいかが不明でした。
- Claude Code に移行して自分で書かなくなり、出番がありませんでした。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: AI ニュース界隈で「良い」と騒がれていた印象でした
- 👍 良い点: コードをちゃんと書く人には良いです
- 👎 ダメな点: コードを書かない人だと触ってもメリットを感じにくいです
- 👥 誰向けか: システムエンジニア向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左半分（Before）にエディタ画面とブラウザタブが並ぶ様子、右半分（After）に Cursor のエディタ内チャットとインライン提案が同居する様子を横並びで対比する
- 登場人物: 開発者（PC の前に座り、2 つの画面を行き来して困り顔）→ Cursor 導入後は同じ人物が 1 画面に集中してスムーズな表情
- 吹き出し・心の声: Before「またコピペして貼り直しか…」 / After「そのままここで頼める！」
- 中央に置くキーワード/ラベル: Before = 「エディタ ＋ 外部 AI」 / After = 「Cursor（統合）」
- Before / After の対比ポイント: 画面の切り替え回数・コピペの有無

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ダウンロード矢印 — インストール
- Step 2 のアイコン/絵柄: 稲妻マーク — Cmd-K インライン生成
- Step 3 のアイコン/絵柄: チャット吹き出し — Cmd-L サイドチャット
- Step 4 のアイコン/絵柄: Tab キーアイコン — Tab 補完
- Step 5 のアイコン/絵柄: 複数ファイルアイコン — Composer 横断編集
- 矢印で示す流れの意図: インストール → コード生成 → チャット → 補完 → 横断編集という使い込む順を示す


## コミュニティ補完メモ

- VS Code（F-30）との住み分け：Cursor は VS Code をフォークしたサービスの説明。VS Code 自体の機能・拡張・エコシステムは F-30 で扱います
- GitHub Copilot（B-5）との住み分け：Copilot は既存エディタへの追加拡張。Cursor はエディタ自体が AI 統合済みという違いを本文では触れるにとどめ、詳細比較は B-5 側で扱います
- Composer / cursor-tab-3 等の独自モデル・機能詳細は D-35 へ。本エントリはサービスとしての Cursor（画面・操作感・入口）にとどめます

## 出典メモ

- cursor.com — checked 2026-04-29
- cursor.com/features — checked 2026-04-29

## 備考

- 料金プランは Hobby（無料）/ Pro（月 $20 前後）/ Business の 3 段構成が基本ですが変動があるため本文には入れず、evaluation_date で管理します
- 「AI エディタ」カテゴリは競合（Windsurf 等）が多く時変性が高いため、サービスの本質的な仕組み（VS Code フォーク × AI 統合）を中心に書き、具体的な機能名や料金の言及は最小限にしています
