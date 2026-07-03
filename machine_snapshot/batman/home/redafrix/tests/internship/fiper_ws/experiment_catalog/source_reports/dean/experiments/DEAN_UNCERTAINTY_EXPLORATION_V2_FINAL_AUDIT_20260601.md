# Dean Uncertainty Exploration v2 Final Audit (2026-06-01)

## Scope

Dean collection remained paused. This run tested whether the new SimVLA uncertainty features can improve the current transformer risk detector.

Dataset snapshot:

- Valid episodes: `4191`
- Successes: `3405`
- Failures/timeouts: `786`
- Excluded bad tasks: `libero_10_object/task_4`, `libero_goal_object/task_9`

## Fixes Compared to v1

- Fixed the failure split bug: previous `random_mixed` left almost no failure-test episodes because it reserved failure calibration rows that were never used.
- Added `all_tasks_random`, which trains over all tasks/suites and evaluates held-out episodes from the same global distribution.
- Added several uncertainty uses:
  - `unc_raw`: base inputs + raw 49D uncertainty + 49D delta.
  - `unc_summary`: base inputs + compact summary statistics of uncertainty/delta.
  - `unc_summary_only`: only compact uncertainty summaries.
  - `unc_raw_dropout`: raw uncertainty with static-input dropout.
- Added post-hoc fusion policies between the trained `base` and `unc_raw` models.

## Main Results

### All Tasks Random

This answers: "if we train on all tasks, are results good?"

| Policy | Seen FA | Failure Det | Det@25 | Det@50 |
|---|---:|---:|---:|---:|
| base | 0.0% | 0.0% | 0.0% | 0.0% |
| unc_raw | 5.6% | 93.3% | 12.2% | 62.8% |
| avg_75base_25unc | 5.6% | 92.8% | 12.2% | 65.0% |
| avg_50base_50unc | 7.2% | 93.9% | 20.0% | 68.3% |
| soft_veto_base_times_unc | 11.7% | 95.6% | 30.6% | 71.7% |

Verdict: yes, when all tasks are represented in training, the uncertainty features clearly help under this calibration. The best low-FA candidate is `unc_raw`; the best early-warning candidate is `soft_veto_base_times_unc`.

### OOD Suite: Hold Out `libero_90`

| Policy | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|
| base | 31.2% | 81.9% | 42.3% | 72.7% |
| unc_raw | 31.5% | 85.4% | 42.7% | 74.6% |
| max_base_unc | 29.2% | 84.6% | 37.3% | 74.2% |
| mild_veto_unc_q95_or_base_q99 | 55.4% | 94.2% | 65.4% | 88.5% |

Verdict: `max_base_unc` is the best balanced OOD-suite result. It improves FA, detection, and Det@50 versus base, but Det@25 is lower. The aggressive veto policies improve recall strongly but are too high-FA for deployment.

### OOD Task Holdout

| Policy | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 |
|---|---:|---:|---:|---:|
| base | 11.9% | 81.5% | 3.2% | 49.2% |
| unc_raw | 1.9% | 62.9% | 0.0% | 7.3% |
| avg_50base_50unc | 8.8% | 79.8% | 2.4% | 48.4% |
| mild_veto_unc_q95_or_base_q99 | 10.0% | 83.9% | 4.0% | 57.3% |
| hard_veto_unc_q95_or_base_q99 | 10.0% | 83.9% | 4.0% | 57.3% |

Verdict: the `mild/hard_veto_unc_q95_or_base_q99` fusion is a real improvement over base on this split: lower FA, higher detection, and better Det@50.

## Final Interpretation

The uncertainty features should not be appended blindly as a replacement detector. Used raw, they often become conservative and lower false alarms by missing failures.

But they are useful:

- On all-task training, `unc_raw` makes the detector work while base fails under the same conformal calibration.
- On `ood_suite_libero90`, `max_base_unc` gives a better balance than base.
- On `ood_task_holdout`, the q95/q99 veto fusion improves all key OOD metrics versus base.

## Recommended Next Candidate

Use a two-model fusion policy:

- Train `base`.
- Train `unc_raw`.
- Evaluate:
  - `max_base_unc` for suite-shift style OOD.
  - `mild_veto_unc_q95_or_base_q99` for task-holdout style OOD.

The next serious step should be a validation-based meta-policy that chooses between these fusion rules using only seen validation buckets, rather than picking per test split.

## Artifact Paths

Remote Dean:

- Transformer variants: `/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_transformer_exploration_v2_20260601`
- Fusion policies: `/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_fusion_policy_v1_20260601`

Local copies:

- `fiper_ws/reports/dean_uncertainty_exploration_v2_20260601/dean_uncertainty_comparison_results.csv`
- `fiper_ws/reports/dean_uncertainty_exploration_v2_20260601/dean_uncertainty_fusion_policy_results.csv`

