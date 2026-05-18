# Stage 8 Sam Path Fix And Real Smokes

2026-05-15T21:12:57+02:00

## Python
Python 3.10.20

## REDA_WS
/home/rootalkhatib/test/reda_ws

## Target build smoke
  wrote /home/rootalkhatib/test/reda_ws/asynchvla_ws/data/processed_stage5/holdout_libero_object/multiseed_candidate_train_multiexp.pt  rows=10000  K_mean=20.0
summary: /home/rootalkhatib/test/reda_ws/asynchvla_ws/data/processed_stage5/holdout_libero_object/multiseed_multi_expert_summary.json
target_build_rc=0

## Target experiment smoke
[stage] target=target_chunk_l2_single_expert staged_split=holdout_libero_object__MET_l2_single_expert parts=['train', 'calib', 'test_id', 'test_ood']
  done action_only_baseline
wrote /home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_holdout_libero_object.json
target_experiment_rc=0

## Tiny model train smoke
TRAIN holdout_libero_object action_only_baseline
wrote /home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/reports/stage6/stage8_final_tiny_model_smoke.md
tiny_model_rc=0

## Calibration smoke
/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md
calibration_rc=0

## Flowtrace builder import/help smoke
usage: build_flowtrace_multiseed_dataset.py [-h] --split-manifest
                                            SPLIT_MANIFEST --split-name
                                            SPLIT_NAME
                                            [--max-contexts MAX_CONTEXTS]
                                            [--max-calib MAX_CALIB]
                                            [--max-test-id MAX_TEST_ID]
                                            [--max-test-ood MAX_TEST_OOD]
                                            [--cap-per-file CAP_PER_FILE]
                                            [--steps STEPS]
                                            [--simvla-seeds SIMVLA_SEEDS [SIMVLA_SEEDS ...]]

options:
  -h, --help            show this help message and exit
  --split-manifest SPLIT_MANIFEST
  --split-name SPLIT_NAME
  --max-contexts MAX_CONTEXTS
  --max-calib MAX_CALIB
  --max-test-id MAX_TEST_ID
  --max-test-ood MAX_TEST_OOD
  --cap-per-file CAP_PER_FILE
flowtrace_help_rc=0

## History data availability
