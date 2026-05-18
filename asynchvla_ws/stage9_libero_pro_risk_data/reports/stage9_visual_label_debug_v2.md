# Stage 9 Visual Label Debug v2

Generated: `2026-05-18T10:57:21`

Image folder: `asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3`

Label counts: `{'GOOD': 64, 'AMBIGUOUS': 32}`

GOOD and AMBIGUOUS before/after examples were saved. BAD examples were not available in this real SimVLA pilot because no clear bad events occurred.

```json
[
  {
    "sample_id": "libero_object_with_mug_t0_s0_b84af382_state_seed0",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s0_b84af382_state_seed0_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s0_b84af382_state_seed0_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06922679081097259,
      "object_delta_max": 4.731606503792706e-09,
      "height_drop_max": 3.843945273196425e-09,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 2.80503024341269e-12,
      "target_height_delta": 2.797054254877196e-12,
      "target_height_drop": -2.797054254877196e-12,
      "target_to_goal_delta": 3.7703173916270316e-13,
      "target_to_eef_before": 0.3286884145129901,
      "target_to_eef_delta": -0.04839146630186031
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s0_b84af382_state_seed1",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s0_b84af382_state_seed1_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s0_b84af382_state_seed1_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06612873567857167,
      "object_delta_max": 4.730273408740927e-09,
      "height_drop_max": 3.842857122793308e-09,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 2.80503024341269e-12,
      "target_height_delta": 2.797054254877196e-12,
      "target_height_drop": -2.797054254877196e-12,
      "target_to_goal_delta": 3.7703173916270316e-13,
      "target_to_eef_before": 0.3286884145129901,
      "target_to_eef_delta": -0.046663487416378435
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s0_b84af382_state_seed2",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s0_b84af382_state_seed2_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s0_b84af382_state_seed2_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06829821410944649,
      "object_delta_max": 4.7313291750851555e-09,
      "height_drop_max": 3.8437188709661285e-09,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 2.80503024341269e-12,
      "target_height_delta": 2.797054254877196e-12,
      "target_height_drop": -2.797054254877196e-12,
      "target_to_goal_delta": 3.7703173916270316e-13,
      "target_to_eef_before": 0.3286884145129901,
      "target_to_eef_delta": -0.04648781277540598
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s0_b84af382_state_seed3",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s0_b84af382_state_seed3_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s0_b84af382_state_seed3_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06839839609061503,
      "object_delta_max": 4.734103869855566e-09,
      "height_drop_max": 3.845983809203091e-09,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 2.80503024341269e-12,
      "target_height_delta": 2.797054254877196e-12,
      "target_height_drop": -2.797054254877196e-12,
      "target_to_goal_delta": 3.7703173916270316e-13,
      "target_to_eef_before": 0.3286884145129901,
      "target_to_eef_delta": -0.04758819063597586
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s1_3c5e268f_state_seed0",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s1_3c5e268f_state_seed0_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s1_3c5e268f_state_seed0_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06870215507739369,
      "object_delta_max": 7.164559246176704e-10,
      "height_drop_max": 0.0,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 1.2264404131252434e-13,
      "target_height_delta": 1.2228412726855709e-13,
      "target_height_drop": -1.2228412726855709e-13,
      "target_to_goal_delta": 1.6764367671839864e-14,
      "target_to_eef_before": 0.32793691854353824,
      "target_to_eef_delta": -0.047947368285432446
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s1_3c5e268f_state_seed1",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s1_3c5e268f_state_seed1_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s1_3c5e268f_state_seed1_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06539130508406188,
      "object_delta_max": 7.177937362144177e-10,
      "height_drop_max": 0.0,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 1.2264404131252434e-13,
      "target_height_delta": 1.2228412726855709e-13,
      "target_height_drop": -1.2228412726855709e-13,
      "target_to_goal_delta": 1.6764367671839864e-14,
      "target_to_eef_before": 0.32793691854353824,
      "target_to_eef_delta": -0.04614694408536074
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s1_3c5e268f_state_seed2",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s1_3c5e268f_state_seed2_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s1_3c5e268f_state_seed2_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06666493546164659,
      "object_delta_max": 7.189445806107623e-10,
      "height_drop_max": 0.0,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 1.2264404131252434e-13,
      "target_height_delta": 1.2228412726855709e-13,
      "target_height_drop": -1.2228412726855709e-13,
      "target_to_goal_delta": 1.6764367671839864e-14,
      "target_to_eef_before": 0.32793691854353824,
      "target_to_eef_delta": -0.04542688336557016
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s1_3c5e268f_state_seed3",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s1_3c5e268f_state_seed3_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s1_3c5e268f_state_seed3_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06764340732707701,
      "object_delta_max": 7.155791594223046e-10,
      "height_drop_max": 0.0,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 1.2264404131252434e-13,
      "target_height_delta": 1.2228412726855709e-13,
      "target_height_drop": -1.2228412726855709e-13,
      "target_to_goal_delta": 1.6764367671839864e-14,
      "target_to_eef_before": 0.32793691854353824,
      "target_to_eef_delta": -0.046922630556319456
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s2_4cecf05b_state_seed0",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s2_4cecf05b_state_seed0_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s2_4cecf05b_state_seed0_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.07411328724762448,
      "object_delta_max": 6.054314211348945e-10,
      "height_drop_max": 2.108329380219945e-15,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 5.3342947154799975e-15,
      "target_height_delta": 5.322131624296844e-15,
      "target_height_drop": -5.322131624296844e-15,
      "target_to_goal_delta": 6.661338147750939e-16,
      "target_to_eef_before": 0.32601713414163724,
      "target_to_eef_delta": -0.050329136301975
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s2_4cecf05b_state_seed1",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s2_4cecf05b_state_seed1_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s2_4cecf05b_state_seed1_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.07195476146756871,
      "object_delta_max": 6.032549601680547e-10,
      "height_drop_max": 2.1082074074755403e-15,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 5.3342947154799975e-15,
      "target_height_delta": 5.322131624296844e-15,
      "target_height_drop": -5.322131624296844e-15,
      "target_to_goal_delta": 6.661338147750939e-16,
      "target_to_eef_before": 0.32601713414163724,
      "target_to_eef_delta": -0.04924492298690697
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s2_4cecf05b_state_seed2",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s2_4cecf05b_state_seed2_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s2_4cecf05b_state_seed2_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.07313281294236805,
      "object_delta_max": 6.078840252257954e-10,
      "height_drop_max": 2.1084344123054044e-15,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 5.3342947154799975e-15,
      "target_height_delta": 5.322131624296844e-15,
      "target_height_drop": -5.322131624296844e-15,
      "target_to_goal_delta": 6.661338147750939e-16,
      "target_to_eef_before": 0.32601713414163724,
      "target_to_eef_delta": -0.04840677527874182
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s2_4cecf05b_state_seed3",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s2_4cecf05b_state_seed3_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s2_4cecf05b_state_seed3_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.07369478870490383,
      "object_delta_max": 6.118513144519886e-10,
      "height_drop_max": 2.1086207595538004e-15,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 5.3342947154799975e-15,
      "target_height_delta": 5.322131624296844e-15,
      "target_height_drop": -5.322131624296844e-15,
      "target_to_goal_delta": 6.661338147750939e-16,
      "target_to_eef_before": 0.32601713414163724,
      "target_to_eef_delta": -0.0494735291237563
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s3_ba22087a_state_seed0",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s3_ba22087a_state_seed0_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s3_ba22087a_state_seed0_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.08872483409324382,
      "object_delta_max": 2.4687630778018065e-09,
      "height_drop_max": 2.024049400306538e-09,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 2.0816681711721685e-16,
      "target_height_delta": 2.0816681711721685e-16,
      "target_height_drop": -2.0816681711721685e-16,
      "target_to_goal_delta": 0.0,
      "target_to_eef_before": 0.3231868898550647,
      "target_to_eef_delta": -0.0565756255673146
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s3_ba22087a_state_seed1",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s3_ba22087a_state_seed1_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s3_ba22087a_state_seed1_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.08714791323095572,
      "object_delta_max": 2.469390689174721e-09,
      "height_drop_max": 2.024561567004479e-09,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 2.0816681711721685e-16,
      "target_height_delta": 2.0816681711721685e-16,
      "target_height_drop": -2.0816681711721685e-16,
      "target_to_goal_delta": 0.0,
      "target_to_eef_before": 0.3231868898550647,
      "target_to_eef_delta": -0.05610942713974232
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s3_ba22087a_state_seed2",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s3_ba22087a_state_seed2_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s3_ba22087a_state_seed2_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.08785477570950827,
      "object_delta_max": 2.4671731084375037e-09,
      "height_drop_max": 2.0227520283744305e-09,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 2.0816681711721685e-16,
      "target_height_delta": 2.0816681711721685e-16,
      "target_height_drop": -2.0816681711721685e-16,
      "target_to_goal_delta": 0.0,
      "target_to_eef_before": 0.3231868898550647,
      "target_to_eef_delta": -0.054768588198372326
    }
  },
  {
    "sample_id": "libero_object_with_mug_t0_s3_ba22087a_state_seed3",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s3_ba22087a_state_seed3_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t0_s3_ba22087a_state_seed3_GOOD_after.png",
    "task": "pick the alphabet soup and place it in the basket",
    "task_context": {
      "task_language": "pick the alphabet soup and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "alphabet_soup_1",
        "basket_1"
      ],
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "target_body_prefix": "alphabet_soup_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.088430079482732,
      "object_delta_max": 2.4713099334587967e-09,
      "height_drop_max": 2.0261275712751825e-09,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 2.0816681711721685e-16,
      "target_height_delta": 2.0816681711721685e-16,
      "target_height_drop": -2.0816681711721685e-16,
      "target_to_goal_delta": 0.0,
      "target_to_eef_before": 0.3231868898550647,
      "target_to_eef_delta": -0.05590486040795012
    }
  },
  {
    "sample_id": "libero_object_with_mug_t1_s0_1617338d_state_seed0",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t1_s0_1617338d_state_seed0_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t1_s0_1617338d_state_seed0_GOOD_after.png",
    "task": "pick the bbq sauce and place it in the basket",
    "task_context": {
      "task_language": "pick the bbq sauce and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "bbq_sauce_1",
        "basket_1"
      ],
      "target_base": "bbq_sauce_1",
      "goal_base": "basket_1",
      "target_body_prefix": "bbq_sauce_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06096627831425135,
      "object_delta_max": 4.720998051607893e-09,
      "height_drop_max": 3.8364594903694815e-09,
      "target_base": "bbq_sauce_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 4.296563105299356e-13,
      "target_height_delta": 4.296563105299356e-13,
      "target_height_drop": -4.296563105299356e-13,
      "target_to_goal_delta": 6.272760089132134e-14,
      "target_to_eef_before": 0.3060355802924927,
      "target_to_eef_delta": -0.04665912454696641
    }
  },
  {
    "sample_id": "libero_object_with_mug_t1_s0_1617338d_state_seed1",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t1_s0_1617338d_state_seed1_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t1_s0_1617338d_state_seed1_GOOD_after.png",
    "task": "pick the bbq sauce and place it in the basket",
    "task_context": {
      "task_language": "pick the bbq sauce and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "bbq_sauce_1",
        "basket_1"
      ],
      "target_base": "bbq_sauce_1",
      "goal_base": "basket_1",
      "target_body_prefix": "bbq_sauce_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.059282561531123025,
      "object_delta_max": 4.720922368638848e-09,
      "height_drop_max": 3.836397727274843e-09,
      "target_base": "bbq_sauce_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 4.296563105299356e-13,
      "target_height_delta": 4.296563105299356e-13,
      "target_height_drop": -4.296563105299356e-13,
      "target_to_goal_delta": 6.272760089132134e-14,
      "target_to_eef_before": 0.3060355802924927,
      "target_to_eef_delta": -0.04535999747567648
    }
  },
  {
    "sample_id": "libero_object_with_mug_t1_s0_1617338d_state_seed2",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t1_s0_1617338d_state_seed2_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t1_s0_1617338d_state_seed2_GOOD_after.png",
    "task": "pick the bbq sauce and place it in the basket",
    "task_context": {
      "task_language": "pick the bbq sauce and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "bbq_sauce_1",
        "basket_1"
      ],
      "target_base": "bbq_sauce_1",
      "goal_base": "basket_1",
      "target_body_prefix": "bbq_sauce_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.06174460126913178,
      "object_delta_max": 4.7171981986555664e-09,
      "height_drop_max": 3.83335790193895e-09,
      "target_base": "bbq_sauce_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 4.296563105299356e-13,
      "target_height_delta": 4.296563105299356e-13,
      "target_height_drop": -4.296563105299356e-13,
      "target_to_goal_delta": 6.272760089132134e-14,
      "target_to_eef_before": 0.3060355802924927,
      "target_to_eef_delta": -0.04671812023588967
    }
  },
  {
    "sample_id": "libero_object_with_mug_t1_s0_1617338d_state_seed3",
    "label": "GOOD",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t1_s0_1617338d_state_seed3_GOOD_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_object_with_mug_t1_s0_1617338d_state_seed3_GOOD_after.png",
    "task": "pick the bbq sauce and place it in the basket",
    "task_context": {
      "task_language": "pick the bbq sauce and place it in the basket",
      "relation": "place_or_put",
      "mentioned_bases": [
        "bbq_sauce_1",
        "basket_1"
      ],
      "target_base": "bbq_sauce_1",
      "goal_base": "basket_1",
      "target_body_prefix": "bbq_sauce_1",
      "goal_body_prefix": "basket_1",
      "parse_confidence": "MEDIUM"
    },
    "reason": [
      "eef_closer_to_target_before_grasp"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.059026237329445744,
      "object_delta_max": 4.720967244179965e-09,
      "height_drop_max": 3.836434378512443e-09,
      "target_base": "bbq_sauce_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "phase": "approach",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 4.296563105299356e-13,
      "target_height_delta": 4.296563105299356e-13,
      "target_height_drop": -4.296563105299356e-13,
      "target_to_goal_delta": 6.272760089132134e-14,
      "target_to_eef_before": 0.3060355802924927,
      "target_to_eef_delta": -0.04542483750761861
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s0_a561d84f_state_seed0",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s0_a561d84f_state_seed0_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s0_a561d84f_state_seed0_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.04630724782700451,
      "object_delta_max": 9.969620416334102e-08,
      "height_drop_max": 4.403792475127233e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s0_a561d84f_state_seed1",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s0_a561d84f_state_seed1_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s0_a561d84f_state_seed1_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.04534140905067141,
      "object_delta_max": 9.969620414161788e-08,
      "height_drop_max": 4.403792475127233e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s0_a561d84f_state_seed2",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s0_a561d84f_state_seed2_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s0_a561d84f_state_seed2_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.04803657586762904,
      "object_delta_max": 9.969620414161788e-08,
      "height_drop_max": 4.403792475127233e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s0_a561d84f_state_seed3",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s0_a561d84f_state_seed3_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s0_a561d84f_state_seed3_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.04736986062327416,
      "object_delta_max": 9.969620411727336e-08,
      "height_drop_max": 4.403792475127233e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s1_1980f010_state_seed0",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s1_1980f010_state_seed0_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s1_1980f010_state_seed0_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.05728405681595075,
      "object_delta_max": 1.1505456791629418e-07,
      "height_drop_max": 8.482624647143666e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s1_1980f010_state_seed1",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s1_1980f010_state_seed1_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s1_1980f010_state_seed1_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.05665319149298104,
      "object_delta_max": 1.1505456794625888e-07,
      "height_drop_max": 8.482624647143666e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s1_1980f010_state_seed2",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s1_1980f010_state_seed2_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s1_1980f010_state_seed2_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.05916174288599292,
      "object_delta_max": 1.1505456790481626e-07,
      "height_drop_max": 8.482624647143666e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s1_1980f010_state_seed3",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s1_1980f010_state_seed3_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s1_1980f010_state_seed3_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.05865071064333236,
      "object_delta_max": 1.1505456790481626e-07,
      "height_drop_max": 8.482624647143666e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s2_50dec676_state_seed0",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s2_50dec676_state_seed0_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s2_50dec676_state_seed0_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.052319883760991094,
      "object_delta_max": 1.394134079905876e-07,
      "height_drop_max": 9.38903943481506e-09,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s2_50dec676_state_seed1",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s2_50dec676_state_seed1_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s2_50dec676_state_seed1_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.05159702185066068,
      "object_delta_max": 1.394134080024443e-07,
      "height_drop_max": 9.38903943481506e-09,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s2_50dec676_state_seed2",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s2_50dec676_state_seed2_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s2_50dec676_state_seed2_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.05379509817236753,
      "object_delta_max": 1.394134080024443e-07,
      "height_drop_max": 9.38903943481506e-09,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s2_50dec676_state_seed3",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s2_50dec676_state_seed3_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s2_50dec676_state_seed3_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.053595843723377445,
      "object_delta_max": 1.394134080024443e-07,
      "height_drop_max": 9.38903943481506e-09,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s3_a097187e_state_seed0",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s3_a097187e_state_seed0_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s3_a097187e_state_seed0_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.07128093312192903,
      "object_delta_max": 6.405177628919022e-08,
      "height_drop_max": 2.1759278268085325e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s3_a097187e_state_seed1",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s3_a097187e_state_seed1_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s3_a097187e_state_seed1_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.0704519586324668,
      "object_delta_max": 6.40517763145857e-08,
      "height_drop_max": 2.1759278268085325e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s3_a097187e_state_seed2",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s3_a097187e_state_seed2_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s3_a097187e_state_seed2_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.07314740958104203,
      "object_delta_max": 6.40517763145857e-08,
      "height_drop_max": 2.1759278268085325e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t0_s3_a097187e_state_seed3",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s3_a097187e_state_seed3_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t0_s3_a097187e_state_seed3_AMBIGUOUS_after.png",
    "task": "open the middle drawer of the cabinet",
    "task_context": {
      "task_language": "open the middle drawer of the cabinet",
      "relation": "articulation_or_toggle",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.07236979081618097,
      "object_delta_max": 6.405177623270555e-08,
      "height_drop_max": 2.1759278268085325e-08,
      "target_base": null,
      "goal_base": null,
      "task_relation": "articulation_or_toggle",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t1_s0_61adebd2_state_seed0",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t1_s0_61adebd2_state_seed0_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t1_s0_61adebd2_state_seed0_AMBIGUOUS_after.png",
    "task": "put the bowl on the stove",
    "task_context": {
      "task_language": "put the bowl on the stove",
      "relation": "place_or_put",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.08341651094478189,
      "object_delta_max": 8.216175370917725e-08,
      "height_drop_max": 0.0,
      "target_base": null,
      "goal_base": null,
      "task_relation": "place_or_put",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t1_s0_61adebd2_state_seed1",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t1_s0_61adebd2_state_seed1_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t1_s0_61adebd2_state_seed1_AMBIGUOUS_after.png",
    "task": "put the bowl on the stove",
    "task_context": {
      "task_language": "put the bowl on the stove",
      "relation": "place_or_put",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.0839174245161052,
      "object_delta_max": 8.216175369475859e-08,
      "height_drop_max": 0.0,
      "target_base": null,
      "goal_base": null,
      "task_relation": "place_or_put",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t1_s0_61adebd2_state_seed2",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t1_s0_61adebd2_state_seed2_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t1_s0_61adebd2_state_seed2_AMBIGUOUS_after.png",
    "task": "put the bowl on the stove",
    "task_context": {
      "task_language": "put the bowl on the stove",
      "relation": "place_or_put",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.08392313838300591,
      "object_delta_max": 8.216175367992896e-08,
      "height_drop_max": 0.0,
      "target_base": null,
      "goal_base": null,
      "task_relation": "place_or_put",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  },
  {
    "sample_id": "libero_goal_with_mug_t1_s0_61adebd2_state_seed3",
    "label": "AMBIGUOUS",
    "before_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t1_s0_61adebd2_state_seed3_AMBIGUOUS_before.png",
    "after_image": "asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3/libero_goal_with_mug_t1_s0_61adebd2_state_seed3_AMBIGUOUS_after.png",
    "task": "put the bowl on the stove",
    "task_context": {
      "task_language": "put the bowl on the stove",
      "relation": "place_or_put",
      "mentioned_bases": [],
      "target_base": null,
      "goal_base": null,
      "target_body_prefix": null,
      "goal_body_prefix": null,
      "parse_confidence": "LOW"
    },
    "reason": [
      "target_object_unknown_or_position_missing"
    ],
    "evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.08241083073161089,
      "object_delta_max": 8.216175370196791e-08,
      "height_drop_max": 0.0,
      "target_base": null,
      "goal_base": null,
      "task_relation": "place_or_put",
      "parse_confidence": "LOW",
      "phase": "approach",
      "target_pos_available": false,
      "goal_pos_available": false,
      "target_motion": null,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": null,
      "target_to_eef_before": null,
      "target_to_eef_delta": null
    }
  }
]
```
