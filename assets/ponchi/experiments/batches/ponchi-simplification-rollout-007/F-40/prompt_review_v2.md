# F-40 candidate v2 independent prompt review

- **Verdict:** PASS
- **Reviewer:** `/root/review_wave001_b` (independent prompt review)
- **Date:** 2026-09-28
- **Reviewed block:** the single fenced text block under “F-40 candidate v2 prompt — corrective revision 1 of 2”
- **Sidecar SHA-256:** `C8BA65B932D0E55C14165110B8C1B5D43862C429C222986F51586DC5D8B04FDE`
- **Exact prompt-body SHA-256:** `67FBA5EC2CF102C7BA986BACC27804F60C9D088C1A2C94798C3D4CAC05E96485` (UTF-8, LF normalized, excluding the fence lines and terminal newline)
- **Edit source:** `assets/ponchi/experiments/batches/ponchi-batch-009/F-40_base_1254x627.png`, SHA-256 `6B1D4F17A4CEEABF80E22C2C21DB3F568F134A49B7D3DB093EF163E9F15C6317`, 1254×627 RGB; current file matches sidecar.
- **Character reference:** `assets/ponchi/references/character-b-teacher-man.png`, SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB; current file matches sidecar.
- **Official npm asset:** `assets/logos/npm/npm-logo-black.svg`, SHA-256 `847B92B289131097FAF97E556D4A546C21FB96F0B85F57B8C9AC78106F49D07D`; present in the brand record and explicitly excluded as an image input. Current logo-bearing final `assets/ponchi/final/F-40.webp` is also excluded.

## Findings

- **V1 findings addressed.** The four pale-blue pseudo-text strokes are replaced with empty square dependency slots. The approved sequence remains manifest → generic registry/source packages → distinct project store → project-script run cue. The prompt preserves exactly one Character B at the terminal and adds no stage or unrelated detail.
- **Composition correction is measurable.** It directly requires primary-content bbox coverage of at least `0.50` and says to meet it only by enlarging/rearranging the approved forms and the existing Character B. This addresses v1’s `0.430` bbox without encouraging invented content.
- **Brand and clearspace are precise.** `internal_base_only`; no npm artwork or logo-like wordmark; source reservation `[686,0,520,220]` maps at 1774×887 to half-open ROI `[970,0,1706,311)`. All forms and other content are prohibited from entering it. This addresses v1’s ROI/background failure while preserving the existing source’s meaning.
- **Template and output constraints are consistent.** One opaque 2:1 PNG; exact RGB `#FFFFFF` blank canvas and reserved ROI; approved navy/black/pale-blue palette plus existing Character B neutral grays; no pseudo-text, texture, glow, or post-generation whitening/recoloring. The output is explicitly internal at the planned F-40 candidate v2 path.
- **Provenance and remaining audit gate.** Sidecar paths and actual source/reference hashes reconcile. The prompt requires the hashed Batch 009 base and the actual second Character B image input. The sidecar records the eight fail-fast sample coordinates and pending same-size 1-bit mask; v1.3’s full-mask and independent-contour checks remain mandatory post-generation acceptance gates. Their absence from the generation block does not weaken or replace those recorded audit gates.

No prompt-level blocker remains. This PASS reviews prompt readiness only; it does not approve or review a generated candidate.
