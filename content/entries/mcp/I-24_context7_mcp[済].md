---
id: I-24
title: Context7 MCP
title_reading: コンテキストセブン エムシーピー
category: mcp
subtype: dev_automation
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - MCP
  - MCP Server
  - Context Window
  - Prompt Engineering
status: ready
---

# Context7 MCP

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

LLM の学習データより新しいライブラリの公式 docs を、プロンプトひとつで取り込む MCP Server です。

## 何をしてくれるか

Upstash 製の MCP Server で、1,000 以上のライブラリ公式 docs をプロンプトから取得できます。`use context7` の一言で Claude や Cursor が自動参照し回答に反映します。

## どこで出会うか

LLM が古い書き方を返してくる場面で出会います。破壊的変更後の旧 API 提案や、バージョン違いの記述が続くときの解毒剤として紹介されます。

## メイン図

### 図の狙い

`use context7` を書く前後で回答の出どころがどう変わるかを示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: LLM の学習データのみで回答する
  - 視覚要素（コード or 概念）: プロンプト → LLM 学習データ（カットオフ済み） → 旧 API の回答
  - つまずき: フレームワークの破壊的変更を反映できない
- After
  - 状況: Context7 が公式 docs を取得して回答に注入する
  - 視覚要素: プロンプト（`use context7`）→ Context7 MCP → 公式ドキュメント → 現在の API の回答
  - うれしさ: 公開中のドキュメントをそのまま参照した回答が返ってくる

## 会話での使い方例

「`use context7` で app router を聞き直したら、動く書き方が返ってきました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM カットオフ後の公式 docs を取得して回答を補強します。

### 2. うれしさ

`use context7` の一言で現行 docs 参照に切り替わります。

### 3. 注意点

未対応ライブラリでは通常の LLM 回答にとどまります。

### 4. どこで役立つか

破壊的変更が多いフレームワークのバイブコーディング。

### 5. はじめに

MCP Server と stdio 接続の概念が前提知識です。

### 6. 深掘り先

MCP、MCP Server、Context Window

## 開発フローでの位置（必須）

1. 環境に追加する — Context7 の MCP Server を起動します
2. AI エディタに登録する — Claude Code や Cursor の MCP 設定に追記します
3. プロンプトに書く — 質問の末尾に `use context7` と加えます
4. 公式 docs が渡る — Context7 が取得した文書が回答に反映されます
5. 回答を受け取る — 公開中のドキュメントを根拠にした回答が返ってきます


## 関連用語

- MCP
- MCP Server
- Context Window
- Prompt Engineering


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 公式情報を取ってくれる価値は感じますが、足す利点が掴めません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 名前をよく聞く MCP のひとつです
- 👍 良い点: 依存関係で困ったとき公式の情報を取ってくれるそうです
- 👎 ダメな点: Codex など GPT 系の検索で代用できそうに思えます
- 👥 誰向けか: バージョンアップに追従したいときに向きます
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左半分に「Before」としてプロンプトが LLM（脳みそアイコン、カットオフ済みの黄色テープが貼ってある）に届き、古い API コードが返ってくる構図。右半分に「After」として `use context7` のプロンプトが Context7 MCP Server を経由し、公式ドキュメントから現在の API コードが返ってくる構図
- 登場人物: 困った顔の開発者キャラクター（Before）、安堵の顔の同一キャラクター（After）
- 吹き出し・心の声: Before 「なぜ古い書き方が返ってくる？」／After 「`use context7` ひとつで解決した」
- 中央に置くキーワード/ラベル: Context7 MCP
- Before / After の対比ポイント: 回答の根拠が「LLM の記憶」か「公開中の公式 docs」か

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ターミナルアイコン（npx 起動）
- Step 2 のアイコン/絵柄: 設定ファイルアイコン（MCP 登録）
- Step 3 のアイコン/絵柄: チャットバブルアイコン（`use context7` 入力）
- Step 4 のアイコン/絵柄: ドキュメントアイコン（公式 docs 取得）
- Step 5 のアイコン/絵柄: チェックアイコン（現在の回答）
- 矢印で示す流れの意図: セットアップ → 登録 → 呼び出し → 取得 → 受け取り

## コミュニティ補完メモ

- I-1 MCP との住み分け：MCP はプロトコルの総論、Context7 MCP は「ライブラリ docs 取得」に特化した個別 Server 事例
- I-2 MCP Server との住み分け：MCP Server は Server の概念説明、Context7 MCP は具体的な 1 Server の紹介
- G-5 Context Window との関係：Context7 は docs を Context Window に注入することで LLM の知識を補う。補完関係にある概念として触れるとよい

## 出典メモ

- [https://github.com/upstash/context7](https://github.com/upstash/context7) — checked 2026-04-29
- [https://context7.com](https://context7.com) — checked 2026-04-29

## 備考

- Context7 が対応するライブラリ数（1,000 以上）は執筆時点の数字です。評価日以降に増減する可能性があります
- Upstash は Redis 互換のサーバーレスデータサービスを提供する企業でもあります（Context7 は別サービスとして展開）
- transport は stdio。`npx -y @upstash/context7-mcp` で追加インストール不要で起動できます
