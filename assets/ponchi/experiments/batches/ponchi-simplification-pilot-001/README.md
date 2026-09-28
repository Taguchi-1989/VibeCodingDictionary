# Ponchi simplification pilot 001

A 20-entry representative candidate batch (two entries per A-J chapter). This is an experiment only. It does not replace or modify `assets/ponchi/final/`.

- Shared production style: white background, uniform black/navy linework, approved pale blues, 2:1 canvas, 1254x627 output.
- Candidate generation never draws a company logo. B-4 and B-7 reserve the same top-right logo area; their official assets are deterministic overlays and remain publication-use review pending.
- Other entries omit logos where the concept remains clear without one. This pilot tests the conditional-logo rule.
- First-pass prompts are in `prompts/`; nine targeted simplification prompts are in `prompts/v2/`. The CSV ledger is the status source for this pilot.
- Human selection remains pending; no final adoption is authorized.

## First-pass review

- `pilot_contact_sheet_v1_20.png` shows the initial 20 candidates. `logo_overlay_comparison.png` shows B-4/B-7 base and official-overlay variants.
- Visual review found the main palette cohesive and no readable generated text or accidental marks. Rework first: A-7, C-9, D-12, E-1, G-10, G-41, J-14, J-84; H-7 is readable with a density note.
- Shortlist for later human selection without immediate rework: A-3, B-4, B-7 (logo use still unverified), C-6, D-51, E-50, F-2, F-43, H-1, I-2, I-4. This is not an adoption decision.
- All rows retain `human_decision=pending` and `final_adoption=not_authorized`. The official source pages were checked on 2026-09-27; actual local-file retrieval dates were not recorded.

## Official mark provenance

- B-4 source page: https://cursor.com/brand. The current guide describes 2D logos as the default, horizontal lockups as preferred, and the product name as “Cursor”. The page does not establish permission for this glossary context.
- B-7 source page: https://www.anthropic.com/news. Anthropic’s newsroom exposes its official press-kit download link; detailed mark-use conditions could not be confirmed from the linked press-kit page.
- Local asset retrieval dates were not recorded. Asset SHA-256, local source path, overlay rectangle, and source-page check date are in the CSV and JSON sidecars. Keep both logo candidates out of final until their use condition is resolved.

## Simplification revision 2

- Revisions were made for A-7, C-9, D-12, E-1, G-10, G-41, H-7, J-14, and J-84. The first version remains alongside each current revision.
- `pilot_contact_sheet_current_20.png` shows the current candidate per ledger row. `pilot_revision_comparison_v1_v2.png` compares the nine revised entries side by side.
- For E-1, G-41, and J-84, one targeted image edit reduced the pet robot and removed its ground shadow.
- Independent second-pass review found the revised candidates readable and consistent with the series style. C-9 and D-12 retain separate semantic confirmation gates. All images remain candidate-only; human adoption and final-image promotion are not authorized.

## Current candidate set

- The current contact sheet follows each row's normalized image path in the ledger. Exact current edit prompts are saved under prompts/current_edits/.
- Current refinements: C-9 was reduced to three pictograms; D-12, H-1, and I-2 were color-corrected while preserving their diagrams; J-84's small robot and grid fills were cleaned up.
- Every selected candidate is 1254x627. The final asset directory remains untouched.

## Current machine audit

- Palette audit: 20/20 pass.
- Image size/density audit: 16/20 pass. A-7 (0.301), B-7 (0.470), C-9 (0.480), and H-7 (0.361) are flagged for manual review because the ink bounding box is below the 0.50 threshold. C-9's lower coverage follows its simpler three-pictogram layout.
- Per-entry outcomes and reports are under audits/ and recorded in the CSV ledger. Density flags are review cues, not automatic semantic failures.

## Remaining human review

- Confirm that C-9's generic compute hardware represents the NVIDIA entry and that D-12's two groups of three convey the intended meaning.
- B-4 (Cursor) and B-7 (Claude Code) use deterministic overlays of official local assets, but publication-use conditions remain unverified. Local asset retrieval dates were not recorded.
- Human selection remains pending for all 20 entries; no final-image adoption is authorized.

## Independent visual review

- Thumbnail readability and series style pass for all 20 current candidates. A-7 and H-7 are intentionally sparse; G-10, G-41, and J-14 use the entry title to clarify an abstract metaphor. Those notes are in the ledger.
- J-84's robot is 95 px tall (15.2% of canvas height); the remaining grid fills are clean and smooth.
- C-9/NVIDIA and D-12's two groups of three still need semantic confirmation. The density audit separately flags A-7, B-7, C-9, and H-7 for manual review.
- Every row remains human-decision pending and final adoption unauthorized.

## Policy constraints to harmonize before production

| Topic | Written policy | Current batch pipeline | Decision needed |
| :-- | :-- | :-- | :-- |
| Palette | The style block in drafts/IMAGE_GEN_POLICY_v2.md lists white, navy, black, and pale blue. | scripts/ponchi_palette_normalize.py recognizes nine colors, including gray and several blue tones; the color audit passes the current 20 candidates against this pipeline. | Choose whether the four-color brief or nine-color normalizer is authoritative. |
| Gradients | The common prompt says no gradients; a later style block permits gradients within navy and pale blue. | Current candidates use smooth in-range tonal fills; no textured fills remain in the reviewed candidates. | Make the gradient rule consistent. |
| Aspect and resolution | The brief lists 4:3, 16:9, 3:2, or 1:1 and asks for a 1500 px long edge for print. | The current slot and image audit use 2:1 at 1254x627; the generation-source images are about 1774x887. | Decide whether 1254x627 is the review preview and 1774x887 the print master, and whether 2:1 is an approved ratio. |
| Logos | The project brief says not to generate company logos and to composite official assets. | B-4 and B-7 use deterministic official-asset overlays. | Their publication-use conditions remain unverified. |

The current machine status is useful for comparing candidates, but production adoption should wait until these source-of-truth differences and the two remaining semantic confirmations are resolved.
