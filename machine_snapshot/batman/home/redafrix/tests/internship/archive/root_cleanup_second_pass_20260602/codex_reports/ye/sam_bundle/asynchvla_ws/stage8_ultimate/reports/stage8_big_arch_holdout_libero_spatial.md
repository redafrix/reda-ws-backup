# Stage 6 Experiments: holdout_libero_spatial

```json
{
  "split": "holdout_libero_spatial",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 152,
      "best_calib_loss": 0.039654023945331573,
      "train_time_sec": 22.31702446937561,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9794176254547633,
            "spearman": 0.9431857716410762,
            "auroc_top30_bad": 0.9992746428571428,
            "mae": 0.10545576210692525,
            "mse": 0.044379175368601385,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.53,
            "expert_lt_simvla_seed0": 0.972,
            "same_context_pred_std": 0.7924810952208057,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.2926503051519394
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.31667732849121094
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.482441627882421
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8229034479449193
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9993424600133918,
            "spearman": 0.9990871794274652,
            "auroc_top30_worst": 0.9993832380952381,
            "pairwise_seed_ranking": 0.8942,
            "predicted_best_mean_error": 1.7767184133529663,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07330729794502266,
            "gap_to_oracle": 0.0030793001055717806,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6045145234465599
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8407930011987687
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1148230959057808
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3617941979487738
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.450148510932924,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681713439424834,
                "rejected_mean_error": 4.288994257926941,
                "gap_rejected_minus_accepted": 2.7208229139844575
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1312448382377625,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3617941979487738,
                "rejected_mean_error": 3.275631947517395,
                "gap_rejected_minus_accepted": 1.9138377495686212
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6241474747657776,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1148230959057808,
                "rejected_mean_error": 2.5656841747760772,
                "gap_rejected_minus_accepted": 1.4508610788702965
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1458740532398224,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8407930011987687,
                "rejected_mean_error": 2.1734071800549826,
                "gap_rejected_minus_accepted": 1.3326141788562138
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4793069839477546,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.146874964237213,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3727611204783121,
                "rejected_mean_error": 3.281819483757019,
                "gap_rejected_minus_accepted": 1.9090583632787068
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6510518193244934,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1212468647956848,
                "rejected_mean_error": 2.578804557800293,
                "gap_rejected_minus_accepted": 1.4575576930046081
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1588796973228455,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8443568954467774,
                "rejected_mean_error": 2.1852486499150596,
                "gap_rejected_minus_accepted": 1.3408917544682821
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.90753754488713,
            "spearman": 0.8908677015129863,
            "auroc_top30_bad": 0.9766841904761905,
            "mae": 0.2471176065146923,
            "mse": 0.1268543220211874,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.476,
            "expert_lt_simvla_seed0": 0.972,
            "same_context_pred_std": 0.7000095452610661,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.31773463463783264
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3103252660036087
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.445614952480793
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7926002957423528
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.790297512222858,
            "spearman": 0.8340108003909124,
            "auroc_top30_worst": 0.9340830476190475,
            "pairwise_seed_ranking": 0.8092,
            "predicted_best_mean_error": 1.5717889623641967,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.08696327698230744,
            "gap_to_oracle": 0.012655801892280438,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6965644381046295
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9335899228851
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.149088644695282
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.392601862263832
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3805233955383303,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5647378007041084,
                "rejected_mean_error": 2.281272162437439,
                "gap_rejected_minus_accepted": 0.7165343617333306
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0345383882522583,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.391785081829816,
                "rejected_mean_error": 2.368646723393815,
                "gap_rejected_minus_accepted": 0.976861641563999
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6065320372581482,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.149088644695282,
                "rejected_mean_error": 2.123693829059601,
                "gap_rejected_minus_accepted": 0.9746051843643189
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2023362219333649,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9321934586515823,
                "rejected_mean_error": 1.8716248596999536,
                "gap_rejected_minus_accepted": 0.9394314010483713
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4448532581329347,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.590990165207121,
                "rejected_mean_error": 2.2686109066009523,
                "gap_rejected_minus_accepted": 0.6776207413938313
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0514720678329468,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4091728774302783,
                "rejected_mean_error": 2.399567170748635,
                "gap_rejected_minus_accepted": 0.9903942933183567
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6574302911758423,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1738196494579316,
                "rejected_mean_error": 2.143684829235077,
                "gap_rejected_minus_accepted": 0.9698651797771454
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2368090152740479,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9363845629351479,
                "rejected_mean_error": 1.902116750650865,
                "gap_rejected_minus_accepted": 0.965732187715717
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8235941085743855,
            "spearman": 0.8135245813030052,
            "auroc_top30_bad": 0.9118826666666668,
            "mae": 0.33974983403384684,
            "mse": 0.24109978768773677,
            "expert_lt_perturb_large": 0.992,
            "expert_lt_other_task": 0.488,
            "expert_lt_simvla_seed0": 0.952,
            "same_context_pred_std": 0.6523613740136995,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46532634752988816
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.44660035494565964
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6472475296676159
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0117928023934364
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.5874369157375257,
            "spearman": 0.6470850297843417,
            "auroc_top30_worst": 0.7770148571428572,
            "pairwise_seed_ranking": 0.7596,
            "predicted_best_mean_error": 1.7709111616611481,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.07268972420692443,
            "gap_to_oracle": 0.031060443401336846,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.285680989742279
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4019072095935161
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.531029458427429
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6856194087691398
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.001210904121399,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7530231476889717,
                "rejected_mean_error": 2.3368324427604676,
                "gap_rejected_minus_accepted": 0.5838092950714959
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8189681768417358,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.685161723016802,
                "rejected_mean_error": 2.189324479323987,
                "gap_rejected_minus_accepted": 0.5041627563071853
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5327906012535095,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.531029458427429,
                "rejected_mean_error": 2.091778695964813,
                "gap_rejected_minus_accepted": 0.5607492375373839
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.300874799489975,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.4016847989429682,
                "rejected_mean_error": 1.9482686813511232,
                "gap_rejected_minus_accepted": 0.546583882408155
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.022264003753662,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7663562721676296,
                "rejected_mean_error": 2.538802409172058,
                "gap_rejected_minus_accepted": 0.7724461370044284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.831027239561081,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.7009185418725652,
                "rejected_mean_error": 2.267118319632515,
                "gap_rejected_minus_accepted": 0.5661997777599499
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5540849566459656,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5279090194702147,
                "rejected_mean_error": 2.15929275226593,
                "gap_rejected_minus_accepted": 0.6313837327957155
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3442338705062866,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.3936704245824663,
                "rejected_mean_error": 1.9951817364616191,
                "gap_rejected_minus_accepted": 0.6015113118791529
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.8064097927411593,
            "spearman": 0.798517893700015,
            "auroc_top30_bad": 0.8880321428571429,
            "mae": 0.40843122997693715,
            "mse": 0.2919344907236216,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.495,
            "expert_lt_simvla_seed0": 0.975,
            "same_context_pred_std": 0.6168604503028625,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4944308666884899
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.4329671059921384
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7635045877285301
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.086757534109056
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.46793997141890376,
            "spearman": 0.5280596280596281,
            "auroc_top30_worst": 0.8001523809523811,
            "pairwise_seed_ranking": 0.703,
            "predicted_best_mean_error": 1.8871573773026467,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.039072686135768864,
            "gap_to_oracle": 0.023855990171432584,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.8495695245265962
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.752564860343933
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.7137921688556672
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8245029609998067
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0462355852127074,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8766754074891407,
                "rejected_mean_error": 2.2575383031368257,
                "gap_rejected_minus_accepted": 0.38086289564768494
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8631557822227478,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8245029609998067,
                "rejected_mean_error": 2.185537905216217,
                "gap_rejected_minus_accepted": 0.36103494421641047
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4914218187332153,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.7137921688556672,
                "rejected_mean_error": 2.1157312252521514,
                "gap_rejected_minus_accepted": 0.4019390563964842
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1831256747245789,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.752564860343933,
                "rejected_mean_error": 1.968827309290568,
                "gap_rejected_minus_accepted": 0.21626244894663493
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0285812616348267,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8912070605489943,
                "rejected_mean_error": 2.241437089443207,
                "gap_rejected_minus_accepted": 0.3502300288942126
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8862740099430084,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8359164428710937,
                "rejected_mean_error": 2.197170925140381,
                "gap_rejected_minus_accepted": 0.36125448226928736
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.525533378124237,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.7227863907814025,
                "rejected_mean_error": 2.1296737360954285,
                "gap_rejected_minus_accepted": 0.40688734531402604
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1827702820301056,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.73918719291687,
                "rejected_mean_error": 1.9885776869455973,
                "gap_rejected_minus_accepted": 0.24939049402872726
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
      "best_epoch": 148,
      "best_calib_loss": 0.014471850357949734,
      "train_time_sec": 28.12689471244812,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998100786977063,
            "spearman": 0.9989680683505158,
            "auroc_top30_bad": 0.9998190952380952,
            "mae": 0.015175012335684733,
            "mse": 0.0004270386777709708,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8055488970161443,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0007317934110760689
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17245466582477093
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4750393141016364
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8226146624078353
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998079382834553,
            "spearman": 0.9996551505381976,
            "auroc_top30_worst": 0.9997579047619047,
            "pairwise_seed_ranking": 0.9308,
            "predicted_best_mean_error": 1.7751469942629337,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07487871703505533,
            "gap_to_oracle": 0.0015078810155391142,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6038790430426597
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8404049053430557
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1145708667397498
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3616696180740993
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4754637002944966,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681211856007575,
                "rejected_mean_error": 4.289445683002472,
                "gap_rejected_minus_accepted": 2.7213244974017146
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1285459995269775,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3616696180740993,
                "rejected_mean_error": 3.2760056871414185,
                "gap_rejected_minus_accepted": 1.9143360690673192
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6328919529914856,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1145708667397498,
                "rejected_mean_error": 2.565936403942108,
                "gap_rejected_minus_accepted": 1.4513655372023582
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1345774233341217,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8404049053430557,
                "rejected_mean_error": 2.17353654534022,
                "gap_rejected_minus_accepted": 1.3331316399971644
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4475727319717415,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771947034200033,
                "rejected_mean_error": 4.3055047821998595,
                "gap_rejected_minus_accepted": 2.728310078779856
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1525411009788513,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3726338240305582,
                "rejected_mean_error": 3.2822013731002806,
                "gap_rejected_minus_accepted": 1.9095675490697224
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6523252725601196,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.121163094997406,
                "rejected_mean_error": 2.578888327598572,
                "gap_rejected_minus_accepted": 1.4577252326011658
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1443473398685455,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8438316326141357,
                "rejected_mean_error": 2.18542373752594,
                "gap_rejected_minus_accepted": 1.3415921049118043
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.976270699908495,
            "spearman": 0.9790113537050954,
            "auroc_top30_bad": 0.9917561904761905,
            "mae": 0.1308098363736819,
            "mse": 0.03493195684178922,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6937926449327951,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05403051209449768
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1710053918838501
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40948767434358596
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.779121324578921
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9497757886186546,
            "spearman": 0.9700149690975803,
            "auroc_top30_worst": 0.9899672380952381,
            "pairwise_seed_ranking": 0.9204,
            "predicted_best_mean_error": 1.5618934313058852,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09685880804061897,
            "gap_to_oracle": 0.002760270833968903,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.49745955276489257
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7860614179800718
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1010381978988648
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3491600862444082
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4483854293823244,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5128558288150364,
                "rejected_mean_error": 2.748209909439087,
                "gap_rejected_minus_accepted": 1.2353540806240504
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0928208231925964,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3478198966196278,
                "rejected_mean_error": 2.5002613513233563,
                "gap_rejected_minus_accepted": 1.1524414547037285
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.604880690574646,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1010381978988648,
                "rejected_mean_error": 2.171744275856018,
                "gap_rejected_minus_accepted": 1.0707060779571531
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2313269674777985,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7863230690026817,
                "rejected_mean_error": 1.9203521083233324,
                "gap_rejected_minus_accepted": 1.1340290393206507
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4452229022979735,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5325476711326176,
                "rejected_mean_error": 2.7945933532714844,
                "gap_rejected_minus_accepted": 1.2620456821388668
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1123839020729065,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3668228300178753,
                "rejected_mean_error": 2.5252728670362443,
                "gap_rejected_minus_accepted": 1.158450037018369
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6277050375938416,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.117502979516983,
                "rejected_mean_error": 2.2000014991760253,
                "gap_rejected_minus_accepted": 1.0824985196590422
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2513343691825867,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8039612131459373,
                "rejected_mean_error": 1.9467299647509733,
                "gap_rejected_minus_accepted": 1.142768751605036
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9708120849812788,
            "spearman": 0.9642595936584266,
            "auroc_top30_bad": 0.9788967619047619,
            "mae": 0.14652176788348006,
            "mse": 0.04253820571091024,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.667730396300772,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0873167600929737
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18539395402669906
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5889983972489834
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.966823649720351
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9356037022640764,
            "spearman": 0.9390594634964521,
            "auroc_top30_worst": 0.9639527619047619,
            "pairwise_seed_ranking": 0.8996,
            "predicted_best_mean_error": 1.7434420199394227,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10015886592864987,
            "gap_to_oracle": 0.003591301679611414,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9160002241134644
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2103019402577326
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.450616261291504
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6198387573649888
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.207553267478943,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.728998355600569,
                "rejected_mean_error": 2.5530555715560914,
                "gap_rejected_minus_accepted": 0.8240572159555224
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.990154653787613,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6190770451643424,
                "rejected_mean_error": 2.38715624656921,
                "gap_rejected_minus_accepted": 0.7680792014048676
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7388207912445068,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.450616261291504,
                "rejected_mean_error": 2.1721918931007385,
                "gap_rejected_minus_accepted": 0.7215756318092346
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4505967795848846,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.2112073867846602,
                "rejected_mean_error": 2.011896674953632,
                "gap_rejected_minus_accepted": 0.8006892881689716
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2365319252014157,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.753295504781935,
                "rejected_mean_error": 2.6563493156433107,
                "gap_rejected_minus_accepted": 0.9030538108613757
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0070577263832092,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6268260555471328,
                "rejected_mean_error": 2.487043636185782,
                "gap_rejected_minus_accepted": 0.8602175806386494
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7574725151062012,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4519609575271606,
                "rejected_mean_error": 2.2352408142089844,
                "gap_rejected_minus_accepted": 0.7832798566818238
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4652891755104065,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2125642753782726,
                "rejected_mean_error": 2.0561961075838875,
                "gap_rejected_minus_accepted": 0.8436318322056149
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9785789483298307,
            "spearman": 0.9610296831246082,
            "auroc_top30_bad": 0.9588654761904762,
            "mae": 0.17164210238582744,
            "mse": 0.04742090054422467,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.99,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6648369509486362,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07630175519734621
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18224355805665254
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6704093523062765
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0575874822959304
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.8928441009357486,
            "spearman": 0.8987534627534629,
            "auroc_top30_worst": 0.9713952380952381,
            "pairwise_seed_ranking": 0.8815,
            "predicted_best_mean_error": 1.8672393283247948,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.05899073511362074,
            "gap_to_oracle": 0.003937941193580707,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.4061189568042756
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.494208598613739
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6516980566978454
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7665791427294413
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.178384780883789,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8511098302735223,
                "rejected_mean_error": 2.4876284980773926,
                "gap_rejected_minus_accepted": 0.6365186678038703
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9123383164405823,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7665791427294413,
                "rejected_mean_error": 2.3593093600273134,
                "gap_rejected_minus_accepted": 0.5927302172978721
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7181103825569153,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6516980566978454,
                "rejected_mean_error": 2.177825337409973,
                "gap_rejected_minus_accepted": 0.5261272807121278
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5189425349235535,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.494208598613739,
                "rejected_mean_error": 2.054946063200633,
                "gap_rejected_minus_accepted": 0.5607374645868939
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.180961561203003,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8658952593803406,
                "rejected_mean_error": 2.4692432999610903,
                "gap_rejected_minus_accepted": 0.6033480405807496
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.919629693031311,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7735810486475627,
                "rejected_mean_error": 2.384177107810974,
                "gap_rejected_minus_accepted": 0.6105960591634114
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7247426509857178,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6586496150493621,
                "rejected_mean_error": 2.193810511827469,
                "gap_rejected_minus_accepted": 0.5351608967781067
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.547251969575882,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5157331681251527,
                "rejected_mean_error": 2.06306236187617,
                "gap_rejected_minus_accepted": 0.5473291937510172
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
      "best_epoch": 156,
      "best_calib_loss": 0.0073221055790781975,
      "train_time_sec": 67.080819606781,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998360877839569,
            "spearman": 0.9991751012418412,
            "auroc_top30_bad": 0.999872619047619,
            "mae": 0.016030804606713356,
            "mse": 0.0004133217952619993,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8126002853719488,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0002508079707622528
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17242182199656964
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47509865348190067
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8224897827933232
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998651620785856,
            "spearman": 0.9997287818451511,
            "auroc_top30_worst": 0.9999169523809524,
            "pairwise_seed_ranking": 0.9645,
            "predicted_best_mean_error": 1.774097257643938,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07592845365405099,
            "gap_to_oracle": 0.0004581443965434584,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6039403234124183
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8405182381868362
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1143955744862557
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3616005051692326
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.46031792163849,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681148606207636,
                "rejected_mean_error": 4.289502607822418,
                "gap_rejected_minus_accepted": 2.7213877472016543
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.133191704750061,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3616005051692326,
                "rejected_mean_error": 3.276213025856018,
                "gap_rejected_minus_accepted": 1.9146125206867854
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6463575959205627,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1143955744862557,
                "rejected_mean_error": 2.5661116961956023,
                "gap_rejected_minus_accepted": 1.4517161217093466
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.162750005722046,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8405182381868362,
                "rejected_mean_error": 2.1734987677256266,
                "gap_rejected_minus_accepted": 1.3329805295387902
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.427792644500734,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1679076552391052,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3725283664067587,
                "rejected_mean_error": 3.28251774597168,
                "gap_rejected_minus_accepted": 1.9099893795649212
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6726491451263428,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1211770787239075,
                "rejected_mean_error": 2.5788743438720703,
                "gap_rejected_minus_accepted": 1.4576972651481628
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1751602590084076,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8438981699943543,
                "rejected_mean_error": 2.1854015583992004,
                "gap_rejected_minus_accepted": 1.341503388404846
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9878102678275337,
            "spearman": 0.9910780852880857,
            "auroc_top30_bad": 0.9971047619047619,
            "mae": 0.08161587860435247,
            "mse": 0.017374811235458202,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7414899284701366,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04258984440565109
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16175684645175933
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40138917413949965
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7748099601507187
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9724421023194911,
            "spearman": 0.9900533491541436,
            "auroc_top30_worst": 0.9966171428571429,
            "pairwise_seed_ranking": 0.9496,
            "predicted_best_mean_error": 1.5597758522033691,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09897638714313506,
            "gap_to_oracle": 0.0006426917314528158,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46576963901519775
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7466117800810398
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0919582365036011
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3455593861750703
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5139278888702394,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5071340249379477,
                "rejected_mean_error": 2.7997061443328857,
                "gap_rejected_minus_accepted": 1.292572119394938
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1022886633872986,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3447308729908636,
                "rejected_mean_error": 2.509508684039497,
                "gap_rejected_minus_accepted": 1.1647778110486333
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7082287073135376,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0919582365036011,
                "rejected_mean_error": 2.1808242372512816,
                "gap_rejected_minus_accepted": 1.0888660007476805
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1092872321605682,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7476143867443925,
                "rejected_mean_error": 1.933282543271939,
                "gap_rejected_minus_accepted": 1.1856681565275464
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.534924364089966,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.523059051434199,
                "rejected_mean_error": 2.879990930557251,
                "gap_rejected_minus_accepted": 1.356931879123052
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1349143981933594,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3627925226713884,
                "rejected_mean_error": 2.5372358428107367,
                "gap_rejected_minus_accepted": 1.1744433201393483
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7373944520950317,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1108080141544343,
                "rejected_mean_error": 2.2066964645385743,
                "gap_rejected_minus_accepted": 1.09588845038414
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1671610176563263,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7606442887631674,
                "rejected_mean_error": 1.9613233670831365,
                "gap_rejected_minus_accepted": 1.2006790783199692
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9881191927275228,
            "spearman": 0.9881264462734362,
            "auroc_top30_bad": 0.9917340952380953,
            "mae": 0.07787772098239511,
            "mse": 0.015738424172242377,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7329844402008431,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.02123147025704384
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1732554763674736
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5719800024449825
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9592778866728147
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9589904889013613,
            "spearman": 0.9786882520557466,
            "auroc_top30_worst": 0.979928380952381,
            "pairwise_seed_ranking": 0.9368,
            "predicted_best_mean_error": 1.741125684738159,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10247520112991348,
            "gap_to_oracle": 0.0012749664783477943,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8756881403923035
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.182454679829952
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4362689415931702
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6119119014694239
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3201657056808473,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7219202953444588,
                "rejected_mean_error": 2.616758113861084,
                "gap_rejected_minus_accepted": 0.8948378185166252
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02699613571167,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.611457206841594,
                "rejected_mean_error": 2.4099670724746898,
                "gap_rejected_minus_accepted": 0.7985098656330958
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.820326805114746,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4362689415931702,
                "rejected_mean_error": 2.1865392127990724,
                "gap_rejected_minus_accepted": 0.7502702712059022
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5428659617900848,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.183435096717871,
                "rejected_mean_error": 2.021173864698461,
                "gap_rejected_minus_accepted": 0.8377387679805899
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4156999826431274,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7455709187189739,
                "rejected_mean_error": 2.725870590209961,
                "gap_rejected_minus_accepted": 0.9802996714909871
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0369988679885864,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6251781235404192,
                "rejected_mean_error": 2.4919351169041226,
                "gap_rejected_minus_accepted": 0.8667569933637034
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.850656807422638,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.44701540184021,
                "rejected_mean_error": 2.2401863698959352,
                "gap_rejected_minus_accepted": 0.7931709680557253
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.570571631193161,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1857695314619277,
                "rejected_mean_error": 2.0652232138230837,
                "gap_rejected_minus_accepted": 0.8794536823611561
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9909967610784052,
            "spearman": 0.9785119396567681,
            "auroc_top30_bad": 0.975247619047619,
            "mae": 0.087068463931093,
            "mse": 0.014659285860428778,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.995,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7364026700457035,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03625380972400308
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16809257770329714
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6625189552344382
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.05514668075492
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9638017553651328,
            "spearman": 0.9442851322851324,
            "auroc_top30_worst": 0.9728619047619047,
            "pairwise_seed_ranking": 0.9145,
            "predicted_best_mean_error": 1.8648408928513527,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.061389170587062836,
            "gap_to_oracle": 0.001539505720138612,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2917470967769622
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4507605319023131
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6480321047306061
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7620900200208027
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.217247796058655,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.843554195827908,
                "rejected_mean_error": 2.5556292080879213,
                "gap_rejected_minus_accepted": 0.7120750122600132
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0305052399635315,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7620900200208027,
                "rejected_mean_error": 2.372776728153229,
                "gap_rejected_minus_accepted": 0.6106867081324261
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8605552315711975,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6480321047306061,
                "rejected_mean_error": 2.1814912893772127,
                "gap_rejected_minus_accepted": 0.5334591846466066
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6544475555419922,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4507605319023131,
                "rejected_mean_error": 2.069428752104441,
                "gap_rejected_minus_accepted": 0.6186682202021281
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.220880389213562,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8532041337754992,
                "rejected_mean_error": 2.583463430404663,
                "gap_rejected_minus_accepted": 0.7302592966291639
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.022578001022339,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7680669260025024,
                "rejected_mean_error": 2.400719475746155,
                "gap_rejected_minus_accepted": 0.6326525497436526
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.872718870639801,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6474029624462128,
                "rejected_mean_error": 2.2050571644306185,
                "gap_rejected_minus_accepted": 0.5576542019844057
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6837716400623322,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.462044427394867,
                "rejected_mean_error": 2.0809586087862653,
                "gap_rejected_minus_accepted": 0.6189141813913983
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
      "best_epoch": 145,
      "best_calib_loss": 0.0066224196925759315,
      "train_time_sec": 70.17680954933167,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998093723750342,
            "spearman": 0.9989770348910031,
            "auroc_top30_bad": 0.9999016666666667,
            "mae": 0.014774009068758096,
            "mse": 0.0005003356471199185,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8082528718067025,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0031277878507971766
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17276524642407895
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47503707225173714
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.822505286342899
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998745106728808,
            "spearman": 0.9998367475774699,
            "auroc_top30_worst": 0.9999081904761905,
            "pairwise_seed_ranking": 0.9657,
            "predicted_best_mean_error": 1.7739406300485134,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07608508124947555,
            "gap_to_oracle": 0.0003015168011188951,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6037812227606774
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.840268371796608
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1144100148797036
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3616338077306747
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4862008333206185,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681104904611904,
                "rejected_mean_error": 4.289541939258576,
                "gap_rejected_minus_accepted": 2.721431448797385
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1313263177871704,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3616338077306747,
                "rejected_mean_error": 3.276113118171692,
                "gap_rejected_minus_accepted": 1.9144793104410174
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.641862690448761,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1144100148797036,
                "rejected_mean_error": 2.5660972558021546,
                "gap_rejected_minus_accepted": 1.451687240922451
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.151303619146347,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.840268371796608,
                "rejected_mean_error": 2.1735820565223696,
                "gap_rejected_minus_accepted": 1.3333136847257616
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.436687707901002,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.150529980659485,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3725591808954876,
                "rejected_mean_error": 3.282425302505493,
                "gap_rejected_minus_accepted": 1.9098661216100055
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6618768572807312,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1211763226985931,
                "rejected_mean_error": 2.5788750998973846,
                "gap_rejected_minus_accepted": 1.4576987771987915
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1634001731872559,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8436630158424377,
                "rejected_mean_error": 2.1854799431165057,
                "gap_rejected_minus_accepted": 1.3418169272740679
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9905512742109515,
            "spearman": 0.9881543328688939,
            "auroc_top30_bad": 0.9974872380952381,
            "mae": 0.08199575140734887,
            "mse": 0.01478068827489216,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7089177572713548,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05917126572132111
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1653617569923401
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4039502362847328
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7740317067861557
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9842065132449034,
            "spearman": 0.9914363644392734,
            "auroc_top30_worst": 0.9985371428571428,
            "pairwise_seed_ranking": 0.9272,
            "predicted_best_mean_error": 1.5603638697862625,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09838836956024166,
            "gap_to_oracle": 0.0012307093143462122,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4689005279541016
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7564276796885026
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0945567712783812
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3428004356081298
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4728570461273196,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4989358887142605,
                "rejected_mean_error": 2.8734893703460695,
                "gap_rejected_minus_accepted": 1.374553481631809
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0582404136657715,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.341999087160654,
                "rejected_mean_error": 2.517686586029613,
                "gap_rejected_minus_accepted": 1.1756874988689592
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5987793803215027,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0945567712783812,
                "rejected_mean_error": 2.1782257024765013,
                "gap_rejected_minus_accepted": 1.08366893119812
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0708981156349182,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7572045040587647,
                "rejected_mean_error": 1.930079014222421,
                "gap_rejected_minus_accepted": 1.1728745101636562
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4937240839004517,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5176937401294708,
                "rejected_mean_error": 2.9282787322998045,
                "gap_rejected_minus_accepted": 1.4105849921703337
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.067657768726349,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3590770687330216,
                "rejected_mean_error": 2.548264253707159,
                "gap_rejected_minus_accepted": 1.1891871849741373
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6057377457618713,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1124467680454253,
                "rejected_mean_error": 2.205057710647583,
                "gap_rejected_minus_accepted": 1.0926109426021577
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1052106022834778,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7687399732688117,
                "rejected_mean_error": 1.958595943960914,
                "gap_rejected_minus_accepted": 1.1898559706921024
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9874777851356547,
            "spearman": 0.9849131091699602,
            "auroc_top30_bad": 0.9935733333333334,
            "mae": 0.09080633417903591,
            "mse": 0.01746708907116768,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.6997458350388807,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06118010383844376
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18225110675096512
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5742196007192135
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9583978711724281
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9740825719418383,
            "spearman": 0.9790116632072264,
            "auroc_top30_worst": 0.986368,
            "pairwise_seed_ranking": 0.9188,
            "predicted_best_mean_error": 1.741853635072708,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10174725079536451,
            "gap_to_oracle": 0.002002916812896771,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8830445713996887
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1887736624250045
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.437555206012726
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6085524385544792
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3477033853530895,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7216954174571568,
                "rejected_mean_error": 2.618782014846802,
                "gap_rejected_minus_accepted": 0.8970865973896451
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.045142710208893,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6079539180819737,
                "rejected_mean_error": 2.4204545535218602,
                "gap_rejected_minus_accepted": 0.8125006354398865
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8011271357536316,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.437555206012726,
                "rejected_mean_error": 2.1852529483795164,
                "gap_rejected_minus_accepted": 0.7476977423667905
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4818956851959229,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1891465436536284,
                "rejected_mean_error": 2.0192659854125568,
                "gap_rejected_minus_accepted": 0.8301194417589284
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4515246629714964,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7450223482979668,
                "rejected_mean_error": 2.7308077239990234,
                "gap_rejected_minus_accepted": 0.9857853757010566
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0673547983169556,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6198875821210483,
                "rejected_mean_error": 2.5076387874663824,
                "gap_rejected_minus_accepted": 0.887751205345334
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8257619142532349,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.445716191291809,
                "rejected_mean_error": 2.241485580444336,
                "gap_rejected_minus_accepted": 0.795769389152527
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.52183797955513,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.196147188307747,
                "rejected_mean_error": 2.0617269978803745,
                "gap_rejected_minus_accepted": 0.8655798095726275
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9872670381031399,
            "spearman": 0.9725797233756079,
            "auroc_top30_bad": 0.9676500000000001,
            "mae": 0.10237867338282512,
            "mse": 0.01891324018938278,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.725200006531805,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0603572409786284
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17314801371842622
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6614718269146979
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0574380845253666
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9379646718789595,
            "spearman": 0.9225797385797385,
            "auroc_top30_worst": 0.9561761904761905,
            "pairwise_seed_ranking": 0.919,
            "predicted_best_mean_error": 1.8646880838274955,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.061541979610920006,
            "gap_to_oracle": 0.001386696696281442,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3069478845596314
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4455937328338624
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6525032300949096
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7670886379877726
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3292526245117187,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8486933498912388,
                "rejected_mean_error": 2.5093768215179444,
                "gap_rejected_minus_accepted": 0.6606834716267056
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0635807514190674,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7670886379877726,
                "rejected_mean_error": 2.3577808742523194,
                "gap_rejected_minus_accepted": 0.5906922362645468
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8038010597229004,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6525032300949096,
                "rejected_mean_error": 2.1770201640129088,
                "gap_rejected_minus_accepted": 0.5245169339179991
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.630044311285019,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4455937328338624,
                "rejected_mean_error": 2.0711510184605917,
                "gap_rejected_minus_accepted": 0.6255572856267293
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3450308799743653,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8608752873208787,
                "rejected_mean_error": 2.5144230484962464,
                "gap_rejected_minus_accepted": 0.6535477611753677
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.058775305747986,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7733531562487284,
                "rejected_mean_error": 2.384860785007477,
                "gap_rejected_minus_accepted": 0.6115076287587486
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8136702179908752,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6569362211227416,
                "rejected_mean_error": 2.195523905754089,
                "gap_rejected_minus_accepted": 0.5385876846313475
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.648589551448822,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.456432433128357,
                "rejected_mean_error": 2.0828292735417686,
                "gap_rejected_minus_accepted": 0.6263968404134117
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
      "best_epoch": 118,
      "best_calib_loss": 0.006089652888476849,
      "train_time_sec": 79.23634839057922,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994777044122158,
            "spearman": 0.9983394210361533,
            "auroc_top30_bad": 0.9994532857142857,
            "mae": 0.02926792887705233,
            "mse": 0.0015540957452965846,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8187698619153557,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0009630484953522682
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17272888947427273
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4752496391519904
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8229534774611393
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.999427783473803,
            "spearman": 0.9990545787381604,
            "auroc_top30_worst": 0.9992660952380952,
            "pairwise_seed_ranking": 0.9631,
            "predicted_best_mean_error": 1.7743850843906404,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07564062690734863,
            "gap_to_oracle": 0.000745971143245816,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.604091782271862
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8407280351877212
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1148855039715766
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3617891509135565
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.515087389945986,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681245109571351,
                "rejected_mean_error": 4.289415754795074,
                "gap_rejected_minus_accepted": 2.721291243837939
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.159403145313263,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3617891509135565,
                "rejected_mean_error": 3.275647088623047,
                "gap_rejected_minus_accepted": 1.9138579377094904
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6715744733810425,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1148855039715766,
                "rejected_mean_error": 2.565621766710281,
                "gap_rejected_minus_accepted": 1.4507362627387046
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1747074127197266,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8407280351877212,
                "rejected_mean_error": 2.173428835391998,
                "gap_rejected_minus_accepted": 1.332700800204277
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4569879293441783,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.189436912536621,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3726406332651775,
                "rejected_mean_error": 3.2821809453964232,
                "gap_rejected_minus_accepted": 1.9095403121312458
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6999289989471436,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1213013045787812,
                "rejected_mean_error": 2.578750118017197,
                "gap_rejected_minus_accepted": 1.4574488134384156
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1880848109722137,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8437692365646362,
                "rejected_mean_error": 2.1854445362091064,
                "gap_rejected_minus_accepted": 1.34167529964447
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9921850930386256,
            "spearman": 0.9873087081563008,
            "auroc_top30_bad": 0.9981653333333333,
            "mae": 0.08399812859436934,
            "mse": 0.012394233934314533,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7174221948008147,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07133283865451813
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16835816299915313
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4029751145005226
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7737791831731796
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9924147894414135,
            "spearman": 0.9951106753988324,
            "auroc_top30_worst": 0.9971260952380951,
            "pairwise_seed_ranking": 0.928,
            "predicted_best_mean_error": 1.560241002202034,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09851123714447008,
            "gap_to_oracle": 0.0011078417301177979,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4723414182662964
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7493566131362548
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0919957414627075
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3430815566577383
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.565470671653748,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4967817976209852,
                "rejected_mean_error": 2.892876190185547,
                "gap_rejected_minus_accepted": 1.396094392564562
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.054976224899292,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3423970624756787,
                "rejected_mean_error": 2.516495203057798,
                "gap_rejected_minus_accepted": 1.1740981405821194
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5731022953987122,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0919957414627075,
                "rejected_mean_error": 2.1807867322921752,
                "gap_rejected_minus_accepted": 1.0887909908294677
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.98625448346138,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7507892083436155,
                "rejected_mean_error": 1.9322220105498933,
                "gap_rejected_minus_accepted": 1.1814328022062779
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5865321159362793,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5153365740511153,
                "rejected_mean_error": 2.949493227005005,
                "gap_rejected_minus_accepted": 1.4341566529538896
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.081552743911743,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3592646480562853,
                "rejected_mean_error": 2.547707470636519,
                "gap_rejected_minus_accepted": 1.1884428225802337
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.602412462234497,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1114664108753205,
                "rejected_mean_error": 2.206038067817688,
                "gap_rejected_minus_accepted": 1.0945716569423674
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0384194254875183,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7638024474893298,
                "rejected_mean_error": 1.9602593884748571,
                "gap_rejected_minus_accepted": 1.1964569409855272
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9867530436086138,
            "spearman": 0.9832070579710965,
            "auroc_top30_bad": 0.9906514285714286,
            "mae": 0.08875242502215842,
            "mse": 0.017256704853734043,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7217011632538078,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.050125860810279844
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19482342621088028
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5740726115643978
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9588405231753985
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9785372312909839,
            "spearman": 0.9758527696606826,
            "auroc_top30_worst": 0.9821318095238095,
            "pairwise_seed_ranking": 0.9328,
            "predicted_best_mean_error": 1.7421752421855927,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10142564368247986,
            "gap_to_oracle": 0.0023245239257814188,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8749765906333923
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1852068429191907
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4405018830299376
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6092948015691884
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4717259645462035,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7205948849254185,
                "rejected_mean_error": 2.6286868076324463,
                "gap_rejected_minus_accepted": 0.9080919227070279
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.103690505027771,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6088885203115204,
                "rejected_mean_error": 2.41765671873245,
                "gap_rejected_minus_accepted": 0.8087681984209296
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7960485219955444,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4405018830299376,
                "rejected_mean_error": 2.1823062713623047,
                "gap_rejected_minus_accepted": 0.7418043883323671
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4693873226642609,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1861417935298273,
                "rejected_mean_error": 2.020269706638544,
                "gap_rejected_minus_accepted": 0.8341279131087167
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.589116835594177,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.740660981602139,
                "rejected_mean_error": 2.7700600242614746,
                "gap_rejected_minus_accepted": 1.0293990426593356
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.158364772796631,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6199491323634265,
                "rejected_mean_error": 2.5074560907151966,
                "gap_rejected_minus_accepted": 0.8875069583517701
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8289395570755005,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4488888778686524,
                "rejected_mean_error": 2.2383128938674925,
                "gap_rejected_minus_accepted": 0.7894240159988402
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4879993498325348,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1900376157155113,
                "rejected_mean_error": 2.0637853030852455,
                "gap_rejected_minus_accepted": 0.8737476873697343
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9889838318203739,
            "spearman": 0.9803340906497334,
            "auroc_top30_bad": 0.9835988095238095,
            "mae": 0.09365371607528232,
            "mse": 0.017492147650594078,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7271652061849972,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07993543174117804
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17297002447396517
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6639566851891577
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0511247805779178
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9657656511663988,
            "spearman": 0.9585468225468226,
            "auroc_top30_worst": 0.9785619047619049,
            "pairwise_seed_ranking": 0.913,
            "predicted_best_mean_error": 1.865155512392521,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06107455104589454,
            "gap_to_oracle": 0.0018541252613069048,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2790154564380645
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4556339979171753
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6421938691139222
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7613815291722617
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3366085052490235,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8432111567921108,
                "rejected_mean_error": 2.558716559410095,
                "gap_rejected_minus_accepted": 0.7155054026179843
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0679051280021667,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7613815291722617,
                "rejected_mean_error": 2.3749022006988527,
                "gap_rejected_minus_accepted": 0.6135206715265911
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8289169073104858,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6421938691139222,
                "rejected_mean_error": 2.1873295249938964,
                "gap_rejected_minus_accepted": 0.5451356558799743
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.584188550710678,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4556339979171753,
                "rejected_mean_error": 2.0678042634328206,
                "gap_rejected_minus_accepted": 0.6121702655156454
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3891310214996335,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8526849495040045,
                "rejected_mean_error": 2.588136088848114,
                "gap_rejected_minus_accepted": 0.7354511393441097
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.073681354522705,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7680793444315592,
                "rejected_mean_error": 2.400682220458984,
                "gap_rejected_minus_accepted": 0.6326028760274249
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8456801176071167,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6482208251953125,
                "rejected_mean_error": 2.2042393016815187,
                "gap_rejected_minus_accepted": 0.5560184764862062
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5785087943077087,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4597622847557068,
                "rejected_mean_error": 2.0817193229993185,
                "gap_rejected_minus_accepted": 0.6219570382436117
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
      "best_epoch": 86,
      "best_calib_loss": 0.008933743461966515,
      "train_time_sec": 55.63628339767456,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9990214322138926,
            "spearman": 0.9976921498243676,
            "auroc_top30_bad": 0.9982618095238095,
            "mae": 0.0350758728368417,
            "mse": 0.0022065502919848307,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8091550183646439,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.001375137485563755
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17284027937352658
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47552869334071873
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8238647496531407
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9984135195635188,
            "spearman": 0.9967683488947339,
            "auroc_top30_worst": 0.9974876190476191,
            "pairwise_seed_ranking": 0.9541,
            "predicted_best_mean_error": 1.774225865662098,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07579984563589104,
            "gap_to_oracle": 0.0005867524147034064,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6050419502854347
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8423169910669327
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1158393860459328
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3626686469157536
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4613972425460826,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5682552396257718,
                "rejected_mean_error": 4.288239196777344,
                "gap_rejected_minus_accepted": 2.719983957151572
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1798295378684998,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3626686469157536,
                "rejected_mean_error": 3.273008600616455,
                "gap_rejected_minus_accepted": 1.9103399537007015
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6571233868598938,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1158393860459328,
                "rejected_mean_error": 2.5646678846359254,
                "gap_rejected_minus_accepted": 1.4488284985899926
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1535395383834839,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8423169910669327,
                "rejected_mean_error": 2.172899183432261,
                "gap_rejected_minus_accepted": 1.3305821923653283
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.436605191230774,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.57722972896364,
                "rejected_mean_error": 4.305189552307129,
                "gap_rejected_minus_accepted": 2.727959823343489
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.209998607635498,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3735821205774943,
                "rejected_mean_error": 3.279356483459473,
                "gap_rejected_minus_accepted": 1.9057743628819785
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6717747449874878,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1229111018180846,
                "rejected_mean_error": 2.577140320777893,
                "gap_rejected_minus_accepted": 1.4542292189598085
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1652450859546661,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8455290770530701,
                "rejected_mean_error": 2.1848579227129616,
                "gap_rejected_minus_accepted": 1.3393288456598915
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9900444714642844,
            "spearman": 0.9871047040172399,
            "auroc_top30_bad": 0.9965074285714286,
            "mae": 0.09682406532158275,
            "mse": 0.01974531762943343,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6943634061809064,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06137496456503868
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16451958391666413
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40356798931360244
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7747941443522771
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9854288507092013,
            "spearman": 0.9906122999118722,
            "auroc_top30_worst": 0.9982049523809524,
            "pairwise_seed_ranking": 0.9292,
            "predicted_best_mean_error": 1.5610228976011276,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09772934174537662,
            "gap_to_oracle": 0.0018897371292112553,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4770189752578735
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7563161997076793
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0934701221466065
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3427958797290127
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.409259080886841,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4987493199242485,
                "rejected_mean_error": 2.875168489456177,
                "gap_rejected_minus_accepted": 1.3764191695319283
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9496975243091583,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.341910482979635,
                "rejected_mean_error": 2.517951832411769,
                "gap_rejected_minus_accepted": 1.1760413494321338
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5766283869743347,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0934701221466065,
                "rejected_mean_error": 2.179312351608276,
                "gap_rejected_minus_accepted": 1.0858422294616696
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0578401982784271,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7572565949001251,
                "rejected_mean_error": 1.9300616135464916,
                "gap_rejected_minus_accepted": 1.1728050186463665
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.418656754493713,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.518961609866884,
                "rejected_mean_error": 2.916867904663086,
                "gap_rejected_minus_accepted": 1.397906294796202
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.974375605583191,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3596927624016522,
                "rejected_mean_error": 2.5464367185320174,
                "gap_rejected_minus_accepted": 1.1867439561303652
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6000863313674927,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.111978884935379,
                "rejected_mean_error": 2.2055255937576295,
                "gap_rejected_minus_accepted": 1.0935467088222504
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0830146968364716,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7734791158683716,
                "rejected_mean_error": 1.956999334422025,
                "gap_rejected_minus_accepted": 1.1835202185536533
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9861978883470157,
            "spearman": 0.9838076375969202,
            "auroc_top30_bad": 0.9929264761904761,
            "mae": 0.10091783513189985,
            "mse": 0.020726274631126328,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.6902687594726791,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.051771349132061
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18335726920366288
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5738957418859005
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9588229873935381
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9692222637621918,
            "spearman": 0.9747333720785487,
            "auroc_top30_worst": 0.9770087619047619,
            "pairwise_seed_ranking": 0.9272,
            "predicted_best_mean_error": 1.7420842595100403,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10151662635803227,
            "gap_to_oracle": 0.0022335412502290097,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8912008481025696
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1873212087994967
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4373043581962586
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6098341708625559
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2846445322036746,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7220530894067552,
                "rejected_mean_error": 2.615562967300415,
                "gap_rejected_minus_accepted": 0.8935098778936599
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9952296614646912,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.609096615711424,
                "rejected_mean_error": 2.4170337622158065,
                "gap_rejected_minus_accepted": 0.8079371465043825
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7498300671577454,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4373043581962586,
                "rejected_mean_error": 2.185503796195984,
                "gap_rejected_minus_accepted": 0.7481994379997254
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4720005095005035,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1876946156398176,
                "rejected_mean_error": 2.0197509944502547,
                "gap_rejected_minus_accepted": 0.8320563788104371
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3762454748153683,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.748798944155375,
                "rejected_mean_error": 2.6968183612823484,
                "gap_rejected_minus_accepted": 0.9480194171269734
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.037082016468048,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6204659913312942,
                "rejected_mean_error": 2.5059219220327953,
                "gap_rejected_minus_accepted": 0.8854559307015011
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7814995646476746,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.445978359222412,
                "rejected_mean_error": 2.2412234125137327,
                "gap_rejected_minus_accepted": 0.7952450532913207
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.497142106294632,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1925926416639299,
                "rejected_mean_error": 2.0629245189421956,
                "gap_rejected_minus_accepted": 0.8703318772782658
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9892629988054563,
            "spearman": 0.9796506693059039,
            "auroc_top30_bad": 0.9784940476190477,
            "mae": 0.11957442213983029,
            "mse": 0.024214243518756125,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7020666552289017,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07093037340790033
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17080275256186725
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6610300455130637
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0533586452032129
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9611320246315371,
            "spearman": 0.9549348937996985,
            "auroc_top30_worst": 0.985,
            "pairwise_seed_ranking": 0.901,
            "predicted_best_mean_error": 1.865505172908306,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06072489053010943,
            "gap_to_oracle": 0.0022037857770920155,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2741482615470887
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4450477333068847
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.643417059659958
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7601981995900473
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2809813976287843,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.847053686512841,
                "rejected_mean_error": 2.524133791923523,
                "gap_rejected_minus_accepted": 0.6770801054106821
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9763924777507782,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7601981995900473,
                "rejected_mean_error": 2.3784521894454955,
                "gap_rejected_minus_accepted": 0.6182539898554482
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.734101951122284,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.643417059659958,
                "rejected_mean_error": 2.1861063344478606,
                "gap_rejected_minus_accepted": 0.5426892747879026
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5596644878387451,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4450477333068847,
                "rejected_mean_error": 2.0713330183029175,
                "gap_rejected_minus_accepted": 0.6262852849960328
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3262417793273924,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8589393973350525,
                "rejected_mean_error": 2.531846058368683,
                "gap_rejected_minus_accepted": 0.6729066610336305
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9651159942150116,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7670949268341065,
                "rejected_mean_error": 2.403635473251343,
                "gap_rejected_minus_accepted": 0.6365405464172365
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.747692584991455,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6492982923984527,
                "rejected_mean_error": 2.203161834478378,
                "gap_rejected_minus_accepted": 0.5538635420799254
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.571177065372467,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.456432433128357,
                "rejected_mean_error": 2.0828292735417686,
                "gap_rejected_minus_accepted": 0.6263968404134117
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
      "best_epoch": 128,
      "best_calib_loss": 0.008082485757768154,
      "train_time_sec": 72.40784931182861,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998026462783611,
            "spearman": 0.998873808418856,
            "auroc_top30_bad": 0.9997732857142857,
            "mae": 0.01918543820416271,
            "mse": 0.0006593376260513978,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8130331124696643,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0008172367140650749
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1725413681000471
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4751248373970389
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8225580363581578
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9997912397795454,
            "spearman": 0.9995800208871908,
            "auroc_top30_worst": 0.9996782857142857,
            "pairwise_seed_ranking": 0.961,
            "predicted_best_mean_error": 1.7740377476215363,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07598796367645266,
            "gap_to_oracle": 0.00039863437414178193,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6041037212014199
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8404547981500625
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1145333953022958
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3616295088847479
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.500618863105777,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.568102427250809,
                "rejected_mean_error": 4.289614508152008,
                "gap_rejected_minus_accepted": 2.721512080901199
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1370331048965454,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3616295088847479,
                "rejected_mean_error": 3.276126014709473,
                "gap_rejected_minus_accepted": 1.914496505824725
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6450260281562805,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1145333953022958,
                "rejected_mean_error": 2.5659738753795622,
                "gap_rejected_minus_accepted": 1.4514404800772664
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1651554107666016,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8404547981500625,
                "rejected_mean_error": 2.1735199144045514,
                "gap_rejected_minus_accepted": 1.3330651162544889
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4681598901748663,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.165264129638672,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3725778725941975,
                "rejected_mean_error": 3.282369227409363,
                "gap_rejected_minus_accepted": 1.9097913548151655
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6709566712379456,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1214210290908813,
                "rejected_mean_error": 2.5786303935050965,
                "gap_rejected_minus_accepted": 1.4572093644142152
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.170205682516098,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8438893666267395,
                "rejected_mean_error": 2.185404492855072,
                "gap_rejected_minus_accepted": 1.3415151262283325
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9885354994980506,
            "spearman": 0.9838938756900875,
            "auroc_top30_bad": 0.9971779047619047,
            "mae": 0.09079689579635052,
            "mse": 0.017695518065492577,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7057710751652607,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0849440204501152
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1744404016494751
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40178936377763746
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7750617166280747
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9853410322111005,
            "spearman": 0.9923593105659589,
            "auroc_top30_worst": 0.9953249523809524,
            "pairwise_seed_ranking": 0.9348,
            "predicted_best_mean_error": 1.5600252636671066,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09872697567939759,
            "gap_to_oracle": 0.0008921031951902858,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46746138429641726
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.748360772545521
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.093020248222351
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3443001400687293
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4411965131759645,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4996887861887613,
                "rejected_mean_error": 2.8667132930755614,
                "gap_rejected_minus_accepted": 1.3670245068868
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02473384141922,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3437287190426122,
                "rejected_mean_error": 2.512508742344646,
                "gap_rejected_minus_accepted": 1.168780023302034
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6064726114273071,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.093020248222351,
                "rejected_mean_error": 2.1797622255325315,
                "gap_rejected_minus_accepted": 1.0867419773101805
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.061466783285141,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7500036920602329,
                "rejected_mean_error": 1.9324844081984514,
                "gap_rejected_minus_accepted": 1.1824807161382185
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4645978927612306,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5197926978270213,
                "rejected_mean_error": 2.9093881130218504,
                "gap_rejected_minus_accepted": 1.389595415194829
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.055661201477051,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3606033154668655,
                "rejected_mean_error": 2.5437339657828923,
                "gap_rejected_minus_accepted": 1.1831306503160268
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.622189998626709,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.112532170534134,
                "rejected_mean_error": 2.2049723081588746,
                "gap_rejected_minus_accepted": 1.0924401376247406
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0874569416046143,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.760949928136099,
                "rejected_mean_error": 1.9612203976687264,
                "gap_rejected_minus_accepted": 1.2002704695326274
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9860495760007961,
            "spearman": 0.9833939907184813,
            "auroc_top30_bad": 0.9938445714285714,
            "mae": 0.0982905239646951,
            "mse": 0.020578710377787548,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6861920714786132,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07494674861431122
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19044732311964035
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5739811495244503
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9580731753945351
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9775889452285091,
            "spearman": 0.9799429451818699,
            "auroc_top30_worst": 0.9847527619047619,
            "pairwise_seed_ranking": 0.9116,
            "predicted_best_mean_error": 1.7424329552650453,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10116793060302731,
            "gap_to_oracle": 0.002582237005233967,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8795703635215759
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.186894582823301
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4354265904426575
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6089839275076445
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.327441906929016,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7195906819767421,
                "rejected_mean_error": 2.637724634170532,
                "gap_rejected_minus_accepted": 0.9181339521937899
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02629691362381,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6083425488899459,
                "rejected_mean_error": 2.419291144361892,
                "gap_rejected_minus_accepted": 0.8109485954719462
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7835087180137634,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4354265904426575,
                "rejected_mean_error": 2.187381563949585,
                "gap_rejected_minus_accepted": 0.7519549735069275
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4564966559410095,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1874734408939227,
                "rejected_mean_error": 2.0198248767292997,
                "gap_rejected_minus_accepted": 0.832351435835377
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4172911405563355,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7439658233854505,
                "rejected_mean_error": 2.74031644821167,
                "gap_rejected_minus_accepted": 0.9963506248262195
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0393856167793274,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.619944766880994,
                "rejected_mean_error": 2.5074690485757496,
                "gap_rejected_minus_accepted": 0.8875242816947555
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8218456506729126,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.443798415184021,
                "rejected_mean_error": 2.243403356552124,
                "gap_rejected_minus_accepted": 0.799604941368103
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4790485501289368,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.190878885132926,
                "rejected_mean_error": 2.0635018807681487,
                "gap_rejected_minus_accepted": 0.8726229956352227
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9868232623765436,
            "spearman": 0.9733318074431365,
            "auroc_top30_bad": 0.9695107142857143,
            "mae": 0.10637185819263635,
            "mse": 0.02136543258481858,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.710388262027561,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07082099761813879
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17368988237529992
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6614640997685493
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0573914725805322
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9514496706985835,
            "spearman": 0.9376322776322776,
            "auroc_top30_worst": 0.9621523809523809,
            "pairwise_seed_ranking": 0.908,
            "predicted_best_mean_error": 1.865369974076748,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.060860089361667535,
            "gap_to_oracle": 0.0020685869455339123,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2781381022930145
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4455453057289123
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6508628044128417
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7652280376752219
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.290816330909729,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8464946977297465,
                "rejected_mean_error": 2.5291646909713745,
                "gap_rejected_minus_accepted": 0.682669993241628
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.000311940908432,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7652280376752219,
                "rejected_mean_error": 2.363362675189972,
                "gap_rejected_minus_accepted": 0.59813463751475
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.768136441707611,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6508628044128417,
                "rejected_mean_error": 2.1786605896949767,
                "gap_rejected_minus_accepted": 0.527797785282135
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.567351073026657,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4455453057289123,
                "rejected_mean_error": 2.0711671608289084,
                "gap_rejected_minus_accepted": 0.6256218550999961
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2950522661209107,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.858786576324039,
                "rejected_mean_error": 2.533221447467804,
                "gap_rejected_minus_accepted": 0.6744348711437649
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9910666346549988,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.774271957874298,
                "rejected_mean_error": 2.3821043801307678,
                "gap_rejected_minus_accepted": 0.6078324222564697
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7726711630821228,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6558426356315612,
                "rejected_mean_error": 2.1966174912452696,
                "gap_rejected_minus_accepted": 0.5407748556137084
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5689839124679565,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4540161156654359,
                "rejected_mean_error": 2.0836347126960755,
                "gap_rejected_minus_accepted": 0.6296185970306396
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
      "best_epoch": 158,
      "best_calib_loss": 0.008546540513634682,
      "train_time_sec": 72.54356837272644,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9992952934532452,
            "spearman": 0.9977604853973435,
            "auroc_top30_bad": 0.9993440000000001,
            "mae": 0.031432575983403606,
            "mse": 0.0018655408065617603,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8105581717536122,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.007885599330067635
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1736366873472929
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47526371404975654
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8227319776048263
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9995352782201143,
            "spearman": 0.9989672832226415,
            "auroc_top30_worst": 0.9989600952380953,
            "pairwise_seed_ranking": 0.958,
            "predicted_best_mean_error": 1.7740065956711768,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07601911562681218,
            "gap_to_oracle": 0.0003674824237822616,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6040525586009026
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8406242467164994
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.114921064388752
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3618544800837835
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4808678388595604,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681364078852866,
                "rejected_mean_error": 4.289308682441711,
                "gap_rejected_minus_accepted": 2.721172274556425
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1470149755477905,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3618544800837835,
                "rejected_mean_error": 3.275451101112366,
                "gap_rejected_minus_accepted": 1.9135966210285824
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6379852294921875,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.114921064388752,
                "rejected_mean_error": 2.5655862062931063,
                "gap_rejected_minus_accepted": 1.4506651419043544
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1581328809261322,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8406242467164994,
                "rejected_mean_error": 2.1734634315490724,
                "gap_rejected_minus_accepted": 1.3328391848325731
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4490347385406515,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1610791087150574,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3727430108388265,
                "rejected_mean_error": 3.2818738126754763,
                "gap_rejected_minus_accepted": 1.9091308018366497
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6596277356147766,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.121312952041626,
                "rejected_mean_error": 2.578738470554352,
                "gap_rejected_minus_accepted": 1.4574255185127258
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1683140695095062,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8438766417503357,
                "rejected_mean_error": 2.1854087344805397,
                "gap_rejected_minus_accepted": 1.341532092730204
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9874973592004104,
            "spearman": 0.9856950317472937,
            "auroc_top30_bad": 0.9979321904761905,
            "mae": 0.09170555809911816,
            "mse": 0.0190227423892205,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7027393099314215,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07814568537473679
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1702032306432724
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4016402360081673
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7742055672089259
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.978507232160419,
            "spearman": 0.9917244322076367,
            "auroc_top30_worst": 0.9969523809523809,
            "pairwise_seed_ranking": 0.9368,
            "predicted_best_mean_error": 1.561632788658142,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09711945068836214,
            "gap_to_oracle": 0.002499628186225733,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5021481819152832
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7466608389065816
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0917063762664796
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3434351209892648
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4571518659591676,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.501792863845825,
                "rejected_mean_error": 2.8477765941619873,
                "gap_rejected_minus_accepted": 1.3459837303161621
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0047897696495056,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3426974944396615,
                "rejected_mean_error": 2.5155958268589105,
                "gap_rejected_minus_accepted": 1.172898332419249
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6084442734718323,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0917063762664796,
                "rejected_mean_error": 2.181076097488403,
                "gap_rejected_minus_accepted": 1.0893697212219235
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0655360221862793,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7478836923361586,
                "rejected_mean_error": 1.9331925831329606,
                "gap_rejected_minus_accepted": 1.1853088907968021
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4735467910766595,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5209694153732725,
                "rejected_mean_error": 2.8987976551055907,
                "gap_rejected_minus_accepted": 1.3778282397323183
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0225601196289062,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3601626764963017,
                "rejected_mean_error": 2.5450418941558355,
                "gap_rejected_minus_accepted": 1.1848792176595337
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6324801445007324,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1097453968524933,
                "rejected_mean_error": 2.207759081840515,
                "gap_rejected_minus_accepted": 1.0980136849880218
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.12276291847229,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7599641448921628,
                "rejected_mean_error": 1.961552506462138,
                "gap_rejected_minus_accepted": 1.2015883615699752
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9870450827570927,
            "spearman": 0.9856242662274336,
            "auroc_top30_bad": 0.9938072380952381,
            "mae": 0.0936904590852696,
            "mse": 0.01945858775651458,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6915840170604002,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04442006134986878
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18191328977346422
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5734867838323117
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.958184686879317
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9740205637620751,
            "spearman": 0.9791892126331309,
            "auroc_top30_worst": 0.9836830476190477,
            "pairwise_seed_ranking": 0.926,
            "predicted_best_mean_error": 1.7421708662509918,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10143001961708076,
            "gap_to_oracle": 0.002320147991180521,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8755257411003112
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1836761826506028
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4360643120765686
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6095381834740832
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.283991479873657,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7224839613702563,
                "rejected_mean_error": 2.6116851196289064,
                "gap_rejected_minus_accepted": 0.8892011582586501
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0166308879852295,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6091188511064747,
                "rejected_mean_error": 2.4169671981098553,
                "gap_rejected_minus_accepted": 0.8078483470033806
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7775165438652039,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4360643120765686,
                "rejected_mean_error": 2.186743842315674,
                "gap_rejected_minus_accepted": 0.7506795302391054
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4688977003097534,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.18480790251741,
                "rejected_mean_error": 2.0207152860268964,
                "gap_rejected_minus_accepted": 0.8359073835094863
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.350795364379883,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7439658233854505,
                "rejected_mean_error": 2.74031644821167,
                "gap_rejected_minus_accepted": 0.9963506248262195
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.017318904399872,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.619724211845806,
                "rejected_mean_error": 2.5081237119341653,
                "gap_rejected_minus_accepted": 0.8883995000883593
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8152248859405518,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4455324783325196,
                "rejected_mean_error": 2.2416692934036253,
                "gap_rejected_minus_accepted": 0.7961368150711057
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4961814284324646,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1902793040351263,
                "rejected_mean_error": 2.0637038786781026,
                "gap_rejected_minus_accepted": 0.8734245746429763
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9877871704462515,
            "spearman": 0.9782077209359697,
            "auroc_top30_bad": 0.9767130952380952,
            "mae": 0.10741397886110314,
            "mse": 0.02102294472509211,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6987810598614632,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07082844067364931
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17007341695576905
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6620847276486457
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0533500287557642
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9563692395415037,
            "spearman": 0.9525434925434927,
            "auroc_top30_worst": 0.9806,
            "pairwise_seed_ranking": 0.922,
            "predicted_best_mean_error": 1.865193861424923,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06103620201349247,
            "gap_to_oracle": 0.001892474293708979,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2754992270469665
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.445430181980133
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.64409650182724
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.763346001625061
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.309126877784729,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.847630263434516,
                "rejected_mean_error": 2.5189445996284485,
                "gap_rejected_minus_accepted": 0.6713143361939324
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0288739800453186,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.763346001625061,
                "rejected_mean_error": 2.3690087833404543,
                "gap_rejected_minus_accepted": 0.6056627817153932
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7835676074028015,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.64409650182724,
                "rejected_mean_error": 2.1854268922805784,
                "gap_rejected_minus_accepted": 0.5413303904533384
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6048763990402222,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.445430181980133,
                "rejected_mean_error": 2.071205535411835,
                "gap_rejected_minus_accepted": 0.6257753534317019
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.33552942276001,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8594001120991177,
                "rejected_mean_error": 2.527699625492096,
                "gap_rejected_minus_accepted": 0.6682995133929783
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.026067614555359,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7689770205815634,
                "rejected_mean_error": 2.397989192008972,
                "gap_rejected_minus_accepted": 0.6290121714274088
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8020001649856567,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.648943910598755,
                "rejected_mean_error": 2.2035162162780764,
                "gap_rejected_minus_accepted": 0.5545723056793215
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.60355144739151,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.455478162765503,
                "rejected_mean_error": 2.08314736366272,
                "gap_rejected_minus_accepted": 0.6276692008972169
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
      "best_epoch": 118,
      "best_calib_loss": 0.00690064299851656,
      "train_time_sec": 79.90927076339722,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994101388787211,
            "spearman": 0.9980532663862756,
            "auroc_top30_bad": 0.9994861428571429,
            "mae": 0.03866822805467236,
            "mse": 0.0027286896831150978,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8249389468755033,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0027518848702311515
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1732020825356245
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47540687389224767
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8229446803877751
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9995535292731281,
            "spearman": 0.999052170194064,
            "auroc_top30_worst": 0.9993542857142858,
            "pairwise_seed_ranking": 0.9627,
            "predicted_best_mean_error": 1.7742490521073342,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.0757766591906548,
            "gap_to_oracle": 0.0006099388599396516,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.605159523665905
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8410040257692337
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1147249081254005
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.361713398273786
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.535454964637757,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681177303857274,
                "rejected_mean_error": 4.289476779937744,
                "gap_rejected_minus_accepted": 2.721359049552017
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.169027030467987,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.361713398273786,
                "rejected_mean_error": 3.2758743465423583,
                "gap_rejected_minus_accepted": 1.9141609482685724
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6605347990989685,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1147249081254005,
                "rejected_mean_error": 2.5657823625564573,
                "gap_rejected_minus_accepted": 1.4510574544310568
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1708572804927826,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8410040257692337,
                "rejected_mean_error": 2.173336838531494,
                "gap_rejected_minus_accepted": 1.3323328127622602
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.5279243230819706,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.213798761367798,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3726886965433756,
                "rejected_mean_error": 3.282036755561829,
                "gap_rejected_minus_accepted": 1.9093480590184533
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6917744278907776,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1214588248729707,
                "rejected_mean_error": 2.578592597723007,
                "gap_rejected_minus_accepted": 1.4571337728500364
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1927312016487122,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8443456263542175,
                "rejected_mean_error": 2.185252406279246,
                "gap_rejected_minus_accepted": 1.3409067799250285
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9909451531867343,
            "spearman": 0.983503754632573,
            "auroc_top30_bad": 0.9979207619047619,
            "mae": 0.08701216510678787,
            "mse": 0.0142251462048034,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7058160567412999,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08165151253342628
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17940480995178223
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40199654895067216
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7748364576101303
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9913691190666273,
            "spearman": 0.9939574458607655,
            "auroc_top30_worst": 0.995992380952381,
            "pairwise_seed_ranking": 0.9264,
            "predicted_best_mean_error": 1.5604667587280274,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09828548061847675,
            "gap_to_oracle": 0.0013335982561111237,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4730659856796265
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7485785778516378
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0919124231338502
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3432267144290624
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4939278125762945,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4984179996914333,
                "rejected_mean_error": 2.8781503715515138,
                "gap_rejected_minus_accepted": 1.3797323718600805
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.00142240524292,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.342446773512768,
                "rejected_mean_error": 2.5163463875889396,
                "gap_rejected_minus_accepted": 1.1738996140761715
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5913277864456177,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0919124231338502,
                "rejected_mean_error": 2.180870050621033,
                "gap_rejected_minus_accepted": 1.0889576274871826
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.063729166984558,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7496319335108748,
                "rejected_mean_error": 1.9326085922176073,
                "gap_rejected_minus_accepted": 1.1829766587067325
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.502194619178772,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.516338670651118,
                "rejected_mean_error": 2.9404743576049803,
                "gap_rejected_minus_accepted": 1.4241356869538624
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0227466821670532,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3598621530647583,
                "rejected_mean_error": 2.5459339240240673,
                "gap_rejected_minus_accepted": 1.186071770959309
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6282885074615479,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1105022366046906,
                "rejected_mean_error": 2.207002242088318,
                "gap_rejected_minus_accepted": 1.0965000054836274
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1240654587745667,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.760949928136099,
                "rejected_mean_error": 1.9612203976687264,
                "gap_rejected_minus_accepted": 1.2002704695326274
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9855504536905157,
            "spearman": 0.9823590479973993,
            "auroc_top30_bad": 0.9921965714285714,
            "mae": 0.09987650158271426,
            "mse": 0.019882954179572303,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7000777169903679,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07254084748029709
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19513404556512834
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5736569531857968
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9585013283054034
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9806934965785183,
            "spearman": 0.9826628082055674,
            "auroc_top30_worst": 0.9865173333333332,
            "pairwise_seed_ranking": 0.9308,
            "predicted_best_mean_error": 1.7419422626495362,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10165862321853636,
            "gap_to_oracle": 0.0020915443897249197,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8814142098426819
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1836358234286308
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.436168194103241
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6081395424378198
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3899405479431155,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7220850182109408,
                "rejected_mean_error": 2.615275608062744,
                "gap_rejected_minus_accepted": 0.8931905898518033
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.041959583759308,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6074225422285155,
                "rejected_mean_error": 2.422045285709369,
                "gap_rejected_minus_accepted": 0.8146227434808533
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7646313905715942,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.436168194103241,
                "rejected_mean_error": 2.1866399602890016,
                "gap_rejected_minus_accepted": 0.7504717661857607
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4479215741157532,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.184021004663108,
                "rejected_mean_error": 2.020978145182069,
                "gap_rejected_minus_accepted": 0.8369571405189611
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5044997930526733,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7419869979222615,
                "rejected_mean_error": 2.758125877380371,
                "gap_rejected_minus_accepted": 1.0161388794581097
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1217042207717896,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6200239486235348,
                "rejected_mean_error": 2.5072340170542398,
                "gap_rejected_minus_accepted": 0.8872100684307049
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7930760979652405,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4442977132797241,
                "rejected_mean_error": 2.242904058456421,
                "gap_rejected_minus_accepted": 0.7986063451766967
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4609909355640411,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1929369389064728,
                "rejected_mean_error": 2.0628085257535314,
                "gap_rejected_minus_accepted": 0.8698715868470586
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9886236982702983,
            "spearman": 0.9800963311829067,
            "auroc_top30_bad": 0.9834547619047619,
            "mae": 0.10279042571295759,
            "mse": 0.01865017350967826,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7196430012217309,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0855351486429572
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17576029808074237
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6641340819634497
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0507566558544834
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9730382841018909,
            "spearman": 0.9690751410751411,
            "auroc_top30_worst": 0.9858047619047621,
            "pairwise_seed_ranking": 0.9075,
            "predicted_best_mean_error": 1.8659982880949975,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06023177534341806,
            "gap_to_oracle": 0.0026969009637833885,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2839660167694091
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4561155452728272
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6389980821609498
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.761464612642924
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.271656632423401,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8409225508901808,
                "rejected_mean_error": 2.579314012527466,
                "gap_rejected_minus_accepted": 0.7383914616372851
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.057624340057373,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.761464612642924,
                "rejected_mean_error": 2.3746529502868654,
                "gap_rejected_minus_accepted": 0.6131883376439413
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8093984127044678,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6389980821609498,
                "rejected_mean_error": 2.190525311946869,
                "gap_rejected_minus_accepted": 0.5515272297859191
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5854566395282745,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4561155452728272,
                "rejected_mean_error": 2.0676437476476033,
                "gap_rejected_minus_accepted": 0.6115282023747761
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3207754373550413,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.851179912355211,
                "rejected_mean_error": 2.601681423187256,
                "gap_rejected_minus_accepted": 0.750501510832045
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0701529383659363,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7703549830118814,
                "rejected_mean_error": 2.3938553047180178,
                "gap_rejected_minus_accepted": 0.6235003217061363
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8428286910057068,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6473669946193694,
                "rejected_mean_error": 2.2050931322574616,
                "gap_rejected_minus_accepted": 0.5577261376380922
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5748911201953888,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.466017804145813,
                "rejected_mean_error": 2.079634149869283,
                "gap_rejected_minus_accepted": 0.6136163457234702
              }
            ]
          }
        }
      }
    },
    {
      "variant": "heteroscedastic_head",
      "feature_mode": "M4_seed_relative",
      "model_kind": "hetero",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 159,
      "best_calib_loss": 0.011430642567574978,
      "train_time_sec": 56.01832675933838,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998099469037675,
            "spearman": 0.9990166251654738,
            "auroc_top30_bad": 0.999918,
            "mae": 0.012548888898640871,
            "mse": 0.0004295460767819845,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8087886366278216,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.004394723169505596
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1724835619300604
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4750802047714591
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8224626633793115
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9999023810865241,
            "spearman": 0.9998623583624943,
            "auroc_top30_worst": 0.9999057142857143,
            "pairwise_seed_ranking": 0.9641,
            "predicted_best_mean_error": 1.7740237270593644,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07600198423862459,
            "gap_to_oracle": 0.00038461381196985833,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6038657117486
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8401692042589187
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1143603150486947
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3616247691869736
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.463855743408204,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.568104995601707,
                "rejected_mean_error": 4.289591392993927,
                "gap_rejected_minus_accepted": 2.72148639739222
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.133719563484192,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3616247691869736,
                "rejected_mean_error": 3.2761402338027956,
                "gap_rejected_minus_accepted": 1.914515464615822
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.639536738395691,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1143603150486947,
                "rejected_mean_error": 2.5661469556331635,
                "gap_rejected_minus_accepted": 1.4517866405844688
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1559174060821533,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8401692042589187,
                "rejected_mean_error": 2.1736151123682657,
                "gap_rejected_minus_accepted": 1.333445908109347
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.415942811965944,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1609004139900208,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3725197118123373,
                "rejected_mean_error": 3.2825437097549437,
                "gap_rejected_minus_accepted": 1.9100239979426064
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6626295447349548,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1210859529972077,
                "rejected_mean_error": 2.5789654695987703,
                "gap_rejected_minus_accepted": 1.4578795166015626
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1635459661483765,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8436643867492676,
                "rejected_mean_error": 2.1854794861475626,
                "gap_rejected_minus_accepted": 1.341815099398295
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9827495640515252,
            "spearman": 0.9848473800366352,
            "auroc_top30_bad": 0.9966255238095237,
            "mae": 0.11071928285686299,
            "mse": 0.025838247430536608,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7479668791140459,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04862683066725731
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17246170897483826
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40878523169755937
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7753711346069971
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9628815811094948,
            "spearman": 0.9830705166531307,
            "auroc_top30_worst": 0.9953371428571429,
            "pairwise_seed_ranking": 0.9236,
            "predicted_best_mean_error": 1.5603677266836167,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.0983845126628875,
            "gap_to_oracle": 0.001234566211700372,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4694941020011902
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7790409404879961
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0927587327957153
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.347583724364543
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.595627570152283,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.509818603515625,
                "rejected_mean_error": 2.7755449371337892,
                "gap_rejected_minus_accepted": 1.2657263336181643
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1157584190368652,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3468442511533087,
                "rejected_mean_error": 2.503182053565979,
                "gap_rejected_minus_accepted": 1.1563378024126703
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7178497910499573,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0927587327957153,
                "rejected_mean_error": 2.1800237409591676,
                "gap_rejected_minus_accepted": 1.0872650081634523
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1814455687999725,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7794623468249751,
                "rejected_mean_error": 1.9226438970550528,
                "gap_rejected_minus_accepted": 1.1431815502300777
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5958266735076903,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.526931145058738,
                "rejected_mean_error": 2.8451420879364013,
                "gap_rejected_minus_accepted": 1.3182109428776634
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1436126828193665,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3633182528503438,
                "rejected_mean_error": 2.5356753421208214,
                "gap_rejected_minus_accepted": 1.1723570892704775
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.740635871887207,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1115054409503937,
                "rejected_mean_error": 2.2059990377426146,
                "gap_rejected_minus_accepted": 1.094493596792221
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2210021317005157,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7876979088972486,
                "rejected_mean_error": 1.952209045861494,
                "gap_rejected_minus_accepted": 1.1645111369642454
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9762415862754548,
            "spearman": 0.9724478482843867,
            "auroc_top30_bad": 0.9825881904761905,
            "mae": 0.10837400333536788,
            "mse": 0.03254727769991929,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.735246205358957,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.062386501848697665
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1758389253973961
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.577707222288847
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9675215871294339
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9386649011974049,
            "spearman": 0.9472333081002676,
            "auroc_top30_worst": 0.9651382857142857,
            "pairwise_seed_ranking": 0.9236,
            "predicted_best_mean_error": 1.7429266474246978,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10067423844337475,
            "gap_to_oracle": 0.003075929164886526,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8957529010772705
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1960256760701156
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4460730360031129
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6252070829304042
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5315690994262705,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7231373590363397,
                "rejected_mean_error": 2.6058045406341552,
                "gap_rejected_minus_accepted": 0.8826671815978155
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.069259464740753,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6249520136172642,
                "rejected_mean_error": 2.369568880944968,
                "gap_rejected_minus_accepted": 0.744616867327704
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8418015837669373,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4460730360031129,
                "rejected_mean_error": 2.1767351183891295,
                "gap_rejected_minus_accepted": 0.7306620823860166
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.526231586933136,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1973803999324957,
                "rejected_mean_error": 2.0165155083418145,
                "gap_rejected_minus_accepted": 0.8191351084093188
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6401147842407227,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7489722458521526,
                "rejected_mean_error": 2.6952586460113523,
                "gap_rejected_minus_accepted": 0.9462864001591997
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0818832516670227,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6408932782749441,
                "rejected_mean_error": 2.445288546501644,
                "gap_rejected_minus_accepted": 0.8043952682266999
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.864393711090088,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4539140071868897,
                "rejected_mean_error": 2.2332877645492553,
                "gap_rejected_minus_accepted": 0.7793737573623656
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5425859987735748,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2013127349671864,
                "rejected_mean_error": 2.059986733497783,
                "gap_rejected_minus_accepted": 0.8586739985305964
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9857958986645599,
            "spearman": 0.9725509202134761,
            "auroc_top30_bad": 0.9737357142857144,
            "mae": 0.09887048134906218,
            "mse": 0.019316382753941333,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.995,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7431764186789869,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0482800410874188
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17441497752815485
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6682578493393958
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0544977990016342
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9316916205224219,
            "spearman": 0.9267078267078269,
            "auroc_top30_worst": 0.9768190476190476,
            "pairwise_seed_ranking": 0.8935,
            "predicted_best_mean_error": 1.866823516190052,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.059406547248363584,
            "gap_to_oracle": 0.003522129058837864,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3286093938350678
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.470425371170044
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.651788061618805
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7633141897519429
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2411882877349854,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8490153103404574,
                "rejected_mean_error": 2.5064791774749757,
                "gap_rejected_minus_accepted": 0.6574638671345183
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.099918484687805,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7633141897519429,
                "rejected_mean_error": 2.369104218959808,
                "gap_rejected_minus_accepted": 0.6057900292078653
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8870991468429565,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.651788061618805,
                "rejected_mean_error": 2.177735332489014,
                "gap_rejected_minus_accepted": 0.5259472708702089
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7082594633102417,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.470425371170044,
                "rejected_mean_error": 2.0628738056818645,
                "gap_rejected_minus_accepted": 0.5924484345118206
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2489855527877807,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8622849530643888,
                "rejected_mean_error": 2.501736056804657,
                "gap_rejected_minus_accepted": 0.6394511037402684
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1169514656066895,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7676159159342448,
                "rejected_mean_error": 2.402072505950928,
                "gap_rejected_minus_accepted": 0.634456590016683
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8922036290168762,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6596960544586181,
                "rejected_mean_error": 2.1927640724182127,
                "gap_rejected_minus_accepted": 0.5330680179595946
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7324041426181793,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4856921076774596,
                "rejected_mean_error": 2.0730760486920676,
                "gap_rejected_minus_accepted": 0.587383941014608
              }
            ]
          }
        }
      }
    },
    {
      "variant": "heteroscedastic_simvla_focused",
      "feature_mode": "M4_seed_relative",
      "model_kind": "hetero",
      "train_setting": "simvla_focused",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 150,
      "best_calib_loss": 0.008825227618217468,
      "train_time_sec": 56.35746431350708,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998987462748469,
            "spearman": 0.9990815103357786,
            "auroc_top30_bad": 0.9999382857142857,
            "mae": 0.009837153896223754,
            "mse": 0.00023378331045738988,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8058323336047897,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.002228606253862381
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17248939933478832
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.475012006162107
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8224412710974613
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2758187427155674
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9999498878066133,
            "spearman": 0.9999129717245147,
            "auroc_top30_worst": 0.9999578095238095,
            "pairwise_seed_ranking": 0.9623,
            "predicted_best_mean_error": 1.7740067575573921,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07601895374059686,
            "gap_to_oracle": 0.00036764430999758346,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6037320502400398
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8401894389390946
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1143448748707772
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.361586173605919
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4743261814117434,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681158070365588,
                "rejected_mean_error": 4.289494090080261,
                "gap_rejected_minus_accepted": 2.721378283043702
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.122678577899933,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.361586173605919,
                "rejected_mean_error": 3.2762560205459597,
                "gap_rejected_minus_accepted": 1.9146698469400407
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6285609006881714,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1143448748707772,
                "rejected_mean_error": 2.566162395811081,
                "gap_rejected_minus_accepted": 1.451817520940304
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1476130187511444,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8401894389390946,
                "rejected_mean_error": 2.173608367474874,
                "gap_rejected_minus_accepted": 1.3334189285357794
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4507818460464486,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.141684889793396,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3725010843276977,
                "rejected_mean_error": 3.282599592208862,
                "gap_rejected_minus_accepted": 1.9100985078811645
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6532419919967651,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1210891275405883,
                "rejected_mean_error": 2.578962295055389,
                "gap_rejected_minus_accepted": 1.457873167514801
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1632525324821472,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8436484961509705,
                "rejected_mean_error": 2.1854847830136617,
                "gap_rejected_minus_accepted": 1.3418362868626912
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9864335508473505,
            "spearman": 0.9852199139276532,
            "auroc_top30_bad": 0.9967001904761904,
            "mae": 0.09332691384227947,
            "mse": 0.01953743300365848,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7247163646494059,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05529758441448212
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16868555376529693
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40837689539194105
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7759362153132756
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1438312957584857
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9739516073319702,
            "spearman": 0.983360759398886,
            "auroc_top30_worst": 0.9915946666666666,
            "pairwise_seed_ranking": 0.9188,
            "predicted_best_mean_error": 1.5616793522834778,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09707288706302641,
            "gap_to_oracle": 0.00254619181156146,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4645547366142273
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7803908938016647
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0941614065170289
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3453443216870842
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5137485742568972,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.49977966732449,
                "rejected_mean_error": 2.865895362854004,
                "gap_rejected_minus_accepted": 1.3661156955295137
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.079368233680725,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3445972112606785,
                "rejected_mean_error": 2.509908815161489,
                "gap_rejected_minus_accepted": 1.1653116039008102
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6597027778625488,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0941614065170289,
                "rejected_mean_error": 2.178621067237854,
                "gap_rejected_minus_accepted": 1.0844596607208252
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1726197302341461,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7810837761662639,
                "rejected_mean_error": 1.922102266976266,
                "gap_rejected_minus_accepted": 1.141018490810002
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5422906160354612,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5184368325604334,
                "rejected_mean_error": 2.9215909004211427,
                "gap_rejected_minus_accepted": 1.4031540678607093
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0972928404808044,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3602935325971899,
                "rejected_mean_error": 2.544653480015104,
                "gap_rejected_minus_accepted": 1.184359947417914
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6765363812446594,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1147758648395538,
                "rejected_mean_error": 2.2027286138534548,
                "gap_rejected_minus_accepted": 1.087952749013901
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.199643224477768,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7980494740463439,
                "rejected_mean_error": 1.948721620169553,
                "gap_rejected_minus_accepted": 1.1506721461232092
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9836478643948989,
            "spearman": 0.9797443687898425,
            "auroc_top30_bad": 0.988448380952381,
            "mae": 0.10538642279710621,
            "mse": 0.022030314110525508,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.7043070219554616,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06030999886989594
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17991657153367996
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5781523969829082
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9614483565926552
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.273068219539523
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9619198410868199,
            "spearman": 0.9638685797003933,
            "auroc_top30_worst": 0.9726232380952381,
            "pairwise_seed_ranking": 0.9336,
            "predicted_best_mean_error": 1.7424382240772247,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10116266179084787,
            "gap_to_oracle": 0.0025875058174134047,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9032958250045776
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1965470913893137
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.439817569065094
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6144534428872026
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4195559024810795,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7209702661832174,
                "rejected_mean_error": 2.625308376312256,
                "gap_rejected_minus_accepted": 0.9043381101290386
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.029708206653595,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6138964903520037,
                "rejected_mean_error": 2.4026648084195656,
                "gap_rejected_minus_accepted": 0.788768318067562
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8064161539077759,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.439817569065094,
                "rejected_mean_error": 2.1829905853271483,
                "gap_rejected_minus_accepted": 0.7431730162620542
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.520652711391449,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1976376901419399,
                "rejected_mean_error": 2.016429561879108,
                "gap_rejected_minus_accepted": 0.8187918717371683
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5130836725234986,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.745223469734192,
                "rejected_mean_error": 2.728997631072998,
                "gap_rejected_minus_accepted": 0.983774161338806
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0330365896224976,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6259865531309403,
                "rejected_mean_error": 2.4895354925640047,
                "gap_rejected_minus_accepted": 0.8635489394330644
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8393135070800781,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4471589946746826,
                "rejected_mean_error": 2.2400427770614626,
                "gap_rejected_minus_accepted": 0.79288378238678
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5474555492401123,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2013533399218606,
                "rejected_mean_error": 2.0599730537536947,
                "gap_rejected_minus_accepted": 0.8586197138318341
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.984682333214649,
            "spearman": 0.9731548644068023,
            "auroc_top30_bad": 0.9712154761904763,
            "mae": 0.10519463309063576,
            "mse": 0.02111908252255313,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.975,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.731735918243649,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07113896269351244
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1816420134678483
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6635989108122885
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0541085067614913
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3405276080984623
              }
            ]
          },
          "simvla_only": {
            "n": 1000,
            "contexts": 200,
            "pearson": 0.9418779764386865,
            "spearman": 0.9301728421728424,
            "auroc_top30_worst": 0.9729761904761904,
            "pairwise_seed_ranking": 0.9295,
            "predicted_best_mean_error": 1.8639988026022911,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.0622312608361244,
            "gap_to_oracle": 0.0006974154710770453,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.329805965423584
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4578902645111085
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6515790629386902
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.764346000512441
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.253078985214233,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8466401558452183,
                "rejected_mean_error": 2.527855567932129,
                "gap_rejected_minus_accepted": 0.6812154120869107
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.108153462409973,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.764346000512441,
                "rejected_mean_error": 2.3660087866783144,
                "gap_rejected_minus_accepted": 0.6016627861658734
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.867758333683014,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6515790629386902,
                "rejected_mean_error": 2.1779443311691282,
                "gap_rejected_minus_accepted": 0.526365268230438
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6933126151561737,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4578902645111085,
                "rejected_mean_error": 2.0670521745681762,
                "gap_rejected_minus_accepted": 0.6091619100570678
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2692263603210447,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8594700217247009,
                "rejected_mean_error": 2.527070438861847,
                "gap_rejected_minus_accepted": 0.6676004171371461
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.112794578075409,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.770005300839742,
                "rejected_mean_error": 2.394904351234436,
                "gap_rejected_minus_accepted": 0.6248990503946941
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8794804811477661,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6542487823963166,
                "rejected_mean_error": 2.1982113444805145,
                "gap_rejected_minus_accepted": 0.5439625620841979
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7075922191143036,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4614642715454103,
                "rejected_mean_error": 2.081151994069417,
                "gap_rejected_minus_accepted": 0.619687722524007
              }
            ]
          }
        }
      }
    }
  ]
}
```
