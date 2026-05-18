#!/usr/bin/env bash
set -uo pipefail
mkdir -p '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status'
echo '[stage8] job flowtrace_medium_bob attempt 1 start '$(date -Is)
bash -lc 'cd "/media/rootalkhatib/My Passport/reda_ws" && source asynchvla_ws/scripts/activate_simvla_bob.sh && python3 asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py --split-manifest asynchvla_ws/data/splits/holdout_libero_object.json --split-name stage8_flowtrace_medium --max-contexts 300 --max-calib 100 --max-test-id 100 --max-test-ood 100 --cap-per-file 40 --simvla-seeds 0 1 2 3 4 && python3 - <<'"'"'PY'"'"'
from pathlib import Path
import torch
base=Path('"'"'asynchvla_ws/data/processed_stage7_flow/stage8_flowtrace_medium'"'"')
lines=['"'"'# Stage 8 Flowtrace Results'"'"','"'"''"'"',f'"'"'Dataset: `{base}`'"'"','"'"''"'"']
for p in sorted(base.glob('"'"'flowtrace_multiseed_trace_*.pt'"'"')):
 d=torch.load(p,map_location='"'"'cpu'"'"'); samples=d.get('"'"'samples'"'"',[]); lines.append(f'"'"'- `{p.name}`: {len(samples)} contexts, seeds={d.get("seeds")}'"'"')
Path('"'"'asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md'"'"').write_text('"'"'\n'"'"'.join(lines)+'"'"'\n'"'"')
PY'
rc=$?
echo '[stage8] job flowtrace_medium_bob exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/flowtrace_medium_bob.json.done_marker'; else echo $rc > '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/flowtrace_medium_bob.json.fail_marker'; fi
exit $rc

