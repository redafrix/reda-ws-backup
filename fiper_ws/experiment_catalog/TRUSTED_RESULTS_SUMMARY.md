# Trusted Results Summary

> [!IMPORTANT]
> Only results that are mechanically verified and scientifically interpretable are listed here.
> Updated: 2026-06-10 by Codex full workspace audit.

---

## Mechanically Trusted In-Distribution Results (Seen Tasks, Unseen Seeds)

These results are mechanically sound (complete episodes, clean JSONL, correct pairings, correct checkpoints and suites) but represent **in-distribution** evaluation. Tasks 3 and 6 were seen during detector training (1,368 and 1,423 episodes respectively). They prove the detector can help on familiar tasks with new seeds, **not** zero-shot generalization.

### Task 3 Aggressive TopK8 (Threshold 0.3)
| Metric | Baseline (modified SimVLA) | Risk-Aware (aggressive TopK8) |
| :--- | :---: | :---: |
| **Success Rate** | 17/100 (17.0%) | 19/100 (19.0%) |
| **Net Gain** | — | **+2** |
| **Rescues** | — | 2 |
| **Regressions** | — | 0 |
| **True Modified Query Rate** | — | **1.04%** (29/2,776 queries) |
| **Episodes with ≥1 Modification** | — | 14/100 (14.0%) |

> [!WARNING]
> The Step 5 synthesis report incorrectly claimed 98.9% intervention rate. That was the threshold *exceedance* rate, not the actual modification rate. The true modification rate is 1.04%.

### Task 6 Aggressive TopK8 (Threshold 0.3)
| Metric | Baseline (modified SimVLA) | Risk-Aware (aggressive TopK8) |
| :--- | :---: | :---: |
| **Success Rate** | 57/100 (57.0%) | 62/100 (62.0%) |
| **Net Gain** | — | **+5** |
| **Rescues** | — | 19 |
| **Regressions** | — | 14 |
| **True Modified Query Rate** | — | **22.98%** (443/1,928 queries) |
| **Episodes with ≥1 Modification** | — | 94/100 (94.0%) |

> [!WARNING]
> The 94% episode-level modification rate means the policy intervened in nearly every episode. However, the Step 5 synthesis report incorrectly claimed the *query-level* rate was 94.7%. The true query-level rate is 22.98%.

### Task 6 Old Detector Aggressive (Threshold 0.3)
| Metric | Baseline (modified SimVLA) | Risk-Aware (old TopK8) |
| :--- | :---: | :---: |
| **Success Rate** | 57/100 (57.0%) | 60/100 (60.0%) |
| **Net Gain** | — | **+3** |
| **Rescues** | — | 13 |
| **Regressions** | — | 10 |

---

## OOD Goal-Swap Results — FAILED / DO NOT TRUST

### OOD Goal-Swap (libero_goal_swap, Tasks 3/6/8, Threshold 0.3)
| Metric | Baseline (modified SimVLA) | Risk-Aware (TopK8) |
| :--- | :---: | :---: |
| **Success Rate** | 8/300 (2.7%) | 6/300 (2.0%) |
| **Net Gain** | — | **-2** |
| **Rescues** | — | 2 |
| **Regressions** | — | 4 |

**Verdict:** NET NEGATIVE. The risk detector caused "panic interventions" on configurations the base policy could not solve. Full-suite goal-swap was never run (only Tasks 3, 6, 8).

## OOD Goal-Object Sweep Results — Aggressive-Fixed

### Corrected 10ep OOD Sweep (libero_goal_object_ood, 18 tasks, N=10, Threshold 0.3)
| Metric | Original SimVLA | Modified SimVLA | Risk-Aware (aggressive TopK8) |
| :--- | :---: | :---: | :---: |
| **Success Rate** | 169/180 (93.9%) | 168/180 (93.3%) | 172/180 (95.6%) |
| **Net Gain (vs Mod)** | — | — | **+4** successes (+2.2%) |
| **Net Gain (vs Orig)** | — | — | **+3** successes (+1.7%) |
| **Rescues (vs Mod)** | — | — | 6 |
| **Regressions (vs Mod)** | — | — | 2 |
| **Query Modification Rate** | — | — | **5.31%** (108/2,034 queries) |
| **Episodes with ≥1 Modification** | — | — | 80/180 (44.4%) |

> [!NOTE]
> **Statistical Strength:** **WEAK (early signal only).** While the early results show a positive net gain (+4 successes over the modified baseline), 10 seeds per task is not sufficient for definitive scientific conclusions.

