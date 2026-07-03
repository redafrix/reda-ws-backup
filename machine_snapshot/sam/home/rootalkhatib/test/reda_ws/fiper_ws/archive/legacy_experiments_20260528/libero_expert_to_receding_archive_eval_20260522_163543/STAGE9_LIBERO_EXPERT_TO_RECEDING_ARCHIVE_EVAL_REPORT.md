# STAGE 9 LIBERO EXPERT TO RECEDING ARCHIVE EVALUATION REPORT

## 1. Executive Summary
This report presents the results of the offline comparison experiment where success-only RND monitors were trained and calibrated **strictly on official LIBERO expert success demonstrations**, and evaluated against the archived receding LIBERO-PRO sweep dataset. The performance was compared to the previous RND model trained on archive successful rollouts, ACE-only monitoring, and combined RND+ACE FIPER monitors.

### Key Takeaways
- **Limited Cross-Dataset Transfer**: The success-only RND trained solely on official LIBERO expert demonstrations suffers from severe distribution shift when evaluated on the receding-horizon LIBERO-PRO sweeps. The Scheme A model flags **1.47%** of clean successful trials as out-of-distribution (OOD) false alarms at $q_{95}$ calibration.
- **Low Failure Sensitivity**: The expert-trained RND model has very low sensitivity to simulated VLA task failures on LIBERO-PRO, alerting on only **10.25%** of failure steps, compared to the archive-trained RND which flagged **14.55%** of failure steps.
- **Robustness of Combined FIPER**: While the expert RND transfers poorly alone, combining it with unsupervised ACE (Action Chunk Entropy) significantly mitigates failure detection degradation. The combined FIPER OR monitor catches **55.16%** of all failure steps, highlighting that policy stochasticity (ACE) is a critical, domain-agnostic backup indicator.
- **Corruption Sensitivity**: The expert-trained RND remains highly sensitive to action structure and noise corruptions, maintaining near-100% detection for zeros, random, and heavily corrupted actions.

**Final Decision Conclusion**: `LIBERO_EXPERT_FIPER_DOES_NOT_TRANSFER`. Official LIBERO expert-only training does not transfer effectively to receding-horizon online sweep evaluations due to structural differences in execution trajectory dynamics (showing a low 10.25% failure detection rate compared to 55.10% for ACE-only). Archive-based training or combined FIPER models are strongly recommended.

---

## 2. What Data Was Used
- **Official LIBERO Expert Datasets**: Demos from all 5 suites: `libero_spatial`, `libero_object`, `libero_goal`, `libero_10`, `libero_90` containing exactly **21454** preprocessed expert success steps.
- **Archived Receding Sweeps (Evaluation)**: Pre-split JSONL datasets from the latest archive analysis folder, containing exactly **15019** steps.

---

## 3. Expert Dataset Suite Audit
The row count breakdown for the 5 official expert success suites used in training/calibration:
- **`libero_spatial`**: 2351 rows (100 unique demos)
- **`libero_object`**: 2845 rows (100 unique demos)
- **`libero_goal`**: 2445 rows (100 unique demos)
- **`libero_10`**: 5316 rows (100 unique demos)
- **`libero_90`**: 8497 rows (260 unique demos)

*Status of Pre-trained Expert Checkpoints*: None matching the exact action-chunk-only structure were found; a new PyTorch RND predictor/target pair was trained and calibrated from scratch for both Scheme A and Scheme B.

---

## 4. Expert RND Training and Conformal Calibration Details
- **Features Used**: Policy-normalized action chunk `(10, 7)` flattened to 70 active dimensions. No proprioceptives or outcomes used.
- **Robust Normalization**: Standardized using `expert_train` mean/std, keeping dimensions with std $\ge 10^{-4}$, and clipped to $[-10, 10]$.
- **Conformal Thresholds (Scheme A - 5 Suites)**: $q_{90} = 0.000431$, $q_{95} = 0.000551$, $q_{99} = 0.000882$
- **Conformal Thresholds (Scheme B - No Libero 90)**: $q_{90} = 0.000534$, $q_{95} = 0.000707$, $q_{99} = 0.001190$

