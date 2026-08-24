---
id: A-4
title: 体験区分の凡例
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
  - A-3 図鑑の歩き方
  - A-5 読者レベルの凡例
  - A-6 評価日・時変情報の見方
status: needs_review
---

# 体験区分の凡例

このページは前付け 7 見開きの 5 番目（注意マーク凡例）の左ページに同居する 3 エントリのうちの 1 つです。A-5 とともに左ページに置き、A-6 が右ページを担当します。

## リード文

各エントリのタイトル横に表示する、著者が実際にどこまで触ったかの印です。

## 3 段階の記号

- **●** `hands_on` — 業務や個人で動かしたことがある
- **◐** `partial` — 一部のみ触れた／概要を確認した
- **○** `research_only` — 公開情報・他者の体験談ベース

## YAML との対応

エントリの YAML フロントマターでは `experience_level` フィールドで管理します。値は `hands_on` / `partial` / `research_only` の 3 つです。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### 左ページ上段（体験区分）

- 描く内容: ●／◐／○ の 3 つの記号を縦に並べ、各行に 1 文ずつ説明
- 記号サイズは 28px、説明文は 14px、行間は広めに
- A-5（読者レベル）と縦に並ぶレイアウト。A-4 が上、A-5 が下
- 色は本編のタグライン青と同系。記号は塗りつぶしの濃淡で表現

## 出典メモ

- 旧 A-4 experience_legend（2026-04-30 版）— 3 段階の発想を継承
- [docs/entry_schema.yaml](../../../docs/entry_schema.yaml) `frontmatter.recommended.experience_level` — checked 2026-05-13

## 備考

- 旧 spread_v1 版（2026-04-30）の tagline・6 視点・開発フロー・著者欄は v0.2 改訂で廃止
- A-4 は同居 layout `front_legend_marks` の左ページ上段担当（`spread_position: left`）
- 体験区分の値は version_status / pricing_note などの時変フラグとは独立した、固定の品質メタ情報
