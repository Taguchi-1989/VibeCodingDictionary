# F-11 candidate v2 independent review

- **Verdict:** HOLD
- **Reviewer:** `/root/review_wave001_b/review_f11_v2`
- **Date:** 2026-09-28
- **Candidate:** `F-11_candidate_v2.png`, 1774×887 RGB
- **Candidate SHA-256:** `A2D8D930C32DAB42BF22035976187521FE38BB0B07BFE795A6234EE3C52F9186`
- **Prompt sidecar:** `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/F-11.md`
- **Prompt sidecar SHA-256:** `07A5F60F6279235E3A0B54485312A23892C37621E3A107E63EBC37CFBAAE5F01`
- **Edit source:** `assets/ponchi/experiments/batches/ponchi-batch-008/F-11_base_1254x627.png`, SHA-256 `0EEE682C4E8035C9755336E22827E345AE32528325E4D8F616B06A79A11DDBA1` (matches the sidecar; visually inspected)
- **Character reference:** `assets/ponchi/references/character-a-reader-woman.png`, SHA-256 `18E2B7E216BF76CD382002CA4E6CAF20EF175332E28EC7B6AB0E5EBC2AF7DDF0` (matches the sidecar; visually inspected)
- **Human brief:** `content/entries/term_tool/F-11_next_js[済].md`
- **Compared against:** the v2 prompt in the sidecar and `F-11/candidate_review_v1.md`.

## Findings

- **Meaning and layout — PASS.** At native size and an approximately 200px-wide preview, one central boundary groups four separate panels and the arrows give a clear left-to-right reading order. The forms read as a generic component/window, a branching route map, server processing, and deployment settings. This supports the human brief's Next.js umbrella relationship. No outside hosting provider is implied.
- **Simplification and prompt adherence — HOLD.** The server concept is drawn as three repeated server rows, while the reviewed v2 prompt asks for “one simple server box.” The component window retains three small header dots, and the server rows each have a dot-and-line indicator. Together these preserve the tiny repeated/UI-like details the v1 review flagged and the v2 prompt explicitly asked to remove. They remain visible at native size and as miniature marks at 200px. For the next attempt, use one plain server box and remove the header dots and repeated server indicators; keep only large blank forms needed to distinguish the four concepts.
- **Character — PASS with a minor role/readability note.** There is exactly one Character A figure outside the boundary, and her hairstyle, face, clothing, and laptop match the approved reference. Her pose reads as working at a laptop; the image does not strongly show her looking toward the diagram or asking what falls within the framework's responsibility. This is a small semantic weakness, not a second-character or identity problem.
- **Brand and text — PASS.** I see no Next.js, React, or Vercel logo/wordmark, branded screen, readable text, code, or external-hosting cue. The four symbols are generic. The unlabelled settings control stays inside the framework boundary.
- **Reserved ROI — visual PASS; machine check pending.** The mapped reserved area `[970,0,1706,255)` appears visually empty, with the canopy top and all visible illustration content below it. This visual inspection does not replace the registered-point or mask audit.
- **Canvas background — visual observation only; strict-white status pending.** The canvas looks white in the displayed image. Appearance cannot establish exact RGB `#FFFFFF`; corner/sample-point checks and the full same-size background-mask review remain pending. I did not run numerical geometry, palette, or background audits.
- **Internal-only status — PASS.** The candidate is under the experiments directory and contains no visible official mark. Keep it internal; this review does not authorize an overlay, adoption, or publication.

## Gate

Keep candidate v2 on **HOLD**. Its overall meaning, layout, reference identity, and visible ROI are sound, but the server stack and repeated micro-UI details conflict with explicit v2 simplification requirements. A next candidate must address those details, then pass the independent exact-white and full-mask checks before any candidate-level PASS.
