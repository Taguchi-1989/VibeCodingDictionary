# F-11 candidate v1 independent review

- **Verdict:** HOLD
- **Reviewer:** `/root/review_wave001_c` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `F-11_candidate_v1.png`, 1774×887 RGB
- **Candidate SHA-256:** `9c3ad1e667de3958654326ef68a7d89af00eb1e54a204cec4a629c3261e6a459`
- **Sidecar:** `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/F-11.md`
- **Sidecar SHA-256:** `5042b1331719a201cf21a9d1c43572c8df7d3883f50773b8ae3e18bfac4d21ff`
- **Edit source:** `assets/ponchi/experiments/batches/ponchi-batch-008/F-11_base_1254x627.png`, SHA-256 `0eee682c4e8035c9755336e22827e345ae32528325e4d8f616b06a79a11ddba1` (logo-free base; visually inspected)
- **Character reference:** `assets/ponchi/references/character-a-reader-woman.png`, SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0` (visually inspected)
- **Official Next.js asset:** `assets/logos/nextjs/nextjs-assets/NEXTJS/logotype/light-background/nextjs-logotype-light-background.svg`, SHA-256 `603d77738f767d2afa37e225da1407dbdb2cd92e76695f010316910ae1e88761` (recorded in sidecar; not used as an edit input)

## Findings

- **Meaning and small-size readability — PARTIAL PASS.** The 2:1 composition clearly groups four separate panels inside one central framework canopy, with one reader outside. At roughly 200px wide the canopy, four-panel sequence, and left-to-right arrows remain distinguishable. React, routing, server, and deployment/settings are suggested by the atom, route nodes, server stack, and gear/cloud symbols, respectively. However, the atom is the recognizable React mark rather than a neutral component-window shape, and placing a cloud inside the Next.js boundary can imply an external hosting provider belongs to Next.js. Replace the atom with a generic component/window symbol and the cloud with an unbranded settings/deployment motif that does not depict a provider.
- **Character — PASS.** Exactly one Character A reader appears outside the diagram and visually matches the supplied reference. No second character or robot is visible.
- **Logo/text constraints — PARTIAL.** No Next.js or Vercel lockup and no readable words/code are visible. The React atom resembles a product mark and conflicts with the sidecar's generic-form/no-logo-like-mark rule. Small repeated dots in browser/server panels also approach pseudo-text/UI decoration; simplify them if revising.
- **Composition and reserved ROI — FAIL.** The sidecar's source clearspace `[686,0,520,180]` maps to candidate ROI `x=970..1705, y=0..254` (half-open). The machine image audit reports `clearspace ink=0.0187`; the background/ROI audit finds `13,980` foreground-proxy pixels with bounds `(970,236)-(1705,254)`. The canopy's lower border enters the reserved area. Keep the entire diagram and its outline below/outside the ROI.
- **Exact-white background — FAIL.** All four image corners fail exact `#FFFFFF`. Only 3 of 8 registered points pass: p5, p7, and p8. The remaining samples are p1 `(253,253,253)`, p2 `(255,254,254)`, p3 `(254,253,254)`, p4 `(254,254,254)`, and p6 `(253,253,253)`; corners are `(254,253,255)`, `(255,254,254)`, `(254,253,254)`, and `(253,253,253)`. The mapped ROI is not empty or uniform white. Regenerate on an opaque flat exact-white canvas and pass both registered-point and full-mask checks.
- **Canvas and palette — PARTIAL.** Candidate is 1774×887 RGB, approximately 2:1, and exceeds the 1500px long-edge target. `ponchi-image-audit-v1.md` reports bbox `0.558`, clearspace ink `0.0187`, status `review`. `ponchi-color-audit-v1.md` reports palette pass with off-palette ratio `0.004323`; that does not satisfy the stricter exact-white/background or ROI requirements.
- **Internal-only boundary — PASS.** Candidate is under the experiments directory and has no visible brand lockup. Keep it internal; no overlay, adoption, publication, or release.

## Gate

Keep candidate v1 on HOLD. A revision needs a generic React/component symbol, a deployment-settings motif that does not place a hosting provider inside the framework boundary, a diagram fully outside the reserved ROI, and exact opaque `#FFFFFF` confirmed by corners, registered samples, and a full same-size background mask. Do not paint/post-process this candidate to simulate compliance or promote it to production.
