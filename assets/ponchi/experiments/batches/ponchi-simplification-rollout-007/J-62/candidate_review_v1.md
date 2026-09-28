# J-62 candidate v1 independent review

- Candidate: `J-62_candidate_v1.png`
- SHA-256: `A7D404E281D291F68F485F6FF40CA285B1F77CD55AD52261889039C7615650B8`
- Dimensions/mode: 1774×887 RGB.
- Verdict: **HOLD**. Keep internal; no promotion/adoption.

## Provenance and audit completeness

- Source `assets/ponchi/final/J-62.webp`: actual SHA-256 `32C751FC85AABD3ADF82BC6FE60896F5AD8A42E0D278ABC31F32C0EE9906739C`, 1254×627 RGB; matches the sidecar.
- Character A reference `assets/ponchi/references/character-a-reader-woman.png`: actual SHA-256 `18E2B7E216BF76CD382002CA4E6CAF20EF175332E28EC7B6AB0E5EBC2AF7DDF0`, 320×420 RGB; matches the sidecar.
- Character C reference `assets/ponchi/references/character-c-pet-robot.png`: actual SHA-256 `BE52EC9F31CCCCC881A164CABF3EB2FE0F7AE1196B04229866B7613D73D636FD`, 320×420 RGB; matches the sidecar.
- Image and color audit CSV/MD plus both contact sheets are present and readable in this folder. Image audit: bbox `0.778`, size pass, clearspace not required, status pass. Color audit: palette status pass, off-palette ratio `0.009880`.

## Independent visual review

- Reviewed the full candidate and an in-memory 200×100 preview. The judge on the left, full-height opaque partition, and two respondents to its right remain clear at thumbnail size. The partition separates the judge from both respondents; only small message slots interrupt it, and the judge has no direct sightline to either respondent.
- Character A is the sole judge and matches the approved black-bob/dark-jacket Reader-woman reference. Behind the partition there is one generic male respondent and one Character C robot. The robot's white rectangular head, black eyes, blue side accents, and blue antenna match the approved reference; no second fixed character or extra robot/person appears.
- A tablet and two parallel, dashed written-message routes communicate the question to the respondents; two separate return routes/cards communicate their replies. Cards are blank apart from a generic blue dot. There are no speech balloons, oral cues, readable words, logos, product branding, or apparent pseudo-text.
- HOLD — the drawing appears to show three cards per respondent route: one on the judge side of the wall, another on the respondent side, and one reply card returning. This makes six cards in total and can read as duplicate question cards, while the sidecar explicitly calls for one matching question per route, two replies, and removal of duplicate cards. At 200px the duplication is still visible; simplify to the intended question/reply count.
- The flat black/navy/pale-blue linework and simple figure drawing fit the existing series style. The generic desks/tablets do not resemble branded product UI.

## Background and logo gates

- The sidecar sets `LOGO_MODE: not_required` and both `LOGO_RECT` and `LOGO_CLEARSPACE_RECT` to none; no brand/logo ROI is required. The local image-audit policy records `logo_avoid`.
- Exact-white fails all four canvas corners: TL `(253,255,255)`, TR `(254,255,254)`, BL `(253,253,253)`, BR `(253,253,253)`. The registered 12-point CSV has only 2/12 exact-white samples. No background mask is present; fail-fast background checks remain HOLD, with no mask or white-paint postprocessing.

## Final decision

**HOLD** for exact-white failure and apparent duplicate question cards. Core Turing-test meaning, visibility wall, respondent identities, written-message treatment, no-text/no-logo constraints, dimensions, style, and palette audit are otherwise acceptable for internal review.
