# ASYNCVLA SimVLA Stage 8 Ultimate Experiment Report

Generated: `2026-05-17T00:34:03`

## Executive Summary

This final report is generated from the currently available Stage 8 reports. If the 72-hour queue is still running, treat this as an interim report.

## Queue Status

```json
[
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:09:43+02:00",
    "job_id": "smoke_bob_cpu",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "614539",
    "state": "DONE",
    "updated_at": "2026-05-15T15:09:43+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:09:44+02:00",
    "job_id": "smoke_sam_cpu",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2122302",
    "state": "DONE",
    "updated_at": "2026-05-15T15:09:44+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:09:51+02:00",
    "job_id": "smoke_dependency_child",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "614763",
    "state": "DONE",
    "updated_at": "2026-05-15T15:09:51+02:00"
  },
  {
    "attempt": 2,
    "completed_at": "2026-05-15T15:10:18+02:00",
    "job_id": "smoke_retry_failure",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "615217",
    "state": "DONE",
    "updated_at": "2026-05-15T15:10:18+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:00:59+02:00",
    "job_id": "libero_pro_pilot_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "629034",
    "state": "DONE",
    "updated_at": "2026-05-15T16:00:59+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:39:23+02:00",
    "job_id": "stage8_sam_model_sweep",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2132768",
    "state": "DONE",
    "updated_at": "2026-05-15T15:39:23+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:39:35+02:00",
    "job_id": "stage8_sam_calibration_sweep",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2142583",
    "state": "DONE",
    "updated_at": "2026-05-15T15:39:35+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T21:37:12+02:00",
    "job_id": "stage8_sam_flowtrace_real",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2422750",
    "state": "DONE",
    "updated_at": "2026-05-15T21:37:12+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T22:58:07+02:00",
    "job_id": "stage8_sam_target_real",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2423059",
    "state": "DONE",
    "updated_at": "2026-05-15T22:58:07+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-16T00:49:45+02:00",
    "job_id": "stage8_sam_arch_big",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2485517",
    "state": "DONE",
    "updated_at": "2026-05-16T00:49:45+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:14:44+02:00",
    "job_id": "flowtrace_experiments_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2164506",
    "state": "DONE",
    "updated_at": "2026-05-15T16:14:44+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-16T01:00:00+02:00",
    "job_id": "stage8_sam_calibration_real",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2552618",
    "state": "DONE",
    "updated_at": "2026-05-16T01:00:00+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-16T01:00:08+02:00",
    "job_id": "stage8_sam_history_real",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2560420",
    "state": "DONE",
    "updated_at": "2026-05-16T01:00:08+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:14:55+02:00",
    "job_id": "target_sweep_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2164866",
    "state": "DONE",
    "updated_at": "2026-05-15T16:14:55+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:49:59+02:00",
    "job_id": "architecture_loss_sweep_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2167999",
    "state": "DONE",
    "updated_at": "2026-05-15T16:49:59+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T19:41:31+02:00",
    "job_id": "normal_libero_hard_baseline_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "649690",
    "state": "DONE",
    "updated_at": "2026-05-15T19:41:31+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T22:58:09+02:00",
    "job_id": "libero_pro_expanded_rollout_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "776740",
    "state": "DONE",
    "updated_at": "2026-05-15T22:58:09+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T23:08:24+02:00",
    "job_id": "flowtrace_medium_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "890020",
    "state": "DONE",
    "updated_at": "2026-05-15T23:08:24+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:50:11+02:00",
    "job_id": "calibration_mega_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2203428",
    "state": "DONE",
    "updated_at": "2026-05-15T16:50:11+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-16T07:23:52+02:00",
    "job_id": "normal_libero_hard_30eps_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "895341",
    "state": "DONE",
    "updated_at": "2026-05-16T07:23:52+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-17T00:33:56+02:00",
    "job_id": "libero_pro_expanded_30eps_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "1156081",
    "state": "DONE",
    "updated_at": "2026-05-17T00:33:56+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:15:03+02:00",
    "job_id": "history_models_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2168517",
    "state": "DONE",
    "updated_at": "2026-05-15T16:15:03+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-16T07:24:01+02:00",
    "job_id": "switch_policy_analysis_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "1156129",
    "state": "DONE",
    "updated_at": "2026-05-16T07:24:01+02:00"
  },
  {
    "attempt": 1,
    "command_file": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/jobs/stage8_libero_pro_20eps_bob.sh",
    "job_id": "stage8_libero_pro_20eps_bob",
    "log_path": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_libero_pro_20eps_bob.log",
    "machine": "bob",
    "pid": "1705181",
    "started_at": "2026-05-17T00:33:59+02:00",
    "state": "RUNNING",
    "updated_at": "2026-05-17T00:33:59+02:00"
  },
  {
    "job_id": "stage8_libero_pro_50eps_backup_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "job_id": "stage8_normal_libero_50eps_backup_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "job_id": "stage8_switch_policy_extended_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "attempt": 1,
    "command_file": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/jobs/stage8_final_report_bob.sh",
    "job_id": "stage8_final_report_bob",
    "log_path": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_final_report_bob.log",
    "machine": "bob",
    "pid": "1705283",
    "started_at": "2026-05-17T00:34:00+02:00",
    "state": "RUNNING",
    "updated_at": "2026-05-17T00:34:00+02:00"
  }
]
```

## LIBERO-PRO Results

# Stage 8 LIBERO-PRO Expanded Rollout Results (30 episodes/task)

- Input dir: `asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_30eps`
- Files: `20`
- Episodes: `2400`

## Aggregate By Suite/Task/Mode

