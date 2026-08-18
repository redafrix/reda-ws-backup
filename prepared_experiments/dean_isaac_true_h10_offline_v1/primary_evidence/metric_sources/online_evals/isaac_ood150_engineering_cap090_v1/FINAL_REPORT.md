# Definitive Active Online OOD150 Result (Engineering Cap 0.90)

## Executive Summary
- **Protocol ID:** `isaac_ood150_definitive_active_cap090_v1`
- **Main Alarm Threshold ($A$):** `0.7990124225616455` (Seen V1 `best_val_f1`)
- **Alternative Safe Cap ($C$):** `0.9` (Engineering development-informed operating point)
- **Minimum Delta ($M$):** `0.0`
- **Active Success Count:** **75 / 150** (50.0%)
- **Historical Baseline Success Count:** **72 / 150** (48.0%)
- **Net Absolute Delta:** **+3 episodes** (+2.0 percentage points)

## Provenance Note
- **Main Detector Threshold:** Seen-calibrated (`best_val_f1` on seen validation split).
- **Alternative Cap:** Engineering development-informed (derived from preserved live 9-candidate OOD decisions).
- **Evaluation Status:** Active engineering evaluation on locked OOD150 membership (NOT a pristine untouched OOD holdout for controller selection).

## Paired Analysis
- **Rescues (Baseline Fail -> Active Success):** 11
- **Regressions (Baseline Success -> Active Fail):** 8
- **Persisted Successes:** 64
- **Persisted Failures:** 67

## Controller Decision Statistics
- **Total Online Decisions:** 5757
- **Total Alarms:** 3327
- **Accepted Action Replacements:** 57
- **Episodes with Interventions:** 36 / 150
- **Candidate Replacement Histogram:** `{'1': 9, '4': 9, '6': 12, '7': 7, '3': 6, '5': 6, '2': 6, '8': 2}`
