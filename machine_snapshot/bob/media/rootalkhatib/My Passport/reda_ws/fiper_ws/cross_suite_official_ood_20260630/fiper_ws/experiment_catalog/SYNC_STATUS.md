# Catalog Synchronization Status

Last updated: 2026-06-25 (Pi0.5 offline model complete).

| Host | Catalog state | Raw workspace state | Access state |
|---|---|---|---|
| Batman | Canonical catalog present and updated (2026-06-25) | Obsidian report consolidated. Local reports/configs, forensic audit scripts in `/checks/`. | Available |
| Bob | Full catalog mirror synchronized on 2026-06-25. | Pi0.5 collection stopped safely (4,090 episodes). Offline risk SeqRiskModel trained: test AUROC 0.9534, AUPRC 0.9728. OOD sweeps complete. | Available through `pcrobot` |
| Dean | Full catalog mirror synchronized on 2026-06-16. | Selected-cap 100ep complete and positive: 1,741/1,800 (+15 vs Modified). Delay30 100ep complete and negative. OOD assets resolved via experiment-local fallback. | Available through direct `dean` and fallback `dean-via-bob` |
| Sam | Full catalog mirror synchronized on 2026-06-16. | Sam Timeout800 selected-cap 100ep campaign complete and positive (+10 vs Modified, +38 vs Original). Policy render sweeps active. | Available through `sam` |

## Sam Re-Integration Completed (2026-06-09)

Sam is back online and has been integrated into the workspace experiment catalog. The following actions were taken:
1. Checked and mapped all active/completed run paths and reports on Sam.
2. Created `SAM_WORKSPACE_SCAN_20260609.md` outlining host/workspace specifications and verifying all raw evaluations.
3. Updated `HOST_WORKSPACE_MAP.md` and `SYNC_STATUS.md` to reflect Sam's workspace paths.
4. Created `/home/rootalkhatib/test/reda_ws/fiper_ws/experiment_catalog/` on Sam and synchronized all canonical catalog files.

## Catalog Files Update Log (2026-06-09)

New files created by the workspace catalog audit:
- `TRUSTED_RESULTS_SUMMARY.md` — forensic-verified results with corrected intervention rates
- `MASTER_EXPERIMENT_INDEX.md` — central table of all campaigns
- `DATASET_MAP.md` — all datasets across hosts with provenance chain
- `HOST_WORKSPACE_MAP.md` — host details, SSH configs, GPU specs, paths
- `MODEL_AND_SUITE_IDENTITY.md` — checkpoint/detector hashes and suite verification
- `FORENSIC_AUDIT_MAP.md` — map of the 8-step forensic audit
- `OBSIDIAN_REPORT_ACCURACY_AUDIT_20260609.md` — cross-check of Obsidian report claims

Existing files updated:
- `KEY_RESULTS.md` — added OOD goal-swap results, forensic corrections, updated active work status
- `README.md` — added links to new files, new semantic corrections
- `SYNC_STATUS.md` — this file (updated host statuses)

Backup files (pre-update snapshots):
- `README.md.20260609_115800.bak`
- `KEY_RESULTS.md.20260609_115800.bak`
- `WORKSPACE_MAP.md.20260609_115800.bak`
- `inventory.json.20260609_115800.bak`

## Catalog Files Update Log (2026-06-10)

Updates from the Codex full workspace audit:
- `MASTER_EXPERIMENT_INDEX.md` — corrected Bob Campaign 7 from running to complete, added Bob 0.5 and q95 campaigns, added Sam V2 adaptive-horizon diagnostics.
- `TRUSTED_RESULTS_SUMMARY.md` — added q95 completed net-negative status and Sam V2B/V2C/V2D trusted-negative diagnostics.
- `KEY_RESULTS.md` — added full-suite OOD goal-object summary and adaptive-horizon interpretation.
- `HOST_WORKSPACE_MAP.md` — updated Bob completed q95 status, Dean direct SSH status, and Dean OOD asset caveat.
- `hosts/bob.md` — added recent OOD campaign paths.
- `hosts/sam.md` — added V2D commit-gate experiment entry.
- `CODEX_FULL_WORKSPACE_AUDIT_20260610.md` — direct Codex audit report from raw JSONL/config/host checks.
- `hosts/dean.md` / `MASTER_EXPERIMENT_INDEX.md` — added completed Dean selected-cap 10ep diagnostic and active 100ep confirmation.
- `DEAN_SELECTED_CAP_GATE_20260610.md` — detailed selected-cap result report and 100ep confirmation status.
- `MASTER_EXPERIMENT_INDEX.md` / `DEAN_SELECTED_CAP_GATE_20260610.md` — added completed Dean selected-cap margin-0.10 10ep diagnostic; mechanically valid but not selected for scaling.
- `MASTER_EXPERIMENT_INDEX.md` / `TRUSTED_RESULTS_SUMMARY.md` / `KEY_RESULTS.md` — marked Bob q95 OOD full-suite sweep complete: 1,710/1,800 risk successes, 10 rescues / 18 regressions, net -8 vs modified baseline.
- `DEAN_SELECTED_CAP_GATE_20260610.md` / `CODEX_FULL_WORKSPACE_AUDIT_20260610.md` / `source_reports/dean/reports/DEAN_SELECTED_CAP_INTERIM_FORENSIC_AUDIT_20260610.md` — added direct Codex forensic checks for the active Dean selected-cap 100ep run, including config schema, hashes, Task 0-3 paired results, Task 4 active progress, and the post-hoc `risk_reduction >= 0.08` candidate gate.
- `MASTER_EXPERIMENT_INDEX.md` / `TRUSTED_RESULTS_SUMMARY.md` / `KEY_RESULTS.md` / `source_reports/dean/reports/DEAN_SELECTED_CAP_FINAL_ANALYSIS_20260611.md` — marked Dean selected-cap 100ep full-suite run complete and trusted positive: 1,741/1,800 vs 1,726/1,800, paired 38 rescues / 23 regressions, net +15.
- `MASTER_EXPERIMENT_INDEX.md` / `TRUSTED_RESULTS_SUMMARY.md` — registered active Dean delay30 replication with seeds 400-499 in tmux `dean_selected_cap_delay30_100ep_20260611`.
- `source_configs/dean/realtime_deployment/selected_cap_delay30_100ep_20260611/` — archived the generator and README for the active Dean delay30 replication.
- `MASTER_EXPERIMENT_INDEX.md` / `KEY_RESULTS.md` / `inventory.json` / `hosts/bob.md` — added the June 5 Bob chunk10 modified-vs-official SimVLA diagnostic: modified 80/100, official 78/100, net +2. This is historical diagnostic evidence, not risk-aware evidence.

