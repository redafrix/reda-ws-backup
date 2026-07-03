# OpenVLA Experiment Map

Updated: 2026-06-22 by Codex from Bob filesystem and live tmux status.

This file indexes the isolated OpenVLA-OFT work on Bob. It is separate from the SimVLA/FIPER catalog entries because the policy, feature schema, native horizon, risk model inputs, and environment are different.

## Canonical Workspace

| Property | Value |
| :--- | :--- |
| **Host** | Bob / `pcrobot` / `PCROBOTUBUNTU02` |
| **Workspace root** | `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616` |
| **Env** | `/home/rootalkhatib/openvla_oft_env_20260616` plus workspace activation script `activate_openvla_oft_bob.sh` |
| **Model** | `moojink/openvla-7b-oft-finetuned-libero-goal` |
| **Quantization** | 8-bit |
| **Unnormalization key** | `libero_goal_no_noops` |
| **Native OpenVLA horizon** | 8 predicted actions |
| **Compatibility module** | `src/openvla_oft_bob_compat.py` |
| **Important caveat** | OpenVLA risk records do not have SimVLA uncertainty/ACE candidate features. They use proprioception, OpenVLA action chunk stats, and rolling history. |

## Required OpenVLA Patches And Smoke Tests

| ID | Date | Path / Report | Status | Meaning |
| :--- | :--- | :--- | :--- | :--- |
| `openvla_bob_model_audit_20260616` | 2026-06-16 | `reports/OPENVLA_OFT_BOB_MODEL_AUDIT_AND_FIX_REPORT_20260616.md` | Complete | Verified model files, cache isolation, correct unnorm key, action shape `(8, 7)`, and LIBERO env smoke. Both compatibility patches are required under current packages. |
| `openvla_clean_room_patch_audit_20260616` | 2026-06-16 | `reports/CLEAN_ROOM_PATCH_AUDIT_REPORT.md` | Complete | Established that the `.to()` no-op and rotary `inv_freq` device alignment patches are both needed. |
| `openvla_task0_tiny_rollout_20260616` | 2026-06-16 | `reports/OPENVLA_OFT_BOB_TINY_LIBERO_GOAL_TASK0_ROLLOUT_20260616.md` | Complete | 1-trial and 5-trial smoke on plain `libero_goal` task 0; 5-trial result 4/5 successes. |
| `openvla_goal_object_10task_smoke_20260616` | 2026-06-16/17 | `reports/OPENVLA_OFT_GOAL_OBJECT_PRO_10TASK_SMOKE_20260616.md`, `reports/OPENVLA_OFT_GOAL_OBJECT_PRO_COLLECTOR_PATCH_PARITY_20260617.md` | Complete | Verified the corrected `libero_goal_object` 10-task suite with XML/site injection patches for LIBERO-PRO assets. |

## Data Collection Datasets

| ID | Suite | Path | Count | Status | Use |
| :--- | :--- | :--- | ---: | :--- | :--- |
| `openvla_old6000_plain_goal_20260616_discarded_name` | Plain `libero_goal` despite confusing folder name | `outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded` | 6,009 episodes | Retained, diagnostic/source dataset | Old OpenVLA `libero_goal` risk training source. Do not treat as goal-object/pro despite folder name. |
| `openvla_goal_object_partial_20260617` | `libero_goal_object` | `outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260617` | Partial raw collection, superseded by cleaned dataset | Superseded | Raw corrected goal-object collection before final cleanup. |
| `openvla_goal_object_final_1890_20260618` | `libero_goal_object` | `datasets/openvla_goal_object_final_1890_complete_rounds_20260618` | 1,890 episodes: 787 success, 1,103 failure | Final/frozen | Current final OpenVLA goal-object risk-model dataset. Complete paired rounds only: reset seeds `100000..100188`, 10 tasks each. |

## Offline Risk Training And Evaluation

