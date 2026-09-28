# H-57 candidate v3 prompt independent review

- **Verdict:** PASS
- **Reviewer:** `/root/review_wave001_b/review_prompt_v3_a`
- **Date:** 2026-09-28
- **Scope:** Prompt review only. Candidate generation and image review remain separate gates.
- **Whole sidecar SHA-256 (raw bytes):** `2C43CA2ABF95E2D0EF7A52EF29B459C540725E574E5F93C6772ACA899CA51D42`
- **Exact v3 prompt-body SHA-256 (UTF-8, LF-normalized; Markdown fence excluded):** `3DF3A73DB5AF9646F9AAF5ED423BD06A746E922B281C3852944B30E8E33CF4B6`

## Evidence

- **Source and reference — PASS.** The exact logo-free Batch 014 source `assets/ponchi/experiments/batches/ponchi-batch-014/H-57_base_1254x627.png` is SHA-256 `FA22A75414D2DF28E4E7019F5133C3920677701D1D3FD27D6D27CDCE0F150B56`, 1254×627 RGB. The actual Character B reference `assets/ponchi/references/character-b-teacher-man.png` is `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB. Both match sidecar/v3. The current final is explicitly excluded because it bears the Gemini mark.
- **Official asset and logo policy — PASS.** The recorded official Gemini sparkle `assets/logos/gemini/gemini_sparkle_4g_512_lt.png` is SHA-256 `5E7CFECAA53F4F65A313FE89B0F389548126544A78FAD8489510C70AE641A4A1` (512×512 RGBA); its source/retrieval metadata is in the sidecar. Use conditions remain pending, so `internal_base_only` is appropriate. The prompt forbids the mark and lookalikes, says the blank reservation does not authorize use, and excludes the logo-bearing final as input.
- **Human meaning and v2 findings — PASS.** The human brief describes five chronological generation nodes and subordinate within-generation variants, with three confirmed Ultra/Pro/Nano variants only for the first generation. The v2 review held because all later generations appeared to have three members, the illustration entered the reserved ROI, the canvas was underfilled, and strict-white checks failed. v3 retains exactly five equal-level nodes, exactly three chips only under the first, count-neutral open brackets beneath later nodes, one observer, and enlarges/spreads the timeline to a >=0.50 useful-content target without decorative fill.
- **Reserved ROI — PASS.** The full source reservation `[966,16,240,240]` and its corresponding upper-right area on the generated canvas are required blank, with no nodes, family cues, lines, or observer parts. No Gemini mark is to be drawn or attached. The sidecar records the 1774×887 mapped reservation as approximately `[1366,22,341,341]`.
- **Background and revision boundary — PASS.** The prompt requires an opaque exact-white 2:1 canvas, exact-white corners, eight registered points, full reserved rectangle, and blank 3% perimeter. Any fail-fast failure is HOLD; no post-processing is permitted. A same-size mask follows only after successful fail-fast checks; the sidecar's v1.3 gate requires complete-background pixel verification and independent contour review. This is final corrective revision 2/2 and says stop on failure.
- **Production boundary — PASS.** Output remains in the experiments folder; no overlay, promotion, adoption, publication, or release.

## Acceptance criteria

| Criterion | Status | Evidence |
|---|---|---|
| Exact logo-free source and Character B reference | VERIFIED | Actual hashes and dimensions match sidecar/v3. |
| Five generations vs subordinate variants | VERIFIED | First group has exactly three; later groups are count-neutral brackets. |
| v2 size, unsupported-count, and reserved-area findings | VERIFIED | >=0.50 occupancy goal; no later count assertion; full mapped ROI blank. |
| Official Gemini asset policy | VERIFIED | Asset provenance reconciles; pending use conditions keep prompt internal-only and logo-free. |
| v1.3 strict-white and attempt limits | VERIFIED | Exact-white fail-fast/full-mask sidecar gate/no post-processing; final 2/2 stop rule. |

## Decision

PASS for the v3 prompt. This does not approve a generated candidate or waive independent semantic, palette, ROI, or full-background-mask review.
