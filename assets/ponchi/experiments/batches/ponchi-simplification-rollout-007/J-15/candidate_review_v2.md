# J-15 candidate v2 independent review

- **Verdict:** HOLD
- **Reviewer:** `/root/review_wave001_b` (independent visual review)
- **Date:** 2026-09-28
- **Candidate:** `J-15_candidate_v2.png`, 1774×887 RGB
- **Candidate SHA-256:** `C90FFA6B74585BCD1FA5C0CB808B73349D5F16A0117DBDCDDA880B9E3A2A39DB`
- **Sidecar SHA-256 at v2 candidate review:** `DD9C9987B414113BE2899BAD3FF91FAE4A1A9B414D419255DB24585218860110`
- **Reviewed v2 prompt body SHA-256:** `C810F93AEE94E28A1F0460404F0CAB60B1DE26F5A849673F32DFE870B1FCC833`
- **Source:** `assets/ponchi/final/J-15.webp`, actual SHA-256 `B0025952EA39352D278251907AFB3B87B5D3BBFCCFF5F72482E8F07964386B74`, 1254×627 RGB; matches sidecar.
- **Character A reference:** `assets/ponchi/references/character-a-reader-woman.png`, actual SHA-256 `18E2B7E216BF76CD382002CA4E6CAF20EF175332E28EC7B6AB0E5EBC2AF7DDF0`, 320×420 RGB; matches sidecar and the sole visible engineer.

## Findings

- **Meaning and 200px readability — PARTIAL.** The image-to-language direction and separate text-token input are recognizable at 200×100, and a blank output bubble remains. The engineer is the only character and the source robot is gone. However, the visual flow still contains a second full-sized copy of the input landscape, divided into a dense patch grid, before a separate encoder tile. The encoder and LLM are also drawn as repeated multi-row box/node diagrams rather than the v2 prompt’s compact encoder with a few patches and one plain LLM block. These preserve the duplicate-image/patch-grid and layer-diagram complexity the sidecar says to remove. The overall meaning survives, but it is not yet the approved simplified flow.
- **Character and brand — PASS.** Character A’s bobbed hair, dark jacket, face, and laptop-side pose match the approved Reader-woman reference. There is no second person or robot, readable label, logo, logo-like mark, or branded UI. `LOGO_MODE` is `not_required`; no ROI is reserved.
- **Text-free and simplification — HOLD.** The final response bubble is empty, resolving v1’s three pseudo-text strokes. The added blank bubble beside the engineer is an extra input cue beyond the single requested text-token row and final output bubble; simplify it away or clearly keep the text-token row as the sole input representation. The encoder and LLM’s repeated cells, dots, and row structure remain visible at thumbnail size and conflict with “few patches” / “plain LLM block.”
- **Series style — PARTIAL.** The approved navy/black/pale-blue editorial linework and the existing landscape input are retained. The diagrams remain too detailed and panel-like for the required simplified treatment.
- **Machine audits — mixed; background gate FAIL.** `image_audit_v2.md` reports bbox `0.635` and status `pass`. `color_audit_v2.md` reports palette status `pass` with off-palette ratio `0.006681`. The item has no logo ROI; any default clearspace field is not applicable to its `not_required` logo policy. `background_samples_v2.md/csv` reports opaque RGB, exact-white corners `0/4`, registered points `3/12`, and exact-white pixels in the 3% perimeter `39059/184094`; verdict `HOLD_fail_fast`. No background mask was created because fail-fast checks failed.

## Gate

Keep v2 on HOLD. The v1 pseudo-text strokes are removed and basic image→language meaning remains, but the duplicate full-image patch grid and dense encoder/LLM diagrams violate the approved simplification. Exact-white also fails the item-local v2 perimeter audit. No promotion/adoption decision is made.
