# Sam Mimic-style SimVLA H10 risk-head ablation — frozen protocol

Date: 2026-08-18
Machine: Sam / PCROBOTUBUNTU05
Clean worktree: `/home/rootalkhatib/test/reda_ws_current_20260818`
Branch: `experiment/sam-mimic-head-ablation-h10-20260818`

## Scientific goal

This is an **architecture / feature-family ablation**, not an attempt to beat the promoted TopK8 detector.

Train a SimVLA H10 risk monitor that stays as close as possible to the supplied Mimic/video-model **Single-Head GRU — K1 Combined without ACE** monitor, while preserving the native SimVLA policy and LIBERO action semantics.

Primary outputs are offline detector metrics only: success-episode false alarm, failed-episode detection, Det@25, Det@50, AUROC and AUPRC. No online intervention is part of this experiment.

## Collection scope — immutable

Collect **only official LIBERO-PRO Goal-Object**, exactly the 10 official tasks.

Do not collect Goal-Swap, Goal-Task, Spatial-Object, Object-Object, LIBERO-10-Object, LIBERO-90 or any local/generated suite in this training campaign.

Target size: **1000 complete episodes = 100 per task**.

Use the official 50 initial states per task with two independent policy-sampling seeds per initial state.

The two episodes derived from the same `(task_id, init_state_idx)` must always remain in the same data assignment to prevent reset-state leakage.

Assignment by init-state index, identically for every task:

- training: init states 0..29 -> 30 states x 2 seeds x 10 tasks = 600 episodes
- id_development: init states 30..39 -> 10 states x 2 seeds x 10 tasks = 200 episodes
- successful_calibration: init states 40..49 -> 10 states x 2 seeds x 10 tasks = 200 episodes total; only successful episodes from this assignment are used to derive operating thresholds

OOD episodes are **not** collected in this campaign.

## Policy / rollout semantics — immutable

- SimVLA only
- native proposal horizon H=10
- execute the **full H10 chunk** subject only to environment early termination/success
- action budget: 300 environment actions per episode
- success: official LIBERO environment task-completion signal
- timeout after exhausting the action budget without success
- eventual_failure_target = 0 for success, 1 for failure/timeout
- no risk-aware intervention during data collection
- no early replan based on risk
- no task ID or timestep may enter the risk-head features

The final/current corrected SimVLA checkpoint, normalization, image preprocessing, environment reset, action postprocessing, success checking, and seed semantics must be taken from the **latest corrected pipeline that supports the final promoted SimVLA paper evidence**. Old/superseded collection scripts must not be used as the implementation base.

Canonical evidence family for source tracing: `fiper_ws/cross_suite_official_ood_20260630` and the final promoted SimVLA training/evaluation artifacts referenced by the report. The source-provenance gate must resolve exact paths and hashes before code adaptation or launch.

## Mimic-style K1 feature contract — immutable

Primary monitor: **Single-Head GRU — Combined without ACE**.

At every SimVLA policy query collect exactly **8 genuine stochastic H10 candidates** from the same observation/instruction/query state.

Candidate tensor after deterministic SimVLA-7D -> Mimic-10D action adaptation:

`action_candidates: float32 [8,10,10]`

10D action convention:

`[translation_delta_xyz (3), rotation_6d (6), gripper (1)]`

The adapter must be mathematically derived from the actual current SimVLA environment action rotation convention and independently parity-tested. Do not guess or pad dimensions.

### Required nine action-candidate disagreement scalars

Derived exactly from the eight candidates:

1. `w2a_action_variance_mean`
2. `w2a_action_variance_max`
3. `w2a_pairwise_mse_mean`
4. `w2a_first_candidate_vs_mean_mse`
5. `w2a_endpoint_position_spread_mean_m`
6. `w2a_endpoint_position_spread_max_m`
7. `w2a_position_variance_mean`
8. `w2a_rotation_variance_mean`
9. `w2a_gripper_variance_mean`

### Required genuine denoising-step metrics

For every SimVLA denoising iteration record exactly:

- `sample_pairwise_mse_mean`
- `sample_variance_max`
- `sample_variance_mean`
- `sample_velocity_mse_mean`
- `vector_field_l2_mean`

Denoising steps must be contiguous `0..D-1`. The expected current SimVLA denoising count is 10 but the collector must record and assert the actual configured value rather than silently assume it.

The monitor later reduces each of the five traces using `first`, `last`, `mean`, `max`, and `last-first`, yielding 25 scalars.

