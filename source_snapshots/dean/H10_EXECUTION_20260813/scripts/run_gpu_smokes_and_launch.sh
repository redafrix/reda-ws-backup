#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
RUNNER="$WORKSPACE/scripts/run_collector.sh"
VALIDATOR="$WORKSPACE/scripts/validate_collection_output.py"
VERIFY=/mnt/ai/projects/simvla_reproduction_workspace/verify-softplus-setup.sh
SEEN_CONFIG="$WORKSPACE/configs/seen_smoke.yaml"
PROD_CONFIG="$WORKSPACE/configs/seen_chunk_h10_4000.yaml"
SEEN_MANIFEST="$WORKSPACE/manifests/seen_4000_master.json"
OOD_CONFIG="$WORKSPACE/configs/ood_schema_smoke.yaml"
OOD_MANIFEST=/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab/configs/benchmarks/reaching_train_ood150/full_ood.json
SMOKE_ROOT="$WORKSPACE/smokes"
LOG_ROOT="$WORKSPACE/logs"
REPORT_ROOT="$WORKSPACE/reports"
COLLECTION_OUTPUT="$WORKSPACE/outputs/seen_chunk_h10_4000"
COLLECTION_LOG="$LOG_ROOT/seen_chunk_h10_4000.log"
COLLECTION_SESSION=simvla-risk-seen-4000

mkdir -p "$SMOKE_ROOT" "$LOG_ROOT" "$REPORT_ROOT" "$WORKSPACE/outputs"
exec > >(tee -a "$LOG_ROOT/gpu_smoke_pipeline.log") 2>&1

trainer_active() {
    pgrep -af '/mnt/ai/pi05/openpi/.venv/bin/python.*train_grad_accum.py' >/dev/null
}

rollout_active() {
    pgrep -af '[s]imvla_reaching_rollout.py|[c]ollect_isaac_risk.py' >/dev/null
}

