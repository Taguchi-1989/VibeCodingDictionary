# G-47 candidate v2 independent review

- Reviewer: `/root/review_wave001_b/review_g47_h57_v2` (independent visual review)
- Review date: 2026-09-28
- Verdict: **HOLD** — keep this candidate internal; no promotion or adoption.
- Candidate: `G-47_candidate_v2.png`
- Candidate SHA-256: `C217EB8CA52D1D964508E030E1E540281EA2A96620032B0BB4C21ECC6171E64C`
- Dimensions/mode: 1774×887 RGB
- Current sidecar SHA-256: `00871F2706EFA5765C2018FAB00F412619865653FD15AD083BB76FBE06E9DBC0`
- Current v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `9886d8af57fe49a5bb14dae87bfb532a52aa47838411227ff21414cc396d089e`; matches the body hash in the v2 prompt PASS record.

## Inputs and brief alignment

- Logo-free source `assets/ponchi/experiments/batches/ponchi-batch-013/G-47_base_1254x627.png`: actual SHA-256 `D73CAA0F0E5EE1F935697E650A4436EA33ECCE405F221D206310E9A03B26146A`; 1254×627 RGB; matches the sidecar and approved v2 prompt.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`; 320×420 RGB; matches the sidecar and approved v2 prompt.
- The human brief `content/entries/term_llm/G-47_auto_compact[済].md` describes a long conversation being compressed into a shorter digest and continued work. The v1 review held for pseudo-text bars, forked follow-up arrows, and non-white background. The v2 prompt body remains the independently reviewed body and directly targeted those findings.

## Visual review at 200×100

- **Meaning and sequence — PASS.** The stacked conversation converges through one central compaction symbol to one summary card and two serial follow-up messages. The continuation reads as a single flow; there is no parallel branch.
- **Character identity/count — PASS.** One engineer appears at lower left. His hair, clothing, seated laptop pose, and thoughtful hand position are consistent with the approved Character B reference. No second person or robot is visible.
- **Logo avoidance and series treatment — PASS.** No Claude Code/Anthropic mark, product UI, readable words, or recognizable logo is visible. The clean navy, light-blue, charcoal, and neutral-gray line style is consistent with the series and remains readable at 200×100.
- **Text-free simplification — HOLD.** Each of the six left-side message cards still contains one prominent blue dot aligned like a bullet/list marker. At 200×100 these read as repeated UI/pseudo-text marks, despite the v2 prompt explicitly prohibiting any dot that could read as pseudo-text. This is a residual version of the v1 text-like-row issue.

## Machine evidence and gates

- `image_audit_v2.csv` / `.md`: bbox coverage `0.576`, `density_ok=true`, `clearspace_required=false`, clearspace ink ratio `0.0000`, `clearspace_ok=true`, status `pass`.
- `color_audit_v2.csv` / `.md`: off-palette ratio `0.002283`, status `pass`.
- `background_samples_v2.md`: exact-white corners `0/4`; exact-white registered points `1/8`; exact-white 3% perimeter pixels `48,913/184,094`; background-mask status `not_created_fail_fast`; verdict `HOLD_fail_fast`. Do not infer a mask result or whiten the image after generation.

## Final decision

**HOLD** for the repeated bullet-like dots and strict-white background failure. The main flow, single-character identity, logo avoidance, and v2 palette/image-audit checks are acceptable, but the candidate does not meet its text-free prompt or background gate. Keep v2 internal and request a targeted revision that removes every marker inside the message cards and passes the fail-fast white checks before any later gate.
