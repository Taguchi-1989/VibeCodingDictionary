# H-57 candidate v3 independent review

- **Verdict:** HOLD — final corrective revision 2/2; no further generation.
- **Reviewer:** `/root/review_wave001_b` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `H-57_candidate_v3.png`, 1774×887 RGB; exact 2:1 and long edge exceeds 1500px.
- **Candidate SHA-256:** `61FFC277FF7D5B8F5E04398579870C0D6EA485093EFA4003308A91353FB508AA`
- **Current sidecar SHA-256 (raw bytes):** `2C43CA2ABF95E2D0EF7A52EF29B459C540725E574E5F93C6772ACA899CA51D42`
- **Exact current v3 prompt-body SHA-256 (UTF-8, LF-normalized; fences excluded):** `3DF3A73DB5AF9646F9AAF5ED423BD06A746E922B281C3852944B30E8E33CF4B6`

## Provenance

- Source `assets/ponchi/experiments/batches/ponchi-batch-014/H-57_base_1254x627.png`: actual SHA-256 `FA22A75414D2DF28E4E7019F5133C3920677701D1D3FD27D6D27CDCE0F150B56`, 1254×627 RGB; matches the current prompt and sidecar.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB; matches prompt/sidecar.
- The human brief `content/entries/history/H-57_gemini_naming_history[人書].md` describes the five-generation timeline and confirms the Ultra/Pro/Nano family only for the first generation. The prompt's independent review record is PASS for the recorded sidecar/body SHA pair above.

## Visual review at 200×100

- **Timeline and count fidelity — PASS.** Five equal-level generation nodes read left-to-right. Only the first node has three visible variant chips; each later node has one count-neutral open bracket without repeated chips or circles. The timeline retains the requested chronological structure without labels or dates.
- **Observer and series style — PARTIAL.** One thoughtful Character B observer is outside the timeline at left and matches the approved reference. At thumbnail size he is nearly as tall as an individual generation panel, so he reads as a prominent figure rather than a small observer. The flat navy/black/pale-blue editorial treatment remains recognizable, though the repeated interior rows make the panels feel interface-like.
- **Text-free simplification — HOLD.** All five generation panels contain repeated dot-and-line rows and an adjacent filled rectangle. At 200×100 these read as list/form UI or pseudo-text and add the repeated detail prohibited by the v3 prompt. Three radiating strokes above the middle generation are additional decorative marks, also outside the prompt's simplification constraints. No readable text or actual labels are visible; the issue is the pseudo-UI appearance.
- **Logo/content — HOLD.** No Gemini sparkle, brand mark, readable model name, extra person, or robot is visible. However, the fifth generation panel and its timeline content enter the reserved upper-right logo-clearspace area, which the prompt requires to remain completely blank.
- **Exact-white perimeter and ROI — HOLD.** At full resolution the background looks near-white, but it fails the exact pixel gate. The left side also contains illustration close to the canvas edge. The dedicated audit for reserved ROI `[1365,22,1707,363)` reports only `18,524/116,622` exact-white pixels, so the reservation is substantially occupied. No background mask was created after fail-fast failure.

## Machine evidence

- `background_samples_v3.md`: candidate hash matches; exact-white corners `0/4`, registered points `1/8`, exact-white 3% perimeter `37,161/184,094`; reserved ROI exact-white `18,524/116,622`; mask `not_created_fail_fast`.
- `color_audit_v3.csv` / `.md`: status `review`, off-palette ratio `0.011575`. Do not treat it as a palette pass.
- `image_audit_v3.csv` / `.md`: bbox `0.609`, status `review`, `size_ok=false`, `clearspace_required=true`, clearspace ink ratio `0.0000`. The file itself is 1774×887 and exact 2:1; the size flag's cause is not inferred. The reported zero ink does not establish ROI compliance: the dedicated exact-white ROI audit finds only 18,524 white pixels out of 116,622.

## Final decision

**HOLD** for the mandatory exact-white/perimeter and reserved-ROI failures, plus repeated pseudo-UI rows and decorative rays. The five-node chronology, first-only three-member family, no-logo appearance, and observer identity are present. Keep internal; revision 2/2 is final, so do not regenerate, promote, or adopt.
