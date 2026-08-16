#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
UNIT=simvla-isaac-risk-h10-pipeline.service
STOP="$WORKSPACE/automation/STOP_PIPELINE_AFTER_CURRENT_EPISODE"
STATUS="$WORKSPACE/automation/pipeline_live_status.json"
LOG="$WORKSPACE/logs/final_risk_pipeline_supervisor.log"

case "${1:-}" in
    start|resume)
        rm -f "$STOP"
        systemctl --user enable --now "$UNIT"
        printf 'SERVICE=%s\nSTATUS=%s\nLOG=%s\n' "$UNIT" "$STATUS" "$LOG"
        ;;
    stop)
        touch "$STOP"
        for output in "$WORKSPACE"/outputs/final_seen_h10_round_*_seed*; do
            [[ -d "$output" ]] || continue
            state=$(python3 - "$output/live_status.json" <<'PY'
import json,sys
from pathlib import Path
p=Path(sys.argv[1]); print(json.loads(p.read_text()).get("state","") if p.exists() else "")
PY
)
            [[ "$state" == running ]] && touch "$output/STOP_AFTER_CURRENT_EPISODE"
        done
        printf 'Clean stop requested after the current episode.\n'
        ;;
    status)
        systemctl --user --no-pager status "$UNIT" || true
        [[ -f "$STATUS" ]] && cat "$STATUS"
        pgrep -af '[c]ollect_isaac_risk.py|[t]rain_isaac_topk8.py' || true
        ;;
    logs)
        tail -n 100 -F "$LOG"
        ;;
    *)
        printf 'Usage: %s start|resume|stop|status|logs\n' "$0" >&2
        exit 2
        ;;
esac
