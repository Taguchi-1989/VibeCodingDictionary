# 前付け（A 章）の例外レイアウト仕様

*2026-05-13 起票・同日 v0.2 改訂。A 章（A-1〜A-11）は本書の前付けで、用語エントリ用の `spread_v1` テンプレでは内容が空転します。前付け部分だけ独自のレイアウトを許容する例外仕様をここに集約します。本書本体（B〜J 章）の `spread_v1` には影響しません。*

**原典への接続**: [docs/v2_rules_summary.md](v2_rules_summary.md) §1〜2 の `spread_v1` を「本編の標準」として温存し、本書冒頭の 7 見開きだけが本仕様で動きます。

## 1. なぜ例外にするのか

A 章は辞書本体ではなく、**読者が本編に入る前に渡す「使い方」と「凡例」**です。`spread_v1` の以下の節は前付けでは意味が立ちません。

- `tagline` 青帯（用語の言い換えではなく一歩先の定義）
- 「どこで出会うか」（前付けに「出会う」場面はない）
- 6 視点（役割／うれしさ／注意点／…）
- 「開発フローでの位置」（メタ情報に開発フローはない）

スケルトンを `spread_v1` で埋めてきたため、現状の A-1〜A-11 は無理やり書かれた節が並んでいます。前付けを「ビジュアル先行・節構造自由」にすることで、本来の役割（読み方・凡例・索引）に戻します。

## 2. 構成（圧縮案 5 見開き＋巻末）

A-1〜A-11 の 11 エントリを、**前付け 5 見開き＋巻末 1 見開き**に再編成します（2026-06-13 更新。旧「重め 7 見開き」から圧縮案へ切替。経緯は [drafts/front_section/page_count_plan.html](../drafts/front_section/page_count_plan.html)）。ID は維持し、複数 ID を 1 見開きに同居させるときは **同じ `page_layout` 値を共有させる**ことで束ねます（`spread_group` 別フィールドは設けない。§4-2）。

圧縮の要点は 2 つ:

1. **扉とまえがきを 1 見開きに統合**（左＝扉コピー「知らないことばで、止まらない。」＋ 3 コマ、右＝まえがき本文）。重複していた「読み方ミニチュア」は分解図（A-2）と被るため扉から外し、「ことばの橋」イラストは外してまえがき右ページにリード 1 文だけ残す。統合 HTML は [drafts/front_section/1_concept_preface.html](../drafts/front_section/1_concept_preface.html)。旧 `0_concept_spread.html` / `1_a1_preface.html` は参照用に残置。
2. **更新履歴・略称（A-10 + A-11）を巻末へ移動**。前付けを軽くし、参照系は巻末でまとめて引けるようにする。

| # | 構成 ID | 見開き名 | layout 名 | 位置 |
| :-: | :-- | :-- | :-- | :-- |
| FR-01 | `front_concept` + A-1 | 扉＋まえがき（統合） | `front_concept_preface` | 前付け |
| FR-02 | A-2 | 見開きの読み方（分解図） | `front_anatomy` | 前付け |
| FR-03 | A-3 | 図鑑の歩き方と語の探し方 | `front_map_index` | 前付け |
| FR-04 | A-4 + A-5 + A-6 + A-8 | この本の記号と凡例（1 見開きに集約） | `front_legend_all` | 前付け |
| BK-1 | A-10 + A-11 | 更新履歴と略称 | `front_log_glossary` | 巻末 |
| BK-2 | A-9 | 全件索引（総目次） | `back_full_index` | 巻末 |

2026-06-13〜14 の追加変更（編集判断）:

