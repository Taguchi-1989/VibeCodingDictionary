# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 40 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `docs/ponchi_batch_audits/ponchi-batch-019-final-color-audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-019-final-color-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `final` | 40 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `C-15` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/C-15.png` |
| `F-210` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/F-210.png` |
| `F-211` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/F-211.png` |
| `F-212` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/F-212.png` |
| `G-48` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/G-48.png` |
| `J-24` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-24.png` |
| `J-25` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-25.png` |
| `J-26` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-26.png` |
| `J-27` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-27.png` |
| `J-28` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-28.png` |
| `J-29` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-29.png` |
| `J-30` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-30.png` |
| `J-82` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-82.png` |
| `J-83` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-83.png` |
| `J-84` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-84.png` |
| `J-85` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-85.png` |
| `J-86` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-86.png` |
| `J-87` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-87.png` |
| `J-88` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-88.png` |
| `J-89` |  | `final` | 0.000000 | `pass` | `` | `assets/ponchi/final/J-89.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
