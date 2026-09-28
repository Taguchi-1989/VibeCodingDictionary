# I-80 candidate v3 independent review

- **Verdict: HOLD**
- **Reviewer:** `/root/review_wave001_b` (independent visual review)
- **Date:** 2026-09-28
- **Candidate:** `I-80_candidate_v3.png`, 1774×887 RGB
- **Candidate SHA-256:** `A5EE37AFC9BB2D92DFCAE3C5731CA7BA5C47F0764D2C717E1C78CBF22D8F70D4`
- **Current sidecar SHA-256:** `6074BA8AAB87C76A99F8E00ACB4B1E5833609B82ED47AE6B613F2F4D271E1BF9`
- **PASS-reviewed v3 prompt body SHA-256:** `E08B163C700DB1BE5ABF47A2E931E025EC856448C1A62E8EE3A675E1AAFFBAD7`
- **Source:** `assets/ponchi/final/I-80.webp`, actual SHA-256 `F7312FBE52652E19A41DB37BABD92704679979AB65AAEEAA4FA51895D66BF0A8`, 1254×627 RGB; matches sidecar/prompt.
- **Character A reference:** `assets/ponchi/references/character-a-reader-woman.png`, actual SHA-256 `18E2B7E216BF76CD382002CA4E6CAF20EF175332E28EC7B6AB0E5EBC2AF7DDF0`, 320×420 RGB; matches sidecar/prompt.
- **Human brief:** `content/entries/mcp/I-80_diy_mcp_template[人書].md` describes one developer-built server with three capabilities and local-vs-shared connection choices.
- **Logo policy:** `not_needed` / `logo_avoid`; no logo or reserved logo ROI is required.

## Findings

- **Meaning and 200×100 readability — PASS.** Character A is beside the central server with both hands visibly fitting/connecting the top drawer, preserving the authoring action. One cabinet contains exactly three distinct drawers: wrench, database/storage cylinder, and blank speech-card cue. A solid short route reaches one nearby computer; a separate dashed shared route branches to three generic endpoints. At 200×100, the three meanings and local-versus-shared topology remain recognizable.
- **Character, extra content and text — PASS.** The developer's bob, face and dark jacket match the approved Character A reference. There is one person and no robot. Endpoint screens are blank; no readable or pseudo-text, logo, branded UI or recognizable product mark appears.
- **Simplification and style — PARTIAL.** The v2 extra control board/cards are gone, and the diagram reads clearly. The server nevertheless has a large beveled 3D casing, layered inner frames, repeated circular drawer fittings and shaded drawer faces. Those details make the central object heavier than the PASS-reviewed prompt's plain outlined enclosure and add complexity that is not needed to distinguish the three drawers. Visually, pale-blue gradients/shading appear on the cabinet and device screens despite the requested flat fills; `color_audit_v3.md` records `review` with off-palette ratio `0.011370` (including cyan/teal and purple pixels).
- **Geometry audit — PASS, no logo gate.** `image_audit_v3.md` reports native 1774×887, bbox `0.579`, `clearspace_required=false`, status `pass`. No logo clearspace is required for this item.
- **Strict-white and perimeter — FAIL.** `background_samples_v3.md` reports exact-white corners `0/4`, registered points `2/12`, and exact-white pixels in the required 3% perimeter `26,759/184,094`; verdict is `HOLD_fail_fast`. No mask was created and no post-processing is recorded. The main artwork stays within the visible 3% margin, but that does not pass the exact-white sample/perimeter gate.

## Gate

Keep v3 on HOLD: semantics, character identity and routing are clear, but exact-white fail-fast blocks acceptance and the color audit remains `review`. The cabinet can be simpler and its fills flatter in any separately authorized future work. This is final revision 2/2; this review does not approve another generation, promotion or production adoption.
