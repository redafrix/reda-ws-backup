# Stage 7 Target Comparison

## Targets Considered

- T0 current normalized action L2: already used through Stage 6 and remains the only fully evaluated target.
- T1 multi-expert min-distance: not run yet; requires building nearest/same-task expert-action pools and replacing single expert L2 with min/softmin distance.
- T2 same-state short rollout progress: blocked until LIBERO/robosuite execution is available.
- T3 success/progress-within-H classification: blocked until rollout logs exist.
- T4 hybrid target: intentionally not stacked before T1/T2/T3 are tested independently.

## Current Result

No new target was trained in this Stage 7 pass. The main blocker is execution rollout availability: Bob's active SimVLA environment imports `libero`, but not `robosuite`, so simulator progress labels cannot be generated yet.

## Recommended Next T1 Command

After the extra-OOD job finishes, implement a CPU-only multi-expert target pass from existing Stage 5 candidate datasets:

```bash
python3 asynchvla_ws/src/data_building/build_multi_expert_min_distance_targets.py \
  --split holdout_libero_object \
  --same-task-k 20 \
  --output asynchvla_ws/data/processed_stage7_targets/holdout_libero_object
```

## Decision

Action L2 is still the operational target. It is not sufficient for the final paper claim until either rollout progress labels or multi-expert validity labels are evaluated.
