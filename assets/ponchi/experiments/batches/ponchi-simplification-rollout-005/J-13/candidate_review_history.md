# J-13 candidate review history

- Source: `assets/ponchi/final/J-13.webp`; SHA-256 `9f0645451c8eaf4be79e2afefeecadb2593748a4018a8ab07aeeac14e9b82d63`.
- Prompt: `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-005/J-13.md`; independent prompt review passed before generation.
- v1: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-005/J-13/J-13_candidate_v1.png`; SHA-256 `4176fc5d45e1d31660f062a193c3498bfa3a1219180bdeb62883001c6fcdafb2`; 1774x887 RGBA; corners `[(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]`.
  - Independent review: Superseded: initial generated output had alpha; not an approved review target.
- v2: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-005/J-13/J-13_candidate_v2.png`; SHA-256 `7ae15de0bf91f40f9024835e9b77f03a61ecd616b97e8394d3624ed73906059c`; 1774x887 RGB; corners `[(253, 255, 255), (254, 255, 254), (253, 253, 253), (254, 253, 253)]`.
  - Independent review: HOLD for non-white background and palette; main stage order/person count pass.
- v3: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-005/J-13/J-13_candidate_v3.png`; SHA-256 `b301a3a3ffcd6910a96200d22f8e85b40b951a7a20e865b9c4effb25e8cd31a9`; 1774x887 RGB; corners `[(253, 255, 255), (254, 255, 254), (253, 253, 253), (254, 253, 254)]`.
  - Latest review state: pending independent review; exact-white machine gate fails and revision cap is reached.


## Candidate v3 — final independent review 2026-09-28

- Path: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-005/J-13/J-13_candidate_v3.png`; SHA-256 `b301a3a3ffcd6910a96200d22f8e85b40b951a7a20e865b9c4effb25e8cd31a9`; 1774x887 RGB.
- Independent 200px review: HOLD: v3 shows input→Encoder→three Attention slabs→Decoder→output plus one observer at 200px; no pseudo-text; revision cap reached.
- Style gate: HOLD: pure white only 19.616%, #FEFEFE 46.697%, other key colors outside exact palette; no further generation.
- Disposition: HOLD. Two targeted revisions are complete; no further image generation. No adoption, overlay, or production final update.
