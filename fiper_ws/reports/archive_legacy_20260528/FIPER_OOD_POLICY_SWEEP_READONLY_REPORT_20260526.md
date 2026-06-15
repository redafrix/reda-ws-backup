# FIPER OOD Policy Sweep Report (Read-Only)

**Date:** 2026-05-26  
**Project:** Stage 9 / LIBERO-PRO / SimVLA / FIPER monitor  
**Experiment Directory:** `experiments/fiper_ood_task_8_9_v2_loaderfix_20260526`  

## 1. Input Specifications & Metadata

- **RND Scores File:** `experiments/fiper_ood_task_8_9_v2_loaderfix_20260526/scores/rnd_scores_by_split.jsonl`
- **ACE Scores File:** `experiments/fiper_ood_task_8_9_v2_loaderfix_20260526/scores/ace_scores_by_split.jsonl`
- **RND Calibration Thresholds:**
  - `q90`: `0.028686`
  - `q95`: `0.036919`
  - `q99`: `0.058993`
- **ACE Calibration Thresholds:**
  - `q90`: `-342.286048`
  - `q95`: `-341.281387`
  - `q99`: `-338.711003`

### Split Statistics:

| Split | Number of Rows Read | Number of Episodes |
|---|---:|---:|
| `success_test_seen` | 54288 | 425 |
| `success_test_ood` | 98630 | 790 |
| `failure_eval_seen` | 152400 | 508 |
| `failure_eval_ood` | 19200 | 64 |

---

## 2. Top 10 Rules Sorted by Balanced Score

The ranking is based on the following formula:
`balanced_score = 2.0 * failure_eval_ood_det_at_25 + 1.0 * failure_eval_ood_episode_alarm_rate - 1.5 * success_test_ood_episode_alarm_rate - 1.0 * failure_eval_ood_never_rate`

| Rank | Rule Name | Balanced Score | Success Seen FA % | Success OOD FA % | Failure Seen Det % | Failure OOD Det % | Failure OOD Det@25 % | Failure OOD Never % |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `OR_q99_K1` | 186.52 | 27.76% | 58.99% | 74.80% | 98.44% | 89.06% | 1.56% |
| 2 | `RND_q99_K1` | 184.26 | 22.12% | 56.33% | 67.91% | 95.31% | 89.06% | 4.69% |
| 3 | `RND_q95_K2` | 181.65 | 41.65% | 68.48% | 79.33% | 96.88% | 95.31% | 3.12% |
| 4 | `RND_q90_K5` | 180.43 | 38.35% | 67.22% | 78.74% | 96.88% | 93.75% | 3.12% |
| 5 | `RND_q95_K3` | 179.11 | 31.29% | 63.92% | 73.43% | 95.31% | 92.19% | 4.69% |
| 6 | `OR_q95_K2` | 178.98 | 61.65% | 74.43% | 89.17% | 100.00% | 95.31% | 0.00% |
| 7 | `OR_q95_K3` | 178.91 | 50.59% | 68.23% | 85.63% | 98.44% | 92.19% | 1.56% |
| 8 | `TIER_A_yellow` | 178.91 | 50.59% | 68.23% | 85.63% | 98.44% | 92.19% | 1.56% |
| 9 | `TIER_B_yellow` | 178.91 | 50.59% | 68.23% | 85.63% | 98.44% | 92.19% | 1.56% |
| 10 | `OR_q90_K5` | 174.82 | 59.76% | 73.04% | 90.16% | 98.44% | 93.75% | 1.56% |

---

## 3. Selected Deployment Policies

### Best Safety / Maximum Failure Detection Rule
- **Rule:** `OR_q90_K1`
- **Balanced Score:** `157.78`
- **Success Test Seen False Alarm Rate:** `95.06%`
- **Success Test OOD False Alarm Rate:** `94.81%`
- **Failure Eval Seen Detection Rate:** `98.03%`
- **Failure Eval OOD Detection Rate:** `100.00%`
- **Failure Eval OOD Det @10%:** `78.12%`
- **Failure Eval OOD Det @25%:** `100.00%`
- **Failure Eval OOD Mean Detection Time (detected only):** `0.0427`
- **Never Detected Rate:** `0.00%`
- **Mean Alarm Steps (Successful OOD Episode):** `47.17`
- **Median Alarm Steps (Successful OOD Episode):** `35.00`

### Best Balanced Deployment Warning Rule
- **Rule:** `OR_q99_K1`
- **Balanced Score:** `186.52`
- **Success Test Seen False Alarm Rate:** `27.76%`
- **Success Test OOD False Alarm Rate:** `58.99%`
- **Failure Eval Seen Detection Rate:** `74.80%`
- **Failure Eval OOD Detection Rate:** `98.44%`
- **Failure Eval OOD Det @10%:** `35.94%`
- **Failure Eval OOD Det @25%:** `89.06%`
- **Failure Eval OOD Mean Detection Time (detected only):** `0.1497`
- **Never Detected Rate:** `1.56%`
- **Mean Alarm Steps (Successful OOD Episode):** `14.55`
- **Median Alarm Steps (Successful OOD Episode):** `3.00`

### Best Low False Alarm Conservative Mode Rule
- **Rule:** `AND_q90_K5`
- **Balanced Score:** `124.42`
- **Success Test Seen False Alarm Rate:** `19.29%`
- **Success Test OOD False Alarm Rate:** `27.47%`
- **Failure Eval Seen Detection Rate:** `60.63%`
- **Failure Eval OOD Detection Rate:** `87.50%`
- **Failure Eval OOD Det @10%:** `4.69%`
- **Failure Eval OOD Det @25%:** `45.31%`
- **Failure Eval OOD Mean Detection Time (detected only):** `0.3258`
- **Never Detected Rate:** `12.50%`
- **Mean Alarm Steps (Successful OOD Episode):** `1.89`
- **Median Alarm Steps (Successful OOD Episode):** `0.00`

---

## 4. Brutally Honest Deployment Verdict

- **AND Rule Tradeoff:** Yes, AND rules significantly suppress false alarms but completely destroy early detection (det@25 is very low or never detected rate is extremely high). For instance, `AND_q95_K2` yields a never-detected rate of 12.50% on OOD task failures.
- **OR Rule Tradeoff:** Yes, OR rules (e.g., `OR_q95_K3`) successfully detect failures (with a high detection rate of 98.44%) but suffer from massive false alarm rates (e.g. 68.23% on successful OOD episodes).
- **Hard-Stop Deployability Verdict:** **NOT DEPLOYABLE AS A HARD STOP MONITOR.** 
  The success OOD false alarm rates are unacceptably high across all safe/high-recall rules. Stopping the robot autonomously based on these triggers would result in aborted successful trajectories more than 50% of the time.
- **Warning Monitor vs. Hard Stop:** FIPER is best interpreted as a **WARNING monitor** that signals potential risk to a human operator or a high-level policy switcher, rather than an autonomous hard-stop policy.
- **Need for New Model/Method:** **YES.** The current RND+ACE formulation lacks the granularity to distinguish OOD task success from actual trajectory failures. We need a model idea that is more robust to task distribution shifts while remaining sensitive to local physical perturbations and failures.

---

## 5. Final Key Fields

```text
BEST_SAFETY_RULE = OR_q90_K1
BEST_BALANCED_RULE = OR_q99_K1
BEST_LOW_FA_RULE = AND_q90_K5
READY_FOR_NEXT_OOD_PERTURBATION_TRAINING = YES
NEEDS_NEW_MODEL_IDEA = YES
```
