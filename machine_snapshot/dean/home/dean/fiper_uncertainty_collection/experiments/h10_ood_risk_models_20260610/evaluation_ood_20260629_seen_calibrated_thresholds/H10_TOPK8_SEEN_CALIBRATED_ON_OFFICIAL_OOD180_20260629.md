# H10 TopK8 Seen-Calibrated Thresholds Applied to Official OOD180

Protocol: train/model unchanged; row thresholds and mass thresholds selected only from seen `libero_goal_object` buckets on Bob. The official `libero_goal_object_ood` 180 episode dataset is used only once as final test.

## actual_max800

- Rows: `44630`
- Episodes: `180`

| Policy | Row Th | Mass Th | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| q99_seen_success_FA010 | 0.9666 | 0.0560 | 57.7% | 100.0% | 22.6% | 90.3% | 96.8% | 0.147 | 0.0% |
| q99_seen_supervised_FAle25 | 0.9666 | 0.0029 | 66.4% | 100.0% | 48.4% | 93.5% | 100.0% | 0.106 | 0.0% |
| q97_seen_success_FA025 | 0.7686 | 0.4166 | 84.6% | 100.0% | 67.7% | 100.0% | 100.0% | 0.090 | 0.0% |
| q95_seen_success_FA025 | 0.6155 | 1.2979 | 86.6% | 100.0% | 90.3% | 100.0% | 100.0% | 0.072 | 0.0% |
| q97_seen_supervised_FAle25 | 0.7686 | 0.1751 | 89.3% | 100.0% | 83.9% | 100.0% | 100.0% | 0.086 | 0.0% |
| q95_seen_supervised_FAle25 | 0.6155 | 0.7010 | 91.9% | 100.0% | 100.0% | 100.0% | 100.0% | 0.053 | 0.0% |
| q95_seen_supervised_FAle10 | 0.6155 | 0.7010 | 91.9% | 100.0% | 100.0% | 100.0% | 100.0% | 0.053 | 0.0% |
| q95_seen_success_FA050 | 0.6155 | 0.2467 | 94.6% | 100.0% | 100.0% | 100.0% | 100.0% | 0.032 | 0.0% |
| saved_original_q95_mass_0.15 | 0.6155 | 0.1500 | 96.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.025 | 0.0% |

## cap300_forensic

- Rows: `28031`
- Episodes: `180`

| Policy | Row Th | Mass Th | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| q99_seen_success_FA010 | 0.9666 | 0.0560 | 57.3% | 89.2% | 2.7% | 16.2% | 86.5% | 0.287 | 10.8% |
| q99_seen_supervised_FAle25 | 0.9666 | 0.0029 | 66.4% | 94.6% | 2.7% | 27.0% | 89.2% | 0.277 | 5.4% |
| q97_seen_success_FA025 | 0.7686 | 0.4166 | 84.6% | 94.6% | 5.4% | 40.5% | 91.9% | 0.233 | 5.4% |
| q95_seen_supervised_FAle25 | 0.6155 | 0.7010 | 91.6% | 100.0% | 29.7% | 89.2% | 100.0% | 0.142 | 0.0% |
| q95_seen_supervised_FAle10 | 0.6155 | 0.7010 | 91.6% | 100.0% | 29.7% | 89.2% | 100.0% | 0.142 | 0.0% |
| q95_seen_success_FA025 | 0.6155 | 1.2979 | 86.7% | 94.6% | 16.2% | 56.8% | 94.6% | 0.190 | 5.4% |
| q95_seen_success_FA050 | 0.6155 | 0.2467 | 94.4% | 100.0% | 51.4% | 100.0% | 100.0% | 0.092 | 0.0% |
| q97_seen_supervised_FAle25 | 0.7686 | 0.1751 | 89.5% | 94.6% | 5.4% | 48.6% | 91.9% | 0.223 | 5.4% |
| saved_original_q95_mass_0.15 | 0.6155 | 0.1500 | 95.8% | 100.0% | 62.2% | 100.0% | 100.0% | 0.078 | 0.0% |

## Key Interpretation

- `saved_original_q95_mass_0.15` is the old seen-calibrated online point. It over-alarms on OOD.
- `*_seen_success_*` thresholds use only success episodes for calibration, closest to conformal/FIPER style.
- `*_seen_supervised_*` thresholds use seen validation successes plus seen validation failures. This is legitimate for our supervised risk model and is not available to original FIPER, but must be labeled as supervised calibration.
- No threshold in this report is selected from OOD performance.