### Required temporal-change fields

At query q:

- `history_available`
- absolute change in mean action variance from query q-1
- absolute change in endpoint positional spread from query q-1

At query 0: history_available=0 and the two change values are zero.

### Required H10 horizon feature channels

For each of the 10 proposal steps:

1. position variance mean
2. position variance max
3. rotation variance mean
4. gripper variance
5. cumulative position spread mean
6. cumulative position spread max

Total neural feature contract: **37 scalars + 10x6 horizon features**.

No ACE. No TopK8. No V2W/K3. No fake proposal-overlap features.

## Candidate execution semantics

Candidate index 0 is the nominal SimVLA proposal used for environment execution.

All eight candidates are genuine samples from the same frozen policy query. Candidate 0 must not be duplicated into the remaining slots.

All candidate seeds must be unique inside one query and stored in the raw record.

## Raw dataset format

Produce a portable dataset root compatible with the supplied handoff:

```
DATA_ROOT/
  queries.jsonl
  arrays/
    <query>.npz
  collection_manifest.json
  episode_summaries.jsonl
  split_manifest.json
  sha256sums.txt
```

Every query JSON row must contain at minimum:

- episode_key
- task_id
- init_state_idx
- rollout_seed
- query_index
- assignment
- eventual_failure_target (backfilled only after episode completion)
- arrays_path
- candidate_seeds[8]
- `w2a_denoising_step_metrics`
- current instruction
- provenance fields for checkpoint/code/normalization

The referenced NPZ must contain `action_candidates float32 [8,10,10]`.

The dataset must not require absolute machine paths for training.

## Training protocol — follow friend head

Use the supplied `simvla_h10_risk_monitor_handoff` implementation as the architecture/training source of truth for the Single-Head GRU unless an adaptation is strictly necessary for loading this dataset.

Training hyperparameters:

- hidden_dim 128
- query_embedding_dim 64
- H10 horizon Transformer: 2 layers, 4 heads
- GRU temporal layers: 1
- dropout 0.10
- batch size 64 episodes
- AdamW
- learning rate 1e-3
- weight decay 1e-4
- gradient clip 1.0
- 25 epochs
- seeds 0,1,2,3,4
- eventual-failure BCE with positive class weight from training episodes
- feature normalizer fit on training only
- checkpoint selection on id_development only

No OOD result may select a checkpoint, feature normalization, threshold or seed.

## Threshold / offline metrics

Thresholds are derived from **successful_calibration successful episodes only**.

At minimum report friend-style conformal alpha 0.05 / 0.10 / 0.15 operating points plus AUROC/AUPRC.

For comparison with the promoted SimVLA paper detector, also materialize success-only empirical q90/q95/q99 episode operating points if possible without altering the trained model.

Report on any evaluation set:

- successful-episode false alarm rate
- failed-episode detection rate
- Det@25
- Det@50
- AUROC
- AUPRC
- episode counts S/F

## OOD evaluation — later, offline only

This fresh 1000-episode campaign is training/development/calibration data only.

The six paper OOD suites are not recollected here. If this head is later evaluated on the exact six frozen paper OOD datasets, the required Mimic-style features must be rematerialized from their frozen query states or otherwise generated without changing their episode identities/outcomes. Do not substitute new OOD episodes.

## Provenance gate

Before writing/adapting collector code, identify the exact latest corrected collection/runtime source behind the final promoted SimVLA paper evidence and record:

- collector/runtime source path + SHA256
- SimVLA checkpoint path + SHA256
- normalization path + SHA256
- LIBERO-PRO repository/path + commit/identity
- action adapter/postprocess source + SHA256
- success-check/reset semantics source + SHA256
- current trainer family used for the final promoted detector, including `run_clean_temporal_nextgen_campaign_v2.py` and/or the exact final promoted training launcher if different

If exact provenance cannot be resolved, STOP. Do not fall back to the archived June collector.

## Validation gates before full 1000

1. static unit tests for 7D->10D rotation/action adapter
2. synthetic feature-contract tests against the supplied handoff extractor
3. 1-query policy test: exactly 8 unique candidates, H10, finite denoising metrics, correct shapes
4. 1 complete episode smoke on one Goal-Object task
5. 10-episode smoke: one episode per task, validate outcome backfill and query contiguity
6. only then launch 1000 episodes

Do not train until the 1000-episode collection completes and the dataset integrity audit passes.
