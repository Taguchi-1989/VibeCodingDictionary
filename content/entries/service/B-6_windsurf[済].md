---
id: B-6
title: Windsurf
title_reading: ウィンドサーフ
category: service
subtype: ai_assistant
experience_level: partial
reader_level: 2-3
importance: C
figure_type: comparison
page_layout: spread_v1
start_date: 2024-11-01
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Cursor
  - VS Code
  - GitHub Copilot
  - Claude Code
status: ready
---

# Windsurf

<!--
バイブコーディング図鑑 エントリー v2（spread_v1 準拠）
-->

## tagline

Codeium が 2024 年 11 月に公開した AI コードエディタ。Cascade が複数ファイルを横断編集します。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Cascade（カスケード）と呼ばれるエージェントが、リポジトリ全体を把握して複数ファイルを同時に書き換えます。指示すると、関連ファイルを自律的に探して一括変更します。

## どこで出会うか

Cursor（B-4）との比較記事や、バイブコーディング入門の文脈でよく登場します。VS Code（F-30）互換で macOS・Windows・Linux に対応し、無料から試せます。

## メイン図

### 図の狙い

Cursor と Windsurf を並べ、それぞれの「AI の介入の仕方」の違いを示します。

### B. 登場シーン（figure_type: comparison）

- シーン1: Cursor — Tab 補完と Composer で手元作業を加速するエディタ
- シーン2: Windsurf — Cascade が自律的にリポジトリを読んで複数ファイルを書き換えるエディタ
- シーン3: 共通点 — VS Code ベース、freemium、AI と常時対話できる環境
- 並べる基準: AI の自律度（補助 vs 自律）

## 会話での使い方例

「Windsurf の Cascade に複数ファイル横断のリファクタを任せました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Cascade が複数ファイルを自律的に横断編集するエディタです。

### 2. うれしさ

変更箇所をエージェントが探すため、ファイルを自分で探す手間が減ります。

### 3. 注意点

自律編集の範囲が広く、意図しないファイルが書き換わることがあります。

### 4. どこで役立つか

既存コードのリファクタや、変更が複数ファイルに及ぶ作業で役立ちます。

### 5. はじめに

VS Code 互換で動き、Cascade は Cursor の Composer に相当する、と押さえれば十分です。

### 6. 深掘り先

Cursor（B-4）、VS Code（F-30）、Claude Code（B-7）

## 開発フローでの位置（必須）

1. インストール — windsurf.com から入手し、既存プロジェクトを開きます
2. Cascade に指示 — チャットに「○○をリファクタして」と日本語で依頼します
3. 自律探索 — Cascade がリポジトリを読み、対象ファイルを選びます
4. 一括編集 — 複数ファイルの変更案が示され、差分を確認して承認します
5. 反復 — 結果を見て追加指示を重ね、ゴールに近づけます

## 関連用語

- Cursor
- VS Code
- GitHub Copilot
- Claude Code


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 名前はよく聞きますが使う機会がなく、何が良いのか掴みにくいです。
- 「VS Code ベースより良い」と聞く一方で、本当にそうか判断しにくいです。
- 設計思想が Antigravity に近く、いま追いかける優先順位が分かりにくいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: CI 活用を模索する中で VS Code が最適と感じ、別の選択肢として名前を聞いていました。
- 👍 良い点: リポジトリ管理やプランで計画を管理できる仕組みがあると聞き、良さそうに感じました。
- 👎 ダメな点: Claude Code や Codex のデスクトップ版に役割を巻き取られた印象です。
- 👥 誰向けか: 歴史的な存在になりつつあり、その経緯を知りたい人向けだと思います。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: Cursor と Windsurf を左右に並べた比較図。左に Cursor、右に Windsurf を配置し、それぞれの AI の介入度を矢印と吹き出しで示す
- 登場人物: 開発者（PC 前に座り、2 つのエディタ画面を見比べている）
- 吹き出し・心の声: Cursor 側「Tab と Composer で手を動かす感覚」/ Windsurf 側「Cascade に全部まかせてみた」
- 中央に置くキーワード/ラベル: 左「Cursor：補助型」/ 右「Windsurf：自律型」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ダウンロード矢印 — インストール
- Step 2 のアイコン/絵柄: チャット吹き出し — Cascade への指示
- Step 3 のアイコン/絵柄: 虫眼鏡 — 自律探索
- Step 4 のアイコン/絵柄: 複数ファイルアイコン — 一括編集と差分確認
- Step 5 のアイコン/絵柄: 繰り返し矢印 — 追加指示の反復
- 矢印で示す流れの意図: インストール → 指示 → 探索 → 編集 → 反復という Cascade の使い方の流れを示す

## コミュニティ補完メモ

- Cursor（B-4）との住み分け：Cursor は Tab 補完・Cmd-K・Cmd-L が主役で手元操作を加速するエディタ。Windsurf は Cascade の自律探索・一括編集が主役。どちらも VS Code ベースで freemium だが、AI の介入度で役割を分けて説明します
- Claude Code（B-7）との住み分け：Claude Code はターミナル上で動く CLI エージェント。Windsurf はエディタ GUI を提供するサービス。GUI vs CLI という切り口で住み分けます
- 企業経緯（詳細は備考）：買収劇の経緯は本文に入れず備考に保存し、誌面には「Codeium が開発」程度にとどめます

## 出典メモ

- windsurf.com — checked 2026-04-30
- codeium.com — checked 2026-04-30

## 備考

- 企業経緯：2025 年に OpenAI による買収交渉が報じられたが破談。最終的に Google が研究チームを取り込み、製品・サービス部分（Codeium）は Cognition（Devin の親会社）が引き取るという複雑な流れがあった。評価日以降に状況が変わっている可能性があるため本文には入れていない
- 料金：無料プランあり、Pro 月 $15 / Team 月 $30 程度（evaluation_date 基準）。変動する可能性があるため本文には入れていない
- Cascade は Cursor の Composer に相当するマルチファイル編集エージェント機能。両者の比較はブリーフ通り「自律的な複数ファイル編集」が Windsurf の売りとして整理する
