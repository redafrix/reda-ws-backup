# Stage 8 Manager Smoke

Generated: `2026-05-15T15:23:52`

## Result

PASS. The Stage 8 job manager launched and tracked:

- one Bob CPU job,
- one Sam CPU job,
- one dependency-chain job,
- one intentionally failing job that succeeded on retry.

## Status Table

| job_id | machine | state | attempt | missing_outputs |
|---|---|---:|---:|---|
| smoke_bob_cpu | bob | DONE | 1 | [] |
| smoke_sam_cpu | sam | DONE | 1 | [] |
| smoke_dependency_child | bob | DONE | 1 | [] |
| smoke_retry_failure | bob | DONE | 2 | [] |

## Manager Files

- `asynchvla_ws/scripts/stage8_job_manager.py`
- `asynchvla_ws/scripts/stage8_status.sh`
- `asynchvla_ws/scripts/stage8_collect_reports.sh`
- `asynchvla_ws/stage8_ultimate/configs/stage8_job_manifest.json`

## Notes

The wrapper bug where a command with `exit 7` could terminate before writing a fail marker was fixed. The retry smoke then completed on attempt 2.
