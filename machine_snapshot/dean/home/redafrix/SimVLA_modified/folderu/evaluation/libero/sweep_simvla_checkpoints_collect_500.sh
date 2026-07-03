#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Sweep SimVLA checkpoints and collect fixed rollout sets.
#
# Default episode count per checkpoint:
#   10 tasks * 5 seeds * 10 trials = 500 episodes
#
# Assumes run_libero_pro_eval.sh supports:
#   TASK_SUITE, TASK_ID, NUM_TRIALS, SEED, PORT, NO_VIDEO,
#   REPLAN_STEPS, UNCERTAINTY_LOG
# ============================================================

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"

NORM_STATS="${NORM_STATS:-${REPO_ROOT}/norm_stats/libero_norm.json}"
BASE_CKPT_DIR="${BASE_CKPT_DIR:-${REPO_ROOT}/runs/simvla_libero_uncertainty}"

# Checkpoints to sweep.
CHECKPOINTS="${CHECKPOINTS:-ckpt-60000 ckpt-50000 ckpt-30000 ckpt-20000 ckpt-10000}"

# Server config.
PORTS="${PORTS:-8111 8112 8113 8114 8115}"
GPU_IDS="${GPU_IDS:-${CUDA_VISIBLE_DEVICES:-0}}"
BASE_SEED="${BASE_SEED:-700}"
MAX_PARALLEL="${MAX_PARALLEL:-5}"
NUM_ACTION_SAMPLES="${NUM_ACTION_SAMPLES:-1}"

# Collection config.
TASK_SUITE="${TASK_SUITE:-libero_object_object}"
TASK_IDS="${TASK_IDS:-0 1 2 3 4 5 6 7 8 9}"
SEEDS="${SEEDS:-401 409 421 431 443}"
NUM_TRIALS="${NUM_TRIALS:-10}"
NO_VIDEO="${NO_VIDEO:-true}"
REPLAN_STEPS="${REPLAN_STEPS:-5}"
FORCE_LIBERO_PRO_REGEN="${FORCE_LIBERO_PRO_REGEN:-false}"

RUN_GROUP="${RUN_GROUP:-phase2_tdqc_ckpt_sweep_500eps_$(date +%Y%m%d_%H%M%S)}"
OUT_ROOT="${OUT_ROOT:-${EVAL_DIR}/eval_libero_pro/${RUN_GROUP}}"

SERVER_READY_TIMEOUT_SEC="${SERVER_READY_TIMEOUT_SEC:-900}"

read -r -a PORT_ARRAY <<< "${PORTS}"

mkdir -p "${OUT_ROOT}"
cd "${EVAL_DIR}"

MASTER_LOG="${OUT_ROOT}/sweep_master.log"
: > "${MASTER_LOG}"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "${MASTER_LOG}"
}

count_expected() {
  local n_tasks n_seeds
  n_tasks=$(wc -w <<< "${TASK_IDS}")
  n_seeds=$(wc -w <<< "${SEEDS}")
  echo $((n_tasks * n_seeds * NUM_TRIALS))
}

ckpt_label() {
  basename "$1" | sed 's/[^A-Za-z0-9_.-]/_/g'
}

port_is_open() {
  local port="$1"
  python - "$port" <<'PY'
import socket
import sys

port = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1.0)
try:
    s.connect(("127.0.0.1", port))
    sys.exit(0)
except Exception:
    sys.exit(1)
finally:
    s.close()
PY
}

wait_for_servers() {
  local start_t now elapsed
  start_t=$(date +%s)

  log "Waiting for servers on ports: ${PORTS}"

  while true; do
    local ready=0
    for p in ${PORTS}; do
      if port_is_open "${p}"; then
        ready=$((ready + 1))
      fi
    done

    if [ "${ready}" -eq "${#PORT_ARRAY[@]}" ]; then
      log "All ${ready}/${#PORT_ARRAY[@]} servers are ready."
      return 0
    fi

    now=$(date +%s)
    elapsed=$((now - start_t))

    if [ "${elapsed}" -gt "${SERVER_READY_TIMEOUT_SEC}" ]; then
      log "[ERROR] Timeout waiting for servers. Ready ${ready}/${#PORT_ARRAY[@]}."
      return 1
    fi

    log "Servers ready: ${ready}/${#PORT_ARRAY[@]} ..."
    sleep 10
  done
}

