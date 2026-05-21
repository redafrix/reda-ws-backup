# Stage 9 Dense 15h Bob V6 Live Report

- Started: 2026-05-21 10:01:59
- Deadline epoch: 1779404519
- Data root: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v6_parserfix_scorerfix_20seed_evalhorizon_20260521`
- Policy: Bob only, real SimVLA seeds only, dense failed-episode timestep scan.
- Parent max steps: 400.
- Replay starts at env step 10.
- Replay seeds per state: 20.
- Target action chunk: first 10 SimVLA actions.
- Scoring/evidence horizons: 10, 20, and 40 steps. H20/H40 continue with SimVLA policy after the initial 10-action target chunk.
- Fixes active: env runtime counters restored on same-state replay; pick/place task parser v2 preserves target/goal roles; same-state strong-progress alternatives raise action-specific no-progress risk; phase does not use absolute table-object z as transport; weak approach progress becomes GOOD_WEAK/low risk.


## 2026-05-21 10:01:59

Bob-only V6 parser/scorer-fix eval-horizon queue launched. Sam is intentionally unused.

## 2026-05-21 10:01:59

Starting `h10_libero_spatial_with_mug_task0_round0`: suite=libero_spatial_with_mug, task_id=0, target_chunk=10, eval_horizon=10, max_states=0, 20 seeds/state, timeout=54000s.

## 2026-05-21 10:41:45

Finished `h10_libero_spatial_with_mug_task0_round0` with status 0. Replay samples=7620; same-state groups=381; output=`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v6_parserfix_scorerfix_20seed_evalhorizon_20260521/h10_libero_spatial_with_mug_task0_round0`.

## 2026-05-21 10:41:45

Starting `h20_libero_spatial_with_mug_task0_round0`: suite=libero_spatial_with_mug, task_id=0, target_chunk=10, eval_horizon=20, max_states=220, 20 seeds/state, timeout=51614s.
