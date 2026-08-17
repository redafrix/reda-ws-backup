# H10 Live Correctness Audit

Audit time: 2026-08-14 00:06-00:10 CEST.

## Verdict

The active Round-0 collector is producing true H10-execution rows. The current
committed data passed an exhaustive immutable-episode snapshot audit. The
future pipeline is fail-closed and serial, but its future training/evaluation
results cannot be certified until those stages actually complete.

## Live State

- Service: `simvla-isaac-risk-h10-pipeline.service`, active and enabled.
- Collector PID at audit: `1777611`.
- Output: `outputs/final_seen_h10_round_000_seed20260730`.
- Execution mode: `chunk_h10`.
- Snapshot: 186 committed episodes, 179 successes, seven genuine timeouts.
- Rows audited: 3,592.
- GPU snapshot: 93% utilization, 17,787 MiB used, 60 C, 347 W.
- SSD free space: approximately 310 GiB.
- Traceback/fatal/CUDA/OOM scan: none found.

Every observed timeout had exactly:

```text
simulation_steps=2400
control_ticks=600
decision_rows=60
```

## Exhaustive Snapshot Parity

All committed episode directories present at snapshot start were treated as
immutable and audited independently. Results:

```text
max_ace_abs_difference=0.0
max_candidate0_trace_abs_difference=0.0
max_candidate_seed_difference=0
max_executed_action_abs_difference=0.0
max_feature49_abs_difference=0.0
max_feature_delta_abs_difference=0.0
max_history_abs_difference=0.0
```

Every nonterminal row executed exactly ten actions matching the complete main
chunk. A successful terminal row executed only the exact remaining prefix.
Rows per episode equal `ceil(control_ticks / 10)`.

## H10 Semantics

The SimVLA eval config has `num_actions: 10` and `replan_steps: 10`. The run
manifest records:

```text
main chunk [10,7]
eight alternatives [8,10,7]
one policy query per H10 execution chunk
maximum 60 policy queries per timeout
```

The promoted LIBERO TopK8 trainer and its native chunk-10 online code were
checked directly. They define one 21D history token per policy query using:

```text
proprio at query time: 8
first action actually executed from the selected H10 chunk: 7
first six ACE values: 6
```

This matches the current Isaac H10 run manifest and row implementation.

The future Isaac temporal risk head is a new checkpoint trained on Isaac rows.
"Same model" means the same promoted `SeqRiskModel` architecture and training
recipe; it does not mean loading or reusing the LIBERO-trained risk-head weights.

## Pipeline Isolation

All collector launchers for Round 0, generated seen rounds, hard-1000, and
locked OOD-150 explicitly pass `--execution-mode chunk_h10`. Runtime source in
`scripts`, `src`, `automation`, and `risk_head_pipeline` has no H1 execution
reference. H1 data/models/evaluations remain under the separate H1 archive and
are not enumerated by H10 builders.

## Orchestration Correction

During this audit, a future-stage race was removed: the primary supervisor no
longer enters open-ended broad collection after its first H10 train/evaluation
cycle. It now explicitly hands off to the hard-1000 orchestrator and exits.
The already-running process is additionally protected by the active systemd
path handoff and a fail-closed external round-stage guard. Even if the stale
process wins the scheduling race, any post-cycle broad round exits before a
collector is launched.

Persistence:

```text
simvla-isaac-risk-h10-pipeline.service: active/enabled
simvla-h10-hard1000-handoff.path: active/enabled
simvla-h10-hard1000-watchdog.timer: active/enabled
```

Post-correction tests: `38 passed, 2 expected skips`. The skips require the
future H10 Round-0-derived hard manifest and cannot run yet.

## Scope of Certainty

```text
ACTIVE_H10_COLLECTION_CONTRACT=PASS
CURRENT_COMMITTED_ROWS_PARITY=PASS
H10_HISTORY_SEMANTICS_MATCH_PROMOTED_REFERENCE=PASS
H1_RUNTIME_PATH_PRESENT=NO
GPU_STAGE_OVERLAP_ALLOWED=NO
AUTOMATIC_HANDOFF_CONFIGURED=YES
FUTURE_RESULTS_ALREADY_CERTIFIED=NO
```

Future stages must still produce their completion markers and pass exhaustive
audits. Any failed gate stops the chain rather than accepting or silently
relabeling data.
