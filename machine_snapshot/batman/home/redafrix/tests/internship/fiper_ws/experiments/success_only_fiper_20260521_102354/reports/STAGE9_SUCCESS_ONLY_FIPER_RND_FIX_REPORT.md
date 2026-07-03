# STAGE 9 SUCCESS-ONLY FIPER — RND FEATURE FIX REPORT

## 1. Executive Summary

This report documents the **RND feature explosion fix** for the success-only FIPER safety monitor on **Sam**. The original RND-OE model suffered from a numerical instability where 10 of 81 features were constant in the expert training data, causing their normalization standard deviations to be clipped to `1e-6`. When rollout data deviated on these features, normalized values exploded to `~1,000,000`, producing RND scores in the billions.

**Fix applied**: Drop all features with training `std < 1e-4`, clip normalized values to `[-10, 10]`, and save the feature mask in the checkpoint for consistent application at evaluation time.

### Final Decision:
**`RND_FIX_WORKS_ID_ONLY`**

* **Why**: The feature fix completely eliminates the RND score explosion (rollout scores now `0.002–0.097` instead of `1e10`). ID false alarm rates remain well-calibrated (4.94% at q95 vs nominal 5%). OOD task generalization is excellent (0.52% at q95). However, OOD suite false alarm rate remains elevated at **13.44% at q95** — essentially unchanged from the pre-fix value of 13.23%. The fix solved the numerical bug but did not improve OOD suite generalization, confirming that the high OOD-suite FAR is a genuine distributional sensitivity issue, not an artifact of the bug.

---

## 2. What Caused the RND Explosion

The original `train_rnd_oe.py` normalized input features using:
```python
X_std = X_tensor.std(dim=0, keepdim=True).clamp(min=1e-6)
X_norm = (X_tensor - X_mean) / X_std
```

When all training samples had the same value for a feature, `std=0.0` was clipped to `1e-6`. At evaluation time, any deviation from that constant value was divided by `1e-6`, producing normalized values of order `1,000,000` instead of order `1`.

**Example**: `outcome_steps_executed` was always `10` in expert data. A rollout with `steps_executed=8` produced a normalized value of `(8 - 10) / 1e-6 = -2,000,000`.

---

## 3. Exact Feature Fix

### 3.1 Dropped Features (10 of 81)

All features with training `std < 1e-4` were identified and permanently excluded:

| Index | Feature Name | Training Mean | Training Std |
|:---:|:---|:---:|:---:|
| 70 | `flowtrace_action_norm_mean` | 0.000 | 0.00e+00 |
| 71 | `flowtrace_action_norm_std` | 0.000 | 0.00e+00 |
| 72 | `flowtrace_action_norm_max` | 0.000 | 0.00e+00 |
| 73 | `flowtrace_gripper_change_count` | 0.000 | 0.00e+00 |
| 74 | `flowtrace_gripper_open_fraction` | 0.000 | 0.00e+00 |
| 75 | `flowtrace_direction_change_count` | 0.000 | 0.00e+00 |
| 76 | `flowtrace_smoothness_score` | 0.000 | 0.00e+00 |
| 78 | `outcome_steps_executed` | 10.000 | 0.00e+00 |
| 79 | `outcome_H_used` | 10.000 | 0.00e+00 |
| 80 | `history_length` | 0.000 | 0.00e+00 |

**Why these are constant in expert data**:
- **Flowtrace features (7)**: Expert demos are extracted from HDF5 files and don't pass through the flowtrace pipeline. All flowtrace fields are empty/zero.
- **`steps_executed` and `H_used`**: Expert chunks are exactly 10 steps long by construction.
- **`history_length`**: Expert demos have no history buffer.

### 3.2 Kept Features (71 of 81)

The 71 remaining features are:
- **70 action dimensions**: `action_step{0-9}_dim{0-6}` — the 10-step × 7-dim normalized candidate action chunk. These have training std in `[0.047, 0.991]`.
- **1 outcome feature**: `outcome_reward_sum_H` — the reward accumulated over the H-step rollout.

### 3.3 Normalization Clipping

After masking, normalized values are clipped to `[-10, 10]`:
- **Max |normalized| before clip**: `13.09` (some extreme expert actions)
- **Max |normalized| after clip**: `10.00`

This prevents any single feature from dominating the network input even when values are within the kept feature set.

### 3.4 Checkpoint Metadata

The fixed checkpoint (`rnd_oe_fixed.pt`) now stores:
- `feature_mask`: boolean list (len=81), True = kept
- `kept_feature_names`: list of 71 kept feature names
- `dropped_feature_names`: list of 10 dropped feature names
- `clip_val`: 10.0
- `X_mean`, `X_std`: computed on masked features only (shape `[1, 71]`)

