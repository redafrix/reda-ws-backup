# Stage 9 FIPER Workspace

This workspace is the intended home for the LIBERO-PRO / SimVLA FIPER monitor
work:

- RND: success-only action-normality monitor.
- ACE: action entropy from unexecuted candidate chunks.
- FIPER: combined RND + ACE quadrant monitor.

## Canonical Layout

```text
fiper_ws/
  configs/                 Current campaign and split configuration.
  collection/              Collector and launch scripts copied from asynchvla_ws/stage9_v2_tools.
  data/                    Frozen JSONL/log snapshots and manifests.
  experiments/             Previous and future train/eval outputs.
  external/                External FIPER reference repo, when present.
  reports/                 Current and previous reports.
  scripts/                 Current train/eval/audit entry points.
  stage9_fiper_bridge/     Legacy bridge/scaffold code.
  stage9_v2_tools/         Legacy Stage 9 training/eval utilities.
```

## Current Dataset State

Collection was stopped on both machines on 2026-05-26 after user instruction.
Final stopped row counts:

- Sam: 319,730 rows.
- Bob: 316,191 rows.
- Combined: 635,921 rows.

The active collectors wrote the raw JSONLs outside `fiper_ws` under each
machine's `asynchvla_ws/stage9_libero_pro_risk_data/campaigns` tree. For model
work, use frozen snapshots under `fiper_ws/data/frozen`, not growing live files.

## Current Pipeline Entry Point

Use:

```bash
python3 scripts/analyze_current_fiper_sweep.py \
  --config configs/current_fiper_sweep_eternal.json \
  --output-dir experiments/current_fiper_sweep_analysis_YYYYMMDD_HHMMSS
```

That command audits the dataset and writes manifests only. To train/evaluate:

```bash
python3 scripts/analyze_current_fiper_sweep.py \
  --config configs/current_fiper_sweep_eternal.json \
  --output-dir experiments/current_fiper_sweep_analysis_YYYYMMDD_HHMMSS \
  --run-train-eval
```

Do not train RND on failure/timeout rows. They are eval/challenge only.

## Known Exclusions

The user explicitly said to ignore:

- `libero_10_with_milk`, task 3.
- `libero_10_with_milk`, task 4.

The current config encodes those exclusions.

