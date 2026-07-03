#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-/home/redafrix/SimVLA_modified}"
EVAL_DIR="${EVAL_DIR:-${REPO_ROOT}/evaluation/libero}"
CHECKPOINT="${CHECKPOINT:-${REPO_ROOT}/runs/simvla_libero_uncertainty/ckpt-60000}"
NORM_STATS="${NORM_STATS:-${REPO_ROOT}/norm_stats/libero_norm.json}"
PORTS="${PORTS:-8103 8104}"
GPU_IDS="${GPU_IDS:-${CUDA_VISIBLE_DEVICES:-0}}"
BASE_SEED="${BASE_SEED:-7}"
NUM_ACTION_SAMPLES="${NUM_ACTION_SAMPLES:-1}"
SERVER_LOG_DIR="${SERVER_LOG_DIR:-${EVAL_DIR}/server_logs}"

mkdir -p "${SERVER_LOG_DIR}"

if [ -f "${HOME}/miniconda3/etc/profile.d/conda.sh" ]; then
  source "${HOME}/miniconda3/etc/profile.d/conda.sh"
elif [ -f "${HOME}/anaconda3/etc/profile.d/conda.sh" ]; then
  source "${HOME}/anaconda3/etc/profile.d/conda.sh"
else
  echo "[ERROR] Could not find conda.sh. Activate conda manually or fix the path." >&2
  exit 1
fi

conda activate simvla

cd "${EVAL_DIR}"

read -r -a PORT_ARRAY <<< "${PORTS}"
if [ "${#PORT_ARRAY[@]}" -eq 0 ]; then
  echo "[ERROR] PORTS is empty. Example: PORTS=\"8103 8104\"" >&2
  exit 1
fi
read -r -a GPU_ARRAY <<< "${GPU_IDS}"
if [ "${#GPU_ARRAY[@]}" -eq 0 ]; then
  echo "[ERROR] GPU_IDS is empty. Example: GPU_IDS=\"0 1\"" >&2
  exit 1
fi

echo "Starting SimVLA servers"
echo "CHECKPOINT = ${CHECKPOINT}"
echo "NORM_STATS = ${NORM_STATS}"
echo "PORTS      = ${PORTS}"
echo "GPU_IDS    = ${GPU_IDS}"
echo "SAMPLES    = ${NUM_ACTION_SAMPLES}"
echo "LOG DIR    = ${SERVER_LOG_DIR}"

for idx in "${!PORT_ARRAY[@]}"; do
  port="${PORT_ARRAY[$idx]}"
  gpu_id="${GPU_ARRAY[$((idx % ${#GPU_ARRAY[@]}))]}"
  seed=$((BASE_SEED + idx))
  log_path="${SERVER_LOG_DIR}/server_${port}.log"
  echo "Launching server on port ${port} with seed ${seed} on GPU ${gpu_id}"
  CUDA_VISIBLE_DEVICES="${gpu_id}" \
    nohup python serve_smolvlm_libero.py \
      --checkpoint "${CHECKPOINT}" \
      --norm_stats "${NORM_STATS}" \
      --port "${port}" \
      --seed "${seed}" \
      --num_action_samples "${NUM_ACTION_SAMPLES}" \
      > "${log_path}" 2>&1 &
done

echo ""
echo "Servers launched in background. Check logs with:"
echo "  tail -f ${SERVER_LOG_DIR}/server_8103.log"
