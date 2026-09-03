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

- CSV: `docs/ponchi_batch_audits/ponchi-batch-019-color-audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-019-color-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `ponchi-batch-019` | 40 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `C-15` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/C-15_base_1254x627.png` |
| `F-210` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/F-210_base_1254x627.png` |
| `F-211` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/F-211_base_1254x627.png` |
| `F-212` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/F-212_base_1254x627.png` |
| `G-48` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/G-48_base_1254x627.png` |
| `J-101` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-101_base_1254x627.png` |
| `J-102` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-102_base_1254x627.png` |
| `J-103` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-103_base_1254x627.png` |
| `J-104` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-104_base_1254x627.png` |
| `J-105` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-105_base_1254x627.png` |
| `J-106` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-106_base_1254x627.png` |
| `J-107` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-107_base_1254x627.png` |
| `J-108` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-108_base_1254x627.png` |
| `J-109` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-109_base_1254x627.png` |
| `J-110` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-110_base_1254x627.png` |
| `J-111` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-111_base_1254x627.png` |
| `J-112` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-112_base_1254x627.png` |
| `J-113` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-113_base_1254x627.png` |
| `J-114` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-114_base_1254x627.png` |
| `J-24` |  | `ponchi-batch-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-019/J-24_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
