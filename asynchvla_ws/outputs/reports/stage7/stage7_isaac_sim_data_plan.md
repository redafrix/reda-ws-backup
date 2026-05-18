# Stage 7 Isaac Sim Data Plan

## Purpose

Prepare a future dataset that tests whether SimVLA uncertainty predicts execution risk/progress, not just normalized expert-action L2.

## Proposed Tasks

- Pick-and-place with object swaps: bowl, mug, plate, drawer, cabinet, basket.
- Spatial rearrangement tasks with same object but altered target relations.
- Distractor-object tasks where image novelty alone should not imply high uncertainty.
- Initial-state perturbations: object pose, robot start pose, lighting/camera offsets.
- Instruction perturbations: same scene with different target object/relation.

## Data To Collect Per Decision Context

- Observation images matching SimVLA views.
- Language instruction/task ID.
- Robot proprio/state in the same 8D format used by SimVLA.
- Expert action chunk aligned to SimVLA `[10,7]` normalized and postprocessed formats.
- Multiple SimVLA generated action chunks for seeds `0..4`.
- Optional bad/counterfactual candidate actions: wrong task, wrong object, perturbations.
- Short-horizon progress labels after executing a candidate action.
- Final success/failure as evaluation label, not the only training target.

## Progress Labels

- Reward delta if available.
- Distance-to-goal reduction.
- Object pose error reduction.
- Gripper-object distance reduction for grasp phases.
- Success within horizon H.
- Collision/unsafe event if available.

## Schema Alignment

The Isaac dataset should match current rater fields:

- `context_id`
- `task_name`
- `language_instruction`
- `proprio`
- `pooled_vlm_features`
- `candidate_action_normalized [10,7]`
- `target_expert_action_normalized [10,7]`
- `true_chunk_l2_error`
- `progress_label`
- `candidate_type`
- `split`

## Scale

Pilot: 5 tasks, 20 demos/task, 5 seeds/context, 50-100 counterfactual candidates/task.

Paper-scale: 20-50 tasks, 50 demos/task, controlled ID/OOD splits by object, scene, initial state, and instruction.

## Next Step

Do not implement Isaac Sim collection yet. First finish LIBERO execution rollout validation and decide whether action-L2 is sufficient or whether progress/next-state labels must become the main target.
