#!/usr/bin/env python3
"""Strictly audit white backgrounds using a reviewer-verified binary mask.

An independent reviewer must verify that the mask does not hide broad blank
regions: every true background pixel must be marked 255, while illustration
and antialiased edge pixels must be marked 0. This tool only audits files; it
never edits the image or mask.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("This script requires Pillow. Use the bundled Codex Python runtime.") from exc


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def corner_points(width: int, height: int) -> tuple[tuple[str, int, int], ...]:
    return (
        ("top_left", 0, 0),
        ("top_right", width - 1, 0),
        ("bottom_left", 0, height - 1),
        ("bottom_right", width - 1, height - 1),
    )


def pixel_text(pixel: object) -> str:
    if isinstance(pixel, tuple):
        return "(" + ",".join(str(channel) for channel in pixel) + ")"
    return str(pixel)


def audit(image_path: Path, mask_path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    details: list[str] = []

    for label, path in (("image", image_path), ("mask", mask_path)):
        if not path.is_file():
            errors.append(f"{label} file not found: {path}")
        else:
            try:
                details.append(f"{label}_sha256={sha256_file(path)}")
            except OSError as exc:
                errors.append(f"cannot hash {label}: {exc}")

    if errors:
        return details, errors

    try:
        with Image.open(image_path) as opened_image:
            image = opened_image.copy()
        with Image.open(mask_path) as opened_mask:
            mask = opened_mask.copy()
    except Exception as exc:
        return details, [f"cannot open image or mask: {exc}"]

    details.extend(
        [
            f"image_size={image.width}x{image.height}",
            f"image_mode={image.mode}",
            f"mask_size={mask.width}x{mask.height}",
            f"mask_mode={mask.mode}",
        ]
    )

    if image.size != mask.size:
        errors.append("image and mask dimensions differ")

    if image.mode not in {"RGB", "RGBA"}:
        errors.append(f"image mode must be RGB or RGBA, got {image.mode}")

    if mask.mode not in {"1", "L"}:
        errors.append(f"mask mode must be 1-bit or grayscale L, got {mask.mode}")

    background_count = 0
    foreground_count = 0
    binary_mask = mask.mode in {"1", "L"}
    if binary_mask:
        for value in mask.getdata():
            if value == 255:
                background_count += 1
            elif value == 0:
                foreground_count += 1
            else:
                binary_mask = False

    details.append(f"mask_binary={'true' if binary_mask else 'false'}")
    if not binary_mask:
        errors.append("mask must contain only binary values 0 and 255")
        return details, errors

    details.extend(
        [
            f"background_pixels={background_count}",
            f"foreground_pixels={foreground_count}",
        ]
    )
    if background_count == 0:
        errors.append("mask has no background pixels marked 255")
    if foreground_count == 0:
        errors.append("mask has no foreground pixels marked 0")

    if image.mode not in {"RGB", "RGBA"}:
        return details, errors

    transparency_key = "transparency" in image.info
    details.append(f"transparency_metadata={'present' if transparency_key else 'absent'}")
    if transparency_key:
        errors.append("image contains transparency metadata (such as an RGB transparency color key)")

    if image.mode == "RGBA":
        nonopaque_count = sum(pixel[3] != 255 for pixel in image.getdata())
        details.append(f"nonopaque_pixels={nonopaque_count}")
        if nonopaque_count:
            errors.append(f"image contains {nonopaque_count} pixels with alpha other than 255")
    else:
        details.append("nonopaque_pixels=0 (RGB image is implicitly opaque)")

    if image.size == mask.size:
        background_nonwhite = 0
        mask_values = mask.getdata()
        image_pixels = image.getdata()
        for mask_value, pixel in zip(mask_values, image_pixels):
            if mask_value == 255 and pixel[:3] != (255, 255, 255):
                background_nonwhite += 1
        details.append(f"nonwhite_background_pixels={background_nonwhite}")
        if background_nonwhite:
            errors.append(f"{background_nonwhite} mask-background pixels are not exact RGB white")

        corner_summary: list[str] = []
        for name, x, y in corner_points(image.width, image.height):
            marked_value = mask.getpixel((x, y))
            marked_background = marked_value == 255
            pixel = image.getpixel((x, y))
            exact_white = pixel[:3] == (255, 255, 255)
            opaque = image.mode == "RGB" or pixel[3] == 255
            corner_summary.append(
                f"{name}:mask={marked_value},pixel={pixel_text(pixel)},"
                f"background={'true' if marked_background else 'false'},"
                f"white={'true' if exact_white else 'false'},opaque={'true' if opaque else 'false'}"
            )
            if not marked_background:
                errors.append(f"corner {name} is not marked as background")
            if not exact_white:
                errors.append(f"corner {name} is not exact RGB white")
            if not opaque:
                errors.append(f"corner {name} is not fully opaque")
        details.append("corners=" + "; ".join(corner_summary))

    return details, errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Strictly check exact-white pixels selected by a reviewer-verified background mask.",
        epilog=(
            "An independent reviewer must verify that the mask does not hide broad blank regions. "
            "Mask 255 means background; mask 0 means illustration or antialiased edge. "
            "This tool reports findings and never edits the image."
        ),
    )
    parser.add_argument("--image", required=True, type=Path, help="RGB or fully opaque RGBA candidate image")
    parser.add_argument("--mask", required=True, type=Path, help="same-size 1-bit or binary grayscale mask")
    args = parser.parse_args()

    details, errors = audit(args.image, args.mask)
    print(f"image={args.image}")
    print(f"mask={args.mask}")
    for detail in details:
        print(detail)
    for error in errors:
        print(f"error={error}")
    print(f"status={'fail' if errors else 'pass'}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
