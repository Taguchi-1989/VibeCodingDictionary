# J-15 v3 prompt independent review

- **Verdict:** PASS
- **Reviewer:** `/root/review_wave001_b`
- **Date:** 2026-09-28
- **Sidecar SHA-256 (raw file):** `CAA3D0E98C2C86F98D525B5FE9D36C31D4E09509D87A385546C9EF6D42535597`
- **Exact v3 prompt body SHA-256 (UTF-8/LF, excluding fences and terminal newline):** `FFCDE6E47AF48ED1E919A5CEFA8284E5B37299D8E77CF3624D515440724FB861`

## Evidence

- Source `assets/ponchi/final/J-15.webp`: actual SHA-256 `B0025952EA39352D278251907AFB3B87B5D3BBFCCFF5F72482E8F07964386B74`, 1254×627 RGB; matches the prompt and sidecar.
- Character A reference `assets/ponchi/references/character-a-reader-woman.png`: actual SHA-256 `18E2B7E216BF76CD382002CA4E6CAF20EF175332E28EC7B6AB0E5EBC2AF7DDF0`, 320×420 RGB; matches.
- Human-authored VLM article describes image input → image encoder/embedding, joined with text tokens before an LLM → text response, with one female engineer in the figure memo. The sidecar's human review explicitly removes the source robot and fixes one Character A engineer; v3 follows that confirmed instruction.
- Logo matrix row J-15 (`docs/ponchi_logo_requirement_matrix_2026-06-01.md:292`) is `not_needed` / `logo_avoid`; v3 does not reserve an ROI or introduce product branding.
- v3 resolves v1/v2 findings: it specifies one small image tile, three encoder patches, three image-embedding tiles, a separate three-tile text row joining before one plain LLM block, one empty response bubble, and one Character A. It removes the duplicate landscape/grid, extra bubbles/robot, detailed encoder/LLM diagrams, and pseudo-text. It raises the primary-content bbox target to ≥0.50 while keeping 200px readability.
- Exact 2:1, opaque uniform `#FFFFFF`, exact-white corners/12 registered points/3% perimeter, no postprocessing, fail-fast stop, and same-size-mask creation/review only after all fail-fast points pass are explicit. The approved palette and internal-only output gate remain. Revision 2/2 is identified as final; failed mandatory checks stop the attempt.
- The v1.3 template's separate post-generation full-mask/background and candidate gates remain applicable; this prompt does not claim an image candidate already passes them.

## Decision

PASS for one internal v3 candidate generation. The v1/v2 semantic and simplification findings are covered, and source/reference provenance, logo handling, background instructions, and the two-revision stop limit reconcile. This prompt PASS is not a candidate-image or production-adoption PASS.