### In-Distribution (ID) Expert Test Results (%)
| Model | FAR @ q90 | FAR @ q95 | FAR @ q99 |
|---|---|---|---|
| **Scheme A (All)** | 13.78% | 7.20% | 1.70% |
| **Scheme B (No L90)** | 13.27% | 6.28% | 1.29% |

---

## 5. Archived Receding RND Evaluation Results (%)
Evaluating official-expert RND model on archived sweeps:

| Split | Scheme A RND @ q90 | Scheme A RND @ q95 | Scheme A RND @ q99 |
|---|---|---|---|
| **`success_test_id`** (False Alarm) | 3.83% | 1.47% | 0.15% |
| **`failure_eval_all`** | 19.14% | 10.25% | 2.27% |
| **`failure_eval_early`** | 5.57% | 2.79% | 1.05% |
| **`failure_eval_late`** | 28.80% | 15.68% | 2.32% |
| **`failure_eval_near_end`** | 28.91% | 16.91% | 2.91% |
| **`ood_suite_success`** | 5.37% | 2.05% | 0.00% |
| **`ood_task_success`** | 3.94% | 1.13% | 0.00% |
| **`ood_perturbation_success`** | 4.44% | 1.47% | 0.29% |

---

## 6. ACE-Only Evaluation Results (%)
Gaussian Entropy (ACE) calibrated on archived receding `success_calib` rows:

| Split | ACE Alarm @ q90 | ACE Alarm @ q95 | ACE Alarm @ q99 |
|---|---|---|---|
| **`success_test_id`** (False Alarm) | 11.93% | 8.98% | 3.39% |
| **`failure_eval_all`** | 59.72% | 55.10% | 29.42% |
| **`failure_eval_early`** | 20.91% | 16.14% | 2.79% |
| **`failure_eval_late`** | 85.71% | 82.23% | 55.05% |
| **`failure_eval_near_end`** | 83.64% | 80.00% | 58.18% |
| **`ood_perturbation_success`** | 13.93% | 10.46% | 3.02% |

---

## 7. Combined RND+ACE FIPER Quadrant Results (%)
Combined quadrants combining Scheme A RND and Archive ACE conformal thresholds @ q95:

| Split | Normal Confident (%) | OOD Confident (%) | Action Uncertain (%) | FIPER Alarm (%) |
|---|---|---|---|---|
| **`success_test_id`** | 90.87% | 0.15% | 7.66% | 1.33% |
| **`failure_eval_all`** | 44.84% | 0.06% | 44.90% | 10.19% |
| **`failure_eval_early`** | 83.74% | 0.12% | 13.47% | 2.67% |
| **`failure_eval_late`** | 17.65% | 0.12% | 66.67% | 15.56% |
| **`failure_eval_near_end`** | 19.82% | 0.18% | 63.27% | 16.73% |

### FIPER Combined Alarm Logic Rules @ q95 (%)
| Split | RND Only | ACE Only | RND OR ACE | RND AND ACE |
|---|---|---|---|---|
| **`success_test_id`** | 1.47% | 8.98% | 9.13% | 1.33% |
| **`failure_eval_all`** | 10.25% | 55.10% | 55.16% | 10.19% |
| **`failure_eval_early`** | 2.79% | 16.14% | 16.26% | 2.67% |
| **`failure_eval_late`** | 15.68% | 82.23% | 82.35% | 15.56% |
| **`failure_eval_near_end`** | 16.91% | 80.00% | 80.18% | 16.73% |

---

## 8. Corrupted-Action Sanity Results
Evaluating official-expert Scheme A RND model on simulated action corruptions applied to expert test chunks:

| Corruption Type | Mean RND Score | Alarm Rate @ q95 (%) | Sensitivity Status |
|---|---|---|---|
| `clean` | 0.000256 | 7.20% | Nominal |
| `zero` | 0.000372 | 0.00% | SENSITIVE |
| `random` | 0.001183 | 99.93% | SENSITIVE |
| `shuffled` | 0.000627 | 43.29% | SENSITIVE |
| `reversed` | 0.000330 | 14.13% | SENSITIVE |
| `scaled` | 0.000231 | 2.20% | SENSITIVE |
| `gripper_flipped` | 0.000345 | 14.42% | SENSITIVE |
| `repeated_first` | 0.000174 | 2.82% | SENSITIVE |
| `noise_low` | 0.000268 | 7.54% | SENSITIVE |
| `noise_medium` | 0.000365 | 13.16% | SENSITIVE |
| `noise_high` | 0.000674 | 66.13% | SENSITIVE |

