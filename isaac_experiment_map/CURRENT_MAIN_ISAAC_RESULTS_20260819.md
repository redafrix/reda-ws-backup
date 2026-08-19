# Current Main Isaac Results & Conformal Detection Evidence — 2026-08-19

> [!NOTE]
> **Scope Statement**: This document defines the CURRENT canonical Isaac main model, exact dataset, locked internal test split results, and zero-shot external transfer evaluation on the exact-only converted historical OOD150 subset (136/150 episodes). Older 2cm / 600-tick / dwell results and V1 models remain preserved as historical benchmarks.

---

## 1. Current Task Protocol & Dataset Definition

### Protocol Specification
- **Task**: Franka reaching in Isaac Sim.
- **Success Rule**: First control tick where `tcp_target_distance_m <= 0.030 m` (3.0 cm) $\implies$ immediate **SUCCESS** (Label 0).
- **Failure Rule**: Episode reaches 350 control ticks without reaching $\le 0.030$ m $\implies$ **FAILURE/TIMEOUT** (Label 1).
- **Dwell / Settle Time**: **NO DWELL** (immediate termination on first crossing).
- **Execution & Rate**: Control rate = 30 Hz, Physics rate = 120 Hz, Decimation = 4, Execution = `H10` (10 actions per decision query, maximum 35 queries / `decision_index <= 34`).

