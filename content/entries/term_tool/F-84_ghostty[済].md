---
id: F-84
title: Ghostty
title_reading: ゴースティ
category: term_tool
subtype: terminal
experience_level: hands_on
reader_level: 3-4
importance: E
figure_type: comparison
page_layout: spread_v1
start_date: 2024-12-26
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - bash
  - Claude Code
  - WSL
  - Warp
status: ready
---

# Ghostty

## tagline

GPU 描画で動く高速ターミナルエミュレータです。AI エージェントの長文出力も滑らかに流せます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ターミナルエミュレータ（端末画面）とは、コマンドを打ち込む「黒い画面」のアプリです。Ghostty は GPU 描画による高速表示と、300 以上の設定項目による細かなカスタマイズを両立しています。

## どこで出会うか

Claude Code（CC）や bash などを日常的に使う開発者が乗り換え先として話題にします。AI エージェントが大量のテキストを出力する場面でも描画が詰まりにくく、バイブコーディング環境の整備記事でよく名前が出ます。


## メイン図

### 図の狙い

「ターミナルエミュレータ」と「シェル」の役割分担を一枚の図で示し、Ghostty がどのレイヤーに属するかを明確にする。

### B. 登場シーン（figure_type: comparison）

- シーン1: 開発者がターミナルアプリ（Ghostty）を開く → 中で bash や zsh（シェル）が起動する
- シーン2: Claude Code が長文ログを出力 → Ghostty の GPU 描画でスクロールが滑らか
- シーン3: Kitty グラフィックスプロトコル対応ツールを使う → 画像プレビューなどが表示される
- 並べる基準: ターミナル（外箱）とシェル（中身）という階層関係


## 会話での使い方例

「Ghostty に乗り換えたら、Claude Code の長文出力もスクロールが滑らかでした。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ターミナルエミュレータとして、シェルとやり取りする画面を提供します。

### 2. うれしさ

GPU 描画で AI の大量テキスト出力でも描画が快適に保たれます。

### 3. 注意点

macOS・Linux 対応で、Windows は対応を検討中です（2026-04-30 時点）。

### 4. どこで役立つか

バイブコーディングで AI エージェントを長時間動かす環境で重宝します。

### 5. はじめに

ターミナルはアプリ、シェルはその中身という層の違いを把握しておくと理解が早まります。

### 6. 深掘り先

bash、WSL、Warp


## 開発フローでの位置（必須）

1. 環境構築 — Ghostty を入れて設定ファイルの場所を確認します
2. シェル連携 — bash や zsh を既定にしてプロンプト表示を確認します
3. AI ツール起動 — Claude Code などを起動し描画速度を体感します
4. カスタマイズ — 設定項目からフォント・色などを好みに合わせます
5. 運用 — スクロールで AI エージェントの出力を読み取ります


## 関連用語

- bash
- Claude Code
- WSL
- Warp


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 開発系 YouTuber が推しているのは知っていましたが、Windows では入れられませんでした
- Mac 限定な面もあり、VS Code のターミナルとの差がわかりませんでした
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: なんかかっこいい感じはします
- 👍 良い点: 触っていると、なんとなくエンジニアっぽい感じがします。
- 👎 ダメな点: 正直、いまは Codex や Claude Code のアプリがとても充実しているので、使う必要がなくなってしまった気がします。道具としての陳腐化が、それだけ早く進んでしまいました。
- 👥 誰向けか: 相当マニアックなところまで行っている人です。いまなら Codex や Claude Code を使えば終わる話なので、正直、レガシーだと思っています。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: ターミナルエミュレータ（外箱）とシェル（内部）の二層構造。左にシェルなし・もたつく旧環境、右に Ghostty + bash のスムーズな環境を並べる
- 登場人物: ノートPC を見つめる開発者（1名）
- 吹き出し・心の声: 「スクロールが滑らか！」「やっと AI の出力を追えた」
- 中央に置くキーワード/ラベル: Ghostty（外箱）／ bash（中身）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: インストールアイコン（ダウンロード矢印）
- Step 2 のアイコン/絵柄: ターミナル画面 + シェルプロンプト
- Step 3 のアイコン/絵柄: AI ロボット + 長いテキスト
- Step 4 のアイコン/絵柄: スライダー・設定歯車
- Step 5 のアイコン/絵柄: スクロールバー + 目のアイコン
- 矢印で示す流れの意図: インストールから日常運用までの順序

## コミュニティ補完メモ

- Warp（B 系ツール）との住み分け：Warp は AI 機能を内蔵した統合ターミナル。Ghostty は AI 非内蔵の高速描画特化ターミナルで、外部 AI ツールを組み合わせて使う。
- iTerm2 との住み分け：iTerm2 は macOS の老舗ターミナルで機能豊富だが描画速度は Ghostty より遅い場面がある。
- F-81 bash との関係：bash はシェル（コマンド解釈プログラム）、Ghostty はそのシェルを動かす外箱（エミュレータ）。層が異なる。
- F-82 WSL との関係：WSL（Windows Subsystem for Linux）は Windows 上に Linux 環境を作る仕組みで、Ghostty のターミナル画面から WSL に接続して使うパターンがある。


## 出典メモ

- <https://ghostty.org/> — checked 2026-04-30
- <https://github.com/ghostty-org/ghostty> — checked 2026-04-30


## 備考

- Windows 対応は 2026-04-30 時点で研究段階（"Tier 3" として issue あり）。将来変わる可能性があるため version_status: active のまま出典メモに記載。
- 開発者は Mitchell Hashimoto（Vagrant・Terraform を擁する HashiCorp の共同創業者）。HashiCorp 退任後の個人プロジェクトとして開発。
- Zig 言語で書かれており、低レベル最適化による高速化が特徴。
