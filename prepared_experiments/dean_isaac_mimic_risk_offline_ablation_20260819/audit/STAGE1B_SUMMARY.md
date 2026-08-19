# Stage 1B Repair Audit Summary — Dean Isaac Mimic-style Risk Offline Ablation

## 1. Full-Corpus Round0 Census
- Number of Episode Row Files Opened: 4000
- Total Rows Streamed: 75603
- Total Rows Accepted into Frozen Round0: 75603
- Total Rows Excluded: 0
- Required Field Presence Counts across all 75,603 rows:
  - `episode_id`: 75603 / 75,603 (100.0%)
  - `decision_index`: 75603 / 75,603 (100.0%)
  - `main_candidate_action_chunk_normalized`: 75603 / 75,603 (100.0%)
  - `main_candidate_action_chunk_env`: 75603 / 75,603 (100.0%)
  - `ace_candidate_chunks_normalized`: 75603 / 75,603 (100.0%)
  - `ace_candidate_chunks_env`: 75603 / 75,603 (100.0%)
  - `main_seed`: 75603 / 75,603 (100.0%)
  - `ace_candidate_seeds`: 75603 / 75,603 (100.0%)
  - `current.proprio`: 75603 / 75,603 (100.0%)
  - `history`: 75603 / 75,603 (100.0%)
  - `simvla_uncertainty_49d`: 75603 / 75,603 (100.0%)
  - `simvla_uncertainty_delta_49d`: 75603 / 75,603 (100.0%)
  - `simvla_uncertainty_raw`: 75603 / 75,603 (100.0%)
  - `parent_episode_risk_label`: 75603 / 75,603 (100.0%)

## 2. Candidate0 Raw Dynamics Reconstructibility
- Initial Noise Shape: `(10, 7)`
- Update Vector Trace Shape: `(10, 70)`
- dt: `-0.1` (constant and source-backed)
- X_d Exactly Reconstructible: `YES` (`X_0 = initial_noise`, `X_d = initial_noise + sum_{i=0}^{d-1} update_vector_trace[i].reshape(10, 7)`)
- V_d Exactly Reconstructible: `YES` (`V_d = update_vector_trace[d].reshape(10, 7) / dt = -10.0 * update_vector_trace[d].reshape(10, 7)`)
- Source Path: `src/risk_collection/adapter.py:TorchSimVLABackend.sample_one`

## 3. Alternative Candidates Initial Noise
- Exactly Regenerable from Seed: `YES`
- Generator: `torch.Generator(device=device).manual_seed(seed)`
- Shape: `(1, 10, 7)`
- Dtype: `torch.float32`
- Source Path: `src/risk_collection/adapter.py:TorchSimVLABackend.sample_one`

## 4. Original Friend Source Search
- Original Executable Friend Risk-Head Source Found on Dean/Bob disk: `NO`
- Inspected Candidate Files:
  - `evaluator/run.py` (VAM policy runner, no standalone risk head)
  - `train_pi05_risk_no_task9_20260625.py` (SeqRiskModel Transformer, not SingleHead GRU)
  - `mimic_video/geometry.py` (10D rotation conversion only)
- Fallback Contract: `MIMIC_H10_HANDOFF_CONTRACT.md` (to be decided by user/ChatGPT)
