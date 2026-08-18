# Dean Isaac OOD400 Future Evaluation Setup

Status: **SETUP ONLY — DO NOT RUN**

This package freezes the new 400-scene Isaac OOD benchmark for future evaluation after the current HARD1000 collection finishes.

Canonical source manifest expected SHA-256:

`264dae5a7de872e5aee0a9554f88adfe7af3d38b5a7e29fd7f9b3e0d1c10da41`

The manifest itself is to be copied byte-for-byte into:

`automation/generated/locked_ood400_v1/manifest.json`

and verified against the SHA above before any future evaluation.

## Scientific role

- Candidate role: independent future confirmation benchmark for the already-frozen SimVLA true-H10 V1 detector/controller.
- Do not use OOD400 for training, normalization, model selection, threshold calibration, controller-cap tuning, or early stopping.
- The current SimVLA controller was frozen before this OOD400 manifest was introduced into this project.
- The manifest provenance says it was previously intended/used for Mimic Video risk OOD evaluation; therefore do not describe OOD400 as an untouched holdout for the Mimic/world-model branch without a separate provenance audit.
- Preserve the existing OOD150 result. OOD400 is a future confirmation benchmark, not a replacement that erases OOD150 history.

## Future comparison design

When eventually authorized, evaluate two frozen arms on the exact same 400-scene membership:

1. baseline/shadow arm: same live nine-candidate generation/scoring stack, but always execute candidate 0;
2. active arm: same stack with the already-frozen controller `A=0.7990124225616455`, `C=0.9`, `M=0.0`.

No threshold or controller changes may be made after looking at OOD400 outcomes.

## Current prohibition

Do not launch Isaac, SimVLA evaluation, baseline, shadow, active-controller evaluation, or any OOD400 rollout while HARD1000 is still running.
