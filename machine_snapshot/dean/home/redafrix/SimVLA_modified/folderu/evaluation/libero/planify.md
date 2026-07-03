## Verdict

**Phase 1 is mostly coherent and the code in the zip matches the main draft.** The model has the new config flags, split velocity/log-variance heads, uncertainty loss, backward-compatible old `generate_actions(...)`, and a new `generate_actions_with_uncertainty(...)` path. This matches the Phase-1 goal: add an uncertainty head, change the loss, and expose uncertainty without changing the server/eval contract. 

**But it is not “perfect” yet.** I found several issues you should fix before building Phase 2 on top of it.

**Phase 2 / TDQC is promising and mathematically defensible, but the current draft should not be implemented exactly as written.** The big idea is right: TDQC is a much better fit than applying the same episode label to every step with BCE. The TDQC paper explicitly connects sequential Brier minimization to value estimation, uses TD bootstrapping with a target network, and shows TD-based methods outperform BCE-style predictors in sequential VLA calibration settings. ([arXiv][1])

---

## Phase 1 code review

### What is coherent

The implementation correctly adds the config fields:

```python
predict_uncertainty
uncertainty_beta
uncertainty_eps
return_uncertainty
```

in `models/configuration_smolvlm_vla.py:50-85`.

The transformer split is also correct. In concat mode, the old single `action_decoder` becomes:

```python
velocity_head
logvar_head
```

and in AdaLN mode, the old `final_layer` becomes:

```python
velocity_final_layer
logvar_final_layer
```

See `models/transformer_smolvlm.py:315-341` and the tuple returns at `411-461`. This matches your Phase-1 draft’s “one shared action transformer + two final heads” design. 

The training loss is implemented in the expected place: `models/modeling_smolvlm_vla.py:489-505`. The code computes:

```python
var_t = F.softplus(logvar_t) + eps
sq_err = (v_t - u_t)^2
weight = var_t.pow(beta).detach()
loss = weight * (sq_err / (2 var_t) + 0.5 log(var_t) + constant)
```

This is mathematically coherent as a **stabilized β-NLL-style heteroscedastic regression loss**. For one scalar residual (e = v-u), the inner Gaussian term has optimum:

[
\frac{\partial}{\partial \sigma^2}
\left(
\frac{e^2}{2\sigma^2} + \frac{1}{2}\log\sigma^2
\right)=0
\quad\Rightarrow\quad
\sigma^2=e^2
]

So the variance head is encouraged to learn expected squared residual size. The detached ((\sigma^2)^\beta) changes gradient scaling but does not change the variance optimum inside the bracket. That is a reasonable choice.

The old inference path is preserved. `generate_actions(...)` still returns only the action, and when uncertainty is enabled it discards the log-variance safely at `models/modeling_smolvlm_vla.py:563-571`. The new method returns `action`, `path_variance`, and `last_step_variance` at `573-630`, matching the draft contract. 

The training script also includes the uncertainty heads in the trainable action group: `train_smolvlm.py:204-220`. Good.

---

## Phase 1 problems to fix

### 1. Your launcher contradicts your Phase-1 training assumption

Your Phase-1 draft repeatedly frames the current setup as **`action_heads_only`**, meaning only:

```text
action_encoder + velocity_head + logvar_head
```

are trained. 

But the zipped launcher uses:

```bash
FREEZE_MODE="${FREEZE_MODE:-freeze_vlm_entire_run}"
FREEZE_STEPS="${FREEZE_STEPS:-60000}"
```

in `run_uncertainty_lr_sweep.sh`.

That means the default run trains:

```text
transformer_core + action_heads
```

for the whole run, with only the VLM frozen. This is a much larger fine-tuning regime than your Phase-1 plan. It is not automatically wrong, but it changes the scientific claim.

You need to choose one:

```bash
# Strict Phase 1 minimal version
FREEZE_MODE="${FREEZE_MODE:-action_heads_only}"
FREEZE_STEPS="${FREEZE_STEPS:-60000}"
```

or update the plan and say:

> Phase 1 implementation is minimal architecturally, but fine-tuning trains the action transformer core plus uncertainty heads while keeping the VLM frozen.

Right now the plan and code are not coherent.

---

### 2. The draft says “only modify 3 files,” but the implementation modifies training too

The Phase-1 draft says to modify only:

```text
configuration_smolvlm_vla.py
transformer_smolvlm.py
modeling_smolvlm_vla.py
```

and not touch other code. 

But the zip necessarily modifies `train_smolvlm.py` and the launcher to expose:

