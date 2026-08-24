---
# ── 識別・分類 ──
id: F-86
title: ollama
title_reading: オラマ
category: term_tool
subtype: runtime

# ── 読者・体験 ──
experience_level: hands_on
reader_level: 3-4
importance: C

# ── 誌面形式 ──
figure_type: structure
page_layout: spread_v1

# ── 時変情報 ──
start_date:
end_date:
version_status: active
pricing_note: none

evaluation_date: 2026-04-30

# ── 関係 ──
related_terms:
  - VRAM
  - Llama 系
  - Mistral 系
  - Qwen 系
  - llama.cpp

# ── 制作状態 ──
status: needs_review
---

# ollama

<!--
バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠）
-->

## tagline

ローカル PC で LLM を 1 コマンド実行できる配布・実行ツールです。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`ollama run llama3` の 1 行でモデルを取得・起動します。NVIDIA CUDA・Mac Metal など GPU 高速化にも対応します。

## どこで出会うか

API 課金なしでローカル LLM を試したい場面で登場します。Claude Code や MCP の呼び出し先として設定でき OpenAI 互換 API も提供します。

## メイン図

### 図の狙い

ollama がモデルの取得から API 提供までを一手に担う様子を、人物視点で示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: ollama（実行ランタイム）
- 周辺の要素: モデルファイル（GGUF）／llama.cpp バックエンド／GPU（Metal / CUDA / ROCm）／HTTP API（OpenAI 互換）／CLI
- 関係の描き方: ollama を中心に、左から「モデル取得」、下から「GPU 高速化」、右へ「API 出力」の矢印


## 会話での使い方例

「ollama でローカルに Llama 3 を入れたら、API 課金なしで補助が効きました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ローカル PC 上で LLM を取得・実行する配布ランタイムです。

### 2. うれしさ

API 課金なしでモデルを試せ、オフライン環境でも動作します。

### 3. 注意点

大きいモデルは VRAM 不足でクラッシュするため、量子化バリアント選びが重要です。

### 4. どこで役立つか

Claude Code や MCP サーバーのローカル LLM 連携先として機能します。

### 5. はじめに

`ollama run llama3` で動作確認し、`ollama list` でサイズを確認します。

### 6. 深掘り先

llama.cpp、VRAM、GGUF 量子化


## 開発フローでの位置（必須）

1. モデル取得 — `ollama pull qwen2.5:7b` で量子化バリアントを指定してダウンロードします
2. 起動確認 — `ollama run` でモデルを対話起動し、VRAM 内に収まるか確かめます
3. API 接続 — OpenAI 互換の HTTP API をアプリや MCP サーバーから呼び出します
4. ツール連携 — Claude Code や Cursor のローカル LLM バックエンドとして設定します


## 関連用語

- VRAM
- Llama 系
- Mistral 系
- Qwen 系


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- ローカル LLM は GPU の VRAM 量に大きく左右され、家の PC では入りきらないことがあります。
- ollama に入る全モデルが自分の PC で使えるわけではなく、見極めが難しいです。
- 大きいモデルは VRAM がたくさん必要で、ハードルが高くなります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: ローカルでできるなら今後 PC で全部済むのでは、と期待しました。
- 👍 良い点: フリーで回せて、特に小さいモデルなら気軽に試せるのが嬉しいです。
- 👎 ダメな点: 大きいモデルは VRAM のでかい GPU が必要で、現実的に厳しいです。
- 👥 誰向けか: Mac ユーザーが一番向いています。RAM と VRAM が共有でコスパ良好です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: ollama を中心に置き、左からモデルファイル（GGUF）が流れ込み、下から GPU が支え、右へ HTTP API と CLI が出ていく構造図
- 登場人物（いれば）: PC の前に座る開発者（男女どちらでも可）
- 吹き出し・心の声: 「コマンド 1 行でモデルが動いた！」
- 中央に置くキーワード/ラベル: ollama

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ダウンロード矢印（モデル取得）
- Step 2 のアイコン/絵柄: ターミナル画面（起動確認）
- Step 3 のアイコン/絵柄: API プラグアイコン（HTTP 連携）
- Step 4 のアイコン/絵柄: ツール連携（エディタ + サーバー）
- 矢印で示す流れの意図: 取得 → 確認 → 連携 → 管理の一方向フロー


## コミュニティ補完メモ

- llama.cpp（F 系列）との住み分け：llama.cpp は ollama の内部エンジン。エンドユーザーは ollama を入口として使い、llama.cpp を直接触ることは少ない
- LM Studio との住み分け：LM Studio は GUI 中心のローカル LLM ツール。ollama は CLI・API 中心でスクリプト連携向き
- VRAM（J-70）との関係：モデルサイズが VRAM を超えるとクラッシュするため、`ollama list` でサイズ確認が必須。量子化バリアント（`:7b` `:3b` 等）を選ぶことで回避できる


## 出典メモ

- https://ollama.com — checked 2026-04-30
- https://github.com/ollama/ollama — checked 2026-04-30


## 備考

- モデルの提供状況（対応モデル名・バリアント）は頻繁に変わる時変情報のため、具体的なモデル名列挙は避けブリーフ記載の代表例にとどめた
- OpenAI 互換エンドポイントのデフォルトポートは `11434`（2026-04-30 時点）