## Catalog Files Update Log (2026-06-12)

Updates from the selected-cap replication and report cleanup:
- `MASTER_EXPERIMENT_INDEX.md` — marked Bob selected-cap 10ep/100ep and Dean delay30 100ep as complete.
- `TRUSTED_RESULTS_SUMMARY.md` — added final Bob selected-cap 100ep table and Dean delay30 final table.
- `KEY_RESULTS.md` — added Bob selected-cap replication interpretation and updated Dean delay30 verdict.
- `source_reports/bob/reports/BOB_SELECTED_CAP_100EP_FINAL_ANALYSIS_20260612.md` — final Bob 100ep selected-cap report.
- `source_reports/dean/reports/DEAN_SELECTED_CAP_DELAY30_FINAL_ANALYSIS_20260612.md` — final Dean delay30 report.
- Obsidian main report rewritten as a consolidated single-file report with updated results, corrected architecture explanation, and five plot assets under `FIPER Risk-Aware Report 20260602/assets/`.

## Catalog Files Update Log (2026-06-16)

Updates from the pre-push workspace audit and sync:
- `MASTER_EXPERIMENT_INDEX.md` / `TRUSTED_RESULTS_SUMMARY.md` / `KEY_RESULTS.md` / `hosts/sam.md` — registered Sam timeout800 selected-cap 100ep campaign results (Original 1,716/1,800, Modified 1,744/1,800, Selected-cap 1,754/1,800; net +10 vs Modified, +38 vs Original).
- `source_reports/sam/reports/SAM_TIMEOUT800_SELECTED_CAP_100EP_FINAL_ANALYSIS_20260616.md` — registered Sam's final analysis report.
- `SYNC_STATUS.md` — updated with June 16 sync information and workspace/GPU running-process checks.
- Synchronized all updated catalog files to Bob, Sam, and Dean.

## Catalog Files Update Log (2026-06-19)

Updates from the OpenVLA workspace audit, offline cross-dataset tests, and active online OOD run:
- `OPENVLA_EXPERIMENT_MAP_20260619.md` — new canonical OpenVLA map covering Bob workspace setup, required compatibility patches, smoke tests, old/plain-goal dataset, final 1,890 goal-object dataset, offline risk models, cross-dataset OOD tests, active online OOD run, and the portable OOD asset package.
- `README.md` — linked the OpenVLA map and added a semantic warning that OpenVLA results use a different policy and feature schema from SimVLA/FIPER.
- `MASTER_EXPERIMENT_INDEX.md` — added OpenVLA offline risk models, OpenVLA data collection datasets, and the active OpenVLA online OOD run.
- `KEY_RESULTS.md` — added the final OpenVLA goal-object dataset, old-goal to goal-object OOD transfer results, and active OpenVLA online OOD run snapshot.
- `WORKSPACE_MAP.md` — added Bob's OpenVLA workspace root and key OpenVLA artifact roots.
- `README_WORKSPACE_NAVIGATION.md` — linked the new OpenVLA experiment map from the top-level workspace navigation.

Historical 2026-06-19 live OpenVLA online snapshot recorded in the map at that time: tmux `openvla_ood_basic_vs_risk_100ep_20260618`, 2,628/3,600 episodes written; `openvla_basic` complete at 976/1,800 and `openvla_risk_horizon` still partial. This snapshot was superseded by the completed 2026-06-22 result below.

## Catalog Files Update Log (2026-06-19, later OpenVLA diagnostics)

