#!/usr/bin/env python3
"""
鮮度監査キュー（ledgers/freshness_queue.md）を再生成するスクリプト

「陳腐化していそうなエントリ」を 1 画面で見えるようにします。
revision_queue.md（＝文章の直し）とは作業種別が違うので別台帳にしています。
こちらは **事実の再確認**（最新モデル名・料金・提供状況が今も正しいか）です。

Usage:
    python3 scripts/audit_freshness.py                 # 台帳を再生成して要約を表示
    python3 scripts/audit_freshness.py --quiet         # Hook 経由（無音）
    python3 scripts/audit_freshness.py --list          # 期限超過を標準出力に一覧
    python3 scripts/audit_freshness.py --list --tier S --letter D
    python3 scripts/audit_freshness.py --list --details  # 確認すべき本文行も出す
    python3 scripts/audit_freshness.py --as-of 2026-12-01 --list  # 未来日で素振り

設計メモ（2026-09-19 追加）:
    - 経過日数だけでは測らない。「変数」と「Claude Opus」を同列に並べても意味が無いので、
      frontmatter から **陳腐化しやすさ（Tier S/A/B）** を導出し、Tier ごとに期限を変える
    - Tier は原則自動導出。例外だけ任意フィールド `volatility: high|mid|low` で上書きする
    - 確認日は `last_audited`（＝最後に事実を確認した日）を正とし、無ければ
      `evaluation_date` にフォールバックする。`evaluation_date` は執筆時点の記録として
      凍結し、「見たが変化なし」は `last_audited` の更新だけで済ませる
    - 本文の時変シグナル（モデル名・バージョン・価格・時点表現・提供状況）を
      **行単位**で拾う。1 エントリあたり確認すべき箇所が数行に絞れるので、
      100 件規模でも現実的な作業量に落ちる
    - 誌面に刷られない節（著者記入欄・裏台帳メモ）はシグナル検出の対象外。
      出典メモの checked 日付を時点表現として誤検出するのを避ける狙いもある
    - ☆ 違反にはしない。鮮度は刊行ブロックではなく棚卸しの優先順位付けなので、
      validator 側は書式の警告だけに留める
"""

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_entry import extract_printed_body, parse_frontmatter  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "content" / "entries"
QUEUE_PATH = PROJECT_ROOT / "ledgers" / "freshness_queue.md"

SKIP_STATUSES = {"skeleton", "sample", "archived"}

# ─── Tier（陳腐化しやすさ）の導出ルール ─────────────────
# 期限は「この日数を過ぎたら事実を見に行く」の目安。docs/entry_schema.yaml と対。
TIER_LIMIT_DAYS = {"S": 90, "A": 180, "B": 365}

TIER_LABEL = {
    "S": "S（高）",
    "A": "A（中）",
    "B": "B（低）",
}

# category だけで Tier S に上げるもの（外の世界が動くと本文が古くなる）
HIGH_CATEGORIES = {"model", "service", "benchmark", "mcp", "tool_agent"}
# category だけで Tier A に上げるもの
MID_CATEGORIES = {"term_tool", "person_org", "workflow"}

# 任意フィールド volatility での手動上書き
VOLATILITY_TO_TIER = {"high": "S", "mid": "A", "low": "B"}

# ─── 本文の時変シグナル ─────────────────────────────
# ラベル → (正規表現, 短い説明)
SIGNALS: list[tuple[str, re.Pattern, str]] = [
    (
        "モデル名",
        re.compile(
            r"(GPT-?\d(\.\d)?|Claude\s*(Opus|Sonnet|Haiku)\s*\d*(\.\d)?|Claude\s*\d(\.\d)?"
            r"|Gemini\s*\d(\.\d)?|Llama\s*\d|(?<![A-Za-z])o\d(?![A-Za-z0-9])"
            r"|DeepSeek|Grok\s*\d|Qwen|Mistral)"
        ),
        "後継モデルが出ていないか",
    ),
    (
        "バージョン",
        re.compile(r"(?<![\w.])v?\d+\.\d+(\.\d+)?(?![\w.])"),
        "バージョン番号が現行か",
    ),
    (
        "価格",
        re.compile(
            r"(\$\s?\d|\d+\s*ドル|月額|年額|無料枠|無料プラン|従量課金|トークン単価"
            r"|per\s*(month|token)|/\s*1M)"
        ),
        "料金・無料枠が変わっていないか",
    ),
    (
        "時点表現",
        re.compile(r"(現在|現時点|最新|時点で|今のところ|20\d\d\s*年)"),
        "「現在」「最新」が今も成り立つか",
    ),
    (
        "提供状況",
        re.compile(
            r"(ベータ|β版|プレビュー|一般提供|提供終了|提供停止|サポート終了"
            r"|非推奨|deprecated|後継|廃止)"
        ),
        "提供状況（ベータ／終了）が現状と合うか",
    ),
]

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_date(value: str) -> date | None:
    value = str(value).strip().strip('"').strip("'")
    if not DATE_RE.match(value):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def derive_tier(fm: dict, signal_labels: list[str]) -> tuple[str, str]:
    """(tier, 判定理由) を返す。volatility があれば最優先。"""
    volatility = str(fm.get("volatility", "")).strip().lower()
    if volatility in VOLATILITY_TO_TIER:
        return VOLATILITY_TO_TIER[volatility], f"volatility: {volatility}（手動指定）"

    category = str(fm.get("category", "")).strip()
    version_status = str(fm.get("version_status", "")).strip()
    pricing_note = str(fm.get("pricing_note", "")).strip()

    if category in HIGH_CATEGORIES:
        return "S", f"category: {category}"
    if version_status in {"preview", "deprecated"}:
        return "S", f"version_status: {version_status}"
    if pricing_note in {"paid", "freemium"}:
        return "S", f"pricing_note: {pricing_note}"
    if category in MID_CATEGORIES:
        return "A", f"category: {category}"
    if len(signal_labels) >= 3:
        return "A", f"本文シグナル {len(signal_labels)} 種"
    return "B", f"category: {category}" if category else "時変シグナルなし"


