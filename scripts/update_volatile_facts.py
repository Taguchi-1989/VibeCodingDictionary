#!/usr/bin/env python3
"""
時変ファクト watchlist（ledgers/volatile_facts.md）を再生成するスクリプト

ledgers/volatile_facts.yaml に定義した「事実」ごとに、本文を走査して
**その事実に依存しているエントリ**を集め、一覧を markdown に書き出します。

Usage:
    python3 scripts/update_volatile_facts.py             # 台帳を再生成
    python3 scripts/update_volatile_facts.py --quiet      # Hook 経由（無音）
    python3 scripts/update_volatile_facts.py --fact F-model-openai
                                                          # 1 つの事実の影響エントリを標準出力へ
    python3 scripts/update_volatile_facts.py --fact F-model-openai --ids
                                                          # ID だけを改行区切りで（他スクリプトへ渡す用）

設計メモ（2026-09-19 追加）:
    - audit_freshness.py が「エントリ側」から鮮度を見るのに対し、こちらは
      「事実側」から見る。GPT の世代名は 26 件、価格の記述は 18 件に散っていて、
      エントリを 1 件ずつ巡回する方式では事実の変化を取りこぼすため
    - 事実の定義（何を・どこで確認するか）は人が書く。影響エントリの収集だけ機械がやる。
      定義ファイルは yaml、出力は md で、md は手で編集しない
    - PyYAML が無い環境でも保存フックを壊さないよう、import 失敗時は無音で抜ける
"""

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_entry import extract_printed_body, parse_frontmatter  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "content" / "entries"
FACTS_PATH = PROJECT_ROOT / "ledgers" / "volatile_facts.yaml"
OUT_PATH = PROJECT_ROOT / "ledgers" / "volatile_facts.md"

SKIP_STATUSES = {"skeleton", "sample", "archived"}

KIND_LABEL = {
    "model": "モデル世代",
    "pricing": "料金",
    "benchmark": "ベンチマーク",
    "spec": "仕様",
    "availability": "提供状況",
}


def load_facts() -> list[dict] | None:
    try:
        import yaml  # noqa: PLC0415
    except ImportError:
        return None
    if not FACTS_PATH.exists():
        return []
    data = yaml.safe_load(FACTS_PATH.read_text(encoding="utf-8")) or {}
    return data.get("facts", []) or []


