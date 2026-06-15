# FIPER NextGen V2 Implementation, Smoke, and Full Launch Report

Date: 2026-05-27

## Executive Summary

Implemented and launched a corrected NextGen v2 campaign on Bob (`pcrobot`) for Stage 9 / LIBERO-PRO / FIPER.

The previous v1 issues were fixed:

- Dynamics residual no longer uses future `t+1` proprio. It uses only the online-legal past/current delta: `proprio_t - proprio_t_minus_1`.
- GroupDRO/adversarial jobs now use ref metadata as training labels only, not raw-row missing fields and not model inputs.
- Hard-stop metrics are emitted only for jobs with a real residual gate.
- Feature audit is now dynamic and records actual input fields, group counts, and future-feature status.
- Forced runs clear stale job folders and stale `failed_jobs.jsonl`.

## Implemented Ideas

Total configured ideas: **44**.

Families:

- TCN history windows: k1, k2, k4, k6, k8, k12, k16, k24, k32.
- LSTM history windows: k4, k8, k16, k24.
- GRU history windows: k8, k16.
- Transformer variants: small k8, medium k8, k16, focal k8.
- Input ablations: no current proprio, no current ACE, no ACE history, action-token-only, history-only, first-action static, flat-action static, seqstats static.
- Capacity/dropout variants: wide TCN, low-dropout TCN, high-dropout TCN.
- Loss variants: focal, positive class weighting, label smoothing.
- Multi-horizon survival heads: TCN k8, LSTM k8, TCN k16, focal TCN k8.
- Robustness variants: GroupDRO and adversarial training using ref-combined metadata groups.
- Dynamics variants: past-delta residual TCN and past-delta residual survival TCN.

## Legality / No-Cheating Constraints

Forbidden as model inputs:

- object positions
- reward
- success flag
- task id
- suite id
- language instruction
- episode outcome
- future timestep features

Allowed:

- current SimVLA action chunk
- ACE candidate chunk metrics
- current proprio
- previous executed action history
- previous proprio history
- previous ACE history
- ref metadata only as a training group label for GroupDRO/adversarial losses

## Smoke Validation

Smoke command:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
scripts/run_nextgen_v2_smoke_all_splits.sh
```

Smoke output:

```text
experiments/clean_temporal_nextgen_v2_smoke_all_20260527
```

Validation result:

```text
Status: PASS
Expected splits: 15
Expected jobs per split: 44
Summary files: 660
Feature audit files: 660
Failures: 0
```

Validation report:

```text
experiments/clean_temporal_nextgen_v2_smoke_all_20260527/NEXTGEN_V2_VALIDATION_REPORT.md
experiments/clean_temporal_nextgen_v2_smoke_all_20260527/NEXTGEN_V2_VALIDATION_REPORT.json
```

## Full Campaign Launch

Full campaign is launched detached on Bob.

Driver PID:

```text
1253188
```

Current first training process at launch audit:

```text
1253196
```

Command launched:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
nohup bash scripts/run_nextgen_v2_full_all_splits.sh \
  > logs/nextgen_v2_full_all_20260527/driver.log 2>&1 &
```

Full output root:

```text
experiments/clean_temporal_nextgen_v2_full_all_20260527
```

Full log:

```text
logs/nextgen_v2_full_all_20260527/driver.log
```

The full run is using:

```text
max_epochs = 120
patience = 18
batch_size = 384
splits = 15
jobs_per_split = 44
total_jobs = 660
```

At the last audit, the full run had loaded full fold_00 data and was actively training `v2_001_tcn_k1_baseline`, reaching epoch 18 with improving/early-stopping tracked validation metrics.

## Files Added / Updated

```text
configs/clean_temporal_nextgen_campaign_v2.json
scripts/run_clean_temporal_nextgen_campaign_v1.py
scripts/run_clean_temporal_nextgen_campaign_v2.py
scripts/run_nextgen_v2_smoke_all_splits.sh
scripts/run_nextgen_v2_full_all_splits.sh
scripts/validate_nextgen_v2_campaign.py
reports/FIPER_NEXTGEN_V2_IMPLEMENTATION_SMOKE_AND_FULL_LAUNCH_REPORT_20260527.md
```

## Current Decision Fields

```text
NEXTGEN_V2_IDEAS_CONFIGURED = 44
NEXTGEN_V2_SMOKE_ALL_SPLITS_PASS = YES
NEXTGEN_V2_FORBIDDEN_FEATURE_AUDIT_PASS = YES
NEXTGEN_V2_GROUP_METHODS_FIXED = YES
NEXTGEN_V2_DYNAMICS_FUTURE_CHEAT_FIXED = YES
NEXTGEN_V2_FULL_CAMPAIGN_LAUNCHED_ON_BOB = YES
NEXTGEN_V2_FULL_CAMPAIGN_FINISHED = NO
```

## How To Check Progress

```bash
ssh pcrobot "pgrep -af 'run_nextgen_v2_full_all_splits|run_clean_temporal_nextgen_campaign_v2'"
ssh pcrobot "cd '/media/rootalkhatib/My Passport/reda_ws/fiper_ws' && tail -n 100 logs/nextgen_v2_full_all_20260527/driver.log"
ssh pcrobot "cd '/media/rootalkhatib/My Passport/reda_ws/fiper_ws' && find experiments/clean_temporal_nextgen_v2_full_all_20260527 -path '*/summary.json' | wc -l"
```