Updates from the OpenVLA risk-input forensic audit, focused horizon diagnostic, and long-run resume:
- `OPENVLA_EXPERIMENT_MAP_20260619.md` — added explicit-input forensic audit showing the Transformer risk heads use no explicit task id or timestep (`static_dim=43`, `history_dim=21`), while stale MLP/GRU baselines had 25D task/timestep inputs and are not used online.
- `OPENVLA_EXPERIMENT_MAP_20260619.md` / `KEY_RESULTS.md` — added the focused task 2/task 8 rescue-seed diagnostic: Basic H=8 = 0/10, Basic H=1 = 3/10, adaptive risk H=1/8 = 10/10 on identical selected seeds.
- `MASTER_EXPERIMENT_INDEX.md` — registered `openvla_risk_input_forensic_audit_20260619` and `openvla_focused_horizon_diagnostic_20260619`.
- `WORKSPACE_MAP.md` — added Bob focused diagnostic output roots and the H=1 diagnostic script path.
- Active OpenVLA online snapshot updated: the long run was paused safely at 2,686/3,600, the focused H=1 diagnostic was run, and the long run was resumed from task 8 seed 96 in tmux `openvla_ood_basic_vs_risk_100ep_20260618`.

## 2026-06-19 Scheduled OpenVLA Fixed-H1 Baseline

- Added `openvla_ood_basic_h1_100ep_20260619` to the OpenVLA map and master index.
- Created Bob runner `src/run_openvla_ood_basic_h1_full_20260619.py`, which uses the same OpenVLA checkpoint, suite, task IDs, seeds 10-109, max steps 800, init-state indexing, and LIBERO-PRO patches as the current online run, but forces `openvla_basic_h1` fixed execution horizon H=1.
- Created Bob waiter `src/wait_then_launch_openvla_basic_h1_after_current_20260619.sh` and launched tmux `openvla_wait_then_basic_h1_20260619`; it waits for the current `openvla_ood_basic_vs_risk_100ep_20260618` summary file to reach 3,600 rows before launching tmux `openvla_ood_basic_h1_100ep_20260619`.
- The H=1 baseline writes to a separate output root: `online_evals/libero_goal_object_ood_openvla_basic_h1_100ep_20260619`.

## 2026-06-22 OpenVLA Online Result Update

- `OPENVLA_EXPERIMENT_MAP_20260619.md` — marked `openvla_ood_basic_vs_risk_100ep_20260618` complete: 3,600/3,600 summaries, zero malformed rows, log ends with `DONE`. Final result: basic H8 976/1,800 = 54.22%; adaptive risk H1/8 1,014/1,800 = 56.33%.
- `KEY_RESULTS.md` / `TRUSTED_RESULTS_SUMMARY.md` / `MASTER_EXPERIMENT_INDEX.md` — replaced stale partial-run language with the completed OpenVLA result.
- Fixed-H1 baseline `openvla_ood_basic_h1_100ep_20260619` is running/healthy on Bob. Snapshot: 1,096/1,800 rows; H1 completed subset 680/1,096 = 62.04%; matching H8 subset 660/1,096 = 60.22%; matching adaptive-risk subset 690/1,096 = 62.96%.

## 2026-06-22 SimVLA Dataset Sync Update

