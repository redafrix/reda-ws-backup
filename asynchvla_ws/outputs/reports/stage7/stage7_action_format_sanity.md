# Stage 7 — Action Format Sanity

- Timestamp: 2026-05-15 (Gemini)

## Action Logic Verification

1. **Model Output:** SimVLA produces `generated_normalized_action` in range roughly `[-1, 1]` (Z-score or Quantile).
2. **Post-process:** The script uses `generated_postprocessed_action`, which is unnormalized via `LiberoJointActionSpace.unnormalize_action`.
3. **Unnormalization Stats:** Loaded from `libero_norm.json`. 
   - `dx/dy/dz` std ≈ 0.3-0.4.
   - `dr/dp/dy` std ≈ 0.04-0.08.
   - `gripper` std ≈ 1.0.
4. **Resulting Scale:** Unnormalized actions are roughly in `[-1.0, 1.0]`. 

## Expert Comparison

- **Expert Dataset:** `pick_up_the_alphabet_soup_and_place_it_in_the_basket_demo.hdf5`
- **Expert Action Min/Max (first 3 dims):** `[-0.51, 0.37]`, `[-0.83, 0.80]`, `[-0.93, 0.93]`.
- **Gemini Debug (SimVLA A_passive):** `[0.16, -0.40, -0.00]`.

**Verdict:** The action format and scale are consistent with expert data and successfully drive the LIBERO environment.

## Answers to Technical Questions

- **Is SimVLA output already postprocessed?** Yes, `generated_postprocessed_action` is used.
- **Is the script executing normalized actions?** No, it uses the postprocessed ones.
- **Is gripper sign/scale correct?** Yes, expert data uses `[-1, 1]` and model output matches.
- **Action shape?** `(7,)` per step.
- **Executing chunk?** It executes one action from the `postprocessed_action` chunk per env step.
