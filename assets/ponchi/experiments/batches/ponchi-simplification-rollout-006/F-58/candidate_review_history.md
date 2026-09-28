# F-58 candidate review history

- Source: `assets/ponchi/final/F-58.webp`; hash from prompt sidecar. Prompt: `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-006/F-58.md`; independent prompt review PASS preceded generation.
- v1: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-58/F-58_candidate_v1.png`; SHA-256 `85f2e2c845c7dd93921091283179fdb6a9a4f5f0b2e400ea313b4eb666d52fb1`; 1774x887 RGB. Independent review: HOLD: Character B is repeated three times, document strokes resemble pseudo-text, and exact-white/palette gate fails.
- v2: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-58/F-58_candidate_v2.png`; SHA-256 `9d007fbcc4ad8c18278ba1cb3c6182b1e6b2036d4aa32f381666b3f020fad24b`; 1774x887 RGBA; corners `[(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]`; exact opaque white pixels 0.000%; transparent pixels 99.826%.
- v2 color audit: repository audit PASS under tolerant palette rules; see `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/color_audit_v2.csv`. Strict full-canvas white gate: FAIL. color audit pass (off-palette 0.008057); strict white canvas FAIL: fully transparent background (99.826% transparent pixels), no opaque white corners.
- Independent v2 semantic/style review: pending. One targeted revision used of maximum two; no next revision before review. Final production image, official overlay, adoption, and publication remain untouched/unauthorized.

## Independent v2 review — 2026-09-28

- Reviewer: `/root/batch007_primary_a`; candidate SHA/path and source sidecar hash checked.
- Result: HOLD. Stash → separate work → restore reads clearly at 200px; exactly one Character B matches the approved reference. The canvas is RGBA and 99.826% transparent; document icons have text-like strokes and decorative bursts remain. One final revision: opaque pure-white background, blank solid bundle shapes without interior strokes, remove bursts.
- Disposition: HOLD pending one second/final targeted revision (revision 2/2), followed by independent final review. If a required meaning, character, layout, or strict-white gate remains, stop generation and close HOLD. No adoption, overlay, or publication.

## v3 final revision and independent review — 2026-09-28

- v3: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-58/F-58_candidate_v3.png`; SHA-256 `0152015d8763f57467fe88712041689ef424c08fdd69facc2eb6a646dd23f280`; 1774x887 RGB; corner pixels `[(255, 255, 255, 255), (254, 255, 254, 255), (254, 253, 253, 255), (254, 253, 254, 255)]`; exact opaque-white pixels 14.670%; transparent pixels 0.000%. Exact input paths/hashes and generation prompt: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-58/candidate_v3_generation_prompt.md`.
- Independent final review: HOLD. At 200px stash → separate work → restore reads; one Character B matches reference, and v2 transparency, pseudo-text strokes, and bursts are corrected. Exact-white fails: opaque RGB, corners off-white, only 14.670% exact white. No more edits after revision 2/2.
- Tolerant repository color audit: PASS; strict opaque four-corner white gate: FAIL. Revision count 2/2. Disposition: HOLD; no more generation, logo overlay, adoption, or publication.
