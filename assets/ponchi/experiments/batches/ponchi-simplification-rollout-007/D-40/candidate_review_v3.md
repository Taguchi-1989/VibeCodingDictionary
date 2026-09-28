# D-40 candidate v3 review record

- Candidate: `D-40_candidate_v3.png`
- SHA-256: `BDD4BA6F5501984BFAC2640AB78B60C84169C5CAFD2C17D5C8C5FA40F90440E2`
- Dimensions/mode: 1774×887 RGB
- Independent reviewer: `/root/review_wave001_b`, 2026-09-28.
- Overall: **HOLD; final candidate revision 2/2. No further generation.**

## Independent semantic and visual review

At 200px, the four-node left-to-right timeline and generic motifs read; the original observer remains at left. The mapped upper-right reserved rectangle has no foreground. No readable wording, extra figures, or logos were found. The v2 motif collision is corrected. Chat bubbles suggest conversation but do not strongly distinguish multilingual support; this is a semantic caveat.

Exact-white fails at all four corners and seven of eight registered points (only `(0.20,0.02)` is exact white). The diagram also fails exact solid palette despite tolerance audit PASS: among 73,751 foreground proxy pixels (`min(R,G,B)<245`), only 55 match an exact allowed color. Frequent near colors include `#114085` and `#DDE9F8`.

## Machine audits

- Geometry audit: PASS, bbox coverage 0.622; clearspace ink ratio 0.0000.
- Tolerance palette audit: PASS.
- Strict exact-white: FAIL; all four corners and 7/8 samples fail. No background mask was prepared because fail-fast samples failed.
- Reserved ROI foreground proxy: 0 pixels; independent reviewer confirms the mapped rectangle is clear.

The exact-white, reserved-ROI, and palette gates are not met. Preserve this final experiment as HOLD. Do not generate a fourth candidate or alter the pixels after generation.