- **A-9 ミニ索引を廃止**し、**巻末に全件索引（全 354 語を章 A〜J ごと・ID 順に列挙）**を新設。[scripts/build_full_index.py](../scripts/build_full_index.py) が entries.csv から [drafts/front_section/9_full_index.html](../drafts/front_section/9_full_index.html) を生成。FR-03 の右ページは「語の探し方」（3 ルート＋巻末索引への誘導）に置き換え。§7 の「巻末索引はスコープ外」は撤回。
- **A-7 図のタイプの凡例ページを廃止**（しょぼい・本文側で `figure_type` 指定すれば足りる判断）。
- **凡例を 1 見開きに集約**：旧 FR-04（A-4 体験区分／A-5 読者レベル／A-6 評価日・時変）＋旧 FR-05（A-8 色・記号）が 4 ページに薄く広がって余白だらけだったため、[drafts/front_section/4_legend_all.html](../drafts/front_section/4_legend_all.html) に統合（左＝読む前の区分、右＝誌面に出る記号）。4 ページ→2 ページ。旧 `4_a4_a5_a6_legend_marks.html` / `5_a7_a8_swatch.html` は参照用に残置。
- 結果、**前付けは 4 見開き**（FR-01〜FR-04）＋巻末（更新履歴・略称／全件索引）。

> 旧 7 見開き構成（扉単独・まえがき単独・A-7 図タイプ・A-9 ミニ索引・A-10/A-11 前付け）は §3 以降の各 layout 設計の記述を流用しています。FR-01 の設計は旧「0. 扉」＋「1. A-1 まえがき」を 1 見開きに圧縮したものとして読んでください。

## 3. 各見開きの設計

各見開きは「左右ページの主役」を 1 つに絞り、残りは余白と装飾で支えます。文字量は `spread_v1` より一段軽い前提（各 layout の目安は §4-5）です。

### 0. 扉  `front_concept_spread`

**主役**: 1 枚絵で「知らないことばで止まる → 引く → 戻る」を見せる。

- 左ページ: 「知らないことばで、止まらないために。」のコピー＋抽象人物のイラスト 3 コマ（困る／引く／戻る）
- 右ページ: 「1 項目は見開き 2 ページ。左でつかみ、右で使う。」のコピー＋見開きミニチュア（実際の `spread_v1` の縮小サムネを置き、6 つの場所を矢印で指す）
- 既存資産: [assets/opening/opening-spread-concept.png](../assets/opening/opening-spread-concept.png) を出発点に使えます
- 文字量目安: 左 80〜120 字／右 80〜120 字。タイトル無し、ページ番号無し、章ラベル無し
- YAML: `id: front_concept`（letter ID とは別系統、`^front_` 接頭辞ルール）、ledger 外。詳細は §4-3

### 1. A-1 まえがき  `front_essay`

**主役**: 著者の声で書く巻頭言。

- 左ページ全面: 大判の「ことばの橋」イラスト 1 枚＋短いリード文（30〜50 字）
- 右ページ: 縦組み風の本文 2 段（合計 350〜500 字）。「同じ日本語を話していても、同じ言語空間にいるとは限りません。」を冒頭に据える
- 既存テンプレの 6 視点・開発フロー・関連用語・つまずき・私のコメントは**置かない**
- 著者欄（私のコメント）も置かない。前付けは著者ボイスそのものなので、別欄にする必要が無いため

### 2. A-2 見開きの読み方（分解図）  `front_anatomy`

**主役**: 本編 1 エントリの実物見開きの注釈図。

- 見開き全面に **実物大の `spread_v1` 1 枚を半透明で敷き**、コールアウト矢印で各部位を指す
- 指す対象: タイトル ／ 読み ／ tagline 青帯 ／ 何をしてくれるか ／ どこで出会うか ／ メイン図 ／ ポンチ絵 ／ 会話での使い方例 ／ 6 視点 ／ 開発フロー ／ 関連用語 ／ 著者欄（つまずき・私のコメント）／ 参考 URL
- コールアウトは 1 件 20〜40 字以内
- 注釈の「下地」サンプルには TypeScript（F-2 など実書済みの定番エントリ）を使うと、本書のトーンが伝わります

### 3. A-3 + A-9 図鑑の歩き方と索引  `front_map_index`

**主役**: A〜J の地図とミニ索引。

