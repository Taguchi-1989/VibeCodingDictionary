# Ponchi Image Audit

| file | size | bbox | clearspace required | clearspace ink | status |
| :-- | :-- | --: | :-- | --: | :-- |
| `E-31_candidate_v3.png` | `1774x887` | 1.000 | `false` | 0.9936 | `pass` |
| `G-14_candidate_v3.png` | `1774x887` | 0.791 | `false` | 0.0265 | `pass` |
| `I-5_candidate_v3.png` | `1774x887` | 0.538 | `false` | 0.0257 | `pass` |
| `J-71_candidate_v3.png` | `1774x887` | 0.855 | `false` | 0.0676 | `pass` |


## Transparency interpretation

E-31 v3 is RGBA with 99.79% of pixels below alpha 255 and 75.05% fully transparent. The image-audit bbox treats transparent black RGB as ink, reports bbox 1.000, and labels it pass. This is not a valid density/background pass; treat E-31 v3 as HOLD for the solid white-background requirement. G-14, I-5, and J-71 v3 are fully opaque.
