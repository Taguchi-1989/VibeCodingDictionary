# バイブコーディング図鑑 (VibeCodingDictionary)

非エンジニア・周辺職種の人が、AI 開発まわりの語彙を「辞書引き」できるようにする図鑑プロジェクトです。
詳細な趣旨は [docs/book_philosophy.md](docs/book_philosophy.md)、編集ガイドは [CLAUDE.md](CLAUDE.md) を参照してください。

## 読者像

- AI を仕事で使いたいが、プログラミングで生計を立てているわけではない人
- 打ち合わせで「コンテキストが足りない」と言われたとき、Claude と ChatGPT の違いを聞かれたとき、AI への指示が思うように返ってこないとき、手元で引きたい人
- 完全な入門書ではなく、現場の会話の前提をそろえるための共通語彙集として

## 開発状況（at a glance）

| 指標 | 値 |
|:--|--:|
| エントリ総数 | 461 件（A〜J 章） |
| ☑ 完成 (ready) | 387 件 |
| ✍ 著者書き待ち (needs_review) | 66 件 |
| ⛬ archived | 7 件 |
| ポンチ絵 PNG あり | 390 件（`assets/ponchi/final/`） |

## ディレクトリ構成

```
content/
  entries/         本のエントリ本文（A-1〜J-100、全 327 件）
docs/              編集方針・仕様（スキーマ・スタイル・前付け仕様 等）
templates/         エントリ・スケルトンのテンプレート
ledgers/           編集台帳（候補一覧・進行状況・要直しキュー）
scripts/           自動化スクリプト（生成・検証・索引）
drafts/
  prototypes/      v2 誌面プロトタイプ（HTML / CSS / 検証ツール）
  front_section/   前付け 7 見開きの HTML たたき台
  back_section/    あとがき HTML たたき台
  reading_routes/  読者タイプ別おすすめルート HTML
  search/          全 327 件の検索 UI（HTML 単体で動作）
  IMAGE_GEN_TODO.md 画像生成枠の集約
skills/            執筆・取り込みスキル
.claude/           Claude Code 用エージェント設定
```

## 主なスクリプト

| スクリプト | 用途 |
|:--|:--|
| `scripts/generate_skeleton.py` | エントリのスケルトン生成（YAML + 必須節） |
| `scripts/validate_entry.py` | エントリ検証（字数・構造・トーン）。保存時に自動実行 |
| `scripts/update_review_queue.py` | `ledgers/revision_queue.md` の自動更新 |
| `scripts/sync_entries_csv.py` | `ledgers/entries.csv` をディスクの最新 path に同期 |
| `scripts/preview_gen.py` | 開発用 HTML プレビュー生成 |
| `scripts/build_search_index.py` | 検索 UI のインデックス生成・HTML 注入 |

## 主要ドキュメント

- [docs/v2_rules_summary.md](docs/v2_rules_summary.md) — v2 確定ルール総覧（執筆前に最初に読む）
- [docs/entry_schema.yaml](docs/entry_schema.yaml) — 字数・必須節の機械可読版
- [docs/editorial_style.md](docs/editorial_style.md) — トーン・文体の原則
- [docs/component_spec_v2.md](docs/component_spec_v2.md) — 実装担当（Astro + React）への引き渡し仕様
- [docs/front_section_layout.md](docs/front_section_layout.md) — 前付け（A 章）の例外レイアウト仕様
- [drafts/front_section/page_count_plan.html](drafts/front_section/page_count_plan.html) — 前付け・後付けのページ数設計 HTML
- [templates/entry_template.md](templates/entry_template.md) — エントリの構造テンプレート

## 監視レポート（コミット対象）

- [ledgers/revision_queue.md](ledgers/revision_queue.md) — validator 自動生成、要レビュー一覧
- [ledgers/author_fill_queue.md](ledgers/author_fill_queue.md) — 著者欄記入待ちのエントリ
- [ledgers/writing_priority.md](ledgers/writing_priority.md) — 執筆優先度
- [ledgers/next_session_handoff.md](ledgers/next_session_handoff.md) — 次セッション引き継ぎ

## ID 体系

A〜J の 10 区切り、10 番刻みのサブ範囲。欠番は詰めず、追加は空き番号のみ。詳細は [docs/id_scheme.md](docs/id_scheme.md)。

## ライセンス

本リポジトリは **デュアルライセンス** で公開しています。コードと本文で適用範囲を分けています。

| 対象 | ライセンス | 詳細 |
|:--|:--|:--|
| **ソースコード**（`scripts/` / `drafts/**/*.html` の構造・CSS・JS） | **MIT License** | [LICENSE](LICENSE) |
| **本の中身**（`content/entries/**/*.md` / `docs/` / 本文テキスト） | **CC BY-SA 4.0** | [LICENSE-CONTENT.md](LICENSE-CONTENT.md) |

### あなたができること

- **読む・引用する** — 制限なし。SNS で紹介・記事で引用・授業教材で配布、すべて OK
- **改変・派生作品を作る** — OK。「ライセンス」と「著者表示」を継承してください
- **商用利用** — OK（CC BY-SA 4.0 は営利目的を含む）
- **再配布** — OK。元の出典（著者名 / リポジトリ URL）の明記をお願いします
- **派生作品の公開** — OK。ただし**同じ CC BY-SA 4.0** で公開する必要があります（継承条項）

### クレジット表記例

```
Based on "バイブコーディング図鑑 (VibeCodingDictionary)" by Taguchi-1989,
licensed under CC BY-SA 4.0.
https://github.com/Taguchi-1989/VibeCodingDictionary
```

## 貢献について

Issue や PR、誤字脱字の指摘、新規エントリの提案、いずれも歓迎します。プロジェクトの方針は [docs/book_philosophy.md](docs/book_philosophy.md)、執筆スタイルは [docs/editorial_style.md](docs/editorial_style.md) を先にご一読ください。

ローカル開発の流れ：

1. リポジトリを fork して clone
2. `python3 scripts/generate_skeleton.py {ID}` で新規エントリの骨格生成
3. テンプレに沿って執筆
4. 保存時 `scripts/validate_entry.py` が自動で字数・構造を検証
5. `status` を `needs_review` まで上げて PR

## リポジトリ

<https://github.com/Taguchi-1989/VibeCodingDictionary>（`main` ブランチ）
