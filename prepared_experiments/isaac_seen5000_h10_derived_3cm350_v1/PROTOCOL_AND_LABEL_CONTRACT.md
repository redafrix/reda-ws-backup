# Protocol and Label Contract: isaac_seen5000_h10_derived_3cm350_v1

## 1. Provenance & Scale
- Total episodes: 5,000 (4,000 Seen Round-0 + 1,000 Hard Round-2).
- Unique scene fingerprints: 5,000 / 5,000 (zero collisions).
- Maximum Horizon: 350 control ticks @ 30 Hz (equivalent to $\le 35$ decision queries in H10 chunking; `decision_index <= 34`).
- Total retained decision rows: 100,173 (73,303 Seen + 26,870 Hard).

## 2. Label Provenance Contract
Legacy data stores `summary.minimum_tcp_distance_m` (full-episode scalar) and decision rows at the 3 Hz query rate, but lacks 30 Hz continuous distance traces.

### A. exact_label (Ternary: 0, 1, -1)
- **0 (Exact Success)**: `original_outcome == "success"` AND `original_completed_step <= 1400` (<=350 control ticks).
  - Proves distance reached $\le 0.020$ m ($\le 0.030$ m) before the 350-tick cap.
  - Count: 4,387 (Seen: 3,908, Hard: 479).
- **1 (Exact Failure)**: `minimum_tcp_distance_m > 0.030`.
  - If minimum over entire 2,400-step episode was $>3.0$ cm, it could not have entered $\le 3.0$ cm in the first 350 ticks.
  - Count: 517 (Seen: 47, Hard: 470).
- **-1 (Timing Ambiguous)**:
  - Original failures with `minimum_tcp_distance_m <= 0.030` (95 episodes: 45 Seen, 50 Hard) where entry time is unrecorded.
  - Original successes with `completed_step > 1400` (1 episode: `r002_s003101` in Hard) where 3cm entry timing relative to tick 350 is unrecorded.
  - Count: 96 (Seen: 45, Hard: 51).

### B. heuristic_label_3cm350 (Binary: 0, 1)
- Diagnostic binary label assigning full-episode minimum $\le 3.0$ cm as success (`0`) and timeout $>1400$ as failure (`1`).
- Count: 4,482 success, 518 failure.

### C. Training Eligibility
- `training_eligible_exact`: `True` iff `exact_label in (0, 1)`. `False` for all 96 ambiguous episodes.
- `training_eligible_heuristic`: `False` by default for ambiguous episodes.

## 3. Feature Contract
- History: `(16, 21)` float32.
- Action: `(10, 7)` float32 (main candidate chunk normalized).
- Static: `(51,)` float32 (action statistics 28D + ACE features 7D + proprio 8D + TopK8 SimVLA uncertainty 8D).
- Maximum decision index: `34`.