- 左ページ（`spread_position: left`、A-3 担当）: A〜J を円環または横並びの地図にして、章ごとのテーマラベルを置く。読者レベル別の推奨ルート 3 本（Lv1 はここから／Lv3 はここから／Lv5 はここから）を色違いの線で重ねる
- 右ページ（`spread_position: right`、A-9 担当）: **ミニ索引（A〜J 各章の代表語 3〜5 個ずつ）** を表形式で置く。letter 順 ／ 五十音順 のどちらをいつ使うかも 1 文ずつ書く
- A-3 と A-9 の本文は短く要約（合計 300〜450 字）
- **巻末の本物索引はスコープ外**（§7 参照）。A-9 spread の右ページミニ索引で自己完結させる前提

### 4. A-4 + A-5 + A-6 注意マーク（凡例）  `front_legend_marks`

**主役**: 各エントリに付くマーク／タグ／日付の見方をまとめて 1 見開きに。

- 左ページ: 「体験区分」（A-4）と「読者レベル」（A-5）のタグ凡例。アイコン＋短い説明を 2 行ずつ
  - 体験区分: `hands_on` / `partial` / `research_only`
  - 読者レベル: 1〜6 を縦の階段で表現し、各段に「読める語の例」を 2〜3 個
- 右ページ: 「評価日・時変情報」（A-6）の凡例。`evaluation_date` ／ `version_status` ／ `pricing_note` がなぜ要るかを 1 ブロック（80〜120 字）＋例示
- 3 つの A エントリの本文は各 80〜120 字に圧縮。`spread_position`: A-4 / A-5 は left、A-6 は right

### 5. A-7 + A-8 図と色の見本帳  `front_swatch`

**主役**: 本書で使う図のタイプとカラー／記号の物理サンプル。

- 左ページ（A-7）: 「図のタイプ」のカタログ。`structure` / `timeline` / `comparison` / `before_after` / `workflow` のミニサムネ 5 枚を 2 段グリッドで並べ、各 1 行で「いつ使う図か」
- 右ページ（A-8）: 「色・記号」のスウォッチ。
  - 青のトーン（タグライン帯・dashed 枠・参考 URL リンク）
  - ☆ 違反 ／ ⚠ 警告のバッジ
  - 私のコメントの 4 種（★/✓/!/☺）と意味
  - 関連用語ピル、6 視点アイコン
- 装飾より「実物が並んでいる」ことが大事。文字は最小限（合計 250〜350 字）

### 6. A-10 + A-11 更新履歴と略称  `front_log_glossary`

**主役**: 機能的な前付け（リファレンス）。

- 左ページ（A-10）: 「更新履歴」。横向きタイムライン。`evaluation_date` の運用と「次に何が変わる予定か」枠
- 右ページ（A-11）: 「略称表記」。略称 ／ 正式名称 ／ 読み ／ 初出ページ の 4 列表。CC＝Claude Code、MCP＝Model Context Protocol、a11y＝accessibility 等
- 文字装飾は最小、表とタイムラインのレイアウトが主役

## 4. YAML への影響

### 4-1. `page_layout` enum 拡張

| 取りうる値 | 用途 |
| :-- | :-- |
| `spread_v1` | 本編（B〜J 章）。既存仕様維持 |
| `front_concept_spread` | 扉 |
| `front_essay` | A-1 まえがき |
| `front_anatomy` | A-2 見開きの読み方 |
| `front_map_index` | A-3 + A-9 |
| `front_legend_marks` | A-4 + A-5 + A-6 |
| `front_swatch` | A-7 + A-8 |
| `front_log_glossary` | A-10 + A-11 |

`docs/entry_schema.yaml` の `frontmatter.required[page_layout].enum` をこの 8 値に拡張します。

### 4-2. 同居の仕組み

**`spread_group` 別フィールドは導入しない**（v0.1 案から変更）。1 layout = 1 見開き が確定しているため、同じ `page_layout` 値を持つエントリは同居と解釈します。複数エントリが同居する layout でだけ、新設の **`spread_position`** で左右どちらの面を担当するか明示します。

```yaml
page_layout: front_map_index   # 同値を持つ A-3 と A-9 は同居
spread_position: left          # left / right / full （単独 layout は full または省略）
```

- 単独で 1 見開きを占める layout（`front_concept_spread` / `front_essay` / `front_anatomy`）には `spread_position` は不要
- 将来 1 layout で別 group が必要になった時点で改めて `spread_group` を導入する

