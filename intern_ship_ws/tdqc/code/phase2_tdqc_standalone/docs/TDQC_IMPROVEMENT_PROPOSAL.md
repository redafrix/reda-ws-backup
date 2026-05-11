# Proposal: Strategic Improvements for the TDQC Uncertainty Calibrator

After a deep architectural and implementation review of the current `TDQCLSTMCalibrator`, its feature extraction (`v6`), and the TD(0) loss formulations, we have identified several concrete avenues to break through the ~80% validation accuracy ceiling. 

Currently, the model acts as a "blind" observer: it only sees the *variance* of the VLA policy's predictions over time, without any context of *what* the robot is doing or *which* task it is attempting. The following are proposed improvements categorized by implementation effort and expected impact.

---

## 1. Low-Hanging Fruit: Better Use of Existing Data (High Impact, Low Effort)

### 1.1. Inject Task Embeddings (Contextualization)
*   **The Problem:** The current `.pt` dataset contains a `task_id` for every episode, but the `TDQCLSTMCalibrator` completely ignores it. High variance might be acceptable during a transit phase in Task A, but a sign of catastrophic failure in the insertion phase of Task B.
*   **The Solution:** Add a learned `nn.Embedding(num_tasks, embedding_dim)` layer to the calibrator. Concatenate this task embedding with the normalized variance features before passing them into the LSTM. This provides the model with critical priors about the task's inherent difficulty and variance profile.

### 1.2. Temporal Derivatives ($\Delta$ Features)
*   **The Problem:** The LSTM must implicitly learn the rate of change of variance over time.
*   **The Solution:** Explicitly compute the temporal derivative (step-to-step difference) of the 8 variance features: $\Delta f_t = f_t - f_{t-1}$. Concatenate these 8 new derivatives with the original 8 features. Sudden spikes in variance are often the strongest predictors of imminent failure.

---

## 2. Advanced Training Objectives (Medium Impact, Medium Effort)

### 2.1. Switch from TD(0) to TD($\lambda$) or $n$-step Returns
*   **The Problem:** The current model uses strict TD(0) learning (`target[t] = online_q[t+1]`). In long rollouts (e.g., 200 steps), it takes thousands of epochs for the terminal failure signal to propagate back to the early steps.
*   **The Solution:** Implement TD($\lambda$) or an $n$-step return mechanism. Mixing the pure Monte Carlo return (the actual terminal failure label) with the TD estimate will vastly accelerate learning and improve calibration at early horizons (e.g., step 50).

### 2.2. Implementation of Continuous Focal Loss
*   **The Problem:** The dataset likely suffers from class imbalance (e.g., more successful steps than failure-bound steps), and MSE loss treats all errors equally.
*   **The Solution:** Replace standard masked MSE with a Brier-adapted Focal Loss. By down-weighting the loss for "easy" predictions (where the model is already confident and correct), the network will be forced to focus its gradient updates on the ambiguous, hard-to-predict moments right before a failure occurs.

---

## 3. Architectural Upgrades (High Impact, High Effort)

### 3.1. Deep Ensembles for Calibrated Uncertainty
*   **The Problem:** A single LSTM predicting a probability $p$ provides no measure of its *own* uncertainty (epistemic uncertainty). If the variance features are ambiguous, a single model might confidently output $p=0.5$, which is uninformative.
*   **The Solution:** Train an ensemble of 3-5 lightweight LSTMs (different random initializations/data shuffles). The mean of the ensemble provides a much better calibrated failure probability, and the variance of the ensemble tells the system when the calibrator itself is "confused."

### 3.2. Replace LSTM with a Causal Transformer or TCN
*   **The Problem:** LSTMs suffer from bottlenecking and forgetting over long sequences (e.g., $T > 100$).
*   **The Solution:** Upgrade the sequential backbone to a **Causal Transformer** (e.g., a lightweight GPT-style architecture) or a **Temporal Convolutional Network (TCN)**. A Causal Transformer allows the model to attend directly to a massive variance spike that happened 50 steps ago, rather than relying on the LSTM's hidden state to remember it.

---

## 4. Next-Generation Dataset: Context-Aware Features (Transformative Impact)

*   **The Problem:** Currently, the features (slots 0-7) only contain log-variances. The model does not know *where* the robot's arm is, nor *what* action the policy is attempting. It only knows that the policy is uncertain. 
*   **The Solution for Dataset `v7`:** Modify the Phase 1 feature extraction script to capture contextual anchors alongside the variance:
    1.  **Action Means:** The actual mean predicted action (e.g., the expected delta XYZ, Roll, Pitch, Yaw). This tells the calibrator *what* the robot is trying to do.
    2.  **Proprioception/State:** A low-dimensional vector of the robot's current joint positions or end-effector pose.
    3.  **Image Embeddings:** The frozen ResNet/CLIP features from the visual encoder.
    *By feeding (Variance + Actions + State) into the calibrator, it evolves from a blind variance-tracker into a full state-action-uncertainty critic.*