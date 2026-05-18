# Stage 6 Experiments: id_task_split

```json
{
  "split": "id_task_split",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 41,
      "best_calib_loss": 0.08417635411024094,
      "train_time_sec": 18.657267332077026,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8864956866550702,
            "spearman": 0.8165908324978959,
            "auroc_top30_bad": 0.8869046904761905,
            "mae": 0.20833337292969226,
            "mse": 0.2338945184826655,
            "expert_lt_perturb_large": 0.972,
            "expert_lt_other_task": 0.499,
            "expert_lt_simvla_seed0": 0.953,
            "same_context_pred_std": 0.7986717734553678,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5459223752096295
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5461367380052805
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6903458061292768
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0052490525315205
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9977647272237471,
            "spearman": 0.9961288789007833,
            "auroc_top30_worst": 0.9981397142857144,
            "pairwise_seed_ranking": 0.81,
            "predicted_best_mean_error": 1.6362513569295407,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.07019899317622169,
            "gap_to_oracle": 0.013104836016893495,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5259475241899491
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7341034357070922
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0135276437044143
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.251014784415563
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1481579542160043,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4533566133843527,
                "rejected_mean_error": 3.913212927341461,
                "gap_rejected_minus_accepted": 2.4598563139571086
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0057345628738403,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.251014784415563,
                "rejected_mean_error": 3.044324625873566,
                "gap_rejected_minus_accepted": 1.7933098414580029
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.473471760749817,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0135276437044143,
                "rejected_mean_error": 2.385156845855713,
                "gap_rejected_minus_accepted": 1.3716292021512986
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0525514483451843,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7341034357070922,
                "rejected_mean_error": 2.021088514471054,
                "gap_rejected_minus_accepted": 1.2869850787639616
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1227967977523803,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4561398416757583,
                "rejected_mean_error": 3.9592449259757996,
                "gap_rejected_minus_accepted": 2.5031050843000413
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.006988763809204,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2503580593268075,
                "rejected_mean_error": 3.0747272224426268,
                "gap_rejected_minus_accepted": 1.8243691631158192
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4774478077888489,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0093048959970474,
                "rejected_mean_error": 2.4035958042144774,
                "gap_rejected_minus_accepted": 1.39429090821743
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0523589849472046,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7234871623516083,
                "rejected_mean_error": 2.034104746023814,
                "gap_rejected_minus_accepted": 1.3106175836722058
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6913963579296573,
            "spearman": 0.6579155267818543,
            "auroc_top30_bad": 0.7936049523809524,
            "mae": 0.43552118628025055,
            "mse": 0.4522322285683793,
            "expert_lt_perturb_large": 0.948,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.96,
            "same_context_pred_std": 0.6802504190804967,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.688999910891056
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.723732202219963
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8242196280121803
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1395950271050135
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.8031286720734732,
            "spearman": 0.8036097774142577,
            "auroc_top30_worst": 0.883056761904762,
            "pairwise_seed_ranking": 0.7316,
            "predicted_best_mean_error": 1.66998728120327,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.05800833857059495,
            "gap_to_oracle": 0.02091502666473377,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6825502851009368
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9912960320138015
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2616245610713959
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.503082955410994
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3383621931076064,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6133788447115156,
                "rejected_mean_error": 2.756230779647827,
                "gap_rejected_minus_accepted": 1.1428519349363115
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.905492752790451,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.502522441690734,
                "rejected_mean_error": 2.4016502232978136,
                "gap_rejected_minus_accepted": 0.8991277816070797
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6136221289634705,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2616245610713959,
                "rejected_mean_error": 2.1937035153388975,
                "gap_rejected_minus_accepted": 0.9320789542675016
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2743529081344604,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9931251870367093,
                "rejected_mean_error": 1.973032939395884,
                "gap_rejected_minus_accepted": 0.9799077523591748
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.415853929519653,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6106649282243517,
                "rejected_mean_error": 2.7839718437194825,
                "gap_rejected_minus_accepted": 1.1733069154951308
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9334197044372559,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5054487850576799,
                "rejected_mean_error": 2.3885711450425404,
                "gap_rejected_minus_accepted": 0.8831223599848605
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6239147782325745,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.247851448059082,
                "rejected_mean_error": 2.2081397914886476,
                "gap_rejected_minus_accepted": 0.9602883434295655
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3049658238887787,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.977712853560372,
                "rejected_mean_error": 1.9807646800489986,
                "gap_rejected_minus_accepted": 1.0030518264886266
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6039268166304487,
            "spearman": 0.5325931178498188,
            "auroc_top30_bad": 0.7116933333333333,
            "mae": 0.5237702184259891,
            "mse": 0.5750083757867224,
            "expert_lt_perturb_large": 0.944,
            "expert_lt_other_task": 0.508,
            "expert_lt_simvla_seed0": 0.908,
            "same_context_pred_std": 0.7051226745303434,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5699083508849144
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7926711813211441
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.870268076312542
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0177683277050653
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.7529162230612612,
            "spearman": 0.6640634429846036,
            "auroc_top30_worst": 0.8681752380952381,
            "pairwise_seed_ranking": 0.7132,
            "predicted_best_mean_error": 1.4314282431602479,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.05063096559047686,
            "gap_to_oracle": 0.02997172689437866,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8303254890441895
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9866777176085191
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0594472818374634
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1751094355956833
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7099576234817513,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2864290573596955,
                "rejected_mean_error": 3.131129439353943,
                "gap_rejected_minus_accepted": 1.8447003819942476
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.106701135635376,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1744354550777403,
                "rejected_mean_error": 2.3583956806423565,
                "gap_rejected_minus_accepted": 1.1839602255646162
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.640610933303833,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0594472818374634,
                "rejected_mean_error": 1.882350909280777,
                "gap_rejected_minus_accepted": 0.8229036274433137
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0705654919147491,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9864251982099332,
                "rejected_mean_error": 1.6327350932862232,
                "gap_rejected_minus_accepted": 0.64630989507629
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7270670413970945,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3027702319622039,
                "rejected_mean_error": 3.095659999847412,
                "gap_rejected_minus_accepted": 1.792889767885208
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1418884992599487,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.17989450581571,
                "rejected_mean_error": 2.378960787303864,
                "gap_rejected_minus_accepted": 1.199066281488154
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6890850067138672,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0615847194194794,
                "rejected_mean_error": 1.9025336980819703,
                "gap_rejected_minus_accepted": 0.8409489786624909
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.091513603925705,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.007298312016896,
                "rejected_mean_error": 1.6420053932118543,
                "gap_rejected_minus_accepted": 0.6347070811949584
              }
            ]
          }
        }
      }
    },
    {
      "variant": "full_old_baseline",
      "feature_mode": "A2_full_old",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1038,
      "best_epoch": 120,
      "best_calib_loss": 0.042510904371738434,
      "train_time_sec": 21.379923582077026,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9987942163807344,
            "spearman": 0.9974314909760111,
            "auroc_top30_bad": 0.9993173333333334,
            "mae": 0.035243360929656777,
            "mse": 0.00245904497301494,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7990720043865766,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03354135467112064
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18672431243360044
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5935820699080825
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9738211875667174
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9996418529690443,
            "spearman": 0.9992650756905501,
            "auroc_top30_worst": 0.9996651428571429,
            "pairwise_seed_ranking": 0.9333,
            "predicted_best_mean_error": 1.6250181298255921,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08143222028017028,
            "gap_to_oracle": 0.001871608912944911,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5164561076164246
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7319818779468537
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.011127080988884
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.250347170972824
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1092359542846686,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.453075705435541,
                "rejected_mean_error": 3.9157410988807677,
                "gap_rejected_minus_accepted": 2.462665393445227
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.983218401670456,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.250347170972824,
                "rejected_mean_error": 3.0463274662017823,
                "gap_rejected_minus_accepted": 1.7959802952289583
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4956150650978088,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.011127080988884,
                "rejected_mean_error": 2.387557408571243,
                "gap_rejected_minus_accepted": 1.3764303275823593
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.056570142507553,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7319818779468537,
                "rejected_mean_error": 2.0217957003911335,
                "gap_rejected_minus_accepted": 1.28981382244428
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.17131245136261,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455667041738828,
                "rejected_mean_error": 3.9635001254081725,
                "gap_rejected_minus_accepted": 2.5078330836693445
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9785126745700836,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2495326604048411,
                "rejected_mean_error": 3.0772034192085265,
                "gap_rejected_minus_accepted": 1.8276707588036853
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.496329665184021,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.007960973381996,
                "rejected_mean_error": 2.4049397268295287,
                "gap_rejected_minus_accepted": 1.3969787534475326
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.06271231174469,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7211291491985321,
                "rejected_mean_error": 2.034890750408173,
                "gap_rejected_minus_accepted": 1.3137616012096407
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9177402824060901,
            "spearman": 0.9170946184709977,
            "auroc_top30_bad": 0.9472175238095238,
            "mae": 0.26217449852079155,
            "mse": 0.1448049314155942,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.9,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6117151608389964,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11802101087570191
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.31204749324321746
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6794888358235359
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0441502918799719
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9396837418940711,
            "spearman": 0.9271253733922391,
            "auroc_top30_worst": 0.9804860952380953,
            "pairwise_seed_ranking": 0.8392,
            "predicted_best_mean_error": 1.6613571592569352,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.06663846051692968,
            "gap_to_oracle": 0.012284904718399048,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6755638020038605
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9181356589572552
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2068010723590852
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4214645901532061
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6590737104415902,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5906315664980146,
                "rejected_mean_error": 2.960956283569336,
                "gap_rejected_minus_accepted": 1.3703247170713213
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.309371054172516,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4210829270751142,
                "rejected_mean_error": 2.6454483868595893,
                "gap_rejected_minus_accepted": 1.224365459784475
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8230579495429993,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2068010723590852,
                "rejected_mean_error": 2.2485270040512084,
                "gap_rejected_minus_accepted": 1.0417259316921232
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4193598926067352,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9194265184120629,
                "rejected_mean_error": 1.997651598178717,
                "gap_rejected_minus_accepted": 1.0782250797666542
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6521374702453615,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5874107837677003,
                "rejected_mean_error": 2.993259143829346,
                "gap_rejected_minus_accepted": 1.4058483600616456
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.346420168876648,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4081806639299035,
                "rejected_mean_error": 2.67728763156467,
                "gap_rejected_minus_accepted": 1.2691069676347666
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8131040334701538,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.198324984550476,
                "rejected_mean_error": 2.2576662549972535,
                "gap_rejected_minus_accepted": 1.0593412704467775
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4024845361709595,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9034776640316796,
                "rejected_mean_error": 2.005774396307328,
                "gap_rejected_minus_accepted": 1.1022967322756485
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9301793553095843,
            "spearman": 0.9115501924925525,
            "auroc_top30_bad": 0.9662430476190476,
            "mae": 0.2472267526730895,
            "mse": 0.12347995070280103,
            "expert_lt_perturb_large": 0.988,
            "expert_lt_other_task": 0.948,
            "expert_lt_simvla_seed0": 0.956,
            "same_context_pred_std": 0.5884385423990957,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1245888625383377
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.290492720079422
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6311562600970269
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9085004442930221
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9546831323883126,
            "spearman": 0.8618652136097368,
            "auroc_top30_worst": 0.9888487619047619,
            "pairwise_seed_ranking": 0.796,
            "predicted_best_mean_error": 1.4173584576845168,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.06470075106620787,
            "gap_to_oracle": 0.015901941418647647,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6563316676616668
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8604710850004966
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9894716401576996
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1236024203140345
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6621870994567898,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2642221383253733,
                "rejected_mean_error": 3.330991710662842,
                "gap_rejected_minus_accepted": 2.066769572337469
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9170686900615692,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1227150882257342,
                "rejected_mean_error": 2.5132262996210457,
                "gap_rejected_minus_accepted": 1.3905112113953115
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4730320572853088,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9894716401576996,
                "rejected_mean_error": 1.9523265509605408,
                "gap_rejected_minus_accepted": 0.9628549108028411
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1698740720748901,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8612792727094107,
                "rejected_mean_error": 1.674539441932609,
                "gap_rejected_minus_accepted": 0.8132601692231982
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6899481534957883,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2739171005619896,
                "rejected_mean_error": 3.3553381824493407,
                "gap_rejected_minus_accepted": 2.081421081887351
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9385459125041962,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.129855248220464,
                "rejected_mean_error": 2.527490012229435,
                "gap_rejected_minus_accepted": 1.397634764008971
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5097821354866028,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9909551193714142,
                "rejected_mean_error": 1.9731632981300353,
                "gap_rejected_minus_accepted": 0.9822081787586211
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1695544123649597,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8655465798718589,
                "rejected_mean_error": 1.6897613243623213,
                "gap_rejected_minus_accepted": 0.8242147444904624
              }
            ]
          }
        }
      }
    },
    {
      "variant": "context_gated_action",
      "feature_mode": "M3_gated_base",
      "model_kind": "gated",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1456,
      "best_epoch": 109,
      "best_calib_loss": 0.009819942526519299,
      "train_time_sec": 51.103047370910645,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997906627995572,
            "spearman": 0.9988767616739345,
            "auroc_top30_bad": 0.9996991904761904,
            "mae": 0.022661085142730734,
            "mse": 0.0008427265777376812,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8152087036088229,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00011665445566177368
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1861272808998823
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5934539686068893
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9736255870252848
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998076842169592,
            "spearman": 0.9995813389912332,
            "auroc_top30_worst": 0.9995937142857143,
            "pairwise_seed_ranking": 0.9585,
            "predicted_best_mean_error": 1.6241244483888149,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08232590171694754,
            "gap_to_oracle": 0.0009779274761676504,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.515314950466156
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7315454797267914
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0108714109182357
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2503071954568228
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.190136790275574,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530237915383446,
                "rejected_mean_error": 3.916208323955536,
                "gap_rejected_minus_accepted": 2.4631845324171913
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.024245858192444,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2503071954568228,
                "rejected_mean_error": 3.0464473927497866,
                "gap_rejected_minus_accepted": 1.7961401972929638
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5215364694595337,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0108714109182357,
                "rejected_mean_error": 2.3878130786418916,
                "gap_rejected_minus_accepted": 1.376941667723656
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0797984898090363,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7315454797267914,
                "rejected_mean_error": 2.0219411664644875,
                "gap_rejected_minus_accepted": 1.2903956867376962
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.245657324790955,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455667041738828,
                "rejected_mean_error": 3.9635001254081725,
                "gap_rejected_minus_accepted": 2.5078330836693445
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02888423204422,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.249622970978419,
                "rejected_mean_error": 3.076932487487793,
                "gap_rejected_minus_accepted": 1.827309516509374
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5217655897140503,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0077221401929854,
                "rejected_mean_error": 2.4051785600185394,
                "gap_rejected_minus_accepted": 1.397456419825554
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0960052609443665,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7209967777729035,
                "rejected_mean_error": 2.0349348742167157,
                "gap_rejected_minus_accepted": 1.3139380964438123
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9857040682963502,
            "spearman": 0.9872830666087914,
            "auroc_top30_bad": 0.9945523809523809,
            "mae": 0.09780734302494674,
            "mse": 0.022000165089932647,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.968,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7373285538434484,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07908708733320237
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21521765117645264
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6408353058695793
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0249503218889235
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9829959469520946,
            "spearman": 0.9910571503725764,
            "auroc_top30_worst": 0.9975619047619048,
            "pairwise_seed_ranking": 0.888,
            "predicted_best_mean_error": 1.6558891489505767,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07210647082328814,
            "gap_to_oracle": 0.006816894412040586,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6533857538700104
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8621171060471963
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1528725492954255
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4112671371271361
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5841464519500734,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5959057376914554,
                "rejected_mean_error": 2.913488742828369,
                "gap_rejected_minus_accepted": 1.3175830051369137
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1771650314331055,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4104207828243362,
                "rejected_mean_error": 2.677366690894666,
                "gap_rejected_minus_accepted": 1.2669459080703298
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6376065015792847,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1528725492954255,
                "rejected_mean_error": 2.3024555271148683,
                "gap_rejected_minus_accepted": 1.1495829778194429
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1894042491912842,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8631501728162979,
                "rejected_mean_error": 2.016450420133332,
                "gap_rejected_minus_accepted": 1.1533002473170342
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6016281127929686,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5960426616668701,
                "rejected_mean_error": 2.9155722427368165,
                "gap_rejected_minus_accepted": 1.3195295810699463
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1943199038505554,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.400802769125464,
                "rejected_mean_error": 2.699187097095308,
                "gap_rejected_minus_accepted": 1.298384327969844
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6183903217315674,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.138958306312561,
                "rejected_mean_error": 2.3170329332351685,
                "gap_rejected_minus_accepted": 1.1780746269226074
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2119164764881134,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8610512150658501,
                "rejected_mean_error": 2.020067798900094,
                "gap_rejected_minus_accepted": 1.1590165838342439
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.976892462189924,
            "spearman": 0.9804776615022059,
            "auroc_top30_bad": 0.9955405714285714,
            "mae": 0.12613640097947793,
            "mse": 0.03742233136719102,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7163481388815588,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06407669746875763
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2509019254684448
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5655707435250282
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8900571706851323
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9783779927310314,
            "spearman": 0.9863231584788217,
            "auroc_top30_worst": 0.9976228571428571,
            "pairwise_seed_ranking": 0.888,
            "predicted_best_mean_error": 1.4095200901031495,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07253911864757523,
            "gap_to_oracle": 0.008063573837280291,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6298030216693878
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7794228905859666
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9394990925312042
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1157411081768047
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6395575523376484,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2639896647400326,
                "rejected_mean_error": 3.333083972930908,
                "gap_rejected_minus_accepted": 2.0690943081908753
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8935576379299164,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.11499068325459,
                "rejected_mean_error": 2.536350157314215,
                "gap_rejected_minus_accepted": 1.4213594740596251
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2985746264457703,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9394990925312042,
                "rejected_mean_error": 2.002299098587036,
                "gap_rejected_minus_accepted": 1.062800006055832
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.985562801361084,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7802451253889467,
                "rejected_mean_error": 1.701608479404653,
                "gap_rejected_minus_accepted": 0.9213633540157063
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6432484149932858,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2739171005619896,
                "rejected_mean_error": 3.3553381824493407,
                "gap_rejected_minus_accepted": 2.081421081887351
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9246705770492554,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1187037495687047,
                "rejected_mean_error": 2.560590492354499,
                "gap_rejected_minus_accepted": 1.4418867427857942
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2951550483703613,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.936716912984848,
                "rejected_mean_error": 2.0274015045166016,
                "gap_rejected_minus_accepted": 1.0906845915317536
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9700106978416443,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7774618812023647,
                "rejected_mean_error": 1.719436918031723,
                "gap_rejected_minus_accepted": 0.9419750368293583
              }
            ]
          }
        }
      }
    },
    {
      "variant": "seed_relative_rater",
      "feature_mode": "M4_seed_relative",
      "model_kind": "mlp_big",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 113,
      "best_calib_loss": 0.009734677150845528,
      "train_time_sec": 53.35411262512207,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9980814837319677,
            "spearman": 0.9965727756057303,
            "auroc_top30_bad": 0.9978241904761905,
            "mae": 0.05840970685661836,
            "mse": 0.006953922759330829,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8308014081157276,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.009497709847986698
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18702904098927975
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5938990330323577
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9751925307184458
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9979962213646218,
            "spearman": 0.9982067945201857,
            "auroc_top30_worst": 0.9992398095238095,
            "pairwise_seed_ranking": 0.9517,
            "predicted_best_mean_error": 1.624324370265007,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08212597984075543,
            "gap_to_oracle": 0.001177849352359761,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5163458689451218
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7325767183303833
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0119683804750443
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2505806689739227
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.311673688888551,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.453290761113167,
                "rejected_mean_error": 3.913805597782135,
                "gap_rejected_minus_accepted": 2.4605148366689678
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.121500611305237,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2505806689739227,
                "rejected_mean_error": 3.0456269721984865,
                "gap_rejected_minus_accepted": 1.7950463032245638
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.562330961227417,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0119683804750443,
                "rejected_mean_error": 2.386716109085083,
                "gap_rejected_minus_accepted": 1.3747477286100387
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0943315029144287,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7325767183303833,
                "rejected_mean_error": 2.0215974202632903,
                "gap_rejected_minus_accepted": 1.289020701932907
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.307530212402344,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4561032846901152,
                "rejected_mean_error": 3.9595739388465883,
                "gap_rejected_minus_accepted": 2.503470654156473
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.109695553779602,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2496538175741831,
                "rejected_mean_error": 3.0768399477005004,
                "gap_rejected_minus_accepted": 1.8271861301263173
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5586456060409546,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0083875921964645,
                "rejected_mean_error": 2.4045131080150606,
                "gap_rejected_minus_accepted": 1.3961255158185961
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1042989492416382,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7223655333518982,
                "rejected_mean_error": 2.034478622357051,
                "gap_rejected_minus_accepted": 1.3121130890051527
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9860723372601258,
            "spearman": 0.9850968239516457,
            "auroc_top30_bad": 0.9899542857142858,
            "mae": 0.10424978421800675,
            "mse": 0.021053402554383736,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7408488021958582,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07189783602952957
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20883957242965698
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6442542034029961
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.028571928334236
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9806246527547102,
            "spearman": 0.9854771291373629,
            "auroc_top30_worst": 0.992207238095238,
            "pairwise_seed_ranking": 0.8896,
            "predicted_best_mean_error": 1.6534685400724412,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07452707970142369,
            "gap_to_oracle": 0.004396285533905031,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6378711822032929
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8659763489969265
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1531783188343048
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4123513777690655
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.722785258293152,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5943711977269914,
                "rejected_mean_error": 2.927299602508545,
                "gap_rejected_minus_accepted": 1.3329284047815535
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.187197268009186,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4112295974980296,
                "rejected_mean_error": 2.6749454150184655,
                "gap_rejected_minus_accepted": 1.263715817520436
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7060012221336365,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1531783188343048,
                "rejected_mean_error": 2.3021497575759886,
                "gap_rejected_minus_accepted": 1.1489714387416838
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2021490335464478,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8668856945472022,
                "rejected_mean_error": 2.015202588434535,
                "gap_rejected_minus_accepted": 1.1483168938873325
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7617056369781494,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5937638992733425,
                "rejected_mean_error": 2.9360811042785646,
                "gap_rejected_minus_accepted": 1.3423172050052221
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.186927914619446,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4024418088841566,
                "rejected_mean_error": 2.694322010827443,
                "gap_rejected_minus_accepted": 1.2918802019432865
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.707998812198639,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1407724246978759,
                "rejected_mean_error": 2.3152188148498536,
                "gap_rejected_minus_accepted": 1.1744463901519777
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1961442530155182,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8624854939324516,
                "rejected_mean_error": 2.0195845926509186,
                "gap_rejected_minus_accepted": 1.157099098718467
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9797682189570901,
            "spearman": 0.9775075326680365,
            "auroc_top30_bad": 0.994296380952381,
            "mae": 0.12157544629018026,
            "mse": 0.03090750710907272,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6749185658563397,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04950193005800247
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24255089662075044
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5704311230301857
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8910843651533127
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9773642636171505,
            "spearman": 0.9586021192973564,
            "auroc_top30_worst": 0.9917348571428571,
            "pairwise_seed_ranking": 0.904,
            "predicted_best_mean_error": 1.4095234508514405,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07253575789928424,
            "gap_to_oracle": 0.008066934585571284,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6357866261005402
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.795631122799256
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.955591936159134
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.116480614362495
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.359001207351685,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2638040748437245,
                "rejected_mean_error": 3.3347542819976805,
                "gap_rejected_minus_accepted": 2.070950207153956
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7839987576007843,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.115769988730979,
                "rejected_mean_error": 2.5340172204727565,
                "gap_rejected_minus_accepted": 1.4182472317417774
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2727019786834717,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.955591936159134,
                "rejected_mean_error": 1.9862062549591064,
                "gap_rejected_minus_accepted": 1.0306143187999726
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9026441276073456,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7955790802884025,
                "rejected_mean_error": 1.6964862511404806,
                "gap_rejected_minus_accepted": 0.900907170852078
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3621848106384276,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.807433396577835,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1191721184049699,
                "rejected_mean_error": 2.5592002546976484,
                "gap_rejected_minus_accepted": 1.4400281362926786
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2713412046432495,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9545144898891449,
                "rejected_mean_error": 2.0096039276123046,
                "gap_rejected_minus_accepted": 1.0550894377231597
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9015567600727081,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7906262746879033,
                "rejected_mean_error": 1.715001854985793,
                "gap_rejected_minus_accepted": 0.9243755802978898
              }
            ]
          }
        }
      }
    },
    {
      "variant": "seed_relative_pairwise",
      "feature_mode": "M4_seed_relative",
      "model_kind": "mlp_big_pairwise",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 68,
      "best_calib_loss": 0.009330164641141891,
      "train_time_sec": 60.187905073165894,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994296198107706,
            "spearman": 0.9980934561507249,
            "auroc_top30_bad": 0.9989716666666666,
            "mae": 0.02689689025154248,
            "mse": 0.0012594994718668302,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8094988944828114,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0010982860699295998
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18654015619456768
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5936020424708724
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9739739938646554
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9994111106323635,
            "spearman": 0.9988566556022113,
            "auroc_top30_worst": 0.9989994285714285,
            "pairwise_seed_ranking": 0.9609,
            "predicted_best_mean_error": 1.6241316408813,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08231870922446238,
            "gap_to_oracle": 0.0009851199686528034,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.516710693359375
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7321459860324859
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.011242490696907
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2504562650203705
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1646183490753197,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530933487812678,
                "rejected_mean_error": 3.915582308769226,
                "gap_rejected_minus_accepted": 2.462488959987958
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0191916823387146,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2504562650203705,
                "rejected_mean_error": 3.046000184059143,
                "gap_rejected_minus_accepted": 1.7955439190387723
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5067734122276306,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.011242490696907,
                "rejected_mean_error": 2.38744199886322,
                "gap_rejected_minus_accepted": 1.376199508166313
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.06831294298172,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7321459860324859,
                "rejected_mean_error": 2.0217409976959226,
                "gap_rejected_minus_accepted": 1.2895950116634367
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2101752042770393,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455705801712142,
                "rejected_mean_error": 3.9631512856483457,
                "gap_rejected_minus_accepted": 2.5074454839362037
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.026887536048889,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2497307720979054,
                "rejected_mean_error": 3.0766090841293336,
                "gap_rejected_minus_accepted": 1.8268783120314283
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5112019181251526,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.007869593501091,
                "rejected_mean_error": 2.405031106710434,
                "gap_rejected_minus_accepted": 1.397161513209343
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0819616913795471,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7212628710269928,
                "rejected_mean_error": 2.0348461764653525,
                "gap_rejected_minus_accepted": 1.3135833054383597
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9881369739933777,
            "spearman": 0.9868085216203646,
            "auroc_top30_bad": 0.9930780952380953,
            "mae": 0.10202775240615508,
            "mse": 0.02026503763214997,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7309483879358012,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08850141268968582
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21057822983264923
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.640327191722393
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0260116730928421
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9910657268332148,
            "spearman": 0.9934078401330177,
            "auroc_top30_worst": 0.9970194285714287,
            "pairwise_seed_ranking": 0.904,
            "predicted_best_mean_error": 1.6523682364225387,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07562738335132613,
            "gap_to_oracle": 0.0032959818840025967,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6504744417667389
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8597742327703879
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1510036585330963
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4104447216430962
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5360071897506717,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5891419318781959,
                "rejected_mean_error": 2.974362995147705,
                "gap_rejected_minus_accepted": 1.385221063269509
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1871854662895203,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4093879097744648,
                "rejected_mean_error": 2.680458710216486,
                "gap_rejected_minus_accepted": 1.271070800442021
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6281022429466248,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1510036585330963,
                "rejected_mean_error": 2.304324417877197,
                "gap_rejected_minus_accepted": 1.1533207593441008
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.094515472650528,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.860751640396758,
                "rejected_mean_error": 2.0172516374730503,
                "gap_rejected_minus_accepted": 1.1564999970762924
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.575856280326843,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.586392814848158,
                "rejected_mean_error": 3.0024208641052246,
                "gap_rejected_minus_accepted": 1.4160280492570665
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2185129523277283,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4011279376432857,
                "rejected_mean_error": 2.6982219143519326,
                "gap_rejected_minus_accepted": 1.297093976708647
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6347945928573608,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1386801872253418,
                "rejected_mean_error": 2.317311052322388,
                "gap_rejected_minus_accepted": 1.178630865097046
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1216318607330322,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8490279212830558,
                "rejected_mean_error": 2.024118427286811,
                "gap_rejected_minus_accepted": 1.175090506003755
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9706035517706504,
            "spearman": 0.9658135633922524,
            "auroc_top30_bad": 0.9942491428571429,
            "mae": 0.15541074501836907,
            "mse": 0.04888591762482739,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6558444581312755,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08464011943340302
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2727405432939529
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5715644298195839
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8906069988330205
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9725571468995785,
            "spearman": 0.9474057964837099,
            "auroc_top30_worst": 0.9935634285714285,
            "pairwise_seed_ranking": 0.898,
            "predicted_best_mean_error": 1.4091189315319061,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07294027721881857,
            "gap_to_oracle": 0.007662415266036948,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7044802801609039
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8165448591686212
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.953214895105362
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1158902223494007
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.26761248111725,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.263955241759618,
                "rejected_mean_error": 3.3333937797546387,
                "gap_rejected_minus_accepted": 2.069438537995021
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.64396071434021,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1153538198137742,
                "rejected_mean_error": 2.5352630679980637,
                "gap_rejected_minus_accepted": 1.4199092481842894
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.184596598148346,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.953214895105362,
                "rejected_mean_error": 1.9885832960128784,
                "gap_rejected_minus_accepted": 1.0353684009075166
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.797445997595787,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8162889304442909,
                "rejected_mean_error": 1.6895682328920354,
                "gap_rejected_minus_accepted": 0.8732793024477445
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.290411353111267,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2736090128951603,
                "rejected_mean_error": 3.3581109714508055,
                "gap_rejected_minus_accepted": 2.084501958555645
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6794693171977997,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.119524202085434,
                "rejected_mean_error": 2.5581551809159535,
                "gap_rejected_minus_accepted": 1.4386309788305196
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1825587749481201,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9526079137325287,
                "rejected_mean_error": 2.0115105037689207,
                "gap_rejected_minus_accepted": 1.058902590036392
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.797553226351738,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8078855782274216,
                "rejected_mean_error": 1.7091872233120515,
                "gap_rejected_minus_accepted": 0.90130164508463
              }
            ]
          }
        }
      }
    },
    {
      "variant": "per_step_error_head",
      "feature_mode": "M4_seed_relative",
      "model_kind": "perstep",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 45,
      "best_calib_loss": 0.012157942168414593,
      "train_time_sec": 41.42435908317566,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994187786992597,
            "spearman": 0.9983230421296028,
            "auroc_top30_bad": 0.9993492380952381,
            "mae": 0.025304221869806496,
            "mse": 0.0014236344802608292,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8093416696450821,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.004406181700527668
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1865738742083311
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5935229934796691
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9737340248495341
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9995329962140094,
            "spearman": 0.9994281532730711,
            "auroc_top30_worst": 0.9994386666666667,
            "pairwise_seed_ranking": 0.9474,
            "predicted_best_mean_error": 1.6250874013602734,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.081362948745489,
            "gap_to_oracle": 0.001940880447626192,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5155455228090287
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7315778125286102
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0108279209375381
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2503794866085052
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2011754512786865,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530961235496733,
                "rejected_mean_error": 3.9155573358535767,
                "gap_rejected_minus_accepted": 2.4624612123039036
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0098888278007507,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2503794866085052,
                "rejected_mean_error": 3.0462305192947388,
                "gap_rejected_minus_accepted": 1.7958510326862336
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.506755769252777,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0108279209375381,
                "rejected_mean_error": 2.387856568622589,
                "gap_rejected_minus_accepted": 1.377028647685051
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0618877708911896,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7315778125286102,
                "rejected_mean_error": 2.0219303888638813,
                "gap_rejected_minus_accepted": 1.290352576335271
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2013277769088746,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4557858547237184,
                "rejected_mean_error": 3.962430808544159,
                "gap_rejected_minus_accepted": 2.506644953820441
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.013474941253662,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2496652955214183,
                "rejected_mean_error": 3.0768055138587953,
                "gap_rejected_minus_accepted": 1.827140218337377
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.506755769252777,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0077481907606125,
                "rejected_mean_error": 2.4051525094509123,
                "gap_rejected_minus_accepted": 1.3974043186902998
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.078670620918274,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7209036629199982,
                "rejected_mean_error": 2.034965912501017,
                "gap_rejected_minus_accepted": 1.3140622495810188
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9835935077363591,
            "spearman": 0.9840432886350845,
            "auroc_top30_bad": 0.9907542857142857,
            "mae": 0.11639634116930392,
            "mse": 0.026947491314002918,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.727441797727588,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.084599769115448
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20928235750198365
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6430871653437614
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0268146854956945
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9777567073462331,
            "spearman": 0.985270420269069,
            "auroc_top30_worst": 0.9969584761904762,
            "pairwise_seed_ranking": 0.8796,
            "predicted_best_mean_error": 1.6550593093633652,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07293631041049964,
            "gap_to_oracle": 0.005987054824829086,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6625823686122895
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.867405257641505
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.152279663705826
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.412816111625893
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6567549705505384,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5959144820372264,
                "rejected_mean_error": 2.9134100437164308,
                "gap_rejected_minus_accepted": 1.3174955616792043
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1573486924171448,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4118420987716989,
                "rejected_mean_error": 2.6731118249436157,
                "gap_rejected_minus_accepted": 1.2612697261719168
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6549565196037292,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.152279663705826,
                "rejected_mean_error": 2.303048412704468,
                "gap_rejected_minus_accepted": 1.150768748998642
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.084513545036316,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8690495111119633,
                "rejected_mean_error": 2.014479776711194,
                "gap_rejected_minus_accepted": 1.1454302655992308
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6931758165359496,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.594072568681505,
                "rejected_mean_error": 2.9333030796051025,
                "gap_rejected_minus_accepted": 1.3392305109235976
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.179887294769287,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4035245938734575,
                "rejected_mean_error": 2.691108029986185,
                "gap_rejected_minus_accepted": 1.2875834361127274
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6472833156585693,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1391536026000977,
                "rejected_mean_error": 2.316837636947632,
                "gap_rejected_minus_accepted": 1.1776840343475343
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0920677483081818,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.861664891242981,
                "rejected_mean_error": 2.0198610523805263,
                "gap_rejected_minus_accepted": 1.1581961611375453
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9692981566859901,
            "spearman": 0.9675801728841495,
            "auroc_top30_bad": 0.9940891428571428,
            "mae": 0.14588387077674853,
            "mse": 0.05169098129482335,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6527345407249541,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.13582340973615648
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.26682201919555665
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5717708822846412
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8900041893720627
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9605386073521834,
            "spearman": 0.9399781380980085,
            "auroc_top30_worst": 0.9894887619047619,
            "pairwise_seed_ranking": 0.8944,
            "predicted_best_mean_error": 1.4104929599761964,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07156624877452833,
            "gap_to_oracle": 0.009036443710327191,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7359559895992279
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8124207517084403
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9560111689090729
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1161633692125776
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3526462793350236,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2645197603702545,
                "rejected_mean_error": 3.328313112258911,
                "gap_rejected_minus_accepted": 2.0637933518886564
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.65944305062294,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1154766336258346,
                "rejected_mean_error": 2.534895411314675,
                "gap_rejected_minus_accepted": 1.4194187776888403
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1865441799163818,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9560111689090729,
                "rejected_mean_error": 1.9857870222091676,
                "gap_rejected_minus_accepted": 1.0297758533000947
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.845473513007164,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8128498037592672,
                "rejected_mean_error": 1.690717055359925,
                "gap_rejected_minus_accepted": 0.8778672516006577
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.341379117965698,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2745754706859589,
                "rejected_mean_error": 3.3494128513336183,
                "gap_rejected_minus_accepted": 2.0748373806476597
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6790851652622223,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1192299062236746,
                "rejected_mean_error": 2.559028725775461,
                "gap_rejected_minus_accepted": 1.4397988195517866
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1883306503295898,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9580643985271454,
                "rejected_mean_error": 2.006054018974304,
                "gap_rejected_minus_accepted": 1.0479896204471588
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.845473513007164,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8188357726922111,
                "rejected_mean_error": 1.705498120364021,
                "gap_rejected_minus_accepted": 0.8866623476718098
              }
            ]
          }
        }
      }
    },
    {
      "variant": "full_engineered_mlp",
      "feature_mode": "M2_engineered",
      "model_kind": "mlp_big",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1562,
      "best_epoch": 55,
      "best_calib_loss": 0.011622936464846134,
      "train_time_sec": 56.79639458656311,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9990970676010151,
            "spearman": 0.9976510313717654,
            "auroc_top30_bad": 0.9989420000000001,
            "mae": 0.039930076464029914,
            "mse": 0.0028902464237305406,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8163470810636669,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0042408787831664085
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1872965686529875
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5936682077273726
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9742109323094289
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9991136492612418,
            "spearman": 0.9985465818537586,
            "auroc_top30_worst": 0.9988392380952381,
            "pairwise_seed_ranking": 0.9433,
            "predicted_best_mean_error": 1.6255194463133813,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.0809309037923811,
            "gap_to_oracle": 0.0023729254007340828,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5169112862348556
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7326951603889466
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0113121023416518
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.250632860994339
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2165378093719488,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530605185429255,
                "rejected_mean_error": 3.9158777809143066,
                "gap_rejected_minus_accepted": 2.462817262371381
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0739632844924927,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.250632860994339,
                "rejected_mean_error": 3.0454703961372376,
                "gap_rejected_minus_accepted": 1.7948375351428987
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5322266221046448,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0113121023416518,
                "rejected_mean_error": 2.3873723872184756,
                "gap_rejected_minus_accepted": 1.3760602848768237
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0752995610237122,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7326951603889466,
                "rejected_mean_error": 2.021557939577103,
                "gap_rejected_minus_accepted": 1.2888627791881562
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.271590495109559,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4557090449995465,
                "rejected_mean_error": 3.9631220960617064,
                "gap_rejected_minus_accepted": 2.50741305106216
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0598820447921753,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2498227657477061,
                "rejected_mean_error": 3.0763331031799317,
                "gap_rejected_minus_accepted": 1.8265103374322256
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5339698195457458,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0081698020696641,
                "rejected_mean_error": 2.404730898141861,
                "gap_rejected_minus_accepted": 1.396561096072197
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0719060599803925,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7216924579143524,
                "rejected_mean_error": 2.0347029808362325,
                "gap_rejected_minus_accepted": 1.31301052292188
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9825582053396387,
            "spearman": 0.9839447254669209,
            "auroc_top30_bad": 0.9940777142857145,
            "mae": 0.11462567998434074,
            "mse": 0.026343455361971656,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7310042828855637,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10099813884496689
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21674449076652527
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6423648307681084
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0266400920788448
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9772500753717129,
            "spearman": 0.9843099035583384,
            "auroc_top30_worst": 0.9960441904761905,
            "pairwise_seed_ranking": 0.878,
            "predicted_best_mean_error": 1.6540378915071487,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.0739577282667161,
            "gap_to_oracle": 0.00496563696861263,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6770691554546356
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8651957558706785
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1530009514331818
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4161306707653156
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.622959136962892,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.593338425238927,
                "rejected_mean_error": 2.936594554901123,
                "gap_rejected_minus_accepted": 1.343256129662196
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2058780193328857,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4148512603188272,
                "rejected_mean_error": 2.664103568171541,
                "gap_rejected_minus_accepted": 1.2492523078527136
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.631301999092102,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1530009514331818,
                "rejected_mean_error": 2.302327124977112,
                "gap_rejected_minus_accepted": 1.14932617354393
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.172798365354538,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8656964242077483,
                "rejected_mean_error": 2.0155998580356544,
                "gap_rejected_minus_accepted": 1.1499034338279062
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6891007661819457,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5922718408372667,
                "rejected_mean_error": 2.949509630203247,
                "gap_rejected_minus_accepted": 1.3572377893659802
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.224581480026245,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.406177305282756,
                "rejected_mean_error": 2.683234108818902,
                "gap_rejected_minus_accepted": 1.277056803536146
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6199054718017578,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1414182481765747,
                "rejected_mean_error": 2.3145729913711546,
                "gap_rejected_minus_accepted": 1.17315474319458
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1860470175743103,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8544646236631606,
                "rejected_mean_error": 2.022286810976936,
                "gap_rejected_minus_accepted": 1.1678221873137755
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9679681876120365,
            "spearman": 0.963671957337818,
            "auroc_top30_bad": 0.9906270476190476,
            "mae": 0.14988760891982358,
            "mse": 0.04921180013015089,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6516464323792397,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07982764029502869
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.27224691755771635
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5752978317856788
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8955343511025111
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9615310809625861,
            "spearman": 0.9272180679795637,
            "auroc_top30_worst": 0.9802910476190476,
            "pairwise_seed_ranking": 0.9048,
            "predicted_best_mean_error": 1.411207089662552,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.0708521190881728,
            "gap_to_oracle": 0.009750573396682727,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7381240499019622
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8228250488829918
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9644909714221954
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.115949361213743
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.333885335922241,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.263920703490575,
                "rejected_mean_error": 3.3337046241760255,
                "gap_rejected_minus_accepted": 2.0697839206854507
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7827737033367157,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1153200124663758,
                "rejected_mean_error": 2.5353642740188698,
                "gap_rejected_minus_accepted": 1.420044261552494
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2117953300476074,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9644909714221954,
                "rejected_mean_error": 1.9773072196960448,
                "gap_rejected_minus_accepted": 1.0128162482738494
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8863438367843628,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8226092898617157,
                "rejected_mean_error": 1.6874569495434186,
                "gap_rejected_minus_accepted": 0.864847659681703
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3367411136627196,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8232746124267578,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.11988346063517,
                "rejected_mean_error": 2.55708881030007,
                "gap_rejected_minus_accepted": 1.4372053496649
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.204014241695404,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9670674560070038,
                "rejected_mean_error": 1.9970509614944458,
                "gap_rejected_minus_accepted": 1.029983505487442
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8761799037456512,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8310210851449815,
                "rejected_mean_error": 1.701392908147312,
                "gap_rejected_minus_accepted": 0.8703718230023305
              }
            ]
          }
        }
      }
    },
    {
      "variant": "full_engineered_simvla_focused",
      "feature_mode": "M2_engineered",
      "model_kind": "mlp_big",
      "train_setting": "simvla_focused",
      "train_rows": 10000,
      "input_dim": 1562,
      "best_epoch": 91,
      "best_calib_loss": 0.010306158103048801,
      "train_time_sec": 55.6901113986969,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9990839461743105,
            "spearman": 0.9976650450985153,
            "auroc_top30_bad": 0.999191,
            "mae": 0.03193730734095675,
            "mse": 0.0018713363256130102,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8033718319263755,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0053109355792403225
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18683450046479702
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5936471075639129
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9740873883634805
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9992750259202532,
            "spearman": 0.9988757490429758,
            "auroc_top30_worst": 0.9991535238095238,
            "pairwise_seed_ranking": 0.9499,
            "predicted_best_mean_error": 1.624535800665617,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08191454944014542,
            "gap_to_oracle": 0.0013892797529697631,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5168323088884353
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7324455829143525
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0112423667669297
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2505842172781627
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.169257974624635,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.453197444346216,
                "rejected_mean_error": 3.914645448684692,
                "gap_rejected_minus_accepted": 2.461448004338476
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0044451355934143,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2505842172781627,
                "rejected_mean_error": 3.045616327285767,
                "gap_rejected_minus_accepted": 1.795032110007604
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5038526058197021,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0112423667669297,
                "rejected_mean_error": 2.3874421227931975,
                "gap_rejected_minus_accepted": 1.3761997560262678
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0706997513771057,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7324455829143525,
                "rejected_mean_error": 2.021641132068634,
                "gap_rejected_minus_accepted": 1.2891955491542815
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2161753416061405,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4558035747872458,
                "rejected_mean_error": 3.962271327972412,
                "gap_rejected_minus_accepted": 2.5064677531851665
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9932612776756287,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2497797451814017,
                "rejected_mean_error": 3.076462164878845,
                "gap_rejected_minus_accepted": 1.8266824196974434
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4990500807762146,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0079376167058944,
                "rejected_mean_error": 2.4049630835056304,
                "gap_rejected_minus_accepted": 1.397025466799736
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.06919726729393,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7210639750957489,
                "rejected_mean_error": 2.0349124751091003,
                "gap_rejected_minus_accepted": 1.3138485000133513
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9855175946050935,
            "spearman": 0.985590140955299,
            "auroc_top30_bad": 0.992160761904762,
            "mae": 0.10840319482229285,
            "mse": 0.022668088346156957,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7263724015995934,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08583100479841232
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21122686882019043
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6423026923060418
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0268700252453486
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9834471365874714,
            "spearman": 0.9880117273675056,
            "auroc_top30_worst": 0.9956419047619047,
            "pairwise_seed_ranking": 0.892,
            "predicted_best_mean_error": 1.6530657478570938,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07492987191677103,
            "gap_to_oracle": 0.003993493318557695,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6700753052234649
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.863700112566734
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1513128494739533
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4116086229396019
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.626659631729127,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.591050742811627,
                "rejected_mean_error": 2.957183696746826,
                "gap_rejected_minus_accepted": 1.3661329539351992
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.169405162334442,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.410666043533205,
                "rejected_mean_error": 2.6766324759291384,
                "gap_rejected_minus_accepted": 1.2659664323959334
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6392275094985962,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1513128494739533,
                "rejected_mean_error": 2.3040152269363405,
                "gap_rejected_minus_accepted": 1.1527023774623872
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.145729422569275,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8646299569561078,
                "rejected_mean_error": 2.0159561059009303,
                "gap_rejected_minus_accepted": 1.1513261489448225
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.657180380821228,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5888885529836019,
                "rejected_mean_error": 2.9799592208862307,
                "gap_rejected_minus_accepted": 1.3910706679026288
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1872408986091614,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4030908288802693,
                "rejected_mean_error": 2.692395554648505,
                "gap_rejected_minus_accepted": 1.289304725768236
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.638574481010437,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1389093523025513,
                "rejected_mean_error": 2.317081887245178,
                "gap_rejected_minus_accepted": 1.1781725349426269
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1476545929908752,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8557838333977593,
                "rejected_mean_error": 2.021842371333729,
                "gap_rejected_minus_accepted": 1.1660585379359696
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9700958237298437,
            "spearman": 0.9666385529418919,
            "auroc_top30_bad": 0.9919177142857143,
            "mae": 0.15100017014328715,
            "mse": 0.047724044481313586,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6507284836829399,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08255961728096008
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2614020577430725
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.572750178873539
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8936694977521896
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9673983081594926,
            "spearman": 0.9418970272620976,
            "auroc_top30_worst": 0.9851916190476191,
            "pairwise_seed_ranking": 0.902,
            "predicted_best_mean_error": 1.4112030646800995,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07085614407062524,
            "gap_to_oracle": 0.009746548414230283,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7057047846317291
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8216151372553446
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9587364029407501
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.116616560483792
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3536264657974244,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.263833387401369,
                "rejected_mean_error": 3.3344904689788817,
                "gap_rejected_minus_accepted": 2.0706570815775125
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7233443558216095,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1160983276278131,
                "rejected_mean_error": 2.533034301794375,
                "gap_rejected_minus_accepted": 1.416935974166562
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2340105772018433,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9587364029407501,
                "rejected_mean_error": 1.9830617881774901,
                "gap_rejected_minus_accepted": 1.02432538523674
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8376221805810928,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8214472211397494,
                "rejected_mean_error": 1.6878451325850146,
                "gap_rejected_minus_accepted": 0.8663979114452651
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3393121957778926,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7570212185382843,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1200003819988373,
                "rejected_mean_error": 2.556741757998391,
                "gap_rejected_minus_accepted": 1.4367413759995535
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2325815558433533,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9563448598384857,
                "rejected_mean_error": 2.007773557662964,
                "gap_rejected_minus_accepted": 1.0514286978244782
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.841237023472786,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8125840912735651,
                "rejected_mean_error": 1.7076043018045273,
                "gap_rejected_minus_accepted": 0.8950202105309621
              }
            ]
          }
        }
      }
    },
    {
      "variant": "seed_relative_simvla_focused",
      "feature_mode": "M4_seed_relative",
      "model_kind": "mlp_big_pairwise",
      "train_setting": "simvla_focused",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 69,
      "best_calib_loss": 0.00978406798094511,
      "train_time_sec": 60.15664744377136,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9991887209146203,
            "spearman": 0.9978512681891316,
            "auroc_top30_bad": 0.9988710476190475,
            "mae": 0.04996276796979764,
            "mse": 0.003944065998025203,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8232196608723398,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0015489479824900628
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1870604071110487
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.593681992469728
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9740775634040435
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9993216998478424,
            "spearman": 0.9986919158036137,
            "auroc_top30_worst": 0.9990809523809524,
            "pairwise_seed_ranking": 0.9579,
            "predicted_best_mean_error": 1.6244578323066234,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08199251779913896,
            "gap_to_oracle": 0.0013113113939762222,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5167964183092117
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7321455941677093
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.011325526213646
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2504180793285369
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.198470330238343,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4531720761855442,
                "rejected_mean_error": 3.9148737621307372,
                "gap_rejected_minus_accepted": 2.461701685945193
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0569260120391846,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2504180793285369,
                "rejected_mean_error": 3.0461147411346436,
                "gap_rejected_minus_accepted": 1.7956966618061068
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5534764528274536,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.011325526213646,
                "rejected_mean_error": 2.387358963346481,
                "gap_rejected_minus_accepted": 1.376033437132835
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.098181277513504,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7321455941677093,
                "rejected_mean_error": 2.021741128317515,
                "gap_rejected_minus_accepted": 1.2895955341498055
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2470793485641485,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455705801712142,
                "rejected_mean_error": 3.9631512856483457,
                "gap_rejected_minus_accepted": 2.5074454839362037
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.06947660446167,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2495712708632152,
                "rejected_mean_error": 3.0770875878334047,
                "gap_rejected_minus_accepted": 1.8275163169701896
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.547622263431549,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0080160819292068,
                "rejected_mean_error": 2.4048846182823183,
                "gap_rejected_minus_accepted": 1.3968685363531115
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1201915442943573,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7213483564853668,
                "rejected_mean_error": 2.034817681312561,
                "gap_rejected_minus_accepted": 1.313469324827194
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9853201672981033,
            "spearman": 0.9843814277186355,
            "auroc_top30_bad": 0.9917874285714285,
            "mae": 0.0988534117257303,
            "mse": 0.022325949715148972,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7333061642338943,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09877856761217117
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2158934340953827
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6415378224253655
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0258258527040482
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9898192265163759,
            "spearman": 0.9903558737637592,
            "auroc_top30_worst": 0.995623619047619,
            "pairwise_seed_ranking": 0.896,
            "predicted_best_mean_error": 1.6520506910085677,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07594492876529713,
            "gap_to_oracle": 0.002978436470031598,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6535677788257599
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8611428960202596
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1523178732395172
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.411629359001544
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5840492725372317,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5891313378281064,
                "rejected_mean_error": 2.9744583415985106,
                "gap_rejected_minus_accepted": 1.3853270037704042
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.234514355659485,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4107072792605377,
                "rejected_mean_error": 2.6765090322342164,
                "gap_rejected_minus_accepted": 1.2658017529736787
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6612969040870667,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1523178732395172,
                "rejected_mean_error": 2.303010203170776,
                "gap_rejected_minus_accepted": 1.150692329931259
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1110671162605286,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8620809104305487,
                "rejected_mean_error": 2.016807601698689,
                "gap_rejected_minus_accepted": 1.1547266912681404
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.588117504119873,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5866629409790038,
                "rejected_mean_error": 2.9999897289276123,
                "gap_rejected_minus_accepted": 1.4133267879486084
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2347450852394104,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.402070884398598,
                "rejected_mean_error": 2.6954230089036244,
                "gap_rejected_minus_accepted": 1.2933521245050263
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.645780324935913,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.139765305519104,
                "rejected_mean_error": 2.3162259340286253,
                "gap_rejected_minus_accepted": 1.1764606285095214
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1321786642074585,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8539810729405236,
                "rejected_mean_error": 2.022449718439643,
                "gap_rejected_minus_accepted": 1.1684686454991193
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9770043244315545,
            "spearman": 0.9754312661815516,
            "auroc_top30_bad": 0.9934765714285715,
            "mae": 0.127584389804845,
            "mse": 0.035951644066146704,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.67216110822022,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06338792783021927
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2435474226474762
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5709291602253914
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.891062930115064
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.981411429921508,
            "spearman": 0.9634568654443939,
            "auroc_top30_worst": 0.9897386666666668,
            "pairwise_seed_ranking": 0.8976,
            "predicted_best_mean_error": 1.4089546446800232,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07310456407070154,
            "gap_to_oracle": 0.007498128414153982,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6568083488941192
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8024227113868946
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9496290165424347
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.116820171729588
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3130115985870363,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2644003251658547,
                "rejected_mean_error": 3.329388029098511,
                "gap_rejected_minus_accepted": 2.0649877039326565
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6656022667884827,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1160743168158618,
                "rejected_mean_error": 2.5331061808065103,
                "gap_rejected_minus_accepted": 1.4170318639906485
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1997292637825012,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9496290165424347,
                "rejected_mean_error": 1.9921691745758057,
                "gap_rejected_minus_accepted": 1.042540158033371
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8536787033081055,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8029759245368239,
                "rejected_mean_error": 1.694015373606056,
                "gap_rejected_minus_accepted": 0.891039449069232
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.319951272010803,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7052516341209412,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1200003819988373,
                "rejected_mean_error": 2.556741757998391,
                "gap_rejected_minus_accepted": 1.4367413759995535
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.201608121395111,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9477162358760833,
                "rejected_mean_error": 2.016402181625366,
                "gap_rejected_minus_accepted": 1.0686859457492828
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8526128381490707,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7970240839890071,
                "rejected_mean_error": 1.7128464432961163,
                "gap_rejected_minus_accepted": 0.9158223593071092
              }
            ]
          }
        }
      }
    }
  ]
}
```
