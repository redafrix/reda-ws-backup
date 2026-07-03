# Deep Experiment Coverage Audit - 2026-07-03

This audit was created after the user requested a slower, more complete pass over every experiment map and archived experiment family. It is a coverage audit, not a new scientific result. Its job is to make future Codex/Gemini sessions find the same artifacts quickly and avoid losing older runs.

## Method

- Read the existing local catalog files under `fiper_ws/experiment_catalog`.
- Scanned local/Batman, Bob, Sam, and Dean workspaces for experiment-like roots and key files (`episode_summaries.jsonl`, `run_manifest.json`, `metrics.json`, `results.json`, `thresholds.json`, reports, scripts, and model/report markers).
- Reduced raw files into experiment roots, then compared those roots against the text already present in the catalog maps.
- Separately parsed high-value `episode_summaries.jsonl` files for counts and per-task success where that was cheap and safe.
- Kept the raw scan outputs in `/tmp/internship_deep_audit_20260703`; committed only this report and the compact summary manifest.

## Fresh Scan Counts

| Host | Reduced experiment roots | Filtered roots not clearly covered before |
|---|---:|---:|
| `bob` | 1747 | 44 |
| `batman` | 909 | 347 |
| `dean` | 146 | 53 |
| `sam` | 86 | 1 |
| **Total** | **2888** | **445** |

Important: the filtered-missing number still includes many local archives, cloned-package internals, and smoke subfolders. It is a triage signal, not a claim that 445 scientific campaigns were missing.

## Catalog Issues Found

- `CROSS_MACHINE_EXPERIMENT_MAP_20260703.md`, `HOST_WORKSPACE_MAP.md`, and `GIT_SYNC_PLAN_20260703.md` still said the local Git repo was broken. That became stale after the repo was rebuilt and pushed on 2026-07-03.
- `manifests/bob.json`, `manifests/dean.json`, and `manifests/batman.json` are old June snapshots; `manifests/sam.json` is absent locally. Treat them as historical, not complete current truth.
- Several real experiment families were only present in remote folders or archives, not surfaced in the main current maps.
- Some existing entries mixed “running/partial” status with later completed files. Example: OpenVLA H1 follow-up now has 1800 parsed rows and should no longer be treated as only `1720/1800` based on older text.

## High-Priority Roots Added Back To The Mental Map

### OpenVLA main OOD H8 vs risk H1/H8

- Host: `Bob`
- Path: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`
- Evidence checked: 3600 rows; paired policies total 1990 success / 1610 fail; per-policy map already records H8 976/1800 and risk 1014/1800.

### OpenVLA H1 follow-up

- Host: `Bob`
- Path: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_h1_100ep_20260619`
- Evidence checked: 1800 rows parsed; 1022 success / 778 fail; older maps saying partial/interrupted are stale.

### Pi0.5 OOD18 10ep smoke/full

- Host: `Bob`
- Path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625`
- Evidence checked: 180 rows for basic and 180 rows for risk; both 176/180 success in parsed JSONL.

### Pi0.5 official OOD18 100ep

- Host: `Bob`
- Path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625`
- Evidence checked: 1800 basic rows = 1754 success; 1800 risk rows = 1736 success.

### Pi0.5 official goal-swap 50ep

- Host: `Bob`
- Path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625`
- Evidence checked: 500 basic rows = 161 success; 500 risk rows = 166 success; action-change summary already in map.

### Pi0.5 frozen local goal-object dataset

- Host: `Bob`
- Path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_20260625`
- Evidence checked: 4090 rows in episode summaries; 3298 success / 792 fail; task9 has 0/409 success due local rack issue.

### Dean 20260605 goal-object production exact/continuous

- Host: `Dean`
- Path: `/home/dean/fiper_goal_object_collection_20260605/runs/production_20260605`
- Evidence checked: exact_200 chunk10 162/200 success; exact_200 receding 153/200; continuous chunk10 14005/17409; continuous receding 2072/2745.