def scan_signals(printed: str) -> tuple[list[str], list[tuple[str, str]]]:
    """(検出ラベル一覧, [(ラベル, 該当行), ...]) を返す。"""
    labels: list[str] = []
    lines: list[tuple[str, str]] = []
    seen_lines: set[str] = set()
    for label, rx, _hint in SIGNALS:
        hit_line = None
        for raw in printed.split("\n"):
            line = raw.strip()
            if not line or line.startswith("#") or line.startswith("<!--"):
                continue
            if rx.search(line):
                if hit_line is None:
                    hit_line = line
                break
        if hit_line is not None:
            labels.append(label)
            if hit_line not in seen_lines:
                seen_lines.add(hit_line)
                lines.append((label, hit_line))
    return labels, lines


def letter_of(entry_id: str) -> str:
    m = re.match(r"^([A-J])-", entry_id)
    return m.group(1) if m else "-"


def sort_key(row: dict) -> tuple:
    """ID を letter + 数値で自然順に。"""
    m = re.match(r"^([A-J])-(\d+)$", row["id"])
    if m:
        return (0, m.group(1), int(m.group(2)))
    return (1, row["id"], 0)


def collect(as_of: date) -> list[dict]:
    rows: list[dict] = []
    for md_path in sorted(ENTRIES_DIR.rglob("*.md")):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, body = parse_frontmatter(text)
        if not fm:
            continue
        status = str(fm.get("status", "")).strip()
        if status in SKIP_STATUSES:
            continue
        layout = str(fm.get("page_layout", "")).strip()
        if layout.startswith("front_") or layout.startswith("back_"):
            continue

        printed = extract_printed_body(body)
        signal_labels, signal_lines = scan_signals(printed)
        tier, tier_reason = derive_tier(fm, signal_labels)

        audited = parse_date(fm.get("last_audited", ""))
        evaluated = parse_date(fm.get("evaluation_date", ""))
        checked = audited or evaluated
        age = (as_of - checked).days if checked else None
        limit = TIER_LIMIT_DAYS[tier]
        overdue = age is not None and age > limit

        rows.append(
            {
                "id": str(fm.get("id", "")).strip(),
                "title": str(fm.get("title", "")).strip(),
                "category": str(fm.get("category", "")).strip(),
                "status": status,
                "tier": tier,
                "tier_reason": tier_reason,
                "checked": checked,
                "checked_source": "last_audited" if audited else "evaluation_date",
                "age": age,
                "limit": limit,
                "overdue": overdue,
                "signals": signal_labels,
                "signal_lines": signal_lines,
                "path": md_path.relative_to(PROJECT_ROOT).as_posix(),
                "letter": letter_of(str(fm.get("id", "")).strip()),
            }
        )
    return rows


# ─── 台帳のレンダリング ─────────────────────────────