| ID | Train data | Test data | Path / Report | Main result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `openvla_old6000_risk_base_20260617` | Old 6,009 plain `libero_goal` episodes | Old heldout split | `offline_risk_experiments/openvla_old6000_risk_base_20260617/reports/OPENVLA_OLD6000_OFFLINE_RISK_BASE_REPORT_20260617.md` | 800-step old model: heldout AUROC 0.9953, AUPRC 0.9909, best-F1 threshold 0.7100. | Complete |
| `openvla_old6000_risk_base_cut300_20260617` | Old 6,009 plain `libero_goal` episodes with failed episodes capped at 300 steps | Old heldout split | `offline_risk_experiments/openvla_old6000_risk_base_20260617_cut300/reports/OPENVLA_OLD6000_OFFLINE_RISK_BASE_REPORT_300STEPS_20260617.md` | 300-step old model: best-F1 threshold 0.8700; low in-domain episode false alarms, but lower AUROC than the 800-step old model in later cross-dataset replay. | Complete |
| `openvla_new1891_risk_20260618` | Early corrected goal-object partial dataset | Internal split | `offline_risk_experiments/openvla_new1891_risk_20260618/reports/NEW_DATASET_1891EP_EVALUATION_REPORT_20260618.md` | Historical partial training run, superseded by cleaned 1,890 dataset. | Superseded |
| `openvla_new1894_risk_corrected_20260618` | Intermediate corrected goal-object dataset | Internal split | `offline_risk_experiments/openvla_new1894_risk_corrected_20260618/reports/NEW_DATASET_1894EP_CORRECTED_EVALUATION_REPORT_20260618.md` | Intermediate corrected run, superseded by final 1,890 dataset. | Superseded |
| `openvla_final1890_risk_20260618` | Final 1,890 `libero_goal_object` dataset | Internal split | `offline_risk_experiments/openvla_final1890_risk_20260618/reports/FINAL_1890_DATASET_RISK_EVALUATION_REPORT_20260618.md` | Current final OpenVLA goal-object risk model. The online runner uses `models/model_300steps.pt` and validation Q95 threshold `0.8049`. | Current |
| `openvla_old6000_to_goal_object_ood_20260619` | Old 6,009 plain `libero_goal` 800-step model | Old heldout split plus full final 1,890 goal-object dataset | `offline_risk_experiments/openvla_old6000_to_goal_object_ood_20260619/reports/OLD6000_TO_GOAL_OBJECT_OOD_EVAL_20260619.md` | Strict cross-dataset test: old-goal model transfers partly. On goal-object OOD at threshold 0.7100: AUROC 0.8302, AUPRC 0.9789, 15.63% episode false alarms, 100% failure detected, 83.14% detected by first 25%. | Complete |
| `openvla_old6000_cut300_to_goal_object_ood_20260619` | Old 6,009 plain `libero_goal` 300-step model | Old heldout split plus full final 1,890 goal-object dataset | `offline_risk_experiments/openvla_old6000_cut300_to_goal_object_ood_20260619/reports/OLD6000_TO_GOAL_OBJECT_OOD_EVAL_20260619.md` | Strict cross-dataset test: old 300-step model transfers worse. On goal-object OOD at threshold 0.8700: AUROC 0.6782, AUPRC 0.9562, 22.11% episode false alarms, 84.50% failure detected, 80.24% detected by first 25%. | Complete |

### Explicit-Input Forensic Audit (2026-06-19)

The OpenVLA risk checkpoints used for online OOD testing were audited after conflicting notes about task-id leakage. The final verdict is that the Transformer risk heads do **not** receive explicit task id or explicit timestep inputs. The stale 25-dimensional feature-schema text in the old 6,000-episode report describes secondary MLP/GRU baseline files, not the Transformer checkpoint used online.