### Dean TDQC/SimVLA legacy evaluations

- Host: `Dean`
- Path: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro` and `.../runs/tdqc_calibrator`
- Evidence checked: Dozens of JSON metric/report roots exist; catalog should treat them as legacy evidence, not current H10 TopK8 model evidence.

### Sam video review reels

- Host: `Sam`
- Path: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616`
- Evidence checked: Contains OOD selected-cap and goal-object video-manifest evidence useful for visual/manual review provenance.

### Bob v2_018 clean rerun

- Host: `Bob`
- Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/re_run_v2_018_audit_20260624/CLEAN_OFFLINE_ORIGINAL_FIPER_VS_V2018_REPORT.md`
- Evidence checked: Clean rerun verifies v2_018 selected q95 K3: seen FA 16.2%, OOD FA 26.1%, OOD failure det 95.2%; close to audited 25.59% OOD FA.

## Missing/Weakly Covered Families From The Fresh Scan

### Bob Pi0.5 uncovered subruns

- Count in filtered missing scan: 18
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_ood_18task_10ep_eval_no_task9_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_ood_18task_10ep_eval_no_task9_20260625/offline_ood_eval_metrics.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_ood_18task_10ep_eval_no_task9_20260625/PI05_NO_TASK9_OOD_OFFLINE_EVAL_REPORT_20260625.md`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_smoke_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_smoke_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_smoke_20260625/policy_pi05_basic_h10/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625/policy_pi05_basic_h10/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_no_task9_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_no_task9_20260625/metrics.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_no_task9_20260625/models/thresholds.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_q95mass1_loose_task9_task12_40ep_timeout300_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_q95mass1_loose_task9_task12_40ep_timeout300_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_q95mass1_loose_task9_task12_40ep_timeout300_20260625/policy_pi05_risk_selected_cap_topk8_h10/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_q95mass02_loose_task9_task12_40ep_timeout300_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_q95mass02_loose_task9_task12_40ep_timeout300_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_q95mass02_loose_task9_task12_40ep_timeout300_20260625/policy_pi05_risk_selected_cap_topk8_h10/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_always_lowest_task13_task14_40ep_timeout300_seed430_init20_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_always_lowest_task13_task14_40ep_timeout300_seed430_init20_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_always_lowest_task13_task14_40ep_timeout300_seed430_init20_20260625/policy_pi05_risk_selected_cap_topk8_h10/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_no_task9_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_no_task9_20260625/episode_summaries.jsonl`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_no_task9_20260625/DATASET_FREEZE_REPORT_NO_TASK9_20260625.md`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_no_task9_always_lowest_task13_task14_40ep_timeout300_seed430_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_no_task9_always_lowest_task13_task14_40ep_timeout300_seed430_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_no_task9_always_lowest_task13_task14_40ep_timeout300_seed430_20260625/policy_pi05_risk_selected_cap_topk8_h10/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_no_task9_always_lowest_task13_task14_40ep_timeout300_seed430_v2_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_no_task9_always_lowest_task13_task14_40ep_timeout300_seed430_v2_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_no_task9_always_lowest_task13_task14_40ep_timeout300_seed430_v2_20260625/policy_pi05_risk_selected_cap_topk8_h10/run_manifest.json`
- ... 8 additional roots in `manifests/deep_audit_summary_20260703.json`.

### Bob OpenVLA smoke/followup roots

- Count in filtered missing scan: 4
- `bob` `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke3`  Examples: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke3/run_manifest.json`, `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke3/episode_summaries.jsonl`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/openvla_scripts`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/openvla_scripts/clean_openvla_goal_object_final_dataset.py`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/openvla_scripts/openvla_old6000_to_goal_object_ood_eval_20260619.py`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke`  Examples: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke2`  Examples: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke2/run_manifest.json`

### Bob risk-matrix campaign