def render(rows: list[dict], as_of: date) -> str:
    total = len(rows)
    overdue = [r for r in rows if r["overdue"]]
    unknown = [r for r in rows if r["age"] is None]
    by_tier: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_tier[r["tier"]].append(r)

    out: list[str] = [
        "# 鮮度監査キュー（自動生成）",
        "",
        f"*基準日 {as_of.isoformat()} — `python3 scripts/audit_freshness.py` が再生成します。"
        "手で編集しないでください。*",
        "",
        "このキューは「文章を直す」ための [revision_queue.md](revision_queue.md) とは別で、"
        "**事実がまだ正しいかを見に行く**ための台帳です。"
        "最新モデル名・料金・提供状況のように、こちらが何もしなくても外の世界が動いて古くなる情報を扱います。",
        "",
        "---",
        "",
        "## 1. 全体像",
        "",
        f"- 監査対象: **{total} 件**（skeleton / sample / archived と前付け・巻末は対象外）",
        f"- 期限超過: **{len(overdue)} 件**",
        f"- 確認日が読めない: {len(unknown)} 件",
        "",
        "| Tier | 意味 | 再確認の期限 | 件数 | 期限超過 |",
        "| :-- | :-- | --: | --: | --: |",
    ]
    tier_meaning = {
        "S": "モデル・サービス・ベンチマーク・MCP・有料/フリーミアム・preview/deprecated",
        "A": "ツール用語・人物組織・ワークフロー、または本文に時変シグナル 3 種以上",
        "B": "一般用語・歴史・概念など、外の世界が動いても古くならないもの",
    }
    for tier in "SAB":
        group = by_tier.get(tier, [])
        n_over = sum(1 for r in group if r["overdue"])
        out.append(
            f"| {TIER_LABEL[tier]} | {tier_meaning[tier]} | {TIER_LIMIT_DAYS[tier]} 日 | "
            f"{len(group)} | {n_over} |"
        )
    out.append("")

    # 経過日数の分布
    buckets = Counter()
    for r in rows:
        age = r["age"]
        if age is None:
            buckets["不明"] += 1
        elif age <= 90:
            buckets["90 日以内"] += 1
        elif age <= 180:
            buckets["91〜180 日"] += 1
        elif age <= 365:
            buckets["181〜365 日"] += 1
        else:
            buckets["365 日超"] += 1
    out += ["### 最終確認からの経過", "", "| 経過 | 件数 |", "| :-- | --: |"]
    for key in ["90 日以内", "91〜180 日", "181〜365 日", "365 日超", "不明"]:
        if buckets[key]:
            out.append(f"| {key} | {buckets[key]} |")
    out.append("")

    # 優先順（category 別）
    out += [
        "---",
        "",
        "## 2. どこから手を付けるか",
        "",
        "期限超過を category 別に並べたものです。上から束で片付けるのが速いです"
        "（同じ一次情報で複数エントリを確認できるため）。",
        "",
        "| category | 期限超過 | 主な確認ポイント |",
        "| :-- | --: | :-- |",
    ]
    cat_hint = {
        "model": "後継モデルの有無・提供終了・コンテキスト長",
        "service": "料金プラン・無料枠・提供地域・名称変更",
        "benchmark": "スコアの更新・上位モデルの入れ替わり",
        "mcp": "公式／コミュニティの別・配布場所・対応クライアント",
        "tool_agent": "バージョン・対応モデル・提供形態",
        "term_tool": "ツールのバージョン・推奨手順の変化",
        "person_org": "所属・役職・社名の変更",
    }
    for cat, n in Counter(r["category"] for r in overdue).most_common():
        out.append(f"| {cat} | {n} | {cat_hint.get(cat, '本文の時変シグナルを参照')} |")
    if not overdue:
        out.append("| — | 0 | 期限超過はありません |")
    out.append("")

    # 期限超過の一覧
    out += ["---", "", "## 3. 期限超過エントリ", ""]
    for tier in "SAB":
        group = sorted(
            [r for r in by_tier.get(tier, []) if r["overdue"]],
            key=lambda r: (-(r["age"] or 0), sort_key(r)),
        )
        out.append(f"### Tier {TIER_LABEL[tier]} — {len(group)} 件（期限 {TIER_LIMIT_DAYS[tier]} 日）")
        out.append("")
        if not group:
            out += ["_なし_", ""]
            continue
        out += [
            "| ID | 用語 | category | 最終確認 | 経過 | 時変シグナル | path |",
            "| :-- | :-- | :-- | :-- | --: | :-- | :-- |",
        ]
        for r in group:
            source_mark = "" if r["checked_source"] == "last_audited" else "※"
            signals = "／".join(r["signals"]) if r["signals"] else "—"
            out.append(
                f"| {r['id']} | {r['title']} | {r['category']} | "
                f"{r['checked'].isoformat()}{source_mark} | {r['age']} 日 | {signals} | "
                f"`{r['path']}` |"
            )
        out.append("")
    out.append("※ = `last_audited` が未記入で `evaluation_date` を代用しているもの。")
    out.append("")

    # 確認ポイント（本文行）
    s_overdue = sorted(
        [r for r in by_tier.get("S", []) if r["overdue"]],
        key=lambda r: (-(r["age"] or 0), sort_key(r)),
    )
    out += [
        "---",
        "",
        "## 4. 確認すべき本文行（Tier S の期限超過）",
        "",
        "エントリを開かなくても「どこを見ればいいか」が分かるように、"
        "時変シグナルに当たった行を 1 種類につき 1 行だけ抜いています。",
        "",
    ]
    for r in s_overdue:
        if not r["signal_lines"]:
            continue
        out.append(f"**{r['id']} {r['title']}**（{r['age']} 日経過）")
        out.append("")
        for label, line in r["signal_lines"]:
            snippet = line if len(line) <= 90 else line[:90] + "…"
            out.append(f"- `{label}` {snippet}")
        out.append("")
    if not s_overdue:
        out += ["_なし_", ""]

    # 確認日が読めないもの
    if unknown:
        out += [
            "---",
            "",
            "## 5. 確認日が読めないエントリ",
            "",
            "| ID | 用語 | status | path |",
            "| :-- | :-- | :-- | :-- |",
        ]
        for r in sorted(unknown, key=sort_key):
            out.append(f"| {r['id']} | {r['title']} | {r['status']} | `{r['path']}` |")
        out.append("")

    out += [
        "---",
        "",
        "## 使い方",
        "",
        "1. §2 で束を選ぶ（モデル → サービス → ベンチマーク → MCP の順が安いです）",
        "2. §4 の該当行を見ながら一次情報（公式ドキュメント・料金ページ）を確認する",
        "3. **変更が無かった場合**: frontmatter の `last_audited` を確認日に更新するだけで完了です。"
        "`evaluation_date` は執筆時点の記録なので動かしません",
        "4. **変更があった場合**: 本文を直し、出典メモの `checked YYYY-MM-DD` も合わせ、"
        "`last_audited` を更新します。本文の改訂は entry-writer サブエージェントに渡せます",
        "5. 監査した範囲と結果は [freshness_audit_log.md](freshness_audit_log.md) に 1 行追記してください",
        "",
        "Tier の判定が実態と合わないときは、frontmatter に "
        "`volatility: high | mid | low` を足すと上書きできます"
        "（[docs/entry_schema.yaml](../docs/entry_schema.yaml) 参照）。",
        "",
    ]
    return "\n".join(out)


