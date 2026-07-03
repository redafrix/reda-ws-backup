# Dataset Map

Updated: 2026-06-23 by workspace catalog audit plus Sam H10 OOD correction.

This file catalogs all known offline training datasets and data collections across hosts.

---

## 1. FIPER Sweep Eternal (Bob + Sam, 2026-05-27)

| Property | Value |
| :--- | :--- |
| **Purpose** | Original FIPER receding-horizon rollout data collection for detector training |
| **Execution Mode** | Receding horizon (execute first action only) |
| **Instances** | `bob_instance_A` (5.7 GB), `bob_instance_B`, `sam_instance_A`, `sam_instance_B` |
| **Bob Path** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260527_combined` |
| **Sam Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260527_combined` |
| **Batman Path** | `/home/redafrix/tests/internship/fiper_ws/data/frozen/fiper_sweep_eternal_20260526_combined` |
| **Data Format** | `fiper_receding_samples.jsonl` per instance |
| **Total Rows** | ~734,266 receding rows (combined) |
| **Status** | Frozen. Used for the original `v2_018_transformer_k16` detector training. |

---

## 2. Dean Object Uncertainty Collection (Dean, 2026-05-29)

| Property | Value |
| :--- | :--- |
| **Purpose** | Data collection with modified SimVLA `ckpt-60000` to capture uncertainty features |
| **Execution Mode** | Receding horizon with uncertainty head active |
| **Workers** | 4 workers (worker_0 through worker_3) |
| **Dean Path** | `/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529` |
| **Episodes** | worker_0: 1,136 / worker_1: 1,043 / worker_2: 1,084 / worker_3: 994 = **4,257 total** |
| **Data Format** | `episode_summaries.jsonl` + `fiper_receding_samples.jsonl` (7.3 GB per worker) per worker |
| **Suites** | Multi-suite (includes `libero_spatial_object`, `libero_goal_object`, etc.) |
| **Status** | Frozen. Used for Dean's offline detector training (all-tasks, OOD last2-taskids, TopK sweep). |

---

## 3. Goal-Object Production Collection (Dean, 2026-06-05)

| Property | Value |
| :--- | :--- |
| **Purpose** | Focused `libero_goal_object` data collection for H10 chunk-10 detector training |
| **Execution Modes** | Dual: chunk10 + receding (paired collections) |
| **Dean Path** | `/home/dean/fiper_goal_object_collection_20260605/runs/production_20260605` |
| **Sub-datasets** | |
| | `exact_200/chunk10` — 200 validated episodes (162 success, 38 failure) |
| | `exact_200/receding` — 200 validated episodes (153 success, 47 failure) |
| | `continuous_100000/chunk10` — 17,409 episodes (ongoing) |
| | `continuous_100000/receding` — 2,745 episodes (ongoing) |
| **Validation** | `EXACT_200_VALIDATED_AND_PROTECTED.json` — validated at 2026-06-05T19:05 |
| **Data Format** | `episode_summaries.jsonl` + `.npz` per episode |
| **Status** | The `exact_200` subset is frozen and validated. The `continuous_100000` dataset continues to grow. |

---

## 4. H10 Continuous Chunk10 Flat (Bob, 2026-06-08)