- Count in filtered missing scan: 1
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/bob_risk_matrix_campaign_20260605`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/bob_risk_matrix_campaign_20260605/README.md`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/bob_risk_matrix_campaign_20260605/configs/v2_018_only.json`

### Bob/Sam goal-object-OOD audit roots

- Count in filtered missing scan: 7
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_smoke_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_smoke_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_smoke_20260625/policy_pi05_basic_h10/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625`  Examples: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625/live_status.json`, `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625/policy_pi05_basic_h10/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_audit_20260609`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_audit_20260609/config_ood_audit.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_audit_20260609/bundle/verification/episode_identity_table.csv`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke3`  Examples: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke3/run_manifest.json`, `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke3/episode_summaries.jsonl`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_full_sweep_20260609`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_full_sweep_20260609/run_production_sweep_ood.py`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_full_sweep_20260609/src/run_policy_matrix.py`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke`  Examples: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke/run_manifest.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke2`  Examples: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_risk_100ep_20260618_smoke2/run_manifest.json`

### Bob clean v2_018 rerun

- Count in filtered missing scan: 1
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/re_run_v2_018_audit_20260624`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/re_run_v2_018_audit_20260624/runner_snapshot.py`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/re_run_v2_018_audit_20260624/dataset_manifest.json`

### Dean goal-object collection workspace

- Count in filtered missing scan: 6
- `dean` `/home/dean/fiper_goal_object_collection_20260605/runs/parallel_benchmark`  Examples: `/home/dean/fiper_goal_object_collection_20260605/runs/parallel_benchmark/chunk10/live_status.json`, `/home/dean/fiper_goal_object_collection_20260605/runs/parallel_benchmark/chunk10/episode_summaries.jsonl`
- `dean` `/home/dean/fiper_goal_object_collection_20260605/runs/smoke_receding`  Examples: `/home/dean/fiper_goal_object_collection_20260605/runs/smoke_receding/live_status.json`, `/home/dean/fiper_goal_object_collection_20260605/runs/smoke_receding/episode_summaries.jsonl`
- `dean` `/home/dean/fiper_goal_object_collection_20260605/runs/smoke_chunk10`  Examples: `/home/dean/fiper_goal_object_collection_20260605/runs/smoke_chunk10/live_status.json`, `/home/dean/fiper_goal_object_collection_20260605/runs/smoke_chunk10/episode_summaries.jsonl`
- `dean` `/home/dean/fiper_goal_object_collection_20260605/runs/single_receding_benchmark`  Examples: `/home/dean/fiper_goal_object_collection_20260605/runs/single_receding_benchmark/live_status.json`, `/home/dean/fiper_goal_object_collection_20260605/runs/single_receding_benchmark/episode_summaries.jsonl`
- `dean` `/home/dean/fiper_goal_object_collection_20260605/runs/continuous_smoke`  Examples: `/home/dean/fiper_goal_object_collection_20260605/runs/continuous_smoke/chunk10/live_status.json`, `/home/dean/fiper_goal_object_collection_20260605/runs/continuous_smoke/chunk10/episode_summaries.jsonl`
- `dean` `/home/dean/fiper_goal_object_collection_20260605/libero_goal_object_reproduction_bundle_20260605`  Examples: `/home/dean/fiper_goal_object_collection_20260605/libero_goal_object_reproduction_bundle_20260605/README.md`, `/home/dean/fiper_goal_object_collection_20260605/libero_goal_object_reproduction_bundle_20260605/MANIFEST.json`

### Dean SimVLA/TDQC legacy roots

- Count in filtered missing scan: 34
- `dean` `/home/redafrix/SimVLA_modified/folderu/runs/tdqc_calibrator`  Examples: `/home/redafrix/SimVLA_modified/folderu/runs/tdqc_calibrator/TDQC Model Comparison.md`, `/home/redafrix/SimVLA_modified/folderu/runs/tdqc_calibrator/phase2_tdqc_raw_pro_4000_20260428_171248_raw_lstm_w50/feature_stats.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_balanced_50_50_20260512_121118/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_balanced_50_50_20260512_121118/raw_batches/libero_spatial_object__task0_batch13_seed50013.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_balanced_50_50_20260512_121118/raw_batches/libero_spatial_object__task1_batch14_seed51014.metrics.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_155941/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_155941/raw_batches/libero_spatial_object__task0_batch3_seed70003.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_155941/raw_batches/libero_spatial_object__task1_batch13_seed71013.metrics.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_balanced_50_50_20260512_120800/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_balanced_50_50_20260512_120800/raw_batches/libero_spatial_object__task0_batch13_seed50013.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_balanced_50_50_20260512_120800/raw_batches/libero_spatial_object__task1_batch14_seed51014.metrics.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_swap_smoke_20260512_164014/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_swap_smoke_20260512_164014/raw_batches/libero_spatial_object__task1_batch13_seed71013.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_swap_smoke_20260512_164014/raw_batches/libero_spatial_object__task1_batch19_seed71019.metrics.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_tasks3_9_hard_only_20260513_092952/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_tasks3_9_hard_only_20260513_092952/raw_batches/libero_spatial_object__task3_batch1_seed73001.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_tasks3_9_hard_only_20260513_092952/raw_batches/libero_spatial_object__task3_batch2_seed73002.metrics.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_160822/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_160822/raw_batches/libero_spatial_object__task0_batch1_seed70001.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_160822/raw_batches/libero_spatial_object__task2_batch0_seed72000.metrics.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_swap_tasks3_5_smoke_20260513_100221/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_swap_tasks3_5_smoke_20260513_100221/raw_batches/libero_spatial_swap__task5_batch0_seed85000.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_swap_tasks3_5_smoke_20260513_100221/raw_batches/libero_spatial_swap__task4_batch0_seed84000.metrics.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_tasks3_5_extra_hard_smoke_20260513_110123/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_tasks3_5_extra_hard_smoke_20260513_110123/raw_batches/libero_spatial_object__task3_batch0_seed93000.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_tasks3_5_extra_hard_smoke_20260513_110123/raw_batches/libero_spatial_object__task4_batch0_seed94000.metrics.json`
- `dean` `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_162402/raw_batches`  Examples: `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_162402/raw_batches/libero_spatial_object__task2_batch0_seed72000.metrics.json`, `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro/phase2_tdqc_spatial_object_hard_smoke_20260512_162402/raw_batches/libero_spatial_object__task0_batch0_seed70000.metrics.json`
- ... 24 additional roots in `manifests/deep_audit_summary_20260703.json`.

### Sam/local video review reels

- Count in filtered missing scan: 2
- `sam` `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616`  Examples: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616/run_goal_object_render.py`, `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616/collect_fiper_uncertainty_receding_dean_v1.py`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/reports_and_notes/presenation/video_reels_20260616`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/reports_and_notes/presenation/video_reels_20260616/VIDEO_REELS_CREATION_REPORT.md`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/reports_and_notes/presenation/video_reels_20260616/basic_goal_reel_manifest.json`

### Local archived experiment material

- Count in filtered missing scan: 347
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/pi05_scripts`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/pi05_scripts/run_pi05_q95mass1_2task.py`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/pi05_scripts/eval_pi05_official_ood_two_heads_20260625.py`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/openvla_scripts`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/openvla_scripts/clean_openvla_goal_object_final_dataset.py`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/openvla_scripts/openvla_old6000_to_goal_object_ood_eval_20260619.py`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/pi05_goal_swap_task_official_video_smoke_20260625/libero_goal_task/policy_pi05_basic_h10`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/pi05_goal_swap_task_official_video_smoke_20260625/libero_goal_task/policy_pi05_basic_h10/episode_summaries.jsonl`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/pi05_goal_swap_task_official_video_smoke_20260625/libero_goal_task/policy_pi05_basic_h10/run_manifest.json`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/pi05_goal_swap_task_official_video_smoke_20260625/libero_goal_swap/policy_pi05_basic_h10`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/pi05_goal_swap_task_official_video_smoke_20260625/libero_goal_swap/policy_pi05_basic_h10/episode_summaries.jsonl`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/pi05_goal_swap_task_official_video_smoke_20260625/libero_goal_swap/policy_pi05_basic_h10/run_manifest.json`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_second_pass_20260602/codex_reports/stage7`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_second_pass_20260602/codex_reports/stage7/run_stage7_multi_expert_target_experiments.py`, `/home/redafrix/tests/internship/archive/root_cleanup_second_pass_20260602/codex_reports/stage7/stage7_hard_task_scan.md`
- `batman` `/home/redafrix/tests/internship/archive/workspace_cleanup_20260602`  Examples: `/home/redafrix/tests/internship/archive/workspace_cleanup_20260602/merged_smoke_test_results.json`, `/home/redafrix/tests/internship/archive/workspace_cleanup_20260602/check_suites3.py`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/libero_pro_simvla_audit_20260623/files/simvla_modified_risk_topk8_h10_20260608`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/libero_pro_simvla_audit_20260623/files/simvla_modified_risk_topk8_h10_20260608/README_DEPLOY.md`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/libero_pro_simvla_audit_20260623/files/simvla_modified_risk_topk8_h10_20260608/MANIFEST.json`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_second_pass_20260602/codex_reports/stage8`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_second_pass_20260602/codex_reports/stage8/stage8_final_72h_audit_before_expansion.md`, `/home/redafrix/tests/internship/archive/root_cleanup_second_pass_20260602/codex_reports/stage8/stage8_plan_and_smoke_status.md`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/official_fiper_scripts`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/official_fiper_scripts/wait_then_run_official_fiper_eval_20260622.sh`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/official_fiper_scripts/run_official_fiper_ood180_cap300_threshold_sweep_20260629.py`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/libero_pro_simvla_audit_20260623/files/SimVLA_modified/phase2_tdqc`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/libero_pro_simvla_audit_20260623/files/SimVLA_modified/phase2_tdqc/dataset.py`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/video_and_suite_artifacts/libero_pro_simvla_audit_20260623/files/SimVLA_modified/phase2_tdqc/model.py`
- ... 337 additional roots in `manifests/deep_audit_summary_20260703.json`.

