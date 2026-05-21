# Stage 9 Dense 15h Bob V5 Live Report

- Started: 2026-05-21 09:33:54
- Deadline epoch: 1779402834
- Data root: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v5_20seed_evalhorizon_20260521`
- Policy: Bob only, real SimVLA seeds only, dense failed-episode timestep scan.
- Parent max steps: 400.
- Replay starts at env step 10.
- Replay seeds per state: 20.
- Target action chunk: first 10 SimVLA actions.
- Scoring/evidence horizons: 10, 20, and 40 steps. H20/H40 continue with SimVLA policy after the initial 10-action target chunk.
- Fixes active: env runtime counters restored on same-state replay; phase does not use absolute table-object z as transport; weak approach progress becomes GOOD_WEAK/low risk.


## 2026-05-21 09:33:54

Bob-only V5 eval-horizon queue launched. Sam is intentionally unused.

## 2026-05-21 09:33:54

Starting `h10_libero_spatial_with_mug_task0_round0`: suite=libero_spatial_with_mug, task_id=0, target_chunk=10, eval_horizon=10, max_states=0, 20 seeds/state, timeout=54000s.
