from __future__ import annotations
import os
import re
from dataclasses import dataclass
from pathlib import Path

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

_bddl_cache: dict[str, tuple[str | None, str | None]] | None = None

def get_bddl_mapping() -> dict[str, tuple[str | None, str | None]]:
    global _bddl_cache
    if _bddl_cache is not None:
        return _bddl_cache

    # 1. Try to dynamically load and parse BDDL files on the filesystem
    bddl_paths = [
        Path("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/LIBERO/libero/libero/bddl_files"),
        Path("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files"),
    ]
    
    bddl_dir = None
    for p in bddl_paths:
        if p.exists():
            bddl_dir = p
            break
            
    if bddl_dir:
        try:
            bddl_files = list(bddl_dir.rglob("*.bddl"))
            if bddl_files:
                mapping = {}
                for f_path in bddl_files:
                    content = f_path.read_text()
                    lang_match = re.search(r'\(:language\s+([^)]+)\)', content)
                    if not lang_match:
                        continue
                    language = lang_match.group(1).strip()
                    if (language.startswith('"') and language.endswith('"')) or (language.startswith("'") and language.endswith("'")):
                        language = language[1:-1]
                    
                    goal_match = re.search(r'\(:goal\s+(.*?)\n\s*\)', content, re.DOTALL)
                    if not goal_match:
                        continue
                    goal_str = goal_match.group(1).strip()
                    
                    # Prioritize In/On/Under
                    target, goal = None, None
                    pattern = r'\(\s*(in|on|under|open|close|turnon|turnoff|closed|turnedon|turnedoff)\s+([^)]+)\)'
                    predicates = re.findall(pattern, goal_str, re.IGNORECASE)
                    
                    found_io = False
                    for pred, args_str in predicates:
                        pred_lower = pred.lower()
                        if pred_lower in ("in", "on", "under"):
                            args = args_str.split()
                            if len(args) >= 2:
                                target = args[0]
                                goal_obj = args[1]
                                suffixes = [
                                    "_region", "_contain_region", "_init_region", "_front_region", 
                                    "_left_region", "_right_region", "_back_region", "_top_region", 
                                    "_bottom_region", "_cook_region", "_heating_region"
                                ]
                                for suffix in suffixes:
                                    if goal_obj.endswith(suffix):
                                        goal_obj = goal_obj[:-len(suffix)]
                                        break
                                parts = [
                                    "_back_contain", "_front_contain", "_left_contain", "_right_contain", 
                                    "_heating", "_cook", "_drawer_bottom", "_drawer_top", "_drawer", 
                                    "_bottom", "_top"
                                ]
                                for part in parts:
                                    if goal_obj.endswith(part):
                                        goal_obj = goal_obj[:-len(part)]
                                target = target
                                goal = goal_obj
                                found_io = True
                                break
                    if not found_io:
                        for pred, args_str in predicates:
                            pred_lower = pred.lower()
                            if pred_lower in ("open", "close", "turnon", "turnoff", "closed", "turnedon", "turnedoff"):
                                args = args_str.split()
                                if args:
                                    target = args[0]
                                    goal = None
                                    break
                    mapping[language.strip()] = (target, goal)
                _bddl_cache = mapping
                return _bddl_cache
        except Exception:
            pass

    # 2. Fallback to pre-compiled dictionary
    _bddl_cache = {
        'turn on the stove and put the moka pot on it': ('moka_pot_1', 'flat_stove_1'),
        'put the black bowl in the bottom drawer of the cabinet and close it': ('akita_black_bowl_1', 'white_cabinet_1'),
        'put the yellow and white mug in the microwave and close it': ('white_yellow_mug_1', 'microwave_1'),
        'put both moka pots on the stove': ('moka_pot_1', 'flat_stove_1'),
        'put both the alphabet soup and the cream cheese box in the basket': ('alphabet_soup_1', 'basket_1_contain'),
        'put both the alphabet soup and the tomato sauce in the basket': ('alphabet_soup_1', 'basket_1_contain'),
        'put both the cream cheese box and the butter in the basket': ('cream_cheese_1', 'basket_1_contain'),
        'put the white mug on the left plate and put the yellow and white mug on the right plate': ('porcelain_mug_1', 'plate_1'),
        'put the white mug on the plate and put the chocolate pudding to the right of the plate': ('porcelain_mug_1', 'plate_1'),
        'pick up the book and place it in the back compartment of the caddy': ('black_book_1', 'desk_caddy_1'),
        'close the top drawer of the cabinet': ('white_cabinet_1_top_region', None),
        'close the top drawer of the cabinet and put the black bowl on top of it': ('akita_black_bowl_1', 'wooden_cabinet_1_top_side'),
        'put the black bowl in the top drawer of the cabinet': ('akita_black_bowl_1', 'white_cabinet_1'),
        'put the butter at the back in the top drawer of the cabinet and close it': ('butter_2', 'wooden_cabinet_1'),
        'put the butter at the front in the top drawer of the cabinet and close it': ('butter_1', 'wooden_cabinet_1'),
        'put the chocolate pudding in the top drawer of the cabinet and close it': ('chocolate_pudding_1', 'wooden_cabinet_1'),
        'open the bottom drawer of the cabinet': ('wooden_cabinet_1_bottom_region', None),
        'open the top drawer of the cabinet': ('wooden_cabinet_1_top_region', None),
        'open the top drawer of the cabinet and put the bowl in it': ('akita_black_bowl_1', 'wooden_cabinet_1'),
        'put the black bowl on the plate': ('akita_black_bowl_1', 'plate_1'),
        'put the black bowl on top of the cabinet': ('akita_black_bowl_1', 'white_cabinet_1_top_side'),
        'put the black bowl at the back on the plate': ('akita_black_bowl_3', 'plate_1'),
        'put the black bowl at the front on the plate': ('akita_black_bowl_1', 'plate_1'),
        'put the black bowl in the middle on the plate': ('akita_black_bowl_2', 'plate_1'),
        'put the middle black bowl on top of the cabinet': ('akita_black_bowl_2', 'wooden_cabinet_1_top_side'),
        'stack the black bowl at the front on the black bowl in the middle': ('akita_black_bowl_1', 'akita_black_bowl_2'),
        'stack the black bowl in the middle on the black bowl at the front': ('akita_black_bowl_2', 'akita_black_bowl_3'),
        'put the frying pan on the stove': ('chefmate_8_frypan_1', 'flat_stove_1'),
        'put the moka pot on the stove': ('moka_pot_1', 'flat_stove_1'),
        'turn on the stove': ('flat_stove_1', None),
        'turn on the stove and put the frying pan on it': ('chefmate_8_frypan_1', 'flat_stove_1'),
        'close the bottom drawer of the cabinet': ('white_cabinet_1_bottom_region', None),
        'close the bottom drawer of the cabinet and open the top drawer': ('white_cabinet_1_bottom_region', None),
        'put the black bowl in the bottom drawer of the cabinet': ('akita_black_bowl_1', 'white_cabinet_1'),
        'put the wine bottle in the bottom drawer of the cabinet': ('wine_bottle_1', 'white_cabinet_1'),
        'put the wine bottle on the wine rack': ('wine_bottle_1', 'wine_rack_1'),
        'put the ketchup in the top drawer of the cabinet': ('ketchup_1', 'white_cabinet_1'),
        'close the microwave': ('microwave_1', None),
        'put the yellow and white mug to the front of the white mug': ('white_yellow_mug_1', 'kitchen_table_porcelain_mug_front'),
        'open the microwave': ('microwave_1', None),
        'put the white bowl on the plate': ('white_bowl_1', 'plate_1'),
        'put the white bowl to the right of the plate': ('white_bowl_1', 'kitchen_table_plate_right'),
        'put the right moka pot on the stove': ('moka_pot_1', 'flat_stove_1'),
        'turn off the stove': ('flat_stove_1', None),
        'put the frying pan on the cabinet shelf': ('chefmate_8_frypan_1', 'wooden_two_layer_shelf_1'),
        'put the frying pan on top of the cabinet': ('chefmate_8_frypan_1', 'wooden_two_layer_shelf_1_top_side'),
        'put the frying pan under the cabinet shelf': ('chefmate_8_frypan_1', 'wooden_two_layer_shelf_1'),
        'put the white bowl on top of the cabinet': ('white_bowl_1', 'wooden_two_layer_shelf_1_top_side'),
        'pick up the alphabet soup and put it in the basket': ('alphabet_soup_1', 'basket_1_contain'),
        'pick up the cream cheese box and put it in the basket': ('cream_cheese_1', 'basket_1_contain'),
        'pick up the ketchup and put it in the basket': ('ketchup_1', 'basket_1_contain'),
        'pick up the tomato sauce and put it in the basket': ('tomato_sauce_1', 'basket_1_contain'),
        'pick up the butter and put it in the basket': ('butter_1', 'basket_1_contain'),
        'pick up the milk and put it in the basket': ('milk_1', 'basket_1_contain'),
        'pick up the orange juice and put it in the basket': ('orange_juice_1', 'basket_1_contain'),
        'pick up the alphabet soup and put it in the tray': ('alphabet_soup_1', 'wooden_tray_1_contain'),
        'pick up the butter and put it in the tray': ('butter_1', 'wooden_tray_1_contain'),
        'pick up the cream cheese and put it in the tray': ('cream_cheese_1', 'wooden_tray_1_contain'),
        'pick up the ketchup and put it in the tray': ('ketchup_1', 'wooden_tray_1_contain'),
        'pick up the tomato sauce and put it in the tray': ('tomato_sauce_1', 'wooden_tray_1_contain'),
        'pick up the black bowl on the left and put it in the tray': ('akita_black_bowl_1', 'wooden_tray_1_contain'),
        'pick up the chocolate pudding and put it in the tray': ('chocolate_pudding_1', 'wooden_tray_1_contain'),
        'pick up the salad dressing and put it in the tray': ('new_salad_dressing_1', 'wooden_tray_1_contain'),
        'stack the left bowl on the right bowl and place them in the tray': ('akita_black_bowl_1', 'akita_black_bowl_2'),
        'stack the right bowl on the left bowl and place them in the tray': ('akita_black_bowl_2', 'akita_black_bowl_1'),
        'put the red mug on the left plate': ('red_coffee_mug_1', 'plate_1'),
        'put the red mug on the right plate': ('red_coffee_mug_1', 'plate_2'),
        'put the white mug on the left plate': ('porcelain_mug_1', 'plate_1'),
        'put the yellow and white mug on the right plate': ('white_yellow_mug_1', 'plate_2'),
        'put the chocolate pudding to the left of the plate': ('chocolate_pudding_1', 'living_room_table_plate_left'),
        'put the chocolate pudding to the right of the plate': ('chocolate_pudding_1', 'living_room_table_plate_right'),
        'put the red mug on the plate': ('red_coffee_mug_1', 'plate_1'),
        'put the white mug on the plate': ('porcelain_mug_1', 'plate_1'),
        'pick up the book and place it in the back compartment of the caddy': ('black_book_1', 'desk_caddy_1'),
        'pick up the book and place it in the front compartment of the caddy': ('black_book_1', 'desk_caddy_1'),
        'pick up the book and place it in the left compartment of the caddy': ('black_book_1', 'desk_caddy_1'),
        'pick up the book and place it in the right compartment of the caddy': ('black_book_1', 'desk_caddy_1'),
        'pick up the yellow and white mug and place it to the right of the caddy': ('white_yellow_mug_1', 'study_table_desk_caddy_right'),
        'pick up the red mug and place it to the right compartment of the caddy': ('red_coffee_mug_1', 'study_table_desk_caddy_right'),
        'pick up the white mug and place it to the right compartment of the caddy': ('porcelain_mug_1', 'study_table_desk_caddy_right'),
        'pick up the book in the middle and place it on the cabinet shelf': ('black_book_1', 'wooden_two_layer_shelf_1'),
        'pick up the book on the left and place it on top of the shelf': ('yellow_book_2', 'wooden_two_layer_shelf_1_top_side'),
        'pick up the book on the right and place it on the cabinet shelf': ('yellow_book_1', 'wooden_two_layer_shelf_1'),
        'pick up the book on the right and place it under the cabinet shelf': ('yellow_book_1', 'wooden_two_layer_shelf_1'),
        'Open the middle layer of the drawer': ('wooden_cabinet_1_middle_region', None),
        'Open the top layer of the drawer and put the bowl inside': ('akita_black_bowl_1', 'wooden_cabinet_1'),
        'Push the plate to the front of the stove': ('plate_1', 'main_table_stove_front'),
        'Put the bowl on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Put the bowl on the stove': ('akita_black_bowl_1', 'flat_stove_1'),
        'Put the bowl on the top of the drawer': ('akita_black_bowl_1', 'wooden_cabinet_1_top_side'),
        'Put the cream cheese on the bowl': ('cream_cheese_1', 'akita_black_bowl_1'),
        'Put the wine bottle on the rack': ('wine_bottle_1', 'wine_rack_1'),
        'Put the wine bottle on the top of the drawer': ('wine_bottle_1', 'wooden_cabinet_1_top_side'),
        'Turn on the stove': ('flat_stove_1', None),
        'Pick the alphabet soup and place it in the basket': ('alphabet_soup_1', 'basket_1_contain'),
        'Pick the bbq sauce and place it in the basket': ('bbq_sauce_1', 'basket_1_contain'),
        'Pick the butter and place it in the basket': ('butter_1', 'basket_1_contain'),
        'Pick the chocolate pudding and place it in the basket': ('chocolate_pudding_1', 'basket_1_contain'),
        'Pick the cream cheese and place it in the basket': ('cream_cheese_1', 'basket_1_contain'),
        'Pick the ketchup and place it in the basket': ('ketchup_1', 'basket_1_contain'),
        'Pick the milk and place it in the basket': ('milk_1', 'basket_1_contain'),
        'Pick the orange juice and place it in the basket': ('orange_juice_1', 'basket_1_contain'),
        'Pick the salad dressing and place it in the basket': ('salad_dressing_1', 'basket_1_contain'),
        'Pick the tomato sauce and place it in the basket': ('tomato_sauce_1', 'basket_1_contain'),
        'Pick the akita black bowl between the plate and the ramekin and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl from table center and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl in the top layer of the wooden cabinet and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl next to the cookies box and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl next to the plate and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl next to the ramekin and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl on the cookies box and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl on the ramekin and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl on the stove and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
        'Pick the akita black bowl on the wooden cabinet and place it on the plate': ('akita_black_bowl_1', 'plate_1'),
    }
    return _bddl_cache

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
                distinct_shared = set(shared)
                # Relaxed from len(distinct_shared) >= 2 to >= 1 to catch single token matches
                if len(distinct_shared) >= 1:
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
    # 1. BDDL mapping lookup
    bddl_map = get_bddl_mapping()
    norm_lang = language.strip().lower()
    
    bddl_match = None
    if norm_lang in bddl_map:
        bddl_match = bddl_map[norm_lang]
    else:
        def clean_key(s):
            return re.sub(r'[^a-z0-9]', '', s.lower())
        cleaned_lang = clean_key(norm_lang)
        for k, v in bddl_map.items():
            if clean_key(k) == cleaned_lang:
                bddl_match = v
                break

    mentioned = mentioned_bases(language, obs, all_bodies)
    relation = extract_relation(language)
    target = None
    goal = None
    confidence = "LOW"

    if bddl_match is not None:
        bddl_target, bddl_goal = bddl_match
        target = select_base_for_phrase(bddl_target, mentioned, obs, language_for_between=language)
        goal = select_base_for_phrase(bddl_goal, mentioned, obs, exclude={target} if target else set())
        
        if target is None and bddl_target:
            target = select_base_for_phrase(bddl_target.replace("_1", "").replace("_2", "").replace("_3", ""), mentioned, obs)
        if goal is None and bddl_goal:
            goal = select_base_for_phrase(bddl_goal.replace("_1", "").replace("_2", "").replace("_3", ""), mentioned, obs, exclude={target} if target else set())
        
        if target:
            confidence = "HIGH"
        else:
            confidence = "LOW"
    else:
        # Template fallback
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
            
        if target:
            confidence = "HIGH" if relation == "place_or_put" and goal else "MEDIUM"
        else:
            confidence = "LOW"

    return {
        "task_language": language,
        "relation": relation,
        "mentioned_bases": mentioned,
        "target_base": target,
        "goal_base": goal,
        "target_body_prefix": base_to_body_prefix(target) if target else None,
        "goal_body_prefix": base_to_body_prefix(goal) if goal else None,
        "parse_confidence": confidence,
        "parser_version": "stage9_task_parser_v3_bddl_priority",
        "parsed_target_phrase": extract_pick_target_phrase(language),
        "parsed_goal_phrase": extract_goal_phrase(language),
    }