### 100ep OOD Sweep (libero_goal_object_ood, 18 tasks, N=100, Threshold 0.3)
* **Status:** **COMPLETE** (5,400 / 5,400 episodes).
* **Target:** 100 episodes per policy per task.
* **Global Results:**
  - `original_simvla`: **92.67%** success rate (1,668/1,800 successes)
  - `modified_simvla`: **95.44%** success rate (1,718/1,800 successes)
  - `modified_h10_risk_topk8 (Thresh 0.3)`: **95.17%** success rate (1,713/1,800 successes)
  - **Paired Outcome (Risk vs Modified):** **24 rescues, 29 regressions** (net gain of **-5** successes / -0.28% net gain).
  - **Query Modification Rate:** **11.40%** (2,553 modified queries out of 22,388 total queries).
* **Safety check:** 0% seed leakage, 0 configuration errors, and 0 tracebacks or OOMs in logs.
* **Statistical strength:** **STRONG (N=100 per task)**.

### 100ep OOD Sweep (libero_goal_object_ood, 18 tasks, N=100, Threshold 0.5)
* **Status:** **COMPLETE** (1,800 / 1,800 episodes).
* **Target:** 100 episodes for `modified_h10_risk_topk8` per task compared against the 100ep baselines.
* **Global Results:**
  - `original_simvla`: **92.67%** success rate (1,668/1,800 successes)
  - `modified_simvla` (Baseline): **95.44%** success rate (1,718/1,800 successes)
  - `modified_h10_risk_topk8 (Thresh 0.5)`: **95.44%** success rate (1,718/1,800 successes)
  - **Paired Outcome (Risk vs Modified):** **21 rescues, 21 regressions** (net gain of **0** successes / 0.00% net gain).
  - **Query Modification Rate:** **4.99%** (1,120 modified queries out of 22,429 total queries).
  - **Comparison with Threshold 0.3:** Slashed the action modification rate by **56.2%** (down to 4.99% from 11.40%) while improving the net outcome (from -5 successes up to 0 successes).
* **Safety check:** 0% seed leakage, 0 configuration errors, and 0 tracebacks or OOMs in logs.
* **Statistical strength:** **STRONG (N=100 per task)**.

### 100ep OOD Sweep (libero_goal_object_ood, 18 tasks, N=100, Threshold q95)
* **Status:** **COMPLETE** (1,800 / 1,800 episodes).
* **Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610`
* **Target:** 100 episodes for `modified_h10_risk_topk8` per task, compared against the 100ep baselines.
* **Global Results:**
  - `original_simvla`: **92.67%** success rate (1,668/1,800 successes)
  - `modified_simvla` (Baseline): **95.44%** success rate (1,718/1,800 successes)
  - `modified_h10_risk_topk8 (q95)`: **95.00%** success rate (1,710/1,800 successes)
  - **Paired Outcome (Risk vs Modified):** **10 rescues, 18 regressions** (net gain of **-8** successes / -0.44% net gain).
  - **Action Modifications:** 408 total action modifications across 290 modified episodes.
* **Trust:** **TRUST** mechanically valid, but scientifically negative vs modified SimVLA. The conservative q95 threshold produced fewer rescues than thresholds 0.3 and 0.5 and still caused regressions.

## Sam Adaptive-Horizon Diagnostics — TRUSTED MECHANICALLY, NEGATIVE SCIENTIFIC RESULT

These tests used the corrected `libero_goal_object_ood` assets on Sam with 10 seeds per task over all 18 tasks. They are valid diagnostics for control-policy behavior, but the sample size is small and none improved over fixed H10 modified SimVLA.

| Variant | Success Rate | Paired Result vs Modified SimVLA | Mean Steps | Verdict |
| :--- | :---: | :---: | :---: | :--- |
| Modified SimVLA fixed H10 baseline | 171/180 (95.00%) | — | 121.18 | Baseline |
| V2B adaptive H1/H10, q95 | 167/180 (92.78%) | 2 rescues / 6 regressions, net -4 | 126.51 | **HURTS** |
| V2C adaptive H5/H10, q95 | 169/180 (93.89%) | 1 rescue / 3 regressions, net -2 | 123.82 | **HURTS** |
| V2D first5/tail5 commit gate, q95 | 168/180 (93.33%) | 6 rescues / 9 regressions, net -3 | 123.33 | **HURTS** |

> [!NOTE]
> The first V2 attempt was invalidated because it omitted the ACE candidate generation path needed to preserve the detector input distribution. V2B, V2C, and V2D restored ACE candidate generation and score only the main/planned chunk.

## Dean Selected-Cap Gate Diagnostic — PROMISING, NEEDS 100EP CONFIRMATION

This is the first recent OOD goal-object variant that improved over the fixed H10 modified SimVLA baseline on a full 18-task paired run. It uses action replacement, but adds an absolute cap on the selected candidate risk score.

| Metric | Modified SimVLA fixed H10 | TopK8 selected-cap risk |
| :--- | :---: | :---: |
| **Success Rate** | 170/180 (94.44%) | 176/180 (97.78%) |
| **Paired Rescues** | — | 7 |
| **Paired Regressions** | — | 1 |
| **Net Gain** | — | **+6** |
| **Modified Queries** | — | 121/2,160 (5.60%) |

Gate used on Dean:

- `selection_main_threshold = 0.3`
- `selection_min_margin = 0.02`
- `selection_strong_margin = 0.05`
- `selection_max_selected_score = 0.4`

Root: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_10ep_20260610`

