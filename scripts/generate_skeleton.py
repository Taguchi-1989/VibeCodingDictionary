#!/usr/bin/env python3
"""
スケルトンエントリ生成スクリプト

ledgers/entries.csv の path 空欄行（＝未生成エントリ）に対して、
templates/skeleton_template.md を流し込んだスケルトン md を作る。
作成後、entries.csv の path / status を更新する。

スケルトンとは:
    - YAML フロントマター ＋ 必須節の見出しだけ置いた、本文未着手の状態
    - status: skeleton
    - validator は archived/sample と同様にスキップする
    - 本書きでは status を `drafting` に上げ、entry-writer サブエージェントに渡す

使い方:
    # 全件（path 空の全行に対して生成）
    python3 scripts/generate_skeleton.py

    # 単発
    python3 scripts/generate_skeleton.py B-4

    # letter 単位
    python3 scripts/generate_skeleton.py --letter B

    # 範囲（カンマ区切り）
    python3 scripts/generate_skeleton.py --range B-4,B-9,C-3

    # 影響だけ確認したい
    python3 scripts/generate_skeleton.py --dry-run

    # 既存ファイルがあっても上書き（通常は skip）
    python3 scripts/generate_skeleton.py --force B-4
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import re
import sys
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "ledgers" / "entries.csv"
CANDIDATES_PATH = ROOT / "ledgers" / "entry_candidates.md"
TEMPLATE_PATH = ROOT / "templates" / "skeleton_template.md"
ENTRIES_DIR = ROOT / "content" / "entries"

# category（CSV）→ ディレクトリ名
CATEGORY_DIR_MAP = {
    "common": "common",
    "service": "service",
    "model": "model",
    "term": "term",
    "term_general": "term_general",
    "tool": "tool",
    "workflow": "workflow",
    "history": "history",
    "person": "person",
    "person_org": "person",   # 既存規約に合わせて person ディレクトリへ
    "benchmark": "benchmark",
    "mcp": "mcp",
}

# 日本語タイトル → 英語スラグ（手動マップ）
# 必要に応じて書き足す。マップに無い日本語タイトルは ID のみのファイル名にする。
SLUG_OVERRIDES: dict[str, str] = {
    # Lv6 自己学習シェルフ（和文・混在タイトル用、2026-06-22）
    "J-94": "parallelism",
    "J-95": "semiconductor_supply_chain",
    "J-96": "semiconductor_equipment",
    "J-97": "electronic_materials",
    "J-98": "critical_minerals_geopolitics",
    "J-99": "cowos",
    "J-101": "semiconductor_process",
    "J-102": "chiplet_3d_stacking",
    "J-103": "loop_engineering",
    "J-104": "react_agent_loop",
    "J-105": "context_management",
    "J-106": "harness_engineering",
    "J-107": "autonomous_loop_guardrails",
    "J-108": "ralph_loop",
    "J-109": "model_routing",
    "J-110": "uncertainty_deferral",
    "J-111": "human_cognition_bottleneck",
    "J-112": "cognitive_cost_quantification",
    "J-113": "generative_ui_agent_native",
    "C-15": "intel",
    "J-89": "moe_routing",
    "J-25": "tokenizer_bpe",
    "J-26": "latent_space",
    "J-82": "speculative_decoding",
    "J-84": "batch_inference",
    "J-85": "throughput_latency",
    "A-1": "preface",
    "A-2": "reading_guide",
    "A-3": "walking_guide",
    "A-4": "experience_legend",
    "A-5": "reader_level_legend",
    "A-6": "evaluation_date_legend",
    "A-7": "figure_types_legend",
    "A-8": "color_symbol_legend",
    "A-9": "index",
    "A-10": "changelog",
    "A-11": "abbreviations",
    # B 料金プラン系
    "B-50": "claude_pricing",
    "B-51": "chatgpt_pricing",
    "B-52": "gemini_pricing",
    # 既存の archived 命名と整合させる
    "D-2": "gemini25",
    "D-11": "claude35",
    "D-12": "claude4",
}


def parse_candidate_descriptions() -> dict[str, str]:
    """entry_candidates.md から ID → 一言（"—" の右側）を抜く。

    形式: `- **B-4 Cursor** — AI を中核にしたエディタ／IDE サービス`
    """
    text = CANDIDATES_PATH.read_text(encoding="utf-8")
    result: dict[str, str] = {}
    pat = re.compile(r"^\-\s+\*\*([A-J]-\d+)\s+[^*]+\*\*\s+[—\-–]\s+(.+)$", re.MULTILINE)
    for m in pat.finditer(text):
        entry_id = m.group(1).strip()
        desc = m.group(2).strip()
        # （checked YYYY-MM-DD）等の末尾装飾を残しても tagline seed としては許容
        result[entry_id] = desc
    return result


def make_slug(entry_id: str, title: str) -> str | None:
    """タイトルから英語スラグを作る。日本語混じりは None を返す（→ ID のみのファイル名）。

    優先順:
        1. SLUG_OVERRIDES に登録があればそれを使う
        2. ASCII（記号と数字を含む英数字）だけならスラグ化
        3. それ以外は None
    """
    if entry_id in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[entry_id]

    # （...） や (…) の補足を取り除く
    t = re.sub(r"[（(][^)）]*[)）]", "", title).strip()

    # 「Claude の料金プラン」みたいに日本語が混ざるパターンは ASCII 抽出が空になる
    ascii_only = re.sub(r"[^A-Za-z0-9\s\-\._/]", "", t).strip()
    has_japanese = any(ord(c) > 127 for c in t)

    if has_japanese:
        # ASCII 部分があれば（"GPT-3 系" → "gpt-3" など）ASCII だけスラグ化したいが、
        # 誤解を生むのでマップ未登録の和文タイトルは ID のみで運用する
        return None

    if not ascii_only:
        return None

    slug = re.sub(r"[^A-Za-z0-9]+", "_", t.lower()).strip("_")
    return slug or None


def build_path(entry_id: str, title: str, category: str) -> Path:
    """エントリの保存先パスを決める。

    - {ID}_{slug}.md（slug が作れる場合）
    - {ID}.md（日本語タイトル等で slug が無い場合）
    """
    cat_dir = CATEGORY_DIR_MAP.get(category, category)
    slug = make_slug(entry_id, title)
    fname = f"{entry_id}_{slug}.md" if slug else f"{entry_id}.md"
    return ENTRIES_DIR / cat_dir / fname


def load_template() -> str:
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def render_skeleton(
    entry_id: str,
    title: str,
    category: str,
    subtype: str,
    tagline_seed: str,
    today: str,
) -> str:
    """skeleton_template.md のプレースホルダを埋める。"""
    tpl = load_template()
    return (
        tpl.replace("{{ID}}", entry_id)
        .replace("{{TITLE}}", title)
        .replace("{{CATEGORY}}", category)
        .replace("{{SUBTYPE}}", subtype or "")
        .replace("{{TAGLINE_SEED}}", tagline_seed or "")
        .replace("{{TODAY}}", today)
    )


def normalize_tagline(desc: str) -> str:
    """候補リストの一言を tagline 仮値に整える。

    - 末尾の「（checked YYYY-MM-DD）」は残す（時変情報の手がかり）
    - 改行や HTML エンティティは除去
    """
    s = desc.strip()
    s = re.sub(r"\s+", " ", s)
    return s


# ─── CSV 操作 ─────────────────────────────────────────


def read_csv() -> tuple[list[str], list[dict]]:
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    return fieldnames, rows


def write_csv(fieldnames: list[str], rows: list[dict]) -> None:
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# ─── メイン ─────────────────────────────────────────


def select_targets(
    rows: list[dict],
    only_id: str | None,
    only_letter: str | None,
    id_range: list[str] | None,
) -> list[dict]:
    targets: list[dict] = []
    for row in rows:
        entry_id = row.get("new_id", "").strip()
        if not entry_id:
            continue

        # フィルタ
        if only_id and entry_id != only_id:
            continue
        if only_letter and not entry_id.startswith(only_letter + "-"):
            continue
        if id_range and entry_id not in id_range:
            continue

        # 既に書かれているエントリ（CSV の path 列が埋まっている）は対象外。
        # スケルトンは「未生成」のものだけに当てる。既存 md は手で書かれた本文なので壊さない。
        existing_path = row.get("path", "").strip()
        if existing_path:
            full = ROOT / existing_path
            if full.exists():
                continue

        targets.append(row)
    return targets


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("entry_id", nargs="?", help="単一 ID（例: B-4）")
    ap.add_argument("--letter", help="letter 一文字（例: B）")
    ap.add_argument("--range", dest="id_range", help="カンマ区切り ID（例: B-4,B-9,C-3）")
    ap.add_argument("--dry-run", action="store_true", help="ファイルを書かずに対象だけ表示")
    args = ap.parse_args()

    if not TEMPLATE_PATH.exists():
        print(f"テンプレが見つかりません: {TEMPLATE_PATH}", file=sys.stderr)
        return 2
    if not CSV_PATH.exists():
        print(f"CSV が見つかりません: {CSV_PATH}", file=sys.stderr)
        return 2

    fieldnames, rows = read_csv()
    if "path" not in fieldnames:
        fieldnames = list(fieldnames) + ["path"]

    descriptions = parse_candidate_descriptions()
    today = dt.date.today().isoformat()

    id_range_list = (
        [s.strip() for s in args.id_range.split(",") if s.strip()] if args.id_range else None
    )

    targets = select_targets(
        rows,
        only_id=args.entry_id,
        only_letter=args.letter,
        id_range=id_range_list,
    )

    if not targets:
        print("対象がありません（既に生成済みの可能性）。")
        return 0

    print(f"対象 {len(targets)} 件:")
    for row in targets:
        print(f"  {row['new_id']:6s}  {row.get('title','')}  ({row.get('category','')})")

    if args.dry_run:
        print("\n--dry-run のため書き出しません。")
        return 0

    written = 0
    skipped = 0
    for row in targets:
        entry_id = row["new_id"].strip()
        title = (row.get("title") or "").strip()
        category = (row.get("category") or "").strip()
        subtype = (row.get("subtype") or "").strip()
        seed = normalize_tagline(descriptions.get(entry_id, title))

        out_path = build_path(entry_id, title, category)
        out_path.parent.mkdir(parents=True, exist_ok=True)

        if out_path.exists():
            # 二重防護: select_targets で弾けていないケースに備え、ここでも既存ファイルは上書きしない。
            # 上書きが本当に必要なら手で削除してから再生成する運用にする（事故防止）。
            print(f"  skip (file exists, no overwrite): {out_path.relative_to(ROOT)}")
            skipped += 1
            continue

        body = render_skeleton(
            entry_id=entry_id,
            title=title,
            category=category,
            subtype=subtype,
            tagline_seed=seed,
            today=today,
        )
        out_path.write_text(body, encoding="utf-8")

        rel = out_path.relative_to(ROOT).as_posix()
        row["path"] = rel
        # CSV 上の status を skeleton に上げる（candidate / drafting の手前）
        # 既に needs_review / ready / archived 等になっている行は触らない
        cur_status = (row.get("status") or "").strip()
        if cur_status in ("", "candidate"):
            row["status"] = "skeleton"

        print(f"  wrote: {rel}")
        written += 1

    write_csv(fieldnames, rows)

    print()
    print(f"書き出し: {written} 件 / スキップ: {skipped} 件")
    print(f"CSV 更新: {CSV_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
