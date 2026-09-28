# F-55 candidate v2 semantic review

- Verdict: **PASS**
- Review date: 2026-09-27
- Candidate: `F-55_candidate_v2.png`
- Candidate SHA-256: `C9A082F8F0814FE511AD4039C2D3F6ABB3CE56D98AAF869378C93A658948EFCA`
- Dimensions: 1774×887 (2:1); inspected full-size and at 200×100 px.
- Edit target check: candidate v1 SHA-256 is `B1077AA96E8CD964D661B33C8345691DC4FFA22D51FB7F075ACCC2762237EBD1`, matching the v1.2 prompt/revision input.
- Source checked: `content/entries/term_tool/F-55_merge[済].md`; original source SHA-256 in prompt matches `assets/ponchi/final/F-55.webp`.

## Findings

- The Before/After two-panel order is intact. Before shows two distinct commit-bearing branch lanes; After shows both converging once at a merge cue, with a single shared continuation. Core branch and merge meaning remains clear at 200 px.
- The same male character remains once per state, with the left confusion cue and right relieved cue intact. No third character or robot was added.
- Both gray chair-back props are removed; the character outlines, pose, expressions, and approved palette remain visually intact. No gray chair remains at full-size or thumbnail scale.
- No readable text, pseudo-text, logo, or branded mark is visible. No non-target structural change was apparent. A pixel comparison does show small edge/raster differences outside approximate chair regions (about 0.95% of all pixels at max-channel delta >25; about 0.09% at >100); these do not shift or alter any visible semantic element.
- The v2 file exists even though the prompt/revision preambles still say generation has not run; this is a status-text mismatch, not an image-semantic blocker.

