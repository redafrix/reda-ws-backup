# Codex Full Workspace Audit - 2026-06-10

This report records checks performed directly by Codex from raw configs, JSONL episode summaries, remote host status, and workspace catalog files. It separates raw evidence from Gemini/Antigravity narrative reports.

## Scope

- Local workspace: `/home/redafrix/tests/internship`
- Catalog root: `/home/redafrix/tests/internship/fiper_ws/experiment_catalog`
- Hosts checked: Bob (`pcrobot`), Sam (`sam`), Dean (`dean` and `dean-via-bob`)
- Focus: H10 risk-aware campaigns, OOD goal-object generated suite, Sam adaptive-horizon variants, catalog consistency.

## Host Status Snapshot

| Host | SSH | GPU | Active experiment state |
|---|---|---|---|
| Bob / `pcrobot` | OK | RTX 4070 Ti SUPER, idle in latest check | OOD 0.3/0.5/q95 full-suite sweeps complete; no active q95 process |
| Sam / `sam` | OK | RTX 4070 Ti SUPER, idle | No active tmux after V2B/V2C/V2D diagnostics completed |
| Dean / `dean-via-bob` | Direct SSH flaky; reachable via Bob | RTX A5000, active | selected-cap OOD 100ep confirmation complete; delay30 replication running in tmux `dean_selected_cap_delay30_100ep_20260611` |

## OOD Asset Identity

Bob and Sam both contain the generated OOD goal-object assets:

- BDDL: `.../LIBERO-PRO/libero/libero/bddl_files/libero_goal_object_ood_temp`
- Init files: `.../LIBERO-PRO/libero/libero/init_files/libero_goal_object_ood`
- The standard BDDL folder `libero_goal_object_ood` is absent on Bob/Sam; the experiment-local runner maps the suite to `_temp`.
- Hash spot checks matched between Bob and Sam for representative BDDL/init files.

Dean now contains an experiment-local OOD asset fallback copied from Bob/Sam:

- BDDL fallback: `/home/dean/LIBERO-PRO/libero/libero/bddl_files/libero_goal_object_ood_temp`
- Init fallback: `/home/dean/LIBERO-PRO/libero/libero/init_files/libero_goal_object_ood`
- Important: `/home/dean/LIBERO-PRO` is a partial fallback tree, not a full LIBERO-PRO checkout. Dean experiments still import from `/home/redafrix/LIBERO-PRO`; the isolated collector resolves only the OOD BDDL/init files from the fallback.
- The Dean selected-cap runner was patched locally under `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/src` so canonical LIBERO-PRO files are not modified.

## Recomputed Bob Results

### Corrected 10ep OOD Goal-Object Sweep, threshold 0.3

Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609`

| Policy | Success | Rate | Mean steps |
|---|---:|---:|---:|
| original_simvla | 169/180 | 93.89% | 127.16 |
| modified_simvla | 168/180 | 93.33% | 122.41 |
| modified_h10_risk_topk8 | 172/180 | 95.56% | 118.49 |

Trust: mechanically valid, but N=10 per task is weak statistically.

### Corrected 100ep OOD Goal-Object Sweep, threshold 0.3

Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609`

| Policy | Success | Rate | Mean steps |
|---|---:|---:|---:|
| original_simvla | 1668/1800 | 92.67% | 127.62 |
| modified_simvla | 1718/1800 | 95.44% | 119.89 |
| modified_h10_risk_topk8 | 1713/1800 | 95.17% | 120.08 |

Trust: mechanically valid and complete. Scientific outcome: risk-aware threshold 0.3 is net negative vs modified SimVLA globally.

### Corrected 100ep OOD Goal-Object Sweep, threshold 0.5

Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_0.5_20260610`

| Policy | Success | Rate | Mean steps |
|---|---:|---:|---:|
| modified_h10_risk_topk8 | 1718/1800 | 95.44% | 120.29 |

Compared against the threshold 0.3 campaign's modified baseline, threshold 0.5 ties the baseline globally. It reduces harmful interventions but does not outperform modified SimVLA.

### 100ep OOD Goal-Object Sweep, q95

Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610`

Status: complete on Bob. Raw count at final audit:

| Policy | Success | Rate | Mean steps |
|---|---:|---:|---:|
| original_simvla | 1668/1800 | 92.67% | 127.62 |
| modified_simvla | 1718/1800 | 95.44% | 119.89 |
| modified_h10_risk_topk8 q95 | 1710/1800 | 95.00% | 120.78 |

