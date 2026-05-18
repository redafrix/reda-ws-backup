# Stage 7 Multi-Expert Target Experiments: holdout_libero_goal

```json
{
  "split": "holdout_libero_goal",
  "by_target": {
    "target_chunk_l2_single_expert": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 74,
        "best_calib_loss": 0.05788557603955269,
        "train_time_sec": 11.048765420913696,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9755614316325152,
              "spearman": 0.9408842172993089,
              "auroc_top30_bad": 0.9991508571428571,
              "mae": 0.1255400044336915,
              "mse": 0.047621739783028603,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 0.974,
              "same_context_pred_std": 0.7395634775881433,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3010564105659723
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.32443130972981454
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.48462027342617514
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8179438002129396
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9988457776420215,
              "spearman": 0.9978117328084692,
              "auroc_top30_worst": 0.998178857142857,
              "pairwise_seed_ranking": 0.8611,
              "predicted_best_mean_error": 1.6903341224193573,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.06900418120622631,
              "gap_to_oracle": 0.005270311355590751,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6116930367350578
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8485748816728592
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1108946244359017
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3370694047371547
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7848685264587414,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4977046497199271,
                  "rejected_mean_error": 4.007711332798004,
                  "gap_rejected_minus_accepted": 2.5100066830780765
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.955022931098938,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3370694047371547,
                  "rejected_mean_error": 2.983613057899475,
                  "gap_rejected_minus_accepted": 1.6465436531623203
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5541808009147644,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1108946244359017,
                  "rejected_mean_error": 2.386516011619568,
                  "gap_rejected_minus_accepted": 1.2756213871836661
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1249407231807709,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8485748816728592,
                  "rejected_mean_error": 2.0487487968126934,
                  "gap_rejected_minus_accepted": 1.200173915139834
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7876909255981452,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5080876645114687,
                  "rejected_mean_error": 4.0205940556526185,
                  "gap_rejected_minus_accepted": 2.51250639114115
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9644325375556946,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.347178504228592,
                  "rejected_mean_error": 2.995817701816559,
                  "gap_rejected_minus_accepted": 1.6486391975879668
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5607041716575623,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1174917401075364,
                  "rejected_mean_error": 2.401184867143631,
                  "gap_rejected_minus_accepted": 1.2836931270360945
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1391964852809906,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8519523589611053,
                  "rejected_mean_error": 2.06180028518041,
                  "gap_rejected_minus_accepted": 1.2098479262193045
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8495319535067557,
              "spearman": 0.843565892030527,
              "auroc_top30_bad": 0.9254102857142857,
              "mae": 0.32616431339979174,
              "mse": 0.21386507892361037,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.6737610554346756,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3030768063366413
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.33034478594064715
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4977381482243538
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8485444941918056
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6612335232874369,
              "spearman": 0.6866141676890674,
              "auroc_top30_worst": 0.8359801904761905,
              "pairwise_seed_ranking": 0.788,
              "predicted_best_mean_error": 1.6042565277814864,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.08630361390113839,
              "gap_to_oracle": 0.015729046344757025,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0615514619350432
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0280264132680037
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2700263335227966
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4389781787324307
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.52659170627594,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5978495292133754,
                  "rejected_mean_error": 2.304294797897339,
                  "gap_rejected_minus_accepted": 0.7064452686839635
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.89163276553154,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4393749209707294,
                  "rejected_mean_error": 2.3543874413822405,
                  "gap_rejected_minus_accepted": 0.9150125204115112
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.566700041294098,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2700263335227966,
                  "rejected_mean_error": 2.066961778640747,
                  "gap_rejected_minus_accepted": 0.7969354451179504
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0091446042060852,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0278430834364967,
                  "rejected_mean_error": 1.8825001974243238,
                  "gap_rejected_minus_accepted": 0.8546571139878272
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.535924291610718,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6210613924927182,
                  "rejected_mean_error": 2.3160488843917846,
                  "gap_rejected_minus_accepted": 0.6949874918990664
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9501333832740784,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4615509161018432,
                  "rejected_mean_error": 2.3703176842795477,
                  "gap_rejected_minus_accepted": 0.9087667681777045
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.600242257118225,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2844324781894685,
                  "rejected_mean_error": 2.0966878051757813,
                  "gap_rejected_minus_accepted": 0.8122553269863129
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0307787656784058,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0207928281927865,
                  "rejected_mean_error": 1.916203675104335,
                  "gap_rejected_minus_accepted": 0.8954108469115485
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8896508745937555,
              "spearman": 0.8592334327828507,
              "auroc_top30_bad": 0.9292434285714286,
              "mae": 0.28107573706805705,
              "mse": 0.15002504495410102,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 0.972,
              "same_context_pred_std": 0.6900826693683285,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3249001106917858
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.35111856590509416
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5811829263031483
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9860006156245867
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7483003276101069,
              "spearman": 0.7403505722563665,
              "auroc_top30_worst": 0.8190659047619047,
              "pairwise_seed_ranking": 0.7916,
              "predicted_best_mean_error": 1.7760264101028442,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.09086771202087407,
              "gap_to_oracle": 0.01799207901954647,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0377252502441405
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.279249584254546
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5257343463897706
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6976079311706365
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1367515563964847,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7772165916760763,
                  "rejected_mean_error": 2.338850345611572,
                  "gap_rejected_minus_accepted": 0.5616337539354959
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9571446478366852,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.697095915627454,
                  "rejected_mean_error": 2.241361296786287,
                  "gap_rejected_minus_accepted": 0.5442653811588329
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7054588198661804,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5257343463897706,
                  "rejected_mean_error": 2.141025587749481,
                  "gap_rejected_minus_accepted": 0.6152912413597105
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.391766905784607,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2806096505433227,
                  "rejected_mean_error": 2.018030030114165,
                  "gap_rejected_minus_accepted": 0.7374203795708423
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.180365967750549,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8029187297821045,
                  "rejected_mean_error": 2.442672653198242,
                  "gap_rejected_minus_accepted": 0.6397539234161376
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9663289785385132,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7140069237367355,
                  "rejected_mean_error": 2.320702155431112,
                  "gap_rejected_minus_accepted": 0.6066952316943763
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.721621811389923,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5313044004440308,
                  "rejected_mean_error": 2.202483843803406,
                  "gap_rejected_minus_accepted": 0.671179443359375
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4315576553344727,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2596461148489089,
                  "rejected_mean_error": 2.0714750015799375,
                  "gap_rejected_minus_accepted": 0.8118288867310286
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8734160901329462,
              "spearman": 0.8489113279741428,
              "auroc_top30_bad": 0.9215095238095238,
              "mae": 0.4232157054916024,
              "mse": 0.3689963671278966,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.495,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7359145420517763,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5040221733599901
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4807959127128124
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8102707254588604
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.131521800895532
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8169451743833116,
              "spearman": 0.7012924732924734,
              "auroc_top30_worst": 0.8206619047619048,
              "pairwise_seed_ranking": 0.7315,
              "predicted_best_mean_error": 2.260086405873299,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.06654601037502283,
              "gap_to_oracle": 0.018675881326198684,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.8610091906785966
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.8043388385772705
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8213463785648345
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8761020220120748
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.199215173721314,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.1425055436293285,
                  "rejected_mean_error": 3.9246609950065614,
                  "gap_rejected_minus_accepted": 1.7821554513772329
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.239692986011505,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8761020220120748,
                  "rejected_mean_error": 3.6545782890319822,
                  "gap_rejected_minus_accepted": 1.7784762670199075
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6366352438926697,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.8213463785648345,
                  "rejected_mean_error": 2.8200957989692688,
                  "gap_rejected_minus_accepted": 0.9987494204044343
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.240502119064331,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.8043388385772705,
                  "rejected_mean_error": 2.492848505496979,
                  "gap_rejected_minus_accepted": 0.6885096669197084
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1998553514480585,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1488088766733804,
                  "rejected_mean_error": 3.9270442724227905,
                  "gap_rejected_minus_accepted": 1.7782353957494101
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.30790913105011,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8860305960973103,
                  "rejected_mean_error": 3.648437876701355,
                  "gap_rejected_minus_accepted": 1.7624072806040447
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6947033405303955,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8379672908782958,
                  "rejected_mean_error": 2.815297541618347,
                  "gap_rejected_minus_accepted": 0.9773302507400514
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2200652062892914,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.8104269051551818,
                  "rejected_mean_error": 2.498700919946035,
                  "gap_rejected_minus_accepted": 0.688274014790853
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 73,
        "best_calib_loss": 0.013740090653300285,
        "train_time_sec": 35.236366510391235,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997851420927706,
              "spearman": 0.9988295191862662,
              "auroc_top30_bad": 0.9998569047619048,
              "mae": 0.01585989978304133,
              "mse": 0.0004432832583022619,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7678080327300286,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0004415875524282455
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17377719233632088
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47780501110851764
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8172738874614238
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998632313974309,
              "spearman": 0.9997105881404166,
              "auroc_top30_worst": 0.9997819047619048,
              "pairwise_seed_ranking": 0.9442,
              "predicted_best_mean_error": 1.6858004261851312,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.07353787744045248,
              "gap_to_oracle": 0.0007366151213645811,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6085692955851555
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8468824316263199
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1102546112179756
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3366660552422205
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8732919216156025,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4976223174267345,
                  "rejected_mean_error": 4.008452323436737,
                  "gap_rejected_minus_accepted": 2.5108300060100026
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.002564311027527,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3366660552422205,
                  "rejected_mean_error": 2.9848231063842774,
                  "gap_rejected_minus_accepted": 1.648157051142057
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.605503261089325,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1102546112179756,
                  "rejected_mean_error": 2.387156024837494,
                  "gap_rejected_minus_accepted": 1.2769014136195183
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1561248302459717,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8468824316263199,
                  "rejected_mean_error": 2.0493129468282065,
                  "gap_rejected_minus_accepted": 1.2024305152018866
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.894766139984131,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5080162266227934,
                  "rejected_mean_error": 4.021236996650696,
                  "gap_rejected_minus_accepted": 2.513220770027903
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0166446566581726,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3469705584049225,
                  "rejected_mean_error": 2.996441539287567,
                  "gap_rejected_minus_accepted": 1.6494709808826444
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6172258853912354,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1168913735151291,
                  "rejected_mean_error": 2.4017852337360384,
                  "gap_rejected_minus_accepted": 1.2848938602209092
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1676359474658966,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8504813458919526,
                  "rejected_mean_error": 2.0622906228701274,
                  "gap_rejected_minus_accepted": 1.2118092769781748
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9756835503937338,
              "spearman": 0.9827325567862052,
              "auroc_top30_bad": 0.9928891428571429,
              "mae": 0.11892645864635706,
              "mse": 0.03532725567491194,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.972,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7421271752675415,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06976925683021545
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16510597262382506
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4197288850903511
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8057508502403895
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.939361159048815,
              "spearman": 0.9732482634548887,
              "auroc_top30_worst": 0.9752624761904762,
              "pairwise_seed_ranking": 0.9404,
              "predicted_best_mean_error": 1.5900335260629654,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.10052661561965937,
              "gap_to_oracle": 0.0015060446262360472,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46478781843185424
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7564243020919653
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1174948548316956
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3934976391827882
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5695218801498414,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5619253136846754,
                  "rejected_mean_error": 2.6276127376556397,
                  "gap_rejected_minus_accepted": 1.0656874239709644
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.095278561115265,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3925674771422891,
                  "rejected_mean_error": 2.494510683769616,
                  "gap_rejected_minus_accepted": 1.101943206627327
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7104899287223816,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1174948548316956,
                  "rejected_mean_error": 2.219493257331848,
                  "gap_rejected_minus_accepted": 1.1019984025001526
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.156132459640503,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7571500781625985,
                  "rejected_mean_error": 1.9729237947036515,
                  "gap_rejected_minus_accepted": 1.2157737165410532
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.640967035293579,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5776567714744143,
                  "rejected_mean_error": 2.7066904735565185,
                  "gap_rejected_minus_accepted": 1.1290337020821042
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.133047103881836,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4080010743383418,
                  "rejected_mean_error": 2.529267214593433,
                  "gap_rejected_minus_accepted": 1.1212661402550914
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7316219806671143,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1328479673862457,
                  "rejected_mean_error": 2.248272315979004,
                  "gap_rejected_minus_accepted": 1.1154243485927582
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.179139405488968,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7681849272478194,
                  "rejected_mean_error": 2.0013068716793776,
                  "gap_rejected_minus_accepted": 1.2331219444315582
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9844270308430492,
              "spearman": 0.9811094357731921,
              "auroc_top30_bad": 0.9861729523809524,
              "mae": 0.09650923431115226,
              "mse": 0.021444451420625742,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7663553966912721,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05519605165719986
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16957560638189315
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5376255432069301
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9457855738282204
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9476666547433839,
              "spearman": 0.9620944694364605,
              "auroc_top30_worst": 0.968783238095238,
              "pairwise_seed_ranking": 0.9268,
              "predicted_best_mean_error": 1.760712111711502,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.1061820104122162,
              "gap_to_oracle": 0.0026777806282043404,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8675877223014832
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1755644275974004
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4560783940315247
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6424988247057013
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.387579250335693,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7526180120574104,
                  "rejected_mean_error": 2.5602375621795654,
                  "gap_rejected_minus_accepted": 0.807619550122155
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1251391768455505,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6417457869747532,
                  "rejected_mean_error": 2.407058007800922,
                  "gap_rejected_minus_accepted": 0.7653122208261687
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.878700077533722,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4560783940315247,
                  "rejected_mean_error": 2.210681540107727,
                  "gap_rejected_minus_accepted": 0.7546031460762024
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.526538074016571,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1766234040260315,
                  "rejected_mean_error": 2.0527660975206876,
                  "gap_rejected_minus_accepted": 0.8761426934946561
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.488384509086609,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7767007870144313,
                  "rejected_mean_error": 2.6786341381073,
                  "gap_rejected_minus_accepted": 0.9019333510928687
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1434929370880127,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6566261894562666,
                  "rejected_mean_error": 2.4910227476604403,
                  "gap_rejected_minus_accepted": 0.8343965582041737
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.891528308391571,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4702360191345214,
                  "rejected_mean_error": 2.263552225112915,
                  "gap_rejected_minus_accepted": 0.7933162059783938
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.577826052904129,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1834092329418848,
                  "rejected_mean_error": 2.0971590847892556,
                  "gap_rejected_minus_accepted": 0.9137498518473708
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9881111575394412,
              "spearman": 0.9866095534298769,
              "auroc_top30_bad": 0.9928119047619048,
              "mae": 0.11535896962671541,
              "mse": 0.03137497948823136,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.985,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9071396876802871,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0695051308721304
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2204474041759968
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7042114396095276
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.082671810388565
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9832088992254795,
              "spearman": 0.9877719157719158,
              "auroc_top30_worst": 0.9925904761904762,
              "pairwise_seed_ranking": 0.891,
              "predicted_best_mean_error": 2.2440944692492484,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08253794699907324,
              "gap_to_oracle": 0.0026839447021482776,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.301912121772766
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.483361605644226
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6542626445293427
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8753441783587137
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.965232491493225,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0962958975632984,
                  "rejected_mean_error": 4.34054780960083,
                  "gap_rejected_minus_accepted": 2.2442519120375315
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6132395267486572,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8753441783587137,
                  "rejected_mean_error": 3.6568518199920654,
                  "gap_rejected_minus_accepted": 1.7815076416333517
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.048532247543335,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6542626445293427,
                  "rejected_mean_error": 2.9871795330047606,
                  "gap_rejected_minus_accepted": 1.332916888475418
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.709319293498993,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.483361605644226,
                  "rejected_mean_error": 2.59984091647466,
                  "gap_rejected_minus_accepted": 1.116479310830434
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.964351725578308,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6141768097877502,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8898193041483562,
                  "rejected_mean_error": 3.6370717525482177,
                  "gap_rejected_minus_accepted": 1.7472524483998615
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0550507307052612,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6711355865001678,
                  "rejected_mean_error": 2.982129245996475,
                  "gap_rejected_minus_accepted": 1.3109936594963074
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7276693880558014,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4998782134056092,
                  "rejected_mean_error": 2.6022171505292255,
                  "gap_rejected_minus_accepted": 1.1023389371236163
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 68,
        "best_calib_loss": 0.010922934859991074,
        "train_time_sec": 41.47898840904236,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993530291804573,
              "spearman": 0.9980877283679268,
              "auroc_top30_bad": 0.999280619047619,
              "mae": 0.03257832728644753,
              "mse": 0.0019911649510747425,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7806282152744177,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.002633060157299042
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1740386725604534
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47817998705208303
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8176728396912416
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9993773368138787,
              "spearman": 0.9985593172863725,
              "auroc_top30_worst": 0.9989662857142858,
              "pairwise_seed_ranking": 0.9643,
              "predicted_best_mean_error": 1.6855437838435172,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.07379451978206641,
              "gap_to_oracle": 0.0004799727797506481,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6090297806859016
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8478529746294021
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1108228278279304
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3369382331291835
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.937847042083742,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4976235654155414,
                  "rejected_mean_error": 4.008441091537476,
                  "gap_rejected_minus_accepted": 2.5108175261219343
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0307071805000305,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3369382331291835,
                  "rejected_mean_error": 2.9840065727233887,
                  "gap_rejected_minus_accepted": 1.6470683395942052
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6183471083641052,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1108228278279304,
                  "rejected_mean_error": 2.386587808227539,
                  "gap_rejected_minus_accepted": 1.2757649803996087
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1761825382709503,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8478529746294021,
                  "rejected_mean_error": 2.048989432493846,
                  "gap_rejected_minus_accepted": 1.2011364578644437
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.938084387779236,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5080162266227934,
                  "rejected_mean_error": 4.021236996650696,
                  "gap_rejected_minus_accepted": 2.513220770027903
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.052142083644867,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3474020966688791,
                  "rejected_mean_error": 2.995146924495697,
                  "gap_rejected_minus_accepted": 1.6477448278268179
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6391234993934631,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1171256769895554,
                  "rejected_mean_error": 2.401550930261612,
                  "gap_rejected_minus_accepted": 1.2844252532720566
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1849367320537567,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8520549237728119,
                  "rejected_mean_error": 2.061766096909841,
                  "gap_rejected_minus_accepted": 1.2097111731370291
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9841974900053532,
              "spearman": 0.9745267499583865,
              "auroc_top30_bad": 0.9950773333333334,
              "mae": 0.11059753731862147,
              "mse": 0.02407937967126903,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7027514763519944,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10714183232188225
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19433119206428529
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4185652436375618
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8036808062314987
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9839328142729645,
              "spearman": 0.9865322880846644,
              "auroc_top30_worst": 0.9840304761904762,
              "pairwise_seed_ranking": 0.9352,
              "predicted_best_mean_error": 1.5894878333806992,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.1010723083019256,
              "gap_to_oracle": 0.0009603519439698172,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46586763095855716
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7514090528472875
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.118617952632904
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3879756806120436
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.51807656288147,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5352955508232116,
                  "rejected_mean_error": 2.8672806034088136,
                  "gap_rejected_minus_accepted": 1.331985052585602
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0460020303726196,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.387246713885121,
                  "rejected_mean_error": 2.5104389750538543,
                  "gap_rejected_minus_accepted": 1.1231922611687333
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5989294648170471,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.118617952632904,
                  "rejected_mean_error": 2.2183701595306395,
                  "gap_rejected_minus_accepted": 1.0997522068977355
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0720875561237335,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7525847325690638,
                  "rejected_mean_error": 1.9744488247685141,
                  "gap_rejected_minus_accepted": 1.2218640921994504
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.568144154548645,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5529751969708336,
                  "rejected_mean_error": 2.928824644088745,
                  "gap_rejected_minus_accepted": 1.3758494471179115
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.082208573818207,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4064033823536042,
                  "rejected_mean_error": 2.534009570167178,
                  "gap_rejected_minus_accepted": 1.127606187813574
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6124882102012634,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1359083778858186,
                  "rejected_mean_error": 2.2452119054794313,
                  "gap_rejected_minus_accepted": 1.1093035275936127
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1026975214481354,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7694846755928464,
                  "rejected_mean_error": 2.000868988547096,
                  "gap_rejected_minus_accepted": 1.2313843129542494
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9812861109486805,
              "spearman": 0.9757972624244484,
              "auroc_top30_bad": 0.9830278095238096,
              "mae": 0.10821408708266718,
              "mse": 0.025451190008623083,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7377555829469956,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10793926137685776
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19446143304109573
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5404024608552456
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9438433694799742
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9653717932412919,
              "spearman": 0.9720459126053843,
              "auroc_top30_worst": 0.9888426666666666,
              "pairwise_seed_ranking": 0.9328,
              "predicted_best_mean_error": 1.7601809117794036,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.10671321034431469,
              "gap_to_oracle": 0.0021465806961058487,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8823754687309265
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1789650105130978
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4553283478736878
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6357347479125839
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4631514310836793,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.749283004283905,
                  "rejected_mean_error": 2.5902526321411132,
                  "gap_rejected_minus_accepted": 0.8409696278572083
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2102556228637695,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6350372803885502,
                  "rejected_mean_error": 2.42714066170275,
                  "gap_rejected_minus_accepted": 0.7921033813141998
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.812738060951233,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4553283478736878,
                  "rejected_mean_error": 2.211431586265564,
                  "gap_rejected_minus_accepted": 0.756103238391876
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4756019115447998,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1799091563438073,
                  "rejected_mean_error": 2.0516685089662974,
                  "gap_rejected_minus_accepted": 0.87175935262249
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.543219971656799,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.770903721915351,
                  "rejected_mean_error": 2.7308077239990234,
                  "gap_rejected_minus_accepted": 0.9599040020836724
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.269872784614563,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6513563362672368,
                  "rejected_mean_error": 2.506665010300894,
                  "gap_rejected_minus_accepted": 0.8553086740336571
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.831095576286316,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4669472827911376,
                  "rejected_mean_error": 2.2668409614562988,
                  "gap_rejected_minus_accepted": 0.7998936786651611
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5037972033023834,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1909375247501193,
                  "rejected_mean_error": 2.094622815356535,
                  "gap_rejected_minus_accepted": 0.9036852906064157
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9870176679345699,
              "spearman": 0.9809587774719724,
              "auroc_top30_bad": 0.9914107142857143,
              "mae": 0.1201920040889454,
              "mse": 0.0322347886021573,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9117400499319905,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07602023385465145
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2198966870009899
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7074108575582504
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0850461328824361
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9846244975454481,
              "spearman": 0.9706148746148746,
              "auroc_top30_worst": 0.9935095238095238,
              "pairwise_seed_ranking": 0.897,
              "predicted_best_mean_error": 2.2452849516272546,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08134746462106701,
              "gap_to_oracle": 0.0038744270801545078,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3196672928333282
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5071510043144225
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6594249835014343
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8661644180615744
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.00791130065918,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0954242747359806,
                  "rejected_mean_error": 4.348392415046692,
                  "gap_rejected_minus_accepted": 2.252968140310711
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.767831027507782,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8661644180615744,
                  "rejected_mean_error": 3.684391100883484,
                  "gap_rejected_minus_accepted": 1.8182266828219096
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9742552638053894,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6594249835014343,
                  "rejected_mean_error": 2.982017194032669,
                  "gap_rejected_minus_accepted": 1.3225922105312347
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6518453061580658,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.5071510043144225,
                  "rejected_mean_error": 2.591911116917928,
                  "gap_rejected_minus_accepted": 1.0847601126035054
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.9857608318328857,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.763790726661682,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8760858297348022,
                  "rejected_mean_error": 3.678272175788879,
                  "gap_rejected_minus_accepted": 1.802186346054077
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9805837869644165,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6742783868312836,
                  "rejected_mean_error": 2.9789864456653596,
                  "gap_rejected_minus_accepted": 1.304708058834076
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.662588655948639,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.529696125984192,
                  "rejected_mean_error": 2.5922778463363647,
                  "gap_rejected_minus_accepted": 1.0625817203521728
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 74,
        "best_calib_loss": 0.011770201846957207,
        "train_time_sec": 29.126551628112793,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994944020882442,
              "spearman": 0.9984459974417365,
              "auroc_top30_bad": 0.9995911428571429,
              "mae": 0.041037533845818146,
              "mse": 0.003520956538167671,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7947814106901572,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0028028707355260848
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17405936083197593
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4779323050290346
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8174871368428072
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999575893585486,
              "spearman": 0.9991333155173326,
              "auroc_top30_worst": 0.9991321904761905,
              "pairwise_seed_ranking": 0.9564,
              "predicted_best_mean_error": 1.6855258285999297,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.07381247502565391,
              "gap_to_oracle": 0.00046201753616315067,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6088975235819817
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8471621457338333
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1104462612748147
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.336936136476199
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9652429819107065,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.497635279874007,
                  "rejected_mean_error": 4.0083356614112855,
                  "gap_rejected_minus_accepted": 2.5107003815372786
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.07196444272995,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.336936136476199,
                  "rejected_mean_error": 2.9840128626823423,
                  "gap_rejected_minus_accepted": 1.6470767262061434
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.643350064754486,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1104462612748147,
                  "rejected_mean_error": 2.386964374780655,
                  "gap_rejected_minus_accepted": 1.27651811350584
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1753893196582794,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8471621457338333,
                  "rejected_mean_error": 2.0492197087923687,
                  "gap_rejected_minus_accepted": 1.2020575630585353
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.971537804603577,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.508043487932947,
                  "rejected_mean_error": 4.020991644859314,
                  "gap_rejected_minus_accepted": 2.5129481569263667
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0721410512924194,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3474155938625336,
                  "rejected_mean_error": 2.995106432914734,
                  "gap_rejected_minus_accepted": 1.6476908390522005
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6571881175041199,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1170208455324173,
                  "rejected_mean_error": 2.40165576171875,
                  "gap_rejected_minus_accepted": 1.2846349161863329
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1885688304901123,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8506369335651398,
                  "rejected_mean_error": 2.062238760312398,
                  "gap_rejected_minus_accepted": 1.2116018267472584
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.98218418332726,
              "spearman": 0.9778474664763334,
              "auroc_top30_bad": 0.9966857142857143,
              "mae": 0.11475105037517096,
              "mse": 0.028832342719065922,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7095961883388132,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08203720381855964
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19625274760723113
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4192311535477638
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8019532250165939
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9668440328505282,
              "spearman": 0.9855553300194113,
              "auroc_top30_worst": 0.9885165714285714,
              "pairwise_seed_ranking": 0.934,
              "predicted_best_mean_error": 1.589657555103302,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.10090258657932272,
              "gap_to_oracle": 0.0011300736665726951,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5365738830566407
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7553747439613709
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1150705285072327
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3863170223830859
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.517769145965577,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5404371278021072,
                  "rejected_mean_error": 2.8210064105987547,
                  "gap_rejected_minus_accepted": 1.2805692827966475
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.03581702709198,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3854793362963542,
                  "rejected_mean_error": 2.5157298146726226,
                  "gap_rejected_minus_accepted": 1.1302504783762684
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5935389995574951,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1150705285072327,
                  "rejected_mean_error": 2.221917583656311,
                  "gap_rejected_minus_accepted": 1.1068470551490786
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0498628914356232,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.756218385582153,
                  "rejected_mean_error": 1.9732350217876211,
                  "gap_rejected_minus_accepted": 1.217016636205468
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.539932036399841,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.55591615902053,
                  "rejected_mean_error": 2.9023559856414796,
                  "gap_rejected_minus_accepted": 1.3464398266209496
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0483410954475403,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.403711914538062,
                  "rejected_mean_error": 2.5419985301910883,
                  "gap_rejected_minus_accepted": 1.1382866156530262
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5887173414230347,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.13279434132576,
                  "rejected_mean_error": 2.24832594203949,
                  "gap_rejected_minus_accepted": 1.11553160071373
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0891034007072449,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7694993023834531,
                  "rejected_mean_error": 2.0008640608048056,
                  "gap_rejected_minus_accepted": 1.2313647584213525
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9849373916097932,
              "spearman": 0.9813019433448316,
              "auroc_top30_bad": 0.9909554285714285,
              "mae": 0.10030598146191641,
              "mse": 0.020540100582690353,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7439514705998823,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07093826347589492
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1835459119439125
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5391141960084438
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9436709032654762
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9673086774512776,
              "spearman": 0.9739062739880153,
              "auroc_top30_worst": 0.9879893333333333,
              "pairwise_seed_ranking": 0.9428,
              "predicted_best_mean_error": 1.7598732991218566,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.10702082300186166,
              "gap_to_oracle": 0.0018389680385588747,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8752084431648255
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1787580968095706
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.451484983730316
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6359619259961378
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.378758788108826,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7541381661627027,
                  "rejected_mean_error": 2.5465561752319337,
                  "gap_rejected_minus_accepted": 0.792418009069231
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.176030457019806,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.635407999905349,
                  "rejected_mean_error": 2.426030871967157,
                  "gap_rejected_minus_accepted": 0.790622872061808
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9031667709350586,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.451484983730316,
                  "rejected_mean_error": 2.2152749504089355,
                  "gap_rejected_minus_accepted": 0.7637899666786194
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4741386473178864,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.17975100522605,
                  "rejected_mean_error": 2.051721338528579,
                  "gap_rejected_minus_accepted": 0.871970333302529
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.446147084236145,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7774217722151016,
                  "rejected_mean_error": 2.6721452713012694,
                  "gap_rejected_minus_accepted": 0.8947234990861679
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2361549139022827,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.64810793540057,
                  "rejected_mean_error": 2.516307089063856,
                  "gap_rejected_minus_accepted": 0.868199153663286
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9229949116706848,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4656139392852783,
                  "rejected_mean_error": 2.2681743049621583,
                  "gap_rejected_minus_accepted": 0.80256036567688
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.514315128326416,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.189549900236584,
                  "rejected_mean_error": 2.0950903038290094,
                  "gap_rejected_minus_accepted": 0.9055404035924255
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9901980859171686,
              "spearman": 0.9864413852842028,
              "auroc_top30_bad": 0.9919392857142856,
              "mae": 0.10808651927449932,
              "mse": 0.02478212599870197,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.924715405085182,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07840810462832451
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19920679619908332
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7035476266145706
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.084665633360545
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9858971705460781,
              "spearman": 0.982918774918775,
              "auroc_top30_worst": 0.9922904761904762,
              "pairwise_seed_ranking": 0.893,
              "predicted_best_mean_error": 2.244864439070225,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.0817679771780968,
              "gap_to_oracle": 0.0034539145231247126,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3059061217308043
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4870447397232056
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6583743109703064
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.865737287680308
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.948216438293457,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.095821299155553,
                  "rejected_mean_error": 4.344819195270539,
                  "gap_rejected_minus_accepted": 2.2489978961149855
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6670116782188416,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.865737287680308,
                  "rejected_mean_error": 3.6856724920272828,
                  "gap_rejected_minus_accepted": 1.8199352043469748
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0623621940612793,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6583743109703064,
                  "rejected_mean_error": 2.983067866563797,
                  "gap_rejected_minus_accepted": 1.3246935555934904
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7024131417274475,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4870447397232056,
                  "rejected_mean_error": 2.5986132051150004,
                  "gap_rejected_minus_accepted": 1.1115684653917948
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.9132122039794917,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.658177435398102,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8736931991577148,
                  "rejected_mean_error": 3.685450067520142,
                  "gap_rejected_minus_accepted": 1.811756868362427
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.064077615737915,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6736064100265502,
                  "rejected_mean_error": 2.979658422470093,
                  "gap_rejected_minus_accepted": 1.3060520124435426
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7298353910446167,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5007981991767883,
                  "rejected_mean_error": 2.6019104886054993,
                  "gap_rejected_minus_accepted": 1.101112289428711
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      }
    ],
    "target_chunk_min_l2_K5": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 67,
        "best_calib_loss": 0.06641969829797745,
        "train_time_sec": 10.871607065200806,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9816147413794141,
              "spearman": 0.9422874642531148,
              "auroc_top30_bad": 0.9993636190476191,
              "mae": 0.10148551031347597,
              "mse": 0.0339363584227864,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.507,
              "expert_lt_simvla_seed0": 0.961,
              "same_context_pred_std": 0.7429671252875321,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2973112899959087
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31848224927708507
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45988013591177296
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7919545972307989
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2083991026848904
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9990226710630833,
              "spearman": 0.9986990769478694,
              "auroc_top30_worst": 0.999011619047619,
              "pairwise_seed_ranking": 0.8658,
              "predicted_best_mean_error": 1.6631152266860008,
              "seed0_mean_error": 1.7301399188935758,
              "random_seed_mean_error": 1.719811507731676,
              "oracle_best_mean_error": 1.658122716575861,
              "improvement_over_seed0": 0.06702469220757501,
              "gap_to_oracle": 0.004992510110139792,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5594481525421142
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7987991519451141
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.068895714879036
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3020831681410472
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7197170986533166
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8195489645004277,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4664314337174098,
                  "rejected_mean_error": 3.999288083076477,
                  "gap_rejected_minus_accepted": 2.5328566493590676
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9806495308876038,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3020831681410472,
                  "rejected_mean_error": 2.9726188901901245,
                  "gap_rejected_minus_accepted": 1.6705357220490773
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5771207213401794,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.068895714879036,
                  "rejected_mean_error": 2.3705384824275972,
                  "gap_rejected_minus_accepted": 1.3016427675485613
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1215699017047882,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7987991519451141,
                  "rejected_mean_error": 2.0266897475560506,
                  "gap_rejected_minus_accepted": 1.2278905956109365
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8230844020843513,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4765959200263024,
                  "rejected_mean_error": 4.012035908699036,
                  "gap_rejected_minus_accepted": 2.5354399886727337
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.002125859260559,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3120410298903784,
                  "rejected_mean_error": 2.984436585903168,
                  "gap_rejected_minus_accepted": 1.6723955560127894
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5876678824424744,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0753996068835259,
                  "rejected_mean_error": 2.3848802309036254,
                  "gap_rejected_minus_accepted": 1.3094806240200996
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1348030269145966,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8011606425046921,
                  "rejected_mean_error": 2.0397996776898704,
                  "gap_rejected_minus_accepted": 1.2386390351851784
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8233701137542632,
              "spearman": 0.84770202073306,
              "auroc_top30_bad": 0.9293942857142857,
              "mae": 0.36299505487680434,
              "mse": 0.2732699304462199,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.468,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.6788605074831854,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3300596471428871
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.38041522740125655
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5166093414306641
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8787372689882914
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2194438674449921
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6296191451222365,
              "spearman": 0.7029877661361704,
              "auroc_top30_worst": 0.8552868571428571,
              "pairwise_seed_ranking": 0.7956,
              "predicted_best_mean_error": 1.6624643959999084,
              "seed0_mean_error": 1.7495110768079758,
              "random_seed_mean_error": 1.7313665192127228,
              "oracle_best_mean_error": 1.6478551789522171,
              "improvement_over_seed0": 0.08704668080806743,
              "gap_to_oracle": 0.014609217047691248,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9108707013130188
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.007043370260642
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2675428958892823
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4807905674870334
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7276662902355193
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6702233791351317,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.663341213385264,
                  "rejected_mean_error": 2.3065919818878173,
                  "gap_rejected_minus_accepted": 0.6432507685025532
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9573749005794525,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4801806555613637,
                  "rejected_mean_error": 2.4685418164006436,
                  "gap_rejected_minus_accepted": 0.9883611608392799
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5699931979179382,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2675428958892823,
                  "rejected_mean_error": 2.1877896845817566,
                  "gap_rejected_minus_accepted": 0.9202467886924743
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9223614484071732,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0098164487189758,
                  "rejected_mean_error": 1.967460314135923,
                  "gap_rejected_minus_accepted": 0.9576438654169472
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.712331557273864,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6836881901158227,
                  "rejected_mean_error": 2.3419170570373535,
                  "gap_rejected_minus_accepted": 0.6582288669215308
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0411017537117004,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5097640253962044,
                  "rejected_mean_error": 2.4611412135381547,
                  "gap_rejected_minus_accepted": 0.9513771881419504
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.605276107788086,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2810881178379059,
                  "rejected_mean_error": 2.2179340357780455,
                  "gap_rejected_minus_accepted": 0.9368459179401396
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9212326407432556,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0410775367229703,
                  "rejected_mean_error": 1.9881811999382182,
                  "gap_rejected_minus_accepted": 0.9471036632152479
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8761996720216663,
              "spearman": 0.8506025351679465,
              "auroc_top30_bad": 0.9267725714285715,
              "mae": 0.30256221695542335,
              "mse": 0.18019930810734977,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.492,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.6957268393019883,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3579357900619507
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.41367706890106204
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6195564440011978
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0301266290267308
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3105179348289966
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7093148732542112,
              "spearman": 0.708331396820094,
              "auroc_top30_worst": 0.7955047619047618,
              "pairwise_seed_ranking": 0.7952,
              "predicted_best_mean_error": 1.83643203496933,
              "seed0_mean_error": 1.9260229082107545,
              "random_seed_mean_error": 1.8919984726905823,
              "oracle_best_mean_error": 1.8184930961132049,
              "improvement_over_seed0": 0.08959087324142456,
              "gap_to_oracle": 0.017938938856125075,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0800362215042114
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3264041073047197
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5964629377365112
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7658461486734052
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8931304200649262
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1801404476165773,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.837207458443112,
                  "rejected_mean_error": 2.3964370746612547,
                  "gap_rejected_minus_accepted": 0.5592296162181427
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0411001443862915,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7656884085915767,
                  "rejected_mean_error": 2.274642128533068,
                  "gap_rejected_minus_accepted": 0.5089537199414911
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.72505521774292,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5964629377365112,
                  "rejected_mean_error": 2.189797902393341,
                  "gap_rejected_minus_accepted": 0.5933349646568298
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3455315828323364,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.327699419789421,
                  "rejected_mean_error": 2.082009718982998,
                  "gap_rejected_minus_accepted": 0.7543102991935768
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.247659707069397,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.862757723066542,
                  "rejected_mean_error": 2.495409574508667,
                  "gap_rejected_minus_accepted": 0.6326518514421249
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0465425848960876,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7770162247081491,
                  "rejected_mean_error": 2.3683125878137257,
                  "gap_rejected_minus_accepted": 0.5912963631055765
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.739503562450409,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.619632272720337,
                  "rejected_mean_error": 2.232413543701172,
                  "gap_rejected_minus_accepted": 0.6127812709808349
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.371068000793457,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.335693255303398,
                  "rejected_mean_error": 2.124904021222324,
                  "gap_rejected_minus_accepted": 0.7892107659189258
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8784591887326026,
              "spearman": 0.8525863021717583,
              "auroc_top30_bad": 0.9327119047619048,
              "mae": 0.39844927725940943,
              "mse": 0.3243553636591662,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.475,
              "expert_lt_simvla_seed0": 0.985,
              "same_context_pred_std": 0.7411475307032483,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.45681020587682725
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5283284396529198
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8090911643803119
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1309422658979893
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8524819791645619,
              "spearman": 0.7702236982236982,
              "auroc_top30_worst": 0.8677952380952381,
              "pairwise_seed_ranking": 0.7645,
              "predicted_best_mean_error": 2.255044920742512,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07158749550580978,
              "gap_to_oracle": 0.013634396195411735,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4739098823070527
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7344870676994324
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7994795298576356
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8748857108751933
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.248918175697327,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.141214405298233,
                  "rejected_mean_error": 3.9362812399864198,
                  "gap_rejected_minus_accepted": 1.7950668346881868
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3038447499275208,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8748857108751933,
                  "rejected_mean_error": 3.658227222442627,
                  "gap_rejected_minus_accepted": 1.7833415115674338
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7203574776649475,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7994795298576356,
                  "rejected_mean_error": 2.841962647676468,
                  "gap_rejected_minus_accepted": 1.0424831178188325
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3408390879631042,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7344870676994324,
                  "rejected_mean_error": 2.516132429122925,
                  "gap_rejected_minus_accepted": 0.7816453614234926
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2730851411819453,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1488088766733804,
                  "rejected_mean_error": 3.9270442724227905,
                  "gap_rejected_minus_accepted": 1.7782353957494101
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.324476659297943,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.88446004708608,
                  "rejected_mean_error": 3.6531495237350464,
                  "gap_rejected_minus_accepted": 1.7686894766489665
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7456024885177612,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8188675403594972,
                  "rejected_mean_error": 2.834397292137146,
                  "gap_rejected_minus_accepted": 1.015529751777649
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3629405796527863,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7674706888198852,
                  "rejected_mean_error": 2.513019658724467,
                  "gap_rejected_minus_accepted": 0.7455489699045816
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K5"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 78,
        "best_calib_loss": 0.020844420418143272,
        "train_time_sec": 35.013065576553345,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997964191943398,
              "spearman": 0.9992908969808283,
              "auroc_top30_bad": 0.9997968571428572,
              "mae": 0.01597339686412597,
              "mse": 0.0004157322847504737,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7558293124340647,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.060756514989188874
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.190328904354712
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45487079314596485
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7915093132774501
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2083991026848904
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998660355533969,
              "spearman": 0.9997413117176401,
              "auroc_top30_worst": 0.9998878095238095,
              "pairwise_seed_ranking": 0.9422,
              "predicted_best_mean_error": 1.659154795885086,
              "seed0_mean_error": 1.7301399188935758,
              "random_seed_mean_error": 1.719811507731676,
              "oracle_best_mean_error": 1.658122716575861,
              "improvement_over_seed0": 0.07098512300848969,
              "gap_to_oracle": 0.001032079309225109,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5582425400018692
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7975677191257476
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0684039905309677
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3017724702040354
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7197170986533166
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8756038427352926,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4663996455801858,
                  "rejected_mean_error": 3.999574176311493,
                  "gap_rejected_minus_accepted": 2.533174530731307
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9983771443367004,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3017724702040354,
                  "rejected_mean_error": 2.9735509840011596,
                  "gap_rejected_minus_accepted": 1.6717785137971242
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5767545104026794,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0684039905309677,
                  "rejected_mean_error": 2.3710302067756652,
                  "gap_rejected_minus_accepted": 1.3026262162446975
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1283907294273376,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7975677191257476,
                  "rejected_mean_error": 2.0271002251625063,
                  "gap_rejected_minus_accepted": 1.2295325060367586
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8609118700027474,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4765525527464018,
                  "rejected_mean_error": 4.01242621421814,
                  "gap_rejected_minus_accepted": 2.535873661471738
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0062605142593384,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3118993060986202,
                  "rejected_mean_error": 2.984861757278442,
                  "gap_rejected_minus_accepted": 1.672962451179822
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5863376259803772,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.074849450290203,
                  "rejected_mean_error": 2.3854303874969482,
                  "gap_rejected_minus_accepted": 1.3105809372067452
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1377678513526917,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7999825109243393,
                  "rejected_mean_error": 2.0401923882166546,
                  "gap_rejected_minus_accepted": 1.2402098772923154
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9621784534128244,
              "spearman": 0.9682468609329509,
              "auroc_top30_bad": 0.9878194285714286,
              "mae": 0.15831587993949653,
              "mse": 0.06675905659711272,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7157895490504081,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14740148836374284
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23489365558624267
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45963958942890165
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8421928937276204
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2194438674449921
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9277490998621709,
              "spearman": 0.9682201642369052,
              "auroc_top30_worst": 0.9791024761904762,
              "pairwise_seed_ranking": 0.9308,
              "predicted_best_mean_error": 1.649945806145668,
              "seed0_mean_error": 1.7495110768079758,
              "random_seed_mean_error": 1.7313665192127228,
              "oracle_best_mean_error": 1.6478551789522171,
              "improvement_over_seed0": 0.0995652706623078,
              "gap_to_oracle": 0.002090627193450878,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47284894275665285
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7634989936382343
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1395911316871643
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4189398607084238
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7276662902355193
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5256010055542,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.591326830069224,
                  "rejected_mean_error": 2.9547214317321777,
                  "gap_rejected_minus_accepted": 1.3633946016629537
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.042404353618622,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.41758300788629,
                  "rejected_mean_error": 2.6559347744566946,
                  "gap_rejected_minus_accepted": 1.2383517665704045
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.685662031173706,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1395911316871643,
                  "rejected_mean_error": 2.3157414487838746,
                  "gap_rejected_minus_accepted": 1.1761503170967103
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.076745480298996,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7645272896312677,
                  "rejected_mean_error": 2.0493978880894477,
                  "gap_rejected_minus_accepted": 1.28487059845818
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5370489358901978,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.60388433125284,
                  "rejected_mean_error": 3.0601517868041994,
                  "gap_rejected_minus_accepted": 1.4562674555513595
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0893675088882446,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4324170349434735,
                  "rejected_mean_error": 2.6907267248819746,
                  "gap_rejected_minus_accepted": 1.2583096899385011
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7217910289764404,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1570596406459808,
                  "rejected_mean_error": 2.3419625129699706,
                  "gap_rejected_minus_accepted": 1.1849028723239898
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0916085541248322,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7749293224206046,
                  "rejected_mean_error": 2.0778461063609406,
                  "gap_rejected_minus_accepted": 1.302916783940336
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9695068278215935,
              "spearman": 0.9658343908151161,
              "auroc_top30_bad": 0.9751740952380952,
              "mae": 0.15067326435931028,
              "mse": 0.04641462542304156,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7480469749776021,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12754711973667146
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24522228894233702
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5681639816880226
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9854108866135279
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3105179348289966
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9019501805017398,
              "spearman": 0.9178218891660092,
              "auroc_top30_worst": 0.9361219047619047,
              "pairwise_seed_ranking": 0.9072,
              "predicted_best_mean_error": 1.8217877640724183,
              "seed0_mean_error": 1.9260229082107545,
              "random_seed_mean_error": 1.8919984726905823,
              "oracle_best_mean_error": 1.8184930961132049,
              "improvement_over_seed0": 0.10423514413833623,
              "gap_to_oracle": 0.0032946679592134043,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8849613938331604
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2139159985459769
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5086830471992492
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.708479705713451
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8931304200649262
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.375944828987122,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8156264429622226,
                  "rejected_mean_error": 2.590666213989258,
                  "gap_rejected_minus_accepted": 0.7750397710270354
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.137861430644989,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.707853088574832,
                  "rejected_mean_error": 2.447778533822812,
                  "gap_rejected_minus_accepted": 0.7399254452479802
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8683319091796875,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5086830471992492,
                  "rejected_mean_error": 2.277577792930603,
                  "gap_rejected_minus_accepted": 0.7688947457313537
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.475475698709488,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2162392632648968,
                  "rejected_mean_error": 2.119242407341777,
                  "gap_rejected_minus_accepted": 0.9030031440768802
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4538676738739014,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.841288079155816,
                  "rejected_mean_error": 2.6886363697052,
                  "gap_rejected_minus_accepted": 0.8473482905493841
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.143313407897949,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7145363009549717,
                  "rejected_mean_error": 2.5537688694302996,
                  "gap_rejected_minus_accepted": 0.8392325684753279
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.892547607421875,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5209547834396362,
                  "rejected_mean_error": 2.3310910329818726,
                  "gap_rejected_minus_accepted": 0.8101362495422364
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4928658306598663,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2145972762789046,
                  "rejected_mean_error": 2.1657010622840516,
                  "gap_rejected_minus_accepted": 0.951103786005147
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9881311043655964,
              "spearman": 0.9869155723014097,
              "auroc_top30_bad": 0.9927464285714286,
              "mae": 0.12067813033331186,
              "mse": 0.03129955853552804,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9036562426110418,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06569699458777904
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21677949929237367
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7046781004667282
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0826769536336263
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9818481509557466,
              "spearman": 0.9887284247284247,
              "auroc_top30_worst": 0.9926333333333333,
              "pairwise_seed_ranking": 0.886,
              "predicted_best_mean_error": 2.243642435371876,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08298998087644582,
              "gap_to_oracle": 0.002231910824775696,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2954313659667969
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4821722497940064
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6547603936195374
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8762352840105692
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8977156162261966,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.095265774594413,
                  "rejected_mean_error": 4.3498189163208005,
                  "gap_rejected_minus_accepted": 2.2545531417263875
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6046494841575623,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8762352840105692,
                  "rejected_mean_error": 3.654178503036499,
                  "gap_rejected_minus_accepted": 1.7779432190259299
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.054421305656433,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6547603936195374,
                  "rejected_mean_error": 2.986681783914566,
                  "gap_rejected_minus_accepted": 1.3319213902950287
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7168073058128357,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4821722497940064,
                  "rejected_mean_error": 2.6002373684247333,
                  "gap_rejected_minus_accepted": 1.1180651186307269
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8989097356796263,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.612832248210907,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8902548027038575,
                  "rejected_mean_error": 3.635765256881714,
                  "gap_rejected_minus_accepted": 1.7455104541778563
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0623421669006348,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6712451195716858,
                  "rejected_mean_error": 2.9820197129249575,
                  "gap_rejected_minus_accepted": 1.3107745933532717
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.727175772190094,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4963640284538269,
                  "rejected_mean_error": 2.603388545513153,
                  "gap_rejected_minus_accepted": 1.1070245170593263
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K5"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 80,
        "best_calib_loss": 0.02034200169146061,
        "train_time_sec": 41.44338798522949,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993906952672369,
              "spearman": 0.9982415996692462,
              "auroc_top30_bad": 0.9996700476190477,
              "mae": 0.036065701308252755,
              "mse": 0.002294026083738907,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7654106938218913,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06254579341819044
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19077171129002235
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4550538976133568
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7916596114278305
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2083991026848904
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999518086793981,
              "spearman": 0.9990572938582238,
              "auroc_top30_worst": 0.9993672380952381,
              "pairwise_seed_ranking": 0.9561,
              "predicted_best_mean_error": 1.659078278928995,
              "seed0_mean_error": 1.7301399188935758,
              "random_seed_mean_error": 1.719811507731676,
              "oracle_best_mean_error": 1.658122716575861,
              "improvement_over_seed0": 0.0710616399645807,
              "gap_to_oracle": 0.0009555623531340984,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5589357278347016
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7980948313236237
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0687439306497575
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3019859420617421
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7197170986533166
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.910379219055178,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4664427136182785,
                  "rejected_mean_error": 3.9991865639686583,
                  "gap_rejected_minus_accepted": 2.53274385035038
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0337018966674805,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3019859420617421,
                  "rejected_mean_error": 2.9729105684280395,
                  "gap_rejected_minus_accepted": 1.6709246263662973
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.591838300228119,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0687439306497575,
                  "rejected_mean_error": 2.3706902666568754,
                  "gap_rejected_minus_accepted": 1.301946336007118
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1333390176296234,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7980948313236237,
                  "rejected_mean_error": 2.0269245210965474,
                  "gap_rejected_minus_accepted": 1.2288296897729238
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.909955859184266,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4765525527464018,
                  "rejected_mean_error": 4.01242621421814,
                  "gap_rejected_minus_accepted": 2.535873661471738
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0462194085121155,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3120142678817113,
                  "rejected_mean_error": 2.9845168719291686,
                  "gap_rejected_minus_accepted": 1.6725026040474573
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6079204082489014,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0749789463877677,
                  "rejected_mean_error": 2.3853008913993836,
                  "gap_rejected_minus_accepted": 1.310321945011616
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.142007738351822,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8000226100683212,
                  "rejected_mean_error": 2.040179021835327,
                  "gap_rejected_minus_accepted": 1.2401564117670059
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9718522470423254,
              "spearman": 0.9656060433990702,
              "auroc_top30_bad": 0.9947321904761904,
              "mae": 0.1605852478680201,
              "mse": 0.05387642987961488,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7019908014196061,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.18871836864948272
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2524319852352142
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4577199832201004
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8366470238367717
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2194438674449921
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9635932917455663,
              "spearman": 0.9835154777059059,
              "auroc_top30_worst": 0.983911619047619,
              "pairwise_seed_ranking": 0.93,
              "predicted_best_mean_error": 1.649389432668686,
              "seed0_mean_error": 1.7495110768079758,
              "random_seed_mean_error": 1.7313665192127228,
              "oracle_best_mean_error": 1.6478551789522171,
              "improvement_over_seed0": 0.10012164413928981,
              "gap_to_oracle": 0.0015342537164688697,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47046034908294676
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.755685741893756
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.132747675037384
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4129437001656369
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7276662902355193
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5485866785049445,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5699903055297004,
                  "rejected_mean_error": 3.1467501525878907,
                  "gap_rejected_minus_accepted": 1.5767598470581903
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0776273608207703,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4121057233408396,
                  "rejected_mean_error": 2.6723316294697526,
                  "gap_rejected_minus_accepted": 1.260225906128913
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5362019538879395,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.132747675037384,
                  "rejected_mean_error": 2.3225849054336547,
                  "gap_rejected_minus_accepted": 1.1898372303962708
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0089960992336273,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7571019800707174,
                  "rejected_mean_error": 2.05187827431405,
                  "gap_rejected_minus_accepted": 1.2947762942433325
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.552899956703186,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5855842122766706,
                  "rejected_mean_error": 3.2248528575897217,
                  "gap_rejected_minus_accepted": 1.6392686453130512
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0981951355934143,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4267162879839301,
                  "rejected_mean_error": 2.707647989666651,
                  "gap_rejected_minus_accepted": 1.2809317016827209
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5417141914367676,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1517900817394258,
                  "rejected_mean_error": 2.347232071876526,
                  "gap_rejected_minus_accepted": 1.1954419901371003
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0379423201084137,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7685085151876722,
                  "rejected_mean_error": 2.080009266016955,
                  "gap_rejected_minus_accepted": 1.3115007508292829
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9719111486979143,
              "spearman": 0.9664078522479773,
              "auroc_top30_bad": 0.9836213333333332,
              "mae": 0.1428743680730462,
              "mse": 0.041673216750670476,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7316912009860977,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1418375210762024
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.273664120388031
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5691585394501686
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.980639874625206
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3105179348289966
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9408410349756179,
              "spearman": 0.9517813041800348,
              "auroc_top30_worst": 0.9737752380952381,
              "pairwise_seed_ranking": 0.9212,
              "predicted_best_mean_error": 1.8203428411483764,
              "seed0_mean_error": 1.9260229082107545,
              "random_seed_mean_error": 1.8919984726905823,
              "oracle_best_mean_error": 1.8184930961132049,
              "improvement_over_seed0": 0.10568006706237809,
              "gap_to_oracle": 0.001849745035171546,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8791279349327087
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2021957809726398
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5021238112449646
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6935181924656255
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8931304200649262
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4765111446380614,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8098659476704069,
                  "rejected_mean_error": 2.6425106716156006,
                  "gap_rejected_minus_accepted": 0.8326447239451937
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1850536465644836,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6927643366150058,
                  "rejected_mean_error": 2.4929483759517486,
                  "gap_rejected_minus_accepted": 0.8001840393367428
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8492653965950012,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5021238112449646,
                  "rejected_mean_error": 2.2841370288848877,
                  "gap_rejected_minus_accepted": 0.782013217639923
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4237270057201385,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2031103736295488,
                  "rejected_mean_error": 2.123628044968099,
                  "gap_rejected_minus_accepted": 0.9205176713385503
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.555529975891113,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8300610012478298,
                  "rejected_mean_error": 2.789680070877075,
                  "gap_rejected_minus_accepted": 0.9596190696292453
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.25053334236145,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7072588364708232,
                  "rejected_mean_error": 2.5753702322642007,
                  "gap_rejected_minus_accepted": 0.8681113957933775
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.88827246427536,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.515362386703491,
                  "rejected_mean_error": 2.3366834297180175,
                  "gap_rejected_minus_accepted": 0.8213210430145264
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.437385469675064,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2132037215762668,
                  "rejected_mean_error": 2.1661705486277207,
                  "gap_rejected_minus_accepted": 0.952966827051454
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9874294238120663,
              "spearman": 0.9813598734168696,
              "auroc_top30_bad": 0.992217857142857,
              "mae": 0.12716452409722842,
              "mse": 0.03155201798825774,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8975063530095787,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11062041707336903
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23593897852301599
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7050783340930938
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0852627731959026
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9866647282654881,
              "spearman": 0.9775010215010215,
              "auroc_top30_worst": 0.9951476190476191,
              "pairwise_seed_ranking": 0.904,
              "predicted_best_mean_error": 2.243380312025547,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08325210422277474,
              "gap_to_oracle": 0.001969787478446783,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.313180627822876
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4927982573509215
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.660777391910553
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8626422750155132
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.980863571166992,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.094555504454507,
                  "rejected_mean_error": 4.356211347579956,
                  "gap_rejected_minus_accepted": 2.261655843125449
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.776165544986725,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8626422750155132,
                  "rejected_mean_error": 3.6949575300216675,
                  "gap_rejected_minus_accepted": 1.8323152550061543
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0053569078445435,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.660777391910553,
                  "rejected_mean_error": 2.98066478562355,
                  "gap_rejected_minus_accepted": 1.3198873937129971
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6581006348133087,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4927982573509215,
                  "rejected_mean_error": 2.5966953659057617,
                  "gap_rejected_minus_accepted": 1.1038971085548401
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.973484444618225,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1027985480096607,
                  "rejected_mean_error": 4.341137230396271,
                  "gap_rejected_minus_accepted": 2.23833868238661
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.774878978729248,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8737707551320393,
                  "rejected_mean_error": 3.685217399597168,
                  "gap_rejected_minus_accepted": 1.8114466444651287
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0053569078445435,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6762558686733247,
                  "rejected_mean_error": 2.9770089638233186,
                  "gap_rejected_minus_accepted": 1.300753095149994
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6894018352031708,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5006223797798157,
                  "rejected_mean_error": 2.6019690950711567,
                  "gap_rejected_minus_accepted": 1.101346715291341
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K5"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 57,
        "best_calib_loss": 0.022627001628279686,
        "train_time_sec": 29.187400817871094,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995576300514448,
              "spearman": 0.9986523760275657,
              "auroc_top30_bad": 0.9997426666666667,
              "mae": 0.03130286524445983,
              "mse": 0.0015346402443980618,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7714950324790936,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06104261064936872
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19047656393065118
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4550040396869881
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7915985992869207
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2083991026848904
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996370530682473,
              "spearman": 0.9994175463526599,
              "auroc_top30_worst": 0.9996249523809524,
              "pairwise_seed_ranking": 0.9475,
              "predicted_best_mean_error": 1.6590632778704166,
              "seed0_mean_error": 1.7301399188935758,
              "random_seed_mean_error": 1.719811507731676,
              "oracle_best_mean_error": 1.658122716575861,
              "improvement_over_seed0": 0.07107664102315914,
              "gap_to_oracle": 0.0009405612945556641,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5584458320140838
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7978741169452668
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0685045164823532
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.301813424984614
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7197170986533166
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.905272817611695,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4664088240067163,
                  "rejected_mean_error": 3.9994915704727174,
                  "gap_rejected_minus_accepted": 2.5330827464660013
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.021049439907074,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.301813424984614,
                  "rejected_mean_error": 2.973428119659424,
                  "gap_rejected_minus_accepted": 1.6716146946748098
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.595099925994873,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0685045164823532,
                  "rejected_mean_error": 2.37092968082428,
                  "gap_rejected_minus_accepted": 1.3024251643419267
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.141482651233673,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7978741169452668,
                  "rejected_mean_error": 2.0269980925559996,
                  "gap_rejected_minus_accepted": 1.2291239756107328
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9117102384567266,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4765525527464018,
                  "rejected_mean_error": 4.01242621421814,
                  "gap_rejected_minus_accepted": 2.535873661471738
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0310698747634888,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.311912161151568,
                  "rejected_mean_error": 2.9848231921195985,
                  "gap_rejected_minus_accepted": 1.6729110309680304
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6073696613311768,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0749169084429742,
                  "rejected_mean_error": 2.3853629293441774,
                  "gap_rejected_minus_accepted": 1.3104460209012032
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1531137228012085,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8006819905042648,
                  "rejected_mean_error": 2.0399592283566794,
                  "gap_rejected_minus_accepted": 1.2392772378524146
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9673226750945034,
              "spearman": 0.9693797770483287,
              "auroc_top30_bad": 0.9931230476190477,
              "mae": 0.17101419632779435,
              "mse": 0.06853980176067062,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6915321055527527,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.16925803795456887
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2435233532190323
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.46168538510799406
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.837633029683431
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2194438674449921
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9484847812725063,
              "spearman": 0.980774227409975,
              "auroc_top30_worst": 0.9893485714285714,
              "pairwise_seed_ranking": 0.9386,
              "predicted_best_mean_error": 1.6495375682115554,
              "seed0_mean_error": 1.7495110768079758,
              "random_seed_mean_error": 1.7313665192127228,
              "oracle_best_mean_error": 1.6478551789522171,
              "improvement_over_seed0": 0.0999735085964204,
              "gap_to_oracle": 0.0016823892593382794,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4689499797821045
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7693937520186106
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1326258749961853
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4118575266302267
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7276662902355193
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4574764251708996,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.576799548625946,
                  "rejected_mean_error": 3.0854669647216797,
                  "gap_rejected_minus_accepted": 1.5086674160957336
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9805887341499329,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4112056616530728,
                  "rejected_mean_error": 2.6750260633401597,
                  "gap_rejected_minus_accepted": 1.2638204016870869
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5443719029426575,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1326258749961853,
                  "rejected_mean_error": 2.3227067054748534,
                  "gap_rejected_minus_accepted": 1.190080830478668
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0426334738731384,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7709626755394494,
                  "rejected_mean_error": 2.0472481807369816,
                  "gap_rejected_minus_accepted": 1.2762855051975321
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.477805256843567,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.592400235997306,
                  "rejected_mean_error": 3.163508644104004,
                  "gap_rejected_minus_accepted": 1.5711084081066982
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0127158761024475,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.422007461123288,
                  "rejected_mean_error": 2.721624983681573,
                  "gap_rejected_minus_accepted": 1.2996175225582849
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5712531805038452,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1491621186733245,
                  "rejected_mean_error": 2.349860034942627,
                  "gap_rejected_minus_accepted": 1.2006979162693026
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0584775805473328,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7816098233064016,
                  "rejected_mean_error": 2.0755954563298964,
                  "gap_rejected_minus_accepted": 1.2939856330234947
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9662808438763728,
              "spearman": 0.9612248426455697,
              "auroc_top30_bad": 0.9834262857142858,
              "mae": 0.15910229685544036,
              "mse": 0.056913178349421306,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7135808766713351,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1656683658361435
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2735574682474136
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5715147342324257
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9822186144272487
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3105179348289966
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9197249333280499,
              "spearman": 0.938278104497987,
              "auroc_top30_worst": 0.96192,
              "pairwise_seed_ranking": 0.9216,
              "predicted_best_mean_error": 1.8198432989120483,
              "seed0_mean_error": 1.9260229082107545,
              "random_seed_mean_error": 1.8919984726905823,
              "oracle_best_mean_error": 1.8184930961132049,
              "improvement_over_seed0": 0.10617960929870618,
              "gap_to_oracle": 0.0013502027988434584,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9008578143119812
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2089730201241298
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4997349146842958
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7104477021358668
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8931304200649262
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2773665428161625,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.814326665825314,
                  "rejected_mean_error": 2.6023642082214353,
                  "gap_rejected_minus_accepted": 0.7880375423961212
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0621140599250793,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7101558022590686,
                  "rejected_mean_error": 2.4408851065955606,
                  "gap_rejected_minus_accepted": 0.730729304336492
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.812246024608612,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4997349146842958,
                  "rejected_mean_error": 2.2865259254455568,
                  "gap_rejected_minus_accepted": 0.786791010761261
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4341029822826385,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2098657740190768,
                  "rejected_mean_error": 2.121371438434564,
                  "gap_rejected_minus_accepted": 0.9115056644154873
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.361301732063293,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8377573023902045,
                  "rejected_mean_error": 2.7204133605957033,
                  "gap_rejected_minus_accepted": 0.8826560582054988
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.083091914653778,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7210981998851593,
                  "rejected_mean_error": 2.534291486891489,
                  "gap_rejected_minus_accepted": 0.8131932870063296
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.835357904434204,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5134544448852538,
                  "rejected_mean_error": 2.3385913715362547,
                  "gap_rejected_minus_accepted": 0.8251369266510009
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4526469707489014,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.220586687799484,
                  "rejected_mean_error": 2.1636832391514496,
                  "gap_rejected_minus_accepted": 0.9430965513519656
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9882030494644444,
              "spearman": 0.9835012528910114,
              "auroc_top30_bad": 0.9922452380952381,
              "mae": 0.12140818471612874,
              "mse": 0.03021915986714604,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.995,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9050912664903693,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08581167623400689
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23412978199124337
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7052407521009445
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.083961253086726
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9859522627440314,
              "spearman": 0.9785811665811666,
              "auroc_top30_worst": 0.9939333333333333,
              "pairwise_seed_ranking": 0.8875,
              "predicted_best_mean_error": 2.244564965069294,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.0820674511790278,
              "gap_to_oracle": 0.0031544405221937133,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3160416650772095
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4948925428390503
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6585723814964295
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8643579471906027
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.9252694606781007,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.095821299155553,
                  "rejected_mean_error": 4.344819195270539,
                  "gap_rejected_minus_accepted": 2.2489978961149855
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6838924288749695,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8643579471906027,
                  "rejected_mean_error": 3.6898105134963988,
                  "gap_rejected_minus_accepted": 1.825452566305796
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0425180196762085,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6585723814964295,
                  "rejected_mean_error": 2.982869796037674,
                  "gap_rejected_minus_accepted": 1.3242974145412445
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6807649433612823,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4948925428390503,
                  "rejected_mean_error": 2.595997270743052,
                  "gap_rejected_minus_accepted": 1.1011047279040018
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.9038771152496334,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.673850357532501,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8761990213394164,
                  "rejected_mean_error": 3.6779326009750366,
                  "gap_rejected_minus_accepted": 1.8017335796356202
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0530405044555664,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6720655429363251,
                  "rejected_mean_error": 2.981199289560318,
                  "gap_rejected_minus_accepted": 1.309133746623993
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.691766083240509,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5122991728782653,
                  "rejected_mean_error": 2.598076830705007,
                  "gap_rejected_minus_accepted": 1.0857776578267415
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K5"
      }
    ],
    "target_chunk_min_l2_K10": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 78,
        "best_calib_loss": 0.0670488104224205,
        "train_time_sec": 11.028903245925903,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9844313575403829,
              "spearman": 0.9430686463456084,
              "auroc_top30_bad": 0.9993034047619048,
              "mae": 0.09478764578286791,
              "mse": 0.02977824907848064,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.49,
              "expert_lt_simvla_seed0": 0.982,
              "same_context_pred_std": 0.7507999342187468,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2702892460525036
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.29722230814262296
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.42438428501121234
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7663741030152111
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.188646869606932
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.998818144275349,
              "spearman": 0.9983267840610711,
              "auroc_top30_worst": 0.9987998095238096,
              "pairwise_seed_ranking": 0.8709,
              "predicted_best_mean_error": 1.6587051635086536,
              "seed0_mean_error": 1.7257746937572955,
              "random_seed_mean_error": 1.7155524998605252,
              "oracle_best_mean_error": 1.6542172869741916,
              "improvement_over_seed0": 0.06706953024864193,
              "gap_to_oracle": 0.004487876534462032,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5517194510698319
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7903004289627075
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0623149359703064
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2970415309906005
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.715404778456688
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8002678632736235,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4619641137917836,
                  "rejected_mean_error": 3.9963707604408265,
                  "gap_rejected_minus_accepted": 2.534406646649043
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9669231176376343,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2970415309906005,
                  "rejected_mean_error": 2.97049452085495,
                  "gap_rejected_minus_accepted": 1.6734529898643493
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.539688527584076,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0623149359703064,
                  "rejected_mean_error": 2.3684946209430695,
                  "gap_rejected_minus_accepted": 1.3061796849727632
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0989190340042114,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7903004289627075,
                  "rejected_mean_error": 2.0237728949546816,
                  "gap_rejected_minus_accepted": 1.2334724659919742
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.799450206756592,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.472095134821203,
                  "rejected_mean_error": 4.0088907241821286,
                  "gap_rejected_minus_accepted": 2.5367955893609255
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.970497965812683,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.307232728679975,
                  "rejected_mean_error": 2.9814005889892576,
                  "gap_rejected_minus_accepted": 1.6741678603092827
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5502318143844604,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0684728675484658,
                  "rejected_mean_error": 2.3830765199661257,
                  "gap_rejected_minus_accepted": 1.3146036524176599
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1141351461410522,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7922751537561417,
                  "rejected_mean_error": 2.036941207091014,
                  "gap_rejected_minus_accepted": 1.2446660533348721
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8257480295856972,
              "spearman": 0.8391532174513479,
              "auroc_top30_bad": 0.9215855238095239,
              "mae": 0.36637920441627503,
              "mse": 0.28557017602196755,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.464,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.6574364757900114,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3687986426055431
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3690372833371162
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5335140677809715
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8745913019895554
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2162184780657292
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.630010645311582,
              "spearman": 0.6825832403092739,
              "auroc_top30_worst": 0.8489813333333334,
              "pairwise_seed_ranking": 0.7888,
              "predicted_best_mean_error": 1.66148792886734,
              "seed0_mean_error": 1.7482785412073136,
              "random_seed_mean_error": 1.7301191527843476,
              "oracle_best_mean_error": 1.6468809620141982,
              "improvement_over_seed0": 0.08679061233997354,
              "gap_to_oracle": 0.01460696685314189,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0695702209472657
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0876081082492302
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2770696640968322
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4711201651645367
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7264184505939484
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3937399864196776,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6685252331097922,
                  "rejected_mean_error": 2.247457407951355,
                  "gap_rejected_minus_accepted": 0.578932174841563
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8624442219734192,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.470347453652222,
                  "rejected_mean_error": 2.4929952050169435,
                  "gap_rejected_minus_accepted": 1.0226477513647214
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.484756886959076,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2770696640968322,
                  "rejected_mean_error": 2.1757672370910646,
                  "gap_rejected_minus_accepted": 0.8986975729942324
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8686407208442688,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0903083166946619,
                  "rejected_mean_error": 1.9389077482572106,
                  "gap_rejected_minus_accepted": 0.8485994315625487
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.410958170890808,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6921962193648021,
                  "rejected_mean_error": 2.253019437789917,
                  "gap_rejected_minus_accepted": 0.5608232184251147
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9161398708820343,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.495410520284571,
                  "rejected_mean_error": 2.498855047755771,
                  "gap_rejected_minus_accepted": 1.0034445274712
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5289716720581055,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2883265316486359,
                  "rejected_mean_error": 2.2082305507659914,
                  "gap_rejected_minus_accepted": 0.9199040191173555
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8586146384477615,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0965738736447834,
                  "rejected_mean_error": 1.9678367981936205,
                  "gap_rejected_minus_accepted": 0.871262924548837
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8664025998702007,
              "spearman": 0.8358675838511221,
              "auroc_top30_bad": 0.9131040000000001,
              "mae": 0.3316332142114639,
              "mse": 0.2114029150776249,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.976,
              "same_context_pred_std": 0.6835509673324834,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.37915937864780425
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.40003274166584013
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6160194224596024
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.041879355398814
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3083135934591292
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6772801555550461,
              "spearman": 0.66768817183243,
              "auroc_top30_worst": 0.7532769523809524,
              "pairwise_seed_ranking": 0.7832,
              "predicted_best_mean_error": 1.8369960687160491,
              "seed0_mean_error": 1.925728751182556,
              "random_seed_mean_error": 1.8916268434524537,
              "oracle_best_mean_error": 1.8181929438114166,
              "improvement_over_seed0": 0.0887326824665069,
              "gap_to_oracle": 0.01880312490463254,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0612181434631347
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3459610870251288
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6051649551391602
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7796457860388482
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8927852801799774
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1239694595336918,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.843321418179406,
                  "rejected_mean_error": 2.3379600381851198,
                  "gap_rejected_minus_accepted": 0.4946386200057138
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9306627810001373,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7788070751356087,
                  "rejected_mean_error": 2.2339916000731836,
                  "gap_rejected_minus_accepted": 0.455184524937575
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6651676297187805,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6051649551391602,
                  "rejected_mean_error": 2.1804056052207947,
                  "gap_rejected_minus_accepted": 0.5752406500816345
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2708792090415955,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3474534631918034,
                  "rejected_mean_error": 2.0749505509561765,
                  "gap_rejected_minus_accepted": 0.7274970877643732
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1554319620132447,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.869064499007331,
                  "rejected_mean_error": 2.4357070207595823,
                  "gap_rejected_minus_accepted": 0.5666425217522513
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9551335871219635,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7855284679382242,
                  "rejected_mean_error": 2.341878798272875,
                  "gap_rejected_minus_accepted": 0.5563503303346506
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.678931713104248,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6123393402099608,
                  "rejected_mean_error": 2.2391181621551515,
                  "gap_rejected_minus_accepted": 0.6267788219451906
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3116801083087921,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3472643447300745,
                  "rejected_mean_error": 2.120612481698633,
                  "gap_rejected_minus_accepted": 0.7733481369685584
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8895894171972142,
              "spearman": 0.8590830145734131,
              "auroc_top30_bad": 0.9293321428571428,
              "mae": 0.3908986723050475,
              "mse": 0.30596723332691,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.51,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7640958315130798,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4361163894087076
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.48084057864546775
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7808566063195467
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.133864421715339
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8606724254907038,
              "spearman": 0.7522074562074563,
              "auroc_top30_worst": 0.8521619047619047,
              "pairwise_seed_ranking": 0.757,
              "predicted_best_mean_error": 2.254332695901394,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07229972034692755,
              "gap_to_oracle": 0.012922171354293965,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4194523644447328
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7199653596878053
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8225638103485107
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8778942580223084
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.453978824615479,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.1396085880862343,
                  "rejected_mean_error": 3.9507335948944093,
                  "gap_rejected_minus_accepted": 1.811125006808175
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2180280685424805,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8778942580223084,
                  "rejected_mean_error": 3.649201581001282,
                  "gap_rejected_minus_accepted": 1.7713073229789735
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6881192326545715,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.8225638103485107,
                  "rejected_mean_error": 2.818878367185593,
                  "gap_rejected_minus_accepted": 0.9963145568370821
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3164141476154327,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7199653596878053,
                  "rejected_mean_error": 2.5209729984601337,
                  "gap_rejected_minus_accepted": 0.8010076387723284
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4737989425659177,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1488088766733804,
                  "rejected_mean_error": 3.9270442724227905,
                  "gap_rejected_minus_accepted": 1.7782353957494101
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2173308730125427,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8897308063507081,
                  "rejected_mean_error": 3.637337245941162,
                  "gap_rejected_minus_accepted": 1.747606439590454
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7194722890853882,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.840899189710617,
                  "rejected_mean_error": 2.812365642786026,
                  "gap_rejected_minus_accepted": 0.9714664530754089
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3449482023715973,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7316044425964356,
                  "rejected_mean_error": 2.5249750741322834,
                  "gap_rejected_minus_accepted": 0.7933706315358477
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 73,
        "best_calib_loss": 0.021121172234416008,
        "train_time_sec": 35.200661182403564,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995952937742658,
              "spearman": 0.9988786218490733,
              "auroc_top30_bad": 0.9996616666666667,
              "mae": 0.03182866780326003,
              "mse": 0.001562405711161326,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7846323043244712,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06017933824693318
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17699905882342717
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4210543114089174
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7658897218322226
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.188646869606932
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997108228080491,
              "spearman": 0.999483228715329,
              "auroc_top30_worst": 0.9997977142857143,
              "pairwise_seed_ranking": 0.9457,
              "predicted_best_mean_error": 1.6552389026284218,
              "seed0_mean_error": 1.7257746937572955,
              "random_seed_mean_error": 1.7155524998605252,
              "oracle_best_mean_error": 1.6542172869741916,
              "improvement_over_seed0": 0.07053579112887376,
              "gap_to_oracle": 0.0010216156542302013,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5506357746124267
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7899693910598755
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0614366287708283
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.296433961836497
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.715404778456688
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8940781354904184,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4617645092805227,
                  "rejected_mean_error": 3.9981672010421754,
                  "gap_rejected_minus_accepted": 2.5364026917616527
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0219202637672424,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.296433961836497,
                  "rejected_mean_error": 2.9723172283172605,
                  "gap_rejected_minus_accepted": 1.6758832664807635
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.60416179895401,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0614366287708283,
                  "rejected_mean_error": 2.3693729281425475,
                  "gap_rejected_minus_accepted": 1.3079362993717192
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.138628363609314,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7899693910598755,
                  "rejected_mean_error": 2.023883240922292,
                  "gap_rejected_minus_accepted": 1.2339138498624165
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.89828999042511,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4719050511055523,
                  "rejected_mean_error": 4.010601477622986,
                  "gap_rejected_minus_accepted": 2.5386964265174337
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0371541380882263,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.306405320684115,
                  "rejected_mean_error": 2.9838828129768373,
                  "gap_rejected_minus_accepted": 1.6774774922927222
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6130446195602417,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0677838593125344,
                  "rejected_mean_error": 2.3837655282020567,
                  "gap_rejected_minus_accepted": 1.3159816688895223
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.154875099658966,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.792315781712532,
                  "rejected_mean_error": 2.0369276644388834,
                  "gap_rejected_minus_accepted": 1.2446118827263515
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9649581791992397,
              "spearman": 0.961813189488449,
              "auroc_top30_bad": 0.9887497142857143,
              "mae": 0.16201900355890395,
              "mse": 0.058006138593369304,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.972,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7506107421066701,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17672679993510246
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24709822845458984
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45534011319875717
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8370120138883591
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2162184780657292
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9393619580632226,
              "spearman": 0.9678293134267607,
              "auroc_top30_worst": 0.9754179047619047,
              "pairwise_seed_ranking": 0.9392,
              "predicted_best_mean_error": 1.648055770635605,
              "seed0_mean_error": 1.7482785412073136,
              "random_seed_mean_error": 1.7301191527843476,
              "oracle_best_mean_error": 1.6468809620141982,
              "improvement_over_seed0": 0.1002227705717087,
              "gap_to_oracle": 0.001174808621406731,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46804126930236817
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7617548438601005
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.133766009235382
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4186446133580035
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7264184505939484
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6475383520126354,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5815364713139004,
                  "rejected_mean_error": 3.03035626411438,
                  "gap_rejected_minus_accepted": 1.4488197928004796
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1171128153800964,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4172782272641153,
                  "rejected_mean_error": 2.651863783693161,
                  "gap_rejected_minus_accepted": 1.2345855564290458
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6637976169586182,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.133766009235382,
                  "rejected_mean_error": 2.3190708919525145,
                  "gap_rejected_minus_accepted": 1.1853048827171324
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1198962330818176,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7625564079695997,
                  "rejected_mean_error": 2.048391576892157,
                  "gap_rejected_minus_accepted": 1.2858351689225571
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.679504919052124,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5965619485908085,
                  "rejected_mean_error": 3.113727874755859,
                  "gap_rejected_minus_accepted": 1.5171659261650507
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.16766220331192,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4335429529773998,
                  "rejected_mean_error": 2.682493699921502,
                  "gap_rejected_minus_accepted": 1.2489507469441024
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6945854425430298,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1522600882053375,
                  "rejected_mean_error": 2.3442969942092895,
                  "gap_rejected_minus_accepted": 1.192036906003952
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1607020497322083,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7789971927801768,
                  "rejected_mean_error": 2.0748278724956,
                  "gap_rejected_minus_accepted": 1.2958306797154235
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9715818853104679,
              "spearman": 0.9638433407124686,
              "auroc_top30_bad": 0.9775603809523808,
              "mae": 0.1486061386808753,
              "mse": 0.04363314733114842,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7905152577345999,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15272177976369858
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24741672632694245
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5643538185596466
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9815336099306743
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3083135934591292
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9229683011815393,
              "spearman": 0.9345964575977329,
              "auroc_top30_worst": 0.9490499047619048,
              "pairwise_seed_ranking": 0.9184,
              "predicted_best_mean_error": 1.8209410129785537,
              "seed0_mean_error": 1.925728751182556,
              "random_seed_mean_error": 1.8916268434524537,
              "oracle_best_mean_error": 1.8181929438114166,
              "improvement_over_seed0": 0.10478773820400233,
              "gap_to_oracle": 0.0027480691671371016,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8865737490653992
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2077821284914627
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5049603371620177
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6896986420601925
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8927852801799774
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4859464168548593,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8131250196562874,
                  "rejected_mean_error": 2.6097276248931887,
                  "gap_rejected_minus_accepted": 0.7966026052369013
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.173467516899109,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6893125265486848,
                  "rejected_mean_error": 2.50190339568324,
                  "gap_rejected_minus_accepted": 0.8125908691345551
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9146664142608643,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5049603371620177,
                  "rejected_mean_error": 2.280610223197937,
                  "gap_rejected_minus_accepted": 0.7756498860359191
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5260021090507507,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2092809469555132,
                  "rejected_mean_error": 2.1211063648109882,
                  "gap_rejected_minus_accepted": 0.911825417855475
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.593058204650879,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8383650631374784,
                  "rejected_mean_error": 2.7120019435882567,
                  "gap_rejected_minus_accepted": 0.8736368804507784
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.173134207725525,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7036942830060255,
                  "rejected_mean_error": 2.5847834424367027,
                  "gap_rejected_minus_accepted": 0.8810891594306771
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9500548839569092,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5183215055465697,
                  "rejected_mean_error": 2.3331359968185423,
                  "gap_rejected_minus_accepted": 0.8148144912719726
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5679374635219574,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2211847778350589,
                  "rejected_mean_error": 2.163088485518879,
                  "gap_rejected_minus_accepted": 0.9419037076838201
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9792581426489527,
              "spearman": 0.9803038175020702,
              "auroc_top30_bad": 0.9915428571428573,
              "mae": 0.1629776981975883,
              "mse": 0.05177777958964877,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.995,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9214588668022347,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09696829818189144
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24702659738063812
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7033423124551773
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.084037047624588
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9740620121166685,
              "spearman": 0.984962952962953,
              "auroc_top30_worst": 0.9933333333333332,
              "pairwise_seed_ranking": 0.896,
              "predicted_best_mean_error": 2.2426220479607584,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08401036828756325,
              "gap_to_oracle": 0.0012115234136582664,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2923968124389649
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4812910771369934
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.658537769794464
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.867998973051707
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8247008323669434,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.1019229638576507,
                  "rejected_mean_error": 4.28990421295166,
                  "gap_rejected_minus_accepted": 2.187981249094009
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8165102005004883,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.867998973051707,
                  "rejected_mean_error": 3.678887435913086,
                  "gap_rejected_minus_accepted": 1.810888462861379
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.064878463745117,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.658537769794464,
                  "rejected_mean_error": 2.9829044077396394,
                  "gap_rejected_minus_accepted": 1.3243666379451753
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6976889967918396,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4812910771369934,
                  "rejected_mean_error": 2.6005310926437377,
                  "gap_rejected_minus_accepted": 1.1192400155067443
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.790111494064331,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1094102899233502,
                  "rejected_mean_error": 4.2816315531730655,
                  "gap_rejected_minus_accepted": 2.1722212632497153
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.856359601020813,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.880282998085022,
                  "rejected_mean_error": 3.66568067073822,
                  "gap_rejected_minus_accepted": 1.7853976726531982
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.077574372291565,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6745522892475129,
                  "rejected_mean_error": 2.9787125432491304,
                  "gap_rejected_minus_accepted": 1.3041602540016175
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.731490582227707,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4962398266792298,
                  "rejected_mean_error": 2.6034299461046855,
                  "gap_rejected_minus_accepted": 1.1071901194254556
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 57,
        "best_calib_loss": 0.023394200950860977,
        "train_time_sec": 41.58703327178955,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994515467773548,
              "spearman": 0.9979972669532498,
              "auroc_top30_bad": 0.9996605714285715,
              "mae": 0.028338648363726678,
              "mse": 0.0013496694532869383,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7682303080685288,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.061540248088887896
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1775421102629509
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.42106608240834903
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7659969664827455
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.188646869606932
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995557656060534,
              "spearman": 0.999187811239454,
              "auroc_top30_worst": 0.9993697142857142,
              "pairwise_seed_ranking": 0.9561,
              "predicted_best_mean_error": 1.655022640913725,
              "seed0_mean_error": 1.7257746937572955,
              "random_seed_mean_error": 1.7155524998605252,
              "oracle_best_mean_error": 1.6542172869741916,
              "improvement_over_seed0": 0.07075205284357056,
              "gap_to_oracle": 0.0008053539395334042,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5510314244031906
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7898781758308411
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0615809959411622
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2965605061531067
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.715404778456688
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8652448177337653,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4617744407918718,
                  "rejected_mean_error": 3.998077817440033,
                  "gap_rejected_minus_accepted": 2.536303376648161
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9944747388362885,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2965605061531067,
                  "rejected_mean_error": 2.971937595367432,
                  "gap_rejected_minus_accepted": 1.6753770892143252
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5724807977676392,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0615809959411622,
                  "rejected_mean_error": 2.3692285609722137,
                  "gap_rejected_minus_accepted": 1.3076475650310515
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1212170124053955,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7898781758308411,
                  "rejected_mean_error": 2.023913645998637,
                  "gap_rejected_minus_accepted": 1.234035470167796
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8804141044616705,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4719080329272483,
                  "rejected_mean_error": 4.010574641227723,
                  "gap_rejected_minus_accepted": 2.538666608300474
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0107498168945312,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3066547589699427,
                  "rejected_mean_error": 2.9831344981193544,
                  "gap_rejected_minus_accepted": 1.6764797391494117
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5860353708267212,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0677372820973396,
                  "rejected_mean_error": 2.3838121054172516,
                  "gap_rejected_minus_accepted": 1.316074823319912
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1340596973896027,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7919459277391434,
                  "rejected_mean_error": 2.0370509490966797,
                  "gap_rejected_minus_accepted": 1.2451050213575363
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9663558753957993,
              "spearman": 0.9627452181230751,
              "auroc_top30_bad": 0.9942087619047619,
              "mae": 0.1765436027494259,
              "mse": 0.0648443615160086,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6946149000895743,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1847697606086731
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25515822410583494
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45688977390527724
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8325719116926193
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2162184780657292
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.951059881313367,
              "spearman": 0.980922376270321,
              "auroc_top30_worst": 0.9849356190476191,
              "pairwise_seed_ranking": 0.9348,
              "predicted_best_mean_error": 1.6482635372877121,
              "seed0_mean_error": 1.7482785412073136,
              "random_seed_mean_error": 1.7301191527843476,
              "oracle_best_mean_error": 1.6468809620141982,
              "improvement_over_seed0": 0.1000150039196015,
              "gap_to_oracle": 0.0013825752735139307,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4683729739189148
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7642340432756987
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1298887988090516
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.414019279452021
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7264184505939484
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.524477624893189,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5761976390944588,
                  "rejected_mean_error": 3.0784057540893555,
                  "gap_rejected_minus_accepted": 1.5022081149948967
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.059844732284546,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.413410689622132,
                  "rejected_mean_error": 2.6634416839185233,
                  "gap_rejected_minus_accepted": 1.2500309942963914
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5144968032836914,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1298887988090516,
                  "rejected_mean_error": 2.322948102378845,
                  "gap_rejected_minus_accepted": 1.1930593035697936
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9760441780090332,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7648712733683114,
                  "rejected_mean_error": 2.0476183080876775,
                  "gap_rejected_minus_accepted": 1.2827470347193661
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5188051223754884,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.589184925953547,
                  "rejected_mean_error": 3.180121078491211,
                  "gap_rejected_minus_accepted": 1.590936152537664
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.125075876712799,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4263009663252908,
                  "rejected_mean_error": 2.7039897555396673,
                  "gap_rejected_minus_accepted": 1.2776887892143765
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.520354151725769,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.149342386484146,
                  "rejected_mean_error": 2.347214695930481,
                  "gap_rejected_minus_accepted": 1.1978723094463348
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.016721248626709,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7763564610292041,
                  "rejected_mean_error": 2.0757175307860347,
                  "gap_rejected_minus_accepted": 1.2993610697568307
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9729036903570658,
              "spearman": 0.9666974560066259,
              "auroc_top30_bad": 0.9858689523809525,
              "mae": 0.15420978963002563,
              "mse": 0.04516683055290479,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7264976982775107,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15778378546237945
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2613767236709595
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5660997351646423
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9781974905967712
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3083135934591292
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9495282120049201,
              "spearman": 0.9574593944046701,
              "auroc_top30_worst": 0.9750278095238096,
              "pairwise_seed_ranking": 0.924,
              "predicted_best_mean_error": 1.8200124094486236,
              "seed0_mean_error": 1.925728751182556,
              "random_seed_mean_error": 1.8916268434524537,
              "oracle_best_mean_error": 1.8181929438114166,
              "improvement_over_seed0": 0.1057163417339324,
              "gap_to_oracle": 0.0018194656372070295,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.887426691532135
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.203099940640804
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4987085770606994
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6889916601846975
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8927852801799774
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.425914835929871,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8083158022032844,
                  "rejected_mean_error": 2.6530105819702148,
                  "gap_rejected_minus_accepted": 0.8446947797669304
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.089536964893341,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6885824294456677,
                  "rejected_mean_error": 2.5040890218350835,
                  "gap_rejected_minus_accepted": 0.8155065923894158
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7964106798171997,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4987085770606994,
                  "rejected_mean_error": 2.2868619832992554,
                  "gap_rejected_minus_accepted": 0.788153406238556
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3805595934391022,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.204223820005362,
                  "rejected_mean_error": 2.1227956718925225,
                  "gap_rejected_minus_accepted": 0.9185718518871604
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5402633905410767,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8312755054897731,
                  "rejected_mean_error": 2.7758079624176024,
                  "gap_rejected_minus_accepted": 0.9445324569278293
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1444477438926697,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6992589496673747,
                  "rejected_mean_error": 2.597948638219682,
                  "gap_rejected_minus_accepted": 0.8986896885523075
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8196247816085815,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5095182809829713,
                  "rejected_mean_error": 2.341939221382141,
                  "gap_rejected_minus_accepted": 0.8324209403991698
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4009829461574554,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.214140598736112,
                  "rejected_mean_error": 2.165461658156492,
                  "gap_rejected_minus_accepted": 0.95132105942038
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9870565356904056,
              "spearman": 0.9809311779120825,
              "auroc_top30_bad": 0.9909619047619047,
              "mae": 0.14526112464047036,
              "mse": 0.038762504055544864,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.995,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8858191113581521,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11505157366394997
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21720626145601274
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.706913791179657
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0844709584712982
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9851954292238124,
              "spearman": 0.9720131880131879,
              "auroc_top30_worst": 0.9944190476190476,
              "pairwise_seed_ranking": 0.8835,
              "predicted_best_mean_error": 2.2439217260479927,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08271069020032895,
              "gap_to_oracle": 0.002511201500892568,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3141428673267364
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5000829005241394
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.663423431634903
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8628458663622538
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.85421679019928,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0954242747359806,
                  "rejected_mean_error": 4.348392415046692,
                  "gap_rejected_minus_accepted": 2.252968140310711
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.580803632736206,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8628458663622538,
                  "rejected_mean_error": 3.6943467559814454,
                  "gap_rejected_minus_accepted": 1.8315008896191916
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9667235612869263,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.663423431634903,
                  "rejected_mean_error": 2.9780187458992002,
                  "gap_rejected_minus_accepted": 1.3145953142642972
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6542360484600067,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.5000829005241394,
                  "rejected_mean_error": 2.594267151514689,
                  "gap_rejected_minus_accepted": 1.0941842509905497
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8522674322128294,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.5505935549736023,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8760858297348022,
                  "rejected_mean_error": 3.678272175788879,
                  "gap_rejected_minus_accepted": 1.802186346054077
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9807106852531433,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.67655832529068,
                  "rejected_mean_error": 2.976706507205963,
                  "gap_rejected_minus_accepted": 1.3001481819152831
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6765128672122955,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5063812494277955,
                  "rejected_mean_error": 2.6000494718551637,
                  "gap_rejected_minus_accepted": 1.0936682224273682
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 79,
        "best_calib_loss": 0.025133958086371422,
        "train_time_sec": 29.33071732521057,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9996852473323586,
              "spearman": 0.9989975177166072,
              "auroc_top30_bad": 0.999862761904762,
              "mae": 0.02632141018473776,
              "mse": 0.0011091955640747636,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7863677664559,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06062637746927794
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17670866543515584
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4208958832883043
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7658126963392365
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.188646869606932
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997465426727864,
              "spearman": 0.9996436069697358,
              "auroc_top30_worst": 0.9996100952380953,
              "pairwise_seed_ranking": 0.9549,
              "predicted_best_mean_error": 1.654842622280121,
              "seed0_mean_error": 1.7257746937572955,
              "random_seed_mean_error": 1.7155524998605252,
              "oracle_best_mean_error": 1.6542172869741916,
              "improvement_over_seed0": 0.07093207147717462,
              "gap_to_oracle": 0.0006253353059293421,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5501317168474198
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7892336418151855
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0614013914108276
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2964890551884969
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.715404778456688
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9015988349914563,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4617713727686141,
                  "rejected_mean_error": 3.9981054296493532,
                  "gap_rejected_minus_accepted": 2.5363340568807393
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0158000588417053,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2964890551884969,
                  "rejected_mean_error": 2.972151948261261,
                  "gap_rejected_minus_accepted": 1.675662893072764
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.591421663761139,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0614013914108276,
                  "rejected_mean_error": 2.369408165502548,
                  "gap_rejected_minus_accepted": 1.3080067740917205
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1324939131736755,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7892336418151855,
                  "rejected_mean_error": 2.024128490670522,
                  "gap_rejected_minus_accepted": 1.2348948488553366
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.934745669364929,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4719471489389737,
                  "rejected_mean_error": 4.010222597122192,
                  "gap_rejected_minus_accepted": 2.5382754481832186
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0310980081558228,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3064157605568567,
                  "rejected_mean_error": 2.983851493358612,
                  "gap_rejected_minus_accepted": 1.6774357328017555
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.599564254283905,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.067737265408039,
                  "rejected_mean_error": 2.3838121221065522,
                  "gap_rejected_minus_accepted": 1.3160748566985132
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1433607041835785,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7912781587839126,
                  "rejected_mean_error": 2.037273538748423,
                  "gap_rejected_minus_accepted": 1.2459953799645105
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9623569122292218,
              "spearman": 0.95978745500941,
              "auroc_top30_bad": 0.9915337142857142,
              "mae": 0.1792907864765264,
              "mse": 0.0790941613671047,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6979879711478805,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17084480729699134
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2594314285516739
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45508366771936415
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.835721938141187
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2162184780657292
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9352571180377347,
              "spearman": 0.9703080688051641,
              "auroc_top30_worst": 0.9791329523809523,
              "pairwise_seed_ranking": 0.9252,
              "predicted_best_mean_error": 1.6488275110721589,
              "seed0_mean_error": 1.7482785412073136,
              "random_seed_mean_error": 1.7301191527843476,
              "oracle_best_mean_error": 1.6468809620141982,
              "improvement_over_seed0": 0.09945103013515477,
              "gap_to_oracle": 0.001946549057960656,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5234071927070618
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7609477295325353
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1342735991477966
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4151204387897622
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7264184505939484
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.460686111450196,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5835787411265903,
                  "rejected_mean_error": 3.011975835800171,
                  "gap_rejected_minus_accepted": 1.4283970946735807
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.014945089817047,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4142265976938393,
                  "rejected_mean_error": 2.6609991731735083,
                  "gap_rejected_minus_accepted": 1.246772575479669
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5486629605293274,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1342735991477966,
                  "rejected_mean_error": 2.3185633020401,
                  "gap_rejected_minus_accepted": 1.1842897028923036
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9937103539705276,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7623579757282147,
                  "rejected_mean_error": 2.048457862155287,
                  "gap_rejected_minus_accepted": 1.2860998864270723
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4998688220977785,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5927476974328358,
                  "rejected_mean_error": 3.148056135177612,
                  "gap_rejected_minus_accepted": 1.5553084377447763
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0421600937843323,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4283376933737872,
                  "rejected_mean_error": 2.697944232395717,
                  "gap_rejected_minus_accepted": 1.2696065390219298
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5580062866210938,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1516285135746003,
                  "rejected_mean_error": 2.344928568840027,
                  "gap_rejected_minus_accepted": 1.1933000552654267
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0123531520366669,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7763957764421191,
                  "rejected_mean_error": 2.0757042854864967,
                  "gap_rejected_minus_accepted": 1.2993085090443777
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9682887949113719,
              "spearman": 0.9620218760970562,
              "auroc_top30_bad": 0.9842118095238096,
              "mae": 0.1645708311099559,
              "mse": 0.05527472652070069,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7365447398853853,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15472603172063829
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2751924082040787
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5663124240398407
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9789788234392802
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3083135934591292
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.922495663510551,
              "spearman": 0.9374512321607887,
              "auroc_top30_worst": 0.9633828571428571,
              "pairwise_seed_ranking": 0.9244,
              "predicted_best_mean_error": 1.820458437204361,
              "seed0_mean_error": 1.925728751182556,
              "random_seed_mean_error": 1.8916268434524537,
              "oracle_best_mean_error": 1.8181929438114166,
              "improvement_over_seed0": 0.10527031397819497,
              "gap_to_oracle": 0.002265493392944462,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9015918154716491
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.208623146590514
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.503052729511261
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7003466303287538
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8927852801799774
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.361485743522644,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8194490807321337,
                  "rejected_mean_error": 2.5528110752105713,
                  "gap_rejected_minus_accepted": 0.7333619944784375
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0953373312950134,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6998446512502183,
                  "rejected_mean_error": 2.470374319500055,
                  "gap_rejected_minus_accepted": 0.7705296682498366
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8408663868904114,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.503052729511261,
                  "rejected_mean_error": 2.2825178308486938,
                  "gap_rejected_minus_accepted": 0.7794651013374327
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3776693642139435,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2095371871329725,
                  "rejected_mean_error": 2.1210207691060314,
                  "gap_rejected_minus_accepted": 0.9114835819730589
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4604153871536254,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8452901554107666,
                  "rejected_mean_error": 2.649676113128662,
                  "gap_rejected_minus_accepted": 0.8043859577178953
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1535086631774902,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7148988042923219,
                  "rejected_mean_error": 2.5515255776662675,
                  "gap_rejected_minus_accepted": 0.8366267733739456
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8627337217330933,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5173966703414916,
                  "rejected_mean_error": 2.3340608320236207,
                  "gap_rejected_minus_accepted": 0.8166641616821291
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4135980904102325,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2190402500213138,
                  "rejected_mean_error": 2.1638109734989106,
                  "gap_rejected_minus_accepted": 0.9447707234775968
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9843557772296407,
              "spearman": 0.9795492204271176,
              "auroc_top30_bad": 0.9906178571428571,
              "mae": 0.15017631719296332,
              "mse": 0.043807113141100175,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9233594389716224,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10668707877397537
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22564879682660102
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7062216150760651
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0841534140904745
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9846424351772284,
              "spearman": 0.9761839721839722,
              "auroc_top30_worst": 0.9958857142857143,
              "pairwise_seed_ranking": 0.9015,
              "predicted_best_mean_error": 2.2441196295619013,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08251278668642037,
              "gap_to_oracle": 0.0027091050148011497,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.312134051322937
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.502885172367096
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6566593277454376
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8595468974113465
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8586889743804935,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0962958975632984,
                  "rejected_mean_error": 4.34054780960083,
                  "gap_rejected_minus_accepted": 2.2442519120375315
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6082451343536377,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8595468974113465,
                  "rejected_mean_error": 3.7042436628341675,
                  "gap_rejected_minus_accepted": 1.844696765422821
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.029666781425476,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6566593277454376,
                  "rejected_mean_error": 2.9847828497886657,
                  "gap_rejected_minus_accepted": 1.3281235220432281
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7196220457553864,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.502885172367096,
                  "rejected_mean_error": 2.5933330609003704,
                  "gap_rejected_minus_accepted": 1.0904478885332745
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8613191604614254,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.589352011680603,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8688090626398723,
                  "rejected_mean_error": 3.7001024770736692,
                  "gap_rejected_minus_accepted": 1.831293414433797
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.02402400970459,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6718537533283233,
                  "rejected_mean_error": 2.9814110791683195,
                  "gap_rejected_minus_accepted": 1.3095573258399962
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7256633043289185,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5240629482269288,
                  "rejected_mean_error": 2.5941555722554526,
                  "gap_rejected_minus_accepted": 1.0700926240285238
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      }
    ],
    "target_chunk_min_l2_K20": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 58,
        "best_calib_loss": 0.06997580826282501,
        "train_time_sec": 10.702090501785278,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.987502681424042,
              "spearman": 0.960177749332684,
              "auroc_top30_bad": 0.9991445238095238,
              "mae": 0.09722065485451603,
              "mse": 0.02595465342123659,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.521,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7915834007564126,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09421755781990941
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1694590998956468
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3230941978820367
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6989433494811722
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1374262927238248
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979506256036282,
              "spearman": 0.9965709197988367,
              "auroc_top30_worst": 0.9959893333333333,
              "pairwise_seed_ranking": 0.853,
              "predicted_best_mean_error": 1.6594992717206478,
              "seed0_mean_error": 1.7251936940252781,
              "random_seed_mean_error": 1.715085545092821,
              "oracle_best_mean_error": 1.653713216215372,
              "improvement_over_seed0": 0.0656944223046303,
              "gap_to_oracle": 0.005786055505275778,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5497484360933304
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7897084285736083
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0615290463924407
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2977493216832479
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.714853994178772
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.837765002250674,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4613007440037198,
                  "rejected_mean_error": 3.996833245754242,
                  "gap_rejected_minus_accepted": 2.535532501750522
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9454954266548157,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2977493216832479,
                  "rejected_mean_error": 2.9661680116653444,
                  "gap_rejected_minus_accepted": 1.6684186899820965
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5563990473747253,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0615290463924407,
                  "rejected_mean_error": 2.368178941965103,
                  "gap_rejected_minus_accepted": 1.3066498955726624
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1226755380630493,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7897084285736083,
                  "rejected_mean_error": 2.023235849380493,
                  "gap_rejected_minus_accepted": 1.233527420806885
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8613977432250977,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4714341080519888,
                  "rejected_mean_error": 4.0090299677848815,
                  "gap_rejected_minus_accepted": 2.5375958597328925
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9560562074184418,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3080307188431421,
                  "rejected_mean_error": 2.976682619571686,
                  "gap_rejected_minus_accepted": 1.6686519007285436
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5668469667434692,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.06714851385355,
                  "rejected_mean_error": 2.3832388741970063,
                  "gap_rejected_minus_accepted": 1.3160903603434564
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1357762515544891,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7916380349397659,
                  "rejected_mean_error": 2.0363789137204487,
                  "gap_rejected_minus_accepted": 1.2447408787806826
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8358465453302946,
              "spearman": 0.8368334811181373,
              "auroc_top30_bad": 0.9252365714285715,
              "mae": 0.3806069904476404,
              "mse": 0.2748720209536485,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7219842046899018,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3835392787754536
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.37524129948616025
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5126610885739327
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8711837969700496
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2130705400884152
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6480755552320783,
              "spearman": 0.6899640936730201,
              "auroc_top30_worst": 0.8464761904761904,
              "pairwise_seed_ranking": 0.7716,
              "predicted_best_mean_error": 1.6603966987133025,
              "seed0_mean_error": 1.7480104013681412,
              "random_seed_mean_error": 1.7297815368175506,
              "oracle_best_mean_error": 1.6466209226846695,
              "improvement_over_seed0": 0.0876137026548387,
              "gap_to_oracle": 0.013775776028633002,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8034731600284576
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0060739075908294
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3018951803207397
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4667211475529904
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7261501743793488
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6522266864776616,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6677415686183505,
                  "rejected_mean_error": 2.2518276262283323,
                  "gap_rejected_minus_accepted": 0.5840860576099818
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9266445338726044,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4658761049283862,
                  "rejected_mean_error": 2.5053092896367035,
                  "gap_rejected_minus_accepted": 1.0394331847083174
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5143529176712036,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3018951803207397,
                  "rejected_mean_error": 2.150405168437958,
                  "gap_rejected_minus_accepted": 0.8485099881172182
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9329154789447784,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.005960713560208,
                  "rejected_mean_error": 1.9667257359976957,
                  "gap_rejected_minus_accepted": 0.9607650224374877
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.652226686477661,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.698168112039566,
                  "rejected_mean_error": 2.1965910053253173,
                  "gap_rejected_minus_accepted": 0.4984228932857513
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9729928970336914,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4906486242531456,
                  "rejected_mean_error": 2.5119255175666204,
                  "gap_rejected_minus_accepted": 1.0212768933134748
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5659199953079224,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.310031498670578,
                  "rejected_mean_error": 2.1859893040657044,
                  "gap_rejected_minus_accepted": 0.8759578053951262
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9965436011552811,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0419953640491244,
                  "rejected_mean_error": 1.985865734796473,
                  "gap_rejected_minus_accepted": 0.9438703707473486
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8818467858320365,
              "spearman": 0.8393281666172288,
              "auroc_top30_bad": 0.9246148571428571,
              "mae": 0.3170274698406458,
              "mse": 0.18850876762481544,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.7238800318120456,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.43533414345979693
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.41858779618740083
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.598653631234169
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0285579412142436
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.305430052804947
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7338383643648134,
              "spearman": 0.7166934353237987,
              "auroc_top30_worst": 0.7849752380952381,
              "pairwise_seed_ranking": 0.7864,
              "predicted_best_mean_error": 1.8318500490188598,
              "seed0_mean_error": 1.925728751182556,
              "random_seed_mean_error": 1.8916268434524537,
              "oracle_best_mean_error": 1.8181929438114166,
              "improvement_over_seed0": 0.0938787021636962,
              "gap_to_oracle": 0.013657105207443232,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0182639074325561
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3181181280658796
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5926480796813964
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7598877103725221
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8927852801799774
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.191142082214357,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8352603620423211,
                  "rejected_mean_error": 2.4105095434188843,
                  "gap_rejected_minus_accepted": 0.5752491813765632
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9538345336914062,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7588604713453173,
                  "rejected_mean_error": 2.2937039571067395,
                  "gap_rejected_minus_accepted": 0.5348434857614222
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7049255967140198,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5926480796813964,
                  "rejected_mean_error": 2.1929224806785585,
                  "gap_rejected_minus_accepted": 0.6002744009971621
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.352080374956131,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3193464703834095,
                  "rejected_mean_error": 2.084339546419386,
                  "gap_rejected_minus_accepted": 0.7649930760359767
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2782290935516354,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.862414919535319,
                  "rejected_mean_error": 2.4955532360076904,
                  "gap_rejected_minus_accepted": 0.6331383164723714
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9552432894706726,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7772308211913084,
                  "rejected_mean_error": 2.3665083211565774,
                  "gap_rejected_minus_accepted": 0.589277499965269
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7271361351013184,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.604884066581726,
                  "rejected_mean_error": 2.2465734357833864,
                  "gap_rejected_minus_accepted": 0.6416893692016603
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3828760385513306,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3282873838666887,
                  "rejected_mean_error": 2.127005789369185,
                  "gap_rejected_minus_accepted": 0.7987184055024965
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8788189952117947,
              "spearman": 0.8368895448848018,
              "auroc_top30_bad": 0.9270238095238095,
              "mae": 0.40717883300967517,
              "mse": 0.3410867344753255,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.49,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8188863435647054,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6786572100967169
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5822864396572113
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7963618477284908
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1342603245576224
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.859045901306706,
              "spearman": 0.746973950973951,
              "auroc_top30_worst": 0.8539952380952381,
              "pairwise_seed_ranking": 0.768,
              "predicted_best_mean_error": 2.2546326276659965,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07199978858232514,
              "gap_to_oracle": 0.013222103118896378,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4625539469718933
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.767864347934723
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8134308745861054
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.874733784198761
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5725840330123906,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.140288045273887,
                  "rejected_mean_error": 3.944618480205536,
                  "gap_rejected_minus_accepted": 1.8043304349316491
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.341584265232086,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.874733784198761,
                  "rejected_mean_error": 3.658683002471924,
                  "gap_rejected_minus_accepted": 1.7839492182731629
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.681874930858612,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.8134308745861054,
                  "rejected_mean_error": 2.828011302947998,
                  "gap_rejected_minus_accepted": 1.0145804283618924
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2631414234638214,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.767864347934723,
                  "rejected_mean_error": 2.5050066690444948,
                  "gap_rejected_minus_accepted": 0.7371423211097718
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.6076151847839353,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.146726703643799,
                  "rejected_mean_error": 3.945783829689026,
                  "gap_rejected_minus_accepted": 1.799057126045227
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3740344643592834,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8838839912414551,
                  "rejected_mean_error": 3.6548776912689207,
                  "gap_rejected_minus_accepted": 1.7709937000274656
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7140401601791382,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8293899965286256,
                  "rejected_mean_error": 2.8238748359680175,
                  "gap_rejected_minus_accepted": 0.9944848394393919
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2646713554859161,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7950707173347473,
                  "rejected_mean_error": 2.503819649219513,
                  "gap_rejected_minus_accepted": 0.7087489318847655
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K20"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 76,
        "best_calib_loss": 0.025863340124487877,
        "train_time_sec": 35.35828709602356,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995250819122287,
              "spearman": 0.9971268916173512,
              "auroc_top30_bad": 0.999734,
              "mae": 0.02263091758034425,
              "mse": 0.0011007059296709218,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.961,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8149053857198393,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.007803265636786819
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.07321687807007693
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3216338336356683
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6979161065663366
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1374262927238248
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997906206154976,
              "spearman": 0.9996119225764767,
              "auroc_top30_worst": 0.9997638095238095,
              "pairwise_seed_ranking": 0.9315,
              "predicted_best_mean_error": 1.6551340345442296,
              "seed0_mean_error": 1.7251936940252781,
              "random_seed_mean_error": 1.715085545092821,
              "oracle_best_mean_error": 1.653713216215372,
              "improvement_over_seed0": 0.07005965948104853,
              "gap_to_oracle": 0.0014208183288575427,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5487308202981949
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7875498420715332
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0602547268867493
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2957875118255615
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.714853994178772
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8405681371688853,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4611546767552694,
                  "rejected_mean_error": 3.9981478509902955,
                  "gap_rejected_minus_accepted": 2.5369931742350262
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9952025413513184,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2957875118255615,
                  "rejected_mean_error": 2.9720534412384034,
                  "gap_rejected_minus_accepted": 1.676265929412842
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.573333501815796,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0602547268867493,
                  "rejected_mean_error": 2.369453261470795,
                  "gap_rejected_minus_accepted": 1.3091985345840456
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.134695053100586,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7875498420715332,
                  "rejected_mean_error": 2.0239553782145183,
                  "gap_rejected_minus_accepted": 1.236405536142985
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8432486057281507,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4712163990404872,
                  "rejected_mean_error": 4.010989348888398,
                  "gap_rejected_minus_accepted": 2.5397729498479107
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.004140794277191,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.305834149400393,
                  "rejected_mean_error": 2.983272327899933,
                  "gap_rejected_minus_accepted": 1.6774381784995398
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5803903341293335,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0665702753663062,
                  "rejected_mean_error": 2.38381711268425,
                  "gap_rejected_minus_accepted": 1.3172468373179438
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1581205129623413,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7897171617746354,
                  "rejected_mean_error": 2.0370192047754925,
                  "gap_rejected_minus_accepted": 1.247302043000857
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9559866913120025,
              "spearman": 0.9541446582211307,
              "auroc_top30_bad": 0.989000380952381,
              "mae": 0.18205581297334283,
              "mse": 0.076464481254019,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.904,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7599813683798597,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2203274197280407
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25915442152023316
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.44966304839849475
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8323169670025508
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2130705400884152
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9176908872921403,
              "spearman": 0.9657263974682503,
              "auroc_top30_worst": 0.9763961904761904,
              "pairwise_seed_ranking": 0.9316,
              "predicted_best_mean_error": 1.648558630347252,
              "seed0_mean_error": 1.7480104013681412,
              "random_seed_mean_error": 1.7297815368175506,
              "oracle_best_mean_error": 1.6466209226846695,
              "improvement_over_seed0": 0.09945177102088931,
              "gap_to_oracle": 0.0019377076625823886,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46871640491485594
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7640492213078034
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1346074078559876
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4186138685451133
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7261501743793488
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.640459442138672,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5974217591285707,
                  "rejected_mean_error": 2.8847059116363525,
                  "gap_rejected_minus_accepted": 1.2872841525077818
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.093274772167206,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4181018775784218,
                  "rejected_mean_error": 2.648326705058162,
                  "gap_rejected_minus_accepted": 1.2302248274797403
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6745129823684692,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1346074078559876,
                  "rejected_mean_error": 2.31769294090271,
                  "gap_rejected_minus_accepted": 1.1830855330467225
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0787098407745361,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7648371279049224,
                  "rejected_mean_error": 2.0472718217075188,
                  "gap_rejected_minus_accepted": 1.2824346938025963
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6752674102783205,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6167014584276411,
                  "rejected_mean_error": 2.9297908878326417,
                  "gap_rejected_minus_accepted": 1.3130894294050006
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.147897958755493,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4304583902983743,
                  "rejected_mean_error": 2.690585418353005,
                  "gap_rejected_minus_accepted": 1.2601270280546308
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7127712965011597,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1529456808567047,
                  "rejected_mean_error": 2.343075121879578,
                  "gap_rejected_minus_accepted": 1.190129441022873
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0935260355472565,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7754671644596827,
                  "rejected_mean_error": 2.075658657652809,
                  "gap_rejected_minus_accepted": 1.3001914931931262
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9647696003183228,
              "spearman": 0.9473672563653651,
              "auroc_top30_bad": 0.9792540952380951,
              "mae": 0.17348059564698487,
              "mse": 0.062313488754149125,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.884,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7838782056942885,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.28969877076148987
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28712230048179627
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5587967403411865
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9781266562143962
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.305430052804947
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9231889428052495,
              "spearman": 0.9382393112571594,
              "auroc_top30_worst": 0.9494095238095238,
              "pairwise_seed_ranking": 0.918,
              "predicted_best_mean_error": 1.820513038635254,
              "seed0_mean_error": 1.925728751182556,
              "random_seed_mean_error": 1.8916268434524537,
              "oracle_best_mean_error": 1.8181929438114166,
              "improvement_over_seed0": 0.10521571254730211,
              "gap_to_oracle": 0.0023200948238373265,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8928418555259705
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2071597620080678
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5073027331352233
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6899671416674087
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8927852801799774
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3609480142593386,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8102604388660855,
                  "rejected_mean_error": 2.635508852005005,
                  "gap_rejected_minus_accepted": 0.8252484131389195
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0795041918754578,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6896894927849255,
                  "rejected_mean_error": 2.500774905704462,
                  "gap_rejected_minus_accepted": 0.8110854129195364
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8590688109397888,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5073027331352233,
                  "rejected_mean_error": 2.2782678272247314,
                  "gap_rejected_minus_accepted": 0.7709650940895081
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4717368185520172,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.208478913710902,
                  "rejected_mean_error": 2.1213742798649515,
                  "gap_rejected_minus_accepted": 0.9128953661540495
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.460134100914001,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8367605442470973,
                  "rejected_mean_error": 2.7264426136016846,
                  "gap_rejected_minus_accepted": 0.8896820693545873
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1044443249702454,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.702437757808257,
                  "rejected_mean_error": 2.5885131283411904,
                  "gap_rejected_minus_accepted": 0.8860753705329334
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8864653706550598,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.522566047668457,
                  "rejected_mean_error": 2.3288914546966555,
                  "gap_rejected_minus_accepted": 0.8063254070281984
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5005553662776947,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2140060644301156,
                  "rejected_mean_error": 2.1655069825483517,
                  "gap_rejected_minus_accepted": 0.9515009181182361
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9614816459684025,
              "spearman": 0.9487977879463758,
              "auroc_top30_bad": 0.9924107142857143,
              "mae": 0.1955136188203469,
              "mse": 0.10991838961725794,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9621271759423096,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5081724958121776
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.366828587859869
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7056851185560227
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.082761534055074
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9806410504711818,
              "spearman": 0.9852908412908413,
              "auroc_top30_worst": 0.9910238095238095,
              "pairwise_seed_ranking": 0.8855,
              "predicted_best_mean_error": 2.2467971155047417,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07983530074357992,
              "gap_to_oracle": 0.0053865909576416016,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3013999354839325
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.485121401309967
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6565844156742096
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.873894323825836
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8499957084655763,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.096707424455219,
                  "rejected_mean_error": 4.336844067573548,
                  "gap_rejected_minus_accepted": 2.240136643118329
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.444590210914612,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.873894323825836,
                  "rejected_mean_error": 3.661201383590698,
                  "gap_rejected_minus_accepted": 1.787307059764862
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.019702196121216,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6565844156742096,
                  "rejected_mean_error": 2.9848577618598937,
                  "gap_rejected_minus_accepted": 1.3282733461856842
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.702451229095459,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.485121401309967,
                  "rejected_mean_error": 2.599254317919413,
                  "gap_rejected_minus_accepted": 1.1141329166094462
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.854226279258728,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1060607194900514,
                  "rejected_mean_error": 4.3117776870727536,
                  "gap_rejected_minus_accepted": 2.205716967582702
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4511138796806335,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.885411418279012,
                  "rejected_mean_error": 3.65029541015625,
                  "gap_rejected_minus_accepted": 1.764883991877238
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.018206000328064,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6741591012477874,
                  "rejected_mean_error": 2.979105731248856,
                  "gap_rejected_minus_accepted": 1.3049466300010684
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7178921401500702,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.498574664592743,
                  "rejected_mean_error": 2.602651666800181,
                  "gap_rejected_minus_accepted": 1.1040770022074382
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K20"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 38,
        "best_calib_loss": 0.02393743209540844,
        "train_time_sec": 41.673646450042725,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.998660928112293,
              "spearman": 0.9924648846813521,
              "auroc_top30_bad": 0.9992633333333333,
              "mae": 0.04261479074762319,
              "mse": 0.003533777484754435,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.941,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8331296798245539,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.02312212849536445
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.07762691645189189
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3218523109682603
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6982262583658565
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1374262927238248
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9992074113931697,
              "spearman": 0.998522129956885,
              "auroc_top30_worst": 0.9992626666666666,
              "pairwise_seed_ranking": 0.9461,
              "predicted_best_mean_error": 1.6549709870219231,
              "seed0_mean_error": 1.7251936940252781,
              "random_seed_mean_error": 1.715085545092821,
              "oracle_best_mean_error": 1.653713216215372,
              "improvement_over_seed0": 0.07022270700335498,
              "gap_to_oracle": 0.001257770806551095,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5497697049379349
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7884234354972839
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0606983059883117
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2962311219215392
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.714853994178772
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.903216910362245,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4613429165416294,
                  "rejected_mean_error": 3.9964536929130556,
                  "gap_rejected_minus_accepted": 2.5351107763714262
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0284974575042725,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2962311219215392,
                  "rejected_mean_error": 2.97072261095047,
                  "gap_rejected_minus_accepted": 1.6744914890289309
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5798395276069641,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0606983059883117,
                  "rejected_mean_error": 2.3690096823692324,
                  "gap_rejected_minus_accepted": 1.3083113763809207
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1224221289157867,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7884234354972839,
                  "rejected_mean_error": 2.0236641804059348,
                  "gap_rejected_minus_accepted": 1.2352407449086509
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.904008340835573,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4714895191788673,
                  "rejected_mean_error": 4.008531267642975,
                  "gap_rejected_minus_accepted": 2.537041748464108
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0476948022842407,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3057940057516098,
                  "rejected_mean_error": 2.983392758846283,
                  "gap_rejected_minus_accepted": 1.6775987530946732
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6004212498664856,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0669170482754706,
                  "rejected_mean_error": 2.3834703397750854,
                  "gap_rejected_minus_accepted": 1.3165532914996148
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1379629373550415,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7901252623796463,
                  "rejected_mean_error": 2.036883171240489,
                  "gap_rejected_minus_accepted": 1.2467579088608427
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9683606690479075,
              "spearman": 0.9463255685241547,
              "auroc_top30_bad": 0.9939039999999999,
              "mae": 0.1755514290753752,
              "mse": 0.065084393107937,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.936,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7571063542417528,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24955184006690978
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28302969017028806
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4486604069828987
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8294653503974279
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2130705400884152
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9646109006860497,
              "spearman": 0.9850760424166672,
              "auroc_top30_worst": 0.9906438095238095,
              "pairwise_seed_ranking": 0.9204,
              "predicted_best_mean_error": 1.6485707709789277,
              "seed0_mean_error": 1.7480104013681412,
              "random_seed_mean_error": 1.7297815368175506,
              "oracle_best_mean_error": 1.6466209226846695,
              "improvement_over_seed0": 0.09943963038921355,
              "gap_to_oracle": 0.0019498482942581497,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47054749155044556
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.760409112733144
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1307141541481018
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4085724326466191
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7261501743793488
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.531155872344971,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5684871394369337,
                  "rejected_mean_error": 3.145117488861084,
                  "gap_rejected_minus_accepted": 1.5766303494241503
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1012128591537476,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4078146307674517,
                  "rejected_mean_error": 2.679122712284612,
                  "gap_rejected_minus_accepted": 1.2713080815171605
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.581269919872284,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1307141541481018,
                  "rejected_mean_error": 2.3215861946105956,
                  "gap_rejected_minus_accepted": 1.1908720404624937
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.001274824142456,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7612897631840203,
                  "rejected_mean_error": 2.0484568005310435,
                  "gap_rejected_minus_accepted": 1.2871670373470232
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.533732295036316,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5851237706343333,
                  "rejected_mean_error": 3.213990077972412,
                  "gap_rejected_minus_accepted": 1.6288663073380787
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.125681161880493,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.418910245366275,
                  "rejected_mean_error": 2.7248632453736805,
                  "gap_rejected_minus_accepted": 1.3059530000074056
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6076407432556152,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1500075924396516,
                  "rejected_mean_error": 2.346013210296631,
                  "gap_rejected_minus_accepted": 1.1960056178569793
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0189219415187836,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.774472878565864,
                  "rejected_mean_error": 2.0759936309753253,
                  "gap_rejected_minus_accepted": 1.3015207524094614
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9654818714501654,
              "spearman": 0.94568871313742,
              "auroc_top30_bad": 0.9798255238095238,
              "mae": 0.17880816714540124,
              "mse": 0.06271093028527466,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.964,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8031563984040048,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2580931571125984
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3035349935293198
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5585351445198059
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9767125048319498
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.305430052804947
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9509298697988465,
              "spearman": 0.9480686914999628,
              "auroc_top30_worst": 0.9671619047619048,
              "pairwise_seed_ranking": 0.9208,
              "predicted_best_mean_error": 1.8210713698863983,
              "seed0_mean_error": 1.925728751182556,
              "random_seed_mean_error": 1.8916268434524537,
              "oracle_best_mean_error": 1.8181929438114166,
              "improvement_over_seed0": 0.10465738129615776,
              "gap_to_oracle": 0.002878426074981677,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8860321125984192
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.203177969998274
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5064120512962342
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6876549702336285
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8927852801799774
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5186266899108896,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8048136490186055,
                  "rejected_mean_error": 2.6845299606323243,
                  "gap_rejected_minus_accepted": 0.8797163116137188
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2012311220169067,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6870800153041217,
                  "rejected_mean_error": 2.50858666416936,
                  "gap_rejected_minus_accepted": 0.8215066488652385
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8804168701171875,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5064120512962342,
                  "rejected_mean_error": 2.2791585090637208,
                  "gap_rejected_minus_accepted": 0.7727464577674865
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3947460651397705,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2041094072710592,
                  "rejected_mean_error": 2.122833890874205,
                  "gap_rejected_minus_accepted": 0.9187244836031458
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.639814591407776,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8288505967458089,
                  "rejected_mean_error": 2.797632141113281,
                  "gap_rejected_minus_accepted": 0.9687815443674723
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.260239064693451,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.703254753255589,
                  "rejected_mean_error": 2.586088078362601,
                  "gap_rejected_minus_accepted": 0.882833325107012
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9191790223121643,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5211235637664795,
                  "rejected_mean_error": 2.330333938598633,
                  "gap_rejected_minus_accepted": 0.8092103748321535
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4191200137138367,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2138651230978588,
                  "rejected_mean_error": 2.1655544654570797,
                  "gap_rejected_minus_accepted": 0.951689342359221
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9692180293988847,
              "spearman": 0.9546255429586361,
              "auroc_top30_bad": 0.9930285714285714,
              "mae": 0.1925006799780531,
              "mse": 0.09782758520278594,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.89,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9840438112746159,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4033507689833641
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3665400356352329
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7050470422506332
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0838853766123453
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9876243756609753,
              "spearman": 0.9827221907221907,
              "auroc_top30_worst": 0.9953761904761904,
              "pairwise_seed_ranking": 0.8825,
              "predicted_best_mean_error": 2.2459580853581427,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08067433089017895,
              "gap_to_oracle": 0.0045475608110425725,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3254667508602143
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.484883794784546
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6588479607105255
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8616181839307149
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.942051649093628,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0943464556005265,
                  "rejected_mean_error": 4.358092787265778,
                  "gap_rejected_minus_accepted": 2.2637463316652515
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6972503066062927,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8616181839307149,
                  "rejected_mean_error": 3.698029803276062,
                  "gap_rejected_minus_accepted": 1.8364116193453472
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.007302761077881,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6588479607105255,
                  "rejected_mean_error": 2.982594216823578,
                  "gap_rejected_minus_accepted": 1.3237462561130524
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5856520235538483,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.484883794784546,
                  "rejected_mean_error": 2.5993335200945538,
                  "gap_rejected_minus_accepted": 1.1144497253100079
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.949103593826294,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1021911515129936,
                  "rejected_mean_error": 4.346603798866272,
                  "gap_rejected_minus_accepted": 2.244412647353278
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.699414908885956,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8688090626398723,
                  "rejected_mean_error": 3.7001024770736692,
                  "gap_rejected_minus_accepted": 1.831293414433797
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.007302761077881,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6742740368843079,
                  "rejected_mean_error": 2.978990795612335,
                  "gap_rejected_minus_accepted": 1.3047167587280273
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6131843328475952,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5004814434051514,
                  "rejected_mean_error": 2.6020160738627114,
                  "gap_rejected_minus_accepted": 1.10153463045756
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K20"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 74,
        "best_calib_loss": 0.02932017296552658,
        "train_time_sec": 29.453606128692627,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9992892842773238,
              "spearman": 0.9937207047089068,
              "auroc_top30_bad": 0.9996047142857143,
              "mae": 0.028562404316075846,
              "mse": 0.0016576051079951282,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.979,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8323500592737492,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.018509921129210852
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.07331551418467425
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.32170107363543937
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6981554228390722
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1374262927238248
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9994145360348156,
              "spearman": 0.9988472713138906,
              "auroc_top30_worst": 0.9983133333333334,
              "pairwise_seed_ranking": 0.948,
              "predicted_best_mean_error": 1.654555047661066,
              "seed0_mean_error": 1.7251936940252781,
              "random_seed_mean_error": 1.715085545092821,
              "oracle_best_mean_error": 1.653713216215372,
              "improvement_over_seed0": 0.07063864636421213,
              "gap_to_oracle": 0.0008418314456939413,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5484039169549942
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7880900105476379
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0606226775169372
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2961316965421041
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.714853994178772
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8677912950515756,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4611923354996574,
                  "rejected_mean_error": 3.997808922290802,
                  "gap_rejected_minus_accepted": 2.5366165867911445
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0077885389328003,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2961316965421041,
                  "rejected_mean_error": 2.9710208870887755,
                  "gap_rejected_minus_accepted": 1.6748891905466714
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5849032998085022,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0606226775169372,
                  "rejected_mean_error": 2.3690853108406067,
                  "gap_rejected_minus_accepted": 1.3084626333236695
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1187998056411743,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7880900105476379,
                  "rejected_mean_error": 2.023775322055817,
                  "gap_rejected_minus_accepted": 1.235685311508179
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8714142084121708,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.471304845975505,
                  "rejected_mean_error": 4.010193326473236,
                  "gap_rejected_minus_accepted": 2.5388884804977314
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0268118381500244,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3060115744670233,
                  "rejected_mean_error": 2.9827400527000427,
                  "gap_rejected_minus_accepted": 1.6767284782330194
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5902298092842102,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0670069034695626,
                  "rejected_mean_error": 2.383380484580994,
                  "gap_rejected_minus_accepted": 1.3163735811114312
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.135516881942749,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7901116906404495,
                  "rejected_mean_error": 2.0368876951535544,
                  "gap_rejected_minus_accepted": 1.2467760045131049
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9620617991651992,
              "spearman": 0.9493101019912141,
              "auroc_top30_bad": 0.9927466666666668,
              "mae": 0.20337477150615305,
              "mse": 0.08932817159534137,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.952,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7348791695571826,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22146767604351045
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2792899531364441
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.44714479378461836
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8313518920183182
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2130705400884152
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9444526296071966,
              "spearman": 0.9787527564497643,
              "auroc_top30_worst": 0.985103238095238,
              "pairwise_seed_ranking": 0.9244,
              "predicted_best_mean_error": 1.649030633211136,
              "seed0_mean_error": 1.7480104013681412,
              "random_seed_mean_error": 1.7297815368175506,
              "oracle_best_mean_error": 1.6466209226846695,
              "improvement_over_seed0": 0.09897976815700527,
              "gap_to_oracle": 0.0024097105264664354,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47120265769958497
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7588348061992571
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1338431380271912
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4125380160839065
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7261501743793488
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.449996304512024,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5768151618639628,
                  "rejected_mean_error": 3.070165287017822,
                  "gap_rejected_minus_accepted": 1.4933501251538595
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9963097274303436,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4116076085330838,
                  "rejected_mean_error": 2.6677680152673693,
                  "gap_rejected_minus_accepted": 1.2561604067342855
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5547758340835571,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1338431380271912,
                  "rejected_mean_error": 2.3184572107315065,
                  "gap_rejected_minus_accepted": 1.1846140727043153
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.972128763794899,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.75991483408803,
                  "rejected_mean_error": 2.048916088478797,
                  "gap_rejected_minus_accepted": 1.289001254390767
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.46170060634613,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5907948002550336,
                  "rejected_mean_error": 3.1629508113861085,
                  "gap_rejected_minus_accepted": 1.5721560111310748
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.028306305408478,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4260762306776913,
                  "rejected_mean_error": 2.7035927810366194,
                  "gap_rejected_minus_accepted": 1.277516550358928
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5810441374778748,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1498011543750764,
                  "rejected_mean_error": 2.346219648361206,
                  "gap_rejected_minus_accepted": 1.1964184939861298
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0140965580940247,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7734390672237154,
                  "rejected_mean_error": 2.0763419203579745,
                  "gap_rejected_minus_accepted": 1.3029028531342592
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9637641051915626,
              "spearman": 0.9460840996754677,
              "auroc_top30_bad": 0.9859459047619047,
              "mae": 0.19199985565680544,
              "mse": 0.07783850886434994,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.944,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7879313317349186,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2659718033671379
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31342165002822875
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5611965457916259
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9737861494700114
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.305430052804947
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.927103301873527,
              "spearman": 0.9433520564173162,
              "auroc_top30_worst": 0.9661409523809524,
              "pairwise_seed_ranking": 0.9164,
              "predicted_best_mean_error": 1.8208156888484954,
              "seed0_mean_error": 1.925728751182556,
              "random_seed_mean_error": 1.8916268434524537,
              "oracle_best_mean_error": 1.8181929438114166,
              "improvement_over_seed0": 0.10491306233406061,
              "gap_to_oracle": 0.002622745037078822,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.904233018398285
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.214526589291218
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5002257412910462
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.695563901271393
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8927852801799774
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.331036949157715,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.817652752717336,
                  "rejected_mean_error": 2.56897802734375,
                  "gap_rejected_minus_accepted": 0.7513252746264139
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0812246799468994,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6947168268923316,
                  "rejected_mean_error": 2.4857250269228657,
                  "gap_rejected_minus_accepted": 0.7910082000305341
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8078651428222656,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5002257412910462,
                  "rejected_mean_error": 2.2853448190689085,
                  "gap_rejected_minus_accepted": 0.7851190777778623
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4103157818317413,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2157258482786795,
                  "rejected_mean_error": 2.1189534788833995,
                  "gap_rejected_minus_accepted": 0.90322763060472
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.384237957000732,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.841056105295817,
                  "rejected_mean_error": 2.687782564163208,
                  "gap_rejected_minus_accepted": 0.8467264588673911
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.148321509361267,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7052344357903628,
                  "rejected_mean_error": 2.580211877822876,
                  "gap_rejected_minus_accepted": 0.8749774420325132
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8232669234275818,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5122461433410646,
                  "rejected_mean_error": 2.339211359024048,
                  "gap_rejected_minus_accepted": 0.8269652156829834
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4264423847198486,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.222148541420225,
                  "rejected_mean_error": 2.162763795113181,
                  "gap_rejected_minus_accepted": 0.940615253692956
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.968832801377554,
              "spearman": 0.9600789236465982,
              "auroc_top30_bad": 0.9899440476190476,
              "mae": 0.19893242719693807,
              "mse": 0.09737624685140996,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.975,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9651150614423496,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2653785198181868
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3392386254668236
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7075780675411224
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0857020759582519
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9839963626201681,
              "spearman": 0.9722655242655243,
              "auroc_top30_worst": 0.9907285714285714,
              "pairwise_seed_ranking": 0.8875,
              "predicted_best_mean_error": 2.245077129304409,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08155528694391245,
              "gap_to_oracle": 0.0036666047573090665,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3242247223854064
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5002097063064574
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6616605198383332
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8677866803805034
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8089516162872314,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0946951303217145,
                  "rejected_mean_error": 4.3549547147750856,
                  "gap_rejected_minus_accepted": 2.260259584453371
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.667647361755371,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8677866803805034,
                  "rejected_mean_error": 3.679524313926697,
                  "gap_rejected_minus_accepted": 1.8117376335461934
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9776180982589722,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6616605198383332,
                  "rejected_mean_error": 2.9797816576957703,
                  "gap_rejected_minus_accepted": 1.3181211378574371
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6538609862327576,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.5002097063064574,
                  "rejected_mean_error": 2.594224882920583,
                  "gap_rejected_minus_accepted": 1.0940151766141255
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.7914404630661007,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1027985480096607,
                  "rejected_mean_error": 4.341137230396271,
                  "gap_rejected_minus_accepted": 2.23833868238661
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6589425206184387,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8784610144297282,
                  "rejected_mean_error": 3.6711466217041018,
                  "gap_rejected_minus_accepted": 1.7926856072743735
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9776676297187805,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6746373200416564,
                  "rejected_mean_error": 2.9786275124549864,
                  "gap_rejected_minus_accepted": 1.30399019241333
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6624062061309814,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.516460464000702,
                  "rejected_mean_error": 2.5966897336641948,
                  "gap_rejected_minus_accepted": 1.0802292696634928
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K20"
      }
    ],
    "target_chunk_softmin_l2_K10": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 70,
        "best_calib_loss": 0.1039917841553688,
        "train_time_sec": 10.742870330810547,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9787506423466475,
              "spearman": 0.9144008902589355,
              "auroc_top30_bad": 0.9990864285714285,
              "mae": 0.13836875002738622,
              "mse": 0.04417956542100119,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.52,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6749573140397634,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.1275567743331194
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.13126383172869682
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.04684967875778675
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.282230430217584
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.6930385868519544
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9976573784872742,
              "spearman": 0.9965457481178297,
              "auroc_top30_worst": 0.9981565714285715,
              "pairwise_seed_ranking": 0.8563,
              "predicted_best_mean_error": 1.1556775877475738,
              "seed0_mean_error": 1.2208289574980735,
              "random_seed_mean_error": 1.211028855830431,
              "oracle_best_mean_error": 1.1496094880104064,
              "improvement_over_seed0": 0.06515136975049973,
              "gap_to_oracle": 0.006068099737167376,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05569877469539642
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.29864125254154206
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5695854215502739
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8002481591939926
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2107466048061848
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3581349849700928,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9614099658661418,
                  "rejected_mean_error": 3.454776355266571,
                  "gap_rejected_minus_accepted": 2.493366389400429
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.485951542854309,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.8002481591939926,
                  "rejected_mean_error": 2.442241941642761,
                  "gap_rejected_minus_accepted": 1.6419937824487687
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0862337350845337,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5695854215502739,
                  "rejected_mean_error": 1.8519077880620956,
                  "gap_rejected_minus_accepted": 1.2823223665118215
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6682721674442291,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.29864125254154206,
                  "rejected_mean_error": 1.5147817222277324,
                  "gap_rejected_minus_accepted": 1.2161404696861904
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3743914842605593,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9710722602076001,
                  "rejected_mean_error": 3.4686392331123352,
                  "gap_rejected_minus_accepted": 2.4975669729047354
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5109557509422302,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.809771049896876,
                  "rejected_mean_error": 2.454002680301666,
                  "gap_rejected_minus_accepted": 1.6442316304047901
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0903205871582031,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5755990874767304,
                  "rejected_mean_error": 1.8660588275194168,
                  "gap_rejected_minus_accepted": 1.2904597400426865
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6862597912549973,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.3014462161064148,
                  "rejected_mean_error": 1.5272898712952931,
                  "gap_rejected_minus_accepted": 1.2258436551888783
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8062335892850558,
              "spearman": 0.8221233106159423,
              "auroc_top30_bad": 0.916656761904762,
              "mae": 0.5220203581208198,
              "mse": 0.4781337469771882,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.603368833153063,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.25189824068546296
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28568631598949434
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.46514546999931333
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.782560742576917
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.11107659612298
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6398623627352087,
              "spearman": 0.6758630086803256,
              "auroc_top30_worst": 0.8253866666666667,
              "pairwise_seed_ranking": 0.7396,
              "predicted_best_mean_error": 1.5729663974046708,
              "seed0_mean_error": 1.6396151496171951,
              "random_seed_mean_error": 1.6214258460998534,
              "oracle_best_mean_error": 1.5384068163633347,
              "improvement_over_seed0": 0.06664875221252431,
              "gap_to_oracle": 0.03455958104133616,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1216143016815185
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0353242063369505
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1864477533340454
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3757733899011795
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6178956131458282
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2396049022674567,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5433853329022726,
                  "rejected_mean_error": 2.2884881353378295,
                  "gap_rejected_minus_accepted": 0.7451028024355568
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4475559890270233,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.37543118731571,
                  "rejected_mean_error": 2.3437395971804,
                  "gap_rejected_minus_accepted": 0.9683084098646901
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0605509877204895,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1864477533340454,
                  "rejected_mean_error": 2.049343472957611,
                  "gap_rejected_minus_accepted": 0.8628957196235658
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.39942219108343124,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0326227663804928,
                  "rejected_mean_error": 1.8134029781805667,
                  "gap_rejected_minus_accepted": 0.780780211800074
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2789657354354858,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.56709181216028,
                  "rejected_mean_error": 2.292325186729431,
                  "gap_rejected_minus_accepted": 0.725233374569151
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5216699242591858,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4052871301531153,
                  "rejected_mean_error": 2.335160223264543,
                  "gap_rejected_minus_accepted": 0.9298730931114276
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1034764647483826,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2056042063236236,
                  "rejected_mean_error": 2.0736260929107666,
                  "gap_rejected_minus_accepted": 0.868021886587143
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.3978150561451912,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0238445481610676,
                  "rejected_mean_error": 1.8470672773804895,
                  "gap_rejected_minus_accepted": 0.8232227292194219
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8304477195898499,
              "spearman": 0.8232787137361263,
              "auroc_top30_bad": 0.9274780952380952,
              "mae": 0.5220884093241579,
              "mse": 0.4360070760422307,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.6160617109471695,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3274740437865257
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3080790857791901
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5157639893531799
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8906414859056473
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1814250491917133
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6372396501189774,
              "spearman": 0.665477387185528,
              "auroc_top30_worst": 0.7940144761904762,
              "pairwise_seed_ranking": 0.797,
              "predicted_best_mean_error": 1.7107897831201553,
              "seed0_mean_error": 1.7961009569168092,
              "random_seed_mean_error": 1.7621203367710114,
              "oracle_best_mean_error": 1.6886851382255554,
              "improvement_over_seed0": 0.08531117379665387,
              "gap_to_oracle": 0.022104644894599845,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1176730470657348
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.280584764595215
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4324708611488342
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6252847373612653
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7633036189079285
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7085140466690065,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.69967835521698,
                  "rejected_mean_error": 2.335930992126465,
                  "gap_rejected_minus_accepted": 0.6362526369094847
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.495558738708496,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.624719416191891,
                  "rejected_mean_error": 2.178170704993958,
                  "gap_rejected_minus_accepted": 0.5534512888020671
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2232609987258911,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4324708611488342,
                  "rejected_mean_error": 2.0941363766670227,
                  "gap_rejected_minus_accepted": 0.6616655155181885
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8348844349384308,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2812042466748637,
                  "rejected_mean_error": 1.924346418810756,
                  "gap_rejected_minus_accepted": 0.6431421721358923
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.779377782344818,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7153064907921685,
                  "rejected_mean_error": 2.5232511520385743,
                  "gap_rejected_minus_accepted": 0.8079446612464058
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5045377314090729,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6363140102376275,
                  "rejected_mean_error": 2.270389195472475,
                  "gap_rejected_minus_accepted": 0.6340751852348474
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2441585659980774,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4355641345977783,
                  "rejected_mean_error": 2.1566377792358398,
                  "gap_rejected_minus_accepted": 0.7210736446380615
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8684003949165344,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3027237890258667,
                  "rejected_mean_error": 1.9623189332650945,
                  "gap_rejected_minus_accepted": 0.6595951442392278
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8791401179747489,
              "spearman": 0.8265441733446385,
              "auroc_top30_bad": 0.9217464285714286,
              "mae": 0.6913383386690177,
              "mse": 0.7002651247387706,
              "expert_lt_perturb_large": 0.985,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.7260700146926277,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.48712913438677785
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.545188535541296
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8391278459876775
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1394032566547394
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8595982945886227,
              "spearman": 0.7236526716526717,
              "auroc_top30_worst": 0.8481809523809524,
              "pairwise_seed_ranking": 0.7545,
              "predicted_best_mean_error": 2.2518438467383386,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07478856950998303,
              "gap_to_oracle": 0.010433322191238492,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4765374481678009
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7957633829116821
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.826118710756302
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8757036849657696
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9600374937057494,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.1364444397555458,
                  "rejected_mean_error": 3.9792109298706055,
                  "gap_rejected_minus_accepted": 1.8427664901150598
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8213865756988525,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8757036849657696,
                  "rejected_mean_error": 3.6557733001708983,
                  "gap_rejected_minus_accepted": 1.7800696152051287
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.225718080997467,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.826118710756302,
                  "rejected_mean_error": 2.8153234667778015,
                  "gap_rejected_minus_accepted": 0.9892047560214996
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9268108159303665,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7957633829116821,
                  "rejected_mean_error": 2.4957069907188414,
                  "gap_rejected_minus_accepted": 0.6999436078071593
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.954794287681579,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.142963327301873,
                  "rejected_mean_error": 3.9796542167663573,
                  "gap_rejected_minus_accepted": 1.8366908894644842
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8388993740081787,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8860522476832071,
                  "rejected_mean_error": 3.6483729219436647,
                  "gap_rejected_minus_accepted": 1.7623206742604576
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2317776679992676,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.838979561328888,
                  "rejected_mean_error": 2.8142852711677553,
                  "gap_rejected_minus_accepted": 0.9753057098388673
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9479788839817047,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.8333303236961365,
                  "rejected_mean_error": 2.49106644709905,
                  "gap_rejected_minus_accepted": 0.6577361234029133
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 15,
        "best_calib_loss": 0.06907264143228531,
        "train_time_sec": 36.12504982948303,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9906238602982305,
              "spearman": 0.9812585329371918,
              "auroc_top30_bad": 0.9985956666666665,
              "mae": 0.15010668467583602,
              "mse": 0.03585040115083379,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.962,
              "expert_lt_simvla_seed0": 0.998,
              "same_context_pred_std": 0.6939090090256216,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.32186338090896605
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.2789277509331703
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.054618819099664685
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.28256488311688105
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.6930385868519544
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9982940823722964,
              "spearman": 0.9982779141071164,
              "auroc_top30_worst": 0.998721142857143,
              "pairwise_seed_ranking": 0.8701,
              "predicted_best_mean_error": 1.1544960471093655,
              "seed0_mean_error": 1.2208289574980735,
              "random_seed_mean_error": 1.211028855830431,
              "oracle_best_mean_error": 1.1496094880104064,
              "improvement_over_seed0": 0.06633291038870803,
              "gap_to_oracle": 0.004886559098959076,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.050758403182029725
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2968715948820114
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.568839183151722
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8001211517731349
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2107466048061848
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.54920928478241,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.961454893304242,
                  "rejected_mean_error": 3.4543720083236695,
                  "gap_rejected_minus_accepted": 2.4929171150194276
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5907199084758759,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.8001211517731349,
                  "rejected_mean_error": 2.4426229639053343,
                  "gap_rejected_minus_accepted": 1.6425018121321995
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1439923644065857,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.568839183151722,
                  "rejected_mean_error": 1.8526540264606475,
                  "gap_rejected_minus_accepted": 1.2838148433089254
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.702033132314682,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.2968715948820114,
                  "rejected_mean_error": 1.5153716081142425,
                  "gap_rejected_minus_accepted": 1.218500013232231
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5506457090377808,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9712185776895947,
                  "rejected_mean_error": 3.4673223757743834,
                  "gap_rejected_minus_accepted": 2.4961037980847887
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6020311117172241,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.8092335730393727,
                  "rejected_mean_error": 2.455615110874176,
                  "gap_rejected_minus_accepted": 1.6463815378348032
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1472883820533752,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.574551196694374,
                  "rejected_mean_error": 1.867106718301773,
                  "gap_rejected_minus_accepted": 1.2925555216073992
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7169637382030487,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.2991273810863495,
                  "rejected_mean_error": 1.5280628163019816,
                  "gap_rejected_minus_accepted": 1.228935435215632
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9428770770615453,
              "spearman": 0.9388214755797623,
              "auroc_top30_bad": 0.9726849523809524,
              "mae": 0.3805529387794901,
              "mse": 0.21508986028981586,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.84,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6430750073399206,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10043179517984391
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16205595965385436
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.36579445954561235
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7519063879728317
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.11107659612298
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9093974352035239,
              "spearman": 0.934644645020573,
              "auroc_top30_worst": 0.9539413333333334,
              "pairwise_seed_ranking": 0.9172,
              "predicted_best_mean_error": 1.5405804357528687,
              "seed0_mean_error": 1.6396151496171951,
              "random_seed_mean_error": 1.6214258460998534,
              "oracle_best_mean_error": 1.5384068163633347,
              "improvement_over_seed0": 0.09903471386432638,
              "gap_to_oracle": 0.002173619389534087,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4216065664291382
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7229031693094816
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.066124422931671
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3444536238718134
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6178956131458282
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0655066728591924,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5060887044800653,
                  "rejected_mean_error": 2.624157791137695,
                  "gap_rejected_minus_accepted": 1.11806908665763
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6141934394836426,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.343818044904202,
                  "rejected_mean_error": 2.438377023504946,
                  "gap_rejected_minus_accepted": 1.094558978600744
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2406935095787048,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.066124422931671,
                  "rejected_mean_error": 2.1696668033599855,
                  "gap_rejected_minus_accepted": 1.1035423804283144
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6272199749946594,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7239815223331268,
                  "rejected_mean_error": 1.9165029881985236,
                  "gap_rejected_minus_accepted": 1.1925214658653966
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.096111226081848,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5275338640477922,
                  "rejected_mean_error": 2.6483467197418213,
                  "gap_rejected_minus_accepted": 1.120812855694029
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6548438370227814,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.360584595783509,
                  "rejected_mean_error": 2.4678486982981362,
                  "gap_rejected_minus_accepted": 1.1072641025146273
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2759569883346558,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0815105183124543,
                  "rejected_mean_error": 2.197719780921936,
                  "gap_rejected_minus_accepted": 1.116209262609482
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6467554718255997,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7278384987324004,
                  "rejected_mean_error": 1.9467912405569923,
                  "gap_rejected_minus_accepted": 1.2189527418245918
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9445343162947176,
              "spearman": 0.9299791371486839,
              "auroc_top30_bad": 0.9765340952380952,
              "mae": 0.3563517216120148,
              "mse": 0.18776226318487016,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.916,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6707392673817822,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14352613466978073
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1759916311264038
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4461717905640602
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8464393345912298
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1814250491917133
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8920280231850106,
              "spearman": 0.9003176403952899,
              "auroc_top30_worst": 0.9318095238095239,
              "pairwise_seed_ranking": 0.872,
              "predicted_best_mean_error": 1.6958994610309601,
              "seed0_mean_error": 1.7961009569168092,
              "random_seed_mean_error": 1.7621203367710114,
              "oracle_best_mean_error": 1.6886851382255554,
              "improvement_over_seed0": 0.10020149588584903,
              "gap_to_oracle": 0.007214322805404683,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8266128640174866
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0947461185547023
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3477397441864014
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5743321074859928
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7633036189079285
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9031293749809266,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6911324747933283,
                  "rejected_mean_error": 2.412843915939331,
                  "gap_rejected_minus_accepted": 0.7217114411460028
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6919620037078857,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5735568701266733,
                  "rejected_mean_error": 2.3313314259623565,
                  "gap_rejected_minus_accepted": 0.7577745558356832
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4202058911323547,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3477397441864014,
                  "rejected_mean_error": 2.1788674936294554,
                  "gap_rejected_minus_accepted": 0.831127749443054
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.05199334025383,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.09636282463805,
                  "rejected_mean_error": 1.9860917390855934,
                  "gap_rejected_minus_accepted": 0.8897289144475435
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9562790632247924,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7188175063663058,
                  "rejected_mean_error": 2.491652011871338,
                  "gap_rejected_minus_accepted": 0.7728345055050321
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7253104448318481,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.584992436801686,
                  "rejected_mean_error": 2.4227246594807457,
                  "gap_rejected_minus_accepted": 0.8377322226790596
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4403020143508911,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3619958381652832,
                  "rejected_mean_error": 2.230206075668335,
                  "gap_rejected_minus_accepted": 0.8682102375030518
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0595679581165314,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1019554440937345,
                  "rejected_mean_error": 2.029957466584476,
                  "gap_rejected_minus_accepted": 0.9280020224907415
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9694575876621995,
              "spearman": 0.9667733975858085,
              "auroc_top30_bad": 0.9849988095238096,
              "mae": 0.3734506058945262,
              "mse": 0.1930146162475756,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.975,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8792034143043892,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15901132464408874
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2562853637635708
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7066783974170685
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0875638072490692
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9628206240163045,
              "spearman": 0.9685435045435047,
              "auroc_top30_worst": 0.9784285714285714,
              "pairwise_seed_ranking": 0.8465,
              "predicted_best_mean_error": 2.250591512620449,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07604090362787241,
              "gap_to_oracle": 0.009180988073349106,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.306471666097641
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4981701483726502
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6623996839523316
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.892399517218272
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.647922706604004,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0958327713277605,
                  "rejected_mean_error": 4.344715945720672,
                  "gap_rejected_minus_accepted": 2.248883174392912
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.445559084415436,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.892399517218272,
                  "rejected_mean_error": 3.605685803413391,
                  "gap_rejected_minus_accepted": 1.7132862861951192
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6843690276145935,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6623996839523316,
                  "rejected_mean_error": 2.9790424935817716,
                  "gap_rejected_minus_accepted": 1.31664280962944
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3503004312515259,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4981701483726502,
                  "rejected_mean_error": 2.5949047355651857,
                  "gap_rejected_minus_accepted": 1.0967345871925356
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.642143177986145,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4523350596427917,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.9066586701075237,
                  "rejected_mean_error": 3.5865536546707153,
                  "gap_rejected_minus_accepted": 1.6798949845631916
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6889681220054626,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6717067337036133,
                  "rejected_mean_error": 2.98155809879303,
                  "gap_rejected_minus_accepted": 1.3098513650894166
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3585904836654663,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5173685097694396,
                  "rejected_mean_error": 2.596387051741282,
                  "gap_rejected_minus_accepted": 1.0790185419718423
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 60,
        "best_calib_loss": 0.07577109336853027,
        "train_time_sec": 41.680283308029175,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9804985797336957,
              "spearman": 0.9030216885137622,
              "auroc_top30_bad": 0.9992779047619047,
              "mae": 0.13214436895816895,
              "mse": 0.04021344427158946,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.337,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.68712445134675,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.06557301044464112
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.09415923633575439
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.05161155979037285
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.2820163003404935
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.6930385868519544
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9989312261537169,
              "spearman": 0.998511127684445,
              "auroc_top30_worst": 0.9988954285714285,
              "pairwise_seed_ranking": 0.9355,
              "predicted_best_mean_error": 1.1515810731649399,
              "seed0_mean_error": 1.2208289574980735,
              "random_seed_mean_error": 1.211028855830431,
              "oracle_best_mean_error": 1.1496094880104064,
              "improvement_over_seed0": 0.06924788433313367,
              "gap_to_oracle": 0.0019715851545334395,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04935647016763687
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.29595466215610505
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5689268950581551
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8004237889051438
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2107466048061848
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4090196132659925,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9613420697119501,
                  "rejected_mean_error": 3.4553874206542967,
                  "gap_rejected_minus_accepted": 2.4940453509423466
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5099692642688751,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.8004237889051438,
                  "rejected_mean_error": 2.441715052509308,
                  "gap_rejected_minus_accepted": 1.641291263604164
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.080160677433014,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5689268950581551,
                  "rejected_mean_error": 1.8525663145542144,
                  "gap_rejected_minus_accepted": 1.2836394194960592
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6464979946613312,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.29595466215610505,
                  "rejected_mean_error": 1.5156772523562114,
                  "gap_rejected_minus_accepted": 1.2197225902001063
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4294008493423465,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9711218459738625,
                  "rejected_mean_error": 3.4681929612159728,
                  "gap_rejected_minus_accepted": 2.49707111524211
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5449673533439636,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.8095044926802317,
                  "rejected_mean_error": 2.454802351951599,
                  "gap_rejected_minus_accepted": 1.6452978592713672
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0950197577476501,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5749902740716935,
                  "rejected_mean_error": 1.8666676409244538,
                  "gap_rejected_minus_accepted": 1.2916773668527604
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6666305661201477,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.29895865273475647,
                  "rejected_mean_error": 1.528119059085846,
                  "gap_rejected_minus_accepted": 1.2291604063510895
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9536897085414537,
              "spearman": 0.8929862873744039,
              "auroc_top30_bad": 0.9796647619047619,
              "mae": 0.41191595979657825,
              "mse": 0.2343998665963168,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.388,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6409183930304887,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3384736960232258
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.30813422558307646
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.36953938838243483
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7457454869667689
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.11107659612298
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9634075875351247,
              "spearman": 0.9652620721037263,
              "auroc_top30_worst": 0.979087238095238,
              "pairwise_seed_ranking": 0.9204,
              "predicted_best_mean_error": 1.540847524046898,
              "seed0_mean_error": 1.6396151496171951,
              "random_seed_mean_error": 1.6214258460998534,
              "oracle_best_mean_error": 1.5384068163633347,
              "improvement_over_seed0": 0.09876762557029717,
              "gap_to_oracle": 0.0024407076835633035,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4410007801055908
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7233627799611825
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0579271828651429
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3301427744980305
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6178956131458282
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1280381441116334,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.478195016278161,
                  "rejected_mean_error": 2.875200984954834,
                  "gap_rejected_minus_accepted": 1.3970059686766731
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5910639464855194,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3293770995058651,
                  "rejected_mean_error": 2.481607585288465,
                  "gap_rejected_minus_accepted": 1.1522304857826
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0957174897193909,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0579271828651429,
                  "rejected_mean_error": 2.1778640434265135,
                  "gap_rejected_minus_accepted": 1.1199368605613707
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6578281968832016,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7239623968593609,
                  "rejected_mean_error": 1.9165093769640398,
                  "gap_rejected_minus_accepted": 1.1925469801046789
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1479969024658203,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4973043231169383,
                  "rejected_mean_error": 2.9204125881195067,
                  "gap_rejected_minus_accepted": 1.4231082650025684
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6377004086971283,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.348224438607374,
                  "rejected_mean_error": 2.504536783884442,
                  "gap_rejected_minus_accepted": 1.156312345277068
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1371387839317322,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0748325760364532,
                  "rejected_mean_error": 2.204397723197937,
                  "gap_rejected_minus_accepted": 1.1295651471614836
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6954442113637924,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.728609829194962,
                  "rejected_mean_error": 1.9465313805615838,
                  "gap_rejected_minus_accepted": 1.2179215513666217
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9441806868611182,
              "spearman": 0.9113243723949407,
              "auroc_top30_bad": 0.9823504761904763,
              "mae": 0.3990124781893659,
              "mse": 0.22332273779542838,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.404,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6823974044652141,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2759851594567299
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2891115951061249
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45169480897188186
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8437573037226995
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1814250491917133
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9479113866649802,
              "spearman": 0.9415803714434378,
              "auroc_top30_worst": 0.9892449523809523,
              "pairwise_seed_ranking": 0.898,
              "predicted_best_mean_error": 1.6951988291740419,
              "seed0_mean_error": 1.7961009569168092,
              "random_seed_mean_error": 1.7621203367710114,
              "oracle_best_mean_error": 1.6886851382255554,
              "improvement_over_seed0": 0.1009021277427673,
              "gap_to_oracle": 0.006513690948486417,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8188413352966308
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1070146228258426
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3444656095504761
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.546656522542429
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7633036189079285
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0685596466064458,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.668511958969964,
                  "rejected_mean_error": 2.616428558349609,
                  "gap_rejected_minus_accepted": 0.9479165993796452
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6433121860027313,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5461185496288532,
                  "rejected_mean_error": 2.4134710627242018,
                  "gap_rejected_minus_accepted": 0.8673525130953486
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3877333998680115,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3444656095504761,
                  "rejected_mean_error": 2.1821416282653807,
                  "gap_rejected_minus_accepted": 0.8376760187149046
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.938990518450737,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.108246709211185,
                  "rejected_mean_error": 1.9821219889560402,
                  "gap_rejected_minus_accepted": 0.8738752797448552
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2281934022903442,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6923390293121339,
                  "rejected_mean_error": 2.7299583053588865,
                  "gap_rejected_minus_accepted": 1.0376192760467526
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7050365507602692,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5606354207278572,
                  "rejected_mean_error": 2.4950224690967135,
                  "gap_rejected_minus_accepted": 0.9343870483688563
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4228889346122742,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3562246313095092,
                  "rejected_mean_error": 2.235977282524109,
                  "gap_rejected_minus_accepted": 0.8797526512145999
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9844744950532913,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.113920664030408,
                  "rejected_mean_error": 2.0259264031833504,
                  "gap_rejected_minus_accepted": 0.9120057391529424
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9540774843785522,
              "spearman": 0.9032918998331394,
              "auroc_top30_bad": 0.9855511904761906,
              "mae": 0.48950560217278816,
              "mse": 0.35184118860769176,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.4,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9036354115570916,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6605668447911739
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.59830074685812
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7073678983449936
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.085576519648234
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9829511900826585,
              "spearman": 0.9682633882633883,
              "auroc_top30_worst": 0.9920571428571429,
              "pairwise_seed_ranking": 0.8405,
              "predicted_best_mean_error": 2.2487773045897486,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07785511165857306,
              "gap_to_oracle": 0.0073667800426484575,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.323710604906082
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4994899249076843
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.66393075299263
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.867539115746816
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.359815287590027,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0946225933233897,
                  "rejected_mean_error": 4.35560754776001,
                  "gap_rejected_minus_accepted": 2.26098495443662
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3110822439193726,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.867539115746816,
                  "rejected_mean_error": 3.6802670078277586,
                  "gap_rejected_minus_accepted": 1.8127278920809426
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5889532566070557,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.66393075299263,
                  "rejected_mean_error": 2.9775114245414733,
                  "gap_rejected_minus_accepted": 1.3135806715488434
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2927485406398773,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4994899249076843,
                  "rejected_mean_error": 2.5944648100535077,
                  "gap_rejected_minus_accepted": 1.0949748851458234
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.3390084266662594,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1027985480096607,
                  "rejected_mean_error": 4.341137230396271,
                  "gap_rejected_minus_accepted": 2.23833868238661
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.311582863330841,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8792980114618938,
                  "rejected_mean_error": 3.668635630607605,
                  "gap_rejected_minus_accepted": 1.789337619145711
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5965216159820557,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6750849950313569,
                  "rejected_mean_error": 2.9781798374652864,
                  "gap_rejected_minus_accepted": 1.3030948424339295
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3315836489200592,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.51546480178833,
                  "rejected_mean_error": 2.597021621068319,
                  "gap_rejected_minus_accepted": 1.0815568192799887
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 25,
        "best_calib_loss": 0.07495929300785065,
        "train_time_sec": 29.369190454483032,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9892445706061918,
              "spearman": 0.9737281645215722,
              "auroc_top30_bad": 0.9991545714285714,
              "mae": 0.11714268673289796,
              "mse": 0.03004850775546679,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.975,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6677798405193474,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.28488226793706417
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.2604012945711613
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.055364871519804
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.28221115922530493
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.6930385868519544
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9988585055871015,
              "spearman": 0.9986349873933011,
              "auroc_top30_worst": 0.9988687619047618,
              "pairwise_seed_ranking": 0.9101,
              "predicted_best_mean_error": 1.1529245287775993,
              "seed0_mean_error": 1.2208289574980735,
              "random_seed_mean_error": 1.211028855830431,
              "oracle_best_mean_error": 1.1496094880104064,
              "improvement_over_seed0": 0.0679044287204742,
              "gap_to_oracle": 0.0033150407671929116,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04976298290491104
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2960989952802658
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.568893580019474
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.800114089401563
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2107466048061848
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.456350541114809,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9613540737165345,
                  "rejected_mean_error": 3.455279384613037,
                  "gap_rejected_minus_accepted": 2.4939253108965023
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.515889972448349,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.800114089401563,
                  "rejected_mean_error": 2.44264415102005,
                  "gap_rejected_minus_accepted": 1.6425300616184868
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0875930786132812,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.568893580019474,
                  "rejected_mean_error": 1.8525996295928955,
                  "gap_rejected_minus_accepted": 1.2837060495734214
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.638041228055954,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.2960989952802658,
                  "rejected_mean_error": 1.5156291413148244,
                  "gap_rejected_minus_accepted": 1.2195301460345587
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4637237548828126,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9709777985016504,
                  "rejected_mean_error": 3.4694893884658815,
                  "gap_rejected_minus_accepted": 2.498511589964231
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5168768465518951,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.8093607424894969,
                  "rejected_mean_error": 2.4552336025238035,
                  "gap_rejected_minus_accepted": 1.6458728600343067
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1031018495559692,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.574573321223259,
                  "rejected_mean_error": 1.8670845937728882,
                  "gap_rejected_minus_accepted": 1.2925112725496293
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.645911455154419,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.2984296944141388,
                  "rejected_mean_error": 1.5282953785260518,
                  "gap_rejected_minus_accepted": 1.229865684111913
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9557492640802259,
              "spearman": 0.9390473665422006,
              "auroc_top30_bad": 0.9725097142857143,
              "mae": 0.4053481643678788,
              "mse": 0.23750571484194352,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.936,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5940871677803099,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10736678248643874
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1768051472425461
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3693056614995003
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7503186346769333
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.11107659612298
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9335348024061039,
              "spearman": 0.939713270088493,
              "auroc_top30_worst": 0.970432,
              "pairwise_seed_ranking": 0.9184,
              "predicted_best_mean_error": 1.5404104698896408,
              "seed0_mean_error": 1.6396151496171951,
              "random_seed_mean_error": 1.6214258460998534,
              "oracle_best_mean_error": 1.5384068163633347,
              "improvement_over_seed0": 0.09920467972755431,
              "gap_to_oracle": 0.0020036535263061594,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.43868653392791745
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7452537996264604
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.066130143070221
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3381176009488258
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6178956131458282
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9149663686752318,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4844108976258172,
                  "rejected_mean_error": 2.8192580528259277,
                  "gap_rejected_minus_accepted": 1.3348471552001104
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5158804655075073,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3373013488638235,
                  "rejected_mean_error": 2.457885471395791,
                  "gap_rejected_minus_accepted": 1.1205841225319675
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1050664782524109,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.066130143070221,
                  "rejected_mean_error": 2.1696610832214356,
                  "gap_rejected_minus_accepted": 1.1035309401512146
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7036736905574799,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7458105390064251,
                  "rejected_mean_error": 1.9092111181678486,
                  "gap_rejected_minus_accepted": 1.1634005791614235
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.922126817703247,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5023042203320398,
                  "rejected_mean_error": 2.875413513183594,
                  "gap_rejected_minus_accepted": 1.373109292851554
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5419594049453735,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3517801234110154,
                  "rejected_mean_error": 2.493982608356173,
                  "gap_rejected_minus_accepted": 1.1422024849451575
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1252386569976807,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0848037045001984,
                  "rejected_mean_error": 2.194426594734192,
                  "gap_rejected_minus_accepted": 1.1096228902339937
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7204632610082626,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7620266917205992,
                  "rejected_mean_error": 1.9352732931866365,
                  "gap_rejected_minus_accepted": 1.1732466014660372
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9472141310483109,
              "spearman": 0.929545146372492,
              "auroc_top30_bad": 0.9748937142857143,
              "mae": 0.39968240916197295,
              "mse": 0.21713090465667975,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.948,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6279477575244113,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1838948963880539
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17651117520332335
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4465554477334023
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8495372773885727
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1814250491917133
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9338714905745871,
              "spearman": 0.9305729644626973,
              "auroc_top30_worst": 0.9621150476190476,
              "pairwise_seed_ranking": 0.8984,
              "predicted_best_mean_error": 1.693591187477112,
              "seed0_mean_error": 1.7961009569168092,
              "random_seed_mean_error": 1.7621203367710114,
              "oracle_best_mean_error": 1.6886851382255554,
              "improvement_over_seed0": 0.10250976943969725,
              "gap_to_oracle": 0.004906049251556466,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7953180623054504
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0945148059190848
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3511191987991333
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5564341988644874
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7633036189079285
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9274028778076173,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6741269085142347,
                  "rejected_mean_error": 2.5658940124511718,
                  "gap_rejected_minus_accepted": 0.891767103936937
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5675287246704102,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5558153261115482,
                  "rejected_mean_error": 2.384442693509233,
                  "gap_rejected_minus_accepted": 0.8286273673976849
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3540423512458801,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3511191987991333,
                  "rejected_mean_error": 2.1754880390167237,
                  "gap_rejected_minus_accepted": 0.8243688402175904
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9314317852258682,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.095341790217561,
                  "rejected_mean_error": 1.9864328103487876,
                  "gap_rejected_minus_accepted": 0.8910910201312265
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.002960133552551,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7001590315500896,
                  "rejected_mean_error": 2.659578285217285,
                  "gap_rejected_minus_accepted": 0.9594192536671955
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5951490700244904,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5727700830143403,
                  "rejected_mean_error": 2.4590037096114385,
                  "gap_rejected_minus_accepted": 0.8862336265970983
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3815427422523499,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3649186401367188,
                  "rejected_mean_error": 2.2272832736968993,
                  "gap_rejected_minus_accepted": 0.8623646335601804
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9532853215932846,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0987282139914376,
                  "rejected_mean_error": 2.0310447152285653,
                  "gap_rejected_minus_accepted": 0.9323165012371277
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.971865016482537,
              "spearman": 0.9617412446660297,
              "auroc_top30_bad": 0.9798964285714287,
              "mae": 0.42604653945374305,
              "mse": 0.25232713637048804,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8684727689053813,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15424109861254692
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2782609139680862
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7087470809221268
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0886155534585318
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9811093733791354,
              "spearman": 0.9555850635850637,
              "auroc_top30_worst": 0.9927238095238096,
              "pairwise_seed_ranking": 0.8545,
              "predicted_best_mean_error": 2.2455729058384897,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08105951040983195,
              "gap_to_oracle": 0.004162381291389572,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.323496825695038
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5027108306884767
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.669998286485672
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8669302179018656
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5050065517425537,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0958090054988863,
                  "rejected_mean_error": 4.344929838180542,
                  "gap_rejected_minus_accepted": 2.249120832681656
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3166372776031494,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8669302179018656,
                  "rejected_mean_error": 3.68209370136261,
                  "gap_rejected_minus_accepted": 1.8151634834607442
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.584364652633667,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.669998286485672,
                  "rejected_mean_error": 2.9714438910484313,
                  "gap_rejected_minus_accepted": 1.3014456045627594
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3042913973331451,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.5027108306884767,
                  "rejected_mean_error": 2.5933911747932434,
                  "gap_rejected_minus_accepted": 1.0906803441047668
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.480106687545776,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.315706431865692,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8787243143717447,
                  "rejected_mean_error": 3.670356721878052,
                  "gap_rejected_minus_accepted": 1.7916324075063073
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5844810605049133,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6850526535511017,
                  "rejected_mean_error": 2.9682121789455413,
                  "gap_rejected_minus_accepted": 1.2831595253944397
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3290376663208008,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.529228093624115,
                  "rejected_mean_error": 2.592433857123057,
                  "gap_rejected_minus_accepted": 1.0632057634989422
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      }
    ],
    "target_chunk_mean_top3_l2_K10": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 60,
        "best_calib_loss": 0.07268692553043365,
        "train_time_sec": 10.752551317214966,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9876013509490686,
              "spearman": 0.9568258960193745,
              "auroc_top30_bad": 0.9991926666666667,
              "mae": 0.09076812358605675,
              "mse": 0.027324986456893113,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.499,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8004873950714898,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14584883080469443
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20872633667755872
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3479375765004195
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.717611035810473
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1531497817177792
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9988008949305689,
              "spearman": 0.9982291890411251,
              "auroc_top30_worst": 0.9989417142857143,
              "pairwise_seed_ranking": 0.8507,
              "predicted_best_mean_error": 1.6676366158723832,
              "seed0_mean_error": 1.7323092467486858,
              "random_seed_mean_error": 1.7222694219350816,
              "oracle_best_mean_error": 1.6611087808907032,
              "improvement_over_seed0": 0.0646726308763026,
              "gap_to_oracle": 0.00652783498167997,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.557329802274704
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7965797588348389
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.069236041688919
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3041528829892477
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7220452085018159
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7793939828872687,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.468885741657681,
                  "rejected_mean_error": 4.00048041009903,
                  "gap_rejected_minus_accepted": 2.5315946684413486
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9442317187786102,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3041528829892477,
                  "rejected_mean_error": 2.9757221850395204,
                  "gap_rejected_minus_accepted": 1.6715693020502727
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5310263633728027,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.069236041688919,
                  "rejected_mean_error": 2.3748543753147127,
                  "gap_rejected_minus_accepted": 1.3056183336257936
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0962743163108826,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7965797588348389,
                  "rejected_mean_error": 2.030533691724141,
                  "gap_rejected_minus_accepted": 1.2339539328893023
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7719019651412964,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4787299420767361,
                  "rejected_mean_error": 4.014522988796234,
                  "gap_rejected_minus_accepted": 2.5357930467194976
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.962273895740509,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3140290828943253,
                  "rejected_mean_error": 2.9871497383117678,
                  "gap_rejected_minus_accepted": 1.6731206554174425
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.541788637638092,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0752409936785698,
                  "rejected_mean_error": 2.389377499818802,
                  "gap_rejected_minus_accepted": 1.3141365061402321
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1176143288612366,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7984216970205307,
                  "rejected_mean_error": 2.0436050966580708,
                  "gap_rejected_minus_accepted": 1.24518339963754
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.833586480285937,
              "spearman": 0.8390232306248749,
              "auroc_top30_bad": 0.927472,
              "mae": 0.3917642779439688,
              "mse": 0.302565608701315,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.448,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7204865398587895,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.34964089807868004
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3792938976287842
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.510833581316471
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8718139075358708
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2142092528164388
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6371927411139862,
              "spearman": 0.7008534681942197,
              "auroc_top30_worst": 0.8520015238095237,
              "pairwise_seed_ranking": 0.7996,
              "predicted_best_mean_error": 1.6616709830760956,
              "seed0_mean_error": 1.7485437024831771,
              "random_seed_mean_error": 1.7303086619377137,
              "oracle_best_mean_error": 1.6471324812173844,
              "improvement_over_seed0": 0.08687271940708152,
              "gap_to_oracle": 0.014538501858711195,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9597129335403443
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0094646458060315
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.276816438293457
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4726789764631023
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7266808372974396
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.530571842193604,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.669052697552575,
                  "rejected_mean_error": 2.245334095001221,
                  "gap_rejected_minus_accepted": 0.5762813974486458
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8723436892032623,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4717942604133134,
                  "rejected_mean_error": 2.4897118997269163,
                  "gap_rejected_minus_accepted": 1.017917639313603
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5135715007781982,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.276816438293457,
                  "rejected_mean_error": 2.176545236301422,
                  "gap_rejected_minus_accepted": 0.8997287980079649
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.869492769241333,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0092613874152065,
                  "rejected_mean_error": 1.9663310911001493,
                  "gap_rejected_minus_accepted": 0.9570697036849427
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5547902584075928,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6980482227272458,
                  "rejected_mean_error": 2.2030030202865603,
                  "gap_rejected_minus_accepted": 0.5049547975593145
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9321621358394623,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4918210874585545,
                  "rejected_mean_error": 2.5105616232705494,
                  "gap_rejected_minus_accepted": 1.018740535811995
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5689775943756104,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.278665441274643,
                  "rejected_mean_error": 2.2184219636917115,
                  "gap_rejected_minus_accepted": 0.9397565224170685
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8797096908092499,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0165139819894518,
                  "rejected_mean_error": 1.9951633409382825,
                  "gap_rejected_minus_accepted": 0.9786493589488308
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8776944697372959,
              "spearman": 0.8312172957760796,
              "auroc_top30_bad": 0.9170620952380952,
              "mae": 0.331345119035244,
              "mse": 0.21153152526845706,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.524,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.7432302113927398,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40966503125429155
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4167346745491028
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.610021158528328
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.034860243988037
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3066077157020568
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6973104101165434,
              "spearman": 0.6768963318376525,
              "auroc_top30_worst": 0.7585371428571429,
              "pairwise_seed_ranking": 0.7892,
              "predicted_best_mean_error": 1.8443378665447234,
              "seed0_mean_error": 1.9263914308547974,
              "random_seed_mean_error": 1.8923319072723388,
              "oracle_best_mean_error": 1.8188599121570588,
              "improvement_over_seed0": 0.08205356431007393,
              "gap_to_oracle": 0.025477954387664647,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.064860969543457
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3491041908661525
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6095907686233522
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7793234515545973
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8934757905483246
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.17822597026825,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8387632229063247,
                  "rejected_mean_error": 2.3858888993263245,
                  "gap_rejected_minus_accepted": 0.5471256764199999
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.946009486913681,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7780283909597163,
                  "rejected_mean_error": 2.2390803062496856,
                  "gap_rejected_minus_accepted": 0.46105191528996925
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6870219707489014,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6095907686233522,
                  "rejected_mean_error": 2.1773608124732973,
                  "gap_rejected_minus_accepted": 0.5677700438499451
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3378349840641022,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3513839096306992,
                  "rejected_mean_error": 2.07455877745037,
                  "gap_rejected_minus_accepted": 0.7231748678196708
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.186789035797119,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8623387071821424,
                  "rejected_mean_error": 2.5028659439086915,
                  "gap_rejected_minus_accepted": 0.6405272367265491
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.967104732990265,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.790737175686474,
                  "rejected_mean_error": 2.329047712068709,
                  "gap_rejected_minus_accepted": 0.5383105363822349
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.707514762878418,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.624610694885254,
                  "rejected_mean_error": 2.228172166824341,
                  "gap_rejected_minus_accepted": 0.6035614719390869
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3718200027942657,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.361569296746027,
                  "rejected_mean_error": 2.116679101704276,
                  "gap_rejected_minus_accepted": 0.7551098049582492
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8951436201614287,
              "spearman": 0.8471051007788387,
              "auroc_top30_bad": 0.9339095238095239,
              "mae": 0.4093416676595807,
              "mse": 0.33321603840470776,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.53,
              "expert_lt_simvla_seed0": 0.99,
              "same_context_pred_std": 0.8217310305423343,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6956767137348652
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5855953945219516
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7751500727981329
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1325730541447798
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.871695256919686,
              "spearman": 0.7758590238590239,
              "auroc_top30_worst": 0.8630809523809524,
              "pairwise_seed_ranking": 0.7465,
              "predicted_best_mean_error": 2.2525500521063804,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07408236414194125,
              "gap_to_oracle": 0.011139527559280271,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4015022218227386
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.6958516721725463
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8208530855178833
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.87612988169988
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4692140102386477,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.137639183335834,
                  "rejected_mean_error": 3.96845823764801,
                  "gap_rejected_minus_accepted": 1.830819054312176
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2830452919006348,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.87612988169988,
                  "rejected_mean_error": 3.6544947099685667,
                  "gap_rejected_minus_accepted": 1.7783648282686868
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.626963496208191,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.8208530855178833,
                  "rejected_mean_error": 2.82058909201622,
                  "gap_rejected_minus_accepted": 0.9997360064983367
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3044554591178894,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.6958516721725463,
                  "rejected_mean_error": 2.5290108942985534,
                  "gap_rejected_minus_accepted": 0.8331592221260071
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4637279510498042,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.142963327301873,
                  "rejected_mean_error": 3.9796542167663573,
                  "gap_rejected_minus_accepted": 1.8366908894644842
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3259031772613525,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8860522476832071,
                  "rejected_mean_error": 3.6483729219436647,
                  "gap_rejected_minus_accepted": 1.7623206742604576
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6513340473175049,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8392606985569,
                  "rejected_mean_error": 2.814004133939743,
                  "gap_rejected_minus_accepted": 0.974743435382843
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3157410025596619,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.716785533428192,
                  "rejected_mean_error": 2.529914710521698,
                  "gap_rejected_minus_accepted": 0.8131291770935061
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_mean_top3_l2_K10"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 73,
        "best_calib_loss": 0.02562894858419895,
        "train_time_sec": 35.20534634590149,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997098113924021,
              "spearman": 0.9985253590412381,
              "auroc_top30_bad": 0.9998050952380952,
              "mae": 0.02245804480439983,
              "mse": 0.0008262470808442488,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.985,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8164971212341274,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.045480972124729305
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.10757209578398615
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.34613827801132574
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7172235828107223
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1531497817177792
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997615626328876,
              "spearman": 0.999615606240606,
              "auroc_top30_worst": 0.9997339047619047,
              "pairwise_seed_ranking": 0.9382,
              "predicted_best_mean_error": 1.6621946706473827,
              "seed0_mean_error": 1.7323092467486858,
              "random_seed_mean_error": 1.7222694219350816,
              "oracle_best_mean_error": 1.6611087808907032,
              "improvement_over_seed0": 0.07011457610130312,
              "gap_to_oracle": 0.0010858897566794479,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5557523761987686
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.795094854927063
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0685641571044922
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3038963272094726
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7220452085018159
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.883305287361146,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4687567825317382,
                  "rejected_mean_error": 4.001641042232514,
                  "gap_rejected_minus_accepted": 2.5328842597007757
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0104933977127075,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3038963272094726,
                  "rejected_mean_error": 2.976491852378845,
                  "gap_rejected_minus_accepted": 1.6725955251693725
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6018143892288208,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0685641571044922,
                  "rejected_mean_error": 2.3755262598991393,
                  "gap_rejected_minus_accepted": 1.3069621027946472
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1534791886806488,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.795094854927063,
                  "rejected_mean_error": 2.0310286596934,
                  "gap_rejected_minus_accepted": 1.2359338047663369
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.927722930908203,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4787606321109665,
                  "rejected_mean_error": 4.014246778488159,
                  "gap_rejected_minus_accepted": 2.5354861463771927
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0129860639572144,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.313634751756986,
                  "rejected_mean_error": 2.9883327317237853,
                  "gap_rejected_minus_accepted": 1.6746979799667994
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6071293354034424,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0747329537272454,
                  "rejected_mean_error": 2.3898855397701264,
                  "gap_rejected_minus_accepted": 1.315152586042881
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1745768189430237,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7970844787359238,
                  "rejected_mean_error": 2.044050836086273,
                  "gap_rejected_minus_accepted": 1.2469663573503493
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9588190496673351,
              "spearman": 0.9530671615752736,
              "auroc_top30_bad": 0.9896068571428571,
              "mae": 0.18353028880506753,
              "mse": 0.07159248739903896,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.936,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7711378530283098,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.21820213720202447
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.26353780081272127
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45269087306261063
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8323146067063014
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2142092528164388
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9262753017922652,
              "spearman": 0.9661357617508877,
              "auroc_top30_worst": 0.9778986666666667,
              "pairwise_seed_ranking": 0.94,
              "predicted_best_mean_error": 1.648184506893158,
              "seed0_mean_error": 1.7485437024831771,
              "random_seed_mean_error": 1.7303086619377137,
              "oracle_best_mean_error": 1.6471324812173844,
              "improvement_over_seed0": 0.10035919559001916,
              "gap_to_oracle": 0.0010520256757735602,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4689700875282288
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7688973853603388
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.136833891773224
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4165872915594309
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7266808372974396
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7012211561203006,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5930448769993253,
                  "rejected_mean_error": 2.9294044799804686,
                  "gap_rejected_minus_accepted": 1.3363596029811433
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1150662899017334,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4157197359022997,
                  "rejected_mean_error": 2.6575771695889605,
                  "gap_rejected_minus_accepted": 1.2418574336866608
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6648004651069641,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.136833891773224,
                  "rejected_mean_error": 2.3165277828216553,
                  "gap_rejected_minus_accepted": 1.1796938910484314
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1070508360862732,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7694385049822993,
                  "rejected_mean_error": 2.046442683631099,
                  "gap_rejected_minus_accepted": 1.2770041786488
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.748940634727478,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6053605899545882,
                  "rejected_mean_error": 3.0371917152404784,
                  "gap_rejected_minus_accepted": 1.4318311252858902
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1711897253990173,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4310917087735977,
                  "rejected_mean_error": 2.6908218425417703,
                  "gap_rejected_minus_accepted": 1.2597301337681726
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6858391165733337,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1559947221279143,
                  "rejected_mean_error": 2.3410926828384397,
                  "gap_rejected_minus_accepted": 1.1850979607105254
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1246106028556824,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7814826610542479,
                  "rejected_mean_error": 2.0743450159057577,
                  "gap_rejected_minus_accepted": 1.29286235485151
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9645767055412694,
              "spearman": 0.9501541141196359,
              "auroc_top30_bad": 0.9766720000000001,
              "mae": 0.16776186532229184,
              "mse": 0.05769816098843814,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.948,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.8015332147705322,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.230255177795887
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2817043994665146
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5612690403938293
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.981598129526774
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3066077157020568
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9088230920099041,
              "spearman": 0.9244288929464917,
              "auroc_top30_worst": 0.9401539047619047,
              "pairwise_seed_ranking": 0.9132,
              "predicted_best_mean_error": 1.8220088531970977,
              "seed0_mean_error": 1.9263914308547974,
              "random_seed_mean_error": 1.8923319072723388,
              "oracle_best_mean_error": 1.8188599121570588,
              "improvement_over_seed0": 0.10438257765769965,
              "gap_to_oracle": 0.003148941040038933,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8805799641609192
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2143228942385087
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5105743844032287
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6979913042425347
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8934757905483246
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.508497738838196,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8162619954744974,
                  "rejected_mean_error": 2.5883999462127685,
                  "gap_rejected_minus_accepted": 0.7721379507382711
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1588950157165527,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6977249892187984,
                  "rejected_mean_error": 2.479477390694542,
                  "gap_rejected_minus_accepted": 0.7817524014757438
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8838152289390564,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5105743844032287,
                  "rejected_mean_error": 2.2763771966934203,
                  "gap_rejected_minus_accepted": 0.7658028122901916
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5020817518234253,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2156900607358914,
                  "rejected_mean_error": 2.119886605309575,
                  "gap_rejected_minus_accepted": 0.9041965445736837
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6448341608047485,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8424661668141682,
                  "rejected_mean_error": 2.681718807220459,
                  "gap_rejected_minus_accepted": 0.8392526404062908
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1740762591362,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.708230661198417,
                  "rejected_mean_error": 2.573948001104688,
                  "gap_rejected_minus_accepted": 0.865717339906271
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8986701369285583,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5264347648620606,
                  "rejected_mean_error": 2.3263480968475343,
                  "gap_rejected_minus_accepted": 0.7999133319854737
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5133142471313477,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.221308358131893,
                  "rejected_mean_error": 2.1639327869058294,
                  "gap_rejected_minus_accepted": 0.9426244287739363
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9692736047578092,
              "spearman": 0.9673318967899934,
              "auroc_top30_bad": 0.9905357142857143,
              "mae": 0.19145659241639076,
              "mse": 0.07758340153823522,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.965,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9595632337114351,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24939172588288783
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2899859475791454
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7059002243280411
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0841399411360422
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9814014767170336,
              "spearman": 0.9835292275292277,
              "auroc_top30_worst": 0.991747619047619,
              "pairwise_seed_ranking": 0.8845,
              "predicted_best_mean_error": 2.2436388525366784,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08299356371164324,
              "gap_to_oracle": 0.0022283279895782826,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3023995125293732
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4876755046844483
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6585303990840912
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8742449968655903
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8615788698196414,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.095396581623289,
                  "rejected_mean_error": 4.348641653060913,
                  "gap_rejected_minus_accepted": 2.2532450714376235
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.616753578186035,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8742449968655903,
                  "rejected_mean_error": 3.6601493644714354,
                  "gap_rejected_minus_accepted": 1.785904367605845
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0859687328338623,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6585303990840912,
                  "rejected_mean_error": 2.982911778450012,
                  "gap_rejected_minus_accepted": 1.324381379365921
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7504717707633972,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4876755046844483,
                  "rejected_mean_error": 2.5984029501279196,
                  "gap_rejected_minus_accepted": 1.1107274454434712
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.841065716743469,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6322511434555054,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8853337558110554,
                  "rejected_mean_error": 3.6505283975601195,
                  "gap_rejected_minus_accepted": 1.765194641749064
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0968852043151855,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.674389555454254,
                  "rejected_mean_error": 2.978875277042389,
                  "gap_rejected_minus_accepted": 1.304485721588135
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.762263000011444,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5029146480560303,
                  "rejected_mean_error": 2.601205005645752,
                  "gap_rejected_minus_accepted": 1.0982903575897218
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_mean_top3_l2_K10"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 72,
        "best_calib_loss": 0.02445819228887558,
        "train_time_sec": 41.57349991798401,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9992467592885392,
              "spearman": 0.996473308843089,
              "auroc_top30_bad": 0.9994362857142857,
              "mae": 0.05439027175740339,
              "mse": 0.0051246266946319875,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.97,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8459903408163932,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05089467240741942
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1091296437876299
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.34639195248270405
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7174503923441594
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1531497817177792
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9993091671488726,
              "spearman": 0.9987898679675368,
              "auroc_top30_worst": 0.9994009523809524,
              "pairwise_seed_ranking": 0.961,
              "predicted_best_mean_error": 1.6617538293004035,
              "seed0_mean_error": 1.7323092467486858,
              "random_seed_mean_error": 1.7222694219350816,
              "oracle_best_mean_error": 1.6611087808907032,
              "improvement_over_seed0": 0.07055541744828231,
              "gap_to_oracle": 0.0006450484097002551,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5567567392587661
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7958209314346314
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0690197890758515
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.304073264503479
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7220452085018159
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.98098225593567,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4687709206475152,
                  "rejected_mean_error": 4.001513799190521,
                  "gap_rejected_minus_accepted": 2.5327428785430057
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.080547273159027,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.304073264503479,
                  "rejected_mean_error": 2.975961040496826,
                  "gap_rejected_minus_accepted": 1.6718877759933473
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6346591114997864,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0690197890758515,
                  "rejected_mean_error": 2.37507062792778,
                  "gap_rejected_minus_accepted": 1.3060508388519285
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1611219644546509,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7958209314346314,
                  "rejected_mean_error": 2.030786634190877,
                  "gap_rejected_minus_accepted": 1.2349657027562457
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9997621774673466,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4787299420767361,
                  "rejected_mean_error": 4.014522988796234,
                  "gap_rejected_minus_accepted": 2.5357930467194976
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.105596959590912,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3137067819833756,
                  "rejected_mean_error": 2.9881166410446167,
                  "gap_rejected_minus_accepted": 1.674409859061241
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6619068384170532,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0749695808291435,
                  "rejected_mean_error": 2.3896489126682283,
                  "gap_rejected_minus_accepted": 1.3146793318390848
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1889901161193848,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.798557214140892,
                  "rejected_mean_error": 2.043559924284617,
                  "gap_rejected_minus_accepted": 1.245002710143725
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9667234164101981,
              "spearman": 0.945156040147204,
              "auroc_top30_bad": 0.9920662857142858,
              "mae": 0.17799225647393613,
              "mse": 0.06366012064480876,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.936,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7619887265182859,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.233304059445858
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2906130368232727
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4526299192070961
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8310542133728663
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2142092528164388
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9596198261847828,
              "spearman": 0.9751352468065582,
              "auroc_top30_worst": 0.980056380952381,
              "pairwise_seed_ranking": 0.9276,
              "predicted_best_mean_error": 1.6488250263929367,
              "seed0_mean_error": 1.7485437024831771,
              "random_seed_mean_error": 1.7303086619377137,
              "oracle_best_mean_error": 1.6471324812173844,
              "improvement_over_seed0": 0.09971867609024043,
              "gap_to_oracle": 0.0016925451755522847,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47182087087631225
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7715990591125611
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.137126048183441
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4132207106552652
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7266808372974396
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.568648099899292,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5701686785486009,
                  "rejected_mean_error": 3.1352902660369875,
                  "gap_rejected_minus_accepted": 1.5651215874883866
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.12570583820343,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4124194426241399,
                  "rejected_mean_error": 2.6674569612874772,
                  "gap_rejected_minus_accepted": 1.2550375186633373
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.607511043548584,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.137126048183441,
                  "rejected_mean_error": 2.316235626411438,
                  "gap_rejected_minus_accepted": 1.179109578227997
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0291720032691956,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7734339006792623,
                  "rejected_mean_error": 2.0451080423790717,
                  "gap_rejected_minus_accepted": 1.2716741416998094
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5742639541625976,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.586234966251585,
                  "rejected_mean_error": 3.209322328567505,
                  "gap_rejected_minus_accepted": 1.6230873623159199
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1510602235794067,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4271310362267622,
                  "rejected_mean_error": 2.7025781245458695,
                  "gap_rejected_minus_accepted": 1.2754470883191074
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6316620707511902,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.151501915693283,
                  "rejected_mean_error": 2.345585489273071,
                  "gap_rejected_minus_accepted": 1.1940835735797881
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0679604709148407,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7812227819647107,
                  "rejected_mean_error": 2.0744325687541045,
                  "gap_rejected_minus_accepted": 1.2932097867893937
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9677379418022951,
              "spearman": 0.9497909365210304,
              "auroc_top30_bad": 0.9854339047619047,
              "mae": 0.1708977914262563,
              "mse": 0.05685733962344998,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.96,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8024905401511435,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24945219796895982
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.29899813876152037
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5610412594795227
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9765086462020874
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3066077157020568
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9517632626293229,
              "spearman": 0.9554756630244245,
              "auroc_top30_worst": 0.9704838095238095,
              "pairwise_seed_ranking": 0.9348,
              "predicted_best_mean_error": 1.820172388792038,
              "seed0_mean_error": 1.9263914308547974,
              "random_seed_mean_error": 1.8923319072723388,
              "oracle_best_mean_error": 1.8188599121570588,
              "improvement_over_seed0": 0.10621904206275934,
              "gap_to_oracle": 0.0013124766349792427,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8864448304176331
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.20324479139004
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4987435404777527
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6902719129250248
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8934757905483246
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.544242024421692,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8059941619767084,
                  "rejected_mean_error": 2.680810447692871,
                  "gap_rejected_minus_accepted": 0.8748162857161625
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.221368432044983,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6899852771133088,
                  "rejected_mean_error": 2.5026470719815825,
                  "gap_rejected_minus_accepted": 0.8126617948682737
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8343554735183716,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4987435404777527,
                  "rejected_mean_error": 2.2882080406188963,
                  "gap_rejected_minus_accepted": 0.7894645001411436
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4272200763225555,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.204574432045507,
                  "rejected_mean_error": 2.1235997235380597,
                  "gap_rejected_minus_accepted": 0.9190252914925527
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6556202888488767,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8302882713741726,
                  "rejected_mean_error": 2.79131986618042,
                  "gap_rejected_minus_accepted": 0.9610315948062473
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.287058115005493,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.704817817810385,
                  "rejected_mean_error": 2.5840781870342435,
                  "gap_rejected_minus_accepted": 0.8792603692238585
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8585323691368103,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.510624213218689,
                  "rejected_mean_error": 2.342158648490906,
                  "gap_rejected_minus_accepted": 0.8315344352722169
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4551079869270325,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2130219520084442,
                  "rejected_mean_error": 2.1667244638351195,
                  "gap_rejected_minus_accepted": 0.9537025118266753
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9686816865376107,
              "spearman": 0.9564303647806681,
              "auroc_top30_bad": 0.9880869047619047,
              "mae": 0.19116799867711962,
              "mse": 0.08305848566782631,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.975,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9727553230461488,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.33389170534908774
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3186773639321327
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7075880566835403
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0858553943634033
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9801116119417317,
              "spearman": 0.9562107202107202,
              "auroc_top30_worst": 0.9935571428571429,
              "pairwise_seed_ranking": 0.8805,
              "predicted_best_mean_error": 2.244058835208416,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08257358103990553,
              "gap_to_oracle": 0.002648310661315989,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3189901864528657
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5062828989028931
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6719803392887116
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8648575275739034
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.929066109657288,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0958402094576094,
                  "rejected_mean_error": 4.344649002552033,
                  "gap_rejected_minus_accepted": 2.2488087930944234
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.809944748878479,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8648575275739034,
                  "rejected_mean_error": 3.6883117723464967,
                  "gap_rejected_minus_accepted": 1.8234542447725932
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.048092246055603,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6719803392887116,
                  "rejected_mean_error": 2.9694618382453917,
                  "gap_rejected_minus_accepted": 1.29748149895668
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.73002228140831,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.5062828989028931,
                  "rejected_mean_error": 2.592200485388438,
                  "gap_rejected_minus_accepted": 1.0859175864855448
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.9006222486495967,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7800193428993225,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8757227436701456,
                  "rejected_mean_error": 3.6793614339828493,
                  "gap_rejected_minus_accepted": 1.8036386903127037
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.059959888458252,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6866987812519074,
                  "rejected_mean_error": 2.966566051244736,
                  "gap_rejected_minus_accepted": 1.2798672699928284
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7591967582702637,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5375428366661072,
                  "rejected_mean_error": 2.5896622761090597,
                  "gap_rejected_minus_accepted": 1.0521194394429525
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_mean_top3_l2_K10"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 64,
        "best_calib_loss": 0.025540214031934738,
        "train_time_sec": 29.208784103393555,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993829912679657,
              "spearman": 0.9954155708381591,
              "auroc_top30_bad": 0.9995865714285714,
              "mae": 0.03152328489343636,
              "mse": 0.0020234621514515425,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.995,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8249706689269434,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05550306095695123
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.10781384675670415
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3461709778108634
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7174362704302495
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1531497817177792
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9992173002539346,
              "spearman": 0.9990463509618311,
              "auroc_top30_worst": 0.9991737142857142,
              "pairwise_seed_ranking": 0.9464,
              "predicted_best_mean_error": 1.662069745004177,
              "seed0_mean_error": 1.7323092467486858,
              "random_seed_mean_error": 1.7222694219350816,
              "oracle_best_mean_error": 1.6611087808907032,
              "improvement_over_seed0": 0.07023950174450877,
              "gap_to_oracle": 0.0009609641134737945,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.555969043135643
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7950936309814454
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0689099420547485
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3040539602915446
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7220452085018159
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.93342685699463,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4688657947646246,
                  "rejected_mean_error": 4.000659932136536,
                  "gap_rejected_minus_accepted": 2.531794137371911
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0502482652664185,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3040539602915446,
                  "rejected_mean_error": 2.9760189531326295,
                  "gap_rejected_minus_accepted": 1.671964992841085
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.598857820034027,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0689099420547485,
                  "rejected_mean_error": 2.375180474948883,
                  "gap_rejected_minus_accepted": 1.3062705328941346
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1315825581550598,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7950936309814454,
                  "rejected_mean_error": 2.0310290676752727,
                  "gap_rejected_minus_accepted": 1.2359354366938273
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.952242994308472,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4787439348631435,
                  "rejected_mean_error": 4.014397053718567,
                  "gap_rejected_minus_accepted": 2.5356531188554237
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0569481253623962,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.313752221226692,
                  "rejected_mean_error": 2.987980323314667,
                  "gap_rejected_minus_accepted": 1.6742281020879748
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6024328470230103,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0750739941000937,
                  "rejected_mean_error": 2.3895444993972776,
                  "gap_rejected_minus_accepted": 1.314470505297184
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1427004039287567,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7971025117635727,
                  "rejected_mean_error": 2.044044825077057,
                  "gap_rejected_minus_accepted": 1.2469423133134843
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9662833476950485,
              "spearman": 0.9546828439577125,
              "auroc_top30_bad": 0.9928678095238095,
              "mae": 0.1846253928784281,
              "mse": 0.07532751548689505,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7176391874627778,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.21552945476770402
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2718299900531769
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45208422030210493
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8314631524165471
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2142092528164388
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9533706170273377,
              "spearman": 0.9796474954543971,
              "auroc_top30_worst": 0.9857371428571429,
              "pairwise_seed_ranking": 0.934,
              "predicted_best_mean_error": 1.6482876875400543,
              "seed0_mean_error": 1.7485437024831771,
              "random_seed_mean_error": 1.7303086619377137,
              "oracle_best_mean_error": 1.6471324812173844,
              "improvement_over_seed0": 0.10025601494312286,
              "gap_to_oracle": 0.001155206322669855,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4723486332893372
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7666788842433538
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1334046792030334
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4114339621717742
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7266808372974396
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.444294548034668,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5715724364916484,
                  "rejected_mean_error": 3.1226564445495604,
                  "gap_rejected_minus_accepted": 1.551084008057912
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9985352456569672,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4105798435440187,
                  "rejected_mean_error": 2.6729640039011313,
                  "gap_rejected_minus_accepted": 1.2623841603571127
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5467936992645264,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1334046792030334,
                  "rejected_mean_error": 2.3199569953918457,
                  "gap_rejected_minus_accepted": 1.1865523161888123
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0213465690612793,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.767426140011309,
                  "rejected_mean_error": 2.047114903733468,
                  "gap_rejected_minus_accepted": 1.279688763722159
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4505369901657104,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5878641185495588,
                  "rejected_mean_error": 3.194659957885742,
                  "gap_rejected_minus_accepted": 1.6067958393361832
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0285247564315796,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4245379575114836,
                  "rejected_mean_error": 2.7102750407324896,
                  "gap_rejected_minus_accepted": 1.285737083221006
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5749399662017822,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.149577028989792,
                  "rejected_mean_error": 2.3475103759765625,
                  "gap_rejected_minus_accepted": 1.1979333469867706
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0416235327720642,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7757437366341787,
                  "rejected_mean_error": 2.0762784503360483,
                  "gap_rejected_minus_accepted": 1.3005347137018695
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9650768350754912,
              "spearman": 0.951584517272214,
              "auroc_top30_bad": 0.9812662857142858,
              "mae": 0.18437279298976064,
              "mse": 0.0679304156066742,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7713627133667955,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.20703975820541382
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3011461270332336
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5642430209159851
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9776712285359701
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3066077157020568
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9202460428593562,
              "spearman": 0.935003657602341,
              "auroc_top30_worst": 0.9639100952380953,
              "pairwise_seed_ranking": 0.918,
              "predicted_best_mean_error": 1.821489845275879,
              "seed0_mean_error": 1.9263914308547974,
              "random_seed_mean_error": 1.8923319072723388,
              "oracle_best_mean_error": 1.8188599121570588,
              "improvement_over_seed0": 0.10490158557891838,
              "gap_to_oracle": 0.0026299331188202046,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9162171149253845
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2130265879707458
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.505417726802826
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.695262166419263
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8934757905483246
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3441052436828618,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8168630906740824,
                  "rejected_mean_error": 2.582990089416504,
                  "gap_rejected_minus_accepted": 0.7661269987424217
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1053786277770996,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.694155365260459,
                  "rejected_mean_error": 2.490163453470785,
                  "gap_rejected_minus_accepted": 0.7960080882103258
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8344393372535706,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.505417726802826,
                  "rejected_mean_error": 2.2815338542938233,
                  "gap_rejected_minus_accepted": 0.7761161274909973
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3929488062858582,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2132242542867082,
                  "rejected_mean_error": 2.120710295190679,
                  "gap_rejected_minus_accepted": 0.9074860409039707
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4097837448120116,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8347139528062608,
                  "rejected_mean_error": 2.751488733291626,
                  "gap_rejected_minus_accepted": 0.916774780485365
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1635183095932007,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.704911754730551,
                  "rejected_mean_error": 2.583799358398195,
                  "gap_rejected_minus_accepted": 0.8788876036676441
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.877470314502716,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.523332799911499,
                  "rejected_mean_error": 2.3294500617980956,
                  "gap_rejected_minus_accepted": 0.8061172618865966
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4395439326763153,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.223309698558989,
                  "rejected_mean_error": 2.163258538526647,
                  "gap_rejected_minus_accepted": 0.9399488399676581
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9702604559649277,
              "spearman": 0.9654280209046454,
              "auroc_top30_bad": 0.9891511904761905,
              "mae": 0.18929023358598351,
              "mse": 0.08137854487241868,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.995,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9804222953455701,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17135182224214077
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3234042952656746
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7072731249332428
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.08616184147199
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.979929734538503,
              "spearman": 0.9707151707151708,
              "auroc_top30_worst": 0.9890476190476191,
              "pairwise_seed_ranking": 0.891,
              "predicted_best_mean_error": 2.244485007226467,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08214740902185458,
              "gap_to_oracle": 0.003074482679366941,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3168630051612853
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.502493968963623
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6616862034797668
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8667655742963156
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.9562824726104737,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0958402094576094,
                  "rejected_mean_error": 4.344649002552033,
                  "gap_rejected_minus_accepted": 2.2488087930944234
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.760150134563446,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8667655742963156,
                  "rejected_mean_error": 3.6825876321792603,
                  "gap_rejected_minus_accepted": 1.8158220578829447
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0775009393692017,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6616862034797668,
                  "rejected_mean_error": 2.9797559740543367,
                  "gap_rejected_minus_accepted": 1.3180697705745699
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7148175537586212,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.502493968963623,
                  "rejected_mean_error": 2.5934634620348613,
                  "gap_rejected_minus_accepted": 1.0909694930712384
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.9386560201644896,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.756535530090332,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8771100489298502,
                  "rejected_mean_error": 3.675199518203735,
                  "gap_rejected_minus_accepted": 1.798089469273885
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0868453979492188,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6726912367343902,
                  "rejected_mean_error": 2.980573595762253,
                  "gap_rejected_minus_accepted": 1.3078823590278628
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.730425238609314,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.518658800125122,
                  "rejected_mean_error": 2.595956954956055,
                  "gap_rejected_minus_accepted": 1.0772981548309328
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_mean_top3_l2_K10"
      }
    ]
  }
}
```
