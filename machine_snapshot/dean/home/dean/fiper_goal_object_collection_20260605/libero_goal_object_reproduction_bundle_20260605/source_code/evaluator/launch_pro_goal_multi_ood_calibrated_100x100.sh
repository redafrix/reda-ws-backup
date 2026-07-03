#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-${ROOT_DIR}/model/.venv/bin/python}"
LOG_DIR="${LOG_DIR:-${ROOT_DIR}/logs}"
TIMESTAMP="${TIMESTAMP:-$(date +%Y%m%d_%H%M%S)}"

PROTOCOL_JSON="${PROTOCOL_JSON:-${ROOT_DIR}/configs/uq_benchmarks/libero_goal_multi_ood_calibrated_100s100f_trials0to9_40to49_20260604.json}"
TASK_IDS="${TASK_IDS:-0-9}"
TRIAL_WINDOWS="${TRIAL_WINDOWS:-0:10,40:10}"
MAX_EPISODE_STEPS="${MAX_EPISODE_STEPS:-250}"
SEED="${SEED:-0}"
SELECTION_SEED="${SELECTION_SEED:-20260604}"
HEAD_KIND="${HEAD_KIND:-modeb10}"
CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
VALIDATE_ONLY="${VALIDATE_ONLY:-0}"
PRECOMPUTE_EMBEDDINGS="${PRECOMPUTE_EMBEDDINGS:-0}"
RUN_SUFFIX_PREFIX="${RUN_SUFFIX_PREFIX:-pgcal100_${TIMESTAMP}}"

PER_WINDOW_SUCCESS_TARGET="${PER_WINDOW_SUCCESS_TARGET:-0}"
PER_WINDOW_FAILURE_TARGET="${PER_WINDOW_FAILURE_TARGET:-0}"
BALANCED_TARGET_EPISODES_PER_CLASS="${BALANCED_TARGET_EPISODES_PER_CLASS:-100}"
MIN_BALANCED_EPISODES_PER_CLASS="${MIN_BALANCED_EPISODES_PER_CLASS:-100}"
MAX_EPISODES_PER_SUITE_PER_CLASS="${MAX_EPISODES_PER_SUITE_PER_CLASS:-50}"

BALANCED_PARENT_DIR="${BALANCED_PARENT_DIR:-${ROOT_DIR}/results/balanced_heldout_sets}"
BALANCED_DIR="${BALANCED_DIR:-${BALANCED_PARENT_DIR}/pro_goal_multi_ood_calibrated_100s_100f_${TIMESTAMP}}"

CURRENT_MULTI_OOD_DIR_GLOB="${CURRENT_MULTI_OOD_DIR_GLOB:-${ROOT_DIR}/results/*pgmod200_20260604_124716*}"
PREVIOUS_PRO_OBJECT_DIR="${PREVIOUS_PRO_OBJECT_DIR:-${ROOT_DIR}/results/w2a_libero_goal_half_v2w_libero_goal_agentview_lora_rank256_lr1.778e-04_bsz32_iter_000007020_fused_lr1.000e-04_layer20_bsz128_iter_000050022_step2_stopafter0_execute14_uqK8_w2ab4_wuqK3_v2wuq_pro_goal_object_ood_test100_pool_t10to39_20260604_115848/libero_goal_object}"

cd "${ROOT_DIR}"
mkdir -p "${LOG_DIR}" "${BALANCED_PARENT_DIR}"

require_file() {
  local path="$1"
  if [[ ! -f "${path}" ]]; then
    echo "Missing required file: ${path}" >&2
    exit 1
  fi
}

