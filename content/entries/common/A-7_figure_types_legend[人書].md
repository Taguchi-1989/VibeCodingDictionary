---
id: A-7
title: 図のタイプ
category: common
subtype: meta
experience_level: research_only
reader_level: 1
importance: A
page_layout: front_swatch
spread_position: left
evaluation_date: 2026-05-13
related_terms:
  - A-1 まえがき
  - A-2 この本の読み方
  - A-3 図鑑の歩き方
  - A-8 色・記号の凡例
status: needs_review
---

# 図のタイプ

このページは前付け 7 見開きの 6 番目（図と色の見本帳）の左ページです。右ページは A-8（色・記号）。本書で使う 5 種類の図タイプを実物サムネで並べます。

## リード文

各エントリのメイン図は、内容に合った 5 つのタイプから 1 つを選びます。タイプ名は YAML の `figure_type` フィールドで管理します。

## 5 タイプのカタログ

- **structure**（概念図） — 中心概念と周辺要素の関係を示す。例: A-3 の A〜J 地図
- **timeline**（時系列） — 時間軸に沿った変化や歴史。例: H 章の各エントリ、A-10 更新履歴
- **comparison**（対比） — 2 つ以上の選択肢を並べて違いを見せる。例: B-1 と B-2 の比較
- **before_after**（前後） — 「触る前／触った後」「使う前／使った後」の対比
- **workflow**（手順） — 開始から終了までの流れ。例: 開発フロー図

## どこに使うか

エントリの主役図（メイン図）と、左ページ最下段の擬人化ポンチ絵スロットは独立。`figure_type` で指定するのはメイン図側のみです。

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### 左ページ全面（図タイプ カタログ）

- 描く内容: 5 タイプのミニサムネを 2 段グリッド（上段 3 枚、下段 2 枚）で並べる
- 各サムネ下に英名と日本語名、その下に 1 行で「いつ使う図か」
- サムネは 80x60px、本編のメイン図の縮小版を流用
- 線画・濃紺主体。サムネだけ実物色で塗る

## 出典メモ

- 旧 A-7 figure_types_legend（2026-04-30 版）— 5 タイプの発想を継承
- [docs/entry_schema.yaml](../../../docs/entry_schema.yaml) `frontmatter.required.figure_type` — checked 2026-05-13

## 備考

- 旧 spread_v1 版（2026-04-30）の tagline・6 視点・開発フロー・著者欄は v0.2 改訂で廃止
- A-7 は同居 layout `front_swatch` の左ページ担当（`spread_position: left`）
- `figure_type` 自体は本編 spread_v1 では必須、前付け front_* では任意（[docs/front_section_layout.md](../../../docs/front_section_layout.md) §4-4）