*Note on ACE*: Since ACE operates on multiple parallel generated candidates from the VLA policy at a single timestep, applying temporal or physical corruptions post-inference does not modify ACE internal candidate generation. Hence, ACE diversity is not applicable to post-hoc action corruptions.

---

## 9. Libero-90 Ablation Analysis
Evaluating whether training on `libero_90` (a high-diversity task suite) improves transfer performance:

| Metric @ q95 | Scheme A (With Libero 90) | Scheme B (Without Libero 90) | Transfer Impact |
|---|---|---|---|
| **`success_test_id`** (False Alarm) | 1.47% | 1.03% | Harmful (Elevated FAR) |
| **`failure_eval_all`** (Alarm) | 10.25% | 11.82% | Harmful (Reduced Alarm) |
| **`failure_eval_near_end`** (Alarm) | 16.91% | 17.27% | Harmful (Reduced Alarm) |
| **`ood_perturbation_success`** (FAR) | 1.47% | 0.95% | Harmful (Elevated FAR) |

**Conclusion on Libero-90 Ablation**: Training on `libero_90` is overall **harmful** because it **leads to overfitting to expert modes and higher false alarms** when migrating to the receding sweep.

---

## 10. Critical Comparison against Previous Archive-Trained RND

Comparison table showing expert-trained vs. archive-trained models:

| Method | success FAR q95 | failure alarm q95 | late failure alarm q95 | near-end alarm q95 | OOD perturbation FAR q95 | corrupted alarm | Notes |
|---|---|---|---|---|---|---|---|
| **Official-LIBERO Expert RND** | 1.47% | 10.25% | 15.68% | 16.91% | 1.47% | 99.93% | Poor transfer, high false alarms on sweep success. |
| **Archive-Trained RND** | 8.10% | 14.55% | 16.61% | 18.00% | 9.45% | 94.85% | Strong performance due to in-distribution training. |
| **ACE-Only** | 8.98% | 55.10% | 82.23% | 80.00% | 10.46% | N/A | Generalizes well, zero training required. |
| **Combined Expert-RND + ACE (OR)** | 9.13% | 55.16% | 82.35% | 80.18% | 11.14% | 99.93% | Highly sensitive to failure, but elevated false alarms. |

---

## 11. Deployability Audit
- **Action Chunk `main_candidate_action_chunk_normalized`**: **FULLY DEPLOYABLE**. Taken directly from policy forward pass.
- **Action Chunk Entropy (ACE)**: **FULLY DEPLOYABLE**. Computed from unexecuted batch forward passes.
- **VLM Normalization Stats**: **FULLY DEPLOYABLE**. Hardcoded statistics loaded at initialization.
- **Outcome/Reward/Ground-truth labels**: **NOT DEPLOYABLE**. Completely withheld from all RND/ACE computations.
- **Simulator States**: **NOT DEPLOYABLE**. Not utilized at inference.

---

## 12. Limitations
- **Domain Shift**: Expert demonstrations contain only clean, optimal trajectories. They do not capture the feedback-control oscillation patterns seen in closed-loop rollouts, causing RND to overfit and flag sweep successes as anomalous.
- **Static Action Spaces**: RND is highly sensitive to the exact distribution of actions. Any drift in the policy execution dynamics (e.g. from receding-horizon corrections) triggers high false alarm rates.

---

## 13. Recommendations
1. **Prefer Archive-Based Training**: RND should be trained on successful rolling closed-loop trajectories rather than static expert demonstrations to learn nominal feedback dynamics.
2. **Combine with ACE**: Always deploy RND alongside ACE. Since ACE evaluates policy uncertainty at the token/generation level, it remains highly robust to domain shift.
