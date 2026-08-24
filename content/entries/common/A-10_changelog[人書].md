---
id: A-10
title: 更新履歴と更新方針
category: common
subtype: meta
experience_level: research_only
reader_level: 1
importance: A
page_layout: front_log_glossary
spread_position: left
evaluation_date: 2026-05-13
related_terms:
  - A-1 まえがき
  - A-6 評価日・時変情報の見方
  - A-11 略称表記
status: needs_review
---

# 更新履歴と更新方針

このページは前付け 7 見開きの 7 番目（更新履歴と略称）の左ページです。右ページは A-11（略称表記）。横向きタイムラインで本書の主要更新を見せます。

## リード文

本書は AI 業界の動きに合わせて随時更新します。各エントリには `evaluation_date` を必ず付け、いつ時点の記述かが分かる作りにしています。

## 主要更新（横向きタイムライン）

- **2026-04-21** 要件定義 — 本書のコンセプト確定
- **2026-04-25** v2 レイアウト凍結 — 見開き 2 ページの構造を確定
- **2026-04-28** スケルトン運用開始 — 全候補 339 件のスケルトン先行生成
- **2026-04-30** 並列本書き完走 — 245 件本書き、残スケルトン 42 件
- **2026-05-13** 前付け 7 見開き再構成 — A 章を front_* レイアウトに移行

## 次に変わる予定

- 巻末索引（letter 順／五十音順／アルファベット順）の本物実装
- B〜J 章エントリの著者欄記入（needs_review → ready 昇格）
- 残スケルトンの本書き完走

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### 左ページ全面（横向きタイムライン）

- 描く内容: 上半分に横向きタイムライン（左→右に時間流）、各マイルストーンに日付＋短ラベル
- 下半分に「次に変わる予定」枠を点線囲みで配置
- タイムラインの線は薄青、マイルストーンの点は濃青
- 線画・濃紺主体。余白を広く取って読みやすく

## 出典メモ

- 旧 A-10 changelog（2026-04-30 版）— 更新運用の発想を継承
- [docs/front_section_layout.md](../../../docs/front_section_layout.md) §6 残作業 — checked 2026-05-13
- [ledgers/next_session_handoff.md](../../../ledgers/next_session_handoff.md) — checked 2026-05-13

## 備考

- 旧 spread_v1 版（2026-04-30）の tagline・6 視点・開発フロー・著者欄は v0.2 改訂で廃止
- A-10 は同居 layout `front_log_glossary` の左ページ担当（`spread_position: left`）
- 詳細な開発ログは `ledgers/next_session_handoff.md` を参照。本ページは読者向けの「主要更新」要約に絞る
