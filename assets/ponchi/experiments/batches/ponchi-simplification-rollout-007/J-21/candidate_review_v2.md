# J-21 candidate v2 independent review

- **Verdict:** HOLD
- **Reviewer:** `/root/review_wave001_b` (independent visual review)
- **Date:** 2026-09-28
- **Candidate:** `J-21_candidate_v2.png`, 1774×887 RGB
- **Candidate SHA-256:** `A6B2F4833570D33E7E3B4AA4ED54243F2B4555A7BD17D8E75FA7F9B209EA8A55`
- **Sidecar SHA-256 at v2 candidate review:** `96A8BB930F1619AB2D7FA83F71920C9445A0E304E98017A71DBC82F84154F51C`
- **Reviewed v2 prompt body SHA-256:** `737F9AEC463FFA5AC93EE820E08B48D7D93F4428BEBA1657A7A30E54F99D1C68`
- **Source:** `assets/ponchi/final/J-21.webp`, actual SHA-256 `839F8AD76990C5F2272D825472D747DFC387EE4863B2BF4B29FF2BF1CB711DB5`, 1254×627 RGB; matches sidecar.
- **Character references:** None required; the sidecar and prompt explicitly prohibit people and robots.

## Findings

- **Meaning and 200px readability — visual PASS.** The two side-by-side states remain distinct at 200×100. The left shows a generic model with navy update marks distributed across its full node network; the right shows an unfilled/near-black outlined base with one lock and exactly one attached pale-blue adapter tile carrying the only active blue mark. Incoming training-data arrows feed both sides. The comparison reads as whole-model fine-tuning versus a frozen base with a separately trained adapter, without implying the base weights change.
- **Simplification and unwanted content — PASS.** The input document stacks have blank front pages, resolving the v1 pseudo-text risk. There is no readable text, fake UI, dashboard, repeated adapter, extra lock, company/model mark, person, or robot. The panel separator and simple node grids support the comparison rather than adding another workflow stage.
- **Palette and series style — PASS.** Flat navy, black, and pale-blue linework are consistent with the v1.3 series treatment. The frozen model is not filled gray; only its outlined nodes are shown. The single blue active marker is confined to the adapter tile.
- **Machine audits — mixed; background gate FAIL.** `image_audit_v2.md` reports bbox `0.699` and status `pass`; it also reports `clearspace required=true` and clearspace ink `0.0038`. The sidecar’s `LOGO_MODE` is `not_required` with no logo ROI, so that default clearspace measurement is not a brand-clearspace gate. `color_audit_v2.md` reports palette status `pass` with off-palette ratio `0.007242`. `background_samples_v2.md/csv` reports opaque RGB, exact-white corners `0/4`, registered points `2/12`, and exact-white pixels in the 3% perimeter `37495/184094`; verdict `HOLD_fail_fast`. No background mask was created because fail-fast checks failed.
- **Logo and background visual check.** No logo/brand mark is present and no logo ROI is required. The visible canvas looks white, but the exact-white v2 audit above fails; appearance does not override it.

## Gate

Keep v2 on HOLD because exact-white fails the v2 perimeter gate, despite the visual meaning/layout and geometry/palette audits passing. No promotion/adoption decision is made.
