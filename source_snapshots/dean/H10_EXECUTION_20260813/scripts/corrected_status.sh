#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
OUTPUT="$WORKSPACE/outputs/seen_chunk_h10_4000_timeout2400"
SESSION=simvla-risk-seen-4000-timeout2400

printf 'PI05_TRAINING_ACTIVE=%s\n' "$(
    pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*train_grad_accum.py' \
        >/dev/null && printf YES || printf NO
)"
printf 'CORRECTED_COLLECTION_TMUX=%s\n' "$(
    tmux has-session -t "$SESSION" 2>/dev/null &&
        printf ACTIVE || printf ABSENT
)"
printf 'CORRECTED_COLLECTOR_PROCESS=\n'
pgrep -af '[c]ollect_isaac_risk.py' || true
if [[ -f "$OUTPUT/live_status.json" ]]; then
    printf 'CORRECTED_COLLECTION_STATUS='
    jq -c . "$OUTPUT/live_status.json"
else
    printf 'CORRECTED_COLLECTION_STATUS=NOT_STARTED\n'
fi
printf 'FINALIZED_EPISODES=%s\n' "$(
    find "$OUTPUT/episodes" -mindepth 2 -maxdepth 2 \
        -type f -name COMMITTED 2>/dev/null | wc -l
)"
