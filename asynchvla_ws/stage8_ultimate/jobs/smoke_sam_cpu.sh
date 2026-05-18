#!/usr/bin/env bash
set -uo pipefail
mkdir -p /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status
echo '[stage8] job smoke_sam_cpu attempt 1 start '$(date -Is)
cd /home/rootalkhatib/test/reda_ws && mkdir -p asynchvla_ws/stage8_ultimate/results && echo sam_ok > asynchvla_ws/stage8_ultimate/results/smoke_sam_cpu.txt
rc=$?
echo '[stage8] job smoke_sam_cpu exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_sam_cpu.json.done_marker; else echo $rc > /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_sam_cpu.json.fail_marker; fi
exit $rc

