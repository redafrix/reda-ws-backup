# Bob Risk-Aware Broad Results Report

Checked at: `2026-06-08T09:28:16+0200` on Bob.

Campaign root:

```text
/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/bob_risk_matrix_campaign_20260605
```

## Current Scheduler State

```text
completed: 256
running:   1
pending:   104
failed:    4
blocked:   6
```

Current running job:

```text
broad_libero_10_object_t02_original_risk_base_h10_prod100
```

Blocked/failed items that matter:

- `libero_goal_object` task 9 smoke tests failed for all relevant policies because LIBERO-PRO crashes during reset with `KeyError: wine_rack_stand_1_top_region`.
- `512_package_old_native` failed after packaging because the detector package is incomplete, notably missing the expected `normalization.json`.
- The `libero_10_object` task 2 risk-base broad test is still running, so it is not a final comparison yet.

## How To Read This Report

`Orig` means original SimVLA only.

`RiskBase` means original SimVLA plus the base risk-aware detector. This is the clean comparison for the question: does risk-aware improve original SimVLA?

`TopK8` means modified SimVLA checkpoint plus the uncertainty TopK8 risk-aware detector. This is not a clean comparison against original SimVLA because the base policy checkpoint is different.

`Delta` is `RiskBase - Orig`, measured in number of successful episodes.

All broad task rows below use H10 chunk execution and 100 episodes, unless explicitly marked partial.

## Main Answer

For the clean comparison `Original SimVLA` vs `Original SimVLA + RiskBase`, Bob currently gives:

```text
Completed broad task comparisons: 31
RiskBase better than Orig:        2 tasks
RiskBase equal to Orig:           28 tasks
RiskBase worse than Orig:         1 task
```

The two clean positive tasks are:

| Suite | Task | Orig | RiskBase | Delta |
|---|---:|---:|---:|---:|
| `libero_goal_object` | 3 | 9/100 | 13/100 | +4 |
| `libero_goal_object` | 6 | 47/100 | 50/100 | +3 |

The only clean negative completed task is:

| Suite | Task | Orig | RiskBase | Delta |
|---|---:|---:|---:|---:|
| `libero_goal_object` | 8 | 96/100 | 94/100 | -2 |

So the current evidence is task-local, not global. It shows RiskBase can slightly help on some hard `libero_goal_object` tasks, but it does not prove a broad overall improvement.

## Core Balanced 100-Episode Tests

These are the balanced core tests, not the broad per-task scan.

| Checkpoint | Policy | Horizon | Success | Rate | Mean Steps | Action Mods | Proposed Mods |
|---|---|---:|---:|---:|---:|---:|---:|
| original | SimVLA only | H10 | 76/100 | 76.0% | 135.18 | 0 | 0 |
| original | shadow base | H10 | 76/100 | 76.0% | 135.18 | 0 | 24 |
| original | RiskBase | H10 | 76/100 | 76.0% | 134.68 | 28 | 28 |
| original | SimVLA only | H1 | 75/100 | 75.0% | 149.88 | 0 | 0 |
| original | shadow base | H1 | 75/100 | 75.0% | 150.22 | 0 | 356 |
| original | RiskBase | H1 | 75/100 | 75.0% | 149.96 | 355 | 355 |
| modified | SimVLA only | H10 | 83/100 | 83.0% | 128.64 | 0 | 0 |
| modified | shadow base | H10 | 83/100 | 83.0% | 128.64 | 0 | 29 |
| modified | RiskBase | H10 | 82/100 | 82.0% | 128.67 | 27 | 27 |
| modified | shadow TopK8 | H10 | 83/100 | 83.0% | 128.63 | 0 | 37 |
| modified | RiskTopK8 | H10 | 81/100 | 81.0% | 130.65 | 41 | 41 |
| modified | SimVLA only | H1 | 76/100 | 76.0% | 145.15 | 0 | 0 |
| modified | shadow base | H1 | 75/100 | 75.0% | 145.34 | 0 | 361 |
| modified | RiskBase | H1 | 76/100 | 76.0% | 143.50 | 334 | 334 |
| modified | shadow TopK8 | H1 | 75/100 | 75.0% | 145.35 | 0 | 384 |
| modified | RiskTopK8 | H1 | 74/100 | 74.0% | 145.96 | 369 | 369 |

Core-test interpretation:

- Original H10: RiskBase equals original SimVLA at `76/100`.
- Original H1: RiskBase equals original SimVLA at `75/100`.
- Modified H10: RiskBase and TopK8 are slightly worse than modified SimVLA alone.
- Modified H1: RiskBase equals modified SimVLA, while TopK8 is slightly worse.

## Broad Task Scan: `libero_goal_object`