| suite | task | mode | episodes | success_rate | avg_steps | avg_unc | max_unc | avg_rejects | reward_sum |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| libero_10_with_mug | 0 | A_passive | 30 | 0.967 | 259.10 | 1.243 | 2.393 | 7.77 | 29.000 |
| libero_10_with_mug | 0 | B_deliberation | 30 | 1.000 | 248.73 | 1.236 | 2.599 | 7.53 | 30.000 |
| libero_10_with_mug | 0 | C_random_seed | 30 | 0.933 | 277.10 | 1.229 | 2.387 | 7.43 | 28.000 |
| libero_10_with_mug | 0 | D_low_uncertainty_reject_log | 30 | 0.967 | 259.10 | 1.243 | 2.393 | 7.77 | 29.000 |
| libero_10_with_mug | 1 | A_passive | 30 | 0.900 | 281.53 | 1.366 | 2.811 | 9.00 | 27.000 |
| libero_10_with_mug | 1 | B_deliberation | 30 | 0.933 | 279.80 | 1.363 | 2.116 | 8.07 | 28.000 |
| libero_10_with_mug | 1 | C_random_seed | 30 | 0.933 | 273.70 | 1.379 | 2.775 | 8.17 | 28.000 |
| libero_10_with_mug | 1 | D_low_uncertainty_reject_log | 30 | 0.900 | 281.53 | 1.366 | 2.811 | 9.00 | 27.000 |
| libero_10_with_mug | 2 | A_passive | 30 | 0.833 | 296.43 | 1.571 | 4.008 | 18.07 | 25.000 |
| libero_10_with_mug | 2 | B_deliberation | 30 | 0.967 | 255.93 | 1.671 | 4.147 | 19.30 | 29.000 |
| libero_10_with_mug | 2 | C_random_seed | 30 | 1.000 | 233.97 | 1.646 | 3.910 | 16.43 | 30.000 |
| libero_10_with_mug | 2 | D_low_uncertainty_reject_log | 30 | 0.833 | 296.43 | 1.571 | 4.008 | 18.07 | 25.000 |
| libero_10_with_mug | 3 | A_passive | 30 | 0.933 | 280.60 | 1.720 | 4.156 | 25.60 | 28.000 |
| libero_10_with_mug | 3 | B_deliberation | 30 | 0.933 | 264.07 | 1.725 | 4.222 | 20.03 | 28.000 |
| libero_10_with_mug | 3 | C_random_seed | 30 | 0.933 | 295.67 | 1.737 | 4.316 | 27.13 | 28.000 |
| libero_10_with_mug | 3 | D_low_uncertainty_reject_log | 30 | 0.933 | 280.60 | 1.720 | 4.156 | 25.60 | 28.000 |
| libero_10_with_mug | 4 | A_passive | 30 | 1.000 | 226.27 | 1.120 | 2.407 | 1.23 | 30.000 |
| libero_10_with_mug | 4 | B_deliberation | 30 | 0.933 | 253.80 | 1.107 | 2.527 | 1.77 | 28.000 |
| libero_10_with_mug | 4 | C_random_seed | 30 | 0.967 | 248.23 | 1.101 | 2.803 | 1.70 | 29.000 |
| libero_10_with_mug | 4 | D_low_uncertainty_reject_log | 30 | 1.000 | 226.27 | 1.120 | 2.407 | 1.23 | 30.000 |
| libero_goal_with_mug | 0 | A_passive | 30 | 0.867 | 226.33 | 2.157 | 3.250 | 22.13 | 26.000 |
| libero_goal_with_mug | 0 | B_deliberation | 30 | 0.867 | 233.10 | 2.137 | 3.361 | 17.63 | 26.000 |
| libero_goal_with_mug | 0 | C_random_seed | 30 | 0.933 | 216.23 | 2.125 | 3.297 | 21.03 | 28.000 |
| libero_goal_with_mug | 0 | D_low_uncertainty_reject_log | 30 | 0.867 | 226.33 | 2.157 | 3.250 | 22.13 | 26.000 |
| libero_goal_with_mug | 1 | A_passive | 30 | 0.967 | 99.03 | 1.547 | 3.587 | 5.47 | 29.000 |
| libero_goal_with_mug | 1 | B_deliberation | 30 | 0.967 | 101.30 | 1.539 | 3.081 | 4.77 | 29.000 |
| libero_goal_with_mug | 1 | C_random_seed | 30 | 1.000 | 83.23 | 1.554 | 2.108 | 4.63 | 30.000 |
| libero_goal_with_mug | 1 | D_low_uncertainty_reject_log | 30 | 0.967 | 99.03 | 1.547 | 3.587 | 5.47 | 29.000 |
| libero_goal_with_mug | 2 | A_passive | 30 | 0.833 | 173.73 | 2.114 | 4.368 | 16.53 | 25.000 |
| libero_goal_with_mug | 2 | B_deliberation | 30 | 0.933 | 139.20 | 2.241 | 4.275 | 16.27 | 28.000 |
| libero_goal_with_mug | 2 | C_random_seed | 30 | 0.933 | 132.43 | 2.199 | 4.334 | 13.83 | 28.000 |
| libero_goal_with_mug | 2 | D_low_uncertainty_reject_log | 30 | 0.833 | 173.73 | 2.114 | 4.368 | 16.53 | 25.000 |
| libero_goal_with_mug | 3 | A_passive | 30 | 0.867 | 232.57 | 1.576 | 3.219 | 12.73 | 26.000 |
| libero_goal_with_mug | 3 | B_deliberation | 30 | 0.967 | 194.73 | 1.620 | 3.301 | 15.10 | 29.000 |
| libero_goal_with_mug | 3 | C_random_seed | 30 | 0.900 | 220.83 | 1.599 | 3.403 | 13.93 | 27.000 |
| libero_goal_with_mug | 3 | D_low_uncertainty_reject_log | 30 | 0.867 | 232.57 | 1.576 | 3.219 | 12.73 | 26.000 |
| libero_goal_with_mug | 4 | A_passive | 30 | 1.000 | 84.10 | 1.616 | 3.031 | 6.77 | 30.000 |
| libero_goal_with_mug | 4 | B_deliberation | 30 | 1.000 | 86.23 | 1.648 | 2.395 | 6.87 | 30.000 |
| libero_goal_with_mug | 4 | C_random_seed | 30 | 1.000 | 84.53 | 1.637 | 2.422 | 6.73 | 30.000 |
| libero_goal_with_mug | 4 | D_low_uncertainty_reject_log | 30 | 1.000 | 84.10 | 1.616 | 3.031 | 6.77 | 30.000 |
| libero_object_with_mug | 0 | A_passive | 30 | 1.000 | 142.37 | 1.372 | 2.224 | 2.70 | 30.000 |
| libero_object_with_mug | 0 | B_deliberation | 30 | 1.000 | 155.20 | 1.378 | 2.564 | 3.77 | 30.000 |
| libero_object_with_mug | 0 | C_random_seed | 30 | 1.000 | 144.60 | 1.397 | 2.568 | 3.67 | 30.000 |
| libero_object_with_mug | 0 | D_low_uncertainty_reject_log | 30 | 1.000 | 142.37 | 1.372 | 2.224 | 2.70 | 30.000 |
| libero_object_with_mug | 1 | A_passive | 30 | 1.000 | 136.23 | 1.315 | 2.226 | 3.40 | 30.000 |
| libero_object_with_mug | 1 | B_deliberation | 30 | 1.000 | 132.57 | 1.369 | 2.330 | 3.93 | 30.000 |
| libero_object_with_mug | 1 | C_random_seed | 30 | 0.967 | 154.67 | 1.326 | 2.198 | 3.80 | 29.000 |
| libero_object_with_mug | 1 | D_low_uncertainty_reject_log | 30 | 1.000 | 136.23 | 1.315 | 2.226 | 3.40 | 30.000 |
| libero_object_with_mug | 2 | A_passive | 30 | 0.967 | 183.87 | 1.351 | 2.079 | 3.97 | 29.000 |
| libero_object_with_mug | 2 | B_deliberation | 30 | 0.933 | 229.73 | 1.304 | 2.445 | 4.40 | 28.000 |
| libero_object_with_mug | 2 | C_random_seed | 30 | 0.900 | 223.00 | 1.313 | 2.084 | 4.53 | 27.000 |
| libero_object_with_mug | 2 | D_low_uncertainty_reject_log | 30 | 0.967 | 183.87 | 1.351 | 2.079 | 3.97 | 29.000 |
| libero_object_with_mug | 3 | A_passive | 30 | 1.000 | 146.90 | 1.417 | 2.330 | 4.63 | 30.000 |
| libero_object_with_mug | 3 | B_deliberation | 30 | 1.000 | 160.13 | 1.386 | 2.385 | 4.77 | 30.000 |
| libero_object_with_mug | 3 | C_random_seed | 30 | 0.967 | 167.13 | 1.397 | 2.452 | 4.73 | 29.000 |
| libero_object_with_mug | 3 | D_low_uncertainty_reject_log | 30 | 1.000 | 146.90 | 1.417 | 2.330 | 4.63 | 30.000 |
| libero_object_with_mug | 4 | A_passive | 30 | 1.000 | 135.83 | 1.285 | 1.992 | 1.23 | 30.000 |
| libero_object_with_mug | 4 | B_deliberation | 30 | 1.000 | 128.70 | 1.341 | 2.314 | 1.87 | 30.000 |
| libero_object_with_mug | 4 | C_random_seed | 30 | 1.000 | 129.80 | 1.331 | 2.307 | 1.80 | 30.000 |
| libero_object_with_mug | 4 | D_low_uncertainty_reject_log | 30 | 1.000 | 135.83 | 1.285 | 1.992 | 1.23 | 30.000 |
| libero_spatial_with_mug | 0 | A_passive | 30 | 0.833 | 178.97 | 1.768 | 3.188 | 13.40 | 25.000 |
| libero_spatial_with_mug | 0 | B_deliberation | 30 | 0.800 | 186.37 | 1.781 | 3.087 | 14.13 | 24.000 |
| libero_spatial_with_mug | 0 | C_random_seed | 30 | 0.867 | 167.30 | 1.808 | 3.195 | 15.23 | 26.000 |
| libero_spatial_with_mug | 0 | D_low_uncertainty_reject_log | 30 | 0.833 | 179.00 | 1.768 | 3.188 | 13.43 | 25.000 |
| libero_spatial_with_mug | 1 | A_passive | 30 | 1.000 | 106.70 | 1.785 | 2.863 | 9.57 | 30.000 |
| libero_spatial_with_mug | 1 | B_deliberation | 30 | 0.967 | 126.37 | 1.765 | 2.924 | 10.10 | 29.000 |
| libero_spatial_with_mug | 1 | C_random_seed | 30 | 1.000 | 111.23 | 1.775 | 2.753 | 9.87 | 30.000 |
| libero_spatial_with_mug | 1 | D_low_uncertainty_reject_log | 30 | 1.000 | 106.70 | 1.785 | 2.863 | 9.57 | 30.000 |
| libero_spatial_with_mug | 2 | A_passive | 30 | 0.933 | 129.07 | 1.566 | 2.848 | 8.47 | 28.000 |
| libero_spatial_with_mug | 2 | B_deliberation | 30 | 0.967 | 114.80 | 1.544 | 2.701 | 7.47 | 29.000 |
| libero_spatial_with_mug | 2 | C_random_seed | 30 | 0.967 | 113.83 | 1.571 | 2.699 | 8.30 | 29.000 |
| libero_spatial_with_mug | 2 | D_low_uncertainty_reject_log | 30 | 0.933 | 129.07 | 1.566 | 2.848 | 8.47 | 28.000 |
| libero_spatial_with_mug | 3 | A_passive | 30 | 1.000 | 86.73 | 1.810 | 3.021 | 10.50 | 30.000 |
| libero_spatial_with_mug | 3 | B_deliberation | 30 | 0.967 | 103.97 | 1.776 | 2.787 | 10.40 | 29.000 |
| libero_spatial_with_mug | 3 | C_random_seed | 30 | 1.000 | 89.57 | 1.793 | 2.966 | 10.87 | 30.000 |
| libero_spatial_with_mug | 3 | D_low_uncertainty_reject_log | 30 | 1.000 | 86.73 | 1.810 | 3.021 | 10.50 | 30.000 |
| libero_spatial_with_mug | 4 | A_passive | 30 | 1.000 | 135.17 | 1.815 | 2.635 | 15.27 | 30.000 |
| libero_spatial_with_mug | 4 | B_deliberation | 30 | 1.000 | 127.87 | 1.796 | 2.785 | 14.77 | 30.000 |
| libero_spatial_with_mug | 4 | C_random_seed | 30 | 1.000 | 125.37 | 1.807 | 2.737 | 14.97 | 30.000 |
| libero_spatial_with_mug | 4 | D_low_uncertainty_reject_log | 30 | 1.000 | 135.17 | 1.815 | 2.635 | 15.27 | 30.000 |

