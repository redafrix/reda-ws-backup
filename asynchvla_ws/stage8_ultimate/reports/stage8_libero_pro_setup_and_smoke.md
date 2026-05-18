# Stage 8 LIBERO-PRO Setup And Smoke

Generated: `2026-05-15T15:23:52`

## Status

LIBERO-PRO is now locally available on Bob and can create/reset a perturbed environment through the current LIBERO/robosuite stack.

## Repository And Config

- Repo: `intern_ship_ws/assets/repos/LIBERO-PRO`
- Config: `asynchvla_ws/configs/libero_pro_bob/config.yaml`
- Primary injected path: `intern_ship_ws/assets/repos/LIBERO-PRO`
- BDDL root: `intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files`
- Init-state root: `intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files`

## Smoke Environment

- Suite: `libero_object_with_mug`
- Task id: `0`
- Language: `pick the alphabet soup and place it in the basket`
- Result file: `asynchvla_ws/stage8_ultimate/results/libero_pro_smoke_object_mug_t0.json`

## One-Episode Smoke Results

The 80-step smoke is an integration test, not a success-rate benchmark.

| mode | success | steps | walltime_sec |
|---|---:|---:|---:|
| A_passive | False | 80 | 10.58 |
| B_deliberation | False | 80 | 10.42 |

## Decision

LIBERO-PRO smoke passed sufficiently to launch the pilot benchmark. The first full benchmark should use 600 max steps and compare A/B/C/D/E policies before making deployment claims.
