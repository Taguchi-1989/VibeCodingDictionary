# F-50 candidate v1 review

- Candidate: `F-50_candidate_v1.png`
- SHA-256: `fcf7cd915c14de7ee93a4220b76ef5cbcb813e1268d6cc983974de0c3041b080`
- Dimensions/mode: 1774×887 RGB
- Source and Character B reference hashes: verified against sidecar and files on 2026-09-28.
- Independent semantic/style reviewer: `/root/review_wave001_b`, 2026-09-28.
- Independent review: the folder scatter → one history/diff, one branch, and two depictions of Character B read clearly at 200px; the reserved upper-right clearspace is blank. No readable labels, commands, Git mark, or extra robot. The restore-to-earlier-state requirement is not explicit beyond the timeline.
- Overall HOLD: strict-white perimeter fails, and the return cue needs one simple explicit depiction.
- Overall: **HOLD** at the strict-white gate.

## Machine audit results

- Image geometry audit: PASS; 1774×887, bbox coverage 0.541, logo clearspace ink 0.0000.
- Palette audit: PASS; off-palette ratio 0.003238. This does not verify exact-white background.
- Exact-white perimeter audit: FAIL; four corners fail and seven of eight registered points fail.
- Exact #FFFFFF pixels: 269,138 / 1,573,538 (17.104%); no full-canvas background mask was created because the perimeter gate already failed.

Coordinates use `round(normalized_coordinate × dimension)`, clamped to the last pixel.

| Point | x | y | RGB | Exact white |
| :-- | --: | --: | :-- | :-- |
| top_left_corner | 0 | 0 | (253,255,255) | no |
| top_right_corner | 1773 | 0 | (254,255,254) | no |
| bottom_left_corner | 0 | 886 | (253,253,253) | no |
| bottom_right_corner | 1773 | 886 | (254,253,254) | no |
| registered_1 | 35 | 18 | (253,253,253) | no |
| registered_2 | 355 | 18 | (255,255,255) | yes |
| registered_3 | 1419 | 18 | (254,254,254) | no |
| registered_4 | 1739 | 18 | (254,254,254) | no |
| registered_5 | 35 | 869 | (254,255,254) | no |
| registered_6 | 355 | 869 | (254,253,254) | no |
| registered_7 | 1419 | 869 | (253,253,253) | no |
| registered_8 | 1739 | 869 | (254,254,254) | no |

## Next action

Keep v1 unchanged in experiments. A focused v2 prompt revision is underway to require exact white and one clear return-to-earlier-state cue. Obtain independent prompt review before generating v2. Do not white-paint or otherwise postprocess the image.
