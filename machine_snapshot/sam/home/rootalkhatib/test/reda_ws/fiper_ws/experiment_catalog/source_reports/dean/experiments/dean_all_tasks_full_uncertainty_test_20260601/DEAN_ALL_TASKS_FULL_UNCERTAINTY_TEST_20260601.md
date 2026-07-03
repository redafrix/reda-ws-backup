# Dean All-Tasks Full Uncertainty Test (2026-06-01)

## Question

If we train on all available tasks/suites from Dean, does the risk detector work?

## Dataset Usage

This run uses all valid Dean episodes across the experiment. There are no artificial caps like 260/180 episodes.

Valid Dean episodes:

- Total: `4191`
- Successes: `3405`
- Failures/timeouts: `786`

Split support:

| Bucket | Episodes | Rows |
|---|---:|---:|
| success_train_seen | 1872 | 248352 |
| failure_train_seen | 432 | 129600 |
| success_val_seen | 510 | 67470 |
| failure_val_seen | 117 | 35100 |
| success_calib_seen | 510 | 66197 |
| success_test_seen | 513 | 68376 |
| failure_test_seen | 237 | 71100 |

Total rows used: `686195`.

## Results

| Variant | Test Success FA | Test Failure Detection | Det@25 | Det@50 | Mean Detection Time | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|
| base | 14.2% | 95.8% | 54.0% | 89.0% | 0.231 | 8 |
| unc_raw | 16.8% | 97.5% | 67.1% | 87.8% | 0.207 | 4 |

Thresholds:

| Variant | q95 | q99 | Conformal Mass |
|---|---:|---:|---:|
| base | 0.9224 | 0.9997 | 0.1500 |
| unc_raw | 0.8469 | 0.9958 | 0.1984 |

## Verdict

Yes, when training uses all tasks/suites with all available Dean episodes, the model works.

The earlier balanced run made `base` look broken because the balanced calibration produced an extremely high q95 and the conformal mass policy became too conservative. In this full-data test, `base` is not broken:

- `base`: 95.8% failure detection with 14.2% false alarms.
- `unc_raw`: improves detection and early detection, but increases false alarms.

The uncertainty features help most on detection and earliness:

- Detection improves from 95.8% to 97.5%.
- Det@25 improves from 54.0% to 67.1%.
- Mean detection time improves from 0.231 to 0.207.

But false alarms get worse:

- FA increases from 14.2% to 16.8%.

Current best answer for this specific all-tasks-full question:

- Use `base` if false alarm rate matters most.
- Use `unc_raw` if detection and early warning matter more.

