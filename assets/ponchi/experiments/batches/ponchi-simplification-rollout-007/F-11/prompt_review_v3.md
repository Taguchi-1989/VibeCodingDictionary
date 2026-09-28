# F-11 candidate v3 prompt independent review

- **Verdict:** PASS
- **Reviewer:** `/root/review_wave001_b/review_prompt_v3_a`
- **Date:** 2026-09-28
- **Scope:** Prompt review only. This does not itself reconcile the batch generation gate.
- **Whole sidecar SHA-256 (raw bytes):** `5495FC04AD640DD314B0E725F97CE226BA0B85625313BA84EB301CFE05ABB141`
- **Exact v3 prompt-body SHA-256 (UTF-8, LF-normalized; fence excluded):** `54DE2A53B1EB41839283BA708C2E408F04FE6F2A180319C5C09EAB73A639CD4D`

## Evidence

- **Input provenance — PASS.** The prompt source `assets/ponchi/experiments/batches/ponchi-batch-008/F-11_base_1254x627.png` is SHA-256 `0EEE682C4E8035C9755336E22827E345AE32528325E4D8F616B06A79A11DDBA1`, 1254×627 RGB; it matches the sidecar and prompt. The actual Character A reference `assets/ponchi/references/character-a-reader-woman.png` is SHA-256 `18E2B7E216BF76CD382002CA4E6CAF20EF175332E28EC7B6AB0E5EBC2AF7DDF0`, 320×420 RGB, also matching. The recorded official Next.js lockup hash `603D77738F767D2AFA37E225DA1407DBDB2CD92E76695F010316910AE1E88761` matches the local asset; the prompt excludes both Next.js/Vercel marks and the logo-bearing final from inputs.
- **Human meaning and v1/v2 findings — PASS.** The central umbrella retains four distinct concepts and one observing Character A outside. The generic component panes replace the React mark; hosting/cloud cues are excluded; server is one plain box; browser/header dots, server indicators, repeated rows, micro-controls and decorative marks are expressly removed. The prompt addresses v2's reported 0.436 bbox by requiring at least 0.50 through scaling/spreading approved forms only.
- **Brand and ROI — PASS.** `internal_base_only` remains logo-free. The exact reserved source rectangle and 1774×887 mapped ROI are specified empty; no canopy, reader, arrows, forms, or shadows may enter it. No official logo is used or composited and output remains experiment-only.
- **Template/background and attempt gate — PASS.** Opaque exact 2:1, exact-white corners/eight registered points/ROI/perimeter, no tint or post-processing, fail-fast checks, and a same-size independently reviewed mask after fail-fast success are explicit. These conditions align with the v1.3 template and sidecar's sample/mask records. It is final corrective revision 2/2 and directs a stop/HOLD on any mandatory failure.

## Acceptance criteria

| Criterion | Status | Evidence |
|---|---|---|
| Exact logo-free source and Character A reference | VERIFIED | Actual source/reference hashes and dimensions match sidecar/v3. |
| Four Next.js concepts and observer relationship | VERIFIED | Four named forms remain under one canopy; one observer remains outside and looks toward diagram. |
| v1/v2 brand, hosting, micro-UI, and size findings | VERIFIED | React/cloud excluded; dots, repeated server rows, UI details removed; bbox target >=0.50. |
| Official mark policy and reserved ROI | VERIFIED | Internal-only, exact empty mapped ROI, no logo input/drawing/composite. |
| v1.3 background and attempt constraints | VERIFIED | Exact-white fail-fast and independent mask gate; no post-processing; final 2/2 stop rule. |

## Decision

PASS for the v3 prompt. Candidate generation remains subject to the separate batch gate and subsequent candidate, image, color, ROI, and background-mask reviews.
