#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
SESSION=simvla-h10-hard1000-pipeline
PY=/home/redafrix/miniconda3/bin/python
RUNNER="$WORKSPACE/automation/hard1000_pipeline.py"
LOG="$WORKSPACE/logs/hard1000_pipeline.log"
STATUS="$WORKSPACE/automation/hard1000_pipeline_status.json"
STOP="$WORKSPACE/automation/STOP_HARD1000_PIPELINE_AFTER_CURRENT_EPISODE"
COMPLETE="$WORKSPACE/automation/HARD1000_COMBINED_TRAIN_AND_EVAL_COMPLETE"
HARD_OUTPUT="$WORKSPACE/outputs/final_seen_h10_round_002_seed20260804"

case "${1:-}" in
    start)
        rm -f "$STOP"
        if tmux has-session -t "$SESSION" 2>/dev/null; then
            echo "SESSION_ALREADY_RUNNING=$SESSION"
            exit 0
        fi
        mkdir -p "$(dirname "$LOG")"
        tmux new-session -d -s "$SESSION" \
            "exec '$PY' -u '$RUNNER' >> '$LOG' 2>&1"
        echo "SESSION=$SESSION"
        echo "LOG=$LOG"
        echo "STATUS=$STATUS"
        ;;
    ensure)
        if [[ -f "$COMPLETE" ]]; then
            echo "PIPELINE_ALREADY_COMPLETE=YES"
        elif [[ -f "$STOP" ]]; then
            echo "PIPELINE_STOP_REQUESTED=YES"
        elif tmux has-session -t "$SESSION" 2>/dev/null; then
            echo "SESSION_ALREADY_RUNNING=$SESSION"
        else
            mkdir -p "$(dirname "$LOG")"
            tmux new-session -d -s "$SESSION" \
                "exec '$PY' -u '$RUNNER' >> '$LOG' 2>&1"
            echo "SESSION_RECREATED=$SESSION"
        fi
        ;;
    status)
        tmux has-session -t "$SESSION" 2>/dev/null && echo "TMUX_ACTIVE=YES" || echo "TMUX_ACTIVE=NO"
        [[ -f "$STATUS" ]] && cat "$STATUS"
        pgrep -af '[h]ard1000_pipeline.py|[c]ollect_isaac_risk.py|[t]rain_isaac_topk8.py' || true
        ;;
    stop)
        touch "$STOP"
        [[ -d "$HARD_OUTPUT" ]] && touch "$HARD_OUTPUT/STOP_AFTER_CURRENT_EPISODE"
        echo "STOP_REQUESTED_AFTER_CURRENT_ATOMIC_EPISODE=YES"
        ;;
    resume)
        "$0" start
        ;;
    logs)
        tail -n 100 -F "$LOG"
        ;;
    attach)
        exec tmux attach-session -t "$SESSION"
        ;;
    *)
        echo "Usage: $0 start|ensure|status|stop|resume|logs|attach" >&2
        exit 2
        ;;
esac
