# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 0 |
| `review` | 1 |
| `fail` | 3 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_v3.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_contact_v3.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `E-31` | 0 | 0 | 1 | 0 |
| `G-14` | 0 | 1 | 0 | 0 |
| `I-5` | 0 | 0 | 1 | 0 |
| `J-71` | 0 | 0 | 1 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-71_candidate_v3` |  | `J-71` | 0.063911 | `fail` | `blue:18563;dark:1530;purple:15;neutral:6` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/J-71/J-71_candidate_v3.png` |
| `E-31_candidate_v3` |  | `E-31` | 0.061910 | `fail` | `blue:20890;dark:257;neutral:95;purple:57;cyan_teal:8` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/E-31/E-31_candidate_v3.png` |
| `I-5_candidate_v3` |  | `I-5` | 0.059222 | `fail` | `blue:23227;dark:53;neutral:17` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/I-5/I-5_candidate_v3.png` |
| `G-14_candidate_v3` |  | `G-14` | 0.011872 | `review` | `blue:18680;neutral:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/G-14/G-14_candidate_v3.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
