# Stage 9 Dense 15h Bob Live Report

- Started: 2026-05-20 16:57:30
- Deadline epoch: 1779343050
- Data root: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v3_20260520`
- Policy: Bob only, real SimVLA seeds only, dense failed-episode timestep scan.
- Parent max steps: 400
- Replay starts at env step 10.
- Stop step by horizon: H10=390, H20=380, H40=360.
- Scorer v3 fixes: phase does not use absolute table-object z as transport; weak approach progress becomes GOOD_WEAK/low risk.


## 2026-05-20 16:57:30

Bob-only queue launched. Sam is intentionally unused.

## 2026-05-20 16:57:30

Starting `h10_full_task012_seed11`: H=10, stop_step=390, max_replay_states=0, task_ids=0 1 2, timeout=54000s.

## 2026-05-20 19:55:42

Finished `h10_full_task012_seed11` with status 0. Replay samples=76200; same-state groups=381; output=`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v3_20260520/h10_full_task012_seed11`.

## 2026-05-20 19:55:42

Starting `h20_mid_task012_seed21`: H=20, stop_step=380, max_replay_states=220, task_ids=0 1 2, timeout=43308s.

## 2026-05-20 22:37:07

Finished `h20_mid_task012_seed21` with status 0. Replay samples=44000; same-state groups=220; output=`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v3_20260520/h20_mid_task012_seed21`.

## 2026-05-20 22:37:07

Starting `h40_short_task012_seed31`: H=40, stop_step=360, max_replay_states=120, task_ids=0 1 2, timeout=33623s.

## 2026-05-21 01:09:58

Finished `h40_short_task012_seed31` with status 0. Replay samples=24000; same-state groups=120; output=`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v3_20260520/h40_short_task012_seed31`.

## 2026-05-21 01:09:58

Starting `h10_full_task012_seed41`: H=10, stop_step=390, max_replay_states=0, task_ids=0 1 2, timeout=24452s.

## 2026-05-21 04:08:24

Finished `h10_full_task012_seed41` with status 0. Replay samples=76200; same-state groups=381; output=`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v3_20260520/h10_full_task012_seed41`.

## 2026-05-21 04:08:24

Starting `h20_mid_task012_seed51`: H=20, stop_step=380, max_replay_states=220, task_ids=0 1 2, timeout=13746s.

## 2026-05-21 06:50:35

Finished `h20_mid_task012_seed51` with status 0. Replay samples=44000; same-state groups=220; output=`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_15h_bob_v3_20260520/h20_mid_task012_seed51`.

## 2026-05-21 06:50:35

Starting `h40_short_task012_seed61`: H=40, stop_step=360, max_replay_states=120, task_ids=0 1 2, timeout=4015s.