- Sam plain-goal SimVLA dataset frozen at `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_uncertainty_final_5410ep_20260622`: 5,410 episodes, exactly 541 per task 0-9, 5,120 successes, 290 failures, failures preserve timeout-800 trajectories.
- Bob canonical H10 `libero_goal_object` flat training dataset confirmed at `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/inputs/datasets/continuous_chunk10_flat`: 17,409 episodes, 235,466 query rows, 2,292,591 transition rows.
- Transfer of the Bob flat `libero_goal_object` dataset to Sam launched in local tmux `transfer_bob_goal_object_flat_to_sam_20260622`.
- Sam destination for that transfer: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_object_h10_continuous_flat_from_bob_20260622`.
- Transfer log: `/home/redafrix/tests/internship/transfer_logs/transfer_bob_goal_object_flat_to_sam_20260622.log`. Wait for `TRANSFER_DONE` and final `wc -l` verification before launching training that depends on this copy.
- Auto-launch watcher started in local tmux `wait_transfer_then_launch_sam_goal_to_goal_object_ood_20260622`. After transfer verification it deploys `scripts/train_simvla_goal_to_goal_object_ood_20260622.py` to Sam and launches tmux `simvla_goal_to_goal_object_ood_train_20260622`.
- Planned Sam output root: `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_goal_to_goal_object_ood_topk8_20260622`.
- Planned Sam train/eval log: `/home/rootalkhatib/test/reda_ws/fiper_ws/logs/simvla_goal_to_goal_object_ood_topk8_20260622/train_eval.log`.

## 2026-06-22 SimVLA Goal-to-Goal-Object Offline OOD Result

- Bob-to-Sam transfer completed at 2026-06-22 13:03 CEST with verified line counts: 17,409 episode summaries, 235,466 query rows, and 2,292,591 transitions.
- Sam train/eval tmux `simvla_goal_to_goal_object_ood_train_20260622` completed cleanly; log ends with `DONE`.
- Output root: `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_goal_to_goal_object_ood_topk8_20260622`.
- Report: `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_goal_to_goal_object_ood_topk8_20260622/SIMVLA_GOAL_TO_GOAL_OBJECT_OOD_REPORT_20260622.md`.
- Model artifact shape audit: `hist_proj.weight=(128,21)`, `action_proj.weight=(128,7)`, `static.0.weight=(128,51)`, matching H10 TopK8-style SimVLA risk schema and excluding explicit task id/timestep inputs.
- Source heldout result at best-val-F1 threshold 0.6014: AUROC 0.9307, AUPRC 0.9051, 17.06% episode false alarms, 97.67% failure detection.
- Full `libero_goal_object` OOD result at the same threshold: AUROC 0.7627, AUPRC 0.6998, 4.59% episode false alarms, 78.91% failure detection, Det@25 0.15%, Det@50 7.61%.
- Interpretation: trusted offline diagnostic, but plain-goal-only training transfers poorly for early OOD warning on goal-object; keep goal-object-trained detectors for online goal-object/OOD work.
- Direct comparison to previous best offline detector added to `KEY_RESULTS.md`, `MASTER_EXPERIMENT_INDEX.md`, `TRUSTED_RESULTS_SUMMARY.md`, and the Obsidian report addendum. Previous best remains stronger for early OOD warning: OOD failure detection 95.2% vs 78.91%, Det@25 26.2% vs 0.15%, Det@50 85.7% vs 7.61%, mean detection time/fraction 0.332 vs 0.722.

## 2026-06-22 Dean Official-FIPER Materialization Status

- Dean has no active tmux jobs and GPU is idle/free after the attempted official-FIPER run.
- The closer-to-official materialized-code attempt at `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622` did **not** complete.
- Waiter log: `/home/dean/fiper_uncertainty_collection/logs/wait_then_run_official_fiper_eval_20260622.log`; it reports that the materialization tmux disappeared and validation did not pass.
- Materialization logs under `/home/dean/fiper_uncertainty_collection/logs/official_fiper_sharded_20260622/` end with MuJoCo/EGL cleanup failures (`OpenGL.raw.EGL._errors.EGLError`, `EGL_NOT_INITIALIZED`).
- Partial tensors exist but are incomplete: `obs_embeddings.pt=(1225,960)` and `action_preds.pt=(1225,9,10,7)` under both `official_fiper_data/libero_fold00/processed_rollouts` and `official_fiper_data/libero_fold00_hygiene/processed_rollouts`; partial shards `shard_batches_0000_0004.pt`, `0005_0009.pt`, and `0010_0014.pt` exist.
- Added source report: `source_reports/dean/reports/DEAN_OFFICIAL_FIPER_MATERIALIZATION_STATUS_20260622.md`.
- Updated `MASTER_EXPERIMENT_INDEX.md`, `KEY_RESULTS.md`, and `TRUSTED_RESULTS_SUMMARY.md`: **DO_NOT_USE as final official-FIPER ablation**. The completed 2026-06-19 clean reimplementation remains the latest usable Dean offline comparison.

## 2026-06-22 Sam 18-Task OOD 180ep Collection Launch

- Launched Sam tmux `simvla_ood180_collect_eval_20260622`.
- Dataset target: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622`.
- Result target after automatic scoring: `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622_selected_cap_topk8_offline_eval`.
- Collection policy: modified SimVLA `ckpt-60000` with uncertainty head, **not** the risk-aware selected-cap policy.
- Target: official 18-task `libero_goal_object_ood`, 10 episodes/task, H10 action chunks, 8 ACE candidates, 49D uncertainty, timeout 800.
- First episode verified complete: task 0 episode `worker_0_libero_goal_object_ood_t0_r0`, success, 178 steps/rows.
- Automatic post-collection evaluator: `/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/eval_selected_cap_topk8_on_ood_dataset_20260622.py`, loading the selected-cap TopK8 risk model from `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`.

## 2026-06-23 Sam 18-Task OOD H10 Offline Audit Correction

- The Sam 18-task official `libero_goal_object_ood` dataset is complete/frozen: 180 episodes, exactly 10 per task, 149 successes and 31 failures.
- Corrected evaluator path: `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace`.
- The first offline evaluator result was superseded because it used a mismatched ACE formula and an overly misleading any-row/mass interpretation. The corrected evaluator uses the same ACE formula as online `run_policy_matrix.py`.
- H10 `unc_topk8` model directory itself has no OOD buckets: `success_test_ood=0`, `failure_eval_ood=0` in `metrics.json`; its saved metrics are seen/train/val/calib only.
- Corrected old-style detector-only metrics on the official 18-task OOD dataset:
  - `score_q95_K3`: FA 95.3%, Det 100.0%, Det@25 100.0%, Det@50 100.0%.
  - `score_q99_K3`: FA 60.4%, Det 100.0%, Det@25 90.3%, Det@50 96.8%.
  - saved `score_q95_mass_0.15`: FA 96.0%, Det 100.0%, Det@25 100.0%, Det@50 100.0%.
  - `score_q95_mass_20`: FA 20.8%, Det 96.8%, Det@25 90.3%, Det@50 96.8%.
  - `score_q95_mass_50`: FA 2.7%, Det 96.8%, Det@25 16.1%, Det@50 90.3%.
- Interpretation recorded in `MASTER_EXPERIMENT_INDEX.md`, `DATASET_MAP.md`, and `TRUSTED_RESULTS_SUMMARY.md`: the dataset and H10 detector family are aligned; the main finding is threshold/calibration drift on official 18-task OOD, not invalid data collection.

## 2026-06-23 Sam 18-Task OOD H10 Cap-300 Derivative

