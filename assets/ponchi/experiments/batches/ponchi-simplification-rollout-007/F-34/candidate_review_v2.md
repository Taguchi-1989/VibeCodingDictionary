# F-34 candidate v2 machine review record

- Candidate: `F-34_candidate_v2.png`
- SHA-256: `2BC091B749092B37C188995C438F08E1AEE3061693473BCD91220355289222AF`
- Dimensions/mode: 1774×887 RGB
- Source SHA-256: `0a462262856c4dad6b9da7e8b233ee8685f0be9ff27cf79981ba653e750fd511`
- Character B reference SHA-256: `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99`
- Independent candidate reviewer: pending.
- Provisional overall: **HOLD** at exact-white and mapped clearspace gates; semantic/style review pending.

## Machine audits

- Geometry: PASS, bbox coverage 0.644 at native 1774×887.
- Tolerance color audit: PASS.
- Exact-white: FAIL at all four corners and four of eight registered points (p2, p5, p7, p8 pass). No mask retained because fail-fast points failed.
- Sidecar reserved area `[986,0,220,240]` on 1254×627 maps to candidate ROI `(1395,0)-(1706,340)`. Foreground proxy (`min(R,G,B)<245`) finds 2,738 pixels / 105,740 (2.5894%), concentrated on the editor border near the lower edge of the ROI.

The general image audit's default top-right clearspace proxy is not the same as the mapped sidecar rectangle. Independent review must check the exact mapped ROI, plus meaning, single Character B, magnifier/publisher-check cue, capability transfer, no pseudo-text/extra person/brand, and style at 200px.

No pixel edits or post-processing. Candidate remains internal.
