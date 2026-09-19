# 鮮度監査ログ（手で書く台帳）

*「いつ・どの範囲を・何を見て確認し、何を直したか」を残す監査履歴です。自動生成の [freshness_queue.md](freshness_queue.md) と対で使います。*

キューは「今どこが古いか」のスナップショットなので、時間が経つと上書きされて消えます。
**何をもって「確認した」と言えるのか**を後から辿れるように、監査した範囲はここに 1 行足してください。
刊行前に「この本の事実はいつ時点のものか」を説明する根拠にもなります。

## 書き方

| 日付 | 範囲 | 件数 | 見た一次情報 | 結果 | 記入者 |
| :-- | :-- | --: | :-- | :-- | :-- |

- **範囲**: `D 章 model 全件` / `B-1〜B-12` / `F-model-anthropic の影響エントリ`（[volatile_facts.md](volatile_facts.md) の事実 ID）のように、後から再現できる粒度で
- **見た一次情報**: 公式ドキュメント・料金ページ・リリースノートなど。URL は代表 1 本で構いません
- **結果**: `変更なし（last_audited のみ更新）` / `n 件改訂（内容）` のように、直したか直していないかが分かるように
- 確認したエントリは frontmatter の `last_audited` を確認日に更新してください。`evaluation_date` は執筆時点の記録なので動かしません

---

## 履歴

| 日付 | 範囲 | 件数 | 見た一次情報 | 結果 | 記入者 |
| :-- | :-- | --: | :-- | :-- | :-- |
| 2026-09-19 | 仕組み導入（監査はまだ未実施） | — | — | `last_audited` / `volatility` を schema v2.31.0 に追加し、`scripts/audit_freshness.py` と `freshness_queue.md` を新設。初回走査で Tier S の期限超過 131 件（service 38 / model 34 / benchmark 19 / mcp 11 / その他 29）を検出 | Claude Code |
| 2026-09-19 | 時変ファクト watchlist を新設（監査はまだ未実施） | — | — | `volatile_facts.yaml` に事実 15 件を定義し、`update_volatile_facts.py` が影響エントリを自動収集する形に。`touch_last_audited.py` で確認済みの一括押印も可能に。15 件すべて `last_checked` 未記入＝未確認の状態 | Claude Code |

---

## 未監査の残り（2026-09-19 時点）

初回走査の結果です。上から束で片付けるのが速い順に並べています。

| 優先 | 範囲 | 件数 | 確認ポイント |
| :-- | :-- | --: | :-- |
| 1 | D 章 model | 34 | 後継モデルの有無・提供終了・コンテキスト長。一次情報が各社 1 ページに集まるので最も安く回せます |
| 2 | B 章 service | 38 | 料金プラン・無料枠・名称変更。`価格` シグナルが出ているものを優先 |
| 3 | E 章 benchmark | 19 | スコアと上位モデルの入れ替わり。数字の裏取りが要るので時間がかかります |
| 4 | I 章 mcp | 11 | 公式／コミュニティの別・配布場所・対応クライアント |
| 5 | その他（person_org 7 / term_tool 6 / term_general 6 / term_llm 5 / tool_agent 4 / history 1） | 29 | Tier 判定が実態と合わないものは `volatility: low` で落とす |

最新の内訳は `python3 scripts/audit_freshness.py` を走らせて [freshness_queue.md](freshness_queue.md) を見てください。