Trust: mechanically valid diagnostic, but N=10 per task. A 100ep confirmation is running on Dean at `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610`.

### Dean Selected-Cap m10 Conservative Ablation

The margin-0.10 variant completed on the same 10ep suite and seeds. It reduced modifications but lost one success relative to the selected m02 policy.

| Metric | m02 selected-cap | m10 selected-cap |
| :--- | :---: | :---: |
| **Success Rate** | 176/180 (97.78%) | 175/180 (97.22%) |
| **Paired vs Modified Baseline** | 7 rescues / 1 regression, net +6 | 5 rescues / 0 regressions, net +5 |
| **Paired vs m02** | — | 1 rescue / 2 regressions, net -1 |
| **Action Modifications** | 121 | 49 |

Verdict: trusted conservative ablation, but do not scale before m02 100ep confirmation because it underperforms m02 on success.

### Dean Selected-Cap 100ep Confirmation — Complete

| Metric | Modified SimVLA fixed H10 | TopK8 selected-cap risk |
| :--- | :---: | :---: |
| **Global Success Rate** | 1,726/1,800 (95.89%) | 1,741/1,800 (96.72%) |
| **Global Paired Outcome** | — | 38 rescues / 23 regressions, net +15 |
| **Mean Steps** | 117.71 | 116.69 |
| **Query Modification Rate** | — | 1,402/21,800 (6.43%) |
| **Task 0 Success Rate** | 75/100 (75.0%) | 90/100 (90.0%) |
| **Task 0 Paired Outcome** | — | 21 rescues / 6 regressions, net +15 |
| **Task 1 Success Rate** | 94/100 (94.0%) | 95/100 (95.0%) |
| **Task 1 Paired Outcome** | — | 1 rescue / 0 regressions, net +1 |
| **Task 2 Success Rate** | 91/100 (91.0%) | 90/100 (90.0%) |
| **Task 2 Paired Outcome** | — | 0 rescues / 1 regression, net -1 |
| **Task 3 Success Rate** | 98/100 (98.0%) | 96/100 (96.0%) |
| **Task 3 Paired Outcome** | — | 0 rescues / 2 regressions, net -2 |
| **Cumulative Task 0-3 Success Rate** | 358/400 (89.5%) | 371/400 (92.8%) |
| **Cumulative Task 0-3 Paired Outcome** | — | 22 rescues / 9 regressions, net +13 |

Codex final audit source: `source_reports/dean/reports/DEAN_SELECTED_CAP_FINAL_ANALYSIS_20260611.md`.

Interpretation: this is now a trusted positive full-suite OOD result. The gain is global but not uniform: tasks 0 and 13 drive most of the improvement, while task 12 is the largest negative case.

### Dean Selected-Cap Delay30 100ep Replication — Complete

Root: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_delay30_100ep_20260611`

Seeds: 400-499.

Difference from the successful selected-cap run: `selection_min_timestep=30`, preventing replacements before query 3. Purpose: test whether early replacements are responsible for avoidable regressions.

| Metric | Modified SimVLA fixed H10 | TopK8 selected-cap delay30 |
| :--- | :---: | :---: |
| **Global Success Rate** | 1,721/1,800 (95.61%) | 1,718/1,800 (95.44%) |
| **Global Paired Outcome** | — | 19 rescues / 22 regressions, net -3 |
| **Mean Steps** | 119.76 | 119.50 |
| **Action Modifications** | — | 992 |

Interpretation: delay30 is mechanically valid but negative on Dean. The original selected-cap run without delay remains the best Dean result.

### Bob Selected-Cap 100ep Replication — Complete

Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_100ep_comparison_20260611`