### Official FIPER prep/materialization roots

- Count in filtered missing scan: 2
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/seen_goal_object_fiper_subset`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/seen_goal_object_fiper_subset/selected_episodes.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/seen_goal_object_fiper_subset/SPLIT_SUMMARY.md`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/official_fiper_scripts`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/official_fiper_scripts/wait_then_run_official_fiper_eval_20260622.sh`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/official_fiper_scripts/run_official_fiper_ood180_cap300_threshold_sweep_20260629.py`

### Cross-suite per-dataset roots

- Count in filtered missing scan: 13
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_libero10_object_100`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_libero10_object_100/results.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_libero10_object_100/split_episode_ids.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_goal_task_100`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_goal_task_100/results.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_goal_task_100/split_episode_ids.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_goal_object_ood_180`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_goal_object_ood_180/results.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_goal_object_ood_180/split_episode_ids.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_spatial_object_100`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_spatial_object_100/results.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_spatial_object_100/split_episode_ids.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_object_object_100`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_object_object_100/results.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/train_seen_goal_object_eval_object_object_100/split_episode_ids.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_swap_100_smoke`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_swap_100_smoke/run_manifest.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_swap_100_smoke/live_status.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/source_seen_goal_object_hf_official_1000_smoke`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/source_seen_goal_object_hf_official_1000_smoke/run_manifest.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/source_seen_goal_object_hf_official_1000_smoke/live_status.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_task_100_smoke`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_task_100_smoke/run_manifest.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_task_100_smoke/live_status.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_object_ood_180_smoke`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_object_ood_180_smoke/run_manifest.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_object_ood_180_smoke/live_status.json`
- `bob` `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/libero10_object_100_smoke`  Examples: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/libero10_object_100_smoke/run_manifest.json`, `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/libero10_object_100_smoke/live_status.json`
- ... 3 additional roots in `manifests/deep_audit_summary_20260703.json`.

