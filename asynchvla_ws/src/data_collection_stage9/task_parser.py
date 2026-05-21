from __future__ import annotations
import re
from dataclasses import dataclass

STOP = {
    "the", "a", "an", "and", "it", "both", "left", "right", "front", "back",
    "of", "to", "in", "on", "at", "into", "onto",
    "place", "put", "pick", "up", "move", "stack", "with",
}
LOCATOR = {
    "between", "near", "next", "beside", "inside", "from", "under", "above",
    "behind", "front", "left", "right", "middle", "top", "bottom", "main",
}
GOAL_HINTS = {
    "basket", "tray", "plate", "drawer", "cabinet", "stove", "microwave", "caddy",
    "rack", "shelf", "compartment", "bowl", "ramekin", "mug", "cup", "box",
    "container", "pan", "pot", "middle", "top", "bottom",
}

def norm(s: str) -> str:
    s = s.lower().replace("-", " ")
    s = re.sub(r"[^a-z0-9_ ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def obs_bases(obs: dict) -> list[str]:
    bases = []
    for k in obs.keys():
        if k.endswith("_pos") and not k.endswith("_to_robot0_eef_pos"):
            bases.append(k[:-4])
    return sorted(set(bases), key=len, reverse=True)

def base_to_phrase(base: str) -> str:
    return re.sub(r"_\d+", "", base).replace("_", " ")

def base_to_body_prefix(base: str) -> str:
    return base

def content_tokens(s: str) -> list[str]:
    return [
        t for t in norm(s).split()
        if t not in STOP and t not in LOCATOR and not t.isdigit()
    ]

def strip_locator_phrase(s: str) -> str:
    text = norm(s)
    for marker in [
        " between ", " next to ", " beside ", " near ", " in front of ",
        " behind ", " on the left", " on the right", " from ",
    ]:
        if marker in text:
            return text.split(marker, 1)[0].strip()
    return text

def extract_pick_target_phrase(language: str) -> str | None:
    text = norm(language)
    match = re.search(
        r"(?:pick up|pick|grasp|take|lift)\s+(?:the\s+|a\s+|an\s+)?(.+?)(?:\s+and\s+(?:place|put|move|stack)|\s+then\s+(?:place|put|move|stack)|$)",
        text,
    )
    if not match:
        return None
    return strip_locator_phrase(match.group(1))

def extract_goal_phrase(language: str) -> str | None:
    text = norm(language)
    patterns = [
        r"(?:place|put|move|stack)\s+(?:it|the object|the item)?\s*(?:on|onto|in|into|inside|to)\s+(?:the\s+|a\s+|an\s+)?(.+?)(?:$|\s+and\s+)",
        r"(?:place|put|move|stack).+?\s(?:on|onto|in|into|inside|to)\s+(?:the\s+|a\s+|an\s+)?(.+?)(?:$|\s+and\s+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return strip_locator_phrase(match.group(1))
    return None

def _position_for_base(obs: dict, base: str):
    import numpy as np
    candidates = [base]
    if base.endswith("_main"):
        candidates.append(base[:-5])
    for cand in candidates:
        key = f"{cand}_pos"
        if key in obs:
            try:
                return np.asarray(obs[key], dtype=float)
            except Exception:
                return None
    return None

def _between_locator_phrases(language: str) -> tuple[str, str] | None:
    text = norm(language)
    match = re.search(
        r"\bbetween\s+(?:the\s+|a\s+|an\s+)?(.+?)\s+and\s+(?:the\s+|a\s+|an\s+)?(.+?)(?:$|\s+and\s+(?:place|put|move|stack)|\s+then\s+)",
        text,
    )
    if not match:
        return None
    return strip_locator_phrase(match.group(1)), strip_locator_phrase(match.group(2))

def select_base_for_phrase(
    phrase: str | None,
    mentioned: list[str],
    obs: dict,
    exclude: set[str] | None = None,
    language_for_between: str | None = None,
) -> str | None:
    if not phrase:
        return None
    exclude = exclude or set()
    obs_base_set = set(obs_bases(obs))
    query_tokens = set(content_tokens(phrase))
    if not query_tokens:
        return None

    scored: list[tuple[float, str]] = []
    for base in mentioned:
        if base in exclude:
            continue
        phrase_base = base_to_phrase(base)
        base_tokens = set(content_tokens(phrase_base))
        shared = query_tokens & base_tokens
        if not shared:
            continue
        score = 10.0 * len(shared)
        if " ".join(query_tokens) in phrase_base:
            score += 4.0
        if base in obs_base_set:
            score += 2.0
        # Prefer concrete object bases over object sub-bodies when both match.
        if base.endswith("_main"):
            score -= 0.5
        scored.append((score, base))
    if not scored:
        return None

    best_score = max(score for score, _base in scored)
    candidates = [base for score, base in scored if abs(score - best_score) < 1e-6]

    # If the instruction disambiguates the object spatially ("bowl between
    # plate and ramekin"), use the midpoint between locator objects as a
    # tie-breaker among same-name candidates.
    if language_for_between and len(candidates) > 1:
        between = _between_locator_phrases(language_for_between)
        if between:
            left = select_base_for_phrase(between[0], mentioned, obs, exclude=set(candidates))
            right = select_base_for_phrase(between[1], mentioned, obs, exclude=set(candidates) | ({left} if left else set()))
            left_pos = _position_for_base(obs, left) if left else None
            right_pos = _position_for_base(obs, right) if right else None
            if left_pos is not None and right_pos is not None:
                import numpy as np
                midpoint = 0.5 * (left_pos + right_pos)
                with_dist = []
                for base in candidates:
                    pos = _position_for_base(obs, base)
                    if pos is not None:
                        with_dist.append((float(np.linalg.norm(pos - midpoint)), base))
                if with_dist:
                    with_dist.sort(key=lambda x: x[0])
                    return with_dist[0][1]

    return sorted(candidates, key=lambda b: (b.endswith("_main"), -len(b), b))[0]

def mentioned_bases(language: str, obs: dict, all_bodies: list[str] | None = None) -> list[str]:
    text = norm(language)
    found_with_score = []
    bases = obs_bases(obs)
    if all_bodies:
        ignore = ("world", "robot", "gripper", "eef", "mount", "base", "link", "wrist", "camera", "table", "floor")
        filtered_bodies = [b for b in all_bodies if not any(x in b.lower() for x in ignore)]
        bases = sorted(set(bases + filtered_bodies), key=len, reverse=True)

    for base in bases:
        phrase = base_to_phrase(base)
        toks = [t for t in phrase.split() if t not in STOP]
        score = 0
        if phrase in text:
            score = 100 # Exact phrase match
        elif toks:
            shared = [t for t in toks if t in text]
            if len(shared) > 0:
                # Count how many distinct tokens from base are in text
                distinct_shared = set(shared)
                if len(distinct_shared) >= 2 or (len(distinct_shared) == 1 and any(h in distinct_shared for h in GOAL_HINTS)):
                    score = len(distinct_shared)
        
        if score > 0:
            found_with_score.append((base, score))
    
    # Sort by score descending, then by length descending
    found_with_score.sort(key=lambda x: (x[1], len(x[0])), reverse=True)
    return [x[0] for x in found_with_score]

def extract_relation(language: str) -> str:
    t = norm(language)
    if any(w in t for w in ["place", "put", "stack"]):
        return "place_or_put"
    if "open" in t or "close" in t or "turn" in t:
        return "articulation_or_toggle"
    if "pick" in t:
        return "pick"
    return "unknown"

def parse_task_context(language: str, obs: dict, all_bodies: list[str] | None = None) -> dict:
    mentioned = mentioned_bases(language, obs, all_bodies)
    relation = extract_relation(language)
    target = None
    goal = None

    if relation == "place_or_put":
        target = select_base_for_phrase(
            extract_pick_target_phrase(language),
            mentioned,
            obs,
            language_for_between=language,
        )
        goal = select_base_for_phrase(
            extract_goal_phrase(language),
            mentioned,
            obs,
            exclude={target} if target else set(),
        )

    if target is None:
        target = mentioned[0] if mentioned else None
    if goal is None:
        for base in mentioned:
            if base == target:
                continue
            phrase = base_to_phrase(base)
            if any(h in phrase.split() or h in phrase for h in GOAL_HINTS):
                goal = base
                break
    if goal is None and len(mentioned) >= 2:
        goal = next((base for base in mentioned if base != target), None)
    confidence = "LOW"
    if target:
        confidence = "HIGH" if relation == "place_or_put" and goal else "MEDIUM"
    return {
        "task_language": language,
        "relation": relation,
        "mentioned_bases": mentioned,
        "target_base": target,
        "goal_base": goal,
        "target_body_prefix": base_to_body_prefix(target) if target else None,
        "goal_body_prefix": base_to_body_prefix(goal) if goal else None,
        "parse_confidence": confidence,
        "parser_version": "stage9_task_parser_v2_pick_place_roles",
        "parsed_target_phrase": extract_pick_target_phrase(language),
        "parsed_goal_phrase": extract_goal_phrase(language),
    }
