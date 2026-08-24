---
id: F-200
title: Rust
title_reading: ラスト
category: term_tool
subtype: language
experience_level: partial
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2015-05-15
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Tauri
  - ripgrep
  - TypeScript
  - Cargo
status: needs_review
---

# Rust

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

メモリ安全と高速性を両立するシステム言語です。AI 周辺の高速ツールを支える基盤として注目されています。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

「所有権（Ownership）」という独自の仕組みで、メモリ管理ミスをコンパイル時に検出します。ガベージコレクション（自動メモリ回収）なしで C++ に迫る速度を出せます。


## どこで出会うか

ripgrep（F-71）・uv・Tauri（F-13）・Ghostty（F-84）など AI 開発で使う高速ツールの多くが Rust 製です。「このツールはなぜ速いのか」と調べると Rust の名前に辿り着くことがあります。


## メイン図

### 図の狙い

「所有権」がコンパイル時に問題を止める流れと、Rust 製ツールの広がりを一枚で見せる。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Rust（所有権・コンパイル安全）
- 周辺の要素: ripgrep / uv / Tauri / Ghostty / Linux カーネル一部
- 関係の描き方: 中央から各ツール名へ矢印。矢印ラベルは「Rust 製」


## 会話での使い方例

「ripgrep が速いのは Rust 製で、borrow checker のおかげで安全性も高いそうです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

コンパイル時にメモリ安全を保証するシステム言語です。

### 2. うれしさ

コンパイルが通れば実行時のメモリ系クラッシュが減ります。

### 3. 注意点

borrow checker のエラーが最初の壁になりやすいです。

### 4. どこで役立つか

CLI ツールや高速バックエンド開発で効果が出やすいです。

### 5. はじめに

所有権の概念と Cargo（パッケージマネージャ）を押さえます。

### 6. 深掘り先

Tauri, ripgrep, Cargo


## 開発フローでの位置（必須）

1. 環境構築 — `rustup` で Rust をインストールし Cargo が使える状態にします
2. 実装 — 所有権ルールを守りながらコードを書き、コンパイルエラーを確認します
3. AI 支援 — borrow checker のエラーを Claude や Cursor に貼り付けて解説してもらいます
4. ビルド — `cargo build` でコンパイルし、テストを通して動作確認します


## 関連用語

- Tauri
- ripgrep
- TypeScript
- Cargo


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 言語名なのかソフト名なのか、初見では何を指す言葉か掴めません。
- Python や JavaScript ほど一般的でなく、話題に出すとマニアック扱いされます。
- ターミナル系ツールの裏側で出てくる名前で、出会う面が偏っている印象です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 速いと言われても最初はピンと来ず、書籍などで名前を見かけて知りました。
- 👍 良い点: 速いツールの多くがこれで書かれていて、信頼の地盤になっているところです。
- 👎 ダメな点: 自分が直接書くわけではないので、知っていても活かしどころが見えにくいです。
- 👥 誰向けか: 言語の本質を「なぜ速いか」から理解したいエンジニア寄りの人向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に大きく「Rust」のロゴ（歯車風）を置き、周囲に ripgrep / uv / Tauri / Ghostty を配置。矢印ラベルは「Rust 製」
- 登場人物: 開発者（男性または女性）がターミナルの前で座っている姿
- 吹き出し・心の声: 「コンパイル通った！安心して使える。」
- 中央に置くキーワード/ラベル: Rust（所有権・コンパイル安全）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: PC ＋ ダウンロードマーク（rustup）
- Step 2 のアイコン/絵柄: コードエディタ画面（borrow checker エラー表示）
- Step 3 のアイコン/絵柄: AI チャット画面（エラー解説）
- Step 4 のアイコン/絵柄: ターミナル ＋ チェックマーク（cargo build 成功）
- 矢印で示す流れの意図: セットアップ → 実装 → AI 支援 → ビルド完了


## コミュニティ補完メモ

- F-1 JavaScript との住み分け：JavaScript はフロントエンド・スクリプト寄り、Rust はシステム・ツール層。同じ「プログラミング言語」でも対象レイヤーが異なります
- F-13 Tauri との住み分け：Tauri は Rust 製フレームワーク（デスクトップアプリ構築）。Rust の採用例として本エントリから参照します
- F-71 ripgrep との住み分け：ripgrep は Rust 製ツール（高速検索）。同様に採用例として参照します
- F-84 Ghostty との住み分け：Ghostty は Rust 製ターミナルエミュレータ。同様の採用例

## 出典メモ

- [rust-lang.org](https://www.rust-lang.org/) — checked 2026-04-30
- [Rust Foundation](https://foundation.rust-lang.org/) — checked 2026-04-30
- ripgrep GitHub: [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) — checked 2026-04-30


## 備考

- Rust 1.0 リリースは 2015-05-15。現在は Rust Foundation が管理
- borrow checker のエラーメッセージは英語で詳細だが、非エンジニアには難解。「Claude に貼り付けて解説」というワークフローはブリーフ記載の実用例
- Linux カーネルへの採用（一部）は 2022 年以降。採用範囲は拡大中だが、全体から見るとまだ限定的