### 4-3. 扉エントリの YAML 規約

扉見開きは **letter ID 体系の外**に置く前付けです。

- ファイル: `content/frontmatter/00_concept_spread.md`
- `id`: `front_concept`（letter ID `^[A-J]-\d{1,2}$` とは別系統。validator は `^front_` 接頭辞 ID を別経路で受け入れる）
- `page_layout`: `front_concept_spread`
- `status`: 通常通り `drafting` → `needs_review` → `ready` で運用するが、**自動昇格（drafting → needs_review）は `front_*` レイアウトでは停止**（前付けは著者本人レビュー前提のため）
- ledger `entries.csv` には載せない（339 件カウントは A-1〜A-11 のみ）

### 4-4. `figure_type` と `related_terms` の任意化

`front_*` レイアウトでは、用語エントリ用の必須キーの一部が意味を持ちません。layout ごとに必須／任意を切り替えます。

| layout | `figure_type` | `related_terms` | `version_status` / `pricing_note` |
| :-- | :-: | :-: | :-: |
| `front_concept_spread` | 任意 | 任意 | 不要 |
| `front_essay` | 任意 | 任意 | 不要 |
| `front_anatomy` | 任意 | 任意 | 不要 |
| `front_map_index` | 任意 | 3〜5（A-3／A-9 それぞれに付与） | 不要 |
| `front_legend_marks` | 任意 | 3〜5（A-4／A-5／A-6 それぞれ） | 不要 |
| `front_swatch` | 任意 | 任意 | 不要 |
| `front_log_glossary` | 任意 | 任意 | 不要 |

「任意」は YAML キー自体を省略可（あっても空でよい）。validator はこのテーブルを参照して必須／任意を切り替えます。

### 4-5. 字数判定（page_totals の扱い）

`front_*` レイアウトでは `docs/entry_schema.yaml` の `page_totals` 判定（左 155-250 / 右 220-430 ＋ ☆ 違反 +100）を**全面スキップ**します。代わりに layout ごとの緩い目安だけを置きます（validator は警告のみ、☆ にしない）。

| layout | 左ページ目安 | 右ページ目安 |
| :-- | :-- | :-- |
| `front_concept_spread` | 80〜120 字 | 80〜120 字 |
| `front_essay` | 30〜50 字（リード） | 350〜500 字（本文） |
| `front_anatomy` | コールアウトのみ（合計 200〜300 字） | 同左 |
| `front_map_index` | 150〜250 字（地図） | 150〜250 字（ミニ索引） |
| `front_legend_marks` | 200〜300 字（タグ／レベル凡例） | 100〜180 字（評価日凡例） |
| `front_swatch` | 100〜180 字（図カタログ） | 100〜180 字（色・記号） |
| `front_log_glossary` | 履歴 1 ブロック＋表 | 略称 4 列表（本文文字量は最小） |

## 5. validator・generator・hook への影響

このセクションは別タスク。仕様確定後にスクリプト側を改修します。**仕様 §4 を validator が読む前に本文整理を進めると ☆ 違反だらけになるため、改修を先に行います**（§6 順序）。

### [scripts/validate_entry.py](../scripts/validate_entry.py) 改修項目

- L252 の `page_layout != "spread_v1"` 警告を撤廃。代わりに `page_layout` 値で分岐するハンドラを用意し、`front_*` は別ルールセットで判定
- `front_*` レイアウト時、`check_structure` の必須節リスト（`## tagline` / `## 何をしてくれるか` / `## どこで出会うか` / `## メイン図` / `## 会話での使い方例` / `## 関連用語` / `## この用語の見どころ` / `## 開発フローでの位置（必須）` / `## 非エンジニアのつまずき` / `## 私のコメント`）と必須サブ節（6 視点）の検査を**全スキップ**
- `front_*` レイアウト時、`SECTION_TARGETS` の字数チェックと `page_totals` 判定を**スキップ**。代わりに §4-5 の layout 別目安で警告のみ
- `front_*` レイアウト時、`figure_type` `related_terms` の必須チェックを §4-4 の表で切り替え
- `id` フィールドの正規表現に `^front_[a-z_]+$` を追加（letter ID と OR）
- `^front_` 接頭辞 ID は自動昇格対象から除外（drafting に留まる）

