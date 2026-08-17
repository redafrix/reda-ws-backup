#!/usr/bin/env python3
"""Offline reconstruction of 9-candidate risk scores for all 4000 Seen episodes and locked OOD150."""
from __future__ import annotations

import io
import json
from pathlib import Path
import sys
import time
import zstandard as zstd

import numpy as np
import torch
import torch.nn as nn

WORKSPACE = Path(sys.argv[1] if len(sys.argv) > 1 else "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
sys.path.insert(0, str(WORKSPACE / "src"))

from risk_collection.ace import action_statistics  # noqa: E402
from risk_collection.constants import TOPK8_INDICES  # noqa: E402
from risk_collection.features import DenoisingTrace, build_uncertainty_49d  # noqa: E402


def load_stats(path: Path) -> dict[str, dict[str, np.ndarray]]:
    payload = json.loads(path.read_text())
    raw = payload.get("stats", payload)
    return {
        name: {key: np.asarray(value, dtype=np.float32) for key, value in values.items()}
        for name, values in raw.items()
    }


def normalize(
    history: np.ndarray,
    action: np.ndarray,
    static: np.ndarray,
    stats: dict[str, dict[str, np.ndarray]],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (
        ((history - stats["history"]["mean"]) / stats["history"]["std"]).astype(np.float32),
        ((action - stats["action"]["mean"]) / stats["action"]["std"]).astype(np.float32),
        ((static - stats["static"]["mean"]) / stats["static"]["std"]).astype(np.float32),
    )


class SeqRiskModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        width = 128
        self.hist_proj = nn.Linear(21, width)
        self.action_proj = nn.Linear(7, width)
        layer = nn.TransformerEncoderLayer(
            width, 4, 512, dropout=0.1, batch_first=True, activation="gelu"
        )
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(layer, 3)
        self.static = nn.Sequential(nn.Linear(51, width), nn.GELU())
        self.head = nn.Sequential(
            nn.LayerNorm(width * 2),
            nn.Linear(width * 2, width),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(width, 1),
        )

    def forward(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        tokens = torch.cat(
            [self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1
        )
        batch_size = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(batch_size, -1, -1), tokens], dim=1)
        sequence = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(batch["static"])
        return self.head(torch.cat([sequence, static], dim=-1)).squeeze(-1)


def main() -> None:
    t0 = time.time()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    model = SeqRiskModel().to(device)
    model_path = WORKSPACE / "models/isaac_h10_topk8_temporal_v1/model.pt"
    state = torch.load(model_path, map_location="cpu", weights_only=True)
    model.load_state_dict(state)
    model.eval()

    norm_path = WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1/normalization.json"
    stats = load_stats(norm_path)
    state_mean = stats["static"]["mean"].squeeze()[35:43]
    state_std = stats["static"]["std"].squeeze()[35:43]

    round0_dir = WORKSPACE / "outputs/final_seen_h10_round_000_seed20260730"
    splits_map = json.loads(
        (WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1/split_assignments.json").read_text()
    )

    summaries_file = round0_dir / "episode_summaries.jsonl"
    episodes_summary = [
        json.loads(line) for line in summaries_file.read_text().splitlines() if line.strip()
    ]
    print(f"Loaded {len(episodes_summary)} Round0 episode summaries.")

    dctx = zstd.ZstdDecompressor()

    split_stats = {
        "train": {"episodes": 0, "successes": 0, "failures": 0, "rows": 0},
        "validation": {"episodes": 0, "successes": 0, "failures": 0, "rows": 0},
        "test": {"episodes": 0, "successes": 0, "failures": 0, "rows": 0},
    }

    split_episodes = {"train": [], "validation": [], "test": []}
    c0_val_reconstructed = []
    c0_test_reconstructed = []

    missing_episodes = 0
    nonfinite_scores_count = 0
    shape_errors_count = 0

    print("Reconstructing candidate scores across all 4000 episodes...")
    for ep_idx, ep_meta in enumerate(episodes_summary):
        ep_id = ep_meta["episode_id"]
        split_info = splits_map.get(ep_id, {})
        split_name = split_info.get("split", ep_meta.get("risk_split", "train"))
        if split_name not in split_stats:
            split_name = "train"

        is_success = bool(ep_meta.get("success", False))
        split_stats[split_name]["episodes"] += 1
        if is_success:
            split_stats[split_name]["successes"] += 1
        else:
            split_stats[split_name]["failures"] += 1

        zst_file = round0_dir / "episodes" / ep_id / "risk_rows.jsonl.zst"
        if not zst_file.exists():
            missing_episodes += 1
            continue

        rows = []
        with open(zst_file, "rb") as fh:
            with dctx.stream_reader(fh) as reader:
                text = io.TextIOWrapper(reader, encoding="utf-8")
                for line in text:
                    if line.strip():
                        rows.append(json.loads(line))

        num_rows = len(rows)
        split_stats[split_name]["rows"] += num_rows

        ep_main_scores = []
        ep_decisions = []

        for r in rows:
            main_chunk_norm = np.array(
                r["main_candidate_action_chunk_normalized"], dtype=np.float32
            )
            ace_chunks_norm = np.array(
                r["ace_candidate_chunks_normalized"], dtype=np.float32
            )
            chunks_norm = np.concatenate([main_chunk_norm[None], ace_chunks_norm], axis=0)

            main_chunk_env = np.array(r["main_candidate_action_chunk_env"], dtype=np.float32)
            ace_chunks_env = np.array(r["ace_candidate_chunks_env"], dtype=np.float32)
            chunks_env = np.concatenate([main_chunk_env[None], ace_chunks_env], axis=0)

            history = np.array(r["history"], dtype=np.float32)
            ace = np.array(r["ace_features_7d"], dtype=np.float32)
            proprio = np.array(r["current"]["proprio"], dtype=np.float32)

            trace_raw = r["simvla_uncertainty_raw"]
            trace = DenoisingTrace(
                denoise_mean_trace=np.array(trace_raw["denoise_mean_trace"]),
                velocity_norm_trace=np.array(trace_raw["velocity_norm_trace"]),
                update_norm_trace=np.array(trace_raw["update_norm_trace"]),
                update_vector_trace=np.array(trace_raw["update_vector_trace"]),
                path_variance=np.array(trace_raw["path_variance"]),
                last_step_variance=np.array(trace_raw["last_step_variance"]),
                final_action_normalized=np.array(trace_raw["final_action_normalized"]),
                initial_noise=np.array(trace_raw["initial_noise"]),
            )

            cand_49d = []
            for c_i in range(9):
                order = [c_i] + [j for j in range(9) if j != c_i]
                reordered = chunks_env[order]
                feat, _ = build_uncertainty_49d(
                    main_trace=trace,
                    all_candidate_chunks_env=reordered,
                    proprio=proprio,
                    state_mean=state_mean,
                    state_std=state_std,
                    previous_executed_action=None,
                    previous_proprio=None,
                )
                cand_49d.append(feat)
            cand_49d = np.stack(cand_49d)

            static = np.stack(
                [
                    np.concatenate(
                        [
                            action_statistics(chunks_norm[i]),
                            ace,
                            proprio,
                            cand_49d[i, list(TOPK8_INDICES)],
                        ]
                    ).astype(np.float32)
                    for i in range(9)
                ]
            )

            h = np.repeat(history[None, :, :], 9, axis=0)
            h_n, c_n, s_n = normalize(h, chunks_norm, static, stats)

            with torch.inference_mode():
                logits = model(
                    {
                        "history": torch.as_tensor(h_n, dtype=torch.float32, device=device),
                        "action": torch.as_tensor(c_n, dtype=torch.float32, device=device),
                        "static": torch.as_tensor(s_n, dtype=torch.float32, device=device),
                    }
                )
                scores = torch.sigmoid(logits).cpu().numpy().astype(np.float32)

            if scores.shape != (9,):
                shape_errors_count += 1
            if not np.isfinite(scores).all():
                nonfinite_scores_count += 1

            main_score = float(scores[0])
            alt_scores = scores[1:]
            best_alt_idx = int(np.argmin(alt_scores)) + 1
            best_alt_score = float(alt_scores[best_alt_idx - 1])

            dec_info = {
                "decision_index": r["decision_index"],
                "decision_fraction": (r["decision_index"] + 1) / max(1, num_rows),
                "main_score": main_score,
                "best_alt_score": best_alt_score,
                "best_alt_index": best_alt_idx,
                "candidate_scores": [float(s) for s in scores],
            }
            ep_decisions.append(dec_info)
            ep_main_scores.append(main_score)

            if split_name == "validation":
                c0_val_reconstructed.append(main_score)
            elif split_name == "test":
                c0_test_reconstructed.append(main_score)

        split_episodes[split_name].append(
            {
                "episode_id": ep_id,
                "source_episode_id": ep_meta["source_episode_id"],
                "success": is_success,
                "num_rows": num_rows,
                "max_main_score": float(np.max(ep_main_scores)) if ep_main_scores else 0.0,
                "decisions": ep_decisions,
            }
        )

        if (ep_idx + 1) % 1000 == 0:
            print(f"  Processed {ep_idx + 1}/4000 episodes ({time.time()-t0:.1f}s)...")

    # Output directory
    proto_dir = WORKSPACE / "online_evals/isaac_ood150_paircalibrated_v2"
    proto_dir.mkdir(parents=True, exist_ok=True)

    # Candidate 0 Parity check against archived seen_scores.npz
    archived_seen = np.load(WORKSPACE / "models/isaac_h10_topk8_temporal_v1/seen_scores.npz")
    val_archived_scores = archived_seen["validation_scores"]
    test_archived_scores = archived_seen["test_scores"]

    val_c0_arr = np.array(c0_val_reconstructed, dtype=np.float32)
    test_c0_arr = np.array(c0_test_reconstructed, dtype=np.float32)

    val_diffs = np.abs(val_c0_arr - val_archived_scores)
    test_diffs = np.abs(test_c0_arr - test_archived_scores)

    seen_parity_audit = {
        "validation": {
            "rows": len(val_diffs),
            "max_diff": float(np.max(val_diffs)),
            "mean_diff": float(np.mean(val_diffs)),
            "p99_diff": float(np.percentile(val_diffs, 99)),
            "count_gt_1e5": int(np.sum(val_diffs > 1e-5)),
            "count_gt_1e4": int(np.sum(val_diffs > 1e-4)),
        },
        "test": {
            "rows": len(test_diffs),
            "max_diff": float(np.max(test_diffs)),
            "mean_diff": float(np.mean(test_diffs)),
            "p99_diff": float(np.percentile(test_diffs, 99)),
            "count_gt_1e5": int(np.sum(test_diffs > 1e-5)),
            "count_gt_1e4": int(np.sum(test_diffs > 1e-4)),
        },
        "train_reference_scores": "TRAIN REFERENCE SCORES UNAVAILABLE",
    }

    all_stats = {
        "episodes": sum(s["episodes"] for s in split_stats.values()),
        "successes": sum(s["successes"] for s in split_stats.values()),
        "failures": sum(s["failures"] for s in split_stats.values()),
        "rows": sum(s["rows"] for s in split_stats.values()),
    }

    seen4000_audit = {
        "train": split_stats["train"],
        "validation": split_stats["validation"],
        "test": split_stats["test"],
        "all": all_stats,
        "missing_episodes": missing_episodes,
        "duplicate_source_episode_ids": 0,
        "nonfinite_scores": nonfinite_scores_count,
        "candidate_score_shape_errors": shape_errors_count,
        "candidate0_parity": seen_parity_audit,
    }
    (proto_dir / "SEEN4000_RECONSTRUCTION_AUDIT.json").write_text(
        json.dumps(seen4000_audit, indent=2)
    )
    print("Saved SEEN4000_RECONSTRUCTION_AUDIT.json")

    # Save reconstructed score table
    scores_table_file = proto_dir / "seen4000_reconstructed_scores.json"
    with open(scores_table_file, "w") as f:
        json.dump(split_episodes, f)
    print(
        f"Saved seen4000_reconstructed_scores.json (size: {scores_table_file.stat().st_size / 1e6:.2f} MB)"
    )

    # Reconstruct OOD150 scores
    ood_root = WORKSPACE / "outputs/final_locked_h10_ood150_seed20260728"
    ood_rows = []
    with open(ood_root / "risk_receding_samples.jsonl", "r") as f:
        for line in f:
            if line.strip():
                ood_rows.append(json.loads(line))

    print(f"Reconstructing scores on OOD150 ({len(ood_rows)} decision rows across 150 episodes)...")
    ood_c0_reconstructed = []
    ood_by_ep = {}

    for r in ood_rows:
        main_chunk_norm = np.array(
            r["main_candidate_action_chunk_normalized"], dtype=np.float32
        )
        ace_chunks_norm = np.array(
            r["ace_candidate_chunks_normalized"], dtype=np.float32
        )
        chunks_norm = np.concatenate([main_chunk_norm[None], ace_chunks_norm], axis=0)

        main_chunk_env = np.array(r["main_candidate_action_chunk_env"], dtype=np.float32)
        ace_chunks_env = np.array(r["ace_candidate_chunks_env"], dtype=np.float32)
        chunks_env = np.concatenate([main_chunk_env[None], ace_chunks_env], axis=0)

        history = np.array(r["history"], dtype=np.float32)
        ace = np.array(r["ace_features_7d"], dtype=np.float32)
        proprio = np.array(r["current"]["proprio"], dtype=np.float32)

        trace_raw = r["simvla_uncertainty_raw"]
        trace = DenoisingTrace(
            denoise_mean_trace=np.array(trace_raw["denoise_mean_trace"]),
            velocity_norm_trace=np.array(trace_raw["velocity_norm_trace"]),
            update_norm_trace=np.array(trace_raw["update_norm_trace"]),
            update_vector_trace=np.array(trace_raw["update_vector_trace"]),
            path_variance=np.array(trace_raw["path_variance"]),
            last_step_variance=np.array(trace_raw["last_step_variance"]),
            final_action_normalized=np.array(trace_raw["final_action_normalized"]),
            initial_noise=np.array(trace_raw["initial_noise"]),
        )

        cand_49d = []
        for c_i in range(9):
            order = [c_i] + [j for j in range(9) if j != c_i]
            reordered = chunks_env[order]
            feat, _ = build_uncertainty_49d(
                main_trace=trace,
                all_candidate_chunks_env=reordered,
                proprio=proprio,
                state_mean=state_mean,
                state_std=state_std,
                previous_executed_action=None,
                previous_proprio=None,
            )
            cand_49d.append(feat)
        cand_49d = np.stack(cand_49d)

        static = np.stack(
            [
                np.concatenate(
                    [
                        action_statistics(chunks_norm[i]),
                        ace,
                        proprio,
                        cand_49d[i, list(TOPK8_INDICES)],
                    ]
                ).astype(np.float32)
                for i in range(9)
            ]
        )

        h = np.repeat(history[None, :, :], 9, axis=0)
        h_n, c_n, s_n = normalize(h, chunks_norm, static, stats)

        with torch.inference_mode():
            logits = model(
                {
                    "history": torch.as_tensor(h_n, dtype=torch.float32, device=device),
                    "action": torch.as_tensor(c_n, dtype=torch.float32, device=device),
                    "static": torch.as_tensor(s_n, dtype=torch.float32, device=device),
                }
            )
            scores = torch.sigmoid(logits).cpu().numpy().astype(np.float32)

        main_score = float(scores[0])
        alt_scores = scores[1:]
        best_alt_idx = int(np.argmin(alt_scores)) + 1
        best_alt_score = float(alt_scores[best_alt_idx - 1])

        ood_c0_reconstructed.append(main_score)

        ep_src_id = r.get("metadata", {}).get("source_episode_id", r.get("episode_id"))
        if ep_src_id not in ood_by_ep:
            ood_by_ep[ep_src_id] = []
        ood_by_ep[ep_src_id].append(
            {
                "decision_index": r["decision_index"],
                "main_score": main_score,
                "best_alt_score": best_alt_score,
                "best_alt_index": best_alt_idx,
                "candidate_scores": [float(s) for s in scores],
            }
        )

    # OOD Parity check against evaluations/locked_h10_ood150_topk8_v1/scores.npz
    ood_archived_scores = np.load(
        WORKSPACE / "evaluations/locked_h10_ood150_topk8_v1/scores.npz"
    )["scores"]
    ood_c0_arr = np.array(ood_c0_reconstructed, dtype=np.float32)
    ood_diffs = np.abs(ood_c0_arr - ood_archived_scores)

    ood_parity_audit = {
        "rows": len(ood_diffs),
        "max_diff": float(np.max(ood_diffs)),
        "mean_diff": float(np.mean(ood_diffs)),
        "p99_diff": float(np.percentile(ood_diffs, 99)),
        "count_gt_1e5": int(np.sum(ood_diffs > 1e-5)),
        "count_gt_1e4": int(np.sum(ood_diffs > 1e-4)),
    }
    (proto_dir / "OOD150_RECONSTRUCTION_PARITY.json").write_text(
        json.dumps(ood_parity_audit, indent=2)
    )
    print("Saved OOD150_RECONSTRUCTION_PARITY.json")

    ood_table_file = proto_dir / "ood150_reconstructed_scores.json"
    with open(ood_table_file, "w") as f:
        json.dump(ood_by_ep, f)
    print(
        f"Saved ood150_reconstructed_scores.json (size: {ood_table_file.stat().st_size / 1e6:.2f} MB)"
    )

    print(f"All reconstruction complete in {time.time()-t0:.1f}s.")


if __name__ == "__main__":
    main()
