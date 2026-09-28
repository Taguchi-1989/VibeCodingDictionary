# C-82 candidate v1 independent review (2026-09-28)

- Candidate: `C-82_candidate_v1.png`; SHA-256 `9dbf5ac1b949879a0cc1aca6dc76b13a717edc0eaf4a24a29a937fc12e3db64d`; 1774×887 RGB, opaque.
- Disposition: **HOLD**. The 200px review found the three-stage news → video → viewer composition, one viewer, one Pet Robot, and reserved avatar rectangle intact. No official logo or readable text was seen.
- Style blockers: repeated horizontal strokes inside the news cards and summary sheet read as pseudo-text; background corners are not exact `#FFFFFF`; the dominant dark line color measured `#083E86`, not the specified `#123E82`.
- Avatar clearspace: mapped region `[1499,22,1697,220]` was empty of artwork; all 39,204 pixels were within two RGB levels of white.
- Action: v2 removes the pseudo-text strokes and makes the summary sheet blank. v2 is pending a fresh independent review and palette check.
- Adoption, official-avatar overlay, and publication remain unauthorized.

## Candidate v3 — 2026-09-28

- Path: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-004/C-82/C-82_candidate_v3.png`; SHA-256 `65ea3089222f6d1888e2c7eefa97133ab4b229bf0243a83e3d40de36521cec1a`; 1774x887 RGB.
- Corners: `[(253, 255, 255), (254, 255, 254), (254, 253, 253), (254, 253, 254)]`; exact-white gate fails.
- Independent review pending. Revision cap reached; no further generation.

## Candidate v3 — independent review (2026-09-28)

- Disposition: **HOLD**. At 200px, the three news examples → video channel → viewer flow reads clearly; one viewer and one Pet Robot remain, with no readable text or logo. Reserved avatar region is empty.
- Machine/style: 1774×887 RGB; SHA-256 `65ea3089222f6d1888e2c7eefa97133ab4b229bf0243a83e3d40de36521cec1a`. Pure `#FFFFFF` is 15.088%; `#FEFEFE` is 38.567%; exact palette fails.
- Avatar public-use terms remain unverified. Revision cap reached; no more generation or overlay.
