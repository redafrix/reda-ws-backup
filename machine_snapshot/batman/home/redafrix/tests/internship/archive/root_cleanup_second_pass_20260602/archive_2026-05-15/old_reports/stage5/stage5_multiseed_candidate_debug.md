# Stage 5 Multi-Seed Candidate Debug Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`
Workspace: `/media/rootalkhatib/My Passport/reda_ws`
Branch: `bob`
Date: 2026-05-13

## 1. Candidate Debug Dataset Status

Status: `OK`

Dataset:
`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/stage5_debug/multiseed_candidate_debug.pt`

Builder:
`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_multiseed_candidate_dataset.py`

Command:
```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
python3 asynchvla_ws/src/data_building/build_multiseed_candidate_dataset.py --debug true
```

## 2. Dataset Properties

- **Number of Contexts:** 50
- **Number of Candidates:** 500
- **Candidates per Context:** 10
- **File Size:** 2.80 MB

## 3. Candidate Types and True Error Statistics

| Candidate Type | Count | Mean True Error | Min Error | Max Error |
| --- | --- | --- | --- | --- |
| `expert_action` | 50 | 0.0000 | 0.0000 | 0.0000 |
| `simvla_seed0` | 50 | 1.5281 | 0.3198 | 2.7826 |
| `simvla_seed1` | 50 | 1.5119 | 0.3313 | 2.6603 |
| `simvla_seed2` | 50 | 1.4843 | 0.3338 | 2.5982 |
| `simvla_seed3` | 50 | 1.5402 | 0.3443 | 2.7052 |
| `simvla_seed4` | 50 | 1.4850 | 0.3455 | 2.5581 |
| `perturb_small` | 50 | 0.2575 | 0.2154 | 0.3056 |
| `perturb_large` | 50 | 1.9046 | 1.6185 | 2.2654 |
| `same_task_far` | 50 | 0.6348 | 0.2505 | 0.9860 |
| `other_demo_or_other_task` | 50 | 0.7795 | 0.2670 | 1.2516 |

## 4. Same-Context Anti-Cheat Proof

To ensure the rater evaluates action-error sensitivity directly, `pooled_vlm_features`, `proprio`, and `target_expert_action_normalized` MUST be identical for all candidates corresponding to the same `context_id`. Only `candidate_action_normalized` varies.

**Proof on 3 contexts:**

*Context: debug_ctx_0000017*
- Types found: `['expert_action', 'simvla_seed0', 'simvla_seed1', 'simvla_seed2', 'simvla_seed3', 'simvla_seed4', 'perturb_small', 'perturb_large', 'same_task_far', 'other_demo_or_other_task']`
- pooled VLM identical across candidates: True
- proprio identical across candidates: True
- target expert action identical across candidates: True

*Context: debug_ctx_0000024*
- Types found: `['expert_action', 'simvla_seed0', 'simvla_seed1', 'simvla_seed2', 'simvla_seed3', 'simvla_seed4', 'perturb_small', 'perturb_large', 'same_task_far', 'other_demo_or_other_task']`
- pooled VLM identical across candidates: True
- proprio identical across candidates: True
- target expert action identical across candidates: True

*Context: debug_ctx_0000002*
- Types found: `['expert_action', 'simvla_seed0', 'simvla_seed1', 'simvla_seed2', 'simvla_seed3', 'simvla_seed4', 'perturb_small', 'perturb_large', 'same_task_far', 'other_demo_or_other_task']`
- pooled VLM identical across candidates: True
- proprio identical across candidates: True
- target expert action identical across candidates: True

## 5. Conclusion
Phase 2 completed successfully. Candidate dataset effectively pairs context observations with expert, small/large perturbations, far frames, and 5 distinct SimVLA-generated chunks per state.
