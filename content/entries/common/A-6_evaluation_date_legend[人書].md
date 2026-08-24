---
id: A-6
title: 評価日・時変情報の見方
category: common
subtype: meta
experience_level: research_only
reader_level: 1-2
importance: A
page_layout: front_legend_marks
spread_position: right
evaluation_date: 2026-05-13
related_terms:
  - A-1 まえがき
  - A-3 図鑑の歩き方
  - A-4 体験区分の凡例
  - A-10 更新履歴と更新方針
status: needs_review
---

# 評価日・時変情報の見方

このページは前付け 7 見開きの 5 番目（注意マーク凡例）の右ページです。左ページの A-4／A-5 と対をなし、評価日と時変フラグの読み方をまとめます。

## リード文

各エントリの記述が「どの時点のものか」を示す凡例です。AI 業界の速い変化に備えるための見方を覚えてください。

## 3 つの時変フラグ

- **`evaluation_date`**（評価日・必須）: そのエントリを書いた／確認した日付（YYYY-MM-DD）。料金・モデル名・プレビュー状況など、時期で変わる情報は「この日時点では…」と読みます
- **`version_status`**（任意）: モデルやサービスの状態。`active` / `preview` / `deprecated` の 3 値
- **`pricing_note`**（任意）: 料金の発生有無。`none` / `paid` / `freemium` の 3 値

`version_status` または `pricing_note` を載せたエントリは、本文の出典メモに `checked YYYY-MM-DD` 形式で確認日を必ず添えます。

## 誌面での見え方

評価日はエントリ左ページ下チロムの `2026.05 · Draft` のような書式で表示します。時変フラグはタグライン帯付近に小さなバッジで示し、`Preview` `Deprecated` などの英語短文が見えます。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### 右ページ全面（評価日凡例）

- 描く内容: カレンダー＋時計のアイコンを上部に配置、下に 3 つの時変フラグを縦並びで説明
- 各フラグの説明は 14px、enum 値はコードフォントで青系のバッジに
- 右下に「本書のモデル・料金は時点情報。現在の状況は公式を確認」の注記 1 行
- 線画・濃紺主体・余白多め。アイコンは塗りつぶし最小限

## 出典メモ

- 旧 A-6 evaluation_date_legend（2026-04-30 版）— 時変情報発想を継承
- [docs/entry_schema.yaml](../../../docs/entry_schema.yaml) `frontmatter.time_varying_required` — checked 2026-05-13

## 備考

- 旧 spread_v1 版（2026-04-30）の tagline・6 視点・開発フロー・著者欄は v0.2 改訂で廃止
- A-6 は同居 layout `front_legend_marks` の右ページ担当（`spread_position: right`）
- 本エントリ自体は時変情報を含まないため、`version_status` / `pricing_note` は YAML に置きません
- 詳細な更新方針・履歴は A-10 で扱います
