# F-34 candidate v3 machine review record

- Candidate: `F-34_candidate_v3.png`
- SHA-256: `1D6D434176D94A1D69C16C311DEE3CC86BA9576F8729B06576679D7255C567A7`
- Dimensions/mode: 1774×887 RGB
- Independent candidate reviewer: `/root/review_wave001_b` completed; see independent visual review below.
- Overall: **HOLD at strict-white and mapped-clearspace machine gates; final revision 2/2.**

## Machine audits

- Geometry: PASS, bbox coverage 0.655.
- Tolerance color audit: REVIEW.
- Exact-white: FAIL at all four corners and 4/8 registered points. Exact-white count 271,453 / 1,573,538 (17.2511%). No background mask retained because fail-fast samples failed.
- Sidecar reserved rectangle `[986,0,220,240]` on 1254×627 maps to `(1395,0)-(1706,340)` on this candidate. Foreground proxy (`min(R,G,B)<245`) finds 1,648 pixels in the mapped ROI.

| Point | x | y | RGB | Exact white |
| :-- | --: | --: | :-- | :-- |
| top_left_corner | 0 | 0 | (254,253,254) | no |
| top_right_corner | 1773 | 0 | (254,255,254) | no |
| bottom_left_corner | 0 | 886 | (253,253,253) | no |
| bottom_right_corner | 1773 | 886 | (254,253,254) | no |
| p1 | 71 | 35 | (253,253,253) | no |
| p2 | 532 | 35 | (255,255,255) | yes |
| p3 | 1242 | 35 | (254,254,254) | no |
| p4 | 1703 | 35 | (254,254,254) | no |
| p5 | 71 | 852 | (255,255,255) | yes |
| p6 | 532 | 852 | (254,253,254) | no |
| p7 | 1242 | 852 | (255,255,255) | yes |
| p8 | 1703 | 852 | (255,255,255) | yes |

Independent reviewer must assess the final candidate's meaning, character, pseudo-text and exact mapped ROI. No further candidate generation or postprocessing is permitted after revision 2/2.

## Independent visual review

- Independent reviewer: `/root/review_wave001_b`; reviewed full canvas and an in-memory 200×100 preview (no temporary image file saved).
- Semantic/layout findings: the exactly three generic chooser tiles remain distinct. One Character B is shown inspecting the selected puzzle-piece tile, with a magnifier cue; one transfer arrow carries the puzzle capability into the editor. The small avatar/profile glyph appears removed. No second person, robot, readable brand, or product logo was observed.
- HOLD — The editor is not blank: repeated blue and pale-blue horizontal rows remain inside its canvas and read as pseudo-text/content rows. This contradicts the prompt's explicit no-rows/no-faux-code/no-pseudo-text requirement.
- HOLD — The top horizontal editor frame intrudes into the mapped reserved ROI along its bottom edge (observed around y=328–335); machine foreground proxy reports 1,648 pixels, bounding region x=1395–1705, y=328–335. The ROI is therefore not empty.
- Exact-white remains failed as recorded above (4/4 corners, 4/8 points); no mask or white-paint postprocessing should be applied. Geometry bbox 0.655 passes; tolerance palette remains REVIEW.
- Final verdict: **HOLD**. Revision 2/2 is final; do not promote or generate another candidate.
