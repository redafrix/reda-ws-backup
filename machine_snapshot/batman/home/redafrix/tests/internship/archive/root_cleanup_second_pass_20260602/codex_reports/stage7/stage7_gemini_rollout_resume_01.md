# Stage 7 — Gemini Rollout Resume (01)

- Timestamp: 2026-05-15 (Gemini)
- Context: Inspecting the "norm" vs "fixed" runs on Bob.

## Findings

1. **The "Norm" Run is a success!**
   - File: `stage7_libero_execution_tiny_object_t0_norm.json`
   - Result: **100% Success** (6/6 episodes).
   - Modes: `A_passive` (3/3), `B_deliberation` (3/3).
   - Avg steps to success: ~250.

2. **The "Fixed" Run (pre-patch) was a failure.**
   - File: `stage7_libero_execution_tiny_object_t0_fixed.json`
   - Result: **0% Success** (0/6 episodes).
   - Reason: Missing `norm_stats` loading for `LiberoJointActionSpace`.

3. **Verification of Norm Stats.**
   - The "norm" log confirms: `[setup] loaded norm_stats from .../libero_norm.json`.
   - Action stats debug (added by Gemini) confirms unnormalized actions are in the range `[-1.0, 1.0]`, matching expert demonstrations.

## Metrics Summary (Norm Run)

| Mode | Success Rate | Avg Steps |
|---|---|---|
| A_passive | 100% (3/3) | 227.0 |
| B_deliberation | 100% (3/3) | 305.7 |

(Note: B_deliberation took more steps on avg, but one episode took 592 steps.)

## Conclusion

The environment blocker is resolved. Loading `libero_norm.json` correctly scales the actions for the LIBERO environment.
