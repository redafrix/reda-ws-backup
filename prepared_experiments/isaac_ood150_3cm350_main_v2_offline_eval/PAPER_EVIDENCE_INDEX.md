# Converted OOD150 Offline Evaluation — Primary Paper Evidence Index

This document is the authoritative index pointing to all primary artifacts, manifests, configurations, checksums, and source commits for the offline evaluation of the current main Isaac risk model (`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`) on the exact-only converted historical OOD150 subset.

---

## 1. Source Git Repository & Commits
- **Repository**: `redafrix/reda-ws-backup`
- **Working Branch**: `experiment/dean-isaac-online-ood150-20260817`
- **Local Path**: `/home/redafrix/tests/internship`
- **Authoritative OOD Evaluation Commit**: [`cdd55fbd6958264322b3bc53aea8c63b4edeff33`](https://github.com/redafrix/reda-ws-backup/commit/cdd55fbd6958264322b3bc53aea8c63b4edeff33)

---

## 2. Dataset Scope & Relabeling Protocol
- **Source Baseline**: 150 historical candidate-0 OOD episodes (`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728`)
- **Conversion Mode**: `EXACT_ONLY`
- **Scope Statement**: "exact-only converted historical OOD150 subset (136/150 episodes)"
- **Included Exact Episodes**: **136 episodes** (72 success, 64 failure)
- **Excluded Unresolvable Episodes**: **14 episodes** (all old failures entering $(0.020\text{ m}, 0.030\text{ m}]$ without recorded first crossing tick relative to tick 350)
- **Retained Decision Rows (`decision_index <= 34`)**: **3,447 rows** (1,207 success rows, 2,240 failure rows; max decision index: 34)

---

## 3. Evaluated Model Checkpoint
- **Model Name**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`
- **Model Checkpoint**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/model.pt`
  - **SHA256**: `00ad096a9ca38577366e992e1d7f8aa25b6f56f2f2bd7354abce1790baf890f1`
- **Train Normalization**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/norm.npz`
  - **SHA256**: `6fbd2b221c4490c975e3e1492c96a9e879a586f0b3a4c4eaf97ea05920960341`

---

## 4. Primary Evidence Files & Checksums

| File | Relative Path | SHA256 Checksum |
|:---|:---|:---|
| `OOD150_SOURCE_AUDIT.json` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_SOURCE_AUDIT.json` | `01191abc19ce03fabe98b72a8d6e85b8100eb54d33d7dec11eb6459cd1568b6f` |
| `OOD150_CONVERSION_AUDIT.json` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_CONVERSION_AUDIT.json` | `c44fd5f8b60407d05d077a94a61ad9a81dc7df2a30c95d68ce897f525dfe1a30` |
| `OOD150_INCLUDED_EPISODES.jsonl` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_INCLUDED_EPISODES.jsonl` | `b97f5a8cbbdf9055665d2bebb193888219d68f157cbf2da4107bac243f974187` |
| `OOD150_EXCLUDED_EPISODES.jsonl` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_EXCLUDED_EPISODES.jsonl` | `c43e0162ddd4310a31a3e4d86d47be3baf93b06ae1603e06f9b7c3384694c30b` |
| `OOD150_FEATURE_AUDIT.json` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_FEATURE_AUDIT.json` | `75d2e2cf1c4dc34c1664c464175b78f9737a8f9e7046fbcb9a4c632d8c961587` |
| `OOD150_MODEL_METRICS.json` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_MODEL_METRICS.json` | `9a6494fffba5ae843fdb0e9a6d0baa78cbe18ec6aba0e3d18f8ce5e7c636f0f1` |
| `OOD150_THRESHOLD_SWEEP.json` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_THRESHOLD_SWEEP.json` | `924fbdd9540b22c04f3e13b65774b90e22cc6b2b635ad6957a245c8a87176c8e` |
| `OOD150_THRESHOLD_SWEEP.csv` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_THRESHOLD_SWEEP.csv` | `62ba36b0c225d9806107286bbc4cf6d578916989c40a5bfd1bfd98d82bc3defa` |
| `OOD150_THRESHOLD_SWEEP.md` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_THRESHOLD_SWEEP.md` | `04dd9b8fe855044ad0b6417a858bba6d881aa003c3ef65a40af358a8fd49775d` |
| `OOD150_PAPER_STYLE_TABLE.md` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_PAPER_STYLE_TABLE.md` | `e2988d803f9404fb4f3d5df3400e83e1137a8a20cf8ed8d721935109340fb7aa` |
| `SEEN_VS_OOD_PAPER_TABLE.md` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/SEEN_VS_OOD_PAPER_TABLE.md` | `5265a31b191c0376bd6a874ffbf555269364d077971070c0c5b5ce2e1d70f19f` |
| `OOD150_SCORES.jsonl` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_SCORES.jsonl` | `04d0bb6f3fea62871b7cedc576e63ee220deadd2942240b2a8b7da4937aba229` |
| `README.md` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/README.md` | `477697bd6b70ca6d74e4a72a2a0b693574ca89465a683fb1e298117e0f33860d` |
| `LOCAL_SOURCE_PATHS.txt` | `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/LOCAL_SOURCE_PATHS.txt` | `9ee0963ed74f8b94661bbbe434088cfa0c1d687e59e121761ec65191c4b7fbad` |
