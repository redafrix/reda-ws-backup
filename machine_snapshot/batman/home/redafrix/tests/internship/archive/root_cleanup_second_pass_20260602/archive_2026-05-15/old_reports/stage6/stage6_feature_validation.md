# Stage 6 Feature Validation

- Source dataset: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/processed_stage5/holdout_libero_object/multiseed_candidate_train.pt`
- Rows checked: `500`
- Contexts with seed ensemble stats in checked subset: `50`

## Feature Modes

| Mode | Dim | Finite | Mean abs | Max abs |
|---|---:|---|---:|---:|
| `A0_action_flat` | 70 | `True` | 0.636031 | 3.087732 |
| `A1_context` | 968 | `True` | 0.641698 | 16.531433 |
| `A2_full_old` | 1038 | `True` | 0.641316 | 16.531433 |
| `F1_action_geometry` | 124 | `True` | 0.779686 | 5.767104 |
| `F2_proprio_action_delta` | 36 | `True` | 3.648032 | 28.774900 |
| `F3_seed_ensemble` | 364 | `True` | 1.157379 | 10.339428 |
| `F4_context_action_interactions` | 116 | `True` | 1.113272 | 50.172226 |
| `M2_engineered` | 1562 | `True` | 0.841858 | 28.774900 |
| `M4_seed_relative` | 1526 | `True` | 0.775657 | 16.531433 |
| `M3_gated_base` | 1456 | `True` | 0.782370 | 16.531433 |

## Flow Trace Features

Current Stage 5 candidate datasets do not store denoising/flow path metadata. `F5_flow_trace_features` is pending until trace extraction stores update norms / velocity norms / final-step metadata.
