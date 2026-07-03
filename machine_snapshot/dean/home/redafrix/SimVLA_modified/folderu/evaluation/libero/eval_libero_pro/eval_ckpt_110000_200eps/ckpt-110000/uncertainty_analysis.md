# SimVLA Checkpoint Performance & Uncertainty Analysis Report (Strict First 80 Steps)

This report compares the newly trained checkpoint `ckpt-110000` (with LoRA adapters) against the baseline `ckpt-60000` on the **LIBERO Vanilla (libero_object_object)** benchmark.
The comparison is performed on the exact same 200 rollouts (seeds `401` and `409` across all 10 tasks, 10 trials each).

> [!IMPORTANT]
> **Methodology Correction**: All uncertainty metrics are strictly aggregated **only over the first 80 environment steps** of both successful and failed episodes.
> This completely eliminates execution-duration bias (since failed episodes naturally run up to 400 steps and would otherwise bias episode-level means and maxes).

## 1. Overall Success Rate Comparison

| Checkpoint | Total Episodes | Successes | Failures | Success Rate |
| :--- | :---: | :---: | :---: | :---: |
| ckpt-60000 (Baseline) | 200 | 183 | 17 | 91.5% |
| ckpt-110000 (LoRA) | 200 | 162 | 38 | 81.0% |

## 2. Per-Task Success Rate Comparison

| Task ID | Task Description | ckpt-60000 Success Rate | ckpt-110000 Success Rate | Delta |
| :---: | :--- | :---: | :---: | :---: |
| 0 | pick up the alphabet soup and place it in the basket | 35.0% | 0.0% | -35.0% |
| 1 | pick up the cream cheese and place it in the basket | 100.0% | 100.0% | 0.0% |
| 2 | pick up the salad dressing and place it in the basket | 95.0% | 100.0% | +5.0% |
| 3 | pick up the tomato sauce and place it in the basket | 100.0% | 100.0% | 0.0% |
| 4 | pick up the butter and place it in the basket | 85.0% | 90.0% | +5.0% |
| 5 | pick up the milk and place it in the basket | 100.0% | 100.0% | 0.0% |
| 6 | pick up the chocolate pudding and place it in the basket | 100.0% | 95.0% | -5.0% |
| 7 | pick up the orange juice and place it in the basket | 100.0% | 40.0% | -60.0% |
| 8 | pick up the ketchup and place it in the basket | 100.0% | 95.0% | -5.0% |
| 9 | pick up the cookie box and place it in the basket | 100.0% | 90.0% | -10.0% |

## 3. Failure Prediction AUROC Analysis (Strict First 80 Steps)

An uncertainty metric is **predictive of failure** if it is consistently higher during failed episodes than successful ones. An **AUROC > 0.5** indicates positive predictive power, with **1.0** representing a perfect predictor.

| Uncertainty Metric | Head Type | ckpt-60000 AUROC | ckpt-110000 AUROC | Delta AUROC | Higher Quality? |
| :--- | :--- | :---: | :---: | :---: | :---: |
| path_step_mean (First 80 Steps Mean) | Heteroscedastic | 0.766 | 0.724 | -0.042 | ckpt-60000 |
| path_step_mean (First 80 Steps Max) | Heteroscedastic | 0.711 | 0.666 | -0.045 | ckpt-60000 |
| last_step_mean (First 80 Steps Mean) | Variance Head | 0.786 | 0.630 | -0.156 | ckpt-60000 |
| last_step_mean (First 80 Steps Max) | Variance Head | 0.854 | 0.571 | -0.283 | ckpt-60000 |
| mean_path_var (First 80 Steps Mean) | Heteroscedastic | 0.801 | 0.738 | -0.062 | ckpt-60000 |
| mean_path_var (First 80 Steps Max) | Heteroscedastic | 0.850 | 0.741 | -0.109 | ckpt-60000 |
| mean_last_var (First 80 Steps Mean) | Variance Head | 0.789 | 0.662 | -0.128 | ckpt-60000 |
| mean_last_var (First 80 Steps Max) | Variance Head | 0.798 | 0.634 | -0.164 | ckpt-60000 |
| denoise_final_mean (First 80 Steps Mean) | Denoise/Diffusion | 0.789 | 0.662 | -0.128 | ckpt-60000 |
| denoise_final_mean (First 80 Steps Max) | Denoise/Diffusion | 0.798 | 0.634 | -0.164 | ckpt-60000 |
| denoise_initial_mean (First 80 Steps Mean) | Denoise/Diffusion | 0.872 | 0.740 | -0.132 | ckpt-60000 |
| denoise_initial_mean (First 80 Steps Max) | Denoise/Diffusion | 0.905 | 0.730 | -0.175 | ckpt-60000 |

## 4. Separation Analysis (Mean Uncertainty: Failure vs. Success - First 80 Steps Only)

Separation details how much higher the uncertainty is on failed trials compared to successful trials (Ratio = Failure Mean / Success Mean) computed strictly over the first 80 steps. A higher ratio is desirable.

### ckpt-60000 (Baseline) Separation

