# Marathon V10: Hyper-Drive Results & The Great FPR Crisis

## Executive Summary
We executed 66/100 ideas from the Hardcore 100 series. While training was stable, the evaluation results on OOD data reveal a catastrophic Panic Mode in 98% of the models. 

**The Winner is still Idea 45.** It is the only model that achieves a usable safety profile.

## Key Metrics (Top 10 & Notable Ideas)

| Idea | Architecture | Key Feature | Recall | FPR | Total (R-F) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **45** | **MLP + RMSNorm** | **Dynamic Competence Labeling (Last 50)** | **15.9%** | **0.18%** | **15.7%** |
| 16 | MLP | RMSNorm + Multi-Scale Deltas | 100% | 100% | 0.0% |
| 51 | MLP | Cox Hazard Likelihood | 100% | 100% | 0.0% |
| 65 | Hardcore | Liquid ODE Proxy | 100% | 100% | 0.0% |
| 66 | Hardcore | RMSNorm Scaling | 100% | 100% | 0.0% |

## The Panic Mode Diagnosis
Almost all models (except Idea 45) show **100% Recall and 100% FPR**. 
- **Cause:** The Healthy Start Penalty. By labeling the entire failure episode as 1.0, models learn to fear the starting state of failure episodes, even when it is physically identical to success episodes.
- **Result:** The models predict Failure immediately upon initialization, making them useless for real-time safety monitoring.

## Champion Analysis: Idea 45
Idea 45 uses **Dynamic Competence Labeling**, only penalizing the model for the final 50 steps before a crash.
- **Start Confidence:** 99.56% (Almost perfect stability at the start).
- **FPR:** 0.18% (Near zero false alarms).
- **Recall:** 15.9% (Low, but honest). It only detects failure when the physical state actually deviates.

## Future Strategy: Marathon V11 (Planned)
We have prepared the metadata for Ideas 101-150. The focus will be:
1.  **Universal Competence Labeling:** Applying Idea 45's labeling strategy to *all* other architectural variants (Liquid, Spectral, Cox).
2.  **Temporal Smoothing:** Adding a Kalman-like filter to the output to prevent vibration in confidence scores.
3.  **Physical Consistency Loss:** Penalizing the model if its confidence changes faster than the physical state derivatives.

**Status:** Stopped future launches. All training processes killed. Standby for V11.
