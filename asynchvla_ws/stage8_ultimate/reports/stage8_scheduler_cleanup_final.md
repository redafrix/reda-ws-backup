# Stage 8 Scheduler Cleanup Final

Generated: `2026-05-15T21:11:15`

## Action Taken
Stopped obsolete `stage8_scheduler_loop.sh` processes only.

Terminated PIDs:
- `629551`
- `629554`
- `629790`
- `631249`
- `631250`
- `631253`

## Kept Running
- `stage8_watchdog.py` PID `658116` remains running.
- Active experiment jobs were not killed.
- The active Bob LIBERO-PRO expanded rollout was left untouched.

## Reason
The old scheduler loop and new watchdog could both attempt launches, creating duplicate/racing orchestration. The current controller should be the watchdog only.