## Episode Rows

| file | suite | task | mode | success | steps | unc_mean | unc_max | rejects |
|---|---|---:|---|---:|---:|---:|---:|---:|
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 235 | 1.3228194041455046 | 2.3278584480285645 | 9 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 254 | 1.2559007666150077 | 1.936976671218872 | 8 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 302 | 1.1537152142071527 | 1.8988014459609985 | 8 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 246 | 1.1647795793172475 | 1.8617807626724243 | 3 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 241 | 1.2151056684296706 | 2.0774405002593994 | 7 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 236 | 1.1808953108921858 | 2.030364751815796 | 5 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 254 | 1.249215229612882 | 1.968496561050415 | 6 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 249 | 1.3516032446586965 | 2.0774641036987305 | 10 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 249 | 1.278774432514025 | 2.1351699829101562 | 7 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 275 | 1.1374222148548474 | 1.9177813529968262 | 6 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 238 | 1.3418219131189626 | 2.3926916122436523 | 13 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 237 | 1.248235179248609 | 2.1843605041503906 | 6 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 233 | 1.26634431630373 | 2.070075511932373 | 8 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 0 | 600 | 1.170671996474266 | 2.258634328842163 | 10 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 244 | 1.2675080486531958 | 1.9597324132919312 | 8 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 248 | 1.2885995975276767 | 2.0646474361419678 | 9 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 235 | 1.23446845754664 | 1.9387849569320679 | 8 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 257 | 1.2806770292300622 | 1.9499542713165283 | 12 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 239 | 1.1841825518873925 | 1.9601194858551025 | 5 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 247 | 1.1475941629120798 | 2.113678455352783 | 4 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 248 | 1.2502534231483535 | 2.002563953399658 | 7 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 235 | 1.3850341667520238 | 2.1544744968414307 | 14 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 256 | 1.3150145496640886 | 2.144198417663574 | 12 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 240 | 1.1939479168504477 | 2.0094892978668213 | 6 |
| `libero_10_with_mug_task0.json` | libero_10_with_mug | 0 | A_passive | 1 | 246 | 1.200125832614061 | 1.963302731513977 | 4 |
| `libero_10_with_mug_task0.json

# Stage 8 LIBERO-PRO Pilot Results

- Input dir: `asynchvla_ws/stage8_ultimate/results/libero_pro_pilot`
- Files: `3`
- Episodes: `75`

## Aggregate By Suite/Task/Mode

| suite | task | mode | episodes | success_rate | avg_steps | avg_unc | max_unc | avg_rejects | reward_sum |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| libero_object_with_mug | 0 | A_passive | 5 | 1.000 | 148.60 | 1.350 | 2.028 | 3.40 | 5.000 |
| libero_object_with_mug | 0 | B_deliberation | 5 | 1.000 | 203.20 | 1.298 | 2.094 | 3.60 | 5.000 |
| libero_object_with_mug | 0 | C_random_seed | 5 | 1.000 | 151.00 | 1.387 | 2.140 | 4.60 | 5.000 |
| libero_object_with_mug | 0 | D_low_uncertainty_reject_log | 5 | 1.000 | 148.60 | 1.350 | 2.028 | 3.40 | 5.000 |
| libero_object_with_mug | 0 | E_conservative_switch_proxy | 5 | 1.000 | 150.20 | 1.362 | 2.090 | 3.80 | 5.000 |
| libero_object_with_mug | 1 | A_passive | 5 | 1.000 | 145.20 | 1.284 | 2.020 | 3.60 | 5.000 |
| libero_object_with_mug | 1 | B_deliberation | 5 | 1.000 | 135.20 | 1.365 | 2.092 | 3.60 | 5.000 |
| libero_object_with_mug | 1 | C_random_seed | 5 | 0.800 | 225.60 | 1.264 | 2.036 | 3.80 | 4.000 |
| libero_object_with_mug | 1 | D_low_uncertainty_reject_log | 5 | 1.000 | 145.20 | 1.284 | 2.020 | 3.60 | 5.000 |
| libero_object_with_mug | 1 | E_conservative_switch_proxy | 5 | 1.000 | 155.60 | 1.278 | 2.069 | 4.20 | 5.000 |
| libero_object_with_mug | 2 | A_passive | 5 | 1.000 | 149.20 | 1.401 | 2.067 | 4.20 | 5.000 |
| libero_object_with_mug | 2 | B_deliberation | 5 | 1.000 | 190.60 | 1.339 | 2.239 | 5.00 | 5.000 |
| libero_object_with_mug | 2 | C_random_seed | 5 | 0.800 | 263.00 | 1.297 | 2.084 | 5.80 | 4.000 |
| libero_object_with_mug | 2 | D_low_uncertainty_reject_log | 5 | 1.000 | 149.20 | 1.401 | 2.067 | 4.20 | 5.000 |
| libero_object_with_mug | 2 | E_conservative_switch_proxy | 5 | 1.000 | 149.40 | 1.389 | 2.085 | 4.80 | 5.000 |

## Episode Rows

| file | suite | task | mode | success | steps | unc_mean | unc_max | rejects |
|---|---|---:|---|---:|---:|---:|---:|---:|
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | A_passive | 1 | 141 | 1.3458920955657958 | 1.7838618755340576 | 1 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | A_passive | 1 | 180 | 1.2703235513634152 | 1.81827712059021 | 4 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | A_passive | 1 | 146 | 1.3341690146110274 | 1.802276849746704 | 2 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | A_passive | 1 | 142 | 1.3694110690501697 | 1.9007728099822998 | 4 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | A_passive | 1 | 134 | 1.4300726222695772 | 2.027705430984497 | 6 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | B_deliberation | 1 | 161 | 1.3287728201482714 | 2.0546746253967285 | 2 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | B_deliberation | 1 | 186 | 1.284450682678393 | 1.7887241840362549 | 2 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | B_deliberation | 1 | 155 | 1.3916436664519771 | 2.0310986042022705 | 3 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | B_deliberation | 1 | 376 | 1.0535867082334198 | 2.0944840908050537 | 6 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | B_deliberation | 1 | 138 | 1.4295030789202954 | 1.9205390214920044 | 5 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | C_random_seed | 1 | 143 | 1.3959131268567817 | 2.029696464538574 | 4 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | C_random_seed | 1 | 159 | 1.3464636503089784 | 2.015604019165039 | 4 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | C_random_seed | 1 | 143 | 1.4154958822006403 | 1.9498521089553833 | 4 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | C_random_seed | 1 | 176 | 1.370895801850085 | 2.140467882156372 | 5 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | C_random_seed | 1 | 134 | 1.4051845362467796 | 2.0660111904144287 | 6 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | D_low_uncertainty_reject_log | 1 | 141 | 1.3458920955657958 | 1.7838618755340576 | 1 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | D_low_uncertainty_reject_log | 1 | 180 | 1.2703235513634152 | 1.81827712059021 | 4 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | D_low_uncertainty_reject_log | 1 | 146 | 1.3341690146110274 | 1.802276849746704 | 2 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | D_low_uncertainty_reject_log | 1 | 142 | 1.3694110690501697 | 1.9007728099822998 | 4 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | D_low_uncertainty_reject_log | 1 | 134 | 1.4300726222695772 | 2.027705430984497 | 6 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | E_conservative_switch_proxy | 1 | 161 | 1.3081620685833018 | 2.0897247791290283 | 2 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | E_conservative_switch_proxy | 1 | 169 | 1.303075778366897 | 1.810227870941162 | 5 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | E_conservative_switch_proxy | 1 | 145 | 1.3500118461148491 | 1.7780816555023193 | 2 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | E_conservative_switch_proxy | 1 | 143 | 1.4296640788399897 | 1.9552630186080933 | 5 |
| `libero_object_with_mug_task0.json` | libero_object_with_mug | 0 | E_conservative_switch_proxy | 1 | 133 | 1.41758606210351 | 1.9282153844833374 | 5 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | A_passive | 1 | 126 | 1.2882959576029527 | 1.9312241077423096 | 4 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | A_passive | 1 | 132 | 1.2876116194815006 | 1.8901830911636353 | 2 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | A_passive | 1 | 158 | 1.2373448371887208 | 2.019604206085205 | 4 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | A_passive | 1 | 131 | 1.3913249803494803 | 1.9367212057113647 | 3 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | A_passive | 1 | 179 | 1.2156025731286337 | 1.947263240814209 | 5 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | B_deliberation | 1 | 128 | 1.345960848517232 | 1.92464017868042 | 3 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | B_deliberation | 1 | 132 | 1.3266541058162473 | 1.909196376800537 | 2 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | B_deliberation | 1 | 134 | 1.339732121236576 | 1.9623247385025024 | 3 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | B_deliberation | 1 | 147 | 1.4291511188119144 | 2.0918333530426025 | 6 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | B_deliberation | 1 | 135 | 1.3810570173793368 | 1.9458632469177246 | 4 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | C_random_seed | 1 | 125 | 1.311650607585907 | 1.931654691696167 | 2 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | C_random_seed | 1 | 127 | 1.356157566986832 | 1.9784493446350098 | 3 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | C_random_seed | 1 | 136 | 1.3387448264331352 | 2.0358493328094482 | 4 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | C_random_seed | 1 | 140 | 1.3670675158500671 | 1.9537049531936646 | 5 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | C_random_seed | 0 | 600 | 0.9459040939807892 | 1.9424411058425903 | 5 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | D_low_uncertainty_reject_log | 1 | 126 | 1.2882959576029527 | 1.9312241077423096 | 4 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | D_low_uncertainty_reject_log | 1 | 132 | 1.2876116194815006 | 1.8901830911636353 | 2 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | D_low_uncertainty_reject_log | 1 | 158 | 1.2373448371887208 | 2.019604206085205 | 4 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | D_low_uncertainty_reject_log | 1 | 131 | 1.3913249803494803 | 1.9367212057113647 | 3 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | D_low_uncertainty_reject_log | 1 | 179 | 1.2156025731286337 | 1.947263240814209 | 5 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | E_conservative_switch_proxy | 1 | 125 | 1.2919130969047545 | 1.9290498495101929 | 3 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | E_conservative_switch_proxy | 1 | 132 | 1.3169576087087955 | 1.8901830911636353 | 2 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | E_conservative_switch_proxy | 1 | 155 | 1.2436558027421274 | 1.9962306022644043 | 4 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | E_conservative_switch_proxy | 1 | 202 | 1.2883138803788174 | 1.9467430114746094 | 7 |
| `libero_object_with_mug_task1.json` | libero_object_with_mug | 1 | E_conservative_switch_proxy | 1 | 164 | 1.251464390815212 | 2.0685248374938965 | 5 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | A_passive | 1 | 144 | 1.387283532605695 | 1.93386971950531 | 4 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | A_passive | 1 | 138 | 1.4387796406286308 | 2.0667848587036133 | 3 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | A_passive | 1 | 168 | 1.3376535608036684 | 1.9748769998550415 | 5 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | A_passive | 1 | 141 | 1.4503673371146708 | 2.0135416984558105 | 6 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | A_passive | 1 | 155 | 1.391089948915666 | 1.8743575811386108 | 3 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | B_deliberation | 1 | 279 | 1.1972749706524521 | 1.9185658693313599 | 6 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | B_deliberation | 1 | 184 | 1.3503033143902257 | 2.092149019241333 | 5 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | B_deliberation | 1 | 144 | 1.4310789390795493 | 1.9654778242111206 | 5 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | B_deliberation | 1 | 142 | 1.434514185838532 | 2.238616466522217 | 6 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | B_deliberation | 1 | 204 | 1.2814120798694844 | 1.8768784999847412 | 3 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | C_random_seed | 1 | 274 | 1.1961292347284798 | 1.9517346620559692 | 6 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | C_random_seed | 0 | 600 | 1.0211523269613585 | 2.084132671356201 | 7 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | C_random_seed | 1 | 144 | 1.4303391896231326 | 2.01426100730896 | 4 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | C_random_seed | 1 | 140 | 1.4549077259642738 | 1.9888503551483154 | 6 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | C_random_seed | 1 | 157 | 1.3825223729723977 | 1.891080617904663 | 6 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | D_low_uncertainty_reject_log | 1 | 144 | 1.387283532605695 | 1.93386971950531 | 4 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | D_low_uncertainty_reject_log | 1 | 138 | 1.4387796406286308 | 2.0667848587036133 | 3 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | D_low_uncertainty_reject_log | 1 | 168 | 1.3376535608036684 | 1.9748769998550415 | 5 |
| `libero_object_with_mug_task2.json` | libero_object_with_mug | 2 | D_low_uncertainty_reject_log | 1 | 141 | 1.4503673371146708 | 2.

## Normal LIBERO Hard-Task Baseline

# Stage 8 Normal LIBERO Hard-Task Results (30 episodes/task)

- Input dir: `asynchvla_ws/stage8_ultimate/results/normal_libero_hard_30eps`
- Files: `7`
- Episodes: `840`

## Aggregate By Suite/Task/Mode

| suite | task | mode | episodes | success_rate | avg_steps | avg_unc | max_unc | avg_rejects | reward_sum |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| libero_10 | 0 | A_passive | 30 | 1.000 | 245.87 | 1.257 | 2.355 | 7.97 | 30.000 |
| libero_10 | 0 | B_deliberation | 30 | 0.967 | 261.27 | 1.250 | 2.561 | 8.80 | 29.000 |
| libero_10 | 0 | C_random_seed | 30 | 1.000 | 248.40 | 1.257 | 2.615 | 8.50 | 30.000 |
| libero_10 | 0 | D_low_uncertainty_reject_log | 30 | 1.000 | 245.87 | 1.257 | 2.355 | 7.97 | 30.000 |
| libero_10 | 1 | A_passive | 30 | 1.000 | 238.47 | 1.423 | 2.312 | 9.20 | 30.000 |
| libero_10 | 1 | B_deliberation | 30 | 0.967 | 267.60 | 1.380 | 2.387 | 8.83 | 29.000 |
| libero_10 | 1 | C_random_seed | 30 | 1.000 | 243.53 | 1.400 | 2.298 | 8.40 | 30.000 |
| libero_10 | 1 | D_low_uncertainty_reject_log | 30 | 1.000 | 238.47 | 1.423 | 2.312 | 9.20 | 30.000 |
| libero_goal | 0 | A_passive | 30 | 0.900 | 214.50 | 2.175 | 3.407 | 21.83 | 27.000 |
| libero_goal | 0 | B_deliberation | 30 | 0.800 | 257.83 | 2.116 | 3.307 | 20.20 | 24.000 |
| libero_goal | 0 | C_random_seed | 30 | 0.867 | 226.60 | 2.128 | 3.277 | 20.97 | 26.000 |
| libero_goal | 0 | D_low_uncertainty_reject_log | 30 | 0.900 | 214.50 | 2.175 | 3.407 | 21.83 | 27.000 |
| libero_goal | 2 | A_passive | 30 | 0.900 | 136.97 | 2.180 | 4.342 | 15.20 | 27.000 |
| libero_goal | 2 | B_deliberation | 30 | 0.967 | 112.20 | 2.284 | 4.436 | 14.80 | 29.000 |
| libero_goal | 2 | C_random_seed | 30 | 0.933 | 129.27 | 2.225 | 4.330 | 14.90 | 28.000 |
| libero_goal | 2 | D_low_uncertainty_reject_log | 30 | 0.900 | 136.97 | 2.180 | 4.342 | 15.23 | 27.000 |
| libero_goal | 9 | A_passive | 30 | 0.900 | 175.23 | 2.674 | 5.546 | 20.80 | 27.000 |
| libero_goal | 9 | B_deliberation | 30 | 0.867 | 225.37 | 2.530 | 5.551 | 23.30 | 26.000 |
| libero_goal | 9 | C_random_seed | 30 | 0.967 | 160.07 | 2.731 | 5.693 | 21.00 | 29.000 |
| libero_goal | 9 | D_low_uncertainty_reject_log | 30 | 0.900 | 175.23 | 2.674 | 5.546 | 20.80 | 27.000 |
| libero_object | 0 | A_passive | 30 | 1.000 | 142.77 | 1.376 | 2.518 | 3.03 | 30.000 |
| libero_object | 0 | B_deliberation | 30 | 1.000 | 143.47 | 1.383 | 2.616 | 3.90 | 30.000 |
| libero_object | 0 | C_random_seed | 30 | 1.000 | 143.60 | 1.388 | 2.817 | 3.90 | 30.000 |
| libero_object | 0 | D_low_uncertainty_reject_log | 30 | 1.000 | 142.77 | 1.376 | 2.518 | 3.03 | 30.000 |
| libero_spatial | 5 | A_passive | 30 | 0.133 | 540.93 | 1.459 | 3.218 | 23.17 | 4.000 |
| libero_spatial | 5 | B_deliberation | 30 | 0.133 | 550.70 | 1.455 | 2.969 | 26.33 | 4.000 |
| libero_spatial | 5 | C_random_seed | 30 | 0.133 | 537.30 | 1.516 | 3.258 | 30.50 | 4.000 |
| libero_spatial | 5 | D_low_uncertainty_reject_log | 30 | 0.133 | 540.93 | 1.459 | 3.218 | 23.13 | 4.000 |

## Episode Rows

| file | suite | task | mode | success | steps | unc_mean | unc_max | rejects |
|---|---|---:|---|---:|---:|---:|---:|---:|
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 252 | 1.2554136809736196 | 2.060796022415161 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 247 | 1.2565333494032271 | 2.1268422603607178 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 226 | 1.2271213553407614 | 2.1923000812530518 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 236 | 1.2850458233709066 | 2.032543897628784 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 257 | 1.1997454872409117 | 1.876509428024292 | 5 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 255 | 1.2514217700444015 | 1.911618947982788 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 227 | 1.1998815032152028 | 2.041109561920166 | 4 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 240 | 1.2461348213255405 | 2.0732476711273193 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 245 | 1.310061284473964 | 2.068537473678589 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 232 | 1.2515993259286369 | 1.9776602983474731 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 364 | 1.1024025641807975 | 1.9286420345306396 | 5 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 239 | 1.2701190211631694 | 2.0774271488189697 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 231 | 1.2768568514491156 | 2.074481725692749 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 242 | 1.151555324338146 | 1.9632402658462524 | 4 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 260 | 1.1864467824880893 | 1.9495453834533691 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 247 | 1.2790394028027852 | 2.121891736984253 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 246 | 1.3274420368913058 | 2.3553078174591064 | 11 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 252 | 1.2412386176609758 | 1.9938633441925049 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 248 | 1.2592123834878806 | 2.097349166870117 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 252 | 1.3380544044003628 | 2.313502788543701 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 247 | 1.156817191477978 | 1.8834444284439087 | 4 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 242 | 1.2328770467915486 | 1.9581462144851685 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 230 | 1.3191926233146503 | 2.1070282459259033 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 251 | 1.2828768053591646 | 2.236588478088379 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 232 | 1.3832274252368557 | 2.1260156631469727 | 14 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 231 | 1.2475501663393254 | 1.9424694776535034 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 230 | 1.3223061950310417 | 2.0756447315216064 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 236 | 1.3059528020905777 | 2.355083465576172 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 232 | 1.3007652653801827 | 2.070502519607544 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 247 | 1.2529742513040099 | 2.049419403076172 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 247 | 1.2365834050708346 | 2.1132490634918213 | 12 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 244 | 1.2689821181036913 | 2.262010335922241 | 11 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 232 | 1.2259952329820203 | 2.2365901470184326 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 242 | 1.2559704448758942 | 2.0866007804870605 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 283 | 1.2605836002265707 | 1.9753830432891846 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 0 | 600 | 1.1090728737413884 | 1.989168643951416 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 242 | 1.2022597095401018 | 2.0375711917877197 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 237 | 1.2193888199956793 | 2.092953681945801 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 242 | 1.2585780006094076 | 2.160140037536621 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 238 | 1.2110912345506095 | 2.001297950744629 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 232 | 1.2361429279209466 | 2.044421911239624 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 239 | 1.3007177849679874 | 2.1986846923828125 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 239 | 1.2197955601722106 | 2.043642044067383 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 244 | 1.1620317381193206 | 1.9643272161483765 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 266 | 1.1449440091848373 | 2.0324134826660156 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 241 | 1.2414941654123108 | 2.099076509475708 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 249 | 1.3014171087622244 | 2.1245853900909424 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 254 | 1.223168466130241 | 2.017082452774048 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 252 | 1.2740072132927356 | 2.2813174724578857 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 253 | 1.347625467730196 | 2.4767680168151855 | 12 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 252 | 1.1352868800116058 | 1.974595546722412 | 5 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 249 | 1.2013497215050917 | 2.090083360671997 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 245 | 1.3079288346426827 | 2.2332680225372314 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 246 | 1.2797478441451047 | 2.2401986122131348 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 242 | 1.3981435212892355 | 2.224970817565918 | 15 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 370 | 1.2089934103392266 | 2.223832368850708 | 13 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 238 | 1.3332437506088843 | 2.0985636711120605 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 235 | 1.381129116454023 | 2.5607895851135254 | 11 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 233 | 1.296649764265333 | 2.1110405921936035 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 252 | 1.2554563708824686 | 2.019657850265503 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 249 | 1.2019851819727334 | 2.1257855892181396 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 244 | 1.26255052081554 | 2.338524341583252 | 11 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 227 | 1.2535840675726042 | 2.1967897415161133 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 236 | 1.3193026575404154 | 2.070793628692627 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 283 | 1.2420336334144368 | 1.9316167831420898 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 257 | 1.2422435515135237 | 1.92954683303833 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 241 | 1.153869861569898 | 2.002964973449707 | 3 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 258 | 1.1777338937405617 | 2.1807470321655273 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 238 | 1.312186095681224 | 2.20215106010437 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 237 | 1.2404912214530142 | 2.030667781829834 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 235 | 1.196500855557462 | 2.0249013900756836 | 5 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 244 | 1.2836256399496424 | 2.1854310035705566 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 233 | 1.237216610780784 | 2.0719752311706543 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 237 | 1.1596012033914265 | 2.0641186237335205 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 278 | 1.145100193823169 | 1.995278000831604 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 238 | 1.2582465195572459 | 2.0954651832580566 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 249 | 1.3223069808554888 | 2.2533469200134277 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 253 | 1.2305582985281944 | 2.0523805618286133 | 9 |
| `libero_10_task0.json` | 

# Stage 8 Normal LIBERO Hard-Task Baseline

- Input dir: `asynchvla_ws/stage8_ultimate/results/normal_libero_hard`
- Files: `7`
- Episodes: `350`

## Aggregate By Suite/Task/Mode

| suite | task | mode | episodes | success_rate | avg_steps | avg_unc | max_unc | avg_rejects | reward_sum |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| libero_10 | 0 | A_passive | 10 | 1.000 | 241.70 | 1.248 | 2.192 | 7.40 | 10.000 |
| libero_10 | 0 | B_deliberation | 10 | 0.900 | 280.70 | 1.225 | 2.262 | 8.50 | 9.000 |
| libero_10 | 0 | C_random_seed | 10 | 1.000 | 247.00 | 1.241 | 2.339 | 8.10 | 10.000 |
| libero_10 | 0 | D_low_uncertainty_reject_log | 10 | 1.000 | 241.70 | 1.248 | 2.192 | 7.40 | 10.000 |
| libero_10 | 0 | E_conservative_switch_proxy | 10 | 1.000 | 240.20 | 1.247 | 2.304 | 7.20 | 10.000 |
| libero_10 | 1 | A_passive | 10 | 1.000 | 237.20 | 1.421 | 2.312 | 10.10 | 10.000 |
| libero_10 | 1 | B_deliberation | 10 | 1.000 | 252.10 | 1.396 | 2.387 | 9.60 | 10.000 |
| libero_10 | 1 | C_random_seed | 10 | 1.000 | 241.40 | 1.408 | 2.212 | 9.40 | 10.000 |
| libero_10 | 1 | D_low_uncertainty_reject_log | 10 | 1.000 | 237.20 | 1.421 | 2.312 | 10.10 | 10.000 |
| libero_10 | 1 | E_conservative_switch_proxy | 10 | 1.000 | 235.80 | 1.427 | 2.376 | 10.00 | 10.000 |
| libero_goal | 0 | A_passive | 10 | 0.900 | 221.30 | 2.151 | 3.241 | 20.60 | 9.000 |
| libero_goal | 0 | B_deliberation | 10 | 0.800 | 272.60 | 2.118 | 3.244 | 20.90 | 8.000 |
| libero_goal | 0 | C_random_seed | 10 | 1.000 | 194.40 | 2.145 | 3.245 | 18.50 | 10.000 |
| libero_goal | 0 | D_low_uncertainty_reject_log | 10 | 0.900 | 221.30 | 2.151 | 3.241 | 20.60 | 9.000 |
| libero_goal | 0 | E_conservative_switch_proxy | 10 | 0.800 | 218.30 | 2.206 | 3.244 | 18.40 | 8.000 |
| libero_goal | 2 | A_passive | 10 | 0.800 | 188.20 | 2.144 | 4.342 | 16.50 | 8.000 |
| libero_goal | 2 | B_deliberation | 10 | 1.000 | 89.40 | 2.341 | 4.300 | 13.40 | 10.000 |
| libero_goal | 2 | C_random_seed | 10 | 0.900 | 138.20 | 2.235 | 4.330 | 16.20 | 9.000 |
| libero_goal | 2 | D_low_uncertainty_reject_log | 10 | 0.800 | 188.20 | 2.164 | 4.342 | 19.50 | 8.000 |
| libero_goal | 2 | E_conservative_switch_proxy | 10 | 0.900 | 142.80 | 2.248 | 4.364 | 15.50 | 9.000 |
| libero_goal | 9 | A_passive | 10 | 0.700 | 270.70 | 2.427 | 5.392 | 23.80 | 7.000 |
| libero_goal | 9 | B_deliberation | 10 | 0.700 | 272.60 | 2.456 | 5.369 | 26.50 | 7.000 |
| libero_goal | 9 | C_random_seed | 10 | 0.900 | 175.40 | 2.705 | 5.591 | 20.60 | 9.000 |
| libero_goal | 9 | D_low_uncertainty_reject_log | 10 | 0.700 | 270.70 | 2.427 | 5.392 | 23.80 | 7.000 |
| libero_goal | 9 | E_conservative_switch_proxy | 10 | 0.800 | 248.80 | 2.507 | 5.385 | 25.50 | 8.000 |
| libero_object | 0 | A_passive | 10 | 1.000 | 144.10 | 1.356 | 2.518 | 2.80 | 10.000 |
| libero_object | 0 | B_deliberation | 10 | 1.000 | 147.70 | 1.355 | 2.616 | 3.30 | 10.000 |
| libero_object | 0 | C_random_seed | 10 | 1.000 | 145.20 | 1.372 | 2.652 | 3.90 | 10.000 |
| libero_object | 0 | D_low_uncertainty_reject_log | 10 | 1.000 | 144.10 | 1.356 | 2.518 | 2.80 | 10.000 |
| libero_object | 0 | E_conservative_switch_proxy | 10 | 1.000 | 160.70 | 1.305 | 2.087 | 2.60 | 10.000 |
| libero_spatial | 5 | A_passive | 10 | 0.200 | 525.60 | 1.501 | 3.218 | 24.80 | 2.000 |
| libero_spatial | 5 | B_deliberation | 10 | 0.000 | 600.00 | 1.442 | 2.876 | 30.10 | 0.000 |
| libero_spatial | 5 | C_random_seed | 10 | 0.000 | 600.00 | 1.483 | 2.960 | 33.80 | 0.000 |
| libero_spatial | 5 | D_low_uncertainty_reject_log | 10 | 0.200 | 525.60 | 1.501 | 3.218 | 24.80 | 2.000 |
| libero_spatial | 5 | E_conservative_switch_proxy | 10 | 0.000 | 600.00 | 1.403 | 2.874 | 24.00 | 0.000 |

## Episode Rows

| file | suite | task | mode | success | steps | unc_mean | unc_max | rejects |
|---|---|---:|---|---:|---:|---:|---:|---:|
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 252 | 1.2554136809736196 | 2.060796022415161 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 247 | 1.2565333494032271 | 2.1268422603607178 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 226 | 1.2271213553407614 | 2.1923000812530518 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 236 | 1.2850458233709066 | 2.032543897628784 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 257 | 1.1997454872409117 | 1.876509428024292 | 5 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 255 | 1.2514217700444015 | 1.911618947982788 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 227 | 1.1998815032152028 | 2.041109561920166 | 4 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 240 | 1.2461348213255405 | 2.0732476711273193 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 245 | 1.310061284473964 | 2.068537473678589 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | A_passive | 1 | 232 | 1.2515993259286369 | 1.9776602983474731 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 247 | 1.2365834050708346 | 2.1132490634918213 | 12 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 244 | 1.2689821181036913 | 2.262010335922241 | 11 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 232 | 1.2259952329820203 | 2.2365901470184326 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 242 | 1.2559704448758942 | 2.0866007804870605 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 283 | 1.2605836002265707 | 1.9753830432891846 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 0 | 600 | 1.1090728737413884 | 1.989168643951416 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 242 | 1.2022597095401018 | 2.0375711917877197 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 237 | 1.2193888199956793 | 2.092953681945801 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 242 | 1.2585780006094076 | 2.160140037536621 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | B_deliberation | 1 | 238 | 1.2110912345506095 | 2.001297950744629 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 249 | 1.2019851819727334 | 2.1257855892181396 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 244 | 1.26255052081554 | 2.338524341583252 | 11 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 227 | 1.2535840675726042 | 2.1967897415161133 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 236 | 1.3193026575404154 | 2.070793628692627 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 283 | 1.2420336334144368 | 1.9316167831420898 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 257 | 1.2422435515135237 | 1.92954683303833 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 241 | 1.153869861569898 | 2.002964973449707 | 3 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 258 | 1.1777338937405617 | 2.1807470321655273 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 238 | 1.312186095681224 | 2.20215106010437 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | C_random_seed | 1 | 237 | 1.2404912214530142 | 2.030667781829834 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 252 | 1.2554136809736196 | 2.060796022415161 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 247 | 1.2565333494032271 | 2.1268422603607178 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 226 | 1.2271213553407614 | 2.1923000812530518 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 236 | 1.2850458233709066 | 2.032543897628784 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 257 | 1.1997454872409117 | 1.876509428024292 | 5 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 255 | 1.2514217700444015 | 1.911618947982788 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 227 | 1.1998815032152028 | 2.041109561920166 | 4 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 240 | 1.2461348213255405 | 2.0732476711273193 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 245 | 1.310061284473964 | 2.068537473678589 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | D_low_uncertainty_reject_log | 1 | 232 | 1.2515993259286369 | 1.9776602983474731 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 250 | 1.2264311683177949 | 2.060796022415161 | 8 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 247 | 1.2571701858982895 | 2.3037269115448 | 9 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 224 | 1.215300178217622 | 2.205590009689331 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 233 | 1.2960213203515325 | 2.032543897628784 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 253 | 1.2150635001690764 | 1.9096057415008545 | 6 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 256 | 1.2223169830712406 | 1.8907458782196045 | 5 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 232 | 1.1960346493669736 | 1.9819049835205078 | 5 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 230 | 1.2528395264045051 | 2.008357048034668 | 7 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 244 | 1.337398996328738 | 2.068537473678589 | 10 |
| `libero_10_task0.json` | libero_10 | 0 | E_conservative_switch_proxy | 1 | 233 | 1.2527192388262067 | 1.9786940813064575 | 5 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 222 | 1.4780967657485704 | 2.209041118621826 | 9 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 244 | 1.3457935417878344 | 1.9870789051055908 | 6 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 243 | 1.3779079989619452 | 2.0441248416900635 | 9 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 238 | 1.4426920730750878 | 2.052755832672119 | 14 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 238 | 1.4491730228170647 | 2.113786458969116 | 12 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 232 | 1.4538540686330488 | 1.9951326847076416 | 11 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 233 | 1.531027507356235 | 2.1396398544311523 | 20 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 236 | 1.450215907583774 | 2.3122243881225586 | 8 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 232 | 1.3411100513191634 | 2.0206105709075928 | 8 |
| `libero_10_task1.json` | libero_10 | 1 | A_passive | 1 | 254 | 1.3382389224943567 | 1.9585689306259155 | 4 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 235 | 1.4149027657001576 | 1.9548306465148926 | 8 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 237 | 1.3739675546947279 | 1.9893033504486084 | 7 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 341 | 1.219694732020541 | 2.0300774574279785 | 11 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 243 | 1.4466583732872793 | 1.9879931211471558 | 14 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 232 | 1.4937826612944245 | 1.9869097471237183 | 13 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 235 | 1.441394586512383 | 2.135523796081543 | 8 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 239 | 1.4829817817186228 | 2.3868350982666016 | 14 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 259 | 1.415831272145943 | 2.055346965789795 | 8 |
| `libero_10_task1.json` | libero_10 | 1 | B_deliberation | 1 | 237 | 1.3647781422263698 | 1.9804792404174805 | 10 |
| `libero_10_task1.json` | libero_10 | 1 | B_deli

## Flowtrace Results

# Stage 8 Flowtrace Results

Dataset: `asynchvla_ws/data/processed_stage7_flow/stage8_flowtrace_medium`

- `flowtrace_multiseed_trace_calib.pt`: 100 contexts, seeds=[0, 1, 2, 3, 4]
- `flowtrace_multiseed_trace_test_id.pt`: 100 contexts, seeds=[0, 1, 2, 3, 4]
- `flowtrace_multiseed_trace_test_ood.pt`: 100 contexts, seeds=[0, 1, 2, 3, 4]
- `flowtrace_multiseed_trace_train.pt`: 300 contexts, seeds=[0, 1, 2, 3, 4]


## Target Comparison

_Missing: `stage8_target_comparison.md`_

## Model Sweep

_Missing: `stage8_model_sweep_results.md`_

## Calibration

_Missing: `stage8_calibration_mega_sweep.md`_

# Stage 8 Calibration Best Method

- `id_task_split` `context_gated_action` `test_id_simvla` `global_residual_all` coverage=0.900 width=0.196
- `holdout_object_bowl` `context_gated_action` `test_ood_all` `affine_plus_residual_all` coverage=0.900 width=0.123
- `holdout_object_bowl` `full_engineered_simvla_focused` `test_ood_all` `global_residual_all` coverage=0.900 width=0.158
- `holdout_libero_object` `context_gated_action` `test_id_all` `global_residual_all` coverage=0.899 width=0.099
- `holdout_object_bowl` `context_gated_action` `test_ood_all` `global_residual_simvla` coverage=0.899 width=0.114
- `holdout_object_bowl` `context_gated_action` `test_ood_all` `global_residual_all` coverage=0.899 width=0.114
- `holdout_libero_object` `context_gated_action` `test_ood_simvla` `global_residual_simvla` coverage=0.899 width=0.123
- `holdout_scene_kitchen_scene2` `context_gated_action` `test_id_all` `global_residual_simvla` coverage=0.901 width=0.242
- `id_task_split` `full_old_baseline` `test_id_all` `global_residual_all` coverage=0.901 width=0.250
- `holdout_libero_goal` `action_only_baseline` `test_ood_simvla` `global_residual_simvla` coverage=0.899 width=1.017


## History Models

_Missing: `stage8_history_models.md`_

## Switch Policy

# Stage 8 Switch Policy Results

Episodes parsed: `1665`

| mode | episodes | success_rate | avg_steps | avg_rejects | avg_unc |
|---|---:|---:|---:|---:|---:|
| `A_passive` | 395 | 0.856 | 227.61 | 12.95 | 1.711 |
| `B_deliberation` | 395 | 0.838 | 243.20 | 13.91 | 1.704 |
| `C_random_seed` | 395 | 0.861 | 228.13 | 13.69 | 1.729 |
| `D_low_uncertainty_reject_log` | 395 | 0.856 | 227.61 | 13.02 | 1.712 |
| `E_conservative_switch_proxy` | 85 | 0.824 | 244.02 | 12.89 | 1.690 |

## Interpretation

- This is an offline policy analysis over available rollout logs.
- Oracle WM/expert fallback is not claimed unless expert-action rollout substitution is explicitly available.
- Threshold stability and accepted/rejected risk should be revisited after expanded LIBERO-PRO and hard-task jobs finish.


## Failure Analysis

- Missing LIBERO-PRO init-state files block some perturbation suites; valid suites with local `.pruned_init` files should be preferred.
- Deliberation must be judged by success/progress and steps, not only lower predicted uncertainty.

## Final Decision

Interim until the 72-hour queue completes. Current direction: keep LIBERO-PRO as the primary benchmark and use normal LIBERO only as baseline/fallback.

## Artifact/report list

```text

```
