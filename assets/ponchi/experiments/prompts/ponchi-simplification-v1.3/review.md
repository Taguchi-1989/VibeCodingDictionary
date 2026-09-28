# ponchi-simplification-v1.3 independent prompt review

- **Review date:** 2026-09-28
- **Reviewer:** `/root/batch007_primary_b`
- **Result:** PASS
- **Review scope:** template wording and gate consistency only; no image generation or adoption.

## Evidence and decision

- The candidate-only rule applies to every `LOGO_MODE`: no logo overlay, promotion to `assets/ponchi/final`, production adoption, publication, or release without separate human approval and required production gates.
- Pre-registered background sample points are fail-fast only. A strict-white PASS requires a same-size 1-bit background mask; every pixel classified as background must be exact RGB `#FFFFFF` with alpha 255. Independent review checks that the mask excludes only illustration and its antialiased boundary, not broad blank areas.
- The rule rejects palette tolerance, sample-only success, and global white-pixel ratio as substitutes. It prohibits post-generation repainting.
- The approved palette, fixed-character/reference requirements, semantic/layout fields, brand handling, and two-targeted-revision stop rule remain consistent with v1.2.
- Batch006 v3 candidates remain HOLD at revision 2/2. This template does not authorize any additional edit or generation for them.

## Use status

Approved as the shared template for future item-specific sidecars. Each sidecar still requires its own independent prompt review before image generation. No candidate was generated from this template during the review.
