# VibeCodingDictionary プロジェクト向け CLAUDE.md

*次のセッションがこのプロジェクトに入ったときに、テイストと構造を外さないようにするための手引きです。毎セッション最初にこのファイルを読む前提。*

## 1. このプロジェクトは何か

非エンジニア・周辺職種の人が、AI 開発まわりの語彙を「辞書引き」できるようにする図鑑。詳細は [docs/book_philosophy.md](docs/book_philosophy.md)。

読者像は **「AI を仕事で使いたいが、プログラミングで生計を立てているわけではない人」**。著者も同じ立場（応用情報・G 検定保持、機械系の開発業務、AI を使う側）。

## 2. 今やっていること

**本書きはほぼ完走**（2026-09-03 時点: ready 348 / needs_review 78 / drafting 1 / archived 7、☆ 違反 0・警告 0。スケルトンは残っていません）。フェーズは執筆から**品質仕上げ・刊行準備**に移っています。

- 現在の内訳と次の作業は [ledgers/revision_queue.md](ledgers/revision_queue.md) で確認（保存ごとに自動再生成）
- 改善課題と追加語候補は [docs/design_improvement_proposal_2026-08.md](docs/design_improvement_proposal_2026-08.md) に集約（仕様同期・品質バグ・表紙・収録語の抜け監査）
- 最終ポンチ絵は `assets/ponchi/final/` に 370 枚差し込み済み。前付け（`drafts/front_section/`）のイラスト 13 枠が残（[drafts/IMAGE_GEN_TODO.md](drafts/IMAGE_GEN_TODO.md)）
- プレビューは `python3 scripts/preview_gen.py` → `drafts/prototypes/preview/`。Cloudflare Pages（`drafts/` を公開）にデプロイ

新規エントリを追加するときは `python3 scripts/generate_skeleton.py B-99` のように単発で生成 →（status を `drafting` に上げて）entry-writer で本書き、の流れは従来どおりです（既存ファイルは絶対に上書きしません）。

## 3. 書くときに必ず守ること

### トーン

- **「です・ます」調で書く**（必須）
- 結論から書く
- 読者を馬鹿にしない、強い断定を避ける

### 構造（[templates/entry_template.md](templates/entry_template.md) の順序・節名に従う）

**確定した全ルールは [docs/v2_rules_summary.md](docs/v2_rules_summary.md) に集約**。執筆前に必ず目を通す。

- **左ページ**：tagline ／ 何をしてくれるか ／ どこで出会うか ／ メイン図 ／ **会話での使い方例**（2026-04-26 追加、25〜50 字 1 文）／ 関連用語（**「ひとことで」は削除、「バイブコーディングでの位置づけ」は「どこで出会うか」にリネーム**）
- **右ページ**：この用語の見どころ（6 視点: 役割／うれしさ／注意点／どこで役立つか／**はじめに**／深掘り先）／ 開発フローでの位置（必須）
- **著者記入欄**（非エンジニアのつまずき ／ 私のコメント＝first/good/bad/who）：**著者本人のみ記入。AI は空スケルトンだけ残す**
- **裏台帳メモ**：誌面ポンチ絵メモ ／ コミュニティ補完メモ ／ 出典メモ ／ 備考

### 書き方の細則

- カタカナ語は初出で日本語訳を補う（例：Context ＝ 文脈）
- 略称は初出で展開（例：CC ＝ Claude Code）
- **タイトルが略称・ヌメロニム（MCP / a11y / LLM 等）なら、tagline 冒頭に正式名称を入れる**（例：`Model Context Protocol の略。…`）。`title_reading` は「英単語をカタカナで並べた読み」（例：`モデルコンテキストプロトコル` / `ラージランゲージモデル` / `アクセシビリティ`）にし、正式名称・日本語訳は入れない（2026-04-28 追加。詳細は [docs/v2_rules_summary.md](docs/v2_rules_summary.md) と [docs/editorial_style.md](docs/editorial_style.md) の「略称・ヌメロニムの扱い」）
- モデル・料金・提供状況は `evaluation_date` つきの時変情報
- 事実と主観を分ける（主観は「私のコメント」欄だけ、AI は触らない）

詳細は [docs/editorial_style.md](docs/editorial_style.md)。

