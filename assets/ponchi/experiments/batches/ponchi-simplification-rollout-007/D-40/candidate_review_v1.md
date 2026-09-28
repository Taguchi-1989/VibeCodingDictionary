# D-40 candidate v1 review

- Candidate: `D-40_candidate_v1.png`
- SHA-256: `89bc3d73de9314e265d4414a92404148a92cfb2737748296b2e1351eec2f5f57`
- Dimensions/mode: 1774×887 RGB (opaque)
- Independent reviewer: `/root/review_wave001_b`, 2026-09-28
- Overall: **HOLD**

## Semantic and composition review

The four timeline motifs remain distinguishable at 200px and match the sidecar. The single pointing observer matches the source role and appearance. No readable text, logo, or unsupported model sub-cards were found.

## Strict-white audit

All four corners and all eight registered perimeter samples fail exact RGB `#FFFFFF`. The existing palette color audit (`color_audit_v1.csv`) reports PASS with off-palette ratio 0.002921; this is not evidence of exact-white compliance. The entire canvas is predominantly near-white. Coordinates use `round(normalized_coordinate × dimension)`, clamped to the last pixel.

| Point | x | y | RGB | Result |
| :-- | --: | --: | :-- | :-- |
| top-left corner | 0 | 0 | (253,255,255) | HOLD |
| top-right corner | 1773 | 0 | (254,255,254) | HOLD |
| bottom-left corner | 0 | 886 | (254,253,253) | HOLD |
| bottom-right corner | 1773 | 886 | (254,253,254) | HOLD |
| registered 1 (0.02,0.02) | 35 | 18 | (253,253,253) | HOLD |
| registered 2 (0.20,0.02) | 355 | 18 | (255,254,255) | HOLD |
| registered 3 (0.80,0.02) | 1419 | 18 | (254,254,254) | HOLD |
| registered 4 (0.98,0.02) | 1739 | 18 | (254,254,254) | HOLD |
| registered 5 (0.02,0.98) | 35 | 869 | (254,254,254) | HOLD |
| registered 6 (0.20,0.98) | 355 | 869 | (254,254,254) | HOLD |
| registered 7 (0.80,0.98) | 1419 | 869 | (253,253,253) | HOLD |
| registered 8 (0.98,0.98) | 1739 | 869 | (254,254,254) | HOLD |

## Targeted style finding

Pale-blue circular icon backplates are local foreground, not canvas background. They are unrequested decorative emphasis. Remove or simplify them in one focused prompt revision. Do not paint or recolor the generated image after generation.

## Next action

Revise the D-40 prompt once to explicitly require a flat opaque exact-`#FFFFFF` canvas and remove circular backplates/halos; independently review that prompt before generating candidate v2. Candidate v1 remains preserved and unadopted in experiments.
