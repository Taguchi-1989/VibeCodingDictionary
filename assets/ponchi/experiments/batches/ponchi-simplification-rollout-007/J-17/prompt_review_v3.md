# J-17 v3 prompt independent review

- **Verdict:** PASS
- **Reviewer:** `/root/review_wave001_b`
- **Date:** 2026-09-28
- **Sidecar SHA-256 (raw file):** `5DBE0B127AC97E7337181B5FDAB4499E469E9AF85EF0B6B33141ACA8B314478C`
- **Exact v3 prompt body SHA-256 (UTF-8/LF, excluding fences and terminal newline):** `E56D9F77D8AF5B4C8ECB8F42310A4C8CBE0546F4CB820FE80ABE7377869CA992`

## Evidence

- Source `assets/ponchi/final/J-17.webp`: actual SHA-256 `241BAC1B908021FF04ECC06E7E67E62112118E1857AB4D85C7B1E74B0C1132F9`, 1254×627 RGB; matches the v3 prompt and sidecar.
- Character A reference `assets/ponchi/references/character-a-reader-woman.png`: actual SHA-256 `18E2B7E216BF76CD382002CA4E6CAF20EF175332E28EC7B6AB0E5EBC2AF7DDF0`, 320×420 RGB; matches.
- The human brief `content/entries/term_general/J-17_attention[済].md` and figure memo specify `今日 / の / 天気 / は / ？`, with `天気` selected, two thin arrows to `今日` and `は`, and two thick arrows to itself and `？`. The v2 independent review accepted exactly this arrangement and Character A outside the diagram; v3 preserves the order, arrow direction/count/weight/self-loop, and no-text intent.
- Logo matrix row J-17 (`docs/ponchi_logo_requirement_matrix_2026-06-01.md:294`) is `not_needed` / `logo_avoid`; no logo or ROI is needed or introduced.
- v3 directly addresses both open v2 gates: it keeps all ink within a blank 3% perimeter and enlarges the observer/diagram together to a usable bbox target of at least half the canvas, without adding detail. It preserves separation and forbids extra rows, legends, labels, or stages.
- Exact 2:1, opaque uniform `#FFFFFF`, all corners and eight registered points, no background effects or postprocessing, fail-fast stop, and conditional same-size independently reviewed mask are explicit. The palette, attached approved character reference, and internal-only output restriction remain.
- Attempt limit is clear: v3 is final corrective revision 2/2; generation is blocked until independent prompt PASS, and failure of v3 ends the entry.

## Decision

PASS for one internal v3 candidate generation. Source/reference provenance and human-authored token/arrow semantics reconcile; the remaining density, perimeter, strict-white, and full-mask checks stay mandatory candidate gates. This prompt PASS does not approve the candidate image or production adoption.
