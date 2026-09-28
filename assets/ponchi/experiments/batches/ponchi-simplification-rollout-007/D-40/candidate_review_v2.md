# D-40 candidate v2 review record

- Candidate: `D-40_candidate_v2.png`
- SHA-256: `76802068ddb23ebf590e8c14fd8c13657f7611d45c03c4786e7e446f8d7e0947`
- Dimensions/mode: 1774×887 RGB
- Independent prompt review for v2: PASS by `/root/review_wave001_b`, 2026-09-28.
- Independent candidate reviewer: `/root/review_wave001_b`, 2026-09-28.
- Semantic/layout at 200px: PASS; four nodes and motifs are legible, the source observer broadly matches identity/role, with no readable text or unsupported labels. No pale circular backplates.
- Overall: HOLD. The strict-white gate fails at four corners and seven/eight registered points. The Llama 4 paper/image motif enters the reserved rectangle at x1466–1561, y237–273 (1,286 chromatic pixels by reviewer measurement). The bars also contain intermediate blue shades beyond the exact listed palette.
- Provisional status: **HOLD** at strict-white gate; logo-reservation overlap needs independent confirmation.

## Machine audits

- Geometry audit: PASS, bbox coverage 0.648.
- Palette audit: PASS.
- Exact-white perimeter samples: FAIL; all four corners and seven of eight registered points are not exact RGB (255,255,255).
- Exact-white pixels: 339,058 / 1,573,538 (21.547%); no full background mask was prepared because the fail-fast samples did not pass.

Coordinates use `round(normalized_coordinate × dimension)`, clamped to the last pixel.

| Point | x | y | RGB | Exact white |
| :-- | --: | --: | :-- | :-- |
| top_left_corner | 0 | 0 | (253,255,255) | no |
| top_right_corner | 1773 | 0 | (254,255,254) | no |
| bottom_left_corner | 0 | 886 | (254,254,254) | no |
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

- Source review rectangle: `[1036,22,172,172]` on 1254×627; scaled ROI sampled as `1466,31–1709,274` on this 1774×887 candidate.
- A foreground proxy (`min(R,G,B) < 245`, to ignore the candidate's near-white canvas) finds 1,302 dark/colored pixels in the ROI (2.205% of ROI). The upper-right multimodal motif appears to overlap the reserved rectangle; independent reviewer confirmation is pending.

- General image audit at the same normalized start/end reports clearspace ink ratio 0.0143 and PASS at its 0.015 tolerance. That broad-threshold geometry result is not proof that the sidecar's specific rectangle is completely blank.

## Next action

Keep v2 internal and unchanged. Review confirmed a reserved-rectangle collision and off-palette intermediate blues in addition to the strict-white failure. Prepare a focused second and final candidate revision that moves the Llama 4 motif below/left of the reserved rectangle, uses flat approved fills, and reiterates exact-white controls. No background painting or other post-generation modification.
