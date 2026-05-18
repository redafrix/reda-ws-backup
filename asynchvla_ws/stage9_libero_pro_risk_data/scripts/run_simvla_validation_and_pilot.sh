#!/usr/bin/env bash
set -euo pipefail
ROOT="/media/rootalkhatib/My Passport/reda_ws"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="$ROOT/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export PYTHONPATH="$ROOT/asynchvla_ws/src:$PYTHONPATH"
python3 -m data_collection_stage9.validate_simvla_seed_repeatability --suite libero_object_with_mug --task-id 0
python3 -m data_collection_stage9.collect_counterfactual_dataset --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug --task-ids 0 1 --states-per-task 3 --simvla-seeds 0 1 2 3 --horizon 10 --history-k 4 --save-images --out-dir "$ROOT/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/smoke_counterfactual"
python3 -m data_collection_stage9.analyze_dataset_quality --dataset "$ROOT/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/smoke_counterfactual/counterfactual_samples.jsonl"
python3 -m data_collection_stage9.validate_labeler --dataset "$ROOT/asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/smoke_counterfactual/counterfactual_samples.jsonl"
