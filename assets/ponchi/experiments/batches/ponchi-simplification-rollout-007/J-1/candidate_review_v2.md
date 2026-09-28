# J-1 candidate v2 independent review

- Reviewer: `/root/review_wave001_b/review_j1_v2` (independent candidate reviewer)
- Review date: 2026-09-28
- Candidate: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/J-1/J-1_candidate_v2.png`
- Candidate SHA-256: `0AB7DF2A0A4AFAAAD059AC8BF367B541E36D25FAAC984FA5C11C8F27C080A95F`
- Dimensions/mode: 1774×887 RGB; exact 2:1
- Verdict: **HOLD**. Keep internal; no promotion/adoption.

## Provenance and reviewed prompt

- Current sidecar `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/J-1.md` SHA-256: `C6781C64F413D1238E3C0717785086446B35279EC5EAAFA2740702F7BB9D8B23`.
- Exact current v2 prompt body SHA-256: `CFC08ED8E2D8E0217F8D97120694E8D7CB58F257CD3EDE5524F4C50BDD5EFA90`; it matches the body SHA recorded by the independent v2 prompt review.
- Source `assets/ponchi/final/J-1.webp`: actual SHA-256 `87E93C2CB304EF4063C7BDD866DD615FB80BA56033D7D4298634EB992BD2AAC7`, 1254×627 RGB; matches the sidecar.
- Character C reference `assets/ponchi/references/character-c-pet-robot.png`: actual SHA-256 `BE52EC9F31CCCC881A164CABF3EB2FE0F7AE1196B04229866B7613D73D636FD`, 320×420 RGB; matches the sidecar.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB; matches the sidecar.
- Compared with the J-1 human brief and v1 review: the central brain, document-like pseudo-text, and large question mark are absent; the middle group now has a distinct eye looking toward a framed scene as a visual-perception cue.

## Independent visual review

Reviewed the full-resolution candidate and an in-memory 200×100 preview.

- The required subject count and left-to-right sequence are clear: one Character C specialist robot at far left, a second depiction of that same Character C robot in the middle, and one Character B researcher at far right. The two robots retain the same recognizable head, antenna, eyes, and blue side modules. The researcher is beyond the middle group and is not between the robots.
- The dashed enclosure surrounds the middle hypothetical AGI group only. The image does not imply that AGI has been achieved. No extra people/robots, visible words, logos, or company/product marks were observed. The series-like editorial line style and the specialist-versus-generalist distinction remain recognizable at 200px.
- The middle group has three cues: a flowchart-like planning cue, the eye-and-scene visual-perception cue, and a simple path/node cue. The v1 brain, text-like document bars, and question-mark symbol are resolved.
- **HOLD — three large bordered, dashboard-like panels remain around the middle capability cues.** At native size, each cue is enclosed in a separate rectangular card connected to the robot. This reads as capability cards/fake interface and conflicts with the v2 prompt's prohibition on capability cards, fake interface, and extra panels. It also retains much of the card-heavy density that v1 was meant to simplify.
- **HOLD — the researcher still has a vertical measuring ruler with repeated graduation marks.** It is unnumbered, but the v2 prompt explicitly prohibits scale marks; this repeats a v1 concern about the oversized ruler and its ticks.
- **HOLD — the perimeter is not visually clear.** The horizontal baseline reaches into the outer edge margin on both sides, so the requested blank 3% perimeter is not maintained.

## Background and logo observations

- J-1 is `LOGO_MODE: not_required` with no reserved logo ROI. No logo or brand mark is visible.
- At native display size, the center inside the dashed enclosure appears faintly blue-tinted relative to the outer white canvas. This is a visual observation only; exact-white pixels, all registered sample points, and fail-fast background checks remain pending the root machine audit. I am not assigning a numeric background or palette result.
- No logo-clearspace/ROI machine checks or other image/color audits were run in this review. Root machine checks remain pending.

## Final decision

**HOLD** for the remaining capability-card/panel treatment, prohibited ruler scale marks, and nonblank outer perimeter. The prompt-v2 fixes to meaning and subjects are otherwise visibly present. Keep the candidate internal until those visible issues are corrected and the separate machine audit passes.
