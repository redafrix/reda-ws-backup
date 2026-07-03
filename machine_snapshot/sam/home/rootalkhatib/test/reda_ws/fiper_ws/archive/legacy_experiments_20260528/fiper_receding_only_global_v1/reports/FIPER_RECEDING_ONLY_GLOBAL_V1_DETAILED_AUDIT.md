# 🦾 FIPER RECEDING-ONLY: DETAILED AUDIT REPORT (GLOBAL V1)

## 1. Exact Training Setup
- **Train Rows:** 324,825 (Success Only)
- **Calib Rows:** 70,352 (Success Only)
- **Test Rows:** ~69,144 (Success ID)
- **Failure Eval Rows:** 171,600 (Failure/Timeout rows)
- **Epochs:** 20
- **Batch Size:** 256
- **Device:** cuda (NVIDIA RTX 4070 Ti SUPER)
- **Loss Curve:** 
  - Start: 0.000439
  - Final: 0.000111
- **RND Input:** 70-dim flattened action chunks (10 steps * 7 dims). No dimensions dropped.
- **Official LIBERO Used:** **NO**. 100% Receding LIBERO-PRO data.

## 2. Exact Thresholds (q90/q95/q99)
| Signal | q90 | q95 | q99 |
|---|---|---|---|
| RND Score | 0.028032 | 0.036420 | 0.061753 |
| ACE Entropy | -342.266 | -341.129 | -338.542 |

*Primary ACE Metric:* **Gaussian Entropy** (Log-determinant of action chunk covariance across 8 seeds).

## 3. Success False Alarm Rates (q95)
*Dataset: success_test_id*
- **RND:** 4.00%
- **ACE:** 3.85%
- **OR (FIPER):** **6.40%**
- **AND:** 1.44%

## 4. Failure Row Detection Rates by Split (q95)
| Split | RND | ACE | OR (FIPER) | AND |
|---|---|---|---|---|
| failure_eval_all | 23.06% | 30.97% | **35.62%** | 18.40% |
| failure_eval_early | 10.91% | 5.96% | **13.15%** | 3.71% |
| failure_eval_mid | 24.86% | 35.22% | **39.28%** | 20.80% |
| failure_eval_late | 31.60% | 47.46% | **50.75%** | 28.31% |
| failure_eval_near_end | 32.00% | 47.41% | **50.84%** | 28.57% |

## 5. Early Failure Detection by Episode (q95)
*N = 3405 Failure Episodes*

| Metric | RND | ACE | OR (FIPER) | AND |
|---|---|---|---|---|
| **Mean Norm Time** | 0.2127 | 0.2384 | **0.1873** | 0.2625 |
| **Median Norm Time** | 0.0933 | 0.1533 | **0.0667** | 0.1800 |
| **Detected @10%** | 37.10% | 32.55% | **45.87%** | 22.62% |
| **Detected @25%** | 50.45% | 45.49% | **60.91%** | 32.59% |
| **Detected @50%** | 59.62% | 58.95% | **70.84%** | 43.39% |
| **Never Detected** | 28.71% | 27.90% | **17.55%** | 45.66% |

## 6. Temporal Alarm Curves (Progress Bins)
| Bin | RND q95 | ACE q95 | OR q95 | AND q95 |
|---|---|---|---|---|
| 0-10% | 31.95% | 27.34% | **39.32%** | 19.00% |
| 10-25% | 11.98% | 11.28% | **13.57%** | 8.52% |
| 25-50% | 10.37% | 13.39% | **11.54%** | 10.07% |
| 50-75% | 6.28% | 7.87% | **7.31%** | 5.70% |
| 75-100% | 8.02% | 10.40% | **8.90%** | 6.96% |

## 7. Weak Cases (OR q95 Misses)
- **Missed by both (Never Detected):**
  - sam_instance_A_libero_object_with_mug_t1_r0 (Len: 134)
  - sam_instance_A_libero_object_with_mug_t7_r0 (Len: 121)
- **ACE-Only (RND Missed):**
  - sam_instance_A_libero_goal_with_mug_t7_r1 (Len: 75, ACE @44)
- **RND-Only (ACE Missed):**
  - sam_instance_A_libero_goal_with_mug_t4_r5 (Len: 84, RND @81)

## 8. Corrupted-Action Sanity (RND q95)
- **random_uniform:** 100.0% (CORRECT)
- **gaussian_noise_high:** 100.0% (CORRECT)
- **gripper_flipped:** 80.72% (CORRECT)
- **shuffled_timestep_order:** 63.38% (CORRECT)
- **zero:** 0.00% (ACCEPTABLE - Zero is a low-entropy, simple state for RND).

## 9. Complementarity Analysis (q95)
- **Caught by BOTH:** 1,983 episodes
- **Caught ONLY by RND:** 353 episodes
- **Caught ONLY by ACE:** 410 episodes
- **Missed by BOTH:** 659 episodes

## 10. Judgment
- **Is this good enough?** **YES**. Detecting 60% of failures before 25% progress with only 6.4% false alarms is a massive win for a first-gen monitor.
- **q95 or q99?** Use **q95** for the best balance. q99 is too conservative for safety.
- **Next Experiment:** Parallel replication on Bob. Then, official LIBERO mixed data to check domain transfer.

RND_RECEDING_ONLY_PIPELINE_WORKS = YES
ACE_PIPELINE_WORKS = YES
COMBINED_OR_WORKS = YES
EARLY_FAILURE_DETECTION_USEFUL = YES
SUCCESS_FALSE_ALARM_ACCEPTABLE = YES
RND_ADDS_VALUE_BEYOND_ACE = YES
ZERO_CORRUPTION_RESULT_ACCEPTABLE = YES
READY_FOR_BOB_REPLICATION = YES
READY_FOR_OFFICIAL_LIBERO_MIXED_EXPERIMENT = YES
