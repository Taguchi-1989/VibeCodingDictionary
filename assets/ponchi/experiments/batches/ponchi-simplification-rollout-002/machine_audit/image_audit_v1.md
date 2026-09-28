# Ponchi Image Audit

| file | size | bbox | clearspace required | clearspace ink | status |
| :-- | :-- | --: | :-- | --: | :-- |
| `E-31_candidate_v1.png` | `1774x887` | 0.750 | `false` | 0.0541 | `pass` |
| `G-14_candidate_v1.png` | `1774x887` | 0.790 | `false` | 0.0266 | `pass` |
| `G-16_candidate_v1.png` | `1774x887` | 0.765 | `false` | 0.0187 | `pass` |
| `I-5_candidate_v1.png` | `1774x887` | 1.000 | `false` | 0.9561 | `pass` |
| `J-71_candidate_v1.png` | `1774x887` | 1.000 | `false` | 0.5325 | `pass` |


## Transparency interpretation

The script's bbox routine counts RGB pixels without applying the alpha channel. E-31, G-14, and G-16 are fully opaque. I-5 has 99.83% pixels with alpha below 255 (75.54% fully transparent), and J-71 has 99.68% below 255 (34.81% fully transparent). Their raw RGB bbox values of 1.000 are therefore invalid; treat their image-density result as review, and the specified white background as unverified. The color audit ignores sufficiently transparent pixels; J-71 still fails its palette gate at 0.023255.
