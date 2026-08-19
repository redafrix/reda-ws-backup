# Stage 1C Summary — TopK8 Best-Val-F1 Threshold Semantics Proof

## 1. Source Artifact Verification
- `thresholds.json` SHA256: `43a43e24c96d5820ccd4dc389cca8c8a330cbe2e1682020564adf291a039d1ac`
- `CONFORMAL_THRESHOLD_SWEEP.json` SHA256: `de7226b1af317cc12af9974aac5b5cc7ca33bc8e5343446eb3b075700d387841`
- `split_manifest.json` SHA256: `34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8`
- `train_isaac_topk8.py` SHA256: `adc0f368c5f277df83590540d3a2bd656ca19ba5228648ef8e4d19a0f640a660`
- `common.py` SHA256: `e89a69592ed75b8bb52850019780f6c8d4309e9a82186c59d3e01afbc2822c46`

## 2. Provenance and Semantics
- Threshold: 0.579133152961731
- Validation-Only Selection: YES (`threshold_table` computed exclusively over validation split predictions)
- Row-Level F1 Argmax: YES (`index = int(np.nanargmax(f1[:len(thresholds)])); best = float(thresholds[index])`)
- Same 735 Validation Episode Partition: YES (bound to `split_manifest.json` SHA `34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8`)
- Test-Independent Selection: YES (`thresholds.json` frozen at model training completion before test scoring)
- Rule Equivalence to Mimic `row_best_f1`: YES (both methods execute exact same validation precision-recall curve argmax-F1 rule)
