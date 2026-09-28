# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 3 |
| `review` | 1 |
| `fail` | 1 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_contact.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `E-25` | 1 | 0 | 0 | 0 |
| `ponchi-simplification-rollout-002` | 2 | 1 | 1 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-3_candidate_v2` |  | `ponchi-simplification-rollout-002` | 0.024486 | `fail` | `blue:31272;dark:6926;neutral:265;cyan_teal:57;purple:9` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/I-3_candidate_v2.png` |
| `E-30_candidate_v2` |  | `ponchi-simplification-rollout-002` | 0.016020 | `review` | `blue:24808;dark:368;neutral:29;purple:3` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/E-30_candidate_v2.png` |
| `G-44` |  | `ponchi-simplification-rollout-002` | 0.006677 | `pass` | `dark:9489;blue:893;neutral:105;cyan_teal:13;purple:7` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/G-44_candidate.png` |
| `H-6` |  | `ponchi-simplification-rollout-002` | 0.005372 | `pass` | `blue:5381;dark:2739;neutral:295;purple:36;orange:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/H-6_candidate.png` |
| `E-25_candidate_v2` |  | `E-25` | 0.003122 | `pass` | `blue:3459;dark:1273;neutral:111;purple:67;orange:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/E-25/E-25_candidate_v2.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
