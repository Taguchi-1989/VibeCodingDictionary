# J-1 candidate v1 independent review

- Candidate: `J-1_candidate_v1.png`
- SHA-256: `96CCD1CF259DFDEFCE18114917BB1F811775DB08EB24DB4C511D648BCC6DDAAA`
- Dimensions/mode: 1774×887 RGB.
- Verdict: **HOLD**. Keep internal; no promotion/adoption.

## Provenance and machine audits

- Source `assets/ponchi/final/J-1.webp`: actual SHA-256 `87E93C2CB304EF4063C7BDD866DD615FB80BA56033D7D4298634EB992BD2AAC7`, 1254×627 RGB; matches sidecar.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB; matches sidecar.
- Character C reference `assets/ponchi/references/character-c-pet-robot.png`: actual SHA-256 `BE52EC9F31CCCCC881A164CABF3EB2FE0F7AE1196B04229866B7613D73D636FD`, 320×420 RGB; matches sidecar.
- Machine image audit and contact sheet are present/readable: bbox `0.710`, dimensions pass, logo clearspace not required, status pass. Color audit and contact sheet are present/readable: palette pass, off-palette ratio `0.008994`.

## Independent visual review

- Reviewed the full canvas and an in-memory 200×100 preview. The required left-to-right order is clear: one vision-specialist Character C robot at far left; a second depiction of the same Character C design in the middle within a dashed hypothetical boundary; one Character B researcher at far right. The researcher is not between the robots. Both robots retain the same white rectangular head/body, round black eyes, blue side accents, and blue antenna; poses differ, but the series identity is consistent.
- The left robot has one generic image cue. The middle robot has three broad cues: a head/brain icon, a folded document with horizontal pseudo-text bars, and a planning/flowchart glyph. The dashed enclosure clearly presents this AGI depiction as hypothetical, not achieved. The far-right researcher matches Character B and the open-ended dashed measuring frame suggests an unresolved boundary.
- HOLD — the middle capability set lacks a clear visual-perception cue: its three cues read as brain/reasoning, document/text, and planning. The left image cue communicates the specialist's narrow vision task, but does not clearly represent visual perception among the hypothetical system's broad capabilities.
- HOLD — an explicit brain graphic remains inside the middle head silhouette, despite the sidecar's “no brain icon” instruction.
- HOLD — the document icon contains several horizontal bars that read as fake text/pseudo-text at full size and as text-like marks in the 200px preview; the sidecar prohibits pseudo-text.
- HOLD — a large `?` appears beside the researcher's measuring frame. The boundary is correctly unresolved, but this visible punctuation is unrequested and conflicts with the text/symbol-free direction.
- The image is otherwise clean, flat black/navy/pale-blue linework in the series style. No extra people/robots, logos, product marks, score, numeric scale, or identifiable branded UI were observed.

## Background and logo gates

- Sidecar `LOGO_MODE: not_required`; `LOGO_RECT` and `LOGO_CLEARSPACE_RECT` are none. No logo ROI is required; the local image audit policy records `logo_avoid`.
- Exact-white fails all four corners: TL `(254,255,255)`, TR `(254,255,254)`, BL `(253,253,253)`, BR `(253,253,253)`. The registered 12-point sample CSV has only 2/12 exact-white points. No background mask is present; fail-fast background checks remain HOLD. Do not add a mask or white-paint postprocessing.

## Final decision

**HOLD** for exact-white failure, the remaining brain icon, pseudo-text, visible question mark, and missing clear visual-perception cue in the hypothetical capability group. The required subject order, repeated Character C identity, researcher placement, dashed hypothetical treatment, overall meaning, style, dimensions, and palette audit are otherwise acceptable for internal review.
