# Stage 8 Status Check

Generated: `2026-05-15T16:09:00+02:00`

Scope: status check only. No new jobs were launched by this check.

## 1. Job States

| job | machine | state | notes |
|---|---|---:|---|
| `smoke_bob_cpu` | bob | DONE | manager smoke |
| `smoke_sam_cpu` | sam | DONE | manager smoke |
| `smoke_dependency_child` | bob | DONE | dependency-chain smoke |
| `smoke_retry_failure` | bob | DONE | retry smoke completed on attempt 2 |
| `libero_pro_pilot_bob` | bob | DONE | completed at `2026-05-15T16:00:59+02:00` |
| `stage8_sam_model_sweep` | sam | DONE | completed at `2026-05-15T15:39:23+02:00` |
| `stage8_sam_calibration_sweep` | sam | DONE | completed at `2026-05-15T15:39:35+02:00` |
| `normal_libero_hard_baseline_bob` | bob | RUNNING | scheduler started it at `2026-05-15T16:01:01+02:00` before this status-only request |
| `flowtrace_medium_bob` | bob | PENDING | waiting for Bob GPU availability/dependencies |

## 2. LIBERO-PRO Pilot Status

`libero_pro_pilot_bob` is no longer running. It finished successfully from the manager perspective and wrote:

- `asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_pilot_results.md`
- `asynchvla_ws/stage8_ultimate/results/libero_pro_pilot/libero_object_with_mug_task0.json`
- `asynchvla_ws/stage8_ultimate/results/libero_pro_pilot/libero_object_with_mug_task1.json`
- `asynchvla_ws/stage8_ultimate/results/libero_pro_pilot/libero_object_with_mug_task2.json`

Important limitation: only `libero_object_with_mug` tasks produced result JSON files. The attempted `libero_object_env` tasks failed because required `.pruned_init` files were missing under the LIBERO-PRO `init_files/libero_object_env/` path.

## 3. Sam Model Sweep Status

`stage8_sam_model_sweep` finished. The Sam log shows training/evaluation completed for:

- `holdout_libero_object`
- `holdout_object_bowl`
- `holdout_libero_spatial`

Variants included:

- `action_only_baseline`
- `full_old_baseline`
- `context_gated_action`
- `seed_relative_pairwise`
- `per_step_error_head`
- `full_engineered_simvla_focused`

Reports on Sam:

- `asynchvla_ws/stage8_ultimate/reports/stage8_holdout_libero_object_model_sweep.md/json`
- `asynchvla_ws/stage8_ultimate/reports/stage8_holdout_object_bowl_model_sweep.md/json`
- `asynchvla_ws/stage8_ultimate/reports/stage8_holdout_libero_spatial_model_sweep.md/json`

## 4. Calibration Sweep Status

`stage8_sam_calibration_sweep` did start and finished. Reports exist on Sam and previous Bob-side calibration reports exist under:

- `asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md/json`
- `asynchvla_ws/stage8_ultimate/reports/stage8_calibration_best_method.md`
- `asynchvla_ws/stage8_ultimate/reports/stage8_calibration_by_domain.md`
- `asynchvla_ws/stage8_ultimate/reports/stage8_calibration_threshold_transfer.md`

## 5. Errors / Warnings In Logs

### Real errors

The LIBERO-PRO pilot log contains repeated `FileNotFoundError` failures for `libero_object_env` init-state files, for example:

```text
FileNotFoundError: ... init_files/libero_object_env/pick_up_the_alphabet_soup_and_place_it_in_the_basket.pruned_init
FileNotFoundError: ... init_files/libero_object_env/pick_up_the_cream_cheese_and_place_it_in_the_basket.pruned_init
FileNotFoundError: ... init_files/libero_object_env/pick_up_the_salad_dressing_and_place_it_in_the_basket.pruned_init
```

These failures were caught by the pilot script and logged as warnings, so the job exited `0`, but they mean that the LIBERO-PRO pilot coverage is currently incomplete.

### Non-fatal warnings

- `TRANSFORMERS_CACHE` deprecation warning.
- robosuite private macro warning.
- PyTorch `torch.load(weights_only=False)` future warning.
- Normal LIBERO hard-task log reports a missing datasets path warning, but the environment still reset and began running.

## 6. Current Best Result Available

Current best deployment-relevant result is from the completed LIBERO-PRO `libero_object_with_mug` pilot, but it is still a small pilot and not enough for final claims.

Aggregate pilot result from `stage8_libero_pro_pilot_results.md`:

| suite | task | mode | episodes | success_rate | avg_steps | avg_unc |
|---|---:|---|---:|---:|---:|---:|
| `libero_object_with_mug` | 0 | `A_passive` | 5 | 1.000 | 148.60 | 1.350 |
| `libero_object_with_mug` | 0 | `B_deliberation` | 5 | 1.000 | 203.20 | 1.298 |
| `libero_object_with_mug` | 0 | `E_conservative_switch_proxy` | 5 | 1.000 | 150.20 | 1.362 |
| `libero_object_with_mug` | 1 | `A_passive` | 5 | 1.000 | 145.20 | 1.284 |
| `libero_object_with_mug` | 1 | `B_deliberation` | 5 | 1.000 | 135.20 | 1.365 |
| `libero_object_with_mug` | 1 | `E_conservative_switch_proxy` | 5 | 1.000 | 155.60 | 1.278 |
| `libero_object_with_mug` | 2 | `A_passive` | 5 | 1.000 | 149.20 | 1.401 |
| `libero_object_with_mug` | 2 | `B_deliberation` | 5 | 1.000 | 190.60 | 1.339 |
| `libero_object_with_mug` | 2 | `E_conservative_switch_proxy` | 5 | 1.000 | 149.40 | 1.389 |

Interpretation at this checkpoint:

- Seed0/passive is already strong on the completed LIBERO-PRO `with_mug` tasks.
- Deliberation lowers predicted uncertainty in some cases but often increases steps, so it is not clearly better as an action selector yet.
- Conservative switch proxy roughly matches seed0 on these easy completed tasks.
- Random seed mode failed one episode each on tasks 1 and 2, suggesting seed choice can matter.
- The more important next evidence is the currently running normal LIBERO hard baseline and fixing/selecting LIBERO-PRO perturbation suites with valid init states.

## 7. Files Checked

Commands requested were run on Bob:

```bash
bash asynchvla_ws/scripts/stage8_status.sh
tail -80 asynchvla_ws/stage8_ultimate/logs/libero_pro_pilot_bob.log || true
tail -80 asynchvla_ws/stage8_ultimate/logs/stage8_sam_model_sweep.log || true
cat asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md || true
find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f -printf "%T@ %p\n" | sort -n | tail -20
```

Additional read-only checks were used to inspect the Sam-side model-sweep log and the completed LIBERO-PRO pilot summary.
