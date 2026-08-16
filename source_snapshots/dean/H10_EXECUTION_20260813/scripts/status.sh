#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
TRAIN_LOG=/mnt/ai/pi05/training/reaching_pose_v1_4400_pi05_fullpose_v3/logs/production_v1.log
OUTPUT="$WORKSPACE/outputs/seen_chunk_h10_4000"

printf 'PI05_TRAINING_ACTIVE=%s\n' "$(
    pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*train_grad_accum.py' \
        >/dev/null && printf YES || printf NO
)"
tr -d '\000\r' < "$TRAIN_LOG" 2>/dev/null |
    grep 'TRAIN_METRICS_JSON=' |
    tail -1 || true
printf 'SUPERVISOR_TMUX=%s\n' "$(
    tmux has-session -t simvla-risk-supervisor 2>/dev/null &&
        printf ACTIVE || printf ABSENT
)"
printf 'COLLECTION_TMUX=%s\n' "$(
    tmux has-session -t simvla-risk-seen-4000 2>/dev/null &&
        printf ACTIVE || printf ABSENT
)"
if [[ -f "$OUTPUT/live_status.json" ]]; then
    printf 'COLLECTION_STATUS='
    jq -c . "$OUTPUT/live_status.json"
else
    printf 'COLLECTION_STATUS=NOT_STARTED\n'
fi
