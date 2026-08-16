#!/usr/bin/env bash
set -euo pipefail

if (($# != 0)); then
    printf 'Production launcher accepts no arguments; smoke flags are forbidden.\n' >&2
    exit 29
fi

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
RUNNER="$WORKSPACE/scripts/run_collector.sh"
CONFIG="$WORKSPACE/configs/seen_chunk_h10_4000_timeout2400.yaml"
MANIFEST="$WORKSPACE/manifests/seen_4000_master.json"
OUTPUT="$WORKSPACE/outputs/seen_chunk_h10_4000_timeout2400"
LOG="$WORKSPACE/logs/seen_chunk_h10_4000_timeout2400.log"
SESSION=simvla-risk-seen-4000-timeout2400

if pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*train_grad_accum.py' >/dev/null; then
    printf 'Refusing launch: pi0.5 fine-tuning is active.\n' >&2
    exit 30
fi
if pgrep -af '[c]ollect_isaac_risk.py' >/dev/null; then
    printf 'Refusing launch: another risk collector is active.\n' >&2
    exit 31
fi
if tmux has-session -t "$SESSION" 2>/dev/null; then
    printf 'Session already exists: %s\n' "$SESSION" >&2
    exit 32
fi
if [[ -e "$OUTPUT/STOP_AFTER_CURRENT_EPISODE" ]]; then
    printf 'Refusing launch while stop marker exists: %s\n' \
        "$OUTPUT/STOP_AFTER_CURRENT_EPISODE" >&2
    exit 33
fi

mkdir -p "$OUTPUT" "$(dirname "$LOG")"
chmod 0755 "$OUTPUT" "$(dirname "$LOG")"
touch "$LOG"
chmod 0644 "$LOG"

tmux new-session -d -s "$SESSION" \
    "bash -lc 'exec \"$RUNNER\" \
    --run-config \"$CONFIG\" \
    --manifest \"$MANIFEST\" \
    --output-dir \"$OUTPUT\" \
    --offset 0 --count 4000 \
    --execution-mode chunk_h10 \
    --viz none --device cuda:0 \
    >> \"$LOG\" 2>&1'"

printf 'CORRECTED_COLLECTION_TMUX=%s\n' "$SESSION"
printf 'CORRECTED_COLLECTION_LOG=%s\n' "$LOG"
printf 'CORRECTED_COLLECTION_OUTPUT=%s\n' "$OUTPUT"
printf 'CORRECTED_COLLECTION_STATUS=%s/live_status.json\n' "$OUTPUT"
