# F-50 candidate v3 review record

- Candidate: `F-50_candidate_v3.png`
- SHA-256: `2483C33A93B52C135E6E51CF711644782BD2E47DB05A63166A031FE6961FF822`
- Dimensions/mode: 1774×887 RGB
- Independent reviewer: `/root/review_wave001_b`, 2026-09-28.
- Overall: **HOLD; final candidate revision 2/2. No further generation.**

## Independent semantic/style review

At 200px, scattered backups plus a confused Character B read as Before; the ordered history, diff, and calm matching Character B read as After. The single return arrow and one rejoining branch are visible. No extra figures, robot, Git/GitHub logo, or words. Two literal `?` glyphs appear by Before; they communicate confusion but may conflict with the prompt's no-text rule.

The sidecar clearspace `[836,16,370,179]` maps to candidate ROI `(1183,23)-(1706,276)`. Independent review confirms the return arrow enters the ROI, with foreground proxy bbox `(1263,240)-(1466,275)` and 1,242 pixels.

## Machine audits

- Geometry: PASS, 1774×887, bbox coverage 0.674.
- Tolerance color audit: PASS.
- Exact-white: FAIL at all four corners and seven of eight registered points; only `(0.20,0.02)` is exact white. Exact-white count 246,830 / 1,573,538 (15.6863%). No background mask retained because fail-fast samples failed.
- Exact mapped logo ROI proxy: 1,242 foreground pixels / 132,319 (0.9386%).

| Point | x | y | RGB | Exact white |
| :-- | --: | --: | :-- | :-- |
| top_left_corner | 0 | 0 | (253,255,255) | no |
| top_right_corner | 1773 | 0 | (254,255,254) | no |
| bottom_left_corner | 0 | 886 | (253,253,253) | no |
| bottom_right_corner | 1773 | 886 | (254,253,254) | no |
| p1 | 35 | 18 | (253,253,253) | no |
| p2 | 355 | 18 | (255,255,255) | yes |
| p3 | 1419 | 18 | (254,254,254) | no |
| p4 | 1739 | 18 | (254,254,254) | no |
| p5 | 35 | 869 | (254,254,254) | no |
| p6 | 355 | 869 | (254,254,254) | no |
| p7 | 1419 | 869 | (253,253,253) | no |
| p8 | 1739 | 869 | (254,254,254) | no |

Keep the candidate unchanged in experiments; final revision limit is reached. No production use or post-processing.