### Canonical Exact Dataset (`isaac_seen4904_h10_3cm350_exact_v1`)
- **Dean Storage Path**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen4904_h10_3cm350_exact_v1`
- **Repo Evidence Path**: `prepared_experiments/isaac_seen4904_h10_3cm350_exact_v1/`
- **Total Source Pool**: 5,000 episodes (4,000 Seen Round-0 + 1,000 HARD Round-2).
- **Included Episodes**: **4,904 episodes** (4,387 success, 517 failure).
- **Excluded Timing-Unresolvable Episodes**: **96 episodes** (45 Seen, 51 Hard) excluded because exact first crossing timing relative to tick 350 could not be resolved from legacy scalar minimum summaries.
- **Total Decision Rows**: **96,813 rows**.
- **Dataset Manifest SHA-256**: `61462ceead4a79d6d44a0ae80ee9ff25b958c4c1afbd67142c4df276801a0a3c`
- **Dataset Freeze Commit**: [`e9f5276f4901adebea8e2d6aa8feeee817046456`](https://github.com/redafrix/reda-ws-backup/commit/e9f5276f4901adebea8e2d6aa8feeee817046456)

---

## 2. Canonical Unified Split & Model Details

### Split Specification (Seed: `20260819`)
- **Stratification Variable**: Binary episode label ONLY (0 = success, 1 = failure).
- **Source Campaign**: Recorded as provenance metadata only; not used for assignment.

| Split | Episodes | Success | Failure | Decision Rows |
|:---|---:|---:|---:|---:|
| **Train** | 3,433 | 3,071 | 362 | 67,725 |
| **Validation** | 735 | 658 | 77 | 14,562 |
| **Test (Locked)** | 736 | 658 | 78 | 14,526 |
| **Total** | **4,904** | **4,387** | **517** | **96,813** |

- **Split Manifest SHA-256**: `34db754f88cc9f77ca72dc358a51235f7059278e561e662103451ec4ef8095b8`
- **Split Audit SHA-256**: `765ec0882995694111151eb2bc4cd9dc3311ccd5f46d4618b021df111c78db8a`

### Canonical Model (`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`)
- **Dean Directory**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`
- **Architecture**: `SeqRiskModel` (width 128, 3 layers, 4 heads, ffn 512, dropout 0.1; 27 tokens = 1 CLS + 16 history + 10 action; static branch 51).
- **Training Recipe**: 10 epochs, AdamW (lr 2e-4, wd 1e-4), batch size 512, pos_weight = 4.3453, seed 20260819.
- **Model Checkpoint SHA-256 (`model.pt`)**: `00ad096a9ca38577366e992e1d7f8aa25b6f56f2f2bd7354abce1790baf890f1`
- **Train Normalization SHA-256 (`norm.npz`)**: `6fbd2b221c4490c975e3e1492c96a9e879a586f0b3a4c4eaf97ea05920960341`
- **Best Epoch**: 9 (selected by highest validation query AUPRC = `0.9020`).
- **Training Commit**: [`bc2ed0c7ad50e388ae918d46162628c310827971`](https://github.com/redafrix/reda-ws-backup/commit/bc2ed0c7ad50e388ae918d46162628c310827971)

---

## 3. Conformal Calibration & Thresholds

- **Calibration Object**: Maximum risk score across all queries in each successful validation episode ($S_e = \max_t p_{\text{failure}}(e, t)$).
- **Calibration Set Size**: $n = 658$ successful validation episodes.
- **Mean Retained Success Test Length**: 17.93 queries ($\approx 179.3$ control ticks).
- **Mean Success Cutoff**: **18 monitor queries** ($\approx 180$ control ticks).

### Conformal Thresholds
- `q50 success` ($\alpha=0.500, k=330$): `0.3667067587375641`
- `q60 success` ($\alpha=0.400, k=396$): `0.4030410051345825`
- `q70 success` ($\alpha=0.300, k=462$): `0.44121062755584717`
- `q75 success` ($\alpha=0.250, k=495$): `0.4608674645423889`
- `q80 success` ($\alpha=0.200, k=528$): `0.48487842082977295`
- `q85 success` ($\alpha=0.150, k=561$): `0.5137637257575989`
- `q90 success` ($\alpha=0.100, k=594$): `0.5631080269813538`
- `q92.5 success` ($\alpha=0.075, k=610$): `0.5950250029563904`
- `q95 success` ($\alpha=0.050, k=627$): `0.6643207669258118`
- `q97.5 success` ($\alpha=0.025, k=643$): `0.7885398268699646`
- `q99 success` ($\alpha=0.010, k=653$): `0.8792325258255005`

---

## 4. Locked Test Results & Threshold Sweep

### Full Conformal Threshold Sweep Table (Locked Test: 736 episodes / 14,526 rows)

| Rule | alpha | tau | Succ FA n/% | Fail Det n/% | Det@25% FailLen n/% | Det@50% FailLen n/% | Det@100% FailLen n/% | Det@100% MeanSuccLen n/% | Never n/% |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Best F1 | - | 0.5791 | 50/7.60% | 78/100.00% | 47/60.26% | 67/85.90% | 78/100.00% | 67/85.90% | 0/0.00% |
| Fixed 0.5 | - | 0.5000 | 115/17.48% | 78/100.00% | 54/69.23% | 71/91.03% | 78/100.00% | 71/91.03% | 0/0.00% |
| q50 success | 0.500 | 0.3667 | 332/50.46% | 78/100.00% | 72/92.31% | 77/98.72% | 78/100.00% | 77/98.72% | 0/0.00% |
| q60 success | 0.400 | 0.4030 | 264/40.12% | 78/100.00% | 69/88.46% | 77/98.72% | 78/100.00% | 77/98.72% | 0/0.00% |
| q70 success | 0.300 | 0.4412 | 192/29.18% | 78/100.00% | 65/83.33% | 75/96.15% | 78/100.00% | 75/96.15% | 0/0.00% |
| q75 success | 0.250 | 0.4609 | 163/24.77% | 78/100.00% | 62/79.49% | 73/93.59% | 78/100.00% | 73/93.59% | 0/0.00% |
| q80 success | 0.200 | 0.4849 | 137/20.82% | 78/100.00% | 58/74.36% | 71/91.03% | 78/100.00% | 71/91.03% | 0/0.00% |
| q85 success | 0.150 | 0.5138 | 96/14.59% | 78/100.00% | 51/65.38% | 70/89.74% | 78/100.00% | 70/89.74% | 0/0.00% |
| q90 success | 0.100 | 0.5631 | 59/8.97% | 78/100.00% | 48/61.54% | 67/85.90% | 78/100.00% | 67/85.90% | 0/0.00% |
| q92.5 success | 0.075 | 0.5950 | 42/6.38% | 78/100.00% | 47/60.26% | 67/85.90% | 78/100.00% | 67/85.90% | 0/0.00% |
| q95 success | 0.050 | 0.6643 | 24/3.65% | 78/100.00% | 43/55.13% | 65/83.33% | 78/100.00% | 65/83.33% | 0/0.00% |
| q97.5 success | 0.025 | 0.7885 | 13/1.98% | 78/100.00% | 35/44.87% | 61/78.21% | 78/100.00% | 61/78.21% | 0/0.00% |
| q99 success | 0.010 | 0.8792 | 8/1.22% | 78/100.00% | 30/38.46% | 58/74.36% | 78/100.00% | 58/74.36% | 0/0.00% |

### Paper-Style Compact Table

| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@MeanSucc100 % | Never % |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| Best F1 | 0.5791 | 7.60% | 100.00% | 60.26% | 85.90% | 100.00% | 85.90% | 0.00% |
| Fixed 0.5 | 0.5000 | 17.48% | 100.00% | 69.23% | 91.03% | 100.00% | 91.03% | 0.00% |
| q90 success | 0.5631 | 8.97% | 100.00% | 61.54% | 85.90% | 100.00% | 85.90% | 0.00% |
| q95 success | 0.6643 | 3.65% | 100.00% | 55.13% | 83.33% | 100.00% | 83.33% | 0.00% |
| q99 success | 0.8792 | 1.22% | 100.00% | 38.46% | 74.36% | 100.00% | 74.36% | 0.00% |

---

---

## 5. Current External / OOD Transfer — Exact-Only Converted Historical OOD150

> [!NOTE]
> **Scope Statement**: This evaluation tests zero-shot operating threshold transfer on the **exact-only converted historical OOD150 subset (136/150 episodes)**. All thresholds were calibrated strictly on Seen VALIDATION data; **no threshold calibration or tuning was performed on OOD data**. Success query lengths are retained legacy query lengths, not exact reconstructed first-3cm termination lengths.

### OOD Scope & Dataset
- **Source Baseline**: Historical 150-episode candidate-0 collection (`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728`).
- **Conversion Mode**: `EXACT_ONLY`.
- **Included Exact Episodes**: **136 episodes** (72 success, 64 failure).
- **Excluded Unresolvable Episodes**: **14 episodes** (`000007`, `000022`, `000023`, `000038`, `000044`, `000084`, `000090`, `000103`, `000114`, `000170`, `000195`, `000226`, `000232`, `000284`) reached $\le 3\text{ cm}$ at some unknown point during the full legacy trajectory, but the first crossing time relative to tick 350 cannot be reconstructed from the saved evidence; their new-protocol outcome is unresolved and they are excluded.
- **Retained Decision Rows (`decision_index <= 34`)**: **3,447 rows** (1,207 success rows, 2,240 failure rows; max decision index: 34).

### Discrimination Performance
- **Query AUROC / AUPRC**: **0.9201 / 0.9621** (AUROC: `0.9200878062492603`, AUPRC: `0.9621235135144359`)
- **Episode-Balanced AUROC / AUPRC**: **0.9954 / 0.9940** (AUROC: `0.9954427083333334`, AUPRC: `0.9939601620974798`)
- **Mean Retained Success Query Length**: `16.76` queries (OOD cutoff: 17 queries / $\approx 170$ control ticks; Canonical Seen cutoff: 18 queries / $\approx 180$ control ticks).

### Conformal & Paper-Style OOD Table (136 episodes / 3,447 rows)

| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@OODMeanSucc100 % | Det@Canonical18Q % | Never % |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Best F1 | 0.5791 | 18.06% | 100.00% | 70.31% | 85.94% | 100.00% | 82.81% | 85.94% | 0.00% |
| Fixed 0.5 | 0.5000 | 25.00% | 100.00% | 75.00% | 89.06% | 100.00% | 89.06% | 89.06% | 0.00% |
| q90 success | 0.5631 | 19.44% | 100.00% | 70.31% | 85.94% | 100.00% | 84.38% | 85.94% | 0.00% |
| q95 success | 0.6643 | 13.89% | 100.00% | 59.38% | 81.25% | 100.00% | 78.12% | 81.25% | 0.00% |
| q99 success | 0.8792 | 5.56% | 100.00% | 42.19% | 75.00% | 100.00% | 67.19% | 75.00% | 0.00% |

### Side-by-Side Comparison: Seen Internal TEST vs Converted OOD150

| Rule | Split | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Never % |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| **Best F1** | **Seen internal TEST** | 0.5791 | 7.60% | 100.00% | 60.26% | 85.90% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5791 | 18.06% | 100.00% | 70.31% | 85.94% | 100.00% | 0.00% |
| **Fixed 0.5** | **Seen internal TEST** | 0.5000 | 17.48% | 100.00% | 69.23% | 91.03% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5000 | 25.00% | 100.00% | 75.00% | 89.06% | 100.00% | 0.00% |
| **q90 success** | **Seen internal TEST** | 0.5631 | 8.97% | 100.00% | 61.54% | 85.90% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5631 | 19.44% | 100.00% | 70.31% | 85.94% | 100.00% | 0.00% |
| **q95 success** | **Seen internal TEST** | 0.6643 | 3.65% | 100.00% | 55.13% | 83.33% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.6643 | 13.89% | 100.00% | 59.38% | 81.25% | 100.00% | 0.00% |
| **q99 success** | **Seen internal TEST** | 0.8792 | 1.22% | 100.00% | 38.46% | 74.36% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.8792 | 5.56% | 100.00% | 42.19% | 75.00% | 100.00% | 0.00% |

---

## 6. Primary Evidence Artifacts & Commits
- **Primary Seen Evidence Directory**: `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/`
- **Primary OOD Evidence Directory**: `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/`
- **Dataset Freeze Commit**: [`e9f5276f4901adebea8e2d6aa8feeee817046456`](https://github.com/redafrix/reda-ws-backup/commit/e9f5276f4901adebea8e2d6aa8feeee817046456)
- **Model Training Commit**: [`bc2ed0c7ad50e388ae918d46162628c310827971`](https://github.com/redafrix/reda-ws-backup/commit/bc2ed0c7ad50e388ae918d46162628c310827971)
- **Conformal Sweep Commit**: [`e053ae6e119b1fceff149cd575f9429636b0cc64`](https://github.com/redafrix/reda-ws-backup/commit/e053ae6e119b1fceff149cd575f9429636b0cc64)
- **OOD Evaluation Commit**: [`cdd55fbd6958264322b3bc53aea8c63b4edeff33`](https://github.com/redafrix/reda-ws-backup/commit/cdd55fbd6958264322b3bc53aea8c63b4edeff33)