require_gpu() {
  if ! command -v nvidia-smi >/dev/null 2>&1; then
    if [[ "${VALIDATE_ONLY}" == "1" ]]; then
      echo "VALIDATE_ONLY=1: skipping GPU availability check because nvidia-smi is not installed."
      return
    fi
    echo "nvidia-smi is required for local GPU collection." >&2
    exit 1
  fi
  local count
  if ! count="$(nvidia-smi -L | wc -l)"; then
    if [[ "${VALIDATE_ONLY}" == "1" ]]; then
      echo "VALIDATE_ONLY=1: skipping GPU availability check because nvidia-smi failed."
      return
    fi
    echo "nvidia-smi failed; GPU collection cannot start." >&2
    exit 1
  fi
  if (( count < 1 )); then
    echo "Expected at least 1 visible GPU, found ${count}." >&2
    exit 1
  fi
}

validate_protocol() {
  "${PYTHON}" - "${PROTOCOL_JSON}" <<'PY'
import json
import os
import pathlib
import sys

protocol = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
expected_suites = ["libero_goal_swap", "libero_goal_object", "libero_goal_task", "libero_goal_lan"]
actual_suites = [row["task_suite_name"] for row in protocol["suites"]]
if actual_suites != expected_suites:
    raise SystemExit(f"Suite order mismatch: expected {expected_suites}, got {actual_suites}")

def parse_task_ids(spec: str) -> list[int]:
    ids = []
    for part in spec.split(","):
        token = part.strip()
        if not token:
            continue
        if "-" in token:
            start, end = token.split("-", 1)
            ids.extend(range(int(start), int(end) + 1))
        else:
            ids.append(int(token))
    return ids

runtime = protocol["runtime"]
candidate_spec = protocol["candidate_episode_spec"]
selection = protocol["selection"]
checks = {
    "TASK_IDS": parse_task_ids(os.environ["TASK_IDS"]),
    "TRIAL_WINDOWS": os.environ["TRIAL_WINDOWS"],
    "MAX_EPISODE_STEPS": int(os.environ["MAX_EPISODE_STEPS"]),
    "SEED": int(os.environ["SEED"]),
    "SELECTION_SEED": int(os.environ["SELECTION_SEED"]),
    "BALANCED_TARGET_EPISODES_PER_CLASS": int(os.environ["BALANCED_TARGET_EPISODES_PER_CLASS"]),
    "MIN_BALANCED_EPISODES_PER_CLASS": int(os.environ["MIN_BALANCED_EPISODES_PER_CLASS"]),
    "MAX_EPISODES_PER_SUITE_PER_CLASS": int(os.environ["MAX_EPISODES_PER_SUITE_PER_CLASS"]),
}
expected = {
    "TASK_IDS": candidate_spec["task_ids"],
    "TRIAL_WINDOWS": ",".join(
        f"{row['trial_start_index']}:{row['num_trials_per_task']}" for row in runtime["trial_windows"]
    ),
    "MAX_EPISODE_STEPS": runtime["max_episode_steps"],
    "SEED": candidate_spec["eval_seed"],
    "SELECTION_SEED": selection["selection_seed"],
    "BALANCED_TARGET_EPISODES_PER_CLASS": selection["target_successes"],
    "MIN_BALANCED_EPISODES_PER_CLASS": selection["min_episodes_per_class"],
    "MAX_EPISODES_PER_SUITE_PER_CLASS": selection["max_episodes_per_suite_per_class"],
}
for key, expected_value in expected.items():
    actual = checks[key]
    if actual != expected_value:
        raise SystemExit(f"Protocol/env mismatch for {key}: expected {expected_value!r}, got {actual!r}")
trial_indices = candidate_spec["initial_state_indices"]
expected_trial_indices = []
for window in runtime["trial_windows"]:
    start = window["trial_start_index"]
    count = window["num_trials_per_task"]
    end = window["trial_end_index"]
    if end != start + count - 1:
        raise SystemExit(f"Invalid trial window: {window}")
    expected_trial_indices.extend(range(start, end + 1))
if trial_indices != expected_trial_indices:
    raise SystemExit(
        f"Protocol initial_state_indices mismatch: expected {expected_trial_indices}, got {trial_indices}"
    )
expected_candidates = len(actual_suites) * len(candidate_spec["task_ids"]) * len(trial_indices)
if candidate_spec["total_candidates"] != expected_candidates:
    raise SystemExit(
        f"Protocol total_candidates mismatch: expected {expected_candidates}, "
        f"got {candidate_spec['total_candidates']}"
    )
print(f"validated calibrated protocol: suites={actual_suites}; candidates={expected_candidates}")
PY
}

