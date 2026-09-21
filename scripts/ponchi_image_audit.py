#!/usr/bin/env python3
"""Audit ponchi image scale, ink load, and logo clearspace cleanliness.

Two different things used to be called "density" here, which made the old
`bbox_coverage >= 0.50` gate read as "draw more stuff":

- span      = ink bounding box / canvas. How BIG the drawing is drawn.
              Should be high and, above all, consistent across the book.
- ink_ratio = painted pixels / canvas. How MUCH is drawn.
              Should be low; this is the reader's information load.

A good ponchi image has a high span and a low ink ratio: few elements, drawn
large. See docs/ponchi_clarity_first_prompt_2026-09-20.md.
"""
from __future__ import annotations

import argparse
import csv
import statistics
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageDraw
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("This script requires Pillow. Use the bundled Codex Python runtime.") from exc


def ink_mask(image: Image.Image) -> Image.Image:
    """Return a 0/255 mask of pixels that read as ink rather than paper."""
    rgb = image.convert("RGB")
    dark_r, dark_g, dark_b = (ImageChops.invert(channel) for channel in rgb.split())
    # min darkness across channels > 18, or total darkness > 55 (add clips at
    # 255, which is harmless because the threshold is far below the clip point)
    min_dark = ImageChops.darker(ImageChops.darker(dark_r, dark_g), dark_b)
    sum_dark = ImageChops.add(ImageChops.add(dark_r, dark_g), dark_b)
    return ImageChops.lighter(
        min_dark.point(lambda value: 255 if value > 18 else 0),
        sum_dark.point(lambda value: 255 if value > 55 else 0),
    )


def ink_metrics(image: Image.Image) -> tuple[float, float]:
    """Return (span, ink_ratio) for one image."""
    mask = ink_mask(image)
    total = image.width * image.height
    painted = sum(count for value, count in enumerate(mask.histogram()) if value)
    box = mask.getbbox()
    span = 0.0 if box is None else ((box[2] - box[0]) * (box[3] - box[1])) / total
    return span, painted / total


def clearspace_ink_ratio(image: Image.Image, x_start_ratio: float, y_end_ratio: float) -> float:
    x_start = int(image.width * x_start_ratio)
    y_end = int(image.height * y_end_ratio)
    total = max(1, (image.width - x_start) * y_end)
    region = ink_mask(image).crop((x_start, 0, image.width, y_end))
    ink = sum(count for value, count in enumerate(region.histogram()) if value)
    return ink / total


def entry_id_from_path(path: Path) -> str:
    name = path.name
    for suffix in (
        "_base_1254x627.png",
        "_overlay_1254x627.png",
        "_base_selected_1254x627.png",
        ".webp",
        ".png",
    ):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return path.stem.split("_", 1)[0]


def load_clearspace_requirements(args: argparse.Namespace) -> dict[str, bool]:
    if not args.ledger or not args.batch_id:
        return {}
    requirements: dict[str, bool] = {}
    with args.ledger.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("batch_id") != args.batch_id:
                continue
            entry_id = row.get("entry_id", "")
            logo_need = row.get("logo_need", "")
            logo_status = row.get("logo_status", "")
            requirements[entry_id] = not (
                logo_need in {"not_needed", "avoid", "none"}
                or logo_status in {"logo_avoid", "not_required"}
            )
    return requirements


def audit_image(path: Path, args: argparse.Namespace, clearspace_requirements: dict[str, bool]) -> dict[str, str]:
    image = Image.open(path).convert("RGB")
    span, ink_ratio = ink_metrics(image)
    clearspace = clearspace_ink_ratio(image, args.clearspace_x_start, args.clearspace_y_end)
    entry_id = entry_id_from_path(path)
    clearspace_required = clearspace_requirements.get(entry_id, True)
    size_ok = image.size == (args.width, args.height)
    span_ok = args.span_min <= span <= args.span_max
    ink_ok = args.ink_min <= ink_ratio <= args.ink_max
    clearspace_ok = (clearspace <= args.max_clearspace_ink) if clearspace_required else True
    status = "pass" if size_ok and span_ok and ink_ok and clearspace_ok else "review"
    return {
        "file": str(path),
        "entry_id": entry_id,
        "size": f"{image.width}x{image.height}",
        "size_ok": str(size_ok).lower(),
        "bbox_coverage": f"{span:.3f}",
        "span_ok": str(span_ok).lower(),
        "span_verdict": span_verdict(span, args),
        "ink_ratio": f"{ink_ratio:.3f}",
        "ink_ok": str(ink_ok).lower(),
        "ink_verdict": ink_verdict(ink_ratio, args),
        "clearspace_required": str(clearspace_required).lower(),
        "clearspace_ink_ratio": f"{clearspace:.4f}",
        "clearspace_ok": str(clearspace_ok).lower(),
        "status": status,
    }


def span_verdict(span: float, args: argparse.Namespace) -> str:
    if span < args.span_min:
        return "too_small"
    if span > args.span_max:
        return "too_large"
    return "in_band"


def ink_verdict(ink_ratio: float, args: argparse.Namespace) -> str:
    if ink_ratio < args.ink_min:
        return "too_light"
    if ink_ratio > args.ink_max:
        return "too_heavy"
    return "in_band"


