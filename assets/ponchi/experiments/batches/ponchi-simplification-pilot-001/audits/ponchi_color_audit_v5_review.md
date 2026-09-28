# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 1 |
| `review` | 0 |
| `fail` | 1 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/audits/ponchi_color_audit_v5_review.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/audits/ponchi_color_audit_v5_review_contact.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `v5_muted` | 1 | 0 | 1 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `C-9` |  | `v5_muted` | 0.023420 | `fail` | `blue:18414` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v5_muted/C-9_base_1254x627.png` |
| `H-1` |  | `v5_muted` | 0.009582 | `pass` | `blue:7534` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v5_muted/H-1_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
