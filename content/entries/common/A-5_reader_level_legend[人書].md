---
id: A-5
title: 読者レベルの凡例
category: common
subtype: meta
experience_level: hands_on
reader_level: 1
importance: A
page_layout: front_legend_marks
spread_position: left
evaluation_date: 2026-05-13
related_terms:
  - A-1 まえがき
  - A-2 この本の読み方
  - A-3 図鑑の歩き方
  - A-4 体験区分の凡例
status: needs_review
---

# 読者レベルの凡例

このページは前付け 7 見開きの 5 番目（注意マーク凡例）の左ページ下段です。A-4 と縦に並ぶレイアウトで、A-4 が上、A-5 が下。

## リード文

各エントリに付く「1〜6」の数値で、読むのに必要な前提知識の目安を示します。

## 6 段階のはしご

- **1** 入門 — AI ニュースを見たことがある人。例: ChatGPT、Hallucination
- **2** 一般 — 仕事で AI を使っている非エンジニア。例: Context、MCP、Cursor
- **3** 中級 — 業務で本格活用する人。例: Tool Use、Hook、Slash Command
- **4** 応用 — フロントエンドや軽い実装に踏み込む人。例: TypeScript、Lint
- **5** 上級 — エンジニア・実装者。例: 量子化、LoRA、Tensor コア
- **6** 専門 — 研究者・コア実装。例: gpt-oss、ノイマン型、Anthropic 創業史

範囲表記（`2-3` のような）は「両端のレベルでも読める」エントリを表します。

## YAML との対応

エントリの YAML フロントマターでは `reader_level` フィールドに `1`〜`6` または範囲（`2-3` 等）を記載します。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### 左ページ下段（読者レベル）

- 描く内容: 縦のはしご図 6 段。各段にレベル名、右に例語 2〜3 個
- 段ごとに色を薄〜濃のグラデーション 1〜6（青系単色の濃淡）
- A-4（体験区分）の下に配置。左ページは A-4 / A-5 が縦並び
- レベル 6 の濃さは本編タグライン青と同程度に。1 は最薄に

## 出典メモ

- 旧 A-5 reader_level_legend（2026-04-30 版）— 6 段階の発想を継承
- [docs/entry_schema.yaml](../../../docs/entry_schema.yaml) `frontmatter.recommended.reader_level` — checked 2026-05-13
- [docs/entry_schema.yaml](../../../docs/entry_schema.yaml) `frontmatter.recommended.importance` の A〜E 例語 — checked 2026-05-13（例語の選定に流用）

## 備考

- 旧 spread_v1 版（2026-04-30）の tagline・6 視点・開発フロー・著者欄は v0.2 改訂で廃止
- A-5 は同居 layout `front_legend_marks` の左ページ下段担当（`spread_position: left`）
- reader_level（前提知識レベル 1〜6）は importance（読み始める優先度 A〜E）とは独立した軸
