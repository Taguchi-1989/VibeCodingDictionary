#!/usr/bin/env python3
"""
確認済みエントリの `last_audited` を一括で押印するスクリプト

鮮度監査で一次情報を見に行った結果、**記述に変更が無かった**ケースが大半になります。
そのたびに 30 件のファイルを手で開いて日付を書き換えるのは現実的ではないので、
対象をまとめて指定して押印できるようにしたものです。

`evaluation_date` は執筆・評価した時点の記録なので **絶対に触りません**。
更新するのは `last_audited` だけです（無ければ `evaluation_date` の直後に足します）。

Usage:
    # 事実 ID の影響エントリをまとめて押印（volatile_facts.yaml と連動）
    python3 scripts/touch_last_audited.py --fact F-model-openai

    # ID 指定
    python3 scripts/touch_last_audited.py --ids D-20,D-21,D-22

    # category / letter 単位
    python3 scripts/touch_last_audited.py --category model
    python3 scripts/touch_last_audited.py --letter B

    # 日付を明示（既定は今日）／まず確認だけ
    python3 scripts/touch_last_audited.py --category model --date 2026-09-20
    python3 scripts/touch_last_audited.py --category model --dry-run

安全のため、対象が 1 件も無いときと、対象指定が何も無いときは何もしません。
--dry-run で対象を確かめてから実行することを勧めます。
"""

import argparse
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_entry import parse_frontmatter  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "content" / "entries"

SKIP_STATUSES = {"skeleton", "sample", "archived"}


def parse_date(value: str) -> date | None:
    value = str(value or "").strip()
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def ids_from_fact(fact_id: str) -> list[str]:
    """update_volatile_facts.py に影響エントリを問い合わせる。"""
    script = Path(__file__).resolve().parent / "update_volatile_facts.py"
    try:
        result = subprocess.run(
            [sys.executable, str(script), "--fact", fact_id, "--ids", "--no-write"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
            check=False,
        )
    except Exception as exc:
        print(f"影響エントリの取得に失敗しました: {exc}", file=sys.stderr)
        return []
    if result.returncode != 0:
        print(result.stderr.strip() or f"事実 ID が解決できません: {fact_id}", file=sys.stderr)
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def collect_targets(args) -> list[tuple[Path, dict]]:
    wanted_ids: set[str] | None = None
    if args.fact:
        wanted_ids = set(ids_from_fact(args.fact))
        if not wanted_ids:
            return []
    if args.ids:
        explicit = {s.strip() for s in args.ids.split(",") if s.strip()}
        wanted_ids = explicit if wanted_ids is None else (wanted_ids & explicit)

    targets = []
    for md_path in sorted(ENTRIES_DIR.rglob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, _body = parse_frontmatter(text)
        if not fm:
            continue
        if str(fm.get("status", "")).strip() in SKIP_STATUSES:
            continue
        layout = str(fm.get("page_layout", "")).strip()
        if layout.startswith("front_") or layout.startswith("back_"):
            continue

        entry_id = str(fm.get("id", "")).strip()
        if wanted_ids is not None and entry_id not in wanted_ids:
            continue
        if args.category and str(fm.get("category", "")).strip() != args.category:
            continue
        if args.letter:
            m = re.match(r"^([A-J])-", entry_id)
            if not m or m.group(1) != args.letter.upper():
                continue
        targets.append((md_path, fm))
    return targets


def stamp(md_path: Path, stamp_date: str) -> str:
    """last_audited を書き換える。戻り値は 'updated' / 'added' / 'unchanged'。"""
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return "unchanged"
    end = text.find("\n---\n", 4)
    if end == -1:
        return "unchanged"
    fm_text = text[4:end]
    rest = text[end:]

    if re.search(r"^last_audited:", fm_text, flags=re.MULTILINE):
        current = re.search(r"^last_audited:\s*(.*)$", fm_text, flags=re.MULTILINE)
        if current and current.group(1).strip().strip('"') == stamp_date:
            return "unchanged"
        new_fm = re.sub(
            r"^last_audited:.*$", f"last_audited: {stamp_date}", fm_text, flags=re.MULTILINE
        )
        action = "updated"
    elif re.search(r"^evaluation_date:", fm_text, flags=re.MULTILINE):
        # evaluation_date の直後に置く（時変情報のキーをひとかたまりにしておく）
        new_fm = re.sub(
            r"^(evaluation_date:.*)$",
            r"\1\n" + f"last_audited: {stamp_date}",
            fm_text,
            count=1,
            flags=re.MULTILINE,
        )
        action = "added"
    else:
        new_fm = fm_text.rstrip("\n") + f"\nlast_audited: {stamp_date}"
        action = "added"

    md_path.write_text("---\n" + new_fm + rest, encoding="utf-8")
    return action


def main() -> int:
    ap = argparse.ArgumentParser(description="確認済みエントリの last_audited を一括で押印する")
    ap.add_argument("--fact", help="volatile_facts.yaml の事実 ID（影響エントリを対象にする）")
    ap.add_argument("--ids", help="エントリ ID をカンマ区切りで指定")
    ap.add_argument("--category", help="category で絞る")
    ap.add_argument("--letter", help="章 letter（A〜J）で絞る")
    ap.add_argument("--date", help="押印する日付 YYYY-MM-DD（既定は今日）")
    ap.add_argument("--dry-run", action="store_true", help="書き換えずに対象を表示する")
    args = ap.parse_args()

    if not any([args.fact, args.ids, args.category, args.letter]):
        print(
            "対象の指定がありません。--fact / --ids / --category / --letter のいずれかを付けてください。\n"
            "全件を無条件に押印する使い方は、確認していないものまで「確認済み」にしてしまうため用意していません。",
            file=sys.stderr,
        )
        return 1

    stamp_date = args.date or date.today().isoformat()
    if parse_date(stamp_date) is None:
        print("--date は YYYY-MM-DD で指定してください", file=sys.stderr)
        return 1

    targets = collect_targets(args)
    if not targets:
        print("対象が 0 件でした（指定を見直してください）", file=sys.stderr)
        return 1

    if args.dry_run:
        print(f"対象 {len(targets)} 件（--dry-run なので書き換えません / 押印日 {stamp_date}）:")
        for md_path, fm in targets:
            current = str(fm.get("last_audited", "") or "—")
            print(
                f"  {str(fm.get('id', '')):>7} {str(fm.get('title', ''))[:22]:<22} "
                f"last_audited: {current} → {stamp_date}"
            )
        return 0

    counts = {"updated": 0, "added": 0, "unchanged": 0}
    for md_path, _fm in targets:
        counts[stamp(md_path, stamp_date)] += 1

    print(
        f"last_audited を {stamp_date} に更新: 新規 {counts['added']} / "
        f"更新 {counts['updated']} / 変更なし {counts['unchanged']}（対象 {len(targets)} 件）"
    )
    print("鮮度キューを再生成するには: python3 scripts/audit_freshness.py")
    print("監査した範囲は ledgers/freshness_audit_log.md に 1 行追記してください")
    return 0


if __name__ == "__main__":
    sys.exit(main())
