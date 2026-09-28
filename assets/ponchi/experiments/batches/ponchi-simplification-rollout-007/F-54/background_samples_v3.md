# F-54 candidate v3 exact-white fail-fast audit

- Candidate: `F-54_candidate_v3.png`; dimensions `1774x887`; mode `RGB`; fully opaque: `True`.
- Four corners exact `#FFFFFF`: `0/4`.
- Registered points exact `#FFFFFF`: `4/8`.
- Fail-fast result: `FAIL`.
- Same-size background mask: not created because fail-fast checks failed.

| Check | x | y | RGB | Exact white |
|---|---:|---:|---|---|
| corner_top_left | 0 | 0 | `254,255,255` | no |
| corner_top_right | 1773 | 0 | `254,254,254` | no |
| corner_bottom_left | 0 | 886 | `254,253,253` | no |
| corner_bottom_right | 1773 | 886 | `254,253,254` | no |
| registered_1 | 71 | 35 | `253,253,253` | no |
| registered_2 | 532 | 35 | `255,255,255` | yes |
| registered_3 | 1242 | 35 | `254,254,254` | no |
| registered_4 | 1703 | 35 | `254,254,254` | no |
| registered_5 | 71 | 852 | `255,255,255` | yes |
| registered_6 | 532 | 852 | `254,253,254` | no |
| registered_7 | 1242 | 852 | `255,255,255` | yes |
| registered_8 | 1703 | 852 | `255,255,255` | yes |