---

## 4. Training Results

| Metric | Old (Broken) | Fixed |
|:---|:---:|:---:|
| Input dimensions | 81 | **71** |
| Training samples | 11,199 | 11,199 |
| Epochs | 30 | 30 |
| Best loss | 0.000287 | **0.000317** |
| Features dropped | 0 | **10** |

Training loss is slightly higher because the network lost 10 input dimensions. This is expected and healthy — those dimensions were carrying no information in the expert data anyway.

---

## 5. Conformal Threshold Calibration

Thresholds calibrated strictly on `calib_success_id` (3,574 samples):

| Quantile | Old (Broken) | Fixed | Change |
|:---|:---:|:---:|:---:|
| **q90** | 0.000592 | **0.000662** | +11.8% |
| **q95** | 0.000754 | **0.000853** | +13.1% |
| **q99** | 0.001125 | **0.001333** | +18.5% |

Thresholds increased slightly because the model has fewer dimensions to overfit on, producing slightly wider score distributions.

---

## 6. False Alarm Rate Evaluation

### 6.1 Before vs After Fix

| Split | Count | Old FA@q95 | **Fixed FA@q95** | Old FA@q99 | **Fixed FA@q99** |
|:---|:---:|:---:|:---:|:---:|:---:|
| `train_success_id` | 11,199 | 2.55% | **2.59%** | 0.51% | **0.42%** |
| `test_success_id` | 3,944 | 4.67% | **4.94%** | 1.01% | **0.91%** |
| `test_success_ood_task` | 386 | 0.52% | **0.52%** | 0.26% | **0.26%** |
| `test_success_ood_suite` | 2,351 | 13.23% | **13.44%** | 3.62% | **3.70%** |

### 6.2 Interpretation

- **ID calibration**: `test_success_id` FA at q95 = **4.94%** (target: 5.0%). Near-perfect calibration is maintained.
- **OOD task**: FA at q95 = **0.52%**. Excellent generalization to unseen tasks within trained suites.
- **OOD suite**: FA at q95 = **13.44%**. This is essentially unchanged from the broken model's 13.23%. This proves the high OOD-suite FAR is a **real distributional shift problem**, not an artifact of the feature explosion bug.

---

## 7. Rollout RND Sanity Check

### 7.1 Before Fix (Broken) — RND Scores on Rollouts
| Dataset | Mean RND | Max RND | Finite? |
|:---|:---:|:---:|:---:|
| safe_mass | ~1.2e10 | ~1.6e13 | ⚠️ Yes but nonsensical |
| failure_mined | ~1.2e10 | ~1.6e13 | ⚠️ Yes but nonsensical |

### 7.2 After Fix — RND Scores on Rollouts
| Dataset | Count | Mean RND | Min RND | Max RND | Max |Normalized| | Finite? |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **safe_mass** | 5,120 | **0.0294** | 0.0053 | **0.0845** | 66.26 | ✅ Yes |
| **failure_mined** | 8,192 | **0.0206** | 0.0023 | **0.0968** | 64.25 | ✅ Yes |

**Key observations**:
- All scores are now finite and in a reasonable range (0.002–0.097).
- The explosion from billions to `~0.03` confirms the fix works.
- Both rollout datasets have RND scores **well above** the q95 threshold (0.000853), which is expected — rollouts are genuinely out-of-distribution relative to expert success data.
- `max_abs_normalized` of 64–66 means some rollout features are 64 standard deviations from the expert mean even on the kept features. This is clipped to 10.0 by the clipping mechanism, preventing any single feature from dominating.

---

## 8. ACE + Fixed RND Quadrant Summary

Using the same ACE threshold (`q95` = `-82.1781`) and the fixed RND threshold (`q95` = `0.000853`):

### Safe Mass Dataset (80 states / 5,120 samples)
| Quadrant | States | % |
|:---|:---:|:---:|
| `OOD_confident` (RND high, ACE low) | 76 | 95.0% |
| `FIPER_alarm` (RND high, ACE high) | 4 | 5.0% |
| `action_uncertain` (RND low, ACE high) | 0 | 0.0% |
| `normal_confident` (RND low, ACE low) | 0 | 0.0% |

### Failure Mined Dataset (128 states / 8,192 samples)
| Quadrant | States | % |
|:---|:---:|:---:|
| `OOD_confident` (RND high, ACE low) | 128 | 100.0% |
| `FIPER_alarm` (RND high, ACE high) | 0 | 0.0% |
| `action_uncertain` (RND low, ACE high) | 0 | 0.0% |
| `normal_confident` (RND low, ACE low) | 0 | 0.0% |

