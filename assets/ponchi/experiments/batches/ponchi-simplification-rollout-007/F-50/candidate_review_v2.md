# F-50 candidate v2 review record

- Candidate: `F-50_candidate_v2.png`
- SHA-256: `3f234bfa649dce43406398028f697951bedf9ea8f6bda2749bf4facae63bb72e`
- Dimensions/mode: 1774×887 RGB
- Independent semantic/style review: pending.
- Provisional status: **HOLD** at exact-white fail-fast perimeter gate.

## Machine audits

- Geometry audit: PASS; bbox coverage 0.570; logo clearspace ink ratio 0.0000.
- Palette audit: PASS (see `color_audit_v2.csv`); it does not establish exact white.
- Exact-white perimeter: FAIL; three/four corners and seven/eight registered points differ from exact RGB #FFFFFF.
- Exact-white pixels: 278,934 / 1,573,538 (17.727%); no mask prepared because fail-fast points do not pass.

Coordinates use `round(normalized_coordinate × dimension)`, clamped to the last pixel.

| Point | x | y | RGB | Exact white |
| :-- | --: | --: | :-- | :-- |
| top_left_corner | 0 | 0 | (255,255,255) | yes |
| top_right_corner | 1773 | 0 | (254,255,254) | no |
| bottom_left_corner | 0 | 886 | (254,253,254) | no |
| bottom_right_corner | 1773 | 886 | (254,253,254) | no |
| registered_1 | 35 | 18 | (253,253,253) | no |
| registered_2 | 355 | 18 | (255,255,255) | yes |
| registered_3 | 1419 | 18 | (254,254,254) | no |
| registered_4 | 1739 | 18 | (254,254,254) | no |
| registered_5 | 35 | 869 | (254,254,254) | no |
| registered_6 | 355 | 869 | (254,254,254) | no |
| registered_7 | 1419 | 869 | (253,253,253) | no |
| registered_8 | 1739 | 869 | (254,254,254) | no |

## Reserved mark rectangle

- Sidecar rectangle `[836,16,370,179]` scaled to `1183,23–1706,276` pixels. Foreground proxy (`min(R,G,B) < 245`) count: 0; no foreground detected in the rectangle.

## Next action

Obtain independent semantic/style review of the v2 return cue and 200px readability. If no new blocker exists, target only exact-white output in the final allowed prompt revision; do not postprocess the candidate.
