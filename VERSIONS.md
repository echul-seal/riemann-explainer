# Version notes

## v1 (2026-11-24)
- script.md: narration script, 6 sections, about 11 minutes.
- Scenes: 27 manim CE 0.22 scenes (scenes/), one per narration clip, each timed to its clip by word position.
- Domain colorings of zeta (dcA: sigma -14..6; dcB: critical strip, t 0..32) are precomputed with mpmath.
- Explicit-formula scene rebuilds psi(x) from the first 1000 nontrivial zeros (Odlyzko's table).
- Zero-spacing histogram uses zeros 10,001 to 100,000, unfolded, against the GUE Wigner surmise.
- QA pass: automated blank-frame and edge-clipping check (tools/qa.py). Fixed six scenes that opened on an empty frame and the S4_1 axis labels clipping the bottom edge.
- Final: 1080p30 H.264 + AAC, 11:12.
- Facts checked against riemann-watch data.json and math.mit.edu/~drew/grh/ at 14:23Z Nov 24.