| Model | Explicit task id train | Explicit task id test | Explicit timestep train | Explicit timestep test | Static dim | History dim | Verdict |
| :--- | :---: | :---: | :---: | :---: | ---: | ---: | :--- |
| `final_1890_risk` Transformer (`model_300steps.pt`, `model_800steps.pt`) | No | No | No | No | 43 | 21 | Clean explicit inputs |
| `old_6000_base` Transformer (`model.pt`) | No | No | No | No | 43 | 21 | Clean explicit inputs |
| `old_6000_cut300` Transformer | No | No | No | No | 43 | 21 | Clean explicit inputs |
| Old 6,000 MLP baseline (`risk_mlp.pt`) | Yes | No / unused online | Yes | No / unused online | N/A | N/A | Leaked baseline, not the online model |
| Old 6,000 GRU baseline (`risk_gru.pt`) | Yes | No / unused online | Yes | No / unused online | N/A | N/A | Leaked baseline, not the online model |

Direct checkpoint shape evidence reported by the audit:

- Transformer: `hist_proj.weight` shape `[128, 21]`, `action_proj.weight` shape `[128, 7]`, `static.0.weight` shape `[128, 43]`.
- MLP/GRU baselines: MLP `net.0.weight` shape `[64, 25]`, GRU `gru.weight_ih_l0` shape `[192, 25]`.
- Transformer static vector: action stats 28 + ACE/dummy padding 7 + current proprio 8 = 43.
- Transformer history token: previous proprio 8 + previous executed action 7 + ACE/dummy padding first 6 = 21.
- Remaining caveat: task identity can still leak implicitly through proprio/start-state/task geometry; this is not explicit task-id input.

## Online OpenVLA OOD Evaluation

| ID | Suite | Policies | Seeds | Path | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `openvla_ood_basic_vs_risk_100ep_20260618` | `libero_goal_object_ood`, 18 tasks | `openvla_basic` vs `openvla_risk_horizon` | 10-109 per task | `online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618` | Complete as of Bob check on 2026-06-22: 3,600/3,600 episode summaries, zero malformed JSON rows, supervisor log ends with `DONE`. Overall: `openvla_basic` 976/1800 = 54.22%; `openvla_risk_horizon` 1014/1800 = 56.33%. |
| `openvla_ood_basic_h1_100ep_20260619` | `libero_goal_object_ood`, 18 tasks | `openvla_basic_h1` fixed H=1 | 10-109 per task | `online_evals/libero_goal_object_ood_openvla_basic_h1_100ep_20260619` | Resumed/running as of 2026-06-29 09:45 CEST in tmux `openvla_ood_basic_h1_100ep_20260619`. It was interrupted at 1,720/1,800 rows; resume log confirms `1720/1800 already complete` and first resumed episode `[1721/1800] task=17 seed=30`. |

Final per-task result for the completed basic-vs-risk run:

| Task | Description | `openvla_basic` | `openvla_risk_horizon` | Delta / status |
| :---: | :--- | :---: | :---: | :--- |
| 0 | open the middle drawer of the cabinet (yellow cabinet) | 98/100 | 98/100 | neutral |
| 1 | open the top drawer and put the bowl inside (yellow bowl) | 95/100 | 96/100 | +1 |
| 2 | open the top drawer and put the bowl inside (yellow cabinet) | 70/100 | 78/100 | +8 |
| 3 | push the plate to the front of the stove (yellow plate) | 100/100 | 100/100 | neutral |
| 4 | push the plate to the front of the stove (yellow stove) | 100/100 | 100/100 | neutral |
| 5 | put the bowl on the plate (yellow bowl) | 98/100 | 98/100 | neutral |
| 6 | put the bowl on the plate (yellow plate) | 98/100 | 98/100 | neutral |
| 7 | put the bowl on the stove (yellow bowl) | 1/100 | 3/100 | +2 |
| 8 | put the bowl on the stove (yellow stove) | 0/100 | 19/100 | +19 |
| 9 | put the bowl on top of the cabinet (yellow bowl) | 0/100 | 0/100 | neutral |
| 10 | put the bowl on top of the cabinet (yellow cabinet) | 0/100 | 0/100 | neutral |
| 11 | put the cream cheese in the bowl (red cream cheese) | 100/100 | 100/100 | neutral |
| 12 | put the cream cheese in the bowl (yellow bowl) | 100/100 | 100/100 | neutral |
| 13 | put the wine bottle on the rack (brown rack) | 10/100 | 9/100 | -1 |
| 14 | put the wine bottle on the rack (green bottle) | 4/100 | 6/100 | +2 |
| 15 | put the wine bottle on top of the cabinet (green bottle) | 2/100 | 0/100 | -2 |
| 16 | put the wine bottle on top of the cabinet (yellow cabinet) | 0/100 | 9/100 | +9 |
| 17 | turn on the stove (yellow stove) | 100/100 | 100/100 | neutral |