| Property | Value |
| :--- | :--- |
| **Purpose** | The specific dataset used to train the production H10 base and TopK8 detectors |
| **Execution Mode** | Chunk-10 (H10) |
| **Bob Path** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/inputs/datasets/continuous_chunk10_flat` |
| **Total Episodes** | **17,409** (14,005 successes, 3,404 failures/timeouts) |
| **Split Allocations** | |
| | `failure_train_seen`: 2,724 episodes (68,100 query rows) |
| | `failure_val_seen`: 680 episodes (17,000 query rows) |
| | `success_train_seen`: 11,205 episodes (120,030 query rows) |
| | `success_val_seen`: 1,400 episodes (14,997 query rows) |
| | `success_calib_seen`: 1,400 episodes (15,339 query rows) |
| | `success_test_seen` / `failure_test_seen`: 0 episodes (test evaluated separately on `exact_200_chunk10`) |
| **Task Distribution** | Task 3: 1,368 episodes / Task 6: 1,423 episodes / Task 8: also present |
| **Seed Overlap with Evaluation** | **0%** |
| **Status** | Frozen. This is the canonical training dataset for the H10 detector campaign. |

---

## 5. Dean Offline Detector Models (Dean, 2026-06-01/02)

| Path on Dean | Split | Detectors |
| :--- | :--- | :--- |
| `experiments/dean_all_tasks_full_uncertainty_test_20260601` | all_tasks_random | base, unc_raw |
| `experiments/dean_ood_last2_taskids_full_v1_20260601` | ood_last2_taskids_full | base, unc_raw |
| `experiments/dean_uncertainty_topk_feature_sweep_v1_20260602` | all_tasks_full + ood_last2_taskids_full | unc_topk8, unc_topk16, unc_topk32 |
| `experiments/current_dean_risk_models_20260602` | all_tasks_full + ood_last2_taskids_full | base, unc_topk8 (packaged current models) |

---

## 6. SimVLA Goal Uncertainty Collection (Sam, 2026-06-19)

| Property | Value |
| :--- | :--- |
| **Purpose** | Plain `libero_goal` training data for the SimVLA goal-to-goal-object offline OOD risk test |
| **Execution Mode** | Receding horizon; H10 candidate action chunks; execute first action only |
| **Sam Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/simvla_goal_uncertainty_2000ep_20260619/worker_0` |
| **Launcher** | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/simvla_goal_uncertainty_2000ep_20260619/launch_10000_resume.sh` |
| **Tmux Session** | `simvla_goal_uncertainty_10000ep_20260619` |
| **Target Episodes** | 10,000 total, tasks 0-9 round-robin |
| **Suite** | `libero_goal` |
| **Checkpoint** | Modified SimVLA uncertainty checkpoint `/home/rootalkhatib/test/reda_ws/fiper_ws/checkpoints/ckpt-60000` |
| **Timeout** | 800 steps, so failures/timeouts are retained as long trajectories |
| **Features** | `main_candidate_action_chunk_*`, 8 ACE candidate chunks, history, proprio, `simvla_uncertainty_49d`, `simvla_uncertainty_delta_49d` |
| **Data Format** | `episode_summaries.jsonl`, `fiper_receding_samples.jsonl`, `live_status.json`, `run_manifest.json` |
| **Frozen Dataset** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_uncertainty_final_5410ep_20260622` |
| **Frozen Episode Count** | 5,410 episodes; exactly 541 episodes per task 0-9 |
| **Frozen Outcome Count** | 5,120 successes, 290 failures; failed episodes include timeout-800 trajectories |
| **Validation** | CLI2 validation reported no duplicate episode IDs, all sample rows map to frozen episode IDs, and no NaN/inf in feature arrays |
| **Status** | Frozen/validated as of 2026-06-22. This is the clean plain-`libero_goal` SimVLA source dataset for goal-to-goal-object offline OOD tests. |

---

## 7. SimVLA Goal-Object H10 Canonical Training Dataset Transfer to Sam (Bob → Sam, 2026-06-22)

| Property | Value |
| :--- | :--- |
| **Purpose** | Local Sam copy of the canonical Bob H10 `libero_goal_object` flat training dataset used by the main H10 detector campaign |
| **Bob Source** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/inputs/datasets/continuous_chunk10_flat` |
| **Sam Destination** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_object_h10_continuous_flat_from_bob_20260622` |
| **Content** | `worker_0/episode_summaries.jsonl`, `worker_0/query_samples.jsonl`, `worker_0/transitions.jsonl` |
| **Episode Count** | 17,409 `libero_goal_object` episodes on Bob source |
| **Query Rows** | 235,466 `query_samples.jsonl` rows on Bob source |
| **Transition Rows** | 2,292,591 `transitions.jsonl` rows on Bob source |
| **Transfer Status** | Complete as of 2026-06-22 13:03 CEST. Transfer log verified final line counts: 17,409 episode summaries, 235,466 query rows, 2,292,591 transitions. |

---

## 8. SimVLA LIBERO Goal-Object-OOD H10 180ep Collection (Sam, launched 2026-06-22)

