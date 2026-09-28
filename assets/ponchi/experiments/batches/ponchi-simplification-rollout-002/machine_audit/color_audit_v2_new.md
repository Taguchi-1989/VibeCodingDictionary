# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 1 |
| `review` | 2 |
| `fail` | 2 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_v2_new.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_contact_v2_new.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `E-31` | 0 | 1 | 0 | 0 |
| `G-14` | 0 | 1 | 0 | 0 |
| `G-16` | 1 | 0 | 0 | 0 |
| `I-5` | 0 | 0 | 1 | 0 |
| `J-71` | 0 | 0 | 1 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-5_candidate_v2` |  | `I-5` | 0.052545 | `fail` | `blue:20584;dark:64;neutral:23` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/I-5/I-5_candidate_v2.png` |
| `J-71_candidate_v2` |  | `J-71` | 0.045206 | `fail` | `blue:21611;dark:2095;neutral:5` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/J-71/J-71_candidate_v2.png` |
| `G-14_candidate_v2` |  | `G-14` | 0.010922 | `review` | `blue:17186` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/G-14/G-14_candidate_v2.png` |
| `E-31_candidate_v2` |  | `E-31` | 0.010463 | `review` | `blue:15918;dark:490;purple:32;neutral:24` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/E-31/E-31_candidate_v2.png` |
| `G-16_candidate_v2` |  | `G-16` | 0.000859 | `pass` | `blue:1349;purple:2` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/G-16/G-16_candidate_v2.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
