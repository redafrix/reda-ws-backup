# Stage 9 Mini-Failure Review Pack v7

Generated: 2026-05-22

This pack uses the corrected mini-failure detector with:

- `pre_failure_steps = 60`
- `core_label_steps = 10`
- `pick_confirmation_steps = 60`
- `stable_lift_steps = 30`
- `stable_lift_height = 0.030`
- agent view + wrist view in each frame

The detector no longer treats object motion alone as a good pickup or a failed pickup. A pickup is suppressed as healthy only when the target/same-family object stays held through a sustained confirmation window and does not fall. If the object only bumps upward, drops back down, or the arm comes back to retry, it can be flagged as `unstable_pick_or_failed_lift`.

## Real Trace Results

Bob output:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v7_pre60_core10_stablepick_20260522`

Raw input:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/raw_failure_episodes`

Summary:

- Episodes: 7
- Step labels: 2374
- Chunk labels: 239
- Events: 22
- Event counts: `missed_place=8`, `unstable_pick_or_failed_lift=4`, `wrong_object_picked=10`
- Chunk risk bins: `RISKY_STRONG=26`, `RISKY_WEAK=23`, `SAFE_WEAK=125`, `UNCERTAIN=65`

## Review Videos

Most clips are 70 simulator steps: 60 before onset and 10 failure-core steps. At 20 FPS, this is 3.5 seconds. Clip 02 starts at episode step 0, so it is shorter.

1. `01_missed_place_onset169_libero_spatial_with_mug_t0_r8_pseed2026052108.mp4`
2. `02_unstable_pick_or_failed_lift_onset48_libero_spatial_with_mug_t1_r9_pseed2026052129.mp4`
3. `03_wrong_object_picked_onset131_libero_spatial_with_mug_t0_r1_pseed2026052101.mp4`
4. `04_missed_place_onset114_libero_spatial_with_mug_t0_r8_pseed2026052108.mp4`
5. `05_unstable_pick_or_failed_lift_onset351_libero_spatial_with_mug_t0_r8_pseed2026052108.mp4`
6. `06_wrong_object_picked_onset145_libero_spatial_with_mug_t0_r1_pseed2026052101.mp4`
7. `07_missed_place_onset70_libero_spatial_with_mug_t0_r8_pseed2026052108.mp4`
8. `08_unstable_pick_or_failed_lift_onset319_libero_spatial_with_mug_t0_r8_pseed2026052108.mp4`
9. `09_wrong_object_picked_onset182_libero_spatial_with_mug_t0_r4_pseed2026052104.mp4`
10. `10_missed_place_onset128_libero_spatial_with_mug_t0_r8_pseed2026052108.mp4`

## Smoke Test

The synthetic smoke test passes on Bob. It includes:

- `missed_pick`
- `wrong_object`
- `drop`
- `missed_place`
- `unstable_pick`
- healthy pickup negative control

The healthy pickup negative control produces zero events.
