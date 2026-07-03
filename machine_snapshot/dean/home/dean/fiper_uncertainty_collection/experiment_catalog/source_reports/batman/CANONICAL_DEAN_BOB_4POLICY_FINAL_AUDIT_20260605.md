# Canonical Dean/Bob Four-Policy Final Audit

Audit time: 2026-06-05 09:26 Europe/Paris

Run ID: `canonical_dean_bob_task0_4policy_seq100_20260604`

Task: `libero_object_object`, task ID `0`, 100 paired reset seeds per policy.

## Completion and health

- Bob completed all four stages at 2026-06-05 00:13:43 CEST.
- Dean completed all four stages at 2026-06-05 05:36:26 CEST.
- Every stage exited with code 0 and contains exactly 100 unique episode indexes and 100 unique reset seeds.
- No traceback, runtime error, recorded episode error, seed collision, or main-action/ACE seed collision was found.
- The four policies used the same ordered reset-seed list on each host. The seed-list hash is also identical across hosts.
- Checkpoint hashes, runner hash, detector model files, normalization files, thresholds, and selected uncertainty dimensions match across Bob and Dean.
- No canonical experiment process remains active. Both GPUs are idle.
- Bob still exposes a pre-existing orphan CUDA allocation of 3158 MiB (`PID 848267`, process not found). It did not prevent these runs from completing, but it should be cleared before future memory-heavy work.

## Aggregate results

| Host | Policy | Success | Rate | Mean steps | Mean wall/episode | Total wall | Modified episodes | Total action modifications |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Bob | Original SimVLA | 10/100 | 10% | 284.64 | 52.10 s | 1.45 h | 0 | 0 |
| Bob | Modified SimVLA ckpt-60000 | 28/100 | 28% | 262.84 | 48.41 s | 1.34 h | 0 | 0 |
| Bob | Risk base | 25/100 | 25% | 265.04 | 167.55 s | 4.65 h | 69 | 337 |
| Bob | Risk + top-8 uncertainty | 26/100 | 26% | 262.65 | 166.73 s | 4.63 h | 78 | 345 |
| Dean | Original SimVLA | 14/100 | 14% | 279.74 | 60.53 s | 1.68 h | 0 | 0 |
| Dean | Modified SimVLA ckpt-60000 | 22/100 | 22% | 269.00 | 58.82 s | 1.63 h | 0 | 0 |
| Dean | Risk base | 25/100 | 25% | 269.96 | 254.41 s | 7.07 h | 75 | 311 |
| Dean | Risk + top-8 uncertainty | 20/100 | 20% | 270.39 | 254.73 s | 7.08 h | 80 | 400 |

Risk-aware inference was about 3.4 times slower than modified SimVLA on Bob and 4.3 times slower on Dean.

## Paired policy comparisons

`Recoveries` are failures of policy A that policy B turned into successes. `Regressions` are successes of A that B turned into failures.

| Host | A -> B | Success change | Recoveries | Regressions | Exact paired p-value |
|---|---|---:|---:|---:|---:|
| Bob | Original -> Modified | +18 | 25 | 7 | not used for risk-model verdict |
| Bob | Modified -> Risk base | -3 | 3 | 6 | 0.508 |
| Bob | Modified -> Risk + top-8 | -2 | 6 | 8 | 0.791 |
| Bob | Risk base -> Risk + top-8 | +1 | 6 | 5 | 1.000 |
| Dean | Original -> Modified | +8 | 15 | 7 | not used for risk-model verdict |
| Dean | Modified -> Risk base | +3 | 8 | 5 | 0.581 |
| Dean | Modified -> Risk + top-8 | -2 | 3 | 5 | 0.727 |
| Dean | Risk base -> Risk + top-8 | -5 | 5 | 10 | 0.302 |

None of the risk-aware comparisons is statistically persuasive at 100 episodes. The top-8 model is effectively tied with risk base on Bob and worse by five successes on Dean.

## Cross-host reproducibility

The inputs and artifacts match, but exact episode outcomes do not match across GPUs:

| Policy | Bob success | Dean success | Same outcome | Different outcome |
|---|---:|---:|---:|---:|
| Original SimVLA | 10 | 14 | 86 | 14 |
| Modified SimVLA | 28 | 22 | 82 | 18 |
| Risk base | 25 | 25 | 84 | 16 |
| Risk + top-8 uncertainty | 26 | 20 | 80 | 20 |

This is consistent with previously measured small cross-GPU action differences being amplified by closed-loop control. LIBERO is deterministic for an identical state/action sequence, but the RTX 4070 Ti SUPER and RTX A5000 do not produce bit-identical policy actions. Therefore Bob and Dean must be treated as separate replications, not as identical duplicated trajectories.

## Verdict

1. The canonical experiment completed correctly; there is no evidence of a crashed stage, mixed seeds, wrong checkpoint, mismatched detector artifact, or malformed result file.
2. The modified SimVLA checkpoint clearly outperformed original SimVLA on both hosts for this task.
3. Risk base did not show a stable advantage over modified SimVLA: it was -3 points on Bob and +3 points on Dean.
4. Adding the selected top-8 uncertainty features did not produce a replicated online benefit: +1 point versus risk base on Bob, but -5 points on Dean, while modifying more episodes on Dean.
5. The current online evidence does not validate the top-8 uncertainty model as better than risk base or plain modified SimVLA. Further work should focus on why intervention decisions are unstable and whether the risk threshold/action-selection rule improves conditional success, rather than running more copies of this exact configuration.

