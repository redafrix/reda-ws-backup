# SimVLA Modified - Phase 1 Uncertainty Changes

This repo is a working copy of:

- [SimVLA baseline](/home/redafrix/tests/intern_ship_research/intern_ship_ws/SimVLA)

The baseline repo stays untouched for baseline comparisons.

This modified repo is where phase-1 uncertainty was implemented.

---

## Scope of the change

Phase 1 adds only:

1. one uncertainty head on top of the action transformer
2. one uncertainty-aware training loss
3. one inference method that returns uncertainty tensors

Phase 1 does **not** add:

- repeated sampling
- AAC entropy
- medoid selection
- calibrator
- branch-risk outputs
- server API changes

---

## Files modified

### 1. `models/configuration_smolvlm_vla.py`

Added config fields:

- `predict_uncertainty`
- `uncertainty_beta`
- `uncertainty_eps`
- `return_uncertainty`

Purpose:

- make the new feature checkpoint-visible
- allow old checkpoints to keep loading with uncertainty disabled by default

---

### 2. `models/transformer_smolvlm.py`

Changed the action transformer head.

#### Old behavior

- concat mode:
  - one `action_decoder`
- AdaLN mode:
  - one `final_layer`

#### New behavior

If `predict_uncertainty=False`:

- keep old single-head behavior

If `predict_uncertainty=True`:

- concat mode:
  - `velocity_head`
  - `logvar_head`
- AdaLN mode:
  - `velocity_final_layer`
  - `logvar_final_layer`

Changed return contract:

- old:
  - returns `v_t`
- new:
  - if uncertainty disabled:
    - returns `v_t`
  - if uncertainty enabled:
    - returns `(v_t, logvar_t)`

No changes were made to:

- attention
- transformer blocks
- MLP blocks
- positional embeddings

---

### 3. `models/modeling_smolvlm_vla.py`

This file got the main logic changes.

#### 3.1 Transformer construction

The model now passes:

- `predict_uncertainty=config.predict_uncertainty`

into `SmolVLMActionTransformer`.

#### 3.2 Legacy checkpoint upgrade path

Added:

- `_init_uncertainty_heads_from_legacy(...)`
- `_upgrade_legacy_state_dict_for_uncertainty(...)`
- `_maybe_copy_legacy_output_head(...)`
- custom `from_pretrained(...)`
- custom `load_state_dict(...)`

Purpose:

- old official checkpoints have only one output head
- new model has:
  - velocity head
  - log-variance head

What happens now when loading the official checkpoint with uncertainty enabled:

- old velocity head weights are copied into the new `velocity_head`
- new `logvar_head` is initialized with:
  - weight = `0`
  - bias = `-2.0`

This keeps action behavior close to the original checkpoint while giving the uncertainty head a stable start.

#### 3.3 Training forward

Old training behavior:

- predict `v_t`
- train with plain MSE

New training behavior when uncertainty is enabled:

- predict `(v_t, logvar_t)`
- compute:
  - `var_t = softplus(logvar_t) + eps`
- optimize:
  - heteroscedastic uncertainty-aware loss with an enlarged fixed constant term chosen so the final scalar stays nonnegative

Exact optimization loss:

- `loss`
- alias `velocity_nll_loss`

Implemented form:

\[
\operatorname{sg}(var^\beta)\left(
\frac{(v-u)^2}{2\,var}
+
\frac{1}{2}\log(var)
+
\kappa
\right)
\]

where:

\[
\kappa = -\frac{1}{2}\log(\varepsilon)
\]

Why:

- this keeps the optimized scalar nonnegative for `var >= eps`
- it is still a constant with respect to model parameters
- gradients are unchanged relative to any other fixed-constant version of the same loss
- logs are easier to read

Additional returned diagnostics:

- `mse_proxy`
- `mean_var`
- `mean_logvar`

If uncertainty is disabled:

- old `velocity_loss` path is preserved

#### 3.4 Inference

Kept:

- `generate_actions(...)`

This still returns only the action tensor.

Added:

- `generate_actions_with_uncertainty(...)`

This returns:

- `action`
- `path_variance`
- `last_step_variance`

