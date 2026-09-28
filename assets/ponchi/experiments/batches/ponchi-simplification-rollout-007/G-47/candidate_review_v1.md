# G-47 candidate v1 independent review

- Candidate: `G-47_candidate_v1.png`
- Candidate SHA-256: `0F560B573924D74CB9C24E16BDA5FEA6900830F36C18AED44B7AA7817AA320CF`
- Dimensions/mode: 1774×887 RGB; matches the sidecar's 2:1, long-edge-at-least-1500 output requirement.
- Overall verdict: **HOLD**. Keep internal; no promotion/adoption.

## Provenance and prompt alignment

- Sidecar source path `assets/ponchi/experiments/batches/ponchi-batch-013/G-47_base_1254x627.png` actual SHA-256: `D73CAA0F0E5EE1F935697E650A4436EA33ECCE405F221D206310E9A03B26146A`; matches the declared hash.
- Required Character B reference `assets/ponchi/references/character-b-teacher-man.png` actual SHA-256: `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`; matches the declared hash.
- Current final reference actual SHA-256 also matches its declared `B3466D14803922E2A9F2FC973684523247A114CD17A22627085A5B0E0E89FDF4` provenance value. Candidate uses the specified logo-free Batch 013 base and does not overlay the final/logo asset.
- Reviewed against `G-47.md` and `content/entries/term_llm/G-47_auto_compact[済].md` (`メイン図 / A. Before / After`, `誌面ポンチ絵メモ`): long conversation → compaction → short summary → continued conversation, one engineer, no labels or threshold.

## Visual review

- At 200×100 (in-memory preview), the long message stack, central folding/compression symbol, one compact summary card, and two continuation cards remain distinguishable in the intended left-to-right order. The two outgoing arrows fork to the two right-side messages, which slightly suggests parallel branches; the overall continued-work meaning still reads.
- Exactly one engineer is present at lower left. The black-haired, light-gray-shirted male figure at the laptop matches the approved Character B design and role; the duplicate figure from the source is removed.
- No readable words, numeric threshold, command, product name, Claude Code/Anthropic mark, recognizable logo, or real branded product UI is visible. The laptop is generic and consistent with the engineer reference.
- The message cards contain repeated short horizontal placeholder bars. They are not readable at 200px, but evoke pseudo-text/UI rows despite the prompt's no-fake-text/no-UI-like-bars direction. The cards are generic and convey conversation; simplifying these bars further would improve strict text-free compliance.
- Series treatment is clean, flat, high-contrast navy/light-blue/charcoal line art with ample whitespace. No unrelated figure, robot, product card, or extra stage was observed.

## Machine evidence and gates

- Candidate SHA and size were checked from the local file. Image audit artifact in this folder reports bbox coverage `0.578`, clearspace `not required`, clearspace ink ratio `0.0000`, and status `pass`; this is consistent with sidecar `LOGO_MODE: not_required` / `logo_avoid` and no reserved logo rectangle.
- The folder's color audit reports tolerance-palette `pass` (off-palette ratio `0.002573`). This does not override the separate exact-white requirement.
- Exact-white fails all four corners: TL `(253,255,255)`, TR `(254,255,254)`, BL `(253,253,253)`, BR `(253,253,253)`. Using normalized sample positions rounded against `(W−1,H−1)`, only p2 is exact white; p1 and p3–p8 fail (1/8 exact). Exact-white pixels are about `17.62%` of the canvas, so the background is not an exact-white full canvas.
- No same-size background mask is present among the G-47 audit artifacts. Since the exact-white fail-fast checks fail, no mask should be created and no white-paint post-processing should be applied.

## Final decision

**HOLD** on exact-white background compliance. Semantic flow, single-character identity, brand avoidance, dimensions, and palette audit are acceptable for this internal candidate. Keep the pseudo-text-like bars and branched continuation arrows noted for any authorized future revision; do not promote this candidate or treat the machine palette/image audit passes as acceptance.
