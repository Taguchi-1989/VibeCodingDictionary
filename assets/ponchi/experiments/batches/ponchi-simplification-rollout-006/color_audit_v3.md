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

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/color_audit_v3.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/color_audit_contact_sheet_v3.png`

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
| `J-16_candidate_v3` |  | `J-16` | 0.007054 | `pass` | `blue:6869;dark:4184;neutral:33;purple:9;cyan_teal:4` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/J-16/J-16_candidate_v3.png` |
| `G-43_candidate_v3` |  | `G-43` | 0.006772 | `pass` | `blue:8944;dark:1593;neutral:115;purple:4` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/G-43/G-43_candidate_v3.png` |
| `G-39_candidate_v3` |  | `G-39` | 0.002789 | `pass` | `dark:3788;blue:407;neutral:143;cyan_teal:49;purple:2` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/G-39/G-39_candidate_v3.png` |
| `F-91_candidate_v3` |  | `F-91` | 0.002614 | `pass` | `blue:3907;dark:181;neutral:16;purple:9` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-91/F-91_candidate_v3.png` |
| `E-4_candidate_v3` |  | `E-4` | 0.002058 | `pass` | `dark:1931;blue:1279;neutral:25;purple:3` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/E-4/E-4_candidate_v3.png` |
| `F-58_candidate_v3` |  | `F-58` | 0.001195 | `pass` | `blue:1213;dark:649;neutral:17;purple:2` | `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-58/F-58_candidate_v3.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
