# J-15 v2 independent prompt review

- Reviewer: `/root/review_wave001_c` (independent of prompt author)
- Review date: 2026-09-28
- Verdict: **PASS** for prompt content; candidate image gates remain separate.
- Sidecar SHA-256: `c027ddb772b339caac3ea9aabab10778e63dae1670c32eb981b439d085013bdc`
- Exact v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `c810f93aee94e28a1f0460404f0cab60b1de26f5a849673f32dfe870b1fcc833`

## Inputs and source meaning

- Source `assets/ponchi/final/J-15.webp`: actual SHA-256 `b0025952ea39352d278251907afb3b87b5d3bbfccff5f72482e8f07964386b74`; matches sidecar and prompt and remains read-only.
- Character A reference `assets/ponchi/references/character-a-reader-woman.png`: actual SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0`; matches sidecar and prompt.
- Human brief `content/entries/term_general/J-15_vlm[済].md` calls for the image → visual encoder/embedding → LLM → text-response flow. V2 retains one image input, one compact encoder, one visual embedding sequence joining separate text tokens before one LLM, and one blank response-bubble outline, with one Character A engineer and no robot.
- Candidate v1 review accepts meaning, 200px flow, Character A, palette, and logo avoidance; it identifies pseudo-text strokes in the response bubble, bbox `0.497` just below the `0.50` threshold, and strict-white failures. V2 addresses each by blanking the bubble, enlarging/reflowing only existing approved elements to a stated bbox target, and specifying exact-white points.

## Acceptance review

- The prompt explicitly preserves image-to-language direction and the difference between visual embeddings and text-token input; it removes all marks inside the output bubble and prohibits extra stages/cards. It keeps exactly one approved Character A and no extra person/robot.
- `LOGO_MODE: not_required` remains correct; no logo or blank clearspace is introduced. Product marks and pseudo-text are prohibited.
- It restricts color to the approved palette and reference-only neutral clothing colors, requires exact-white corners and all 12 registered perimeter samples with a blank 3% perimeter, and makes any sample failure a stop/HOLD. Post-generation whitening or recoloring is prohibited.
- The bbox change uses only already-required objects, preventing decorative inflation. The internal experiment output path and no-promotion boundary are explicit.

## Gate status

`J-15_candidate_v2.png` was absent at review time. Prompt content is **PASS**; keep generation blocked until the independent PASS is reconciled in the applicable gate/ledger. Candidate v1 remains HOLD pending candidate-side review of all prior image failures.
