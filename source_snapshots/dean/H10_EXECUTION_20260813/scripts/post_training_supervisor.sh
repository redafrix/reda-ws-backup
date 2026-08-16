#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
LOG="$WORKSPACE/logs/post_training_supervisor.log"
PIPELINE="$WORKSPACE/scripts/run_gpu_smokes_and_launch.sh"
TRAIN_LOG=/mnt/ai/pi05/training/reaching_pose_v1_4400_pi05_fullpose_v3/logs/production_v1.log
TRAIN_UNIT=pi05-franka-fullpose-v3-stock-train.service

mkdir -p "$WORKSPACE/logs" "$WORKSPACE/reports"
exec >> "$LOG" 2>&1

trainer_active() {
    pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*train_grad_accum.py' >/dev/null
}

printf '[%s] Supervisor started; no CUDA/Isaac import will occur while training runs.\n' \
    "$(date -Is)"

while trainer_active; do
    metric="$(
        tr -d '\000\r' < "$TRAIN_LOG" 2>/dev/null |
            grep 'TRAIN_METRICS_JSON=' |
            tail -1 || true
    )"
    printf '[%s] pi0.5 active; waiting 300 seconds. %s\n' \
        "$(date -Is)" "$metric"
    sleep 300
done

printf '[%s] Trainer process is absent; confirming stable natural completion.\n' \
    "$(date -Is)"
sleep 120
if trainer_active; then
    printf '[%s] Trainer reappeared; returning to wait loop by restarting supervisor.\n' \
        "$(date -Is)"
    exec "$0"
fi

UNIT_STATE="$(
    systemctl --user show "$TRAIN_UNIT" \
        --property=ActiveState,Result,ExecMainStatus 2>&1 || true
)"
printf '[%s] Training unit state:\n%s\n' "$(date -Is)" "$UNIT_STATE"
if grep -q '^Result=failed$' <<<"$UNIT_STATE"; then
    printf '[%s] Training unit failed; GPU smokes will not start automatically.\n' \
        "$(date -Is)"
    cat > "$WORKSPACE/reports/COLLECTION_PREFLIGHT_REPORT.md" <<EOF
# Collection Preflight Report

Status: **BLOCKED**

The pi0.5 trainer disappeared with a failed systemd unit. GPU smokes and collection
were not launched.

\`\`\`text
$UNIT_STATE
\`\`\`

FULL_COLLECTION_LAUNCHED=NO
EOF
    exit 40
fi

FINAL_METRIC="$(
    tr -d '\000\r' < "$TRAIN_LOG" 2>/dev/null |
        grep 'TRAIN_METRICS_JSON=' |
        tail -1 || true
)"
FINAL_STEP="$(
    python3 - "$FINAL_METRIC" <<'PY'
import json
import sys

line = sys.argv[1]
prefix = "TRAIN_METRICS_JSON="
if prefix not in line:
    print(-1)
else:
    print(int(json.loads(line.split(prefix, 1)[1])["optimizer_step"]))
PY
)"
printf '[%s] Final logged pi0.5 optimizer step: %s\n' "$(date -Is)" "$FINAL_STEP"
if ((FINAL_STEP < 30000)); then
    printf '[%s] Training did not reach 30,000 updates; GPU smokes remain blocked.\n' \
        "$(date -Is)"
    cat > "$WORKSPACE/reports/COLLECTION_PREFLIGHT_REPORT.md" <<EOF
# Collection Preflight Report

Status: **BLOCKED**

The pi0.5 process ended without a failed unit, but the final logged optimizer
step was only $FINAL_STEP. The supervisor requires the natural 30,000-update
completion before starting GPU smokes.

FULL_COLLECTION_LAUNCHED=NO
EOF
    exit 41
fi

printf '[%s] Starting guarded GPU smoke pipeline.\n' "$(date -Is)"
exec "$PIPELINE"
