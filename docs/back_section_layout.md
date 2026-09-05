# 巻末付録（back_*）レイアウト仕様

*2026-09-05 作成。前付け仕様 [docs/front_section_layout.md](front_section_layout.md) の巻末版です。*

## 1. 何のための枠か

本編は 1 語 1 見開き（`spread_v1`）で統一されています。ところが**複数の語をまとめて見比べる誌面**は、この枠に入りません。字数の上限に収まらず、6 視点や開発フローという節立ても合いません。

巻末付録（`back_*`）は、そういう「一覧・比較が主役のページ」を、本編のルールを崩さずに置くための枠です。

## 2. 前付け（front_*）との違い

| | front_* | back_* |
| :-- | :-- | :-- |
| 置き場所 | 本編の前 | 本編の後 |
| ファイル | `content/frontmatter/` | `content/backmatter/` |
| ID | `A-1`〜`A-11` ／ `front_concept` | `back_` 接頭辞（letter ID 体系外） |
| 読者の動線 | 最初に読む | 必要になったときに引く |
| 著者記入欄 | 置かない | 置かない |

検証は front_* と同じ軽いルートを通ります（[scripts/validate_entry.py](../scripts/validate_entry.py) の `SPECIAL_LAYOUTS`）。必須節・左右ページ字数合計の判定はかからず、YAML とトーンだけ見ます。`status` の自動昇格もしません（著者本人が上げる）。

## 3. 共通ルール

- `id` は `^back_[a-z_]+$`。**letter ID は振りません**。本編の ID 体系（[docs/id_scheme.md](id_scheme.md)）は触らない、という原則を守るためです
- `page_layout` は `back_*` のいずれか。現在は `back_matrix` の 1 値のみ
- `category: common` / `subtype: appendix`
- **著者記入欄（非エンジニアのつまずき・私のコメント）は置きません**。著者キュー（[scripts/update_author_fill_queue.py](../scripts/update_author_fill_queue.py)）の対象外です
- 本文は「表の読み方」に徹します。事実そのものは本編の各エントリ側に持たせ、付録は重複させません
- トーンは本編と同じです（です・ます調、強い断定を避ける）

## 4. レイアウト別

### 4-1. back_matrix — 一覧・比較の 1 枚

| | 内容 |
| :-- | :-- |
| 左ページ | 比較表（縦 5〜6 行 × 横 4〜5 列）。列の 1 つを「主役の列」に決め、他より強く見せる |
| 右ページ | 2 軸マップ 1 点 ＋ 読み方の本文 150〜250 字 |
| figure_type | 任意（表と 2 軸図が主役なので指定しなくてよい） |
| related_terms | 任意。代わりに「本編への案内」節で ID を並べる |

**行数は増やさないでください。** 1 枚で見渡せることがこのページの価値なので、対象が増えたときは行を足すのではなく、載せるものを選び直します。

現在の割り当て:

| ID | ファイル | 中身 |
| :-- | :-- | :-- |
| `back_standards_matrix` | [content/backmatter/01_standards_matrix.md](../content/backmatter/01_standards_matrix.md) | AI をめぐる規格・ガイドライン 6 つの比較 |
| `back_iso_mapping` | [content/backmatter/02_iso_mapping.md](../content/backmatter/02_iso_mapping.md) | 従来の ISO（9001・27001）と ISO/IEC 42001 の対応。どこまで同じで、どこから AI 固有か |

### 4-2. back_steps — 時間の順に並べる 1 枚

| | 内容 |
| :-- | :-- |
| 左ページ | ステップ（横）× レーン（縦 2 本）の流れ図。上レーン＝従来からやること、下レーン＝それに足されること |
| 右ページ | 記録と担い手の帯 2 段 ＋ 読み方の本文 200〜300 字 |
| figure_type | 任意 |
| related_terms | 任意。「本編への案内」節で ID を並べる |

**上下のレーンは同じ太さで描きます。** 「全部作り直しではなく、隣に 1 本増えるだけ」という見え方自体がこのレイアウトの主張です。ステップは 6 段までに収めてください。

現在の割り当て:

| ID | ファイル | 中身 |
| :-- | :-- | :-- |
| `back_step_map` | [content/backmatter/03_step_map.md](../content/backmatter/03_step_map.md) | AI 導入の 6 ステップ × 「従来からやること／AI で足されること」の 2 レーン |

## 5. 追加するとき

1. `content/backmatter/` に md を置く（連番プレフィクス + slug）
2. 新しいレイアウトが要るなら、`docs/entry_schema.yaml` の `page_layout` enum と末尾の `back_layouts:` 節、`scripts/validate_entry.py` の `BACK_LAYOUTS` の 3 か所を揃えて足す
3. 本節の「現在の割り当て」表に 1 行足す