| Property | Value |
| :--- | :--- |
| **Purpose** | Small clean offline evaluation dataset for the official 18-task `libero_goal_object_ood` suite |
| **Sam Dataset Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622` |
| **Original Auto-Eval Result Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622_selected_cap_topk8_offline_eval` |
| **Corrected Eval Result Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace` |
| **Tmux Session** | `simvla_ood180_collect_eval_20260622` |
| **Suite** | `libero_goal_object_ood` |
| **Target Episodes** | 180 total: 10 episodes per task across tasks 0-17 |
| **Execution / Features** | H10 action chunks, 8 ACE candidates, 49D SimVLA uncertainty, history/proprio, timeout 800 |
| **Collection Policy** | Modified SimVLA `ckpt-60000` with uncertainty head; **not** the risk-aware selected-cap policy |
| **Post-Collection Scoring** | Automatically loads selected-cap TopK8 detector from `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8` |
| **Final Dataset Status** | Complete/frozen: 180 episodes, exactly 10 per task across tasks 0-17; 149 successes and 31 failures |
| **Corrected Offline Status** | Complete as of 2026-06-23. Initial evaluator had ACE/metric interpretation issues; corrected evaluator uses the online ACE formula and reports K-window plus mass-threshold metrics. |
| **Corrected Headline** | Saved H10 threshold `q95_mass_0.15` over-alarms on official OOD success episodes (96.0% FA). Stronger mass thresholds expose usable separation: `q95_mass_20` gives 20.8% FA, 96.8% detection, Det@25 90.3%, Det@50 96.8%; `q95_mass_50` gives 2.7% FA, 96.8% detection, Det@25 16.1%, Det@50 90.3%. |
| **Trust** | Dataset is valid for detector-only offline audits. Do not treat this as an online selected-cap replay; it is a threshold/calibration audit for the H10 TopK8 detector. |

---

## 9. SimVLA LIBERO Goal-Object-OOD H10 180ep Cap-300 Derivative (Sam, created 2026-06-23)

| Property | Value |
| :--- | :--- |
| **Source Dataset Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622` |
| **Derived Dataset Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623` |
| **Result Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace` |
| **Report** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace/SIMVLA_H10_TOPK8_OFFICIAL_OOD_CAP300_AUDIT_20260623.md` |
| **Derivation Rule** | Keep rows with `timestep < 300`; success only if original episode succeeded before 300 steps; every episode reaching 300 is relabeled failure. |
| **Counts** | 180 episodes, 143 successes, 37 failures, 28,031 rows; six max-800 successes converted to cap-300 failures. |
| **Corrected Headline** | Cap-300 makes the detector-only audit stricter. `q95_mass_20` gives 18.9% FA, 91.9% detection, Det@25 0.0%, Det@50 83.8%; `q95_mass_50` gives 0.0% FA, 83.8% detection, but no Det@50. |
| **Trust** | Valid derived offline diagnostic. Do not cite as a separately collected cap-300 rollout dataset. |

## 10. Official FIPER Materialized Dataset (Dean, 2026-06-23)

| Property | Value |
| :--- | :--- |
| **Purpose** | Materialized official-format observation embeddings and action predictions for FIPER baseline training/evaluation |
| **Execution Mode** | Sharded materialization from MuJoCo states |
| **Dean Path** | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622/official_fiper_data` |
| **Sub-datasets** | `libero_fold00/processed_rollouts` and `libero_fold00_hygiene/processed_rollouts` |
| **Data Format** | `obs_embeddings.pt` (170,943, 960), `action_preds.pt` (170,943, 9, 10, 7), `metadata.pkl` |
| **Status** | Frozen and validated (`VALIDATION_PASS`). Used for Option A/B runs. |

## 11. Pi0.5 Goal-Object H10 Frozen Dataset (Bob, 2026-06-25)

