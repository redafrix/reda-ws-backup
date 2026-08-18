# Dean Official-FIPER Materialization Status - 2026-06-22

## Verdict

The stricter official-FIPER reproduction attempt on Dean did **not** finish correctly and must not be used as a completed ablation result.

## Host And Root

- Host: Dean (`dean`)
- Root: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622`
- External official repo clone: `/home/dean/fiper_uncertainty_collection/external/fiper`
- Main materializer: `/home/dean/fiper_uncertainty_collection/scripts/materialize_official_fiper_fold00_obs_embeddings_20260622.py`
- Orchestrator: `/home/dean/fiper_uncertainty_collection/scripts/run_official_fiper_rndoe_entropy_fold00_20260622.py`

## What Ran

The run attempted to reconstruct official-format FIPER rollout tensors by rendering saved MuJoCo states, extracting 960D SimVLA/SmolVLM observation embeddings, and writing official-style `processed_rollouts` tensors for the official RND/OE + entropy pipeline.

The unsharded materialization crashed with EGL/OpenGL cleanup errors. A later sharded materialization also failed validation.

## Evidence

The waiter log says:

```text
[waiter] waiting for sharded materialization validation: /home/dean/fiper_uncertainty_collection/logs/official_fiper_sharded_20260622/validate.log
[waiter] materialization tmux is gone and validation has not passed
```

The materialization logs end in EGL/OpenGL errors such as:

```text
OpenGL.raw.EGL._errors.EGLError: EGLError(
  err = EGL_NOT_INITIALIZED,
  baseOperation = eglMakeCurrent,
)
```

## Partial Artifacts

Partial official-format tensors exist but are incomplete:

| Artifact | Shape / count |
|---|---:|
| `official_fiper_data/libero_fold00/processed_rollouts/obs_embeddings.pt` | `(1225, 960)` |
| `official_fiper_data/libero_fold00/processed_rollouts/action_preds.pt` | `(1225, 9, 10, 7)` |
| `official_fiper_data/libero_fold00_hygiene/processed_rollouts/obs_embeddings.pt` | `(1225, 960)` |
| `official_fiper_data/libero_fold00_hygiene/processed_rollouts/action_preds.pt` | `(1225, 9, 10, 7)` |
| `materialized_shards/shard_batches_0000_0004.pt` | partial shard |
| `materialized_shards/shard_batches_0005_0009.pt` | partial shard |
| `materialized_shards/shard_batches_0010_0014.pt` | partial shard |

These artifacts are not enough to claim the official-FIPER ablation finished.

## Relationship To Previous Dean Result

This failed run is separate from the completed 2026-06-19 Dean clean offline comparison:

`/home/dean/fiper_uncertainty_collection/experiments/clean_offline_original_fiper_vs_v2018_fold00_20260619`

That earlier result is a clean reimplementation-style comparison, not the fully official materialized-code path.

## Status Flags

- `OFFICIAL_FIPER_MATERIALIZATION_COMPLETE = NO`
- `OFFICIAL_FIPER_VALIDATION_PASS = NO`
- `OFFICIAL_FIPER_FINAL_EVAL_PASS = NO`
- `SAFE_TO_COMPARE_AS_COMPLETED_OFFICIAL_ABLATION = NO`
- `PARTIAL_TENSORS_EXIST = YES`
- `BLOCKER = EGL/OpenGL context cleanup/resource failure during MuJoCo rendering`