# ─── 標準出力への一覧 ───────────────────────────────

def print_list(rows: list[dict], args) -> None:
    target = [r for r in rows if r["overdue"]]
    if args.tier:
        target = [r for r in target if r["tier"] == args.tier.upper()]
    if args.letter:
        target = [r for r in target if r["letter"] == args.letter.upper()]
    if args.category:
        target = [r for r in target if r["category"] == args.category]
    target.sort(key=lambda r: (r["tier"], -(r["age"] or 0), sort_key(r)))

    if not target:
        print("期限超過なし")
        return
    for r in target:
        signals = ",".join(r["signals"]) if r["signals"] else "-"
        print(
            f"[{r['tier']}] {r['id']:>7} {r['title'][:20]:<20} {r['category']:<12} "
            f"{r['checked'].isoformat()} ({r['age']:>3} 日) {signals}"
        )
        if args.details:
            for label, line in r["signal_lines"]:
                snippet = line if len(line) <= 100 else line[:100] + "…"
                print(f"          {label}: {snippet}")
    print(f"\n計 {len(target)} 件")


def main() -> int:
    ap = argparse.ArgumentParser(description="エントリの鮮度（事実の古さ）を監査する")
    ap.add_argument("--quiet", action="store_true", help="Hook 経由の無音実行")
    ap.add_argument("--list", action="store_true", help="期限超過を標準出力に一覧する")
    ap.add_argument("--details", action="store_true", help="--list に確認すべき本文行を添える")
    ap.add_argument("--tier", help="S / A / B で絞る")
    ap.add_argument("--letter", help="章 letter（A〜J）で絞る")
    ap.add_argument("--category", help="category で絞る")
    ap.add_argument("--as-of", help="基準日 YYYY-MM-DD（既定は今日）")
    ap.add_argument("--no-write", action="store_true", help="台帳を書かずに集計だけ")
    args = ap.parse_args()

    as_of = parse_date(args.as_of) if args.as_of else date.today()
    if as_of is None:
        print("--as-of は YYYY-MM-DD で指定してください", file=sys.stderr)
        return 1

    rows = collect(as_of)
    if not args.no_write:
        QUEUE_PATH.write_text(render(rows, as_of), encoding="utf-8")

    if args.list:
        print_list(rows, args)
        return 0

    if not args.quiet:
        overdue = [r for r in rows if r["overdue"]]
        by_tier = Counter(r["tier"] for r in overdue)
        print(
            f"updated: {QUEUE_PATH.relative_to(PROJECT_ROOT).as_posix()}  "
            f"({len(rows)} entries / 期限超過 {len(overdue)} "
            f"[S {by_tier['S']} / A {by_tier['A']} / B {by_tier['B']}])"
        )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # `| head` で切られたときに traceback を出さない
        try:
            sys.stdout.close()
        finally:
            sys.exit(0)