### Isaac/IsaacLab archived material

- Count in filtered missing scan: 116
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/VERIFIED_STATUS.md`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_checkpoints/STAGE4_WORKING_BASELINE_20260611/RESTORE_GUIDE.md`
- `batman` `/home/redafrix/tests/internship/isaac_pi05_work`  Examples: `/home/redafrix/tests/internship/isaac_pi05_work/run_pi05_droid_pick_place_rollout.sh`, `/home/redafrix/tests/internship/isaac_pi05_work/run_pi05_droid_reaching_rollout.sh`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/code/dynamic-vla-static-v1`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/code/dynamic-vla-static-v1/run.py`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/code/dynamic-vla-static-v1/README.md`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/code/dynamic-vla`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/code/dynamic-vla/run.py`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/code/dynamic-vla/README.md`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/006_final_dataset_readiness`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/006_final_dataset_readiness/readiness_results.json`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/checkpoint_reference`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/checkpoint_reference/VERIFIED_STATUS.md`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/checkpoint_reference/RESTORE_GUIDE.md`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/reports/real_collision_viewer`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/reports/real_collision_viewer/placed_objects.json`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/reports/real_collision_viewer/HOW_TO_ENABLE_COLLISION_OVERLAY.md`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/dynamic-vla`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/dynamic-vla/run.py`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/dynamic-vla/README.md`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/README_PORTABLE_PACK.md`, `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_exports/dynamicvla_scripted_collection_portable_pack/SAFETY_SCAN.md`
- `batman` `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/bob_isaac6_setup_reports`  Examples: `/home/redafrix/tests/internship/archive/root_cleanup_20260629/isaaclab_old/bob_isaac6_setup_reports/BOB_ISAAC6_PREFLIGHT_REPORT.md`
- ... 106 additional roots in `manifests/deep_audit_summary_20260703.json`.