Propagation rule used:

- diagonal
- additive
- Euler-aligned

Exact update:

- `path_variance = path_variance + (dt * dt) * var_t`

This is a first-order diagonal approximation, not full covariance transport.

---

### 4. `train_smolvlm.py`

This file was changed so the modified model can actually be trained.

#### 4.1 New CLI args

Added:

- `--predict_uncertainty`
- `--uncertainty_beta`
- `--uncertainty_eps`

#### 4.2 Checkpoint loading

When loading a checkpoint, the script now passes:

- `predict_uncertainty`
- `uncertainty_beta`
- `uncertainty_eps`

into `SmolVLMVLA.from_pretrained(...)`

This is required so old checkpoints can be upgraded into the new head layout.

#### 4.3 Optimizer grouping

Updated `get_param_groups(...)`.

If uncertainty is enabled:

- action-head parameter group now includes:
  - velocity head
  - log-variance head
  - action encoder

If uncertainty is disabled:

- old grouping stays unchanged

#### 4.4 Loss handling

The trainer previously summed all returned tensors from the model.

That would be wrong now because the model returns:

- one optimization loss
- several diagnostics

Changed logic:

- if `"loss"` exists:
  - optimize that
- else fallback to old keys

This prevents:

- accidentally optimizing `mean_var`
- accidentally optimizing `mean_logvar`

---

## Files intentionally not changed

These were intentionally left alone in phase 1:

- `models/action_hub.py`
- dataset code
- server code
- eval code

Reason:

- phase 1 is only about the action head, loss, and uncertainty-returning inference

---

## Current output contract

### Training with uncertainty enabled

Model returns:

- `loss`
- `velocity_nll_loss`
- `mse_proxy`
- `mean_var`
- `mean_logvar`

### Inference with uncertainty enabled

`generate_actions_with_uncertainty(...)` returns:

- `action`
- `path_variance`
- `last_step_variance`

Shapes:

- all uncertainty tensors are `[B, H, D]`

---

## Smoke tests run

### 1. Syntax check

Passed:

- `models/configuration_smolvlm_vla.py`
- `models/transformer_smolvlm.py`
- `models/modeling_smolvlm_vla.py`
- `train_smolvlm.py`

### 2. Official checkpoint load with uncertainty enabled

Tested from:

- `/home/redafrix/tests/intern_ship_research/intern_ship_ws/models/huggingface/SimVLA-LIBERO`

Verified:

- model loads
- `predict_uncertainty=True`
- new velocity head exists
- new log-variance head exists
- old action head weights are copied into velocity head
- log-variance head bias is initialized to about `-2.0`

### 3. Real batch forward smoke

Used one real LIBERO batch.

Verified:

- training forward runs
- returned keys include:
  - `loss`
  - `velocity_nll_loss`
  - `mse_proxy`
  - `mean_var`
  - `mean_logvar`
- new inference method runs
- returned tensors include:
  - `action`
  - `path_variance`
  - `last_step_variance`

### 4. Short training smoke

Ran:

- official checkpoint as init
- uncertainty enabled
- `iters=2`
- `batch_size=1`
- `freeze_mode=action_heads_only`

Verified:

- backward pass works
- optimizer step works
- checkpoint saves successfully

Smoke checkpoint:

- [ckpt-2](/home/redafrix/tests/intern_ship_research/intern_ship_ws/runs/simvla_modified_uncertainty_smoke/ckpt-2)

### 5. Reload smoke from the new modified checkpoint

Verified:

- saved modified checkpoint reloads
- uncertainty config persists
- velocity head exists
- log-variance head exists

---

## Current limitations

Not implemented yet:

- repeated-sample uncertainty
- external covariance / AAC entropy
- medoid selection
- calibrator
- server exposure of uncertainty tensors
- eval integration of uncertainty outputs

This repo is only phase 1.

## Note on loss sign

The previous draft version omitted the Gaussian constant term.

That made the scalar objective harder to interpret and easier to go negative.

The current implementation includes:

- `0.5 * log(2*pi)`

so the loss is now the cleaner Gaussian-style form we actually want for phase 1.
