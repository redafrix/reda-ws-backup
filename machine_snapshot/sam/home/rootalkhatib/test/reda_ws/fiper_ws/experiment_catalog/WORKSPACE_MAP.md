# Distributed Workspace Map

## Batman

- Root: `/home/redafrix/tests/internship`
- FIPER workspace: `/home/redafrix/tests/internship/fiper_ws`
- Role: control machine, canonical catalog, consolidated reports, presentation, reproduction package, and small mirrored artifacts.
- Canonical catalog: `/home/redafrix/tests/internship/fiper_ws/experiment_catalog`

Batman should not be treated as the canonical location for large remote JSONL files or checkpoints unless their hashes and provenance are explicitly recorded.

## Bob

- Host alias: `pcrobot`
- Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws`
- OpenVLA-OFT root: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`
- Role: historical FIPER datasets and detector experiments, old four-task deployments, chunk-execution experiments, and current online replications.
- OpenVLA role: isolated OpenVLA-OFT setup, OpenVLA-specific datasets, offline risk experiments, and the active OpenVLA OOD basic-vs-risk run.
- Raw online runs: `realtime_deployment/runs/`
- Deployment configs: `realtime_deployment/configs/`
- Historical offline experiments: `experiments/`
- Checkpoints: `checkpoints/`
- Canonical catalog mirror: `experiment_catalog/`

Bob's May 29 to June 1 folders use several misleading `baseline` or `vanilla` labels. Consult the catalog README before interpreting them.

## Dean

- Host alias: `dean-via-bob` while direct Tailscale access is unavailable
- Root: `/home/dean/fiper_uncertainty_collection`
- Role: 49D uncertainty data collection, full-data offline detector training, retained `base` and `unc_topk8` detector artifacts, and newer online tests.
- Current retained models: `experiments/current_dean_risk_models_20260602/`
- Offline uncertainty experiments: `experiments/`
- Raw collection runs: `runs/`
- Online deployments: `realtime_deployment/runs/`
- Canonical catalog mirror: `experiment_catalog/`

## Sam

- Host alias: `sam`
- Root: `/home/rootalkhatib/test/reda_ws/fiper_ws`
- Role: historical second 16 GB worker, including Task 7 and Task 8 portions of the four-task campaign.
- Current state: offline and unreachable from Batman and Bob at the latest audit.
- Catalog state: four known historical result entries are represented from audited summaries. The complete catalog must be synchronized when Sam returns online.

## Canonical Artifact Rules

1. Raw outputs remain on the machine that generated them.
2. Small reports, configs, and manifests are mirrored into Batman's catalog.
3. A checkpoint is identified by path, role, and preferably SHA-256, not by a folder nickname.
4. Every new experiment gets a dedicated result directory and an associated catalog entry.
5. Existing experiment directories are not renamed while scripts or reports reference their paths.
6. Archiving means moving a complete immutable bundle under `archive/`; it never means deleting raw evidence.
7. Results from different execution horizons, checkpoints, tasks, or GPU hosts are separate experiments and must not be pooled without an explicit analysis.

### Bob New Trash Roots (2026-06-08)

- H10 Campaign: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608`
- Aggressive Ablation: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608`
- Old Detector Comparison: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608`

### Bob OpenVLA Roots (2026-06-16 to 2026-06-19)

- OpenVLA workspace: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`
- Final OpenVLA goal-object dataset: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618`
- Final OpenVLA goal-object risk experiment: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_final1890_risk_20260618`
- OpenVLA old-goal to goal-object OOD offline tests: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_old6000_to_goal_object_ood_20260619` and `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_old6000_cut300_to_goal_object_ood_20260619`
- Active OpenVLA online OOD eval: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`
- OpenVLA focused rescue-seed diagnostic: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/focused_ood_task2_task8_rescue_seeds_10ep_20260619`
- OpenVLA basic H=1 diagnostic: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/focused_ood_task2_task8_basic_h1_seeds_10ep_20260619`
- OpenVLA H=1 diagnostic script: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/run_focused_diagnostic_basic_h1_20260619.py`

### Sam SimVLA Roots (2026-06-19)

- Active SimVLA plain-goal uncertainty collection: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/simvla_goal_uncertainty_2000ep_20260619`
- Active tmux session: `simvla_goal_uncertainty_10000ep_20260619`
- Purpose: collect 10,000 modified-SimVLA `libero_goal` receding episodes with H10 action chunks, 8 ACE candidates, 49D uncertainty, and 800-step failure timeout for the SimVLA goal-to-goal-object offline OOD test.
