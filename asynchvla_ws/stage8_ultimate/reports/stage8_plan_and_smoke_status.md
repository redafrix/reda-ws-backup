# Stage 8 Plan And Smoke Status

Generated: `2026-05-15T15:23:52`

## Objective

Stage 8 prepares a 3-day unattended Bob/Sam pipeline with LIBERO-PRO as the primary benchmark. Normal LIBERO is used only for sanity, hard-task baseline, and fallback.

## Smoke Gate Status

| Smoke | Status | Evidence |
|---|---:|---|
| Job manager Bob/Sam/dependency/retry | PASS | `asynchvla_ws/stage8_ultimate/reports/stage8_manager_smoke.md` |
| Bob LIBERO-PRO import/reset/rollout | PASS integration, no success claim | `asynchvla_ws/stage8_ultimate/results/libero_pro_smoke_object_mug_t0.json` |
| Sam training smoke | PASS | Sam `asynchvla_ws/stage8_ultimate/reports/stage8_sam_training_smoke.md` and portable Stage6 smoke report |
| Flowtrace smoke | PASS | `asynchvla_ws/data/processed_stage7_flow/stage8_flowtrace_smoke/flowtrace_multiseed_trace_train.pt`, 10 contexts, seeds 0 and 1 |
| Calibration smoke | PASS | `asynchvla_ws/stage8_ultimate/reports/stage8_calibration_smoke.md` |
| Normal LIBERO hard-task smoke | PASS integration, no success claim | `asynchvla_ws/stage8_ultimate/results/normal_libero_hard_smoke_spatial_t5.json` |

## LIBERO-PRO First Queue

Priority order for unattended launch:

1. LIBERO-PRO pilot on Bob with A/B/C/D/E modes.
2. Sam model/calibration jobs on existing processed data.
3. Normal LIBERO hard-task baseline as fallback/baseline.
4. Flowtrace and target experiments when GPU is free.
5. Switch-policy and final dashboard generation after rollout results exist.

## Interpretation Rules

- Do not treat synthetic candidate metrics as deployment evidence.
- Deliberation is useful only if it improves success/progress or accepted/rejected quality, not just predicted uncertainty.
- If LIBERO-PRO blocks, the exact blocker must be reported and normal LIBERO remains fallback only.
