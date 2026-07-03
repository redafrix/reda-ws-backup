#!/usr/bin/env bash
set -euo pipefail

LOCAL_ROOT="/home/redafrix/tests/internship"
TRANSFER_LOG="${LOCAL_ROOT}/transfer_logs/transfer_bob_goal_object_flat_to_sam_20260622.log"
TRAIN_SCRIPT_LOCAL="${LOCAL_ROOT}/scripts/train_simvla_goal_to_goal_object_ood_20260622.py"
TRAIN_SCRIPT_REMOTE="/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/train_simvla_goal_to_goal_object_ood_20260622.py"
REMOTE_LOG_DIR="/home/rootalkhatib/test/reda_ws/fiper_ws/logs/simvla_goal_to_goal_object_ood_topk8_20260622"
REMOTE_OUT="/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_goal_to_goal_object_ood_topk8_20260622"
SOURCE_JSONL="/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_uncertainty_final_5410ep_20260622/fiper_receding_samples.jsonl"
TARGET_ROOT="/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_object_h10_continuous_flat_from_bob_20260622"
WATCH_LOG="${LOCAL_ROOT}/transfer_logs/wait_transfer_then_launch_sam_goal_to_goal_object_ood_20260622.log"

{
  echo "START $(date -Is)"
  echo "Waiting for transfer log: ${TRANSFER_LOG}"
  while true; do
    if grep -q "END " "${TRANSFER_LOG}" 2>/dev/null; then
      echo "Transfer completed at $(date -Is)"
      break
    fi
    if ! tmux has-session -t transfer_bob_goal_object_flat_to_sam_20260622 2>/dev/null; then
      if grep -q "TRANSFER_DONE" "${TRANSFER_LOG}" 2>/dev/null; then
        echo "Transfer tmux gone but TRANSFER_DONE found at $(date -Is)"
        break
      fi
      echo "ERROR transfer tmux ended before completion marker. Last log:"
      tail -n 80 "${TRANSFER_LOG}" || true
      exit 1
    fi
    sleep 60
  done

  echo "Deploying training script to Sam"
  scp "${TRAIN_SCRIPT_LOCAL}" "sam:${TRAIN_SCRIPT_REMOTE}"

  echo "Launching Sam train/eval tmux"
  ssh sam "mkdir -p \"${REMOTE_LOG_DIR}\" \"${REMOTE_OUT}\""
  ssh sam "tmux has-session -t simvla_goal_to_goal_object_ood_train_20260622 2>/dev/null && tmux kill-session -t simvla_goal_to_goal_object_ood_train_20260622 || true"
  ssh sam "tmux new-session -d -s simvla_goal_to_goal_object_ood_train_20260622 'source /home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh && python3 -u \"${TRAIN_SCRIPT_REMOTE}\" --source-jsonl \"${SOURCE_JSONL}\" --target-root \"${TARGET_ROOT}\" --output-root \"${REMOTE_OUT}\" --epochs 10 --batch-size 512 > \"${REMOTE_LOG_DIR}/train_eval.log\" 2>&1'"

  echo "Launched at $(date -Is)"
  ssh sam "tmux ls | grep simvla_goal_to_goal_object_ood_train_20260622 || true"
  echo "Remote log: ${REMOTE_LOG_DIR}/train_eval.log"
  echo "Remote report: ${REMOTE_OUT}/SIMVLA_GOAL_TO_GOAL_OBJECT_OOD_REPORT_20260622.md"
  echo "END $(date -Is)"
} >"${WATCH_LOG}" 2>&1
