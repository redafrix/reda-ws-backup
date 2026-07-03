# Prompt For The Other Repository Agent

You are auditing a result discrepancy between two implementations of LIBERO Pro
`libero_goal_object` evaluation for SimVLA. You have this zip from the first
repo and you are working inside the second repo. Your job is to determine
whether one implementation is wrong, or whether both are valid but differ in
benchmark definition, environment setup, prompts, seeds, action execution,
camera/preprocessing, reset behavior, success predicates, or policy inference.

Do not stop at a superficial diff. Produce a written report with exact file
paths, line references where possible, and a clear conclusion.

## Known Reference From First Repo

The first repo's reference run is:

- Suite: `libero_goal_object`
- LIBERO implementation label in manifest: `LIBERO-PRO`
- Episode count: 100
- Tasks: task IDs 0-9, initial states/trials 0-9
- `eval_seed`: 0
- `episode_seed`: same as `trial_index`
- Prompt source: `task_language`
- HF/base SimVLA result: 49/100 success, 392.9814066740091 wall seconds
- Run output: `files/mimic-video/results/libero_goal_object_100_official_tasklang_20260623/hf_simvla/`
- Exact manifest: `files/mimic-video/configs/uq_benchmarks/libero_goal_object_task0to9_trials0to9_eval_seed0_tasklang_20260623.csv`
- Config: `files/mimic-video/configs/arbiter/goal_object_100_tasklang_hf_simvla_20260623.json`

There is also a modified SimVLA top-k8 run in:

- Config: `files/mimic-video/configs/arbiter/goal_object_100_tasklang_modified_simvla_topk8_q95_20260623.json`
- Results: `files/mimic-video/results/libero_goal_object_100_official_tasklang_20260623/modified_simvla_topk8_q95/`
- Top-k risk metadata: `files/simvla_modified_risk_topk8_h10_20260608/risk_models/h10_unc_topk8/`

## Required Investigation

1. Compare the exact episode set.
   - Match task IDs, task names, BDDL filenames, BDDL content, initial state
     files, initial state indices, trial ordering, eval seeds, episode seeds,
     and prompt strings.
   - Use the first repo manifest CSV as the ground-truth list of episodes to
     compare against.

2. Compare LIBERO Pro implementation details.
   - Compare task suite registration, task-to-BDDL mapping, BDDL parser usage,
     environment construction, reset/init state loading, object/asset
     definitions, predicate/success checks, robot/action space, controller
     settings, camera names, camera dimensions, and max episode length.
   - Inspect first repo files under:
     - `files/LIBERO-PRO-HF/bddl_files/libero_goal_object/`
     - `files/LIBERO-PRO-HF/init_files/libero_goal_object/`
     - `files/LIBERO-PRO/libero/libero/benchmark/`
     - `files/LIBERO-PRO/libero/libero/envs/`
     - `files/LIBERO-PRO/libero/libero/utils/`

3. Compare SimVLA inference.
   - Compare model checkpoint identity, norm stats, image resize/crop path,
     camera selection, language prompt source, action normalization and
     denormalization, action dimensionality, gripper convention, action horizon,
     execution horizon, warmup/history length, denoising steps, stochastic
     seeds, and whether actions are clipped or transformed.
   - Inspect first repo files:
     - `files/mimic-video/scripts/run_simvla_world_model_arbiter.py`
     - `files/mimic-video/eval/libero/run.py`
     - `files/SimVLA_modified/models/`
     - `files/SimVLA_modified/datasets/`
     - `files/SimVLA_modified/norm_stats/libero_norm.json`

4. Compare top-k8 or modified SimVLA logic if relevant.
   - Identify whether the second repo is running plain HF/base SimVLA,
     modified SimVLA, or top-k8 uncertainty selection.
   - Compare expected top-k dims, candidate count, risk score source,
     thresholds, model denoise steps, and fallback/selection behavior.
   - Inspect:
     - `files/simvla_modified_risk_topk8_h10_20260608/`
     - `files/SimVLA_modified/phase2_tdqc/`

5. Compare outcome logs episode by episode.
   - From first repo, parse `episode_summaries.jsonl` and the manifest CSV.
   - In the second repo, produce the same per-episode table if possible:
     `episode_uid`, task ID, init index, seed, prompt, success/failure, steps,
     final status/reason.
   - Highlight all episodes where success differs. Group discrepancies by task.

6. Determine correctness.
   - If one repo violates the official LIBERO Pro task definitions or a stated
     benchmark protocol, say which one and show evidence.
   - If both are internally correct but evaluate different protocols, say so
     precisely and enumerate each protocol difference.
   - If the difference is likely stochastic, quantify what is controlled and
     uncontrolled, and identify the minimum rerun needed to prove it.

## Required Report Format

Write a report with these sections:

1. Executive conclusion: one paragraph stating whether repo A, repo B, both, or
   neither are correct.
2. Reproduction table: exact benchmark name, task set, episode count, seeds,
   prompt source, model/checkpoint, preprocessing, action horizon, max steps,
   and success-rate definition for both repos.
3. File-by-file differences: exact paths and line references for meaningful
   differences.
4. Episode-level outcome comparison: include mismatched episode IDs and grouped
   per-task summary.
5. Root-cause analysis: rank differences by likelihood of causing the score gap.
6. Fixes or alignment steps: concrete edits or commands needed so both repos run
   the same benchmark.
7. Residual uncertainty: list anything not provable from available files.

Be strict about evidence. Do not claim an implementation is wrong unless you can
point to a concrete mismatch against the declared protocol or official task
definition.