Paired against the Campaign 7 modified baseline: 10 rescues / 18 regressions, net -8. Trust: mechanically valid and complete, but net negative scientifically.

## Recomputed Sam Results

Baseline source for paired comparison: V2B root fixed H10 `modified_simvla`, 171/180 successes.

| Variant | Root | Success | Mean steps | Paired vs modified baseline | Verdict |
|---|---|---:|---:|---:|---|
| V2B H1/H10 | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2b_feature_preserving_adaptive_horizon_20260610` | 167/180 | 126.51 | 2 rescues / 6 regressions, net -4 | HURTS |
| V2C H5/H10 | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2c_h5_adaptive_horizon_20260610` | 169/180 | 123.82 | 1 rescue / 3 regressions, net -2 | HURTS |
| V2D commit gate | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2d_commit_gate_20260610` | 168/180 | 123.33 | 6 rescues / 9 regressions, net -3 | HURTS |

The original V2 run was invalidated because it omitted ACE candidate generation and changed the detector input distribution. V2B/V2C/V2D restored ACE candidate generation and score only the planned/main chunk.

Important caveat for V2D: committed tail actions may be executed while current ACE features are computed from the fresh candidate set at t+5. This does not invalidate the logged result, but it means V2D is not a clean proof that risk scoring on the committed tail was evaluated directly.

## Dean Selected-Cap Gate Follow-Up

After the negative/neutral Bob threshold sweeps and Sam adaptive-horizon diagnostics, Codex launched an isolated Dean-only test of a stricter TopK8 replacement rule:

- Root 10ep: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_10ep_20260610`
- Root 100ep confirmation: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610`
- Runner: `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/src/run_policy_matrix_selected_cap.py`
- Suite: `libero_goal_object_ood`
- Gate: `selection_main_threshold=0.3`, `selection_min_margin=0.02`, `selection_strong_margin=0.05`, `selection_max_selected_score=0.4`
- Checkpoint hash: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- Detector hash: `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d`

The 10ep diagnostic completed with modified SimVLA 170/180 and selected-cap TopK8 176/180, with 7 rescues and 1 regression. The 100ep confirmation is now complete and globally positive.

### Interim 100ep Forensic Check

Codex rechecked the active Dean selected-cap 100ep run directly from raw configs, manifests, episode summaries, and `step_scores_risk_topk8.jsonl` at 2026-06-10 21:32 CEST.

Verified:

- 36 task policy configs are present, plus `seed_plan.json`.
- Seeds are `300..399` and match between baseline and risk policy for every checked task.
- Runtime manifests point to `libero_goal_object_ood`, H10 execution, and detector directory `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/unc_topk8`.
- Config schema uses `risk_model_unc_topk8_dir`, not `risk_model_dir`.
- Runner SHA256: `3e071164def5c48a9c54f9f4ab96b18069f4edd4238c29c5295e9d2522fa05c5`.
- Modified SimVLA checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`.
- TopK8 detector SHA256: `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d`.
- Thresholds: q95 `0.6155413389205933`, q99 `0.9665935635566711`.

Results snapshot:

| Task | Modified SimVLA | TopK8 selected-cap | Paired result |
|---:|---:|---:|---:|
| 0 | 75/100 | 90/100 | 21 rescues / 6 regressions, net +15 |
| 1 | 94/100 | 95/100 | 1 rescue / 0 regressions, net +1 |
| 2 | 91/100 | 90/100 | 0 rescues / 1 regression, net -1 |
| 3 | 98/100 | 96/100 | 0 rescues / 2 regressions, net -2 |
| 4 | 100/100 | 53/53 active | no paired difference so far |

Completed-task cumulative result: modified SimVLA `358/400`, selected-cap risk `371/400`, paired `22 rescues / 9 regressions`, net `+13`.

Every Task 0-3 rescue and regression had at least one actual replacement. A post-hoc gate sweep suggested delaying early replacements as a possible improvement.

### Final 100ep Result

Final Dean selected-cap report:

`source_reports/dean/reports/DEAN_SELECTED_CAP_FINAL_ANALYSIS_20260611.md`

| Metric | Modified SimVLA fixed H10 | TopK8 selected-cap |
|---|---:|---:|
| Episodes | 1,800 | 1,800 |
| Successes | 1,726/1,800 | 1,741/1,800 |
| Success rate | 95.89% | 96.72% |
| Mean steps | 117.71 | 116.69 |
| Paired rescues | - | 38 |
| Paired regressions | - | 23 |
| Paired net gain | - | +15 |
| Query modification rate | - | 1,402/21,800 (6.43%) |