fail() {
    printf '[%s] GPU smoke pipeline failed: %s\n' "$(date -Is)" "$*" >&2
    cat > "$REPORT_ROOT/GPU_SMOKE_REPORT.md" <<EOF
# GPU Smoke Report

Status: **FAIL**

- Time: $(date -Is)
- Failure: $*
- Log: \`$LOG_ROOT/gpu_smoke_pipeline.log\`
- No production collection was launched by this failed run.
EOF
    exit 1
}

trainer_active && fail "pi0.5 trainer is still active"
rollout_active && fail "another Isaac/SimVLA process is active"

printf '[%s] Verifying package and pinned worktrees.\n' "$(date -Is)"
"$VERIFY" > "$LOG_ROOT/packaged_setup_verifier.log" 2>&1 ||
    fail "packaged setup verifier failed"

SIMVLA_HEAD="$(git -C /mnt/ai/projects/simvla_reproduction_workspace/SimVLA rev-parse HEAD)"
ISAAC_HEAD="$(git -C /mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab rev-parse HEAD)"
[[ "$SIMVLA_HEAD" == ee1294a17e723b21051f4f4434508ead30a69044 ]] ||
    fail "pinned SimVLA commit changed"
[[ "$ISAAC_HEAD" == 9ae798c143fcb2a20e324aea06c0d10b159af502 ]] ||
    fail "pinned Isaac commit changed"
[[ -z "$(git -C /mnt/ai/projects/simvla_reproduction_workspace/SimVLA status --porcelain)" ]] ||
    fail "pinned SimVLA worktree is dirty"
[[ -z "$(git -C /mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab status --porcelain)" ]] ||
    fail "pinned Isaac worktree is dirty"

GPU_QUERY="$(
    nvidia-smi --query-gpu=name,memory.total,memory.free,temperature.gpu \
        --format=csv,noheader,nounits
)" || fail "nvidia-smi GPU query failed"
FREE_MIB="$(printf '%s\n' "$GPU_QUERY" | awk -F, 'NR==1 {gsub(/ /, "", $3); print $3}')"
[[ "$FREE_MIB" =~ ^[0-9]+$ ]] || fail "could not parse free VRAM"
((FREE_MIB >= 28000)) || fail "less than 28000 MiB GPU memory is free"
COMPUTE_PROCESSES="$(
    nvidia-smi --query-compute-apps=pid,process_name \
        --format=csv,noheader 2>/dev/null || true
)"
[[ -z "$COMPUTE_PROCESSES" ]] ||
    fail "a CUDA compute process is already active: $COMPUTE_PROCESSES"

run_smoke() {
    local name="$1"
    local output="$2"
    shift 2
    local marker="$output/SMOKE_VALIDATED"
    local log="$LOG_ROOT/${name}.log"
    local time_log="$LOG_ROOT/${name}.time.txt"
    local gpu_log="$LOG_ROOT/${name}.gpu_memory_mib.txt"
    local metrics="$output/smoke_metrics.json"
    local start_s
    local end_s
    local elapsed_s
    local command_pid
    local monitor_pid
    local rc

    if [[ -f "$marker" ]]; then
        printf '[%s] Reusing validated smoke: %s\n' "$(date -Is)" "$name"
        return
    fi
    rm -rf "$output"
    mkdir -p "$output"
    printf '[%s] Starting smoke: %s\n' "$(date -Is)" "$name"
    start_s="$(date +%s)"
    set +e
    /usr/bin/time -v -o "$time_log" \
        timeout --signal=INT --kill-after=90s 3600s \
        "$RUNNER" "$@" > "$log" 2>&1 &
    command_pid=$!
    (
        while kill -0 "$command_pid" 2>/dev/null; do
            nvidia-smi --query-compute-apps=used_memory \
                --format=csv,noheader,nounits 2>/dev/null |
                awk '{sum += $1} END {print sum + 0}'
            sleep 2
        done
    ) > "$gpu_log" &
    monitor_pid=$!
    wait "$command_pid"
    rc=$?
    wait "$monitor_pid" 2>/dev/null || true
    set -e
    ((rc == 0)) || fail "$name failed with exit $rc; inspect $log"
    if grep -Eq '^Traceback \(most recent call last\):|Segmentation fault|CUDA error' "$log"; then
        fail "$name emitted a fatal runtime error despite exit $rc; inspect $log"
    fi
    end_s="$(date +%s)"
    elapsed_s=$((end_s - start_s))
    python3 - "$name" "$output" "$elapsed_s" "$time_log" "$gpu_log" "$metrics" <<'PY'
import json
import sys
from pathlib import Path

name, output, elapsed, time_log, gpu_log, destination = sys.argv[1:]
output = Path(output)
rows = 0
for path in output.glob("episodes/*/risk_rows.jsonl"):
    rows += len(path.read_text().splitlines())
rss_kib = None
for line in Path(time_log).read_text().splitlines():
    if "Maximum resident set size (kbytes)" in line:
        rss_kib = int(line.rsplit(":", 1)[1].strip())
gpu_values = [
    int(line.strip())
    for line in Path(gpu_log).read_text().splitlines()
    if line.strip().isdigit()
]
payload = {
    "smoke": name,
    "elapsed_seconds": int(elapsed),
    "decision_rows": rows,
    "decision_rows_per_second": rows / max(int(elapsed), 1),
    "peak_host_rss_kib": rss_kib,
    "peak_compute_memory_mib": max(gpu_values, default=0),
}
Path(destination).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps(payload, sort_keys=True))
PY
}

INFERENCE_OUT="$SMOKE_ROOT/01_inference_only"
run_smoke inference_only "$INFERENCE_OUT" \
    --run-config "$SEEN_CONFIG" \
    --manifest "$SEEN_MANIFEST" \
    --output-dir "$INFERENCE_OUT" \
    --offset 0 --count 1 \
    --execution-mode chunk_h10 \
    --inference-only \
    --viz none --device cuda:0
python3 - "$INFERENCE_OUT/live_status.json" <<'PY' ||
import json
import sys
from pathlib import Path

status = json.loads(Path(sys.argv[1]).read_text())
assert status["inference_only"] is True
assert status["nine_seeds_unique"] is True
assert status["main_chunk_shape"] == [10, 7]
assert status["ace_chunk_shape"] == [8, 10, 7]
assert status["uncertainty_shape"] == [49]
assert status["vlm_encoding_count"] == 1
assert status["candidate0_single_runtime_parity"] is True
assert float(status["single_runtime_parity_max_abs"]) <= 1e-5
print("INFERENCE_ONLY_OBSERVATION=PASS")
print("CANDIDATE0_SINGLE_RUNTIME_PARITY=PASS")
print(f"CANDIDATE0_MAX_ABS={status['single_runtime_parity_max_abs']}")
PY
    fail "inference-only status or candidate-0 parity failed"
touch "$INFERENCE_OUT/SMOKE_VALIDATED"

CHUNK_OUT="$SMOKE_ROOT/02_seen_chunk_h10"
run_smoke seen_chunk_h10 "$CHUNK_OUT" \
    --run-config "$SEEN_CONFIG" \
    --manifest "$SEEN_MANIFEST" \
    --output-dir "$CHUNK_OUT" \
    --offset 1 --count 1 \
    --execution-mode chunk_h10 \
    --save-video \
    --viz none --device cuda:0
python3 "$VALIDATOR" "$CHUNK_OUT" --require-episodes 1 --require-video \
    --expected-mode chunk_h10 --expected-risk-split train ||
    fail "seen chunk_h10 output validation failed"
touch "$CHUNK_OUT/SMOKE_VALIDATED"

RECEDING_OUT="$SMOKE_ROOT/03_seen_chunk_h10"
run_smoke seen_chunk_h10 "$RECEDING_OUT" \
    --run-config "$SEEN_CONFIG" \
    --manifest "$SEEN_MANIFEST" \
    --output-dir "$RECEDING_OUT" \
    --offset 2 --count 1 \
    --execution-mode chunk_h10 \
    --save-video \
    --viz none --device cuda:0
python3 "$VALIDATOR" "$RECEDING_OUT" --require-episodes 1 --require-video \
    --expected-mode chunk_h10 --expected-risk-split train ||
    fail "seen chunk_h10 output validation failed"
touch "$RECEDING_OUT/SMOKE_VALIDATED"

OOD_OUT="$SMOKE_ROOT/04_ood_schema"
run_smoke ood_schema "$OOD_OUT" \
    --run-config "$OOD_CONFIG" \
    --manifest "$OOD_MANIFEST" \
    --output-dir "$OOD_OUT" \
    --offset 0 --count 1 \
    --execution-mode chunk_h10 \
    --save-video \
    --viz none --device cuda:0
python3 "$VALIDATOR" "$OOD_OUT" --require-episodes 1 --require-video \
    --expected-mode chunk_h10 --expected-risk-split ood_smoke ||
    fail "OOD schema output validation failed"
touch "$OOD_OUT/SMOKE_VALIDATED"

cat > "$REPORT_ROOT/GPU_SMOKE_REPORT.md" <<EOF
# GPU Smoke Report

Status: **PASS**

- Completed: $(date -Is)
- GPU snapshot: \`$GPU_QUERY\`
- Inference-only observation: PASS
- Candidate-0 parity: PASS
- Seen chunk_h10 episode: PASS
- Seen chunk_h10 episode: PASS
- Fixed OOD schema-only episode: PASS
- OOD training/calibration eligibility: false
- Per-smoke timing/RSS/VRAM/throughput: \`$SMOKE_ROOT/*/smoke_metrics.json\`
- Logs: \`$LOG_ROOT\`
- Smoke outputs: \`$SMOKE_ROOT\`

GPU_SMOKES_PASS=YES
EOF

if tmux has-session -t "$COLLECTION_SESSION" 2>/dev/null; then
    printf '[%s] Production collection session already exists.\n' "$(date -Is)"
else
    tmux new-session -d -s "$COLLECTION_SESSION" \
        "bash -lc 'exec \"$RUNNER\" \
        --run-config \"$PROD_CONFIG\" \
        --manifest \"$SEEN_MANIFEST\" \
        --output-dir \"$COLLECTION_OUTPUT\" \
        --offset 0 --count 4000 \
        --execution-mode chunk_h10 \
        --viz none --device cuda:0 \
        >> \"$COLLECTION_LOG\" 2>&1'"
fi

sleep 120
if ! tmux has-session -t "$COLLECTION_SESSION" 2>/dev/null; then
    fail "production collection tmux session exited during health check"
fi
trainer_active && fail "pi0.5 trainer reappeared after collection launch"

cat > "$REPORT_ROOT/COLLECTION_PREFLIGHT_REPORT.md" <<EOF
# Collection Preflight Report

Status: **PASS AND LAUNCHED**

- Completed: $(date -Is)
- Session: \`$COLLECTION_SESSION\`
- Command launcher: \`$RUNNER\`
- Manifest: \`$SEEN_MANIFEST\`
- Manifest SHA-256: \`$(sha256sum "$SEEN_MANIFEST" | awk '{print $1}')\`
- Output: \`$COLLECTION_OUTPUT\`
- Log: \`$COLLECTION_LOG\`
- Status: \`$COLLECTION_OUTPUT/live_status.json\`
- Execution mode: \`chunk_h10\`
- Declared cap: 4,000 seen-distribution episodes
- Videos: disabled
- Fixed OOD-150 used for training: NO
- Fixed OOD-150 used for calibration: NO

COLLECTION_PREFLIGHT=PASS
FULL_COLLECTION_LAUNCHED=YES
EOF

printf '[%s] Collection launched in tmux session %s.\n' \
    "$(date -Is)" "$COLLECTION_SESSION"
