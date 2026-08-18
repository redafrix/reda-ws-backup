# Cross-Machine Experiment Map

Updated: 2026-07-03 by Codex after local/Bob/Sam/Dean audit.

This is the current entry point for future Codex/Gemini sessions. It does not replace the detailed historical maps; it ties them together and records the current canonical datasets, models, results, reports, and machine locations.

## Start Here

Read these files in this order:

1. `CROSS_MACHINE_EXPERIMENT_MAP_20260703.md` - this file, current cross-host map.
2. `DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md` - cross-host/archive coverage audit and missing-family triage.
3. `KEY_RESULTS.md` - curated scientific conclusions and caveats.
4. `DATASET_MAP.md` - dataset provenance and exact paths.
5. `MASTER_EXPERIMENT_INDEX.md` - chronological/campaign-level index.
6. `TRUSTED_RESULTS_SUMMARY.md` - forensic trust verdicts.
7. `OPENVLA_EXPERIMENT_MAP_20260619.md` - OpenVLA-specific work.
8. `BIG_ARTIFACTS_NOT_IN_GIT_20260703.md` - remote heavy artifacts that must not be committed.
9. Obsidian report: `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md`.

## Host Status Snapshot

Captured 2026-07-03 around 10:55-12:20 CEST, then updated after the Git repair and deep coverage audit.

| Host | SSH alias | Role | Disk status | Current caution |
|---|---|---|---|---|
| Batman/local laptop | local | Catalog, Obsidian report, local scripts | Git repo repaired and clean after catalog commit/push | Keep large artifacts excluded; use the branch-per-host catalog branches listed below. |
| Bob / PCROBOTUBUNTU02 | `pcrobot` | Main online/eval host, OpenVLA, Pi0.5, official FIPER on Bob, cross-suite OOD | `/media/rootalkhatib/My Passport`: 101G free, 95% used; `/`: 313G free | External disk is nearly full but usable for logs/reports; avoid new huge datasets without cleanup. |
| Sam / PCROBOTUBUNTU05 | `sam` | Official SimVLA source data collection and older timeout800 selected-cap run | `/`: 1.9G free, 100% used | Do not launch large jobs until space is freed. Current official source dataset is frozen/usable, not actively collecting. |
| Dean / Batman | `dean` | Historical FIPER materialization, official FIPER ablations, Dean online selected-cap | `/`: 3.8G free, 100% used | Do not materialize more embeddings on root without cleanup or external target. |

## Canonical Model Lineage

| Model / policy | Host/root | Training data | Inputs | Current use | Key caveat |
|---|---|---|---|---|---|
| `v2_018_transformer_k16` | historical Bob/FIPER baseline | original FIPER receding datasets | temporal history/action/proprio/ACE-style risk features | Historical baseline vs official FIPER fold00 | Good early-warning baseline; older dataset/protocol. |
| H10 TopK8 detector, hash `687b5d35...` | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8` | 17,409 local `libero_goal_object` H10 chunk10 episodes | history `16x21`, action `10x7`, static `51` with TopK8 uncertainty | SimVLA H10 selected-cap/threshold studies | Local goal-object suite differed from byte-identical official suite; use with provenance note. |
| Promoted official-source H10 TopK8 model | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/models/simvla_h10_topk8_official_goal_object_seen_main_20260701` | Sam official `libero_goal_object_official` source, 4,469 episodes | same H10 TopK8 schema; no task id/timestep | Current main cross-suite offline model | Selected by seen/source validation AUPRC only; OOD thresholds are diagnostic unless predeclared. |
| Official FIPER seen model/checkpoints | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701` | 500 train success + 150 calibration success + heldout seen test | `obs_embeddings.pt` 960D + `action_preds.pt` `[9,10,7]` | Official FIPER baseline and seen-selected q95 operating points | Method code close to official repo; dataset adapter and runtime compatibility are documented. |
| OpenVLA final risk head | Bob: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_final1890_risk_20260618` | 1,890 cleaned OpenVLA `libero_goal_object` episodes | static 43, history 21, action 7; no explicit task id/timestep | OpenVLA H8 vs adaptive H1/H8 OOD test | No ACE/ensemble; dummy ACE padding only. |
| Pi0.5 H10 risk head | Bob: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_20260625` | 4,090 Pi0.5 `libero_goal_object` episodes, task9 infra rounds excluded | Pi0.5 H10 chunks + real ACE candidates; uncertainty TopK8 zeroed | Pi0.5 online/offline selected-cap studies | First dataset used local goal-object; task9 rack issue later discovered for local data. |

## Canonical Datasets

| Dataset | Host/path | Size/count | Purpose | Status |
|---|---|---:|---|---|
| Original FIPER sweep eternal | Bob/Sam/local, see `DATASET_MAP.md` | ~734K receding rows | Historical risk detector training | Frozen. |
| Dean object uncertainty | Dean: `/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529` | 4,257 episodes | Multi-suite uncertainty/offline detector work | Frozen. |
| Local H10 continuous chunk10 flat | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/inputs/datasets/continuous_chunk10_flat` | 17,409 episodes | Original H10 base/TopK8 training | Frozen; local suite provenance caveat. |
| Official SimVLA H10 source from Sam | Sam: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626`; Bob copy: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630` | 4,469 episodes, 1,060,884 rows, 52.25GB samples | Current official seen-source training/calibration base | Frozen/validated; official `libero_goal_object_official` BDDL/init SHA matched. |
| Cross-suite official OOD collection | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets` | 680 OOD episodes total | Cross-suite offline testing for our model and FIPER materialization | Complete. |
| OOD180 official goal-object dataset | Sam: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622` | 180 episodes, 149 success / 31 failure | Early OOD offline detector/FIPER comparison | Frozen; timeout 800. |
| OOD180 cap300 derivative | Sam: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623` | 180 episodes, 143 success / 37 failure | Cap-300 offline threshold sensitivity | Derived, not freshly collected. |
| OpenVLA final goal-object dataset | Bob: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618` | 1,890 episodes | OpenVLA risk head training | Frozen. |
| Pi0.5 frozen goal-object dataset | Bob: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_20260625` | 4,090 episodes | Pi0.5 risk head training | Frozen; local suite/task9 caveat. |

## Cross-Suite Official OOD Collection Details

Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630`.

