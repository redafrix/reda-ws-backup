#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
PY=/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python
OUTPUT="$WORKSPACE/outputs/final_seen_h10_round_000_seed20260730"
LOG="$WORKSPACE/logs/final_seen_h10_round_000_seed20260730.log"
STAGE_LOG="$WORKSPACE/logs/final_seen_h10_round_000_stage.log"
SESSION=simvla-risk-h10-final-seen-r000
STAGE="$WORKSPACE/scripts/run_final_seen_h10_round_000_stage.sh"
TEST_LOG="$WORKSPACE/logs/final_seen_h10_round_000_cpu_tests.log"
PREFLIGHT_REPORT="$WORKSPACE/reports/FINAL_SEEN_ROUND_000_PREFLIGHT.json"

usage() {
    printf 'Usage: %s preflight|start|resume|status|stop|logs|health\n' "$0"
}

require_no_competitors() {
    if pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*[t]rain_grad_accum.py' >/dev/null; then
        printf 'Refusing launch: pi0.5 training is active.\n' >&2
        exit 30
    fi
    if pgrep -af '[c]ollect_isaac_risk.py|[s]imvla_reaching_rollout.py' >/dev/null; then
        printf 'Refusing launch: another SimVLA/Isaac process is active.\n' >&2
        exit 31
    fi
    if tmux has-session -t "$SESSION" 2>/dev/null; then
        printf 'Refusing launch: tmux session already exists: %s\n' "$SESSION" >&2
        exit 32
    fi
}

run_preflight() {
    require_no_competitors
    if [[ -d "$OUTPUT" ]] && find "$OUTPUT" -mindepth 1 -print -quit | grep -q .; then
        printf 'Round 0 output is not empty: %s\n' "$OUTPUT" >&2
        exit 33
    fi
    free_bytes=$(df --output=avail -B1 /mnt/ai | tail -1 | tr -d ' ')
    if ((free_bytes < 100 * 1024 * 1024 * 1024)); then
        printf 'Less than 100 GiB is free on /mnt/ai.\n' >&2
        exit 34
    fi
    compute_processes=$(nvidia-smi \
        --query-compute-apps=pid,process_name,used_memory \
        --format=csv,noheader,nounits | sed '/^[[:space:]]*$/d' || true)
    if [[ -n "$compute_processes" ]]; then
        printf 'GPU compute process already active:\n%s\n' "$compute_processes" >&2
        exit 35
    fi

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$WORKSPACE/src" \
        "$PY" -m pytest -p no:cacheprovider -q "$WORKSPACE/tests" \
        > "$TEST_LOG" 2>&1
    test_count=$(sed -n 's/^\([0-9][0-9]*\) passed.*$/\1/p' "$TEST_LOG" | tail -1)
    [[ "${test_count:-0}" -ge 16 ]] || {
        cat "$TEST_LOG" >&2
        printf 'Expected at least 16 passing CPU tests.\n' >&2
        exit 36
    }
    "$PY" "$WORKSPACE/scripts/cpu_preflight.py" \
        > "$WORKSPACE/logs/final_seen_h10_round_000_source_preflight.log" 2>&1

    FREE_BYTES="$free_bytes" TEST_LOG="$TEST_LOG" TEST_COUNT="$test_count" OUTPUT="$OUTPUT" \
        "$PY" - "$PREFLIGHT_REPORT" <<'PY'
import hashlib
import json
import os
from pathlib import Path
import sys
import time

workspace = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
payload = {
    "pass": True,
    "generated_at_unix_s": time.time(),
    "cpu_tests": f"{os.environ['TEST_COUNT']}/{os.environ['TEST_COUNT']}",
    "cpu_test_log": os.environ["TEST_LOG"],
    "gpu_compute_processes": [],
    "pi05_training_active": False,
    "other_isaac_collector_active": False,
    "ssd_free_bytes": int(os.environ["FREE_BYTES"]),
    "output_dir": os.environ["OUTPUT"],
    "output_was_empty": True,
    "config_path": str(workspace / "configs/final_seen_h10_round_000_seed20260730.yaml"),
    "config_sha256": digest(workspace / "configs/final_seen_h10_round_000_seed20260730.yaml"),
    "manifest_path": str(workspace / "manifests/seen_4000_master.json"),
    "manifest_sha256": digest(workspace / "manifests/seen_4000_master.json"),
    "collector_sha256": digest(workspace / "scripts/collect_isaac_risk.py"),
}
destination = Path(sys.argv[1])
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
PY
    cat "$PREFLIGHT_REPORT"
}

launch_stage() {
    mkdir -p "$(dirname "$LOG")"
    touch "$LOG" "$STAGE_LOG"
    chmod 0644 "$LOG" "$STAGE_LOG"
    tmux new-session -d -s "$SESSION" \
        "bash -lc 'exec \"$STAGE\" >> \"$STAGE_LOG\" 2>&1'"
    printf 'TMUX_SESSION=%s\n' "$SESSION"
    printf 'COLLECTOR_LOG=%s\n' "$LOG"
    printf 'LIVE_STATUS=%s/live_status.json\n' "$OUTPUT"
    printf 'OUTPUT=%s\n' "$OUTPUT"
}

case "${1:-}" in
    preflight)
        run_preflight
        ;;
    start)
        run_preflight
        launch_stage
        ;;
    resume)
        require_no_competitors
        [[ -f "$OUTPUT/run_manifest.json" ]] || {
            printf 'No resumable Round 0 manifest: %s\n' "$OUTPUT/run_manifest.json" >&2
            exit 37
        }
        rm -f "$OUTPUT/STOP_AFTER_CURRENT_EPISODE"
        launch_stage
        ;;
    status)
        tmux has-session -t "$SESSION" 2>/dev/null \
            && printf 'TMUX_ACTIVE=YES\n' \
            || printf 'TMUX_ACTIVE=NO\n'
        pgrep -af '[c]ollect_isaac_risk.py' || true
        [[ -f "$OUTPUT/live_status.json" ]] && cat "$OUTPUT/live_status.json"
        [[ -f "$OUTPUT/reports/stage_status.json" ]] \
            && cat "$OUTPUT/reports/stage_status.json"
        printf 'COMMITTED_EPISODES=%s\n' "$(find "$OUTPUT/episodes" -mindepth 2 -maxdepth 2 -name COMMITTED 2>/dev/null | wc -l)"
        df -h /mnt/ai
        ;;
    stop)
        [[ -d "$OUTPUT" ]] || {
            printf 'Round output does not exist.\n' >&2
            exit 38
        }
        touch "$OUTPUT/STOP_AFTER_CURRENT_EPISODE"
        chmod 0644 "$OUTPUT/STOP_AFTER_CURRENT_EPISODE"
        printf 'Requested a clean stop after the current episode.\n'
        ;;
    logs)
        tail -n 100 -F "$LOG"
        ;;
    health)
        "$PY" "$WORKSPACE/scripts/check_round_health.py" \
            "$OUTPUT" \
            --collector-log "$LOG" \
            --report-json "$WORKSPACE/reports/FINAL_SEEN_ROUND_000_LAUNCH_HEALTH.json"
        ;;
    *)
        usage
        exit 2
        ;;
esac
