#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
PY=/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python

if (($# != 5)); then
    printf 'Usage: %s ROUND_ID ROUND_KIND MASTER_SEED POLICY_SEED GENERATED_DIR\n' "$0" >&2
    exit 2
fi

ROUND_ID=$1
ROUND_KIND=$2
MASTER_SEED=$3
POLICY_SEED=$4
GENERATED_DIR=$5
CONFIG="$GENERATED_DIR/run_config.yaml"
MANIFEST="$GENERATED_DIR/manifest.json"
OUTPUT="$WORKSPACE/outputs/final_seen_h10_round_$(printf '%03d' "$ROUND_ID")_seed${POLICY_SEED}"
LOG="$WORKSPACE/logs/final_seen_h10_round_$(printf '%03d' "$ROUND_ID")_seed${POLICY_SEED}.log"
REPORTS="$OUTPUT/reports"
STATUS="$REPORTS/stage_status.json"
EPISODE_COUNT=$("$PY" - "$MANIFEST" <<'PY'
import json,sys
from pathlib import Path
print(len(json.loads(Path(sys.argv[1]).read_text())["episodes"]))
PY
)

mkdir -p "$REPORTS" "$(dirname "$LOG")"
touch "$LOG"
chmod 0644 "$LOG"

write_status() {
    local state=$1 rc=${2:-0}
    STATE="$state" RC="$rc" OUTPUT="$OUTPUT" LOG="$LOG" "$PY" - "$STATUS" <<'PY'
import json, os, sys, time
from pathlib import Path
p=Path(sys.argv[1]); p.parent.mkdir(parents=True, exist_ok=True)
t=p.with_suffix('.tmp')
t.write_text(json.dumps({"state":os.environ["STATE"],"exit_code":int(os.environ["RC"]),"output_dir":os.environ["OUTPUT"],"log":os.environ["LOG"],"updated_at_unix_s":time.time()},indent=2,sort_keys=True)+"\n")
t.replace(p)
PY
}

# The process collecting Round 0 predates the explicit finite handoff patch and
# may still have the old open-ended supervisor code in memory. Fail closed if
# it races the systemd handoff and attempts another broad collection after the
# first model/evaluation cycle. Round 1 may still be generated as an offline
# candidate pool for hard-scene selection; it must not be collected here.
FIRST_CYCLE_COMPLETE="$WORKSPACE/automation/FIRST_RISK_TRAIN_AND_LOCKED_EVAL_COMPLETE"
if [[ "$ROUND_KIND" == broad && "$ROUND_ID" != 0 && -f "$FIRST_CYCLE_COMPLETE" ]]; then
    write_status blocked_by_hard1000_handoff 75
    printf 'Broad Round %s blocked: finite H10 pipeline has handed off to hard-1000.\n' \
        "$ROUND_ID" >&2
    exit 75
fi

free_bytes=$(df --output=avail -B1 /mnt/ai | tail -1 | tr -d ' ')
if ((free_bytes < 100 * 1024 * 1024 * 1024)); then
    write_status blocked_disk_floor 70
    exit 70
fi
if pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*[t]rain_grad_accum.py|[t]rain_isaac_topk8.py' >/dev/null; then
    write_status blocked_gpu_competitor 71
    exit 71
fi

rm -f "$OUTPUT/STOP_AFTER_CURRENT_EPISODE"
write_status collector_running 0
set +e
"$PY" "$WORKSPACE/automation/run_with_progress_watchdog.py" \
    --status "$OUTPUT/live_status.json" \
    --events "$OUTPUT/watchdog_stall_events.jsonl" \
    --watchdog-status "$OUTPUT/watchdog_status.json" \
    --stall-seconds 1800 --max-stall-restarts 5 -- \
    "$WORKSPACE/scripts/run_collector.sh" \
        --run-config "$CONFIG" \
        --manifest "$MANIFEST" \
        --output-dir "$OUTPUT" \
        --offset 0 --count "$EPISODE_COUNT" \
        --round-id "$ROUND_ID" \
        --round-kind "$ROUND_KIND" \
        --round-master-seed "$MASTER_SEED" \
        --balanced-order \
        --execution-mode chunk_h10 \
        --viz none --device cuda:0 \
        >> "$LOG" 2>&1
rc=$?
set -e
if ((rc != 0)); then
    write_status collector_failed "$rc"
    exit "$rc"
fi

if [[ ! -f "$OUTPUT/live_status.json" ]]; then
    write_status collector_failed_missing_terminal_status 125
    printf 'Collector exited without creating durable live status: %s\n' \
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
    write_status "$state" 0
    exit 0
fi

write_status exhaustive_audit_running 0
/usr/bin/timeout --signal=INT --kill-after=120s 4h \
  "$PY" "$WORKSPACE/scripts/audit_corrected_collection.py" "$OUTPUT" \
    --report-json "$REPORTS/exhaustive_audit.json" \
    --expected-outcome production_round \
    > "$REPORTS/exhaustive_audit.log" 2>&1

write_status round_summary_running 0
/usr/bin/timeout --signal=INT --kill-after=120s 30m \
  "$PY" "$WORKSPACE/scripts/summarize_production_round.py" "$OUTPUT" \
    --audit-json "$REPORTS/exhaustive_audit.json" \
    --report-json "$REPORTS/round_audit_summary.json" \
    > "$REPORTS/round_summary.log" 2>&1
write_status complete_and_audited 0
