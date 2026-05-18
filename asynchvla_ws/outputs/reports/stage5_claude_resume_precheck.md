# Stage 5 Claude Resume Precheck

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`
Workspace: `/media/rootalkhatib/My Passport/reda_ws`
Branch: `bob`
Date: 2026-05-13

## Environment

- `which python3` -> `/usr/bin/python3`
- `python3 --version` -> Python 3.10.12
- Torch 2.5.1+cu121, CUDA True (per stage5_preflight)
- Activation: `asynchvla_ws/scripts/activate_simvla_bob.sh` works.

## Git status (relevant lines)

```
branch: bob
 M outputs/checkpoints/stage5_debug/predictions.json
?? outputs/reports/stage5_debug_rater_metrics.md
?? train_stage5_rater.py   # stray copy at repo root, NOT the intended path
```

## Rater script status

- Intended path: `asynchvla_ws/src/rater/train_stage5_rater.py` (7.9K, modified 16:22).
  Inspection: this file is the OLD version. It does **not** define `NpEncoder` and contains three bare `json.dumps(...)` calls (lines 170, 173, 176) that can fail on numpy types.

- Stray copy: `asynchvla_ws/train_stage5_rater.py` (8.2K, modified 16:37).
  Inspection: this file does have `NpEncoder` (lines 104-109) and uses `cls=NpEncoder` on all three `json.dumps` calls.

Conclusion: Gemini fixed the wrong file. The intended script at `src/rater/train_stage5_rater.py` is still broken w.r.t. NpEncoder, and additionally still uses a row-order debug split (first 400 / last 100) which is **not** context-level and can leak rows from the same context_id between train and calib partitions. Phase B will overwrite `src/rater/train_stage5_rater.py` with the corrected, context-level version and remove the stray root copy from active use (we will NOT delete it; the user rule says no deletes — we will leave it untouched).

## Debug data state

`asynchvla_ws/data/stage5_debug/`:
- `multiseed_trace_debug.pt` (647K) — 50 contexts, seeds 0..4, no all-identical contexts (per stage5_multiseed_trace_debug.md).
- `multiseed_candidate_debug.pt` (2.8M) — 500 candidates, 50 unique context_ids, 10 candidate types as expected.
  Direct load confirms: `pooled_vlm_features` shape `[960]`, `proprio` `[8]`, `candidate_action_normalized` `[10, 7]`.

`asynchvla_ws/outputs/reports/` already contains:
- `stage5_preflight.md`, `stage5_multiseed_trace_debug.md`, `stage5_multiseed_candidate_debug.md`,
  `stage5_simvla_only_eval_utility.md`, `stage5_debug_rater_metrics.md` (v1 from the old run).

`asynchvla_ws/data/processed_stage5/` does **not** exist yet. Medium datasets must be built.

## Split manifests present

All present under `asynchvla_ws/data/splits/`:
- `id_task_split.json` (23K)
- `holdout_libero_object.json` (23K)
- `holdout_object_bowl.json` (23K)
- (others: scene/object holdouts also available)

## Eval / data-building utilities present

- `src/eval/eval_simvla_only.py` — SimVLA-only metrics: Pearson/Spearman, AUROC, pairwise seed ranking, best-seed selection, risk-coverage, switch proxy (1/4/3 lines look fine).
- `src/data_building/build_multiseed_trace_dataset.py` (160 lines) — supports both `--debug true` and full split-manifest mode.
- `src/data_building/build_multiseed_candidate_dataset.py` (100 lines) — supports both modes.

## Plan derived from precheck

1. Overwrite `src/rater/train_stage5_rater.py` with a corrected version that:
   - defines a complete `NpEncoder` (np.integer, np.floating, np.ndarray, torch.Tensor, Path),
   - uses every `json.dumps` with `cls=NpEncoder`,
   - performs **context-level** train/val splits on debug,
   - reports counts by context_id and row count,
   - computes both full-candidate and SimVLA-only metrics,
   - compares full / context-only / action-only baselines,
   - handles `--debug` with both bool and string forms,
   - is robust to missing partitions and shape variations.
2. Run debug, interpret, then build medium datasets and continue.

Note on time risk: medium dataset build calls SimVLA five times per context (one per seed) plus VLM encoding. For 1000 train contexts that is on the order of 5000 forward passes; Phase D may be the longest single step. We will start with 1000/250/250 sizes and reduce if time becomes a problem.
