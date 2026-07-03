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
| Bob / `pcrobot` | OK | RTX 4070 Ti SUPER, GPU active | q95 full-suite OOD risk-only sweep running in tmux `ood_production_threshold_q95_100ep_202610` |
| Sam / `sam` | OK | RTX 4070 Ti SUPER, idle | No active tmux after V2B/V2C/V2D diagnostics completed |
| Dean / `dean-via-bob` | Direct SSH flaky; reachable via Bob | RTX A5000, active | selected-cap OOD 100ep confirmation running in tmux `dean_selected_cap_t03_c04_100ep_20260610` |

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

Status during audit: running on Bob. Partial raw count at 2026-06-10 18:39 CEST:

| Task | Completed | Success |
|---|---:|---:|
| cumulative | 922 | 864 |

Trust: pending. Do not cite global q95 performance until all 1,800 episodes finish and pairing against the Campaign 7 modified baseline is recomputed.

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

The 10ep diagnostic completed with modified SimVLA 170/180 and selected-cap TopK8 176/180, with 7 rescues and 1 regression. The 100ep confirmation is running and must finish before any final claim is made.

## Catalog Corrections Made

Updated local catalog files:

- `MASTER_EXPERIMENT_INDEX.md`: Campaign 7 corrected to complete, Campaign 8 threshold 0.5 added, Campaign 9 q95 active added, Sam V2 diagnostics added.
- `TRUSTED_RESULTS_SUMMARY.md`: q95 pending and Sam V2B/V2C/V2D trusted-negative diagnostics added.
- `KEY_RESULTS.md`: current active work and OOD full-suite summary updated.
- `HOST_WORKSPACE_MAP.md`: Bob q95 active status, Dean direct SSH status, and Dean OOD asset caveat updated.
- `SYNC_STATUS.md`: 2026-06-10 update log added.
- `hosts/bob.md`: recent OOD campaign paths added.
- `hosts/sam.md`: V2D path added.
- `inventory.json`: q95 and Sam V2 entries added; backup saved as `inventory.json.20260610_codex_full_audit.bak`.

## Catalog Sync Verification

The catalog was synchronized to Bob, Sam, and Dean with `checks/sync_catalog.sh`. The following SHA256 hashes matched on local, Bob, Sam, and Dean:

| File | SHA256 |
|---|---|
| `MASTER_EXPERIMENT_INDEX.md` | `19815bb3e25419383b9acbde5ab2b26688b2e9351867a3b69ecdc5c89ad3b359` |
| `TRUSTED_RESULTS_SUMMARY.md` | `0357301de9f737a791ef052221c50016be87773100c64baeb583e39a0d85ef6a` |
| `SYNC_STATUS.md` | `6b15fed7b6c936c91e825bb25d5eb077a904a11f66517bb5dabb4576b2a37448` |
| `inventory.json` | `455047d07d913cd38e4331f5ec82156e632de649a01bbcb078164a2b07968e02` |

## Current Trust Verdict

- Mechanically trusted: Bob 10ep OOD threshold 0.3, Bob 100ep OOD threshold 0.3, Bob 100ep OOD threshold 0.5, Sam V2B/V2C/V2D diagnostics.
- Scientifically positive: only the 10ep threshold 0.3 OOD signal is positive, but it is weak and did not hold at N=100.
- Scientifically negative or neutral: Bob 100ep threshold 0.3 hurts, threshold 0.5 ties, Sam V2B/V2C/V2D hurt.
- Pending: Bob q95 sweep.

## Next Verification Needed

1. Let Bob q95 finish, then recompute raw paired results against the Campaign 7 modified baseline.
2. Let Dean selected-cap 100ep confirmation finish, then recompute full paired raw JSONL analysis against its own fixed-H10 modified baseline.
3. Do not claim risk-aware OOD improvement until a full-suite N=100 run beats modified SimVLA in paired raw JSONL analysis.