### [templates/skeleton_template.md](../templates/skeleton_template.md) 改修

- `page_layout: spread_v1` を本編の既定値として温存
- 前付け用のスケルトンテンプレートは `templates/skeleton_front_template.md`（新設）として layout 別に分岐。少数なので最初は手書きでもよい

### [scripts/update_review_queue.py](../scripts/update_review_queue.py) 改修

- L44 `ENTRIES_DIR = PROJECT_ROOT / "content" / "entries"` に加えて `content/frontmatter/` も巡回対象に追加
- `ledgers/revision_queue.md` の集計に「前付け」セクションを 1 つ追加し、扉＋ A-1〜A-11 を 7 見開き単位で見えるようにする

### [.claude/settings.json](../.claude/settings.json) Hook

- `PostToolUse` の `matcher: "Edit|Write|MultiEdit"` は維持。`content/frontmatter/` 配下の保存も hook 発火対象（matcher はパスを見ていないので自動で拾う）

### [.claude/agents/entry-writer.md](../.claude/agents/entry-writer.md) 改修（優先度：低）

- 前付けエントリは件数が少なく、手書きでも回るため、当面は entry-writer に front_* 用プロンプトを足さない
- A-3〜A-11 を再構成する段になって作業量が見えてきたら、`entry-writer-front` のような layout 別サブエージェントを切り出す判断をする

## 6. 残作業（順序を組み替え）

優先順:

1. **本仕様の合意** — このドキュメント v0.2 を確認 → 承認
2. **validator・スキーマ改修を先に**（§5 の `validate_entry.py` ／ `entry_schema.yaml` ／ `update_review_queue.py`）— `front_*` を許容、必須節チェックを layout で分岐、`content/frontmatter/` を巡回対象に追加、自動昇格を `front_*` で停止
3. **扉エントリ新規執筆** — `content/frontmatter/00_concept_spread.md` を書く。validator が静かにパスすることを確認
4. **A-1〜A-11 の YAML 差し替え** — 1 件ずつ `page_layout` を `front_*` 系に差し替え、必要な layout に `spread_position` を追加
5. **A-1〜A-11 の本文整理** — 各見開きの設計（§3）に合わせて節を入れ替え。`spread_v1` 用に書かれた tagline・6 視点・開発フローは前付け版では削るか転用
6. **デザイン担当への引き渡し** — 7 見開きぶんのレイアウト指示書（本ドキュメント §3 がベース）。本編 `spread_v1` とは別系の HTML/CSS が要る

## 7. スコープ外（別仕様で扱うもの）

- **巻末索引（letter 順／五十音順の本物索引）**: 本書末尾の専用ページ。本仕様では扱わず、[docs/back_matter_layout.md](back_matter_layout.md)（2026-09-04 作成）で別途。A-9 spread の右ページにミニ索引を載せることで、本書前付けは自己完結します
- **本編 `spread_v1`**: [docs/v2_rules_summary.md](v2_rules_summary.md) の管轄。前付け仕様は本編を一切変更しません

## 8. 開いておくべき関連ファイル

- [drafts/opening_spread_brief.md](../drafts/opening_spread_brief.md) — 扉見開きの最初のブリーフ。§3-0 はここを継承
- [drafts/opening/opening-spread-annotated.html](../drafts/opening/opening-spread-annotated.html) — 扉見開きの注釈版モック
- [assets/opening/opening-spread-concept.png](../assets/opening/opening-spread-concept.png) — 扉のコンセプト画像
- [content/entries/common/A-*.md](../content/entries/common/) — 既存 11 エントリ。本仕様で再編成対象
- [docs/v2_rules_summary.md](v2_rules_summary.md) — 本編 `spread_v1` の確定仕様（こちらは触らない）
- [docs/entry_schema.yaml](entry_schema.yaml) — §4 の改修対象
- [scripts/validate_entry.py](../scripts/validate_entry.py) — §5 の改修対象