```bash
--predict_uncertainty
--uncertainty_beta
--uncertainty_eps
```

This is fine technically, but the document should be corrected. Otherwise, future you will think the implementation violated the plan.

---

### 3. The variance is in normalized action space, not physical action space

During training, actions are normalized before flow matching. During inference, `x_t` lives in normalized action space, then the final action is postprocessed/unnormalized:

```python
action = self.action_space.postprocess(x_t)
```

But `path_variance` and `last_step_variance` are returned before physical-space variance conversion. So the returned variance tensors are in **normalized action units**.

That is okay for Phase 2 **if the calibrator is trained and tested on the same normalized variance convention**. But do not interpret the numbers as physical joint/action variance unless you rescale:

```python
var_physical[..., d] = var_normalized[..., d] * action_std[d] ** 2
```

For the calibrator, I would keep normalized variance. It makes dimensions comparable and avoids unit dominance.

---

### 4. “Stochasticity of the environment” is too strong

Your Phase-1 validation conclusion says the uncertainty head is learning the “stochasticity of the environment.” 

Strictly, Phase 1 learns:

> expected residual/error of the flow velocity prediction (v_t) against (u_t)

That can correlate with environment difficulty, grasp instability, distribution shift, or policy confusion. But it is not a direct environment stochasticity estimator.

Use this wording instead:

> The Phase-1 uncertainty head learns a useful predictive residual uncertainty signal. Empirically, this signal separates successful and failing rollouts on the tested task, making it promising as an input to a calibrated failure-risk predictor.

That is mathematically cleaner.

---

### 5. Backward compatibility is mostly good, but fragile for checkpoint formats

You added:

```python
_upgrade_legacy_state_dict_for_uncertainty(...)
_maybe_copy_legacy_output_head(...)
```

Good idea. But `_maybe_copy_legacy_output_head(...)` only checks:

```python
model.safetensors
```

If a checkpoint is sharded, uses `model.safetensors.index.json`, or uses `pytorch_model.bin`, the copy path may silently fail. Then the new velocity head may not inherit the old action head.

Add a robust fallback:

```python
# check model.safetensors
# else check model.safetensors.index.json and load shard containing action_decoder
# else check pytorch_model.bin
```

Then run the three tests from your own draft: old checkpoint/old config, old checkpoint/new uncertainty config, new checkpoint/uncertainty config. 

---

### 6. AdaLN has a hidden initialization risk

In `FinalLayer.__init__`, you zero-initialize the AdaLN modulation and linear layer. But later, `SmolVLMActionTransformer.__init__` calls:

```python
self.apply(basic_init)
```

This reinitializes all `nn.Linear` layers, including the `FinalLayer` internals. So the intended DiT zero-init is undone.

This matters only if `use_adaln=True`. Your launcher has:

```bash
USE_ADALN=false
```

so it does not affect your current run. Still, fix it before relying on AdaLN.

---

## Phase 2 / TDQC review

### Main verdict

The Phase-2 direction is good. TDQC is a strong choice because your labels are naturally episode-level success/failure labels, and applying the same BCE label to every time step is indeed a bad credit-assignment rule. The TDQC paper makes the same core argument: sequential calibration has delayed terminal feedback, and minimizing sequential Brier score connects to value estimation in RL. ([arXiv][1])

The paper also reports that TD-based predictors outperform BCE-style alternatives for Brier score and failure detection, and it explicitly interprets the learned uncertainty estimates as probability of failure in its training/evaluation details. ([arXiv][1])

So yes: **TDQC is useful, promising, and mathematically relevant for your Phase-2 calibrator.**

But you need to clean up four things before coding.

---

## Phase 2 fixes before implementation

### 1. Be consistent: failure probability or success probability

Your draft defines:

```text
Y = 1 for failure
fθ = predicted failure probability
```

That is fine. But the TDQC paper often frames the learned value as success/future reward probability. The paper’s method section links sequential Brier minimization to estimating the value function / future reward predictor. ([arXiv][1])

For your implementation, write it explicitly as:

```text
Y_fail ∈ {0,1}
Y_fail = 1 if the rollout fails
qθ(t) = P(failure | φ0:t)
```

Then the TD target is:

```python
target_t = q_target(t+1)      # non-terminal
target_last = Y_fail          # terminal
```

Do **not** mix this with “success Q-value” language unless you define:

```python
p_fail = 1 - q_success
```

This is the most important mathematical cleanup.

---

### 2. Fix the indexing

Your draft writes trajectories as:

```text
[φ(0), ..., φ(T)]
```

