# Stage 9 Final Collection Plan

Status: generated but not launched.

Do not launch final collection yet. Required fixes first:

1. Add after-image/video capture for every candidate rollout.
2. Parse target object and goal/receptacle from BDDL predicates or task metadata.
3. Replace generic approach-to-any-object GOOD with task-aware progress: target-object approach, grasp/lift, object-to-goal progress, success/reward.
4. Add later-state sampling from real parent rollouts near grasp/placement phases, not only initial approach.
5. Validate object drop and bad collision on states where those events can actually occur.
6. Re-run pilot until labels include GOOD, BAD, and AMBIGUOUS without manually forcing classes.

Proposed final command after fixes:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
nohup python3 -m data_collection_stage9.collect_counterfactual_dataset   --suites <validated_libero_pro_suites>   --task-ids <validated_task_ids>   --states-per-task 50   --simvla-seeds 0 1 2 3 4 5 6 7   --horizon <validated_H>   --history-k 4   --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/final/run_001   --save-images   > asynchvla_ws/stage9_libero_pro_risk_data/logs/final_run_001.log 2>&1 &
```
