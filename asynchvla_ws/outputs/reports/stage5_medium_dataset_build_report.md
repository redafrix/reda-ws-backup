# Stage 5 Medium Dataset Build Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`
Workspace: `/media/rootalkhatib/My Passport/reda_ws`
Branch: `bob`
Date: 2026-05-13
Builder versions:
- `asynchvla_ws/src/data_building/build_multiseed_trace_dataset.py`
- `asynchvla_ws/src/data_building/build_multiseed_candidate_dataset.py`

## Builds

All three medium splits were built at the same sizes:
- `--max-contexts 1000 --max-calib 250 --max-test-id 250 --max-test-ood 250`
- `--cap-per-file 80`
- `--simvla-seeds 0 1 2 3 4`
- `--steps 10` (flow-matching)

Wall-clock times (trace build only, end-to-end):
- `id_task_split`: 849.7 s ≈ 14.2 min (no `test_ood` for this split)
- `holdout_libero_object`: 1000.9 s ≈ 16.7 min
- `holdout_object_bowl`:   996.4 s ≈ 16.6 min

Candidate building (CPU-only, reads trace .pt and emits candidate .pt) is ~30 s per split. The 14–17 min runtime is essentially 5 SimVLA forward passes per context × 1500–1750 contexts per split.

## Per-split outputs

### id_task_split
- `data/processed_stage5/id_task_split/multiseed_trace_{train,calib,test_id}.pt`
- `data/processed_stage5/id_task_split/multiseed_candidate_{train,calib,test_id}.pt`
- No `test_ood` (split manifest had 0 OOD files).
- Counts: train 1000 ctx / 10000 candidates; calib 250 / 2500; test_id 250 / 2500.

### holdout_libero_object
- Heldout suite: `libero_object` (held out at the suite level — none of those tasks are in train).
- `multiseed_trace_{train,calib,test_id,test_ood}.pt` and corresponding candidates.
- Counts (all parts): train 1000 / 10000; calib 250 / 2500; test_id 250 / 2500; test_ood 250 / 2500.

### holdout_object_bowl
- Excluded object: `bowl`.
- All four partitions present.
- Counts: train 1000 / 10000; calib 250 / 2500; test_id 250 / 2500; test_ood 250 / 2500.

## File sizes on disk

| split | trace_train | candidate_train | candidate_calib | candidate_test_id | candidate_test_ood |
| --- | ---: | ---: | ---: | ---: | ---: |
| id_task_split | 13 MB | 57 MB | 14 MB | 15 MB | n/a |
| holdout_libero_object | 13 MB | 57 MB | 14 MB | 15 MB | 15 MB |
| holdout_object_bowl | 13 MB | 57 MB | 14 MB | 15 MB | 15 MB |

Total Stage 5 medium data ≈ 0.32 GB on Passport drive — disk usage is negligible.

## Candidate type counts per partition (all splits identical)

Every partition contains, per context, 10 candidates:
- `expert_action` (1 per context)
- `simvla_seed0..4` (5 per context)
- `perturb_small`, `perturb_large` (2 per context)
- `same_task_far`, `other_demo_or_other_task` (2 per context)

So 1000 contexts → 10000 candidates per train; 250 contexts → 2500 candidates for calib/test_id/test_ood.

## Error stats per candidate type

Drawn from the per-split metrics JSON. Mean per-chunk-L2-error on the train partition:

| candidate type | id_task_split | holdout_libero_object | holdout_object_bowl |
| --- | ---: | ---: | ---: |
| expert_action | 0.000 | 0.000 | 0.000 |
| simvla_seed0 | 1.699 | 1.785 | 1.611 |
| simvla_seed1 | 1.700 | 1.787 | 1.610 |
| simvla_seed2 | 1.690 | 1.781 | 1.608 |
| simvla_seed3 | 1.706 | 1.794 | 1.616 |
| simvla_seed4 | 1.701 | 1.788 | 1.610 |
| perturb_small | 0.250 | 0.250 | 0.250 |
| perturb_large | 1.880 | 1.882 | 1.880 |
| same_task_far | 0.713 | 0.708 | 0.704 |
| other_demo_or_other_task | 0.793 | 0.795 | 0.788 |

(Per-seed means are essentially equal — seeds give diverse actions but with similar overall difficulty for any given task.)

## Failures and caveats

- None of the three builds errored. All `done multiseed trace ...` messages were observed.
- `id_task_split` has no OOD partition by design — `test_id` is the only held-out partition for that split.
- Builders use float32 throughout; no NaN/Inf observed during the trace build (per stage5_multiseed_trace_debug.md the same code path was already validated on debug).
- SmolVLM `torch_dtype` and `TRANSFORMERS_CACHE` deprecation warnings appear in build logs — they do not affect output.
- Trace builder uses `cap-per-file 80` for ALL partitions including calib/test_id/test_ood. With small file lists in some manifests, only a handful of files contribute to those partitions — this is a known limitation of the existing builder, not introduced in Stage 5.

## Activation

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
```

## Exact commands

```bash
python3 -u asynchvla_ws/src/data_building/build_multiseed_trace_dataset.py \
  --split-manifest asynchvla_ws/data/splits/<split>.json \
  --split-name <split> \
  --max-contexts 1000 --max-calib 250 --max-test-id 250 --max-test-ood 250 \
  --cap-per-file 80 --simvla-seeds 0 1 2 3 4

python3 -u asynchvla_ws/src/data_building/build_multiseed_candidate_dataset.py \
  --split-name <split>
```
