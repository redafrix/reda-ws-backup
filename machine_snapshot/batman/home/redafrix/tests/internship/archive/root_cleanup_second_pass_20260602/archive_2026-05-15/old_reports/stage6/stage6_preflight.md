# Stage 6 Preflight

- hostname: PCROBOTUBUNTU02
- branch: bob
- git status short:
   M asynchvla_ws/outputs/checkpoints/stage5_debug/predictions.json
   M asynchvla_ws/src/eval/eval_simvla_only.py
   M asynchvla_ws/src/rater/train_stage5_rater.py
  ?? asynchvla_ws/ASYNCVLA_SIMVLA_STAGE5_MULTI_SEED_REPORT.md
  ?? asynchvla_ws/outputs/checkpoints/stage5/
  ?? asynchvla_ws/outputs/reports/stage5_claude_resume_precheck.md
  ?? asynchvla_ws/outputs/reports/stage5_debug_interpretation.md
  ?? asynchvla_ws/outputs/reports/stage5_debug_rater_metrics.md
  ?? asynchvla_ws/outputs/reports/stage5_debug_rater_metrics_v2.json
  ?? asynchvla_ws/outputs/reports/stage5_debug_rater_metrics_v2.md
  ?? asynchvla_ws/outputs/reports/stage5_holdout_libero_object_metrics.json
  ?? asynchvla_ws/outputs/reports/stage5_holdout_libero_object_metrics.md
  ?? asynchvla_ws/outputs/reports/stage5_holdout_libero_object_simvla_only_calibration.json
  ?? asynchvla_ws/outputs/reports/stage5_holdout_libero_object_simvla_only_calibration.md
  ?? asynchvla_ws/outputs/reports/stage5_holdout_object_bowl_metrics.json
  ?? asynchvla_ws/outputs/reports/stage5_holdout_object_bowl_metrics.md
  ?? asynchvla_ws/outputs/reports/stage5_holdout_object_bowl_simvla_only_calibration.json
  ?? asynchvla_ws/outputs/reports/stage5_holdout_object_bowl_simvla_only_calibration.md
  ?? asynchvla_ws/outputs/reports/stage5_id_task_split_metrics.json
  ?? asynchvla_ws/outputs/reports/stage5_id_task_split_metrics.md
  ?? asynchvla_ws/outputs/reports/stage5_id_task_split_simvla_only_calibration.json
  ?? asynchvla_ws/outputs/reports/stage5_id_task_split_simvla_only_calibration.md
  ?? asynchvla_ws/outputs/reports/stage5_medium_dataset_build_report.md
  ?? asynchvla_ws/outputs/reports/stage5_simvla_only_calibration.md
  ?? asynchvla_ws/outputs/reports/stage6_preflight.md
  ?? asynchvla_ws/src/calibration/calibrate_stage5_simvla_only.py
  ?? asynchvla_ws/train_stage5_rater.py

- which python3: /usr/bin/python3
- python3 version: Python 3.10.12
- torch: 2.5.1+cu121
- cuda available: True
- torch cuda: 12.1

