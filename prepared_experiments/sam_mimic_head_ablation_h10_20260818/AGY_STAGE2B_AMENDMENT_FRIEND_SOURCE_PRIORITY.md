# Stage 2B amendment — friend source has priority

For every Mimic/W2A-specific convention, the friend's actual source code is authoritative and overrides inferred conventions in Stage 2B.

This includes, when recoverable:

- 10D rotation 6D serialization order
- 10D -> 7D converter behavior
- candidate disagreement formulas
- whether pairwise metrics include/exclude diagonals and how pairs are averaged
- horizon-channel formulas
- scalar feature ordering
- denoising-summary ordering
- temporal-change formulas
- model input ordering

Therefore:

1. First locate and hash the friend's real feature/conversion implementation in the historical Sam workspace / `fiper_ws/external/fiper` family.
2. Copy the relevant small source files verbatim into `source_snapshot/friend_head/`.
3. Build compatibility wrappers around those functions wherever possible instead of rewriting their mathematics.
4. If an exact friend formula conflicts with an inferred formula written in `AGY_STAGE2B_REAL_IMPLEMENTATION.md`, use the friend's exact formula and record the deviation in `FRIEND_PARITY_MAP.json`.
5. Never change SimVLA-native H10 execution/checkpoint/environment semantics to imitate the friend's policy. Only the risk-head evidence/representation/model conventions should be adapted as closely as possible.
6. If a required friend convention cannot be recovered from source, mark it `NOT_RECOVERED` and STOP before rollout rather than guessing.

The previous rejected stub commit `57e012251d63b4f148cb23388e24f7ca45808e1d` remains invalid and must not be launched.
