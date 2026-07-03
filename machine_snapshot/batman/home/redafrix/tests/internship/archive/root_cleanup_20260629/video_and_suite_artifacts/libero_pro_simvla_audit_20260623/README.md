# LIBERO Pro SimVLA Audit Bundle

Created from `/home/utilisateur/worldmodel` on 2026-06-23.

This package is for comparing this repository's LIBERO Pro `libero_goal_object`
implementation and SimVLA inference path against another repository.

## Primary Run

The run matching the latest note `HF/base SimVLA 49/100 392.98s` is:

- Results: `files/mimic-video/results/libero_goal_object_100_official_tasklang_20260623/`
- Audit: `files/mimic-video/results/libero_goal_object_100_official_tasklang_20260623/audit_report.json`
- HF/base config: `files/mimic-video/configs/arbiter/goal_object_100_tasklang_hf_simvla_20260623.json`
- Modified top-k8 config: `files/mimic-video/configs/arbiter/goal_object_100_tasklang_modified_simvla_topk8_q95_20260623.json`
- Exact episode manifest: `files/mimic-video/configs/uq_benchmarks/libero_goal_object_task0to9_trials0to9_eval_seed0_tasklang_20260623.csv`

The exact episode manifest has 100 episodes: task IDs 0-9, trials/initial
states 0-9, `eval_seed=0`, `episode_seed` equal to the trial index, and
`prompt_source=task_language`.

The audit report records:

- `world_model`: 49/100, 622.3583218889953 seconds
- `simvla` / HF-base SimVLA: 49/100, 392.9814066740091 seconds
- per-task success rates and agreement/disagreement with the world model

## Included Content

- Exact 100-episode manifest CSV and arbiter configs.
- Complete structured result logs for HF/base SimVLA, modified SimVLA top-k8,
  and WM h56 k1 for this run.
- Core SimVLA inference/evaluation source:
  `run_simvla_world_model_arbiter.py`, launch scripts, audit scripts, and
  `eval/libero` entrypoints.
- LIBERO Pro goal-object BDDL and pruned init files from `LIBERO-PRO-HF`.
- Selected LIBERO Pro environment, benchmark, utility, and config source from
  `LIBERO-PRO`.
- Modified SimVLA model/runtime source and top-k8 uncertainty implementation
  files from `SimVLA_modified`.
- SimVLA modified risk bundle metadata, checkpoint config/state, checksums,
  top-k8 risk model config/normalization/thresholds/history/metrics, and the
  small risk model `model.pt`.

## Explicitly Excluded

Large generated or binary files were excluded to keep this package portable:

- `*.safetensors`, including the 3.1 GB modified SimVLA checkpoint weights.
- `*.pyc`, `__pycache__/`, generated plots, and videos.
- Large candidate/action variance array dumps from unrelated or older runs.

If the other repository needs to rerun the exact policy, it must use its own
model weights or fetch the same referenced checkpoints. This package is meant
to compare implementation, configuration, task definitions, seeds, prompts,
and structured outcomes.

## Suggested First Files To Read

1. `PROMPT_FOR_OTHER_AGENT.md`
2. `files/mimic-video/results/libero_goal_object_100_official_tasklang_20260623/audit_report.json`
3. `files/mimic-video/configs/uq_benchmarks/libero_goal_object_task0to9_trials0to9_eval_seed0_tasklang_20260623.csv`
4. `files/mimic-video/configs/arbiter/goal_object_100_tasklang_hf_simvla_20260623.json`
5. `files/mimic-video/scripts/run_simvla_world_model_arbiter.py`
6. `files/LIBERO-PRO-HF/bddl_files/libero_goal_object/`
7. `files/LIBERO-PRO-HF/init_files/libero_goal_object/`

