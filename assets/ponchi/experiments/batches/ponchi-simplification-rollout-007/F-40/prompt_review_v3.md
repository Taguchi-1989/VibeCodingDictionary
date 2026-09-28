# F-40 v3 independent prompt review

- **Verdict:** PASS
- **Reviewer:** `/root/review_wave001_b` (independent re-review of the revised prompt)
- **Date:** 2026-09-28
- **Scope:** Prompt only; no candidate generated or changed.
- **Whole sidecar SHA-256 (raw bytes):** `9040E43704072FDD66BB6F0F6A53F39AE66C42B332D2435FD534E3C885EF077D`
- **Exact v3 prompt-body SHA-256 (UTF-8, LF-normalized; fences excluded):** `E945966C83AA0B1C720F6F74722729D06A3C47F2FF6237E6C82AF18BE0E91DBD`

## Evidence

- **Source and reference provenance — PASS.** The exact edit input `assets/ponchi/experiments/batches/ponchi-batch-009/F-40_base_1254x627.png` is SHA-256 `6B1D4F17A4CEEABF80E22C2C21DB3F568F134A49B7D3DB093EF163E9F15C6317`, 1254×627 RGB. The actual Character B reference `assets/ponchi/references/character-b-teacher-man.png` is `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB. Both match the sidecar and revised prompt; the prompt explicitly requires the reference as an actual image input. The recorded official npm SVG is present at the stated path with matching SHA `847B92B289131097FAF97E556D4A546C21FB96F0B85F57B8C9AC78106F49D07D`.
- **Meaning and v2 findings — PASS.** The prompt now specifies the approved order and arrows unambiguously: blank dependency manifest → generic package source/acquisition → project store receiving those same three package blocks → script run/output. It prohibits any source, package, or arrow before the manifest and caps the flow at three large package blocks. The single approved Character B is explicitly operating a blank generic terminal at the run cue, which resolves the prior role omission and agrees with the brief. No extra stages, text, pseudo-text, or npm mark are allowed.
- **Brand and reserved area — PASS.** The logo matrix and sidecar allow only `internal_base_only` for this new candidate. The prompt forbids attaching, drawing, imitating, or compositing npm branding and keeps the source clearspace `[686,0,520,220]` empty; its mapped half-open output ROI `[970,0,1706,311)` is explicitly protected from all content.
- **Template, output, and gates — PASS.** It requires the approved v1.3 palette/style, opaque 2:1 PNG, exact-white corners, eight registered points, full reserved ROI, and 3% perimeter. It prohibits postprocessing and requires fail-fast checks plus an independently reviewed same-size mask only after they pass. The planned output remains internal-only, final corrective revision 2/2, and generation is explicitly blocked pending independent PASS.

| Criterion | Status | Evidence |
|---|---|---|
| Exact source and Character B reference | VERIFIED | Fresh file hashes and dimensions above match sidecar/prompt. |
| Correct package flow and terminal role | VERIFIED | Manifest-first arrows, three package blocks, distinct store, script/output, and Character B operating terminal are explicit. |
| Logo policy and reserved clearspace | VERIFIED | `internal_base_only`; npm mark prohibited; mapped ROI explicitly empty. |
| v1.3 background/output and revision gates | VERIFIED | Corners/8 points/ROI/perimeter, fail-fast, independently reviewed mask, no postprocessing, internal-only, final 2/2. |

**Prompt-level result: PASS.** This review does not approve any generated candidate or production adoption; the wave ledger and all candidate-level gates remain separate.
