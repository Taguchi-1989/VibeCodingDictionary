# F-34 candidate v1 review record

- Candidate: `F-34_candidate_v1.png`
- SHA-256: `abcf6b2839865d969932d0863b1fe5a6fbaa6e708491948a804bf157c97bcf79`
- Dimensions/mode: 1774×887 RGB
- Independent reviewer: `/root/review_wave001_b`, 2026-09-28.
- At 200px, the three generic alternatives, chooser-to-editor direction, one Character B and series palette/line style are recognizable; no logo/readable words. Reserved logo clearspace contains no foreground ink.
- HOLD: required magnifier/publisher-check cue is absent; selected tile is not visibly carried into the editor by a capability/puzzle piece; editor has pseudo-text-like marks. Geometry remains `review` at bbox 0.462 (<0.50). Exact-white gate still fails.
- Provisional status: **HOLD** at exact-white fail-fast checks; geometry also needs review.

## Machine audits

- Geometry audit: `review`, bbox coverage 0.462 (configured threshold 0.50); upper-right clearspace ink ratio 0.0000.
- Palette audit: PASS (see `color_audit_v1.csv`).
- Exact-white perimeter: FAIL; four corners fail and five/eight registered points fail exact RGB #FFFFFF.
- Exact-white pixels: 206,777 / 1,573,538 (13.141%); no background mask prepared because fail-fast samples fail.

Coordinates use `round(normalized_coordinate × dimension)`, clamped to the last pixel.

| Point | x | y | RGB | Exact white |
| :-- | --: | --: | :-- | :-- |
| top_left_corner | 0 | 0 | (253,255,255) | no |
| top_right_corner | 1773 | 0 | (255,254,254) | no |
| bottom_left_corner | 0 | 886 | (253,253,253) | no |
| bottom_right_corner | 1773 | 886 | (254,253,254) | no |
| registered_1 | 71 | 35 | (253,253,253) | no |
| registered_2 | 532 | 35 | (255,254,255) | no |
| registered_3 | 1242 | 35 | (254,254,254) | no |
| registered_4 | 1703 | 35 | (254,254,254) | no |
| registered_5 | 71 | 852 | (255,255,255) | yes |
| registered_6 | 532 | 852 | (254,253,253) | no |
| registered_7 | 1242 | 852 | (255,255,255) | yes |
| registered_8 | 1703 | 852 | (255,255,255) | yes |

## Next action

Keep v1 internal. Author a focused v2 prompt for the missing inspection and selected-capability transfer, removing pseudo-text and increasing the main illustration scale while preserving clearspace; include strict-white constraints. Obtain independent prompt review before candidate_v2. No post-generation white painting.
