# Stage 9 LIBERO-PRO Risk Data Collection Pipeline Report

Generated: `2026-05-18T10:39:09`

## 1. What Was Implemented

Created a Stage 9 LIBERO-PRO counterfactual data-collection framework under `asynchvla_ws/stage9_libero_pro_risk_data/` and `asynchvla_ws/src/data_collection_stage9/`. The collector saves simulator states, history windows, real SimVLA candidate actions from different seeds, short-horizon outcomes after resetting to the same state, and GOOD/BAD/AMBIGUOUS label evidence.

## 2. Exact Scripts Created

- `libero_pro_env_utils.py`
- `sim_state_utils.py`
- `simvla_candidate_sampler.py`
- `history_buffer.py`
- `outcome_metrics.py`
- `label_rules.py`
- `collect_counterfactual_dataset.py`
- `validate_labeler.py`
- `validate_reset_determinism.py`
- `validate_observation_signals.py`
- `validate_controlled_actions.py`
- `validate_simvla_seed_repeatability.py`
- `analyze_dataset_quality.py`
- `export_dataset_splits.py`

## 3. Data Schema

Schema file: `asynchvla_ws/stage9_libero_pro_risk_data/schemas/sample_schema.json`. Samples include metadata, history, current state/proprio/image reference, SimVLA candidate action, short-horizon outcome metrics, and label evidence. Perturbation/task/seed metadata is saved for analysis/splitting only and must not be fed as model input.

## 4. Label Rules

Current rule version: `stage9_rules_v3_sparse_reward_approach_progress`.

Rules are not final-ready. v1 collapsed to BAD because sparse reward/object movement is absent during valid early approach. v3 added object-to-EEF approach evidence, but that collapsed the pilot to GOOD. Generic approach-to-any-object is too weak as a final label criterion.

## 5. Which Signals Are Available From LIBERO-PRO

Signal audit confirms access to reward, success check, EEF pose, gripper state, object-state/object body positions, simulator state get/set, images, and MuJoCo contacts. See `stage9_observation_signal_audit.md`.

## 6. Which Signals Are Missing / Weak

Exact task goal/receptacle distance is not yet parsed. Contact classification is not trusted because static floor-object contacts are abundant at rest. After-images were not saved by the first collector version, only before-images.

## 7. Reset Determinism Result

Same-state reset passed. Reward sequences matched exactly and final simulator state difference was approximately `1.34e-14`. This validates the counterfactual reset mechanism.

## 8. SimVLA Seed Repeatability Result

Same seed reproducibility passed: max absolute action difference `0.0`. Different seed diversity passed: L2 distance `0.1729`.

## 9. Controlled Action Sanity Result

No-op is labeled BAD due to no progress. Large random became AMBIGUOUS. Gripper-only actions became weak GOOD because the controller moves the EEF toward an object; this is a warning that approach-only GOOD is too permissive.

## 10. Object / Drop / Contact / Progress Detection Result

- Object positions and height changes are available.
- Drop detection is implemented but not validated on real drop events.
- Contact access works but raw contacts are diagnostic only.
- Approach progress is available through `*_to_robot0_eef_pos`, but it must be task-aware before final collection.

## 11. Pilot Dataset Stats

```json
[
  {
    "num_samples": 72,
    "label_counts": {
      "BAD": 72
    },
    "out_dir": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/smoke_counterfactual",
    "suites": [
      "libero_object_with_mug",
      "libero_spatial_with_mug",
      "libero_goal_with_mug"
    ],
    "task_ids": [
      0,
      1
    ],
    "states_per_task": 3,
    "simvla_seeds": [
      0,
      1,
      2,
      3
    ],
    "horizon": 10,
    "history_k": 4
  },
  {
    "num_samples": 72,
    "label_counts": {
      "GOOD": 72
    },
    "out_dir": "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/smoke_counterfactual_v2",
    "suites": [
      "libero_object_with_mug",
      "libero_spatial_with_mug",
      "libero_goal_with_mug"
    ],
    "task_ids": [
      0,
      1
    ],
    "states_per_task": 3,
    "simvla_seeds": [
      0,
      1,
      2,
      3
    ],
    "horizon": 20,
    "history_k": 4
  },
  {
    "num_samples": 96,
    "label_counts": {
      "GOOD": 96
    },
    "out_dir": "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/later_state_counterfactual_v1",
    "suites": [
      "libero_object_with_mug",
      "libero_spatial_with_mug",
      "libero_goal_with_mug"
    ],
    "task_ids": [
      0
    ],
    "states_per_task": 8,
    "simvla_seeds": [
      0,
      1,
      2,
      3
    ],
    "horizon": 20,
    "history_k": 4
  }
]
```

Latest real SimVLA pilot rows: `96`. Latest label counts: `{'GOOD': 96}`.

## 12. Label Distribution

Label distribution failed the Stage 9 success criterion. The first pilot collapsed to 100% BAD; after repair it collapsed to 100% GOOD. Therefore labels are not trustworthy enough for final large collection.

## 13. Visual Examples Saved

Visual before-images were saved under `asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/`. No after-images were saved in the current collector; this must be fixed before final collection.

## 14. Suspicious Labels Audit

The main suspicious pattern is class collapse. The latest pilot has no BAD or AMBIGUOUS real SimVLA samples, so BAD/GOOD contradiction analysis is not meaningful yet.

## 15. Whether Labels Are Trustworthy

No. Mechanics are promising, but the labeler is not final-ready. Same-state counterfactual execution works; SimVLA seed diversity works; signal access works. The remaining blocker is label semantics, especially task-aware progress and state selection.

## 16. Whether Final Collection Can Launch

No. Final collection should not launch until label diversity and visual evidence pass validation. Launching now would produce a large one-class dataset and teach the model the wrong thing.

## 17. Exact Next Command To Launch Final Collection

Do not run this until the fixes in `stage9_final_collection_plan.md` are implemented and a balanced pilot passes.

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
python3 -m data_collection_stage9.collect_counterfactual_dataset   --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug   --task-ids 0 1   --states-per-task 10   --simvla-seeds 0 1 2 3 4 5 6 7   --horizon 20   --history-k 4   --parent-roll-steps 40   --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/target_aware_pilot_v1   --save-images
```

## 18. Any Blocker

Primary blocker: label quality. The current labeler lacks task-aware object-goal progress and after-image validation, causing class collapse.

## Report Index

- `stage9_observation_signal_audit.md`
- `stage9_reset_determinism_report.md`
- `stage9_simvla_seed_repeatability.md`
- `stage9_controlled_action_labeler_sanity.md`
- `stage9_object_drop_detection.md`
- `stage9_object_goal_distance_check.md`
- `stage9_contact_check_report.md`
- `stage9_label_distribution_pilot.md`
- `stage9_visual_label_debug_report.md`
- `stage9_label_consistency_audit.md`
- `stage9_pilot_collection_report.md`
- `stage9_label_learnability_smoke.md`
- `stage9_final_collection_plan.md`