| Dataset | Episodes | Source file size | Notes |
|---|---:|---:|---|
| `goal_swap_100` | 100 | `fiper_receding_samples.jsonl` 1.46GB | official HF `libero_goal_swap`. |
| `goal_task_100` | 100 | 1.35GB | official HF `libero_goal_task`. |
| `goal_object_ood_180` | 180 | 1.43GB | local OOD suite, BDDL under `libero_goal_object_ood_temp`, init under `libero_goal_object_ood`. |
| `spatial_object_100` | 100 | 602MB | official HF spatial/object target. |
| `object_object_100` | 100 | 990MB | official HF object/object target. |
| `libero10_object_100` | 100 | 1.44GB | official HF LIBERO-10 object target. |

All OOD datasets save H10 main action chunks `[10,7]`, 8 ACE candidate chunks `[8,10,7]`, 49D uncertainty, history/proprio fields, and MuJoCo states for FIPER materialization.

## Main Result Families

### Deep Coverage Audit

- Deep audit report: `DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md`.
- Compact manifest: `manifests/deep_audit_summary_20260703.json`.
- Scope: local/Batman, Bob, Sam, Dean, and archived folders. The scan reduced 2,888 experiment-like roots and triaged 445 roots that were not clearly covered by older text maps.
- Important recovered families: Bob `bob_risk_matrix_campaign_20260605`, Bob `re_run_v2_018_audit_20260624`, Pi0.5 smoke/10ep/no-task9/40ep runs, Sam video reels, Dean `fiper_goal_object_collection_20260605`, Dean TDQC/SimVLA legacy roots, and local Stage6-9/official-FIPER/Pi0.5/OpenVLA archives.

### SimVLA H10 Online/Offline

- Best older online result: Sam timeout800 selected-cap, `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615`, selected-cap 1,754/1,800 = 97.44%, +10 over modified SimVLA, but timeout is 800 not 300.
- Dean selected-cap 100ep: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610`, selected-cap 1,741/1,800 = 96.72%, +15 over modified SimVLA.
- Bob selected-cap 100ep: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_100ep_comparison_20260611`, delay30 small positive on Bob but not reproduced on Dean.
- Official-source promoted offline model: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/eval_promoted_single_model_all_ood_20260701`.

### Official FIPER Baselines

- Dean fold00 materialized official-FIPER run: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622`.
- Bob official FIPER seen train/eval: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701`.
- Bob official FIPER seen thresholds on cross-suite OOD: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702`.
- Latest audit verdict: mechanically consistent, no OOD calibration, no OOD threshold tuning, 5 RND seeds reused (`0,1,2,42,43`), aggregate CSV exactly matches per-seed mean.

### OpenVLA

- Workspace: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`.
- Main online OOD result: `online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`, fixed H8 976/1,800 = 54.22%, adaptive risk H1/H8 1,014/1,800 = 56.33%.
- H1 follow-up exists under `online_evals/libero_goal_object_ood_openvla_basic_h1_100ep_20260619`; older map listed it partial at 1,720/1,800 and resumed.
- Use `OPENVLA_EXPERIMENT_MAP_20260619.md` before comparing to SimVLA, because the feature schema and policy are different.

### Pi0.5

- Workspace: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623`.
- Offline risk model: `pi05_goal_object_h10_risk_20260625`, test AUROC 0.9534 / AUPRC 0.9728; `q95_mass_10` gave 2.98% Success FA and 99.21% Failure Detection on its internal test split.
- Official goal-swap online/offline: `online_evals/pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625`, basic 161/500, selected-cap 166/500.
- Official OOD18 online/offline: `online_evals/pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625`, basic 1,754/1,800, selected-cap 1,736/1,800.