Fixed-H1 baseline partial snapshot from 2026-06-29:

| Task | `openvla_basic_h1` completed so far | Matching `openvla_basic` H=8 subset | Matching `openvla_risk_horizon` subset |
| :---: | :---: | :---: | :---: |
| 0 | 84/100 | 98/100 | 98/100 |
| 1 | 93/100 | 95/100 | 96/100 |
| 2 | 74/100 | 70/100 | 78/100 |
| 3 | 98/100 | 100/100 | 100/100 |
| 4 | 94/100 | 100/100 | 100/100 |
| 5 | 98/100 | 98/100 | 98/100 |
| 6 | 100/100 | 98/100 | 98/100 |
| 7 | 16/100 | 1/100 | 3/100 |
| 8 | 23/100 | 0/100 | 19/100 |
| 9 | 0/100 | 0/100 | 0/100 |
| 10 | 0/100 | 0/100 | 0/100 |
| 11 | 100/100 | 100/100 | 100/100 |
| 12 | 92/100 | 100/100 | 100/100 |
| 13 | 33/100 | 10/100 | 9/100 |
| 14 | 3/100 | 4/100 | 6/100 |
| 15 | 17/100 | 2/100 | 0/100 |
| 16 | 4/100 | 0/100 | 9/100 |
| 17 | 18/20 | 20/20 | 20/20 |

Completed H1 subset aggregate at the 2026-06-29 snapshot: fixed H=1 `openvla_basic_h1` 947/1720 = 55.06%. This is incomplete because task 17 has only 20/100 rows and the log ends in `KeyboardInterrupt`.

Online runner details:

- Script: `src/run_openvla_ood_online_baseline_vs_risk_20260618.py`
- Log: `logs/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618/sweep_supervisor.log`
- Risk policy: `model_300steps.pt` from `openvla_final1890_risk_20260618`, validation Q95 threshold `0.8049`.
- Execution rule: OpenVLA predicts 8 real actions; if risk score crosses threshold, execute horizon 1, otherwise execute horizon 8. For the risk model's 10-action-token input, the 8 real OpenVLA actions are padded with 2 dummy zero action tokens. The robot never executes the padded actions.
- No OpenVLA candidate generator or ACE uncertainty replacement was validated, so this is a horizon-control test, not selected-cap action replacement.

Scheduled fixed-H1 baseline details:

- Runner: `src/run_openvla_ood_basic_h1_full_20260619.py`
- Waiter: `src/wait_then_launch_openvla_basic_h1_after_current_20260619.sh`
- Waiter log: `logs/wait_then_launch_openvla_basic_h1_after_current_20260619.log`
- H1 run log after launch: `logs/libero_goal_object_ood_openvla_basic_h1_100ep_20260619/sweep_supervisor.log`
- Policy label in JSONL: `openvla_basic_h1`
- It writes a separate `episode_summaries.jsonl` and `query_records.jsonl`; it must not be merged into the active basic-vs-risk output.

Risk model input schema used online:

- Transformer sequence branch: `[CLS]` + 16 history tokens + 10 action tokens.
- History token shape 21: previous proprio 8 + previous executed action 7 + ACE dummy/placeholder first 6.
- Action token shape 7: one predicted action vector. OpenVLA supplies 8 real action tokens; the risk feature builder pads to 10.
- Static MLP shape 43: first action 7 + action mean 7 + action std 7 + last-minus-first action delta 7 + ACE dummy padding 7 + current proprio 8.
- OpenVLA has no native stochastic candidate generator in this setup (`use_l1_regression=True`, `use_diffusion=False`), so ACE channels are hardcoded dummy zeros.

