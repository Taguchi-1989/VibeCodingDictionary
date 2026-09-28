# G-19 independent candidate review history

Scope: semantic and visual/style audit of candidate images against the human-authored brief, the instantiated prompt, brand record, and thumbnail intent. Independent agents did not edit candidates.

## Candidate v1

- SHA-256: `70fe0d0685802350e3209a6981a9ef0cabf759f979d58c4d9d71a68e18c5951d`
- Semantic review: PARTIAL. Ten rows on each side and cache reuse were shown, with no unsupported provider, price, or total-savings claim. The first write mark did not visibly represent the documented 1.25× amount.
- Visual/style review: PARTIAL. Exact 2:1 canvas and palette/artifact checks passed. Measured marks were approximately 154px normal, 160px write (1.04×), and 19px hit (0.12×); the engineer competed with the comparison.
- Action: preserve v1; target the write ratio and reduce figure prominence.

## Candidate v2

- SHA-256: `aea8aad25777a422ac22409d31cac5c4920dd6870eac943c70e5fc4cba19452c`
- Semantic review: PARTIAL. Ten aligned requests on each side, document reuse, cache cylinder, and one secondary engineer remained. No total-savings implication or other semantic regression. Measured marks: 153px normal, 168px write (1.10×), 19px hit (0.12×).
- Visual/style review: PARTIAL. Exact 2:1, permitted palette, no text/logo/watermark, and secondary figure passed. The write premium remained nearly invisible at 200px.
- Action: preserve v2; anchor follow-up lengths to the unchanged normal-bar reference.

## Candidate v3

- SHA-256: `e9424237eadcc25f9f987ae077ab42ecb6a516d62cd1120e5844d54e112d26d5`
- Semantic review: PARTIAL. Meaning, ten-row layout, one secondary engineer, and no-total-savings reading passed. Measured marks: 153px normal, 182px write (1.19×), 19px hit (0.124×).
- Visual/style review: PARTIAL. Exact 2:1, simplicity, palette, and figure hierarchy passed. The initial write remained short of 1.25×.
- Action: preserve v3; make one final ratio-focused adjustment.

## Candidate v4

- SHA-256: `8540d79eb3c6eecad706f2363cd7ae281a1a29654b9d2e22a1403e554d650bf5`
- Semantic review: PARTIAL. Ten requests per side, cache reuse, and no unsupported aggregate claim passed. Measured marks: 153px normal, 182px write (1.19×, target 1.25×), and 16px hit (0.105×, target 0.1×).
- Visual/style review: PARTIAL. Exact 2:1, palette, simplicity, figure prominence, and no visible text/logo/watermark passed. At 200px, the write remained around 20.5px versus 17px normal; the hit marks were around 1.8px.
- Decision: ratio blocker remains. Keep as an internal candidate only; do not adopt into `assets/ponchi/final/`. The next candidate can proceed using the v1.1 template and should not repeat image-generation edits for this same unresolved mark.
