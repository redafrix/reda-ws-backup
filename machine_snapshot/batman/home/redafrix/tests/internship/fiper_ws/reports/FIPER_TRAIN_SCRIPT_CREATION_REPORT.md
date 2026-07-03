# FIPER Training Script Creation Report

**Date:** Tuesday, May 26, 2026
**Status:** Success

## 1. Script Creation
- **Path:** `/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/run_receding_only_fiper_train_eval.py`
- **Features Implemented:**
    - Action-based RND (Predictor and Prior MLPs).
    - ACE computation (Variance-based entropy proxy).
    - Success-only training and calibration.
    - Evaluation across multiple splits (ID success and various failure stages).
    - Early failure detection metrics (First alarm index, normalized time, detection rates).
    - Corrupted-action sanity check (Zero-action and Noise-action benchmarks).
    - Efficient row loading from combined JSONL files.

## 2. Validation
- **py_compile:** PASSED.
- **Smoke Test:** PASSED.
    - **Command:**
      ```bash
      python3 scripts/run_receding_only_fiper_train_eval.py \
        --experiment-dir experiments/fiper_receding_only_global_v1_smoke \
        --device cpu \
        --epochs 1 \
        --batch-size 128 \
        --seed 42 \
        --max-train-rows 2000 \
        --max-calib-rows 1000 \
        --max-eval-rows 1000
      ```
    - **Outcome:** Trained for 1 epoch, calibrated thresholds, evaluated all splits, and ran sanity checks successfully.

## 3. Smoke Test Artifacts
The following files were produced in `experiments/fiper_receding_only_global_v1_smoke/`:
- `model.pth`: Saved RND model.
- `stats.npz`: Training set mean/std for normalization.
- `thresholds.json`: Calibrated RND and ACE quantiles (q90, q95, q99).
- `summary_*.json`: Per-split episode detection summaries.
- `sanity_results.json`: Detailed results for corrupted action tests.

## 4. Bug Fixes During Creation
- **ACE Reshape Error:** Fixed a shape mismatch in ACE calculation. The dataset contains 8 candidate seeds per row, not 64 as initially assumed. The script was updated to handle dynamic sample counts.

## 5. Next Step: Full Training
It is now safe to launch the full training run on Sam.

**Recommended Command:**
```bash
cd /home/rootalkhatib/test/reda_ws/fiper_ws
source ../asynchvla_ws/scripts/activate_simvla_sam.sh
python3 scripts/run_receding_only_fiper_train_eval.py \
  --experiment-dir experiments/fiper_receding_only_global_v1 \
  --device cuda \
  --epochs 20 \
  --batch-size 256 \
  --seed 42
```
