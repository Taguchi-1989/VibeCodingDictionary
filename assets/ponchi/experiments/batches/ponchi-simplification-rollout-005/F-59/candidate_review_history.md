# F-59 candidate review history

- Source: `assets/ponchi/experiments/batches/ponchi-batch-009/F-59_base_1254x627.png`; SHA-256 `dbab44651afbcdaf5822e732f06d346cef8a17796e37c9a13dd925e046e225c2`.
- Prompt: `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-005/F-59.md`; independent prompt review passed before generation.
- v1: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-005/F-59/F-59_candidate_v1.png`; SHA-256 `fc166d7a6358550648315997b5bf9936d9bc1fb732fd5f4ecc09f5537652b8bc`; 1774x887 RGB; corners `[(253, 255, 255), (254, 254, 254), (253, 253, 253), (253, 253, 253)]`.
  - Independent review: HOLD: duplicate documents, line-like pseudo-text, developer appearance differs from Character B, and white/palette are off-spec.
- v2: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-005/F-59/F-59_candidate_v2.png`; SHA-256 `680e7a6bcdc891d3eaa03c66b12cfca772a3126034213b9fe7152f65f9f79c8b`; 1774x887 RGB; corners `[(254, 255, 255), (255, 255, 254), (253, 253, 253), (254, 253, 253)]`.
  - Latest review state: pending independent review after one targeted revision; exact-white machine gate currently fails at image corners.


## Candidate v3 — final independent review 2026-09-28

- Path: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-005/F-59/F-59_candidate_v3.png`; SHA-256 `b1c266d1532cafb9410f48b0c82d876f18f9fb21ec044e0c136da0eb463fd8dc`; 1774x887 RGB.
- Independent 200px review: HOLD: v3 main document/repository/developer+robot meaning and no pseudo-text pass at 200px; background and exact palette fail; revision cap reached.
- Style gate: HOLD: pure white only 17.478%, #FEFEFE 44.849%; blue includes #073C8F outside exact palette; no further generation.
- Disposition: HOLD. Two targeted revisions are complete; no further image generation. No adoption, overlay, or production final update.
