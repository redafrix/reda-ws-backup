# asynchvla_ws

AsyncVLA-inspired SimVLA action-error uncertainty workspace.

Goal: estimate how wrong a candidate/generated SimVLA flow-matching action chunk is compared with the expert action for the same LIBERO observation.

This workspace is separate from TDQC and does not train an OOD detector or terminal failure predictor.

Current status: stopped at Phase 2 because checkpoint loading requires local SmolVLM backbone files that were not found on Bob. See `ASYNCVLA_SIMVLA_IMPLEMENTATION_REPORT.md` and `outputs/reports/checkpoint_smoke_test.md`.
