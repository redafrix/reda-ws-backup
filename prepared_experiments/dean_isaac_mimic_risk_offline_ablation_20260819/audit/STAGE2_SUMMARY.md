# Stage 2 Summary — Isaac Mimic H10 Implementation and Materialization

## 1. Action Adapter Provenance
- Isaac 7D Action Semantics: `[translation(3) in meters, rotvec(3) axis-angle in radians, gripper(1) discrete]`
  - Source: `/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab/src/franka_wrist_camera_scene/control/reaching_pose_actions.py`
  - SHA256: `8c0acff1bc1a1d3d78341f15d5e5ba6b7d7aae92a17e6aeb93dd59b43d4914f9`
- Mimic 10D Action Semantics: `[translation(3) in meters, rot6(6) continuous 6D rotation matrix, gripper(1)]`
  - Source: `/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab/src/franka_wrist_camera_scene/mimic_video/geometry.py`
  - SHA256: `167608d28fb99af48ee4293e19945a32cc7c61ecd70df5c35075cdf594be0253`
- Round-Trip Tests: 2000 random cases + identity
  - Max Error: `1.86e-9` (strict tolerance `1e-6`)
  - Provenance Complete: `YES`

## 2. Implementation Files & Tests
- Files created under `implementation/`:
  - `action_adapter.py`
  - `c0_dynamics.py`
  - `candidate_features.py`
  - `constants.py`
  - `dataset.py`
  - `model.py`
  - `train.py`
  - `evaluate.py`
  - `calibration.py`
  - `metrics.py`
  - `materialize.py`
- Static no-stub scan: `PASSED` (no TODO/FIXME/pass/ellipsis)
- Unit Tests: `20 / 20 PASSED` (in 0.049s)

## 3. Full-Corpus Materialization
- Root: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/derived_datasets/isaac_mimic_h10_c0dyn_v1`
- Total Rows: `75,603`
  - Train Rows: `52,825` (3,840 positive / 48,985 negative)
  - Validation Rows: `11,410`
  - Held-out Test Rows: `11,368`
- Calculated Train pos_weight: `12.756510416666666`
- Finite Check: `100% FINITE (0 NaN / 0 Inf)`
- Candidate0 Recurrence Parity: `100% PASSED`
  - Worst max-abs error: `0.0`
- Normalization SHA256: `40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`
- Dataset Manifest SHA256: `730ac7e73ac31047490b81c00955bc1d46fd809e016069a530a71f2112ae3ef3`
