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

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/F-54/ponchi-color-audit-v1.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/F-54/ponchi-color-audit-contact-v1.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `F-54` | 1 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `F-54_candidate_v1` |  | `F-54` | 0.002445 | `pass` | `dark:3426;blue:419;neutral:3` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/F-54/F-54_candidate_v1.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
