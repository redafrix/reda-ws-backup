# H1 to H10 Execution Migration and Launch

Date: 2026-08-13 (Europe/Paris)

## Decision

The previous dataset predicted H10 action chunks but executed only action zero
before replanning. Its execution contract was `receding_h1`; it is not H10
execution data and will not be mixed with the replacement dataset.

The replacement pipeline uses `chunk_h10`: it predicts one `[10,7]` main chunk
and eight `[10,7]` alternatives, executes the full main H10 chunk, then replans.
A terminal success may stop the final chunk early. This is the only permitted
short chunk.

## H1 Preservation

- Archive: `/mnt/ai/projects/simvla_isaac_risk_collection_H1_EXECUTION_ARCHIVE_20260813`
- Compatibility symlink: `/mnt/ai/projects/simvla_isaac_risk_collection_20260730`
- Archive size at launch: approximately 24 GiB.
- The interrupted hard-enrichment run stopped after an atomic commit at 33
  episodes; its last source episode was `1773`.
- H1 collectors are stopped.
- The three historical H1 pipeline units are disabled.
- H1 outputs, normalization, risk-head checkpoints, calibration thresholds,
  evaluations and videos remain historical evidence only.

## H10 Workspace

- Root: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`
- Config: `configs/final_seen_h10_round_000_seed20260730.yaml`
- Collector: `scripts/collect_isaac_risk.py`
- Auditor: `scripts/audit_corrected_collection.py`
- Output: `outputs/final_seen_h10_round_000_seed20260730`
- Service: `simvla-isaac-risk-h10-pipeline.service`
- Unit: `/home/redafrix/.config/systemd/user/simvla-isaac-risk-h10-pipeline.service`
- Tmux: `simvla-risk-h10-final-seen-r000`
- Log: `logs/final_seen_h10_round_000_stage.log`
- Live status: `outputs/final_seen_h10_round_000_seed20260730/live_status.json`

The H10 workspace was created from source/configuration files only. It did not
copy H1 outputs, models, frozen datasets, evaluations, logs or smoke data.

## Runtime Contract

| Field | H10 value |
|---|---:|
| Execution mode | `chunk_h10` |
| Main chunk | `[10,7]` |
| ACE alternatives | `[8,10,7]` |
| Actions applied per normal replan | 10 |
| Maximum simulator steps | 2400 |
| Maximum control ticks | 600 |
| Maximum decision rows | 60 |
| Physics/control frequency | 120/30 Hz |
| Success criterion | 0.02 m for 0.2 s |
| ACE metric | `new_training` |
| Uncertainty features | 49 |
| History | `[16,21]` |

The schema rejects `receding_h1`. Auditors require every nonterminal chunk and
every timeout chunk to contain exactly ten executed actions. A terminal success
row must contain the exact contiguous prefix of the predicted main chunk.

## Verification

Initial CPU tests: `36 passed, 2 skipped`. After installing the complete
Round-0 -> train/eval -> hard-1000 -> combined train/eval handoff, the suite
passed `37 passed, 2 skipped`. The two skips are H10 hard-enrichment tests
whose manifest can only be created later from completed H10 outcomes.

Candidate parity smoke:

- main `[10,7]`;
- alternatives `[8,10,7]`;
- nine distinct seeds;
- candidate-zero maximum difference `0.0`;
- uncertainty `[49]`.

Real success smoke, source `000001`:

- outcome `success`;
- 835 simulator steps, 209 control ticks, 21 decision rows;
- 20 complete H10 chunks plus a terminal nine-action prefix;
- ACE, feature-49, delta, history and executed-prefix maximum errors: `0.0`.

Forced-timeout smoke, source `000006`:

- `synthetic_smoke=true`, `training_eligible=false`;
- outcome `failure_or_timeout`;
- exactly 2400 simulator steps, 600 control ticks and 60 decision rows;
- every executed sequence `[10,7]`;
- exhaustive audit and aggregate reconstruction passed;
- ACE, feature-49, delta, history and executed-prefix maximum errors: `0.0`.

Atomic resume smoke preserved committed rows byte-for-byte. SHA-256 remained:
`f3f63e44e251243e226f914f719c3f18a223b0724de688864f665aec88ab637f`.

## Production Launch Health

Health report: `reports/FINAL_SEEN_H10_ROUND_000_LAUNCH_HEALTH.json`

At the launch health check:

- service active;
- collector PID `1777611`;
- execution mode `chunk_h10`;
- checkpoint SHA-256
  `68b3e8dc73b0e0ee19e9b7e8d12d2d6ab24a341e824722ffeaebd1091ea2ebcd`;
- three episodes committed and the fourth active;
- no traceback;
- GPU process detected;
- health gate `pass=true`.

Direct inspection of committed episode `r000_s003109` showed 162 control ticks
in 17 decision rows: sixteen exact H10 sequences and a final two-action prefix
ending on successful dwell. Every executed value exactly matched the
corresponding prefix of the predicted main H10 chunk (`max difference 0.0`).

## Hashes

- Collector: `a53fb3c3da9ea6a066ebff1cb791bcfe5bbb530cc645e3b1c6b9eea5fd6edb9b`
- Auditor: `369a9e3bfc3719c19538d51b8f72307e5e346151c52f8eeac7c09de64e79001b`
- Parity auditor: `9d6bddc6632bb25aaeb36c55992a10029d542c1b2f9c03f93e60ca3e2e740a8e`
- Row schema: `81dac9e54ff40c0bbd44f653c17ab42f4c54d2ca6d67e3f0ebb32ab53918b9a0`
- Round-0 config: `f30b025ae2013e432895c8a3cb5e8cea3a89f4623fee82bb11b98f1d52c5e768`
- Selected manifest: `d704db4ec37610a2231541abecf817f5b094ceabdf1c47ef791a01c7058211a2`
- Source manifest: `32261a82df8e015b13931afaf3b9f8de2f59b30980fc5e57833166fad0a3ffd6`

## Final Status

```text
H1_COLLECTION_STOPPED=YES
H1_WORKSPACE_ARCHIVED=YES
H1_DATA_REUSED_FOR_H10=NO
H1_SERVICES_DISABLED=YES
H10_ISOLATED_WORKSPACE=YES
H10_SCHEMA_REJECTS_H1=YES
H10_MAIN_CHUNK_SHAPE=[10,7]
H10_ALTERNATIVE_CHUNKS_SHAPE=[8,10,7]
H10_FULL_CHUNK_EXECUTION=PASS
CANDIDATE0_EXACT_PARITY=PASS
ACE_NEW_TRAINING_PARITY=PASS
FEATURE49_PARITY=PASS
HISTORY_16X21_PARITY=PASS
H10_SUCCESS_PATH=PASS
H10_TIMEOUT_PATH=PASS
H10_ATOMIC_RESUME=PASS
H10_CPU_TESTS=37_PASS_2_EXPECTED_SKIP
H10_PRODUCTION_SERVICE_ACTIVE=YES
H10_PRODUCTION_HEALTH=PASS
```