- Derived dataset created from `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622`.
- Derived path: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623`.
- Rule: keep `timestep < 300`; success only if original episode succeeded before 300 steps; reaching 300 is failure.
- Counts: 180 episodes, 143 successes, 37 failures, 28,031 rows. Six original max-800 successes converted to failures.
- Result path: `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace`.
- Report: `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace/SIMVLA_H10_TOPK8_OFFICIAL_OOD_CAP300_AUDIT_20260623.md`.
- Key cap-300 detector-only metrics:
  - `score_q95_K3`: FA 95.1%, Det 100.0%, Det@25 100.0%.
  - `score_q99_K3`: FA 60.1%, Det 89.2%, Det@25 21.6%.
  - saved `score_q95_mass_0.15`: FA 95.8%, Det 100.0%, Det@25 100.0%.
  - `score_q95_mass_20`: FA 18.9%, Det 91.9%, Det@25 0.0%, Det@50 83.8%.
  - `score_q95_mass_50`: FA 0.0%, Det 83.8%, Det@25 0.0%, Det@50 0.0%.

## 2026-06-23 Dean Official-FIPER Baseline Completed

- Successfully resolved the MuJoCo/EGL materialization failures by using a sharded materialization workaround (`BATCH_SIZE=10` over 105 batches).
- Successfully completed both Option A (in-domain) and Option B (hygiene cross-domain) training and evaluations on Dean.
- Patched `run_fiper.py` on Dean to bypass the results manager for the hygiene task to prevent `pandas.errors.EmptyDataError` crashes.
- Output root on Dean: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622`
- Final results report written to `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622/reports/OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_20260623.md`.
- Converted metrics show best row is `rnd_oe_and_entropy Option B` with Success FA 26.7%, Failure Det 88.3%, Accuracy 80.8%, TWA 0.625. Our newer method `v2_018_transformer_k16` (score q95 K3) outperforms it on failure detection (95.2% vs 88.3%) and detection time (0.343s vs 0.415s).
- Updated `MASTER_EXPERIMENT_INDEX.md`, `KEY_RESULTS.md`, and `TRUSTED_RESULTS_SUMMARY.md` to reflect status complete/trusted.

## 2026-06-24 Dean Official-FIPER Baseline Verification Completed

- Successfully performed a comprehensive forensic verification pass on FIPER OOD-only ablation results, computing standard metrics (including Det@10/25/50) and resolving split mismatches.
- Verified dataset counts: OOD test split contains exactly 253 rollouts (211 success, 42 failure). Corrected a mathematical hallucination from the previous summary which claimed "143 success, 110 failure".
- Proven RND-OE saturation at step 0 is physical/mathematical: visual out-of-domain embeddings fail to generalize to the RND space, leading to novelty scores ~27x higher than the step 0 threshold. This is not an indexing or padding bug.
- Compiled the verified final report `OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_VERIFIED_20260624.md` locally and synced it to Dean.
- Updated central catalogs `MASTER_EXPERIMENT_INDEX.md`, `TRUSTED_RESULTS_SUMMARY.md`, and `KEY_RESULTS.md` with verified 2026-06-24 entries.

## 2026-06-25 Pi0.5 Offline Risk Head Complete

- Safely paused/stopped active data collection on Bob.
- Cleanly froze 4,090 episodes (3,298 success / 792 failure) from rounds 2..410, ensuring perfectly balanced round-robin representation (409 per task) and excluding task 9 infrastructure KeyErrors from rounds 0 and 1.
- Split dataset into non-overlapping, episode-grouped splits: Train (2,854 eps), Val (606 eps), Test (630 eps).
- Trained the temporal `SeqRiskModel` (width 128, layers 3, heads 4, history length K=16) with mask=True and padded zero uncertainty.
- Validation-calibrated thresholds: best F1 0.4800, q95 0.7218, q95_mass_10.
- Computed test metrics showing AUROC 0.9534, AUPRC 0.9728. Calibrated `q95_mass_10` threshold achieved **2.98% False Alarm** and **99.21% Failure Detection** on the test split.
- Updated MASTER_EXPERIMENT_INDEX, TRUSTED_RESULTS_SUMMARY, DATASET_MAP, and KEY_RESULTS.
- Frozen dataset path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_20260625`
- Offline risk experiment path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_20260625`
- Verdict: TRUST offline diagnostic/experiment. Safe to proceed to online OOD sweeps next.

## 2026-06-26 Pi0.5 Official Goal-Swap 50ep Online/Offline Audit Complete