## Stage 5 datasets
- asynchvla_ws/data/processed_stage5/id_task_split
  total 110M
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  23K May 13 16:52 manifest_used.json
  drwxr-xr-x 2 rootalkhatib rootalkhatib 1.0M May 13 17:06 metas
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  192 May 13 18:29 multiseed_candidate_build_summary.json
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  14M May 13 18:29 multiseed_candidate_calib.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  15M May 13 18:29 multiseed_candidate_test_id.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  57M May 13 18:29 multiseed_candidate_train.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib 3.2M May 13 17:04 multiseed_trace_calib.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib 3.2M May 13 17:06 multiseed_trace_test_id.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  13M May 13 17:01 multiseed_trace_train.pt
- asynchvla_ws/data/processed_stage5/holdout_libero_object
  total 129M
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  23K May 13 18:29 manifest_used.json
  drwxr-xr-x 2 rootalkhatib rootalkhatib 1.0M May 13 18:45 metas
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  257 May 13 18:46 multiseed_candidate_build_summary.json
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  14M May 13 18:46 multiseed_candidate_calib.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  15M May 13 18:46 multiseed_candidate_test_id.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  15M May 13 18:46 multiseed_candidate_test_ood.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  57M May 13 18:46 multiseed_candidate_train.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib 3.2M May 13 18:41 multiseed_trace_calib.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib 3.2M May 13 18:43 multiseed_trace_test_id.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib 3.2M May 13 18:46 multiseed_trace_test_ood.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  13M May 13 18:38 multiseed_trace_train.pt
- asynchvla_ws/data/processed_stage5/holdout_object_bowl
  total 129M
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  23K May 13 18:46 manifest_used.json
  drwxr-xr-x 2 rootalkhatib rootalkhatib 1.0M May 13 19:02 metas
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  257 May 13 19:03 multiseed_candidate_build_summary.json
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  14M May 13 19:02 multiseed_candidate_calib.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  15M May 13 19:03 multiseed_candidate_test_id.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  15M May 13 19:03 multiseed_candidate_test_ood.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  57M May 13 19:02 multiseed_candidate_train.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib 3.2M May 13 18:58 multiseed_trace_calib.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib 3.2M May 13 19:00 multiseed_trace_test_id.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib 3.2M May 13 19:02 multiseed_trace_test_ood.pt
  -rwxr-xr-x 1 rootalkhatib rootalkhatib  13M May 13 18:55 multiseed_trace_train.pt

## Stage 5 checkpoints/reports
- asynchvla_ws/outputs/checkpoints/stage5/holdout_libero_object/action_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/holdout_libero_object/context_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/holdout_libero_object/full_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/holdout_libero_object/predictions.json
- asynchvla_ws/outputs/checkpoints/stage5/holdout_object_bowl/action_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/holdout_object_bowl/context_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/holdout_object_bowl/full_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/holdout_object_bowl/predictions.json
- asynchvla_ws/outputs/checkpoints/stage5/id_task_split/action_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/id_task_split/context_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/id_task_split/full_rater.pt
- asynchvla_ws/outputs/checkpoints/stage5/id_task_split/predictions.json
- asynchvla_ws/outputs/reports/stage5_claude_resume_precheck.md
- asynchvla_ws/outputs/reports/stage5_debug_interpretation.md
- asynchvla_ws/outputs/reports/stage5_debug_rater_metrics.md
- asynchvla_ws/outputs/reports/stage5_debug_rater_metrics_v2.json
- asynchvla_ws/outputs/reports/stage5_debug_rater_metrics_v2.md
- asynchvla_ws/outputs/reports/stage5_holdout_libero_object_metrics.json
- asynchvla_ws/outputs/reports/stage5_holdout_libero_object_metrics.md
- asynchvla_ws/outputs/reports/stage5_holdout_libero_object_simvla_only_calibration.json
- asynchvla_ws/outputs/reports/stage5_holdout_libero_object_simvla_only_calibration.md
- asynchvla_ws/outputs/reports/stage5_holdout_object_bowl_metrics.json
- asynchvla_ws/outputs/reports/stage5_holdout_object_bowl_metrics.md
- asynchvla_ws/outputs/reports/stage5_holdout_object_bowl_simvla_only_calibration.json
- asynchvla_ws/outputs/reports/stage5_holdout_object_bowl_simvla_only_calibration.md
- asynchvla_ws/outputs/reports/stage5_id_task_split_metrics.json
- asynchvla_ws/outputs/reports/stage5_id_task_split_metrics.md
- asynchvla_ws/outputs/reports/stage5_id_task_split_simvla_only_calibration.json
- asynchvla_ws/outputs/reports/stage5_id_task_split_simvla_only_calibration.md
- asynchvla_ws/outputs/reports/stage5_medium_dataset_build_report.md
- asynchvla_ws/outputs/reports/stage5_multiseed_candidate_debug.md
- asynchvla_ws/outputs/reports/stage5_multiseed_trace_debug.md
- asynchvla_ws/outputs/reports/stage5_preflight.md
- asynchvla_ws/outputs/reports/stage5_simvla_only_calibration.md
- asynchvla_ws/outputs/reports/stage5_simvla_only_eval_utility.md

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       1.9T  323G  1.6T  18% /media/rootalkhatib/My Passport
