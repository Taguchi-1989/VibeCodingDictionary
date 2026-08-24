---
id: A-9
title: 索引
category: common
subtype: meta
experience_level: research_only
reader_level: 1
importance: A
page_layout: front_map_index
spread_position: right
evaluation_date: 2026-05-13
related_terms:
  - A-1 まえがき
  - A-2 この本の読み方
  - A-3 図鑑の歩き方
  - A-11 略称表記
status: needs_review
---

# 索引

このページは前付け 7 見開きの 4 番目の右ページです。同居エントリは左ページの A-3（歩き方）。ここでは前付け内で完結する**ミニ索引**を載せ、巻末の本物索引への入口にします。

## リード文

巻末にアルファベット順と五十音順の本物索引を収録します。前付け段階では、各章の代表語 3 つを並べた「ミニ索引」を見せて、本書のスケールを掴んでもらいます。

## ミニ索引（章ごとの代表語 3 つ）

- **A はじめに** — まえがき／この本の読み方／略称表記
- **B サービス** — Gemini／ChatGPT／Claude Code
- **C 人・組織** — OpenAI／Anthropic／Demis Hassabis
- **D モデル** — Gemini 2 系／Claude 3 系／GPT-4 系
- **E ベンチマーク** — SWE-Bench／MMLU／Chatbot Arena
- **F 従来コード** — TypeScript／HTML／Markdown
- **G バイブ特有** — Context Window／System Prompt／CLAUDE.md
- **H 歴史** — ChatGPT 公開／GPT-4 リリース／Transformer 論文
- **I MCP** — MCP Server／GitHub MCP／Filesystem MCP
- **J 一般語彙** — 機械学習／Hallucination／GPU

## 索引の使い分け

- **letter 順索引**（巻末）: ID から引く。`F-2` を見つけたいときなど位置ベース
- **五十音順索引**（巻末）: 日本語・カタカナ名から引く。「コンテキスト」「プロンプト」など
- **アルファベット順索引**（巻末）: 英字略称から引く。GPT・MCP・RAG など
- 略称・愛称（Nano Banana 等）は正式名エントリへ橋渡し注記で誘導

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### 右ページ図（ミニ索引）

- 描く内容: 10 章 × 3 語のミニ索引を 2 段組の表で配置。章ラベルは見出し風に太く
- 列右端に章番号バッジ（A〜J）を置く。色は左ページの 3 ルート線とは別系
- 表の右上に「巻末に本物索引あり」のキャプション 1 行（小さく）
- 線画・濃紺主体・余白多め。表罫線は dashed

## コミュニティ補完メモ

- A-2（読み方）との住み分け: A-2 は構造案内、A-9 は逆引きの実物（ミニ＋巻末）
- A-11（略称表記）との住み分け: A-11 は略称凡例。A-9 から略称見出しを引いたとき A-11 を参照
- 愛称・表記ゆれ（Nano Banana → Gemini 2.5 Flash Image など）は本物索引内の橋渡し注記で処理

## 出典メモ

- 本書の編集方針（要件定義書）— checked 2026-04-30
- 旧 A-9 index（2026-04-30 版）— 索引の 2 系統発想を継承

## 備考

- 旧 spread_v1 版（2026-04-30）の tagline・6 視点・開発フロー・著者欄は v0.2 改訂で廃止
- A-9 は同居 layout `front_map_index` の右ページ担当（`spread_position: right`）。左ページは A-3
- **巻末索引（本物のアルファベット順／五十音順／letter 順）は本書末尾の専用ページ。本仕様（前付け）のスコープ外で、`docs/back_matter_layout.md`（未作成）で別途扱う**
- ミニ索引の章ごと代表語 3 つは、現時点で執筆済みの ready エントリから選定。今後の追加で増減する可能性あり