Verdict: trusted positive full-suite OOD result. A follow-up replication using seeds 400-499 and `selection_min_timestep=30` is running on Dean at:

`/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_delay30_100ep_20260611`

## Catalog Corrections Made

Updated local catalog files:

- `MASTER_EXPERIMENT_INDEX.md`: Campaign 7 corrected to complete, Campaign 8 threshold 0.5 added, Campaign 9 q95 completed, Sam V2 diagnostics added.
- `TRUSTED_RESULTS_SUMMARY.md`: q95 completed net-negative and Sam V2B/V2C/V2D trusted-negative diagnostics added.
- `KEY_RESULTS.md`: current active work and OOD full-suite summary updated.
- `HOST_WORKSPACE_MAP.md`: Bob q95 completed status, Dean direct SSH status, and Dean OOD asset caveat updated.
- `SYNC_STATUS.md`: 2026-06-10 update log added.
- `hosts/bob.md`: recent OOD campaign paths added.
- `hosts/sam.md`: V2D path added.
- `inventory.json`: q95 and Sam V2 entries added; backup saved as `inventory.json.20260610_codex_full_audit.bak`.
- `source_reports/dean/reports/DEAN_SELECTED_CAP_INTERIM_FORENSIC_AUDIT_20260610.md`: added raw Dean selected-cap interim forensic audit.

## Catalog Sync Verification

The catalog was synchronized to Bob, Sam, and Dean with `checks/sync_catalog.sh`. The following SHA256 hashes matched on local, Bob, Sam, and Dean:

| File | SHA256 |
|---|---|
| `MASTER_EXPERIMENT_INDEX.md` | `51f2b4ad6aa229e224d024e3af0985124804467b8d1265a7bfed510877f10432` |
| `TRUSTED_RESULTS_SUMMARY.md` | `2157465c4d2d0698a546a2ebf65c52cd49da118460cf975916f7a7319e729361` |
| `KEY_RESULTS.md` | `bae0a614b667b559bb4b895a8ec59687be23c8c958ca250c4ecbc37b75fef4af` |
| `SYNC_STATUS.md` | `13ddc6b4f8305b210affefa99982e253b6502a47c1778a7eb1b374ce0d06af33` |
| `HOST_WORKSPACE_MAP.md` | `8f76c2efc7d1fd3eae8ec6ab1590f4806e22cfeb5821d31e3fa1421e97687509` |
| `hosts/bob.md` | `3ae41fe7433594f5b37c7fdc662b5ac96e774dec42902e8627c488198eb78575` |
| `README.md` | `5a2518f87011a12c0166d496bf098c8acf4a9f9bd552dacd6933e36f91b337a7` |
| `CLI_SESSION_PROVENANCE_20260610.md` | `b2c52edf2a091a8e8fc2d5f568e53e6ce2bfb8c96fdcd6e42b6a015617ae95d0` |
| `DEAN_SELECTED_CAP_GATE_20260610.md` | `b72fbce6a829d3e1f18e26645aeb00ba8356f62de11247c5109cbaf7fbc96795` |
| `inventory.json` | `f314c13317b2a1cf291454e764c1053cf9160afba6d83322c56ef25f2e0bdfc1` |
| `source_reports/bob/reports/BOB_Q95_OOD_FINAL_ANALYSIS_20260610.md` | `935ee19163581cdbe4c63990d3a2b8c202b3e7f0242d445cb30ba3136e91a0bb` |
| `source_reports/bob/reports/GOAL_OBJECT_CHUNK10_OFFICIAL_MODIFIED_100EP_20260605.md` | `6ac7a403153ad8740c82790d2edea50d2b768a3cca79ae8c50838671dcd86c21` |

## Current Trust Verdict

- Mechanically trusted: Bob 10ep OOD threshold 0.3, Bob 100ep OOD threshold 0.3, Bob 100ep OOD threshold 0.5, Sam V2B/V2C/V2D diagnostics.
- Scientifically positive: only the 10ep threshold 0.3 OOD signal is positive, but it is weak and did not hold at N=100.
- Scientifically negative or neutral: Bob 100ep threshold 0.3 hurts, threshold 0.5 ties, Sam V2B/V2C/V2D hurt.
- Positive: Dean selected-cap 100ep confirmation is trusted and globally positive.
- Pending: Dean delay30 selected-cap 100ep replication.

## Next Verification Needed

1. Let Dean delay30 selected-cap 100ep replication finish, then recompute full paired raw JSONL analysis.
2. Compare delay30 against the successful selected-cap run to see whether delayed replacements reduce regressions without losing rescues.
