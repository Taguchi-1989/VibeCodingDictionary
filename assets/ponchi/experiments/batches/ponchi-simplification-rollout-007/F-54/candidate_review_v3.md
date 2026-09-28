# F-54 candidate v3 independent review

- Candidate: `F-54_candidate_v3.png`
- SHA-256: `98028035DEBA796DD1A78DF20E2294424FDFDE8674AA15DD28FC009CB56A1482`
- Dimensions/mode: 1774×887 RGB.
- Verdict: **HOLD at strict-white background gate**. Keep internal; no promotion/adoption.

## Provenance and machine audits

- Source `assets/ponchi/final/F-54.webp`: actual SHA-256 `6CA239EE02C95AA820D9DDF0B5F81C498D3E76A758C02AEFC480BEFE64E17B8A`, 1254×627 RGB; matches sidecar.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB; matches sidecar.
- Image/color audit files and both v3 contact sheets are present and readable. Image audit: bbox `0.518`, native-size pass, no logo clearspace required, status pass. Tolerance color audit: pass, off-palette ratio `0.003708`.

## Meaning, layout, and series style

- Reviewed the full canvas and an in-memory 200×100 preview. Three distinct checkpoint nodes run left to right on one line; the middle is highlighted, and one curved arrow returns from the right node toward it. One calm Character B developer is at the right end. This clearly communicates an earlier local-history checkpoint available for return or inspection.
- The three nodes use the same blank file/snapshot glyph. No remote, push, merge, branch, extra arrow, extra person/robot, readable text, pseudo-text, product mark, or logo is visible. The Character B figure and clean flat navy/black/pale-blue linework match the established series style.
- The approved v3 exact-white prompt changes background treatment only; the candidate retains the previously reviewed meaning and layout.

## Strict-white and logo gates

- Background sample report: opaque RGB; exact-white corners `0/4`, registered points `4/8`, fail-fast `FAIL`.
- No same-size background mask was retained because the fail-fast checks failed. No white-paint post-processing was applied.
- Sidecar `LOGO_MODE: not_required`; `LOGO_RECT` and `LOGO_CLEARSPACE_RECT` are none. No logo ROI is required; image audit records clearspace as not required.

## Final decision

**HOLD** solely for strict-white background failure. Meaning, checkpoint sequence, return cue, Character B, no-logo constraints, dimensions, series style, and tolerance palette audit are otherwise acceptable for internal review. Candidate v3 is final revision 2/2; do not generate another candidate.
