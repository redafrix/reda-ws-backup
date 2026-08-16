# SimVLA Isaac H10 Risk Collection

This workspace is the isolated, resumable **H10-execution** pipeline for the
verified SimVLA `softplus_110k` checkpoint.

For every policy replan it predicts:

- one main action chunk with shape `[10, 7]`;
- eight independently seeded alternative chunks with shape `[8, 10, 7]`.

It then executes the complete ten-action main chunk before replanning. Only a
terminal success may shorten the final chunk. Runtime rows therefore use:

```text
execution_mode = chunk_h10
replan_steps = 10
```

The historical H1-execution workspace and all data derived from it are archived
at:

```text
/mnt/ai/projects/simvla_isaac_risk_collection_H1_EXECUTION_ARCHIVE_20260813
```

H1 data, normalization, temporal-risk checkpoints, thresholds, evaluations and
videos are not inputs to this H10 pipeline.

## Production

Round 0 output:

```text
/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_000_seed20260730
```

Persistent service and tmux session:

```text
simvla-isaac-risk-h10-pipeline.service
simvla-risk-h10-final-seen-r000
```

The service cannot start unless `reports/H10_PREPRODUCTION_GATES_PASS.json`
exists. Each finalized episode is committed atomically under `episodes/`.

## Fixed Scientific Contract

```text
maximum simulator steps: 2400
physics frequency:       120 Hz
control frequency:       30 Hz
maximum control ticks:   600
maximum decision rows:   60
success threshold:       0.02 m held for 0.2 s
ACE style:               new_training
uncertainty features:    49
history:                 [16, 21]
```

The candidate, ACE, feature-49, history, camera and checkpoint semantics are
unchanged from the audited implementation. Only execution changed from H1 to
true chunk H10.

## Tests

```bash
ROOT=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
PY=/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python
PYTHONPATH="$ROOT/src" "$PY" -m pytest -q "$ROOT/tests"
```
