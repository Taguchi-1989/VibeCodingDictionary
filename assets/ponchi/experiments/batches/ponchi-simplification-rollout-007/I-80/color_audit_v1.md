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

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/I-80/color_audit_v1.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/I-80/color_audit_contact_sheet_v1.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `I-80` | 0 | 1 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-80_candidate_v1` |  | `I-80` | 0.010950 | `review` | `dark:11053;blue:5821;neutral:331;purple:23;cyan_teal:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/I-80/I-80_candidate_v1.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
