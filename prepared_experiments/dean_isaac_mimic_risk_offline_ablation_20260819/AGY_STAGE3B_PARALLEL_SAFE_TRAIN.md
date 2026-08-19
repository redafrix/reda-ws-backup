# Stage 3B — guarded parallel training on Dean while another GPU job is active

This file OVERRIDES the previous Stage-3 rule that any active GPU process causes an unconditional abort.

The user explicitly allows training to run in parallel with the existing Isaac smoke process **only if it can be done without terminating, pausing, renicing, signaling, reconfiguring, or materially risking the other process**.

Agy remains an operator only. Do not change scientific design.

## 0. Never touch the foreign process

Absolutely forbidden:
- kill / pkill / killall / SIGSTOP / SIGCONT / renice of the active Isaac process;
- changing its environment, CUDA settings, files, run config or output directory;
- restarting it;
- deleting its outputs;
- changing GPU persistence/power clocks/MPS/global settings;
- modifying batch size, architecture, features, split, optimizer, epochs or seeds of the Mimic experiment.

Some GPU throughput sharing is unavoidable when two CUDA processes execute concurrently. This stage's safety goal is: no OOM, no process termination, no global GPU reconfiguration, no CPU/I/O starvation, and no modification of the other job.

## 1. Freeze verification

Before any CUDA allocation verify byte hashes still equal:

- dataset_manifest_v2 SHA256: `043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3`
- normalization SHA256: `40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`
- heavy arrays: match `dataset_manifest_v2.json`
- branch contains code repair commit `1a09d4d350b1457cf4e2e99a6c66ed9a7fc233ac`
- run 26 tests; require 26/26 pass.

If any mismatch: STOP.

## 2. Observe the shared GPU before probing

Record raw outputs of:

`nvidia-smi --query-gpu=index,name,memory.total,memory.used,memory.free,utilization.gpu,utilization.memory,temperature.gpu,power.draw --format=csv,noheader,nounits`

and

`nvidia-smi --query-compute-apps=pid,process_name,used_memory --format=csv,noheader,nounits`

Then sample GPU free memory and utilization every 2 seconds for 60 seconds without touching any process.

Record:
- total VRAM MiB
- minimum free VRAM MiB over 60 s
- maximum used VRAM MiB over 60 s
- active foreign PIDs and their observed memory
- max GPU utilization over 60 s

Do NOT abort merely because utilization is nonzero.

## 3. Exact one-batch training-memory probe

Use the production dataset/model/loss/optimizer and exact batch size 64, but a throwaway model instance and one deterministic TRAIN batch only.

Requirements:
- same normalized 8-query windows as production;
- same `MimicH10RiskMonitor`;
- same AdamW;
- same BCEWithLogitsLoss and train pos_weight;
- forward;
- backward;
- one optimizer step solely so AdamW state allocations are included;
- do NOT save this throwaway model/checkpoint;
- do NOT alter any experiment model directory;
- immediately delete model/optimizer/tensors and `torch.cuda.empty_cache()`.

Measure with CUDA memory statistics:
- peak allocated MiB;
- peak reserved MiB.

This probe is infrastructure sizing only and is NOT one of seeds 0..4.

## 4. Parallel-safety acceptance rule

Let:
- `F = minimum free VRAM MiB observed during the 60-second foreign-job sampling window`
- `P = throwaway probe peak reserved MiB`

Training may proceed in parallel ONLY if BOTH are true:

1. `F >= P + 6144 MiB`
2. after the throwaway probe and cache clear, the foreign PID(s) are still alive and their used-memory values have not jumped by more than 1024 MiB relative to the pre-probe observation.

The 6 GiB reserve is intentionally conservative for foreign-job bursts.

If either condition fails:
- do not train;
- report `PARALLEL_SAFETY: INSUFFICIENT_HEADROOM_ABORTED`.

Do not lower the reserve yourself.

## 5. Resource containment for the real training

If accepted:

- run exactly the frozen batch size 64;
- seeds 0,1,2,3,4 sequentially, never simultaneous;
- 25 epochs each;
- same optimizer/loss/settings;
- launch the Python process with low CPU/I/O priority using:
  `nice -n 10 ionice -c2 -n7 ...`
- `num_workers=0` remains fixed;
- do not enable any global CUDA/MPS setting;
- do not alter GPU clocks/power.

Before starting each seed, record current free VRAM and confirm all foreign PIDs from preflight are still alive.

During training, every 30 seconds record:
- GPU free/used memory;
- foreign PID alive status;
- training PID used memory.

If free VRAM ever falls below 3072 MiB:
- gracefully terminate ONLY the Mimic training process at the next safe opportunity;
- never signal the foreign process;
- mark the current seed incomplete;
- report `PARALLEL_RUNTIME_GUARD: TRAINING_STOPPED_FOR_HEADROOM`.

If the foreign process exits naturally, do not restart it and continue training normally.

## 6. Train and validation-freeze exactly as frozen

Output model root:
`$W/models/isaac_mimic_h10_c0dyn_v1`

For each seed 0..4:
- exactly 25 epochs;
- best epoch = highest validation row AUPRC, earliest epoch on exact tie;
- seed 0 stays PRIMARY regardless of other seeds;
- freeze validation calibration for that seed using the corresponding best checkpoint;
- thresholds include fixed0.5, row-best-F1, conformal alpha .05/.10/.15, empirical q90/q95/q99;
- alpha .10 remains primary operating point.

Do NOT run held-out test.
Do NOT run OOD.

## 7. Freeze artifacts

After all five seeds complete, create a small training freeze manifest containing for every seed:
- 25/25 epochs complete;
- training_summary path + SHA256;
- best_model path + SHA256;
- best epoch;
- best val AUPRC;
- validation freeze path + SHA256;
- all thresholds;
- validation row AUROC/AUPRC;
- validation failure episode count;
- runtime environment;
- shared-GPU observation/probe/monitor summary.

Record aggregate SHA256 for the five-seed training freeze.

Commit only small code/manifest/summary files; never model weights/heavy arrays.

Commit message exactly:
`experiment(dean): train and validation-freeze Mimic H10 monitor under guarded GPU sharing`

## RETURN ONLY

PARALLEL_PREFLIGHT:
foreign_pids:
gpu_name:
total_vram_mib:
min_free_vram_60s_mib:
max_gpu_util_60s_pct:
probe_peak_allocated_mib:
probe_peak_reserved_mib:
required_free_mib:
foreign_processes_alive_after_probe:
foreign_memory_delta_max_mib:
parallel_safety:

TRAINING:
seed0: <best_epoch | best_val_auprc | checkpoint_sha256 | 25/25>
seed1: <best_epoch | best_val_auprc | checkpoint_sha256 | 25/25>
seed2: <best_epoch | best_val_auprc | checkpoint_sha256 | 25/25>
seed3: <best_epoch | best_val_auprc | checkpoint_sha256 | 25/25>
seed4: <best_epoch | best_val_auprc | checkpoint_sha256 | 25/25>
all_seeds_25_epochs_complete:
training_freeze_sha256:

VALIDATION_FREEZE:
seed0: <freeze_sha256 | val_auroc | val_auprc | alpha0.10_threshold>
seed1: <freeze_sha256 | val_auroc | val_auprc | alpha0.10_threshold>
seed2: <freeze_sha256 | val_auroc | val_auprc | alpha0.10_threshold>
seed3: <freeze_sha256 | val_auroc | val_auprc | alpha0.10_threshold>
seed4: <freeze_sha256 | val_auroc | val_auprc | alpha0.10_threshold>
primary_seed:
primary_operating_point:

RUNTIME_GUARD:
minimum_free_vram_seen_mib:
foreign_processes_signaled:
training_stopped_for_headroom:

HELD_OUT_TEST_SCORED:
NO

OOD_SCORED:
NO

ISAAC_SIM_LAUNCHED_BY_THIS_STAGE:
NO

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