def write_markdown(rows: list[dict[str, str]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("# Ponchi Image Audit\n\n")
        handle.write(
            "span = インクの外接矩形 ÷ キャンバス（**大きさ**。高く、かつ揃える）／"
            "ink = 塗られた画素 ÷ キャンバス（**情報量**。低く抑える）。\n\n"
        )
        handle.write("| file | size | span | span verdict | ink | ink verdict | clearspace required | clearspace ink | status |\n")
        handle.write("| :-- | :-- | --: | :-- | --: | :-- | :-- | --: | :-- |\n")
        for row in rows:
            handle.write(
                "| "
                f"`{Path(row['file']).name}` | `{row['size']}` | "
                f"{row['bbox_coverage']} | `{row['span_verdict']}` | "
                f"{row['ink_ratio']} | `{row['ink_verdict']}` | "
                f"`{row['clearspace_required']}` | "
                f"{row['clearspace_ink_ratio']} | "
                f"`{row['status']}` |\n"
            )


def write_contact_sheet(rows: list[dict[str, str]], out: Path) -> None:
    thumb_w, thumb_h = 418, 209
    label_h = 50
    cols = 3
    row_count = (len(rows) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, row_count * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, row in enumerate(rows):
        source = Path(row["file"])
        col = index % cols
        sheet_row = index // cols
        x0 = col * thumb_w
        y0 = sheet_row * (thumb_h + label_h)
        image = Image.open(source).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        outline = (110, 170, 110) if row["status"] == "pass" else (210, 140, 80)
        draw.rectangle([x0, y0, x0 + thumb_w - 1, y0 + thumb_h + label_h - 1], outline=outline)
        draw.text((x0 + 8, y0 + 8), f"{source.stem}", fill=(20, 20, 20))
        draw.text(
            (x0 + 8, y0 + 27),
            f"span {row['bbox_coverage']}  ink {row['ink_ratio']}  {row['status']}",
            fill=(80, 80, 80),
        )
        sheet.paste(image, (x0 + (thumb_w - image.width) // 2, y0 + label_h + (thumb_h - image.height) // 2))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--out-csv", type=Path, default=None)
    parser.add_argument("--out-md", type=Path, default=None)
    parser.add_argument("--contact-sheet", type=Path, default=None)
    parser.add_argument("--width", type=int, default=1254)
    parser.add_argument("--height", type=int, default=627)
    # span band: how big the drawing is drawn. A band, not a floor - the point
    # is that every spread in the book reads at the same scale.
    parser.add_argument("--span-min", type=float, default=0.78)
    parser.add_argument("--span-max", type=float, default=0.90)
    # ink band: how much is drawn. This is the reader's information load.
    parser.add_argument("--ink-min", type=float, default=0.08)
    parser.add_argument("--ink-max", type=float, default=0.14)
    parser.add_argument(
        "--min-bbox-coverage",
        type=float,
        default=None,
        help="deprecated alias for --span-min",
    )
    parser.add_argument("--clearspace-x-start", type=float, default=0.60)
    parser.add_argument("--clearspace-y-end", type=float, default=0.25)
    parser.add_argument("--max-clearspace-ink", type=float, default=0.015)
    parser.add_argument("--ledger", type=Path, default=None)
    parser.add_argument("--batch-id", default=None)
    args = parser.parse_args()
    if args.min_bbox_coverage is not None:
        args.span_min = args.min_bbox_coverage

    clearspace_requirements = load_clearspace_requirements(args)
    rows = [audit_image(path, args, clearspace_requirements) for path in args.images]
    if args.out_csv:
        args.out_csv.parent.mkdir(parents=True, exist_ok=True)
        with args.out_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    if args.out_md:
        write_markdown(rows, args.out_md)
    if args.contact_sheet:
        write_contact_sheet(rows, args.contact_sheet)
    for row in rows:
        print(
            f"{Path(row['file']).name}: {row['status']} "
            f"size={row['size']} span={row['bbox_coverage']}({row['span_verdict']}) "
            f"ink={row['ink_ratio']}({row['ink_verdict']}) "
            f"clearspace={row['clearspace_ink_ratio']}"
        )
    print_distribution(rows, args)
    return 0


def print_distribution(rows: list[dict[str, str]], args: argparse.Namespace) -> None:
    """Print how consistent the batch is. Spread matters more than any one image."""
    if len(rows) < 2:
        return
    spans = sorted(float(row["bbox_coverage"]) for row in rows)
    inks = sorted(float(row["ink_ratio"]) for row in rows)
    total = len(rows)
    print(f"\n-- {total} images --")
    # counts come from the per-image verdicts, which were computed on exact
    # values; the printed spread uses the rounded columns, which is precise enough
    for label, values, low, high, ok_key in (
        ("span", spans, args.span_min, args.span_max, "span_ok"),
        ("ink ", inks, args.ink_min, args.ink_max, "ink_ok"),
    ):
        in_band = sum(1 for row in rows if row[ok_key] == "true")
        print(
            f"{label}: median {statistics.median(values):.3f} "
            f"min {values[0]:.3f} max {values[-1]:.3f} "
            f"sd {statistics.pstdev(values):.3f} | "
            f"in band {low:.2f}-{high:.2f}: {in_band}/{total} "
            f"({100 * in_band / total:.0f}%)"
        )
    both = sum(1 for row in rows if row["span_ok"] == "true" and row["ink_ok"] == "true")
    print(f"both bands: {both}/{total} ({100 * both / total:.0f}%)")


if __name__ == "__main__":
    raise SystemExit(main())