and applies the terminal loss at `t = T`.

In robotics rollouts, the cleaner definition is:

```text
L = number of decision steps
φ_0, ..., φ_{L-1}
Y_fail = terminal outcome after the rollout
```

Then:

```python
for t in 0 ... L-2:
    loss += (qθ(φ0:t) - stopgrad(qθ_target(φ0:t+1)))^2

loss += (qθ(φ0:L-1) - Y_fail)^2
```

This avoids the ambiguity of whether `φ_T` exists after the terminal action. It also makes padding/masking easier.

---

### 3. The 2D feature vector is elegant but probably too compressed

Your current Phase-2 input is:

```text
φ_t = [u_path(t), u_last(t)] ∈ R²
```

where both are exponentially weighted summaries over horizon and action dimensions. 

This is mathematically valid, but I think it is too compressed for a serious calibrator. The TDQC paper’s black-box predictors did not use only one or two scalars; for OpenVLA they used richer action-probability summaries such as top probabilities per degree of freedom, and for other tokenized models they used logits because raw probabilities were not directly interpretable. ([arXiv][1])

I recommend a small but richer vector:

```text
φ_t = [
  log1p(weighted_mean_last_var),
  log1p(weighted_mean_path_var),
  log1p(first_step_last_var),
  log1p(first_step_path_var),
  log1p(max_last_var),
  log1p(max_path_var),
  log1p(gripper_last_var),
  Δ log1p(weighted_mean_last_var)
]
```

That gives you maybe 8 dimensions, not 576. It still avoids the “latent overfit” trap, but it preserves more risk information.

Use `log1p` because variance is usually skewed. Then standardize each feature using training-set mean/std.

---

### 4. Do not hard-code threshold `0.35`

Your draft says the planner can use a threshold like `0.35`. 

Do not do that as a fixed scientific claim. The TDQC paper discusses time-varying thresholds and conformal prediction bands for early stopping, calibrated on successful trajectories. ([arXiv][1])

For your implementation, use:

```text
train split: train TDQC
validation split: choose threshold / CP band
test split: report failure detection metrics
```

Report:

```text
Sequential Brier score
ECE
ROC-AUC
early-warning lead time
false stop rate on successful rollouts
true stop rate on failed rollouts
```

---

## The corrected Phase-2 mathematical contract

Use this as the implementation target:

```text
Dataset:
D = { (φ_i[0:L_i], Y_i_fail) }_{i=1}^N

Y_i_fail = 1 if rollout i fails, else 0
φ_i[t] ∈ R^F, with F = 2 minimum, preferably 6–10
```

Model:

```text
h_t, c_t = LSTM(φ_t, h_{t-1}, c_{t-1})
q_t = sigmoid(MLP(h_t))
q_t ≈ P(failure | φ_0:t)
```

TD-0 loss with masks:

```text
for t < L_i - 1:
    target_t = stopgrad(q^-_{t+1})

for t = L_i - 1:
    target_t = Y_i_fail

L = mean_masked((q_t - target_t)^2)
```

Target network:

```text
θ^- ← τ θ + (1-τ) θ^-
```

or hard update every `C` steps. The TDQC paper used a target network for stability. ([arXiv][1])

---

## Final implementation priority list

Do these before coding Phase 2:

1. **Decide the real Phase-1 training mode.** If you want the clean Phase-1 claim, set the launcher default back to `action_heads_only`. If you want better performance and accept a larger update, update the draft.

2. **Rename the Phase-1 loss honestly.** Call it `velocity_beta_nll_loss` or keep `velocity_nll_loss` but document that it is β-weighted/stabilized, not pure Gaussian NLL.

3. **Document variance units.** Say: `path_variance` and `last_step_variance` are in normalized action space.

4. **Fix Phase-2 target definition.** Use `Y_fail` everywhere if the model outputs failure probability.

5. **Use a slightly richer uncertainty feature vector.** R² is clean but risky. R⁶–R¹⁰ is still lightweight and more defensible.

6. **Validate across tasks, not only one task.** Your Phase-1 Task-5 results are encouraging, but Phase-2 should prove generalization across LIBERO tasks/seeds, not just same-task separation.

7. **Do not use a fixed threshold from the paper.** Learn it on validation rollouts or use conformal/time-varying thresholds.

My final verdict: **Phase 1 is usable after small cleanup. Phase 2 is worth doing and scientifically promising, but rewrite the draft around a precise failure-probability TD target and a richer calibrated feature vector before implementation.**

[1]: https://arxiv.org/html/2604.20472v1 "Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models"
