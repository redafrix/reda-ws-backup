# Forensic Audit Note: Trace Limitation & Invalidation of Commit 70327b4b

## Finding
A forensic audit of the historical Seen Round 0 (4,000 episodes) and locked OOD150 artifacts was conducted across Train, Validation, Test, and OOD splits.

### Archival Structure
- `main_candidate_action_chunk_env` / `main_candidate_action_chunk_normalized`: Present (Candidate 0 action chunk `(10, 7)`).
- `ace_candidate_chunks_env` / `ace_candidate_chunks_normalized`: Present (Alternative candidate action chunks 1..8 `(8, 10, 7)`).
- `ace_features_7d`: Present (7D ACE vector).
- `simvla_uncertainty_raw`: Present, but contains **ONLY Candidate 0's single diffusion denoising trace** (`denoise_mean_trace`, `path_variance`, `last_step_variance`, etc.).
- **Alternative candidate diffusion traces (`traces[1..8]`): NOT ARCHIVED.**

## Invalidation Notice
In commit `70327b4b`, offline 9-candidate scoring reused candidate 0's diffusion trace for constructing candidate 1..8 49D uncertainty vectors. Because the online runtime generates individual candidate-specific diffusion traces `traces[i]` during live SimVLA sampling, offline alternative scoring using shared candidate 0 trace is mathematically non-equivalent.

Consequently, the offline alternative score sweep, cap grid, and shortlist in commit `70327b4b` are **INVALIDATED**.

Offline exact 9-candidate reconstruction from static historical logs is unsupported due to this raw data serialization limitation. No further offline calibration sweep or online simulation will proceed without explicit review.
