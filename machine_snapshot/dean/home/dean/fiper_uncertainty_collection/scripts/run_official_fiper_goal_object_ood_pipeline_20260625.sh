#!/usr/bin/env bash
set -euo pipefail
export PYTHONUNBUFFERED=1
export PYTHONPATH=/home/redafrix/LIBERO-PRO:/home/redafrix/SimVLA_modified:${PYTHONPATH:-}
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export FIPER_VLM_MICRO_BATCH=${FIPER_VLM_MICRO_BATCH:-4}
PY=/home/redafrix/miniconda3/envs/simvla/bin/python
BASE=/home/dean/fiper_uncertainty_collection
EXP=$BASE/experiments/official_fiper_goal_object_ood_ablation_20260625
LOGDIR=$BASE/logs/official_fiper_goal_object_ood_ablation_20260625
mkdir -p "$LOGDIR" "$EXP/reports"
mkdir -p "$EXP" "$EXP/cache" "$EXP/official_fiper_data"
echo "[pipeline] start $(date -Is)"
echo "[pipeline] disk before"; df -h /home/dean
echo "[pipeline] cache files before: $(find "$EXP/cache" -maxdepth 1 -type f 2>/dev/null | wc -l)"
echo "[pipeline] FIPER_VLM_MICRO_BATCH=$FIPER_VLM_MICRO_BATCH"

echo "[pipeline] materialization start $(date -Is)"
$PY -u $BASE/scripts/materialize_ablation_dataset.py 2>&1 | tee "$LOGDIR/materialize.log"
echo "[pipeline] materialization done $(date -Is)"

echo "[pipeline] validation start $(date -Is)"
$PY -u $BASE/scripts/validate_official_fiper_goal_object_ood_ablation.py 2>&1 | tee "$LOGDIR/validate.log"
echo "[pipeline] validation done $(date -Is)"

echo "[pipeline] evaluation start $(date -Is)"
$PY -u $BASE/scripts/run_official_fiper_goal_object_ood_ablation.py 2>&1 | tee "$LOGDIR/eval.log"
echo "[pipeline] evaluation done $(date -Is)"

echo "[pipeline] report start $(date -Is)"
$PY -u $BASE/scripts/write_official_fiper_goal_object_ood_report.py 2>&1 | tee "$LOGDIR/report.log"
echo "[pipeline] done $(date -Is)"
echo "[pipeline] disk after"; df -h /home/dean
