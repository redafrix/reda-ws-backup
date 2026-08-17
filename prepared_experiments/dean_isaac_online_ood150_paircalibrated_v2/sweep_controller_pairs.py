#!/usr/bin/env python3
"""Sweep controller pairs across seen splits, generate Pareto shortlist, and evaluate/select on OOD150."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import numpy as np

WORKSPACE = Path(sys.argv[1] if len(sys.argv) > 1 else "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
PROTO = WORKSPACE / "online_evals/isaac_ood150_paircalibrated_v2"


def main() -> None:
    # 1. Load reconstructed scores
    seen_scores_path = PROTO / "seen4000_reconstructed_scores.json"
    if not seen_scores_path.exists():
        raise FileNotFoundError(f"Missing {seen_scores_path}. Run reconstruct_candidate_scores.py first.")

    with open(seen_scores_path) as f:
        split_episodes = json.load(f)

    ood_scores_path = PROTO / "ood150_reconstructed_scores.json"
    if not ood_scores_path.exists():
        raise FileNotFoundError(f"Missing {ood_scores_path}. Run reconstruct_candidate_scores.py first.")

    with open(ood_scores_path) as f:
        ood_by_ep = json.load(f)

    ood_summaries = [
        json.loads(line)
        for line in (WORKSPACE / "outputs/final_locked_h10_ood150_seed20260728/episode_summaries.jsonl").read_text().splitlines()
        if line.strip()
    ]

    # 2. Main Alarm Threshold Grid
    val_success_eps = [e for e in split_episodes["validation"] if e["success"]]
    val_succ_max_scores = np.array([e["max_main_score"] for e in val_success_eps])
    num_val_succ = len(val_succ_max_scores)

    quantiles = [50, 60, 70, 75, 80, 85, 90, 92.5, 95, 97.5, 99]
    main_threshold_candidates = {}

    for q in quantiles:
        val = float(np.percentile(val_succ_max_scores, q))
        main_threshold_candidates[f"q{q}_val_success_max"] = {
            "name": f"q{q}_val_success_max",
            "value": val,
            "derivation": f"Empirical {q}th percentile of episode-max main scores on successful validation episodes",
            "source_split": "validation_successful_episodes",
            "calibration_episodes_count": num_val_succ,
        }

    named_th = json.loads((WORKSPACE / "models/isaac_h10_topk8_temporal_v1/thresholds.json").read_text())
    for k in ["best_val_f1", "fixed_0.5", "q90_success", "q95_success", "q99_success"]:
        if k in named_th:
            main_threshold_candidates[f"legacy_{k}"] = {
                "name": f"legacy_{k}",
                "value": float(named_th[k]),
                "derivation": f"Historical baseline threshold {k}",
                "source_split": "validation",
                "calibration_episodes_count": num_val_succ,
            }

    unique_main_thresholds = []
    seen_vals = set()
    for k, v in main_threshold_candidates.items():
        rval = round(v["value"], 6)
        if rval not in seen_vals:
            seen_vals.add(rval)
            unique_main_thresholds.append(v)

    unique_main_thresholds.sort(key=lambda x: x["value"])
    (PROTO / "SEEN_MAIN_THRESHOLD_GRID.json").write_text(json.dumps(unique_main_thresholds, indent=2))
    print(f"Generated {len(unique_main_thresholds)} unique main threshold candidates.")

    # 3. Alternative Cap Grid
    val_decisions = []
    for e in split_episodes["validation"]:
        val_decisions.extend(e["decisions"])

    cap_quantiles = [5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95]
    cap_grid_by_alarm = {}

    for m in unique_main_thresholds:
        A = m["value"]
        m_name = m["name"]

        cond_best_alts = [
            d["best_alt_score"]
            for d in val_decisions
            if d["main_score"] >= A and d["best_alt_score"] < d["main_score"]
        ]

        caps = []
        if len(cond_best_alts) >= 10:
            arr = np.array(cond_best_alts)
            seen_cap_vals = set()
            for cq in cap_quantiles:
                cval = float(np.percentile(arr, cq))
                rcval = round(cval, 6)
                if rcval not in seen_cap_vals:
                    seen_cap_vals.add(rcval)
                    caps.append(
                        {
                            "cap_quantile": cq,
                            "cap_value": cval,
                            "derivation": f"Conditional {cq}th percentile of best_alt scores on validation decisions with main >= {A:.4f} and best_alt < main",
                            "calibration_decisions_count": len(cond_best_alts),
                        }
                    )
        else:
            caps.append(
                {
                    "cap_quantile": 50,
                    "cap_value": float(np.median(cond_best_alts)) if cond_best_alts else 0.5,
                    "derivation": "Fallback low-sample conditional median",
                    "calibration_decisions_count": len(cond_best_alts),
                }
            )

        cap_grid_by_alarm[m_name] = {
            "main_threshold": m,
            "conditional_decisions_count": len(cond_best_alts),
            "caps": caps,
        }

    (PROTO / "SEEN_ALARM_CONDITIONAL_CAP_GRID.json").write_text(json.dumps(cap_grid_by_alarm, indent=2))
    print(f"Generated alarm-conditional cap grid for all main thresholds.")

    # 4. Full Pair Sweep on Seen
    def evaluate_pairs_on_split(episodes: list[dict]) -> dict[str, dict]:
        succ_eps = [e for e in episodes if e["success"]]
        fail_eps = [e for e in episodes if not e["success"]]
        num_succ = len(succ_eps)
        num_fail = len(fail_eps)

        pair_results = {}

        for m in unique_main_thresholds:
            A = m["value"]
            m_name = m["name"]
            caps_info = cap_grid_by_alarm[m_name]["caps"]

            for c in caps_info:
                C = c["cap_value"]
                cq = c["cap_quantile"]
                pair_key = f"{m_name}__cap_q{cq}"

                # Evaluate on success episodes
                succ_intervened_eps = 0
                total_succ_opps = 0
                succ_opps_per_ep = []
                succ_first_fracs = []

                for e in succ_eps:
                    opps = 0
                    first_frac = None
                    for d in e["decisions"]:
                        if d["main_score"] >= A and d["best_alt_score"] < d["main_score"] and d["best_alt_score"] <= C:
                            opps += 1
                            if first_frac is None:
                                first_frac = d["decision_fraction"]
                    total_succ_opps += opps
                    succ_opps_per_ep.append(opps)
                    if opps > 0:
                        succ_intervened_eps += 1
                        succ_first_fracs.append(first_frac)

                # Evaluate on failure episodes
                fail_intervened_eps = 0
                total_fail_opps = 0
                fail_opps_per_ep = []
                fail_first_fracs = []
                opp10 = 0
                opp25 = 0
                opp50 = 0

                for e in fail_eps:
                    opps = 0
                    first_frac = None
                    for d in e["decisions"]:
                        if d["main_score"] >= A and d["best_alt_score"] < d["main_score"] and d["best_alt_score"] <= C:
                            opps += 1
                            if first_frac is None:
                                first_frac = d["decision_fraction"]
                    total_fail_opps += opps
                    fail_opps_per_ep.append(opps)
                    if opps > 0:
                        fail_intervened_eps += 1
                        fail_first_fracs.append(first_frac)
                        if first_frac <= 0.10:
                            opp10 += 1
                        if first_frac <= 0.25:
                            opp25 += 1
                        if first_frac <= 0.50:
                            opp50 += 1

                succ_rate = succ_intervened_eps / max(1, num_succ)
                fail_rate = fail_intervened_eps / max(1, num_fail)
                separation = fail_rate - succ_rate
                total_intervened = succ_intervened_eps + fail_intervened_eps
                precision = fail_intervened_eps / max(1, total_intervened)

                pair_results[pair_key] = {
                    "main_name": m_name,
                    "main_value": A,
                    "cap_quantile": cq,
                    "cap_value": C,
                    "success_episodes": num_succ,
                    "failure_episodes": num_fail,
                    "success_intervention_episodes": succ_intervened_eps,
                    "failure_intervention_episodes": fail_intervened_eps,
                    "success_intervention_rate": succ_rate,
                    "failure_intervention_rate": fail_rate,
                    "failure_opp_at_10": opp10 / max(1, num_fail),
                    "failure_opp_at_25": opp25 / max(1, num_fail),
                    "failure_opp_at_50": opp50 / max(1, num_fail),
                    "total_success_opportunities": total_succ_opps,
                    "total_failure_opportunities": total_fail_opps,
                    "mean_succ_opportunities": float(np.mean(succ_opps_per_ep)) if succ_opps_per_ep else 0.0,
                    "mean_fail_opportunities": float(np.mean(fail_opps_per_ep)) if fail_opps_per_ep else 0.0,
                    "mean_first_fail_fraction": float(np.mean(fail_first_fracs)) if fail_first_fracs else None,
                    "separation": separation,
                    "intervention_precision": precision,
                }

        return pair_results

    print("Evaluating pair sweep on Validation...")
    val_pair_results = evaluate_pairs_on_split(split_episodes["validation"])

    print("Evaluating pair sweep on Test...")
    test_pair_results = evaluate_pairs_on_split(split_episodes["test"])

    print("Evaluating pair sweep on Train...")
    train_pair_results = evaluate_pairs_on_split(split_episodes["train"])

    all_eps = split_episodes["train"] + split_episodes["validation"] + split_episodes["test"]
    all_pair_results = evaluate_pairs_on_split(all_eps)

    pair_sweep_export = {
        "validation": val_pair_results,
        "test": test_pair_results,
        "train": train_pair_results,
        "all4000": all_pair_results,
    }
    (PROTO / "SEEN_PAIR_SWEEP.json").write_text(json.dumps(pair_sweep_export, indent=2))
    print(f"Saved SEEN_PAIR_SWEEP.json with {len(val_pair_results)} unique pairs.")

    # 5. Pareto Shortlist from Validation
    pairs_list = list(val_pair_results.values())
    tiers = {
        "very_conservative": [p for p in pairs_list if p["success_intervention_rate"] <= 0.05],
        "balanced": [p for p in pairs_list if p["success_intervention_rate"] <= 0.10],
        "moderate": [p for p in pairs_list if p["success_intervention_rate"] <= 0.20],
        "aggressive": [p for p in pairs_list if p["success_intervention_rate"] <= 0.30],
    }

    def rank_tier(cand_list: list[dict]) -> list[dict]:
        return sorted(
            cand_list,
            key=lambda p: (
                p["failure_intervention_rate"],
                p["failure_opp_at_25"],
                p["separation"],
                p["total_failure_opportunities"],
                -p["success_intervention_rate"],
                p["main_value"],
                -p["cap_value"],
            ),
            reverse=True,
        )

    shortlist_candidates = {}
    for tname, clist in tiers.items():
        if clist:
            ranked = rank_tier(clist)
            for r_idx, best_p in enumerate(ranked[:3]):
                pkey = f"{best_p['main_name']}__cap_q{best_p['cap_quantile']}"
                shortlist_candidates[pkey] = {
                    "tier": tname,
                    "tier_rank": r_idx + 1,
                    "pair_key": pkey,
                    "main_name": best_p["main_name"],
                    "main_value": best_p["main_value"],
                    "cap_quantile": best_p["cap_quantile"],
                    "cap_value": best_p["cap_value"],
                    "seen_validation_metrics": best_p,
                    "seen_test_metrics": test_pair_results[pkey],
                }

    shortlist_list = list(shortlist_candidates.values())
    (PROTO / "SEEN_PARETO_SHORTLIST.json").write_text(json.dumps(shortlist_list, indent=2))
    print(f"Generated Seen Pareto Shortlist with {len(shortlist_list)} unique pairs.")

    # 6. Evaluate Shortlist on Historical OOD150
    ood_succ_eps = [e for e in ood_summaries if e["success"]]
    ood_fail_eps = [e for e in ood_summaries if not e["success"]]
    num_ood_succ = len(ood_succ_eps)
    num_ood_fail = len(ood_fail_eps)

    ood_eval_results = []

    for s_item in shortlist_list:
        A = s_item["main_value"]
        C = s_item["cap_value"]
        m_name = s_item["main_name"]
        cq = s_item["cap_quantile"]

        succ_intervened_eps = 0
        succ_replacements = 0

        for e in ood_succ_eps:
            sid = str(e["source_episode_id"])
            decs = ood_by_ep.get(sid, [])
            opps = 0
            for d in decs:
                if d["main_score"] >= A and d["best_alt_score"] < d["main_score"] and d["best_alt_score"] <= C:
                    opps += 1
            succ_replacements += opps
            if opps > 0:
                succ_intervened_eps += 1

        fail_intervened_eps = 0
        fail_replacements = 0
        opp10 = 0
        opp25 = 0
        opp50 = 0

        for e in ood_fail_eps:
            sid = str(e["source_episode_id"])
            decs = ood_by_ep.get(sid, [])
            opps = 0
            first_frac = None
            n_decs = len(decs)
            for d_i, d in enumerate(decs):
                if d["main_score"] >= A and d["best_alt_score"] < d["main_score"] and d["best_alt_score"] <= C:
                    opps += 1
                    if first_frac is None:
                        first_frac = (d_i + 1) / max(1, n_decs)
            fail_replacements += opps
            if opps > 0:
                fail_intervened_eps += 1
                if first_frac is not None:
                    if first_frac <= 0.10:
                        opp10 += 1
                    if first_frac <= 0.25:
                        opp25 += 1
                    if first_frac <= 0.50:
                        opp50 += 1

        succ_rate = succ_intervened_eps / max(1, num_ood_succ)
        fail_rate = fail_intervened_eps / max(1, num_ood_fail)
        separation = fail_rate - succ_rate
        total_replacements = succ_replacements + fail_replacements
        precision = fail_intervened_eps / max(1, (succ_intervened_eps + fail_intervened_eps))

        eval_record = {
            "pair_key": s_item["pair_key"],
            "tier": s_item["tier"],
            "main_name": m_name,
            "main_value": A,
            "cap_quantile": cq,
            "cap_value": C,
            "historical_success_episodes": num_ood_succ,
            "historical_failure_episodes": num_ood_fail,
            "ood_success_intervention_rate": succ_rate,
            "ood_failure_intervention_rate": fail_rate,
            "ood_failure_opp_at_10": opp10 / max(1, num_ood_fail),
            "ood_failure_opp_at_25": opp25 / max(1, num_ood_fail),
            "ood_failure_opp_at_50": opp50 / max(1, num_ood_fail),
            "ood_total_predicted_replacements": total_replacements,
            "ood_failure_side_replacements": fail_replacements,
            "ood_success_side_replacements": succ_replacements,
            "ood_distinct_failure_episodes": fail_intervened_eps,
            "ood_distinct_success_episodes": succ_intervened_eps,
            "ood_separation": separation,
            "ood_intervention_precision": precision,
            "seen_validation_metrics": s_item["seen_validation_metrics"],
            "seen_test_metrics": s_item["seen_test_metrics"],
        }
        ood_eval_results.append(eval_record)

    (PROTO / "OOD150_SHORTLIST_PAIR_EVAL.json").write_text(json.dumps(ood_eval_results, indent=2))
    print("Saved OOD150_SHORTLIST_PAIR_EVAL.json")

    # 7. Deterministic Ranking on OOD150
    def ood_rank_key(p: dict) -> tuple:
        passes_pref = p["ood_success_intervention_rate"] <= 0.20
        return (
            p["ood_total_predicted_replacements"] > 0,
            p["ood_failure_intervention_rate"] > p["ood_success_intervention_rate"],
            passes_pref,
            p["ood_failure_intervention_rate"],
            p["ood_failure_opp_at_25"],
            p["ood_separation"],
            p["ood_failure_side_replacements"],
            -p["ood_success_intervention_rate"],
            p["main_value"],
            -p["cap_value"],
        )

    sorted_ood_pairs = sorted(ood_eval_results, key=ood_rank_key, reverse=True)
    top10_pairs = sorted_ood_pairs[:10]

    (PROTO / "OOD150_TOP10_PAIRS.json").write_text(json.dumps(top10_pairs, indent=2))
    print("Saved OOD150_TOP10_PAIRS.json")

    selected_pair = sorted_ood_pairs[0]
    print(f"Selected Pair: {selected_pair['pair_key']}")

    # 8. Write SELECTED_CONTROLLER_PAIR.json
    model_sha = hashlib.sha256((WORKSPACE / "models/isaac_h10_topk8_temporal_v1/model.pt").read_bytes()).hexdigest()
    norm_sha = hashlib.sha256((WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1/normalization.json").read_bytes()).hexdigest()
    scorer_sha = hashlib.sha256((Path(__file__)).read_bytes()).hexdigest()

    selected_controller_pair = {
        "schema_version": "isaac_offline_pair_calibrated_controller_v2",
        "model_sha256": model_sha,
        "normalization_sha256": norm_sha,
        "offline_scorer_sha256": scorer_sha,
        "main_threshold_name": selected_pair["main_name"],
        "main_threshold_value": selected_pair["main_value"],
        "main_threshold_derivation": f"Empirical quantile on successful validation episodes",
        "selected_cap_name": f"alarm_conditional_q{selected_pair['cap_quantile']}",
        "selected_cap_value": selected_pair["cap_value"],
        "selected_cap_derivation": f"Conditional {selected_pair['cap_quantile']}th percentile of best_alt scores on validation decisions with main >= alarm and best_alt < main",
        "seen_validation_metrics": selected_pair["seen_validation_metrics"],
        "seen_test_metrics": selected_pair["seen_test_metrics"],
        "ood_offline_metrics": {
            "historical_success_episodes": 72,
            "historical_failure_episodes": 78,
            "success_intervention_rate": selected_pair["ood_success_intervention_rate"],
            "failure_intervention_rate": selected_pair["ood_failure_intervention_rate"],
            "failure_opp_at_25": selected_pair["ood_failure_opp_at_25"],
            "total_predicted_replacements": selected_pair["ood_total_predicted_replacements"],
            "failure_side_replacements": selected_pair["ood_failure_side_replacements"],
            "success_side_replacements": selected_pair["ood_success_side_replacements"],
            "distinct_failure_episodes": selected_pair["ood_distinct_failure_episodes"],
            "distinct_success_episodes": selected_pair["ood_distinct_success_episodes"],
            "separation": selected_pair["ood_separation"],
            "intervention_precision": selected_pair["ood_intervention_precision"],
        },
        "selection_reason": "Deterministic OOD ranking over frozen seen-derived Pareto shortlist with positive intervention opportunities",
    }

    (PROTO / "SELECTED_CONTROLLER_PAIR.json").write_text(json.dumps(selected_controller_pair, indent=2))
    print("Saved SELECTED_CONTROLLER_PAIR.json")


if __name__ == "__main__":
    main()
