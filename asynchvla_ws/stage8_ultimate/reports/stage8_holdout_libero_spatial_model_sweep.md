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
      "best_epoch": 77,
      "best_calib_loss": 0.042111415416002274,
      "train_time_sec": 11.21252989768982,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9791422225709752,
            "spearman": 0.9416561765285448,
            "auroc_top30_bad": 0.9993844523809524,
            "mae": 0.11070322348251939,
            "mse": 0.04476812660666063,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.523,
            "expert_lt_simvla_seed0": 0.972,
            "same_context_pred_std": 0.7765051810468062,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.29607576279342174
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3187328808784485
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4829820122942328
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8228704688539108
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
            "pearson": 0.9993261618778769,
            "spearman": 0.99881395986453,
            "auroc_top30_worst": 0.9992419047619048,
            "pairwise_seed_ranking": 0.8719,
            "predicted_best_mean_error": 1.7775600480735303,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07246566322445869,
            "gap_to_oracle": 0.003920934826135758,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6046829773783684
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8415610903024674
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1150496766209603
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3617346477270127
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.3846562623977663,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.568184296058284,
                "rejected_mean_error": 4.288877688884735,
                "gap_rejected_minus_accepted": 2.720693392826451
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1030579209327698,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3617346477270127,
                "rejected_mean_error": 3.2758105981826784,
                "gap_rejected_minus_accepted": 1.9140759504556657
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6113929748535156,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1150496766209603,
                "rejected_mean_error": 2.5654575940608977,
                "gap_rejected_minus_accepted": 1.4504079174399374
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1508903801441193,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8415610903024674,
                "rejected_mean_error": 2.1731511503537497,
                "gap_rejected_minus_accepted": 1.3315900600512824
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.380270838737489,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1206273436546326,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.372787704149882,
                "rejected_mean_error": 3.2817397327423095,
                "gap_rejected_minus_accepted": 1.9089520285924275
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6311098337173462,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1214046597480773,
                "rejected_mean_error": 2.5786467628479004,
                "gap_rejected_minus_accepted": 1.457242103099823
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1609649658203125,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8446984724998474,
                "rejected_mean_error": 2.1851347908973695,
                "gap_rejected_minus_accepted": 1.340436318397522
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9035216984872534,
            "spearman": 0.8898782101683476,
            "auroc_top30_bad": 0.9764518095238095,
            "mae": 0.258864880412817,
            "mse": 0.13159539803922665,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.508,
            "expert_lt_simvla_seed0": 0.968,
            "same_context_pred_std": 0.6780644539049593,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.31733294630050657
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3063971929788589
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4378586613059044
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7968879567861556
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
            "pearson": 0.7794465164013378,
            "spearman": 0.8305916665504555,
            "auroc_top30_worst": 0.9264,
            "pairwise_seed_ranking": 0.8104,
            "predicted_best_mean_error": 1.5728725973367692,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.08587964200973497,
            "gap_to_oracle": 0.013739436864852905,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5585258390903473
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9051185292311204
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1542724234580994
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4164448690566935
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4271445989608766,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5624381306966146,
                "rejected_mean_error": 2.301969192504883,
                "gap_rejected_minus_accepted": 0.7395310618082682
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9648028910160065,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4153308681388292,
                "rejected_mean_error": 2.298159816775459,
                "gap_rejected_minus_accepted": 0.8828289486366296
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.572738528251648,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1542724234580994,
                "rejected_mean_error": 2.1185100502967833,
                "gap_rejected_minus_accepted": 0.9642376268386839
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1790447235107422,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9053095310640792,
                "rejected_mean_error": 1.880605296556825,
                "gap_rejected_minus_accepted": 0.9752957654927458
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4416403532028195,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5896919569704269,
                "rejected_mean_error": 2.280294780731201,
                "gap_rejected_minus_accepted": 0.6906028237607742
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0223122239112854,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4330756710493628,
                "rejected_mean_error": 2.328617608736432,
                "gap_rejected_minus_accepted": 0.895541937687069
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6072999238967896,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.16836629986763,
                "rejected_mean_error": 2.1491381788253783,
                "gap_rejected_minus_accepted": 0.9807718789577482
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2286290228366852,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9204543795850542,
                "rejected_mean_error": 1.9074836038650675,
                "gap_rejected_minus_accepted": 0.9870292242800134
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8330710446483777,
            "spearman": 0.8170499801210269,
            "auroc_top30_bad": 0.909728,
            "mae": 0.33074139930307866,
            "mse": 0.21679686500462664,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.492,
            "expert_lt_simvla_seed0": 0.96,
            "same_context_pred_std": 0.6367046526154996,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.44737178361415864
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.41326026393175125
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6360278922498226
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0208813271482786
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
            "pearson": 0.5992338761233749,
            "spearman": 0.6106286423642567,
            "auroc_top30_worst": 0.766464,
            "pairwise_seed_ranking": 0.7536,
            "predicted_best_mean_error": 1.770839600086212,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.07276128578186047,
            "gap_to_oracle": 0.030988881826400805,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2131847887039184
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.391326028567094
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.567399142074585
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.691304823482977
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.007050180435181,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7545059385829502,
                "rejected_mean_error": 2.3234873247146606,
                "gap_rejected_minus_accepted": 0.5689813861317103
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8163358867168427,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6909127057298399,
                "rejected_mean_error": 2.172108278678248,
                "gap_rejected_minus_accepted": 0.4811955729484083
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5803698897361755,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.567399142074585,
                "rejected_mean_error": 2.0554090123176576,
                "gap_rejected_minus_accepted": 0.48800987024307263
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2954806685447693,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.392038503013099,
                "rejected_mean_error": 1.9514909765763624,
                "gap_rejected_minus_accepted": 0.5594524735632633
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0288045406341553,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7769954050911798,
                "rejected_mean_error": 2.4430502128601073,
                "gap_rejected_minus_accepted": 0.6660548077689274
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8369874954223633,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.706983056935397,
                "rejected_mean_error": 2.2491172987317283,
                "gap_rejected_minus_accepted": 0.5421342417963313
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6185846328735352,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5641105356216431,
                "rejected_mean_error": 2.123091236114502,
                "gap_rejected_minus_accepted": 0.5589807004928586
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3357330560684204,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.390603538543459,
                "rejected_mean_error": 1.9962149654480226,
                "gap_rejected_minus_accepted": 0.6056114269045636
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.7786624330553307,
            "spearman": 0.7769964706023131,
            "auroc_top30_bad": 0.8745916666666667,
            "mae": 0.4204804486762732,
            "mse": 0.31538972252820524,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.51,
            "expert_lt_simvla_seed0": 0.965,
            "same_context_pred_std": 0.6037339403871812,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.49699316374957564
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.44208922458440064
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7847854320146144
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0917906555558243
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
            "pearson": 0.41615593567556264,
            "spearman": 0.49101401901401903,
            "auroc_top30_worst": 0.7777333333333333,
            "pairwise_seed_ranking": 0.731,
            "predicted_best_mean_error": 1.8844778707623482,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.041752192676067335,
            "gap_to_oracle": 0.021176483631134113,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.887055718898773
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.7422614512443542
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.7464593591690063
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8276204430262248
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0186005592346192,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8735096267859142,
                "rejected_mean_error": 2.286030329465866,
                "gap_rejected_minus_accepted": 0.4125207026799518
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8654074668884277,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8276204430262248,
                "rejected_mean_error": 2.176185459136963,
                "gap_rejected_minus_accepted": 0.3485650161107381
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4921571016311646,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.7464593591690063,
                "rejected_mean_error": 2.083064034938812,
                "gap_rejected_minus_accepted": 0.3366046757698058
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1380931437015533,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.7422614512443542,
                "rejected_mean_error": 1.9722617789904278,
                "gap_rejected_minus_accepted": 0.2300003277460736
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.014775824546814,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.890969157881207,
                "rejected_mean_error": 2.2435782134532927,
                "gap_rejected_minus_accepted": 0.35260905557208577
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8566385209560394,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8412259324391682,
                "rejected_mean_error": 2.1812424564361574,
                "gap_rejected_minus_accepted": 0.34001652399698923
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5208868384361267,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.763481547832489,
                "rejected_mean_error": 2.0889785790443423,
                "gap_rejected_minus_accepted": 0.32549703121185325
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1519815325737,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.7568570637702943,
                "rejected_mean_error": 1.982687729994456,
                "gap_rejected_minus_accepted": 0.2258306662241618
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
      "best_epoch": 78,
      "best_calib_loss": 0.016759611666202545,
      "train_time_sec": 14.335408926010132,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9990533882140646,
            "spearman": 0.997548922541404,
            "auroc_top30_bad": 0.999146,
            "mae": 0.03544018605396268,
            "mse": 0.002142887745415677,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8073371210746504,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.007253324702382088
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1731556126922369
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4753333638176322
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8231539706379175
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
            "pearson": 0.9991583788781057,
            "spearman": 0.9987637459345498,
            "auroc_top30_worst": 0.9992556190476191,
            "pairwise_seed_ranking": 0.9072,
            "predicted_best_mean_error": 1.77581023645401,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07421547484397895,
            "gap_to_oracle": 0.0021711232066154995,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6057557874321937
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8413390090227127
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.115102823984623
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3620483443975449
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4816842555999767,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.568140206846926,
                "rejected_mean_error": 4.289274491786957,
                "gap_rejected_minus_accepted": 2.721134284940031
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1347144842147827,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3620483443975449,
                "rejected_mean_error": 3.2748695081710815,
                "gap_rejected_minus_accepted": 1.9128211637735366
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6465036273002625,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.115102823984623,
                "rejected_mean_error": 2.565404446697235,
                "gap_rejected_minus_accepted": 1.4503016227126122
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.152786374092102,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8413390090227127,
                "rejected_mean_error": 2.173225177447001,
                "gap_rejected_minus_accepted": 1.3318861684242882
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.461885213851929,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771947034200033,
                "rejected_mean_error": 4.3055047821998595,
                "gap_rejected_minus_accepted": 2.728310078779856
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1638623476028442,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3728179969787597,
                "rejected_mean_error": 3.281648854255676,
                "gap_rejected_minus_accepted": 1.9088308572769164
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6615954637527466,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1216223990917207,
                "rejected_mean_error": 2.578429023504257,
                "gap_rejected_minus_accepted": 1.4568066244125364
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1596678793430328,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.84461386013031,
                "rejected_mean_error": 2.1851629950205487,
                "gap_rejected_minus_accepted": 1.3405491348902387
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9718518143988497,
            "spearman": 0.9772718628016931,
            "auroc_top30_bad": 0.9927626666666667,
            "mae": 0.1444993142788764,
            "mse": 0.04054651656427098,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7023438920758804,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06735663542151452
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17340624504089355
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4096684726834297
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7791880117813746
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
            "pearson": 0.9380079213894769,
            "spearman": 0.9665185823478929,
            "auroc_top30_worst": 0.9909790476190475,
            "pairwise_seed_ranking": 0.9148,
            "predicted_best_mean_error": 1.562784296631813,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09596794271469111,
            "gap_to_oracle": 0.0036511361598967618,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5093391575813293
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7823364994464777
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0995691270828247
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3482427210695962
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5381443500518808,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5307845861646865,
                "rejected_mean_error": 2.5868510932922364,
                "gap_rejected_minus_accepted": 1.05606650712755
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.138764262199402,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3474649446623812,
                "rejected_mean_error": 2.501323939131472,
                "gap_rejected_minus_accepted": 1.1538589944690907
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.60246741771698,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0995691270828247,
                "rejected_mean_error": 2.1732133466720582,
                "gap_rejected_minus_accepted": 1.0736442195892335
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2082649171352386,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.783073941358743,
                "rejected_mean_error": 1.9214374625950001,
                "gap_rejected_minus_accepted": 1.1383635212362573
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.601030111312866,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5525582102934519,
                "rejected_mean_error": 2.6144985008239745,
                "gap_rejected_minus_accepted": 1.0619402905305226
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1717730164527893,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3654548925830718,
                "rejected_mean_error": 2.5293332527554226,
                "gap_rejected_minus_accepted": 1.1638783601723508
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6299001574516296,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1206741287708282,
                "rejected_mean_error": 2.19683034992218,
                "gap_rejected_minus_accepted": 1.0761562211513518
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2258889079093933,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7955763382571084,
                "rejected_mean_error": 1.9495548156493487,
                "gap_rejected_minus_accepted": 1.1539784773922404
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9621277056715686,
            "spearman": 0.9591073491508434,
            "auroc_top30_bad": 0.9769508571428572,
            "mae": 0.1643596528586466,
            "mse": 0.051451905736022874,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.6616383221044391,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07686894696950912
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20187161051034927
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5925064199388027
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9651665341973305
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
            "pearson": 0.9236954540354989,
            "spearman": 0.9331756151137516,
            "auroc_top30_worst": 0.9654887619047618,
            "pairwise_seed_ranking": 0.88,
            "predicted_best_mean_error": 1.7462678747177125,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.09733301115036008,
            "gap_to_oracle": 0.006417156457901196,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9277082786560059
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2241870913750086
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4530518878936767
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6181901884612753
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.195612072944641,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7333411062558493,
                "rejected_mean_error": 2.513970815658569,
                "gap_rejected_minus_accepted": 0.7806297094027199
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.012392282485962,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6176865656195227,
                "rejected_mean_error": 2.391318800350348,
                "gap_rejected_minus_accepted": 0.7736322347308251
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.750078022480011,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4530518878936767,
                "rejected_mean_error": 2.1697562664985655,
                "gap_rejected_minus_accepted": 0.7167043786048888
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4257245361804962,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.2242037823405891,
                "rejected_mean_error": 2.0075552962887375,
                "gap_rejected_minus_accepted": 0.7833515139481484
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2281786441802973,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7570153697331747,
                "rejected_mean_error": 2.622870531082153,
                "gap_rejected_minus_accepted": 0.8658551613489784
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0421584844589233,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.627623795188047,
                "rejected_mean_error": 2.4846757423310053,
                "gap_rejected_minus_accepted": 0.8570519471429583
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7736368775367737,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4622838439941406,
                "rejected_mean_error": 2.2249179277420046,
                "gap_rejected_minus_accepted": 0.762634083747864
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4486489295959473,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2243114861231001,
                "rejected_mean_error": 2.0522384911297475,
                "gap_rejected_minus_accepted": 0.8279270050066474
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9752382913900275,
            "spearman": 0.9562733239527288,
            "auroc_top30_bad": 0.9576511904761904,
            "mae": 0.16973781278193928,
            "mse": 0.04673043455615556,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.985,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.656328559033193,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06400159934535622
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18788470713049174
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6723355869092047
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0581670126939813
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
            "pearson": 0.8869174026870976,
            "spearman": 0.8907292467292469,
            "auroc_top30_worst": 0.9575904761904762,
            "pairwise_seed_ranking": 0.857,
            "predicted_best_mean_error": 1.8685039988160133,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.05772606462240226,
            "gap_to_oracle": 0.0052026116847991855,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.4039001476764679
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.5021266837120055
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6435477254390716
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7721404399871825
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.142206335067749,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8493324955304464,
                "rejected_mean_error": 2.503624510765076,
                "gap_rejected_minus_accepted": 0.6542920152346294
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9609180390834808,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7721404399871825,
                "rejected_mean_error": 2.3426254682540892,
                "gap_rejected_minus_accepted": 0.5704850282669067
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7705383896827698,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6435477254390716,
                "rejected_mean_error": 2.185975668668747,
                "gap_rejected_minus_accepted": 0.5424279432296755
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.541918784379959,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.5021266837120055,
                "rejected_mean_error": 2.0523067015012106,
                "gap_rejected_minus_accepted": 0.5501800177892051
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1404831409454346,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.860094436009725,
                "rejected_mean_error": 2.521450710296631,
                "gap_rejected_minus_accepted": 0.6613562742869061
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9647640585899353,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7788493712743123,
                "rejected_mean_error": 2.368372139930725,
                "gap_rejected_minus_accepted": 0.5895227686564128
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.776603877544403,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.652290802001953,
                "rejected_mean_error": 2.200169324874878,
                "gap_rejected_minus_accepted": 0.5478785228729248
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5588819980621338,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5168413710594177,
                "rejected_mean_error": 2.0626929608980813,
                "gap_rejected_minus_accepted": 0.5458515898386636
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
      "best_epoch": 77,
      "best_calib_loss": 0.007930891588330269,
      "train_time_sec": 35.05214071273804,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999865991389632,
            "spearman": 0.9989080724334696,
            "auroc_top30_bad": 0.9999094523809524,
            "mae": 0.013792493884079158,
            "mse": 0.00034319692492641046,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8001025738069302,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0009414666146039962
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17246289329230785
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4750274428352714
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8224978173563878
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
            "pearson": 0.9999072140872829,
            "spearman": 0.999824927096997,
            "auroc_top30_worst": 0.9999015238095238,
            "pairwise_seed_ranking": 0.9521,
            "predicted_best_mean_error": 1.7742985769510269,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.0757271343469621,
            "gap_to_oracle": 0.0006594637036323459,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6037538550496101
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8402186381578446
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1143766427636146
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.361631684978803
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4359414339065566,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.568108947204219,
                "rejected_mean_error": 4.28955582857132,
                "gap_rejected_minus_accepted": 2.7214468813671013
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.11262184381485,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.361631684978803,
                "rejected_mean_error": 3.2761194864273073,
                "gap_rejected_minus_accepted": 1.9144878014485043
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6235225200653076,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1143766427636146,
                "rejected_mean_error": 2.5661306279182434,
                "gap_rejected_minus_accepted": 1.4517539851546288
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1426503360271454,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8402186381578446,
                "rejected_mean_error": 2.1735986344019573,
                "gap_rejected_minus_accepted": 1.3333799962441129
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.400365734100343,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1424204111099243,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.372553502400716,
                "rejected_mean_error": 3.2824423379898073,
                "gap_rejected_minus_accepted": 1.9098888355890913
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6472623348236084,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1211249074935914,
                "rejected_mean_error": 2.5789265151023866,
                "gap_rejected_minus_accepted": 1.4578016076087952
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.15686896443367,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8437439589500427,
                "rejected_mean_error": 2.1854529620806376,
                "gap_rejected_minus_accepted": 1.3417090031305947
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9868634081853298,
            "spearman": 0.9883682991117898,
            "auroc_top30_bad": 0.9971481904761904,
            "mae": 0.08590462471805513,
            "mse": 0.018963211669945468,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.96,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7328532990582312,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.059318547427654265
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16347278151512146
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.402280874979496
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7748356560786566
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
            "pearson": 0.971799657883754,
            "spearman": 0.9893989512953288,
            "auroc_top30_worst": 0.9953462857142857,
            "pairwise_seed_ranking": 0.9456,
            "predicted_best_mean_error": 1.5599413619041442,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09881087744235995,
            "gap_to_oracle": 0.0008082014322279285,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46611059761047363
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7493145483044478
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.091596191596985
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3453746773540847
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.497478866577149,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5071799793243408,
                "rejected_mean_error": 2.799292554855347,
                "gap_rejected_minus_accepted": 1.2921125755310061
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0812162160873413,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3446809323136808,
                "rejected_mean_error": 2.509658186961287,
                "gap_rejected_minus_accepted": 1.164977254647606
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.67028146982193,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.091596191596985,
                "rejected_mean_error": 2.181186282157898,
                "gap_rejected_minus_accepted": 1.0895900905609128
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0659363567829132,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7501140983340839,
                "rejected_mean_error": 1.9324475275541446,
                "gap_rejected_minus_accepted": 1.1823334292200607
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5128309965133666,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5239622784985436,
                "rejected_mean_error": 2.8718618869781496,
                "gap_rejected_minus_accepted": 1.347899608479606
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.103313446044922,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3617293115924387,
                "rejected_mean_error": 2.540391723314921,
                "gap_rejected_minus_accepted": 1.1786624117224822
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7000144124031067,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1115062897205352,
                "rejected_mean_error": 2.2059981889724734,
                "gap_rejected_minus_accepted": 1.0944918992519381
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0992664396762848,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7596585055192312,
                "rejected_mean_error": 1.961655475876548,
                "gap_rejected_minus_accepted": 1.201996970357317
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9827349535796341,
            "spearman": 0.9830053610948766,
            "auroc_top30_bad": 0.9895222857142858,
            "mae": 0.09521765139419586,
            "mse": 0.023071807220017133,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7205666412573958,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.046292073100805284
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17303330100774764
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5726386557996272
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9618437992374103
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
            "pearson": 0.9358701596465906,
            "spearman": 0.961074259059736,
            "auroc_top30_worst": 0.9600060952380952,
            "pairwise_seed_ranking": 0.924,
            "predicted_best_mean_error": 1.7418506720066071,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10175021386146543,
            "gap_to_oracle": 0.001999953746795846,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.884822536945343
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.183518631144976
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.439972524356842
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6180662149940725
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2612583398818975,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.725904913213518,
                "rejected_mean_error": 2.5808965530395507,
                "gap_rejected_minus_accepted": 0.8549916398260327
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0044690370559692,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6174108701556316,
                "rejected_mean_error": 2.3921441251096636,
                "gap_rejected_minus_accepted": 0.774733254954032
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8123679161071777,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.439972524356842,
                "rejected_mean_error": 2.1828356300354006,
                "gap_rejected_minus_accepted": 0.7428631056785586
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.526185929775238,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1843607324761705,
                "rejected_mean_error": 2.0208646608645786,
                "gap_rejected_minus_accepted": 0.8365039283884081
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.349572777748108,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.751323364575704,
                "rejected_mean_error": 2.6740985774993895,
                "gap_rejected_minus_accepted": 0.9227752129236855
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.017315447330475,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.63165916669815,
                "rejected_mean_error": 2.4726977348327637,
                "gap_rejected_minus_accepted": 0.8410385681346138
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8365216255187988,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4490061750411987,
                "rejected_mean_error": 2.2381955966949465,
                "gap_rejected_minus_accepted": 0.7891894216537478
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5410103499889374,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1895925828388758,
                "rejected_mean_error": 2.0639352339474275,
                "gap_rejected_minus_accepted": 0.8743426511085517
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9878139103848274,
            "spearman": 0.9671161627064137,
            "auroc_top30_bad": 0.9604654761904762,
            "mae": 0.10628826910373755,
            "mse": 0.01952971012713689,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.99,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7221710493111192,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05362277882173658
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16985737527161837
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6646044287718833
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0598469089691838
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
            "pearson": 0.9281435528867593,
            "spearman": 0.8908045554769691,
            "auroc_top30_worst": 0.9542690476190475,
            "pairwise_seed_ranking": 0.909,
            "predicted_best_mean_error": 1.864876043498516,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06135401993989942,
            "gap_to_oracle": 0.0015746563673020297,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3253972494602204
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4552000923156738
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.668702940940857
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7664107406934102
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2210530757904055,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8444160008430481,
                "rejected_mean_error": 2.54787296295166,
                "gap_rejected_minus_accepted": 0.703456962108612
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0515193939208984,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7664107406934102,
                "rejected_mean_error": 2.3598145661354066,
                "gap_rejected_minus_accepted": 0.5934038254419964
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8318172097206116,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.668702940940857,
                "rejected_mean_error": 2.1608204531669615,
                "gap_rejected_minus_accepted": 0.49211751222610456
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.623521089553833,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4552000923156738,
                "rejected_mean_error": 2.067948898633321,
                "gap_rejected_minus_accepted": 0.6127488063176472
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2320454597473143,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8564070092307197,
                "rejected_mean_error": 2.5546375513076782,
                "gap_rejected_minus_accepted": 0.6982305420769586
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0614973306655884,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7697764794031778,
                "rejected_mean_error": 2.3955908155441286,
                "gap_rejected_minus_accepted": 0.6258143361409507
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8274505138397217,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6763794314861298,
                "rejected_mean_error": 2.1760806953907013,
                "gap_rejected_minus_accepted": 0.4997012639045715
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6347757577896118,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.461481282711029,
                "rejected_mean_error": 2.0811463236808776,
                "gap_rejected_minus_accepted": 0.6196650409698485
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
      "best_epoch": 76,
      "best_calib_loss": 0.00887270923703909,
      "train_time_sec": 41.331899881362915,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993756975055254,
            "spearman": 0.9979701551824991,
            "auroc_top30_bad": 0.9996208095238095,
            "mae": 0.025713627529339284,
            "mse": 0.0014014828192779973,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.995,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8081611547435453,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00838171785324812
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1731075942724943
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4752025239214301
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8226516791969538
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
            "pearson": 0.9996706242674235,
            "spearman": 0.9993148589165942,
            "auroc_top30_worst": 0.9995817142857142,
            "pairwise_seed_ranking": 0.9616,
            "predicted_best_mean_error": 1.774373625934124,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07565208536386492,
            "gap_to_oracle": 0.0007345126867295271,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6040323044657707
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.840741770195961
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1146911879658699
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3616927003622055
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4537539720535295,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681133849687046,
                "rejected_mean_error": 4.289515888690948,
                "gap_rejected_minus_accepted": 2.721402503722244
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1422746777534485,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3616927003622055,
                "rejected_mean_error": 3.2759364402770994,
                "gap_rejected_minus_accepted": 1.914243739914894
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6343257427215576,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1146911879658699,
                "rejected_mean_error": 2.565816082715988,
                "gap_rejected_minus_accepted": 1.4511248947501183
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1516432166099548,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.840741770195961,
                "rejected_mean_error": 2.1734242570559186,
                "gap_rejected_minus_accepted": 1.3326824868599576
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.3926217079162617,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1735005974769592,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3725915018717447,
                "rejected_mean_error": 3.282328339576721,
                "gap_rejected_minus_accepted": 1.9097368377049764
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6511353254318237,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1212498457431794,
                "rejected_mean_error": 2.5788015768527983,
                "gap_rejected_minus_accepted": 1.4575517311096189
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1599986255168915,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8442060189247131,
                "rejected_mean_error": 2.185298942089081,
                "gap_rejected_minus_accepted": 1.3410929231643678
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9895161842070559,
            "spearman": 0.9825726750052091,
            "auroc_top30_bad": 0.9981455238095238,
            "mae": 0.09878710966949511,
            "mse": 0.01867507704535827,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7009290426442639,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09176293832063676
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1755279548883438
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40281522084474564
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7739767332474391
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
            "pearson": 0.9895178737663244,
            "spearman": 0.9937722793966932,
            "auroc_top30_worst": 0.996864,
            "pairwise_seed_ranking": 0.934,
            "predicted_best_mean_error": 1.5598531227111816,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09889911663532258,
            "gap_to_oracle": 0.0007199622392652927,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46593455791473387
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7500192916546112
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0920550064086914
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3435123501810184
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4384456396102907,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.500090935813056,
                "rejected_mean_error": 2.8630939464569094,
                "gap_rejected_minus_accepted": 1.3630030106438533
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9809237718582153,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.342636686887914,
                "rejected_mean_error": 2.515777860967496,
                "gap_rejected_minus_accepted": 1.1731411740795818
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.542953372001648,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0920550064086914,
                "rejected_mean_error": 2.1807274673461916,
                "gap_rejected_minus_accepted": 1.0886724609375003
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0164556801319122,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7510351289194613,
                "rejected_mean_error": 1.93213986205444,
                "gap_rejected_minus_accepted": 1.1811047331349789
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.47069821357727,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5183037102222443,
                "rejected_mean_error": 2.9227890014648437,
                "gap_rejected_minus_accepted": 1.4044852912425994
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.99130380153656,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.360261078346222,
                "rejected_mean_error": 2.5447498124743264,
                "gap_rejected_minus_accepted": 1.1844887341281045
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.570132315158844,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1105899183750152,
                "rejected_mean_error": 2.206914560317993,
                "gap_rejected_minus_accepted": 1.096324641942978
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.027157723903656,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7671082440822844,
                "rejected_mean_error": 1.9591456709061077,
                "gap_rejected_minus_accepted": 1.1920374268238234
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9843463664376746,
            "spearman": 0.9809914453529744,
            "auroc_top30_bad": 0.9921059047619047,
            "mae": 0.09960712329633242,
            "mse": 0.02226358907413358,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6946993495576675,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09210172259807586
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20348439821004868
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5742024335324765
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9585530477166175
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
            "pearson": 0.9798623821437564,
            "spearman": 0.9847733810795759,
            "auroc_top30_worst": 0.9882361904761905,
            "pairwise_seed_ranking": 0.9248,
            "predicted_best_mean_error": 1.7420842673778534,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.1015166184902192,
            "gap_to_oracle": 0.0022335491180420775,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8758305058479309
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1809980183457718
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.435489004611969
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6073150725634113
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3697106361389175,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.718111839559343,
                "rejected_mean_error": 2.651034215927124,
                "gap_rejected_minus_accepted": 0.9329223763677807
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0132627487182617,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6069414286755956,
                "rejected_mean_error": 2.423485552160123,
                "gap_rejected_minus_accepted": 0.8165441234845272
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7518773078918457,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.435489004611969,
                "rejected_mean_error": 2.1873191497802735,
                "gap_rejected_minus_accepted": 0.7518301451683045
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4300362467765808,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1821050070726071,
                "rejected_mean_error": 2.0216181742597925,
                "gap_rejected_minus_accepted": 0.8395131671871854
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5061259508132934,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7426413424809775,
                "rejected_mean_error": 2.752236776351929,
                "gap_rejected_minus_accepted": 1.0095954338709514
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0825958251953125,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6182914793810106,
                "rejected_mean_error": 2.512376425758241,
                "gap_rejected_minus_accepted": 0.8940849463772302
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.773581624031067,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4439271793365478,
                "rejected_mean_error": 2.2432745923995974,
                "gap_rejected_minus_accepted": 0.7993474130630496
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4387214481830597,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1866638300910828,
                "rejected_mean_error": 2.064921926049625,
                "gap_rejected_minus_accepted": 0.8782580959585422
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9877273562196216,
            "spearman": 0.9773620185249765,
            "auroc_top30_bad": 0.979470238095238,
            "mae": 0.1211065345473562,
            "mse": 0.024450846135254934,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6979809203633629,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0905289969034493
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17626071379333735
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6621716165579855
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.051546057385703
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
            "pearson": 0.96706272406128,
            "spearman": 0.9557785877785878,
            "auroc_top30_worst": 0.9882,
            "pairwise_seed_ranking": 0.928,
            "predicted_best_mean_error": 1.865409253537655,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06082080990076055,
            "gap_to_oracle": 0.0021078664064408947,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2725656390190125
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4491809654235839
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6424336023330688
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7601559953689576
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.259337568283081,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.847013411257002,
                "rejected_mean_error": 2.5244962692260744,
                "gap_rejected_minus_accepted": 0.6774828579690724
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9449032843112946,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7601559953689576,
                "rejected_mean_error": 2.378578802108765,
                "gap_rejected_minus_accepted": 0.6184228067398072
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7774080634117126,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6424336023330688,
                "rejected_mean_error": 2.1870897917747496,
                "gap_rejected_minus_accepted": 0.5446561894416808
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5533556938171387,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4491809654235839,
                "rejected_mean_error": 2.069955274264018,
                "gap_rejected_minus_accepted": 0.620774308840434
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.304927444458008,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8617754128244188,
                "rejected_mean_error": 2.506321918964386,
                "gap_rejected_minus_accepted": 0.6445465061399673
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9288969933986664,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7677240339914957,
                "rejected_mean_error": 2.401748151779175,
                "gap_rejected_minus_accepted": 0.6340241177876793
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.785728096961975,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6452151024341584,
                "rejected_mean_error": 2.2072450244426727,
                "gap_rejected_minus_accepted": 0.5620299220085143
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5635754466056824,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4618497943878175,
                "rejected_mean_error": 2.0810234864552815,
                "gap_rejected_minus_accepted": 0.619173692067464
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
      "best_epoch": 31,
      "best_calib_loss": 0.008726309984922409,
      "train_time_sec": 28.890823364257812,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994240350237458,
            "spearman": 0.9982656933293869,
            "auroc_top30_bad": 0.9995456190476191,
            "mae": 0.04461531159265869,
            "mse": 0.003830034526289075,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.995,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8344823277255844,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.002976466543972492
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1730086583584547
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47516021330207586
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8227642044852177
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
            "pearson": 0.9993681977382696,
            "spearman": 0.9992101049843852,
            "auroc_top30_worst": 0.9990601904761904,
            "pairwise_seed_ranking": 0.9383,
            "predicted_best_mean_error": 1.7747383305430413,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07528738075494767,
            "gap_to_oracle": 0.0010992172956467705,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6041220750212669
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8405920464754104
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1146998987317085
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3619141991058985
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.5696971893310563,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681893733143806,
                "rejected_mean_error": 4.288831993579865,
                "gap_rejected_minus_accepted": 2.720642620265484
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.200769603252411,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3619141991058985,
                "rejected_mean_error": 3.2752719440460205,
                "gap_rejected_minus_accepted": 1.913357744940122
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6914153099060059,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1146998987317085,
                "rejected_mean_error": 2.5658073719501497,
                "gap_rejected_minus_accepted": 1.4511074732184412
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1706815659999847,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8405920464754104,
                "rejected_mean_error": 2.1734741649627685,
                "gap_rejected_minus_accepted": 1.332882118487358
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.5562816143035887,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5774137224091425,
                "rejected_mean_error": 4.303533611297607,
                "gap_rejected_minus_accepted": 2.726119888888465
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.217789590358734,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.372943639119466,
                "rejected_mean_error": 3.281271927833557,
                "gap_rejected_minus_accepted": 1.9083282887140909
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.711740255355835,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1213171412944793,
                "rejected_mean_error": 2.5787342813014984,
                "gap_rejected_minus_accepted": 1.457417140007019
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1846641898155212,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8438814301490783,
                "rejected_mean_error": 2.185407138347626,
                "gap_rejected_minus_accepted": 1.3415257081985477
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.987242627931064,
            "spearman": 0.9830553408604165,
            "auroc_top30_bad": 0.9963512380952381,
            "mae": 0.09498306102532224,
            "mse": 0.019343568609588548,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7120563588267408,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08227811166644096
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17586113634109496
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4055557564854622
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7756064396937689
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
            "pearson": 0.9796730918225109,
            "spearman": 0.9879048032670742,
            "auroc_top30_worst": 0.9938377142857143,
            "pairwise_seed_ranking": 0.9368,
            "predicted_best_mean_error": 1.5602106024026872,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09854163694381701,
            "gap_to_oracle": 0.0010774419307708616,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.47118535089492797
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7607122140052991
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0941772064208983
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3434256493155636
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.515771436691284,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5003690581851536,
                "rejected_mean_error": 2.860590845108032,
                "gap_rejected_minus_accepted": 1.3602217869228785
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0202348828315735,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3425988209540205,
                "rejected_mean_error": 2.5158912168143277,
                "gap_rejected_minus_accepted": 1.1732923958603072
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.603429138660431,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0941772064208983,
                "rejected_mean_error": 2.1786052673339844,
                "gap_rejected_minus_accepted": 1.084428060913086
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0739485919475555,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7615107819676018,
                "rejected_mean_error": 1.9286405243766727,
                "gap_rejected_minus_accepted": 1.1671297424090707
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.526827669143677,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5188808039824169,
                "rejected_mean_error": 2.917595157623291,
                "gap_rejected_minus_accepted": 1.398714353640874
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.058695673942566,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3605049920273338,
                "rejected_mean_error": 2.544025814722455,
                "gap_rejected_minus_accepted": 1.183520822695121
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6088119745254517,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1125386135578155,
                "rejected_mean_error": 2.204965865135193,
                "gap_rejected_minus_accepted": 1.0924272515773774
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1087473034858704,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7773660426101987,
                "rejected_mean_error": 1.9556898350384146,
                "gap_rejected_minus_accepted": 1.178323792428216
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9790167551841062,
            "spearman": 0.9753196173883102,
            "auroc_top30_bad": 0.9911055238095239,
            "mae": 0.11031643046456775,
            "mse": 0.02750710178103999,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7056308143578068,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.135282359957695
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19785603407621383
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5760094463765622
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9602023529966672
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
            "pearson": 0.9470997306049381,
            "spearman": 0.9632482534144317,
            "auroc_top30_worst": 0.9682468571428572,
            "pairwise_seed_ranking": 0.908,
            "predicted_best_mean_error": 1.743796368122101,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.09980451774597165,
            "gap_to_oracle": 0.003945649862289624,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9036112051010132
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1922031845419834
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4387512982368469
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6148809748036521
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3426563739776616,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7225422535472446,
                "rejected_mean_error": 2.611160490036011,
                "gap_rejected_minus_accepted": 0.8886182364887663
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.086982250213623,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6144531088043304,
                "rejected_mean_error": 2.400998509730013,
                "gap_rejected_minus_accepted": 0.7865454009256825
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8083971738815308,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4387512982368469,
                "rejected_mean_error": 2.1840568561553955,
                "gap_rejected_minus_accepted": 0.7453055579185486
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4802413284778595,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1935608076592223,
                "rejected_mean_error": 2.0177914233701335,
                "gap_rejected_minus_accepted": 0.8242306157109112
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4252981185913085,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.747187581062317,
                "rejected_mean_error": 2.7113206291198733,
                "gap_rejected_minus_accepted": 0.9641330480575563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1178391575813293,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.628421387570427,
                "rejected_mean_error": 2.4823082855769565,
                "gap_rejected_minus_accepted": 0.8538868980065295
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8320747017860413,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.446588348388672,
                "rejected_mean_error": 2.2406134233474733,
                "gap_rejected_minus_accepted": 0.7940250749588014
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5036706328392029,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1990076681924244,
                "rejected_mean_error": 2.060763306796232,
                "gap_rejected_minus_accepted": 0.8617556386038077
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9881967924508717,
            "spearman": 0.9753520530559753,
            "auroc_top30_bad": 0.9726488095238095,
            "mae": 0.10008439469236237,
            "mse": 0.01891082051106335,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7221981806260663,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07477148765698076
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1767627451196313
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6619895864762366
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0570927785262465
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
            "pearson": 0.9526025506019908,
            "spearman": 0.933915081915082,
            "auroc_top30_worst": 0.9577904761904762,
            "pairwise_seed_ranking": 0.906,
            "predicted_best_mean_error": 1.8655538269877434,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.060676236450672105,
            "gap_to_oracle": 0.0022524398565293424,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.282716007232666
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.451029990196228
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6503263850212098
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7658457485834758
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.317837882041931,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8449430399470859,
                "rejected_mean_error": 2.5431296110153196,
                "gap_rejected_minus_accepted": 0.6981865710682338
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0098243951797485,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7658457485834758,
                "rejected_mean_error": 2.36150954246521,
                "gap_rejected_minus_accepted": 0.5956637938817342
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8128523230552673,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6503263850212098,
                "rejected_mean_error": 2.179197009086609,
                "gap_rejected_minus_accepted": 0.5288706240653993
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5662406384944916,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.451029990196228,
                "rejected_mean_error": 2.069338932673136,
                "gap_rejected_minus_accepted": 0.6183089424769082
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3324154376983643,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8579559564590453,
                "rejected_mean_error": 2.5406970262527464,
                "gap_rejected_minus_accepted": 0.6827410697937011
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9990268349647522,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.77516348918279,
                "rejected_mean_error": 2.3794297862052916,
                "gap_rejected_minus_accepted": 0.6042662970225015
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8369803428649902,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6574968791007996,
                "rejected_mean_error": 2.1949632477760317,
                "gap_rejected_minus_accepted": 0.5374663686752321
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5676834881305695,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4597162365913392,
                "rejected_mean_error": 2.081734672387441,
                "gap_rejected_minus_accepted": 0.6220184357961016
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
      "best_epoch": 62,
      "best_calib_loss": 0.00939906295388937,
      "train_time_sec": 38.481385707855225,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993633662938514,
            "spearman": 0.9981399807331317,
            "auroc_top30_bad": 0.999498,
            "mae": 0.03687928043523037,
            "mse": 0.002535261813846291,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8260690958868446,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0038006230592727663
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17282910238206386
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47543715436309575
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8228144203335047
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
            "pearson": 0.999480211573727,
            "spearman": 0.9989802841191623,
            "auroc_top30_worst": 0.9991441904761905,
            "pairwise_seed_ranking": 0.9472,
            "predicted_best_mean_error": 1.7744461439549923,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07557956734299665,
            "gap_to_oracle": 0.0008070307075978,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6056483742594719
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8409300440073013
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1148735400795937
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3620112700541813
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.558746671676636,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681326867540677,
                "rejected_mean_error": 4.289342172622681,
                "gap_rejected_minus_accepted": 2.7212094858686133
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.157342791557312,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3620112700541813,
                "rejected_mean_error": 3.274980731201172,
                "gap_rejected_minus_accepted": 1.9129694611469905
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6589245796203613,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1148735400795937,
                "rejected_mean_error": 2.5656337306022645,
                "gap_rejected_minus_accepted": 1.4507601905226708
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1599486768245697,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8409300440073013,
                "rejected_mean_error": 2.173361499118805,
                "gap_rejected_minus_accepted": 1.3324314551115035
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.5232647180557253,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1754831075668335,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3727046496073405,
                "rejected_mean_error": 3.281988896369934,
                "gap_rejected_minus_accepted": 1.9092842467625935
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6804631352424622,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.121434890985489,
                "rejected_mean_error": 2.5786165316104888,
                "gap_rejected_minus_accepted": 1.4571816406249998
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1743160784244537,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8441327919960022,
                "rejected_mean_error": 2.1853233510653176,
                "gap_rejected_minus_accepted": 1.3411905590693154
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9838313096855612,
            "spearman": 0.9768080406170258,
            "auroc_top30_bad": 0.997424,
            "mae": 0.09532023154251379,
            "mse": 0.023900647212349385,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7208215515434968,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0983447959125042
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1976334927558899
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40275440794229506
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7744556896607081
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
            "pearson": 0.9707601635857863,
            "spearman": 0.9883286228023187,
            "auroc_top30_worst": 0.9965470476190476,
            "pairwise_seed_ranking": 0.9268,
            "predicted_best_mean_error": 1.5603242200613021,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09842801928520206,
            "gap_to_oracle": 0.0011910595893858122,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5209325060844422
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7512359682183999
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0950146978378297
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3441785510414954
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.486211252212525,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5005158899095323,
                "rejected_mean_error": 2.859269359588623,
                "gap_rejected_minus_accepted": 1.3587534696790908
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0546929836273193,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3432711104573156,
                "rejected_mean_error": 2.5138786440840164,
                "gap_rejected_minus_accepted": 1.1706075336267008
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6108453273773193,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0950146978378297,
                "rejected_mean_error": 2.177767775917053,
                "gap_rejected_minus_accepted": 1.0827530780792234
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.059971958398819,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7519382524033325,
                "rejected_mean_error": 1.9318381783293048,
                "gap_rejected_minus_accepted": 1.1798999259259724
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5098604917526246,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5189524281024933,
                "rejected_mean_error": 2.9169505405426026,
                "gap_rejected_minus_accepted": 1.3979981124401093
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.070919930934906,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.36007100519012,
                "rejected_mean_error": 2.5453139978741843,
                "gap_rejected_minus_accepted": 1.1852429926840644
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6176059246063232,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1148564455509187,
                "rejected_mean_error": 2.20264803314209,
                "gap_rejected_minus_accepted": 1.0877915875911712
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0780283510684967,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7610495965632181,
                "rejected_mean_error": 1.9611868195355258,
                "gap_rejected_minus_accepted": 1.2001372229723075
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9851175047480967,
            "spearman": 0.9827784808106226,
            "auroc_top30_bad": 0.9926727619047618,
            "mae": 0.09848643162163576,
            "mse": 0.0204429084688081,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.6970165595356002,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0641052072942257
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18818190091848375
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5729254257619381
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.958874736559391
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
            "pearson": 0.9721341797583417,
            "spearman": 0.9762391660685699,
            "auroc_top30_worst": 0.9804617142857142,
            "pairwise_seed_ranking": 0.9048,
            "predicted_best_mean_error": 1.7429608762264253,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10064000964164732,
            "gap_to_oracle": 0.003110157966613958,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8876124753952026
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1823904707263677
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.437716063594818
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6119484924939649
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3645913124084474,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7203195852173698,
                "rejected_mean_error": 2.631164505004883,
                "gap_rejected_minus_accepted": 0.910844919787513
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.067586302757263,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.611385740172774,
                "rejected_mean_error": 2.410181015825119,
                "gap_rejected_minus_accepted": 0.7987952756523451
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8128920197486877,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.437716063594818,
                "rejected_mean_error": 2.1850920907974243,
                "gap_rejected_minus_accepted": 0.7473760272026062
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5072143375873566,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1837887575451178,
                "rejected_mean_error": 2.021055726129701,
                "gap_rejected_minus_accepted": 0.837266968584583
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.455975317955017,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7449949799643623,
                "rejected_mean_error": 2.731054039001465,
                "gap_rejected_minus_accepted": 0.9860590590371028
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0960617065429688,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6209502035283787,
                "rejected_mean_error": 2.5044846572573225,
                "gap_rejected_minus_accepted": 0.8835344537289438
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8350215554237366,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4476564998626709,
                "rejected_mean_error": 2.239545271873474,
                "gap_rejected_minus_accepted": 0.7918887720108032
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.528496891260147,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1913451599696325,
                "rejected_mean_error": 2.063344793523697,
                "gap_rejected_minus_accepted": 0.8719996335540643
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9859925963819548,
            "spearman": 0.9712908034435,
            "auroc_top30_bad": 0.971547619047619,
            "mae": 0.09875466500829673,
            "mse": 0.018960493931483764,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7365300404262125,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09112985530868173
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.177935285307467
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6622708631791174
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0572398492520054
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
            "pearson": 0.9458415116854711,
            "spearman": 0.9255758895758895,
            "auroc_top30_worst": 0.9483857142857143,
            "pairwise_seed_ranking": 0.9205,
            "predicted_best_mean_error": 1.8656731334328651,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.0605569300055504,
            "gap_to_oracle": 0.0023717463016510454,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2944750499725342
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4546887078285218
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6544348266124724
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7668648149172466
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.35883469581604,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8431267669465807,
                "rejected_mean_error": 2.559476068019867,
                "gap_rejected_minus_accepted": 0.7163493010732864
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.105331003665924,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7668648149172466,
                "rejected_mean_error": 2.3584523434638975,
                "gap_rejected_minus_accepted": 0.591587528546651
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.849342703819275,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6544348266124724,
                "rejected_mean_error": 2.175088567495346,
                "gap_rejected_minus_accepted": 0.5206537408828735
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6098850965499878,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4546887078285218,
                "rejected_mean_error": 2.0681193601290384,
                "gap_rejected_minus_accepted": 0.6134306523005166
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.374200463294983,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8509235898653666,
                "rejected_mean_error": 2.603988325595856,
                "gap_rejected_minus_accepted": 0.7530647357304892
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.10442852973938,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7765893356005351,
                "rejected_mean_error": 2.375152246952057,
                "gap_rejected_minus_accepted": 0.5985629113515218
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8606983423233032,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6583169102668762,
                "rejected_mean_error": 2.194143216609955,
                "gap_rejected_minus_accepted": 0.5358263063430786
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6172887682914734,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4652608799934388,
                "rejected_mean_error": 2.0798864579200744,
                "gap_rejected_minus_accepted": 0.6146255779266356
              }
            ]
          }
        }
      }
    }
  ]
}
```
