# F-54 candidate v1 review record

- Candidate: `F-54_candidate_v1.png`
- SHA-256: `C4781A4A71A9AF22DD31F02AE90C6E4AC8B945D20F9ECDB9258712B8C988B84B`
- Dimensions/mode: 1774×887 RGB
- Source SHA-256: `6ca239ee02c95aa820d9ddf0b5f81c498d3e76a758c02aefc480befe64e17b8a`
- Character B reference SHA-256: `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99`
- Independent reviewer: `/root/review_wave001_b`, 2026-09-28.
- Overall: **HOLD at exact-white background gate.**

## Independent semantic and visual review

At 200px, three distinct checkpoints on a left-to-right timeline, the highlighted middle node, and one return arrow from the right checkpoint to the earlier point read clearly. One calm Character B developer stands at right. The durable local-history checkpoint and return meaning are clear without suggesting remote/push/merge. Character B matches the approved reference. No extra figures, readable text, Git/GitHub mark, or logo-like mark found. The sidecar says `LOGO_MODE: not_required`; clearspace is not a required gate.

## Machine audits

- Geometry: PASS, native 1774×887, bbox coverage 0.570.
- Color tolerance audit: PASS. This is a tolerance audit, not a proof of exact pixel colors.
- Exact-white: FAIL at all four corners and seven of eight registered points; only `(.04,.96)` is exact white. Exact-white pixels: 252,276 / 1,573,538 (16.0324%). No background mask retained because fail-fast samples failed.
- Geometry audit sidecar context records `clearspace_required=false`; the measured 0.0173 ratio is informational only because no logo clearspace is required for F-54.

Coordinates use `round(normalized_coordinate × dimension)`, clamped to the last pixel.

| Point | x | y | RGB | Exact white |
| :-- | --: | --: | :-- | :-- |
| top_left_corner | 0 | 0 | (254,255,255) | no |
| top_right_corner | 1773 | 0 | (255,255,254) | no |
| bottom_left_corner | 0 | 886 | (254,253,254) | no |
| bottom_right_corner | 1773 | 886 | (254,253,254) | no |
| registered_1 | 71 | 35 | (253,253,253) | no |
| registered_2 | 532 | 35 | (255,254,255) | no |
| registered_3 | 1242 | 35 | (254,254,254) | no |
| registered_4 | 1703 | 35 | (254,254,254) | no |
| registered_5 | 71 | 852 | (255,255,255) | yes |
| registered_6 | 532 | 852 | (254,253,254) | no |
| registered_7 | 1242 | 852 | (255,255,255) | yes |
| registered_8 | 1703 | 852 | (255,255,255) | yes |

Keep candidate unchanged in experiments. Prepare one focused exact-white prompt revision; independent prompt review must pass before the next candidate. No background painting or color post-processing.
