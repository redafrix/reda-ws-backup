#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws"
RUN_ID="${1:-broad_mini_failure_v1_$(date +%Y%m%d_%H%M%S)}"
RAW_OUT="asynchvla_ws/stage9_libero_pro_risk_data/data/raw_mini_failure_broad/${RUN_ID}"
LABEL_OUT="asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/${RUN_ID}_labels"
VIDEO_OUT="${LABEL_OUT}/event_video_frames_pre60_core10"
LOG_DIR="asynchvla_ws/stage9_libero_pro_risk_data/logs"

cd "$ROOT"
mkdir -p "$LOG_DIR"

source "asynchvla_ws/scripts/activate_simvla_bob.sh"
export PYTHONPATH="${ROOT}/asynchvla_ws/src:${ROOT}/intern_ship_ws/assets/repos/LIBERO-PRO:${PYTHONPATH:-}"
export LIBERO_CONFIG_PATH="${ROOT}/asynchvla_ws/temp_config"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export HF_HUB_DISABLE_XET=1

echo "[stage9-broad] run_id=${RUN_ID}"
echo "[stage9-broad] raw_out=${RAW_OUT}"
echo "[stage9-broad] label_out=${LABEL_OUT}"
echo "[stage9-broad] started_at=$(date -Is)"

python3 -m data_collection_stage9.collect_raw_mini_failure_episodes_v1 \
  --all-perturbed-suites \
  --max-task-id 9 \
  --rollouts-per-task 2 \
  --max-recorded-episodes 100 \
  --max-parent-episodes 220 \
  --max-runtime-minutes 240 \
  --parent-max-steps 400 \
  --parent-policy-chunk-steps 10 \
  --history-k 8 \
  --record-outcomes all \
  --policy-seed-base 2026052200 \
  --env-seed 20260522 \
  --resolution 128 \
  --out-dir "$RAW_OUT"

echo "[stage9-broad] raw collection finished at $(date -Is)"

python3 -m data_collection_stage9.detect_mini_failures \
  --raw-root "$RAW_OUT" \
  --out-dir "$LABEL_OUT" \
  --event-window 20 \
  --pre-failure-steps 60 \
  --core-label-steps 10 \
  --chunk-size 10

echo "[stage9-broad] detection finished at $(date -Is)"

python3 -m data_collection_stage9.make_mini_failure_event_videos \
  --raw-root "$RAW_OUT" \
  --events-jsonl "$LABEL_OUT/mini_failure_events.jsonl" \
  --out-dir "$VIDEO_OUT" \
  --max-videos 30 \
  --pre-steps 60 \
  --core-steps 10 \
  --fps 20 \
  --frames-only

cat > "${LABEL_OUT}/RUN_PATHS.txt" <<EOF
RUN_ID=${RUN_ID}
RAW_OUT=${ROOT}/${RAW_OUT}
LABEL_OUT=${ROOT}/${LABEL_OUT}
VIDEO_OUT=${ROOT}/${VIDEO_OUT}
EOF

echo "[stage9-broad] finished_all=$(date -Is)"
cat "${LABEL_OUT}/RUN_PATHS.txt"
