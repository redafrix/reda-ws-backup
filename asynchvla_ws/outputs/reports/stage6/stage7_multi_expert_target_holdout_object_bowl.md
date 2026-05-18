# Stage 7 Multi-Expert Target Experiments: holdout_object_bowl

```json
{
  "split": "holdout_object_bowl",
  "by_target": {
    "target_chunk_l2_single_expert": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 64,
        "best_calib_loss": 0.09250184148550034,
        "train_time_sec": 11.098455667495728,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8732515729233478,
              "spearman": 0.8244311023385521,
              "auroc_top30_bad": 0.9038754285714286,
              "mae": 0.199150263518095,
              "mse": 0.20494860843099286,
              "expert_lt_perturb_large": 0.982,
              "expert_lt_other_task": 0.556,
              "expert_lt_simvla_seed0": 0.974,
              "same_context_pred_std": 0.7364044416876814,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4581684996932745
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5107572555601597
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6745748174488544
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9525624635318916
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9976608391635352,
              "spearman": 0.9962527628261104,
              "auroc_top30_worst": 0.9989268571428571,
              "pairwise_seed_ranking": 0.8444,
              "predicted_best_mean_error": 1.538602079242468,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.07700624877214435,
              "gap_to_oracle": 0.00974284505844114,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6743697012066842
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.809222345662117
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0109223917841912
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.242154973022143
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7550881385803234,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4058021456599235,
                  "rejected_mean_error": 3.455568561077118,
                  "gap_rejected_minus_accepted": 2.049766415417195
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9782077968120575,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.242154973022143,
                  "rejected_mean_error": 2.716650229740143,
                  "gap_rejected_minus_accepted": 1.4744952567179999
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4217703342437744,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0109223917841912,
                  "rejected_mean_error": 2.210635182619095,
                  "gap_rejected_minus_accepted": 1.1997127908349037
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.043839544057846,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.809222345662117,
                  "rejected_mean_error": 1.8779642677148183,
                  "gap_rejected_minus_accepted": 1.0687419220527012
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7949519157409672,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4106799394885698,
                  "rejected_mean_error": 3.4599638247489928,
                  "gap_rejected_minus_accepted": 2.049283885260423
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9846018254756927,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.243710055867831,
                  "rejected_mean_error": 2.731303144454956,
                  "gap_rejected_minus_accepted": 1.4875930885871251
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4354626536369324,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0045136888623238,
                  "rejected_mean_error": 2.2267029671669007,
                  "gap_rejected_minus_accepted": 1.222189278304577
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0397168099880219,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.800633628487587,
                  "rejected_mean_error": 1.8872665611902872,
                  "gap_rejected_minus_accepted": 1.0866329327027002
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5344456067940385,
              "spearman": 0.4932557004545342,
              "auroc_top30_bad": 0.6620750476190476,
              "mae": 0.4725134448051453,
              "mse": 0.5354562103985607,
              "expert_lt_perturb_large": 0.976,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.6580567902121043,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8696435640454292
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7151101140499115
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9431539795279503
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1627336652358373
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.48124281325993523,
              "spearman": 0.501522842062619,
              "auroc_top30_worst": 0.724912761904762,
              "pairwise_seed_ranking": 0.734,
              "predicted_best_mean_error": 1.4900170176029206,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.03877680611610401,
              "gap_to_oracle": 0.027173995494842673,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9417090802192688
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1861114878302965
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.350894012928009
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4617680027159548
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.143479657173157,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5154707309405009,
                  "rejected_mean_error": 1.7257470383644105,
                  "gap_rejected_minus_accepted": 0.21027630742390957
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8071644008159637,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4617772872699872,
                  "rejected_mean_error": 1.7601841339668907,
                  "gap_rejected_minus_accepted": 0.2984068466969034
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5719630122184753,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.350894012928009,
                  "rejected_mean_error": 1.7221027104377746,
                  "gap_rejected_minus_accepted": 0.3712086975097657
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2599133849143982,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1860992072489316,
                  "rejected_mean_error": 1.6535473855226246,
                  "gap_rejected_minus_accepted": 0.467448178273693
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1192829608917236,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5096642843882242,
                  "rejected_mean_error": 1.7009596776962281,
                  "gap_rejected_minus_accepted": 0.19129539330800394
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8053592145442963,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4528997384290645,
                  "rejected_mean_error": 1.7540667435479542,
                  "gap_rejected_minus_accepted": 0.3011670051188897
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5893374681472778,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.329768606185913,
                  "rejected_mean_error": 1.7278190412521361,
                  "gap_rejected_minus_accepted": 0.39805043506622306
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2346548736095428,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1596785537780276,
                  "rejected_mean_error": 1.6531481659986118,
                  "gap_rejected_minus_accepted": 0.49346961222058416
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.45565524707588406,
              "spearman": 0.37232375041844823,
              "auroc_top30_bad": 0.5742750476190477,
              "mae": 0.6440970298111439,
              "mse": 0.7852837945385199,
              "expert_lt_perturb_large": 0.952,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.8,
              "same_context_pred_std": 0.6416677367790867,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5361030903458596
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5975748111724853
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2047598193407059
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.323514723030726
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.1327744912166865,
              "spearman": -0.03690899462975657,
              "auroc_top30_worst": 0.3728822857142857,
              "pairwise_seed_ranking": 0.7044,
              "predicted_best_mean_error": 1.760267560362816,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.046881021022796565,
              "gap_to_oracle": 0.036380760192871175,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.7532892799377442
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.0418567563860845
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8672461578845978
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7854975385706562
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7729887247085574,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7468567249510023,
                  "rejected_mean_error": 2.302885350227356,
                  "gap_rejected_minus_accepted": 0.5560286252763535
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8976944386959076,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7852182131312317,
                  "rejected_mean_error": 1.8540735419946737,
                  "gap_rejected_minus_accepted": 0.06885532886344192
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4523067474365234,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.8672461578845978,
                  "rejected_mean_error": 1.7376730170726775,
                  "gap_rejected_minus_accepted": -0.12957314081192028
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1852834224700928,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.038556476941886,
                  "rejected_mean_error": 1.723592643613113,
                  "gap_rejected_minus_accepted": -0.31496383332877276
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7639558553695673,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7481526039706337,
                  "rejected_mean_error": 2.3381123781204223,
                  "gap_rejected_minus_accepted": 0.5899597741497886
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9161685705184937,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7783452672435638,
                  "rejected_mean_error": 1.8926441328866142,
                  "gap_rejected_minus_accepted": 0.11429886564305036
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4483343958854675,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8735346076488495,
                  "rejected_mean_error": 1.7407625551223755,
                  "gap_rejected_minus_accepted": -0.13277205252647395
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2058431506156921,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.1086769430410293,
                  "rejected_mean_error": 1.7055641600792422,
                  "gap_rejected_minus_accepted": -0.4031127829617871
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6300008151868374,
              "spearman": 0.608020658913308,
              "auroc_top30_bad": 0.8037314285714285,
              "mae": 0.4866051325559616,
              "mse": 0.483919959617456,
              "expert_lt_perturb_large": 0.968,
              "expert_lt_other_task": 0.52,
              "expert_lt_simvla_seed0": 0.952,
              "same_context_pred_std": 0.6958946157848249,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6433707392215728
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5887044182300568
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8445564165115357
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0389714986165364
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6492209277043868,
              "spearman": 0.5551265607209989,
              "auroc_top30_worst": 0.8575939047619048,
              "pairwise_seed_ranking": 0.7724,
              "predicted_best_mean_error": 1.5645111474990845,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.0548111307621002,
              "gap_to_oracle": 0.013367887258529665,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8015897800922394
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.137714755267669
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2902439646244048
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4147969083681797
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4749040365219117,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5236245155069563,
                  "rejected_mean_error": 2.5174827065467835,
                  "gap_rejected_minus_accepted": 0.9938581910398272
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1479631066322327,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4138661342789294,
                  "rejected_mean_error": 2.2491065509403096,
                  "gap_rejected_minus_accepted": 0.8352404166613803
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7241225838661194,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2902439646244048,
                  "rejected_mean_error": 1.9557767045974732,
                  "gap_rejected_minus_accepted": 0.6655327399730684
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4086147546768188,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1393266152650023,
                  "rejected_mean_error": 1.7845823774660918,
                  "gap_rejected_minus_accepted": 0.6452557622010895
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5133229732513427,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5274459134207832,
                  "rejected_mean_error": 2.4462095618247988,
                  "gap_rejected_minus_accepted": 0.9187636484040156
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1578717827796936,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4080555018256693,
                  "rejected_mean_error": 2.2464157257761275,
                  "gap_rejected_minus_accepted": 0.8383602239504582
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7440264225006104,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2712623672485353,
                  "rejected_mean_error": 1.9673821892738341,
                  "gap_rejected_minus_accepted": 0.6961198220252989
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3442843556404114,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0983237964766366,
                  "rejected_mean_error": 1.7948458309479576,
                  "gap_rejected_minus_accepted": 0.696522034471321
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
        "best_epoch": 72,
        "best_calib_loss": 0.006608848460018635,
        "train_time_sec": 35.394248247146606,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993164122940559,
              "spearman": 0.9983577420162277,
              "auroc_top30_bad": 0.999452,
              "mae": 0.03135530734295026,
              "mse": 0.0016964715296697342,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7374263144541233,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0004921396225690841
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19834575955867767
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5740277749300003
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9269196357250213
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9992945046642425,
              "spearman": 0.9989230181728949,
              "auroc_top30_worst": 0.9997864761904762,
              "pairwise_seed_ranking": 0.9503,
              "predicted_best_mean_error": 1.530733484685421,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.08487484332919126,
              "gap_to_oracle": 0.0018742505013942257,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6665146862864494
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8078397143602372
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.010246845471859
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2414308146715165
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7127034902572658,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4057531255284945,
                  "rejected_mean_error": 3.456009742259979,
                  "gap_rejected_minus_accepted": 2.0502566167314846
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9589014053344727,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2414308146715165,
                  "rejected_mean_error": 2.718822704792023,
                  "gap_rejected_minus_accepted": 1.4773918901205063
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3957725167274475,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.010246845471859,
                  "rejected_mean_error": 2.211310728931427,
                  "gap_rejected_minus_accepted": 1.201063883459568
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0051496922969818,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8078397143602372,
                  "rejected_mean_error": 1.878425144815445,
                  "gap_rejected_minus_accepted": 1.0705854304552078
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.72780945301056,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4107309549715783,
                  "rejected_mean_error": 3.4595046854019165,
                  "gap_rejected_minus_accepted": 2.048773730430338
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9788897633552551,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2432316968043646,
                  "rejected_mean_error": 2.7327382216453553,
                  "gap_rejected_minus_accepted": 1.4895065248409907
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.407336413860321,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0038428853154182,
                  "rejected_mean_error": 2.227373770713806,
                  "gap_rejected_minus_accepted": 1.223530885398388
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.001242846250534,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7992050584554672,
                  "rejected_mean_error": 1.8877427512009939,
                  "gap_rejected_minus_accepted": 1.0885376927455268
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9875808193339655,
              "spearman": 0.9856164412167419,
              "auroc_top30_bad": 0.9883641904761905,
              "mae": 0.0839153189798817,
              "mse": 0.014495156809941045,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6921645029386101,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05811034601926804
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22980206944942475
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6798498718619347
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0344300635258357
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9790017063060935,
              "spearman": 0.9807289691705404,
              "auroc_top30_worst": 0.9896380952380952,
              "pairwise_seed_ranking": 0.884,
              "predicted_best_mean_error": 1.4686399278640747,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.0601538958549499,
              "gap_to_oracle": 0.005796905755996784,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8746969614028931
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9761530779875242
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.170456403541565
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3584342550621358
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.076364016532898,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4564973731570774,
                  "rejected_mean_error": 2.256507258415222,
                  "gap_rejected_minus_accepted": 0.8000098852581448
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8979231715202332,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.357896799975042,
                  "rejected_mean_error": 2.0711618227699695,
                  "gap_rejected_minus_accepted": 0.7132650227949275
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.516311228275299,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.170456403541565,
                  "rejected_mean_error": 1.9025403198242188,
                  "gap_rejected_minus_accepted": 0.7320839162826538
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1845585703849792,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9766812396887392,
                  "rejected_mean_error": 1.723502373619039,
                  "gap_rejected_minus_accepted": 0.7468211339302997
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0887625217437744,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4510493670569526,
                  "rejected_mean_error": 2.2284939336776732,
                  "gap_rejected_minus_accepted": 0.7774445666207206
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8873674869537354,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.350069777213316,
                  "rejected_mean_error": 2.0592921839820013,
                  "gap_rejected_minus_accepted": 0.7092224067686854
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5165117979049683,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1585786447525024,
                  "rejected_mean_error": 1.8990090026855468,
                  "gap_rejected_minus_accepted": 0.7404303579330445
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2052026689052582,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9613440339527433,
                  "rejected_mean_error": 1.7199667475440286,
                  "gap_rejected_minus_accepted": 0.7586227135912853
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9698387538206628,
              "spearman": 0.9746278397920239,
              "auroc_top30_bad": 0.9834247619047618,
              "mae": 0.15367782436516136,
              "mse": 0.060953356370865096,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7118303000231238,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08204714834690094
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20457222640514375
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6975131454348564
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0527054974794388
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9278404835417444,
              "spearman": 0.9542348322782928,
              "auroc_top30_worst": 0.970663619047619,
              "pairwise_seed_ranking": 0.918,
              "predicted_best_mean_error": 1.7257317949533462,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08141678643226635,
              "gap_to_oracle": 0.001844994783401388,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9487190504074097
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1136764918382351
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3110799119949341
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4648215567379363
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.231870985031129,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6615764450497097,
                  "rejected_mean_error": 3.070407869338989,
                  "gap_rejected_minus_accepted": 1.4088314242892794
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8910618126392365,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.464386664052656,
                  "rejected_mean_error": 2.814518147383254,
                  "gap_rejected_minus_accepted": 1.3501314833305982
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.623946189880371,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3110799119949341,
                  "rejected_mean_error": 2.2938392629623414,
                  "gap_rejected_minus_accepted": 0.9827593509674073
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3552919328212738,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1143572330474854,
                  "rejected_mean_error": 2.032316617293953,
                  "gap_rejected_minus_accepted": 0.9179593842464677
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.239777112007141,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.665555573436949,
                  "rejected_mean_error": 3.081485652923584,
                  "gap_rejected_minus_accepted": 1.415930079486635
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9141633212566376,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.462923061879561,
                  "rejected_mean_error": 2.8288973456337336,
                  "gap_rejected_minus_accepted": 1.3659742837541726
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6262873411178589,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.304034340620041,
                  "rejected_mean_error": 2.3102628221511843,
                  "gap_rejected_minus_accepted": 1.0062284815311433
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3521877527236938,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1155537418902866,
                  "rejected_mean_error": 2.04014577330115,
                  "gap_rejected_minus_accepted": 0.9245920314108635
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9882403267103662,
              "spearman": 0.9866602472499564,
              "auroc_top30_bad": 0.9954057142857142,
              "mae": 0.0893630730902776,
              "mse": 0.01761183625610684,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.964,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7421157504692509,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07187999844551086
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19805052495002748
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.589163192653656
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9346246039072672
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9805735685468551,
              "spearman": 0.9832842849819425,
              "auroc_top30_worst": 0.9946544761904762,
              "pairwise_seed_ranking": 0.9276,
              "predicted_best_mean_error": 1.5536651313304901,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06565714693069458,
              "gap_to_oracle": 0.0025218710899352903,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.571248250246048
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8667129729993832
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1178179247379303
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3125028013229878
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6497200250625617,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4774259408579933,
                  "rejected_mean_error": 2.9332698783874513,
                  "gap_rejected_minus_accepted": 1.455843937529458
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.02284699678421,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3116741824493592,
                  "rejected_mean_error": 2.5550294227112595,
                  "gap_rejected_minus_accepted": 1.2433552402619004
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.53538978099823,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1178179247379303,
                  "rejected_mean_error": 2.1282027444839478,
                  "gap_rejected_minus_accepted": 1.0103848197460175
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2697419226169586,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.868118447712816,
                  "rejected_mean_error": 1.8751780620379535,
                  "gap_rejected_minus_accepted": 1.0070596143251374
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.635952234268188,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4691338721911114,
                  "rejected_mean_error": 2.971017932891846,
                  "gap_rejected_minus_accepted": 1.5018840607007344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.022744596004486,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.298858723857186,
                  "rejected_mean_error": 2.570539495301625,
                  "gap_rejected_minus_accepted": 1.2716807714444391
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.553495466709137,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1066490778923035,
                  "rejected_mean_error": 2.131995478630066,
                  "gap_rejected_minus_accepted": 1.0253464007377626
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2661560475826263,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8505419199428861,
                  "rejected_mean_error": 1.8783231476411462,
                  "gap_rejected_minus_accepted": 1.02778122769826
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
        "best_epoch": 62,
        "best_calib_loss": 0.009774171747267246,
        "train_time_sec": 41.79270267486572,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9987955892958243,
              "spearman": 0.9973828152655809,
              "auroc_top30_bad": 0.9992797142857142,
              "mae": 0.032729807943954074,
              "mse": 0.001978913390673602,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7410814621332054,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.007685686901211739
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1982556258916855
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5746552944898605
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9271703943570455
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9985562957371965,
              "spearman": 0.997221139488712,
              "auroc_top30_worst": 0.9993240000000001,
              "pairwise_seed_ranking": 0.9626,
              "predicted_best_mean_error": 1.5310391190648078,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.08456920894980446,
              "gap_to_oracle": 0.0021798848807810245,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6675848305821419
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.808527858376503
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0109939445853233
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2417984057029088
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7506045818328873,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4057584256794717,
                  "rejected_mean_error": 3.455962040901184,
                  "gap_rejected_minus_accepted": 2.0502036152217125
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9891135394573212,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2417984057029088,
                  "rejected_mean_error": 2.7177199316978453,
                  "gap_rejected_minus_accepted": 1.4759215259949365
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4258820414543152,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0109939445853233,
                  "rejected_mean_error": 2.2105636298179627,
                  "gap_rejected_minus_accepted": 1.1995696852326394
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0396640300750732,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.808527858376503,
                  "rejected_mean_error": 1.8781957634766897,
                  "gap_rejected_minus_accepted": 1.0696679051001867
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7894289493560795,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4107723383439912,
                  "rejected_mean_error": 3.4591322350502014,
                  "gap_rejected_minus_accepted": 2.04835989670621
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.018126428127289,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2434530360301335,
                  "rejected_mean_error": 2.732074203968048,
                  "gap_rejected_minus_accepted": 1.4886211679379147
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.436428427696228,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0047041092514992,
                  "rejected_mean_error": 2.2265125467777254,
                  "gap_rejected_minus_accepted": 1.2218084375262261
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0326415598392487,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7994985603094101,
                  "rejected_mean_error": 1.8876449172496796,
                  "gap_rejected_minus_accepted": 1.0881463569402694
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9810211137701131,
              "spearman": 0.9792728278384073,
              "auroc_top30_bad": 0.9855809523809523,
              "mae": 0.10288657846585265,
              "mse": 0.022217719534552434,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.684741087433832,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05997799229621887
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2430175665616989
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6817212314009666
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0372713411569596
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9701714523614715,
              "spearman": 0.9751349027423378,
              "auroc_top30_worst": 0.9827626666666667,
              "pairwise_seed_ranking": 0.8912,
              "predicted_best_mean_error": 1.4667864129543304,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.06200741076469418,
              "gap_to_oracle": 0.003943390846252504,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8844072666168213
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.977264587695782
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.168822119140625
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3617236199917824
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.066435170173645,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.461188960923089,
                  "rejected_mean_error": 2.2142829685211183,
                  "gap_rejected_minus_accepted": 0.7530940075980292
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8971485793590546,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3611826284717978,
                  "rejected_mean_error": 2.0613253329889463,
                  "gap_rejected_minus_accepted": 0.7001427045171484
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.493642508983612,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.168822119140625,
                  "rejected_mean_error": 1.9041746042251586,
                  "gap_rejected_minus_accepted": 0.7353524850845337
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1027243435382843,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9777993363694261,
                  "rejected_mean_error": 1.7231288792102288,
                  "gap_rejected_minus_accepted": 0.7453295428408028
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0819550275802614,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4541653680801392,
                  "rejected_mean_error": 2.200449924468994,
                  "gap_rejected_minus_accepted": 0.7462845563888549
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8988619446754456,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.353086600966632,
                  "rejected_mean_error": 2.050337484904698,
                  "gap_rejected_minus_accepted": 0.697250883938066
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4882574081420898,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.156762788772583,
                  "rejected_mean_error": 1.9008248586654664,
                  "gap_rejected_minus_accepted": 0.7440620698928833
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1140170097351074,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9579109653594002,
                  "rejected_mean_error": 1.7211233428455293,
                  "gap_rejected_minus_accepted": 0.763212377486129
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9700519002388079,
              "spearman": 0.9784101830196877,
              "auroc_top30_bad": 0.9945287619047619,
              "mae": 0.16195935019705793,
              "mse": 0.06812490523746129,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6880327970366211,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07554320102930069
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2143383180141449
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6965736616969108
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0572065977652867
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9449049828574541,
              "spearman": 0.971300368448236,
              "auroc_top30_worst": 0.9938072380952381,
              "pairwise_seed_ranking": 0.9228,
              "predicted_best_mean_error": 1.7263339964151383,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08081458497047422,
              "gap_to_oracle": 0.002447196245193517,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9442452368736267
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1190344511698453
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2874864330291749
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.477318193358399
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1801987409591677,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6512794806162516,
                  "rejected_mean_error": 3.1630805492401124,
                  "gap_rejected_minus_accepted": 1.5118010686238608
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9313549399375916,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4766572020478792,
                  "rejected_mean_error": 2.7777849393911636,
                  "gap_rejected_minus_accepted": 1.3011277373432844
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5389454364776611,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2874864330291749,
                  "rejected_mean_error": 2.3174327419281004,
                  "gap_rejected_minus_accepted": 1.0299463088989256
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3281195163726807,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1199383975598758,
                  "rejected_mean_error": 2.030452258177221,
                  "gap_rejected_minus_accepted": 0.9105138606173451
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1731934309005734,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6520854291650984,
                  "rejected_mean_error": 3.202716951370239,
                  "gap_rejected_minus_accepted": 1.5506315222051408
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.942331075668335,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4876919906725858,
                  "rejected_mean_error": 2.755376874454438,
                  "gap_rejected_minus_accepted": 1.267684883781852
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.527981460094452,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2840002439022065,
                  "rejected_mean_error": 2.3302969188690184,
                  "gap_rejected_minus_accepted": 1.046296674966812
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3534708619117737,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.114241546581662,
                  "rejected_mean_error": 2.0405878497954997,
                  "gap_rejected_minus_accepted": 0.9263463032138377
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9902991452678354,
              "spearman": 0.9882897642855109,
              "auroc_top30_bad": 0.9964449523809523,
              "mae": 0.09466668908580032,
              "mse": 0.0167190446563316,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6932810681175383,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07706621432304382
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2013700318813324
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.589793391418457
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9331917272567749
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9911082811766803,
              "spearman": 0.9854463538216667,
              "auroc_top30_worst": 0.9988601904761905,
              "pairwise_seed_ranking": 0.9072,
              "predicted_best_mean_error": 1.5545144884586335,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.0648077898025512,
              "gap_to_oracle": 0.00337122821807867,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5721910169124603
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8762802299207602
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1162698492527008
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3088677199219845
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4998837232589723,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4753017887804243,
                  "rejected_mean_error": 2.9523872470855714,
                  "gap_rejected_minus_accepted": 1.4770854583051471
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9476731419563293,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3082267734576951,
                  "rejected_mean_error": 2.565349621513781,
                  "gap_rejected_minus_accepted": 1.257122848056086
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4114554524421692,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1162698492527008,
                  "rejected_mean_error": 2.129750819969177,
                  "gap_rejected_minus_accepted": 1.0134809707164762
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1362401247024536,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8771777409143722,
                  "rejected_mean_error": 1.872151852035726,
                  "gap_rejected_minus_accepted": 0.9949741111213539
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4647115230560304,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4688920924398634,
                  "rejected_mean_error": 2.973193950653076,
                  "gap_rejected_minus_accepted": 1.5043018582132126
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9468590319156647,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2967743615415646,
                  "rejected_mean_error": 2.576726412016248,
                  "gap_rejected_minus_accepted": 1.2799520504746835
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4422118067741394,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1035101056098937,
                  "rejected_mean_error": 2.1351344509124757,
                  "gap_rejected_minus_accepted": 1.031624345302582
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1151980459690094,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8613661518172612,
                  "rejected_mean_error": 1.8746764812877472,
                  "gap_rejected_minus_accepted": 1.0133103294704862
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
        "best_epoch": 76,
        "best_calib_loss": 0.011059611104428768,
        "train_time_sec": 29.047210931777954,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9996704698306424,
              "spearman": 0.9987555239047248,
              "auroc_top30_bad": 0.9997656190476191,
              "mae": 0.017163650383946242,
              "mse": 0.0006039163698062851,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7402984942616385,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0015843759328126907
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19793867905139922
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.573978625035286
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.926819246228536
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997207292507548,
              "spearman": 0.9995632078545282,
              "auroc_top30_worst": 0.9997933333333334,
              "pairwise_seed_ranking": 0.9658,
              "predicted_best_mean_error": 1.5296583706736564,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.0859499573409559,
              "gap_to_oracle": 0.0007991364896295927,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6651875501275063
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8070012709856034
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.010102328145504
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2413569559017816
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7588279485702514,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4056644135779806,
                  "rejected_mean_error": 3.4568081498146057,
                  "gap_rejected_minus_accepted": 2.051143736236625
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9508898258209229,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2413569559017816,
                  "rejected_mean_error": 2.719044281101227,
                  "gap_rejected_minus_accepted": 1.4776873251994453
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3961353302001953,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.010102328145504,
                  "rejected_mean_error": 2.211455246257782,
                  "gap_rejected_minus_accepted": 1.2013529181122782
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.021920770406723,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8070012709856034,
                  "rejected_mean_error": 1.8787046259403228,
                  "gap_rejected_minus_accepted": 1.0717033549547195
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8003581762313843,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4106119764182303,
                  "rejected_mean_error": 3.4605754923820498,
                  "gap_rejected_minus_accepted": 2.049963515963819
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9729012846946716,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2431203195651372,
                  "rejected_mean_error": 2.733072353363037,
                  "gap_rejected_minus_accepted": 1.4899520337978998
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4070658683776855,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0037727227807045,
                  "rejected_mean_error": 2.22744393324852,
                  "gap_rejected_minus_accepted": 1.2236712104678154
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0128614008426666,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7986539951562881,
                  "rejected_mean_error": 1.8879264389673869,
                  "gap_rejected_minus_accepted": 1.0892724438110988
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9776617995081439,
              "spearman": 0.9774443829956435,
              "auroc_top30_bad": 0.9832342857142856,
              "mae": 0.10905353167194635,
              "mse": 0.026301862939209848,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.670286725517434,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.061443851113319396
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23746427249908447
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6834573845267295
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0388375192244848
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9662704686206587,
              "spearman": 0.9720777876977843,
              "auroc_top30_worst": 0.9822110476190477,
              "pairwise_seed_ranking": 0.8968,
              "predicted_best_mean_error": 1.4677903163433075,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.061003507375717136,
              "gap_to_oracle": 0.004947294235229549,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8758969717025756
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9781779230405123
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1712398431777955
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3631157634863214
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.029927945137024,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.462734112845527,
                  "rejected_mean_error": 2.2003766012191774,
                  "gap_rejected_minus_accepted": 0.7376424883736505
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8716699182987213,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3625081906069305,
                  "rejected_mean_error": 2.0573571166291402,
                  "gap_rejected_minus_accepted": 0.6948489260222097
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4888978004455566,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1712398431777955,
                  "rejected_mean_error": 1.9017568801879883,
                  "gap_rejected_minus_accepted": 0.7305170370101928
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1083196103572845,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9788691308170843,
                  "rejected_mean_error": 1.7227715199123452,
                  "gap_rejected_minus_accepted": 0.743902389095261
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.031501364707947,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.458751056459215,
                  "rejected_mean_error": 2.159178729057312,
                  "gap_rejected_minus_accepted": 0.7004276725980971
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8673586249351501,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.356426332723648,
                  "rejected_mean_error": 2.040424312864031,
                  "gap_rejected_minus_accepted": 0.6839979801403828
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.492978811264038,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1595196619033814,
                  "rejected_mean_error": 1.898067985534668,
                  "gap_rejected_minus_accepted": 0.7385483236312866
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1150881052017212,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9621994949522472,
                  "rejected_mean_error": 1.719678544105693,
                  "gap_rejected_minus_accepted": 0.7574790491534458
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9606453931501111,
              "spearman": 0.9691055761378675,
              "auroc_top30_bad": 0.987974857142857,
              "mae": 0.1816689935252931,
              "mse": 0.09079982278983591,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6677776024340702,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08549705529212952
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20524405343532562
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6966631805300713
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0737347413301468
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9199597473244577,
              "spearman": 0.9607343467099821,
              "auroc_top30_worst": 0.9829851428571429,
              "pairwise_seed_ranking": 0.9312,
              "predicted_best_mean_error": 1.726581240773201,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08056734061241144,
              "gap_to_oracle": 0.0026944406032562984,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.942697223186493
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1163353755688057
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.287874521446228
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4966040716242435
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.050541019439698,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6600358971489801,
                  "rejected_mean_error": 3.084272800445557,
                  "gap_rejected_minus_accepted": 1.4242369032965767
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8475217819213867,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4962034895936607,
                  "rejected_mean_error": 2.719270973159863,
                  "gap_rejected_minus_accepted": 1.2230674835662025
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5070058107376099,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.287874521446228,
                  "rejected_mean_error": 2.317044653511047,
                  "gap_rejected_minus_accepted": 1.0291701320648192
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3011691570281982,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1169702378324806,
                  "rejected_mean_error": 2.0314437565706838,
                  "gap_rejected_minus_accepted": 0.9144735187382032
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.068675088882446,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6588545299900903,
                  "rejected_mean_error": 3.1417950439453124,
                  "gap_rejected_minus_accepted": 1.482940513955222
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.848277986049652,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.501495646761063,
                  "rejected_mean_error": 2.7144041174934026,
                  "gap_rejected_minus_accepted": 1.2129084707323396
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4950509071350098,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2846237018108368,
                  "rejected_mean_error": 2.329673460960388,
                  "gap_rejected_minus_accepted": 1.0450497591495513
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3169670701026917,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1161426679482536,
                  "rejected_mean_error": 2.039947365057022,
                  "gap_rejected_minus_accepted": 0.9238046971087686
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9885530820125419,
              "spearman": 0.9873071569966829,
              "auroc_top30_bad": 0.996215619047619,
              "mae": 0.09507166715952226,
              "mse": 0.01824012523365051,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6926119664239159,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07927173376083374
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20988853616714478
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5899181925773621
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9332236181259155
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9900935382784158,
              "spearman": 0.9875461961895656,
              "auroc_top30_worst": 0.9986346666666667,
              "pairwise_seed_ranking": 0.918,
              "predicted_best_mean_error": 1.5539589463472365,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06536333191394816,
              "gap_to_oracle": 0.002815686106681703,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5748902313709259
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8723986031344304
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.115752568101883
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3095172591872815
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5305556297302254,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.477066036886639,
                  "rejected_mean_error": 2.936509014129639,
                  "gap_rejected_minus_accepted": 1.4594429772429998
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.916896641254425,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3086845204631699,
                  "rejected_mean_error": 2.56397930539835,
                  "gap_rejected_minus_accepted": 1.25529478493518
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4302647709846497,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.115752568101883,
                  "rejected_mean_error": 2.130268101119995,
                  "gap_rejected_minus_accepted": 1.0145155330181121
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1863001883029938,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8734513971561821,
                  "rejected_mean_error": 1.8733966178802441,
                  "gap_rejected_minus_accepted": 0.999945220724062
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.538309073448181,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4688920924398634,
                  "rejected_mean_error": 2.973193950653076,
                  "gap_rejected_minus_accepted": 1.5043018582132126
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9564788341522217,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2969041122472222,
                  "rejected_mean_error": 2.5763412789692954,
                  "gap_rejected_minus_accepted": 1.2794371667220732
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.462294578552246,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1039512190818788,
                  "rejected_mean_error": 2.1346933374404906,
                  "gap_rejected_minus_accepted": 1.0307421183586118
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.185412973165512,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8553056083028279,
                  "rejected_mean_error": 1.8767182686749626,
                  "gap_rejected_minus_accepted": 1.0214126603721347
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
        "best_epoch": 66,
        "best_calib_loss": 0.09490428864955902,
        "train_time_sec": 10.668074607849121,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8878599180648096,
              "spearman": 0.8366058786364856,
              "auroc_top30_bad": 0.913172619047619,
              "mae": 0.18527197841978632,
              "mse": 0.17465044609544594,
              "expert_lt_perturb_large": 0.984,
              "expert_lt_other_task": 0.528,
              "expert_lt_simvla_seed0": 0.97,
              "same_context_pred_std": 0.6886920723308838,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.43025648371130226
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5205282339112833
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6614450423804111
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9335122415791576
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2854957839774435
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9972806956883277,
              "spearman": 0.9955500472140016,
              "auroc_top30_worst": 0.9984502857142857,
              "pairwise_seed_ranking": 0.8654,
              "predicted_best_mean_error": 1.511984806895256,
              "seed0_mean_error": 1.5883966648578645,
              "random_seed_mean_error": 1.5829028643667697,
              "oracle_best_mean_error": 1.5042814255058765,
              "improvement_over_seed0": 0.07641185796260852,
              "gap_to_oracle": 0.007703381389379427,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6480743292570114
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7759602537631989
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9749528288125991
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2068682440280913
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5820222539305686
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.708745861053467,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3745588674412834,
                  "rejected_mean_error": 3.449192732334137,
                  "gap_rejected_minus_accepted": 2.0746338648928537
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9424722790718079,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2068682440280913,
                  "rejected_mean_error": 2.7074842836380006,
                  "gap_rejected_minus_accepted": 1.5006160396099093
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3582816123962402,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9749528288125991,
                  "rejected_mean_error": 2.189091679048538,
                  "gap_rejected_minus_accepted": 1.2141388502359391
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9582981318235397,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7759602537631989,
                  "rejected_mean_error": 1.850709587319692,
                  "gap_rejected_minus_accepted": 1.074749333556493
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7186801195144654,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3813653906186423,
                  "rejected_mean_error": 3.4516781330108643,
                  "gap_rejected_minus_accepted": 2.070312742392222
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9455167949199677,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.210308404604594,
                  "rejected_mean_error": 2.7226614456176756,
                  "gap_rejected_minus_accepted": 1.5123530410130817
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3669008612632751,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9711188597679138,
                  "rejected_mean_error": 2.205674469947815,
                  "gap_rejected_minus_accepted": 1.2345556101799011
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9530335515737534,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7694804787635803,
                  "rejected_mean_error": 1.8613687268892924,
                  "gap_rejected_minus_accepted": 1.0918882481257122
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5283209790200558,
              "spearman": 0.49487425335270313,
              "auroc_top30_bad": 0.659200380952381,
              "mae": 0.4835950057506561,
              "mse": 0.5235514610556242,
              "expert_lt_perturb_large": 0.972,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.6043289273101388,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5150211170911789
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6810352223157883
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9471548673272133
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1776845086971919
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.41245458694668735,
              "spearman": 0.44219544306908365,
              "auroc_top30_worst": 0.6837729523809524,
              "pairwise_seed_ranking": 0.7376,
              "predicted_best_mean_error": 1.4883030326366424,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.04049079108238218,
              "gap_to_oracle": 0.025460010528564503,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9278787817955018
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1596991654772024
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3909878047943116
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.48014448827772
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1075722694396974,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.523459138976203,
                  "rejected_mean_error": 1.653851366043091,
                  "gap_rejected_minus_accepted": 0.1303922270668878
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7181352972984314,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4798338578630283,
                  "rejected_mean_error": 1.7061297996356464,
                  "gap_rejected_minus_accepted": 0.22629594177261803
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.465326726436615,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3909878047943116,
                  "rejected_mean_error": 1.6820089185714722,
                  "gap_rejected_minus_accepted": 0.29102111377716056
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2302109003067017,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1620910291473705,
                  "rejected_mean_error": 1.6615671931488665,
                  "gap_rejected_minus_accepted": 0.49947616400149597
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.150185227394104,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.516684086587694,
                  "rejected_mean_error": 1.637781457901001,
                  "gap_rejected_minus_accepted": 0.121097371313307
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7209112048149109,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4627018593211862,
                  "rejected_mean_error": 1.7249715593126085,
                  "gap_rejected_minus_accepted": 0.26226969999142224
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4792060852050781,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.382322455883026,
                  "rejected_mean_error": 1.6752651915550232,
                  "gap_rejected_minus_accepted": 0.29294273567199713
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2210009694099426,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1703039738867018,
                  "rejected_mean_error": 1.6495684790101282,
                  "gap_rejected_minus_accepted": 0.47926450512342633
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.42909167241746315,
              "spearman": 0.3687127747065767,
              "auroc_top30_bad": 0.5712655238095239,
              "mae": 0.652670311665535,
              "mse": 0.8405219475575275,
              "expert_lt_perturb_large": 0.896,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.904,
              "same_context_pred_std": 0.6434858754316025,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4851312234401703
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.559269916176796
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.20777395632267
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3306144879579545
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.07616627650195526,
              "spearman": -0.14786839082777015,
              "auroc_top30_worst": 0.31735771428571424,
              "pairwise_seed_ranking": 0.7068,
              "predicted_best_mean_error": 1.7593128224611283,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.04783575892448422,
              "gap_to_oracle": 0.03542602229118352,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.967988622903824
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.2268568738721886
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.885932645702362
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7966261767883545
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.715816140174866,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.745029428799947,
                  "rejected_mean_error": 2.319331015586853,
                  "gap_rejected_minus_accepted": 0.5743015867869061
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.91212660074234,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7963491467045363,
                  "rejected_mean_error": 1.8207518654509474,
                  "gap_rejected_minus_accepted": 0.02440271874641109
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4544544219970703,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.885932645702362,
                  "rejected_mean_error": 1.7189865292549134,
                  "gap_rejected_minus_accepted": -0.1669461164474486
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1135529279708862,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.2240693370183817,
                  "rejected_mean_error": 1.661623032936546,
                  "gap_rejected_minus_accepted": -0.5624463040818357
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7198515653610227,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7481526039706337,
                  "rejected_mean_error": 2.3381123781204223,
                  "gap_rejected_minus_accepted": 0.5899597741497886
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8804101347923279,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.8014994858101727,
                  "rejected_mean_error": 1.8239165317444574,
                  "gap_rejected_minus_accepted": 0.02241704593428473
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4556689858436584,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.882996763944626,
                  "rejected_mean_error": 1.7313003988265991,
                  "gap_rejected_minus_accepted": -0.15169636511802675
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1246864795684814,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.2264540701631517,
                  "rejected_mean_error": 1.6658852348990618,
                  "gap_rejected_minus_accepted": -0.5605688352640898
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.620634151143719,
              "spearman": 0.5982426733720506,
              "auroc_top30_bad": 0.7898769523809523,
              "mae": 0.4867024058640003,
              "mse": 0.47939930576923345,
              "expert_lt_perturb_large": 0.96,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.94,
              "same_context_pred_std": 0.6651048809530594,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5390777618288994
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6967668162107468
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8389372031450272
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0698934072415034
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6766811716291017,
              "spearman": 0.5980459056933797,
              "auroc_top30_worst": 0.8433401904761906,
              "pairwise_seed_ranking": 0.776,
              "predicted_best_mean_error": 1.5635058681964875,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.055816410064697175,
              "gap_to_oracle": 0.012362607955932692,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7427378320693969
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.095861348299644
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2697225506305694
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4282943165696251
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.430217242240906,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5345311315059662,
                  "rejected_mean_error": 2.4193231625556946,
                  "gap_rejected_minus_accepted": 0.8847920310497284
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9447272419929504,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4280758461613792,
                  "rejected_mean_error": 2.2065682121739982,
                  "gap_rejected_minus_accepted": 0.7784923660126191
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.669035255908966,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2697225506305694,
                  "rejected_mean_error": 1.9762981185913087,
                  "gap_rejected_minus_accepted": 0.7065755679607393
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.361068844795227,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0953907371519473,
                  "rejected_mean_error": 1.7992589301335264,
                  "gap_rejected_minus_accepted": 0.7038681929815791
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4776973724365234,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5305504020055134,
                  "rejected_mean_error": 2.418269164562225,
                  "gap_rejected_minus_accepted": 0.8877187625567118
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9554621577262878,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4160777891383451,
                  "rejected_mean_error": 2.2226035396258035,
                  "gap_rejected_minus_accepted": 0.8065257504874583
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6801475882530212,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2754167919158936,
                  "rejected_mean_error": 1.9632277646064757,
                  "gap_rejected_minus_accepted": 0.6878109726905821
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2949818670749664,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0226841455414182,
                  "rejected_mean_error": 1.820328708000999,
                  "gap_rejected_minus_accepted": 0.7976445624595809
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
        "best_epoch": 61,
        "best_calib_loss": 0.008058466017246246,
        "train_time_sec": 34.99385666847229,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995831192937531,
              "spearman": 0.9990842306441692,
              "auroc_top30_bad": 0.9998202857142857,
              "mae": 0.020096959488233552,
              "mse": 0.0007307984189282518,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7208796495923072,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08737808579439298
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23780555352661759
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5673907332514413
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9074362774911647
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2854957839774435
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996022053988729,
              "spearman": 0.9993507182780287,
              "auroc_top30_worst": 0.9998820952380952,
              "pairwise_seed_ranking": 0.9416,
              "predicted_best_mean_error": 1.5064386921226978,
              "seed0_mean_error": 1.5883966648578645,
              "random_seed_mean_error": 1.5829028643667697,
              "oracle_best_mean_error": 1.5042814255058765,
              "improvement_over_seed0": 0.0819579727351667,
              "gap_to_oracle": 0.0021572666168212518,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.640546558380127
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7735350779533386
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9731157085180283
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2059144010066987
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5820222539305686
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7791325330734256,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.374355500790808,
                  "rejected_mean_error": 3.4510230321884157,
                  "gap_rejected_minus_accepted": 2.0766675313976077
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9733960628509521,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2059144010066987,
                  "rejected_mean_error": 2.710345812702179,
                  "gap_rejected_minus_accepted": 1.5044314116954804
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3653891682624817,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9731157085180283,
                  "rejected_mean_error": 2.190928799343109,
                  "gap_rejected_minus_accepted": 1.2178130908250808
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9628657847642899,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7735350779533386,
                  "rejected_mean_error": 1.8515179792563121,
                  "gap_rejected_minus_accepted": 1.0779829013029736
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.810926938056946,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3810052453147041,
                  "rejected_mean_error": 3.4549194407463073,
                  "gap_rejected_minus_accepted": 2.073914195431603
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9894994795322418,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2092749169667563,
                  "rejected_mean_error": 2.725761908531189,
                  "gap_rejected_minus_accepted": 1.5164869915644326
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3841761350631714,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9685494890213012,
                  "rejected_mean_error": 2.2082438406944274,
                  "gap_rejected_minus_accepted": 1.2396943516731262
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9574392437934875,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.767618492603302,
                  "rejected_mean_error": 1.8619893889427186,
                  "gap_rejected_minus_accepted": 1.0943708963394165
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9851697130343089,
              "spearman": 0.9812120383668089,
              "auroc_top30_bad": 0.9857561904761905,
              "mae": 0.09433329328112304,
              "mse": 0.01730650684950789,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6883348603918832,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07082704466581345
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22488007209300995
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6828265101790428
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0359169001499813
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9743033513152168,
              "spearman": 0.9812732050388514,
              "auroc_top30_worst": 0.9894918095238094,
              "pairwise_seed_ranking": 0.892,
              "predicted_best_mean_error": 1.466058271408081,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.06273555231094363,
              "gap_to_oracle": 0.0032152493000030535,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8822098031044007
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.973949657036708
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1696188903808593
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.359115338910109
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.072144484519959,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4601812337239584,
                  "rejected_mean_error": 2.2233525133132934,
                  "gap_rejected_minus_accepted": 0.7631712795893351
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9016349911689758,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3586227643197222,
                  "rejected_mean_error": 2.0689885684857354,
                  "gap_rejected_minus_accepted": 0.7103658041660132
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5181805491447449,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1696188903808593,
                  "rejected_mean_error": 1.9033778329849242,
                  "gap_rejected_minus_accepted": 0.7337589426040649
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1812383830547333,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9745828320804876,
                  "rejected_mean_error": 1.7242033358190205,
                  "gap_rejected_minus_accepted": 0.749620503738533
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1088701248168946,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4540426095326742,
                  "rejected_mean_error": 2.2015547513961793,
                  "gap_rejected_minus_accepted": 0.7475121418635051
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9052537381649017,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3491518765209831,
                  "rejected_mean_error": 2.0620167463544816,
                  "gap_rejected_minus_accepted": 0.7128648698334985
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5292468070983887,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.157300033569336,
                  "rejected_mean_error": 1.9002876138687135,
                  "gap_rejected_minus_accepted": 0.7429875802993775
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1828704476356506,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9547674315316337,
                  "rejected_mean_error": 1.7221823943490013,
                  "gap_rejected_minus_accepted": 0.7674149628173677
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9696990598751551,
              "spearman": 0.9754255784032692,
              "auroc_top30_bad": 0.9868746666666667,
              "mae": 0.16737597336396576,
              "mse": 0.06468466353978804,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6937373556320615,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08141268187761307
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20975809586048128
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6947614863276481
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0533472202857335
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9367808160910519,
              "spearman": 0.9664926039117993,
              "auroc_top30_worst": 0.9876114285714286,
              "pairwise_seed_ranking": 0.9024,
              "predicted_best_mean_error": 1.7266157463788987,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08053283500671382,
              "gap_to_oracle": 0.0027289462089539196,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9479362716674805
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1151050294821079
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2909864416122436
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4625618113383556
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.18761305809021,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6574140061272515,
                  "rejected_mean_error": 3.107869819641113,
                  "gap_rejected_minus_accepted": 1.4504558135138617
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.893504798412323,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4620073091004167,
                  "rejected_mean_error": 2.821641008693951,
                  "gap_rejected_minus_accepted": 1.3596336995935343
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6091512441635132,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2909864416122436,
                  "rejected_mean_error": 2.3139327333450317,
                  "gap_rejected_minus_accepted": 1.022946291732788
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3288918733596802,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1159726712650384,
                  "rejected_mean_error": 2.0317769885190398,
                  "gap_rejected_minus_accepted": 0.9158043172540014
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.185541796684265,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6581968094242943,
                  "rejected_mean_error": 3.1477145290374757,
                  "gap_rejected_minus_accepted": 1.4895177196131815
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.925092339515686,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4623199132355778,
                  "rejected_mean_error": 2.830687643989684,
                  "gap_rejected_minus_accepted": 1.3683677307541062
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6148505806922913,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2879417788982392,
                  "rejected_mean_error": 2.326355383872986,
                  "gap_rejected_minus_accepted": 1.0384136049747466
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3320868611335754,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1152045968033018,
                  "rejected_mean_error": 2.0402633997208293,
                  "gap_rejected_minus_accepted": 0.9250588029175275
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9887319798910882,
              "spearman": 0.987262060900097,
              "auroc_top30_bad": 0.9957729523809523,
              "mae": 0.09765317434743047,
              "mse": 0.01724369391592324,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7361556509988293,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06366525584459305
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2064745512485504
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5899121875762939
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.934414047495524
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9840716169582182,
              "spearman": 0.9828737303511876,
              "auroc_top30_worst": 0.9955017142857143,
              "pairwise_seed_ranking": 0.9252,
              "predicted_best_mean_error": 1.5543056693077086,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06501660895347605,
              "gap_to_oracle": 0.003162409067153815,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5703779828548431
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8692156192010794
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1179430664539338
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.311932954357377
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.667644596099854,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4759307901859284,
                  "rejected_mean_error": 2.946726234436035,
                  "gap_rejected_minus_accepted": 1.4707954442501066
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.046817123889923,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3110078469220958,
                  "rejected_mean_error": 2.557024171558051,
                  "gap_rejected_minus_accepted": 1.2460163246359552
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.567103087902069,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1179430664539338,
                  "rejected_mean_error": 2.128077602767944,
                  "gap_rejected_minus_accepted": 1.0101345363140104
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2450053691864014,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8704213746629965,
                  "rejected_mean_error": 1.8744087812104118,
                  "gap_rejected_minus_accepted": 1.0039874065474153
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6293086051940913,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4680441996786329,
                  "rejected_mean_error": 2.9808249855041504,
                  "gap_rejected_minus_accepted": 1.5127807858255176
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0620186924934387,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.298858723857186,
                  "rejected_mean_error": 2.570539495301625,
                  "gap_rejected_minus_accepted": 1.2716807714444391
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5710186958312988,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.106168200969696,
                  "rejected_mean_error": 2.132476355552673,
                  "gap_rejected_minus_accepted": 1.026308154582977
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2277416586875916,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8540449416826642,
                  "rejected_mean_error": 1.877142985236836,
                  "gap_rejected_minus_accepted": 1.0230980435541719
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
        "best_epoch": 54,
        "best_calib_loss": 0.012053065933287144,
        "train_time_sec": 41.573434591293335,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9991537695840242,
              "spearman": 0.9983723364039819,
              "auroc_top30_bad": 0.9994500476190477,
              "mae": 0.031248380300356076,
              "mse": 0.001584774220490514,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7195274451477719,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08788344526523724
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23799417498800904
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5676709385727532
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9076725250465796
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2854957839774435
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999216810074903,
              "spearman": 0.9984680330907212,
              "auroc_top30_worst": 0.9995714285714286,
              "pairwise_seed_ranking": 0.9458,
              "predicted_best_mean_error": 1.5076642197072505,
              "seed0_mean_error": 1.5883966648578645,
              "random_seed_mean_error": 1.5829028643667697,
              "oracle_best_mean_error": 1.5042814255058765,
              "improvement_over_seed0": 0.08073244515061395,
              "gap_to_oracle": 0.0033827942013739953,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6421741892099381
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7740344908237458
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9734396826505661
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2061030483404795
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5820222539305686
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7903008699417122,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3743644057247373,
                  "rejected_mean_error": 3.4509428877830506,
                  "gap_rejected_minus_accepted": 2.0765784820583133
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9980892539024353,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2061030483404795,
                  "rejected_mean_error": 2.709779870700836,
                  "gap_rejected_minus_accepted": 1.5036768223603565
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3988766074180603,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9734396826505661,
                  "rejected_mean_error": 2.1906048252105714,
                  "gap_rejected_minus_accepted": 1.2171651425600052
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0013470351696014,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7740344908237458,
                  "rejected_mean_error": 1.8513515082995098,
                  "gap_rejected_minus_accepted": 1.077317017475764
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8565992355346683,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3809707016415067,
                  "rejected_mean_error": 3.4552303338050843,
                  "gap_rejected_minus_accepted": 2.0742596321635776
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.029706597328186,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2094088829358418,
                  "rejected_mean_error": 2.7253600106239317,
                  "gap_rejected_minus_accepted": 1.51595112768809
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4280713200569153,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9687259328365326,
                  "rejected_mean_error": 2.208067396879196,
                  "gap_rejected_minus_accepted": 1.2393414640426634
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9924865216016769,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7674214601516723,
                  "rejected_mean_error": 1.8620550664265951,
                  "gap_rejected_minus_accepted": 1.0946336062749227
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.977425902329824,
              "spearman": 0.978376993047953,
              "auroc_top30_bad": 0.9848822857142857,
              "mae": 0.1199633566584438,
              "mse": 0.026892389193173154,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6530512964653077,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09715309500694275
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23091022455692292
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6806474859595298
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.036974295449257
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9749613926956028,
              "spearman": 0.9771573552367074,
              "auroc_top30_worst": 0.9831862857142857,
              "pairwise_seed_ranking": 0.8756,
              "predicted_best_mean_error": 1.469907940864563,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.05888588285446161,
              "gap_to_oracle": 0.007064918756485072,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8769967703819275
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9790261876888764
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1693365787506103
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3611245898803923
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.066444563865662,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4596768867704604,
                  "rejected_mean_error": 2.2278916358947756,
                  "gap_rejected_minus_accepted": 0.7682147491243152
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8750647604465485,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.36066535531902,
                  "rejected_mean_error": 2.0628738471875177,
                  "gap_rejected_minus_accepted": 0.7022084918684977
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4490309953689575,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1693365787506103,
                  "rejected_mean_error": 1.9036601446151733,
                  "gap_rejected_minus_accepted": 0.734323565864563
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.094058245420456,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9796144611919269,
                  "rejected_mean_error": 1.722522546158529,
                  "gap_rejected_minus_accepted": 0.7429080849666021
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1110525369644164,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4521810404459636,
                  "rejected_mean_error": 2.2183088731765745,
                  "gap_rejected_minus_accepted": 0.7661278327306109
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8776533603668213,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3529286709698765,
                  "rejected_mean_error": 2.0508062612442743,
                  "gap_rejected_minus_accepted": 0.6978775902743979
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4706988334655762,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.15809774684906,
                  "rejected_mean_error": 1.8994899005889894,
                  "gap_rejected_minus_accepted": 0.7413921537399293
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.09204563498497,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9602464551017398,
                  "rejected_mean_error": 1.72033652009811,
                  "gap_rejected_minus_accepted": 0.7600900649963702
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9596636054415355,
              "spearman": 0.9678543885322107,
              "auroc_top30_bad": 0.991264,
              "mae": 0.20097110967114568,
              "mse": 0.0881381453879627,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6527947627073135,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10961601680517197
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2201018133878708
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7005768818736077
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.061367627199491
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9224249290644583,
              "spearman": 0.9461418642827932,
              "auroc_top30_worst": 0.9908571428571429,
              "pairwise_seed_ranking": 0.9108,
              "predicted_best_mean_error": 1.725755139231682,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08139344215393063,
              "gap_to_oracle": 0.001868339061737112,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9538700752258301
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1346168942176378
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2935172952651977
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.479068851928467
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1255525588989257,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6608111911349825,
                  "rejected_mean_error": 3.0772951545715332,
                  "gap_rejected_minus_accepted": 1.4164839634365507
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9154885411262512,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.477699556371064,
                  "rejected_mean_error": 2.7746645368326206,
                  "gap_rejected_minus_accepted": 1.2969649804615566
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5341870784759521,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2935172952651977,
                  "rejected_mean_error": 2.3114018796920774,
                  "gap_rejected_minus_accepted": 1.0178845844268798
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3086020350456238,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1346251301872083,
                  "rejected_mean_error": 2.0255462311629677,
                  "gap_rejected_minus_accepted": 0.8909211009757594
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1365895748138426,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6665135000811684,
                  "rejected_mean_error": 3.0728643131256104,
                  "gap_rejected_minus_accepted": 1.406350813044442
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9567139148712158,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4880066968221715,
                  "rejected_mean_error": 2.7544427466770958,
                  "gap_rejected_minus_accepted": 1.2664360498549243
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5179715752601624,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2913717000484466,
                  "rejected_mean_error": 2.3229254627227784,
                  "gap_rejected_minus_accepted": 1.0315537626743319
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3139323592185974,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1520370429470426,
                  "rejected_mean_error": 2.027854607704489,
                  "gap_rejected_minus_accepted": 0.8758175647574464
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9860307089647662,
              "spearman": 0.9844450714622014,
              "auroc_top30_bad": 0.9969180952380952,
              "mae": 0.11049899286162108,
              "mse": 0.022355607385022132,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6977552851855382,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.092173255443573
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21692659378051757
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5932609427928924
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9335862402598063
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9894444087302745,
              "spearman": 0.9816705377731444,
              "auroc_top30_worst": 0.9975923809523809,
              "pairwise_seed_ranking": 0.8972,
              "predicted_best_mean_error": 1.555609435558319,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.0637128427028657,
              "gap_to_oracle": 0.004466175317764165,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.569426057100296
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8804743355856492
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1160114870548248
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.311465377015854
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.574108672142029,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4750725928677453,
                  "rejected_mean_error": 2.9544500102996825,
                  "gap_rejected_minus_accepted": 1.4793774174319372
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.926285594701767,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3105856726301899,
                  "rejected_mean_error": 2.5582879968344594,
                  "gap_rejected_minus_accepted": 1.2477023242042695
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4112759828567505,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1160114870548248,
                  "rejected_mean_error": 2.1300091821670533,
                  "gap_rejected_minus_accepted": 1.0139976951122285
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1114468574523926,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8815796517145139,
                  "rejected_mean_error": 1.8706814165176424,
                  "gap_rejected_minus_accepted": 0.9891017648031285
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.541992712020874,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4676686607466805,
                  "rejected_mean_error": 2.9842048358917235,
                  "gap_rejected_minus_accepted": 1.516536175145043
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9493786096572876,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.300612145247944,
                  "rejected_mean_error": 2.5653348953004866,
                  "gap_rejected_minus_accepted": 1.2647227500525426
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4520359635353088,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1021490979194641,
                  "rejected_mean_error": 2.1364954586029055,
                  "gap_rejected_minus_accepted": 1.0343463606834413
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.103014886379242,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8632246757310534,
                  "rejected_mean_error": 1.8740503475627797,
                  "gap_rejected_minus_accepted": 1.0108256718317263
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
        "best_epoch": 59,
        "best_calib_loss": 0.010512970387935638,
        "train_time_sec": 29.21320343017578,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9991828189630496,
              "spearman": 0.9983211153873004,
              "auroc_top30_bad": 0.9996466666666666,
              "mae": 0.03943391740205698,
              "mse": 0.002702569387155025,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7472301463405687,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09041327296430245
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2377693589637056
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.567390022191871
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9075070089561865
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2854957839774435
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9994777664603152,
              "spearman": 0.9992641851704968,
              "auroc_top30_worst": 0.9995674285714286,
              "pairwise_seed_ranking": 0.9546,
              "predicted_best_mean_error": 1.5052509963810443,
              "seed0_mean_error": 1.5883966648578645,
              "random_seed_mean_error": 1.5829028643667697,
              "oracle_best_mean_error": 1.5042814255058765,
              "improvement_over_seed0": 0.08314566847682014,
              "gap_to_oracle": 0.0009695708751678023,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6397275590896606
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7735278880596161
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9732486979722976
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2058953743139902
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5820222539305686
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.812253952026367,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3743865907324686,
                  "rejected_mean_error": 3.4507432227134704,
                  "gap_rejected_minus_accepted": 2.076356631981002
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9839368760585785,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2058953743139902,
                  "rejected_mean_error": 2.710402892780304,
                  "gap_rejected_minus_accepted": 1.504507518466314
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.397604763507843,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9732486979722976,
                  "rejected_mean_error": 2.1907958098888396,
                  "gap_rejected_minus_accepted": 1.217547111916542
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0006056725978851,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7735278880596161,
                  "rejected_mean_error": 1.851520375887553,
                  "gap_rejected_minus_accepted": 1.0779924878279368
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.835816073417664,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.381026578479343,
                  "rejected_mean_error": 3.454727442264557,
                  "gap_rejected_minus_accepted": 2.073700863785214
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.002825617790222,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2093157496452331,
                  "rejected_mean_error": 2.725639410495758,
                  "gap_rejected_minus_accepted": 1.5163236608505248
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4096046090126038,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9687500295639038,
                  "rejected_mean_error": 2.208043300151825,
                  "gap_rejected_minus_accepted": 1.2392932705879214
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9970150738954544,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7672995061874389,
                  "rejected_mean_error": 1.8620957177480062,
                  "gap_rejected_minus_accepted": 1.0947962115605674
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9798913230420226,
              "spearman": 0.9764313146438153,
              "auroc_top30_bad": 0.9818979047619049,
              "mae": 0.10986828247588128,
              "mse": 0.02330923330437976,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6878388460306164,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05276931196451187
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22731219856739043
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6825760595679283
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0399572129805883
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.966316151784618,
              "spearman": 0.9716157033060502,
              "auroc_top30_worst": 0.9828571428571429,
              "pairwise_seed_ranking": 0.876,
              "predicted_best_mean_error": 1.4694536423683167,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.059340181350707955,
              "gap_to_oracle": 0.006610620260238731,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8734354286193847
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9825931233473313
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1708947460174561
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3623384619826702
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1054663419723516,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4623196725845338,
                  "rejected_mean_error": 2.204106563568115,
                  "gap_rejected_minus_accepted": 0.7417868909835814
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9383375942707062,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3613784034580405,
                  "rejected_mean_error": 2.0607392589885967,
                  "gap_rejected_minus_accepted": 0.6993608555305562
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.491795301437378,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1708947460174561,
                  "rejected_mean_error": 1.9021019773483276,
                  "gap_rejected_minus_accepted": 0.7312072313308715
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1210599839687347,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.983061608034201,
                  "rejected_mean_error": 1.7213710445986232,
                  "gap_rejected_minus_accepted": 0.7383094365644223
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.143157696723938,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4560610347323948,
                  "rejected_mean_error": 2.183388924598694,
                  "gap_rejected_minus_accepted": 0.7273278898662991
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.94496089220047,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3508515753210548,
                  "rejected_mean_error": 2.0569716086463323,
                  "gap_rejected_minus_accepted": 0.7061200333252775
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4980989694595337,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1620485792160034,
                  "rejected_mean_error": 1.8955390682220459,
                  "gap_rejected_minus_accepted": 0.7334904890060425
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1241053342819214,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9625803042971899,
                  "rejected_mean_error": 1.719550250048306,
                  "gap_rejected_minus_accepted": 0.7569699457511161
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9524918996640419,
              "spearman": 0.9562627219562188,
              "auroc_top30_bad": 0.9752502857142857,
              "mae": 0.1992709893392399,
              "mse": 0.10528818808243359,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6751321687991181,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09228761547803879
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20577734858989716
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6983575667262077
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0864689411083857
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8847675976291607,
              "spearman": 0.9354620310156999,
              "auroc_top30_worst": 0.9616182857142858,
              "pairwise_seed_ranking": 0.9168,
              "predicted_best_mean_error": 1.7270581825971603,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08009039878845226,
              "gap_to_oracle": 0.0031713824272154856,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9405301074981689
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1230181768918648
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2954545572280884
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.51664694209597
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9814671158790589,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6731425310770671,
                  "rejected_mean_error": 2.9663130950927736,
                  "gap_rejected_minus_accepted": 1.2931705640157065
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8013093173503876,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.515220020216837,
                  "rejected_mean_error": 2.662342892668118,
                  "gap_rejected_minus_accepted": 1.1471228724512808
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5249769687652588,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2954545572280884,
                  "rejected_mean_error": 2.309464617729187,
                  "gap_rejected_minus_accepted": 1.0140100605010987
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2913353443145752,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1241854177877164,
                  "rejected_mean_error": 2.0290335630530865,
                  "gap_rejected_minus_accepted": 0.90484814526537
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9878210783004762,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6897353785567812,
                  "rejected_mean_error": 2.8638674068450927,
                  "gap_rejected_minus_accepted": 1.1741320282883114
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8087846338748932,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.518132509872875,
                  "rejected_mean_error": 2.6650216825424677,
                  "gap_rejected_minus_accepted": 1.1468891726695927
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5262460112571716,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2905187604427337,
                  "rejected_mean_error": 2.3237784023284913,
                  "gap_rejected_minus_accepted": 1.0332596418857576
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.318730652332306,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1302002039220598,
                  "rejected_mean_error": 2.035211403739644,
                  "gap_rejected_minus_accepted": 0.905011199817584
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9878693639102396,
              "spearman": 0.985684046366112,
              "auroc_top30_bad": 0.996104380952381,
              "mae": 0.10092695673173294,
              "mse": 0.019743691683662704,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7085238551533192,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0675785534977913
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21394155073165894
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5908629325866699
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9336930378595988
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9899241992558347,
              "spearman": 0.9843115378633843,
              "auroc_top30_worst": 0.9982933333333334,
              "pairwise_seed_ranking": 0.8996,
              "predicted_best_mean_error": 1.5555007864236832,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06382149183750152,
              "gap_to_oracle": 0.004357526183128346,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5757869293689728
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8807102530621566
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1158375307559967
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3095693206037287
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5400048017501837,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4755466438134512,
                  "rejected_mean_error": 2.95018355178833,
                  "gap_rejected_minus_accepted": 1.474636907974879
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0152854919433594,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.308664814671432,
                  "rejected_mean_error": 2.564038296857962,
                  "gap_rejected_minus_accepted": 1.2553734821865299
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4399506449699402,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1158375307559967,
                  "rejected_mean_error": 2.130183138465881,
                  "gap_rejected_minus_accepted": 1.0143456077098845
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1998436450958252,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.882604244894113,
                  "rejected_mean_error": 1.8703391564693879,
                  "gap_rejected_minus_accepted": 0.9877349115752748
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.525813031196594,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4676686607466805,
                  "rejected_mean_error": 2.9842048358917235,
                  "gap_rejected_minus_accepted": 1.516536175145043
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.025388181209564,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2980891290832968,
                  "rejected_mean_error": 2.572823848043169,
                  "gap_rejected_minus_accepted": 1.2747347189598723
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.456411898136139,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1036498618125916,
                  "rejected_mean_error": 2.134994694709778,
                  "gap_rejected_minus_accepted": 1.0313448328971864
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2033683359622955,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8670881617636907,
                  "rejected_mean_error": 1.8727487453164902,
                  "gap_rejected_minus_accepted": 1.0056605835527994
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
        "best_epoch": 68,
        "best_calib_loss": 0.09565206617116928,
        "train_time_sec": 10.858550548553467,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8984749133482505,
              "spearman": 0.8487240436437085,
              "auroc_top30_bad": 0.9217149523809525,
              "mae": 0.1762375010588672,
              "mse": 0.1564293066725201,
              "expert_lt_perturb_large": 0.983,
              "expert_lt_other_task": 0.53,
              "expert_lt_simvla_seed0": 0.97,
              "same_context_pred_std": 0.6898233956192539,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4010683890003711
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4766911959247664
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6346330489945597
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9081001825323328
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2657154838076328
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9971014005589931,
              "spearman": 0.9960360872893484,
              "auroc_top30_worst": 0.9988314285714286,
              "pairwise_seed_ranking": 0.8582,
              "predicted_best_mean_error": 1.5066342415511609,
              "seed0_mean_error": 1.5817216905951499,
              "random_seed_mean_error": 1.5773716281354426,
              "oracle_best_mean_error": 1.4989939597547055,
              "improvement_over_seed0": 0.07508744904398901,
              "gap_to_oracle": 0.007640281796455373,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6429033037424088
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7698696933269501
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9665574411153793
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2008339842637379
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.576842271912098
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.706009697914124,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3690229241185718,
                  "rejected_mean_error": 3.447216402053833,
                  "gap_rejected_minus_accepted": 2.078193477935261
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9439513683319092,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2008339842637379,
                  "rejected_mean_error": 2.7048671348571776,
                  "gap_rejected_minus_accepted": 1.5040331505934397
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.356737732887268,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9665574411153793,
                  "rejected_mean_error": 2.1871271027088164,
                  "gap_rejected_minus_accepted": 1.2205696615934372
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9796531498432159,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7698696933269501,
                  "rejected_mean_error": 1.8458331314404806,
                  "gap_rejected_minus_accepted": 1.0759634381135306
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7165956258773805,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3739774517880545,
                  "rejected_mean_error": 3.4514198398590086,
                  "gap_rejected_minus_accepted": 2.077442388070954
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9535497426986694,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2018242531617482,
                  "rejected_mean_error": 2.7214140028953553,
                  "gap_rejected_minus_accepted": 1.519589749733607
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.367137849330902,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9577986892461777,
                  "rejected_mean_error": 2.2056446919441224,
                  "gap_rejected_minus_accepted": 1.2478460026979445
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9665562212467194,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7618976910114288,
                  "rejected_mean_error": 1.854996357123057,
                  "gap_rejected_minus_accepted": 1.0930986661116282
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5141655447014574,
              "spearman": 0.4836322746656225,
              "auroc_top30_bad": 0.6591531428571429,
              "mae": 0.48859289412498474,
              "mse": 0.5375266858639407,
              "expert_lt_perturb_large": 0.972,
              "expert_lt_other_task": 0.46,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.6128981905012322,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5052451729178429
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7882715206861496
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.948150908946991
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1790320019960403
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.39699060417931775,
              "spearman": 0.4398497552034526,
              "auroc_top30_worst": 0.7011824761904761,
              "pairwise_seed_ranking": 0.7496,
              "predicted_best_mean_error": 1.485618510246277,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.04317531347274772,
              "gap_to_oracle": 0.022775488138198963,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9799392733573914
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.181955758195657
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3740967589378357
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4932849391945389
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.039615774154664,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5253178497420417,
                  "rejected_mean_error": 1.6371229691505431,
                  "gap_rejected_minus_accepted": 0.11180511940850146
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7651375234127045,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.493392827798361,
                  "rejected_mean_error": 1.6655395286151777,
                  "gap_rejected_minus_accepted": 0.1721467008168167
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5560898184776306,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3740967589378357,
                  "rejected_mean_error": 1.698899964427948,
                  "gap_rejected_minus_accepted": 0.32480320549011243
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2370950281620026,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1838544237727937,
                  "rejected_mean_error": 1.6542972438236183,
                  "gap_rejected_minus_accepted": 0.4704428200508246
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.081375765800476,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.520583667755127,
                  "rejected_mean_error": 1.602685227394104,
                  "gap_rejected_minus_accepted": 0.08210155963897692
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7682667672634125,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.486873821778731,
                  "rejected_mean_error": 1.6532230358275155,
                  "gap_rejected_minus_accepted": 0.16634921404878455
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5499134063720703,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3593247241973876,
                  "rejected_mean_error": 1.6982629232406616,
                  "gap_rejected_minus_accepted": 0.33893819904327405
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.201572448015213,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1472597453329298,
                  "rejected_mean_error": 1.6573320426405433,
                  "gap_rejected_minus_accepted": 0.5100722973076135
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.41992038084391814,
              "spearman": 0.3497118071120633,
              "auroc_top30_bad": 0.5295352380952381,
              "mae": 0.6623741514742374,
              "mse": 0.8374823550317163,
              "expert_lt_perturb_large": 0.952,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 0.852,
              "same_context_pred_std": 0.6186558952704654,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5444524340033531
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5683018968105317
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2344633990764617
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3257910150925318
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.05132280782005327,
              "spearman": -0.17935486603860337,
              "auroc_top30_worst": 0.26615619047619044,
              "pairwise_seed_ranking": 0.7112,
              "predicted_best_mean_error": 1.7552353435754775,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.051913237810135016,
              "gap_to_oracle": 0.031348543405532725,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 2.2845090334415437
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.130593123535315
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.9328988687515258
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7950347513278155
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.696268320083619,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7486817205217149,
                  "rejected_mean_error": 2.2864603900909426,
                  "gap_rejected_minus_accepted": 0.5377786695692277
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8578498661518097,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7952584407372816,
                  "rejected_mean_error": 1.824017013985509,
                  "gap_rejected_minus_accepted": 0.028758573248227393
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3740574717521667,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.9328988687515258,
                  "rejected_mean_error": 1.6720203062057495,
                  "gap_rejected_minus_accepted": -0.26087856254577635
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.139537125825882,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.1268826831643954,
                  "rejected_mean_error": 1.6940877316092224,
                  "gap_rejected_minus_accepted": -0.432794951555173
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.63017098903656,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7481526039706337,
                  "rejected_mean_error": 2.3381123781204223,
                  "gap_rejected_minus_accepted": 0.5899597741497886
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.891031175851822,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7936271089602283,
                  "rejected_mean_error": 1.8472837455688962,
                  "gap_rejected_minus_accepted": 0.05365663660866793
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.36981999874115,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.937286981344223,
                  "rejected_mean_error": 1.677010181427002,
                  "gap_rejected_minus_accepted": -0.2602767999172211
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1493638157844543,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.1381038479388708,
                  "rejected_mean_error": 1.6956502830280977,
                  "gap_rejected_minus_accepted": -0.44245356491077303
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6619378509639882,
              "spearman": 0.6441975238294758,
              "auroc_top30_bad": 0.8087135238095238,
              "mae": 0.45710694732666013,
              "mse": 0.42572815010071324,
              "expert_lt_perturb_large": 0.976,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.94,
              "same_context_pred_std": 0.6576918414106804,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.44109796118736266
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6748522528648376
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8086096648812294
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0302521906296411
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7087832676885579,
              "spearman": 0.621701445184925,
              "auroc_top30_worst": 0.8752883809523809,
              "pairwise_seed_ranking": 0.7876,
              "predicted_best_mean_error": 1.5641210887432098,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.055201189517974925,
              "gap_to_oracle": 0.012977828502654942,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.764693773984909
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0965551284070199
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2816167286396027
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3921194413641114
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4043575048446657,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5151466830836402,
                  "rejected_mean_error": 2.5937831983566286,
                  "gap_rejected_minus_accepted": 1.0786365152729884
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0615511536598206,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3922166869187431,
                  "rejected_mean_error": 2.3139165578939664,
                  "gap_rejected_minus_accepted": 0.9216998709752233
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6952462792396545,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2816167286396027,
                  "rejected_mean_error": 1.9644039405822753,
                  "gap_rejected_minus_accepted": 0.6827872119426726
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2890335619449615,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0972001210759623,
                  "rejected_mean_error": 1.7986545147992503,
                  "gap_rejected_minus_accepted": 0.701454393723288
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4397021293640138,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5081743560896979,
                  "rejected_mean_error": 2.6196535778045655,
                  "gap_rejected_minus_accepted": 1.1114792217148677
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0861855149269104,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3743190446639444,
                  "rejected_mean_error": 2.3465540986212474,
                  "gap_rejected_minus_accepted": 0.972235053957303
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.714170753955841,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2725559349060058,
                  "rejected_mean_error": 1.9660886216163636,
                  "gap_rejected_minus_accepted": 0.6935326867103577
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.232682704925537,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.030544690669529,
                  "rejected_mean_error": 1.8176805029578387,
                  "gap_rejected_minus_accepted": 0.7871358122883096
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
        "best_epoch": 71,
        "best_calib_loss": 0.011281532235443592,
        "train_time_sec": 35.06679344177246,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994427378476941,
              "spearman": 0.9988228342808259,
              "auroc_top30_bad": 0.9996451904761905,
              "mae": 0.0233388185122516,
              "mse": 0.0008763614109204424,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7097462484386405,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08571951360115782
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2304814625347033
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5481011060935446
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8856732044049228
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2657154838076328
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9993855121122036,
              "spearman": 0.9987116080204334,
              "auroc_top30_worst": 0.9998293333333333,
              "pairwise_seed_ranking": 0.947,
              "predicted_best_mean_error": 1.500899672985077,
              "seed0_mean_error": 1.5817216905951499,
              "random_seed_mean_error": 1.5773716281354426,
              "oracle_best_mean_error": 1.4989939597547055,
              "improvement_over_seed0": 0.0808220176100729,
              "gap_to_oracle": 0.0019057132303714752,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6370489000082016
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7679134915828705
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9654570185899735
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.199353719441096
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.576842271912098
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7610648155212405,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3687029851410124,
                  "rejected_mean_error": 3.4500958528518675,
                  "gap_rejected_minus_accepted": 2.0813928677108553
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9591761827468872,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.199353719441096,
                  "rejected_mean_error": 2.709307929325104,
                  "gap_rejected_minus_accepted": 1.509954209884008
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3498848676681519,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9654570185899735,
                  "rejected_mean_error": 2.1882275252342223,
                  "gap_rejected_minus_accepted": 1.222770506644249
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9697864651679993,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7679134915828705,
                  "rejected_mean_error": 1.8464851986885071,
                  "gap_rejected_minus_accepted": 1.0785717071056367
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8198184967041016,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3736886437071694,
                  "rejected_mean_error": 3.454019112586975,
                  "gap_rejected_minus_accepted": 2.0803304688798057
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9865658581256866,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2007852493127187,
                  "rejected_mean_error": 2.724531014442444,
                  "gap_rejected_minus_accepted": 1.5237457651297253
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3586915731430054,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9574912739992142,
                  "rejected_mean_error": 2.2059521071910857,
                  "gap_rejected_minus_accepted": 1.2484608331918716
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9626419842243195,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7606290214061737,
                  "rejected_mean_error": 1.8554192469914754,
                  "gap_rejected_minus_accepted": 1.0947902255853017
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9787142385507469,
              "spearman": 0.971946807719575,
              "auroc_top30_bad": 0.9772685714285715,
              "mae": 0.11256747981607913,
              "mse": 0.025739977891246518,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6677816570229563,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07841335642337799
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22624371392726897
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6873012577414512
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0392640484730402
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9627680532572638,
              "spearman": 0.9653161946343647,
              "auroc_top30_worst": 0.97984,
              "pairwise_seed_ranking": 0.8952,
              "predicted_best_mean_error": 1.4666443147659303,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.062149508953094346,
              "gap_to_oracle": 0.00380129265785234,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8794582571983337
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9837715679254287
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1751727478027343
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3606878118728525
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0782953262329102,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.462558878580729,
                  "rejected_mean_error": 2.201953709602356,
                  "gap_rejected_minus_accepted": 0.739394831021627
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9037374556064606,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3600252890917637,
                  "rejected_mean_error": 2.0647899559892404,
                  "gap_rejected_minus_accepted": 0.7047646668974767
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4505203366279602,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1751727478027343,
                  "rejected_mean_error": 1.8978239755630493,
                  "gap_rejected_minus_accepted": 0.722651227760315
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.159065455198288,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9843331613479712,
                  "rejected_mean_error": 1.7209462887958376,
                  "gap_rejected_minus_accepted": 0.7366131274478663
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1057029008865356,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4550624879201253,
                  "rejected_mean_error": 2.1923758459091185,
                  "gap_rejected_minus_accepted": 0.7373133579889932
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9035764038562775,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3497845457199422,
                  "rejected_mean_error": 2.0601388234940785,
                  "gap_rejected_minus_accepted": 0.7103542777741363
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4492840766906738,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1615294914245606,
                  "rejected_mean_error": 1.8960581560134888,
                  "gap_rejected_minus_accepted": 0.7345286645889282
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1572857201099396,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9593023875403026,
                  "rejected_mean_error": 1.7206545749450113,
                  "gap_rejected_minus_accepted": 0.7613521874047087
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9640288689192796,
              "spearman": 0.9673385380732011,
              "auroc_top30_bad": 0.9757630476190475,
              "mae": 0.18561316556334495,
              "mse": 0.07978306358911459,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6789153855414468,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08646393233537673
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20937930066585542
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6965165819048882
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0608932029008866
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9228438073857634,
              "spearman": 0.9589603884546487,
              "auroc_top30_worst": 0.9737020952380953,
              "pairwise_seed_ranking": 0.9072,
              "predicted_best_mean_error": 1.7266060127019882,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.0805425686836243,
              "gap_to_oracle": 0.0027192125320434357,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9442235231399536
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1160848018450615
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3038798795700073
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.468629975690008
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1404317140579225,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6546530831654866,
                  "rejected_mean_error": 3.132718126296997,
                  "gap_rejected_minus_accepted": 1.4780650431315103
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8446708917617798,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4681045631207168,
                  "rejected_mean_error": 2.803388206722637,
                  "gap_rejected_minus_accepted": 1.3352836436019204
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5629513263702393,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3038798795700073,
                  "rejected_mean_error": 2.3010392953872683,
                  "gap_rejected_minus_accepted": 0.997159415817261
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3280499279499054,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1167578487731398,
                  "rejected_mean_error": 2.031514704036611,
                  "gap_rejected_minus_accepted": 0.9147568552634711
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.131843090057373,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6586058043109047,
                  "rejected_mean_error": 3.1440335750579833,
                  "gap_rejected_minus_accepted": 1.4854277707470787
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8766788244247437,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4709583589418687,
                  "rejected_mean_error": 2.8050465432424394,
                  "gap_rejected_minus_accepted": 1.3340881843005707
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5649560689926147,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3030261075496674,
                  "rejected_mean_error": 2.3112710552215576,
                  "gap_rejected_minus_accepted": 1.0082449476718902
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3333658277988434,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1169644721916743,
                  "rejected_mean_error": 2.0396705005258164,
                  "gap_rejected_minus_accepted": 0.9227060283341422
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9867856769507382,
              "spearman": 0.9863875030580324,
              "auroc_top30_bad": 0.9955100952380952,
              "mae": 0.0998424421414733,
              "mse": 0.019083044202241082,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7186917276194287,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06520222622156144
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20649156403541566
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5907195605278015
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9345507717768351
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9825286205623576,
              "spearman": 0.9831849794463869,
              "auroc_top30_worst": 0.9959131428571428,
              "pairwise_seed_ranking": 0.9232,
              "predicted_best_mean_error": 1.5536209207773208,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06570135748386385,
              "gap_to_oracle": 0.002477660536766013,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5697630636692047
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8669119520256152
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1176135944843293
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3123429809361378
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.602771496772767,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.47717037902938,
                  "rejected_mean_error": 2.935569934844971,
                  "gap_rejected_minus_accepted": 1.4583995558155909
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0550084114074707,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3115553157751945,
                  "rejected_mean_error": 2.5553852632022895,
                  "gap_rejected_minus_accepted": 1.243829947427095
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5462104082107544,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1176135944843293,
                  "rejected_mean_error": 2.1284070747375488,
                  "gap_rejected_minus_accepted": 1.0107934802532195
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2141553461551666,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8681243594271687,
                  "rejected_mean_error": 1.8751760872603735,
                  "gap_rejected_minus_accepted": 1.007051727833205
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.581571102142334,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4691338721911114,
                  "rejected_mean_error": 2.971017932891846,
                  "gap_rejected_minus_accepted": 1.5018840607007344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.063352346420288,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2992682020294475,
                  "rejected_mean_error": 2.5693240600918967,
                  "gap_rejected_minus_accepted": 1.2700558580624492
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5587292909622192,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1075903334617614,
                  "rejected_mean_error": 2.131054223060608,
                  "gap_rejected_minus_accepted": 1.0234638895988466
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.205785483121872,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8530485544885907,
                  "rejected_mean_error": 1.8774786664840373,
                  "gap_rejected_minus_accepted": 1.0244301119954464
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
        "best_epoch": 62,
        "best_calib_loss": 0.012782910838723183,
        "train_time_sec": 41.649335861206055,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9984282025390563,
              "spearman": 0.9977688417548022,
              "auroc_top30_bad": 0.9989500476190477,
              "mae": 0.049057424998888745,
              "mse": 0.004535426337874307,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.991,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7293633872334339,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08744297294924036
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23053355868700892
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5485667851013132
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8861307755140587
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2657154838076328
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979088969689868,
              "spearman": 0.9976291100810504,
              "auroc_top30_worst": 0.9983245714285713,
              "pairwise_seed_ranking": 0.9479,
              "predicted_best_mean_error": 1.5013395314514637,
              "seed0_mean_error": 1.5817216905951499,
              "random_seed_mean_error": 1.5773716281354426,
              "oracle_best_mean_error": 1.4989939597547055,
              "improvement_over_seed0": 0.08038215914368618,
              "gap_to_oracle": 0.0023455716967581974,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6394662075042724
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7679481491565704
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9656473901987076
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1999988374233246
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.576842271912098
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.822018313407898,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3690162033107545,
                  "rejected_mean_error": 3.447276889324188,
                  "gap_rejected_minus_accepted": 2.078260686013434
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0206111073493958,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1999988374233246,
                  "rejected_mean_error": 2.707372575378418,
                  "gap_rejected_minus_accepted": 1.5073737379550936
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.413805067539215,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9656473901987076,
                  "rejected_mean_error": 2.1880371536254883,
                  "gap_rejected_minus_accepted": 1.2223897634267806
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0228191614151,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7679481491565704,
                  "rejected_mean_error": 1.8464736461639404,
                  "gap_rejected_minus_accepted": 1.0785254970073699
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.84569833278656,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3738041204214095,
                  "rejected_mean_error": 3.4529798221588135,
                  "gap_rejected_minus_accepted": 2.079175701737404
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0361328721046448,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2011163618564606,
                  "rejected_mean_error": 2.723537676811218,
                  "gap_rejected_minus_accepted": 1.5224213149547574
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4193172454833984,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9574474371671676,
                  "rejected_mean_error": 2.2059959440231323,
                  "gap_rejected_minus_accepted": 1.2485485068559647
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0022986084222794,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7600079061985016,
                  "rejected_mean_error": 1.8556262853940328,
                  "gap_rejected_minus_accepted": 1.0956183791955314
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9740147680808049,
              "spearman": 0.9693757385581879,
              "auroc_top30_bad": 0.972680380952381,
              "mae": 0.12190374819003046,
              "mse": 0.030773038432163474,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6686692422335186,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0856516324877739
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24480050365924835
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6851098042845726
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0413772457997004
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.976493382130223,
              "spearman": 0.9756114071113007,
              "auroc_top30_worst": 0.978855619047619,
              "pairwise_seed_ranking": 0.884,
              "predicted_best_mean_error": 1.4683759396076201,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.060417884111404474,
              "gap_to_oracle": 0.0055329174995422115,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8686472406387329
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9756689025805547
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1701238086700438
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3632050377727827
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.095840883255005,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4600193996429442,
                  "rejected_mean_error": 2.2248090200424193,
                  "gap_rejected_minus_accepted": 0.7647896203994751
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9127063751220703,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3627212997943385,
                  "rejected_mean_error": 2.0567191507869635,
                  "gap_rejected_minus_accepted": 0.693997850992625
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.474584698677063,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1701238086700438,
                  "rejected_mean_error": 1.9028729146957397,
                  "gap_rejected_minus_accepted": 0.7327491060256959
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1216241717338562,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9765542604671881,
                  "rejected_mean_error": 1.7235447903707417,
                  "gap_rejected_minus_accepted": 0.7469905299035536
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1053656339645386,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4542925919426812,
                  "rejected_mean_error": 2.199304909706116,
                  "gap_rejected_minus_accepted": 0.7450123177634347
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9128711819648743,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3554045102175545,
                  "rejected_mean_error": 2.043457341572595,
                  "gap_rejected_minus_accepted": 0.6880528313550407
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4683898091316223,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1582814455032349,
                  "rejected_mean_error": 1.8993062019348144,
                  "gap_rejected_minus_accepted": 0.7410247564315795
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1271346807479858,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9559155191693988,
                  "rejected_mean_error": 1.72179560546569,
                  "gap_rejected_minus_accepted": 0.7658800862962912
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9550991916550895,
              "spearman": 0.9587637855353517,
              "auroc_top30_bad": 0.9769790476190476,
              "mae": 0.20001687084287406,
              "mse": 0.10172283657594622,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6754225890259311,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07775955617427827
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21265730278491973
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7027697511553764
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0767308622280756
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8953689836179206,
              "spearman": 0.9487130131923286,
              "auroc_top30_worst": 0.9786666666666666,
              "pairwise_seed_ranking": 0.9188,
              "predicted_best_mean_error": 1.7264624074697494,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08068617391586308,
              "gap_to_oracle": 0.002575607299804661,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9477774133682251
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1209671050310135
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2905149969100953
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.496691847279636
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0329822301864624,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6773760611216226,
                  "rejected_mean_error": 2.9282113246917723,
                  "gap_rejected_minus_accepted": 1.2508352635701496
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8368075489997864,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4953566530089242,
                  "rejected_mean_error": 2.7218060718176846,
                  "gap_rejected_minus_accepted": 1.2264494188087605
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5201826691627502,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2905149969100953,
                  "rejected_mean_error": 2.3144041780471802,
                  "gap_rejected_minus_accepted": 1.023889181137085
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.306904822587967,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1217544482538875,
                  "rejected_mean_error": 2.029845615842935,
                  "gap_rejected_minus_accepted": 0.9080911675890477
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.028835582733154,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6905264672968123,
                  "rejected_mean_error": 2.8567476081848144,
                  "gap_rejected_minus_accepted": 1.166221140888002
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.831721156835556,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.498153117091898,
                  "rejected_mean_error": 2.724325594447908,
                  "gap_rejected_minus_accepted": 1.22617247735601
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4988108277320862,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2871749999523163,
                  "rejected_mean_error": 2.3271221628189087,
                  "gap_rejected_minus_accepted": 1.0399471628665924
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3265184462070465,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1159418967981187,
                  "rejected_mean_error": 2.0400150045354097,
                  "gap_rejected_minus_accepted": 0.924073107737291
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9860468966013607,
              "spearman": 0.9847000678953118,
              "auroc_top30_bad": 0.9954963809523809,
              "mae": 0.1177468586307019,
              "mse": 0.023940679439961348,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6986578838825983,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08783976286649704
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21780186905860902
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5910121936798096
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9340496702194214
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9876236831218033,
              "spearman": 0.9825125980880629,
              "auroc_top30_worst": 0.997184,
              "pairwise_seed_ranking": 0.8976,
              "predicted_best_mean_error": 1.5553452234268188,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06397705483436589,
              "gap_to_oracle": 0.0042019631862639795,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5713494098186493
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.87904896080876
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1162839498996735
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3099456653475507
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6583778142929093,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.475006054798762,
                  "rejected_mean_error": 2.955048852920532,
                  "gap_rejected_minus_accepted": 1.48004279812177
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9836395382881165,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3091554416854456,
                  "rejected_mean_error": 2.5625695508128157,
                  "gap_rejected_minus_accepted": 1.25341410912737
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.404136061668396,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1162839498996735,
                  "rejected_mean_error": 2.1297367193222048,
                  "gap_rejected_minus_accepted": 1.0134527694225313
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.137350857257843,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8808306471798748,
                  "rejected_mean_error": 1.8709316176055208,
                  "gap_rejected_minus_accepted": 0.990100970425646
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6322841882705688,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4682978632715014,
                  "rejected_mean_error": 2.978542013168335,
                  "gap_rejected_minus_accepted": 1.5102441498968335
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9964444935321808,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.297854286145399,
                  "rejected_mean_error": 2.573520921525501,
                  "gap_rejected_minus_accepted": 1.275666635380102
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4349443912506104,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1043741221427918,
                  "rejected_mean_error": 2.1342704343795775,
                  "gap_rejected_minus_accepted": 1.0298963122367857
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.137350857257843,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8607311371773009,
                  "rejected_mean_error": 1.8748904167012097,
                  "gap_rejected_minus_accepted": 1.0141592795239087
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
        "best_epoch": 34,
        "best_calib_loss": 0.012909093871712685,
        "train_time_sec": 29.17780590057373,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9989071139288419,
              "spearman": 0.998038410838707,
              "auroc_top30_bad": 0.9995415714285715,
              "mae": 0.058234692851128055,
              "mse": 0.005005972583205025,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.997,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7458408597159407,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08961532638082281
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2305208410108462
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5480747310620733
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8857641840764011
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2657154838076328
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9991558850564553,
              "spearman": 0.9988113572803972,
              "auroc_top30_worst": 0.9996707619047619,
              "pairwise_seed_ranking": 0.9355,
              "predicted_best_mean_error": 1.5013834279179572,
              "seed0_mean_error": 1.5817216905951499,
              "random_seed_mean_error": 1.5773716281354426,
              "oracle_best_mean_error": 1.4989939597547055,
              "improvement_over_seed0": 0.08033826267719268,
              "gap_to_oracle": 0.0023894681632516956,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6369818376302719
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.767609221458435
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9653787006139756
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1997171795686086
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.576842271912098
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.84950909614563,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3688022874328825,
                  "rejected_mean_error": 3.449202132225037,
                  "gap_rejected_minus_accepted": 2.0803998447921543
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0340664386749268,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1997171795686086,
                  "rejected_mean_error": 2.708217548942566,
                  "gap_rejected_minus_accepted": 1.5085003693739574
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4117698669433594,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9653787006139756,
                  "rejected_mean_error": 2.1883058432102205,
                  "gap_rejected_minus_accepted": 1.222927142596245
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0154474079608917,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.767609221458435,
                  "rejected_mean_error": 1.846586622063319,
                  "gap_rejected_minus_accepted": 1.078977400604884
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8968531847000123,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3738151788049273,
                  "rejected_mean_error": 3.4528802967071535,
                  "gap_rejected_minus_accepted": 2.079065117902226
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.057871639728546,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2009355460007984,
                  "rejected_mean_error": 2.7240801243782045,
                  "gap_rejected_minus_accepted": 1.523144578377406
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.424451231956482,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9575071431398392,
                  "rejected_mean_error": 2.205936238050461,
                  "gap_rejected_minus_accepted": 1.2484290949106218
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0010143220424652,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7596597466468811,
                  "rejected_mean_error": 1.8557423385779064,
                  "gap_rejected_minus_accepted": 1.0960825919310253
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9735873535816768,
              "spearman": 0.9682313942216776,
              "auroc_top30_bad": 0.9734384761904762,
              "mae": 0.12177586820032447,
              "mse": 0.031049898236131628,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6845628033849497,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.058792939484119414
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23198386480808258
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6872458845496178
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0411362119277319
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9638473231966966,
              "spearman": 0.9685683756597605,
              "auroc_top30_worst": 0.9836464761904762,
              "pairwise_seed_ranking": 0.876,
              "predicted_best_mean_error": 1.4698791182041169,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.05891470551490774,
              "gap_to_oracle": 0.007036096096038946,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8833578724861145
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9841740314777081
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1746399892807007
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3613696395715416
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0787244558334352,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4620840383105809,
                  "rejected_mean_error": 2.2062272720336913,
                  "gap_rejected_minus_accepted": 0.7441432337231104
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9176610112190247,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3609062531205607,
                  "rejected_mean_error": 2.0621526930659724,
                  "gap_rejected_minus_accepted": 0.7012464399454117
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4853128790855408,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1746399892807007,
                  "rejected_mean_error": 1.898356734085083,
                  "gap_rejected_minus_accepted": 0.7237167448043824
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1287594437599182,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9845569849776002,
                  "rejected_mean_error": 1.720871521670892,
                  "gap_rejected_minus_accepted": 0.7363145366932918
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0964932680130004,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4568911027908324,
                  "rejected_mean_error": 2.175918312072754,
                  "gap_rejected_minus_accepted": 0.7190272092819217
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.915255457162857,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3538243553855203,
                  "rejected_mean_error": 2.048147642423236,
                  "gap_rejected_minus_accepted": 0.6943232870377158
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4854724407196045,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1638502321243287,
                  "rejected_mean_error": 1.8937374153137208,
                  "gap_rejected_minus_accepted": 0.729887183189392
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1267292499542236,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9595013043237111,
                  "rejected_mean_error": 1.7205875601997986,
                  "gap_rejected_minus_accepted": 0.7610862558760876
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9419086659116259,
              "spearman": 0.9420696181303527,
              "auroc_top30_bad": 0.9613158095238096,
              "mae": 0.22159531161664053,
              "mse": 0.12963696939132974,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6556816869505223,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08495993208885193
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2090550905942917
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7039534909129143
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1051907248099646
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8688925641433736,
              "spearman": 0.9226520040012826,
              "auroc_top30_worst": 0.9489401904761904,
              "pairwise_seed_ranking": 0.9048,
              "predicted_best_mean_error": 1.7261159998178481,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08103258156776438,
              "gap_to_oracle": 0.002229199647903357,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9403786993026734
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1292411994475584
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2912502822875978
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5361915254897909
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9455918312072755,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6895675854153103,
                  "rejected_mean_error": 2.818487606048584,
                  "gap_rejected_minus_accepted": 1.1289200206332737
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7710427045822144,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5359170467392993,
                  "rejected_mean_error": 2.6003840624714814,
                  "gap_rejected_minus_accepted": 1.064467015732182
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4810892343521118,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2912502822875978,
                  "rejected_mean_error": 2.3136688926696776,
                  "gap_rejected_minus_accepted": 1.0224186103820798
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2687993943691254,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.129754301458121,
                  "rejected_mean_error": 2.0271733062880526,
                  "gap_rejected_minus_accepted": 0.8974190048299315
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9335864901542663,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.698665384584003,
                  "rejected_mean_error": 2.7834973526000977,
                  "gap_rejected_minus_accepted": 1.0848319680160947
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7687727808952332,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5313307976021486,
                  "rejected_mean_error": 2.625845812615894,
                  "gap_rejected_minus_accepted": 1.0945150150137455
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.460960030555725,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2871440370082856,
                  "rejected_mean_error": 2.3271531257629396,
                  "gap_rejected_minus_accepted": 1.040009088754654
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2439050674438477,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.138477790450293,
                  "rejected_mean_error": 2.0324226981178324,
                  "gap_rejected_minus_accepted": 0.8939449076675394
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9862035041106747,
              "spearman": 0.9837753691288447,
              "auroc_top30_bad": 0.995872,
              "mae": 0.10289897077009082,
              "mse": 0.021841820740323405,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7187920755637048,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07827746498584748
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21099748504161836
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5932407577514649
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9341816105524698
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.990381273901368,
              "spearman": 0.9813374713199818,
              "auroc_top30_worst": 0.9983238095238095,
              "pairwise_seed_ranking": 0.8944,
              "predicted_best_mean_error": 1.5569808995723724,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06234137868881229,
              "gap_to_oracle": 0.005837639331817579,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5712003314495087
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8812737465859988
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1171388088703156
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3103513052023805
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5680701732635502,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.475815506219864,
                  "rejected_mean_error": 2.9477637901306153,
                  "gap_rejected_minus_accepted": 1.4719482839107514
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.003117620944977,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3095984596643784,
                  "rejected_mean_error": 2.561243327661825,
                  "gap_rejected_minus_accepted": 1.2516448679974466
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4290149807929993,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1171388088703156,
                  "rejected_mean_error": 2.1288818603515627,
                  "gap_rejected_minus_accepted": 1.011743051481247
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1829553842544556,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.881901523270927,
                  "rejected_mean_error": 1.87057389699026,
                  "gap_rejected_minus_accepted": 0.9886723737193331
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5410104036331176,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4680441996786329,
                  "rejected_mean_error": 2.9808249855041504,
                  "gap_rejected_minus_accepted": 1.5127807858255176
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.01384437084198,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2980622406949334,
                  "rejected_mean_error": 2.572903659608629,
                  "gap_rejected_minus_accepted": 1.2748414189136958
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4665120840072632,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1038005366325379,
                  "rejected_mean_error": 2.1348440198898317,
                  "gap_rejected_minus_accepted": 1.031043483257294
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1819757223129272,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8659858713074337,
                  "rejected_mean_error": 1.8731201052028228,
                  "gap_rejected_minus_accepted": 1.007134233895389
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
        "best_epoch": 78,
        "best_calib_loss": 0.09466234594583511,
        "train_time_sec": 10.792363405227661,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.917291160612598,
              "spearman": 0.8677345501827249,
              "auroc_top30_bad": 0.9289697857142858,
              "mae": 0.15582733173719607,
              "mse": 0.12597654345446824,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.546,
              "expert_lt_simvla_seed0": 0.982,
              "same_context_pred_std": 0.6828797233507354,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.41097530953027306
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.43962816091720014
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5885119173043407
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.867166203942212
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2341490384186153
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9982101540120347,
              "spearman": 0.997250722441831,
              "auroc_top30_worst": 0.9991325714285714,
              "pairwise_seed_ranking": 0.8679,
              "predicted_best_mean_error": 1.502465560168028,
              "seed0_mean_error": 1.578147357314825,
              "random_seed_mean_error": 1.5737691277563572,
              "oracle_best_mean_error": 1.495616854697466,
              "improvement_over_seed0": 0.07568179714679713,
              "gap_to_oracle": 0.006848705470561933,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6308647696375846
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7633812571287155
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9616362087607384
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.196187442612648
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5732941660106181
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.707057070732117,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3651615543564162,
                  "rejected_mean_error": 3.4464876708984375,
                  "gap_rejected_minus_accepted": 2.081326116542021
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9561291337013245,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.196187442612648,
                  "rejected_mean_error": 2.704614336204529,
                  "gap_rejected_minus_accepted": 1.508426893591881
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3554959893226624,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9616362087607384,
                  "rejected_mean_error": 2.1849521232604983,
                  "gap_rejected_minus_accepted": 1.2233159144997598
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9602642208337784,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7633812571287155,
                  "rejected_mean_error": 1.843265135637919,
                  "gap_rejected_minus_accepted": 1.0798838785092035
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7161763191223143,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.37025003231234,
                  "rejected_mean_error": 3.4492232823371887,
                  "gap_rejected_minus_accepted": 2.0789732500248483
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9620538353919983,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1976038641532263,
                  "rejected_mean_error": 2.7197778367996217,
                  "gap_rejected_minus_accepted": 1.5221739726463954
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3682451844215393,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.953703904569149,
                  "rejected_mean_error": 2.202590810060501,
                  "gap_rejected_minus_accepted": 1.2488869054913523
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9448854327201843,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.756102487206459,
                  "rejected_mean_error": 1.8521623140176138,
                  "gap_rejected_minus_accepted": 1.0960598268111548
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5255370615531199,
              "spearman": 0.49382900448952005,
              "auroc_top30_bad": 0.6576171428571429,
              "mae": 0.48569390248656275,
              "mse": 0.5261531444530629,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.472,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.606275779506712,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5547954452633858
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7586968105792999
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9349442223191261
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1756938004573185
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.42617208867092604,
              "spearman": 0.4713351819105165,
              "auroc_top30_worst": 0.7102689523809524,
              "pairwise_seed_ranking": 0.7488,
              "predicted_best_mean_error": 1.4877077007293702,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.04108612298965442,
              "gap_to_oracle": 0.02486467862129227,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9611393518447876
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1646916241599963
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3504578935623168
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4921873857471735
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0546341419219973,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5208089978430006,
                  "rejected_mean_error": 1.6777026362419127,
                  "gap_rejected_minus_accepted": 0.15689363839891213
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.733715981245041,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4921047812210457,
                  "rejected_mean_error": 1.6693954380175557,
                  "gap_rejected_minus_accepted": 0.17729065679651002
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5065670013427734,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3504578935623168,
                  "rejected_mean_error": 1.7225388298034667,
                  "gap_rejected_minus_accepted": 0.3720809362411499
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2224797308444977,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.163941897523289,
                  "rejected_mean_error": 1.6609489201481593,
                  "gap_rejected_minus_accepted": 0.4970070226248704
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.054941940307617,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.51808953444163,
                  "rejected_mean_error": 1.6251324272155763,
                  "gap_rejected_minus_accepted": 0.10704289277394619
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7453712821006775,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4808902428111927,
                  "rejected_mean_error": 1.6709838178422716,
                  "gap_rejected_minus_accepted": 0.19009357503107882
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.51131671667099,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3504531207084656,
                  "rejected_mean_error": 1.7071345267295837,
                  "gap_rejected_minus_accepted": 0.3566814060211181
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2113532721996307,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1333090634573073,
                  "rejected_mean_error": 1.6620320049836674,
                  "gap_rejected_minus_accepted": 0.5287229415263601
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4806127633463968,
              "spearman": 0.44582394939189873,
              "auroc_top30_bad": 0.582624,
              "mae": 0.6253550000131131,
              "mse": 0.7729694802980418,
              "expert_lt_perturb_large": 0.98,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.6173724656827733,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5388129852414131
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5536120785474777
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1788547925710677
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.280362308470408
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.12602097852951347,
              "spearman": -0.040883888693688766,
              "auroc_top30_worst": 0.3500830476190476,
              "pairwise_seed_ranking": 0.6612,
              "predicted_best_mean_error": 1.7708862994909287,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.036262281894683834,
              "gap_to_oracle": 0.046999499320983906,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.5983571696281433
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.1618924221167197
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8500409054756164
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7832801561874112
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7167371511459355,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7450440624025132,
                  "rejected_mean_error": 2.3191993131637574,
                  "gap_rejected_minus_accepted": 0.5741552507612442
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7902965545654297,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7830679360677746,
                  "rejected_mean_error": 1.8605106333955028,
                  "gap_rejected_minus_accepted": 0.07744269732772824
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.368977963924408,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.8500409054756164,
                  "rejected_mean_error": 1.754878269481659,
                  "gap_rejected_minus_accepted": -0.09516263599395747
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.058476060628891,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.1579928116295664,
                  "rejected_mean_error": 1.6836955542243786,
                  "gap_rejected_minus_accepted": -0.4742972574051878
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.684781384468078,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7481526039706337,
                  "rejected_mean_error": 2.3381123781204223,
                  "gap_rejected_minus_accepted": 0.5899597741497886
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8003927171230316,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7794386484724953,
                  "rejected_mean_error": 1.889398699715024,
                  "gap_rejected_minus_accepted": 0.10996005124252872
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3558509349822998,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8539288308620452,
                  "rejected_mean_error": 1.7603683319091796,
                  "gap_rejected_minus_accepted": -0.09356049895286556
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0206392109394073,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.1102981960016582,
                  "rejected_mean_error": 1.7050179625577468,
                  "gap_rejected_minus_accepted": -0.4052802334439114
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.703015258581611,
              "spearman": 0.6627707202712341,
              "auroc_top30_bad": 0.8116849523809524,
              "mae": 0.4211716296136379,
              "mse": 0.37861658160092737,
              "expert_lt_perturb_large": 0.984,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.984,
              "same_context_pred_std": 0.675604143356381,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.593815640091896
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6990425882101059
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7629787729978561
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0289340955972672
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7314481907564266,
              "spearman": 0.6463870330797012,
              "auroc_top30_worst": 0.8802377142857143,
              "pairwise_seed_ranking": 0.7792,
              "predicted_best_mean_error": 1.563051544547081,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.05627073371410374,
              "gap_to_oracle": 0.011908284306526129,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7006026074886322
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0713648583071353
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2493981821537017
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4095228212410962
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3815593004226687,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.506512425714069,
                  "rejected_mean_error": 2.67149151468277,
                  "gap_rejected_minus_accepted": 1.1649790889687008
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9497385621070862,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4089609552154927,
                  "rejected_mean_error": 2.263790745133409,
                  "gap_rejected_minus_accepted": 0.8548297899179162
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7105923891067505,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2493981821537017,
                  "rejected_mean_error": 1.9966224870681764,
                  "gap_rejected_minus_accepted": 0.7472243049144747
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4438901841640472,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0723546683407439,
                  "rejected_mean_error": 1.8069540096830532,
                  "gap_rejected_minus_accepted": 0.7345993413423093
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4146222352981566,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4993646783298917,
                  "rejected_mean_error": 2.698940677642822,
                  "gap_rejected_minus_accepted": 1.1995759993129305
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.996316373348236,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4005268200196046,
                  "rejected_mean_error": 2.2687627654227,
                  "gap_rejected_minus_accepted": 0.8682359454030955
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7121708989143372,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2308118829727173,
                  "rejected_mean_error": 2.007832673549652,
                  "gap_rejected_minus_accepted": 0.7770207905769348
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4195348024368286,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.004725988895174,
                  "rejected_mean_error": 1.8263787821652417,
                  "gap_rejected_minus_accepted": 0.8216527932700677
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
        "best_epoch": 53,
        "best_calib_loss": 0.018674230203032494,
        "train_time_sec": 35.20560574531555,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994515822623593,
              "spearman": 0.9988340897473927,
              "auroc_top30_bad": 0.9997701428571429,
              "mae": 0.02582131217480637,
              "mse": 0.001169705142120618,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7162099850239925,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0776703890808858
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21570134072098882
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5171540326287039
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8508115595771
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2341490384186153
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995744463823483,
              "spearman": 0.9992863213074357,
              "auroc_top30_worst": 0.99986,
              "pairwise_seed_ranking": 0.9377,
              "predicted_best_mean_error": 1.4982210748791696,
              "seed0_mean_error": 1.578147357314825,
              "random_seed_mean_error": 1.5737691277563572,
              "oracle_best_mean_error": 1.495616854697466,
              "improvement_over_seed0": 0.07992628243565547,
              "gap_to_oracle": 0.002604220181703587,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6274881868958473
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7620078106641769
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9610555678248406
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1948389499266943
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5732941660106181
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7736982822418224,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3648653640945752,
                  "rejected_mean_error": 3.449153383255005,
                  "gap_rejected_minus_accepted": 2.0842880191604296
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9862355589866638,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1948389499266943,
                  "rejected_mean_error": 2.7086598142623903,
                  "gap_rejected_minus_accepted": 1.513820864335696
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3743373155593872,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9610555678248406,
                  "rejected_mean_error": 2.1855327641963957,
                  "gap_rejected_minus_accepted": 1.2244771963715553
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9803429841995239,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7620078106641769,
                  "rejected_mean_error": 1.8437229511260986,
                  "gap_rejected_minus_accepted": 1.0817151404619216
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8051186323165895,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3697274034221967,
                  "rejected_mean_error": 3.45392694234848,
                  "gap_rejected_minus_accepted": 2.0841995389262835
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.010250687599182,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1961881228685378,
                  "rejected_mean_error": 2.7240250606536867,
                  "gap_rejected_minus_accepted": 1.5278369377851488
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3910488486289978,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9531174210906028,
                  "rejected_mean_error": 2.2031772935390475,
                  "gap_rejected_minus_accepted": 1.2500598724484446
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9723028242588043,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7544598351716996,
                  "rejected_mean_error": 1.8527098646958668,
                  "gap_rejected_minus_accepted": 1.0982500295241673
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9518531243296795,
              "spearman": 0.9350265152287854,
              "auroc_top30_bad": 0.944225523809524,
              "mae": 0.14366732738539575,
              "mse": 0.057776305312230464,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6825503511699874,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07118403309583664
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23404397523403167
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7115991321921349
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.051751821287473
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9674050060854275,
              "spearman": 0.9702903679298356,
              "auroc_top30_worst": 0.9826925714285715,
              "pairwise_seed_ranking": 0.892,
              "predicted_best_mean_error": 1.467291090965271,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.06150273275375362,
              "gap_to_oracle": 0.004448068857193066,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8829909043312073
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9781678552046801
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1729096843719482
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.360104641807613
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1088716030120853,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4643014862272474,
                  "rejected_mean_error": 2.1862702407836916,
                  "gap_rejected_minus_accepted": 0.7219687545564442
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8951581418514252,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3596659005642446,
                  "rejected_mean_error": 2.0658658251594813,
                  "gap_rejected_minus_accepted": 0.7061999245952366
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4881568551063538,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1729096843719482,
                  "rejected_mean_error": 1.9000870389938354,
                  "gap_rejected_minus_accepted": 0.7271773546218872
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1842727661132812,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9796977481141258,
                  "rejected_mean_error": 1.7224947245932694,
                  "gap_rejected_minus_accepted": 0.7427969764791436
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1007784843444823,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4601475832197401,
                  "rejected_mean_error": 2.1466099882125853,
                  "gap_rejected_minus_accepted": 0.6864624049928452
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8968619406223297,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3504923384457348,
                  "rejected_mean_error": 2.0580379149270436,
                  "gap_rejected_minus_accepted": 0.7075455764813088
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4846937656402588,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1617286291122437,
                  "rejected_mean_error": 1.8958590183258057,
                  "gap_rejected_minus_accepted": 0.734130389213562
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.213980257511139,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9601654457667518,
                  "rejected_mean_error": 1.720363812013106,
                  "gap_rejected_minus_accepted": 0.7601983662463542
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9221544092155544,
              "spearman": 0.9103829358997366,
              "auroc_top30_bad": 0.9152152380952381,
              "mae": 0.24205337375327945,
              "mse": 0.14173136238175388,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6581607339859689,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08913263320922851
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2839316745042801
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7553576728701592
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0688645055691401
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9325354010790159,
              "spearman": 0.9485016225930386,
              "auroc_top30_worst": 0.9798857142857142,
              "pairwise_seed_ranking": 0.9036,
              "predicted_best_mean_error": 1.7259307454824449,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08121783590316767,
              "gap_to_oracle": 0.002043945312500073,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9517733459472656
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1223293596353285
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3050791173934937
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4647072856105976
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.180567479133606,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.654147607591417,
                  "rejected_mean_error": 3.1372674064636232,
                  "gap_rejected_minus_accepted": 1.4831197988722062
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9061143696308136,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4641735284025668,
                  "rejected_mean_error": 2.815156192444384,
                  "gap_rejected_minus_accepted": 1.3509826640418172
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5990476608276367,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3050791173934937,
                  "rejected_mean_error": 2.299840057563782,
                  "gap_rejected_minus_accepted": 0.9947609401702882
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3126605153083801,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1230116397047196,
                  "rejected_mean_error": 2.029425657546126,
                  "gap_rejected_minus_accepted": 0.9064140178414062
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.180567479133606,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6553563137849172,
                  "rejected_mean_error": 3.17327898979187,
                  "gap_rejected_minus_accepted": 1.5179226760069529
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9476334750652313,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4625978825245312,
                  "rejected_mean_error": 2.829862560544695,
                  "gap_rejected_minus_accepted": 1.3672646780201638
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6102721691131592,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3022799413204194,
                  "rejected_mean_error": 2.3120172214508057,
                  "gap_rejected_minus_accepted": 1.0097372801303863
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3132240772247314,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1250699678110698,
                  "rejected_mean_error": 2.036939772055111,
                  "gap_rejected_minus_accepted": 0.911869804244041
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9722589180778347,
              "spearman": 0.9666457440659514,
              "auroc_top30_bad": 0.9769340952380952,
              "mae": 0.13920843604654073,
              "mse": 0.041443365807020016,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7362082651630639,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0807480919957161
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21926909053325652
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6004921773910522
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.946022626431783
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9830738560680585,
              "spearman": 0.9799856737188314,
              "auroc_top30_worst": 0.9954925714285714,
              "pairwise_seed_ranking": 0.9192,
              "predicted_best_mean_error": 1.5537258015871047,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06559647667407997,
              "gap_to_oracle": 0.0025825413465498936,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5691688764095306
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.875450406032495
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1173948860645295
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3118738293457133
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7558575153350833,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.476502258963055,
                  "rejected_mean_error": 2.9415830154418945,
                  "gap_rejected_minus_accepted": 1.4650807564788395
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1195428371429443,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3110079550628602,
                  "rejected_mean_error": 2.5570238478267537,
                  "gap_rejected_minus_accepted": 1.2460158927638936
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5897295475006104,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1173948860645295,
                  "rejected_mean_error": 2.1286257831573487,
                  "gap_rejected_minus_accepted": 1.0112308970928192
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2664623856544495,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8767416904719112,
                  "rejected_mean_error": 1.872297512428992,
                  "gap_rejected_minus_accepted": 0.9955558219570808
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.708402204513549,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4680441996786329,
                  "rejected_mean_error": 2.9808249855041504,
                  "gap_rejected_minus_accepted": 1.5127807858255176
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1371712684631348,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2984497531212587,
                  "rejected_mean_error": 2.5717534243114413,
                  "gap_rejected_minus_accepted": 1.2733036711901826
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5928571820259094,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1049126496315003,
                  "rejected_mean_error": 2.133731906890869,
                  "gap_rejected_minus_accepted": 1.0288192572593688
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2666474878787994,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8587347146064516,
                  "rejected_mean_error": 1.8755630082625119,
                  "gap_rejected_minus_accepted": 1.0168282936560602
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
        "best_epoch": 75,
        "best_calib_loss": 0.01922469213604927,
        "train_time_sec": 41.71712064743042,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9990924004893795,
              "spearman": 0.99796113540032,
              "auroc_top30_bad": 0.9994058095238095,
              "mae": 0.0341799550706055,
              "mse": 0.001886487878429461,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.989,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7091754076202859,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07943785853171721
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21603112038169056
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5173610162665137
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8510454349471256
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2341490384186153
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9992603212868871,
              "spearman": 0.9984929399316814,
              "auroc_top30_worst": 0.9994944761904762,
              "pairwise_seed_ranking": 0.958,
              "predicted_best_mean_error": 1.4976182224154473,
              "seed0_mean_error": 1.578147357314825,
              "random_seed_mean_error": 1.5737691277563572,
              "oracle_best_mean_error": 1.495616854697466,
              "improvement_over_seed0": 0.08052913489937774,
              "gap_to_oracle": 0.002001367717981317,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6291069715619088
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7625820794820786
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.961414063680172
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1951368930419286
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5732941660106181
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7795709371566777,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3648185167511304,
                  "rejected_mean_error": 3.4495750093460082,
                  "gap_rejected_minus_accepted": 2.084756492594878
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9902035892009735,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1951368930419286,
                  "rejected_mean_error": 2.707765984916687,
                  "gap_rejected_minus_accepted": 1.5126290918747585
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3819715976715088,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.961414063680172,
                  "rejected_mean_error": 2.1851742683410644,
                  "gap_rejected_minus_accepted": 1.2237602046608924
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.994885727763176,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7625820794820786,
                  "rejected_mean_error": 1.843531528186798,
                  "gap_rejected_minus_accepted": 1.0809494487047195
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8300485610961914,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3697828866044681,
                  "rejected_mean_error": 3.4534275937080383,
                  "gap_rejected_minus_accepted": 2.08364470710357
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0206469297409058,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1963285493453344,
                  "rejected_mean_error": 2.723603781223297,
                  "gap_rejected_minus_accepted": 1.5272752318779625
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4064127206802368,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9533473624587059,
                  "rejected_mean_error": 2.2029473521709444,
                  "gap_rejected_minus_accepted": 1.2495999897122385
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9793595671653748,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7545713773965835,
                  "rejected_mean_error": 1.852672683954239,
                  "gap_rejected_minus_accepted": 1.0981013065576555
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9528821106200971,
              "spearman": 0.9415894351213483,
              "auroc_top30_bad": 0.9520373333333334,
              "mae": 0.1504962954384275,
              "mse": 0.06037368309423834,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6591831406275276,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08522666585445404
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23756305010318757
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7032916672110557
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0462287276188533
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9733611214982356,
              "spearman": 0.9776660050342433,
              "auroc_top30_worst": 0.9840121904761905,
              "pairwise_seed_ranking": 0.886,
              "predicted_best_mean_error": 1.4686699461936952,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.06012387752532944,
              "gap_to_oracle": 0.005826924085617247,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.868502986907959
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9768382998613211
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1695948112487793
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3601554172125452
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.057446885108948,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4595369956758286,
                  "rejected_mean_error": 2.22915065574646,
                  "gap_rejected_minus_accepted": 0.7696136600706314
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8845888674259186,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3596947280930607,
                  "rejected_mean_error": 2.0657795267744947,
                  "gap_rejected_minus_accepted": 0.706084798681434
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.448440432548523,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1695948112487793,
                  "rejected_mean_error": 1.9034019121170045,
                  "gap_rejected_minus_accepted": 0.7338071008682252
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1053625643253326,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9775456864232073,
                  "rejected_mean_error": 1.7232136096618473,
                  "gap_rejected_minus_accepted": 0.7456679232386401
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.094508647918701,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4524575673209297,
                  "rejected_mean_error": 2.21582013130188,
                  "gap_rejected_minus_accepted": 0.7633625639809503
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8879177868366241,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3515180623467593,
                  "rejected_mean_error": 2.054993305887495,
                  "gap_rejected_minus_accepted": 0.7034752435407357
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4525831937789917,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1567178783416747,
                  "rejected_mean_error": 1.9008697690963745,
                  "gap_rejected_minus_accepted": 0.7441518907546998
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0938490331172943,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9553983968401712,
                  "rejected_mean_error": 1.7219698231487988,
                  "gap_rejected_minus_accepted": 0.7665714263086275
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9421730411957168,
              "spearman": 0.9330909695098073,
              "auroc_top30_bad": 0.937280761904762,
              "mae": 0.24400931929978542,
              "mse": 0.1310082201455732,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6588792793585015,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10440796321630477
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22748649632930756
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7423589338183403
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0649229010184607
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9410173625733063,
              "spearman": 0.9590848598303103,
              "auroc_top30_worst": 0.9907474285714286,
              "pairwise_seed_ranking": 0.91,
              "predicted_best_mean_error": 1.7265571924448013,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08059138894081119,
              "gap_to_oracle": 0.002670392274856548,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9556398086547852
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1244908280861683
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.293581678199768
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4638611506551569
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.158809494972229,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6497838971879748,
                  "rejected_mean_error": 3.1765408000946045,
                  "gap_rejected_minus_accepted": 1.5267569029066297
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8990809619426727,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4625851600376238,
                  "rejected_mean_error": 2.8199111482205863,
                  "gap_rejected_minus_accepted": 1.3573259881829625
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5277200937271118,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.293581678199768,
                  "rejected_mean_error": 2.311337496757507,
                  "gap_rejected_minus_accepted": 1.0177558185577391
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.297103613615036,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1245847209193074,
                  "rejected_mean_error": 2.0289001779088087,
                  "gap_rejected_minus_accepted": 0.9043154569895013
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.158920097351074,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.65045604162746,
                  "rejected_mean_error": 3.2173814392089843,
                  "gap_rejected_minus_accepted": 1.5669253975815243
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9243860244750977,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4549362798106862,
                  "rejected_mean_error": 2.852604143203251,
                  "gap_rejected_minus_accepted": 1.3976678633925648
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5054579973220825,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.292455890417099,
                  "rejected_mean_error": 2.321841272354126,
                  "gap_rejected_minus_accepted": 1.0293853819370269
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3185626864433289,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1261856759351396,
                  "rejected_mean_error": 2.0365638917780178,
                  "gap_rejected_minus_accepted": 0.9103782158428781
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9818850735269731,
              "spearman": 0.9776316540272242,
              "auroc_top30_bad": 0.9911657142857142,
              "mae": 0.12712058864397696,
              "mse": 0.03264801566472228,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6883752640054932,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10112466812133789
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2232798185825348
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5946414481163025
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9402687057495117
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9910465615018782,
              "spearman": 0.9825401047936672,
              "auroc_top30_worst": 0.997568,
              "pairwise_seed_ranking": 0.9216,
              "predicted_best_mean_error": 1.5544214037656785,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06490087449550619,
              "gap_to_oracle": 0.003278143525123678,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5729533729553222
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8802106671799452
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1167987452030181
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3092267050989654
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.585885190963746,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4740061166816287,
                  "rejected_mean_error": 2.9640482959747314,
                  "gap_rejected_minus_accepted": 1.4900421792931027
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9590763449668884,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3085664958874978,
                  "rejected_mean_error": 2.564332624974723,
                  "gap_rejected_minus_accepted": 1.255766129087225
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.414780616760254,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1167987452030181,
                  "rejected_mean_error": 2.12922192401886,
                  "gap_rejected_minus_accepted": 1.0124231788158418
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1664260923862457,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8815239124214307,
                  "rejected_mean_error": 1.870700035939985,
                  "gap_rejected_minus_accepted": 0.9891761235185543
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5624251842498778,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.467529227203793,
                  "rejected_mean_error": 2.98545973777771,
                  "gap_rejected_minus_accepted": 1.5179305105739171
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9759806990623474,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2973129318997185,
                  "rejected_mean_error": 2.5751277984134733,
                  "gap_rejected_minus_accepted": 1.2778148665137548
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.427125632762909,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1038214316368102,
                  "rejected_mean_error": 2.134823124885559,
                  "gap_rejected_minus_accepted": 1.031001693248749
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.159220039844513,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8618235200170486,
                  "rejected_mean_error": 1.8745223946749845,
                  "gap_rejected_minus_accepted": 1.0126988746579357
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
        "best_epoch": 24,
        "best_calib_loss": 0.02123120427131653,
        "train_time_sec": 29.2160701751709,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9985941325412924,
              "spearman": 0.9973043557230749,
              "auroc_top30_bad": 0.9994886666666666,
              "mae": 0.040152417453518136,
              "mse": 0.0028676446530042023,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.993,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7275217680622658,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08260941423336043
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21695325113330036
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5176005686451681
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8509955456687137
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2341490384186153
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9991223135076823,
              "spearman": 0.9986738641309229,
              "auroc_top30_worst": 0.9996144761904762,
              "pairwise_seed_ranking": 0.9258,
              "predicted_best_mean_error": 1.4994839368462562,
              "seed0_mean_error": 1.578147357314825,
              "random_seed_mean_error": 1.5737691277563572,
              "oracle_best_mean_error": 1.495616854697466,
              "improvement_over_seed0": 0.07866342046856878,
              "gap_to_oracle": 0.0038670821487902796,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6288651140332222
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7626719363927841
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.961376135957241
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1950133735895156
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5732941660106181
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.80625650882721,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.364938962161541,
                  "rejected_mean_error": 3.448491000652313,
                  "gap_rejected_minus_accepted": 2.083552038490772
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9999719560146332,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1950133735895156,
                  "rejected_mean_error": 2.708136543273926,
                  "gap_rejected_minus_accepted": 1.5131231696844103
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.380296766757965,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.961376135957241,
                  "rejected_mean_error": 2.185212196063995,
                  "gap_rejected_minus_accepted": 1.2238360601067542
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9874657392501831,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7626719363927841,
                  "rejected_mean_error": 1.8435015758832296,
                  "gap_rejected_minus_accepted": 1.0808296394904455
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.847253799438477,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3698503762814733,
                  "rejected_mean_error": 3.45282018661499,
                  "gap_rejected_minus_accepted": 2.082969810333517
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0238605737686157,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.196183477361997,
                  "rejected_mean_error": 2.7240389971733094,
                  "gap_rejected_minus_accepted": 1.5278555198113124
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3938743472099304,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9535585181117058,
                  "rejected_mean_error": 2.2027361965179444,
                  "gap_rejected_minus_accepted": 1.2491776784062387
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9781336635351181,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7548673769235611,
                  "rejected_mean_error": 1.8525740174452463,
                  "gap_rejected_minus_accepted": 1.097706640521685
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9499051911468477,
              "spearman": 0.9342812728196814,
              "auroc_top30_bad": 0.9432434285714286,
              "mae": 0.15821815866688266,
              "mse": 0.0656776763674563,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6633847216667257,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06306955707073211
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23667381784915925
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7083026551604271
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0531145927667618
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9571566776559025,
              "spearman": 0.9644554626914963,
              "auroc_top30_worst": 0.9803672380952382,
              "pairwise_seed_ranking": 0.8628,
              "predicted_best_mean_error": 1.4705801153182982,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.05821370840072637,
              "gap_to_oracle": 0.007737093210220314,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8731683731079102
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9808066246601251
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.172755382156372
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.363425635325629
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.073103737831116,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.46743924469418,
                  "rejected_mean_error": 2.1580304145812987,
                  "gap_rejected_minus_accepted": 0.6905911698871188
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8825913965702057,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3629785853745207,
                  "rejected_mean_error": 2.0559489380437346,
                  "gap_rejected_minus_accepted": 0.6929703526692139
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4605100750923157,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.172755382156372,
                  "rejected_mean_error": 1.9002413412094117,
                  "gap_rejected_minus_accepted": 0.7274859590530396
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1161055266857147,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9812808170105322,
                  "rejected_mean_error": 1.721965908622538,
                  "gap_rejected_minus_accepted": 0.7406850916120059
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.088933324813843,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.461783095465766,
                  "rejected_mean_error": 2.131890377998352,
                  "gap_rejected_minus_accepted": 0.670107282532586
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8853469789028168,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3553042188685207,
                  "rejected_mean_error": 2.0437550317673456,
                  "gap_rejected_minus_accepted": 0.6884508128988249
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4688003063201904,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1624418563842773,
                  "rejected_mean_error": 1.895145791053772,
                  "gap_rejected_minus_accepted": 0.7327039346694946
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1408243477344513,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9599502502925812,
                  "rejected_mean_error": 1.7204363110231207,
                  "gap_rejected_minus_accepted": 0.7604860607305395
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9300512383370564,
              "spearman": 0.9192779072507965,
              "auroc_top30_bad": 0.9326986666666668,
              "mae": 0.2485259529261384,
              "mse": 0.15975907887393456,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6630609260492628,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09614435583353043
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2148530122280121
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7366461744189262
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0990064909537633
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.875383841716967,
              "spearman": 0.9271748264798891,
              "auroc_top30_worst": 0.957583238095238,
              "pairwise_seed_ranking": 0.9192,
              "predicted_best_mean_error": 1.7255203009843827,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08162828040122982,
              "gap_to_oracle": 0.001633500814437916,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9443974685668945
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1312010463995812
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.289871498298645
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.535665961852206
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.956512761116028,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.673632731543647,
                  "rejected_mean_error": 2.9619012908935547,
                  "gap_rejected_minus_accepted": 1.2882685593499077
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7949890196323395,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.534409509651689,
                  "rejected_mean_error": 2.6048970409094716,
                  "gap_rejected_minus_accepted": 1.0704875312577826
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.511201560497284,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.289871498298645,
                  "rejected_mean_error": 2.3150476766586303,
                  "gap_rejected_minus_accepted": 1.0251761783599853
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.255416065454483,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1318418499760734,
                  "rejected_mean_error": 2.026475971510978,
                  "gap_rejected_minus_accepted": 0.8946341215349045
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9551973938941956,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6784952628612517,
                  "rejected_mean_error": 2.9650284481048583,
                  "gap_rejected_minus_accepted": 1.2865331852436066
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.80210942029953,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5368727322886973,
                  "rejected_mean_error": 2.609395942990742,
                  "gap_rejected_minus_accepted": 1.0725232107020448
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5086520314216614,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2880229814052582,
                  "rejected_mean_error": 2.326274181365967,
                  "gap_rejected_minus_accepted": 1.0382511999607087
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2724654972553253,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1372885869608984,
                  "rejected_mean_error": 2.0328233388655965,
                  "gap_rejected_minus_accepted": 0.8955347519046981
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9769251702726819,
              "spearman": 0.9737337813191873,
              "auroc_top30_bad": 0.9876213333333335,
              "mae": 0.13260673862423283,
              "mse": 0.03727581305733289,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7097320969250588,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09857142573595047
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2201359005689621
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.597114407157898
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.942757318687439
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9842142636739284,
              "spearman": 0.9817420724109265,
              "auroc_top30_worst": 0.9986255238095237,
              "pairwise_seed_ranking": 0.8808,
              "predicted_best_mean_error": 1.5557949794530868,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06352729880809793,
              "gap_to_oracle": 0.004651719212531935,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6007231390476226
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8820798019759166
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1160339346408843
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3095609018606926
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6496554613113403,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4780543200439877,
                  "rejected_mean_error": 2.927614465713501,
                  "gap_rejected_minus_accepted": 1.449560145669513
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9800933599472046,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.308739401137689,
                  "rejected_mean_error": 2.5638150140500295,
                  "gap_rejected_minus_accepted": 1.2550756129123406
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4689366817474365,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1160339346408843,
                  "rejected_mean_error": 2.1299867345809935,
                  "gap_rejected_minus_accepted": 1.0139527999401092
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2557500004768372,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8830599675353724,
                  "rejected_mean_error": 1.8701869246799383,
                  "gap_rejected_minus_accepted": 0.9871269571445659
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.662039279937744,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4702935242652893,
                  "rejected_mean_error": 2.960581064224243,
                  "gap_rejected_minus_accepted": 1.490287539958954
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9934913516044617,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2967743615415646,
                  "rejected_mean_error": 2.576726412016248,
                  "gap_rejected_minus_accepted": 1.2799520504746835
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4855502247810364,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1034583268165588,
                  "rejected_mean_error": 2.1351862297058104,
                  "gap_rejected_minus_accepted": 1.0317279028892516
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.258221060037613,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8641115739232018,
                  "rejected_mean_error": 1.8737515529846762,
                  "gap_rejected_minus_accepted": 1.0096399790614745
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
        "best_epoch": 1,
        "best_calib_loss": 0.1357257217168808,
        "train_time_sec": 10.755077123641968,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.7886962250279091,
              "spearman": 0.697901708142238,
              "auroc_top30_bad": 0.8302194047619047,
              "mae": 0.40953303053523415,
              "mse": 0.30607228843705536,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.536,
              "expert_lt_simvla_seed0": 0.926,
              "same_context_pred_std": 0.6036149956525307,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.29657776179909706
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1486917105615139
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.2781060123324394
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.48169918742378554
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7900858353823423
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9128886515184795,
              "spearman": 0.8908443554791545,
              "auroc_top30_worst": 0.9467853333333333,
              "pairwise_seed_ranking": 0.7075,
              "predicted_best_mean_error": 1.0454149528443812,
              "seed0_mean_error": 1.1003441655039787,
              "random_seed_mean_error": 1.0959886793792248,
              "oracle_best_mean_error": 1.0204971807599068,
              "improvement_over_seed0": 0.05492921265959749,
              "gap_to_oracle": 0.024917772084474432,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.27203920191526415
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.42675449814796446
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5547204289317131
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.762374799712499
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0952668563961983
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4345693826675436,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9038761510186725,
                  "rejected_mean_error": 2.81778320479393,
                  "gap_rejected_minus_accepted": 1.9139070537752576
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7149162590503693,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.762374799712499,
                  "rejected_mean_error": 2.0939430264472962,
                  "gap_rejected_minus_accepted": 1.3315682267347972
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9919770061969757,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5547204289317131,
                  "rejected_mean_error": 1.6358132838606834,
                  "gap_rejected_minus_accepted": 1.0810928549289702
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.556590810418129,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.42675449814796446,
                  "rejected_mean_error": 1.3181043091456095,
                  "gap_rejected_minus_accepted": 0.891349810997645
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4168313980102547,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9101404878165987,
                  "rejected_mean_error": 2.812177264690399,
                  "gap_rejected_minus_accepted": 1.9020367768738002
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7192386090755463,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7643939308325449,
                  "rejected_mean_error": 2.10819486951828,
                  "gap_rejected_minus_accepted": 1.3438009386857352
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9852640330791473,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5480875843763351,
                  "rejected_mean_error": 1.6526007466316224,
                  "gap_rejected_minus_accepted": 1.1045131622552873
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5484238266944885,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.4224128564596176,
                  "rejected_mean_error": 1.3263212685187658,
                  "gap_rejected_minus_accepted": 0.9039084120591481
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4885689662329472,
              "spearman": 0.47583804708520766,
              "auroc_top30_bad": 0.6406670476190476,
              "mae": 0.6574645445495844,
              "mse": 0.72682263550166,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.928,
              "same_context_pred_std": 0.5347002810741699,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8609593686461449
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7471058176755905
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9454327780842781
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1713892811059952
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.4330192468842996,
              "spearman": 0.5175810995079038,
              "auroc_top30_worst": 0.7160167619047618,
              "pairwise_seed_ranking": 0.6428,
              "predicted_best_mean_error": 1.4976080186367036,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.03118580508232105,
              "gap_to_oracle": 0.034764996528625636,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9124517855644226
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1332426061614966
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3517904462814332
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4691244274822635
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.080127048492433,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5224940979745654,
                  "rejected_mean_error": 1.6625367350578308,
                  "gap_rejected_minus_accepted": 0.14004263708326548
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5431513488292694,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4690010492931436,
                  "rejected_mean_error": 1.738559006121212,
                  "gap_rejected_minus_accepted": 0.2695579568280684
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.143429696559906,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3517904462814332,
                  "rejected_mean_error": 1.7212062770843506,
                  "gap_rejected_minus_accepted": 0.3694158308029174
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.796953096985817,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.134549250046666,
                  "rejected_mean_error": 1.6707673818986215,
                  "gap_rejected_minus_accepted": 0.5362181318519554
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.080034041404724,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5140704743067424,
                  "rejected_mean_error": 1.6613039684295654,
                  "gap_rejected_minus_accepted": 0.14723349412282305
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5392633974552155,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4619670519854295,
                  "rejected_mean_error": 1.7271526541028703,
                  "gap_rejected_minus_accepted": 0.2651856021174408
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.152127742767334,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.329533571243286,
                  "rejected_mean_error": 1.7280540761947631,
                  "gap_rejected_minus_accepted": 0.39852050495147706
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7643764168024063,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1103424354205056,
                  "rejected_mean_error": 1.6697694251244082,
                  "gap_rejected_minus_accepted": 0.5594269897039026
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.3375553039664375,
              "spearman": 0.32828609942898584,
              "auroc_top30_bad": 0.5080784761904762,
              "mae": 0.8860113203052431,
              "mse": 1.4023617782095688,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.472,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6250374129886184,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7819239916205406
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7565943933725358
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1958978630781174
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2981338826417923
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.0041814507421145675,
              "spearman": -0.16365854851747105,
              "auroc_top30_worst": 0.2939032380952381,
              "pairwise_seed_ranking": 0.6956,
              "predicted_best_mean_error": 1.7544698852300644,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.0526786961555481,
              "gap_to_oracle": 0.03058308506011964,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.7733245992660522
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.1844804684321084
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.9388314622879028
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.780797253158301
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1996920108795166,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.74368402311537,
                  "rejected_mean_error": 2.331439666748047,
                  "gap_rejected_minus_accepted": 0.587755643632677
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.724660038948059,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7808064447523053,
                  "rejected_mean_error": 1.8672806569181692,
                  "gap_rejected_minus_accepted": 0.08647421216586393
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0886594653129578,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.9388314622879028,
                  "rejected_mean_error": 1.6660877126693725,
                  "gap_rejected_minus_accepted": -0.2727437496185303
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.4970392435789108,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.187121505554492,
                  "rejected_mean_error": 1.6739652647916128,
                  "gap_rejected_minus_accepted": -0.5131562407628791
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.115536403656005,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7446472187836966,
                  "rejected_mean_error": 2.3696608448028567,
                  "gap_rejected_minus_accepted": 0.6250136260191601
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7274070382118225,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.783707748600506,
                  "rejected_mean_error": 1.8767269263191828,
                  "gap_rejected_minus_accepted": 0.09301917771867685
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1110191941261292,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.948176331281662,
                  "rejected_mean_error": 1.666120831489563,
                  "gap_rejected_minus_accepted": -0.282055499792099
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.4970392435789108,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.173201605914131,
                  "rejected_mean_error": 1.6838259046727961,
                  "gap_rejected_minus_accepted": -0.4893757012413349
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6522048434062395,
              "spearman": 0.6246404485590143,
              "auroc_top30_bad": 0.7663447619047619,
              "mae": 0.5921751457553357,
              "mse": 0.6013478689427995,
              "expert_lt_perturb_large": 0.984,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.680669335500437,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5053996599912643
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6322008430242538
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7967739927887917
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0727487452189128
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.59010840667311,
              "spearman": 0.5483979916787147,
              "auroc_top30_worst": 0.8203306666666668,
              "pairwise_seed_ranking": 0.7412,
              "predicted_best_mean_error": 1.570262050509453,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.0490602277517318,
              "gap_to_oracle": 0.019118790268898067,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9716807940006256
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1135985772006023
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3439561678409577
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4320302428022376
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4955850839614877,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5362207321855756,
                  "rejected_mean_error": 2.404116756439209,
                  "gap_rejected_minus_accepted": 0.8678960242536335
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0069782435894012,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4315343432708891,
                  "rejected_mean_error": 2.1962148198685325,
                  "gap_rejected_minus_accepted": 0.7646804765976434
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4067839980125427,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3439561678409577,
                  "rejected_mean_error": 1.9020645013809203,
                  "gap_rejected_minus_accepted": 0.5581083335399626
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.754429817199707,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.112422066850784,
                  "rejected_mean_error": 1.793569702603392,
                  "gap_rejected_minus_accepted": 0.6811476357526081
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5368968725204466,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.533938602871365,
                  "rejected_mean_error": 2.387775356769562,
                  "gap_rejected_minus_accepted": 0.8538367538981968
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.013643443584442,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4152683453126387,
                  "rejected_mean_error": 2.2250061744735357,
                  "gap_rejected_minus_accepted": 0.809737829160897
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3955153226852417,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3021623239517213,
                  "rejected_mean_error": 1.936482232570648,
                  "gap_rejected_minus_accepted": 0.6343199086189268
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7183671295642853,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.065061350663503,
                  "rejected_mean_error": 1.8060518955801899,
                  "gap_rejected_minus_accepted": 0.7409905449166869
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
        "best_epoch": 52,
        "best_calib_loss": 0.06722723692655563,
        "train_time_sec": 35.230489015579224,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9920531801820177,
              "spearman": 0.9911065459638786,
              "auroc_top30_bad": 0.9997410952380953,
              "mae": 0.10414623449903156,
              "mse": 0.02323771773657845,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.936,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6322645121929396,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.2958212393671274
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.23132873209118843
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.09596953743100166
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.4236584593733152
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7900858353823423
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9986011020151739,
              "spearman": 0.9991336687013466,
              "auroc_top30_worst": 0.9998266666666666,
              "pairwise_seed_ranking": 0.9438,
              "predicted_best_mean_error": 1.0222262767255306,
              "seed0_mean_error": 1.1003441655039787,
              "random_seed_mean_error": 1.0959886793792248,
              "oracle_best_mean_error": 1.0204971807599068,
              "improvement_over_seed0": 0.07811788877844816,
              "gap_to_oracle": 0.0017290959656237614,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1724560294151306
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31566646807193754
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5103517429828643
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7301354689757029
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0952668563961983
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2861740112304694,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8930213554302852,
                  "rejected_mean_error": 2.9154763650894164,
                  "gap_rejected_minus_accepted": 2.022455009659131
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5072998702526093,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7301354689757029,
                  "rejected_mean_error": 2.1906610186576843,
                  "gap_rejected_minus_accepted": 1.4605255496819813
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9429734647274017,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5103517429828643,
                  "rejected_mean_error": 1.6801819698095322,
                  "gap_rejected_minus_accepted": 1.1698302268266678
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5666707456111908,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.31566646807193754,
                  "rejected_mean_error": 1.3551336525042852,
                  "gap_rejected_minus_accepted": 1.0394671844323478
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.342491745948792,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8979182030757268,
                  "rejected_mean_error": 2.922177827358246,
                  "gap_rejected_minus_accepted": 2.0242596242825193
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5179860889911652,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7310666835308075,
                  "rejected_mean_error": 2.2081766114234926,
                  "gap_rejected_minus_accepted": 1.4771099278926851
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9445032179355621,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5043064407110214,
                  "rejected_mean_error": 1.696381890296936,
                  "gap_rejected_minus_accepted": 1.1920754495859147
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5723030269145966,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.3105356149673462,
                  "rejected_mean_error": 1.3636136823495228,
                  "gap_rejected_minus_accepted": 1.0530780673821767
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9727565607713434,
              "spearman": 0.9708148270728425,
              "auroc_top30_bad": 0.9803059047619047,
              "mae": 0.38090018636930034,
              "mse": 0.180430666747227,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.904,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6129223880247028,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1650816426873207
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2277179276227951
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6828000528693199
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0377946244160334
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.970603903675354,
              "spearman": 0.9757187490039996,
              "auroc_top30_worst": 0.9869958095238095,
              "pairwise_seed_ranking": 0.8876,
              "predicted_best_mean_error": 1.4671502890586854,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.06164353466033923,
              "gap_to_oracle": 0.004307266950607458,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8892550640106202
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9829717907003868
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1693759243011475
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.358956445763106
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6684649109840395,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4598336868286133,
                  "rejected_mean_error": 2.226480435371399,
                  "gap_rejected_minus_accepted": 0.7666467485427857
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5213875472545624,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3584025846346974,
                  "rejected_mean_error": 2.0696477006418634,
                  "gap_rejected_minus_accepted": 0.711245116007166
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1089473366737366,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1693759243011475,
                  "rejected_mean_error": 1.9036207990646363,
                  "gap_rejected_minus_accepted": 0.7342448747634889
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7668797224760056,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9836595814448957,
                  "rejected_mean_error": 1.7211712946759472,
                  "gap_rejected_minus_accepted": 0.7375117132310515
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6763537883758546,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.454019888771905,
                  "rejected_mean_error": 2.201759238243103,
                  "gap_rejected_minus_accepted": 0.7477393494711981
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5270854234695435,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3497034878654277,
                  "rejected_mean_error": 2.0603794237924,
                  "gap_rejected_minus_accepted": 0.7106759359269723
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1344941854476929,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1580268440246582,
                  "rejected_mean_error": 1.899560803413391,
                  "gap_rejected_minus_accepted": 0.7415339593887329
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7729741185903549,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9630183549154372,
                  "rejected_mean_error": 1.7194026714977733,
                  "gap_rejected_minus_accepted": 0.7563843165823361
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9683101778476088,
              "spearman": 0.9670287010909333,
              "auroc_top30_bad": 0.9831474285714287,
              "mae": 0.48128692103134235,
              "mse": 0.307775626784164,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.92,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6395753957170343,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.19838540011644362
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20567598972320555
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.696909828364849
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0554761983156205
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9435003454464583,
              "spearman": 0.9616250491040316,
              "auroc_top30_worst": 0.9820556190476191,
              "pairwise_seed_ranking": 0.9052,
              "predicted_best_mean_error": 1.7262981752157212,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08085040616989136,
              "gap_to_oracle": 0.002411375045776376,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9404483051300049
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1181007000880363
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2945665420532226
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4654841045580946
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7959873199462897,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6553084498511421,
                  "rejected_mean_error": 3.1268198261260984,
                  "gap_rejected_minus_accepted": 1.4715113762749563
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.490998238325119,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4650531107740696,
                  "rejected_mean_error": 2.812523065664517,
                  "gap_rejected_minus_accepted": 1.3474699548904474
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1635085940361023,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2945665420532226,
                  "rejected_mean_error": 2.3103526329040527,
                  "gap_rejected_minus_accepted": 1.01578609085083
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9062207788228989,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.119092284300076,
                  "rejected_mean_error": 2.030734897932095,
                  "gap_rejected_minus_accepted": 0.9116426136320193
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8032382726669312,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6595428370104897,
                  "rejected_mean_error": 3.135600280761719,
                  "gap_rejected_minus_accepted": 1.4760574437512293
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5269995331764221,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.462422294253334,
                  "rejected_mean_error": 2.8303837511274548,
                  "gap_rejected_minus_accepted": 1.3679614568741207
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1581798195838928,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.287332379102707,
                  "rejected_mean_error": 2.326964783668518,
                  "gap_rejected_minus_accepted": 1.039632404565811
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9189177751541138,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1203758541553739,
                  "rejected_mean_error": 2.038521211415051,
                  "gap_rejected_minus_accepted": 0.9181453572596772
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9740558265292234,
              "spearman": 0.9718259819611038,
              "auroc_top30_bad": 0.993335619047619,
              "mae": 0.3687250601820182,
              "mse": 0.17218443492974772,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.836,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.650534012175126,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22817181611061096
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20894639303684234
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5927315492630005
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.935522092628479
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9775334186972574,
              "spearman": 0.9768833818133645,
              "auroc_top30_worst": 0.9930148571428571,
              "pairwise_seed_ranking": 0.9084,
              "predicted_best_mean_error": 1.5544503329992294,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06487194526195528,
              "gap_to_oracle": 0.0033070727586745896,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5888709862232209
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.866738944959182
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1222176388263703
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3126289682157004
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2730704069137584,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4771119389269087,
                  "rejected_mean_error": 2.936095895767212,
                  "gap_rejected_minus_accepted": 1.4589839568403031
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6585503816604614,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3117853440304577,
                  "rejected_mean_error": 2.5546966482656073,
                  "gap_rejected_minus_accepted": 1.2429113042351496
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1488563418388367,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1222176388263703,
                  "rejected_mean_error": 2.123803030395508,
                  "gap_rejected_minus_accepted": 1.0015853915691377
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7809171676635742,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8682379696887141,
                  "rejected_mean_error": 1.8751381363405617,
                  "gap_rejected_minus_accepted": 1.0069001666518476
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2612815380096434,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4691338721911114,
                  "rejected_mean_error": 2.971017932891846,
                  "gap_rejected_minus_accepted": 1.5018840607007344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6675907671451569,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3026016392809823,
                  "rejected_mean_error": 2.559429571742103,
                  "gap_rejected_minus_accepted": 1.256827932461121
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1514414548873901,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1103644309043885,
                  "rejected_mean_error": 2.128280125617981,
                  "gap_rejected_minus_accepted": 1.0179156947135926
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7728981375694275,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8515127906723629,
                  "rejected_mean_error": 1.8779960628499321,
                  "gap_rejected_minus_accepted": 1.0264832721775692
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
        "best_epoch": 8,
        "best_calib_loss": 0.06422016024589539,
        "train_time_sec": 41.61429452896118,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9860563485420212,
              "spearman": 0.9829868237418682,
              "auroc_top30_bad": 0.997043857142857,
              "mae": 0.1292687033710319,
              "mse": 0.030910159267773598,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6470504283805635,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.27921950043737886
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.212220670491457
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.09753889058232307
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.42561469215949377
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7900858353823423
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979654899052985,
              "spearman": 0.9959915711996628,
              "auroc_top30_worst": 0.9975809523809523,
              "pairwise_seed_ranking": 0.9144,
              "predicted_best_mean_error": 1.0239749067723751,
              "seed0_mean_error": 1.1003441655039787,
              "random_seed_mean_error": 1.0959886793792248,
              "oracle_best_mean_error": 1.0204971807599068,
              "improvement_over_seed0": 0.0763692587316036,
              "gap_to_oracle": 0.0034777260124683185,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17605780494213105
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31736628677845
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5114225241184235
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7310105700016022
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0952668563961983
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.33707654476166,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8928564574586021,
                  "rejected_mean_error": 2.916960446834564,
                  "gap_rejected_minus_accepted": 2.024103989375962
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5183209478855133,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7310105700016022,
                  "rejected_mean_error": 2.1880357155799866,
                  "gap_rejected_minus_accepted": 1.4570251455783843
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9432727992534637,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5114225241184235,
                  "rejected_mean_error": 1.6791111886739731,
                  "gap_rejected_minus_accepted": 1.1676886645555498
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5720678120851517,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.31736628677845,
                  "rejected_mean_error": 1.354567046268781,
                  "gap_rejected_minus_accepted": 1.037200759490331
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.362138271331787,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8980153806342019,
                  "rejected_mean_error": 2.9213032293319703,
                  "gap_rejected_minus_accepted": 2.0232878486977683
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.527581363916397,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7319811193943023,
                  "rejected_mean_error": 2.205433303833008,
                  "gap_rejected_minus_accepted": 1.4734521844387056
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9537736177444458,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5053626319169998,
                  "rejected_mean_error": 1.6953256990909575,
                  "gap_rejected_minus_accepted": 1.1899630671739576
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5685010701417923,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.3121546804904938,
                  "rejected_mean_error": 1.363073993841807,
                  "gap_rejected_minus_accepted": 1.0509193133513133
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9657378992608083,
              "spearman": 0.968457844604019,
              "auroc_top30_bad": 0.9739756190476191,
              "mae": 0.3671193278594409,
              "mse": 0.1751748125780939,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6333001016508856,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12732690793275833
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24127006342411042
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6834137962698936
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0415565532922744
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9520302934032105,
              "spearman": 0.9558170177388915,
              "auroc_top30_worst": 0.9688868571428572,
              "pairwise_seed_ranking": 0.8532,
              "predicted_best_mean_error": 1.4716869733333588,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.057106850385665764,
              "gap_to_oracle": 0.008843951225280922,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8968936033248901
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9967764201454627
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1736792314529418
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3671788287315287
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7230474829673772,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4580407768885295,
                  "rejected_mean_error": 2.2426166248321535,
                  "gap_rejected_minus_accepted": 0.784575847943624
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.504652500152588,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.36670246475407,
                  "rejected_mean_error": 2.0448010946615054,
                  "gap_rejected_minus_accepted": 0.6780986299074354
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1219351887702942,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1736792314529418,
                  "rejected_mean_error": 1.8993174919128417,
                  "gap_rejected_minus_accepted": 0.7256382604598999
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.765572115778923,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9975417031647679,
                  "rejected_mean_error": 1.7165340437705896,
                  "gap_rejected_minus_accepted": 0.7189923406058217
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7580410003662108,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4510095177756415,
                  "rejected_mean_error": 2.2288525772094725,
                  "gap_rejected_minus_accepted": 0.777843059433831
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5084357559680939,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3566990988777283,
                  "rejected_mean_error": 2.039614673644777,
                  "gap_rejected_minus_accepted": 0.6829155747670488
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.128121256828308,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.162729037284851,
                  "rejected_mean_error": 1.8948586101531983,
                  "gap_rejected_minus_accepted": 0.7321295728683472
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7713846862316132,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9791731096449352,
                  "rejected_mean_error": 1.7139601605461243,
                  "gap_rejected_minus_accepted": 0.7347870509011891
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9382170066362185,
              "spearman": 0.9376894051499726,
              "auroc_top30_bad": 0.9679447619047619,
              "mae": 0.4968263514632739,
              "mse": 0.3663767677841132,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6270407546826304,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.18519107067584992
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2337467785358429
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7056756506800651
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.09511419664224
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8676280445400025,
              "spearman": 0.9029855311057259,
              "auroc_top30_worst": 0.9584121904761904,
              "pairwise_seed_ranking": 0.8916,
              "predicted_best_mean_error": 1.7272458060979843,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.07990277528762824,
              "gap_to_oracle": 0.0033590059280395046,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9563514084815979
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1461410617981203
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3161786994934082
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5126760181333465
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5933146595954897,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6799717078738743,
                  "rejected_mean_error": 2.9048505039215087,
                  "gap_rejected_minus_accepted": 1.2248787960476344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3834232687950134,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5112902744093726,
                  "rejected_mean_error": 2.6741070198936585,
                  "gap_rejected_minus_accepted": 1.162816745484286
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1326538920402527,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3161786994934082,
                  "rejected_mean_error": 2.288740475463867,
                  "gap_rejected_minus_accepted": 0.972561775970459
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8588900864124298,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1475639358496132,
                  "rejected_mean_error": 2.0212240901039147,
                  "gap_rejected_minus_accepted": 0.8736601542543014
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5732393264770508,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.688059416214625,
                  "rejected_mean_error": 2.8789510679244996,
                  "gap_rejected_minus_accepted": 1.1908916517098747
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3847971558570862,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5081840292973951,
                  "rejected_mean_error": 2.6945512994887335,
                  "gap_rejected_minus_accepted": 1.1863672701913384
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1243484020233154,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.313063330411911,
                  "rejected_mean_error": 2.301233832359314,
                  "gap_rejected_minus_accepted": 0.9881705019474027
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8656903356313705,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1598261003456418,
                  "rejected_mean_error": 2.025230486762715,
                  "gap_rejected_minus_accepted": 0.8654043864170733
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9678010818985213,
              "spearman": 0.9748272130750602,
              "auroc_top30_bad": 0.9951344761904761,
              "mae": 0.3909226137764826,
              "mse": 0.19725212923315763,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6595800814276709,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1514897006750107
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25550149631500246
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5926383444786072
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9349590229670207
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9840364363660337,
              "spearman": 0.9758284133301846,
              "auroc_top30_worst": 0.9975710476190476,
              "pairwise_seed_ranking": 0.8688,
              "predicted_best_mean_error": 1.5572415068149568,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06208077144622792,
              "gap_to_oracle": 0.006098246574401944,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5917152338027954
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.877714914866747
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1175573517322541
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3108531352617085
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.247510862350464,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4757418831984201,
                  "rejected_mean_error": 2.9484263973236082,
                  "gap_rejected_minus_accepted": 1.472684514125188
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5954477488994598,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3100330136565286,
                  "rejected_mean_error": 2.5599424423881993,
                  "gap_rejected_minus_accepted": 1.2499094287316708
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.113660752773285,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1175573517322541,
                  "rejected_mean_error": 2.128463317489624,
                  "gap_rejected_minus_accepted": 1.0109059657573698
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7303986102342606,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8786898018262638,
                  "rejected_mean_error": 1.8716467559146779,
                  "gap_rejected_minus_accepted": 0.9929569540884141
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2372334241867065,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.468246943420834,
                  "rejected_mean_error": 2.979000291824341,
                  "gap_rejected_minus_accepted": 1.5107533484035067
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.618327021598816,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2980891290832968,
                  "rejected_mean_error": 2.572823848043169,
                  "gap_rejected_minus_accepted": 1.2747347189598723
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1423171758651733,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1069465107917786,
                  "rejected_mean_error": 2.131698045730591,
                  "gap_rejected_minus_accepted": 1.0247515349388123
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7546085566282272,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8688026978856042,
                  "rejected_mean_error": 1.8721711208476102,
                  "gap_rejected_minus_accepted": 1.003368422962006
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
        "best_epoch": 12,
        "best_calib_loss": 0.07598327100276947,
        "train_time_sec": 30.28937530517578,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9899051283446296,
              "spearman": 0.9926962125329183,
              "auroc_top30_bad": 0.9989638571428572,
              "mae": 0.09907379782177533,
              "mse": 0.02376784512338128,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.985,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6253508032672077,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.32300288558006285
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.23056683042645454
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.09651333972811699
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.4241860845208168
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7900858353823423
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9975757702875041,
              "spearman": 0.9980315020652599,
              "auroc_top30_worst": 0.9995015238095238,
              "pairwise_seed_ranking": 0.9112,
              "predicted_best_mean_error": 1.0234860960543155,
              "seed0_mean_error": 1.1003441655039787,
              "random_seed_mean_error": 1.0959886793792248,
              "oracle_best_mean_error": 1.0204971807599068,
              "improvement_over_seed0": 0.07685806944966322,
              "gap_to_oracle": 0.0029889152944087005,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17328001314401625
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31622831428050996
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5107903684854508
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7304745007038116
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0952668563961983
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2760744571685794,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8931671235428916,
                  "rejected_mean_error": 2.9141644520759584,
                  "gap_rejected_minus_accepted": 2.020997328533067
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5112112760543823,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7304745007038116,
                  "rejected_mean_error": 2.189643923473358,
                  "gap_rejected_minus_accepted": 1.4591694227695464
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9091149866580963,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5107903684854508,
                  "rejected_mean_error": 1.6797433443069458,
                  "gap_rejected_minus_accepted": 1.1689529758214952
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.549853965640068,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.31622831428050996,
                  "rejected_mean_error": 1.354946370434761,
                  "gap_rejected_minus_accepted": 1.038718056154251
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.326746869087219,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8980806575218836,
                  "rejected_mean_error": 2.9207157373428343,
                  "gap_rejected_minus_accepted": 2.022635079820951
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5250287055969238,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7314394897619884,
                  "rejected_mean_error": 2.2070581927299497,
                  "gap_rejected_minus_accepted": 1.4756187029679615
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9126594960689545,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5045143353939057,
                  "rejected_mean_error": 1.6961739956140518,
                  "gap_rejected_minus_accepted": 1.1916596602201461
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5579192489385605,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.31095348596572875,
                  "rejected_mean_error": 1.3634743920167287,
                  "gap_rejected_minus_accepted": 1.052520906051
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9693476610831677,
              "spearman": 0.9711345128342989,
              "auroc_top30_bad": 0.9801401904761905,
              "mae": 0.41646503792775763,
              "mse": 0.21425070836503982,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5903954535868691,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12973245483636855
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2502999710559845
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.683597484433651
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0391161335229873
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9568430167910889,
              "spearman": 0.968076099632704,
              "auroc_top30_worst": 0.9834422857142857,
              "pairwise_seed_ranking": 0.8524,
              "predicted_best_mean_error": 1.4727676677703858,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.0560261559486388,
              "gap_to_oracle": 0.009924645662307885,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9140148429870606
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9835810978443195
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1731853073120118
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3615101138665986
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5943615317344666,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4594536294937135,
                  "rejected_mean_error": 2.229900951385498,
                  "gap_rejected_minus_accepted": 0.7704473218917847
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4197207987308502,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3609738142538732,
                  "rejected_mean_error": 2.0619504413665672,
                  "gap_rejected_minus_accepted": 0.700976627112694
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.023051381111145,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1731853073120118,
                  "rejected_mean_error": 1.899811416053772,
                  "gap_rejected_minus_accepted": 0.7266261087417603
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7466263473033905,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9833926886034469,
                  "rejected_mean_error": 1.7212604488481706,
                  "gap_rejected_minus_accepted": 0.7378677602447238
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6237545013427734,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4524016030629476,
                  "rejected_mean_error": 2.2163238096237183,
                  "gap_rejected_minus_accepted": 0.7639222065607707
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4211039245128632,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3526429027159583,
                  "rejected_mean_error": 2.0516544939979675,
                  "gap_rejected_minus_accepted": 0.6990115912820092
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0215924382209778,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.161110396385193,
                  "rejected_mean_error": 1.8964772510528565,
                  "gap_rejected_minus_accepted": 0.7353668546676635
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7506825774908066,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.962123745963687,
                  "rejected_mean_error": 1.7197040638184165,
                  "gap_rejected_minus_accepted": 0.7575803178547295
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9485395195613499,
              "spearman": 0.9558022664484495,
              "auroc_top30_bad": 0.9779260952380953,
              "mae": 0.54718199282681,
              "mse": 0.41283948090555067,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5946551852271296,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1266893026828766
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2282786732673645
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.701631515109539
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0862645739793777
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8939998297912677,
              "spearman": 0.9353999397119614,
              "auroc_top30_worst": 0.973056,
              "pairwise_seed_ranking": 0.8812,
              "predicted_best_mean_error": 1.7285077246427536,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.07864085674285892,
              "gap_to_oracle": 0.004620924472808818,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9552388796806336
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1252543368400671
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3036206771850587
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4993025827001152
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5978995442390442,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6587693837483724,
                  "rejected_mean_error": 3.0956714210510254,
                  "gap_rejected_minus_accepted": 1.436902037302653
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3173919916152954,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4989490310563094,
                  "rejected_mean_error": 2.711051892167844,
                  "gap_rejected_minus_accepted": 1.2121028611115345
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0589131116867065,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3036206771850587,
                  "rejected_mean_error": 2.301298497772217,
                  "gap_rejected_minus_accepted": 0.9976778205871581
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.801392525434494,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.126946514406905,
                  "rejected_mean_error": 2.0281112330191418,
                  "gap_rejected_minus_accepted": 0.9011647186122367
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5959837198257447,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.659165840016471,
                  "rejected_mean_error": 3.138993253707886,
                  "gap_rejected_minus_accepted": 1.479827413691415
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.305307298898697,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5020544170377088,
                  "rejected_mean_error": 2.712745545402406,
                  "gap_rejected_minus_accepted": 1.210691128364697
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0623866319656372,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2946067607402802,
                  "rejected_mean_error": 2.319690402030945,
                  "gap_rejected_minus_accepted": 1.0250836412906648
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8003648966550827,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1229548619853125,
                  "rejected_mean_error": 2.0376523478145905,
                  "gap_rejected_minus_accepted": 0.914697485829278
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9728592986515106,
              "spearman": 0.9773189392468934,
              "auroc_top30_bad": 0.9947489523809525,
              "mae": 0.4251405859064726,
              "mse": 0.22319002985684028,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6033420271923833,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13375429600477218
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22202275347709655
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5962732498645782
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9346135945002237
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9777885077560108,
              "spearman": 0.9683606223107984,
              "auroc_top30_worst": 0.9976807619047618,
              "pairwise_seed_ranking": 0.8536,
              "predicted_best_mean_error": 1.5567437210083008,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06257855725288386,
              "gap_to_oracle": 0.005600460767746007,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6206611900329589
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8803404459777551
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.121877742433548
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3100573858027773
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1314383268356325,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4774290909502241,
                  "rejected_mean_error": 2.933241527557373,
                  "gap_rejected_minus_accepted": 1.455812436607149
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5175687670707703,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3092331663966814,
                  "rejected_mean_error": 2.56233687332263,
                  "gap_rejected_minus_accepted": 1.2531037069259485
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0506647825241089,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.121877742433548,
                  "rejected_mean_error": 2.12414292678833,
                  "gap_rejected_minus_accepted": 1.002265184354782
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.742109939455986,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8819085729960054,
                  "rejected_mean_error": 1.8705715420660876,
                  "gap_rejected_minus_accepted": 0.9886629690700821
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1480738162994384,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4690349062283834,
                  "rejected_mean_error": 2.9719086265563965,
                  "gap_rejected_minus_accepted": 1.5028737203280131
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5437543988227844,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2971497841059842,
                  "rejected_mean_error": 2.5756120624996366,
                  "gap_rejected_minus_accepted": 1.2784622783936523
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.062731385231018,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.108585162639618,
                  "rejected_mean_error": 2.1300593938827515,
                  "gap_rejected_minus_accepted": 1.0214742312431335
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7537781894207001,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8675154021808079,
                  "rejected_mean_error": 1.8726048087053757,
                  "gap_rejected_minus_accepted": 1.0050894065245677
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
        "best_epoch": 66,
        "best_calib_loss": 0.09492001682519913,
        "train_time_sec": 10.783213138580322,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9108325174456903,
              "spearman": 0.8640588532616477,
              "auroc_top30_bad": 0.9287775238095238,
              "mae": 0.16503146103252656,
              "mse": 0.13547006189036692,
              "expert_lt_perturb_large": 0.99,
              "expert_lt_other_task": 0.516,
              "expert_lt_simvla_seed0": 0.971,
              "same_context_pred_std": 0.6840237433020921,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4193558727633208
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.46408338079806416
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6190710933151655
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8952120473702128
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2563167701877187
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9970138733844467,
              "spearman": 0.9951717683188706,
              "auroc_top30_worst": 0.9983601904761905,
              "pairwise_seed_ranking": 0.8603,
              "predicted_best_mean_error": 1.5207521255612373,
              "seed0_mean_error": 1.5949208683073521,
              "random_seed_mean_error": 1.5911614976227284,
              "oracle_best_mean_error": 1.5142234272062778,
              "improvement_over_seed0": 0.07416874274611485,
              "gap_to_oracle": 0.006528698354959506,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6671670615673065
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7947630714893341
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9873985015392304
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2156425422668458
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5904509642362594
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7337514400482186,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3834371227953168,
                  "rejected_mean_error": 3.4535755372047423,
                  "gap_rejected_minus_accepted": 2.0701384144094255
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.974184662103653,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2156425422668458,
                  "rejected_mean_error": 2.7148762301445006,
                  "gap_rejected_minus_accepted": 1.4992336878776549
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3883999586105347,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9873985015392304,
                  "rejected_mean_error": 2.1935034269332885,
                  "gap_rejected_minus_accepted": 1.2061049253940581
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.019096165895462,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7947630714893341,
                  "rejected_mean_error": 1.855680261818568,
                  "gap_rejected_minus_accepted": 1.0609171903292338
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.742483520507813,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.387746073835426,
                  "rejected_mean_error": 3.4594940185546874,
                  "gap_rejected_minus_accepted": 2.0717479447192613
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9939951300621033,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2163562546173732,
                  "rejected_mean_error": 2.730614709377289,
                  "gap_rejected_minus_accepted": 1.5142584547599158
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3985188603401184,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9785840616822242,
                  "rejected_mean_error": 2.21125767493248,
                  "gap_rejected_minus_accepted": 1.2326736132502556
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.001441240310669,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7867851411104202,
                  "rejected_mean_error": 1.8642994440396627,
                  "gap_rejected_minus_accepted": 1.0775143029292424
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5219264146312688,
              "spearman": 0.4875690577399871,
              "auroc_top30_bad": 0.6573763809523809,
              "mae": 0.4856350064277649,
              "mse": 0.5341252413014147,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.964,
              "same_context_pred_std": 0.6135761120285723,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5633154588341713
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8084798677921295
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9319505029320717
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1694414593458176
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.4302443967221984,
              "spearman": 0.5166936288599225,
              "auroc_top30_worst": 0.7450697142857144,
              "pairwise_seed_ranking": 0.736,
              "predicted_best_mean_error": 1.4894931066036223,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.039300717115402284,
              "gap_to_oracle": 0.0266500844955444,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0273279280662537
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1412775793518775
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3289374453544616
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4902473415520145
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.168320655822754,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.523190745777554,
                  "rejected_mean_error": 1.6562669048309326,
                  "gap_rejected_minus_accepted": 0.13307615905337866
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8170552551746368,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4906794564955517,
                  "rejected_mean_error": 1.6736623046878047,
                  "gap_rejected_minus_accepted": 0.18298284819225308
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4943177103996277,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3289374453544616,
                  "rejected_mean_error": 1.744059278011322,
                  "gap_rejected_minus_accepted": 0.4151218326568604
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.212509274482727,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1417540336569276,
                  "rejected_mean_error": 1.6683606612262503,
                  "gap_rejected_minus_accepted": 0.5266066275693226
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1768858194351197,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.519113179842631,
                  "rejected_mean_error": 1.6159196186065674,
                  "gap_rejected_minus_accepted": 0.09680643876393646
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8034330010414124,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4797659270903643,
                  "rejected_mean_error": 1.674321072442191,
                  "gap_rejected_minus_accepted": 0.19455514535182683
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.517200529575348,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3249384603500367,
                  "rejected_mean_error": 1.7326491870880127,
                  "gap_rejected_minus_accepted": 0.40771072673797604
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2083057165145874,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1287070635765317,
                  "rejected_mean_error": 1.6635824113606132,
                  "gap_rejected_minus_accepted": 0.5348753477840815
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4521650561133024,
              "spearman": 0.39573496754654097,
              "auroc_top30_bad": 0.5663055238095238,
              "mae": 0.6510380037605763,
              "mse": 0.8107525902223193,
              "expert_lt_perturb_large": 0.94,
              "expert_lt_other_task": 0.476,
              "expert_lt_simvla_seed0": 0.884,
              "same_context_pred_std": 0.6337459025676756,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5301058214902877
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5826403109312057
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1671701202154159
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3008366799592972
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.11303825508466353,
              "spearman": -0.06039194290684347,
              "auroc_top30_worst": 0.35331961904761905,
              "pairwise_seed_ranking": 0.7072,
              "predicted_best_mean_error": 1.7605376065969467,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.04661097478866583,
              "gap_to_oracle": 0.036650806427001914,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.7747495529651642
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.012019169349701
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8797910633087158
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.80190313624929
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8758588075637825,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7463310440911186,
                  "rejected_mean_error": 2.3076164779663086,
                  "gap_rejected_minus_accepted": 0.56128543387519
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9053646326065063,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.8016802735364297,
                  "rejected_mean_error": 1.8047925496634585,
                  "gap_rejected_minus_accepted": 0.0031122761270288013
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4441416263580322,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.8797910633087158,
                  "rejected_mean_error": 1.7251281116485595,
                  "gap_rejected_minus_accepted": -0.1546629516601563
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1502707302570343,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.0097453008634973,
                  "rejected_mean_error": 1.7332168678527453,
                  "gap_rejected_minus_accepted": -0.27652843301075203
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7880968809127804,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7481526039706337,
                  "rejected_mean_error": 2.3381123781204223,
                  "gap_rejected_minus_accepted": 0.5899597741497886
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.910915583372116,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.798764350420651,
                  "rejected_mean_error": 1.8320351082181174,
                  "gap_rejected_minus_accepted": 0.033270757797466466
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4354369640350342,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8737859961986543,
                  "rejected_mean_error": 1.7405111665725708,
                  "gap_rejected_minus_accepted": -0.1332748296260835
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1720440685749054,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.003498590654797,
                  "rejected_mean_error": 1.740998578262839,
                  "gap_rejected_minus_accepted": -0.2625000123919581
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6674720530806053,
              "spearman": 0.6434426291754651,
              "auroc_top30_bad": 0.7904857142857142,
              "mae": 0.46001943586468697,
              "mse": 0.4190393692381489,
              "expert_lt_perturb_large": 0.976,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 0.964,
              "same_context_pred_std": 0.6494587672947533,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5118401079177857
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7165428616762162
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7717247172117233
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0394834584712982
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6529185759286283,
              "spearman": 0.5679005531523541,
              "auroc_top30_worst": 0.841840761904762,
              "pairwise_seed_ranking": 0.7724,
              "predicted_best_mean_error": 1.5639855983257294,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.055336679935455324,
              "gap_to_oracle": 0.012842338085174543,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7728800990581512
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0972871462313027
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2962454720973968
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.423357806448489
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.404586982727051,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5277999844815997,
                  "rejected_mean_error": 2.4799034857749938,
                  "gap_rejected_minus_accepted": 0.952103501293394
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9711875319480896,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4224025620149574,
                  "rejected_mean_error": 2.223551813596354,
                  "gap_rejected_minus_accepted": 0.8011492515813965
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6686571836471558,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2962454720973968,
                  "rejected_mean_error": 1.9497751971244812,
                  "gap_rejected_minus_accepted": 0.6535297250270844
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3048228323459625,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.098207426052124,
                  "rejected_mean_error": 1.7983180297858687,
                  "gap_rejected_minus_accepted": 0.7001106037337448
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4421247243881226,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5206858717070686,
                  "rejected_mean_error": 2.50704993724823,
                  "gap_rejected_minus_accepted": 0.9863640655411614
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.973122090101242,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.404882228310733,
                  "rejected_mean_error": 2.2558348074791925,
                  "gap_rejected_minus_accepted": 0.8509525791684596
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6796395182609558,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2764229736328125,
                  "rejected_mean_error": 1.9622215828895568,
                  "gap_rejected_minus_accepted": 0.6857986092567443
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.253971129655838,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0562014267558144,
                  "rejected_mean_error": 1.8090367897309083,
                  "gap_rejected_minus_accepted": 0.7528353629750939
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
        "best_calib_loss": 0.016147920861840248,
        "train_time_sec": 35.15939378738403,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.999420773373057,
              "spearman": 0.9990794708177707,
              "auroc_top30_bad": 0.9996841428571428,
              "mae": 0.022221498896414414,
              "mse": 0.0009056175512452357,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7005887833742658,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10357018548203632
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23920313561242074
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5458514807774685
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8767097188998635
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2563167701877187
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999471587059,
              "spearman": 0.9994288384491399,
              "auroc_top30_worst": 0.9998222857142858,
              "pairwise_seed_ranking": 0.9488,
              "predicted_best_mean_error": 1.5152195405066013,
              "seed0_mean_error": 1.5949208683073521,
              "random_seed_mean_error": 1.5911614976227284,
              "oracle_best_mean_error": 1.5142234272062778,
              "improvement_over_seed0": 0.07970132780075079,
              "gap_to_oracle": 0.0009961133003235645,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6571682084798813
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7915717805385589
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9857856081008911
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2148672366142272
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5904509642362594
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7689059972763066,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3832249317963918,
                  "rejected_mean_error": 3.455485256195068,
                  "gap_rejected_minus_accepted": 2.0722603243986764
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9540370404720306,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2148672366142272,
                  "rejected_mean_error": 2.717202147102356,
                  "gap_rejected_minus_accepted": 1.5023349104881287
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.366950273513794,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9857856081008911,
                  "rejected_mean_error": 2.195116320371628,
                  "gap_rejected_minus_accepted": 1.2093307122707369
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9901778846979141,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7915717805385589,
                  "rejected_mean_error": 1.8567440254688263,
                  "gap_rejected_minus_accepted": 1.0651722449302674
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.812003540992737,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3876471648282476,
                  "rejected_mean_error": 3.460384199619293,
                  "gap_rejected_minus_accepted": 2.0727370347910457
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9728968441486359,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2155703403552374,
                  "rejected_mean_error": 2.7329724521636964,
                  "gap_rejected_minus_accepted": 1.517402111808459
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.371410310268402,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9773974435925483,
                  "rejected_mean_error": 2.212444293022156,
                  "gap_rejected_minus_accepted": 1.2350468494296076
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9876740127801895,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7842887929677963,
                  "rejected_mean_error": 1.865131560087204,
                  "gap_rejected_minus_accepted": 1.0808427671194076
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9631291696972955,
              "spearman": 0.949359584116095,
              "auroc_top30_bad": 0.957895619047619,
              "mae": 0.13574104191735387,
              "mse": 0.04333968003223198,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6695213460911622,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08741412627696991
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2274751665353775
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6973524299025535
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0475391834497452
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9624166448838851,
              "spearman": 0.9694615602313987,
              "auroc_top30_worst": 0.9850361904761905,
              "pairwise_seed_ranking": 0.8952,
              "predicted_best_mean_error": 1.4677270917892455,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.06106673192977907,
              "gap_to_oracle": 0.004884069681167613,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8806920666694641
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9773780906047577
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1714189697265625
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3609726261228388
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1079188823699955,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4656956890953912,
                  "rejected_mean_error": 2.1737224149703978,
                  "gap_rejected_minus_accepted": 0.7080267258750066
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9565062820911407,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3605278565000698,
                  "rejected_mean_error": 2.0632854650576657,
                  "gap_rejected_minus_accepted": 0.702757608557596
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.500063180923462,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1714189697265625,
                  "rejected_mean_error": 1.901577753639221,
                  "gap_rejected_minus_accepted": 0.7301587839126586
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2049023807048798,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9779752169173366,
                  "rejected_mean_error": 1.7230701272235736,
                  "gap_rejected_minus_accepted": 0.745094910306237
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1248229503631593,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4572483253479005,
                  "rejected_mean_error": 2.172703309059143,
                  "gap_rejected_minus_accepted": 0.7154549837112425
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9645942747592926,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3515189988090393,
                  "rejected_mean_error": 2.054990526229616,
                  "gap_rejected_minus_accepted": 0.7034715274205767
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.480238676071167,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1590171298980714,
                  "rejected_mean_error": 1.898570517539978,
                  "gap_rejected_minus_accepted": 0.7395533876419067
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2132335007190704,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9556582428160167,
                  "rejected_mean_error": 1.7218822814564017,
                  "gap_rejected_minus_accepted": 0.7662240386403849
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9484039455525827,
              "spearman": 0.9364126576453675,
              "auroc_top30_bad": 0.9356411428571428,
              "mae": 0.21303052610456943,
              "mse": 0.10259913813802675,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6705791335013553,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09315723764896393
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23507748699188233
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7290253880381584
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0690973006486892
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9474845201725377,
              "spearman": 0.9478919039308187,
              "auroc_top30_worst": 0.9696579047619047,
              "pairwise_seed_ranking": 0.9084,
              "predicted_best_mean_error": 1.7261399589776993,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08100862240791318,
              "gap_to_oracle": 0.002253158807754563,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9423553581237794
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1160933818572607
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3160817102432252
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.468752710676905
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3245728731155397,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6536944113837349,
                  "rejected_mean_error": 3.1413461723327636,
                  "gap_rejected_minus_accepted": 1.4876517609490287
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8984268307685852,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4682048155887404,
                  "rejected_mean_error": 2.8030880899094166,
                  "gap_rejected_minus_accepted": 1.3348832743206762
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.57795912027359,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3160817102432252,
                  "rejected_mean_error": 2.2888374647140504,
                  "gap_rejected_minus_accepted": 0.9727557544708252
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3315673172473907,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.116853256956838,
                  "rejected_mean_error": 2.031482833426688,
                  "gap_rejected_minus_accepted": 0.9146295764698502
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.312837243080139,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6588124930858612,
                  "rejected_mean_error": 3.142173376083374,
                  "gap_rejected_minus_accepted": 1.4833608829975127
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9256584644317627,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4661541595497234,
                  "rejected_mean_error": 2.819306627152458,
                  "gap_rejected_minus_accepted": 1.3531524676027347
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5903300046920776,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3097704627513886,
                  "rejected_mean_error": 2.3045267000198364,
                  "gap_rejected_minus_accepted": 0.9947562372684478
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3395892679691315,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1195109756219954,
                  "rejected_mean_error": 2.038812587605441,
                  "gap_rejected_minus_accepted": 0.9193016119834454
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9799898431121801,
              "spearman": 0.9764026635102829,
              "auroc_top30_bad": 0.9864921904761905,
              "mae": 0.11859596265032887,
              "mse": 0.02832284222451675,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7088093628025215,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07088250178098679
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2169684586286545
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5929760746002197
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9432353164037068
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9828100225603542,
              "spearman": 0.9817770748013279,
              "auroc_top30_worst": 0.9938438095238096,
              "pairwise_seed_ranking": 0.918,
              "predicted_best_mean_error": 1.5549670135974885,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06435526466369623,
              "gap_to_oracle": 0.0038237533569336346,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5772907145023346
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8661763615524157
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1189322687625884
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3121846838355826
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5216913938522354,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4763242715464697,
                  "rejected_mean_error": 2.9431849021911622,
                  "gap_rejected_minus_accepted": 1.4668606306446925
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0733564496040344,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.311757654269706,
                  "rejected_mean_error": 2.5547795406164835,
                  "gap_rejected_minus_accepted": 1.2430218863467775
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.570241928100586,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1189322687625884,
                  "rejected_mean_error": 2.1270884004592894,
                  "gap_rejected_minus_accepted": 1.008156131696701
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.253305971622467,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8678258311824677,
                  "rejected_mean_error": 1.8752758090753057,
                  "gap_rejected_minus_accepted": 1.007449977892838
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4897903680801385,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4680441996786329,
                  "rejected_mean_error": 2.9808249855041504,
                  "gap_rejected_minus_accepted": 1.5127807858255176
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0858721137046814,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.300031374163806,
                  "rejected_mean_error": 2.567058771375626,
                  "gap_rejected_minus_accepted": 1.2670273972118198
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5824583172798157,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1069674344062805,
                  "rejected_mean_error": 2.131677122116089,
                  "gap_rejected_minus_accepted": 1.0247096877098085
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2375845313072205,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8498167509124392,
                  "rejected_mean_error": 1.878567455924131,
                  "gap_rejected_minus_accepted": 1.0287507050116917
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
        "best_epoch": 56,
        "best_calib_loss": 0.018838517367839813,
        "train_time_sec": 41.96311569213867,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9987982733384674,
              "spearman": 0.9978791283839333,
              "auroc_top30_bad": 0.9990792857142857,
              "mae": 0.03584871788737364,
              "mse": 0.0021370154951942935,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.987,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7032168292056392,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10496540392143652
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24021388143580408
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5462324385954999
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8773294713705158
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2563167701877187
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9990255781541576,
              "spearman": 0.998126347885009,
              "auroc_top30_worst": 0.9988474285714285,
              "pairwise_seed_ranking": 0.9545,
              "predicted_best_mean_error": 1.5155160654485225,
              "seed0_mean_error": 1.5949208683073521,
              "random_seed_mean_error": 1.5911614976227284,
              "oracle_best_mean_error": 1.5142234272062778,
              "improvement_over_seed0": 0.07940480285882967,
              "gap_to_oracle": 0.0012926382422446814,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6585831074714661
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7924127643108367
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9863475038528442
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.215851349290212
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5904509642362594
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.796471309661866,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3831529489358265,
                  "rejected_mean_error": 3.456133101940155,
                  "gap_rejected_minus_accepted": 2.0729801530043286
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9888803958892822,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.215851349290212,
                  "rejected_mean_error": 2.714249809074402,
                  "gap_rejected_minus_accepted": 1.4983984597841897
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3887807130813599,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9863475038528442,
                  "rejected_mean_error": 2.1945544246196746,
                  "gap_rejected_minus_accepted": 1.2082069207668305
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0069662630558014,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7924127643108367,
                  "rejected_mean_error": 1.8564636975447337,
                  "gap_rejected_minus_accepted": 1.064050933233897
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.83553159236908,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3876471648282476,
                  "rejected_mean_error": 3.460384199619293,
                  "gap_rejected_minus_accepted": 2.0727370347910457
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0051507353782654,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.216489849448204,
                  "rejected_mean_error": 2.7302139248847963,
                  "gap_rejected_minus_accepted": 1.5137240754365924
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.394832193851471,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.977654694378376,
                  "rejected_mean_error": 2.2121870422363283,
                  "gap_rejected_minus_accepted": 1.2345323478579524
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0037184059619904,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7844281982183456,
                  "rejected_mean_error": 1.8650850916703543,
                  "gap_rejected_minus_accepted": 1.0806568934520087
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9569260039105684,
              "spearman": 0.9502639022545819,
              "auroc_top30_bad": 0.9570460952380951,
              "mae": 0.15167264443859457,
              "mse": 0.05329534288812936,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6387808099272625,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07625435358285904
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24790314176082612
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.699743424642086
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0462207149108251
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.971472557188842,
              "spearman": 0.9743611576071409,
              "auroc_top30_worst": 0.9842102857142857,
              "pairwise_seed_ranking": 0.892,
              "predicted_best_mean_error": 1.4662935509681703,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.06250027275085435,
              "gap_to_oracle": 0.003450528860092339,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8732994899749756
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9806798635384976
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1698532411575318
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.361989862883269
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0709838151931765,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4602968677944608,
                  "rejected_mean_error": 2.222311806678772,
                  "gap_rejected_minus_accepted": 0.7620149388843114
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8940551280975342,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.361520175236648,
                  "rejected_mean_error": 2.0603148495427335,
                  "gap_rejected_minus_accepted": 0.6987946743060856
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4849680662155151,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1698532411575318,
                  "rejected_mean_error": 1.903143482208252,
                  "gap_rejected_minus_accepted": 0.7332902410507203
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0727802515029907,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9817332676805246,
                  "rejected_mean_error": 1.7218147698181543,
                  "gap_rejected_minus_accepted": 0.7400815021376297
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0769854307174684,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4550551748275757,
                  "rejected_mean_error": 2.1924416637420654,
                  "gap_rejected_minus_accepted": 0.7373864889144897
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8920848369598389,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3546532137508698,
                  "rejected_mean_error": 2.0456873802911666,
                  "gap_rejected_minus_accepted": 0.6910341665402968
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4874988198280334,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1594280920028686,
                  "rejected_mean_error": 1.8981595554351807,
                  "gap_rejected_minus_accepted": 0.7387314634323121
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0738929510116577,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9599203590362791,
                  "rejected_mean_error": 1.7204463813394149,
                  "gap_rejected_minus_accepted": 0.7605260223031357
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9523573685068777,
              "spearman": 0.9469576390517764,
              "auroc_top30_bad": 0.9583481904761905,
              "mae": 0.21960791419148445,
              "mse": 0.10971583751104072,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6618009322308019,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09854056167602539
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22694374270439147
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7284446148753166
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0641149070660274
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9434721471722972,
              "spearman": 0.9563566640362652,
              "auroc_top30_worst": 0.9942247619047619,
              "pairwise_seed_ranking": 0.9052,
              "predicted_best_mean_error": 1.7271068941354752,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08004168725013727,
              "gap_to_oracle": 0.0032200939655304683,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9459154472351075
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1291263367121036
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2922446630477906
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4768286227925753
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1433942794799807,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.649627603530884,
                  "rejected_mean_error": 3.177947443008423,
                  "gap_rejected_minus_accepted": 1.528319839477539
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9384795129299164,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.475456936382306,
                  "rejected_mean_error": 2.7813780669587107,
                  "gap_rejected_minus_accepted": 1.3059211305764047
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5229406356811523,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2922446630477906,
                  "rejected_mean_error": 2.312674511909485,
                  "gap_rejected_minus_accepted": 1.0204298488616943
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2704553306102753,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1303256963388608,
                  "rejected_mean_error": 2.026982434785735,
                  "gap_rejected_minus_accepted": 0.896656738446874
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1507444381713867,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.65045604162746,
                  "rejected_mean_error": 3.2173814392089843,
                  "gap_rejected_minus_accepted": 1.5669253975815243
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9556961953639984,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.477833978473184,
                  "rejected_mean_error": 2.7846379582844083,
                  "gap_rejected_minus_accepted": 1.3068039798112243
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.522634506225586,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2887820117473603,
                  "rejected_mean_error": 2.3255151510238647,
                  "gap_rejected_minus_accepted": 1.0367331392765045
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2845193147659302,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1335355890175653,
                  "rejected_mean_error": 2.034087717851853,
                  "gap_rejected_minus_accepted": 0.9005521288342877
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9850480497616776,
              "spearman": 0.9818528129482472,
              "auroc_top30_bad": 0.9933523809523809,
              "mae": 0.11355207062661647,
              "mse": 0.024451304062520298,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6841083468412336,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09253772521018983
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2143437546014786
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5917683558464051
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9378229612986246
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9911303770019813,
              "spearman": 0.9864208235653272,
              "auroc_top30_worst": 0.9971169523809524,
              "pairwise_seed_ranking": 0.9104,
              "predicted_best_mean_error": 1.5548257049322127,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06449657332897196,
              "gap_to_oracle": 0.0036824446916579046,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5792945556640625
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8677944526649438
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1183788912296295
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3099803215722794
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5405748367309573,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4741341684394413,
                  "rejected_mean_error": 2.962895830154419,
                  "gap_rejected_minus_accepted": 1.4887616617149777
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9520712792873383,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3092881123373323,
                  "rejected_mean_error": 2.5621723865929504,
                  "gap_rejected_minus_accepted": 1.252884274255618
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4627935886383057,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1183788912296295,
                  "rejected_mean_error": 2.1276417779922485,
                  "gap_rejected_minus_accepted": 1.009262886762619
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2133437991142273,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.869438752674828,
                  "rejected_mean_error": 1.8747370209994159,
                  "gap_rejected_minus_accepted": 1.005298268324588
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4962820291519163,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.467422034210629,
                  "rejected_mean_error": 2.9864244747161863,
                  "gap_rejected_minus_accepted": 1.5190024405055573
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9634522199630737,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2986035949406138,
                  "rejected_mean_error": 2.5712967827206565,
                  "gap_rejected_minus_accepted": 1.2726931877800427
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.486323595046997,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1078954157829284,
                  "rejected_mean_error": 2.1307491407394408,
                  "gap_rejected_minus_accepted": 1.0228537249565124
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2042067348957062,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8482517770358494,
                  "rejected_mean_error": 1.8790946931125008,
                  "gap_rejected_minus_accepted": 1.0308429160766512
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
        "best_epoch": 6,
        "best_calib_loss": 0.019247770309448242,
        "train_time_sec": 29.41528081893921,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9963040066886432,
              "spearman": 0.9938622872681196,
              "auroc_top30_bad": 0.9978142380952382,
              "mae": 0.056263752033235505,
              "mse": 0.005793995126570614,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.989,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7088214595553473,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11981709781987593
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24412175191920252
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5473467272534035
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8781799361913776
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2563167701877187
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.997782292729005,
              "spearman": 0.9958192985446715,
              "auroc_top30_worst": 0.9983003809523809,
              "pairwise_seed_ranking": 0.8972,
              "predicted_best_mean_error": 1.5181413426995278,
              "seed0_mean_error": 1.5949208683073521,
              "random_seed_mean_error": 1.5911614976227284,
              "oracle_best_mean_error": 1.5142234272062778,
              "improvement_over_seed0": 0.0767795256078243,
              "gap_to_oracle": 0.003917915493250046,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6629992532730102
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7936573739528656
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9872644308567047
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2155577405611675
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5904509642362594
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8077607393264774,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3832403468290966,
                  "rejected_mean_error": 3.455346520900726,
                  "gap_rejected_minus_accepted": 2.07210617407163
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.976856529712677,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2155577405611675,
                  "rejected_mean_error": 2.7151306352615356,
                  "gap_rejected_minus_accepted": 1.4995728947003681
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.379898488521576,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9872644308567047,
                  "rejected_mean_error": 2.193637497615814,
                  "gap_rejected_minus_accepted": 1.2063730667591095
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0038074254989624,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7936573739528656,
                  "rejected_mean_error": 1.8560488276640574,
                  "gap_rejected_minus_accepted": 1.0623914537111918
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8386113882064823,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3877717586689524,
                  "rejected_mean_error": 3.459262855052948,
                  "gap_rejected_minus_accepted": 2.0714910963839954
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9988528788089752,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2160903760989508,
                  "rejected_mean_error": 2.731412344932556,
                  "gap_rejected_minus_accepted": 1.5153219688336053
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3831390142440796,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9788776307702064,
                  "rejected_mean_error": 2.2109641058444978,
                  "gap_rejected_minus_accepted": 1.2320864750742913
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0015490055084229,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7854207903146744,
                  "rejected_mean_error": 1.8647542276382447,
                  "gap_rejected_minus_accepted": 1.0793334373235703
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9581497645875163,
              "spearman": 0.9455740415243462,
              "auroc_top30_bad": 0.9514544761904763,
              "mae": 0.1566480038627982,
              "mse": 0.052536442131881814,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6523755742515522,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09964396142959595
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2378826319217682
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6990423941016197
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0480244951486588
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9552062420139646,
              "spearman": 0.9598034010901768,
              "auroc_top30_worst": 0.972903619047619,
              "pairwise_seed_ranking": 0.8424,
              "predicted_best_mean_error": 1.4707180633544923,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.058075760364532325,
              "gap_to_oracle": 0.00787504124641436,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8767192044258117
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9851065824429194
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1721728132247924
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3644675736996665
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.031462621688843,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4639889930089314,
                  "rejected_mean_error": 2.189082679748535,
                  "gap_rejected_minus_accepted": 0.7250936867396038
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.864840567111969,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.363809338501449,
                  "rejected_mean_error": 2.0534619869896398,
                  "gap_rejected_minus_accepted": 0.6896526484881909
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4719243049621582,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1721728132247924,
                  "rejected_mean_error": 1.9008239101409912,
                  "gap_rejected_minus_accepted": 0.7286510969161988
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1523597836494446,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9865087114583951,
                  "rejected_mean_error": 1.7202195575423023,
                  "gap_rejected_minus_accepted": 0.7337108460839071
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.046537899971008,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4591403516133625,
                  "rejected_mean_error": 2.155675072669983,
                  "gap_rejected_minus_accepted": 0.6965347210566204
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8731649518013,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.355335054550579,
                  "rejected_mean_error": 2.043663503631713,
                  "gap_rejected_minus_accepted": 0.6883284490811339
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4733433723449707,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1622779483795167,
                  "rejected_mean_error": 1.8953096990585327,
                  "gap_rejected_minus_accepted": 0.733031750679016
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1658940613269806,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9674979675383795,
                  "rejected_mean_error": 1.7178934971916484,
                  "gap_rejected_minus_accepted": 0.750395529653269
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.92865577046836,
              "spearman": 0.9220785377852299,
              "auroc_top30_bad": 0.9407188571428571,
              "mae": 0.26258819330483674,
              "mse": 0.16844517802768058,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6371458656609222,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08590861278772353
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.221010285449028
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.706869029700756
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1324462864478428
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8269148879421769,
              "spearman": 0.8908616742794716,
              "auroc_top30_worst": 0.9162270476190476,
              "pairwise_seed_ranking": 0.8648,
              "predicted_best_mean_error": 1.7294989756345749,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.07764960575103763,
              "gap_to_oracle": 0.005612175464630109,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9509951362609863
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1300260019608033
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2969764669418336
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.579030553160954
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9190288066864014,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.69136335044437,
                  "rejected_mean_error": 2.8023257207870484,
                  "gap_rejected_minus_accepted": 1.1109623703426785
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6816444098949432,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5775047844731056,
                  "rejected_mean_error": 2.4758865856134094,
                  "gap_rejected_minus_accepted": 0.8983818011403037
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.46871817111969,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2969764669418336,
                  "rejected_mean_error": 2.307942708015442,
                  "gap_rejected_minus_accepted": 1.0109662410736084
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.22831392288208,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1309243265432292,
                  "rejected_mean_error": 2.026782465464532,
                  "gap_rejected_minus_accepted": 0.895858138921303
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9352707862854004,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6969891822338103,
                  "rejected_mean_error": 2.798583173751831,
                  "gap_rejected_minus_accepted": 1.1015939915180206
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6905252635478973,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5806991064293499,
                  "rejected_mean_error": 2.4793081340335665,
                  "gap_rejected_minus_accepted": 0.8986090276042167
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4714727997779846,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2906188418865203,
                  "rejected_mean_error": 2.3236783208847047,
                  "gap_rejected_minus_accepted": 1.0330594789981844
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2380770146846771,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.132547947622481,
                  "rejected_mean_error": 2.0344204526534053,
                  "gap_rejected_minus_accepted": 0.9018725050309244
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9792424912680194,
              "spearman": 0.9748345980175844,
              "auroc_top30_bad": 0.9939550476190476,
              "mae": 0.13992926686927676,
              "mse": 0.035185927670046024,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7037521035332275,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13610290044546128
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23847808272838592
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5927634459495544
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9372650844573974
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9863859674631685,
              "spearman": 0.9815809397638015,
              "auroc_top30_worst": 0.9979032380952382,
              "pairwise_seed_ranking": 0.8576,
              "predicted_best_mean_error": 1.5575448378324508,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.0617774404287339,
              "gap_to_oracle": 0.006401577591895968,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6321670579910278
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8772368443508943
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1188426676273346
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3110266525163325
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.569929265975952,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4758405270311568,
                  "rejected_mean_error": 2.9475386028289794,
                  "gap_rejected_minus_accepted": 1.4716980757978226
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0074936151504517,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3103596678474796,
                  "rejected_mean_error": 2.558964567062573,
                  "gap_rejected_minus_accepted": 1.2486048992150933
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4308543801307678,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1188426676273346,
                  "rejected_mean_error": 2.1271780015945434,
                  "gap_rejected_minus_accepted": 1.0083353339672088
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1949375867843628,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8781560260457353,
                  "rejected_mean_error": 1.8718250609512899,
                  "gap_rejected_minus_accepted": 0.9936690349055546
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.570316433906555,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4676686607466805,
                  "rejected_mean_error": 2.9842048358917235,
                  "gap_rejected_minus_accepted": 1.516536175145043
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.021221101284027,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.298140205482748,
                  "rejected_mean_error": 2.572672240317814,
                  "gap_rejected_minus_accepted": 1.274532034835066
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.440732479095459,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1085087933540345,
                  "rejected_mean_error": 2.130135763168335,
                  "gap_rejected_minus_accepted": 1.0216269698143003
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.215829461812973,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8590925506183079,
                  "rejected_mean_error": 1.8754424538841858,
                  "gap_rejected_minus_accepted": 1.016349903265878
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