stop_servers() {
  log "Stopping SimVLA servers on ports: ${PORTS}"

  # Kill server processes that use the selected ports.
  for p in ${PORTS}; do
    pkill -f "serve_smolvlm_libero.py.*--port ${p}" || true
  done

  # Also kill possible parent launcher processes.
  pkill -f "start_multi_smolvlm_servers.sh" || true

  sleep 5

  for p in ${PORTS}; do
    if port_is_open "${p}"; then
      log "[WARNING] Port ${p} still appears open after stop."
    fi
  done
}

start_servers_for_checkpoint() {
  local ckpt_path="$1"
  local label="$2"
  local server_log_dir="${OUT_ROOT}/${label}/server_logs"

  mkdir -p "${server_log_dir}"

  log "Starting servers for checkpoint: ${ckpt_path}"
  log "Server logs: ${server_log_dir}"

  PORTS="${PORTS}" \
  GPU_IDS="${GPU_IDS}" \
  BASE_SEED="${BASE_SEED}" \
  NUM_ACTION_SAMPLES="${NUM_ACTION_SAMPLES}" \
  CHECKPOINT="${ckpt_path}" \
  NORM_STATS="${NORM_STATS}" \
  SERVER_LOG_DIR="${server_log_dir}" \
  ./start_multi_smolvlm_servers.sh > "${server_log_dir}/start_multi_stdout.log" 2>&1 &

  echo "$!" > "${server_log_dir}/start_multi_pid.txt"

  wait_for_servers
}

run_one_eval() {
  local ckpt_out_dir="$1"
  local task_id="$2"
  local seed="$3"
  local port="$4"

  local jsonl="${ckpt_out_dir}/${TASK_SUITE}_task${task_id}_seed${seed}_${NUM_TRIALS}trials.jsonl"
  local run_log="${ckpt_out_dir}/${TASK_SUITE}_task${task_id}_seed${seed}_${NUM_TRIALS}trials.log"
  local status="${ckpt_out_dir}/${TASK_SUITE}_task${task_id}_seed${seed}_${NUM_TRIALS}trials.status"

  rm -f "${jsonl}" "${status}"

  (
    set +e

    TASK_SUITE="${TASK_SUITE}" \
    TASK_ID="${task_id}" \
    NUM_TRIALS="${NUM_TRIALS}" \
    SEED="${seed}" \
    PORT="${port}" \
    NO_VIDEO="${NO_VIDEO}" \
    REPLAN_STEPS="${REPLAN_STEPS}" \
    FORCE_LIBERO_PRO_REGEN="${FORCE_LIBERO_PRO_REGEN}" \
    UNCERTAINTY_LOG="${jsonl}" \
    ./run_libero_pro_eval.sh > "${run_log}" 2>&1

    rc=$?
    echo "${rc}" > "${status}"
    exit 0
  ) &
}