| Property | Value |
| :--- | :--- |
| **Purpose** | Clean frozen round-robin dataset for Pi0.5 risk head training/evaluation |
| **Execution Mode** | Horizon 10 (H10) chunking, zeroed wrist, mask = True |
| **Bob Path** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_20260625` |
| **Episode Count** | 4,090 episodes (exactly 409 episodes per task 0..9) |
| **Success/Failure** | 3,298 success / 792 failure |
| **Row Count** | 1,082,299 total timestep rows |
| **Exclusions** | Discarded rounds 0 and 1 due to Task 9 infrastructure KeyError errors on rollout index 0 and 1; retained rounds 2..410 |
| **Status** | Frozen and validated (`VALIDATION_PASS`). Used for offline SeqRiskModel training. |

## 12. Pi0.5 Official Goal-Swap Online OOD Dataset (Bob, 2026-06-26)

| Property | Value |
| :--- | :--- |
| **Purpose** | Online selected-cap OOD audit and saved offline scoring dataset for Pi0.5 on official `libero_goal_swap` |
| **Execution Mode** | H10 online execution, max 300 env steps, 50 paired seeds per task |
| **Bob Path** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625` |
| **Policies / Episodes** | `pi05_basic_h10`: 500 episodes; `pi05_risk_selected_cap_topk8_h10`: 500 episodes |
| **Suite** | Official `libero_goal_swap`, tasks 0..9 |
| **Saved Records** | Per-policy `episode_summaries.jsonl`, `query_records.jsonl`, `step_records.jsonl`, and videos |
| **Online Outcome** | Basic: 161/500 = 32.20%; selected-cap risk: 166/500 = 33.20%; net +5 successes |
| **Offline Result Path** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_goal_swap_10task_50ep_two_heads_eval_20260625` |
| **Threshold Sweep JSON** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_goal_swap_10task_50ep_two_heads_eval_20260625/old_with_task9_q95_mass_threshold_sweep_20260626.json` |
| **Status** | Complete and validated as an online/offline audit dataset. Not a frozen training dataset. |

## 13. SimVLA Official LIBERO Goal-Object H10 Basic 500ep Dataset (Bob, launched 2026-06-26)

| Property | Value |
| :--- | :--- |
| **Purpose** | Run official SimVLA basic H10 on byte-identical official `libero_goal_object` BDDL/init states while preserving the local modified `libero_goal_object` suite untouched |
| **Execution Mode** | Official SimVLA checkpoint, fixed H10 receding execution, max_steps 800 |
| **Official BDDL Copy** | `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files/libero_goal_object_official` |
| **Official Init Copy** | `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files/libero_goal_object_official` |
| **Byte-Identity Check** | PASS against local official reference `/home/redafrix/tests/internship/libero_pro_simvla_audit_20260623/files/LIBERO-PRO-HF`; 10 BDDL + 10 init files matched by SHA256 |
| **Bob Output Path** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_basic_500ep_20260626` |
| **Script** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/scripts/run_simvla_official_goal_object_h10_50ep_20260626.py` |
| **Log** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/logs/simvla_official_libero_goal_object_h10_basic_500ep_20260626/run.log` |
| **Episode Plan** | 500 episodes: 50 init states per task, tasks 0..9, round-robin by init state then task, deterministic random eval seeds |
| **Final Episodes** | 500/500 complete; exactly 50 init states per task, tasks 0..9 |
| **Final Success** | 422/500 = 84.40%; 78 failures |
| **Per-Task Success** | task0 49/50, task1 49/50, task2 50/50, task3 13/50, task4 49/50, task5 50/50, task6 35/50, task7 50/50, task8 49/50, task9 28/50 |
| **Coverage Check** | PASS: exactly init state indices 0..49 per task; no duplicate `(task_id, initial_state_index)` pairs |
| **Error Check** | PASS: no run-log or summary errors in the final report |
| **Status** | Complete and validated as official basic SimVLA H10 reference dataset |

## 14. Pi0.5 Official Goal-Object-OOD 18-Task Online/Offline Dataset (Bob, 2026-06-27)

| Property | Value |
| :--- | :--- |
| **Purpose** | Full Pi0.5 online selected-cap OOD audit and saved offline scoring dataset on official `libero_goal_object_ood` |
| **Execution Mode** | H10 online execution, max 300 env steps, 100 paired seeds per task |
| **Bob Path** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625` |
| **Policies / Episodes** | `pi05_basic_h10`: 1,800 episodes; `pi05_risk_selected_cap_topk8_h10`: 1,800 episodes |
| **Suite** | Official `libero_goal_object_ood`, tasks 0..17 |
| **Saved Records** | Per-policy `episode_summaries.jsonl`, `query_records.jsonl`, `step_records.jsonl`, and videos |
| **Online Outcome** | Basic: 1,754/1,800 = 97.44%; selected-cap risk: 1,736/1,800 = 96.44%; net -18 successes |
| **Action Modification Audit** | Risk policy made 759 action changes across 529/1,800 episodes; 645 changes on successes and 114 on failures |
| **Offline Result Path** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_ood_18task_100ep_two_heads_eval_20260625` |
| **Report** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_ood_18task_100ep_two_heads_eval_20260625/PI05_OFFICIAL_OOD_18TASK_TWO_HEADS_REPORT_20260625.md` |
| **Status** | Complete and validated as an online/offline audit dataset. Not a frozen training dataset. |

