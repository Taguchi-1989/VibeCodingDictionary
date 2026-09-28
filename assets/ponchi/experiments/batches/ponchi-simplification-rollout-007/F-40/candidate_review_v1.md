# F-40 candidate v1 independent review

- **Verdict:** HOLD
- **Reviewer:** `/root/review_wave001_c` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `F-40_candidate_v1.png`, 1774×887 RGB
- **Candidate SHA-256:** `199519e768f599b0088098c3ec800008ca93ecbb19aca848d640360dd5696708`
- **Sidecar:** `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/F-40.md`
- **Sidecar SHA-256:** `4632320b877dd3fbde41651d3576955784e158d32e1b73cbbd1480f3049cddff`
- **Edit source:** `assets/ponchi/experiments/batches/ponchi-batch-009/F-40_base_1254x627.png`, SHA-256 `6b1d4f17a4ceeabf80e22c2c21db3f568f134a49b7d3db093ef163e9f15c6317` (logo-free base; visually inspected)
- **Character reference:** `assets/ponchi/references/character-b-teacher-man.png`, SHA-256 `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99` (visually inspected; the candidate depicts one matching Character B)
- **Official npm asset:** `assets/logos/npm/npm-logo-black.svg`, SHA-256 `847b92b289131097faf97e556d4a546c21fb96f0b85f57b8c9ac78106f49d07d` (verified asset recorded by the sidecar; not an edit input)

## Findings

- **Meaning and thumbnail readability — PARTIAL PASS.** The large left-to-right sequence of a dependency document, incoming packages, project store, and terminal/script is recognizable at small display size. It conveys package acquisition and use without readable words, code, service branding, or extra people. The registry is implied by packages entering a generic box rather than shown as an unmistakable source; acceptable for a text-free concept, though less explicit than the prompt. The installed store and running script remain distinct.
- **Character and brand constraints — PASS.** Exactly one Character B is present and visually matches the supplied reference. No npm logo, wordmark, logo-like placeholder, or other identifiable product mark is visible. The candidate remains an internal experiment.
- **No-pseudo-text constraint — FAIL.** The manifest contains four pale-blue rounded horizontal strokes. They read as placeholder text lines, contrary to the prompt's explicit prohibition on pseudo-text and request for empty square slots. Replace those strokes with a few empty square dependency slots; do not add labels or text.
- **Canvas and composition — PARTIAL.** The candidate is 1774×887 RGB (approximately 2:1) and meets the prompt's >=1500px long-edge target. Its primary workflow is simple and ordered. The image audit reports bbox coverage `0.430`, density `false`, status `review`; the body is concentrated in a narrow horizontal band with generous blank space. Recheck layout against the desired fuller, balanced occupancy before accepting.
- **Exact-white background and reserved logo ROI — FAIL.** The background/ROI audit reports all four corners fail exact `#FFFFFF`; only 1 of 8 registered points passes. RGBs: corners `(254,255,255)`, `(255,255,254)`, `(254,253,254)`, `(254,253,254)`; registered samples 1–8 are `(253,253,253)`, `(255,254,255)`, `(254,254,254)`, `(254,254,254)`, `(255,255,254)`, `(254,253,254)`, `(255,255,255)`, `(255,255,254)`. The mapped clearspace ROI `[970,0)–[1706,311)` contains `192951/228896` non-white pixels, all consistent with the near-white canvas; the image audit reports clearspace foreground ink `0.0000`, so no visible foreground intrusion is detected. The full-coverage/mask gate did not run because fail-fast point checks failed. Regenerate with opaque flat exact `#FFFFFF`, then rerun the full same-size mask audit.
- **Palette — mechanical pass only.** `color_audit_v1.md` reports `pass`, off-palette ratio `0.003048`. This does not override the exact-white failure.

## Gate

Keep candidate v1 on HOLD. A revision must replace the manifest strokes with empty square slots, achieve a balanced layout, and pass exact-white corner/sample plus full-mask checks including the reserved ROI. Do not post-process/paint the candidate to simulate compliance; do not promote, adopt, publish, or release it. This review records no generation authorization.