suite_tag() {
  case "$1" in
    libero_goal_swap) echo "swap" ;;
    libero_goal_object) echo "object" ;;
    libero_goal_task) echo "task" ;;
    libero_goal_lan) echo "lan" ;;
    *)
      echo "Unknown suite: $1" >&2
      exit 1
      ;;
  esac
}

find_result_dir() {
  local suite_name="$1"
  local run_suffix="$2"
  "${PYTHON}" - "${ROOT_DIR}" "${suite_name}" "${run_suffix}" <<'PY'
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
suite_name = sys.argv[2]
suffix = sys.argv[3]
matches = sorted(root.glob(f"results/*{suffix}/{suite_name}/episode_outcomes.jsonl"))
if len(matches) != 1:
    raise SystemExit(f"Expected one result directory for suite={suite_name} suffix={suffix!r}, found {len(matches)}")
print(matches[0].parent)
PY
}

parse_trial_windows() {
  "${PYTHON}" - "${TRIAL_WINDOWS}" <<'PY'
import sys

for raw in sys.argv[1].split(","):
    token = raw.strip()
    if not token:
        continue
    start, count = token.split(":", 1)
    print(f"{int(start)} {int(count)}")
PY
}

run_suite_collection() {
  local suite_name="$1"
  local window_start="$2"
  local window_count="$3"
  local tag
  tag="$(suite_tag "${suite_name}")"
  local window_end=$((window_start + window_count - 1))
  local run_suffix="${RUN_SUFFIX_PREFIX}_${tag}_t${window_start}to${window_end}"

  export CUDA_VISIBLE_DEVICES
  export OOD_IMPL=pro
  export TASK_SUITE_NAME="${suite_name}"
  export TASK_IDS
  export TRIAL_START_INDEX="${window_start}"
  export NUM_TRIALS_PER_TASK="${window_count}"
  export MAX_EPISODE_STEPS
  export SEED
  export HEAD_KIND
  export RUN_SUFFIX="${run_suffix}"
  export VALIDATE_ONLY
  export PROMPT_SOURCE=bddl_language
  export SAVE_VIDEOS=0
  export PRECOMPUTE_EMBEDDINGS
  export UQ_NUM_ACTION_CANDIDATES=8
  export UQ_ACTION_CANDIDATE_BATCH_SIZE=4
  export UQ_NUM_WORLD_CANDIDATES=3
  export SAVE_V2W_VARIANCE_ARRAYS=1
  export UQ_SAVE_CANDIDATE_ARRAYS=1
  export BALANCED_SUCCESS_TARGET="${PER_WINDOW_SUCCESS_TARGET}"
  export BALANCED_FAILURE_TARGET="${PER_WINDOW_FAILURE_TARGET}"

  echo "Collecting suite=${suite_name} trials=${window_start}-${window_end} run_suffix=${run_suffix} raw_targets=exhaustive"
  ./scripts/run_libero_goal_ood_full_uncertainty_collection.sh

  if [[ "${VALIDATE_ONLY}" == "1" ]]; then
    return
  fi
  local rollout_dir
  rollout_dir="$(find_result_dir "${suite_name}" "${run_suffix}")"
  "${PYTHON}" scripts/audit_full_uq_rollout_integrity.py "${rollout_dir}" --check-arrays --max-array-checks 32
  cp "${PROTOCOL_JSON}" "${rollout_dir}/collection_protocol.json"
  echo "${rollout_dir}" >> "${LOG_DIR}/pro_goal_multi_ood_calibrated_rollout_dirs_${TIMESTAMP}.txt"
}

