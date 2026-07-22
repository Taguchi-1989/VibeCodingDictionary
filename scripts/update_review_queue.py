#!/usr/bin/env python3
"""
レビューキュー（ledgers/revision_queue.md）を再生成するスクリプト

content/entries/ 配下の全 md を走査し、status と validator 結果を集計して
ledgers/revision_queue.md を 1 ファイルだけ書き直す。

Usage:
    # 手動実行
    python3 scripts/update_review_queue.py

    # Hook 経由（無音）
    python3 scripts/update_review_queue.py --quiet

設計メモ:
    - validate_entry.py のチェック関数を import して再利用
    - skeleton / sample / archived はチェックをスキップして件数だけ集計
    - common/ も同様（A-1 まえがき等は validator 対象外）
    - 出力は markdown 1 本。著者・サブエージェントが「次やること」を 1 画面で見える
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

# 兄弟スクリプト validate_entry を import 可能にする
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_entry import (  # noqa: E402
    Report,
    parse_frontmatter,
    check_yaml,
    check_yaml_front,
    check_structure,
    check_author_fields_empty,
    check_char_counts,
    check_tone,
    check_sources_date,
    promote_to_needs_review,
    promote_to_ready,
    is_author_fields_filled,
    reader_level_max,
    FRONT_LAYOUTS,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "content" / "entries"
FRONTMATTER_DIR = PROJECT_ROOT / "content" / "frontmatter"
QUEUE_PATH = PROJECT_ROOT / "ledgers" / "revision_queue.md"

SKIP_STATUSES = {"skeleton", "sample", "archived"}


def validate_silently(path: Path, fm: dict, body: str, status: str):
    """1 件の validator を黙って走らせ、(stars, warnings, summary) を返す。

    summary は警告/違反の冒頭 3 件をセミコロン区切りで圧縮した短文。
    page_layout が front_* なら前付け用ルールセット（軽い）。
    """
    r = Report(path)
    layout = str(fm.get("page_layout", "")).strip()
    if layout.startswith("front_"):
        check_yaml_front(fm, r)
        check_tone(body, r)
    elif reader_level_max(fm) >= 6:
        # Lv6 自己学習シェルフ: 誌面前提の制約（字数・ですます・著者欄）は外す
        # （validate_entry.py の main() ゲートと同じ扱い。docs/level_policy.md §2-6）
        check_yaml(fm, r)
        check_structure(body, r)
        check_sources_date(body, fm, r)
    else:
        check_yaml(fm, r)
        check_structure(body, r)
        check_author_fields_empty(body, status, r)
        check_char_counts(body, r)
        check_tone(body, r)
        check_sources_date(body, fm, r)

    parts: list[str] = []
    for s in r.star_fails:
        head = s.split(":", 1)[-1].strip()
        parts.append("☆ " + head[:50])
    for w in r.warnings:
        head = w.split(":", 1)[-1].strip()
        parts.append("⚠ " + head[:50])
    return len(r.star_fails), len(r.warnings), "; ".join(parts[:3])


def collect():
    rows = []
    promoted_ids: list[str] = []
    paths: list[Path] = sorted(ENTRIES_DIR.rglob("*.md"))
    if FRONTMATTER_DIR.exists():
        paths += sorted(FRONTMATTER_DIR.rglob("*.md"))
    for md_path in paths:
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, body = parse_frontmatter(text)
        eid = str(fm.get("id", "")).strip()
        title = str(fm.get("title", "")).strip()
        if not eid:
            continue
        status = str(fm.get("status", "")).strip() or "(空)"

        posix = md_path.as_posix()
        is_common = "/content/entries/common/" in posix
        is_frontmatter_dir = "/content/frontmatter/" in posix
        layout = str(fm.get("page_layout", "")).strip()
        is_front = layout.startswith("front_")

        # 検証対象判定:
        #  - skeleton / sample / archived は集計のみ
        #  - common/ にあって spread_v1 のまま（front_* 未移行）は当面スキップ
        #  - それ以外（本編 entries、front_*、frontmatter/）は validate を走らせる
        if status in SKIP_STATUSES:
            stars, warns, summary = 0, 0, ""
        elif is_common and not is_front:
            stars, warns, summary = 0, 0, ""
        else:
            stars, warns, summary = validate_silently(md_path, fm, body, status)
            # 自動昇格は spread_v1 だけ。front_* は著者本人レビュー必須
            if not is_front:
                if status == "drafting" and stars == 0 and warns == 0:
                    if promote_to_needs_review(md_path):
                        status = "needs_review"
                        promoted_ids.append(eid + " (drafting→needs_review)")
                if status == "needs_review" and stars == 0 and is_author_fields_filled(body):
                    if promote_to_ready(md_path):
                        status = "ready"
                        promoted_ids.append(eid + " (needs_review→ready)")

        reader_level = str(fm.get("reader_level", "")).strip()
        rl_nums = [int(x) for x in re.findall(r"\d", reader_level)]
        rl_max = max(rl_nums) if rl_nums else 0

        rows.append({
            "id": eid,
            "title": title,
            "status": status,
            "stars": stars,
            "warns": warns,
            "summary": summary,
            "path": md_path.relative_to(PROJECT_ROOT).as_posix(),
            "is_common": is_common,
            "is_frontmatter_dir": is_frontmatter_dir,
            "is_front": is_front,
            "reader_level": reader_level,
            "rl_max": rl_max,
        })
    return rows, promoted_ids


def render(rows):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # status 集計
    by_status: dict[str, int] = {}
    for r in rows:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    # バケツ分け:
    #  - SKIP_STATUSES（skeleton/sample/archived）は全バケツ除外
    #  - common/ で spread_v1 のまま（front_* 未移行）も除外
    #  - 前付け（front_*）は本編とは別バケツに集約
    def is_target_main(r):
        if r["status"] in SKIP_STATUSES:
            return False
        if r["is_front"]:
            return False
        if r["is_common"]:
            return False
        return True

    front_rows = [r for r in rows if r["is_front"] and r["status"] not in SKIP_STATUSES]
    star_violators = [r for r in rows if is_target_main(r) and r["stars"] > 0]
    warn_only      = [r for r in rows if is_target_main(r) and r["stars"] == 0 and r["warns"] > 0]
    drafting_clean = [r for r in rows if is_target_main(r) and r["status"] == "drafting" and r["stars"] == 0 and r["warns"] == 0]
    needs_review   = [r for r in rows if is_target_main(r) and r["status"] == "needs_review" and r["stars"] == 0 and r["warns"] == 0]
    ready_clean    = [r for r in rows if is_target_main(r) and r["status"] == "ready" and r["stars"] == 0 and r["warns"] == 0]

    lines = [
        "# 要直しキュー（revision queue）",
        "",
        f"*自動生成: {now} / `scripts/update_review_queue.py`*",
        "",
        "1 画面で「次やるべき・見直すべき・適合済み」が見えるダッシュボード。`scripts/validate_entry.py` のチェックを全件で走らせた結果を集計して再生成しています。手で編集しないでください。",
        "",
        "## status 内訳",
        "",
    ]
    order = ["skeleton", "candidate", "drafting", "needs_review", "ready", "sample", "archived"]
    seen = set()
    for s in order:
        if s in by_status:
            lines.append(f"- **{s}**: {by_status[s]} 件")
            seen.add(s)
    for s in sorted(by_status):
        if s not in seen:
            lines.append(f"- **{s}**: {by_status[s]} 件")
    lines.append(f"- **合計**: {len(rows)} 件")

    # 刊行スコープ集計（docs/level_policy.md §2-6）:
    #  reader_level 6 = 著者の自己学習シェルフ（刊行外）。誌面ビルドから除外される。
    shelf_rows = [
        r for r in rows
        if r["rl_max"] >= 6 and r["status"] not in SKIP_STATUSES
    ]
    lines.append("")
    lines.append(
        f"- **自己学習シェルフ（reader_level 6・刊行外）**: {len(shelf_rows)} 件"
        "（誌面には出ません。`scripts/preview_gen.py` が除外）"
    )

    def section(title: str, items: list, empty_msg: str = "なし"):
        out = [
            "",
            f"## {title}（{len(items)} 件）",
            "",
        ]
        if not items:
            out.append(f"_{empty_msg}_")
            return out
        out.append("| ID | title | status | 概要 |")
        out.append("| :-- | :-- | :-- | :-- |")
        for r in sorted(items, key=lambda x: (x["id"][:1], x["id"])):
            summary = r["summary"] or "—"
            # `|` を含む行は表崩れするのでエスケープ
            summary = summary.replace("|", "\\|")
            out.append(f"| {r['id']} | {r['title']} | {r['status']} | {summary} |")
        return out

    lines += section("☆ 違反あり（最優先で直す）", star_violators)
    lines += section("⚠️ 警告あり（軽微超過 / 著者か entry-writer で手当て）", warn_only)
    lines += section("✍️ 書きかけ（drafting・全パス済み・自動昇格漏れ）", drafting_clean,
                     empty_msg="なし（drafting で全パスしたものは自動で needs_review に上がります）")
    lines += section("📝 著者レビュー待ち（needs_review・全パス）", needs_review)
    lines += section("✅ 完成（ready・全パス）", ready_clean)
    lines += section("📖 前付け（front_*・著者本人レビュー必須）", front_rows,
                     empty_msg="なし（A 章 / 扉が front_* レイアウトに移行すると表示されます）")
    lines += section("📚 自己学習シェルフ（reader_level 6・今季は刊行しない）", shelf_rows,
                     empty_msg="なし（KV Cache・MLA 等の深掘り技術を 6 にすると、ここに集まり誌面からは外れます）")
    lines.append("")
    lines.append("## 動線")
    lines.append("")
    lines.append("- **☆ 違反**（タグ `[AI直]`）: その場で entry-writer を呼んで直す（status は drafting のまま）")
    lines.append("- **⚠️ 警告**（タグ `[AI整]`）: 軽微なら手で削る／溜まったらまとめて対応")
    lines.append("- **needs_review**（タグ `[人書]`）: 著者本人が「非エンジニアのつまずき」「私のコメント」4 項目を埋める。全項目埋まると保存時に `ready`（`[済]`）へ自動昇格")
    lines.append("- このキューは `Edit/Write` のたびに自動更新されます。手動更新は `python3 scripts/update_review_queue.py`")
    lines.append("- ファイル名のタグを更新するには `python3 scripts/apply_status_markers.py`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true", help="標準出力を抑える（hook 経由用）")
    args = ap.parse_args()

    rows, promoted_ids = collect()
    out = render(rows)
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(out, encoding="utf-8")

    if not args.quiet:
        print(f"updated: {QUEUE_PATH.relative_to(PROJECT_ROOT)}  ({len(rows)} entries)")
        if promoted_ids:
            print(f"promoted drafting → needs_review: {len(promoted_ids)} 件")
            print("  " + ", ".join(promoted_ids))
    return 0


if __name__ == "__main__":
    sys.exit(main())