def load_entries() -> list[dict]:
    entries = []
    for md_path in sorted(ENTRIES_DIR.rglob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, body = parse_frontmatter(text)
        if not fm:
            continue
        if str(fm.get("status", "")).strip() in SKIP_STATUSES:
            continue
        layout = str(fm.get("page_layout", "")).strip()
        if layout.startswith("front_") or layout.startswith("back_"):
            continue
        entries.append(
            {
                "id": str(fm.get("id", "")).strip(),
                "title": str(fm.get("title", "")).strip(),
                "category": str(fm.get("category", "")).strip(),
                "printed": extract_printed_body(body),
                "path": md_path.relative_to(PROJECT_ROOT).as_posix(),
            }
        )
    return entries


def sort_key(entry_id: str) -> tuple:
    m = re.match(r"^([A-J])-(\d+)$", entry_id)
    if m:
        return (0, m.group(1), int(m.group(2)))
    return (1, entry_id, 0)


def match_entries(fact: dict, entries: list[dict]) -> tuple[list[dict], str]:
    """(該当エントリ, エラーメッセージ) を返す。正規表現が壊れていても落とさない。

    pattern で拾ったあと、exclude_categories / exclude_ids で削ります。
    「最新モデル世代」のような事実は、歴史エントリ（H 章）が同じ固有名詞を
    含んでいても影響を受けません（過去の出来事の記述は世代交代で古くならない）。
    そういう取りこぼしではない除外を、定義側で明示できるようにしています。
    """
    pattern = str(fact.get("pattern", "")).strip()
    if not pattern:
        return [], "pattern が未定義"
    try:
        rx = re.compile(pattern)
    except re.error as exc:
        return [], f"pattern が正規表現として不正（{exc}）"

    include_categories = {str(c) for c in (fact.get("include_categories") or [])}
    exclude_categories = {str(c) for c in (fact.get("exclude_categories") or [])}
    exclude_ids = {str(i) for i in (fact.get("exclude_ids") or [])}

    hits = [
        e
        for e in entries
        if rx.search(e["printed"])
        and (not include_categories or e["category"] in include_categories)
        and e["category"] not in exclude_categories
        and e["id"] not in exclude_ids
    ]
    hits.sort(key=lambda e: sort_key(e["id"]))
    return hits, ""


def parse_date(value) -> date | None:
    value = str(value or "").strip().strip('"')
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def render(facts: list[dict], entries: list[dict], today: date) -> str:
    out: list[str] = [
        "# 時変ファクト watchlist（自動生成）",
        "",
        f"*基準日 {today.isoformat()} — `python3 scripts/update_volatile_facts.py` が再生成します。"
        "定義を変えるときは [volatile_facts.yaml](volatile_facts.yaml) を編集してください。"
        "この .md は手で編集しないでください。*",
        "",
        "「最新の Claude は何か」「ChatGPT の月額はいくらか」のような事実は、"
        "1 つ変わるだけで複数のエントリが同時に古くなります。"
        "エントリ側から鮮度を見る [freshness_queue.md](freshness_queue.md) と対で、"
        "こちらは**事実側から影響範囲を引く**ための台帳です。",
        "",
        "---",
        "",
        "## 1. 一覧",
        "",
        "| 事実ID | 事実 | 種別 | 最終確認 | 期限 | 影響エントリ |",
        "| :-- | :-- | :-- | :-- | :-- | --: |",
    ]

    resolved = []
    for fact in facts:
        hits, err = match_entries(fact, entries)
        last_checked = parse_date(fact.get("last_checked"))
        recheck_days = int(fact.get("recheck_days") or 90)
        if last_checked is None:
            age, overdue, checked_disp = None, True, "**未確認**"
        else:
            age = (today - last_checked).days
            overdue = age > recheck_days
            checked_disp = f"{last_checked.isoformat()}（{age} 日前）"
        resolved.append(
            {
                "fact": fact,
                "hits": hits,
                "err": err,
                "overdue": overdue,
                "age": age,
                "checked_disp": checked_disp,
                "recheck_days": recheck_days,
            }
        )
        mark = "⏰ " if overdue else ""
        out.append(
            f"| `{fact.get('id', '')}` | {fact.get('label', '')} | "
            f"{KIND_LABEL.get(str(fact.get('kind', '')), fact.get('kind', ''))} | "
            f"{mark}{checked_disp} | {recheck_days} 日 | {len(hits)} |"
        )

    n_overdue = sum(1 for r in resolved if r["overdue"])
    out += [
        "",
        f"⏰ = 再確認の期限を過ぎているもの（**{n_overdue} / {len(resolved)} 件**）。",
        "",
    ]

    # 定義が腐っているもの
    broken = [r for r in resolved if r["err"] or not r["hits"]]
    if broken:
        out += [
            "### ⚠️ 定義の見直しが要るもの",
            "",
            "本文に 1 件も当たらない、または正規表現が壊れている事実です。"
            "本文の書き方が変わったか、定義が古くなっています。",
            "",
            "| 事実ID | 理由 |",
            "| :-- | :-- |",
        ]
        for r in broken:
            reason = r["err"] or "本文に該当するエントリが 0 件"
            out.append(f"| `{r['fact'].get('id', '')}` | {reason} |")
        out.append("")

    # 事実ごとの詳細
    out += ["---", "", "## 2. 事実ごとの影響範囲", ""]
    for r in resolved:
        fact = r["fact"]
        hits = r["hits"]
        out.append(f"### `{fact.get('id', '')}` {fact.get('label', '')}")
        out.append("")
        out.append(f"- **本書の記述**: {fact.get('book_says', '—')}")
        current = str(fact.get("current_value", "") or "").strip()
        out.append(f"- **最後に確認した実際の値**: {current if current else '_未確認_'}")
        out.append(f"- **最終確認**: {r['checked_disp']}（期限 {r['recheck_days']} 日）")
        source = str(fact.get("source", "") or "—")
        url = str(fact.get("url", "") or "").strip()
        out.append(f"- **確認先**: {source}" + (f" — {url}" if url else "（URL 未設定）"))
        if fact.get("note"):
            out.append(f"- **注意**: {fact['note']}")
        out.append(f"- **影響エントリ**: {len(hits)} 件")
        out.append("")
        if r["err"]:
            out += [f"  _{r['err']}_", ""]
            continue
        if hits:
            ids = "、".join(f"{e['id']} {e['title']}" for e in hits)
            out += [f"  {ids}", ""]
        else:
            out += ["  _該当なし_", ""]

    out += [
        "---",
        "",
        "## 使い方",
        "",
        "1. §1 で ⏰ が付いている事実を選ぶ",
        "2. 確認先の一次情報を見て、**本書の記述が今も成り立つか**を判断する",
        "3. `volatile_facts.yaml` の `current_value` と `last_checked` を更新する",
        "4. 記述が変わっていたら、§2 の影響エントリを直す。"
        "同じ事実に依存しているので、まとめて直すのが速いです",
        "5. 直したエントリ（変更が無かったものも含む）は `last_audited` を更新する。"
        "`python3 scripts/touch_last_audited.py --fact <事実ID>` で一括できます",
        "6. 監査した範囲を [freshness_audit_log.md](freshness_audit_log.md) に 1 行追記する",
        "",
        "事実を足したいときは `volatile_facts.yaml` に 1 ブロック書いてください。"
        "影響エントリの収集は `pattern`（正規表現）で自動化されるので、手で一覧を書く必要はありません。",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="時変ファクト watchlist を再生成する")
    ap.add_argument("--quiet", action="store_true", help="Hook 経由の無音実行")
    ap.add_argument("--fact", help="事実 ID を指定して影響エントリを標準出力へ")
    ap.add_argument("--ids", action="store_true", help="--fact で ID だけを改行区切りで出す")
    ap.add_argument("--no-write", action="store_true", help="台帳を書かずに集計だけ")
    args = ap.parse_args()

    facts = load_facts()
    if facts is None:
        if not args.quiet:
            print(
                "PyYAML が見つからないので skip しました（pip install pyyaml で有効になります）",
                file=sys.stderr,
            )
        return 0
    if not facts:
        if not args.quiet:
            print(f"{FACTS_PATH.name} に facts が定義されていません", file=sys.stderr)
        return 0

    entries = load_entries()
    today = date.today()

    if args.fact:
        target = next((f for f in facts if str(f.get("id", "")) == args.fact), None)
        if target is None:
            print(f"事実 ID が見つかりません: {args.fact}", file=sys.stderr)
            return 1
        hits, err = match_entries(target, entries)
        if err:
            print(err, file=sys.stderr)
            return 1
        if args.ids:
            for e in hits:
                print(e["id"])
        else:
            print(f"{target.get('id')} {target.get('label')} — 影響エントリ {len(hits)} 件")
            for e in hits:
                print(f"  {e['id']:>7} {e['title'][:24]:<24} {e['category']:<12} {e['path']}")
        return 0

    if not args.no_write:
        OUT_PATH.write_text(render(facts, entries, today), encoding="utf-8")
    if not args.quiet:
        n_over = 0
        for f in facts:
            lc = parse_date(f.get("last_checked"))
            if lc is None or (today - lc).days > int(f.get("recheck_days") or 90):
                n_over += 1
        print(
            f"updated: {OUT_PATH.relative_to(PROJECT_ROOT).as_posix()}  "
            f"({len(facts)} facts / 要再確認 {n_over} / {len(entries)} entries 走査)"
        )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        try:
            sys.stdout.close()
        finally:
            sys.exit(0)
