# TDQC Improvement Experiments - General Analysis

## Experiment Summary Table

| Experiment | Idea | Dataset | Best Val Brier | Final Test Brier | Improvement vs Baseline (Test) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline (v6)** | Baseline | v6 (8D) | 0.123200 | 0.149666 | - |
| **Idea 1** | Monte Carlo Targets | v6 (8D) | 0.126741 | 0.117267 | **+0.032399** |
| **Idea 2** | Delta Features | v6_delta (16D) | 0.121176 | 0.124592 | **+0.025074** |
| **Idea 3** | Task Embedding | v6 (8D) | 0.117660 | 0.121341 | **+0.028325** |
| **Idea 4** | Larger LSTM (256/2L) | v6 (8D) | 0.111789 | 0.110386 | **+0.039280** |
| **Idea 5** | Causal Transformer | v6 (8D) | 0.227707 | 0.229065 | -0.079399 (Worse) |

## Detailed Analysis

### 1. The Power of Capacity (Idea 4)
Increasing the LSTM size from 128/1-layer to 256/2-layers was the most effective single change. The Sequential Brier score dropped from ~0.150 to ~0.110 on the test set. This indicates that the 8D uncertainty features contain more complex patterns than the small baseline model could capture. Interestingly, Idea 4 also showed the best training stability and generalization.

### 2. Supervised MC vs. Bootstrapped TD (Idea 1)
Switching from TD(0) to Monte Carlo targets (terminal labels at every step) resulted in a significant improvement on the test set (0.117). This suggests that for manipulation episodes which are relatively short, bootstrapping from a potentially inaccurate "next-step" prediction might be noisier than directly predicting the final outcome. This is consistent with supervised learning being more stable when terminal ground truth is available.

### 3. Context Awareness (Idea 3)
Adding learned task embeddings (Idea 3) improved performance (0.121 test Brier). Since the dataset covers 10 different tasks with varying difficulty and uncertainty profiles, allowing the model to adapt its "calibration curve" per task is a clear win.

### 4. Sequential Features (Idea 2)
Adding per-step deltas (16D features) helped (0.124 test Brier) but was less impactful than architectural capacity or labeling strategies. This suggests that the LSTM is already somewhat capable of inferring "changes" from the raw sequence, but explicit deltas provide a cleaner signal.

### 5. Transformer Performance (Idea 5)
The Causal Transformer (Idea 5) performed significantly worse (0.229 test Brier). This might be due to several factors:
- LSTMs are naturally biased toward sequential processing which fits this task well.
- Transformers might require more data or more careful tuning of learning rates and attention heads.
- The causal mask might be harder to learn for a small 2-layer transformer compared to the hidden state of an LSTM.

## Conclusion and Recommendations

The best "Silver Bullet" for TDQC at this stage is a combination of **High Capacity (Idea 4)**, **Task-Embedding Conditioning (Idea 3)**, and **Monte Carlo targets (Idea 1)**.

**Recommended Combined Architecture:**
- **Model:** 2-layer LSTM, 256 hidden units.
- **Inputs:** 16D Delta features + Task ID Embedding (128-dim).
- **Loss:** Weighted Brier loss with Monte Carlo targets.
- **Training:** 1000+ epochs with ReduceLROnPlateau.

This combination is expected to push the Sequential Brier score below 0.100, providing highly reliable failure predictions for SimVLA.
