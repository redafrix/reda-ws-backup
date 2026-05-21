# Stage 9 Dense 15h Bob V4 Live Report

- Started: 2026-05-21 09:27:14
- Deadline epoch: 1779402434
- Data root: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v4_20seed_runtimefix_20260521`
- Policy: Bob only, real SimVLA seeds only, dense failed-episode timestep scan.
- Parent max steps: 400.
- Replay starts at env step 10.
- Replay seeds per state: 20.
- True executed candidate horizon: 10 SimVLA actions.
- H20/H40 are disabled here because SimVLA currently emits fixed 10-action chunks; longer horizons need a separate continuation-audit implementation.
- Fixes active: env runtime counters restored on same-state replay; phase does not use absolute table-object z as transport; weak approach progress becomes GOOD_WEAK/low risk.


## 2026-05-21 09:27:14

Bob-only V4 queue launched. Sam is intentionally unused.

## 2026-05-21 09:27:14

Starting `h10_libero_spatial_with_mug_task0_round0`: suite=libero_spatial_with_mug, task_id=0, H10 true chunk, 20 seeds/state, timeout=54000s.
