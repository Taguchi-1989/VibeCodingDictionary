# F-40 candidate v1 background and ROI audit

- Candidate dimensions/mode: 1774x887 RGB; RGB sample checks are opaque for this RGB image.
- Four corners and eight registered points exact-white: False.
- Mapped source clearspace `[686,0,520,220]` ROI: `970,0` to `1706,311` (half-open); non-white pixels `192951` / `228896`; entirely exact-white: `False`.
- Per-point RGB values are in `background_points_roi_audit_v1.csv`.
- Background mask not created because at least one fail-fast corner/registered point did not pass exact white.
