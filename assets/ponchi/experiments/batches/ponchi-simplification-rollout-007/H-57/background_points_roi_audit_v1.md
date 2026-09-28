# H-57 v1 background point and reserved-ROI audit

- Candidate: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/H-57/H-57_candidate_v1.png`
- Dimensions/mode: 1774x887 RGB; opacity: True
- Point mapping: registered coordinates map to `(round(x*W), round(y*H))`, clamped to canvas.
- Registered sample points checked: 8; exact-white: 0/8.
- Four extreme canvas corners exact-white: 0/4.
- Reserved rectangle `[966,16,240,240]` mapped by source/output scale, conservative floor/ceil bounds: `[1366,22,341,341]`; area 116281 px; exact-white pixels 17676/116281; non-white pixels 98605; all-white: False.
- Distinct ROI RGB values (most common, max 8): `[((254, 254, 254), 47901), ((255, 255, 255), 17676), ((255, 254, 255), 6422), ((253, 253, 253), 6400), ((254, 253, 254), 3654), ((255, 254, 254), 3583), ((254, 255, 254), 1740), ((254, 255, 255), 1497)]`.
- Fail-fast: FAIL (13 failed checks among corners, points, and ROI).
- Full-canvas background mask: NOT CREATED because the fail-fast exact-white gate failed; no post-generation painting performed.
- Semantic/layout review: pending independent review; this report is machine-only.

Detailed pixel checks: `background_points_roi_audit_v1.csv`.