## 15. Sam Official LIBERO Goal-Object H10 Uncertainty Collection Setup (2026-06-26)

| Property | Value |
| :--- | :--- |
| **Purpose** | Prepare a second large H10 uncertainty/ACE dataset using modified SimVLA on byte-identical official `libero_goal_object`, analogous to the main 17K risk-training dataset but without the local modified goal-object suite. |
| **Host** | Sam (`PCROBOTUBUNTU05`) only |
| **Official BDDL Copy** | `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files/libero_goal_object_official` |
| **Official Init Copy** | `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files/libero_goal_object_official` |
| **Official Source** | Copied from the Bob byte-identical official suite previously validated against `/home/redafrix/tests/internship/libero_pro_simvla_audit_20260623/files/LIBERO-PRO-HF` |
| **Byte-Identity Check** | PASS on Sam: 10 BDDL + 10 init files, SHA256 hashes match the Bob official copy. |
| **Collector Script** | `/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/collect_simvla_official_goal_object_uncertainty_20260626.py` |
| **Launch Script** | `/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/run_sam_official_goal_object_uncertainty_collect_20260626.sh` |
| **Default Dataset Target** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626` |
| **Default Episode Target** | 17,410 episodes (`MAX_EPISODES=17410`), tasks 0..9, H10, max steps 800, 8 ACE candidates, 49D uncertainty + 49D delta uncertainty, saved MuJoCo states enabled. |
| **Checkpoint** | `/home/rootalkhatib/test/reda_ws/fiper_ws/checkpoints/ckpt-60000` (`model.safetensors` symlink to the full modified SimVLA checkpoint); SHA256 `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`. |
| **Smoke Dataset** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_smoke_20260626` |
| **Smoke Result** | PASS: 1 official task-0 episode, success, 252 rows, `VALIDATION_PASS=YES`; sample row contains main action chunk `[10,7]`, ACE candidates `[8,10,7]`, uncertainty `[49]`, uncertainty delta `[49]`. |
| **Full Collection Tmux** | `sam_official_goal_object_h10_uncertainty_17410ep_20260626` |
| **Full Collection Log** | `/home/rootalkhatib/test/reda_ws/fiper_ws/logs/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626/outer.log` |
| **First-Round Audit** | PASS after first 10 episodes: strict round-robin tasks 0..9 with episode index `r0`; H10 action chunks `[10,7]`; ACE candidates `[8,10,7]` real/nonzero on all audited rows; 49D uncertainty + 49D delta; TopK8 indices extractable; current proprio 8D; executed action 7D; history entries contain proprio 8D + executed action 7D; no NaN/Inf; official BDDL/init metadata paths only. |
| **Launch Command** | `ssh sam "tmux new-session -d -s sam_official_goal_object_h10_uncertainty_17410ep_20260626 'bash /home/rootalkhatib/test/reda_ws/fiper_ws/scripts/run_sam_official_goal_object_uncertainty_collect_20260626.sh >> /home/rootalkhatib/test/reda_ws/fiper_ws/logs/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626/outer.log 2>&1'"` |
| **Status** | Running on Sam as of 2026-06-29 09:48 CEST; resumable via `--resume`; safe to stop by killing the tmux session after the current episode writes a summary. Current snapshot: 3,166 episodes, 741,495 rows, 2,660 success / 506 failure, no seed collisions, no main/ACE collisions. Disk warning: Sam root partition is 96% used with about 19GB free. |

---

## Provenance Chain

```
Dean object uncertainty collection (4,257 episodes, multi-suite)
  → Dean offline detector training (all_tasks_full, ood_last2_taskids, topk sweep)
  → TopK8 feature selection: dims [6, 21, 25, 27, 23, 2, 26, 24]
  → Old TopK8 detector (hash 0ea8e943...)

Dean goal-object production (17,409 chunk10 episodes, libero_goal_object only)
  → Transferred to Bob as continuous_chunk10_flat
  → H10 base + TopK8 detector training on Bob
  → H10 TopK8 detector (hash 687b5d35...)
  → Production deployment in online campaigns (Task 3/6/8 + OOD goal-swap)
```

