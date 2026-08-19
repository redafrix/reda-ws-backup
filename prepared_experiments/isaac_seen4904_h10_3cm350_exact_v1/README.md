# Frozen Exact 4,904-Episode Source Dataset: isaac_seen4904_h10_3cm350_exact_v1

## Overview
This directory contains the frozen metadata, contract, and audit evidence for the exact binary 4,904-episode source dataset under the 3.0 cm / 350-control-tick protocol (`decision_index <= 34`).

## Key Dataset Facts
- **Derivation**: Derived entirely offline from raw existing artifacts.
- **Source Pool**: Existing Seen4000 Round-0 (`final_seen_h10_round_000_seed20260730`) + HARD1000 Round-2 (`final_seen_h10_round_002_seed20260804`).
- **No Simulation / No Collection**: No new Isaac collection, no GPU simulation, no policy inference.
- **Exclusions**: 96 timing-unresolvable episodes excluded (45 Seen + 51 Hard) because their exact first <=3cm crossing time relative to the 350-tick horizon cannot be proved from legacy data.
- **Final Dataset**: Exactly 4,904 episodes (3,955 Seen + 949 Hard).
- **Labels**: Strict binary only (0 = Success, 1 = Failure).
  - Success episodes: 4,387 (3,908 Seen + 479 Hard)
  - Failure episodes: 517 (47 Seen + 470 Hard)
- **Total Retained Rows**: 96,813 (Seen: 71,728, Hard: 25,085).
  - Success rows: 78,718
  - Failure rows: 18,095
- **Protocol**: 3cm threshold, 30 Hz control rate, 350 max control ticks (11.6667s), H10 execution (max 35 decision rows, `decision_index <= 34`), NO DWELL, NO SETTLE TIME.
- **Feature Parity**: Checked 71,728 rows against frozen Seen4000 V1 dataset (`max_abs_diff = 0.0` across history, action, static).
- **Supersedes**: This dataset and evidence strictly supersede the obsolete commit `295546aea56dc9ef2a27de72134e9218b0a1f2bc` (which had ambiguous/heuristic 3-class labeling).
