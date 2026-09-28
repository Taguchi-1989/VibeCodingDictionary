# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 4 |
| `review` | 0 |
| `fail` | 1 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_v1.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_contact_v1.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `E-31` | 1 | 0 | 0 | 0 |
| `G-14` | 1 | 0 | 0 | 0 |
| `G-16` | 1 | 0 | 0 | 0 |
| `I-5` | 1 | 0 | 0 | 0 |
| `J-71` | 0 | 0 | 1 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-71_candidate_v1` |  | `J-71` | 0.023255 | `fail` | `blue:17676;dark:3899;neutral:456;purple:71;green:5` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/J-71/J-71_candidate_v1.png` |
| `I-5_candidate_v1` |  | `I-5` | 0.009884 | `pass` | `blue:3189;neutral:161;dark:158;purple:29;cyan_teal:16` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/I-5/I-5_candidate_v1.png` |
| `E-31_candidate_v1` |  | `E-31` | 0.009050 | `pass` | `blue:14014;dark:180;neutral:39;purple:6;cyan_teal:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/E-31/E-31_candidate_v1.png` |
| `G-14_candidate_v1` |  | `G-14` | 0.005470 | `pass` | `blue:8608` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/G-14/G-14_candidate_v1.png` |
| `G-16_candidate_v1` |  | `G-16` | 0.001589 | `pass` | `blue:2497;neutral:3;purple:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/G-16/G-16_candidate_v1.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
