---
id: F-30
title: VS Code
title_reading: ヴイエスコード
category: term_tool
subtype: editor
experience_level: hands_on
reader_level: 2-3
importance: B
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Cursor
  - GitHub Copilot
  - 拡張機能
  - GitHub
  - Terminal
status: ready
---

# VS Code

## tagline

Microsoft が無料で提供するコードエディタです。拡張機能でほぼ何にでも育てられます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

コードを書くエディタ本体に拡張機能（Extension）を後から足せるプラットフォームです。AI 補完・リンター・デバッガーなど多数の拡張が公式マーケットプレイスで配布されています。

## どこで出会うか

入門記事で「まず VS Code を入れましょう」と名前が挙がります。Cursor など AI エディタが VS Code をフォークしているため比較記事でもよく登場します。

## メイン図

### 図の狙い

VS Code 本体と拡張機能の関係を「プラットフォーム ＋ プラグイン」の構造として見せ、何を足せば何ができるかを把握してもらいます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: VS Code 本体（編集・ターミナル・ファイル管理）
- 周辺の要素: GitHub Copilot 拡張 / Python 拡張 / ESLint 拡張 / Prettier 拡張 / Remote-SSH 拡張
- 関係の描き方: 中央の本体を囲む円形に各拡張が刺さる形（ハブ＆スポーク）

## 会話での使い方例

「VS Code に Copilot 拡張を入れるだけで、補完がすぐ使えるようになりますよ。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

拡張機能でどんな言語・ツールにも対応できるエディタ基盤です。

### 2. うれしさ

無料でインストールでき、AI 補完も拡張 1 本で追加できます。

### 3. 注意点

拡張を増やしすぎると起動が遅くなることがあります。

### 4. どこで役立つか

Web・Python・AI 開発など言語を問わず最初の選択肢になります。

### 5. はじめに

インストール後に拡張マーケットプレイスの使い方を押さえるのが出発点です。

### 6. 深掘り先

Cursor（B-4）、GitHub Copilot（B-5）、拡張機能

## 開発フローでの位置（必須）

1. インストール — code.visualstudio.com から無料で入手します
2. 拡張を追加 — マーケットプレイスで AI 補完や言語サポートを足します
3. コードを書く — シンタックスハイライトと補完を使いながら編集します
4. ターミナルを開く — エディタ内で git コマンドやテストを実行します
5. デバッグ — ブレークポイントを置いてエラーの原因を確かめます

## 関連用語

- Cursor
- GitHub Copilot
- 拡張機能
- GitHub
- Terminal


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 拡張を入れるほど重くなり、全体把握に時間がかかりました。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 黒い画面でかっこいい感じですが、最初は難しそうでした。
- 👍 良い点: ターミナル統合でフォルダ構成も見やすく、痒いところに手が届きます。
- 👎 ダメな点: エージェントマルチタスク開発ではベストとは言い切れない場面があります。
- 👥 誰向けか: デスクトップで開発したい人全般に向いています。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「VS Code 本体」のロゴ型ブロックを置き、周囲に拡張機能カードが放射状に並ぶハブ＆スポーク構造。各カードに拡張名と用途アイコン（AI / Python / Lint 等）を添える
- 登場人物: PC の前に座る人物が「この拡張を追加しよう」と指差す姿
- 吹き出し・心の声: 「目的に合わせて拡張を足すだけで自分仕様になります」
- 中央に置くキーワード/ラベル: VS Code（エディタ本体）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ダウンロード矢印 — インストール
- Step 2 のアイコン/絵柄: パズルピース — 拡張追加
- Step 3 のアイコン/絵柄: 鉛筆 — コード編集
- Step 4 のアイコン/絵柄: ターミナル画面 — コマンド実行
- Step 5 のアイコン/絵柄: 虫眼鏡 — デバッグ
- 矢印で示す流れの意図: 入手 → 環境構築 → 編集 → 実行 → 検証の開発サイクルを示す


## コミュニティ補完メモ

- Cursor（B-4）との住み分け：Cursor は VS Code をフォークした AI 常駐エディタ。本エントリは VS Code 本体の構造・拡張エコシステムに絞り、AI エディタとしての比較は B-4 で扱います
- GitHub Copilot（B-5）との住み分け：Copilot は VS Code 拡張として動く代表例。拡張の入れ方の具体例として名前を出す程度にとどめ、詳細は B-5 で扱います
- 個別拡張機能（F-34〜F-38）：拡張の種類・使い方は各エントリに任せ、本エントリは「拡張を足せるプラットフォーム」という構造理解に絞ります
- VS Code Insiders / Codium / Windsurf 等のフォーク派生は「深掘り先」で軽く触れるにとどめます

## 出典メモ

- code.visualstudio.com — checked 2026-04-29
- marketplace.visualstudio.com — checked 2026-04-29

## 備考

- 正式名称は「Visual Studio Code」。「Visual Studio」（別製品）と混同されやすいため、本エントリでは略称「VS Code」を統一表記として使います
- フォーク派生：Cursor / Windsurf / VSCodium など複数が存在します。本エントリは本家 VS Code の機能・エコシステムに絞ります
- 価格：本体は無料。一部拡張機能（GitHub Copilot 等）は有料プランが別途必要です
