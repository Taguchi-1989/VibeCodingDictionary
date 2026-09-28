# G-47 candidate v3 prompt independent review

- **Verdict:** PASS
- **Reviewer:** `/root/review_wave001_b/review_prompt_v3_a`
- **Date:** 2026-09-28
- **Scope:** Prompt review only. Candidate generation and image review remain separate gates.
- **Whole sidecar SHA-256 (raw bytes):** `C924A005DCC97208840ECBAA9E96129002A764AB079B9B9C3F5868BA345C302E`
- **Exact v3 prompt-body SHA-256 (UTF-8, LF-normalized; Markdown fence excluded):** `14FC17C99AF6524FD96CBA55EECC1FF34F86B67618CC75F0D04DEF9CA54FA3AF`

## Evidence

- **Source and reference — PASS.** The exact Batch 013 logo-free base `assets/ponchi/experiments/batches/ponchi-batch-013/G-47_base_1254x627.png` is SHA-256 `D73CAA0F0E5EE1F935697E650A4436EA33ECCE405F221D206310E9A03B26146A`, 1254×627 RGB. The actual Character B reference `assets/ponchi/references/character-b-teacher-man.png` is `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB. Both match the sidecar and v3 prompt. Current final `G-47.webp` is read-only context and is not the edit input.
- **Human meaning and v2 findings — PASS.** The human brief and sidecar define long conversation → compaction → short digest → continued work, with one engineer. The v2 review found a blue bullet-like dot inside each of six cards; v3 leaves all six cards as outline and blank interior, prohibits every internal mark, preserves one convergence flow and two serial follow-ups, and retains one Character B. No threshold, command, product UI, or unsupported stage is introduced.
- **Brand/style — PASS.** The G-47 matrix row is `not_needed` / `logo_avoid`. The prompt prohibits product UI, logos/marks, Anthropic and Claude Code branding, and keeps the generic v1.3 series palette and one approved neutral-gray character.
- **Background and revision boundary — PASS.** The prompt calls for opaque 2:1, exact-white corners and all eight registered perimeter points, a blank 3% perimeter, and fail-fast HOLD on any failed point. It disallows repainting/post-processing and requires a same-size mask after successful fail-fast checks. This sidecar's v1.3/background instructions require the full-canvas mask check and independent contour review. v3 is correctly labeled final corrective revision 2/2 and says stop if it fails.
- **Production boundary — PASS.** Output is a new experiments candidate only; no overlay, final promotion, adoption, publication, or release.

## Acceptance criteria

| Criterion | Status | Evidence |
|---|---|---|
| Exact source and Character B reference | VERIFIED | Actual hashes and dimensions match sidecar/v3. |
| Human meaning, one engineer, single continuation flow | VERIFIED | v3 preserves long→compact→summary→two serial continuation forms and one approved character. |
| v2 bullet/pseudo-text finding | VERIFIED | Every conversation card is explicitly blank inside; all internal marks are prohibited. |
| Brand and output restrictions | VERIFIED | `logo_avoid`, no branded UI/marks, experiments-only output. |
| v1.3 strict-white and attempt limits | VERIFIED | Exact-white fail-fast, same-size mask gate/no post-processing; final 2/2 stop rule. |

## Decision

PASS for the v3 prompt. This does not approve a generated candidate or waive independent semantic, palette, ROI, or full-background-mask review.
