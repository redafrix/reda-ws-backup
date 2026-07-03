# Sam Experiment Index

| Status | Kind | Experiment | Original path |
|---|---|---|---|
| `host_offline_result_known_from_audit` | `realtime_run` | [sam_w0_seen_task7](../entries/sam/sam__realtime_deployment__runs__baseline_same_seed_4worker_20260601__sam_w0_seen_task7/README.md) | `/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment/runs/baseline_same_seed_4worker_20260601/sam_w0_seen_task7` |
| `host_offline_result_known_from_audit` | `realtime_run` | [sam_w1_ood_task8](../entries/sam/sam__realtime_deployment__runs__baseline_same_seed_4worker_20260601__sam_w1_ood_task8/README.md) | `/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment/runs/baseline_same_seed_4worker_20260601/sam_w1_ood_task8` |
| `host_offline_result_known_from_audit` | `realtime_run` | [sam_w0_seen_task7](../entries/sam/sam__realtime_deployment__runs__riskaware_4worker_20260529__sam_w0_seen_task7/README.md) | `/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment/runs/riskaware_4worker_20260529/sam_w0_seen_task7` |
| `host_offline_result_known_from_audit` | `realtime_run` | [sam_w1_ood_task8](../entries/sam/sam__realtime_deployment__runs__riskaware_4worker_20260529__sam_w1_ood_task8/README.md) | `/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment/runs/riskaware_4worker_20260529/sam_w1_ood_task8` |
| `complete` | `realtime_run` | topk8_v2b_feature_preserving_adaptive_horizon | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2b_feature_preserving_adaptive_horizon_20260610` |
| `complete` | `realtime_run` | topk8_v2c_h5_adaptive_horizon | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2c_h5_adaptive_horizon_20260610` |
| `complete` | `realtime_run` | topk8_v2d_commit_gate | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2d_commit_gate_20260610` |
| `complete` | `realtime_run` | timeout800_selected_cap_100ep | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615` |

## Latest Sam Result: Timeout800 Selected-Cap 100ep

Source report: `../source_reports/sam/reports/SAM_TIMEOUT800_SELECTED_CAP_100EP_FINAL_ANALYSIS_20260616.md`

| Policy | Success | Rate | Mean steps |
|---|---:|---:|---:|
| Original SimVLA | 1,716/1,800 | 95.33% | 153.98 |
| Modified SimVLA | 1,744/1,800 | 96.89% | 138.68 |
| Selected-cap risk-aware | 1,754/1,800 | 97.44% | 133.02 |

Paired results: selected-cap is +38 vs Original SimVLA and +10 vs Modified SimVLA. This run used `max_steps=800`, so it must be interpreted separately from the 300-step OOD runs.
