# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 20 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/audits/ponchi_color_audit.csv`
- Contact sheet: `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/audits/ponchi_color_audit_contact.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `ponchi-simplification-pilot-001` | 9 | 0 | 0 | 0 |
| `v2` | 4 | 0 | 0 | 0 |
| `v2_adjusted` | 2 | 0 | 0 | 0 |
| `v4_flat` | 2 | 0 | 0 | 0 |
| `v4_solid` | 1 | 0 | 0 | 0 |
| `v5_muted` | 1 | 0 | 0 | 0 |
| `v6_simplified` | 1 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `H-1` |  | `v5_muted` | 0.009582 | `pass` | `blue:7534` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v5_muted/H-1_base_1254x627.png` |
| `B-7` |  | `ponchi-simplification-pilot-001` | 0.008610 | `pass` | `blue:6422;dark:308;neutral:31;purple:9` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/B-7_base_1254x627.png` |
| `F-43` |  | `ponchi-simplification-pilot-001` | 0.008097 | `pass` | `blue:6349;neutral:9;dark:8` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/F-43_base_1254x627.png` |
| `G-41` |  | `v2_adjusted` | 0.007599 | `pass` | `blue:5943;dark:24;neutral:8` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v2_adjusted/G-41_base_1254x627.png` |
| `I-2` |  | `v4_flat` | 0.007101 | `pass` | `blue:5583` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v4_flat/I-2_base_1254x627.png` |
| `C-9` |  | `v6_simplified` | 0.006664 | `pass` | `blue:5240` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v6_simplified/C-9_base_1254x627.png` |
| `H-7` |  | `v2` | 0.005702 | `pass` | `blue:4031;dark:441;purple:10;neutral:1` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v2/H-7_base_1254x627.png` |
| `C-6` |  | `ponchi-simplification-pilot-001` | 0.005049 | `pass` | `dark:3040;blue:915;neutral:8;purple:7` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/C-6_base_1254x627.png` |
| `E-1` |  | `v2_adjusted` | 0.004656 | `pass` | `blue:2878;dark:611;cyan_teal:125;neutral:35;purple:8` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v2_adjusted/E-1_base_1254x627.png` |
| `F-2` |  | `ponchi-simplification-pilot-001` | 0.004384 | `pass` | `dark:1768;blue:1544;purple:81;neutral:54` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/F-2_base_1254x627.png` |
| `I-4` |  | `ponchi-simplification-pilot-001` | 0.004070 | `pass` | `blue:3173;dark:20;neutral:7` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/I-4_base_1254x627.png` |
| `D-12` |  | `v4_flat` | 0.002610 | `pass` | `blue:2052` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v4_flat/D-12_base_1254x627.png` |
| `E-50` |  | `ponchi-simplification-pilot-001` | 0.001909 | `pass` | `blue:1374;neutral:66;dark:61` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/E-50_base_1254x627.png` |
| `J-84` |  | `v4_solid` | 0.000917 | `pass` | `blue:716;dark:4;neutral:1` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v4_solid/J-84_base_1254x627.png` |
| `B-4` |  | `ponchi-simplification-pilot-001` | 0.000818 | `pass` | `blue:642;dark:1` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/B-4_base_1254x627.png` |
| `A-3` |  | `ponchi-simplification-pilot-001` | 0.000324 | `pass` | `blue:195;neutral:57;purple:2;dark:1` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/A-3_base_1254x627.png` |
| `G-10` |  | `v2` | 0.000233 | `pass` | `dark:181;blue:2` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v2/G-10_base_1254x627.png` |
| `A-7` |  | `v2` | 0.000163 | `pass` | `dark:116;blue:12` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v2/A-7_base_1254x627.png` |
| `J-14` |  | `v2` | 0.000089 | `pass` | `dark:50;blue:20` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/revisions/v2/J-14_base_1254x627.png` |
| `D-51` |  | `ponchi-simplification-pilot-001` | 0.000059 | `pass` | `blue:46` | `assets/ponchi/experiments/batches/ponchi-simplification-pilot-001/D-51_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
