# Bob Risk Matrix Campaign 2026-06-05

This isolated campaign compares exactly two frozen detector architectures:

- `base`: 43 static inputs, no SimVLA uncertainty features.
- `unc_topk8`: the same temporal architecture plus fixed uncertainty dimensions
  `[6, 21, 25, 27, 23, 2, 26, 24]`, for 51 static inputs total.

The campaign changes dataset, episode split, query cadence, SimVLA checkpoint,
and execution horizon. It does not introduce another detector architecture.

## Compatibility

| SimVLA checkpoint | Baseline | Base detector | Top-8 detector |
|---|---:|---:|---:|
| Original paper checkpoint | yes | yes | no |
| Modified checkpoint 60000 | yes | yes | yes |

Top-8 jobs are rejected at startup when the checkpoint has no uncertainty head.

## Fairness Controls

- The main candidate is sampled alone before ACE alternatives are sampled.
- Baseline, shadow, and active policies share reset and action seed plans.
- Shadow policies score alternatives but execute candidate zero.
- Every production job depends on a matching one-episode smoke job.
- Horizon 1 and horizon 10 use one history token per policy query.
- Horizon 10 history stores the first action actually executed from the chunk.
- Outputs include main and selected chunk hashes for trace comparisons.

## Queue

The queue is resumable from `state/scheduler_state.json`. A failed job is
retried once. A permanently failed dependency blocks only dependent jobs.
Unrelated jobs can continue.

The first jobs cover the exact 200-episode goal-object identity bundle and the
first 100 identities for each policy. Later jobs retrain on native and stride-10
cadences, then run a broad five-suite backlog.
