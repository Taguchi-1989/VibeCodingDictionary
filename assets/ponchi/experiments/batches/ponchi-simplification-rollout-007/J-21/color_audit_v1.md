# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 1 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/J-21/color_audit_v1.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/J-21/color_audit_contact_sheet_v1.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `J-21` | 1 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-21_candidate_v1` |  | `J-21` | 0.002738 | `pass` | `dark:2566;blue:1711;neutral:27;purple:4` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/J-21/J-21_candidate_v1.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
