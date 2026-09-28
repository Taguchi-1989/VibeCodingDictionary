# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 0 |
| `review` | 1 |
| `fail` | 1 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_v2_candidates.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/machine_audit/color_audit_v2_candidates_contact.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `ponchi-simplification-rollout-002` | 0 | 1 | 1 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-3_candidate_v2` |  | `ponchi-simplification-rollout-002` | 0.024486 | `fail` | `blue:31272;dark:6926;neutral:265;cyan_teal:57;purple:9` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/I-3_candidate_v2.png` |
| `E-30_candidate_v2` |  | `ponchi-simplification-rollout-002` | 0.016020 | `review` | `blue:24808;dark:368;neutral:29;purple:3` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-002/E-30_candidate_v2.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