| Task | Orig | RiskBase | Delta | TopK8 | Notes |
|---:|---:|---:|---:|---:|---|
| 0 | 89/100 | 89/100 | 0 | 81/100 | RiskBase equal |
| 1 | 95/100 | 95/100 | 0 | 96/100 | RiskBase equal |
| 2 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 3 | 9/100 | 13/100 | +4 | 21/100 | clean RiskBase improvement |
| 4 | 91/100 | 91/100 | 0 | 82/100 | RiskBase equal |
| 5 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 6 | 47/100 | 50/100 | +3 | 63/100 | clean RiskBase improvement |
| 7 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 8 | 96/100 | 94/100 | -2 | 93/100 | RiskBase regression |
| 9 | smoke failed | smoke failed | n/a | smoke failed | reset crash: `wine_rack_stand_1_top_region` |

Detailed `libero_goal_object` metrics:

| Task | Policy | Success | Rate | Mean Steps | Action Mods | Proposed Mods | Errors |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | Orig | 89/100 | 89.0% | 151.33 | 0 | 0 | 0 |
| 0 | RiskBase | 89/100 | 89.0% | 151.16 | 17 | 17 | 0 |
| 0 | TopK8 | 81/100 | 81.0% | 170.02 | 68 | 68 | 0 |
| 1 | Orig | 95/100 | 95.0% | 88.50 | 0 | 0 | 0 |
| 1 | RiskBase | 95/100 | 95.0% | 88.50 | 14 | 14 | 0 |
| 1 | TopK8 | 96/100 | 96.0% | 83.70 | 20 | 20 | 0 |
| 2 | Orig | 100/100 | 100.0% | 92.29 | 0 | 0 | 0 |
| 2 | RiskBase | 100/100 | 100.0% | 92.29 | 0 | 0 | 0 |
| 2 | TopK8 | 100/100 | 100.0% | 91.20 | 1 | 1 | 0 |
| 3 | Orig | 9/100 | 9.0% | 288.37 | 0 | 0 | 0 |
| 3 | RiskBase | 13/100 | 13.0% | 286.11 | 152 | 152 | 0 |
| 3 | TopK8 | 21/100 | 21.0% | 276.67 | 145 | 145 | 0 |
| 4 | Orig | 91/100 | 91.0% | 103.62 | 0 | 0 | 0 |
| 4 | RiskBase | 91/100 | 91.0% | 103.16 | 19 | 19 | 0 |
| 4 | TopK8 | 82/100 | 82.0% | 123.93 | 46 | 46 | 0 |
| 5 | Orig | 100/100 | 100.0% | 117.22 | 0 | 0 | 0 |
| 5 | RiskBase | 100/100 | 100.0% | 117.20 | 1 | 1 | 0 |
| 5 | TopK8 | 100/100 | 100.0% | 120.52 | 0 | 0 | 0 |
| 6 | Orig | 47/100 | 47.0% | 217.70 | 0 | 0 | 0 |
| 6 | RiskBase | 50/100 | 50.0% | 213.11 | 101 | 101 | 0 |
| 6 | TopK8 | 63/100 | 63.0% | 191.57 | 110 | 110 | 0 |
| 7 | Orig | 100/100 | 100.0% | 74.69 | 0 | 0 | 0 |
| 7 | RiskBase | 100/100 | 100.0% | 74.68 | 0 | 0 | 0 |
| 7 | TopK8 | 100/100 | 100.0% | 74.30 | 0 | 0 | 0 |
| 8 | Orig | 96/100 | 96.0% | 103.29 | 0 | 0 | 0 |
| 8 | RiskBase | 94/100 | 94.0% | 101.29 | 37 | 37 | 0 |
| 8 | TopK8 | 93/100 | 93.0% | 106.29 | 36 | 36 | 0 |

## Broad Task Scan: `libero_object_object`

| Task | Orig | RiskBase | Delta | TopK8 | Notes |
|---:|---:|---:|---:|---:|---|
| 0 | 3/100 | 3/100 | 0 | 4/100 | very hard, RiskBase equal |
| 1 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 2 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 3 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 4 | 93/100 | 93/100 | 0 | 100/100 | RiskBase equal |
| 5 | 100/100 | 100/100 | 0 | 99/100 | ceiling task |
| 6 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 7 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 8 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 9 | 100/100 | 100/100 | 0 | 99/100 | ceiling task |

Detailed `libero_object_object` metrics:

| Task | Policy | Success | Rate | Mean Steps | Action Mods | Proposed Mods | Errors |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | Orig | 3/100 | 3.0% | 299.26 | 0 | 0 | 0 |
| 0 | RiskBase | 3/100 | 3.0% | 299.29 | 34 | 34 | 0 |
| 0 | TopK8 | 4/100 | 4.0% | 295.89 | 23 | 23 | 0 |
| 1 | Orig | 100/100 | 100.0% | 134.34 | 0 | 0 | 0 |
| 1 | RiskBase | 100/100 | 100.0% | 134.34 | 0 | 0 | 0 |
| 1 | TopK8 | 100/100 | 100.0% | 130.97 | 21 | 21 | 0 |
| 2 | Orig | 100/100 | 100.0% | 116.11 | 0 | 0 | 0 |
| 2 | RiskBase | 100/100 | 100.0% | 116.11 | 0 | 0 | 0 |
| 2 | TopK8 | 100/100 | 100.0% | 113.29 | 2 | 2 | 0 |
| 3 | Orig | 100/100 | 100.0% | 122.29 | 0 | 0 | 0 |
| 3 | RiskBase | 100/100 | 100.0% | 122.29 | 0 | 0 | 0 |
| 3 | TopK8 | 100/100 | 100.0% | 121.09 | 2 | 2 | 0 |
| 4 | Orig | 93/100 | 93.0% | 157.59 | 0 | 0 | 0 |
| 4 | RiskBase | 93/100 | 93.0% | 157.62 | 2 | 2 | 0 |
| 4 | TopK8 | 100/100 | 100.0% | 138.84 | 15 | 15 | 0 |
| 5 | Orig | 100/100 | 100.0% | 118.02 | 0 | 0 | 0 |
| 5 | RiskBase | 100/100 | 100.0% | 118.10 | 2 | 2 | 0 |
| 5 | TopK8 | 99/100 | 99.0% | 120.81 | 4 | 4 | 0 |
| 6 | Orig | 100/100 | 100.0% | 142.03 | 0 | 0 | 0 |
| 6 | RiskBase | 100/100 | 100.0% | 142.03 | 0 | 0 | 0 |
| 6 | TopK8 | 100/100 | 100.0% | 140.25 | 6 | 6 | 0 |
| 7 | Orig | 100/100 | 100.0% | 129.34 | 0 | 0 | 0 |
| 7 | RiskBase | 100/100 | 100.0% | 129.34 | 1 | 1 | 0 |
| 7 | TopK8 | 100/100 | 100.0% | 130.85 | 12 | 12 | 0 |
| 8 | Orig | 100/100 | 100.0% | 149.03 | 0 | 0 | 0 |
| 8 | RiskBase | 100/100 | 100.0% | 149.03 | 1 | 1 | 0 |
| 8 | TopK8 | 100/100 | 100.0% | 151.28 | 21 | 21 | 0 |
| 9 | Orig | 100/100 | 100.0% | 113.82 | 0 | 0 | 0 |
| 9 | RiskBase | 100/100 | 100.0% | 113.82 | 0 | 0 | 0 |
| 9 | TopK8 | 99/100 | 99.0% | 114.35 | 3 | 3 | 0 |

## Broad Task Scan: `libero_spatial_object`

| Task | Orig | RiskBase | Delta | TopK8 | Notes |
|---:|---:|---:|---:|---:|---|
| 0 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 1 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 2 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 3 | 100/100 | 100/100 | 0 | 99/100 | ceiling task |
| 4 | 98/100 | 98/100 | 0 | 100/100 | RiskBase equal |
| 5 | 94/100 | 94/100 | 0 | 96/100 | RiskBase equal |
| 6 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 7 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 8 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 9 | 100/100 | 100/100 | 0 | 99/100 | ceiling task |

Detailed `libero_spatial_object` metrics:

| Task | Policy | Success | Rate | Mean Steps | Action Mods | Proposed Mods | Errors |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | Orig | 100/100 | 100.0% | 74.89 | 0 | 0 | 0 |
| 0 | RiskBase | 100/100 | 100.0% | 74.89 | 0 | 0 | 0 |
| 0 | TopK8 | 100/100 | 100.0% | 73.51 | 0 | 0 | 0 |
| 1 | Orig | 100/100 | 100.0% | 109.92 | 0 | 0 | 0 |
| 1 | RiskBase | 100/100 | 100.0% | 109.91 | 0 | 0 | 0 |
| 1 | TopK8 | 100/100 | 100.0% | 111.30 | 5 | 5 | 0 |
| 2 | Orig | 100/100 | 100.0% | 97.20 | 0 | 0 | 0 |
| 2 | RiskBase | 100/100 | 100.0% | 97.20 | 0 | 0 | 0 |
| 2 | TopK8 | 100/100 | 100.0% | 94.29 | 0 | 0 | 0 |
| 3 | Orig | 100/100 | 100.0% | 85.80 | 0 | 0 | 0 |
| 3 | RiskBase | 100/100 | 100.0% | 85.80 | 0 | 0 | 0 |
| 3 | TopK8 | 99/100 | 99.0% | 85.59 | 4 | 4 | 0 |
| 4 | Orig | 98/100 | 98.0% | 132.97 | 0 | 0 | 0 |
| 4 | RiskBase | 98/100 | 98.0% | 132.95 | 16 | 16 | 0 |
| 4 | TopK8 | 100/100 | 100.0% | 127.53 | 0 | 0 | 0 |
| 5 | Orig | 94/100 | 94.0% | 110.05 | 0 | 0 | 0 |
| 5 | RiskBase | 94/100 | 94.0% | 110.08 | 6 | 6 | 0 |
| 5 | TopK8 | 96/100 | 96.0% | 102.71 | 8 | 8 | 0 |
| 6 | Orig | 100/100 | 100.0% | 106.70 | 0 | 0 | 0 |
| 6 | RiskBase | 100/100 | 100.0% | 106.76 | 6 | 6 | 0 |
| 6 | TopK8 | 100/100 | 100.0% | 102.27 | 0 | 0 | 0 |
| 7 | Orig | 100/100 | 100.0% | 128.66 | 0 | 0 | 0 |
| 7 | RiskBase | 100/100 | 100.0% | 128.65 | 0 | 0 | 0 |
| 7 | TopK8 | 100/100 | 100.0% | 130.62 | 1 | 1 | 0 |
| 8 | Orig | 100/100 | 100.0% | 92.67 | 0 | 0 | 0 |
| 8 | RiskBase | 100/100 | 100.0% | 92.68 | 1 | 1 | 0 |
| 8 | TopK8 | 100/100 | 100.0% | 89.29 | 1 | 1 | 0 |
| 9 | Orig | 100/100 | 100.0% | 115.71 | 0 | 0 | 0 |
| 9 | RiskBase | 100/100 | 100.0% | 115.73 | 1 | 1 | 0 |
| 9 | TopK8 | 99/100 | 99.0% | 116.32 | 6 | 6 | 0 |

## Broad Task Scan: `libero_10_object`

| Task | Orig | RiskBase | Delta | TopK8 | Notes |
|---:|---:|---:|---:|---:|---|
| 0 | 0/100 | 0/100 | 0 | 0/100 | completely failed for all tested policies |
| 1 | 100/100 | 100/100 | 0 | 100/100 | ceiling task |
| 2 | 71/100 | 42/58 partial | not final | pending | RiskBase is currently running |

Detailed `libero_10_object` metrics:

| Task | Policy | Success | Rate | Mean Steps | Action Mods | Proposed Mods | Errors |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | Orig | 0/100 | 0.0% | 300.00 | 0 | 0 | 0 |
| 0 | RiskBase | 0/100 | 0.0% | 300.00 | 89 | 89 | 0 |
| 0 | TopK8 | 0/100 | 0.0% | 300.00 | 68 | 68 | 0 |
| 1 | Orig | 100/100 | 100.0% | 245.07 | 0 | 0 | 0 |
| 1 | RiskBase | 100/100 | 100.0% | 245.07 | 0 | 0 | 0 |
| 1 | TopK8 | 100/100 | 100.0% | 241.79 | 6 | 6 | 0 |
| 2 | Orig | 71/100 | 71.0% | 270.94 | 0 | 0 | 0 |
| 2 | RiskBase | 42/58 | 72.4% | 270.07 | 18 | 18 | 0 |

## Current Interpretation

The broad scan does show some evidence that the base risk-aware policy can help original SimVLA on selected hard tasks. The strongest clean examples are:

- `libero_goal_object` task 3: `9/100` to `13/100`.
- `libero_goal_object` task 6: `47/100` to `50/100`.

However, the full picture is weak:

- Most completed tasks are unchanged.
- Many tasks are ceiling tasks where improvement is impossible.
- One completed task regresses: `libero_goal_object` task 8, `96/100` to `94/100`.
- The balanced core test does not improve at all.

Therefore the honest statement is:

```text
Bob currently supports a narrow claim:
RiskBase can slightly improve original SimVLA on some hard goal-object tasks.

Bob does not currently support a broad claim:
RiskBase is globally better than original SimVLA.
```

## Best Follow-Up If We Want A Clean Positive Claim

The best next test is to focus on the already positive tasks:

```text
libero_goal_object task 3
libero_goal_object task 6
```

Run paired same-seed experiments with only:

```text
Original SimVLA
Original SimVLA + RiskBase
```

Use more seeds than 100 if possible, and report:

- total success rate,
- paired recovered failures,
- paired regressions,
- net improvement,
- action modification locations,
- whether improvements happen on baseline-failure episodes.

That is the cleanest way to prove a small but real risk-aware benefit if it exists.
