# Stage 9 20h Live Dashboard

Updated: `2026-05-19 09:30:01`
Host: `PCROBOTUBUNTU02`
Role: `bob`
Status: `collecting`
Elapsed hours: `13.88`
Dataset root: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/bob_20260518_193710`

## Counts

- total_samples: `37376`
- total_states: `1426`
- label_counts: `{"AMBIGUOUS": 8969, "GOOD_STRONG": 17790, "GOOD_WEAK": 3739, "VALIDATED_BAD": 6878}`
- bad_subtype_counts: `{"action_specific": 2834, "state_context": 4044}`
- bad_reason_counts: `{"large_object_height_drop": 113, "no_progress_strong": 4694, "repeated_same_state_failure_tail_no_progress": 4120, "target_object_dropped": 241, "target_object_moved_away_from_goal": 1, "terminal_failure_with_successful_same_state_alternative": 2834}`
- suspicious_count: `0`
- trace_incomplete_count: `289`
- same_state_missing_count: `0`
- label_evidence_missing_count: `0`
- disk_free_gb: `1412.65`

## Task/Phase

- task_counts: `{"libero_10_with_mug_task0": 768, "libero_10_with_mug_task1": 768, "libero_10_with_mug_task2": 768, "libero_10_with_mug_task3": 768, "libero_10_with_mug_task4": 768, "libero_10_with_mug_task5": 768, "libero_10_with_mug_task6": 768, "libero_10_with_mug_task7": 768, "libero_10_with_mug_task8": 768, "libero_10_with_mug_task9": 768, "libero_goal_with_mug_task0": 1024, "libero_goal_with_mug_task1": 1024, "libero_goal_with_mug_task2": 1024, "libero_goal_with_mug_task3": 1024, "libero_goal_with_mug_task4": 1024, "libero_goal_with_mug_task5": 1024, "libero_goal_with_mug_task6": 768, "libero_goal_with_mug_task7": 768, "libero_goal_with_mug_task8": 768, "libero_goal_with_mug_task9": 768, "libero_object_with_mug_task0": 1024, "libero_object_with_mug_task1": 1024, "libero_object_with_mug_task2": 1024, "libero_object_with_mug_task3": 1024, "libero_object_with_mug_task4": 1024, "libero_object_with_mug_task5": 1024, "libero_object_with_mug_task6": 1024, "libero_object_with_mug_task7": 1024, "libero_object_with_mug_task8": 1024, "libero_object_with_mug_task9": 1024, "libero_spatial_with_mug_task0": 1024, "libero_spatial_with_mug_task1": 1024, "libero_spatial_with_mug_task2": 1024, "libero_spatial_with_mug_task3": 1024, "libero_spatial_with_mug_task4": 1024, "libero_spatial_with_mug_task5": 1024, "libero_spatial_with_mug_task6": 1024, "libero_spatial_with_mug_task7": 1024, "libero_spatial_with_mug_task8": 1024, "libero_spatial_with_mug_task9": 1024}`
- phase_counts: `{"APPROACH": 48, "GRASP_OR_LIFT": 1080, "NEAR_GRASP": 1496, "PLACE_OR_GOAL": 4464, "STUCK_OR_NO_PROGRESS": 15384, "TRANSPORT": 14904}`

## Active Chunk

```json
{
  "chunk": "bob_c003_libero_goal_with_mug_t6_seeds24-31",
  "seeds": [
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31
  ],
  "suite": "libero_goal_with_mug",
  "task_id": 6
}
```