- Completed Bob `libero_goal_swap` online run: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625`.
- Policies: `pi05_basic_h10` and `pi05_risk_selected_cap_topk8_h10`, 50 paired seeds per task across tasks 0..9, max 300, H10.

## 2026-06-29 Bob Status Audit And Pi0.5 Official OOD 18-Task Update

- Host audited: Bob / `PCROBOTUBUNTU02` at 2026-06-29 09:34 CEST.
- Health: GPU idle (`RTX 4070 Ti SUPER`, 3.3GB/16.4GB VRAM, 0% util, 53C). Disk healthy enough for current work: `/media/rootalkhatib/My Passport` 339GB free (82% used), `/` 326GB free (27% used).
- Stale/old tmux shells still exist (`ood_production_aggressive_fixed_100ep_20260609`, `pi05_collection`, `stage5`, `task6_aggressive_20260608`, `task6_aggressive_old_detector_20260608`), but captured panes show completed/idle prompts or interrupted historical commands. No active heavy GPU experiment was detected.
- OpenVLA main OOD run remains complete: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`, 3,600/3,600 rows. Final: `openvla_basic` 976/1,800 = 54.22%; `openvla_risk_horizon` 1,014/1,800 = 56.33%.
- OpenVLA fixed-H1 follow-up is not complete: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_h1_100ep_20260619`, 1,720/1,800 rows. Current partial result: 947/1,720 = 55.06%; log tail ends in `KeyboardInterrupt`.
- Pi0.5 official `libero_goal_object_ood` 18-task 100ep run is complete and audited from per-policy JSONL files:
  - Online root: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625`
  - Offline result path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_ood_18task_100ep_two_heads_eval_20260625`
  - `pi05_basic_h10`: 1,754/1,800 = 97.44%
  - `pi05_risk_selected_cap_topk8_h10`: 1,736/1,800 = 96.44%, net -18, 759 action modifications across 529 episodes.
- Pi0.5 official `libero_goal_swap` 50ep run remains complete: basic 161/500 = 32.20%; risk selected-cap 166/500 = 33.20%; 1,306 action modifications.
- SimVLA official byte-identical `libero_goal_object` 500ep basic run remains complete: 422/500 = 84.40%, exactly 50 init states per task.
- Catalog files updated locally: `MASTER_EXPERIMENT_INDEX.md`, `KEY_RESULTS.md`, `TRUSTED_RESULTS_SUMMARY.md`, `DATASET_MAP.md`, `OPENVLA_EXPERIMENT_MAP_20260619.md`, and this `SYNC_STATUS.md`.

## 2026-06-29 OpenVLA H1 Follow-Up Resumed On Bob

- Resumed the interrupted fixed-H1 OpenVLA follow-up run in tmux `openvla_ood_basic_h1_100ep_20260619`.
- Command uses the original script and output root:
  - Script: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/run_openvla_ood_basic_h1_full_20260619.py`
  - Output root: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_h1_100ep_20260619`
  - Log: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/logs/libero_goal_object_ood_openvla_basic_h1_100ep_20260619/sweep_supervisor.log`
- Resume verification:
  - Pre-resume rows: 1,720/1,800.
  - Script printed `[info] Starting/resuming openvla_basic_h1: 1720/1800 already complete`.
  - First resumed episode: `[1721/1800] policy=openvla_basic_h1 task=17 seed=30`.
  - Remaining work at launch: task 17 seeds 30..109, 80 episodes.
- Catalog files updated: `MASTER_EXPERIMENT_INDEX.md`, `KEY_RESULTS.md`, `OPENVLA_EXPERIMENT_MAP_20260619.md`, and this `SYNC_STATUS.md`.

## 2026-06-29 Sam Official Goal-Object H10 Uncertainty Collection Snapshot And Cross-Host Sync

- Checked Sam / `PCROBOTUBUNTU05` at 2026-06-29 09:48 CEST.
- Active tmux: `sam_official_goal_object_h10_uncertainty_17410ep_20260626`.
- Dataset path: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626`.
- Current progress:
  - `episode_summaries.jsonl`: 3,166 episodes.
  - `fiper_receding_samples.jsonl`: 741,495 rows, about 36.5GB.
  - Success/failure: 2,660 successes / 506 failures = 84.02% success.
  - Live status: running episode `worker_0_libero_goal_object_official_t6_r316`.
  - No seed collisions and no main/ACE collisions reported in `live_status.json`.
- Per-task snapshot:
  - task0: 281/317 = 88.64%
  - task1: 298/317 = 94.01%
  - task2: 263/317 = 82.97%
  - task3: 105/317 = 33.12%
  - task4: 290/317 = 91.48%
  - task5: 312/317 = 98.42%
  - task6: 219/316 = 69.30%
  - task7: 316/316 = 100.00%
  - task8: 291/316 = 92.09%
  - task9: 285/316 = 90.19%
- Health:
  - GPU active: RTX 4070 Ti SUPER, about 4.1GB/16.4GB VRAM, 89% util, 85C.
  - Disk warning: `/` is 96% used with about 19GB free. Continue monitoring disk usage; do not launch extra large jobs on Sam until more space is available or this run is paused/frozen.
- Synced updated experiment catalog files to Bob, Sam, and Dean after this check.

## 2026-06-29 Dean Official FIPER OOD180 Threshold Sweep

- Ran a no-retrain threshold sweep for official FIPER on the same 180-episode official `libero_goal_object_ood` dataset.
- Script: `/home/dean/fiper_uncertainty_collection/scripts/run_official_fiper_ood180_threshold_sweep_20260629.py`.
- Output directory: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_20260629`.
- CSV: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_20260629/official_fiper_ood180_threshold_sweep.csv`.
- Report: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_20260629/OFFICIAL_FIPER_OOD180_THRESHOLD_SWEEP_20260629.md`.
- Dataset: same 180 OOD episodes, 149 successes / 31 failures.
- No retrain: reused official FIPER RND checkpoints for seeds 0, 1, 2, 42, 43.
- Official deployment point still fails by false-alarming on all OOD successes:
  - `entropy any_1`: 100.0% Success FA / 100.0% Failure Det.
  - `rnd_oe any_1`: 100.0% Success FA / 100.0% Failure Det.
  - `rnd_oe_and_entropy any_1`: 100.0% Success FA / 100.0% Failure Det.
