# J-21 candidate v1 independent review

- Candidate: `J-21_candidate_v1.png`
- SHA-256: `13AB5224C147A0E3BB40FC67743DB8642FB59A63BBCBD7C433B50F67230A1377`
- Dimensions/mode: 1774×887 RGB.
- Verdict: **HOLD**. Keep internal; no promotion/adoption.

## Provenance and machine audits

- Source `assets/ponchi/final/J-21.webp`: actual SHA-256 `839F8AD76990C5F2272D825472D747DFC387EE4863B2BF4B29FF2BF1CB711DB5`, 1254×627 RGB; matches sidecar.
- The folder's image and color audits and contact sheets are present. Image audit reports bbox `0.869`, size pass, `clearspace_ink_ratio 0.0119`, overall pass. Color audit reports palette pass, off-palette ratio `0.002738`.
- Sidecar has `LOGO_MODE: not_required` and no logo/clearspace ROI. The image-audit CSV says `clearspace_required=true`; that default does not agree with the item policy. Treat that clearspace measurement as non-gating; no brand ROI applies.

## Meaning and layout at 200px

- Reviewed the full canvas and an in-memory 200×100 preview. The two equal side-by-side panels remain distinct. Left: one generic model with active navy update marks distributed across its nodes. Right: a similarly sized outlined, unfilled model with one lock and exactly one pale-blue attached adapter tile carrying the only active update mark. This reads clearly as whole-model updates versus frozen base plus one trained adapter; no gray fill is used for the frozen model.
- Training-data arrows feed both panels. There are no people or robots, branded UI, logo, product/model mark, numerical claim, or readable text.
- The front page of each input-document stack has several short horizontal strokes. They are generic line marks, not legible words, but can read as text placeholders at full size. Since the sidecar forbids pseudo-text, treat these strokes as a minor compliance concern and consider blanking/simplifying them in any authorized revision.
- The comparison uses clean, flat navy/black/pale-blue linework consistent with the series. It avoids repeated layer grids, dashboards, and extra update/lock marks. The network-node silhouettes are simple single diagrams, not multilayer architectures.

## Strict-white and background mask

- `background_points_perimeter_audit_v1.md/csv` reports opaque RGB, exact-white corners `0/4`, sidecar perimeter points `2/12`, and fail-fast `FAIL` (15 checks failed). In the 3% perimeter ROI, only `39,702/185,760` pixels are exact white; the ROI is not all-white.
- No same-size background mask was created because fail-fast checks failed; there was no post-generation white painting.
- There is no logo ROI to inspect; the strict-white perimeter check is the applicable background gate.

## Final decision

**HOLD** for strict-white background failure. Meaning, two-panel layout, update-scope contrast, and series treatment are clear at 200px; the document strokes are a minor pseudo-text risk. Do not treat the image/color audit passes as acceptance.
