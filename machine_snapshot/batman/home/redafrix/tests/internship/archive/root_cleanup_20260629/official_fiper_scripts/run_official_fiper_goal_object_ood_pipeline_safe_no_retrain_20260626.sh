#!/usr/bin/env bash
set -euo pipefail
export PYTHONUNBUFFERED=1
export PYTHONPATH=/home/redafrix/LIBERO-PRO:/home/redafrix/SimVLA_modified:${PYTHONPATH:-}
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export FIPER_VLM_MICRO_BATCH=2
PY=/home/redafrix/miniconda3/envs/simvla/bin/python
BASE=/home/dean/fiper_uncertainty_collection
EXP=$BASE/experiments/official_fiper_goal_object_ood_ablation_20260625
LOGDIR=$BASE/logs/official_fiper_goal_object_ood_ablation_20260625

mkdir -p "$LOGDIR"

echo "[pipeline] Starting safe materialization continue..."
$PY -u $BASE/scripts/materialize_ablation_dataset_safe_continue_20260626.py 2>&1 | tee "$LOGDIR/safe_continue.log"

echo "[pipeline] Starting safe merge..."
$PY -u $BASE/scripts/merge_ablation_cache_to_official_fiper_dataset_20260626.py 2>&1 | tee "$LOGDIR/safe_merge.log"

echo "[pipeline] Starting validation..."
$PY -u $BASE/scripts/validate_official_fiper_goal_object_ood_ablation.py 2>&1 | tee "$LOGDIR/validate.log"

echo "[pipeline] Starting FIPER evaluation without retraining..."
$PY -u $BASE/scripts/run_official_fiper_goal_object_ood_ablation_no_retrain_20260626.py 2>&1 | tee "$LOGDIR/safe_eval_no_retrain.log"

echo "[pipeline] Done!"
