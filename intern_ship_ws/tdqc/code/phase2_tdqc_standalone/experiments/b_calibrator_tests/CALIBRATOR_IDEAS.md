# VLA Confidence Calibrator: 10 Experimental Directions

These ideas pivot from 'Forecasting Failure' to 'Evaluating Current State Reliability'.

## Paradigm A: Reconstruction & Density (State-Space Anomaly Detection)
1. **Idea 301: Conv-VAE Bottleneck**
   - Use a Variational Autoencoder to compress the 22D features. 
   - Confidence = Negative Reconstruction Loss. 
   - *Logic:* If the model can't reconstruct the state, the VLA is in an unfamiliar (OOD) territory.

2. **Idea 302: Contrastive 'Safe-Cluster' Mapping**
   - Use Triplet Loss to push all states from 'Success' episodes into a tight hypersphere.
   - Confidence = Distance to the cluster center.

3. **Idea 303: Normalizing Flows for Density Estimation**
   - Model the probability distribution p(feature) of successful trajectories.
   - Confidence = log-likelihood of the current state.

## Paradigm B: Predictive Dynamics (Surprise Metric)
4. **Idea 304: One-Step Forward Predictor (Residual Confidence)**
   - Train the model to predict feature_{t+1} from feature_{t}.
   - Confidence = exp(-||predicted - actual||).
   - *Logic:* Surprising physical states = Low Confidence.

5. **Idea 305: Multi-Step Horizon 'Imagination' Error**
   - Predict the next 10 steps. If the robot deviates from its 'imagined' path, confidence plummets.

6. **Idea 306: Action-Conditioned Dynamics**
   - Predict next state using both current state and the VLA's commanded action.
   - If the physics don't follow the command (e.g., slipping), confidence drops.

## Paradigm C: Dynamic Competence (Step-Level Labels)
7. **Idea 307: The 'Danger Zone' Ramp (H=100)**
   - Use labels that are 0.0 (Safe) until the last 100 steps of a failure, then linear ramp to 1.0.
   - Forces 100% confidence during the early 'Normal' phase of a failure episode.

8. **Idea 308: Self-Supervised Physical Consistency**
   - Label steps as 'Unreliable' if the variance between consecutive frames spikes (vibration detection).

## Paradigm D: Multi-Head Calibration
9. **Idea 309: Ensemble Disagreement (Epistemic Calibration)**
   - Train 5 small MLPs with different seeds. 
   - Confidence = 1.0 - Variance(Predictions).
   - *Logic:* If the models disagree, the state is OOD.

10. **Idea 310: Physics-Sentinel Hybrid (Brier + Force)**
    - Confidence is a weighted sum of the Brier score AND the raw end-effector force magnitude.
    - *Logic:* High forces = Unexpected contact = Danger.
