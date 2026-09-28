# J-21 v1 exact-white background and perimeter ROI audit

- Candidate: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/J-21/J-21_candidate_v1.png`
- Dimensions/mode: 1774x887 RGB; opaque RGB: True
- Four extreme canvas corners exact-white: 0/4.
- Registered sidecar points exact-white: 2/12; coordinates mapped by `(round(x*W), round(y*H))`, clamped to canvas.
- Sidecar has no logo rectangle/clearspace. Audited its explicit 3% blank perimeter as the relevant background ROI: edge strips x=54px, y=27px; union area 185760 px; non-white pixels 146058; exact-white coverage 39702/185760; ROI all-white: False.
- Most common ROI RGBs (max 8): `[((254, 254, 254), 103102), ((255, 255, 255), 39702), ((253, 253, 253), 11716), ((255, 254, 255), 11402), ((254, 253, 254), 5615), ((254, 255, 254), 3033), ((254, 254, 255), 1454), ((255, 255, 254), 1307)]`.
- Fail-fast exact-white gate: FAIL (15 failed checks).
- Same-size background mask: NOT CREATED because fail-fast failed; no post-generation painting.
- Semantic/layout review: pending independent review; this report is machine-only.

Detailed pixel checks: `background_points_perimeter_audit_v1.csv`.