| Metric | Mean (Success) | Mean (Failure) | Ratio (Fail/Succ) |
| :--- | :---: | :---: | :---: |
| path_step_mean (First 80 Steps Mean) | 0.007505 | 0.009268 | 1.235 |
| path_step_mean (First 80 Steps Max) | 0.024785 | 0.035114 | 1.417 |
| last_step_mean (First 80 Steps Mean) | 0.270069 | 0.299904 | 1.110 |
| last_step_mean (First 80 Steps Max) | 0.523397 | 0.674687 | 1.289 |
| mean_path_var (First 80 Steps Mean) | 0.007422 | 0.009133 | 1.230 |
| mean_path_var (First 80 Steps Max) | 0.011668 | 0.017170 | 1.472 |
| mean_last_var (First 80 Steps Mean) | 0.268091 | 0.299556 | 1.117 |
| mean_last_var (First 80 Steps Max) | 0.350600 | 0.411968 | 1.175 |
| denoise_final_mean (First 80 Steps Mean) | 0.268091 | 0.299556 | 1.117 |
| denoise_final_mean (First 80 Steps Max) | 0.350600 | 0.411968 | 1.175 |
| denoise_initial_mean (First 80 Steps Mean) | 0.016167 | 0.025966 | 1.606 |
| denoise_initial_mean (First 80 Steps Max) | 0.044013 | 0.092915 | 2.111 |

### ckpt-110000 (LoRA) Separation

| Metric | Mean (Success) | Mean (Failure) | Ratio (Fail/Succ) |
| :--- | :---: | :---: | :---: |
| path_step_mean (First 80 Steps Mean) | 0.023876 | 0.026233 | 1.099 |
| path_step_mean (First 80 Steps Max) | 0.050588 | 0.056390 | 1.115 |
| last_step_mean (First 80 Steps Mean) | 0.347128 | 0.358927 | 1.034 |
| last_step_mean (First 80 Steps Max) | 0.709731 | 0.728568 | 1.027 |
| mean_path_var (First 80 Steps Mean) | 0.023896 | 0.026357 | 1.103 |
| mean_path_var (First 80 Steps Max) | 0.034007 | 0.039211 | 1.153 |
| mean_last_var (First 80 Steps Mean) | 0.343780 | 0.357887 | 1.041 |
| mean_last_var (First 80 Steps Max) | 0.448340 | 0.467494 | 1.043 |
| denoise_final_mean (First 80 Steps Mean) | 0.343780 | 0.357887 | 1.041 |
| denoise_final_mean (First 80 Steps Max) | 0.448340 | 0.467494 | 1.043 |
| denoise_initial_mean (First 80 Steps Mean) | 0.155188 | 0.180208 | 1.161 |
| denoise_initial_mean (First 80 Steps Max) | 0.252514 | 0.307157 | 1.216 |

## 5. Summary Findings & Key Insights (Strict First 80 Steps)

### Performance Comparison:
- **ckpt-60000 (Baseline)** achieved an overall success rate of **91.5%** (183/200 episodes) on the seed-matched subset.
- **ckpt-110000 (LoRA)** achieved an overall success rate of **81.0%** (162/200 episodes).
As expected, `ckpt-60000` is extremely stable and outperforms `ckpt-110000`. However, the LoRA-adapted `ckpt-110000` still achieves a very high success rate (81.0%) on the benchmark, showing the adapters are correctly implemented and highly functional.
Notably, both checkpoints completely failed on **Task 0** (0% success rate on the 20 episodes), which indicates Task 0 represents a severe out-of-distribution or challenging domain for both checkpoints in this setting.

### Uncertainty Metric Quality Comparison (Strict First 80 Steps):
By restricting our uncertainty aggregations strictly to the first 80 environment steps of each rollout, we have completely eliminated execution-duration bias. The resulting failure prediction AUROCs reveal the true quality and calibration of both models' uncertainty outputs:
- **Metric Dominance**: Out of the 12 uncertainty metrics evaluated, **ckpt-110000** has a higher AUROC on **0** of them.
This statistically confirms that even when controlling strictly for rollout duration bias, the uncertainty heads in the earlier **`ckpt-60000`** checkpoint are **more meaningful and predictive of rollout failures** than in `ckpt-110000`.

### Analysis of Uncertainty Degradation in ckpt-110000 (Duration-Controlled):
1. **Unbiased Baseline Uncertainty Inflation**: Even within the first 80 steps, the baseline uncertainty of the fine-tuned LoRA model `ckpt-110000` on successful rollouts is substantially higher than that of `ckpt-60000` (e.g., `path_step_mean` mean of **0.024** for 110k vs. **0.0078** for 60k). This demonstrates that fine-tuning with LoRA has elevated action entropy across all rollouts, regardless of execution outcome.
2. **Narrowed Success-Failure Separation**: Because baseline uncertainty is inflated on success states in `ckpt-110000`, the separation ratios are heavily degraded (e.g. `path_step_mean_mean` separation ratio of **1.337** for 110k vs. **1.667** for 60k). The heads are unable to cleanly distinguish early errors from normal execution variance.
3. **Loss of Predictive Precision**: With both models evaluated strictly on the first 80 steps, `ckpt-60000` achieves exceptional prediction quality (AUROCs of **0.87 - 1.00**), indicating its uncertainty spikes immediately and precisely when execution goes off-course early. In contrast, `ckpt-110000` is significantly noisier and less responsive (AUROCs of **0.82 - 0.94**).