- Best diagnostic low-FA rows require OOD-test-set threshold selection and are not the unchanged paper deployment rule:
  - `rnd_oe_and_entropy mass_above_1_50`: 6.0% Success FA / 100.0% Failure Det / Det@50 96.8%.
  - `rnd_oe_and_entropy mass_above_1_100`: 2.7% Success FA / 96.8% Failure Det / Det@50 96.8%.
- Updated `KEY_RESULTS.md` and `TRUSTED_RESULTS_SUMMARY.md`; synced catalog files to Bob, Sam, and Dean.

## 2026-06-29 Dean H10 TopK8 OOD180 Cap-300 Extended Sweep

- Ran a no-retrain extended threshold sweep for our H10 TopK8 risk head on the same 180-episode official `libero_goal_object_ood` dataset under the cap-300 label rule.
- Cap-300 labels: 143 successes / 37 failures; 28,031 retained rows.
- Output report: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_cap300_extended_sweep_20260629/TOPK8_OOD180_CAP300_EXTENDED_SWEEP_20260629.md`.
- Output CSV: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_cap300_extended_sweep_20260629/topk8_ood180_cap300_extended_sweep.csv`.
- Selected rows:
  - `q95_mass_20`: 18.9% Success FA / 91.9% Failure Det / Det@50 83.8%.
  - `fixed_0.5_mass_30`: 17.5% Success FA / 91.9% Failure Det / Det@50 83.8%.
  - `q99_mass_2`: 1.4% Success FA / 83.8% Failure Det / Det@50 27.0%.
- Updated Obsidian report addendum 26, `KEY_RESULTS.md`, and `TRUSTED_RESULTS_SUMMARY.md`.

## 2026-06-29 Dean Official FIPER OOD180 Cap-300 Threshold Sweep

- Reran the no-retrain official FIPER threshold sweep with cap-300 relabeling.
- Rule: truncate each episode's normalized FIPER scores to the first 300 steps; count an episode as success only if the original episode succeeded by step 300. Anything reaching/exceeding the cap is a failure.
- Cap-300 label counts: 143 successes / 37 failures.
- Script: `/home/dean/fiper_uncertainty_collection/scripts/run_official_fiper_ood180_cap300_threshold_sweep_20260629.py`.
- Output directory: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_cap300_20260629`.
- CSV: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_cap300_20260629/official_fiper_ood180_cap300_threshold_sweep.csv`.
- Report: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/threshold_sweep_ood180_cap300_20260629/OFFICIAL_FIPER_OOD180_CAP300_THRESHOLD_SWEEP_20260629.md`.
- Key rows:
  - `entropy any_1`: 100.0% Success FA / 100.0% Failure Det / Det@10 81.1%.
  - `rnd_oe any_1`: 100.0% Success FA / 100.0% Failure Det / Det@10 100.0%.
  - `rnd_oe_and_entropy any_1`: 100.0% Success FA / 100.0% Failure Det / Det@10 27.0%.
  - `rnd_oe_and_entropy mass_above_1_20`: 28.7% Success FA / 91.9% Failure Det / Det@25 2.7% / Det@50 78.4%.
  - `rnd_oe_and_entropy mass_above_1_50`: 2.8% Success FA / 91.9% Failure Det / Det@25 0.0% / Det@50 59.5%.
  - `rnd_oe_and_entropy mass_above_1_100`: 0.0% Success FA / 78.4% Failure Det / Det@50 0.0%.
- Interpretation: cap-300 makes the low-false-alarm FIPER threshold-sweep rows much weaker; official deployment threshold still false-alarms all successes.
- Updated `KEY_RESULTS.md` and `TRUSTED_RESULTS_SUMMARY.md`; synced catalog files to Bob, Sam, and Dean.
- Online result: basic 161/500 = 32.20%; risk selected-cap 166/500 = 33.20%; net +5 successes.
- Selected-cap changes: 1,306 total action changes across 383/500 risk episodes; 1,017 changes occurred in failed episodes.
- Offline two-head result path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_goal_swap_10task_50ep_two_heads_eval_20260625`.
- Added dense old-with-task9 q95-mass threshold sweep: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_goal_swap_10task_50ep_two_heads_eval_20260625/old_with_task9_q95_mass_threshold_sweep_20260626.json`.
- Updated `KEY_RESULTS.md`, `MASTER_EXPERIMENT_INDEX.md`, `TRUSTED_RESULTS_SUMMARY.md`, `DATASET_MAP.md`, and Obsidian report with complete online table, action-change summary, and threshold-sweep interpretation.

## 2026-06-26 Sam Official LIBERO Goal-Object H10 Uncertainty Setup Complete

- Freed Sam disk space by deleting the approved stale raw trash source dataset and approved Git tmp packs; Sam returned to ~56G free on `/home/rootalkhatib/test/reda_ws`.
- Installed byte-identical official `libero_goal_object` BDDL/init copies on Sam from the already-validated Bob official suite:
  - BDDL: `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files/libero_goal_object_official`
  - Init: `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files/libero_goal_object_official`
- Verified the Sam official copy has 10 BDDL files + 10 init files with SHA256 hashes matching Bob.
- Created Sam-only modified-SimVLA uncertainty collector:
  - Collector: `/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/collect_simvla_official_goal_object_uncertainty_20260626.py`
  - Launcher: `/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/run_sam_official_goal_object_uncertainty_collect_20260626.sh`
- Smoke test completed successfully at `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_smoke_20260626`: 1 official task-0 episode, success, 252 rows, H10 action chunk, 8 ACE candidates, 49D uncertainty, and validation pass.
- Launched the large 17,410-episode collection in tmux `sam_official_goal_object_h10_uncertainty_17410ep_20260626`.
- Dataset target: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626`.
- Log: `/home/rootalkhatib/test/reda_ws/fiper_ws/logs/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626/outer.log`.
- First full round audit passed after tasks 0..9 completed once each: strict round-robin, H10 chunks, real 8-candidate ACE, 49D uncertainty and delta uncertainty, TopK8 extractable, official metadata paths, no NaN/Inf, continuous timesteps, and compatible history schema.
- Snapshot at audit: 13 episodes complete, 2,842 rows, 11 success / 2 failure-or-timeout; tmux active and GPU running.

