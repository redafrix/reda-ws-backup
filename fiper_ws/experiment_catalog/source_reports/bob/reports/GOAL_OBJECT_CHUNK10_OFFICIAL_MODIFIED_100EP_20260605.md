# Goal-Object Chunk10 Official vs Modified SimVLA Diagnostic

Date: 2026-06-05

## Roots

- Modified SimVLA: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/goal_object_modified_simvla_chunk10_100_20260605`
- Official SimVLA: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/goal_object_official_simvla_chunk10_100_20260605`

## Setup

- Host: Bob (`pcrobot`)
- Suite: `libero_goal_object`
- Episode bundle: exact reproduction bundle from June 5, 2026
- Scope: 100 episodes, tasks 0-9 and init rows 0-9
- Execution: chunk10 open-loop
- Risk detector: none
- ACE candidates: none
- Uncertainty features: none

## Checkpoints

- Modified SimVLA `ckpt-60000`: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- Official/original SimVLA `YuankaiLuo_SimVLA-LIBERO`: `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be`

## Result

| Policy | Success | Success Rate | Mean Environment Steps |
|---|---:|---:|---:|
| Modified SimVLA `ckpt-60000` | 80/100 | 80.0% | 130.92 |
| Official/original SimVLA | 78/100 | 78.0% | 132.38 |

Paired modified-vs-official comparison:

- Common rows: 100
- Modified rescues over official: 8
- Modified regressions vs official: 6
- Net gain: +2

## Trust

Mechanically valid historical diagnostic. It is not a risk-aware result, and it should not be pooled with H10 OOD risk-aware experiments.