## 16. Cross-Suite Official OOD H10 Collection Campaign (Bob, launched 2026-06-30)

| Property | Value |
| :--- | :--- |
| **Purpose** | Build multiple official-suite OOD datasets for offline comparison of seen-trained H10 TopK8 risk heads against official FIPER. |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630` |
| **Collector** | Modified SimVLA `ckpt-60000`, H10 action chunks, 8 ACE candidates, 49D uncertainty + saved MuJoCo states. |
| **Timeout Rule** | Max 300 environment steps; any timeout is a failure. |
| **Training Source** | Sam official `libero_goal_object` H10 uncertainty dataset stopped at 4,469 episodes and transferred completely to Bob under `source_seen_goal_object_from_sam_20260630`. This is the only valid seen-source dataset for this campaign. |
| **OOD Targets** | `libero_goal_swap` 100, `libero_goal_task` 100, `libero_goal_object_ood` 180, `libero_spatial` 100, `libero_object` 100, `libero_10` 100. |
| **Excluded Registry Suites** | `libero_goal_relation_ood`, `libero_goal_semantic_ood`, `libero_spatial_object_ood`, `libero_object_object_ood`, `libero_10_object_ood`; excluded because the current Bob official LIBERO-PRO tree has no matching BDDL/init files. |
| **Tmux** | `cross_suite_official_ood_20260630`; transfer tmux `cross_suite_sam_seen_transfer_20260630`. |
| **Live Dataset Audit** | 2026-06-30 16:45 CEST audit checked real JSONL rows, not just manifests. Source seen folder has 4,469 episodes and 48.66GB samples; current `goal_swap_100` has valid H10 `[10,7]` main chunks, ACE `[8,10,7]`, 49D uncertainty + 49D delta, proprio `[8]`, executed action `[7]`, nonempty history after timestep 10, saved BDDL/init metadata, and finite numeric values. |
| **Do Not Use** | Ignore `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/source_seen_goal_object_hf_official_1000`: it is an abandoned 12-episode Bob source smoke/recollection artifact, not the training source. |
| **Status** | Complete as of 2026-07-01 05:48 CEST. Transfer from Sam is complete; Bob collected all requested OOD datasets and completed train/eval. First smoke and live-row schema validation passed: H10, ACE8, 49D uncertainty, saved state NPZ files. |

## 17. Promoted SimVLA H10 TopK8 Official Goal-Object Main Model (Bob, 2026-07-01)

| Property | Value |
| :--- | :--- |
| **Model Name** | `simvla_h10_topk8_official_goal_object_seen_main_20260701` |
| **Purpose** | New promoted reusable main risk model for cross-suite official OOD offline evaluation. |
| **Selection Rule** | Highest source validation AUPRC among the six repeated same-source trainings; OOD performance was not used for checkpoint selection. |
| **Selected Source Experiment** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_goal_swap_100` |
| **Promoted Model Path** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/models/simvla_h10_topk8_official_goal_object_seen_main_20260701` |
| **Model Files** | `model.pt`, `normalization.json`, `results.json`, `PROMOTED_MODEL_MANIFEST.json`, `README.md` |
| **Training Source** | Sam official `libero_goal_object_official` source at `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl` |
| **Validation Selection Metric** | Source val AUPRC 0.9369, source val AUROC 0.9345, selected epoch 1. |
| **Feature Schema** | history `16x21`, action `10x7`, static 51 = action stats 28 + ACE 7 + proprio 8 + TopK8 uncertainty 8. No explicit task ID or timestep input. |
| **Seen-Calibrated Thresholds** | `best_val_f1=0.3560`, `fixed_0.5=0.5000`, `q90_success=0.6905`, `q95_success=0.9054`, `q99_success=0.9976`. |
| **Single-Checkpoint Eval Path** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/eval_promoted_single_model_all_ood_20260701` |
| **Single-Checkpoint Report** | `PROMOTED_SINGLE_MODEL_OOD_EVAL_REPORT_20260701.md` |
| **Status** | Complete. This is now the promoted main model for future reuse in this campaign. |