## 2026-06-30 Cross-Suite Official OOD Campaign Launch

- Sam official `libero_goal_object` H10 uncertainty collection was stopped safely for disk pressure and transfer. Snapshot before transfer: about 4,469 episodes, about 1.06M sample rows, dataset size about 53GB.
- Bob campaign root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630`.
- Running tmux sessions on Bob: `cross_suite_sam_seen_transfer_20260630` and `cross_suite_official_ood_20260630`.
- Bob supervisor preflight passed for: `libero_goal_swap`, `libero_goal_task`, `libero_goal_object_ood` with documented `libero_goal_object_ood_temp` BDDL alias, `libero_spatial`, `libero_object`, and `libero_10`.
- First smoke dataset passed validation: H10 action chunk, 8 ACE candidates, 49D uncertainty, required fields, and saved MuJoCo state NPZ files.
- Official FIPER materialization/evaluation is intentionally not launched on Dean yet because Dean root disk is nearly full; the Bob datasets save states so FIPER materialization can be run safely after the collection finishes and a suitable host/path is selected.

## 2026-06-30 Correction: Sam Official Goal-Object Dataset Revalidated

- Correction to the earlier cross-suite launch note: the Sam dataset `simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626` is trusted for the strict official campaign.
- Direct SHA256 audit against Hugging Face `zhouxueyang/LIBERO-Pro` showed Sam `libero_goal_object_official` has 20/20 BDDL/init matches.
- Dataset manifest and row metadata confirm collection used suite `libero_goal_object_official` with BDDL/init paths under `libero_goal_object_official`.
- The bad/mismatching folder is the local default `libero_goal_object`, not the explicit `libero_goal_object_official` copy used by the Sam dataset.
- Bob supervisor was corrected to use the Sam transfer as source and not recollect a redundant Bob source dataset.

## 2026-06-30 Correction: Goal-Object-OOD Restored to Cross-Suite Campaign

- Restored `goal_object_ood_180` to the Bob cross-suite campaign target list.
- Provenance: this suite is not part of Hugging Face `zhouxueyang/LIBERO-Pro`; Bob resolves it from local benchmark `libero_goal_object_ood`, with BDDL files under `libero_goal_object_ood_temp` and init states under `libero_goal_object_ood`.
- Preflight passed for all 18 tasks before relaunch.
- Sam-to-Bob transfer of the full verified official `libero_goal_object_official` dataset remains active and resumable; transfer size was 19G at the post-relaunch check.

## 2026-06-30 Cross-Suite Campaign ETA and Provenance Update

- Live Bob sessions: `cross_suite_official_ood_20260630` and `cross_suite_sam_seen_transfer_20260630`.
- Current collection stage: `goal_swap_100`; latest observed episodes are mostly max-300 failures at about 103-104 seconds per episode.
- ETA if most target episodes time out similarly: about 18-20 hours for the 680 target OOD episodes, plus training/evaluation time afterward. If later suites have faster successes, the wall time will be shorter.
- Transfer status: Sam-to-Bob source transfer is active and resumable; transfer size was 26GB at 2026-06-30 14:44 CEST. The transfer script copies `fiper_receding_samples.jsonl`, `episode_summaries.jsonl`, `run_manifest.json`, and `PIPELINE_MANIFEST.txt` for seen-source risk-head training. It intentionally does not copy Sam state NPZ files.
- Official provenance details:
  - Seen source: Sam `libero_goal_object_official`; verified 20/20 BDDL/init SHA256 match against Hugging Face `zhouxueyang/LIBERO-Pro`.
  - HF official PRO target suites: `libero_goal_swap`, `libero_goal_task`, `libero_spatial_object`, `libero_object_object`, `libero_10_object`.
  - `libero_goal_object_ood` target: local benchmark suite, not present in HF `zhouxueyang/LIBERO-Pro`; documented provenance is BDDL under `libero_goal_object_ood_temp` and init under `libero_goal_object_ood`, with 18/18 task preflight pass.
- OOD target datasets save MuJoCo states, H10 main action chunks, 8 ACE candidate chunks, and 49D uncertainty features, so they are suitable raw material for both our offline risk-head evaluation and later official-FIPER materialization.
