# F-91 candidate review history

- Source: `assets/ponchi/final/F-91.webp`; hash from prompt sidecar. Prompt: `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-006/F-91.md`; independent prompt review PASS preceded generation.
- v1: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-91/F-91_candidate_v1.png`; SHA-256 `05857e657b2b05cd3e08864f49d1dfb25182503ded3610c26d2177a7785ba4d1`; 1774x887 RGB. Independent review: HOLD: Git logo, code-like UI, pseudo-text, unclear repo-vs-tracked boundary and app-read relationship; exact-white/palette gate fails.
- v2: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-91/F-91_candidate_v2.png`; SHA-256 `f498ea29c3cc27013a6e9076892eaec2c3bdf6ffda3cdf2f5b053e395a30b2fd`; 1774x887 RGB; corners `[(253, 255, 255, 255), (254, 255, 254, 255), (254, 253, 254, 255), (254, 253, 254, 255)]`; exact opaque white pixels 21.594%; transparent pixels 0.000%.
- v2 color audit: repository audit PASS under tolerant palette rules; see `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/color_audit_v2.csv`. Strict full-canvas white gate: FAIL. color audit pass (off-palette 0.000912); strict white canvas FAIL: corners off-white; exact-white pixels 21.594%.
- Independent v2 semantic/style review: pending. One targeted revision used of maximum two; no next revision before review. Final production image, official overlay, adoption, and publication remain untouched/unauthorized.

## Independent v2 review — 2026-09-28

- Reviewer: `/root/batch007_primary_a`; candidate SHA/path and source sidecar hash checked.
- Result: HOLD. At 200px it reads as a file feeding an app in a repository boundary, but does not show the source/value relationship or distinguish tracked history clearly. It omits the developer required by the sidecar, while the v2 prompt said no person was needed. Exact white fails (21.594% exact white; corners off-white). One final revision: restore one developer, place source in tracked history and local environment file outside it but inside the repository, show the app reading that file, use opaque exact white.
- Disposition: HOLD pending one second/final targeted revision (revision 2/2), followed by independent final review. If a required meaning, character, layout, or strict-white gate remains, stop generation and close HOLD. No adoption, overlay, or publication.

## v3 final revision and independent review — 2026-09-28

- v3: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-91/F-91_candidate_v3.png`; SHA-256 `d364764626d04e1db8be4700f81861646000d966757ec6a8c33e78aa69ab9af9`; 1774x887 RGB; corner pixels `[(254, 255, 255, 255), (254, 255, 254, 255), (254, 253, 254, 255), (253, 253, 253, 255)]`; exact opaque-white pixels 17.525%; transparent pixels 0.000%. Exact input paths/hashes and generation prompt: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-006/F-91/candidate_v3_generation_prompt.md`.
- Independent final review: HOLD. At 200px developer, source inside dashed tracked area, env file outside it but inside repo, and arrow to app read clearly; no logo/pseudo-text. Source and env pages show the same filled tile, so value removal/movement is not distinct. Exact white fails (17.525% exact white); no more edits after revision 2/2.
- Tolerant repository color audit: PASS; strict opaque four-corner white gate: FAIL. Revision count 2/2. Disposition: HOLD; no more generation, logo overlay, adoption, or publication.
