# Stage 9 Harder/Later-State Pilot Report

Generated: `2026-05-18T11:27:46`

## Command

```bash
python3 -m data_collection_stage9.collect_counterfactual_dataset \
  --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug \
  --task-ids 0 1 \
  --states-per-task 6 \
  --simvla-seeds 0 1 2 3 4 5 6 7 \
  --horizon 20 \
  --history-k 8 \
  --parent-roll-steps 40 \
  --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/harder_later_state_v3 \
  --save-images
```

## Result

```json
{
  "GOOD_WEAK": 166,
  "AMBIGUOUS": 122
}
```

## Conclusion

The pilot still lacks reliable strong labels. It mainly contains approach/near-grasp behavior, so the corrected labeler assigns `GOOD_WEAK` or `AMBIGUOUS`. BAD is absent because no clear target drop, target-away, no-progress failure, or unstable/contact event occurred in this pilot.

## Reason BAD Is Still Absent

- sampled tasks are relatively easy or mostly early approach
- H=20 may be too short for later failure evidence
- SimVLA seeds did not create clear bad events in this subset
- task-goal parsing is heuristic and may miss placement progress
- collector still does not explicitly select grasp/lift/transport/place phases from rollout logs

## Decision

Do not launch final collection.
