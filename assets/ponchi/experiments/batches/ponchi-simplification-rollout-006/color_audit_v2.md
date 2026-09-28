# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 6 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/color_audit_v2.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-color-audit-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `E-4` | 1 | 0 | 0 | 0 |
| `F-58` | 1 | 0 | 0 | 0 |
| `F-91` | 1 | 0 | 0 | 0 |
| `G-39` | 1 | 0 | 0 | 0 |
| `G-43` | 1 | 0 | 0 | 0 |
| `J-16` | 1 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `F-58_candidate_v2` |  | `F-58` | 0.008057 | `pass` | `blue:1714;dark:336;neutral:41;purple:4;orange:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-58/F-58_candidate_v2.png` |
| `J-16_candidate_v2` |  | `J-16` | 0.006209 | `pass` | `blue:6262;dark:3479;neutral:24;purple:4;cyan_teal:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/J-16/J-16_candidate_v2.png` |
| `G-43_candidate_v2` |  | `G-43` | 0.003726 | `pass` | `blue:4310;dark:1450;neutral:85;cyan_teal:12;purple:6` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/G-43/G-43_candidate_v2.png` |
| `E-4_candidate_v2` |  | `E-4` | 0.001965 | `pass` | `dark:1959;blue:1098;neutral:31;cyan_teal:3;purple:1` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/E-4/E-4_candidate_v2.png` |
| `G-39_candidate_v2` |  | `G-39` | 0.001734 | `pass` | `blue:1463;dark:1179;neutral:76;cyan_teal:11` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/G-39/G-39_candidate_v2.png` |
| `F-91_candidate_v2` |  | `F-91` | 0.000912 | `pass` | `blue:1435` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-91/F-91_candidate_v2.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
