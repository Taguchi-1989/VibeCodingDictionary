# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 0 |
| `review` | 1 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/manual-2026-09-05/F-214_color_audit.csv`
- Contact sheet: `assets/ponchi/experiments/manual-2026-09-05/F-214_color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `manual-2026-09-05` | 0 | 1 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `F-214_api-key_v1_1254x627` |  | `manual-2026-09-05` | 0.016425 | `review` | `blue:11507;dark:1312;purple:58;neutral:36;orange:1` | `assets/ponchi/experiments/manual-2026-09-05/F-214_api-key_v1_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
