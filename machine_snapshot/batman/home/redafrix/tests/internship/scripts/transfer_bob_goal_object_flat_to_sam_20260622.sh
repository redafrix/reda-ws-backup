#!/usr/bin/env bash
set -euo pipefail

SRC_ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/inputs/datasets/continuous_chunk10_flat"
DST_ROOT="/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_object_h10_continuous_flat_from_bob_20260622"
LOG="/home/redafrix/tests/internship/transfer_logs/transfer_bob_goal_object_flat_to_sam_20260622.log"

{
  echo "START $(date -Is)"
  echo "SRC pcrobot:${SRC_ROOT}"
  echo "DST sam:${DST_ROOT}"

  ssh sam "mkdir -p \"${DST_ROOT}\""

  ssh pcrobot "cd \"${SRC_ROOT}\" && tar -cf - ." \
    | ssh sam "cd \"${DST_ROOT}\" && tar -xf -"

  echo "TRANSFER_DONE $(date -Is)"
  ssh sam "find \"${DST_ROOT}\" -maxdepth 3 -type f -printf '%s %p\n' | sort -nr | head -20"
  ssh sam "wc -l \"${DST_ROOT}\"/worker_0/*.jsonl"
  ssh sam "python3 - << 'PY'
import json, pathlib, collections
p = pathlib.Path('${DST_ROOT}/worker_0/episode_summaries.jsonl')
counts = collections.Counter()
success = collections.Counter()
rows = 0
for line in p.open():
    if not line.strip():
        continue
    row = json.loads(line)
    rows += 1
    task_id = row.get('task_id', row.get('task'))
    counts[task_id] += 1
    if row.get('success') is True or row.get('succeeded') is True:
        success[task_id] += 1
print('episodes', rows)
print('task_counts', dict(sorted(counts.items(), key=lambda kv: str(kv[0]))))
print('task_success', dict(sorted(success.items(), key=lambda kv: str(kv[0]))))
PY"
  echo "END $(date -Is)"
} >"${LOG}" 2>&1
