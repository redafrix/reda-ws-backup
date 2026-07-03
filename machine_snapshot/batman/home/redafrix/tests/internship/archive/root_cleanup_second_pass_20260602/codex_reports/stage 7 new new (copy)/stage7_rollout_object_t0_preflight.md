# Stage 7 — Rollout Object T0 Preflight

- Timestamp: 2026-05-15 (Gemini)
- Machine: pcrobot

## Environment Status

- **Git Branch:** bob
- **GPU:** RTX 4070 Ti SUPER (0% util, 3272MiB used)
- **Python:** 3.10.12
- **Torch:** 2.5.1+cu121 (CUDA: True)
- **Robosuite:** OK
- **LIBERO:** OK

## Rollout Script Argparse

The script `libero_execution_uncertainty_eval.py` supports:
- `--task-suite`: libero_object (default: libero_spatial)
- `--task-id`: 0 (default: 0)
- `--num-episodes`: (to be set to 10)
- `--max-steps`: (to be set to 600)
- `--modes`: A_passive, B_deliberation, etc.
- `--out`: output JSON path

## Plan

1. Run A_passive (10 episodes)
2. Run B_deliberation (10 episodes)
3. Analyze results

All systems nominal.
