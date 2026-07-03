# FIPER Data Layout

This directory is the data entry point for Stage 9 FIPER work.

The active `fiper_sweep_eternal` collectors still write under each machine's
`asynchvla_ws/stage9_libero_pro_risk_data/campaigns` tree. Do not move those
live files while collection is running.

Use this layout inside each remote `reda_ws/fiper_ws`:

```text
data/
  live_local/fiper_sweep_eternal -> symlink to that machine's active collector root
  frozen/                        -> immutable snapshots used for training/eval
  manifests/                     -> dataset inventories and split manifests
```

The train/eval pipeline should read from `data/frozen/...`, not directly from
growing live JSONLs. Failure/timeout rows are evaluation-only; RND train/calib
must use success rows only.

Current ignored cells:

- `libero_10_with_milk`, task 3
- `libero_10_with_milk`, task 4

