#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"

PYTHON="${PYTHON:-${ROOT}/model/.venv/bin/python}"
MANIFEST="${ROOT}/configs/uq_benchmarks/libero_goal_object_task0to9_trials0to9_eval_seed0_tasklang_20260623.csv"
WM_RUNNER="${ROOT}/scripts/run_libero_goal_ood_full_uncertainty_collection.sh"
SIMVLA_RUNNER="${ROOT}/scripts/run_simvla_world_model_arbiter.py"
SIMVLA_CONFIG="${ROOT}/configs/arbiter/goal_object_100_tasklang_hf_simvla_20260623.json"
SMOLVLM_PATH="${SMOLVLM_PATH:-${HOME}/.cache/huggingface/hub/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47}"
RUN_TAG="${RUN_TAG:-$(date +%Y%m%d_%H%M%S)}"
OUT_ROOT="${OUT_ROOT:-${ROOT}/results/libero_goal_object_100_official_tasklang_20260623}"
LOG="${LOG:-${ROOT}/logs/libero_goal_object_100_tasklang_${RUN_TAG}.log}"

for required in "${MANIFEST}" "${WM_RUNNER}" "${SIMVLA_RUNNER}" "${SIMVLA_CONFIG}" "${SMOLVLM_PATH}"; do
  if [[ ! -e "${required}" ]]; then
    echo "Missing required file: ${required}" >&2
    exit 2
  fi
done

if [[ -e "${OUT_ROOT}" ]]; then
  echo "Refusing to overwrite existing output root: ${OUT_ROOT}" >&2
  exit 2
fi

mkdir -p "$(dirname "${LOG}")"

echo "Starting libero_goal_object 100-episode official task.language campaign at $(date --iso-8601=seconds)" | tee -a "${LOG}"
echo "output_root=${OUT_ROOT}" | tee -a "${LOG}"
echo "manifest=${MANIFEST}" | tee -a "${LOG}"
sha256sum "${MANIFEST}" "${SIMVLA_CONFIG}" | tee -a "${LOG}"

result_dir="${OUT_ROOT}/wm_h56_k1/libero_goal_object"
echo "START policy=wm_h56_k1 suite=libero_goal_object $(date --iso-8601=seconds)" | tee -a "${LOG}"
env \
  PYTHON="${PYTHON}" \
  OOD_IMPL=pro \
  LIBERO_PRO_ROOT="${ROOT}/../LIBERO-PRO" \
  EPISODE_MANIFEST_PATH="${MANIFEST}" \
  TASK_SUITE_NAME=libero_goal_object \
  TASK_IDS=0-9 \
  NUM_TRIALS_PER_TASK=10 \
  TRIAL_START_INDEX=0 \
  NUM_STEPS_WAIT=10 \
  MAX_EPISODE_STEPS=250 \
  SEED=0 \
  PROMPT_SOURCE=task_language \
  PRECOMPUTE_EMBEDDINGS=0 \
  SAVE_VIDEOS=0 \
  VALIDATE_ONLY=0 \
  RESULT_DIR_OVERRIDE="${result_dir}" \
  RUN_SUFFIX="object100_official_tasklang_wm_h56_k1" \
  VAM_NUM_SAMPLING_STEPS=2 \
  STOP_VIDEO_DENOISING_STEP=0 \
  NUM_EXECUTE_ACTIONS=56 \
  ENABLE_V2W_UNCERTAINTY=0 \
  UQ_CONTROL_POLICY=first_candidate \
  UQ_NUM_ACTION_CANDIDATES=1 \
  UQ_ACTION_CANDIDATE_BATCH_SIZE=1 \
  UQ_NUM_WORLD_CANDIDATES=1 \
  UQ_SAVE_CANDIDATE_ARRAYS=0 \
  SAVE_V2W_VARIANCE_ARRAYS=0 \
  "${WM_RUNNER}" >> "${LOG}" 2>&1
echo "DONE policy=wm_h56_k1 suite=libero_goal_object $(date --iso-8601=seconds)" | tee -a "${LOG}"

echo "START policy=hf_simvla $(date --iso-8601=seconds)" | tee -a "${LOG}"
env \
  WORLD_ROOT="${ROOT}/.." \
  SIMVLA_ROOT="${ROOT}/../SimVLA_modified" \
  LIBERO_PRO_ROOT="${ROOT}/../LIBERO-PRO" \
  SIMVLA_NORM_STATS="${ROOT}/../SimVLA_modified/norm_stats/libero_norm.json" \
  SMOLVLM_PATH="${SMOLVLM_PATH}" \
  HF_HUB_OFFLINE=1 \
  TRANSFORMERS_OFFLINE=1 \
  MPLCONFIGDIR="/tmp/matplotlib-${USER:-user}" \
  "${PYTHON}" "${SIMVLA_RUNNER}" \
    --config "${SIMVLA_CONFIG}" \
    >> "${LOG}" 2>&1
echo "DONE policy=hf_simvla $(date --iso-8601=seconds)" | tee -a "${LOG}"

echo "Finished libero_goal_object 100-episode official task.language campaign at $(date --iso-8601=seconds)" | tee -a "${LOG}"