## Focused OOD Horizon Diagnostics (2026-06-19)

The long run was paused after the active episode completed, a focused diagnostic was run on the same selected rescue seeds, and the long run was resumed. The diagnostic compared fixed `openvla_basic` horizon 8, fixed `openvla_basic` horizon 1, and the current adaptive risk policy on the exact same 10 seeds.

Paths:

- H=1 diagnostic script: `src/run_focused_diagnostic_basic_h1_20260619.py`
- H=1 diagnostic output: `online_evals/focused_ood_task2_task8_basic_h1_seeds_10ep_20260619`
- Earlier H=8/basic + adaptive risk focused output: `online_evals/focused_ood_task2_task8_rescue_seeds_10ep_20260619`
- Local report artifact from the CLI session: `/home/redafrix/.gemini/antigravity-cli/brain/985aee0d-755b-4df3-84d3-c15cf75b60d1/basic_openvla_horizon_comparison.md`

| Policy / horizon | Task 8 stove seeds `[11,18,19,22,25]` | Task 2 drawer seeds `[12,14,27,43,49]` | Combined | Success steps |
| :--- | :---: | :---: | :---: | :--- |
| Basic OpenVLA, fixed H=8 | 0/5 | 0/5 | 0/10 | N/A |
| Basic OpenVLA, fixed H=1 | 0/5 | 3/5 | 3/10 | successes at 150-160 steps, average about 154 |
| Risk-aware OpenVLA, adaptive H=1/8 | 5/5 | 5/5 | 10/10 | average about 260.6 |

Seed-level summary:

| Task | Seed | Basic H=8 | Basic H=1 | Risk adaptive H=1/8 |
| :---: | ---: | :---: | :---: | :---: |
| 8 | 11 | fail 800 | fail 800 | success 307 |
| 8 | 18 | fail 800 | fail 800 | success 370 |
| 8 | 19 | fail 800 | fail 800 | success 273 |
| 8 | 22 | fail 800 | fail 800 | success 315 |
| 8 | 25 | fail 800 | fail 800 | success 279 |
| 2 | 12 | fail 800 | fail 800 | success 154 |
| 2 | 14 | fail 800 | success 152 | success 156 |
| 2 | 27 | fail 800 | fail 800 | success 157 |
| 2 | 43 | fail 800 | success 150 | success 156 |
| 2 | 49 | fail 800 | success 160 | success 163 |

## OOD Asset Package

| ID | Path | Status | Meaning |
| :--- | :--- | :--- | :--- |
| `libero_goal_object_ood_setup_package_20260618` | Batman: `libero_goal_object_ood_setup_package_20260618.zip` and folder `libero_goal_object_ood_setup_package_20260618/` | Complete | Portable package for setting up generated `libero_goal_object_ood` assets on another PC. Includes README, task manifest, BDDL/init files, installer, and verifier. |

## Interpretation Rules

1. The final OpenVLA goal-object risk model is `openvla_final1890_risk_20260618`, not the old 6,009 plain-goal model.
2. The old 6,009 dataset folder name is misleading. It is retained because it is useful for plain `libero_goal` training and cross-dataset tests, but it is not the final goal-object dataset.
3. Cross-dataset old-goal-to-goal-object tests show partial OOD transfer, not a deployment-ready risk model for goal-object.
4. The `openvla_ood_basic_vs_risk_100ep_20260618` run is complete. The separate fixed-H1 baseline run is still in progress as of the 2026-06-22 snapshot.
5. Do not compare OpenVLA numbers directly to SimVLA selected-cap numbers without noting the policy differences: OpenVLA risk currently changes execution horizon only, while SimVLA selected-cap replaces action candidates using risk scores.
