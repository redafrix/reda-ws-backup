# Correction Note: Offline Selection Bug

## Discovery
A deterministic bug was discovered in the offline threshold selection script `offline_sweep.py`. The `conservative` selector helper function had a default parameter `maximize="det25"`. When called with `minimize="fa"`, the `maximize` branch executed first because it was not explicitly disabled. As a result, it improperly ranked and selected `q90_success` instead of the correct lowest false-alarm threshold.

## Corrected Shortlist
The correct shortlist per the protocol is:
- **Aggressive**: `q95_success` (highest test Det@25 among thresholds with test success false-alarm <= 20% and total failure detection >= 95%)
- **Balanced**: `fixed_0.5` (highest test Det@25 among thresholds with test success false-alarm <= 10% and total failure detection >= 95%)
- **Conservative**: `best_val_f1` (lowest test success false-alarm among thresholds with total failure detection >= 95%)

## Final Controller Selection
Based on the corrected shortlist and the audited locked OOD150 metrics:
1. `q95_success`: FA = 26.39%, det = 100%, Det@25 = 58.97%
2. `fixed_0.5`: FA = 12.50%, det = 100%, Det@25 = 53.85%
3. `best_val_f1`: FA = 1.39%, det = 100%, Det@25 = 39.74%

Our deterministic OOD ranking rule prefers OOD success FA <= 10%. Only `best_val_f1` meets this constraint (1.39% <= 10%).
Therefore, the corrected protocol-selected MAIN ALARM THRESHOLD is `best_val_f1 = 0.7990124225616455`.

The selected alternative risk cap remains `q90_success = 0.2370966076850891`.

## Aborted Run and Definitive Campaign
Before the bug was discovered, an initial run was briefly attempted with `fixed_0.5`. That process was stopped cleanly during initialization (0 completed full-campaign episodes logged) to prevent waste of compute on an unverified controller. 

The single definitive active online campaign for all 150 locked OOD scenes was then launched using the verified, corrected controller (`best_val_f1 = 0.7990124225616455` and `q90_success = 0.2370966076850891` alternative safety cap).
