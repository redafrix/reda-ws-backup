# Stage 9 FIPER Adaptation Design Plan

This document outlines the architectural design for adapting FIPER (Failure Prediction at Runtime) concepts to the Stage 9 / SimVLA / LIBERO-PRO failure prediction and continuous risk collection system.

## Core Philosophy: Success-Only Calibration

Traditional failure detection methods require both successful and failed execution data to train classifiers. In contrast, FIPER uses a **success-only calibration** paradigm:
1. **No failure labels** are used to train RND or fit conformal thresholds.
2. Models are trained and calibrated strictly on successful or expert demonstrations.
3. Runtime deviations (RND-OE) or action prediction variance (ACE) above the calibrated threshold indicate anomalies, out-of-distribution (OOD) states, or high-uncertainty actions.
4. FIPER is used as a **mining signal, OOD-aware risk monitor, and audit signal**, not as the final ground-truth risk labeler (which remains governed by the Stage 9 V2 local continuous scorer).

---

## A. Data Sources

We utilize four key data sources for training, calibration, and evaluation:

1. **Expert LIBERO Demos**: 
   - Clean, human-expert demonstrations in HDF5 format.
   - Act as the primary *success-only normal calibration anchors* representing expert behavior.
2. **Successful SimVLA V2 Chunks**:
   - Successful rollouts/sub-sequences collected during SimVLA execution.
   - Represent *policy-success calibration anchors* (states where the policy might not be expert but succeeds).
3. **Current 64-Seed Same-State Groups**:
   - Subsets of counterfactual samples generated at the same simulated state across 64 seeds.
   - Used as the *ACE action entropy input* to evaluate action distribution variance.
4. **Future Failed/Boundary States**:
   - States where the policy fails or times out.
   - Used **only for mining and validation/evaluation**, never for training the model or fitting thresholds.

---

## B. FIPER Signals

We define and compute two core signals to track runtime risk:

### 1. Action Chunk Entropy (ACE)
Computed across 64 SimVLA candidate action chunks generated for the same state:
- **Action Mean/Std**: Mean and standard deviation of all action components across the 64 candidates.
- **Per-step Action Std**: The standard deviation of predicted actions at each timestep of the 10-step horizon.
- **Gripper Entropy/Std**: The standard deviation/entropy of gripper commands (dimension 7).
- **Trajectory Pairwise Distance**: Mean Euclidean distance between pairs of action sequences (each flattened to $10 \times 7 = 70$ elements).
- **Gaussian Entropy Approximation**: Approximating the action prediction distribution as a multivariate Gaussian and calculating differential entropy:
  $$H(X) = \frac{1}{2} \ln \left( (2\pi e)^k \det(\Sigma + \epsilon I) \right)$$
- **Normalized ACE Score**: Scale the computed entropy relative to calibration thresholds.

### 2. RND Observation Embedding (RND-OE)
Tracks whether the robot's current observation is out of the distribution of successful behavior:
- **Preferred Option**: Extract the 512-dim or 1024-dim `pooled_vlm_features` directly from SimVLA's internal vision-language encoder.
- **Fallback Option**: If internal embedding extraction is unavailable, use a *deployable feature vector* constructed from:
  - Current proprioceptive state (joint/EEF positions).
  - History of proprioceptive states.
  - History of actions executed.
  - Any lightweight visual/VLM embeddings available.

### 3. Conformal Calibration
Conformal thresholds are fit strictly on successful/expert rollouts to control the false alarm rate:
- **Constant Quantile**: Threshold set to a specific quantile (e.g., 95th percentile) of maximum uncertainty scores across successful rollouts.
- **Time-Varying Quantile**: Unique threshold calculated for each rollout timestep $t$.
- **Moving-Window Aggregation**: Accumulate uncertainty scores over a sliding window (e.g., size 5) to smooth out high-frequency noise and prevent transient false alarms.

---

## C. Runtime / Mining Logic

At each state encountered during policy execution, we compute the RND score, generate 64 action chunks, compute ACE, and categorize the state into one of four patterns:

| RND Score | ACE Score | Classification | System Response / Interpretation |
|---|---|---|---|
| **Low** | **Low** | **Normal Confident** | Normal state; high policy confidence; no intervention needed. |
| **High** | **Low** | **OOD Confident (Benign OOD)** | Novel state/context, but the policy generates consistent actions. High potential for auditing to check if it represents a benign variation. |
| **Low** | **High** | **Action Uncertain** | Known state, but the policy is highly uncertain about which action to take. Strong candidate for action-specific mining. |
| **High** | **High** | **High Failure Risk** | OOD state AND highly uncertain actions. Strongest candidate for failure-risk/boundary state mining. |

---

## D. Integration with Stage 9 V2

1. FIPER does **not** replace the final local risk labeler. The Stage 9 V2 `local_chunk_quality.py` remains the final ground-truth source of continuous `risk_score` values.
2. FIPER acts as a **gatekeeper/filter** for active mining: it ranks states to decide which should undergo 64-seed counterfactual replay.
3. FIPER scores are saved as metadata in the generated dataset:
   - `fiper_ace_score`: Raw action chunk entropy value.
   - `fiper_rnd_oe_score`: Raw distillation error score.
   - `fiper_alarm`: Boolean indicating if conformal threshold is breached.
   - `fiper_signal_type`: Categorical pattern classification (e.g. `high_rnd_high_ace`).
