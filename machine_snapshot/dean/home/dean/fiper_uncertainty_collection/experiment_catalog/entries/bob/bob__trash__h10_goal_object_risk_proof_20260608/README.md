# h10_goal_object_risk_proof_20260608

- **Catalog ID:** `bob:trash/h10_goal_object_risk_proof_20260608`
- **Host:** `bob`
- **Kind:** `realtime_run`
- **Status:** `complete_with_results`
- **Original path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608`
- **Checkpoint/model meaning:** SimVLA ckpt-60000 + H10-retrained Risk Detectors
- **Trust level:** High; verified seed parity and results
- **Catalog generated:** 2026-06-08

## What This Result Means

This is the main H10 specialization campaign. It compared the modified SimVLA greedy baseline against conservative (q95) H10-retrained risk detectors (base and unc_topk8) across multiple tasks with a fixed execution horizon of 10.

## Episode Results

| Task | Policy | Success | Failure | SR | Mean steps |
|---|---|---:|---:|---:|---:|
| Task 3 | Greedy (modified_simvla) | 17 | 83 | 17.0% | 278.10 |
| Task 3 | Risk-TopK8 (conservative) | 17 | 83 | 17.0% | 278.12 |
| Task 6 | Greedy (modified_simvla) | 57 | 43 | 57.0% | 200.77 |
| Task 6 | Risk-TopK8 (conservative) | 57 | 43 | 57.0% | 197.97 |

## Navigation

Connect to `bob` and inspect `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608`.
Full results for other policies (original_simvla, risk_base) are available in the raw JSONL files.
