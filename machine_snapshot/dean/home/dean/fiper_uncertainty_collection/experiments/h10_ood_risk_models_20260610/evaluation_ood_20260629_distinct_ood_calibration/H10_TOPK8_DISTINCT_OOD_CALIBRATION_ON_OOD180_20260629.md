# H10 TopK8 Distinct-OOD Calibration Applied to OOD180

Calibration source: `selected_cap_t03_c04_100ep_20260610` risk TopK8 step scores, 1800 episodes, distinct from OOD180 test. This is not seen-only; it is an OOD calibration split with different episodes/seeds.

## actual_max800

| Policy | Row Th | Mass Th | Calib FA | Calib Det | Test FA | Test Det | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cal_q95_oodcal_success_FA01 | 0.9516 | 0.2568 | 1.0% | 83.1% | 53.7% | 100.0% | 90.3% | 96.8% | 0.151 | 0.0% |
| cal_q97_oodcal_success_FA01 | 0.9678 | 0.1136 | 1.0% | 84.7% | 53.7% | 100.0% | 90.3% | 96.8% | 0.151 | 0.0% |
| cal_q99_oodcal_success_FA01 | 0.9924 | 0.0025 | 1.0% | 84.7% | 54.4% | 96.8% | 87.1% | 93.5% | 0.156 | 3.2% |
| cal_q95_oodcal_success_FA02 | 0.9516 | 0.1361 | 2.5% | 91.5% | 57.7% | 100.0% | 90.3% | 96.8% | 0.147 | 0.0% |
| cal_q95_oodcal_supervised_FAle05 | 0.9516 | 0.1741 | 2.1% | 91.5% | 57.7% | 100.0% | 90.3% | 96.8% | 0.148 | 0.0% |
| cal_q97_oodcal_success_FA02 | 0.9678 | 0.0490 | 2.5% | 91.5% | 58.4% | 100.0% | 90.3% | 96.8% | 0.147 | 0.0% |
| cal_q99_oodcal_supervised_FAle50 | 0.9924 | 0.0015 | 1.1% | 88.1% | 55.7% | 96.8% | 87.1% | 93.5% | 0.155 | 3.2% |
| cal_q99_oodcal_supervised_FAle40 | 0.9924 | 0.0015 | 1.1% | 88.1% | 55.7% | 96.8% | 87.1% | 93.5% | 0.155 | 3.2% |

## cap300_forensic

| Policy | Row Th | Mass Th | Calib FA | Calib Det | Test FA | Test Det | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cal_q95_oodcal_success_FA01 | 0.9516 | 0.2568 | 1.0% | 83.1% | 53.1% | 89.2% | 13.5% | 86.5% | 0.298 | 10.8% |
| cal_q97_oodcal_success_FA01 | 0.9678 | 0.1136 | 1.0% | 84.7% | 53.1% | 89.2% | 13.5% | 86.5% | 0.298 | 10.8% |
| cal_q99_oodcal_success_FA01 | 0.9924 | 0.0025 | 1.0% | 84.7% | 53.8% | 86.5% | 13.5% | 83.8% | 0.313 | 13.5% |
| cal_q95_oodcal_success_FA02 | 0.9516 | 0.1361 | 2.5% | 91.5% | 57.3% | 89.2% | 16.2% | 86.5% | 0.287 | 10.8% |
| cal_q95_oodcal_supervised_FAle05 | 0.9516 | 0.1741 | 2.1% | 91.5% | 57.3% | 89.2% | 16.2% | 86.5% | 0.290 | 10.8% |
| cal_q99_oodcal_supervised_FAle50 | 0.9924 | 0.0015 | 1.1% | 88.1% | 55.2% | 86.5% | 13.5% | 83.8% | 0.308 | 13.5% |
| cal_q99_oodcal_supervised_FAle40 | 0.9924 | 0.0015 | 1.1% | 88.1% | 55.2% | 86.5% | 13.5% | 83.8% | 0.308 | 13.5% |
| cal_q99_oodcal_supervised_FAle30 | 0.9924 | 0.0015 | 1.1% | 88.1% | 55.2% | 86.5% | 13.5% | 83.8% | 0.308 | 13.5% |