### Isaac Lab

- New isolated Bob workspace: `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab`.
- Environment: `/home/rootalkhatib/miniconda3/envs/env_isaaclab_6_0`, Python 3.12.13, PyTorch 2.11.0+cu130, Isaac Sim deps 6.0.0.1.
- Driver was upgraded on Bob to NVIDIA 595.71.05 for CUDA 13.0.
- Do not disturb this workspace or env when running SimVLA/OpenVLA/FIPER jobs.

## File/Report Pointers

| Topic | Primary report |
|---|---|
| Cross-suite OOD summary | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/CROSS_SUITE_OFFICIAL_OOD_SUMMARY_20260630.md` |
| Promoted model OOD eval | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/eval_promoted_single_model_all_ood_20260701/PROMOTED_SINGLE_MODEL_OOD_EVAL_REPORT_20260701.md` |
| Official FIPER seen eval | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701/OFFICIAL_FIPER_SEEN_TRAIN_EVAL_REPORT.md` |
| Official FIPER cross-suite OOD | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702/OFFICIAL_FIPER_SEEN_THRESHOLDS_CROSS_SUITE_OOD_20260702.md` |
| Sam official source manifest | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626/run_manifest.json` |
| OpenVLA map | `OPENVLA_EXPERIMENT_MAP_20260619.md` |
| Obsidian full narrative | `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md` |

## Current Git Reality

Git was repaired on 2026-07-03 after the broken local `.git` directory was moved to `.git.broken_20260703_112818`.

- Remote: `https://github.com/redafrix/reda-ws-backup.git`.
- Branches pushed after the deep-audit update: `catalog/batman-20260703`, `catalog/bob-20260703`, `catalog/sam-20260703`, `catalog/dean-20260703`, and `catalog/cross-machine-20260703`.
- Deep-audit content commit: `dcbf0251b59cb58fe3576f17e3f26c2ebd2ef3df`. Follow-up metadata-only commits may be newer; use `git rev-parse HEAD` for the exact local tip.
- Existing remote branches `main`, `bob`, `sam`, and `dean` were not overwritten.
- Heavy artifacts must stay out of Git; use `BIG_ARTIFACTS_NOT_IN_GIT_20260703.md` as the substitute manifest.

## Next Session Checklist

1. Start by reading this file.
2. Check live disk and tmux on Bob/Sam/Dean before launching anything.
3. If working on FIPER official comparisons, use the Bob 20260701/20260702 official-FIPER roots first; do not use older Dean threshold sweeps unless explicitly studying historical ablations.
4. If working on our current SimVLA model, use the promoted official-source model under `cross_suite_official_ood_20260630/models/simvla_h10_topk8_official_goal_object_seen_main_20260701`.
5. If pushing to GitHub, run the large-file audit first and keep large tensors/jsonl/videos out of Git.


## Corrected True-H10 Isaac Sim Result (2026-08-18)

Canonical record: [`ISAAC_RESULTS_20260818.md`](ISAAC_RESULTS_20260818.md) and [`../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md`](../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md).

- Seen4000: **4000 episodes**, **3908 success / 92 failure**, **75,603 decision rows**.
- V1 validation AUROC/AUPRC: **0.9344901338 / 0.8494462696**.
- Locked historical true-H10 OOD150 detector: **72 success / 78 failure**, **5,887 rows**, step **AUROC 0.9165517742 / AUPRC 0.9800307262**.
- Main detector threshold: `best_val_f1 = 0.7990124225616455`, calibrated on Seen validation.
- Definitive active controller: `A=0.7990124225616455`, `C=0.9`, `M=0.0`.
- Active result: **75/150 (50.0%)** versus historical same-membership **72/150 (48.0%)**, net **+3 episodes / +2.0 percentage points**.
- Paired: **11 rescues / 8 regressions / 64 persisted successes / 67 persisted failures**.
- Controller audit: **57 accepted replacements** across **36/150 episodes**, **0 selection mismatches**, **0 execution mismatches**, max selected-vs-executed action difference **0.0**.
- Exact membership: 150 expected / 150 actual / 150 unique, no missing, extra, or duplicate IDs; historical membership exact.
- `A` is Seen-calibrated. `C=0.9` is engineering-development-informed from preserved live nine-candidate OOD-development decisions, so the final 150 is **not** a pristine untouched holdout for controller hyperparameter selection.
- V1 is a current/main H10 proposal failure detector with multi-sample ACE/disagreement context; it was **not** trained on nine independently supervised counterfactual candidate outcomes.
- HARD1000 resumed safely from the preserved 249-episode state and is ongoing; intermediate HARD1000 counts are **not** final results.
- Commit `70327b4b31bde35c01fda29a807f9100b5295a62` is **invalid for historical candidate-wise alternative scores** because candidates 1–8 diffusion traces were not archived. Correction commit: `86f5baf3281596df2305409499fc9e0c21d119ed`.