## Explicit Corrections To Carry Forward

- OpenVLA H1 follow-up should be interpreted from the current Bob JSONL as 1800/1800 parsed rows unless a newer live check contradicts it.
- Pi0.5 local goal-object task9 failures are tied to the local rack/scene issue; official goal-object and official OOD/swap runs should be treated separately.
- Dean `fiper_goal_object_collection_20260605` is a major historical source of 17,409 chunk10 episodes and 2,745 receding episodes; do not let newer Bob/Sam paths hide it.
- The Bob clean `re_run_v2_018_audit_20260624` report is the clean bridge between original FIPER-style comparisons and the audited v2_018 baseline.
- The local archive folders are not disposable from a provenance standpoint: they contain Stage6-9 reports/scripts, official FIPER scripts, Pi0.5/OpenVLA scripts, video-smoke material, and old Isaac work.
- `BIG_ARTIFACTS_NOT_IN_GIT_20260703.md` remains the substitute for tensors, checkpoints, raw JSONL, videos, and external repos.

## What Was Not Done

- The raw scan JSON files were not committed because they are temporary and together exceed 10 MB.
- Package internals, Python environment folders, and cloned upstream repos were not converted into individual experiment entries unless they contained project-specific reports or run outputs.
- No remote datasets, tensors, videos, checkpoints, or raw rollout JSONL files were staged for Git.

## Durable Files From This Audit

- This report: `fiper_ws/experiment_catalog/DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md`.
- Compact machine-readable summary: `fiper_ws/experiment_catalog/manifests/deep_audit_summary_20260703.json`.
- Temporary raw scans: `/tmp/internship_deep_audit_20260703/*.json` on Batman/local only.
