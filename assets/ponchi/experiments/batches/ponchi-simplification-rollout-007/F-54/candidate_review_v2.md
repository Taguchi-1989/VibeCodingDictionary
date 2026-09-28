# F-54 candidate v2 machine review record

- Candidate: `F-54_candidate_v2.png`
- SHA-256: `FDFD93C36C80C31857747B83741421783876A952E3869750F57DC3AC7D26B949`
- Dimensions/mode: 1774×887 RGB
- Independent reviewer: `/root/review_wave001_b`, 2026-09-28.
- Overall: **HOLD only at exact-white gate.**

## Independent semantic/style review

At 200px, three distinct sequential checkpoints with the middle highlighted, one curved return arrow, and one calm Character B at right read clearly. Character B matches the approved reference and candidate v1. The document/snapshot strokes are abstract generic glyphs, not readable words or code. No extra people/robots, logo/brand, branded UI, or remote/push/merge cue. Clearspace is not required by the sidecar.

## Machine audits

- Geometry: PASS, bbox coverage 0.556, native dimensions 1774×887.
- Clearspace is not required for F-54 (`LOGO_MODE: not_required`, verified by experiment-local audit context).
- Tolerance color audit: PASS; this does not prove exact palette pixels.
- Exact-white: FAIL at 3/4 corners and 4/8 registered points. Exact-white pixels: 266,658 / 1,573,538 (16.9464%). No background mask retained because fail-fast checks failed.

Coordinates use `round(normalized_coordinate × dimension)`, clamped to the last pixel.

| Point | x | y | RGB | Exact white |
| :-- | --: | --: | :-- | :-- |
| top_left_corner | 0 | 0 | (255,255,255) | yes |
| top_right_corner | 1773 | 0 | (255,255,254) | no |
| bottom_left_corner | 0 | 886 | (254,253,253) | no |
| bottom_right_corner | 1773 | 886 | (254,253,254) | no |
| registered_1 | 71 | 35 | (253,253,253) | no |
| registered_2 | 532 | 35 | (255,255,255) | yes |
| registered_3 | 1242 | 35 | (254,254,254) | no |
| registered_4 | 1703 | 35 | (254,254,254) | no |
| registered_5 | 71 | 852 | (255,255,255) | yes |
| registered_6 | 532 | 852 | (254,253,254) | no |
| registered_7 | 1242 | 852 | (255,255,255) | yes |
| registered_8 | 1703 | 852 | (255,255,255) | yes |

Keep the image unchanged. Candidate v2 uses revision 1/2. One final exact-white-only candidate revision may be prepared, but remains subject to its own prompt review; no post-processing.
