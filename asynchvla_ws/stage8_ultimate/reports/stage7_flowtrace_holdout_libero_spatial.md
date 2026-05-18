# Stage 7 Flow-trace Experiments: holdout_libero_spatial

```json
{
  "split": "holdout_libero_spatial",
  "variants": [
    {
      "variant": "context_gated_action_no_flow",
      "feature_mode": "M3_gated_base",
      "with_flow": false,
      "model_kind": "gated",
      "input_dim": 1456,
      "best_epoch": 16,
      "best_calib_loss": 0.04961434751749039,
      "train_time_sec": 18.991951942443848,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9943287082523878,
            "spearman": 0.990727449584402,
            "auroc_top30_bad": 0.9993630476190476,
            "mae": 0.07941678099036217,
            "mse": 0.010351315245246556,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6793801022246387,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08875767815113067
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18753932542800902
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47949755213260653
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.761687117433548
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1361381838202476
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9986678034303618,
            "spearman": 0.9971101800385153,
            "auroc_top30_worst": 0.9986255238095237,
            "pairwise_seed_ranking": 0.8044,
            "predicted_best_mean_error": 1.522658410191536,
            "seed0_mean_error": 1.5792292177677154,
            "random_seed_mean_error": 1.5631394336223603,
            "oracle_best_mean_error": 1.5087051717042923,
            "improvement_over_seed0": 0.056570807576179494,
            "gap_to_oracle": 0.013953238487243613,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6758866465091705
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8447914607822895
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0250988450527192
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2078723107764462
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5653816118955612
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4193498849868775,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3467901230653128,
                "rejected_mean_error": 3.532705011367798,
                "gap_rejected_minus_accepted": 2.1859148883024853
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6962843239307404,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2073152206178155,
                "rejected_mean_error": 2.6372928215672795,
                "gap_rejected_minus_accepted": 1.429977600949464
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3391032218933105,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0250988450527192,
                "rejected_mean_error": 2.1056643787384033,
                "gap_rejected_minus_accepted": 1.080565533685684
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0102349817752838,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8454337709437544,
                "rejected_mean_error": 1.8058764616478724,
                "gap_rejected_minus_accepted": 0.960442690704118
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.394552707672119,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3586884893311395,
                "rejected_mean_error": 3.5640957736968994,
                "gap_rejected_minus_accepted": 2.20540728436576
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.691767156124115,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.217947375009404,
                "rejected_mean_error": 2.651605481193179,
                "gap_rejected_minus_accepted": 1.433658106183775
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.35326087474823,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0318364882469178,
                "rejected_mean_error": 2.126621947288513,
                "gap_rejected_minus_accepted": 1.0947854590415953
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0470505058765411,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.84004512192711,
                "rejected_mean_error": 1.8282591537995772,
                "gap_rejected_minus_accepted": 0.9882140318724671
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8925175407103423,
            "spearman": 0.9354774380863871,
            "auroc_top30_bad": 0.9563541666666666,
            "mae": 0.2949088854435831,
            "mse": 0.18341780762788618,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.925,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7839426666913116,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.14509283117949962
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2181876190006733
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5078882766328752
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9300927750642101
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2914017786365002
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.6675574906286996,
            "spearman": 0.8202113138207113,
            "auroc_top30_worst": 0.860654761904762,
            "pairwise_seed_ranking": 0.8575,
            "predicted_best_mean_error": 1.8539507329463958,
            "seed0_mean_error": 1.9440672114491462,
            "random_seed_mean_error": 1.9121361747384071,
            "oracle_best_mean_error": 1.831606737524271,
            "improvement_over_seed0": 0.0901164785027504,
            "gap_to_oracle": 0.02234399542212473,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8120273739099503
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1887828439474106
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.460747776925564
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6954228566090266
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.908190148025751
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.942289924621583,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.867757951054308,
                "rejected_mean_error": 2.272079920768738,
                "gap_rejected_minus_accepted": 0.4043219697144298
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.310125410556793,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.6954228566090266,
                "rejected_mean_error": 2.546492022275925,
                "gap_rejected_minus_accepted": 0.8510691656668983
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9023870825767517,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.460747776925564,
                "rejected_mean_error": 2.3556325191259386,
                "gap_rejected_minus_accepted": 0.8948847422003747
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6013580560684204,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.1887828439474106,
                "rejected_mean_error": 2.147992582718531,
                "gap_rejected_minus_accepted": 0.9592097387711205
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8830267429351815,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9050757669740253,
                "rejected_mean_error": 2.294990211725235,
                "gap_rejected_minus_accepted": 0.38991444475120973
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3132702112197876,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7241531232992808,
                "rejected_mean_error": 2.6038094758987427,
                "gap_rejected_minus_accepted": 0.8796563525994618
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9093124270439148,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.4834285229444504,
                "rejected_mean_error": 2.404705899953842,
                "gap_rejected_minus_accepted": 0.9212773770093916
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6102409958839417,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.1932851433753968,
                "rejected_mean_error": 2.1943279008070626,
                "gap_rejected_minus_accepted": 1.0010427574316658
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8969408740595568,
            "spearman": 0.8756743724980346,
            "auroc_top30_bad": 0.9044940476190476,
            "mae": 0.25377155570313337,
            "mse": 0.13781073317589482,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6632275233266328,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.13923195898532867
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.268172512575984
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6889389326423406
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.072491534203291
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.33953262437135
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.5955214760011525,
            "spearman": 0.6053004706279413,
            "auroc_top30_worst": 0.7530357142857144,
            "pairwise_seed_ranking": 0.7725,
            "predicted_best_mean_error": 1.9016137808561324,
            "seed0_mean_error": 2.011523014307022,
            "random_seed_mean_error": 1.962140828371048,
            "oracle_best_mean_error": 1.8912434473633766,
            "improvement_over_seed0": 0.10990923345088977,
            "gap_to_oracle": 0.010370333492755845,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.4130148082971572
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.6866588926315307
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.7923962515592575
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8561432711283365
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9625638720393181
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4176852941513074,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9124022295077643,
                "rejected_mean_error": 2.414018654823303,
                "gap_rejected_minus_accepted": 0.5016164253155388
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0525511503219604,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.8561432711283365,
                "rejected_mean_error": 2.2818256747722625,
                "gap_rejected_minus_accepted": 0.42568240364392596
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6904116868972778,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.7923962515592575,
                "rejected_mean_error": 2.1327314925193788,
                "gap_rejected_minus_accepted": 0.34033524096012124
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5320782959461212,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.6866588926315307,
                "rejected_mean_error": 2.0545321985085807,
                "gap_rejected_minus_accepted": 0.36787330587705
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.364283633232118,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9549712306923337,
                "rejected_mean_error": 2.520489066839218,
                "gap_rejected_minus_accepted": 0.5655178361468844
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.052278459072113,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.8996816376845043,
                "rejected_mean_error": 2.3470471441745757,
                "gap_rejected_minus_accepted": 0.44736550649007145
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6975815296173096,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.821595412492752,
                "rejected_mean_error": 2.201450616121292,
                "gap_rejected_minus_accepted": 0.3798552036285401
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5524737238883972,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.7271409034729004,
                "rejected_mean_error": 2.1063170512517293,
                "gap_rejected_minus_accepted": 0.3791761477788289
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9232142772529821,
            "spearman": 0.8928419700265037,
            "auroc_top30_bad": 0.9314769345238095,
            "mae": 0.24399915289133786,
            "mse": 0.09777789671079862,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9875,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6026376400153609,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10611432790756226
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22620044335722922
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7429920557141304
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0633981583515804
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3148418681323528
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.6408439431523385,
            "spearman": 0.6981294883093019,
            "auroc_top30_worst": 0.8680357142857144,
            "pairwise_seed_ranking": 0.6375,
            "predicted_best_mean_error": 1.8670002549886704,
            "seed0_mean_error": 1.8995800495147706,
            "random_seed_mean_error": 1.8808846116065978,
            "oracle_best_mean_error": 1.8494211554527282,
            "improvement_over_seed0": 0.03257979452610016,
            "gap_to_oracle": 0.017579099535942166,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.7460916876792907
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.7251595532894135
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6840734434127809
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7992374837398528
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8811210370063782
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0466907262802123,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8507771535052193,
                "rejected_mean_error": 2.1542159885168077,
                "gap_rejected_minus_accepted": 0.3034388350115884
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.987936019897461,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.7992374837398528,
                "rejected_mean_error": 2.126771696805954,
                "gap_rejected_minus_accepted": 0.3275342130661012
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7570715546607971,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.6840734434127809,
                "rejected_mean_error": 2.0781686305999756,
                "gap_rejected_minus_accepted": 0.3940951871871947
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3000822365283966,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.7251595532894135,
                "rejected_mean_error": 1.9331081982453664,
                "gap_rejected_minus_accepted": 0.2079486449559529
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0466907262802123,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.8690822339720197,
                "rejected_mean_error": 2.1740603893995285,
                "gap_rejected_minus_accepted": 0.30497815542750883
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9737117290496826,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.8220155477523803,
                "rejected_mean_error": 2.132273554801941,
                "gap_rejected_minus_accepted": 0.31025800704956064
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7561261653900146,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.7011164486408235,
                "rejected_mean_error": 2.0980436503887177,
                "gap_rejected_minus_accepted": 0.3969272017478942
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3127825558185577,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.767051112651825,
                "rejected_mean_error": 1.943756361802419,
                "gap_rejected_minus_accepted": 0.17670524915059405
              }
            ]
          }
        }
      }
    },
    {
      "variant": "context_gated_action_plus_flow",
      "feature_mode": "M3_gated_base",
      "with_flow": true,
      "model_kind": "gated",
      "input_dim": 1468,
      "best_epoch": 9,
      "best_calib_loss": 0.049271050840616226,
      "train_time_sec": 17.596648693084717,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9654534639247003,
            "spearman": 0.9244780012372215,
            "auroc_top30_bad": 0.9972213333333333,
            "mae": 0.16668353719711304,
            "mse": 0.05161554905375647,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.796,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6409877313996178,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3292598038315773
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.36198208627700806
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4867443300485611
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7630634582360586
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1361381838202476
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9931862599265076,
            "spearman": 0.980619685772599,
            "auroc_top30_worst": 0.9933744761904763,
            "pairwise_seed_ranking": 0.6888,
            "predicted_best_mean_error": 1.5319635331630708,
            "seed0_mean_error": 1.5792292177677154,
            "random_seed_mean_error": 1.5631394336223603,
            "oracle_best_mean_error": 1.5087051717042923,
            "improvement_over_seed0": 0.04726568460464464,
            "gap_to_oracle": 0.023258361458778465,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6933075530529023
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8574664251735578
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0333114102840424
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2106330811278398
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5653816118955612
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.405393505096436,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.346898968882031,
                "rejected_mean_error": 3.531725399017334,
                "gap_rejected_minus_accepted": 2.184826430135303
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6717073321342468,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2099444297169164,
                "rejected_mean_error": 2.629421994328118,
                "gap_rejected_minus_accepted": 1.4194775646112014
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3101617097854614,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0333114102840424,
                "rejected_mean_error": 2.09745181350708,
                "gap_rejected_minus_accepted": 1.0641404032230375
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0400772988796234,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8584224776909374,
                "rejected_mean_error": 1.8015376513897419,
                "gap_rejected_minus_accepted": 0.9431151736988045
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.398741936683655,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.35887250079049,
                "rejected_mean_error": 3.5624396705627444,
                "gap_rejected_minus_accepted": 2.2035671697722545
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6690158545970917,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2201938747084715,
                "rejected_mean_error": 2.6449372995467413,
                "gap_rejected_minus_accepted": 1.4247434248382698
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.312065064907074,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0399748435020446,
                "rejected_mean_error": 2.118483592033386,
                "gap_rejected_minus_accepted": 1.0785087485313416
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0333970785140991,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8512521509140257,
                "rejected_mean_error": 1.824483523713076,
                "gap_rejected_minus_accepted": 0.9732313727990504
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8958076190963159,
            "spearman": 0.9158368747971906,
            "auroc_top30_bad": 0.9691145833333332,
            "mae": 0.2889645140338689,
            "mse": 0.1690036630131045,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.7875,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7430684277538571,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.28588669700548053
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3051418947055936
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5021937120519578
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9219837280487021
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2914017786365002
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.7002709754049127,
            "spearman": 0.8721392008700053,
            "auroc_top30_worst": 0.8927678571428572,
            "pairwise_seed_ranking": 0.6925,
            "predicted_best_mean_error": 1.8915637724101544,
            "seed0_mean_error": 1.9440672114491462,
            "random_seed_mean_error": 1.9121361747384071,
            "oracle_best_mean_error": 1.831606737524271,
            "improvement_over_seed0": 0.052503439038991795,
            "gap_to_oracle": 0.05995703488588333,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7968405470252037
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1343780666589738
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.423221516907215
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.698039533495903
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.908190148025751
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6206850767135625,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8674875227941408,
                "rejected_mean_error": 2.2745137751102447,
                "gap_rejected_minus_accepted": 0.4070262523161039
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.129464030265808,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.698039533495903,
                "rejected_mean_error": 2.5386419916152954,
                "gap_rejected_minus_accepted": 0.8406024581193923
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.770201861858368,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.423221516907215,
                "rejected_mean_error": 2.393158779144287,
                "gap_rejected_minus_accepted": 0.9699372622370719
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5159968435764313,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.1343780666589738,
                "rejected_mean_error": 2.1661275084813436,
                "gap_rejected_minus_accepted": 1.0317494418223698
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.578847002983094,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9050757669740253,
                "rejected_mean_error": 2.294990211725235,
                "gap_rejected_minus_accepted": 0.38991444475120973
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1166566014289856,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7241531232992808,
                "rejected_mean_error": 2.6038094758987427,
                "gap_rejected_minus_accepted": 0.8796563525994618
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7604575157165527,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.4487192541360856,
                "rejected_mean_error": 2.439415168762207,
                "gap_rejected_minus_accepted": 0.9906959146261216
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.515310525894165,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.1483155548572541,
                "rejected_mean_error": 2.209317763646444,
                "gap_rejected_minus_accepted": 1.0610022087891897
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9062372680016109,
            "spearman": 0.8316227630449814,
            "auroc_top30_bad": 0.8829910714285715,
            "mae": 0.28406171668320895,
            "mse": 0.13951732395023791,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.7,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6827531924215242,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3614625284448266
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.39843385756015776
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6365021056681871
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.097797510276238
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.33953262437135
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.5126897575673457,
            "spearman": 0.553175332345827,
            "auroc_top30_worst": 0.7035416666666667,
            "pairwise_seed_ranking": 0.56125,
            "predicted_best_mean_error": 1.9559346228837966,
            "seed0_mean_error": 2.011523014307022,
            "random_seed_mean_error": 1.962140828371048,
            "oracle_best_mean_error": 1.8912434473633766,
            "improvement_over_seed0": 0.05558839142322558,
            "gap_to_oracle": 0.06469117552042003,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3241494834423064
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.587498426437378
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.8116254770755769
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.901543081998825
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9625638720393181
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1641214370727537,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9275892251067692,
                "rejected_mean_error": 2.2773356944322587,
                "gap_rejected_minus_accepted": 0.3497464693254895
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9014559388160706,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.901543081998825,
                "rejected_mean_error": 2.1456262421607972,
                "gap_rejected_minus_accepted": 0.24408316016197218
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.673347532749176,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.8116254770755769,
                "rejected_mean_error": 2.113502267003059,
                "gap_rejected_minus_accepted": 0.30187678992748235
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5168123841285706,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.587498426437378,
                "rejected_mean_error": 2.0875856872399647,
                "gap_rejected_minus_accepted": 0.5000872608025868
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.136220908164978,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.964368806944953,
                "rejected_mean_error": 2.4359108805656433,
                "gap_rejected_minus_accepted": 0.47154207362069034
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8819531202316284,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.9488665759563446,
                "rejected_mean_error": 2.1994923293590545,
                "gap_rejected_minus_accepted": 0.25062575340270987
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.662112534046173,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.8524361371994018,
                "rejected_mean_error": 2.1706098914146423,
                "gap_rejected_minus_accepted": 0.3181737542152405
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.510561764240265,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.6055828034877777,
                "rejected_mean_error": 2.1468364179134367,
                "gap_rejected_minus_accepted": 0.541253614425659
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9224456063680397,
            "spearman": 0.9068389119046898,
            "auroc_top30_bad": 0.9580505952380953,
            "mae": 0.24532353766262532,
            "mse": 0.10153882243400483,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.8125,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6692253624762025,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3028297802433372
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.37223068870604037
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6679790118336677
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0626770037412643
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3148418681323528
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8383189498583579,
            "spearman": 0.8740999006243788,
            "auroc_top30_worst": 0.9409821428571429,
            "pairwise_seed_ranking": 0.5225,
            "predicted_best_mean_error": 1.8717322781682015,
            "seed0_mean_error": 1.8995800495147706,
            "random_seed_mean_error": 1.8808846116065978,
            "oracle_best_mean_error": 1.8494211554527282,
            "improvement_over_seed0": 0.027847771346569017,
            "gap_to_oracle": 0.02231112271547331,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3578439354896545
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.5403614687919616
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6720045328140258
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.780223780075709
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8811210370063782
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1807462692260744,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8415977325704362,
                "rejected_mean_error": 2.2368307769298554,
                "gap_rejected_minus_accepted": 0.3952330443594192
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.013657808303833,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.780223780075709,
                "rejected_mean_error": 2.1838128077983856,
                "gap_rejected_minus_accepted": 0.4035890277226766
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6791804432868958,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.6720045328140258,
                "rejected_mean_error": 2.0902375411987304,
                "gap_rejected_minus_accepted": 0.41823300838470456
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3788692951202393,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.5403614687919616,
                "rejected_mean_error": 1.994707559744517,
                "gap_rejected_minus_accepted": 0.4543460909525554
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1866174221038817,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.8608017497592502,
                "rejected_mean_error": 2.248584747314453,
                "gap_rejected_minus_accepted": 0.38778299755520296
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0030961632728577,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7995789110660554,
                "rejected_mean_error": 2.199583464860916,
                "gap_rejected_minus_accepted": 0.40000455379486066
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6860337257385254,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.6998150646686554,
                "rejected_mean_error": 2.0993450343608857,
                "gap_rejected_minus_accepted": 0.3995299696922303
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3806856572628021,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.5684256732463837,
                "rejected_mean_error": 2.0099648416042326,
                "gap_rejected_minus_accepted": 0.4415391683578489
              }
            ]
          }
        }
      }
    },
    {
      "variant": "action_only_plus_flow",
      "feature_mode": "A0_action_flat",
      "with_flow": true,
      "model_kind": "mlp",
      "input_dim": 82,
      "best_epoch": 93,
      "best_calib_loss": 0.060627032071352005,
      "train_time_sec": 4.768564224243164,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.973974327273947,
            "spearman": 0.9443243371408332,
            "auroc_top30_bad": 0.9996137142857143,
            "mae": 0.10445574271678924,
            "mse": 0.03917257928130318,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.6964139369210345,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.2917317192554474
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3179417454004288
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.48251886603832245
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7614226668516795
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1361381838202476
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9991394514068702,
            "spearman": 0.998005220099341,
            "auroc_top30_worst": 0.9994666666666667,
            "pairwise_seed_ranking": 0.9028,
            "predicted_best_mean_error": 1.5131267499923706,
            "seed0_mean_error": 1.5792292177677154,
            "random_seed_mean_error": 1.5631394336223603,
            "oracle_best_mean_error": 1.5087051717042923,
            "improvement_over_seed0": 0.06610246777534479,
            "gap_to_oracle": 0.0044215782880783205,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6748508956432343
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8435359317331742
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0248456807613373
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2076187972257386
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5653816118955612
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4311743974685673,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3465927023092905,
                "rejected_mean_error": 3.534481798171997,
                "gap_rejected_minus_accepted": 2.1878890958627064
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7717430293560028,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2070813542559917,
                "rejected_mean_error": 2.6379929262990007,
                "gap_rejected_minus_accepted": 1.430911572043009
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3885796666145325,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0248456807613373,
                "rejected_mean_error": 2.105917543029785,
                "gap_rejected_minus_accepted": 1.0810718622684476
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.062845766544342,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.844215799730045,
                "rejected_mean_error": 1.8062833186274787,
                "gap_rejected_minus_accepted": 0.9620675188974337
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4354010105133055,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.358797888490889,
                "rejected_mean_error": 3.5631111812591554,
                "gap_rejected_minus_accepted": 2.2043132927682665
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7858200669288635,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2182200340663685,
                "rejected_mean_error": 2.650796159865364,
                "gap_rejected_minus_accepted": 1.4325761257989957
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.399701714515686,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.031184925556183,
                "rejected_mean_error": 2.127273509979248,
                "gap_rejected_minus_accepted": 1.096088584423065
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0686122477054596,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8382170266575284,
                "rejected_mean_error": 1.828875036163126,
                "gap_rejected_minus_accepted": 0.9906580095055977
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8597976689864422,
            "spearman": 0.8971399227806174,
            "auroc_top30_bad": 0.9656175595238096,
            "mae": 0.33033356747590004,
            "mse": 0.2402308466944569,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.475,
            "expert_lt_simvla_seed0": 0.975,
            "same_context_pred_std": 0.8041981535148445,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.294025644287467
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3493768560141325
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5079190075956285
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9191826190923651
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2914017786365002
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.6008391660483792,
            "spearman": 0.7933982712391952,
            "auroc_top30_worst": 0.8606845238095238,
            "pairwise_seed_ranking": 0.81375,
            "predicted_best_mean_error": 1.836196529120207,
            "seed0_mean_error": 1.9440672114491462,
            "random_seed_mean_error": 1.9121361747384071,
            "oracle_best_mean_error": 1.831606737524271,
            "improvement_over_seed0": 0.10787068232893926,
            "gap_to_oracle": 0.004589791595935866,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8256762564182282
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1876819044351579
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.453513195812702
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7417949746052424
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.908190148025751
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2210126876831056,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8682282608416345,
                "rejected_mean_error": 2.2678471326828005,
                "gap_rejected_minus_accepted": 0.39961887184116596
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.185460388660431,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.7417949746052424,
                "rejected_mean_error": 2.407375668287277,
                "gap_rejected_minus_accepted": 0.6655806936820348
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6973944902420044,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.453513195812702,
                "rejected_mean_error": 2.3628671002388,
                "gap_rejected_minus_accepted": 0.9093539044260979
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5058578252792358,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.1876819044351579,
                "rejected_mean_error": 2.148359562555949,
                "gap_rejected_minus_accepted": 0.9606776581207912
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.29862768650055,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9050757669740253,
                "rejected_mean_error": 2.294990211725235,
                "gap_rejected_minus_accepted": 0.38991444475120973
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2060646414756775,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7952390968799592,
                "rejected_mean_error": 2.3905515551567076,
                "gap_rejected_minus_accepted": 0.5953124582767484
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.727595567703247,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.4664057433605193,
                "rejected_mean_error": 2.421728679537773,
                "gap_rejected_minus_accepted": 0.9553229361772537
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5586944222450256,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.20817528963089,
                "rejected_mean_error": 2.189364518721898,
                "gap_rejected_minus_accepted": 0.9811892290910083
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9129925228140642,
            "spearman": 0.863758662384551,
            "auroc_top30_bad": 0.9154166666666667,
            "mae": 0.27873807985335586,
            "mse": 0.13171529086670028,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.475,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7165884812819128,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3887859402224422
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.36440452247858046
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6344395489245653
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0661853709320228
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.33953262437135
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.5921003537297032,
            "spearman": 0.669657247857799,
            "auroc_top30_worst": 0.8513988095238095,
            "pairwise_seed_ranking": 0.83,
            "predicted_best_mean_error": 1.8978563621640205,
            "seed0_mean_error": 2.011523014307022,
            "random_seed_mean_error": 1.962140828371048,
            "oracle_best_mean_error": 1.8912434473633766,
            "improvement_over_seed0": 0.11366665214300165,
            "gap_to_oracle": 0.006612914800643965,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.338217556476593
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.5706862223148346
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.737043679356575
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8733076337973278
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9625638720393181
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2839441299438477,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9269175628821056,
                "rejected_mean_error": 2.2833806544542314,
                "gap_rejected_minus_accepted": 0.35646309157212586
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8725268244743347,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.8733076337973278,
                "rejected_mean_error": 2.2303325867652894,
                "gap_rejected_minus_accepted": 0.35702495296796166
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6889778971672058,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.737043679356575,
                "rejected_mean_error": 2.188084064722061,
                "gap_rejected_minus_accepted": 0.45104038536548585
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5529386103153229,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.5706862223148346,
                "rejected_mean_error": 2.0931897552808127,
                "gap_rejected_minus_accepted": 0.5225035329659782
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.352378034591675,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9759836710161633,
                "rejected_mean_error": 2.3313771039247513,
                "gap_rejected_minus_accepted": 0.35539343290858794
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.888412743806839,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.913190386692683,
                "rejected_mean_error": 2.3065208971500395,
                "gap_rejected_minus_accepted": 0.39333051045735656
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7460998892784119,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.7678732752799988,
                "rejected_mean_error": 2.2551727533340453,
                "gap_rejected_minus_accepted": 0.4872994780540465
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.57692551612854,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.569658350944519,
                "rejected_mean_error": 2.1588112354278564,
                "gap_rejected_minus_accepted": 0.5891528844833374
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9133886494443558,
            "spearman": 0.8827316332807592,
            "auroc_top30_bad": 0.9347247023809524,
            "mae": 0.31318844359368087,
            "mse": 0.1511655308581902,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5125,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6318614941635916,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.45676944926381113
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.42568257078528404
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6856422904133797
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.05027392466863
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3148418681323528
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.7774048983259455,
            "spearman": 0.7971341757042635,
            "auroc_top30_worst": 0.9538839285714286,
            "pairwise_seed_ranking": 0.64625,
            "predicted_best_mean_error": 1.8608329430222512,
            "seed0_mean_error": 1.8995800495147706,
            "random_seed_mean_error": 1.8808846116065978,
            "oracle_best_mean_error": 1.8494211554527282,
            "improvement_over_seed0": 0.038747106492519334,
            "gap_to_oracle": 0.011411787569522991,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.6040014386177064
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.6236628913879394
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.661742268204689
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7772290734450022
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8811210370063782
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8490483403205873,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8359455506006876,
                "rejected_mean_error": 2.2877004146575928,
                "gap_rejected_minus_accepted": 0.4517548640569051
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.807633489370346,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.7772290734450022,
                "rejected_mean_error": 2.192796927690506,
                "gap_rejected_minus_accepted": 0.4155678542455039
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5801894664764404,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.661742268204689,
                "rejected_mean_error": 2.1004998058080675,
                "gap_rejected_minus_accepted": 0.43875753760337854
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2460663616657257,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.6236628913879394,
                "rejected_mean_error": 1.966940418879191,
                "gap_rejected_minus_accepted": 0.3432775274912516
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8476675152778625,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.8554285963376362,
                "rejected_mean_error": 2.2969431281089783,
                "gap_rejected_minus_accepted": 0.44151453177134203
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8038255274295807,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7980404873689015,
                "rejected_mean_error": 2.204198735952377,
                "gap_rejected_minus_accepted": 0.4061582485834756
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5360721349716187,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.6903088867664338,
                "rejected_mean_error": 2.108851212263107,
                "gap_rejected_minus_accepted": 0.41854232549667336
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2491586208343506,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.641556864976883,
                "rejected_mean_error": 1.9855877776940665,
                "gap_rejected_minus_accepted": 0.34403091271718345
              }
            ]
          }
        }
      }
    },
    {
      "variant": "seed_relative_plus_flow",
      "feature_mode": "M4_seed_relative",
      "with_flow": true,
      "model_kind": "mlp_big",
      "input_dim": 1538,
      "best_epoch": 69,
      "best_calib_loss": 0.042038775980472565,
      "train_time_sec": 21.294074773788452,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9987369971847736,
            "spearman": 0.9974298391322785,
            "auroc_top30_bad": 0.9998430476190476,
            "mae": 0.03310057551917853,
            "mse": 0.0021828745485942135,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.689434133040996,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.009161103904247283
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18191032495498657
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4776795532941818
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7613117447376251
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1361381838202476
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9995291851269451,
            "spearman": 0.9988609938310362,
            "auroc_top30_worst": 0.9997653333333333,
            "pairwise_seed_ranking": 0.9196,
            "predicted_best_mean_error": 1.5114941232204437,
            "seed0_mean_error": 1.5792292177677154,
            "random_seed_mean_error": 1.5631394336223603,
            "oracle_best_mean_error": 1.5087051717042923,
            "improvement_over_seed0": 0.06773509454727167,
            "gap_to_oracle": 0.002788951516151439,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.674448746919632
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8436576119409158
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0244240872859955
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2075735805576036
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5653816118955612
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4395680427551287,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3464904851648543,
                "rejected_mean_error": 3.5354017524719237,
                "gap_rejected_minus_accepted": 2.1889112673070694
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7382489442825317,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2070258275358248,
                "rejected_mean_error": 2.638159151656178,
                "gap_rejected_minus_accepted": 1.4311333241203534
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3704738020896912,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0244240872859955,
                "rejected_mean_error": 2.106339136505127,
                "gap_rejected_minus_accepted": 1.0819150492191314
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0382782518863678,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8443035446226407,
                "rejected_mean_error": 1.806254007900283,
                "gap_rejected_minus_accepted": 0.9619504632776422
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.428794598579407,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3586089295811123,
                "rejected_mean_error": 3.5648118114471434,
                "gap_rejected_minus_accepted": 2.206202881866031
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7551591396331787,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.217947375009404,
                "rejected_mean_error": 2.651605481193179,
                "gap_rejected_minus_accepted": 1.433658106183775
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4026484489440918,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0312952895164489,
                "rejected_mean_error": 2.127163146018982,
                "gap_rejected_minus_accepted": 1.0958678565025333
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0402758717536926,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8382170266575284,
                "rejected_mean_error": 1.828875036163126,
                "gap_rejected_minus_accepted": 0.9906580095055977
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9328190564879761,
            "spearman": 0.961501359727813,
            "auroc_top30_bad": 0.9866592261904761,
            "mae": 0.2615481710043605,
            "mse": 0.14132174634807848,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9375,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6030301200728516,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12499006753787398
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21777141693979502
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4979765439592302
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9054765483116111
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2914017786365002
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8312131812734997,
            "spearman": 0.9203684398027487,
            "auroc_top30_worst": 0.9354166666666667,
            "pairwise_seed_ranking": 0.915,
            "predicted_best_mean_error": 1.8387847363948822,
            "seed0_mean_error": 1.9440672114491462,
            "random_seed_mean_error": 1.9121361747384071,
            "oracle_best_mean_error": 1.831606737524271,
            "improvement_over_seed0": 0.10528247505426402,
            "gap_to_oracle": 0.007177998870611102,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7920277401804924
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.12973271548748
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3975093421339988
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6697854183117549
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.908190148025751
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.261066246032715,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8576117954320377,
                "rejected_mean_error": 2.363395321369171,
                "gap_rejected_minus_accepted": 0.5057835259371333
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0704025626182556,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.6697854183117549,
                "rejected_mean_error": 2.62340433716774,
                "gap_rejected_minus_accepted": 0.9536189188559849
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.677196741104126,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.3975093421339988,
                "rejected_mean_error": 2.4188709539175033,
                "gap_rejected_minus_accepted": 1.0213616117835045
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3828840553760529,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.12973271548748,
                "rejected_mean_error": 2.1676759588718415,
                "gap_rejected_minus_accepted": 1.0379432433843614
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.26715407371521,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.888887854086028,
                "rejected_mean_error": 2.440681427717209,
                "gap_rejected_minus_accepted": 0.5517935736311808
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.085896611213684,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.700576764345169,
                "rejected_mean_error": 2.674538552761078,
                "gap_rejected_minus_accepted": 0.9739617884159089
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6913554072380066,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.4101046830415727,
                "rejected_mean_error": 2.47802973985672,
                "gap_rejected_minus_accepted": 1.0679250568151475
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3934157192707062,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.1515438556671143,
                "rejected_mean_error": 2.2082416633764903,
                "gap_rejected_minus_accepted": 1.056697807709376
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8358120197164044,
            "spearman": 0.8054510641486303,
            "auroc_top30_bad": 0.8468824404761905,
            "mae": 0.34910152622440366,
            "mse": 0.23215190172900094,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.5275271616364104,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1377237517386675
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.26793348014354706
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.759756690338254
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.099793981363376
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.33953262437135
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.3407684883511811,
            "spearman": 0.33017493859336616,
            "auroc_top30_worst": 0.5719940476190476,
            "pairwise_seed_ranking": 0.7975,
            "predicted_best_mean_error": 1.9084831207990647,
            "seed0_mean_error": 2.011523014307022,
            "random_seed_mean_error": 1.962140828371048,
            "oracle_best_mean_error": 1.8912434473633766,
            "improvement_over_seed0": 0.1030398935079575,
            "gap_to_oracle": 0.017239673435688108,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 2.156855347752571
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.9461389064788819
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.862967353463173
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8742498008410136
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9625638720393181
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9636554241180422,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.907104265358713,
                "rejected_mean_error": 2.4617003321647646,
                "gap_rejected_minus_accepted": 0.5545960668060517
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7157820165157318,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.8742498008410136,
                "rejected_mean_error": 2.2275060856342317,
                "gap_rejected_minus_accepted": 0.35325628479321813
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5463338494300842,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.862967353463173,
                "rejected_mean_error": 2.062160390615463,
                "gap_rejected_minus_accepted": 0.1991930371522901
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.368661105632782,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.9461389064788819,
                "rejected_mean_error": 1.9680388605594634,
                "gap_rejected_minus_accepted": 0.02189995408058154
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9955477833747866,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9494092298878565,
                "rejected_mean_error": 2.5705470740795135,
                "gap_rejected_minus_accepted": 0.6211378441916571
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7449188232421875,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.9132497290770212,
                "rejected_mean_error": 2.3063428699970245,
                "gap_rejected_minus_accepted": 0.39309314092000336
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5628840327262878,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.9094029486179351,
                "rejected_mean_error": 2.113643079996109,
                "gap_rejected_minus_accepted": 0.20424013137817387
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3980167210102081,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.9561004519462586,
                "rejected_mean_error": 2.02999720176061,
                "gap_rejected_minus_accepted": 0.07389674981435124
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9049027356536006,
            "spearman": 0.8925432094607604,
            "auroc_top30_bad": 0.9170907738095239,
            "mae": 0.3117806713558204,
            "mse": 0.14494723940636656,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.4754964572669286,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12307733800262213
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2570939939469099
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6840540996193886
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0727914049228033
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3148418681323528
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8557245713382411,
            "spearman": 0.8328188926180788,
            "auroc_top30_worst": 0.9016071428571429,
            "pairwise_seed_ranking": 0.70125,
            "predicted_best_mean_error": 1.8651224434375764,
            "seed0_mean_error": 1.8995800495147706,
            "random_seed_mean_error": 1.8808846116065978,
            "oracle_best_mean_error": 1.8494211554527282,
            "improvement_over_seed0": 0.03445760607719417,
            "gap_to_oracle": 0.015701287984848156,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.281993216276169
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.5266942131519317
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6850041764974595
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7758764958381652
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8811210370063782
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8958741188049317,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8386890841854944,
                "rejected_mean_error": 2.2630086123943327,
                "gap_rejected_minus_accepted": 0.42431952820883834
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.737261325120926,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.7758764958381652,
                "rejected_mean_error": 2.1968546605110166,
                "gap_rejected_minus_accepted": 0.42097816467285143
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5991254448890686,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.6850041764974595,
                "rejected_mean_error": 2.077237897515297,
                "gap_rejected_minus_accepted": 0.3922337210178375
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4523784220218658,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.5266942131519317,
                "rejected_mean_error": 1.999263311624527,
                "gap_rejected_minus_accepted": 0.47256909847259543
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9092869877815246,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.8597175776958466,
                "rejected_mean_error": 2.258342295885086,
                "gap_rejected_minus_accepted": 0.3986247181892395
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7504369616508484,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7886704881985982,
                "rejected_mean_error": 2.232308733463287,
                "gap_rejected_minus_accepted": 0.443638245264689
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5983522534370422,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.7067000657320022,
                "rejected_mean_error": 2.092460033297539,
                "gap_rejected_minus_accepted": 0.38575996756553677
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4495793282985687,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.5857098579406739,
                "rejected_mean_error": 2.004203446706136,
                "gap_rejected_minus_accepted": 0.41849358876546217
              }
            ]
          }
        }
      }
    },
    {
      "variant": "flow_only",
      "feature_mode": "flow_only",
      "with_flow": true,
      "model_kind": "mlp",
      "input_dim": 12,
      "best_epoch": 51,
      "best_calib_loss": 0.059178080409765244,
      "train_time_sec": 6.9266746044158936,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8182478333519305,
            "spearman": 0.6762141757446313,
            "auroc_top30_bad": 0.7660358095238095,
            "mae": 0.305840984249115,
            "mse": 0.2742534574279765,
            "expert_lt_perturb_large": 0.498,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.984,
            "same_context_pred_std": 0.5342229687717379,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6703474785089493
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7099680498123169
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7042226428747177
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8133518642902374
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1361381838202476
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9944502485186145,
            "spearman": 0.9884569157484262,
            "auroc_top30_worst": 0.9972754285714286,
            "pairwise_seed_ranking": 0.8096,
            "predicted_best_mean_error": 1.5225004305839538,
            "seed0_mean_error": 1.5792292177677154,
            "random_seed_mean_error": 1.5631394336223603,
            "oracle_best_mean_error": 1.5087051717042923,
            "improvement_over_seed0": 0.05672878718376162,
            "gap_to_oracle": 0.013795258879661487,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6801707255840301
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8571346760369264
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0262660813808442
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.20838744207613
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5653816118955612
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.301388311386111,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.346928239689933,
                "rejected_mean_error": 3.5314619617462157,
                "gap_rejected_minus_accepted": 2.184533722056283
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7182699143886566,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.207794177589447,
                "rejected_mean_error": 2.6358590110803184,
                "gap_rejected_minus_accepted": 1.4280648334908714
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3546788692474365,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0262660813808442,
                "rejected_mean_error": 2.1044971424102785,
                "gap_rejected_minus_accepted": 1.0782310610294343
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9999592453241348,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8575626243227206,
                "rejected_mean_error": 1.8018248809567128,
                "gap_rejected_minus_accepted": 0.9442622566339922
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2447566032409667,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3592285476790533,
                "rejected_mean_error": 3.559235248565674,
                "gap_rejected_minus_accepted": 2.200006700886621
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7162750959396362,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.218254674245967,
                "rejected_mean_error": 2.6506933390148104,
                "gap_rejected_minus_accepted": 1.4324386647688434
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3862460851669312,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0313593974113464,
                "rejected_mean_error": 2.1270990381240846,
                "gap_rejected_minus_accepted": 1.0957396407127382
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0412567555904388,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8463082266232324,
                "rejected_mean_error": 1.826149123875215,
                "gap_rejected_minus_accepted": 0.9798408972519826
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8408838748294657,
            "spearman": 0.7630787992966951,
            "auroc_top30_bad": 0.8213616071428571,
            "mae": 0.3274217453692108,
            "mse": 0.282235955550473,
            "expert_lt_perturb_large": 0.50625,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6928088254123391,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.651835334673524
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6664039821922779
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6746102226339281
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9274745126937827
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2914017786365002
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9662108068462731,
            "spearman": 0.9256524103275645,
            "auroc_top30_worst": 0.9685416666666666,
            "pairwise_seed_ranking": 0.7825,
            "predicted_best_mean_error": 1.8503244616091252,
            "seed0_mean_error": 1.9440672114491462,
            "random_seed_mean_error": 1.9121361747384071,
            "oracle_best_mean_error": 1.831606737524271,
            "improvement_over_seed0": 0.09374274984002096,
            "gap_to_oracle": 0.01871772408485417,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.790771035850048
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1410704559087754
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4331967195868491
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5955264693498612
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.908190148025751
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1305426120758058,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.7597766295075417,
                "rejected_mean_error": 3.2439118146896364,
                "gap_rejected_minus_accepted": 1.4841351851820948
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9552605152130127,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5955264693498612,
                "rejected_mean_error": 2.846181184053421,
                "gap_rejected_minus_accepted": 1.2506547147035598
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6732208132743835,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.4331967195868491,
                "rejected_mean_error": 2.383183576464653,
                "gap_rejected_minus_accepted": 0.949986856877804
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4938485324382782,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.1410704559087754,
                "rejected_mean_error": 2.163896712064743,
                "gap_rejected_minus_accepted": 1.0228262561559676
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.168454360961915,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.7891194605165057,
                "rejected_mean_error": 3.3385969698429108,
                "gap_rejected_minus_accepted": 1.549477509326405
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8881584405899048,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6158298790454864,
                "rejected_mean_error": 2.9287792086601256,
                "gap_rejected_minus_accepted": 1.3129493296146393
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6422460675239563,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.4545945525169373,
                "rejected_mean_error": 2.433539870381355,
                "gap_rejected_minus_accepted": 0.9789453178644179
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5157183706760406,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.1752903580665588,
                "rejected_mean_error": 2.2003261625766752,
                "gap_rejected_minus_accepted": 1.0250358045101164
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8039700355220158,
            "spearman": 0.7894660342820954,
            "auroc_top30_bad": 0.8670238095238094,
            "mae": 0.37299858797341584,
            "mse": 0.3016912133099446,
            "expert_lt_perturb_large": 0.50625,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6711658973083605,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6497093854472041
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7098341923207044
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7165013767033815
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0391727396349113
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.33953262437135
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8975163589008853,
            "spearman": 0.8662616016350102,
            "auroc_top30_worst": 0.906875,
            "pairwise_seed_ranking": 0.715,
            "predicted_best_mean_error": 1.9137072399258614,
            "seed0_mean_error": 2.011523014307022,
            "random_seed_mean_error": 1.962140828371048,
            "oracle_best_mean_error": 1.8912434473633766,
            "improvement_over_seed0": 0.09781577438116074,
            "gap_to_oracle": 0.022463792562484874,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3362448781728744
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.509926540851593
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6845154654979706
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.811048317750295
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9625638720393181
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2293320655822755,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.883438268303871,
                "rejected_mean_error": 2.6746943056583405,
                "gap_rejected_minus_accepted": 0.7912560373544695
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9799784421920776,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.811048317750295,
                "rejected_mean_error": 2.4171105349063873,
                "gap_rejected_minus_accepted": 0.6060622171560923
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7373831272125244,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.6845154654979706,
                "rejected_mean_error": 2.2406122785806657,
                "gap_rejected_minus_accepted": 0.5560968130826951
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5749193131923676,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.509926540851593,
                "rejected_mean_error": 2.1134429824352265,
                "gap_rejected_minus_accepted": 0.6035164415836336
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2341136932373047,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9258140060636733,
                "rejected_mean_error": 2.782904088497162,
                "gap_rejected_minus_accepted": 0.8570900824334886
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.966069370508194,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.8222352941830953,
                "rejected_mean_error": 2.5793861746788025,
                "gap_rejected_minus_accepted": 0.7571508804957072
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7624958157539368,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.702490621805191,
                "rejected_mean_error": 2.320555406808853,
                "gap_rejected_minus_accepted": 0.618064785003662
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6001352071762085,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.5325631976127625,
                "rejected_mean_error": 2.171176286538442,
                "gap_rejected_minus_accepted": 0.6386130889256794
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.7702087003165334,
            "spearman": 0.7902007835587571,
            "auroc_top30_bad": 0.8639285714285714,
            "mae": 0.3313660552352667,
            "mse": 0.29722794650500767,
            "expert_lt_perturb_large": 0.50625,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7526163345095056,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7675461450591683
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7388016440719366
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7485626992583275
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0553352387746175
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3148418681323528
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9535484747253797,
            "spearman": 0.9180042375264845,
            "auroc_top30_worst": 0.9457440476190476,
            "pairwise_seed_ranking": 0.545,
            "predicted_best_mean_error": 1.8713487192988396,
            "seed0_mean_error": 1.8995800495147706,
            "random_seed_mean_error": 1.8808846116065978,
            "oracle_best_mean_error": 1.8494211554527282,
            "improvement_over_seed0": 0.02823133021593094,
            "gap_to_oracle": 0.021927563846111386,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2314539700746536
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4669682061672211
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6688803178071976
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.773516786893209
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8811210370063782
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.307587146759033,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8376673407024808,
                "rejected_mean_error": 2.272204303741455,
                "gap_rejected_minus_accepted": 0.43453696303897416
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1840705275535583,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.773516786893209,
                "rejected_mean_error": 2.2039337873458864,
                "gap_rejected_minus_accepted": 0.4304170004526775
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.004047989845276,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.6688803178071976,
                "rejected_mean_error": 2.093361756205559,
                "gap_rejected_minus_accepted": 0.4244814383983613
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7644112706184387,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.4669682061672211,
                "rejected_mean_error": 2.0191719806194306,
                "gap_rejected_minus_accepted": 0.5522037744522095
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2543586254119874,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.8532671067449782,
                "rejected_mean_error": 2.3163965344429016,
                "gap_rejected_minus_accepted": 0.4631294276979234
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2203009128570557,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7981067558129629,
                "rejected_mean_error": 2.2039999306201934,
                "gap_rejected_minus_accepted": 0.40589317480723053
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.061761498451233,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.681761732697487,
                "rejected_mean_error": 2.117398366332054,
                "gap_rejected_minus_accepted": 0.43563663363456717
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7688690423965454,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.4908511519432068,
                "rejected_mean_error": 2.0358230153719585,
                "gap_rejected_minus_accepted": 0.5449718634287517
              }
            ]
          }
        }
      }
    }
  ]
}
```
