# Stage 7 — Sam Model Readiness

- Timestamp: `2026-05-15 11:38` (Bob local)
- Goal: confirm Sam can load and run SimVLA + SmolVLM end-to-end.
- Result: **READY**. Sam is now a viable second model machine.

## What changed

1. `model.safetensors` on Sam was 479 MB (partial). Bob has 1015 MB. Difference confirmed by `du -sh` and exact byte-count comparison.
2. Started rsync Bob → Sam under nohup:

```bash
rsync -a --partial --inplace --info=progress2 \
    /media/rootalkhatib/My\ Passport/reda_ws/intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct/ \
    rootalkhatib@100.112.19.30:/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct/
```

Steady ~10 MB/s on Tailscale; took ~50 s to finish. Final `model.safetensors` = 1,015,025,832 bytes (byte-exact match with Bob).

## Verified after sync

- `torch` 2.5.1+cu121, CUDA available, RTX 4070 Ti SUPER detected.
- `SmolVLMVLAConfig.from_pretrained(...)` loads `Idefics3ForConditionalGeneration` arch.
- `SmolVLMVLA.from_pretrained(ckpt-60000, ...).to('cuda')` succeeds; `dim_action=7`; processor loads.
- Sam GPU idle prior to test: 3645 MiB resident, 0% util. SimVLA load OK.

## What Sam still lacks

- The robosuite/mujoco/bddl stack installed on Bob for LIBERO rollout is **not** installed on Sam yet. If we decide to also run LIBERO rollout on Sam, replicate the Phase 3 install steps there (same `--target=/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages`, same package list).
- The Stage 6 rater checkpoints at `asynchvla_ws/outputs/checkpoints/stage6/<split>/<variant>/model.pt` are present on Bob. To run rollout on Sam these would need to be synced (small; can rsync along with a job script).
- The Bob-local LIBERO config at `asynchvla_ws/configs/libero_bob/config.yaml` points to Bob's `/media/rootalkhatib/My Passport/...` paths. For Sam we would write a sister config `asynchvla_ws/configs/libero_sam/config.yaml` with `/home/rootalkhatib/test/reda_ws/...` paths.

## Recommendation

- Use Sam as second machine for **multi-seed SimVLA inference jobs that do not need LIBERO env**: e.g., a duplicate or longer-running flow-trace dataset build on a different split, run in parallel with Bob's load.
- Defer LIBERO rollout on Sam until Bob's tiny rollout (Phase 4) is verified, then optionally fan out for larger scale.
