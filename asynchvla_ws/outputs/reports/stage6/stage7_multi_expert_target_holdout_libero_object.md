# Stage 7 Multi-Expert Target Experiments: holdout_libero_object

```json
{
  "split": "holdout_libero_object",
  "by_target": {
    "target_chunk_l2_single_expert": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 42,
        "best_calib_loss": 0.0899055078625679,
        "train_time_sec": 14.310428857803345,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8991681555427585,
              "spearman": 0.8093614507803335,
              "auroc_top30_bad": 0.8808184523809524,
              "mae": 0.22101796091496945,
              "mse": 0.22268200093386453,
              "expert_lt_perturb_large": 0.98,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.7548112371276122,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5483135046362877
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5651215631306171
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.719374943497777
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0194092186649641
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4164188162431122
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9980035701387457,
              "spearman": 0.9956295592890775,
              "auroc_top30_worst": 0.998583619047619,
              "pairwise_seed_ranking": 0.8488,
              "predicted_best_mean_error": 1.7100098330974578,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.08441456452012064,
              "gap_to_oracle": 0.008415785372257067,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7286869840025901
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.882590970158577
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0851316015124322
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3057706088940302
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.073957705497745,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4902407429946793,
                  "rejected_mean_error": 4.438814097881317,
                  "gap_rejected_minus_accepted": 2.948573354886638
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.016712486743927,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3057706088940302,
                  "rejected_mean_error": 3.223080487251282,
                  "gap_rejected_minus_accepted": 1.9173098783572518
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.533466637134552,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0851316015124322,
                  "rejected_mean_error": 2.485064555454254,
                  "gap_rejected_minus_accepted": 1.399932953941822
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1104669868946075,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.882590970158577,
                  "rejected_mean_error": 2.085933781258265,
                  "gap_rejected_minus_accepted": 1.203342811099688
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1563004016876226,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.491687898006704,
                  "rejected_mean_error": 4.519052894115448,
                  "gap_rejected_minus_accepted": 3.0273649961087434
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0332350730895996,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.30236383330822,
                  "rejected_mean_error": 3.2706060905456544,
                  "gap_rejected_minus_accepted": 1.9682422572374345
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5415182709693909,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0779296801686287,
                  "rejected_mean_error": 2.510919115066528,
                  "gap_rejected_minus_accepted": 1.4329894348978995
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1145033836364746,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8691102238893509,
                  "rejected_mean_error": 2.1028624555269877,
                  "gap_rejected_minus_accepted": 1.2337522316376368
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8123286624196704,
              "spearman": 0.7065300258460302,
              "auroc_top30_bad": 0.7810704761904762,
              "mae": 0.46166310164928437,
              "mse": 0.489073044525976,
              "expert_lt_perturb_large": 0.98,
              "expert_lt_other_task": 0.516,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.8836500262369019,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47561886078119275
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6943267844438553
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.817038269519806
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1036818165222804
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8237708099705128,
              "spearman": 0.7459202224129425,
              "auroc_top30_worst": 0.8478994285714285,
              "pairwise_seed_ranking": 0.7496,
              "predicted_best_mean_error": 2.010444975733757,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.094036028981209,
              "gap_to_oracle": 0.021549746036529482,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2555542476177215
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.222181449429347
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4830646719455718
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.607994439854805
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.2421831607818605,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8439929676850637,
                  "rejected_mean_error": 4.203046527862549,
                  "gap_rejected_minus_accepted": 2.359053560177485
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.656107723712921,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6070089325897212,
                  "rejected_mean_error": 3.4955448395908832,
                  "gap_rejected_minus_accepted": 1.888535907001162
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7987743616104126,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4830646719455718,
                  "rejected_mean_error": 2.6767319754600525,
                  "gap_rejected_minus_accepted": 1.1936673035144807
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.212018460035324,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2235540929503335,
                  "rejected_mean_error": 2.3659556814675144,
                  "gap_rejected_minus_accepted": 1.142401588517181
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.280174779891968,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.87010922325982,
                  "rejected_mean_error": 4.21382703781128,
                  "gap_rejected_minus_accepted": 2.34371781455146
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7164910435676575,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6228707295688078,
                  "rejected_mean_error": 3.5340226150694347,
                  "gap_rejected_minus_accepted": 1.9111518855006269
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8405596613883972,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4941935739517211,
                  "rejected_mean_error": 2.7147684354782102,
                  "gap_rejected_minus_accepted": 1.220574861526489
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.189490020275116,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1638593437179687,
                  "rejected_mean_error": 2.4213749332861467,
                  "gap_rejected_minus_accepted": 1.257515589568178
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6536277521946087,
              "spearman": 0.5811329003021052,
              "auroc_top30_bad": 0.6851108571428571,
              "mae": 0.49859354817271234,
              "mse": 0.6051840002339953,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.492,
              "expert_lt_simvla_seed0": 0.952,
              "same_context_pred_std": 0.6461513319482165,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5962346079349518
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.651244149684906
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8918205834984779
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1269478567679723
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8610148233770789,
              "spearman": 0.8068032033300502,
              "auroc_top30_worst": 0.861632,
              "pairwise_seed_ranking": 0.7672,
              "predicted_best_mean_error": 1.6029009469747544,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.05424219548702225,
              "gap_to_oracle": 0.023003425478935302,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40307791805267335
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7888825071545748
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1128773106575012
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3637691790234052
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.131618881225587,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4797451322873434,
                  "rejected_mean_error": 3.1520585174560547,
                  "gap_rejected_minus_accepted": 1.6723133851687113
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8093335628509521,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3627281260846646,
                  "rejected_mean_error": 2.4979052216100235,
                  "gap_rejected_minus_accepted": 1.1351770955253588
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4957693815231323,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1128773106575012,
                  "rejected_mean_error": 2.181075630950928,
                  "gap_rejected_minus_accepted": 1.0681983202934267
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0374463200569153,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7909779382970767,
                  "rejected_mean_error": 1.932918349859427,
                  "gap_rejected_minus_accepted": 1.1419404115623502
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1838246822357177,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4862745711538528,
                  "rejected_mean_error": 3.194960284233093,
                  "gap_rejected_minus_accepted": 1.7086857130792403
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8315618634223938,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3574807302837066,
                  "rejected_mean_error": 2.5466172865458896,
                  "gap_rejected_minus_accepted": 1.189136556262183
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5275794863700867,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0886347107887269,
                  "rejected_mean_error": 2.225651574134827,
                  "gap_rejected_minus_accepted": 1.1370168633461
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0225926041603088,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8012374648972164,
                  "rejected_mean_error": 1.9454963921225645,
                  "gap_rejected_minus_accepted": 1.1442589272253483
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5199003058748236,
              "spearman": 0.42342587562346146,
              "auroc_top30_bad": 0.5859272380952381,
              "mae": 0.4614382997751236,
              "mse": 0.5894508894895667,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.988,
              "same_context_pred_std": 0.5906425442763901,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6467028358578681
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9680383170366287
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.046624728012085
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.25763592338562
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6972773303730619,
              "spearman": 0.5677019850892705,
              "auroc_top30_worst": 0.681831619047619,
              "pairwise_seed_ranking": 0.7508,
              "predicted_best_mean_error": 1.6095581592321395,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.052192968726158195,
              "gap_to_oracle": 0.017534227252006485,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9146379144191742
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3153801553715498
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.469288575410843
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5753758253891077
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8655693531036377,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6187996847629547,
                  "rejected_mean_error": 2.0289358053207396,
                  "gap_rejected_minus_accepted": 0.4101361205577849
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.755749672651291,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5750130612478694,
                  "rejected_mean_error": 1.9136721489909359,
                  "gap_rejected_minus_accepted": 0.3386590877430664
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5601454973220825,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.469288575410843,
                  "rejected_mean_error": 1.8503380182266236,
                  "gap_rejected_minus_accepted": 0.3810494428157807
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3538374602794647,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.317149942008832,
                  "rejected_mean_error": 1.7742782168352744,
                  "gap_rejected_minus_accepted": 0.45712827482644247
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8621440529823303,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6221821994251675,
                  "rejected_mean_error": 2.0178714847564696,
                  "gap_rejected_minus_accepted": 0.3956892853313021
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7735927104949951,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5766934930959486,
                  "rejected_mean_error": 1.9142237901687622,
                  "gap_rejected_minus_accepted": 0.33753029707281357
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5689610242843628,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4530669140815735,
                  "rejected_mean_error": 1.870435341835022,
                  "gap_rejected_minus_accepted": 0.4173684277534484
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.344507098197937,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3442811615883359,
                  "rejected_mean_error": 1.7687062503182314,
                  "gap_rejected_minus_accepted": 0.4244250887298955
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
        "best_epoch": 80,
        "best_calib_loss": 0.009014376439154148,
        "train_time_sec": 47.61969757080078,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995828539441362,
              "spearman": 0.9984220460749018,
              "auroc_top30_bad": 0.9993904285714287,
              "mae": 0.025756856530485674,
              "mse": 0.0011711700641557307,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8060423287716617,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0016948055550456047
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19982709831595422
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6186869179219008
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9865990408241749
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4164188162431122
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996403186950565,
              "spearman": 0.999150636054005,
              "auroc_top30_worst": 0.9996295238095237,
              "pairwise_seed_ranking": 0.9568,
              "predicted_best_mean_error": 1.7031487736701965,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.09127562394738198,
              "gap_to_oracle": 0.0015547259449957274,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7225461766123772
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8793155644178391
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0839092056155204
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3052735793352126
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1206366777420054,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4899544044004547,
                  "rejected_mean_error": 4.44139114522934,
                  "gap_rejected_minus_accepted": 2.9514367408288855
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9906667172908783,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3052735793352126,
                  "rejected_mean_error": 3.2245715759277345,
                  "gap_rejected_minus_accepted": 1.9192979965925219
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.488910436630249,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0839092056155204,
                  "rejected_mean_error": 2.4862869513511656,
                  "gap_rejected_minus_accepted": 1.4023777457356452
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.062557727098465,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8793155644178391,
                  "rejected_mean_error": 2.0870255831718443,
                  "gap_rejected_minus_accepted": 1.207710018754005
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.18107705116272,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4916475952002737,
                  "rejected_mean_error": 4.519415619373322,
                  "gap_rejected_minus_accepted": 3.0277680241730485
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.995166689157486,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3022425275246303,
                  "rejected_mean_error": 3.2709700078964232,
                  "gap_rejected_minus_accepted": 1.968727480371793
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4822798371315002,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.076591155588627,
                  "rejected_mean_error": 2.5122576396465304,
                  "gap_rejected_minus_accepted": 1.4356664840579034
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0546385943889618,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8666960793733597,
                  "rejected_mean_error": 2.1036671703656515,
                  "gap_rejected_minus_accepted": 1.236971090992292
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9926691774979047,
              "spearman": 0.9871022112028071,
              "auroc_top30_bad": 0.9923291428571429,
              "mae": 0.0970072357257828,
              "mse": 0.019369968693281548,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.905377918769603,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0740316514968872
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1910137516736984
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5851985938668252
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0188502525091172
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9922988284945905,
              "spearman": 0.9931858757029606,
              "auroc_top30_worst": 0.9979245714285714,
              "pairwise_seed_ranking": 0.9144,
              "predicted_best_mean_error": 1.9932112547159195,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.11126974999904649,
              "gap_to_oracle": 0.0043160250186919935,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6182644894123077
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8676446755536091
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.226048609304428
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.553132524972023
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.099062824249268,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8419771511024898,
                  "rejected_mean_error": 4.221188877105713,
                  "gap_rejected_minus_accepted": 2.3792117260032235
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7470244765281677,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.551872720172591,
                  "rejected_mean_error": 3.660601168775711,
                  "gap_rejected_minus_accepted": 2.10872844860312
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8142791390419006,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.226048609304428,
                  "rejected_mean_error": 2.9337480381011964,
                  "gap_rejected_minus_accepted": 1.7076994287967684
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2689123749732971,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8692051674039981,
                  "rejected_mean_error": 2.4843241059029495,
                  "gap_rejected_minus_accepted": 1.6151189384989513
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.133346939086914,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8657044590844047,
                  "rejected_mean_error": 4.253469915390014,
                  "gap_rejected_minus_accepted": 2.3877654563056097
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.831879734992981,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5588921289392972,
                  "rejected_mean_error": 3.7239273502713157,
                  "gap_rejected_minus_accepted": 2.1650352213320185
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8335820436477661,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2246744527816773,
                  "rejected_mean_error": 2.9842875566482543,
                  "gap_rejected_minus_accepted": 1.759613103866577
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2901952266693115,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8654266766139439,
                  "rejected_mean_error": 2.521916420064508,
                  "gap_rejected_minus_accepted": 1.6564897434505643
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9895237820967742,
              "spearman": 0.9877426955247764,
              "auroc_top30_bad": 0.9906674285714286,
              "mae": 0.09262515078485012,
              "mse": 0.02024042299543349,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.762014033264285,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.047613142013549804
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17885076265335084
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6264512667059898
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.040150798312823
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9872165705832866,
              "spearman": 0.9881751210080775,
              "auroc_top30_worst": 0.9814217142857142,
              "pairwise_seed_ranking": 0.89,
              "predicted_best_mean_error": 1.586227074623108,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.07091606783866866,
              "gap_to_oracle": 0.006329553127288889,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.401125116109848
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6541099164348382
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0242801959037782
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3063204857205022
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.624706101417545,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4601333913273282,
                  "rejected_mean_error": 3.3285641860961914,
                  "gap_rejected_minus_accepted": 1.8684307947688632
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9946913123130798,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3056717674022296,
                  "rejected_mean_error": 2.668709720285556,
                  "gap_rejected_minus_accepted": 1.3630379528833263
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6566760540008545,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0242801959037782,
                  "rejected_mean_error": 2.269672745704651,
                  "gap_rejected_minus_accepted": 1.2453925498008727
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0900039970874786,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6554360342101929,
                  "rejected_mean_error": 1.9781954213420254,
                  "gap_rejected_minus_accepted": 1.3227593871318324
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7443535566329955,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4644031617376538,
                  "rejected_mean_error": 3.391802968978882,
                  "gap_rejected_minus_accepted": 1.927399807241228
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.019275724887848,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3031352691471896,
                  "rejected_mean_error": 2.7079284172209483,
                  "gap_rejected_minus_accepted": 1.4047931480737588
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6667841672897339,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0133864045143128,
                  "rejected_mean_error": 2.300899880409241,
                  "gap_rejected_minus_accepted": 1.287513475894928
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1163406074047089,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6435922592405289,
                  "rejected_mean_error": 1.9986068090015554,
                  "gap_rejected_minus_accepted": 1.3550145497610266
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9886481258258999,
              "spearman": 0.9777945392271092,
              "auroc_top30_bad": 0.9763839999999999,
              "mae": 0.08322464252077043,
              "mse": 0.015096256724420274,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7226369529509462,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05961813652515412
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21602241978645326
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7836581362724304
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1404835963567097
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9653405710855133,
              "spearman": 0.9499161443303324,
              "auroc_top30_worst": 0.9520944761904762,
              "pairwise_seed_ranking": 0.9072,
              "predicted_best_mean_error": 1.5985258388519288,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06322528910636893,
              "gap_to_oracle": 0.0065019068717957484,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8507589948177338
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1003117577578776
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3618831221103669
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5216984087025434
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.003371596336365,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6002461128499772,
                  "rejected_mean_error": 2.1959179525375365,
                  "gap_rejected_minus_accepted": 0.5956718396875593
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.854643166065216,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5213070695975293,
                  "rejected_mean_error": 2.0744469546662354,
                  "gap_rejected_minus_accepted": 0.5531398850687061
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6976467967033386,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3618831221103669,
                  "rejected_mean_error": 1.9577434715270996,
                  "gap_rejected_minus_accepted": 0.5958603494167327
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4137089252471924,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1014711579766137,
                  "rejected_mean_error": 1.8463245982675949,
                  "gap_rejected_minus_accepted": 0.7448534402909812
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0004005670547484,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6022532433933683,
                  "rejected_mean_error": 2.1972320890426635,
                  "gap_rejected_minus_accepted": 0.5949788456492953
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8467637598514557,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5309539239674328,
                  "rejected_mean_error": 2.049990447740706,
                  "gap_rejected_minus_accepted": 0.5190365237732733
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.716612696647644,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3738860716819763,
                  "rejected_mean_error": 1.9496161842346191,
                  "gap_rejected_minus_accepted": 0.5757301125526428
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4340913891792297,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1120794453318157,
                  "rejected_mean_error": 1.8469346360089307,
                  "gap_rejected_minus_accepted": 0.734855190677115
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
        "best_epoch": 71,
        "best_calib_loss": 0.01093748677521944,
        "train_time_sec": 53.00937795639038,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9988074864558489,
              "spearman": 0.9971115691890745,
              "auroc_top30_bad": 0.9992027619047619,
              "mae": 0.03869535177182915,
              "mse": 0.0028300551832056526,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8088813815395888,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.008083463050425052
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20056918422579764
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6188665573567153
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9867673078993956
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4164188162431122
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9991741356236583,
              "spearman": 0.9981174493086528,
              "auroc_top30_worst": 0.9995116190476191,
              "pairwise_seed_ranking": 0.962,
              "predicted_best_mean_error": 1.7029961129426956,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.09142828467488284,
              "gap_to_oracle": 0.0014020652174948633,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7253280438780785
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8804500795125961
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0844900006175042
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.305380154856046
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.163908481597905,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4900407304167747,
                  "rejected_mean_error": 4.440614211082458,
                  "gap_rejected_minus_accepted": 2.9505734806656836
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0504284501075745,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.305380154856046,
                  "rejected_mean_error": 3.2242518493652343,
                  "gap_rejected_minus_accepted": 1.9188716945091884
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5402077436447144,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0844900006175042,
                  "rejected_mean_error": 2.485706156349182,
                  "gap_rejected_minus_accepted": 1.4012161557316778
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1113340258598328,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8804500795125961,
                  "rejected_mean_error": 2.0866474114735922,
                  "gap_rejected_minus_accepted": 1.206197331960996
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.249457311630249,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.491825414399306,
                  "rejected_mean_error": 4.517815246582031,
                  "gap_rejected_minus_accepted": 3.025989832182725
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0556721687316895,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3021367488304774,
                  "rejected_mean_error": 3.271287343978882,
                  "gap_rejected_minus_accepted": 1.9691505951484045
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5298117995262146,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.07684196048975,
                  "rejected_mean_error": 2.512006834745407,
                  "gap_rejected_minus_accepted": 1.435164874255657
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1002918481826782,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8671783577203751,
                  "rejected_mean_error": 2.1035064109166464,
                  "gap_rejected_minus_accepted": 1.2363280531962713
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9907576994702688,
              "spearman": 0.9823235236984889,
              "auroc_top30_bad": 0.9932975238095239,
              "mae": 0.11139260838809678,
              "mse": 0.024864280180203834,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8759047924992851,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09072802722454071
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20813982100486755
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5874466431260109
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0192317586660384
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9945661966480808,
              "spearman": 0.991989128185042,
              "auroc_top30_worst": 0.9993325714285715,
              "pairwise_seed_ranking": 0.9136,
              "predicted_best_mean_error": 1.992468312382698,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.11201269233226796,
              "gap_to_oracle": 0.003573082685470519,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6252207038402557
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8689887327834581
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2234644446849823
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5492073583132677
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.98766725063324,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8419498130745358,
                  "rejected_mean_error": 4.2214349193573,
                  "gap_rejected_minus_accepted": 2.379485106282764
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7758296132087708,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5481260355597755,
                  "rejected_mean_error": 3.6718172821373987,
                  "gap_rejected_minus_accepted": 2.123691246577623
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7499738335609436,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2234644446849823,
                  "rejected_mean_error": 2.936332202720642,
                  "gap_rejected_minus_accepted": 1.71286775803566
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1741096079349518,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8705099911545031,
                  "rejected_mean_error": 2.4838882362829837,
                  "gap_rejected_minus_accepted": 1.6133782451284806
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.082135152816773,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.865332776175605,
                  "rejected_mean_error": 4.256815061569214,
                  "gap_rejected_minus_accepted": 2.391482285393609
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8906859755516052,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5548569416617328,
                  "rejected_mean_error": 3.7359048109205943,
                  "gap_rejected_minus_accepted": 2.1810478692588617
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7744271755218506,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2222430114746095,
                  "rejected_mean_error": 2.986718997955322,
                  "gap_rejected_minus_accepted": 1.7644759864807127
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1752210855484009,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8677580753962199,
                  "rejected_mean_error": 2.5211309755549713,
                  "gap_rejected_minus_accepted": 1.6533729001587516
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9871312738326052,
              "spearman": 0.9797062179621575,
              "auroc_top30_bad": 0.9774590476190476,
              "mae": 0.11027245842406447,
              "mse": 0.02593369716684569,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7531970239764304,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06271045333147049
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.185923277425766
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.630175691640377
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0447309526046118
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9844988802778281,
              "spearman": 0.9749344423260432,
              "auroc_top30_worst": 0.962663619047619,
              "pairwise_seed_ranking": 0.8996,
              "predicted_best_mean_error": 1.5848120694160461,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.0723310730457305,
              "gap_to_oracle": 0.0049145479202270526,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3991815419197082
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6571075744353808
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0327724242210388
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3142253584317816
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.536730647087097,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4595137316915725,
                  "rejected_mean_error": 3.3341411228179934,
                  "gap_rejected_minus_accepted": 1.8746273911264209
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9715899229049683,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.313498399237304,
                  "rejected_mean_error": 2.645279835207394,
                  "gap_rejected_minus_accepted": 1.33178143597009
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6312044858932495,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0327724242210388,
                  "rejected_mean_error": 2.2611805173873902,
                  "gap_rejected_minus_accepted": 1.2284080931663515
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0236095190048218,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.65845777737066,
                  "rejected_mean_error": 1.9771860236800975,
                  "gap_rejected_minus_accepted": 1.3187282463094374
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6987662076950074,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4650840894381205,
                  "rejected_mean_error": 3.3856746196746825,
                  "gap_rejected_minus_accepted": 1.920590530236562
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9808738827705383,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3067266325899625,
                  "rejected_mean_error": 2.6972683384304954,
                  "gap_rejected_minus_accepted": 1.390541705840533
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.648266851902008,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0212192463874816,
                  "rejected_mean_error": 2.293067038536072,
                  "gap_rejected_minus_accepted": 1.2718477921485902
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0104674994945526,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6463249439284915,
                  "rejected_mean_error": 1.997686171914167,
                  "gap_rejected_minus_accepted": 1.3513612279856755
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9804222459769105,
              "spearman": 0.9768456190632094,
              "auroc_top30_bad": 0.9817363809523811,
              "mae": 0.1132607690244251,
              "mse": 0.026988008219408208,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6767915526741363,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08220549476146698
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22002614171504975
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7847507157325745
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1398912264506023
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9596293343228173,
              "spearman": 0.9576716713418697,
              "auroc_top30_worst": 0.9673417142857142,
              "pairwise_seed_ranking": 0.8848,
              "predicted_best_mean_error": 1.5991718037128448,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06257932424545287,
              "gap_to_oracle": 0.007147871732711808,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8470604498386383
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1021962273770418
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3601772934436798
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5211663527338743
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0799985170364383,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5994994745519426,
                  "rejected_mean_error": 2.2026376972198487,
                  "gap_rejected_minus_accepted": 0.6031382226679061
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9220757484436035,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.52069432901471,
                  "rejected_mean_error": 2.0762812611394037,
                  "gap_rejected_minus_accepted": 0.5555869321246938
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.685570478439331,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3601772934436798,
                  "rejected_mean_error": 1.9594493001937867,
                  "gap_rejected_minus_accepted": 0.599272006750107
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3224839270114899,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.103150470664326,
                  "rejected_mean_error": 1.8457636325565447,
                  "gap_rejected_minus_accepted": 0.7426131618922187
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0758614540100098,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6076356524891324,
                  "rejected_mean_error": 2.148790407180786,
                  "gap_rejected_minus_accepted": 0.5411547546916535
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9295973181724548,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5281915374618162,
                  "rejected_mean_error": 2.0581899124478538,
                  "gap_rejected_minus_accepted": 0.5299983749860375
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7032188773155212,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3703942217826843,
                  "rejected_mean_error": 1.953108034133911,
                  "gap_rejected_minus_accepted": 0.5827138123512268
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3248361945152283,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1122509666851588,
                  "rejected_mean_error": 1.8468768507401574,
                  "gap_rejected_minus_accepted": 0.7346258840549986
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
        "best_epoch": 75,
        "best_calib_loss": 0.01368700247257948,
        "train_time_sec": 31.556561946868896,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993295023579037,
              "spearman": 0.9978331798555344,
              "auroc_top30_bad": 0.9993380238095237,
              "mae": 0.029134604760593083,
              "mse": 0.0015568372934189267,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8114044397315399,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0021228255182504656
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19984187349677085
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6187394166439771
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9869842651188374
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4164188162431122
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995153571596677,
              "spearman": 0.9986868128514411,
              "auroc_top30_worst": 0.9995691428571428,
              "pairwise_seed_ranking": 0.9625,
              "predicted_best_mean_error": 1.7022930064797401,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.0921313911378383,
              "gap_to_oracle": 0.0006989587545394027,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7219591509699822
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8795208202123642
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0843532946944237
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3053867231289547
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1408658981323243,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4900690446363556,
                  "rejected_mean_error": 4.440359383106232,
                  "gap_rejected_minus_accepted": 2.9502903384698764
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0241920948028564,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3053867231289547,
                  "rejected_mean_error": 3.2242321445465087,
                  "gap_rejected_minus_accepted": 1.918845421417554
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5350763201713562,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0843532946944237,
                  "rejected_mean_error": 2.4858428622722624,
                  "gap_rejected_minus_accepted": 1.4014895675778387
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1026745736598969,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8795208202123642,
                  "rejected_mean_error": 2.0869571645736693,
                  "gap_rejected_minus_accepted": 1.2074363443613052
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.212505960464478,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4916909336050352,
                  "rejected_mean_error": 4.5190255737304685,
                  "gap_rejected_minus_accepted": 3.0273346401254333
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0287980437278748,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3020231611331303,
                  "rejected_mean_error": 3.271628107070923,
                  "gap_rejected_minus_accepted": 1.9696049459377927
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.52348393201828,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0769334836602211,
                  "rejected_mean_error": 2.5119153115749357,
                  "gap_rejected_minus_accepted": 1.4349818279147146
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1013701856136322,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8668178707361222,
                  "rejected_mean_error": 2.1036265732447306,
                  "gap_rejected_minus_accepted": 1.2368087025086085
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9884730954684553,
              "spearman": 0.9788124507058474,
              "auroc_top30_bad": 0.9876647619047619,
              "mae": 0.12396820917260411,
              "mse": 0.031356993075377294,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8829440881386527,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08777400118112565
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21166522142887115
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5890583424210548
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0210497857173284
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9915999567862014,
              "spearman": 0.9862876338480858,
              "auroc_top30_worst": 0.9994514285714285,
              "pairwise_seed_ranking": 0.9332,
              "predicted_best_mean_error": 1.9927438871860503,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.11173711752891569,
              "gap_to_oracle": 0.003848657488822793,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6435894620418549
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8729295049531337
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.231236095571518
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.548097291067719
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.063824510574341,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8425893371105193,
                  "rejected_mean_error": 4.215679203033448,
                  "gap_rejected_minus_accepted": 2.3730898659229283
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.782796025276184,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5470176077385214,
                  "rejected_mean_error": 3.675135482995274,
                  "gap_rejected_minus_accepted": 2.128117875256753
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7255260944366455,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.231236095571518,
                  "rejected_mean_error": 2.9285605518341065,
                  "gap_rejected_minus_accepted": 1.6973244562625884
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.158036470413208,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8743714889207967,
                  "rejected_mean_error": 2.4825983229416284,
                  "gap_rejected_minus_accepted": 1.6082268340208317
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.179214191436768,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.86610019048055,
                  "rejected_mean_error": 4.249908332824707,
                  "gap_rejected_minus_accepted": 2.383808142344157
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8988746404647827,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5549441582378856,
                  "rejected_mean_error": 3.7356459299723306,
                  "gap_rejected_minus_accepted": 2.1807017717344452
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7306792736053467,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2308435773849487,
                  "rejected_mean_error": 2.9781184320449827,
                  "gap_rejected_minus_accepted": 1.747274854660034
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.170277714729309,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8673294177131047,
                  "rejected_mean_error": 2.5212753896407265,
                  "gap_rejected_minus_accepted": 1.6539459719276217
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9841401720340858,
              "spearman": 0.974698970289249,
              "auroc_top30_bad": 0.9707725714285714,
              "mae": 0.12636724918342407,
              "mse": 0.031462463680536,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.736584652835483,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05550540548563004
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19310453097820282
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6329051347136497
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.05038848853906
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9817933079359409,
              "spearman": 0.9661617017354893,
              "auroc_top30_worst": 0.9526399999999999,
              "pairwise_seed_ranking": 0.8972,
              "predicted_best_mean_error": 1.584451998114586,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.0726911443471907,
              "gap_to_oracle": 0.004554476618766845,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4091601822376251
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6559926032637938
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0381217917442322
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3164868327473271
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4906992912292485,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.459008149517907,
                  "rejected_mean_error": 3.3386913623809815,
                  "gap_rejected_minus_accepted": 1.8796832128630745
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9803736507892609,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3158372286289708,
                  "rejected_mean_error": 2.6382782916291454,
                  "gap_rejected_minus_accepted": 1.3224410630001746
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6049970388412476,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0381217917442322,
                  "rejected_mean_error": 2.2558311498641967,
                  "gap_rejected_minus_accepted": 1.2177093581199645
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0856241285800934,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6577477738880121,
                  "rejected_mean_error": 1.9774231966684315,
                  "gap_rejected_minus_accepted": 1.3196754227804193
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6375714778900146,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.464966651863522,
                  "rejected_mean_error": 3.3867315578460695,
                  "gap_rejected_minus_accepted": 1.9217649059825475
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.000991642475128,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3104492492854276,
                  "rejected_mean_error": 2.686218666651892,
                  "gap_rejected_minus_accepted": 1.3757694173664645
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6291810274124146,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0325701909065246,
                  "rejected_mean_error": 2.2817160940170287,
                  "gap_rejected_minus_accepted": 1.249145903110504
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0737275779247284,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.645200370796143,
                  "rejected_mean_error": 1.9980650387983272,
                  "gap_rejected_minus_accepted": 1.352864668002184
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9798778539001531,
              "spearman": 0.9721699503929494,
              "auroc_top30_bad": 0.9741828571428572,
              "mae": 0.11498775181632809,
              "mse": 0.026635657660437947,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.697117006155358,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06069913858175278
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22315181746482848
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7864355658531189
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1416331508636475
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9407971096735677,
              "spearman": 0.9344721643981853,
              "auroc_top30_worst": 0.9457432380952382,
              "pairwise_seed_ranking": 0.8908,
              "predicted_best_mean_error": 1.5989373488426208,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06281377911567687,
              "gap_to_oracle": 0.006913416862487809,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8427051355838776
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1036703014411988
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3638029009342194
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5246618643307737
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0885461568832397,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6083158334361183,
                  "rejected_mean_error": 2.123290467262268,
                  "gap_rejected_minus_accepted": 0.5149746338261496
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9047113060951233,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5244250822029093,
                  "rejected_mean_error": 2.0651128402533243,
                  "gap_rejected_minus_accepted": 0.540687758050415
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6809725761413574,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3638029009342194,
                  "rejected_mean_error": 1.955823692703247,
                  "gap_rejected_minus_accepted": 0.5920207917690277
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.365049123764038,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1046588608441643,
                  "rejected_mean_error": 1.845259762624539,
                  "gap_rejected_minus_accepted": 0.7406009017803747
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0999431133270265,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6124383515781826,
                  "rejected_mean_error": 2.1055661153793337,
                  "gap_rejected_minus_accepted": 0.4931277638011511
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9000052213668823,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5332864060758906,
                  "rejected_mean_error": 2.0430670484663946,
                  "gap_rejected_minus_accepted": 0.509780642390504
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.689516544342041,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3793487610816955,
                  "rejected_mean_error": 1.9441534948349,
                  "gap_rejected_minus_accepted": 0.5648047337532045
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3800317645072937,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1124633635793413,
                  "rejected_mean_error": 1.8468052945672508,
                  "gap_rejected_minus_accepted": 0.7343419309879096
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
        "best_epoch": 45,
        "best_calib_loss": 0.09158487617969513,
        "train_time_sec": 13.885398149490356,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9073353781862434,
              "spearman": 0.8183906509598459,
              "auroc_top30_bad": 0.8835642619047619,
              "mae": 0.2150787087161676,
              "mse": 0.20864498632183537,
              "expert_lt_perturb_large": 0.986,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.975,
              "same_context_pred_std": 0.7414953076492821,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5376026352135231
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5585937593606767
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7099549186668126
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0022992856606066
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4028596238854691
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9968316913273257,
              "spearman": 0.9954591347060385,
              "auroc_top30_worst": 0.9982659047619048,
              "pairwise_seed_ranking": 0.841,
              "predicted_best_mean_error": 1.6925523170232772,
              "seed0_mean_error": 1.7753875075280667,
              "random_seed_mean_error": 1.7670326000750065,
              "oracle_best_mean_error": 1.6848166666328908,
              "improvement_over_seed0": 0.08283519050478949,
              "gap_to_oracle": 0.007735650390386484,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6947774327993393
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8503453673839569
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0597814724445342
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2837660943984985
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7651591389894485
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.962892556190491,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4688965906302134,
                  "rejected_mean_error": 4.431522074222564,
                  "gap_rejected_minus_accepted": 2.962625483592351
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9178723692893982,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2837660943984985,
                  "rejected_mean_error": 3.2093382727622988,
                  "gap_rejected_minus_accepted": 1.9255721783638002
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4531872272491455,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0597814724445342,
                  "rejected_mean_error": 2.470536805534363,
                  "gap_rejected_minus_accepted": 1.4107553330898286
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0631975531578064,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8503453673839569,
                  "rejected_mean_error": 2.0700970628579456,
                  "gap_rejected_minus_accepted": 1.2197516954739887
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.026795530319214,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4716763060291609,
                  "rejected_mean_error": 4.508788321018219,
                  "gap_rejected_minus_accepted": 3.0371120149890585
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.917915254831314,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.282499285976092,
                  "rejected_mean_error": 3.2540521721839903,
                  "gap_rejected_minus_accepted": 1.9715528862078984
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4528335928916931,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0554785031676293,
                  "rejected_mean_error": 2.495296511888504,
                  "gap_rejected_minus_accepted": 1.439818008720875
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0749346017837524,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8424277557134628,
                  "rejected_mean_error": 2.086374091466268,
                  "gap_rejected_minus_accepted": 1.2439463357528053
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8097899883839355,
              "spearman": 0.6971525432974507,
              "auroc_top30_bad": 0.7660190476190477,
              "mae": 0.4707352191567421,
              "mse": 0.49472914926673145,
              "expert_lt_perturb_large": 0.976,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 0.944,
              "same_context_pred_std": 0.8383425642656263,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5594203338623047
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6906688909769059
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7706512782216072
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1242119467258453
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8332675679591165,
              "spearman": 0.761187826424209,
              "auroc_top30_worst": 0.860135619047619,
              "pairwise_seed_ranking": 0.7552,
              "predicted_best_mean_error": 2.0097713240385056,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.09470968067646046,
              "gap_to_oracle": 0.020876094341278018,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2277326693534851
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.172030058522255
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.458064987564087
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6093908038411313
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.215927314758302,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8431366404162512,
                  "rejected_mean_error": 4.21075347328186,
                  "gap_rejected_minus_accepted": 2.3676168328656093
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.58766633272171,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6094598578986898,
                  "rejected_mean_error": 3.488207724528572,
                  "gap_rejected_minus_accepted": 1.878747866629882
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.670718014240265,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.458064987564087,
                  "rejected_mean_error": 2.7017316598415375,
                  "gap_rejected_minus_accepted": 1.2436666722774505
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1397645473480225,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.17524698833688,
                  "rejected_mean_error": 2.3820924197215283,
                  "gap_rejected_minus_accepted": 1.2068454313846484
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.2519148826599125,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8661083624098036,
                  "rejected_mean_error": 4.249834785461426,
                  "gap_rejected_minus_accepted": 2.383726423051622
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6148130297660828,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6235038418183352,
                  "rejected_mean_error": 3.532143377122425,
                  "gap_rejected_minus_accepted": 1.9086395353040897
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7246186137199402,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4772827825546264,
                  "rejected_mean_error": 2.731679226875305,
                  "gap_rejected_minus_accepted": 1.2543964443206785
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1659099757671356,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1455468251591636,
                  "rejected_mean_error": 2.427544391410236,
                  "gap_rejected_minus_accepted": 1.2819975662510723
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6440575723223321,
              "spearman": 0.5555419470190013,
              "auroc_top30_bad": 0.668599619047619,
              "mae": 0.524073143774271,
              "mse": 0.6496221082819993,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.6318520430487917,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5859162237048149
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8581081382989884
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.888701919066906
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1302773050864539
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8435442361992107,
              "spearman": 0.7576586614135434,
              "auroc_top30_worst": 0.8294034285714287,
              "pairwise_seed_ranking": 0.7796,
              "predicted_best_mean_error": 1.5989570860862732,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.05818605637550345,
              "gap_to_oracle": 0.019059564590454103,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40839564967155456
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8298322373093703
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1704574803352357
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.348950096602633
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0795120239257816,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4813283308347067,
                  "rejected_mean_error": 3.137809730529785,
                  "gap_rejected_minus_accepted": 1.6564813996950782
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6847236156463623,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.348425893735224,
                  "rejected_mean_error": 2.5407205305922145,
                  "gap_rejected_minus_accepted": 1.1922946368569904
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.358410120010376,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1704574803352357,
                  "rejected_mean_error": 2.1234954612731936,
                  "gap_rejected_minus_accepted": 0.9530379809379579
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0089759826660156,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8321004513734446,
                  "rejected_mean_error": 1.919181587220256,
                  "gap_rejected_minus_accepted": 1.0870811358468115
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1596390008926387,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4862745711538528,
                  "rejected_mean_error": 3.194960284233093,
                  "gap_rejected_minus_accepted": 1.7086857130792403
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.735156238079071,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3436752924307145,
                  "rejected_mean_error": 2.587595332236517,
                  "gap_rejected_minus_accepted": 1.2439200398058023
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3731107115745544,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1481782698631287,
                  "rejected_mean_error": 2.166108015060425,
                  "gap_rejected_minus_accepted": 1.0179297451972962
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0089759826660156,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8113791100562565,
                  "rejected_mean_error": 1.9420796881385027,
                  "gap_rejected_minus_accepted": 1.130700578082246
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5064077552003428,
              "spearman": 0.39195303679932747,
              "auroc_top30_bad": 0.5828643809523809,
              "mae": 0.4887903015553951,
              "mse": 0.6213055158827264,
              "expert_lt_perturb_large": 0.988,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.5801196351797555,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2486706844568252
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9672044999837875
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0451815161466598
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2591699870427449
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7158597486266789,
              "spearman": 0.5967187332599894,
              "auroc_top30_worst": 0.719719619047619,
              "pairwise_seed_ranking": 0.748,
              "predicted_best_mean_error": 1.6063806923627852,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.05537043559551247,
              "gap_to_oracle": 0.014356760382652212,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.871382979631424
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2718517968478875
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4559047649860382
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5796433543917467
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7786556482315068,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.633472155597475,
                  "rejected_mean_error": 1.8968835678100586,
                  "gap_rejected_minus_accepted": 0.2634114122125837
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6483838856220245,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5793244819948997,
                  "rejected_mean_error": 1.900765435764203,
                  "gap_rejected_minus_accepted": 0.32144095376930326
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4855904579162598,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4559047649860382,
                  "rejected_mean_error": 1.8637218286514283,
                  "gap_rejected_minus_accepted": 0.40781706366539017
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2961320281028748,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2753973369971632,
                  "rejected_mean_error": 1.7882254584240176,
                  "gap_rejected_minus_accepted": 0.5128281214268544
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7767403364181518,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6378330079714458,
                  "rejected_mean_error": 1.8770142078399659,
                  "gap_rejected_minus_accepted": 0.23918119986852004
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6538901031017303,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5765820668342916,
                  "rejected_mean_error": 1.9145545316120935,
                  "gap_rejected_minus_accepted": 0.33797246477780196
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4936169981956482,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4582946362495421,
                  "rejected_mean_error": 1.8652076196670533,
                  "gap_rejected_minus_accepted": 0.40691298341751114
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3137376010417938,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2698457155908858,
                  "rejected_mean_error": 1.7937834326596183,
                  "gap_rejected_minus_accepted": 0.5239377170687325
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
        "best_epoch": 74,
        "best_calib_loss": 0.013291839510202408,
        "train_time_sec": 37.280436754226685,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997527412266353,
              "spearman": 0.9992273678517425,
              "auroc_top30_bad": 0.9998604285714286,
              "mae": 0.019496883286221418,
              "mse": 0.0006781099421843581,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.993,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7812942334947309,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0769127999873599
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23331548493034207
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.613860730386409
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9741823534651814
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4028596238854691
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997880991238806,
              "spearman": 0.9995391016775418,
              "auroc_top30_worst": 0.9999346666666666,
              "pairwise_seed_ranking": 0.9475,
              "predicted_best_mean_error": 1.6862678231298924,
              "seed0_mean_error": 1.7753875075280667,
              "random_seed_mean_error": 1.7670326000750065,
              "oracle_best_mean_error": 1.6848166666328908,
              "improvement_over_seed0": 0.0891196843981743,
              "gap_to_oracle": 0.001451156497001671,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6878561058044433
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8463938921928406
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0580228429317475
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2826848938306172
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7651591389894485
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1146317958831795,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.468431947098838,
                  "rejected_mean_error": 4.4357038660049435,
                  "gap_rejected_minus_accepted": 2.967271918906105
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.012374222278595,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2826848938306172,
                  "rejected_mean_error": 3.2125818744659425,
                  "gap_rejected_minus_accepted": 1.9298969806353252
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5066214203834534,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0580228429317475,
                  "rejected_mean_error": 2.4722954350471498,
                  "gap_rejected_minus_accepted": 1.4142725921154022
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0760286748409271,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8463938921928406,
                  "rejected_mean_error": 2.0714142212549844,
                  "gap_rejected_minus_accepted": 1.225020329062144
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1783810853958134,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4711077121562428,
                  "rejected_mean_error": 4.513905665874481,
                  "gap_rejected_minus_accepted": 3.0427979537182384
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0142738223075867,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2810385285615922,
                  "rejected_mean_error": 3.25843444442749,
                  "gap_rejected_minus_accepted": 1.977395915865898
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5030383467674255,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0535025705695151,
                  "rejected_mean_error": 2.497272444486618,
                  "gap_rejected_minus_accepted": 1.4437698739171028
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0754680037498474,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8390282763242721,
                  "rejected_mean_error": 2.087507251262665,
                  "gap_rejected_minus_accepted": 1.2484789749383927
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9907445223822928,
              "spearman": 0.9840578940858706,
              "auroc_top30_bad": 0.9907299047619048,
              "mae": 0.12406601749584079,
              "mse": 0.02936785291635055,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9219206867879238,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10264255785942078
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.201476775598526
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5851840199112892
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0192308551549911
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.991953647043054,
              "spearman": 0.9930297135550168,
              "auroc_top30_worst": 0.9970407619047619,
              "pairwise_seed_ranking": 0.9168,
              "predicted_best_mean_error": 1.9954929126501084,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.1089880920648576,
              "gap_to_oracle": 0.006597682952880879,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6221957924365997
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8657893896676027
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2273218507289887
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5529802006635585
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.3019246578216555,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8418884470992618,
                  "rejected_mean_error": 4.221987213134765,
                  "gap_rejected_minus_accepted": 2.3800987660355037
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8460472226142883,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5515227578302075,
                  "rejected_mean_error": 3.6616488196217594,
                  "gap_rejected_minus_accepted": 2.1101260617915516
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8470447063446045,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2273218507289887,
                  "rejected_mean_error": 2.932474796676636,
                  "gap_rejected_minus_accepted": 1.705152945947647
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2724813520908356,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.867105780984647,
                  "rejected_mean_error": 2.4850253950697128,
                  "gap_rejected_minus_accepted": 1.6179196140850658
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.36384801864624,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8657708411746554,
                  "rejected_mean_error": 4.252872476577759,
                  "gap_rejected_minus_accepted": 2.387101635403103
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.959209978580475,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5585770963985015,
                  "rejected_mean_error": 3.7248624468606617,
                  "gap_rejected_minus_accepted": 2.16628535046216
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8633259534835815,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2272732305526732,
                  "rejected_mean_error": 2.9816887788772584,
                  "gap_rejected_minus_accepted": 1.7544155483245851
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.281395822763443,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8669613486244565,
                  "rejected_mean_error": 2.5213993915262067,
                  "gap_rejected_minus_accepted": 1.6544380429017502
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9919256111837312,
              "spearman": 0.987237168124433,
              "auroc_top30_bad": 0.9894742857142858,
              "mae": 0.09050372319612653,
              "mse": 0.015381060091949575,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7532594801713558,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07041932612657548
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18725946621894837
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6268359307646751
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.040147565102577
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9944034728087001,
              "spearman": 0.9931199751167842,
              "auroc_top30_worst": 0.9882026666666667,
              "pairwise_seed_ranking": 0.8884,
              "predicted_best_mean_error": 1.5905056689977646,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06663747346401205,
              "gap_to_oracle": 0.010608147501945497,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.41186904287338255
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6528259254036806
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.023582994556427
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3040633190796573
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7307297706604015,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4587033310466342,
                  "rejected_mean_error": 3.3414347286224366,
                  "gap_rejected_minus_accepted": 1.8827313975758024
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.041754722595215,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3034003314620783,
                  "rejected_mean_error": 2.6755095141383407,
                  "gap_rejected_minus_accepted": 1.3721091826762624
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7062382698059082,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.023582994556427,
                  "rejected_mean_error": 2.270369947052002,
                  "gap_rejected_minus_accepted": 1.2467869524955748
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0864848494529724,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6541587565653622,
                  "rejected_mean_error": 1.978622089327972,
                  "gap_rejected_minus_accepted": 1.3244633327626099
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.836366820335388,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4641966636975605,
                  "rejected_mean_error": 3.393661451339722,
                  "gap_rejected_minus_accepted": 1.9294647876421613
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.061680257320404,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2999686892019873,
                  "rejected_mean_error": 2.717327630709088,
                  "gap_rejected_minus_accepted": 1.4173589415071008
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7130231261253357,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.014094795703888,
                  "rejected_mean_error": 2.3001914892196655,
                  "gap_rejected_minus_accepted": 1.2860966935157776
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0698730945587158,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.641842334043412,
                  "rejected_mean_error": 1.9991963559930974,
                  "gap_rejected_minus_accepted": 1.3573540219496856
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9857870881528601,
              "spearman": 0.9755659420689378,
              "auroc_top30_bad": 0.9745897142857143,
              "mae": 0.09701178609915077,
              "mse": 0.01919110408290941,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7054810764011267,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08062541317939759
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21476818284988403
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.784401379108429
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1396464325586955
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9615429680298592,
              "spearman": 0.9482623382158966,
              "auroc_top30_worst": 0.9578179047619048,
              "pairwise_seed_ranking": 0.9296,
              "predicted_best_mean_error": 1.5943579879999161,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06739313995838159,
              "gap_to_oracle": 0.002334056019783093,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8464996092319489
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.102683972949401
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3614243275165558
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5229281567370714
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1349962949752808,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5985284113619063,
                  "rejected_mean_error": 2.211377265930176,
                  "gap_rejected_minus_accepted": 0.6128488545682695
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9173047244548798,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.522486484578732,
                  "rejected_mean_error": 2.0709162459205896,
                  "gap_rejected_minus_accepted": 0.5484297613418576
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7459798455238342,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3614243275165558,
                  "rejected_mean_error": 1.9582022661209106,
                  "gap_rejected_minus_accepted": 0.5967779386043548
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4336241483688354,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1036967165744342,
                  "rejected_mean_error": 1.8455811619376932,
                  "gap_rejected_minus_accepted": 0.7418844453632589
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.118060517311096,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6014024350378249,
                  "rejected_mean_error": 2.2048893642425536,
                  "gap_rejected_minus_accepted": 0.6034869292047287
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9102029502391815,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5274652054603086,
                  "rejected_mean_error": 2.0603458502935985,
                  "gap_rejected_minus_accepted": 0.5328806448332899
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.761368751525879,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3739188857078553,
                  "rejected_mean_error": 1.9495833702087402,
                  "gap_rejected_minus_accepted": 0.5756644845008849
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4467214941978455,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.113523094427018,
                  "rejected_mean_error": 1.8464482729447718,
                  "gap_rejected_minus_accepted": 0.7329251785177537
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
        "best_epoch": 76,
        "best_calib_loss": 0.01239083707332611,
        "train_time_sec": 67.6448028087616,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995198444652573,
              "spearman": 0.9986053671244807,
              "auroc_top30_bad": 0.9994117142857143,
              "mae": 0.02572133211676264,
              "mse": 0.0011021889356358098,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.994,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7861220372939851,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07798031416849699
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23337488899356684
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.61410059878889
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9744153710528433
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4028596238854691
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996357194875667,
              "spearman": 0.9990022238400171,
              "auroc_top30_worst": 0.9996087619047619,
              "pairwise_seed_ranking": 0.9625,
              "predicted_best_mean_error": 1.6862683328390122,
              "seed0_mean_error": 1.7753875075280667,
              "random_seed_mean_error": 1.7670326000750065,
              "oracle_best_mean_error": 1.6848166666328908,
              "improvement_over_seed0": 0.0891191746890545,
              "gap_to_oracle": 0.0014516662061214713,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6885109720230103
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8468506674289703
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0581969421863555
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2828134585380555
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7651591389894485
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1264491319656393,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4684206732908884,
                  "rejected_mean_error": 4.435805330276489,
                  "gap_rejected_minus_accepted": 2.9673846569856006
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0079579949378967,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2828134585380555,
                  "rejected_mean_error": 3.212196180343628,
                  "gap_rejected_minus_accepted": 1.9293827218055726
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4754576683044434,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0581969421863555,
                  "rejected_mean_error": 2.4721213357925413,
                  "gap_rejected_minus_accepted": 1.4139243936061858
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0499405264854431,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8468506674289703,
                  "rejected_mean_error": 2.071261962842941,
                  "gap_rejected_minus_accepted": 1.224411295413971
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.188824439048767,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4711081275343896,
                  "rejected_mean_error": 4.513901927471161,
                  "gap_rejected_minus_accepted": 3.0427937999367716
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0243595242500305,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.28108320693175,
                  "rejected_mean_error": 3.2583004093170165,
                  "gap_rejected_minus_accepted": 1.9772172023852665
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.473950743675232,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0537862896323205,
                  "rejected_mean_error": 2.496988725423813,
                  "gap_rejected_minus_accepted": 1.4432024357914925
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0413899719715118,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8397647861242294,
                  "rejected_mean_error": 2.0872617479960125,
                  "gap_rejected_minus_accepted": 1.247496961871783
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9900845126625081,
              "spearman": 0.9802138755198773,
              "auroc_top30_bad": 0.9918620952380953,
              "mae": 0.12497995384219103,
              "mse": 0.027314624765951912,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8687340740425676,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09061784398555756
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21792977612018585
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5856329087853431
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0200448044220607
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9947309352836694,
              "spearman": 0.9921512377287922,
              "auroc_top30_worst": 0.9994971428571429,
              "pairwise_seed_ranking": 0.9208,
              "predicted_best_mean_error": 1.9931721103191375,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.11130889439582847,
              "gap_to_oracle": 0.004276880621910006,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6236826193332672
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8731154809968594
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2247542130947113
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5471656203968946
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.05439100265503,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.842645393451055,
                  "rejected_mean_error": 4.215174695968628,
                  "gap_rejected_minus_accepted": 2.372529302517573
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.799780547618866,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.54590265839306,
                  "rejected_mean_error": 3.6784732067546906,
                  "gap_rejected_minus_accepted": 2.1325705483616306
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7308731079101562,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2247542130947113,
                  "rejected_mean_error": 2.935042434310913,
                  "gap_rejected_minus_accepted": 1.7102882212162018
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1906661987304688,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8747004688547823,
                  "rejected_mean_error": 2.4824884288975118,
                  "gap_rejected_minus_accepted": 1.6077879600427294
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.1433030128479,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.86610019048055,
                  "rejected_mean_error": 4.249908332824707,
                  "gap_rejected_minus_accepted": 2.383808142344157
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.871477484703064,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5548569416617328,
                  "rejected_mean_error": 3.7359048109205943,
                  "gap_rejected_minus_accepted": 2.1810478692588617
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7367574572563171,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2217185592651367,
                  "rejected_mean_error": 2.987243450164795,
                  "gap_rejected_minus_accepted": 1.7655248908996584
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1673983931541443,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8727790722771297,
                  "rejected_mean_error": 2.5194394097608677,
                  "gap_rejected_minus_accepted": 1.646660337483738
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.988906386690267,
              "spearman": 0.9786416467243632,
              "auroc_top30_bad": 0.9761584761904762,
              "mae": 0.11903961029630154,
              "mse": 0.02480338996979968,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7241178281573731,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08409470093250275
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19014870414733887
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6294278402686119
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0434173145532608
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9897272333531373,
              "spearman": 0.9730778287858105,
              "auroc_top30_worst": 0.9611276190476191,
              "pairwise_seed_ranking": 0.8824,
              "predicted_best_mean_error": 1.5856268889904022,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.07151625347137447,
              "gap_to_oracle": 0.005729367494583082,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40212459802627565
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6536158686264967
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0336756499290467
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3109915638402072
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.502431201934815,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4585228163931105,
                  "rejected_mean_error": 3.3430593605041503,
                  "gap_rejected_minus_accepted": 1.8845365441110398
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9275826215744019,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3103319968205251,
                  "rejected_mean_error": 2.654758809854428,
                  "gap_rejected_minus_accepted": 1.344426813033903
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.584014654159546,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0336756499290467,
                  "rejected_mean_error": 2.2602772916793823,
                  "gap_rejected_minus_accepted": 1.2266016417503356
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0086197257041931,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6550852582096672,
                  "rejected_mean_error": 1.9783125962493513,
                  "gap_rejected_minus_accepted": 1.323227338039684
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6449723720550535,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4643141012721592,
                  "rejected_mean_error": 3.392604513168335,
                  "gap_rejected_minus_accepted": 1.9282904118961757
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.923810750246048,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3040424703276732,
                  "rejected_mean_error": 2.7052356137169733,
                  "gap_rejected_minus_accepted": 1.4011931433893001
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5989057421684265,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0242299160957336,
                  "rejected_mean_error": 2.2900563688278197,
                  "gap_rejected_minus_accepted": 1.2658264527320862
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0051721632480621,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.645200370796143,
                  "rejected_mean_error": 1.9980650387983272,
                  "gap_rejected_minus_accepted": 1.352864668002184
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9784477200592254,
              "spearman": 0.9753217362453,
              "auroc_top30_bad": 0.9802308571428571,
              "mae": 0.12811434081997722,
              "mse": 0.031292981158565485,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6616541805166504,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08659921562671662
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23690446708202362
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7849989892959595
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1388815713882445
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9636210524748465,
              "spearman": 0.9608973409902983,
              "auroc_top30_worst": 0.970870857142857,
              "pairwise_seed_ranking": 0.894,
              "predicted_best_mean_error": 1.5955226856470108,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06622844231128688,
              "gap_to_oracle": 0.0034987536668777963,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8422594339847564
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1063842705618112
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.359582267999649
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5199155010966097
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.050955605506897,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5966496727466584,
                  "rejected_mean_error": 2.228285913467407,
                  "gap_rejected_minus_accepted": 0.6316362407207488
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8694527745246887,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5195562245688037,
                  "rejected_mean_error": 2.079688302244241,
                  "gap_rejected_minus_accepted": 0.5601320776754375
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6468698382377625,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.359582267999649,
                  "rejected_mean_error": 1.9600443256378173,
                  "gap_rejected_minus_accepted": 0.6004620576381683
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2687962353229523,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.107529999444279,
                  "rejected_mean_error": 1.8443006736364538,
                  "gap_rejected_minus_accepted": 0.7367706741921747
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0513208866119386,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6042300481266445,
                  "rejected_mean_error": 2.1794408464431765,
                  "gap_rejected_minus_accepted": 0.575210798316532
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8498650193214417,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5253528946223744,
                  "rejected_mean_error": 2.066615725320483,
                  "gap_rejected_minus_accepted": 0.5412628306981084
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6764671206474304,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3699546437263488,
                  "rejected_mean_error": 1.9535476121902466,
                  "gap_rejected_minus_accepted": 0.5835929684638979
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2693182528018951,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1172547028178261,
                  "rejected_mean_error": 1.8451911000644459,
                  "gap_rejected_minus_accepted": 0.7279363972466197
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
        "best_epoch": 79,
        "best_calib_loss": 0.013475264422595501,
        "train_time_sec": 34.37143683433533,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9982103873582342,
              "spearman": 0.996141785334732,
              "auroc_top30_bad": 0.9977934523809523,
              "mae": 0.04993795074463123,
              "mse": 0.004542371531371736,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7704078604833324,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08557387343363371
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2337971052420791
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6143245249277679
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9757448101047892
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4028596238854691
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9986458082700473,
              "spearman": 0.9970362226730932,
              "auroc_top30_worst": 0.9975675238095238,
              "pairwise_seed_ranking": 0.9535,
              "predicted_best_mean_error": 1.685950813382864,
              "seed0_mean_error": 1.7753875075280667,
              "random_seed_mean_error": 1.7670326000750065,
              "oracle_best_mean_error": 1.6848166666328908,
              "improvement_over_seed0": 0.08943669414520272,
              "gap_to_oracle": 0.0011341467499732527,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6882162579298019
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8471738706588745
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0598596912860871
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2842034792900086
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7651591389894485
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0745227098465007,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4685067716439566,
                  "rejected_mean_error": 4.435030445098877,
                  "gap_rejected_minus_accepted": 2.9665236734549207
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.970459759235382,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2842034792900086,
                  "rejected_mean_error": 3.2080261180877687,
                  "gap_rejected_minus_accepted": 1.9238226387977602
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4506059885025024,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0598596912860871,
                  "rejected_mean_error": 2.47045858669281,
                  "gap_rejected_minus_accepted": 1.410598895406723
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0319771766662598,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8471738706588745,
                  "rejected_mean_error": 2.0711542284329734,
                  "gap_rejected_minus_accepted": 1.2239803577740989
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1202717304229735,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4712991357843082,
                  "rejected_mean_error": 4.512182853221893,
                  "gap_rejected_minus_accepted": 3.040883717437585
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9727935492992401,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.282547442237536,
                  "rejected_mean_error": 3.2539077033996584,
                  "gap_rejected_minus_accepted": 1.9713602611621224
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4416074752807617,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.054980587184429,
                  "rejected_mean_error": 2.495794427871704,
                  "gap_rejected_minus_accepted": 1.4408138406872748
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0240081548690796,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8401921156644822,
                  "rejected_mean_error": 2.087119304815928,
                  "gap_rejected_minus_accepted": 1.246927189151446
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9889898110120594,
              "spearman": 0.9808618321903567,
              "auroc_top30_bad": 0.9893508571428572,
              "mae": 0.13062476289849728,
              "mse": 0.02989173372413734,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8495893047712568,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09812049913406372
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20761597735881807
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5867221505761147
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.021131915195783
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9934655174480321,
              "spearman": 0.9924911363143273,
              "auroc_top30_worst": 0.9993081904761905,
              "pairwise_seed_ranking": 0.9252,
              "predicted_best_mean_error": 1.9931805325746537,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.11130047214031236,
              "gap_to_oracle": 0.004285302877426123,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6252182695865631
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8682674611799228
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2230097106456757
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5492759351727805
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.060677576065063,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8428221029440561,
                  "rejected_mean_error": 4.213584310531616,
                  "gap_rejected_minus_accepted": 2.3707622075875605
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.715634763240814,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5480602366120229,
                  "rejected_mean_error": 3.6720142585400954,
                  "gap_rejected_minus_accepted": 2.1239540219280726
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6996679306030273,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2230097106456757,
                  "rejected_mean_error": 2.936786936759949,
                  "gap_rejected_minus_accepted": 1.7137772261142732
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.15603306889534,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8700753818876066,
                  "rejected_mean_error": 2.4840334152590122,
                  "gap_rejected_minus_accepted": 1.6139580333714056
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.155138301849365,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8669701374901666,
                  "rejected_mean_error": 4.242078809738159,
                  "gap_rejected_minus_accepted": 2.375108672247993
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.78948175907135,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5548569416617328,
                  "rejected_mean_error": 3.7359048109205943,
                  "gap_rejected_minus_accepted": 2.1810478692588617
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7133550643920898,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2218784914016723,
                  "rejected_mean_error": 2.987083518028259,
                  "gap_rejected_minus_accepted": 1.7652050266265868
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.133253127336502,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8673294177131047,
                  "rejected_mean_error": 2.5212753896407265,
                  "gap_rejected_minus_accepted": 1.6539459719276217
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9808252307810468,
              "spearman": 0.9712207499554026,
              "auroc_top30_bad": 0.9652426666666667,
              "mae": 0.15575294738998638,
              "mse": 0.045852290898648014,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6941702135121739,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07477600300312043
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18909604454040527
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6293812798857689
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0543859287500381
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9793956175714709,
              "spearman": 0.974058645285533,
              "auroc_top30_worst": 0.959232,
              "pairwise_seed_ranking": 0.8872,
              "predicted_best_mean_error": 1.5868525782823562,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.07029056417942048,
              "gap_to_oracle": 0.006955056786537073,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40268908643722534
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6540395302268175
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0321283413887024
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3162948597850068
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3595828056335453,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4593762192726136,
                  "rejected_mean_error": 3.335378734588623,
                  "gap_rejected_minus_accepted": 1.8760025153160096
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9788572192192078,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3156377810551492,
                  "rejected_mean_error": 2.638875359925218,
                  "gap_rejected_minus_accepted": 1.323237578870069
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5861693620681763,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0321283413887024,
                  "rejected_mean_error": 2.2618246002197266,
                  "gap_rejected_minus_accepted": 1.2296962588310243
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0194134414196014,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6555075662585493,
                  "rejected_mean_error": 1.9781715264315285,
                  "gap_rejected_minus_accepted": 1.3226639601729793
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.473053646087646,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4645854968494838,
                  "rejected_mean_error": 3.390161952972412,
                  "gap_rejected_minus_accepted": 1.9255764561229283
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0182158946990967,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3121260216529356,
                  "rejected_mean_error": 2.681241580418178,
                  "gap_rejected_minus_accepted": 1.3691155587652424
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6006399393081665,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0237662625312804,
                  "rejected_mean_error": 2.290520022392273,
                  "gap_rejected_minus_accepted": 1.2667537598609924
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9813123345375061,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6435922592405289,
                  "rejected_mean_error": 1.9986068090015554,
                  "gap_rejected_minus_accepted": 1.3550145497610266
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9755821847858155,
              "spearman": 0.9689339570966335,
              "auroc_top30_bad": 0.9689744761904762,
              "mae": 0.1531289650686085,
              "mse": 0.039532438816904956,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6408663539624195,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08563672471046448
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22652722017765045
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7854878050804138
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1409938320159911
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9508822062109457,
              "spearman": 0.9392484331829973,
              "auroc_top30_worst": 0.9407573333333333,
              "pairwise_seed_ranking": 0.9004,
              "predicted_best_mean_error": 1.5948409844636917,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.066910143494606,
              "gap_to_oracle": 0.0028170524835586797,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8448721544742585
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1031751855252645
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3610889162540436
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5258274128251492
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9927089452743532,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6026185546716054,
                  "rejected_mean_error": 2.1745659761428833,
                  "gap_rejected_minus_accepted": 0.5719474214712779
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8204680383205414,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5255125863129708,
                  "rejected_mean_error": 2.061857276831191,
                  "gap_rejected_minus_accepted": 0.5363446905182203
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6275436282157898,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3610889162540436,
                  "rejected_mean_error": 1.9585376773834229,
                  "gap_rejected_minus_accepted": 0.5974487611293793
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2936193943023682,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1043178883794778,
                  "rejected_mean_error": 1.845373662711462,
                  "gap_rejected_minus_accepted": 0.7410557743319843
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9942739963531495,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.607220175796085,
                  "rejected_mean_error": 2.152529697418213,
                  "gap_rejected_minus_accepted": 0.545309521622128
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8118191361427307,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.531490590164368,
                  "rejected_mean_error": 2.0483974861720253,
                  "gap_rejected_minus_accepted": 0.5169068960076573
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.631771743297577,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3773026356697082,
                  "rejected_mean_error": 1.9461996202468872,
                  "gap_rejected_minus_accepted": 0.568896984577179
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2973098158836365,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.113637279896509,
                  "rejected_mean_error": 1.8464098040432853,
                  "gap_rejected_minus_accepted": 0.7327725241467762
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
        "best_epoch": 31,
        "best_calib_loss": 0.0875081941485405,
        "train_time_sec": 14.432110071182251,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9125960563132376,
              "spearman": 0.8256350272523748,
              "auroc_top30_bad": 0.8911934523809524,
              "mae": 0.20215420011287788,
              "mse": 0.1927133622215618,
              "expert_lt_perturb_large": 0.983,
              "expert_lt_other_task": 0.502,
              "expert_lt_simvla_seed0": 0.984,
              "same_context_pred_std": 0.7487518541696613,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4769709323452553
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5439056083274539
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6906734528614906
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.989370669802449
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3885712516240194
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.997881701850449,
              "spearman": 0.9935637317017769,
              "auroc_top30_worst": 0.9983889523809524,
              "pairwise_seed_ranking": 0.8171,
              "predicted_best_mean_error": 1.6926641159653664,
              "seed0_mean_error": 1.7723370801210403,
              "random_seed_mean_error": 1.7639946495592593,
              "oracle_best_mean_error": 1.6821038286685943,
              "improvement_over_seed0": 0.07967296415567393,
              "gap_to_oracle": 0.010560287296772053,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6948117091059685
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8481299739122391
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0563552320122718
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2800934979518255
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.762259884315729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.110870862007142,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4655167637997204,
                  "rejected_mean_error": 4.432947968959808,
                  "gap_rejected_minus_accepted": 2.9674312051600875
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.984189659357071,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2800934979518255,
                  "rejected_mean_error": 3.20875904340744,
                  "gap_rejected_minus_accepted": 1.9286655454556145
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4707656502723694,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0563552320122718,
                  "rejected_mean_error": 2.4681645366191862,
                  "gap_rejected_minus_accepted": 1.4118093046069145
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0462637543678284,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8481299739122391,
                  "rejected_mean_error": 2.066969854450226,
                  "gap_rejected_minus_accepted": 1.218839880537987
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.18914315700531,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4679283045397864,
                  "rejected_mean_error": 4.512016060352326,
                  "gap_rejected_minus_accepted": 3.0440877558125394
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9956721365451813,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2783457363446553,
                  "rejected_mean_error": 3.2543111114501952,
                  "gap_rejected_minus_accepted": 1.97596537510554
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4575331211090088,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0518273851871491,
                  "rejected_mean_error": 2.4928467750549315,
                  "gap_rejected_minus_accepted": 1.4410193898677823
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0468517541885376,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8405468797683716,
                  "rejected_mean_error": 2.08293381357193,
                  "gap_rejected_minus_accepted": 1.2423869338035582
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8282472358933622,
              "spearman": 0.7304818878429319,
              "auroc_top30_bad": 0.7851481904761903,
              "mae": 0.45290846963524817,
              "mse": 0.4646925227291651,
              "expert_lt_perturb_large": 0.988,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.8855710657413502,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4626672436594963
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.647588607621193
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7656620023608207
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1209083436568579
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8349523849584196,
              "spearman": 0.7524696937406041,
              "auroc_top30_worst": 0.8483779047619048,
              "pairwise_seed_ranking": 0.7276,
              "predicted_best_mean_error": 2.010477821111679,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.09400318360328708,
              "gap_to_oracle": 0.021582591414451402,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.063980507850647
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.181168684688134
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.516478274679184
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6008473800888448
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.283997058868408,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8431600298086803,
                  "rejected_mean_error": 4.21054296875,
                  "gap_rejected_minus_accepted": 2.3673829389413195
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7055220007896423,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.600258216627634,
                  "rejected_mean_error": 3.5157538519118923,
                  "gap_rejected_minus_accepted": 1.9154956352842583
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6299776434898376,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.516478274679184,
                  "rejected_mean_error": 2.64331837272644,
                  "gap_rejected_minus_accepted": 1.1268400980472562
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1881040036678314,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1835551971254257,
                  "rejected_mean_error": 2.3793171055797835,
                  "gap_rejected_minus_accepted": 1.1957619084543578
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.2927632331848145,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8661083624098036,
                  "rejected_mean_error": 4.249834785461426,
                  "gap_rejected_minus_accepted": 2.383726423051622
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7668159008026123,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.614295369163554,
                  "rejected_mean_error": 3.5594764626215376,
                  "gap_rejected_minus_accepted": 1.9451810934579836
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6618273854255676,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.532593461036682,
                  "rejected_mean_error": 2.6763685483932496,
                  "gap_rejected_minus_accepted": 1.1437750873565675
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2127615809440613,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1523364451196458,
                  "rejected_mean_error": 2.425256979337988,
                  "gap_rejected_minus_accepted": 1.2729205342183423
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6563023971198647,
              "spearman": 0.5447628346687794,
              "auroc_top30_bad": 0.6467070476190476,
              "mae": 0.5235970257997513,
              "mse": 0.6303396921602528,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.6172351912938278,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7495096800923348
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7485638579368591
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9005426282525063
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1293729121128717
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8634824062396524,
              "spearman": 0.7853205338371417,
              "auroc_top30_worst": 0.8393142857142857,
              "pairwise_seed_ranking": 0.7592,
              "predicted_best_mean_error": 1.602013559103012,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.05512958335876461,
              "gap_to_oracle": 0.02211603760719294,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.41558216214179994
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8225809616538194
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1410051060676574
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3551722832961377
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.159543323516847,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4809971214400397,
                  "rejected_mean_error": 3.1407906150817873,
                  "gap_rejected_minus_accepted": 1.6597934936417476
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7519371807575226,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3544439902427738,
                  "rejected_mean_error": 2.522704695360348,
                  "gap_rejected_minus_accepted": 1.1682607051175742
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.42890864610672,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1410051060676574,
                  "rejected_mean_error": 2.1529478355407714,
                  "gap_rejected_minus_accepted": 1.011942729473114
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9388473331928253,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8227524391759318,
                  "rejected_mean_error": 1.922304242308646,
                  "gap_rejected_minus_accepted": 1.0995518031327143
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.20324866771698,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.486114161544376,
                  "rejected_mean_error": 3.196403970718384,
                  "gap_rejected_minus_accepted": 1.710289809174008
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7710492014884949,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3491075532959107,
                  "rejected_mean_error": 2.571471002366808,
                  "gap_rejected_minus_accepted": 1.2223634490708972
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4457895159721375,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.123989001750946,
                  "rejected_mean_error": 2.1902972831726073,
                  "gap_rejected_minus_accepted": 1.0663082814216613
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9154312014579773,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8259914895844838,
                  "rejected_mean_error": 1.937156800917763,
                  "gap_rejected_minus_accepted": 1.1111653113332793
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5177598726842166,
              "spearman": 0.4053003280930327,
              "auroc_top30_bad": 0.5766822857142857,
              "mae": 0.4712763991057873,
              "mse": 0.6020996420257421,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.988,
              "same_context_pred_std": 0.5895020121817536,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9333120946884155
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0846539572238922
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.030789476299286
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.25394891649882
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7038113905298632,
              "spearman": 0.5849852463265577,
              "auroc_top30_worst": 0.7006506666666666,
              "pairwise_seed_ranking": 0.7196,
              "predicted_best_mean_error": 1.616472379207611,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.045278748750686715,
              "gap_to_oracle": 0.024448447227477965,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8787051627635956
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2717278776451564
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4753234596729279
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5782949623586273
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8958965778350831,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6229259605672623,
                  "rejected_mean_error": 1.9917993230819702,
                  "gap_rejected_minus_accepted": 0.3688733625147078
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7596872746944427,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5781677272111145,
                  "rejected_mean_error": 1.904228308711189,
                  "gap_rejected_minus_accepted": 0.32606058150007455
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.507366120815277,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4753234596729279,
                  "rejected_mean_error": 1.8443031339645386,
                  "gap_rejected_minus_accepted": 0.3689796742916107
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.318953961133957,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2726149308605317,
                  "rejected_mean_error": 1.7891549067919639,
                  "gap_rejected_minus_accepted": 0.5165399759314322
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8853841304779053,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.630075098938412,
                  "rejected_mean_error": 1.946835389137268,
                  "gap_rejected_minus_accepted": 0.316760290198856
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.741341769695282,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5759626955272041,
                  "rejected_mean_error": 1.9163929829521784,
                  "gap_rejected_minus_accepted": 0.3404302874249743
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5110555291175842,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4753175387382507,
                  "rejected_mean_error": 1.8481847171783448,
                  "gap_rejected_minus_accepted": 0.3728671784400941
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3327340483665466,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2706859651066007,
                  "rejected_mean_error": 1.793500353945768,
                  "gap_rejected_minus_accepted": 0.5228143888391672
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
        "best_epoch": 79,
        "best_calib_loss": 0.012172790244221687,
        "train_time_sec": 36.81398892402649,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997289716559382,
              "spearman": 0.9992173921150196,
              "auroc_top30_bad": 0.9997284761904761,
              "mae": 0.01895501625171164,
              "mse": 0.0006018905137354619,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7788463682098609,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07604214892478194
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22623296985304914
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.598207080660644
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.958916639414352
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3885712516240194
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997140791702106,
              "spearman": 0.9992343999693024,
              "auroc_top30_worst": 0.9997777142857143,
              "pairwise_seed_ranking": 0.9531,
              "predicted_best_mean_error": 1.683561887025833,
              "seed0_mean_error": 1.7723370801210403,
              "random_seed_mean_error": 1.7639946495592593,
              "oracle_best_mean_error": 1.6821038286685943,
              "improvement_over_seed0": 0.0887751930952072,
              "gap_to_oracle": 0.0014580583572387784,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6818332069516182
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8413932688951492
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0538209319233893
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2794333547035852
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.762259884315729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1267756462097176,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4652563220726118,
                  "rejected_mean_error": 4.435291944503784,
                  "gap_rejected_minus_accepted": 2.970035622431172
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0019586086273193,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2794333547035852,
                  "rejected_mean_error": 3.210739473152161,
                  "gap_rejected_minus_accepted": 1.9313061184485756
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4784877300262451,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0538209319233893,
                  "rejected_mean_error": 2.4706988367080687,
                  "gap_rejected_minus_accepted": 1.4168779047846793
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.050101399421692,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8413932688951492,
                  "rejected_mean_error": 2.069215422789256,
                  "gap_rejected_minus_accepted": 1.2278221538941065
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.188741207122803,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4677789186106789,
                  "rejected_mean_error": 4.513360533714295,
                  "gap_rejected_minus_accepted": 3.0455816151036155
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0104820132255554,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.277733244895935,
                  "rejected_mean_error": 3.2561485857963564,
                  "gap_rejected_minus_accepted": 1.9784153409004213
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4763280749320984,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.049143423318863,
                  "rejected_mean_error": 2.4955307369232176,
                  "gap_rejected_minus_accepted": 1.4463873136043546
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0543864369392395,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8338631105422973,
                  "rejected_mean_error": 2.085161736647288,
                  "gap_rejected_minus_accepted": 1.2512986261049905
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9901199009903923,
              "spearman": 0.9841853567646471,
              "auroc_top30_bad": 0.9883420952380954,
              "mae": 0.12185438432879746,
              "mse": 0.02641295489981868,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8957987304731659,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07942440736293793
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20082194921970367
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5854755823731422
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0207044774770737
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9905682916209391,
              "spearman": 0.9910024195855486,
              "auroc_top30_worst": 0.9975740952380953,
              "pairwise_seed_ranking": 0.9024,
              "predicted_best_mean_error": 1.9955343461036683,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10894665861129771,
              "gap_to_oracle": 0.00663911640644077,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6228060553073883
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8646255581615827
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2321154256343843
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5541429812910714
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.175384950637818,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8417880230744679,
                  "rejected_mean_error": 4.2228910293579105,
                  "gap_rejected_minus_accepted": 2.3811030062834426
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8439295887947083,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.552419406341005,
                  "rejected_mean_error": 3.6589646034728225,
                  "gap_rejected_minus_accepted": 2.106545197131817
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.837771475315094,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2321154256343843,
                  "rejected_mean_error": 2.9276812217712402,
                  "gap_rejected_minus_accepted": 1.695565796136856
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2470893561840057,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8658902267107187,
                  "rejected_mean_error": 2.4854314446830954,
                  "gap_rejected_minus_accepted": 1.6195412179723767
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.214377403259277,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8652322154574925,
                  "rejected_mean_error": 4.257720108032227,
                  "gap_rejected_minus_accepted": 2.392487892574734
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.884970963001251,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.559777347799291,
                  "rejected_mean_error": 3.721299795877366,
                  "gap_rejected_minus_accepted": 2.161522448078075
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8502811193466187,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2309111375808717,
                  "rejected_mean_error": 2.97805087184906,
                  "gap_rejected_minus_accepted": 1.7471397342681885
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2514486908912659,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.862266358875093,
                  "rejected_mean_error": 2.5229811260406985,
                  "gap_rejected_minus_accepted": 1.6607147671656055
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9873269162874074,
              "spearman": 0.9834555892396422,
              "auroc_top30_bad": 0.9837737142857143,
              "mae": 0.10564175688177348,
              "mse": 0.023122481732699793,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7433673101411753,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05312532156705856
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19140483493804933
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6298827653288841
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0422981135924658
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9905302535036076,
              "spearman": 0.9908028561938281,
              "auroc_top30_worst": 0.9850971428571429,
              "pairwise_seed_ranking": 0.8772,
              "predicted_best_mean_error": 1.5902010937929154,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06694204866886122,
              "gap_to_oracle": 0.01030357229709633,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4248670692443848
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6531649539485956
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0246495059013367
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3051847606452542
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.742920541763306,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4593885392612882,
                  "rejected_mean_error": 3.3352678546905516,
                  "gap_rejected_minus_accepted": 1.8758793154292634
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.076212465763092,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.304534869934477,
                  "rejected_mean_error": 2.672113148168253,
                  "gap_rejected_minus_accepted": 1.3675782782337762
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7129740715026855,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0246495059013367,
                  "rejected_mean_error": 2.2693034357070925,
                  "gap_rejected_minus_accepted": 1.2446539298057557
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0609452724456787,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6544368070916246,
                  "rejected_mean_error": 1.9785292079888896,
                  "gap_rejected_minus_accepted": 1.324092400897265
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.830615448951721,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4644762629932828,
                  "rejected_mean_error": 3.3911450576782225,
                  "gap_rejected_minus_accepted": 1.9266687946849397
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0825714468955994,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.301194495377056,
                  "rejected_mean_error": 2.71368912666563,
                  "gap_rejected_minus_accepted": 1.412494631288574
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7325642108917236,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0155631775856018,
                  "rejected_mean_error": 2.2987231073379517,
                  "gap_rejected_minus_accepted": 1.28315992975235
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0631714463233948,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6435922592405289,
                  "rejected_mean_error": 1.9986068090015554,
                  "gap_rejected_minus_accepted": 1.3550145497610266
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9821402140452189,
              "spearman": 0.9656492628282919,
              "auroc_top30_bad": 0.9608586666666666,
              "mae": 0.1122006225347519,
              "mse": 0.024391215651411724,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6959493606295818,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06736994087696076
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2228721697807312
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7895721297264099
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.140919388071696
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9478025164115091,
              "spearman": 0.916733810645639,
              "auroc_top30_worst": 0.9215055238095238,
              "pairwise_seed_ranking": 0.8984,
              "predicted_best_mean_error": 1.5962637206315995,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06548740732669822,
              "gap_to_oracle": 0.0042397886514664584,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8426949570178985
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1054194822716408
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3719136114597321
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5258742446647777
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.04060537815094,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.602177262014813,
                  "rejected_mean_error": 2.178537610054016,
                  "gap_rejected_minus_accepted": 0.5763603480392032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.889756828546524,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5254790065700752,
                  "rejected_mean_error": 2.0619578014928313,
                  "gap_rejected_minus_accepted": 0.5364787949227561
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7274583578109741,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3719136114597321,
                  "rejected_mean_error": 1.9477129821777344,
                  "gap_rejected_minus_accepted": 0.5757993707180022
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4344109296798706,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1070336454783003,
                  "rejected_mean_error": 1.8444664781096143,
                  "gap_rejected_minus_accepted": 0.737432832631314
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0752987623214723,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6030463067690532,
                  "rejected_mean_error": 2.190094518661499,
                  "gap_rejected_minus_accepted": 0.5870482118924456
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.882496953010559,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5351739927409167,
                  "rejected_mean_error": 2.037464211857508,
                  "gap_rejected_minus_accepted": 0.5022902191165912
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7359861731529236,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3826291394233703,
                  "rejected_mean_error": 1.9408731164932251,
                  "gap_rejected_minus_accepted": 0.5582439770698548
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4468444287776947,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1170454167184376,
                  "rejected_mean_error": 1.8452616082155768,
                  "gap_rejected_minus_accepted": 0.7282161914971392
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
        "best_epoch": 64,
        "best_calib_loss": 0.01480831578373909,
        "train_time_sec": 48.77369165420532,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993935613548265,
              "spearman": 0.998324076769511,
              "auroc_top30_bad": 0.9991358095238094,
              "mae": 0.03210545671327272,
              "mse": 0.0016395964902076456,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.993,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7863460661816734,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07727024501503911
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2264722045866307
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5983859011276392
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9592818430333554
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3885712516240194
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999469179451887,
              "spearman": 0.9985611199983412,
              "auroc_top30_worst": 0.999104380952381,
              "pairwise_seed_ranking": 0.9543,
              "predicted_best_mean_error": 1.6840438524484633,
              "seed0_mean_error": 1.7723370801210403,
              "random_seed_mean_error": 1.7639946495592593,
              "oracle_best_mean_error": 1.6821038286685943,
              "improvement_over_seed0": 0.08829322767257697,
              "gap_to_oracle": 0.0019400237798690156,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6833110496401786
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8419047695875168
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0541245671868325
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2798159047842026
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.762259884315729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.176302027702332,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.465247469537788,
                  "rejected_mean_error": 4.4353716173172,
                  "gap_rejected_minus_accepted": 2.970124147779412
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0234607458114624,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2798159047842026,
                  "rejected_mean_error": 3.209591822910309,
                  "gap_rejected_minus_accepted": 1.9297759181261063
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5101783871650696,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0541245671868325,
                  "rejected_mean_error": 2.4703952014446258,
                  "gap_rejected_minus_accepted": 1.4162706342577933
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0827488601207733,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8419047695875168,
                  "rejected_mean_error": 2.0690449225584664,
                  "gap_rejected_minus_accepted": 1.2271401529709496
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2359241008758546,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.467797689570321,
                  "rejected_mean_error": 4.513191595077514,
                  "gap_rejected_minus_accepted": 3.0453939055071935
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0410444140434265,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2776306465466818,
                  "rejected_mean_error": 3.2564563808441163,
                  "gap_rejected_minus_accepted": 1.9788257342974345
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5078261494636536,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0494228253364564,
                  "rejected_mean_error": 2.4952513349056242,
                  "gap_rejected_minus_accepted": 1.4458285095691679
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.075438231229782,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8335129313468933,
                  "rejected_mean_error": 2.085278463045756,
                  "gap_rejected_minus_accepted": 1.251765531698863
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9880623156350522,
              "spearman": 0.9791560145833035,
              "auroc_top30_bad": 0.9928434285714285,
              "mae": 0.13789486425742506,
              "mse": 0.03335443476949891,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8881142551629614,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09279167336225509
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2184206189393997
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5864560100197792
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0200495961268743
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9941288459671465,
              "spearman": 0.9931181810676359,
              "auroc_top30_worst": 0.9994544761904762,
              "pairwise_seed_ranking": 0.9036,
              "predicted_best_mean_error": 1.997453846693039,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10702715802192708,
              "gap_to_oracle": 0.008558616995811397,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6324608891010285
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8704078586246723
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2223831737041473
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.549057012014806
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.2229673862457275,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8428074530230627,
                  "rejected_mean_error": 4.213716159820557,
                  "gap_rejected_minus_accepted": 2.370908706797494
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8200615644454956,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5471452833048944,
                  "rejected_mean_error": 3.6747532721144704,
                  "gap_rejected_minus_accepted": 2.127607988809576
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7320225834846497,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2223831737041473,
                  "rejected_mean_error": 2.937413473701477,
                  "gap_rejected_minus_accepted": 1.7150302999973297
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1652097404003143,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8717094944498409,
                  "rejected_mean_error": 2.483487548415918,
                  "gap_rejected_minus_accepted": 1.6117780539660769
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.311968851089477,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.86610019048055,
                  "rejected_mean_error": 4.249908332824707,
                  "gap_rejected_minus_accepted": 2.383808142344157
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.895054519176483,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5548569416617328,
                  "rejected_mean_error": 3.7359048109205943,
                  "gap_rejected_minus_accepted": 2.1810478692588617
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.731531023979187,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.220812487602234,
                  "rejected_mean_error": 2.988149521827698,
                  "gap_rejected_minus_accepted": 1.767337034225464
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1628646552562714,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8698922528160943,
                  "rejected_mean_error": 2.5204119746060294,
                  "gap_rejected_minus_accepted": 1.650519721789935
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9841150824130247,
              "spearman": 0.9750304240443408,
              "auroc_top30_bad": 0.9728609523809524,
              "mae": 0.1347486120928079,
              "mse": 0.03342068448767795,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7120748433274328,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09407084643840789
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.195234526348114
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6291804485678673
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0451911822875342
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9881844362720293,
              "spearman": 0.9773777713777739,
              "auroc_top30_worst": 0.9666620952380952,
              "pairwise_seed_ranking": 0.878,
              "predicted_best_mean_error": 1.586780084133148,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.07036305832862855,
              "gap_to_oracle": 0.006882562637329004,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40338980197906493
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6543556228280067
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0287194806098938
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3122162139619082
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.540202307701112,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4594166283607484,
                  "rejected_mean_error": 3.33501505279541,
                  "gap_rejected_minus_accepted": 1.8755984244346617
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9147365093231201,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3115770596068594,
                  "rejected_mean_error": 2.6510315771681814,
                  "gap_rejected_minus_accepted": 1.339454517561322
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6226434111595154,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0287194806098938,
                  "rejected_mean_error": 2.265233460998535,
                  "gap_rejected_minus_accepted": 1.2365139803886414
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0278660655021667,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6553996631893487,
                  "rejected_mean_error": 1.9782075708932785,
                  "gap_rejected_minus_accepted": 1.3228079077039299
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.687488770484924,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4643141012721592,
                  "rejected_mean_error": 3.392604513168335,
                  "gap_rejected_minus_accepted": 1.9282904118961757
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9053919315338135,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.306731986808267,
                  "rejected_mean_error": 2.6972524457507663,
                  "gap_rejected_minus_accepted": 1.3905204589424993
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.640829861164093,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0186877579689027,
                  "rejected_mean_error": 2.295598526954651,
                  "gap_rejected_minus_accepted": 1.2769107689857484
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0345003604888916,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6431051417002602,
                  "rejected_mean_error": 1.9987709181194,
                  "gap_rejected_minus_accepted": 1.3556657764191398
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9749642752119339,
              "spearman": 0.9695949659288225,
              "auroc_top30_bad": 0.9746620952380952,
              "mae": 0.13148649975955487,
              "mse": 0.03526997251648153,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6652284158419481,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09829192578792573
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24511728508472444
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7875208188056946
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1415796930948894
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9546870805594216,
              "spearman": 0.9495421280909621,
              "auroc_top30_worst": 0.9537432380952381,
              "pairwise_seed_ranking": 0.8956,
              "predicted_best_mean_error": 1.5981294924020768,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06362163555622091,
              "gap_to_oracle": 0.006105560421943768,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8443684885501862
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1025183476889744
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3618265432834624
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.522716147590802
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.041643261909485,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6004133204619089,
                  "rejected_mean_error": 2.1944130840301512,
                  "gap_rejected_minus_accepted": 0.5939997635682424
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.862876147031784,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.522336520437497,
                  "rejected_mean_error": 2.0713651801069703,
                  "gap_rejected_minus_accepted": 0.5490286596694733
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.681174635887146,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3618265432834624,
                  "rejected_mean_error": 1.9578000503540038,
                  "gap_rejected_minus_accepted": 0.5959735070705414
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2911526262760162,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.103626218561928,
                  "rejected_mean_error": 1.8456047114338665,
                  "gap_rejected_minus_accepted": 0.7419784928719384
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0540504693984984,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6060923186937968,
                  "rejected_mean_error": 2.162680411338806,
                  "gap_rejected_minus_accepted": 0.5565880926450093
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8617965877056122,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.528376615302448,
                  "rejected_mean_error": 2.057640554412963,
                  "gap_rejected_minus_accepted": 0.5292639391105147
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.702025830745697,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3762391991615295,
                  "rejected_mean_error": 1.947263056755066,
                  "gap_rejected_minus_accepted": 0.5710238575935365
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2810510396957397,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1101071238517761,
                  "rejected_mean_error": 1.847599107951404,
                  "gap_rejected_minus_accepted": 0.7374919840996279
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
        "best_epoch": 57,
        "best_calib_loss": 0.013440089300274849,
        "train_time_sec": 30.609773874282837,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9992169582822771,
              "spearman": 0.998009264544269,
              "auroc_top30_bad": 0.9993058571428571,
              "mae": 0.04005413977584103,
              "mse": 0.002754346714846513,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8065084915674556,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07887183093221392
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22631461791670882
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5982396994217066
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9592341795990088
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3885712516240194
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9994237285764354,
              "spearman": 0.9989697844547418,
              "auroc_top30_worst": 0.9996586666666667,
              "pairwise_seed_ranking": 0.9486,
              "predicted_best_mean_error": 1.683526400655508,
              "seed0_mean_error": 1.7723370801210403,
              "random_seed_mean_error": 1.7639946495592593,
              "oracle_best_mean_error": 1.6821038286685943,
              "improvement_over_seed0": 0.08881067946553234,
              "gap_to_oracle": 0.0014225719869136455,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6813368226885795
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8417694567918778
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0539661549210548
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2795280134916305
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.762259884315729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.199731469154359,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4652960250708793,
                  "rejected_mean_error": 4.434934617519379,
                  "gap_rejected_minus_accepted": 2.9696385924485
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0732643604278564,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2795280134916305,
                  "rejected_mean_error": 3.210455496788025,
                  "gap_rejected_minus_accepted": 1.9309274832963945
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5297881364822388,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0539661549210548,
                  "rejected_mean_error": 2.4705536137104036,
                  "gap_rejected_minus_accepted": 1.4165874587893488
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0812693536281586,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8417694567918778,
                  "rejected_mean_error": 2.06909002682368,
                  "gap_rejected_minus_accepted": 1.227320570031802
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.284671640396119,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4677789186106789,
                  "rejected_mean_error": 4.513360533714295,
                  "gap_rejected_minus_accepted": 3.0455816151036155
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0818724036216736,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.277872399330139,
                  "rejected_mean_error": 3.255731122493744,
                  "gap_rejected_minus_accepted": 1.977858723163605
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5279196500778198,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0496481075286865,
                  "rejected_mean_error": 2.4950260527133943,
                  "gap_rejected_minus_accepted": 1.4453779451847077
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0762723088264465,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8341677892208099,
                  "rejected_mean_error": 2.085060177087784,
                  "gap_rejected_minus_accepted": 1.250892387866974
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9892650199402776,
              "spearman": 0.980720948525356,
              "auroc_top30_bad": 0.9904982857142857,
              "mae": 0.12705922017917037,
              "mse": 0.030339081584699876,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8918662123612557,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08878017246723174
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20936002230644227
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5876591537117958
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0200784406423569
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9936812691974243,
              "spearman": 0.992041935898839,
              "auroc_top30_worst": 0.9993782857142858,
              "pairwise_seed_ranking": 0.9056,
              "predicted_best_mean_error": 1.9969692338705063,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10751177084445973,
              "gap_to_oracle": 0.008074004173278748,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.637303808927536
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8727760161153781
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2231091479778289
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.549024989196995
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.119937944412232,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8418476158512964,
                  "rejected_mean_error": 4.222354694366455,
                  "gap_rejected_minus_accepted": 2.3805070785151585
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8163867592811584,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.547764011578219,
                  "rejected_mean_error": 3.6729010408297897,
                  "gap_rejected_minus_accepted": 2.1251370292515706
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7594439387321472,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2231091479778289,
                  "rejected_mean_error": 2.9366874994277956,
                  "gap_rejected_minus_accepted": 1.7135783514499667
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1996057629585266,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8743201139064642,
                  "rejected_mean_error": 2.4826154844992443,
                  "gap_rejected_minus_accepted": 1.60829537059278
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.246683025360108,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.865689720577664,
                  "rejected_mean_error": 4.253602561950683,
                  "gap_rejected_minus_accepted": 2.3879128413730193
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8865222930908203,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5548569416617328,
                  "rejected_mean_error": 3.7359048109205943,
                  "gap_rejected_minus_accepted": 2.1810478692588617
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7802228331565857,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2207133016586305,
                  "rejected_mean_error": 2.988248707771301,
                  "gap_rejected_minus_accepted": 1.7675354061126707
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1967273354530334,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8698922528160943,
                  "rejected_mean_error": 2.5204119746060294,
                  "gap_rejected_minus_accepted": 1.650519721789935
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.978941571886397,
              "spearman": 0.9642757297851355,
              "auroc_top30_bad": 0.9541310476190477,
              "mae": 0.14451315331179648,
              "mse": 0.038210890367068984,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7218133322432922,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06382163619995117
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20376450476646424
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.635658442056179
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0519296701669694
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9802171811161072,
              "spearman": 0.9640631557524197,
              "auroc_top30_worst": 0.9494430476190476,
              "pairwise_seed_ranking": 0.8764,
              "predicted_best_mean_error": 1.5881213634014129,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06902177906036377,
              "gap_to_oracle": 0.008223841905593776,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4211822400093079
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6555082859137119
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0374756142616273
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3159169683705514
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.518552732467652,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.458843678633372,
                  "rejected_mean_error": 3.340171600341797,
                  "gap_rejected_minus_accepted": 1.8813279217084249
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0774953961372375,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3152711427707937,
                  "rejected_mean_error": 2.6399729320416436,
                  "gap_rejected_minus_accepted": 1.32470178927085
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6531159281730652,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0374756142616273,
                  "rejected_mean_error": 2.256477327346802,
                  "gap_rejected_minus_accepted": 1.2190017130851747
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.054239422082901,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6567835278404407,
                  "rejected_mean_error": 1.9777452980695946,
                  "gap_rejected_minus_accepted": 1.3209617702291538
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6566473484039306,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4641851909955343,
                  "rejected_mean_error": 3.393764705657959,
                  "gap_rejected_minus_accepted": 1.9295795146624248
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.130743443965912,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3088849881753564,
                  "rejected_mean_error": 2.6908617908992465,
                  "gap_rejected_minus_accepted": 1.3819768027238901
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6642674207687378,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0319541172981261,
                  "rejected_mean_error": 2.282332167625427,
                  "gap_rejected_minus_accepted": 1.250378050327301
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0533441305160522,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6439674600722298,
                  "rejected_mean_error": 1.9984804044432818,
                  "gap_rejected_minus_accepted": 1.354512944371052
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9748134613727861,
              "spearman": 0.9679521289495933,
              "auroc_top30_bad": 0.9703900952380953,
              "mae": 0.12816481027361007,
              "mse": 0.03327241408718386,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6815036108181916,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08300230062007904
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2407644963979721
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7862925933837891
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1423318557103475
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.958954176657642,
              "spearman": 0.9529657636900888,
              "auroc_top30_worst": 0.9556632380952381,
              "pairwise_seed_ranking": 0.8868,
              "predicted_best_mean_error": 1.5958240867853164,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06592704117298132,
              "gap_to_oracle": 0.0038001548051833645,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8449016697406769
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1023744750672426
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3597598520755767
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5227148117604794
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1573664903640752,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5961665986643898,
                  "rejected_mean_error": 2.2326335802078248,
                  "gap_rejected_minus_accepted": 0.636466981543435
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.98875293135643,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5223050106360538,
                  "rejected_mean_error": 2.071459508170716,
                  "gap_rejected_minus_accepted": 0.5491544975346623
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7348660230636597,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3597598520755767,
                  "rejected_mean_error": 1.9598667415618896,
                  "gap_rejected_minus_accepted": 0.6001068894863129
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3717684149742126,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1035272851348303,
                  "rejected_mean_error": 1.8456377596331,
                  "gap_rejected_minus_accepted": 0.7421104744982696
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.174001455307007,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.601563617653317,
                  "rejected_mean_error": 2.203438720703125,
                  "gap_rejected_minus_accepted": 0.601875103049808
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9889902472496033,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.528846023235729,
                  "rejected_mean_error": 2.0562472324522716,
                  "gap_rejected_minus_accepted": 0.5274012092165425
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7471030950546265,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3748674511909484,
                  "rejected_mean_error": 1.948634804725647,
                  "gap_rejected_minus_accepted": 0.5737673535346985
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3906776010990143,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1130212327790638,
                  "rejected_mean_error": 1.8466173493288418,
                  "gap_rejected_minus_accepted": 0.733596116549778
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
        "best_epoch": 63,
        "best_calib_loss": 0.0893251821398735,
        "train_time_sec": 14.143645286560059,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9271270434693726,
              "spearman": 0.8473570812393802,
              "auroc_top30_bad": 0.9064475714285715,
              "mae": 0.18397707764214138,
              "mse": 0.1704205633863133,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.51,
              "expert_lt_simvla_seed0": 0.987,
              "same_context_pred_std": 0.7801464423554413,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46412708278314674
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.48825167410722936
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6518322053077398
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9452137679486691
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3561629488177016
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9983320103388982,
              "spearman": 0.9956886303472348,
              "auroc_top30_worst": 0.9983580952380953,
              "pairwise_seed_ranking": 0.8539,
              "predicted_best_mean_error": 1.6887170102000237,
              "seed0_mean_error": 1.7700846727788448,
              "random_seed_mean_error": 1.7617888971567155,
              "oracle_best_mean_error": 1.6800175212025643,
              "improvement_over_seed0": 0.08136766257882111,
              "gap_to_oracle": 0.008699488997459426,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6837456597685814
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8393059880018234
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0522375711798668
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.278071888724963
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7601412408292294
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.132539296150208,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4629496871034304,
                  "rejected_mean_error": 4.4348652243614195,
                  "gap_rejected_minus_accepted": 2.9719155372579893
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.988926500082016,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.278071888724963,
                  "rejected_mean_error": 3.2063492971420287,
                  "gap_rejected_minus_accepted": 1.9282774084170657
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4459299445152283,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0522375711798668,
                  "rejected_mean_error": 2.468044910478592,
                  "gap_rejected_minus_accepted": 1.4158073392987252
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.001179724931717,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8393059880018234,
                  "rejected_mean_error": 2.0670863251050315,
                  "gap_rejected_minus_accepted": 1.227780337103208
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2210633516311646,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4652698549628258,
                  "rejected_mean_error": 4.513418033123016,
                  "gap_rejected_minus_accepted": 3.04814817816019
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9977003931999207,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2762336239417393,
                  "rejected_mean_error": 3.251637819290161,
                  "gap_rejected_minus_accepted": 1.9754041953484218
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4430750012397766,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0470739793181418,
                  "rejected_mean_error": 2.493095366239548,
                  "gap_rejected_minus_accepted": 1.446021386921406
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9877498745918274,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8290666052103043,
                  "rejected_mean_error": 2.0837573619683583,
                  "gap_rejected_minus_accepted": 1.254690756758054
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8253041778938599,
              "spearman": 0.7207107534206304,
              "auroc_top30_bad": 0.7759771428571429,
              "mae": 0.4549674541056156,
              "mse": 0.4967068456421304,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.952,
              "same_context_pred_std": 0.9139485108136894,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5437654227018356
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6949980543375015
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.769589085817337
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1163271336634955
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8336622909530588,
              "spearman": 0.7578751822561168,
              "auroc_top30_worst": 0.8486278095238096,
              "pairwise_seed_ranking": 0.7732,
              "predicted_best_mean_error": 2.005266383290291,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.09921462142467519,
              "gap_to_oracle": 0.016371153593063292,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1503237316608428
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2135117271771798
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4844661587238313
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6006469895272875
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.327433824539185,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8425796183215248,
                  "rejected_mean_error": 4.215766672134399,
                  "gap_rejected_minus_accepted": 2.3731870538128743
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.68816214799881,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6002705402219053,
                  "rejected_mean_error": 3.515716959874089,
                  "gap_rejected_minus_accepted": 1.9154464196521837
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6843637824058533,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4844661587238313,
                  "rejected_mean_error": 2.675330488681793,
                  "gap_rejected_minus_accepted": 1.1908643299579618
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1039529740810394,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2135830744386862,
                  "rejected_mean_error": 2.369286448590402,
                  "gap_rejected_minus_accepted": 1.1557033741517158
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.342549896240234,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8656700144873726,
                  "rejected_mean_error": 4.253779916763306,
                  "gap_rejected_minus_accepted": 2.388109902275933
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.736067771911621,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6131996050237971,
                  "rejected_mean_error": 3.562728968877641,
                  "gap_rejected_minus_accepted": 1.949529363853844
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6927683353424072,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4923965559005736,
                  "rejected_mean_error": 2.7165654535293577,
                  "gap_rejected_minus_accepted": 1.2241688976287841
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0802336037158966,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1376865799464877,
                  "rejected_mean_error": 2.4301924954123675,
                  "gap_rejected_minus_accepted": 1.2925059154658798
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6369595097846218,
              "spearman": 0.4870106401198879,
              "auroc_top30_bad": 0.6101432380952381,
              "mae": 0.5312991592526436,
              "mse": 0.7168088762557119,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.528,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.6635404421829695,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9276174245476723
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9890886557102203
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9244544521450997
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1346382541418076
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8825058961512768,
              "spearman": 0.793415695242045,
              "auroc_top30_worst": 0.8313325714285714,
              "pairwise_seed_ranking": 0.7864,
              "predicted_best_mean_error": 1.6013711878061294,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.055771954655647216,
              "gap_to_oracle": 0.021473666310310335,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4178144426345825
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8143803442899997
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.111772651386261
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3666793874967327
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.065123414993286,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4732334903611077,
                  "rejected_mean_error": 3.2106632947921754,
                  "gap_rejected_minus_accepted": 1.7374298044310676
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7028805613517761,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3654971228974098,
                  "rejected_mean_error": 2.489615924442157,
                  "gap_rejected_minus_accepted": 1.1241188015447474
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3805768489837646,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.111772651386261,
                  "rejected_mean_error": 2.182180290222168,
                  "gap_rejected_minus_accepted": 1.070407638835907
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9092473834753036,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8193546815421253,
                  "rejected_mean_error": 1.9234392456591065,
                  "gap_rejected_minus_accepted": 1.1040845641169812
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1210785150527953,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4786316874292162,
                  "rejected_mean_error": 3.263746237754822,
                  "gap_rejected_minus_accepted": 1.7851145503256056
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7625521123409271,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3548514234190956,
                  "rejected_mean_error": 2.5544217370805287,
                  "gap_rejected_minus_accepted": 1.199570313661433
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3856412172317505,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0855770354270935,
                  "rejected_mean_error": 2.2287092494964598,
                  "gap_rejected_minus_accepted": 1.1431322140693663
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9067384004592896,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7986455834101117,
                  "rejected_mean_error": 1.9463695928374714,
                  "gap_rejected_minus_accepted": 1.1477240094273595
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5165917916980786,
              "spearman": 0.39850688376365706,
              "auroc_top30_bad": 0.5896453333333334,
              "mae": 0.4780342748939991,
              "mse": 0.6572169599947809,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.6374340157258939,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0959326864480972
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0881833607912064
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.032488940501213
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.263668766283989
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7451836966065477,
              "spearman": 0.6515329374290801,
              "auroc_top30_worst": 0.7577721904761905,
              "pairwise_seed_ranking": 0.75,
              "predicted_best_mean_error": 1.6098551222085953,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.051896005749702434,
              "gap_to_oracle": 0.017831190228462246,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8741252501010894
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.230496093726311
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4668182470798492
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5694624198588736
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.931375014781952,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.617196239815818,
                  "rejected_mean_error": 2.043366809844971,
                  "gap_rejected_minus_accepted": 0.42617057002915293
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7738915085792542,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5692791559971002,
                  "rejected_mean_error": 1.9308372263710338,
                  "gap_rejected_minus_accepted": 0.3615580703739336
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4974303245544434,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4668182470798492,
                  "rejected_mean_error": 1.8528083465576173,
                  "gap_rejected_minus_accepted": 0.3859900994777681
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.237717092037201,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2319973597701745,
                  "rejected_mean_error": 1.802722996174335,
                  "gap_rejected_minus_accepted": 0.5707256364041604
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9309006214141846,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6183905307451885,
                  "rejected_mean_error": 2.051996502876282,
                  "gap_rejected_minus_accepted": 0.4336059721310934
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7868236601352692,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.570905618170366,
                  "rejected_mean_error": 1.931403672884381,
                  "gap_rejected_minus_accepted": 0.3604980547140151
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5146753191947937,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4538818469047547,
                  "rejected_mean_error": 1.869620409011841,
                  "gap_rejected_minus_accepted": 0.41573856210708615
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2285212874412537,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2475154825619288,
                  "rejected_mean_error": 1.8013064523431705,
                  "gap_rejected_minus_accepted": 0.5537909697812418
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
        "best_epoch": 65,
        "best_calib_loss": 0.01436353474855423,
        "train_time_sec": 40.25392031669617,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995636538229821,
              "spearman": 0.9987924233441079,
              "auroc_top30_bad": 0.9995015238095237,
              "mae": 0.02381766039902577,
              "mse": 0.0010039370512200977,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7759510767756251,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0719310137698194
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2144538200882729
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.57010666624445
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9247830093790311
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3561629488177016
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999750499583766,
              "spearman": 0.9994085344482988,
              "auroc_top30_worst": 0.999784761904762,
              "pairwise_seed_ranking": 0.946,
              "predicted_best_mean_error": 1.6819063926041127,
              "seed0_mean_error": 1.7700846727788448,
              "random_seed_mean_error": 1.7617888971567155,
              "oracle_best_mean_error": 1.6800175212025643,
              "improvement_over_seed0": 0.08817828017473217,
              "gap_to_oracle": 0.0018888714015483643,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6740059757828712
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8365689047574997
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0504212984919548
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2769693026781082
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7601412408292294
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0708704948425303,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4629072111911243,
                  "rejected_mean_error": 4.435247507572174,
                  "gap_rejected_minus_accepted": 2.9723402963810495
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.996804118156433,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2769693026781082,
                  "rejected_mean_error": 3.2096570552825927,
                  "gap_rejected_minus_accepted": 1.9326877526044846
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4778225421905518,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0504212984919548,
                  "rejected_mean_error": 2.469861183166504,
                  "gap_rejected_minus_accepted": 1.4194398846745493
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0393609404563904,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8365689047574997,
                  "rejected_mean_error": 2.0679986861864728,
                  "gap_rejected_minus_accepted": 1.231429781428973
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.136726808547974,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4652765171726545,
                  "rejected_mean_error": 4.513358073234558,
                  "gap_rejected_minus_accepted": 3.048081556061904
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0086328983306885,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2751882166465123,
                  "rejected_mean_error": 3.254774041175842,
                  "gap_rejected_minus_accepted": 1.9795858245293299
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4700840711593628,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0454866542220116,
                  "rejected_mean_error": 2.494682691335678,
                  "gap_rejected_minus_accepted": 1.4491960371136665
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0340320467948914,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8282477639913559,
                  "rejected_mean_error": 2.0840303090413412,
                  "gap_rejected_minus_accepted": 1.2557825450499853
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.98583221097793,
              "spearman": 0.975015599800798,
              "auroc_top30_bad": 0.9776426666666667,
              "mae": 0.13110539975203575,
              "mse": 0.038325033182790055,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8983666605625283,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09166968059539794
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2063799866437912
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5978379490494728
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0221027768214543
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9937451852897659,
              "spearman": 0.9932525811536521,
              "auroc_top30_worst": 0.998592,
              "pairwise_seed_ranking": 0.912,
              "predicted_best_mean_error": 1.996306567788124,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10817443692684203,
              "gap_to_oracle": 0.007411338090896447,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.627297816991806
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8659069105409659
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2262356933116914
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5483738339976716
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.118152332305908,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8419930285082924,
                  "rejected_mean_error": 4.221045980453491,
                  "gap_rejected_minus_accepted": 2.379052951945199
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8087767958641052,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5468552202590629,
                  "rejected_mean_error": 3.675621607813972,
                  "gap_rejected_minus_accepted": 2.128766387554909
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8252142071723938,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2262356933116914,
                  "rejected_mean_error": 2.933560954093933,
                  "gap_rejected_minus_accepted": 1.7073252607822418
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2168933749198914,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8676533861853444,
                  "rejected_mean_error": 2.4848424703868757,
                  "gap_rejected_minus_accepted": 1.6171890842015313
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.1420409202575685,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8652339469061958,
                  "rejected_mean_error": 4.257704524993897,
                  "gap_rejected_minus_accepted": 2.3924705780877007
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.828617572784424,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5554683450709053,
                  "rejected_mean_error": 3.734090010325114,
                  "gap_rejected_minus_accepted": 2.1786216652542088
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8384248614311218,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2235108261108398,
                  "rejected_mean_error": 2.9854511833190918,
                  "gap_rejected_minus_accepted": 1.761940357208252
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2271137833595276,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.865101420690143,
                  "rejected_mean_error": 2.5220259982634357,
                  "gap_rejected_minus_accepted": 1.6569245775732928
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9590797958073027,
              "spearman": 0.9401566738509786,
              "auroc_top30_bad": 0.9336518095238094,
              "mae": 0.15653872205279767,
              "mse": 0.07161865941255419,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7250470184728119,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07000478899478912
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2258277864217758
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6607817963004112
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0579594363768896
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9914712376171475,
              "spearman": 0.9893926352592868,
              "auroc_top30_worst": 0.9820251428571428,
              "pairwise_seed_ranking": 0.8652,
              "predicted_best_mean_error": 1.5901161340475083,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06702700841426834,
              "gap_to_oracle": 0.01021861255168921,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4221518304347992
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6534811909764241
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0244485447883607
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3067870856221042
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6993622541427618,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.458835721598731,
                  "rejected_mean_error": 3.3402432136535642,
                  "gap_rejected_minus_accepted": 1.8814074920548332
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0548234581947327,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.30600900017719,
                  "rejected_mean_error": 2.667700176802687,
                  "gap_rejected_minus_accepted": 1.361691176625497
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6704344749450684,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0244485447883607,
                  "rejected_mean_error": 2.2695043968200683,
                  "gap_rejected_minus_accepted": 1.2450558520317077
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0632529258728027,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6547520337775111,
                  "rejected_mean_error": 1.9784239081461121,
                  "gap_rejected_minus_accepted": 1.3236718743686011
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.814100241661072,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.463609338071611,
                  "rejected_mean_error": 3.3989473819732665,
                  "gap_rejected_minus_accepted": 1.9353380439016554
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.092936635017395,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3039585998989045,
                  "rejected_mean_error": 2.705484562449985,
                  "gap_rejected_minus_accepted": 1.4015259625510805
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.673993706703186,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0142146000862122,
                  "rejected_mean_error": 2.3000716848373415,
                  "gap_rejected_minus_accepted": 1.2858570847511293
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0674414038658142,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6435922592405289,
                  "rejected_mean_error": 1.9986068090015554,
                  "gap_rejected_minus_accepted": 1.3550145497610266
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9693123372425823,
              "spearman": 0.9495928844471223,
              "auroc_top30_bad": 0.9483619047619047,
              "mae": 0.1388127828620374,
              "mse": 0.04282498872660966,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6801661208332144,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07002921962738037
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2317116405248642
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7944759979248047
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.148577223523458
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9614786683830011,
              "spearman": 0.9366383804405636,
              "auroc_top30_worst": 0.9364114285714286,
              "pairwise_seed_ranking": 0.9084,
              "predicted_best_mean_error": 1.5944442566633223,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06730687129497537,
              "gap_to_oracle": 0.002420324683189312,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8458661100864411
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1032819389723814
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3641659248828888
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.522754333071363
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0482559204101562,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5980482103824616,
                  "rejected_mean_error": 2.2156990747451784,
                  "gap_rejected_minus_accepted": 0.6176508643627168
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8810660541057587,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5223048369747088,
                  "rejected_mean_error": 2.071460028045094,
                  "gap_rejected_minus_accepted": 0.5491551910703851
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7178221344947815,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3641659248828888,
                  "rejected_mean_error": 1.9554606687545777,
                  "gap_rejected_minus_accepted": 0.5912947438716889
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3794127404689789,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1040435919936853,
                  "rejected_mean_error": 1.8454652899993522,
                  "gap_rejected_minus_accepted": 0.7414216980056669
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0595919132232665,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6018709630436367,
                  "rejected_mean_error": 2.2006726121902465,
                  "gap_rejected_minus_accepted": 0.5988016491466097
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.864001214504242,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.533555843932106,
                  "rejected_mean_error": 2.042267288480486,
                  "gap_rejected_minus_accepted": 0.50871144454838
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7435807585716248,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3780789856910705,
                  "rejected_mean_error": 1.945423270225525,
                  "gap_rejected_minus_accepted": 0.5673442845344545
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.409669190645218,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1135004654763236,
                  "rejected_mean_error": 1.8464558966019575,
                  "gap_rejected_minus_accepted": 0.7329554311256339
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
        "best_epoch": 78,
        "best_calib_loss": 0.018442334607243538,
        "train_time_sec": 56.373639822006226,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9990595424231417,
              "spearman": 0.9975399480853182,
              "auroc_top30_bad": 0.9989672857142857,
              "mae": 0.038769163764046974,
              "mse": 0.0024783552272844038,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.989,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7902480619369021,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07337050685973372
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21494385583675465
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5702828610791592
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9251797371794004
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3561629488177016
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9993210522242095,
              "spearman": 0.9985082968602246,
              "auroc_top30_worst": 0.999176,
              "pairwise_seed_ranking": 0.9583,
              "predicted_best_mean_error": 1.6817899655401707,
              "seed0_mean_error": 1.7700846727788448,
              "random_seed_mean_error": 1.7617888971567155,
              "oracle_best_mean_error": 1.6800175212025643,
              "improvement_over_seed0": 0.08829470723867416,
              "gap_to_oracle": 0.0017724443376063714,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6742563478350639
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8372358997583389
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0508554018855094
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2774251341422398
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7601412408292294
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1847133398056053,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4629345185425546,
                  "rejected_mean_error": 4.435001741409302,
                  "gap_rejected_minus_accepted": 2.9720672228667473
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.048196017742157,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2774251341422398,
                  "rejected_mean_error": 3.2082895608901976,
                  "gap_rejected_minus_accepted": 1.9308644267479578
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5241271257400513,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0508554018855094,
                  "rejected_mean_error": 2.469427079772949,
                  "gap_rejected_minus_accepted": 1.4185716778874398
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.085296630859375,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8372358997583389,
                  "rejected_mean_error": 2.067776354519526,
                  "gap_rejected_minus_accepted": 1.2305404547611871
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.232340240478516,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4653339463803503,
                  "rejected_mean_error": 4.512841210365296,
                  "gap_rejected_minus_accepted": 3.0475072639849454
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0598405599594116,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2755361739397049,
                  "rejected_mean_error": 3.2537301692962646,
                  "gap_rejected_minus_accepted": 1.9781939953565597
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.529481053352356,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.045681574523449,
                  "rejected_mean_error": 2.494487771034241,
                  "gap_rejected_minus_accepted": 1.448806196510792
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.089650183916092,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8285466402769088,
                  "rejected_mean_error": 2.0839306836128233,
                  "gap_rejected_minus_accepted": 1.2553840433359145
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9854485917825181,
              "spearman": 0.9731655084167454,
              "auroc_top30_bad": 0.9792716190476191,
              "mae": 0.15848186241984366,
              "mse": 0.04511065757455899,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8987557858194327,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1272332890033722
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21314179854393006
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5980229002594948
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0223878717184067
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9946637026612959,
              "spearman": 0.9922371001837442,
              "auroc_top30_worst": 0.9998019047619048,
              "pairwise_seed_ranking": 0.9224,
              "predicted_best_mean_error": 1.993679416179657,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.11080158853530908,
              "gap_to_oracle": 0.004784186482429398,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6219851534366607
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8719120834691402
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.221882265806198
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5476963465084146
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.19620418548584,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8421478657987382,
                  "rejected_mean_error": 4.219652444839477,
                  "gap_rejected_minus_accepted": 2.377504579040739
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8654476404190063,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5464968605954976,
                  "rejected_mean_error": 3.6766943969665626,
                  "gap_rejected_minus_accepted": 2.130197536371065
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7149661183357239,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.221882265806198,
                  "rejected_mean_error": 2.9379143815994264,
                  "gap_rejected_minus_accepted": 1.7160321157932283
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1738273203372955,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8736393732575182,
                  "rejected_mean_error": 2.482842882389447,
                  "gap_rejected_minus_accepted": 1.609203509131929
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.303495788574218,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.86610019048055,
                  "rejected_mean_error": 4.249908332824707,
                  "gap_rejected_minus_accepted": 2.383808142344157
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9615349173545837,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5548569416617328,
                  "rejected_mean_error": 3.7359048109205943,
                  "gap_rejected_minus_accepted": 2.1810478692588617
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.748920977115631,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2204489135742187,
                  "rejected_mean_error": 2.988513095855713,
                  "gap_rejected_minus_accepted": 1.7680641822814942
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.182428240776062,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8698922528160943,
                  "rejected_mean_error": 2.5204119746060294,
                  "gap_rejected_minus_accepted": 1.650519721789935
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9666016047407431,
              "spearman": 0.9477950514528611,
              "auroc_top30_bad": 0.9407375238095238,
              "mae": 0.1653276702279225,
              "mse": 0.06822567558833939,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7035946006494792,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0755482850074768
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20936709547042848
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6512827608466148
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0555088930368424
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9890842969027942,
              "spearman": 0.9797316805962758,
              "auroc_top30_worst": 0.9699596190476191,
              "pairwise_seed_ranking": 0.884,
              "predicted_best_mean_error": 1.5869577709436418,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.07018537151813486,
              "gap_to_oracle": 0.007060249447822686,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3994874286651611
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.653413138901576
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.029879238986969
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3090744723262056
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.55678677558899,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4591136542956034,
                  "rejected_mean_error": 3.337741819381714,
                  "gap_rejected_minus_accepted": 1.8786281650861105
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9541102349758148,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3086136274811044,
                  "rejected_mean_error": 2.6599029378769115,
                  "gap_rejected_minus_accepted": 1.351289310395807
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6394942998886108,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.029879238986969,
                  "rejected_mean_error": 2.26407370262146,
                  "gap_rejected_minus_accepted": 1.2341944636344908
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0310568809509277,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6550053272384424,
                  "rejected_mean_error": 1.9783392967765587,
                  "gap_rejected_minus_accepted": 1.3233339695381163
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.691281962394714,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4643141012721592,
                  "rejected_mean_error": 3.392604513168335,
                  "gap_rejected_minus_accepted": 1.9282904118961757
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9585007429122925,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3043771354272404,
                  "rejected_mean_error": 2.7042422427071466,
                  "gap_rejected_minus_accepted": 1.3998651072799062
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6659144163131714,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0212274241447448,
                  "rejected_mean_error": 2.2930588607788085,
                  "gap_rejected_minus_accepted": 1.2718314366340637
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0191293954849243,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6431051417002602,
                  "rejected_mean_error": 1.9987709181194,
                  "gap_rejected_minus_accepted": 1.3556657764191398
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.968669059801868,
              "spearman": 0.9531750314605342,
              "auroc_top30_bad": 0.9547299047619049,
              "mae": 0.15677306999489665,
              "mse": 0.04602529319571812,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6834577573358644,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09077903354167938
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22823155093193054
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7929434821128846
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1505164780298869
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9528991499984651,
              "spearman": 0.9500646756253925,
              "auroc_top30_worst": 0.9560807619047619,
              "pairwise_seed_ranking": 0.8908,
              "predicted_best_mean_error": 1.5997914272546767,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.061959700703621,
              "gap_to_oracle": 0.007767495274543679,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8458507874011993
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1014601092499037
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3600387835025787
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5234837344269763
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0968699216842652,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.601233380344179,
                  "rejected_mean_error": 2.1870325450897217,
                  "gap_rejected_minus_accepted": 0.5857991647455427
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9331378042697906,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5231442166812392,
                  "rejected_mean_error": 2.0689472523741066,
                  "gap_rejected_minus_accepted": 0.5458030356928674
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.679709792137146,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3600387835025787,
                  "rejected_mean_error": 1.9595878101348876,
                  "gap_rejected_minus_accepted": 0.5995490266323089
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2993274629116058,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.102661890058091,
                  "rejected_mean_error": 1.8459268403791185,
                  "gap_rejected_minus_accepted": 0.7432649503210276
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0971934318542482,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.609084107875824,
                  "rejected_mean_error": 2.1357543087005615,
                  "gap_rejected_minus_accepted": 0.5266702008247375
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9272109270095825,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5320929731914703,
                  "rejected_mean_error": 2.04660946036142,
                  "gap_rejected_minus_accepted": 0.5145164871699499
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6947523951530457,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3713606877326965,
                  "rejected_mean_error": 1.952141568183899,
                  "gap_rejected_minus_accepted": 0.5807808804512025
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3028816878795624,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1118762256607178,
                  "rejected_mean_error": 1.8470031003901028,
                  "gap_rejected_minus_accepted": 0.7351268747293851
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
        "best_epoch": 65,
        "best_calib_loss": 0.018590670078992844,
        "train_time_sec": 47.667354345321655,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994501176987971,
              "spearman": 0.9981040316267039,
              "auroc_top30_bad": 0.9995072380952381,
              "mae": 0.02988685334288748,
              "mse": 0.0016176728654828296,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7899774779292427,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07451266680599657
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21456609680927358
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5701456483973889
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9247524374414701
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3561629488177016
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998043084734418,
              "spearman": 0.999520755596807,
              "auroc_top30_worst": 0.9998354285714286,
              "pairwise_seed_ranking": 0.953,
              "predicted_best_mean_error": 1.6811028556227685,
              "seed0_mean_error": 1.7700846727788448,
              "random_seed_mean_error": 1.7617888971567155,
              "oracle_best_mean_error": 1.6800175212025643,
              "improvement_over_seed0": 0.08898181715607634,
              "gap_to_oracle": 0.0010853344202041981,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6731478164792061
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8363384014844895
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0504491584181785
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.277030810157458
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7601412408292294
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1570253610610965,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.462883235712846,
                  "rejected_mean_error": 4.435463286876678,
                  "gap_rejected_minus_accepted": 2.972580051163832
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0468170046806335,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.277030810157458,
                  "rejected_mean_error": 3.2094725328445435,
                  "gap_rejected_minus_accepted": 1.9324417226870856
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5078681707382202,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0504491584181785,
                  "rejected_mean_error": 2.4698333232402803,
                  "gap_rejected_minus_accepted": 1.4193841648221017
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0639654397964478,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8363384014844895,
                  "rejected_mean_error": 2.0680755206108095,
                  "gap_rejected_minus_accepted": 1.23173711912632
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.202263045310975,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4652702703409726,
                  "rejected_mean_error": 4.513414294719696,
                  "gap_rejected_minus_accepted": 3.0481440243787232
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.053565263748169,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2751847570339838,
                  "rejected_mean_error": 3.254784420013428,
                  "gap_rejected_minus_accepted": 1.9795996629794441
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4995529651641846,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0454239892363548,
                  "rejected_mean_error": 2.4947453563213347,
                  "gap_rejected_minus_accepted": 1.4493213670849798
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0600526928901672,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8282204278707505,
                  "rejected_mean_error": 2.084039421081543,
                  "gap_rejected_minus_accepted": 1.2558189932107928
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9849396892354051,
              "spearman": 0.9734000089642149,
              "auroc_top30_bad": 0.9767466666666665,
              "mae": 0.15467845973530783,
              "mse": 0.045663587265088734,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8631127592549833,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11487453651428223
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21388185582160948
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5934817886948586
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0240083645264308
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9943514201901025,
              "spearman": 0.991926477776946,
              "auroc_top30_worst": 0.9997257142857143,
              "pairwise_seed_ranking": 0.9132,
              "predicted_best_mean_error": 1.9953679938316344,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10911301088333158,
              "gap_to_oracle": 0.006472764134406894,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6239777333736419
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8709216609788246
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.224761500120163
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5488598906854067
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.124924087524414,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8423724609745873,
                  "rejected_mean_error": 4.2176310882568355,
                  "gap_rejected_minus_accepted": 2.375258627282248
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.738995313644409,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5476049075068126,
                  "rejected_mean_error": 3.6733773364045748,
                  "gap_rejected_minus_accepted": 2.125772428897762
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7170498967170715,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.224761500120163,
                  "rejected_mean_error": 2.935035147285461,
                  "gap_rejected_minus_accepted": 1.7102736471652982
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.14334237575531,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8722086721144545,
                  "rejected_mean_error": 2.4833208007008443,
                  "gap_rejected_minus_accepted": 1.6111121285863899
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.228962421417236,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8664221413930258,
                  "rejected_mean_error": 4.247010774612427,
                  "gap_rejected_minus_accepted": 2.3805886332194013
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.804176449775696,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5548569416617328,
                  "rejected_mean_error": 3.7359048109205943,
                  "gap_rejected_minus_accepted": 2.1810478692588617
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7200531363487244,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2273341045379638,
                  "rejected_mean_error": 2.9816279048919676,
                  "gap_rejected_minus_accepted": 1.7542938003540038
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1454727351665497,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8698922528160943,
                  "rejected_mean_error": 2.5204119746060294,
                  "gap_rejected_minus_accepted": 1.650519721789935
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9658032765020756,
              "spearman": 0.939428674372982,
              "auroc_top30_bad": 0.9227748571428571,
              "mae": 0.1772953752233647,
              "mse": 0.06900505995255506,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6896014758053894,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.053879474401473997
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19214810376167296
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6532045252203942
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0649424343983331
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9849895451526114,
              "spearman": 0.9652502879041843,
              "auroc_top30_worst": 0.9521097142857142,
              "pairwise_seed_ranking": 0.8796,
              "predicted_best_mean_error": 1.5895546731948853,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06758846926689133,
              "gap_to_oracle": 0.009657151699066224,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4005120906829834
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6537597022759609
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0378404006004334
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3147088776646392
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5090089082717926,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4586752546628317,
                  "rejected_mean_error": 3.34168741607666,
                  "gap_rejected_minus_accepted": 1.8830121614138284
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9865238964557648,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3137087559242004,
                  "rejected_mean_error": 2.644650109278889,
                  "gap_rejected_minus_accepted": 1.3309413533546885
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6409366726875305,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0378404006004334,
                  "rejected_mean_error": 2.2561125410079956,
                  "gap_rejected_minus_accepted": 1.2182721404075623
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0702160000801086,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6552135468291017,
                  "rejected_mean_error": 1.9782697421000632,
                  "gap_rejected_minus_accepted": 1.3230561952709614
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5943129539489744,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4638889373673334,
                  "rejected_mean_error": 3.3964309883117676,
                  "gap_rejected_minus_accepted": 1.9325420509444342
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.986963838338852,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.308781307967589,
                  "rejected_mean_error": 2.691169540087382,
                  "gap_rejected_minus_accepted": 1.382388232119793
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6662723422050476,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0293191199302674,
                  "rejected_mean_error": 2.284967164993286,
                  "gap_rejected_minus_accepted": 1.2556480450630187
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0513863563537598,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.645200370796143,
                  "rejected_mean_error": 1.9980650387983272,
                  "gap_rejected_minus_accepted": 1.352864668002184
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9651800094775133,
              "spearman": 0.9429801874601732,
              "auroc_top30_bad": 0.9468510476190476,
              "mae": 0.15420982780857012,
              "mse": 0.049468724507845806,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6644985462452437,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08690648758411408
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2265577615261078
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7982281468391419
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1528558050791422
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9460632024957816,
              "spearman": 0.928937498199999,
              "auroc_top30_worst": 0.9400441904761905,
              "pairwise_seed_ranking": 0.9032,
              "predicted_best_mean_error": 1.5950740603208542,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06667706763744352,
              "gap_to_oracle": 0.003050128340721159,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8439169170856475
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1027745093481662
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3674762884616851
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5265966610931385
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.113536930084229,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6005912136766645,
                  "rejected_mean_error": 2.192812045097351,
                  "gap_rejected_minus_accepted": 0.5922208314206867
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.922676146030426,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5264770918811017,
                  "rejected_mean_error": 2.058969923101675,
                  "gap_rejected_minus_accepted": 0.5324928312205732
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6715219020843506,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3674762884616851,
                  "rejected_mean_error": 1.9521503051757811,
                  "gap_rejected_minus_accepted": 0.584674016714096
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3737301528453827,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1039184923179615,
                  "rejected_mean_error": 1.8455070788985002,
                  "gap_rejected_minus_accepted": 0.7415885865805387
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.126994514465332,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6067938436402216,
                  "rejected_mean_error": 2.156366686820984,
                  "gap_rejected_minus_accepted": 0.5495728431807623
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.927570790052414,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.530801355201293,
                  "rejected_mean_error": 2.050443310586233,
                  "gap_rejected_minus_accepted": 0.5196419553849403
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6698911786079407,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3775070614814757,
                  "rejected_mean_error": 1.9459951944351197,
                  "gap_rejected_minus_accepted": 0.568488132953644
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3742362558841705,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1151320262560769,
                  "rejected_mean_error": 1.8459062263927357,
                  "gap_rejected_minus_accepted": 0.7307742001366588
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
        "best_epoch": 27,
        "best_calib_loss": 0.11895463615655899,
        "train_time_sec": 13.566534757614136,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8964041040661006,
              "spearman": 0.768505031901804,
              "auroc_top30_bad": 0.8373474285714284,
              "mae": 0.2326724903274513,
              "mse": 0.21274340653911628,
              "expert_lt_perturb_large": 0.99,
              "expert_lt_other_task": 0.505,
              "expert_lt_simvla_seed0": 0.993,
              "same_context_pred_std": 0.692105567538141,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13934750910103322
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20051737436652184
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.2456417343467474
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.5069512522041798
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8960445861935615
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979359480197882,
              "spearman": 0.9943374586852267,
              "auroc_top30_worst": 0.9981312380952382,
              "pairwise_seed_ranking": 0.8392,
              "predicted_best_mean_error": 1.1934597614705562,
              "seed0_mean_error": 1.273960811495781,
              "random_seed_mean_error": 1.2650585584044456,
              "oracle_best_mean_error": 1.185694094002247,
              "improvement_over_seed0": 0.08050105002522479,
              "gap_to_oracle": 0.007765667468309312,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22652614280581473
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.36484810799360273
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5713113041222095
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7902038896282514
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635830781012773
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.646046280860906,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9716846889952818,
                  "rejected_mean_error": 3.890668580055237,
                  "gap_rejected_minus_accepted": 2.918983891059955
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5090009570121765,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7902038896282514,
                  "rejected_mean_error": 2.6837206435203553,
                  "gap_rejected_minus_accepted": 1.8935167538921038
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9978062212467194,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5713113041222095,
                  "rejected_mean_error": 1.9558548520803452,
                  "gap_rejected_minus_accepted": 1.3845435479581356
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5658667087554932,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.36484810799360273,
                  "rejected_mean_error": 1.5631614014705022,
                  "gap_rejected_minus_accepted": 1.1983132934768994
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7353270530700686,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9744317620330387,
                  "rejected_mean_error": 3.9697222566604613,
                  "gap_rejected_minus_accepted": 2.9952904946274224
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5314164757728577,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7876212339401245,
                  "rejected_mean_error": 2.7329795441627502,
                  "gap_rejected_minus_accepted": 1.9453583102226257
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9984770119190216,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5658856446743011,
                  "rejected_mean_error": 1.9820359783172607,
                  "gap_rejected_minus_accepted": 1.4161503336429595
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5698907971382141,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.3570273749828339,
                  "rejected_mean_error": 1.57960529033343,
                  "gap_rejected_minus_accepted": 1.222577915350596
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8267788221644071,
              "spearman": 0.7166483125795261,
              "auroc_top30_bad": 0.7762468571428572,
              "mae": 0.5800245806217166,
              "mse": 0.7064452206820258,
              "expert_lt_perturb_large": 0.988,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.8877191860563847,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5760988026857377
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7047780829191208
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7654317074298859
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0953773557106654
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8563083965342542,
              "spearman": 0.8008155458659494,
              "auroc_top30_worst": 0.8882285714285714,
              "pairwise_seed_ranking": 0.7732,
              "predicted_best_mean_error": 2.007619367003441,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.096861637711525,
              "gap_to_oracle": 0.018724137306213473,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1174272973537445
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.133706633765728
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.37064850564003
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.596207412162315
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.959141421318055,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8428660374482473,
                  "rejected_mean_error": 4.213188899993897,
                  "gap_rejected_minus_accepted": 2.37032286254565
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.482189953327179,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5954672176720874,
                  "rejected_mean_error": 3.530096235366675,
                  "gap_rejected_minus_accepted": 1.9346290176945875
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3446066975593567,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.37064850564003,
                  "rejected_mean_error": 2.7891481417655943,
                  "gap_rejected_minus_accepted": 1.4184996361255644
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7728969305753708,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1368663645209596,
                  "rejected_mean_error": 2.394913268445523,
                  "gap_rejected_minus_accepted": 1.2580469039245634
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.985334038734436,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.866182738410102,
                  "rejected_mean_error": 4.2491654014587406,
                  "gap_rejected_minus_accepted": 2.3829826630486384
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.542477548122406,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.607928001944394,
                  "rejected_mean_error": 3.5783764256371393,
                  "gap_rejected_minus_accepted": 1.9704484236927453
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4004038572311401,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3733283252716064,
                  "rejected_mean_error": 2.835633684158325,
                  "gap_rejected_minus_accepted": 1.4623053588867188
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8119887858629227,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1109292526093741,
                  "rejected_mean_error": 2.4392069960660474,
                  "gap_rejected_minus_accepted": 1.3282777434566733
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6323583175792391,
              "spearman": 0.4849691713456502,
              "auroc_top30_bad": 0.6165226666666667,
              "mae": 0.7904942186842827,
              "mse": 1.1376382619067913,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 0.988,
              "same_context_pred_std": 0.5669726947432361,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.081081028342247
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9782951828956604
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9375808424115181
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1220691704034804
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8477830329655808,
              "spearman": 0.8195355455587492,
              "auroc_top30_worst": 0.8847085714285714,
              "pairwise_seed_ranking": 0.778,
              "predicted_best_mean_error": 1.597841672539711,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.05930146992206553,
              "gap_to_oracle": 0.01794415104389202,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6696444129943848
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8266645981333195
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0938512932777404
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3376527340300302
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.724319350719452,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4776771159172057,
                  "rejected_mean_error": 3.1706706647872926,
                  "gap_rejected_minus_accepted": 1.692993548870087
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.2969332337379456,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3373027955328005,
                  "rejected_mean_error": 2.5740187510895653,
                  "gap_rejected_minus_accepted": 1.2367159555567648
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.056077003479004,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0938512932777404,
                  "rejected_mean_error": 2.2001016483306883,
                  "gap_rejected_minus_accepted": 1.1062503550529479
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.48946622014045715,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8272031772250946,
                  "rejected_mean_error": 1.9208174963007614,
                  "gap_rejected_minus_accepted": 1.0936143190756669
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7782152533531188,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4828948696454367,
                  "rejected_mean_error": 3.225377597808838,
                  "gap_rejected_minus_accepted": 1.7424827281634012
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3271062672138214,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3272991196356994,
                  "rejected_mean_error": 2.636203972120134,
                  "gap_rejected_minus_accepted": 1.3089048524844344
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0925158262252808,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0763487248420716,
                  "rejected_mean_error": 2.237937560081482,
                  "gap_rejected_minus_accepted": 1.1615888352394106
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.4806361347436905,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8076874944898818,
                  "rejected_mean_error": 1.9433233875004365,
                  "gap_rejected_minus_accepted": 1.1356358930105548
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5073195820655032,
              "spearman": 0.3750213042866376,
              "auroc_top30_bad": 0.5624499047619047,
              "mae": 0.757445824944468,
              "mse": 1.0765403570588388,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5585841973069534,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2593987809419631
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0050605141162872
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.034938763332367
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.25186464138031
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7057457829032506,
              "spearman": 0.6490444745244638,
              "auroc_top30_worst": 0.7489127619047619,
              "pairwise_seed_ranking": 0.7272,
              "predicted_best_mean_error": 1.6099190499782563,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.05183207798004141,
              "gap_to_oracle": 0.017895117998123267,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9622608211040496
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2719796258860674
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4440826788425445
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5678521431903087
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.4985662817955017,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6189149248600005,
                  "rejected_mean_error": 2.0278986444473266,
                  "gap_rejected_minus_accepted": 0.40898371958732604
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3429930210113525,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.567571253920314,
                  "rejected_mean_error": 1.935950019489081,
                  "gap_rejected_minus_accepted": 0.36837876556876714
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0599234700202942,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4440826788425445,
                  "rejected_mean_error": 1.8755439147949218,
                  "gap_rejected_minus_accepted": 0.4314612359523773
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8163716346025467,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2746013251546853,
                  "rejected_mean_error": 1.788491362059765,
                  "gap_rejected_minus_accepted": 0.5138900369050798
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.494547188282013,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6233557052082486,
                  "rejected_mean_error": 2.0073099327087403,
                  "gap_rejected_minus_accepted": 0.3839542275004917
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3417484760284424,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5632959562826922,
                  "rejected_mean_error": 1.9539910819795396,
                  "gap_rejected_minus_accepted": 0.3906951256968474
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.068224012851715,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.425134024143219,
                  "rejected_mean_error": 1.8983682317733765,
                  "gap_rejected_minus_accepted": 0.47323420763015744
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8311431407928467,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2868110897049072,
                  "rejected_mean_error": 1.7880678253377822,
                  "gap_rejected_minus_accepted": 0.501256735632875
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
        "best_epoch": 31,
        "best_calib_loss": 0.06516274064779282,
        "train_time_sec": 46.84461069107056,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9946127254097022,
              "spearman": 0.9915099331289975,
              "auroc_top30_bad": 0.9994115714285714,
              "mae": 0.12189321976264474,
              "mse": 0.02736678382704414,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.945,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6973885201134864,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.31332325780391695
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.24648322962522506
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.12695993806123734
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.4777634205341339
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8960445861935615
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9988203064565371,
              "spearman": 0.9988509361139825,
              "auroc_top30_worst": 0.9995114285714286,
              "pairwise_seed_ranking": 0.9265,
              "predicted_best_mean_error": 1.1876548494696617,
              "seed0_mean_error": 1.273960811495781,
              "random_seed_mean_error": 1.2650585584044456,
              "oracle_best_mean_error": 1.185694094002247,
              "improvement_over_seed0": 0.08630596202611929,
              "gap_to_oracle": 0.0019607554674148098,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.21409608647227288
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.35988351904153826
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5703777840435504
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7891849661548932
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635830781012773
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.722708606719971,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9715882382955816,
                  "rejected_mean_error": 3.891536636352539,
                  "gap_rejected_minus_accepted": 2.9199483980569574
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5840608477592468,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7891849661548932,
                  "rejected_mean_error": 2.6867774139404297,
                  "gap_rejected_minus_accepted": 1.8975924477855366
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0750116109848022,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5703777840435504,
                  "rejected_mean_error": 1.9567883721590043,
                  "gap_rejected_minus_accepted": 1.3864105881154538
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6367844492197037,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.35988351904153826,
                  "rejected_mean_error": 1.5648162644545238,
                  "gap_rejected_minus_accepted": 1.2049327454129855
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.784820628166199,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9744130292203691,
                  "rejected_mean_error": 3.9698908519744873,
                  "gap_rejected_minus_accepted": 2.9954778227541183
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5816583335399628,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7871189173062643,
                  "rejected_mean_error": 2.734486494064331,
                  "gap_rejected_minus_accepted": 1.947367576758067
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0751540064811707,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5657890415191651,
                  "rejected_mean_error": 1.982132581472397,
                  "gap_rejected_minus_accepted": 1.4163435399532318
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6354649066925049,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.35437368059158325,
                  "rejected_mean_error": 1.5804898551305135,
                  "gap_rejected_minus_accepted": 1.2261161745389302
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9800094161951496,
              "spearman": 0.971913251604188,
              "auroc_top30_bad": 0.9886491428571428,
              "mae": 0.36905025692803317,
              "mse": 0.1778144987354377,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.916,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8475741040486557,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.19489610743522645
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22351931698322297
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5873324797272682
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0211229873418808
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9819266790767669,
              "spearman": 0.9864491535674583,
              "auroc_top30_worst": 0.9912076190476191,
              "pairwise_seed_ranking": 0.9052,
              "predicted_best_mean_error": 1.9943185962438583,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.1101624084711077,
              "gap_to_oracle": 0.005423366546630781,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6269912884235382
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8717252378089305
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2275455468654632
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5586170957985717
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8063507318496708,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8480535232490964,
                  "rejected_mean_error": 4.166501527786255,
                  "gap_rejected_minus_accepted": 2.3184480045371583
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.444188416004181,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5571094140362713,
                  "rejected_mean_error": 3.644924548487313,
                  "gap_rejected_minus_accepted": 2.0878151344510414
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4272952675819397,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2275455468654632,
                  "rejected_mean_error": 2.932251100540161,
                  "gap_rejected_minus_accepted": 1.7047055536746978
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8622753322124481,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8734221712659342,
                  "rejected_mean_error": 2.482915437590478,
                  "gap_rejected_minus_accepted": 1.6094932663245436
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8736823081970213,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8700732156965467,
                  "rejected_mean_error": 4.214151105880737,
                  "gap_rejected_minus_accepted": 2.3440778901841908
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.534190833568573,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.565169240064162,
                  "rejected_mean_error": 3.7052952902657643,
                  "gap_rejected_minus_accepted": 2.1401260502016024
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.46902596950531,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2277824697494506,
                  "rejected_mean_error": 2.9811795396804808,
                  "gap_rejected_minus_accepted": 1.7533970699310302
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8610149174928665,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.867061730415102,
                  "rejected_mean_error": 2.5213655730619786,
                  "gap_rejected_minus_accepted": 1.6543038426468766
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9817358015256572,
              "spearman": 0.9725324340023511,
              "auroc_top30_bad": 0.9783299047619048,
              "mae": 0.3804077401705086,
              "mse": 0.18811993267638613,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.912,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6650756730312363,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15175126987695695
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18844496762752533
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6320056808829307
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0445350670099258
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9832233460427615,
              "spearman": 0.9770245525917137,
              "auroc_top30_worst": 0.9723946666666666,
              "pairwise_seed_ranking": 0.8612,
              "predicted_best_mean_error": 1.5909526872634887,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06619045519828792,
              "gap_to_oracle": 0.011055165767669628,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4123263809680939
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.65475467668894
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0345226155281066
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3098001504884853
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.313513398170471,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.459770775742001,
                  "rejected_mean_error": 3.3318277263641356,
                  "gap_rejected_minus_accepted": 1.8720569506221345
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6411210894584656,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3091551854872525,
                  "rejected_mean_error": 2.658281724293011,
                  "gap_rejected_minus_accepted": 1.3491265388057585
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.274329662322998,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0345226155281066,
                  "rejected_mean_error": 2.2594303260803223,
                  "gap_rejected_minus_accepted": 1.2249077105522157
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6548834592103958,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6557281672383268,
                  "rejected_mean_error": 1.9780978358160852,
                  "gap_rejected_minus_accepted": 1.3223696685777584
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3983484268188473,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4650840894381205,
                  "rejected_mean_error": 3.3856746196746825,
                  "gap_rejected_minus_accepted": 1.920590530236562
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6626265048980713,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3047812389817468,
                  "rejected_mean_error": 2.7030427607278975,
                  "gap_rejected_minus_accepted": 1.3982615217461507
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.274329662322998,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.025672746181488,
                  "rejected_mean_error": 2.2886135387420654,
                  "gap_rejected_minus_accepted": 1.2629407925605773
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6172665506601334,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6444107038634164,
                  "rejected_mean_error": 1.9983310763211173,
                  "gap_rejected_minus_accepted": 1.353920372457701
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9739604022714461,
              "spearman": 0.9538492910818018,
              "auroc_top30_bad": 0.951977142857143,
              "mae": 0.4010510322558926,
              "mse": 0.20419827828167067,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.928,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6285056662054631,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14896767514944076
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.226768683052063
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.792449310207367
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.145902232170105
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9230584349387176,
              "spearman": 0.8906842784539383,
              "auroc_top30_worst": 0.9046339047619048,
              "pairwise_seed_ranking": 0.9016,
              "predicted_best_mean_error": 1.5961893748044969,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06556175315380086,
              "gap_to_oracle": 0.004165442824363819,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8611058971881866
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1073251073368084
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3749967031955719
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.533291143299674
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6457971453666689,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6061606856717003,
                  "rejected_mean_error": 2.1426867971420287,
                  "gap_rejected_minus_accepted": 0.5365261114703284
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4778778851032257,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5328429590358041,
                  "rejected_mean_error": 2.0399129981050095,
                  "gap_rejected_minus_accepted": 0.5070700390692053
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2681311964988708,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3749967031955719,
                  "rejected_mean_error": 1.9446298904418946,
                  "gap_rejected_minus_accepted": 0.5696331872463227
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.010045439004898,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1088260222738162,
                  "rejected_mean_error": 1.8438677439185827,
                  "gap_rejected_minus_accepted": 0.7350417216447664
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.620396363735199,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6104543079270257,
                  "rejected_mean_error": 2.123422508239746,
                  "gap_rejected_minus_accepted": 0.5129682003127203
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4823004305362701,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5391404912433522,
                  "rejected_mean_error": 2.0256906369375804,
                  "gap_rejected_minus_accepted": 0.4865501456942283
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.283193588256836,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3919112362861634,
                  "rejected_mean_error": 1.9315910196304322,
                  "gap_rejected_minus_accepted": 0.5396797833442688
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0428431332111359,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.115725716901204,
                  "rejected_mean_error": 1.8457062129668373,
                  "gap_rejected_minus_accepted": 0.7299804960656333
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
        "best_epoch": 14,
        "best_calib_loss": 0.06984572857618332,
        "train_time_sec": 51.364405155181885,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9910536000282563,
              "spearman": 0.9907282941551717,
              "auroc_top30_bad": 0.9972070714285715,
              "mae": 0.11268561814612962,
              "mse": 0.027836177637155412,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.99,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6886256813974956,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.3377123090922832
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.24121048503518105
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.1275705575108528
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.47868876191775006
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8960445861935615
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979911965876869,
              "spearman": 0.9962999956918224,
              "auroc_top30_worst": 0.998528380952381,
              "pairwise_seed_ranking": 0.9343,
              "predicted_best_mean_error": 1.1876951305568217,
              "seed0_mean_error": 1.273960811495781,
              "random_seed_mean_error": 1.2650585584044456,
              "oracle_best_mean_error": 1.185694094002247,
              "improvement_over_seed0": 0.08626568093895925,
              "gap_to_oracle": 0.002001036554574842,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22059053859114647
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.36171077588796613
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5714155921280384
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7896761040091514
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635830781012773
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.705784344673159,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9717824875017007,
                  "rejected_mean_error": 3.889788393497467,
                  "gap_rejected_minus_accepted": 2.9180059059957664
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5317032039165497,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7896761040091514,
                  "rejected_mean_error": 2.685304000377655,
                  "gap_rejected_minus_accepted": 1.8956278963685036
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0083089470863342,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5714155921280384,
                  "rejected_mean_error": 1.9557505640745163,
                  "gap_rejected_minus_accepted": 1.384334971946478
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5888776183128357,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.36171077588796613,
                  "rejected_mean_error": 1.5642071788390477,
                  "gap_rejected_minus_accepted": 1.2024964029510816
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.758253931999207,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9746639398733775,
                  "rejected_mean_error": 3.967632656097412,
                  "gap_rejected_minus_accepted": 2.9929687162240346
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5461750030517578,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7873122452100118,
                  "rejected_mean_error": 2.7339065103530884,
                  "gap_rejected_minus_accepted": 1.9465942651430765
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0019165873527527,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5664581270217895,
                  "rejected_mean_error": 1.9814634959697723,
                  "gap_rejected_minus_accepted": 1.4150053689479827
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5845560878515244,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.35539527106285096,
                  "rejected_mean_error": 1.5801493249734242,
                  "gap_rejected_minus_accepted": 1.2247540539105732
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9788698586498382,
              "spearman": 0.9739691067273163,
              "auroc_top30_bad": 0.9881295238095237,
              "mae": 0.3873294596089207,
              "mse": 0.2019628739368845,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8234175155454507,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14319253581762315
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21103289816379547
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5917228520035743
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0232284860372542
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9855172618667958,
              "spearman": 0.9816705439171481,
              "auroc_top30_worst": 0.9971047619047619,
              "pairwise_seed_ranking": 0.902,
              "predicted_best_mean_error": 1.996140163064003,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10834084165096303,
              "gap_to_oracle": 0.007244933366775452,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6377156875133514
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8936782910082585
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2300423827648164
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.551969515838857
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.7780519485473634,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8422247830231984,
                  "rejected_mean_error": 4.218960189819336,
                  "gap_rejected_minus_accepted": 2.376735406796138
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.5027658939361572,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5506523264574013,
                  "rejected_mean_error": 3.6642545518783716,
                  "gap_rejected_minus_accepted": 2.11360222542097
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3875412344932556,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2300423827648164,
                  "rejected_mean_error": 2.929754264640808,
                  "gap_rejected_minus_accepted": 1.6997118818759915
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.779264822602272,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8952761102979556,
                  "rejected_mean_error": 2.475615242374872,
                  "gap_rejected_minus_accepted": 1.5803391320769165
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8628864526748656,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8652242936028374,
                  "rejected_mean_error": 4.257791404724121,
                  "gap_rejected_minus_accepted": 2.3925671111212834
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6037264466285706,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5587805069704106,
                  "rejected_mean_error": 3.7242586726234075,
                  "gap_rejected_minus_accepted": 2.165478165652997
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4102455973625183,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2283701810836791,
                  "rejected_mean_error": 2.9805918283462525,
                  "gap_rejected_minus_accepted": 1.7522216472625733
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7760757356882095,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8887838655047946,
                  "rejected_mean_error": 2.5140474205986063,
                  "gap_rejected_minus_accepted": 1.6252635550938117
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9765799015640899,
              "spearman": 0.967462268324936,
              "auroc_top30_bad": 0.9676685714285713,
              "mae": 0.43678177344816466,
              "mse": 0.248376606099711,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6346676034883469,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1213003026843071
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2029856227874756
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6328393008589744
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0458026138544083
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9801258551852388,
              "spearman": 0.9666741976794867,
              "auroc_top30_worst": 0.960128,
              "pairwise_seed_ranking": 0.8724,
              "predicted_best_mean_error": 1.5884340679645539,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06870907449722274,
              "gap_to_oracle": 0.008536546468734807,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.42347283697128296
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6592864739971284
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.036277892780304
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.312847211353306
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1726089000701907,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4608076492415534,
                  "rejected_mean_error": 3.322495864868164,
                  "gap_rejected_minus_accepted": 1.8616882156266108
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5078479647636414,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3120020722757664,
                  "rejected_mean_error": 2.6497592548973645,
                  "gap_rejected_minus_accepted": 1.3377571826215982
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1846486330032349,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.036277892780304,
                  "rejected_mean_error": 2.257675048828125,
                  "gap_rejected_minus_accepted": 1.221397156047821
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.615500345826149,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6607486933184127,
                  "rejected_mean_error": 1.9764207550657469,
                  "gap_rejected_minus_accepted": 1.315672061747334
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3320054054260253,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4650840894381205,
                  "rejected_mean_error": 3.3856746196746825,
                  "gap_rejected_minus_accepted": 1.920590530236562
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5132294297218323,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.305562773171593,
                  "rejected_mean_error": 2.70072296876756,
                  "gap_rejected_minus_accepted": 1.3951601955959667
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2087176442146301,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.026511351108551,
                  "rejected_mean_error": 2.2877749338150024,
                  "gap_rejected_minus_accepted": 1.2612635827064513
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6017308086156845,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6496417484586201,
                  "rejected_mean_error": 1.9965687457890433,
                  "gap_rejected_minus_accepted": 1.3469269973304232
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9762854974309227,
              "spearman": 0.9704144986110095,
              "auroc_top30_bad": 0.9764853333333332,
              "mae": 0.41854856700121434,
              "mse": 0.2167830723695409,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6039092893728855,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11127009296417237
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2326864322423935
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.787743054485321
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1389568073908487
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9563255146447557,
              "spearman": 0.95726318724044,
              "auroc_top30_worst": 0.9689539047619048,
              "pairwise_seed_ranking": 0.8812,
              "predicted_best_mean_error": 1.598592980146408,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06315814781188966,
              "gap_to_oracle": 0.0065690481662750155,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8669385330677033
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.109075569667113
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3626301781177521
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5171157310067465
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6222390413284302,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5926963810655805,
                  "rejected_mean_error": 2.263865538597107,
                  "gap_rejected_minus_accepted": 0.6711691575315264
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4709127843379974,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5166334559149015,
                  "rejected_mean_error": 2.0884379323679036,
                  "gap_rejected_minus_accepted": 0.5718044764530021
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2705997228622437,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3626301781177521,
                  "rejected_mean_error": 1.9569964155197144,
                  "gap_rejected_minus_accepted": 0.5943662374019623
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9238283932209015,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1102559700751076,
                  "rejected_mean_error": 1.8433900772571055,
                  "gap_rejected_minus_accepted": 0.7331341071819979
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.635522150993347,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5986509283383687,
                  "rejected_mean_error": 2.2296529245376586,
                  "gap_rejected_minus_accepted": 0.6310019961992899
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4614683985710144,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5248385562616236,
                  "rejected_mean_error": 2.0681424122008067,
                  "gap_rejected_minus_accepted": 0.5433038559391832
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2889179587364197,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3742926735877992,
                  "rejected_mean_error": 1.9492095823287965,
                  "gap_rejected_minus_accepted": 0.5749169087409973
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9240861237049103,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1219295045686146,
                  "rejected_mean_error": 1.8436161668542872,
                  "gap_rejected_minus_accepted": 0.7216866622856726
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
        "best_epoch": 5,
        "best_calib_loss": 0.06928277760744095,
        "train_time_sec": 36.70528221130371,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9912081003869839,
              "spearman": 0.9890633322535349,
              "auroc_top30_bad": 0.9968783095238094,
              "mae": 0.11411048949019369,
              "mse": 0.028045894674929656,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6964049634150693,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.31783996629714967
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.23896787252426147
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.12751887773275375
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.4790936002254486
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8960445861935615
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9990379176199906,
              "spearman": 0.9976037391520347,
              "auroc_top30_worst": 0.99936,
              "pairwise_seed_ranking": 0.8668,
              "predicted_best_mean_error": 1.1934240526258946,
              "seed0_mean_error": 1.273960811495781,
              "random_seed_mean_error": 1.2650585584044456,
              "oracle_best_mean_error": 1.185694094002247,
              "improvement_over_seed0": 0.08053675886988643,
              "gap_to_oracle": 0.00772995862364767,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.21763486221432685
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.36047175899744033
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5714240451157093
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7892601723710696
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635830781012773
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7136736869812017,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.971539024197393,
                  "rejected_mean_error": 3.8919795632362364,
                  "gap_rejected_minus_accepted": 2.9204405390388435
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5364013612270355,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7892601723710696,
                  "rejected_mean_error": 2.6865517952919005,
                  "gap_rejected_minus_accepted": 1.897291622920831
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.012853980064392,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5714240451157093,
                  "rejected_mean_error": 1.9557421110868454,
                  "gap_rejected_minus_accepted": 1.384318065971136
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5631366521120071,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.36047175899744033,
                  "rejected_mean_error": 1.5646201844692231,
                  "gap_rejected_minus_accepted": 1.2041484254717827
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.789891982078552,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9743760295708974,
                  "rejected_mean_error": 3.9702238488197326,
                  "gap_rejected_minus_accepted": 2.9958478192488354
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.548413097858429,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7870049432118734,
                  "rejected_mean_error": 2.734828416347504,
                  "gap_rejected_minus_accepted": 1.9478234731356303
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0001629292964935,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5664474643468856,
                  "rejected_mean_error": 1.9814741586446762,
                  "gap_rejected_minus_accepted": 1.4150266942977905
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5528766512870789,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.35494975972175596,
                  "rejected_mean_error": 1.5802978287537892,
                  "gap_rejected_minus_accepted": 1.2253480690320333
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9776403615166329,
              "spearman": 0.967338420324658,
              "auroc_top30_bad": 0.9834209523809524,
              "mae": 0.3869322507969906,
              "mse": 0.2016035643817399,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8120162694770718,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15380076479911803
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22508106036186218
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5902190551400185
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0252441588481267
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9840629093736801,
              "spearman": 0.9785625135120087,
              "auroc_top30_worst": 0.9944655238095238,
              "pairwise_seed_ranking": 0.87,
              "predicted_best_mean_error": 1.997721669793129,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10675933492183698,
              "gap_to_oracle": 0.0088264400959015,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.650185478925705
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8855322246941236
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.241353343153
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.549122419025598
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.7364693880081177,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.843955996274948,
                  "rejected_mean_error": 4.203379270553589,
                  "gap_rejected_minus_accepted": 2.359423274278641
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.473044514656067,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.547852757996149,
                  "rejected_mean_error": 3.6726353686457625,
                  "gap_rejected_minus_accepted": 2.1247826106496133
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.349701166152954,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.241353343153,
                  "rejected_mean_error": 2.9184433042526243,
                  "gap_rejected_minus_accepted": 1.6770899610996244
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7884197384119034,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.887657104875333,
                  "rejected_mean_error": 2.4781603316996117,
                  "gap_rejected_minus_accepted": 1.5905032268242787
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.814535713195801,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8669701374901666,
                  "rejected_mean_error": 4.242078809738159,
                  "gap_rejected_minus_accepted": 2.375108672247993
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.5501421689987183,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.555433442885863,
                  "rejected_mean_error": 3.7341936088743664,
                  "gap_rejected_minus_accepted": 2.1787601659885034
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3759230375289917,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.240974419593811,
                  "rejected_mean_error": 2.9679875898361208,
                  "gap_rejected_minus_accepted": 1.7270131702423097
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7982305884361267,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8842713567945693,
                  "rejected_mean_error": 2.5155676775437623,
                  "gap_rejected_minus_accepted": 1.631296320749193
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9735059124026688,
              "spearman": 0.9629572109588957,
              "auroc_top30_bad": 0.9606948571428572,
              "mae": 0.41507273421634966,
              "mse": 0.23097540420310742,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6398956638934424,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09773961859941482
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20976549649238588
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6337555772185326
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0491478194157282
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9770378778571938,
              "spearman": 0.9623104004546563,
              "auroc_top30_worst": 0.948431238095238,
              "pairwise_seed_ranking": 0.862,
              "predicted_best_mean_error": 1.5892828896045685,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06786025285720809,
              "gap_to_oracle": 0.009385368108749459,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4132272112369537
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6549234854487272
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0361675267219543
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3159532869167165
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.110506343841553,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4608887439833746,
                  "rejected_mean_error": 3.3217660121917723,
                  "gap_rejected_minus_accepted": 1.8608772682083976
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5529625415802002,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3153327550170515,
                  "rejected_mean_error": 2.639788488991344,
                  "gap_rejected_minus_accepted": 1.3244557339742926
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2299203872680664,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0361675267219543,
                  "rejected_mean_error": 2.2577854148864747,
                  "gap_rejected_minus_accepted": 1.2216178881645203
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6659564077854156,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6562032179710583,
                  "rejected_mean_error": 1.9779391475777235,
                  "gap_rejected_minus_accepted": 1.3217359296066653
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.207724618911743,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.466823774708642,
                  "rejected_mean_error": 3.37001745223999,
                  "gap_rejected_minus_accepted": 1.9031936775313483
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5747893452644348,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3107312908147108,
                  "rejected_mean_error": 2.685381495763385,
                  "gap_rejected_minus_accepted": 1.3746502049486742
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2604598999023438,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.027425904750824,
                  "rejected_mean_error": 2.2868603801727296,
                  "gap_rejected_minus_accepted": 1.2594344754219056
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6375681459903717,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6422175348751129,
                  "rejected_mean_error": 1.999069951434824,
                  "gap_rejected_minus_accepted": 1.3568524165597111
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9636933370453763,
              "spearman": 0.9500812346139764,
              "auroc_top30_bad": 0.9491634285714287,
              "mae": 0.39701624380127976,
              "mse": 0.20356755532532445,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6082364624382939,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11423812681436539
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24193712742328644
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7922699146270752
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1474093022028604
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8927018011569119,
              "spearman": 0.8736338688216762,
              "auroc_top30_worst": 0.8935070476190478,
              "pairwise_seed_ranking": 0.7948,
              "predicted_best_mean_error": 1.6026350551843642,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.05911607277393349,
              "gap_to_oracle": 0.010611123204231188,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8694133508205414
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1252159366431909
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3712240015506745
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5383283492408073
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6362360358238222,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.613702770365609,
                  "rejected_mean_error": 2.0748080348968507,
                  "gap_rejected_minus_accepted": 0.4611052645312417
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4565942585468292,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5380027757573917,
                  "rejected_mean_error": 2.0244665180151453,
                  "gap_rejected_minus_accepted": 0.4864637422577536
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2998751997947693,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3712240015506745,
                  "rejected_mean_error": 1.948402592086792,
                  "gap_rejected_minus_accepted": 0.5771785905361175
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9126502722501755,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.12634477038353,
                  "rejected_mean_error": 1.8380156967912182,
                  "gap_rejected_minus_accepted": 0.7116709264076881
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.673127794265747,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6156351108021205,
                  "rejected_mean_error": 2.0767952823638915,
                  "gap_rejected_minus_accepted": 0.461160171561771
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4511238038539886,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5425323582588033,
                  "rejected_mean_error": 2.015622714209178,
                  "gap_rejected_minus_accepted": 0.47309035595037474
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3104658126831055,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3802930836677552,
                  "rejected_mean_error": 1.9432091722488403,
                  "gap_rejected_minus_accepted": 0.5629160885810851
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9148916453123093,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1332659068561735,
                  "rejected_mean_error": 1.8397969511103502,
                  "gap_rejected_minus_accepted": 0.7065310442541768
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
        "best_epoch": 69,
        "best_calib_loss": 0.09276588261127472,
        "train_time_sec": 14.22796893119812,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9238402460207257,
              "spearman": 0.8475660024734918,
              "auroc_top30_bad": 0.9089642142857143,
              "mae": 0.17527162368930876,
              "mse": 0.1692110651563311,
              "expert_lt_perturb_large": 0.99,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.981,
              "same_context_pred_std": 0.780968857492803,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4648383450470865
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5050999551862478
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6778830668874085
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9722130785082778
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3764220615681262
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9986167805622298,
              "spearman": 0.9978376551374543,
              "auroc_top30_worst": 0.9990241904761905,
              "pairwise_seed_ranking": 0.8674,
              "predicted_best_mean_error": 1.7011015480160714,
              "seed0_mean_error": 1.783668221414089,
              "random_seed_mean_error": 1.7754869311451913,
              "oracle_best_mean_error": 1.695319577306509,
              "improvement_over_seed0": 0.08256667339801771,
              "gap_to_oracle": 0.005781970709562323,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7088982949256897
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8584189093112946
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0693607777833938
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.293376477575302
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7739667998433113
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1775281906127932,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4779537852737639,
                  "rejected_mean_error": 4.438083930969238,
                  "gap_rejected_minus_accepted": 2.9601301456954747
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.027900755405426,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.293376477575302,
                  "rejected_mean_error": 3.215737766647339,
                  "gap_rejected_minus_accepted": 1.9223612890720367
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.478328287601471,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0693607777833938,
                  "rejected_mean_error": 2.478572821903229,
                  "gap_rejected_minus_accepted": 1.409212044119835
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.053936928510666,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8584189093112946,
                  "rejected_mean_error": 2.0791494300206503,
                  "gap_rejected_minus_accepted": 1.2207305207093557
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2412573575973513,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.480239007141855,
                  "rejected_mean_error": 4.5145311498641965,
                  "gap_rejected_minus_accepted": 3.0342921427223413
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0412715673446655,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2912341789404551,
                  "rejected_mean_error": 3.2609703488349915,
                  "gap_rejected_minus_accepted": 1.9697361698945364
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.46780925989151,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0643228293657303,
                  "rejected_mean_error": 2.503013613462448,
                  "gap_rejected_minus_accepted": 1.4386907840967178
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0630043148994446,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8504447996616363,
                  "rejected_mean_error": 2.0947426953315733,
                  "gap_rejected_minus_accepted": 1.2442978956699369
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8168241866618842,
              "spearman": 0.7162319613188821,
              "auroc_top30_bad": 0.7810003809523809,
              "mae": 0.4725831599712372,
              "mse": 0.4977406763651144,
              "expert_lt_perturb_large": 0.984,
              "expert_lt_other_task": 0.476,
              "expert_lt_simvla_seed0": 0.944,
              "same_context_pred_std": 0.9232881904791781,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46258365988731387
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6865947505950928
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.800701108622551
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.117064287161827
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8243187523972617,
              "spearman": 0.7431310965319019,
              "auroc_top30_worst": 0.848792380952381,
              "pairwise_seed_ranking": 0.7656,
              "predicted_best_mean_error": 2.0099232429265976,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.09455776178836839,
              "gap_to_oracle": 0.02102801322937009,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1548596177101136
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2596890318852205
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.466672075176239
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.61946134218402
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.325383186340333,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8432175122102101,
                  "rejected_mean_error": 4.210025627136231,
                  "gap_rejected_minus_accepted": 2.3668081149260205
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.756624460220337,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6189313013436573,
                  "rejected_mean_error": 3.4598539145990683,
                  "gap_rejected_minus_accepted": 1.840922613255411
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8057512640953064,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.466672075176239,
                  "rejected_mean_error": 2.6931245722293853,
                  "gap_rejected_minus_accepted": 1.2264524970531463
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.249421238899231,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2601308289427346,
                  "rejected_mean_error": 2.3537374121338734,
                  "gap_rejected_minus_accepted": 1.0936065831911388
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.333545112609864,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8661083624098036,
                  "rejected_mean_error": 4.249834785461426,
                  "gap_rejected_minus_accepted": 2.383726423051622
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.814423680305481,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6391346703238665,
                  "rejected_mean_error": 3.485747108383784,
                  "gap_rejected_minus_accepted": 1.8466124380599176
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.851257562637329,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4798987522125244,
                  "rejected_mean_error": 2.7290632572174074,
                  "gap_rejected_minus_accepted": 1.249164505004883
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2533771693706512,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.213657412737135,
                  "rejected_mean_error": 2.40459804372354,
                  "gap_rejected_minus_accepted": 1.190940630986405
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6388738561715129,
              "spearman": 0.5346469320873237,
              "auroc_top30_bad": 0.6550156190476191,
              "mae": 0.5072511795759201,
              "mse": 0.6457311517637945,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.6816025501425348,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6099343497753144
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8846876668214798
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9099253840446472
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1306247113466263
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.859305201854992,
              "spearman": 0.7867676003632643,
              "auroc_top30_worst": 0.8431664761904761,
              "pairwise_seed_ranking": 0.7964,
              "predicted_best_mean_error": 1.5977734017372132,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.05936974072456347,
              "gap_to_oracle": 0.017875880241394082,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4347736620903015
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8417463881465105
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1373452689170838
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3566638744080752
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.243636274337769,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4862849171426562,
                  "rejected_mean_error": 3.09320045375824,
                  "gap_rejected_minus_accepted": 1.6069155366155836
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7850430607795715,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3560500892402014,
                  "rejected_mean_error": 2.5178966609814677,
                  "gap_rejected_minus_accepted": 1.1618465717412663
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4420340061187744,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1373452689170838,
                  "rejected_mean_error": 2.156607672691345,
                  "gap_rejected_minus_accepted": 1.0192624037742612
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.993706002831459,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8410581706430965,
                  "rejected_mean_error": 1.9161893074642251,
                  "gap_rejected_minus_accepted": 1.0751311368211285
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3397722482681274,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4862745711538528,
                  "rejected_mean_error": 3.194960284233093,
                  "gap_rejected_minus_accepted": 1.7086857130792403
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8078815340995789,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.348790076008455,
                  "rejected_mean_error": 2.5724133555851285,
                  "gap_rejected_minus_accepted": 1.2236232795766735
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.466062843799591,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1153779187202453,
                  "rejected_mean_error": 2.198908366203308,
                  "gap_rejected_minus_accepted": 1.0835304474830627
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9827220588922501,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8093950729521494,
                  "rejected_mean_error": 1.9427481070559292,
                  "gap_rejected_minus_accepted": 1.1333530341037799
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5004114348420394,
              "spearman": 0.3709471128117992,
              "auroc_top30_bad": 0.5624590476190476,
              "mae": 0.4910370707392693,
              "mse": 0.6682306824786384,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6359578505876508,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.223851168870926
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.083698788714409
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0350885803699494
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.254775119781494
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7029973486535728,
              "spearman": 0.5929439924121552,
              "auroc_top30_worst": 0.7264975238095237,
              "pairwise_seed_ranking": 0.75,
              "predicted_best_mean_error": 1.611858060002327,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.049893067955970816,
              "gap_to_oracle": 0.019834128022193864,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9052777855396271
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2528699243871064
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4706575397968291
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5784445416762123
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8745428442955017,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6261578180789948,
                  "rejected_mean_error": 1.9627126054763795,
                  "gap_rejected_minus_accepted": 0.33655478739738465
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7573227286338806,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5783194624436194,
                  "rejected_mean_error": 1.9037740725678758,
                  "gap_rejected_minus_accepted": 0.32545461012425636
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.501870572566986,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4706575397968291,
                  "rejected_mean_error": 1.8489690538406371,
                  "gap_rejected_minus_accepted": 0.37831151404380803
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2955001890659332,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2534028406912527,
                  "rejected_mean_error": 1.7955726060694284,
                  "gap_rejected_minus_accepted": 0.5421697653781756
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8741137981414795,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.626321524779002,
                  "rejected_mean_error": 1.9806175565719604,
                  "gap_rejected_minus_accepted": 0.35429603179295843
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7664869725704193,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5755712198701135,
                  "rejected_mean_error": 1.917554982124813,
                  "gap_rejected_minus_accepted": 0.3419837622546995
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5259627103805542,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4643340125083923,
                  "rejected_mean_error": 1.859168243408203,
                  "gap_rejected_minus_accepted": 0.39483423089981073
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2933232486248016,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.265833628556085,
                  "rejected_mean_error": 1.7951350983451395,
                  "gap_rejected_minus_accepted": 0.5293014697890546
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
        "best_epoch": 56,
        "best_calib_loss": 0.015435861423611641,
        "train_time_sec": 38.053771018981934,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.999632946691129,
              "spearman": 0.999077318626867,
              "auroc_top30_bad": 0.9996938571428571,
              "mae": 0.02303605616223067,
              "mse": 0.0009860110063362217,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.986,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7668682620643271,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09393220066651702
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2356476287469268
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5951973806016148
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9484513294771314
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3764220615681262
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997214305491251,
              "spearman": 0.999502024220057,
              "auroc_top30_worst": 0.9998251428571429,
              "pairwise_seed_ranking": 0.946,
              "predicted_best_mean_error": 1.6967905976176263,
              "seed0_mean_error": 1.783668221414089,
              "random_seed_mean_error": 1.7754869311451913,
              "oracle_best_mean_error": 1.695319577306509,
              "improvement_over_seed0": 0.0868776237964628,
              "gap_to_oracle": 0.0014710203111172326,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.705251432299614
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8573685177326202
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.069001440691948
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.292882102282842
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7739667998433113
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.125185656547548,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4777102910810047,
                  "rejected_mean_error": 4.440275378704071,
                  "gap_rejected_minus_accepted": 2.9625650876230667
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0317054986953735,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.292882102282842,
                  "rejected_mean_error": 3.217220892524719,
                  "gap_rejected_minus_accepted": 1.9243387902418772
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5083985924720764,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.069001440691948,
                  "rejected_mean_error": 2.4789321589946747,
                  "gap_rejected_minus_accepted": 1.4099307183027268
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.065043717622757,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8573685177326202,
                  "rejected_mean_error": 2.079499560546875,
                  "gap_rejected_minus_accepted": 1.2221310428142547
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1879928588867195,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4798177313142353,
                  "rejected_mean_error": 4.518322632312775,
                  "gap_rejected_minus_accepted": 3.0385049009985394
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.034630000591278,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.290641145626704,
                  "rejected_mean_error": 3.262749448776245,
                  "gap_rejected_minus_accepted": 1.972108303149541
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5081525444984436,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0638317371606827,
                  "rejected_mean_error": 2.503504705667496,
                  "gap_rejected_minus_accepted": 1.4396729685068133
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0625878870487213,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8494812314510345,
                  "rejected_mean_error": 2.0950638847351075,
                  "gap_rejected_minus_accepted": 1.245582653284073
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.987501011224873,
              "spearman": 0.9780794361867958,
              "auroc_top30_bad": 0.9808952380952382,
              "mae": 0.13659029314890503,
              "mse": 0.03529023223797053,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.916519921665068,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09728514057397843
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20333380784988403
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.589540679705143
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0245867340485255
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9913919854339449,
              "spearman": 0.9926389856249508,
              "auroc_top30_worst": 0.997991619047619,
              "pairwise_seed_ranking": 0.9136,
              "predicted_best_mean_error": 1.9956653254032135,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10881567931175251,
              "gap_to_oracle": 0.006770095705985968,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6254508793354034
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8679778013282862
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2241252389430999
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.55240877690727
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.24638261795044,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8424638948175642,
                  "rejected_mean_error": 4.216808183670044,
                  "gap_rejected_minus_accepted": 2.3743442888524795
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8837682008743286,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5513114497590346,
                  "rejected_mean_error": 3.6622813936239615,
                  "gap_rejected_minus_accepted": 2.110969943864927
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8594610095024109,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2241252389430999,
                  "rejected_mean_error": 2.9356714084625244,
                  "gap_rejected_minus_accepted": 1.7115461695194245
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2688082158565521,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8692872009147852,
                  "rejected_mean_error": 2.4842967030332845,
                  "gap_rejected_minus_accepted": 1.6150095021184994
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.31935830116272,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8663532808091905,
                  "rejected_mean_error": 4.247630519866943,
                  "gap_rejected_minus_accepted": 2.381277239057753
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9588778018951416,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5588921289392972,
                  "rejected_mean_error": 3.7239273502713157,
                  "gap_rejected_minus_accepted": 2.1650352213320185
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8926371335983276,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.222396728515625,
                  "rejected_mean_error": 2.9865652809143066,
                  "gap_rejected_minus_accepted": 1.7641685523986816
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3254468441009521,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8703209104992095,
                  "rejected_mean_error": 2.5202675605202742,
                  "gap_rejected_minus_accepted": 1.6499466500210649
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9675154055723214,
              "spearman": 0.9505988646355046,
              "auroc_top30_bad": 0.9446148571428572,
              "mae": 0.15769989220164715,
              "mse": 0.05634448253951624,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7185251502124366,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08243123370409011
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21343729519844054
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6522568423628807
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0573374668359756
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.988691235849912,
              "spearman": 0.9875430873235759,
              "auroc_top30_worst": 0.9789744761904762,
              "pairwise_seed_ranking": 0.884,
              "predicted_best_mean_error": 1.5901769310235978,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06696621143817882,
              "gap_to_oracle": 0.010279409527778727,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4160859177112579
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6532195647939657
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0240917805671692
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3079034067801576
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7660692930221558,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.459478561030494,
                  "rejected_mean_error": 3.3344576587677004,
                  "gap_rejected_minus_accepted": 1.8749790977372065
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1049344539642334,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3070775198580233,
                  "rejected_mean_error": 2.6645014453619815,
                  "gap_rejected_minus_accepted": 1.3574239255039582
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7079696655273438,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0240917805671692,
                  "rejected_mean_error": 2.2698611610412596,
                  "gap_rejected_minus_accepted": 1.2457693804740904
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0921249389648438,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6545021189287448,
                  "rejected_mean_error": 1.97850739090776,
                  "gap_rejected_minus_accepted": 1.3240052719790152
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8602222442626952,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4644031617376538,
                  "rejected_mean_error": 3.391802968978882,
                  "gap_rejected_minus_accepted": 1.927399807241228
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.126383662223816,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3045784882045686,
                  "rejected_mean_error": 2.7036445765268233,
                  "gap_rejected_minus_accepted": 1.3990660883222548
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7119447588920593,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.013696539402008,
                  "rejected_mean_error": 2.3005897455215454,
                  "gap_rejected_minus_accepted": 1.2868932061195373
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0929123163223267,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.641842334043412,
                  "rejected_mean_error": 1.9991963559930974,
                  "gap_rejected_minus_accepted": 1.3573540219496856
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.974907538333786,
              "spearman": 0.961313439623728,
              "auroc_top30_bad": 0.9628266666666665,
              "mae": 0.13122610670626164,
              "mse": 0.03486393744378197,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6719087124782136,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08742320358753204
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23025442028045653
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7911530882835388
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.145103710492452
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9621525369219861,
              "spearman": 0.9493632837387237,
              "auroc_top30_worst": 0.9553401904761905,
              "pairwise_seed_ranking": 0.9056,
              "predicted_best_mean_error": 1.5958923324346543,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06585879552364338,
              "gap_to_oracle": 0.0038684004545213035,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8451749470233917
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1046930995698159
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3604247936725617
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5221544955648594
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0546612024307254,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5995762278503842,
                  "rejected_mean_error": 2.2019469175338746,
                  "gap_rejected_minus_accepted": 0.6023706896834904
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.917053759098053,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5216600960130497,
                  "rejected_mean_error": 2.073390131179517,
                  "gap_rejected_minus_accepted": 0.5517300351664671
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7778655290603638,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3604247936725617,
                  "rejected_mean_error": 1.9592017999649047,
                  "gap_rejected_minus_accepted": 0.598777006292343
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4367331862449646,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.105464577770081,
                  "rejected_mean_error": 1.8449906170559032,
                  "gap_rejected_minus_accepted": 0.7395260392858223
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0461419343948366,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6009258421262105,
                  "rejected_mean_error": 2.2091787004470826,
                  "gap_rejected_minus_accepted": 0.6082528583208722
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.906057983636856,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5311037961811942,
                  "rejected_mean_error": 2.0495455889474776,
                  "gap_rejected_minus_accepted": 0.5184417927662834
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8077572584152222,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3711420130729675,
                  "rejected_mean_error": 1.952360242843628,
                  "gap_rejected_minus_accepted": 0.5812182297706605
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4501698315143585,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1135321202732267,
                  "rejected_mean_error": 1.8464452321516638,
                  "gap_rejected_minus_accepted": 0.7329131118784371
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
        "best_epoch": 55,
        "best_calib_loss": 0.01527845486998558,
        "train_time_sec": 59.820505142211914,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9991175171563419,
              "spearman": 0.9979600382677092,
              "auroc_top30_bad": 0.9991088095238094,
              "mae": 0.03606176294349134,
              "mse": 0.0023351524585041856,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.982,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7821072522039988,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0942080162577331
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23613712020963432
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5955722042910755
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.948845460279286
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3764220615681262
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9993306432336111,
              "spearman": 0.9984553692501404,
              "auroc_top30_worst": 0.9996186666666667,
              "pairwise_seed_ranking": 0.9507,
              "predicted_best_mean_error": 1.6970375236868858,
              "seed0_mean_error": 1.783668221414089,
              "random_seed_mean_error": 1.7754869311451913,
              "oracle_best_mean_error": 1.695319577306509,
              "improvement_over_seed0": 0.08663069772720333,
              "gap_to_oracle": 0.0017179463803767003,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7079529445171356
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8582610558032989
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0693916753053665
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2929893711884817
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7739667998433113
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.180539274215698,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4777596275144154,
                  "rejected_mean_error": 4.4398313508033755,
                  "gap_rejected_minus_accepted": 2.96207172328896
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0550257563591003,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2929893711884817,
                  "rejected_mean_error": 3.2168990858078,
                  "gap_rejected_minus_accepted": 1.9239097146193185
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5043940544128418,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0693916753053665,
                  "rejected_mean_error": 2.4785419243812563,
                  "gap_rejected_minus_accepted": 1.4091502490758898
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0716425776481628,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8582610558032989,
                  "rejected_mean_error": 2.079202047856649,
                  "gap_rejected_minus_accepted": 1.2209409920533498
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2817734479904175,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.480077878302998,
                  "rejected_mean_error": 4.51598130941391,
                  "gap_rejected_minus_accepted": 3.0359034311109117
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.056571364402771,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2908344473044078,
                  "rejected_mean_error": 3.2621695437431337,
                  "gap_rejected_minus_accepted": 1.971335096438726
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4953376054763794,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0642544745206832,
                  "rejected_mean_error": 2.503081968307495,
                  "gap_rejected_minus_accepted": 1.4388274937868117
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0695398151874542,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8505066096782684,
                  "rejected_mean_error": 2.094722091992696,
                  "gap_rejected_minus_accepted": 1.2442154823144276
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9868596148071945,
              "spearman": 0.9765446106193015,
              "auroc_top30_bad": 0.985295238095238,
              "mae": 0.14237445386704056,
              "mse": 0.036027708687082216,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8721651100353983,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11976954561471939
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21740448639392854
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5903103307366371
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0201123913844425
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9951579883015869,
              "spearman": 0.9940647816094602,
              "auroc_top30_worst": 0.9994940952380952,
              "pairwise_seed_ranking": 0.912,
              "predicted_best_mean_error": 1.9946650965213775,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10981590819358855,
              "gap_to_oracle": 0.005769866824149927,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6245760567188263
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8737878622725989
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2211037875652313
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5491064538770138
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.12243790626526,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8418510081768036,
                  "rejected_mean_error": 4.222324163436889,
                  "gap_rejected_minus_accepted": 2.380473155260086
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8248817324638367,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.547908472881246,
                  "rejected_mean_error": 3.6724685799961274,
                  "gap_rejected_minus_accepted": 2.124560107114881
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7557513117790222,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2211037875652313,
                  "rejected_mean_error": 2.938692859840393,
                  "gap_rejected_minus_accepted": 1.7175890722751619
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2009328305721283,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8757271259166182,
                  "rejected_mean_error": 2.482145479420079,
                  "gap_rejected_minus_accepted": 1.6064183535034606
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.24383282661438,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8655182372199164,
                  "rejected_mean_error": 4.25514591217041,
                  "gap_rejected_minus_accepted": 2.3896276749504937
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.878537654876709,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5549441582378856,
                  "rejected_mean_error": 3.7356459299723306,
                  "gap_rejected_minus_accepted": 2.1807017717344452
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7712903022766113,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2212422533035279,
                  "rejected_mean_error": 2.987719756126404,
                  "gap_rejected_minus_accepted": 1.766477502822876
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2009328305721283,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8731783041878353,
                  "rejected_mean_error": 2.5193049091706303,
                  "gap_rejected_minus_accepted": 1.6461266049827952
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9658785058900254,
              "spearman": 0.9461163155538685,
              "auroc_top30_bad": 0.9357577142857143,
              "mae": 0.17500440849140286,
              "mse": 0.0653876968681075,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6874894620609866,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07642959523200989
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2038411575317383
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.653505398118496
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0590085217396419
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.986612907525156,
              "spearman": 0.9755284016181771,
              "auroc_top30_worst": 0.9654979047619048,
              "pairwise_seed_ranking": 0.8752,
              "predicted_best_mean_error": 1.5887052093744278,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.0684379330873488,
              "gap_to_oracle": 0.00880768787860875,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4064526147842407
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.656894690142228
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0301856196403503
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3131874738090328
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5107969760894777,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.459059784412384,
                  "rejected_mean_error": 3.3382266483306884,
                  "gap_rejected_minus_accepted": 1.8791668639183043
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0075520277023315,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3122358794782307,
                  "rejected_mean_error": 2.649059327265706,
                  "gap_rejected_minus_accepted": 1.3368234477874752
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6523823738098145,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0301856196403503,
                  "rejected_mean_error": 2.2637673219680785,
                  "gap_rejected_minus_accepted": 1.2335817023277282
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9905408769845963,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.658245573219019,
                  "rejected_mean_error": 1.9772569093785648,
                  "gap_rejected_minus_accepted": 1.3190113361595457
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6325599431991575,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4650840894381205,
                  "rejected_mean_error": 3.3856746196746825,
                  "gap_rejected_minus_accepted": 1.920590530236562
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.008526921272278,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3053798187862744,
                  "rejected_mean_error": 2.7012660238477917,
                  "gap_rejected_minus_accepted": 1.3958862050615173
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6512030363082886,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.019579782962799,
                  "rejected_mean_error": 2.2947065019607544,
                  "gap_rejected_minus_accepted": 1.2751267189979554
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9917253404855728,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6463249439284915,
                  "rejected_mean_error": 1.997686171914167,
                  "gap_rejected_minus_accepted": 1.3513612279856755
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9703189047231976,
              "spearman": 0.9609129544133005,
              "auroc_top30_bad": 0.965423238095238,
              "mae": 0.13928369381763042,
              "mse": 0.039776234640660345,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6644276252071191,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09718979108333588
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23661425828933716
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7927923590660095
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1459534392038981
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9671161670650252,
              "spearman": 0.9634441289242426,
              "auroc_top30_worst": 0.9683200000000001,
              "pairwise_seed_ranking": 0.892,
              "predicted_best_mean_error": 1.5972716072797775,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06447952067852025,
              "gap_to_oracle": 0.005247675299644428,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8488761584758758
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1041662556429703
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3598632776737214
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5189596727522197
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.115014982223511,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5925308700402578,
                  "rejected_mean_error": 2.2653551378250123,
                  "gap_rejected_minus_accepted": 0.6728242677847545
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.936521828174591,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5184538569559791,
                  "rejected_mean_error": 2.0829883612002047,
                  "gap_rejected_minus_accepted": 0.5645345042442256
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7390196323394775,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3598632776737214,
                  "rejected_mean_error": 1.959763315963745,
                  "gap_rejected_minus_accepted": 0.5999000382900237
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.337907314300537,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1050825588428936,
                  "rejected_mean_error": 1.8451182285011642,
                  "gap_rejected_minus_accepted": 0.7400356696582706
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.131964325904846,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5986642861366271,
                  "rejected_mean_error": 2.2295327043533324,
                  "gap_rejected_minus_accepted": 0.6308684182167053
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9211075901985168,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.52790957179299,
                  "rejected_mean_error": 2.0590268581632585,
                  "gap_rejected_minus_accepted": 0.5311172863702684
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7548059225082397,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3678767809867858,
                  "rejected_mean_error": 1.9556254749298096,
                  "gap_rejected_minus_accepted": 0.5877486939430239
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.343763530254364,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1155815625947618,
                  "rejected_mean_error": 1.845754778321414,
                  "gap_rejected_minus_accepted": 0.7301732157266523
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
        "best_epoch": 59,
        "best_calib_loss": 0.01690160669386387,
        "train_time_sec": 43.00731348991394,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993663342306023,
              "spearman": 0.9981314975777884,
              "auroc_top30_bad": 0.9995230238095237,
              "mae": 0.03048786818385124,
              "mse": 0.00179916305309198,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.997,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7900056684711357,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09900215369835495
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23587339804023505
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5951521808974445
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9485839234903455
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3764220615681262
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997362388464508,
              "spearman": 0.9994250718409889,
              "auroc_top30_worst": 0.9997043809523809,
              "pairwise_seed_ranking": 0.9507,
              "predicted_best_mean_error": 1.696316385537386,
              "seed0_mean_error": 1.783668221414089,
              "random_seed_mean_error": 1.7754869311451913,
              "oracle_best_mean_error": 1.695319577306509,
              "improvement_over_seed0": 0.08735183587670314,
              "gap_to_oracle": 0.0009968082308768889,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7054569649696351
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.857263285112381
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0690365807771682
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2928568553447723
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7739667998433113
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.158470582962038,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4777213114235137,
                  "rejected_mean_error": 4.440176195621491,
                  "gap_rejected_minus_accepted": 2.962454884197977
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0469987988471985,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2928568553447723,
                  "rejected_mean_error": 3.217296633338928,
                  "gap_rejected_minus_accepted": 1.9244397779941558
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5118755102157593,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0690365807771682,
                  "rejected_mean_error": 2.4788970189094544,
                  "gap_rejected_minus_accepted": 1.4098604381322861
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0766547918319702,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.857263285112381,
                  "rejected_mean_error": 2.0795346380869546,
                  "gap_rejected_minus_accepted": 1.2222713529745737
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.232512664794922,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4798177313142353,
                  "rejected_mean_error": 4.518322632312775,
                  "gap_rejected_minus_accepted": 3.0385049009985394
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.047125816345215,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2906937113602956,
                  "rejected_mean_error": 3.26259175157547,
                  "gap_rejected_minus_accepted": 1.9718980402151742
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5092949867248535,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.064074715256691,
                  "rejected_mean_error": 2.5032617275714872,
                  "gap_rejected_minus_accepted": 1.4391870123147963
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0717917382717133,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.849390900850296,
                  "rejected_mean_error": 2.0950939949353535,
                  "gap_rejected_minus_accepted": 1.2457030940850575
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9859959239642571,
              "spearman": 0.9738116417110299,
              "auroc_top30_bad": 0.9774491428571429,
              "mae": 0.14537048455625773,
              "mse": 0.03953295158034454,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8759923671124993,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11316873967647552
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21536386971473695
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5919959290146828
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0241869109233221
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9919426370324118,
              "spearman": 0.9869709883974327,
              "auroc_top30_worst": 0.9993081904761905,
              "pairwise_seed_ranking": 0.9176,
              "predicted_best_mean_error": 1.9945398499965667,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10994115471839927,
              "gap_to_oracle": 0.005644620299339209,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6366544711589813
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8767353597168739
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2319081079006196
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.54804302694828
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.112228202819824,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8424021935727861,
                  "rejected_mean_error": 4.217363494873047,
                  "gap_rejected_minus_accepted": 2.374961301300261
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8283931016921997,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5468260125836542,
                  "rejected_mean_error": 3.6757090442096843,
                  "gap_rejected_minus_accepted": 2.12888303162603
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7356253266334534,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2319081079006196,
                  "rejected_mean_error": 2.927888539505005,
                  "gap_rejected_minus_accepted": 1.6959804316043854
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.186311036348343,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8774728777880867,
                  "rejected_mean_error": 2.48156232004359,
                  "gap_rejected_minus_accepted": 1.6040894422555034
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.230106973648072,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.86610019048055,
                  "rejected_mean_error": 4.249908332824707,
                  "gap_rejected_minus_accepted": 2.383808142344157
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.928302526473999,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5549441582378856,
                  "rejected_mean_error": 3.7356459299723306,
                  "gap_rejected_minus_accepted": 2.1807017717344452
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.75081068277359,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2302659492492676,
                  "rejected_mean_error": 2.9786960601806642,
                  "gap_rejected_minus_accepted": 1.7484301109313967
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2176400125026703,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8748263896457733,
                  "rejected_mean_error": 2.518749671823838,
                  "gap_rejected_minus_accepted": 1.6439232821780647
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9670626738425319,
              "spearman": 0.9424975542544393,
              "auroc_top30_bad": 0.9289150476190475,
              "mae": 0.17685388715881856,
              "mse": 0.06351204245810943,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7038963164620993,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06271800434589386
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19287171909809112
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6501315814375878
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.060924885837237
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9844297975577275,
              "spearman": 0.9729792543867228,
              "auroc_top30_worst": 0.9611337142857144,
              "pairwise_seed_ranking": 0.882,
              "predicted_best_mean_error": 1.5884111149311066,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06873202753066998,
              "gap_to_oracle": 0.00851359343528757,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40183590054512025
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6565768995728248
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0342382925987244
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3146690555345784
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5289117097854614,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4591189323531257,
                  "rejected_mean_error": 3.3376943168640136,
                  "gap_rejected_minus_accepted": 1.878575384510888
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0592567920684814,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3140491415749491,
                  "rejected_mean_error": 2.6436311273148267,
                  "gap_rejected_minus_accepted": 1.3295819857398776
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6583970189094543,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0342382925987244,
                  "rejected_mean_error": 2.2597146490097044,
                  "gap_rejected_minus_accepted": 1.22547635641098
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0711090862751007,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6570875075297614,
                  "rejected_mean_error": 1.9776437552278043,
                  "gap_rejected_minus_accepted": 1.3205562476980428
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.669582962989807,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.465095562140147,
                  "rejected_mean_error": 3.385571365356445,
                  "gap_rejected_minus_accepted": 1.9204758032162983
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0941773056983948,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3088849881753564,
                  "rejected_mean_error": 2.6908617908992465,
                  "gap_rejected_minus_accepted": 1.3819768027238901
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6739583015441895,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.024836105823517,
                  "rejected_mean_error": 2.2894501791000366,
                  "gap_rejected_minus_accepted": 1.2646140732765196
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0444086492061615,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.645200370796143,
                  "rejected_mean_error": 1.9980650387983272,
                  "gap_rejected_minus_accepted": 1.352864668002184
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9690663659872469,
              "spearman": 0.9486632424617238,
              "auroc_top30_bad": 0.9483900952380954,
              "mae": 0.15135107434280218,
              "mse": 0.042972169742436554,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6699808322131193,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07277802991867065
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2276505341529846
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7927610747337341
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.15231258837382
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9360816302970825,
              "spearman": 0.9197065668568722,
              "auroc_top30_worst": 0.923712,
              "pairwise_seed_ranking": 0.908,
              "predicted_best_mean_error": 1.5937257400751115,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06802538788318624,
              "gap_to_oracle": 0.0017018080949784409,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8438662168979645
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.101814756122155
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3677124664783478
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5273015515954256
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0993242502212524,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.604478936009937,
                  "rejected_mean_error": 2.1578225440979004,
                  "gap_rejected_minus_accepted": 0.5533436080879635
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.946772575378418,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.527021808615362,
                  "rejected_mean_error": 2.0573392535170045,
                  "gap_rejected_minus_accepted": 0.5303174449016426
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.694548487663269,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3677124664783478,
                  "rejected_mean_error": 1.9519141271591187,
                  "gap_rejected_minus_accepted": 0.584201660680771
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3980929851531982,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1030054721778955,
                  "rejected_mean_error": 1.8458120685504111,
                  "gap_rejected_minus_accepted": 0.7428065963725157
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1084751605987546,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.610005051030053,
                  "rejected_mean_error": 2.1274658203125,
                  "gap_rejected_minus_accepted": 0.5174607692824471
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.952722191810608,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5321620361690216,
                  "rejected_mean_error": 2.0464044639042447,
                  "gap_rejected_minus_accepted": 0.5142424277352231
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6944693326950073,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.379250684261322,
                  "rejected_mean_error": 1.9442515716552735,
                  "gap_rejected_minus_accepted": 0.5650008873939516
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4143113195896149,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1112608427093142,
                  "rejected_mean_error": 1.8472104219191852,
                  "gap_rejected_minus_accepted": 0.7359495792098709
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