build_balanced_set() {
  local rollout_dirs_file="${LOG_DIR}/pro_goal_multi_ood_calibrated_rollout_dirs_${TIMESTAMP}.txt"
  local args=()
  while IFS= read -r rollout_dir; do
    [[ -n "${rollout_dir}" ]] && args+=(--input-dir "${rollout_dir}")
  done < "${rollout_dirs_file}"

  local current_matches=()
  while IFS= read -r match; do
    [[ -n "${match}" ]] && current_matches+=("${match}")
  done < <(find ${CURRENT_MULTI_OOD_DIR_GLOB} -maxdepth 1 -type d 2>/dev/null || true)

  local exclude_args=()
  for current_dir in "${current_matches[@]}"; do
    exclude_args+=(--exclude-episode-identity-from "${current_dir}")
  done
  if [[ -d "${PREVIOUS_PRO_OBJECT_DIR}" ]]; then
    exclude_args+=(--exclude-episode-identity-from "${PREVIOUS_PRO_OBJECT_DIR}")
  fi

  "${PYTHON}" scripts/build_balanced_full_uq_heldout_set.py \
    "${args[@]}" \
    "${exclude_args[@]}" \
    --output-dir "${BALANCED_DIR}" \
    --target-episodes-per-class "${BALANCED_TARGET_EPISODES_PER_CLASS}" \
    --min-episodes-per-class "${MIN_BALANCED_EPISODES_PER_CLASS}" \
    --max-episodes-per-suite-per-class "${MAX_EPISODES_PER_SUITE_PER_CLASS}" \
    --seed "${SELECTION_SEED}"
  cp "${PROTOCOL_JSON}" "${BALANCED_DIR}/collection_protocol.json"
  "${PYTHON}" scripts/audit_full_uq_rollout_integrity.py "${BALANCED_DIR}" --check-arrays --max-array-checks 32
}

require_file "${PYTHON}"
require_file "${PROTOCOL_JSON}"
require_file "${ROOT_DIR}/scripts/run_libero_goal_ood_full_uncertainty_collection.sh"
require_file "${ROOT_DIR}/scripts/audit_full_uq_rollout_integrity.py"
require_file "${ROOT_DIR}/scripts/build_balanced_full_uq_heldout_set.py"
export TASK_IDS TRIAL_WINDOWS MAX_EPISODE_STEPS SEED
export SELECTION_SEED BALANCED_TARGET_EPISODES_PER_CLASS MIN_BALANCED_EPISODES_PER_CLASS
export MAX_EPISODES_PER_SUITE_PER_CLASS
require_gpu
validate_protocol

echo "Starting calibrated PRO goal multi-OOD full-UQ collection at $(date --iso-8601=seconds)"
echo "protocol=${PROTOCOL_JSON}"
echo "suites=libero_goal_swap,libero_goal_object,libero_goal_task,libero_goal_lan"
echo "task_ids=${TASK_IDS}"
echo "initial_state_windows=${TRIAL_WINDOWS}"
echo "raw collection: exhaustive over all protocol candidates; no label-based early stop"
echo "final balanced target: ${BALANCED_TARGET_EPISODES_PER_CLASS}/${BALANCED_TARGET_EPISODES_PER_CLASS}; max per suite/class=${MAX_EPISODES_PER_SUITE_PER_CLASS}"
echo "eval_seed=${SEED}; selection_seed=${SELECTION_SEED}"

for suite_name in libero_goal_swap libero_goal_object libero_goal_task libero_goal_lan; do
  while read -r window_start window_count; do
    run_suite_collection "${suite_name}" "${window_start}" "${window_count}"
  done < <(parse_trial_windows)
done

if [[ "${VALIDATE_ONLY}" == "1" ]]; then
  echo "VALIDATE_ONLY=1: calibrated PRO goal multi-OOD preflight passed; no rollout started."
  exit 0
fi

build_balanced_set
echo "Finished calibrated PRO goal multi-OOD collection."
echo "balanced_dir=${BALANCED_DIR}"
