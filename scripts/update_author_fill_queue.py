#!/usr/bin/env python3
"""
著者記入欄キュー（ledgers/author_fill_queue.md）を再生成するスクリプト

「非エンジニアのつまずき」「私のコメント」は著者本人しか書けない欄です。
どこが空で、どこが書きかけで止まっているのかを 1 画面で見えるようにします。

Usage:
    python3 scripts/update_author_fill_queue.py           # 手動実行
    python3 scripts/update_author_fill_queue.py --quiet   # Hook 経由（無音）

設計メモ:
    - validate_entry.author_field_block() を使って user-input マーカーの内側を読む
    - 旧 author_fill_queue.md（2026-05-23、手作業生成）は「空か否か」しか見ておらず、
      「第一印象だけ書いて止まっている」ような書きかけを拾えなかった。ここを分ける
    - 「途中」＝どちらかの欄に手が入っているのに、4 ラベルのどれかが空／つまずきが空
    - archived / skeleton / sample はスキップ
    - 前付けレイアウト（page_layout: front_*）もスキップ。A-1〜A-11 は誌面に著者欄を
      置かない仕様（各 md の冒頭に明記、validate_entry.py も front_* を別ルートで検証）で、
      user-input マーカー自体が無い。ここに並べると「著者が 11 件書き残している」ように
      見えてしまうため、対象から外す
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_entry import author_field_block, parse_frontmatter  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "content" / "entries"
QUEUE_PATH = PROJECT_ROOT / "ledgers" / "author_fill_queue.md"

SKIP_STATUSES = {"skeleton", "sample", "archived"}

# 私のコメントの 4 ラベル（表示順）
COMMENT_LABELS = [
    ("第一印象", "🙂 第一印象"),
    ("良い点", "👍 良い点"),
    ("ダメな点", "👎 ダメな点"),
    ("誰向けか", "👥 誰向けか"),
]


def stumble_count(body: str) -> int:
    """「非エンジニアのつまずき」の、語句が入っている箇条書きの数。"""
    n = 0
    for line in author_field_block(body, "非エンジニアのつまずき").split("\n"):
        line = line.strip()
        if line.startswith("-") and line[1:].strip():
            n += 1
    return n


def comment_filled(body: str) -> list[str]:
    """「私のコメント」で、ラベル後に語句が入っているものの key 一覧。"""
    block = author_field_block(body, "私のコメント")
    filled = []
    for key, _display in COMMENT_LABELS:
        for line in block.split("\n"):
            if key in line and (":" in line or "：" in line):
                sep = ":" if ":" in line else "："
                if line.split(sep, 1)[-1].strip():
                    filled.append(key)
                break
    return filled


def collect() -> list[dict]:
    rows = []
    for md_path in sorted(ENTRIES_DIR.rglob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, body = parse_frontmatter(text)
        status = str(fm.get("status", "")).strip()
        if status in SKIP_STATUSES:
            continue
        # 前付け（front_*）は著者欄を持たないレイアウトなので数えない
        if str(fm.get("page_layout", "")).strip().startswith("front_"):
            continue
        filled = comment_filled(body)
        sn = stumble_count(body)
        missing = [d for k, d in COMMENT_LABELS if k not in filled]
        if sn == 0 and not filled:
            state = "empty"
        elif sn > 0 and len(filled) == len(COMMENT_LABELS):
            state = "done"
        else:
            state = "partial"
        rows.append(
            {
                "id": str(fm.get("id", "?")).strip(),
                "title": str(fm.get("title", "")).strip(),
                "status": status,
                "reader_level": str(fm.get("reader_level", "")).strip(),
                "path": md_path.relative_to(PROJECT_ROOT).as_posix(),
                "stumble": sn,
                "filled": len(filled),
                "missing": missing,
                "state": state,
            }
        )
    return rows


def sort_key(row: dict):
    """A-1, A-2, ..., A-10 の順に並べる（letter → 数値）。"""
    m = re.match(r"([A-Z])-(\d+)", row["id"])
    return (m.group(1), int(m.group(2))) if m else ("Z", 9999)


def render(rows: list[dict]) -> str:
    partial = sorted([r for r in rows if r["state"] == "partial"], key=sort_key)
    empty = sorted([r for r in rows if r["state"] == "empty"], key=sort_key)
    done = [r for r in rows if r["state"] == "done"]

    out = [
        "# 著者記入欄キュー（author fill queue）",
        "",
        f"*自動生成: {datetime.now():%Y-%m-%d %H:%M} / `scripts/update_author_fill_queue.py`。"
        "手で編集しないでください。*",
        "",
        "「非エンジニアのつまずき」「私のコメント」は**著者本人しか書けない欄**です。"
        "AI は空スケルトンを置くだけで、中身には触りません。",
        "",
        "## 内訳",
        "",
        f"- **完了**（つまずき 1 件以上 ＋ コメント 4 ラベル全部）: {len(done)} 件",
        f"- **途中**（書きかけで止まっている）: {len(partial)} 件",
        f"- **手つかず**（両方まるごと空）: {len(empty)} 件",
        f"- **合計**: {len(rows)} 件",
        "",
        "---",
        "",
        f"## ✍️ 途中（あと少しで終わる。ここから手を付けるのが早い）（{len(partial)} 件）",
        "",
    ]
    if partial:
        out += [
            "| ID | title | つまずき | コメント | 空いている欄 | path |",
            "| :-- | :-- | --: | --: | :-- | :-- |",
        ]
        for r in partial:
            miss = " / ".join(r["missing"]) if r["missing"] else "（つまずきのみ）"
            out.append(
                f"| {r['id']} | {r['title']} | {r['stumble']} 件 | "
                f"{r['filled']}/4 | {miss} | `{r['path']}` |"
            )
        out.append("")
    else:
        out += ["_なし_", ""]

    out += [
        "---",
        "",
        f"## ⬜ 手つかず（両方まるごと空）（{len(empty)} 件）",
        "",
    ]
    if empty:
        by_letter: dict[str, list[dict]] = {}
        for r in empty:
            by_letter.setdefault(r["id"].split("-")[0], []).append(r)
        summary = " / ".join(f"{k} {len(v)}件" for k, v in sorted(by_letter.items()))
        out += [f"letter 別: {summary}", ""]
        out += [
            "| ID | title | status | reader_level | path |",
            "| :-- | :-- | :-- | :-- | :-- |",
        ]
        for r in empty:
            out.append(
                f"| {r['id']} | {r['title']} | {r['status']} | "
                f"{r['reader_level']} | `{r['path']}` |"
            )
        out.append("")
    else:
        out += ["_なし_", ""]

    out += [
        "---",
        "",
        "## 使い方",
        "",
        "1. 上の「途中」から埋める。第一印象だけ書いて止まっているものが多く、"
        "残りの 1〜3 欄を足すだけで完了になります",
        "2. スマホからは RepoEdit で `user-input` ブロックを直接編集できます"
        "（[docs/mobile_repoedit_setup.md](../docs/mobile_repoedit_setup.md)）",
        "3. 書き終えたら `status: needs_review → ready` を**手で**上げてください。"
        "自動昇格は既定で無効です（CLAUDE.md の運用に合わせています）。"
        "一括で上げたいときは `VCD_AUTOPROMOTE_READY=1 python3 scripts/update_review_queue.py`",
        "",
        "字数の目安は [docs/entry_schema.yaml](../docs/entry_schema.yaml) を参照してください"
        "（つまずき: 1 項目 15〜60 字 / コメント: 1 項目 10〜45 字）。",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true", help="Hook 経由の無音実行")
    args = ap.parse_args()

    rows = collect()
    QUEUE_PATH.write_text(render(rows), encoding="utf-8")
    if not args.quiet:
        n_partial = sum(1 for r in rows if r["state"] == "partial")
        n_empty = sum(1 for r in rows if r["state"] == "empty")
        print(
            f"updated: {QUEUE_PATH.relative_to(PROJECT_ROOT).as_posix()}  "
            f"({len(rows)} entries / 途中 {n_partial} / 手つかず {n_empty})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
