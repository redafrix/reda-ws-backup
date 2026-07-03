# OOD-Suite Smoke Test Report

This report evaluates cross-suite Random Network Distillation (RND) performance to assess out-of-distribution (OOD) generalization and task separability.

## Experiment 1: Train on Suite A, Test on Suite B
- **Training Suite (In-Distribution):** `libero_spatial_with_mug` (Suite A)
- **Testing Suite (Out-of-Distribution):** `libero_goal_with_mug` (Suite B)
- **Model 1 Thresholds (Calibrated on Suite A Calib):**
  - q90: 0.000713
  - q95: 0.000809
  - q99: 0.001068
- **OOD Suite B Alarm Rates:**
  - Alarm @ q90: 100.00%
  - Alarm @ q95: 100.00%
  - Alarm @ q99: 99.84%

## Experiment 2: Train on Suite B, Test on Suite A
- **Training Suite (In-Distribution):** `libero_goal_with_mug` (Suite B)
- **Testing Suite (Out-of-Distribution):** `libero_spatial_with_mug` (Suite A)
- **Model 2 Thresholds (Calibrated on Suite B Calib):**
  - q90: 0.000232
  - q95: 0.000291
  - q99: 0.000796
- **OOD Suite A Alarm Rates:**
  - Alarm @ q90: 100.00%
  - Alarm @ q95: 99.94%
  - Alarm @ q99: 96.53%

## Key Takeaways
1. **Task Separability**: RND trained on one task-suite exhibits extremely high sensitivity to other tasks. Alarm rates for cross-suite evaluations are 100% (or very close to it).
2. **Conformal Calibration**: Both models maintain exact control of false alarms under in-distribution calibration, but register clear, persistent alarms when shifted to a different workspace layout (Goal vs Spatial layouts).
3. **Conclusion**: RND safety monitors are highly task-specific. Deploying a single RND monitor across multiple distinct task suites without task-specific training/calibration will result in continuous safety alarms.