## 4. ID 体系（触らない）

- letter A〜J の 10 区切り固定
- 10 番刻みサブ範囲
- 欠番は詰め直さない
- v0.5 で renumber は終了。以降は **ID を動かさず、追加は空き番号のみ**

詳細は [docs/id_scheme.md](docs/id_scheme.md)。

## 5. デザインは本プロジェクトのスコープ外（ただし v2 仕様は凍結済）

**誌面レイアウト・HTML/CSS・実レンダリング・配色調整の実装は別担当**。本プロジェクトの Claude Code では CSS/React の実装はしません。

ただし、**v2 レイアウト仕様は 2026-04-25 に凍結済み**:

- 仕様サマリ: [docs/v2_rules_summary.md](docs/v2_rules_summary.md)
- プロトタイプ: [drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html](drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html)
- 追加 CSS: [drafts/prototypes/mockups/design_philosophy_v2/overlay.css](drafts/prototypes/mockups/design_philosophy_v2/overlay.css)
- 反復履歴: [drafts/prototypes/mockups/design_philosophy_v2/screenshots/](drafts/prototypes/mockups/design_philosophy_v2/screenshots/) の iter1-21

実装は別担当に渡す。**Claude Code がやるのは markdown ベースの仕様更新・執筆・検証まで**。

- `drafts/prototypes/mockups/` の過去試作は参照用として残す
- テンプレの「構造」（節の順序、裏台帳への記述）は守る
- `誌面ポンチ絵メモ` にはデザイン担当への**指示書**として「何を描きたいか」を残す

## 6. 書く／レビューする／取り込むときの手順書

### 執筆する（自動化：`entry-writer` サブエージェント経由）

- 「B-3 ChatGPT を書いて」のように頼まれたら、[.claude/agents/entry-writer.md](.claude/agents/entry-writer.md) サブエージェントを呼び出す（Agent tool、subagent_type="entry-writer"）。親エージェントは直接書かない
- 手順の本体：[skills/write-entry.md](skills/write-entry.md) Step 0〜7
- 下準備メモ：[ledgers/stage2_briefs.md](ledgers/stage2_briefs.md)（Stage 2 の 46 件ぶん）
- スケルトンが置かれている場合：YAML の `status: skeleton` を `status: drafting` に上げてから entry-writer を呼ぶ

### スケルトン（構造だけ置いた状態）の追加

- テンプレ：[templates/skeleton_template.md](templates/skeleton_template.md)
- ジェネレータ：`python3 scripts/generate_skeleton.py {ID}`（単発）／`--letter B`（letter 単位）／引数なし（未生成全件）
- 既存ファイルは絶対に上書きしません（事故防止）。上書きしたいときは手で削除してから再実行
- CSV の path / status 列も自動で更新

### レビュー／自動チェック

- **保存すると自動で走る**：[scripts/validate_entry.py](scripts/validate_entry.py) が `content/entries/**/*.md` の Edit/Write 後に発火し、字数・構造・トーンを機械チェック（[.claude/settings.json](.claude/settings.json) の PostToolUse hook で設定）
- 手でも走らせられる：`python3 scripts/validate_entry.py content/entries/service/B-1_gemini.md`
- チェック観点：[docs/quality_checklist.md](docs/quality_checklist.md)（特に §H 誌面量の目安）

### 自動昇格・レビューキュー（2026-04-29 追加）