merge_and_validate_checkpoint() {
  local ckpt_out_dir="$1"
  local combined="${ckpt_out_dir}/combined_${TASK_SUITE}_all_seeds.jsonl"
  local summary="${ckpt_out_dir}/collection_summary.json"

  : > "${combined}"

  python - "${ckpt_out_dir}" "${combined}" "${summary}" <<'PY'
import json
import sys
from pathlib import Path
from collections import Counter

out_dir = Path(sys.argv[1])
combined = Path(sys.argv[2])
summary_path = Path(sys.argv[3])

status_files = sorted(out_dir.glob("*.status"))

summary = {
    "jobs": 0,
    "jobs_ok": 0,
    "jobs_failed": 0,
    "jobs_empty": 0,
    "raw_lines": 0,
    "valid_episodes": 0,
    "bad_json": 0,
    "empty_trace": 0,
    "missing_denoise": 0,
    "success": 0,
    "failure": 0,
    "by_task": {},
    "failed_jobs": [],
    "empty_jobs": [],
}

denoise_keys = [
    "denoise_initial_mean",
    "denoise_final_mean",
    "denoise_delta",
    "denoise_slope",
    "denoise_final_max",
    "denoise_spike",
    "denoise_final_gripper",
    "denoise_final_rotation_mean",
]

by_task = Counter()
by_task_success = Counter()

with combined.open("w", encoding="utf-8") as out:
    for status in status_files:
        summary["jobs"] += 1
        stem = status.with_suffix("")
        jsonl = Path(str(stem) + ".jsonl")
        log = Path(str(stem) + ".log")

        rc = status.read_text().strip()
        if rc == "0":
            summary["jobs_ok"] += 1
        else:
            summary["jobs_failed"] += 1
            summary["failed_jobs"].append({"status": str(status), "rc": rc, "log": str(log)})

        if not jsonl.exists() or jsonl.stat().st_size == 0:
            summary["jobs_empty"] += 1
            summary["empty_jobs"].append(str(jsonl))
            continue

        with jsonl.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue

                summary["raw_lines"] += 1

                try:
                    rec = json.loads(line)
                except Exception:
                    summary["bad_json"] += 1
                    continue

                trace = rec.get("uncertainty_trace") or []
                if not trace:
                    summary["empty_trace"] += 1
                    continue

                if any(k not in trace[0] or trace[0][k] is None for k in denoise_keys):
                    summary["missing_denoise"] += 1
                    continue

                summary["valid_episodes"] += 1
                s = bool(rec.get("success"))
                summary["success"] += int(s)
                summary["failure"] += int(not s)

                task_id = str(rec.get("task_id", "unknown"))
                by_task[task_id] += 1
                by_task_success[task_id] += int(s)

                out.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")

summary["by_task"] = {
    task: {
        "episodes": by_task[task],
        "success": by_task_success[task],
        "failure": by_task[task] - by_task_success[task],
    }
    for task in sorted(by_task, key=lambda x: int(x) if str(x).isdigit() else x)
}

summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

print(json.dumps(summary, indent=2))
PY
}

collect_for_checkpoint() {
  local ckpt_path="$1"
  local label="$2"
  local ckpt_out_dir="${OUT_ROOT}/${label}"
  local expected
  expected=$(count_expected)

  mkdir -p "${ckpt_out_dir}"

  log "============================================================"
  log "Collecting checkpoint: ${label}"
  log "Checkpoint path: ${ckpt_path}"
  log "Output dir: ${ckpt_out_dir}"
  log "TASK_SUITE=${TASK_SUITE}"
  log "TASK_IDS=${TASK_IDS}"
  log "SEEDS=${SEEDS}"
  log "NUM_TRIALS=${NUM_TRIALS}"
  log "Expected episodes if all jobs complete: ${expected}"
  log "============================================================"

  local active=0
  local job_idx=0

  for seed in ${SEEDS}; do
    for task_id in ${TASK_IDS}; do
      local port="${PORT_ARRAY[$((job_idx % ${#PORT_ARRAY[@]}))]}"

      log "Launching task=${task_id}, seed=${seed}, trials=${NUM_TRIALS}, port=${port}"
      run_one_eval "${ckpt_out_dir}" "${task_id}" "${seed}" "${port}"

      active=$((active + 1))
      job_idx=$((job_idx + 1))

      if [ "${active}" -ge "${MAX_PARALLEL}" ]; then
        wait -n
        active=$((active - 1))
      fi
    done
  done

  wait

  log "Merging and validating checkpoint: ${label}"
  merge_and_validate_checkpoint "${ckpt_out_dir}"

  log "Finished checkpoint: ${label}"
}

main() {
  log "Starting checkpoint sweep"
  log "OUT_ROOT=${OUT_ROOT}"
  log "CHECKPOINTS=${CHECKPOINTS}"

  for ckpt in ${CHECKPOINTS}; do
    if [[ "${ckpt}" = /* ]]; then
      ckpt_path="${ckpt}"
    else
      ckpt_path="${BASE_CKPT_DIR}/${ckpt}"
    fi

    label="$(ckpt_label "${ckpt_path}")"

    if [ ! -e "${ckpt_path}" ]; then
      log "[ERROR] Checkpoint does not exist: ${ckpt_path}"
      exit 1
    fi

    stop_servers

    start_servers_for_checkpoint "${ckpt_path}" "${label}"

    collect_for_checkpoint "${ckpt_path}" "${label}"

    stop_servers
  done

  log "All checkpoint sweeps finished."
  log "Results root: ${OUT_ROOT}"
}

main "$@"
