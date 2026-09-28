# G-47 candidate v3 independent review

- **Verdict:** HOLD — final corrective revision 2/2; no further generation.
- **Reviewer:** `/root/review_wave001_b` (independent visual review)
- **Date:** 2026-09-28
- **Candidate:** `G-47_candidate_v3.png`, 1774×887 RGB; exact 2:1 and long edge exceeds 1500px.
- **Candidate SHA-256:** `88A3567405F6E7FE9737F4B7B7BC592E56040237C07B92DC01536DAD1AFD15D5` (matches requested hash and local file)
- **Current sidecar SHA-256 (raw bytes):** `C924A005DCC97208840ECBAA9E96129002A764AB079B9B9C3F5868BA345C302E`
- **Exact current v3 prompt-body SHA-256 (UTF-8, LF-normalized; fences excluded):** `14FC17C99AF6524FD96CBA55EECC1FF34F86B67618CC75F0D04DEF9CA54FA3AF`

## Provenance

- Source `assets/ponchi/experiments/batches/ponchi-batch-013/G-47_base_1254x627.png`: actual SHA-256 `D73CAA0F0E5EE1F935697E650A4436EA33ECCE405F221D206310E9A03B26146A`, 1254×627 RGB; matches sidecar and current prompt.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB; matches sidecar and current prompt.
- Human brief: `content/entries/term_llm/G-47_auto_compact[済].md` describes a long conversation, automatic compression into a short digest, and continued work.

## Visual review at 200×100

- **Meaning and sequence — PASS.** Six blank message-card silhouettes at left converge through one central folding/compaction symbol. One card follows as the short summary, then two cards continue serially along the same left-to-right path. The main flow is singular; the two later cards do not branch. No numerical threshold or invented process stage is shown.
- **Character and series style — PASS.** One engineer appears once at lower left beside the conversation sequence. Hair, face, neutral gray clothing, laptop and thoughtful seated pose match approved Character B. Navy/black/pale-blue outlines and flat editorial treatment fit the series and remain understandable at thumbnail scale.
- **Text, marks, and brand — PASS.** All six input cards and all three output cards are visually empty at 200×100; the v2 bullet-like dots are gone. No readable or pseudo-text, list marks, product UI, Claude Code/Anthropic marks, logo, extra figure, robot or decorative rays are visible. G-47 is `not_required` / `logo_avoid`, so no logo-clearspace ROI is required.
- **Perimeter — HOLD.** The visible baseline/chair line at the far left begins around x=20px, inside the prompt's 3% left margin (about 53px at this output width). The registered background audit also fails: exact-white corners `1/4`, registered points `1/8`, and exact-white perimeter pixels `50,036/184,094`. The background report records fail-fast HOLD and no mask was created; no mask result or exact-white pass is claimed. Despite the canvas appearing white on screen, the machine RGB checks control.

## Machine evidence

- `background_samples_v3.md`: candidate SHA matches; strict-white `HOLD_fail_fast`, corners `1/4`, points `1/8`, perimeter `50,036/184,094`; mask `not_created_fail_fast`.
- `color_audit_v3.csv` / `.md`: palette audit `pass`, off-palette ratio `0.003453` (5,434/1,573,538 pixels). This tolerance audit does not override the exact-white failure.
- `image_audit_v3.csv` / `.md`: bbox `0.543`, status `review`, `size_ok=false`, `clearspace_required=true`, clearspace ink `0.0000`. The actual image is 1774×887 RGB, exact 2:1, and meets the prompt's ≥1500px long-edge target. The audit's `size_ok=false` is recorded without attributing a cause; its clearspace flag is not a brand gate because the matrix/sidecar require no logo ROI for G-47.

## Final decision

**HOLD** for the exact-white fail-fast failure and visible intrusion into the blank left perimeter. Meaning, 200px sequence, simplified blank cards, character identity, style and no-logo constraints pass visually. This is revision 2/2; retain the candidate internally and stop without regeneration, promotion or adoption.
