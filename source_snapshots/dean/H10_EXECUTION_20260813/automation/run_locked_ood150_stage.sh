#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
PY=/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python
GENERATED="$WORKSPACE/automation/generated/locked_ood150"
CONFIG="$GENERATED/run_config.yaml"
MANIFEST="$GENERATED/manifest.json"
OUTPUT="$WORKSPACE/outputs/final_locked_h10_ood150_seed20260728"
LOG="$WORKSPACE/logs/final_locked_h10_ood150_seed20260728.log"
REPORTS="$OUTPUT/reports"

mkdir -p "$REPORTS" "$(dirname "$LOG")"
touch "$LOG"
chmod 0644 "$LOG"
free_bytes=$(df --output=avail -B1 /mnt/ai | tail -1 | tr -d ' ')
if ((free_bytes < 100 * 1024 * 1024 * 1024)); then
    printf 'OOD150 blocked: SSD free space below 100 GiB.\n' >&2
    exit 70
fi
if pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*[t]rain_grad_accum.py|[t]rain_isaac_topk8.py|[c]ollect_isaac_risk.py' >/dev/null; then
    printf 'OOD150 blocked: another GPU job is active.\n' >&2
    exit 71
fi

"$PY" "$WORKSPACE/automation/prepare_locked_ood150.py" \
    > "$REPORTS/preparation.log" 2>&1
rm -f "$OUTPUT/STOP_AFTER_CURRENT_EPISODE"
"$PY" "$WORKSPACE/automation/run_with_progress_watchdog.py" \
    --status "$OUTPUT/live_status.json" \
    --events "$OUTPUT/watchdog_stall_events.jsonl" \
    --watchdog-status "$OUTPUT/watchdog_status.json" \
    --stall-seconds 1800 --max-stall-restarts 5 -- \
    "$WORKSPACE/scripts/run_collector.sh" \
        --run-config "$CONFIG" --manifest "$MANIFEST" --output-dir "$OUTPUT" \
        --offset 0 --count 150 --execution-mode chunk_h10 \
        --viz none --device cuda:0 >> "$LOG" 2>&1

if [[ ! -f "$OUTPUT/live_status.json" ]]; then
    printf 'OOD150 collector exited without durable live status: %s\n' \
        "$OUTPUT/live_status.json" >&2
    exit 125
fi
state=$(
    "$PY" - "$OUTPUT/live_status.json" <<'PY'
import json,sys
from pathlib import Path
print(json.loads(Path(sys.argv[1]).read_text()).get("state","missing"))
PY
)
if [[ "$state" != complete ]]; then
    printf 'OOD150 stage ended without completion: %s\n' "$state" >&2
    exit 72
fi
/usr/bin/timeout --signal=INT --kill-after=120s 4h \
  "$PY" "$WORKSPACE/risk_head_pipeline/audit_ood150.py" "$OUTPUT" \
    --report-json "$REPORTS/exhaustive_audit.json" \
    > "$REPORTS/exhaustive_audit.log" 2>&1
