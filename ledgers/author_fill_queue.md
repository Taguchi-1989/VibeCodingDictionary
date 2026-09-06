# 著者記入欄キュー（author fill queue）

*自動生成: 2026-09-06 06:39 / `scripts/update_author_fill_queue.py`。手で編集しないでください。*

「非エンジニアのつまずき」「私のコメント」は**著者本人しか書けない欄**です。AI は空スケルトンを置くだけで、中身には触りません。

## 内訳

- **完了**（つまずき 1 件以上 ＋ コメント 4 ラベル全部）: 437 件
- **途中**（書きかけで止まっている）: 0 件
- **手つかず**（両方まるごと空）: 21 件
- **合計**: 458 件

---

## ✍️ 途中（あと少しで終わる。ここから手を付けるのが早い）（0 件）

_なし_

---

## ⬜ 手つかず（両方まるごと空）（21 件）

letter 別: F 2件 / G 4件 / H 6件 / I 2件 / J 7件

| ID | title | status | reader_level | path |
| :-- | :-- | :-- | :-- | :-- |
| F-57 | リポジトリ | needs_review | 1-2 | `content/entries/term_tool/F-57_repository[人書].md` |
| F-150 | MIT ライセンス | needs_review | 2-3 | `content/entries/term_tool/F-150_mit_license[人書].md` |
| G-24 | Temperature | needs_review | 2-3 | `content/entries/term_llm/G-24_temperature[人書].md` |
| G-25 | AI のメモリ機能 | needs_review | 1-2 | `content/entries/term_llm/G-25_memory[人書].md` |
| G-26 | Computer Use | needs_review | 3-4 | `content/entries/term_llm/G-26_computer_use[人書].md` |
| G-27 | プロンプトインジェクション | needs_review | 2-3 | `content/entries/term_llm/G-27_prompt_injection[人書].md` |
| H-57 | Gemini の命名史 | needs_review | 2-3 | `content/entries/history/H-57_gemini_naming_history[人書].md` |
| H-60 | Codex → GitHub Copilot の系譜 | needs_review | 2-3 | `content/entries/history/H-60_codex_to_copilot[人書].md` |
| H-61 | Preview 版という文化 | needs_review | 2 | `content/entries/history/H-61_preview_culture[人書].md` |
| H-62 | Anthropic 創業の流れ | needs_review | 2-3 | `content/entries/history/H-62_anthropic_founding[人書].md` |
| H-63 | Vibe Coding 命名 | needs_review | 1-2 | `content/entries/history/H-63_vibe_coding_naming[人書].md` |
| H-64 | DeepSeek ショック | needs_review | 2-3 | `content/entries/history/H-64_deepseek_shock[人書].md` |
| I-80 | 自作 MCP のテンプレ | needs_review | 3-4 | `content/entries/mcp/I-80_diy_mcp_template[人書].md` |
| I-81 | MCP の登録・設定 | needs_review | 2-3 | `content/entries/mcp/I-81_mcp_setup[人書].md` |
| J-125 | 適用宣言書 | needs_review | 3-4 | `content/entries/term_general/J-125_statement_of_applicability[人書].md` |
| J-126 | 内部監査とマネジメントレビュー | needs_review | 3-4 | `content/entries/term_general/J-126_internal_audit_review[人書].md` |
| J-135 | 機能安全 | needs_review | 4 | `content/entries/term_general/J-135_functional_safety[人書].md` |
| J-136 | 3 ステップメソッド | needs_review | 3-4 | `content/entries/term_general/J-136_three_step_method[人書].md` |
| J-137 | ALARP | needs_review | 4 | `content/entries/term_general/J-137_alarp[人書].md` |
| J-138 | 是正処置と不適合 | needs_review | 3 | `content/entries/term_general/J-138_corrective_action[人書].md` |
| J-139 | 説明可能性 | needs_review | 3 | `content/entries/term_general/J-139_explainability[人書].md` |

---

## 使い方

1. 上の「途中」から埋める。第一印象だけ書いて止まっているものが多く、残りの 1〜3 欄を足すだけで完了になります
2. スマホからは RepoEdit で `user-input` ブロックを直接編集できます（[docs/mobile_repoedit_setup.md](../docs/mobile_repoedit_setup.md)）
3. 書き終えたら `status: needs_review → ready` を**手で**上げてください。自動昇格は既定で無効です（CLAUDE.md の運用に合わせています）。一括で上げたいときは `VCD_AUTOPROMOTE_READY=1 python3 scripts/update_review_queue.py`

字数の目安は [docs/entry_schema.yaml](../docs/entry_schema.yaml) を参照してください（つまずき: 1 項目 15〜60 字 / コメント: 1 項目 10〜45 字）。