The quadrant distributions are identical to the broken run. This is because ALL rollout states still score above the RND q95 threshold — they're genuinely OOD relative to expert success data, just at a sane scale now.

---

## 9. Mining Queue Summary

Generated `fiper_candidate_states_fixed.jsonl` with **208 unique states**, sorted by combined priority score.

**Top 5 mining candidates:**

| Rank | State ID | Quadrant | RND Score | ACE Score | Priority |
|:---:|:---|:---|:---:|:---:|:---:|
| 1 | `libero_spatial_..._t0_r6_pseed6_window011` | OOD_confident | 0.0516 | -95.68 | 61.48 |
| 2 | `libero_spatial_..._t0_r11_pSTUCK_s119` | OOD_confident | 0.0509 | -132.33 | 60.30 |
| 3 | `libero_spatial_..._t0_r16_pTRANSPORT_s108` | **FIPER_alarm** | 0.0454 | -80.65 | 59.44 |
| 4 | `libero_spatial_..._t0_r17_pTRANSPORT_s80` | OOD_confident | 0.0487 | -105.76 | 57.97 |
| 5 | `libero_spatial_..._t0_r5_pTRANSPORT_s80` | OOD_confident | 0.0482 | -142.36 | 57.09 |

Priority scores are now in a sane range (57–61) instead of the billions from the broken run.

---

## 10. Code Files Created

All new files are on Sam under `fiper_ws/stage9_v2_tools/`:

1. **`train_rnd_oe_fixed.py`** — New standalone RND-OE training module with:
   - Feature name assignment for all 81 dimensions
   - `compute_feature_mask()`: drops features with `std < 1e-4`
   - `train_rnd_torch_fixed()`: trains on masked features with `[-10, 10]` clipping
   - `score_samples_fixed()`: applies mask + clipping from checkpoint at eval time
   - Saves complete metadata (mask, names, clip_val) in checkpoint

2. **`run_rnd_fix_campaign.py`** — Campaign orchestration script that runs all 8 steps end-to-end.

**Original `train_rnd_oe.py` was NOT modified.** The fix lives in separate files.

---

## 11. Commands Run

All commands were executed on Sam via SSH:

```bash
# Deploy scripts
scp train_rnd_oe_fixed.py run_rnd_fix_campaign.py \
  sam:/home/rootalkhatib/test/reda_ws/fiper_ws/stage9_v2_tools/

# Run campaign
ssh sam "source /home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh && \
  cd /home/rootalkhatib/test/reda_ws/fiper_ws/stage9_v2_tools && \
  python3 run_rnd_fix_campaign.py"
```

---

## 12. Output Artifacts

All fixed outputs are under:
`/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/success_only_fiper_20260521_102354/fiper/rnd_success_only_fixed/`

| File | Description |
|:---|:---|
| `rnd_oe_fixed.pt` | Fixed model checkpoint with feature mask |
| `feature_mask_report.json` | Dropped/kept feature names and indices |
| `rnd_training_summary.json` | Training metrics and loss history |
| `rnd_conformal_thresholds.json` | Calibrated q90/q95/q99 thresholds |
| `rnd_scores_calib.jsonl` | Calib split scores |
| `rnd_scores_train_success_id.jsonl` | Train split scores |
| `rnd_scores_test_success_id.jsonl` | Test ID scores |
| `rnd_scores_test_success_ood_task.jsonl` | OOD task scores |
| `rnd_scores_test_success_ood_suite.jsonl` | OOD suite scores |
| `rnd_scores_safe_mass.jsonl` | Rollout safe mass scores |
| `rnd_scores_failure_mined.jsonl` | Rollout failure-mined scores |
| `fiper_exec_summary_fixed.json` | Full execution summary |
| `fiper_candidate_states_fixed.jsonl` | Mining queue (208 states) |

---

## 13. Final Decision

### **`RND_FIX_WORKS_ID_ONLY`**

| Criterion | Result |
|:---|:---|
| RND explosion eliminated? | ✅ Yes — scores now 0.002–0.097 instead of 1e10 |
| All scores finite? | ✅ Yes |
| ID calibration maintained? | ✅ Yes — 4.94% FA at q95 (target 5%) |
| OOD task generalization? | ✅ Yes — 0.52% FA at q95 |
| OOD suite generalization? | ❌ No — 13.44% FA at q95 (2.7x nominal) |
| Feature fix honest? | ✅ Yes — dropped 10 truly constant features |
| Clipping applied? | ✅ Yes — max |normalized| capped at 10.0 |

The fix solved the engineering bug. The remaining OOD suite sensitivity is a **real problem** — the RND model trained on `libero_object/goal/10/90` action patterns genuinely doesn't know what `libero_spatial` actions look like. Fixing this requires either suite-specific thresholds or including diverse suite data in training.
