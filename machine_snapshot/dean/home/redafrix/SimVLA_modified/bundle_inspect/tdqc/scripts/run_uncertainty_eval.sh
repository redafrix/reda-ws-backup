#!/usr/bin/env bash
# run_uncertainty_eval.sh
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ENV_PATH="$WS_ROOT/assets/envs/simvla"
PYTHON="$ENV_PATH/bin/python"

# Fix for LIBERO initialization paths
export PYTHONPATH="$WS_ROOT/assets/data/LIBERO:$WS_ROOT/simvla/code/SimVLA_modified:$PYTHONPATH"

# Evaluation details
HOST="127.0.0.1"
PORT="8001"
TASK_SUITE="libero_spatial"
TASK_ID="0"
EPISODE_INDEX="0"
OUTPUT_DIR="${OUTPUT_DIR:-$WS_ROOT/outputs/eval/sweep_3_eval}"
VIDEO_PATH="${VIDEO_PATH:-$OUTPUT_DIR/${TASK_SUITE}_task${TASK_ID}_ep${EPISODE_INDEX}_4x.mp4}"
SUMMARY_PATH="${SUMMARY_PATH:-$OUTPUT_DIR/${TASK_SUITE}_task${TASK_ID}_ep${EPISODE_INDEX}_summary.json}"

mkdir -p "$OUTPUT_DIR"

echo "=========================================================="
echo "🚀 Running LIBERO Evaluation (4x Video)"
echo "Task Suite: $TASK_SUITE"
echo "Task ID: $TASK_ID"
echo "Video Output: $VIDEO_PATH"
echo "=========================================================="

cd "$WS_ROOT"
$PYTHON "$WS_ROOT/simvla/scripts/run_libero_single_task_eval.py" \
    --host "$HOST" \
    --port "$PORT" \
    --task_suite "$TASK_SUITE" \
    --task_id "$TASK_ID" \
    --episode_index "$EPISODE_INDEX" \
    --video_path "$VIDEO_PATH" \
    --summary_path "$SUMMARY_PATH"

echo "✅ Evaluation complete!"
echo "Video saved to: $VIDEO_PATH"