- **自動昇格**：validator が「☆違反 0 ＋ 警告 0」と判定したエントリは、status が `drafting` なら自動で `needs_review` に上がります（[scripts/validate_entry.py](scripts/validate_entry.py) `promote_to_needs_review`）
- **要直しキュー**：保存のたびに [scripts/update_review_queue.py](scripts/update_review_queue.py) が走り、[ledgers/revision_queue.md](ledgers/revision_queue.md) を再生成します。1 画面で「☆違反 / 警告 / 書きかけ / 著者レビュー待ち / 完成」の内訳と該当エントリが見えます
- **著者記入欄キュー**：同じく保存のたびに [scripts/update_author_fill_queue.py](scripts/update_author_fill_queue.py) が走り、[ledgers/author_fill_queue.md](ledgers/author_fill_queue.md) を再生成します。「非エンジニアのつまずき」「私のコメント」が **完了 / 途中 / 手つかず** のどれなのかが 1 画面で見えます。「第一印象だけ書いて止まっている」ような書きかけを拾うのが目的です（2026-09-02 追加）
- **使い方**：`cat ledgers/revision_queue.md` で次にやるべきことを確認 → 該当エントリを直す（手動 or entry-writer 呼び出し）→ 再保存で再評価＋キュー更新
- **`needs_review → ready` も自動昇格します**（2026-09-03 有効化）。著者欄（「非エンジニアのつまずき」＋「私のコメント」4 ラベル）が全部埋まっていること自体が著者レビュー完了の signal なので、そこから ready までは自動です。止めたいときは `VCD_AUTOPROMOTE_READY=0 python3 scripts/update_review_queue.py`（[scripts/validate_entry.py](scripts/validate_entry.py) `ready_autopromote_enabled`）
- status が変わったらファイル名タグも揃えてください：`python3 scripts/apply_status_markers.py`（`[人書]`＝needs_review / `[済]`＝ready）→ `python3 scripts/sync_entries_csv.py`
- 原則：[docs/quality_guidelines.md](docs/quality_guidelines.md)

### 外出先コメントを取り込む

- **新方式（推奨）**：[docs/mobile_repoedit_setup.md](docs/mobile_repoedit_setup.md) — [Taguchi-1989/RepoEdit](https://github.com/Taguchi-1989/RepoEdit)（PWA + Cloudflare Worker）で、エントリ内の `user-input` ブロック（「非エンジニアのつまずき」「私のコメント」）をスマホから直接編集。書き戻し先は `mobile-drafts` ブランチ。マーカーは全エントリに埋め込み済み（[scripts/add_user_input_markers.py](scripts/add_user_input_markers.py)）
- **旧方式（参考保持）**：以下は Obsidian Mobile + `mobile_inbox/` の二段運用。新方式が安定するまで併走可
- [docs/mobile_inbox_requirements.md](docs/mobile_inbox_requirements.md) — Obsidian Mobile + Git 連携の仕様
- [docs/mobile_rough_comment_flow.md](docs/mobile_rough_comment_flow.md) — スマホでは雑に話し、PC 側で `mobile_inbox` 形式へ整える軽量運用
- [docs/mobile_setup_guide.md](docs/mobile_setup_guide.md) — Android セットアップ手引き（PAT 作成 → clone → 初回テスト）
- [docs/mobile_editing_guide.md](docs/mobile_editing_guide.md) — Phase 1 完了後の実編集ワークフロー（A〜D モード）
- [skills/import-comments.md](skills/import-comments.md) — `mobile_inbox/` から本編へ反映する手順

## 7. 迷ったとき開く順番

1. **[docs/v2_rules_summary.md](docs/v2_rules_summary.md)** — v2 確定ルール総覧（**最初に読む**）
2. [docs/entry_schema.yaml](docs/entry_schema.yaml) — 文字数・必須節・enum の機械可読版（generator / validator の単一入力）
3. [docs/component_spec_v2.md](docs/component_spec_v2.md) — 実装担当引き渡し仕様（Astro で静的サイト生成予定）
4. [docs/book_philosophy.md](docs/book_philosophy.md) — 根っこのフィロソフィー
5. [docs/editorial_style.md](docs/editorial_style.md) — トーン・文体の原則
6. [templates/entry_template.md](templates/entry_template.md) — 構造の正解
7. [ledgers/entry_candidates.md](ledgers/entry_candidates.md) — 335 件の棚と要確認
8. [ledgers/writing_priority.md](ledgers/writing_priority.md) — ステージ別の執筆順
9. [ledgers/chapters.yaml](ledgers/chapters.yaml) — 章（A〜J）→ ラベル／カテゴリのマップ
10. [docs/id_scheme.md](docs/id_scheme.md) — ID ルール（触らない）

## 8. 次のステップ

[ledgers/next_session_handoff.md](ledgers/next_session_handoff.md) にこの時点の TODO と引き継ぎ事項が入っています。次セッションはまずそれを開いてください。

## 9. リポジトリ

管理は <https://github.com/Taguchi-1989/VibeCodingDictionary>（`main` ブランチ）。
