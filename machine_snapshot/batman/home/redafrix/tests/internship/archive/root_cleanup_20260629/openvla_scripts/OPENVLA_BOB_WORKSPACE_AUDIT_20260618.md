# OpenVLA Bob Workspace Audit - 2026-06-18

## Scope

Audited Bob workspace:

`/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`

This audit checks the OpenVLA-OFT setup, the corrected `libero_goal_object` data collection, and Gemini's offline risk-model results.

## Current Process State

- Host: `PCROBOTUBUNTU02`
- The large OpenVLA collection tmux session `openvla_goal_object_pro_risk_data_10000ep_20260616` is no longer running.
- The collector stopped after a user `Ctrl+C` during round 189 task 4, not due to a normal completion.
- Existing older SimVLA tmux sessions were still present and were not touched.

## Workspace Organization

The OpenVLA work is isolated in its own workspace, separate from SimVLA/FIPER:

- `src/`: OpenVLA helper scripts, smoke runners, corrected collector.
- `outputs/`: smoke outputs, discarded wrong-suite output, corrected `libero_goal_object` collection.
- `logs/`: smoke and collector logs.
- `reports/`: setup, dataset-resolution, smoke, and patch-parity reports.
- `offline_risk_experiments/`: old6000 and new partial-dataset offline training experiments.
- `hf_cache/`, `.venv`, `.venv_clean_openvla`: local OpenVLA assets/envs.

This is adequately isolated. The main reorganization needed is not physical relocation; it is marking which outputs are trusted, diagnostic, or invalid.

## Corrected Dataset Status

Corrected collection path:

`outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260617`

Verified current counts:

- `episode_summaries.jsonl`: 1894 rows
- `query_records.jsonl`: 123142 rows
- `step_records.jsonl`: 982308 rows
- `collection_status.json`: `total_episodes_completed = 1894`, `next_round = 189`, `next_task = 4`

Verified episode totals:

- Total episodes: 1894
- Successes: 789
- Failures: 1105

Per-task counts:

| Task | Episodes | Success | Failure | Success Rate | Avg Steps |
|---:|---:|---:|---:|---:|---:|
| 0 | 190 | 178 | 12 | 93.68% | 217.8 |
| 1 | 190 | 35 | 155 | 18.42% | 682.1 |
| 2 | 190 | 0 | 190 | 0.00% | 800.0 |
| 3 | 190 | 38 | 152 | 20.00% | 671.5 |
| 4 | 189 | 1 | 188 | 0.53% | 796.4 |
| 5 | 189 | 189 | 0 | 100.00% | 123.7 |
| 6 | 189 | 34 | 155 | 17.99% | 688.8 |
| 7 | 189 | 189 | 0 | 100.00% | 72.4 |
| 8 | 189 | 125 | 64 | 66.14% | 327.9 |
| 9 | 189 | 0 | 189 | 0.00% | 800.0 |

## Suite Identity

The corrected collection is on `libero_goal_object`, not plain `libero_goal`.

Task names from the dataset resolution report:

- Task 0: `open the middle drawer of the cabinet`
- Task 1: `put the bowl on the stove`
- Task 2: `put the wine bottle on top of the cabinet`
- Task 3: `open the top drawer and put the bowl inside`
- Task 4: `put the bowl on top of the cabinet`
- Task 5: `push the plate to the front of the stove`
- Task 6: `put the cream cheese in the bowl`
- Task 7: `turn on the stove`
- Task 8: `put the bowl on the plate`
- Task 9: `put the wine bottle on the rack`

BDDL/init roots point to the LIBERO-PRO workspace:

- BDDL: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files/libero_goal_object`
- Init states: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files/libero_goal_object`

## Collector Issues

The collector is usable but not perfect.

Confirmed good:

- Correct suite: `libero_goal_object`
- OpenVLA native horizon: 8
- ACE is explicitly not faked.
- SimVLA uncertainty features are explicitly unavailable.
- Query records contain action chunks, proprio, action stats, task id, reset seed.
- `(task_id, reset_seed)` is unique for all 1894 episodes, so query records can be joined to episode summaries.

Problems:

- `run_manifest.json` is missing from the corrected output root.
- `step_records.jsonl` lacks task id, reset seed, and episode id fields, making it weak for future supervised training unless reconstructed by record order.
- `query_records.jsonl` lacks `episode_index_global`; it can be joined only indirectly through `(task_id, reset_seed)`.
- The collection was interrupted mid-run at round 189 task 4 and has not reached 10000 episodes.
- The log contains a final `KeyboardInterrupt`, expected from the user pause, not a collector bug.

## Offline Training Result Validity

Gemini's report at:

`offline_risk_experiments/openvla_new1891_risk_20260618/reports/NEW_DATASET_1891EP_EVALUATION_REPORT_20260618.md`

is not fully trustworthy as a final result.

Verified issues:

- The report hard-codes `1891` episodes, `788` successes, and `1103` failures. Current dataset contains 1894 episodes, 789 successes, and 1105 failures.
- The script selects `best_f1`, `q90`, and `q95` thresholds on the test set, despite the comment saying validation. This leaks test information and inflates the reported operating points.
- Splits are episode-disjoint, which is good, but not round-held-out.
- Task identity can be a major shortcut: tasks 2 and 9 have zero successes, while tasks 5 and 7 have zero failures in the current partial dataset.
- No ablation was run without task id or timestep, so the model may partly learn task difficulty or timeout structure rather than transferable physical risk.

## Corrective Action Launched

Uploaded and launched a corrected, non-overwriting rerun:

- Script: `offline_risk_experiments/train_and_eval_new_dataset_corrected.py`
- Output folder: `offline_risk_experiments/openvla_new1894_risk_corrected_20260618`
- Tmux: `openvla_new1894_corrected_offline_20260618`

Fixes in the corrected script:

- Counts are derived from JSONL files.
- Thresholds are selected on validation/calibration only.
- The output report explicitly documents remaining limitations.
- The old Gemini outputs are preserved unchanged.

## Current Verdict

- OpenVLA workspace isolation: acceptable.
- Corrected `libero_goal_object` data collection: valid partial dataset, incomplete at 1894/10000 episodes.
- Gemini's original 1891 offline report: useful diagnostic, not final science.
- Corrected offline rerun: in progress and should be used instead for any serious comparison.

