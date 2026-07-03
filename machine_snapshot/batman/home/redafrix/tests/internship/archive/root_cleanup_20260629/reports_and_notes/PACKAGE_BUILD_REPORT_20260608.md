# Package Build Report: simvla_modified_risk_topk8_h10_20260608

**Date**: 2026-06-08  
**Target Folder on Dean**: `/home/dean/deploy_packages/simvla_modified_risk_topk8_h10_20260608`  
**Final Zip on Dean**: `/home/dean/deploy_packages/simvla_modified_risk_topk8_h10_20260608.zip`

---

## 1. Overview & Goal

This package brings together all the required model weights, continuous risk detectors, and evaluation scripts needed to deploy the modified SimVLA policy with the **H10-only Risk-Aware TopK8 detector** on a new workstation. This deployment package enables direct model inference and evaluation on LIBERO/LIBERO-PRO tasks.

---

## 2. Package Provenance

*   **Modified SimVLA Checkpoint (`ckpt-60000`)**
    *   **Source Host**: Dean (`100.124.50.124`)
    *   **Source Path**: `/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000`
*   **H10-only Risk-Aware TopK8 Detector Model**
    *   **Source Host**: Bob (`100.105.217.20`)
    *   **Source Path**: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
*   **Runtime Evaluation Scripts**
    *   **Source Host**: Bob (`100.105.217.20`)
    *   **Source Path**: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/src`

---

## 3. Heldout exact200 Result Summary

The Risk-Aware TopK8 detector model (`h10_unc_topk8`) included in this package was evaluated on the held-out exact200 set. Performance metrics summary:
*   **Failure Detection Recall**: `38 / 38` (100.0%)
*   **Success False Alarm Rate (FPR)**: `14 / 162` (8.64%)
*   **Detection at 25% Horizon (Det@25)**: `68.42%`
*   **Detection at 50% Horizon (Det@50)**: `86.84%`

---

## 4. Package Contents & Integrity Verification

All files inside the package have been validated against their expected paths and verified via SHA256 checksum hashing.

### Packaged Files and Checksums

| Path | Size (Bytes) | SHA256 Checksum |
| :--- | :--- | :--- |
| `README_DEPLOY.md` | 6,756 | `59445c80f7321f98e7f16f46eb10653b85125497b7614b9f077a3f4f251cd6d1` |
| `MANIFEST.json` | 2,826 | `5544c4a494e135f6ecb9ad453b45f26029fdbf76306fe169cd7c7089a92a18fd` |
| `checksums/SHA256SUMS.txt` | 1,602 | `5544c4a494e135f6ecb9ad453b45f26029fdbf76306fe169cd7c7089a92a18fd` |
| `checkpoints/simvla_modified_ckpt_60000/config.json` | 570 | `ba0e65ae6f95af8831fcc77fe45adcdce696b1e537a578bc5552a58837fbec63` |
| `checkpoints/simvla_modified_ckpt_60000/model.safetensors` | 3,245,557,952 | `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71` |
| `checkpoints/simvla_modified_ckpt_60000/state.json` | 22 | `9fe17bcb768c136658d4cd80e30d6f427bacb70fd9ac88f92beada0ed7752521` |
| `configs/example_modified_topk8_task_config.json` | 1,304 | `5ad672dee6b3f2022aae575358c64d6ab36bf074728fc48231459804f4db89d2` |
| `risk_models/h10_unc_topk8/config.json` | 571 | `5b8f6a282616668e9a93a2a9fa106b02d369cb47e52c08aa3353021002076689` |
| `risk_models/h10_unc_topk8/thresholds.json` | 87 | `cef61220101dec3d808937fe028ca736b11ebdc8f1d9a25e9fde70cffa020756` |
| `risk_models/h10_unc_topk8/history.json` | 2,958 | `d3b011cf595f8a3e72e8e72cde8893fd7f9a655ae0a5fa8cec27b95fd59bb4c0` |
| `risk_models/h10_unc_topk8/normalization.json` | 4,428 | `6e29308d590593afa87cb26813f970dc30355aa218d0dc992e39490a632b0355` |
| `risk_models/h10_unc_topk8/metrics.json` | 5,214 | `798ee5ff2e59c1efa1b5ba05a26e8f1b760b59d29b58b5cac5721bb5bf5e5f35` |
| `risk_models/h10_unc_topk8/model.pt` | 2,602,964 | `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d` |
| `scripts/run_online_groups.py` | 4,176 | `2520a871365a07dc5c880f46a447e64ee8d4c5a88ccfe5e4659566ad889e251e` |
| `scripts/run_policy_matrix.py` | 52,338 | `2e7c64425bdb9f58b8fd612d6af9d50dc6346c8d495cf66774aebc9d601cbf82` |
| `scripts/generate_h10_online_configs.py` | 5,575 | `983625e0018ccf6ed3e58919a1e1a7733acb39c12b4fab275d486943dea0d8ee` |
| `scripts/collect_fiper_uncertainty_receding_dean_v1.py` | 47,746 | `9eebc654eed9dbd4198afa4941a59be5a60742afbb69fbd367b30c69f8b5d58a` |

---

## 5. Zip Archive Verification

The final zip file was created and verified with the following steps:
1.  **Integrity Test**: `unzip -t` passed with no errors.
2.  **File Size**: `2.7 GB` (matches the expected size for compressed 3.0 GB safetensors).
3.  **Contents Cleanliness**: Verified that no datasets (NPZs), old training logs, or outputs are present.
4.  **Tree Structure**: Top-level directory structured as `simvla_modified_risk_topk8_h10_20260608/`.

---

## 6. Execution Patterns

### Smoke Test Command
To verify imports and setup on a new PC:
```bash
python scripts/run_policy_matrix.py \
  --config configs/example_modified_topk8_task_config.json \
  --policy risk_topk8 \
  --smoke
```

### Full Evaluation Command
To run full episodes:
```bash
python scripts/run_policy_matrix.py \
  --config configs/example_modified_topk8_task_config.json \
  --policy risk_topk8
```