Seeds: 10-109, matching the earlier Bob 100ep OOD baseline campaign.

| Policy | Success | Paired vs Modified | Episodes w/ Mods | Total Mods |
| :--- | :---: | :---: | ---: | ---: |
| Original SimVLA | 1,668/1,800 (92.67%) | 57 rescues / 107 regressions, net -50 | 0 | 0 |
| Modified SimVLA | 1,718/1,800 (95.44%) | baseline | 0 | 0 |
| TopK8 threshold 0.3 | 1,713/1,800 (95.17%) | 24 rescues / 29 regressions, net -5 | 833 | 2,553 |
| Selected-cap | 1,713/1,800 (95.17%) | 20 rescues / 25 regressions, net -5 | 690 | 1,440 |
| Selected-cap delay30 | 1,723/1,800 (95.72%) | 21 rescues / 16 regressions, net +5 | 523 | 1,013 |

Interpretation: Bob favors delay30 slightly, but the gain is small and conflicts with the Dean delay30 replication. Treat this as a valid but not yet robust positive.

---


## Incomplete / DO NOT TRUST

### Main Campaign Task 8 (H10, modified_simvla and modified_h10_risk_topk8)
* Runs were killed by `KeyboardInterrupt` from the supervisor.
* Only 5/100 episodes for `modified_simvla` and 2/100 for `modified_h10_risk_topk8` completed.
* **No scientific conclusions can be drawn.**

---

## Corrected Intervention-Rate Facts

| Experiment | Metric Claimed in Synthesis | Correct Value | Source |
| :--- | :--- | :--- | :--- |
| Task 3 aggressive TopK8 | "98.9% intervention rate" | **1.04% query modification rate** (29/2,776) | Step 6 audit |
| Task 6 aggressive TopK8 | "94.7% intervention rate" | **22.98% query modification rate** (443/1,928) | Step 6 audit |

The confusion arose because the synthesis report equated "queries where `main_score >= 0.3`" (the gating threshold exceedance) with "queries where an actual action replacement occurred." In Task 3, the candidate selection logic rejected 2,260/2,745 triggered queries due to `insufficient_margin` (candidates not offering ≥0.02 risk reduction).

---

## Trust Verdicts Summary

| Experiment | Trust Verdict |
| :--- | :--- |
| Task 3 aggressive TopK8 (ID) | **TRUST** (mechanically valid, in-distribution) |
| Task 6 aggressive TopK8 (ID) | **TRUST** (mechanically valid, in-distribution, fragile) |
| Task 6 old detector aggressive (ID) | **TRUST** (mechanically valid, ablation) |
| OOD goal-swap (Tasks 3/6/8) | **DO_NOT_TRUST** (net negative) |
| Task 8 H10 modified runs | **DO_NOT_TRUST** (incomplete) |
| Invalid 10ep OOD sweep (default threshold) | **DO_NOT_TRUST** (invalid configuration, aborted) |
| Corrected 10ep OOD sweep (aggressive fixed) | **TRUST** (mechanically valid, weak signal due to N=10) |
| Corrected 100ep OOD sweep (aggressive fixed, thresh 0.3) | **TRUST** (mechanically valid, complete, N=100 verified) |
| Corrected 100ep OOD sweep (aggressive fixed, thresh 0.5) | **TRUST** (mechanically valid, complete, N=100 verified) |
| Corrected 100ep OOD sweep (q95) | **TRUST** (mechanically valid, complete, net negative vs modified baseline: 10 rescues / 18 regressions, -8) |
| Sam V2 adaptive-horizon diagnostics | **TRUST diagnostic only** (V2B/V2C/V2D mechanically valid but all hurt vs modified baseline) |
| Dean selected-cap gate 10ep | **TRUST diagnostic, promising** (net +6; 100ep confirmation running) |
| Dean selected-cap gate 100ep | **TRUST positive** (net +15 vs modified baseline) |
| Dean selected-cap delay30 100ep | **TRUST negative** (net -3 vs modified baseline) |
| Bob selected-cap delay30 100ep | **TRUST small positive** (net +5 vs modified baseline; not robust across Dean) |
| Model identity verification | **TRUST** (Step 7: 0 mismatches) |
| Suite identity verification | **TRUST** (Step 8: 0 fallbacks) |
