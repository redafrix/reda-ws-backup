# Isaac 3cm/350-Tick Main Risk Model — Primary Paper Evidence Index

This document is the single authoritative index pointing to all primary artifacts, manifests, configurations, hashes, and source commits for the canonical Isaac risk model (`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`).

---

## 1. Source Git Repository & Commits
- **Repository**: `redafrix/reda-ws-backup`
- **Working Branch**: `experiment/dean-isaac-online-ood150-20260817`
- **Local Path**: `/home/redafrix/tests/internship`
- **Primary Commits**:
  - **Dataset Freeze (Exact 4904)**: [`e9f5276f4901adebea8e2d6aa8feeee817046456`](https://github.com/redafrix/reda-ws-backup/commit/e9f5276f4901adebea8e2d6aa8feeee817046456)
  - **Canonical Main Training (Unified Split)**: [`bc2ed0c7ad50e388ae918d46162628c310827971`](https://github.com/redafrix/reda-ws-backup/commit/bc2ed0c7ad50e388ae918d46162628c310827971)
  - **Conformal / Early-Detection Sweep**: [`e053ae6e119b1fceff149cd575f9429636b0cc64`](https://github.com/redafrix/reda-ws-backup/commit/e053ae6e119b1fceff149cd575f9429636b0cc64)

---

## 2. Dataset Artifacts (`isaac_seen4904_h10_3cm350_exact_v1`)
- **Dean Storage Path**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen4904_h10_3cm350_exact_v1`
- **Repo Evidence Path**: `prepared_experiments/isaac_seen4904_h10_3cm350_exact_v1/`
- **Dataset Manifest**: `prepared_experiments/isaac_seen4904_h10_3cm350_exact_v1/manifest.json`
  - **SHA256**: `61462ceead4a79d6d44a0ae80ee9ff25b958c4c1afbd67142c4df276801a0a3c`
- **Excluded Episodes Audit (96 unresolvable episodes)**: `prepared_experiments/isaac_seen4904_h10_3cm350_exact_v1/excluded_episodes.jsonl`
  - **SHA256**: `a937a54b38d356c367fa3b3336fe05886d34e2c815fa25d315998a69e7be46fb`
- **Composition**: 4,904 episodes (4,387 success, 517 failure), 96,813 decision rows (`decision_index <= 34`).

---

## 3. Split & Model Training Artifacts (`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`)
- **Dean Model Directory**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`
- **Repo Evidence Path**: `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/`
- **Split Manifest**: `split_manifest.json` (SHA256: `34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8`)
- **Split Audit**: `SPLIT_AUDIT.json` (SHA256: `765ec0882995694111151eb2bc4cd9dc3311ccd5f46d4618b021df111c78db8a`)
- **Training Config**: `TRAINING_CONFIG.json` (SHA256: `3672a2e2a9cf28f0a5edb1b3bb764127021d1c0bb781d082e39bb152df72ec6c`)
- **Training History**: `training_history.json` (SHA256: `f8af8e7e5f0f627e1c9c6ff162bb976606f1b2767a1a02aed14d387d0b825077`)
- **Validation Thresholds**: `thresholds.json` (SHA256: `43a43e24c96d5820ccd4dc389cca8c8a330cbe2e1682020564adf291a039d1ac`)
- **Locked Test Results**: `test_results.json` (SHA256: `2c3de0d3153ffc58b7f1c228af0eb7515f0dc146439b5307f809593e2da7ce56`)
- **Model Checkpoint on Dean (`model.pt`)**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/model.pt`
  - **SHA256**: `00ad096a9ca38577366e992e1d7f8aa25b6f56f2f2bd7354abce1790baf890f1`
- **Train Normalization on Dean (`norm.npz`)**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/norm.npz`
  - **SHA256**: `6fbd2b221c4490c975e3e1492c96a9e879a586f0b3a4c4eaf97ea05920960341`

---

## 4. Conformal Threshold & Early-Detection Sweep
- **JSON Full Sweep**: `CONFORMAL_THRESHOLD_SWEEP.json` (SHA256: `de7226b1af317cc12af9974aac5b5cc7ca33bc8e5343446eb3b075700d387841`)
- **CSV Full Sweep**: `CONFORMAL_THRESHOLD_SWEEP.csv` (SHA256: `cd74bd64737240a09d5898b858ac7376ea91a85909d190ad47c0bce34fa0ccdb`)
- **Markdown Full Sweep**: `CONFORMAL_THRESHOLD_SWEEP.md` (SHA256: `dfbaa67a7e46941e9a7803eaad2b238fa2a514d2a9a72275d8bc833c5c10fa1b`)

---

## 5. Current External / OOD Transfer Evidence
- **Repo Evidence Path**: [`prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/`](file:///home/redafrix/tests/internship/prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/PAPER_EVIDENCE_INDEX.md)
- **Authoritative OOD Commit**: [`cdd55fbd6958264322b3bc53aea8c63b4edeff33`](https://github.com/redafrix/reda-ws-backup/commit/cdd55fbd6958264322b3bc53aea8c63b4edeff33)
- **Conversion Mode**: `EXACT_ONLY`
- **Scope Statement**: exact-only converted historical OOD150 subset (136/150 episodes)
- **Included Exact Episodes**: **136 episodes** (72 success, 64 failure)
- **Excluded Unresolvable Episodes**: **14 episodes**
- **Retained Rows (`decision_index <= 34`)**: **3,447 rows** (1,207 success, 2,240 failure)
- **OOD Performance**: Query AUROC: **0.9201** | Query AUPRC: **0.9621** | Episode-Balanced AUROC: **0.9954** | Episode-Balanced AUPRC: **0.9940**
