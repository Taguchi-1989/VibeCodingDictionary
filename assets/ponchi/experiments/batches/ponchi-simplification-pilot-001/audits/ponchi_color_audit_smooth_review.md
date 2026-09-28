# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 1 |
| `review` | 1 |
| `fail` | 3 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/audits/ponchi_color_audit_smooth_review.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/audits/ponchi_color_audit_smooth_review_contact.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `v3_smooth` | 1 | 1 | 3 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `D-12` |  | `v3_smooth` | 0.051695 | `fail` | `blue:20287;dark:34;neutral:2` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v3_smooth/D-12_base_1254x627.png` |
| `C-9` |  | `v3_smooth` | 0.028488 | `fail` | `blue:22399` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v3_smooth/C-9_base_1254x627.png` |
| `I-2` |  | `v3_smooth` | 0.021536 | `fail` | `blue:16933` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v3_smooth/I-2_base_1254x627.png` |
| `H-1` |  | `v3_smooth` | 0.019861 | `review` | `blue:15602;neutral:14` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v3_smooth/H-1_base_1254x627.png` |
| `J-84` |  | `v3_smooth` | 0.000003 | `pass` | `neutral:1;cyan_teal:1` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v3_smooth/J-84_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
