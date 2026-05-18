# Stage 6 Experiments: holdout_libero_object

```json
{
  "split": "holdout_libero_object",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 60,
      "best_calib_loss": 0.09202325344085693,
      "train_time_sec": 22.27012610435486,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8987805815499059,
            "spearman": 0.8116306885493002,
            "auroc_top30_bad": 0.8795957380952382,
            "mae": 0.2193186775714159,
            "mse": 0.2292228835239942,
            "expert_lt_perturb_large": 0.987,
            "expert_lt_other_task": 0.524,
            "expert_lt_simvla_seed0": 0.984,
            "same_context_pred_std": 0.7668761142329031,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5303397386521101
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5594787854969502
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7182356686651706
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.01834441665411
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
            "pearson": 0.9980835837083615,
            "spearman": 0.9956388342814487,
            "auroc_top30_worst": 0.9987653333333333,
            "pairwise_seed_ranking": 0.8557,
            "predicted_best_mean_error": 1.710136283904314,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.0842881137132645,
            "gap_to_oracle": 0.008542236179113205,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7315950658917427
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8834504606962204
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.084637366425991
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3056796165068945
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.068539738655092,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4903075207008256,
                "rejected_mean_error": 4.438213098526001,
                "gap_rejected_minus_accepted": 2.9479055778251753
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.974001407623291,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3056796165068945,
                "rejected_mean_error": 3.223353464412689,
                "gap_rejected_minus_accepted": 1.9176738479057946
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4936261773109436,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.084637366425991,
                "rejected_mean_error": 2.4855587905406953,
                "gap_rejected_minus_accepted": 1.4009214241147043
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0977640748023987,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8834504606962204,
                "rejected_mean_error": 2.085647284412384,
                "gap_rejected_minus_accepted": 1.2021968237161638
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1202987909317024,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4920862533317671,
                "rejected_mean_error": 4.51546769618988,
                "gap_rejected_minus_accepted": 3.023381442858113
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9979563653469086,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.302303878823916,
                "rejected_mean_error": 3.2707859539985655,
                "gap_rejected_minus_accepted": 1.9684820751746495
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4931560158729553,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0774393766522408,
                "rejected_mean_error": 2.5114094185829163,
                "gap_rejected_minus_accepted": 1.4339700419306756
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0888735353946686,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8723777745962142,
                "rejected_mean_error": 2.101773271958033,
                "gap_rejected_minus_accepted": 1.2293954973618189
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8121353020169891,
            "spearman": 0.7076177843767737,
            "auroc_top30_bad": 0.7733180952380952,
            "mae": 0.47049422031342986,
            "mse": 0.514793114124953,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.52,
            "expert_lt_simvla_seed0": 0.96,
            "same_context_pred_std": 0.8958435374570581,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.48054088759422303
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6768533280611039
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7890986500620842
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0997309345642725
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
            "pearson": 0.8411502819477132,
            "spearman": 0.7736026711057096,
            "auroc_top30_worst": 0.864649142857143,
            "pairwise_seed_ranking": 0.7484,
            "predicted_best_mean_error": 2.012538196206093,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.09194280850887315,
            "gap_to_oracle": 0.023642966508865326,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2709803774356843
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.149781754670235
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4513102859973908
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5964152811369154
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.2943726062774665,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8431301634841495,
                "rejected_mean_error": 4.210811765670776,
                "gap_rejected_minus_accepted": 2.367681602186627
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7652186155319214,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5954097778781882,
                "rejected_mean_error": 3.5302681877209356,
                "gap_rejected_minus_accepted": 1.9348584098427475
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.696239948272705,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4513102859973908,
                "rejected_mean_error": 2.7084863614082337,
                "gap_rejected_minus_accepted": 1.257176075410843
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1995850801467896,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1508928224111137,
                "rejected_mean_error": 2.39022780278958,
                "gap_rejected_minus_accepted": 1.2393349803784663
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.3123046875,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8660761578877767,
                "rejected_mean_error": 4.250124626159668,
                "gap_rejected_minus_accepted": 2.384048468271891
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.796460807323456,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.608955104083301,
                "rejected_mean_error": 3.5753277256375267,
                "gap_rejected_minus_accepted": 1.9663726215542257
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7270631194114685,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.461523892879486,
                "rejected_mean_error": 2.7474381165504456,
                "gap_rejected_minus_accepted": 1.2859142236709595
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2048350870609283,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1077925061422682,
                "rejected_mean_error": 2.4402637609186018,
                "gap_rejected_minus_accepted": 1.3324712547763335
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6154461774184052,
            "spearman": 0.5320843053775053,
            "auroc_top30_bad": 0.6388464761904762,
            "mae": 0.545870159292221,
            "mse": 0.706226490539874,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.98,
            "same_context_pred_std": 0.633484242836719,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5629892661571503
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7918324338436127
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9226623907446861
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1352053724050521
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
            "pearson": 0.8471025632248768,
            "spearman": 0.7711679129394643,
            "auroc_top30_worst": 0.8356358095238096,
            "pairwise_seed_ranking": 0.7868,
            "predicted_best_mean_error": 1.6004279489517212,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.056715193510055384,
            "gap_to_oracle": 0.020530427455902167,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4278632981777191
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8107630671598972
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1628781174659728
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3589279091815705
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.074249410629273,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4766724582778084,
                "rejected_mean_error": 3.1797125835418703,
                "gap_rejected_minus_accepted": 1.703040125264062
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6824575364589691,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.358759059531966,
                "rejected_mean_error": 2.509787059820498,
                "gap_rejected_minus_accepted": 1.151028000288532
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.426658570766449,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1628781174659728,
                "rejected_mean_error": 2.131074824142456,
                "gap_rejected_minus_accepted": 0.9681967066764832
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0672792494297028,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.813495870977164,
                "rejected_mean_error": 1.9253963510025782,
                "gap_rejected_minus_accepted": 1.1119004800254142
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.122824645042419,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4787491250038147,
                "rejected_mean_error": 3.262689299583435,
                "gap_rejected_minus_accepted": 1.7839401745796202
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.712213933467865,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3538778519885426,
                "rejected_mean_error": 2.5573115443426464,
                "gap_rejected_minus_accepted": 1.2034336923541038
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4242556691169739,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.15319038438797,
                "rejected_mean_error": 2.1610959005355834,
                "gap_rejected_minus_accepted": 1.0079055161476134
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0558664500713348,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7959332399898105,
                "rejected_mean_error": 1.9472833769844178,
                "gap_rejected_minus_accepted": 1.1513501369946073
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.49980401092012106,
            "spearman": 0.3861655246332358,
            "auroc_top30_bad": 0.5731935238095238,
            "mae": 0.4871413889825344,
            "mse": 0.6479044993143596,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.48,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6087785781285268,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0789200111031532
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0461139699220658
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.043601739025116
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2608998162905376
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
            "pearson": 0.658683200723723,
            "spearman": 0.534077215537418,
            "auroc_top30_worst": 0.695424,
            "pairwise_seed_ranking": 0.7576,
            "predicted_best_mean_error": 1.6138616790771485,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.04788944888114921,
            "gap_to_oracle": 0.02183774709701547,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9527323348522186
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.310583680581588
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4900796785831452
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5802035185891683
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8637325167655945,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6241606223053402,
                "rejected_mean_error": 1.98068736743927,
                "gap_rejected_minus_accepted": 0.3565267451339298
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7169740796089172,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5797870595847021,
                "rejected_mean_error": 1.8993806587621427,
                "gap_rejected_minus_accepted": 0.31959359917744057
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.51100355386734,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4900796785831452,
                "rejected_mean_error": 1.8295469150543213,
                "gap_rejected_minus_accepted": 0.33946723647117616
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3309429287910461,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.3130862892816624,
                "rejected_mean_error": 1.7756356589949374,
                "gap_rejected_minus_accepted": 0.462549369713275
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8741829156875611,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6314128835995991,
                "rejected_mean_error": 1.9347953271865845,
                "gap_rejected_minus_accepted": 0.3033824435869854
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7330061793327332,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5814808336171238,
                "rejected_mean_error": 1.9000137476694017,
                "gap_rejected_minus_accepted": 0.3185329140522779
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5300822257995605,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4897999768257142,
                "rejected_mean_error": 1.8337022790908812,
                "gap_rejected_minus_accepted": 0.34390230226516705
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.34212988615036,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.3371969716889518,
                "rejected_mean_error": 1.7710929025303235,
                "gap_rejected_minus_accepted": 0.4338959308413717
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
      "best_calib_loss": 0.036357153207063675,
      "train_time_sec": 28.329631567001343,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9985516062609322,
            "spearman": 0.9968069699724613,
            "auroc_top30_bad": 0.9981473333333333,
            "mae": 0.046933227693662045,
            "mse": 0.003793788431013658,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7906167569214236,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.024218861170113088
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19994062561392784
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6187511021345854
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9871566902140776
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
            "pearson": 0.9992087618502851,
            "spearman": 0.9985283988291007,
            "auroc_top30_worst": 0.999400380952381,
            "pairwise_seed_ranking": 0.9386,
            "predicted_best_mean_error": 1.7033712745904923,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09105312302708612,
            "gap_to_oracle": 0.0017772268652915812,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7222689840197564
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8795640072584152
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0842130256056786
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3054726941665014
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.073442196846009,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4901015449033843,
                "rejected_mean_error": 4.440066880702973,
                "gap_rejected_minus_accepted": 2.9499653357995883
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0034558176994324,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3054726941665014,
                "rejected_mean_error": 3.223974231433868,
                "gap_rejected_minus_accepted": 1.9185015372673668
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5133804082870483,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0842130256056786,
                "rejected_mean_error": 2.485983131361008,
                "gap_rejected_minus_accepted": 1.4017701057553293
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1024035811424255,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8795640072584152,
                "rejected_mean_error": 2.0869427688916526,
                "gap_rejected_minus_accepted": 1.2073787616332374
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1268206357955934,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917231916387876,
                "rejected_mean_error": 4.518735251426697,
                "gap_rejected_minus_accepted": 3.027012059787909
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0037341117858887,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3021878136396408,
                "rejected_mean_error": 3.2711341495513917,
                "gap_rejected_minus_accepted": 1.968946335911751
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5144908428192139,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0769231219887734,
                "rejected_mean_error": 2.5119256732463837,
                "gap_rejected_minus_accepted": 1.4350025512576103
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0960260331630707,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8674557930231095,
                "rejected_mean_error": 2.1034139324824017,
                "gap_rejected_minus_accepted": 1.2359581394592922
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9661471008855005,
            "spearman": 0.9525663449960756,
            "auroc_top30_bad": 0.9749668571428571,
            "mae": 0.24261268819868564,
            "mse": 0.10520548784339803,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.7916580846413185,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.13715378099679948
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24717736651897432
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6127776940464973
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0283021376053492
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
            "pearson": 0.9824266802802666,
            "spearman": 0.9799531227859987,
            "auroc_top30_worst": 0.994471619047619,
            "pairwise_seed_ranking": 0.8788,
            "predicted_best_mean_error": 1.999867995738983,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.10461300897598291,
            "gap_to_oracle": 0.010972766041755566,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6499241831302642
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9032445430564575
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2274320991039276
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5530295408547306
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.165778589248657,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8432897193431854,
                "rejected_mean_error": 4.2093757629394535,
                "gap_rejected_minus_accepted": 2.366086043596268
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.831036627292633,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.551771794560116,
                "rejected_mean_error": 3.6609033007210434,
                "gap_rejected_minus_accepted": 2.1091315061609275
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9404817819595337,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2274320991039276,
                "rejected_mean_error": 2.9323645483016967,
                "gap_rejected_minus_accepted": 1.704932449197769
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3898185193538666,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.903588597290813,
                "rejected_mean_error": 2.4728384991211216,
                "gap_rejected_minus_accepted": 1.5692499018303088
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.209654092788696,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8661894883049859,
                "rejected_mean_error": 4.249104652404785,
                "gap_rejected_minus_accepted": 2.382915164099799
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8810665607452393,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5579147581110664,
                "rejected_mean_error": 3.7268284351106673,
                "gap_rejected_minus_accepted": 2.168913676999601
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.962939977645874,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2267870683670044,
                "rejected_mean_error": 2.9821749410629272,
                "gap_rejected_minus_accepted": 1.755387872695923
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3877708315849304,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8893965369179135,
                "rejected_mean_error": 2.513841012582422,
                "gap_rejected_minus_accepted": 1.6244444756645084
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9648235732488873,
            "spearman": 0.9597889536209696,
            "auroc_top30_bad": 0.9653973333333333,
            "mae": 0.20961285582855343,
            "mse": 0.07945735399962964,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6438649231517677,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10747837781906128
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21124903736114503
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6408280757308006
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.046952225581805
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
            "pearson": 0.975385856882044,
            "spearman": 0.9743055282200715,
            "auroc_top30_worst": 0.9695664761904761,
            "pairwise_seed_ranking": 0.8732,
            "predicted_best_mean_error": 1.5858730615377425,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07127008092403408,
            "gap_to_oracle": 0.005975540041923466,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4212164752483368
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6639794709208684
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0305333355903625
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3112612874396066
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5923097848892214,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4631736209127637,
                "rejected_mean_error": 3.3012021198272703,
                "gap_rejected_minus_accepted": 1.8380284989145066
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8794910609722137,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3106178563712374,
                "rejected_mean_error": 2.6539030577808904,
                "gap_rejected_minus_accepted": 1.343285201409653
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6125571727752686,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0305333355903625,
                "rejected_mean_error": 2.2634196060180662,
                "gap_rejected_minus_accepted": 1.2328862704277037
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1128378808498383,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6653077189152995,
                "rejected_mean_error": 1.9748978361630516,
                "gap_rejected_minus_accepted": 1.309590117247752
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6743761062622067,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4687237249480354,
                "rejected_mean_error": 3.3529179000854494,
                "gap_rejected_minus_accepted": 1.884194175137414
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8734810650348663,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3067750474985909,
                "rejected_mean_error": 2.6971246306858365,
                "gap_rejected_minus_accepted": 1.3903495831872457
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6288084387779236,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0211816763877868,
                "rejected_mean_error": 2.2931046085357667,
                "gap_rejected_minus_accepted": 1.27192293214798
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1296105682849884,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.657516738725087,
                "rejected_mean_error": 1.993915674201945,
                "gap_rejected_minus_accepted": 1.3363989354768582
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9457911277070333,
            "spearman": 0.9352984441648549,
            "auroc_top30_bad": 0.944479238095238,
            "mae": 0.21164422187954188,
            "mse": 0.08009243286329583,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.956,
            "expert_lt_simvla_seed0": 0.988,
            "same_context_pred_std": 0.5944495892292605,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1265564957857132
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.26503592722415925
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7992196914672851
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1470276908874513
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
            "pearson": 0.8767798420824703,
            "spearman": 0.8665512699848129,
            "auroc_top30_worst": 0.8928182857142857,
            "pairwise_seed_ranking": 0.8212,
            "predicted_best_mean_error": 1.6091015012264251,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.05264962673187257,
            "gap_to_oracle": 0.017077569246292112,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9040124020576477
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.120463204402954
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3855172827243805
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.533970820655955
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0835143089294434,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6016084952089522,
                "rejected_mean_error": 2.1836565113067627,
                "gap_rejected_minus_accepted": 0.5820480160978105
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.857997566461563,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5336724630732927,
                "rejected_mean_error": 2.0374297863378312,
                "gap_rejected_minus_accepted": 0.5037573232645385
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.604900598526001,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3855172827243805,
                "rejected_mean_error": 1.934109310913086,
                "gap_rejected_minus_accepted": 0.5485920281887056
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3622758984565735,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1219471693991092,
                "rejected_mean_error": 1.8394846926376685,
                "gap_rejected_minus_accepted": 0.7175375232385592
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0849607944488526,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6049324456850689,
                "rejected_mean_error": 2.1731192684173584,
                "gap_rejected_minus_accepted": 0.5681868227322895
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8726381957530975,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5412416314696247,
                "rejected_mean_error": 2.0194539191230896,
                "gap_rejected_minus_accepted": 0.4782122876534649
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5815989971160889,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3939127840995789,
                "rejected_mean_error": 1.9295894718170166,
                "gap_rejected_minus_accepted": 0.5356766877174377
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3327416777610779,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1287453070519462,
                "rejected_mean_error": 1.8413199339320954,
                "gap_rejected_minus_accepted": 0.7125746268801492
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
      "best_epoch": 160,
      "best_calib_loss": 0.010724923573434353,
      "train_time_sec": 66.92751717567444,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998122267281842,
            "spearman": 0.9989101031681721,
            "auroc_top30_bad": 0.9998620952380952,
            "mae": 0.015470888422010467,
            "mse": 0.00044212538725793717,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8115503148537185,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0012693369686603547
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19970632588267326
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185645805329084
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9863486747086048
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
            "pearson": 0.9998072274099244,
            "spearman": 0.9995243179409614,
            "auroc_top30_worst": 0.9998868571428571,
            "pairwise_seed_ranking": 0.9702,
            "predicted_best_mean_error": 1.7021601240038873,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09226427361369116,
            "gap_to_oracle": 0.0005660762786865448,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7220109855532646
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8789971539258957
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0839519506812096
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.305185878745715
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.143379330635071,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899262463715341,
                "rejected_mean_error": 4.441644567489624,
                "gap_rejected_minus_accepted": 2.95171832111809
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.040457308292389,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.305185878745715,
                "rejected_mean_error": 3.224834677696228,
                "gap_rejected_minus_accepted": 1.919648798950513
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.515506088733673,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0839519506812096,
                "rejected_mean_error": 2.486244206285477,
                "gap_rejected_minus_accepted": 1.4022922556042672
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0859380066394806,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8789971539258957,
                "rejected_mean_error": 2.087131720002492,
                "gap_rejected_minus_accepted": 1.2081345660765965
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.191726922988892,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0402501225471497,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020702888568243,
                "rejected_mean_error": 3.2714867238998413,
                "gap_rejected_minus_accepted": 1.969416435043017
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5181037187576294,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0765455630421639,
                "rejected_mean_error": 2.512303232192993,
                "gap_rejected_minus_accepted": 1.4357576691508291
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0827911794185638,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8667690774202347,
                "rejected_mean_error": 2.10364283768336,
                "gap_rejected_minus_accepted": 1.236873760263125
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9932469371741048,
            "spearman": 0.9890551135729363,
            "auroc_top30_bad": 0.9939100952380953,
            "mae": 0.10277812097361311,
            "mse": 0.023416516283514717,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9435466839136141,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05176867461204529
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18887362625598908
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5855266852974892
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0190775304555892
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
            "pearson": 0.9914447564371996,
            "spearman": 0.9940770941933404,
            "auroc_top30_worst": 0.9961478095238094,
            "pairwise_seed_ranking": 0.9256,
            "predicted_best_mean_error": 1.9934128881692887,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11106811654567728,
            "gap_to_oracle": 0.004517658472061203,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6197860777378082
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8676514380062238
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2216337525844574
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.553811035780256
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.240438508987427,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8420477249092526,
                "rejected_mean_error": 4.220553712844849,
                "gap_rejected_minus_accepted": 2.378505987935596
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.875206232070923,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.552767993387316,
                "rejected_mean_error": 3.6579210697271574,
                "gap_rejected_minus_accepted": 2.1051530763398416
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9208567142486572,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2216337525844574,
                "rejected_mean_error": 2.938162894821167,
                "gap_rejected_minus_accepted": 1.7165291422367097
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.297497183084488,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8689489645508531,
                "rejected_mean_error": 2.4844096891399126,
                "gap_rejected_minus_accepted": 1.6154607245890595
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.263794803619385,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8656025314331055,
                "rejected_mean_error": 4.254387264251709,
                "gap_rejected_minus_accepted": 2.3887847328186034
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.961265444755554,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.559065182578755,
                "rejected_mean_error": 3.7234136831192743,
                "gap_rejected_minus_accepted": 2.1643485005405196
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9372839331626892,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2200701093673707,
                "rejected_mean_error": 2.988891900062561,
                "gap_rejected_minus_accepted": 1.7688217906951904
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3025860488414764,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8665054885167924,
                "rejected_mean_error": 2.5215529700651524,
                "gap_rejected_minus_accepted": 1.65504748154836
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9899367062016109,
            "spearman": 0.9887250004545294,
            "auroc_top30_bad": 0.9889104761904762,
            "mae": 0.08690507296686992,
            "mse": 0.01813881604874303,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7784484090277924,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.031617868721485136
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18293830838203431
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6266092551589012
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0414509811639785
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
            "pearson": 0.9846171182572006,
            "spearman": 0.9899178738674393,
            "auroc_top30_worst": 0.9827687619047618,
            "pairwise_seed_ranking": 0.8956,
            "predicted_best_mean_error": 1.5889951121807098,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06814803028106686,
            "gap_to_oracle": 0.009097590684890688,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4079545941352844
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6552566347213892
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0238350720405578
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3071955379519635
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.740742635726933,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4595929243829515,
                "rejected_mean_error": 3.333428388595581,
                "gap_rejected_minus_accepted": 1.8738354642126296
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1069135069847107,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3065203809305597,
                "rejected_mean_error": 2.666169302151226,
                "gap_rejected_minus_accepted": 1.3596489212206662
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7401129603385925,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0238350720405578,
                "rejected_mean_error": 2.270117869567871,
                "gap_rejected_minus_accepted": 1.2462827975273132
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0863606929779053,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6565429726347756,
                "rejected_mean_error": 1.9778256542909107,
                "gap_rejected_minus_accepted": 1.3212826816561352
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.894754195213318,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4644762629932828,
                "rejected_mean_error": 3.3911450576782225,
                "gap_rejected_minus_accepted": 1.9266687946849397
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.107801616191864,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3037933184501322,
                "rejected_mean_error": 2.705975159766182,
                "gap_rejected_minus_accepted": 1.4021818413160498
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.757982075214386,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0151039252281189,
                "rejected_mean_error": 2.2991823596954344,
                "gap_rejected_minus_accepted": 1.2840784344673155
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1114027798175812,
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
            "pearson": 0.99159173289523,
            "spearman": 0.9851164532888194,
            "auroc_top30_bad": 0.9870929523809524,
            "mae": 0.0714207299024798,
            "mse": 0.01126851862821006,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7328209359430967,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05125767081975937
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21534900732040405
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7827534703254699
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.135271560796102
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
            "pearson": 0.9800364627505183,
            "spearman": 0.9708529682258998,
            "auroc_top30_worst": 0.9727634285714285,
            "pairwise_seed_ranking": 0.9136,
            "predicted_best_mean_error": 1.5989358849525452,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06281524300575247,
            "gap_to_oracle": 0.006911952972412205,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8558216650485992
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.101168187860495
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3589977821826935
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5161691085933877
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0732987165451053,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5911065163347455,
                "rejected_mean_error": 2.2781743211746215,
                "gap_rejected_minus_accepted": 0.687067804839876
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9381280541419983,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5156352703510252,
                "rejected_mean_error": 2.091426110877016,
                "gap_rejected_minus_accepted": 0.5757908405259906
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7606855034828186,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3589977821826935,
                "rejected_mean_error": 1.960628811454773,
                "gap_rejected_minus_accepted": 0.6016310292720795
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4497090280056,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.102125715619078,
                "rejected_mean_error": 1.8461059466751815,
                "gap_rejected_minus_accepted": 0.7439802310561034
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.065403699874878,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5979109183947244,
                "rejected_mean_error": 2.2363130140304563,
                "gap_rejected_minus_accepted": 0.6384020956357319
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9394619464874268,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5234655393636163,
                "rejected_mean_error": 2.0722178750567966,
                "gap_rejected_minus_accepted": 0.5487523356931803
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7737712860107422,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3704609360694886,
                "rejected_mean_error": 1.9530413198471068,
                "gap_rejected_minus_accepted": 0.5825803837776182
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4715487658977509,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1125052684829349,
                "rejected_mean_error": 1.8467911768724574,
                "gap_rejected_minus_accepted": 0.7342859083895226
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
      "best_epoch": 160,
      "best_calib_loss": 0.012692101299762726,
      "train_time_sec": 70.34790563583374,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9999226294658936,
            "spearman": 0.999250195496121,
            "auroc_top30_bad": 0.9999244285714285,
            "mae": 0.009611072118595769,
            "mse": 0.00018391192892276933,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8057021058946504,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00019051821529865264
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19964732012152672
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185158040493727
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9863460011780262
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
            "pearson": 0.9999306045659515,
            "spearman": 0.9998114598084539,
            "auroc_top30_worst": 0.9999493333333334,
            "pairwise_seed_ranking": 0.9728,
            "predicted_best_mean_error": 1.7020918348431586,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09233256277441981,
            "gap_to_oracle": 0.000497787117957893,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7211429787278175
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8787070515394211
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.083759618461132
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.30514169374307
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1491596937179573,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899192884167036,
                "rejected_mean_error": 4.4417071890830995,
                "gap_rejected_minus_accepted": 2.951787900666396
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.027694582939148,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.30514169374307,
                "rejected_mean_error": 3.2249672327041625,
                "gap_rejected_minus_accepted": 1.9198255389610925
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5165104269981384,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.083759618461132,
                "rejected_mean_error": 2.4864365385055542,
                "gap_rejected_minus_accepted": 1.4026769200444222
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.093380630016327,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8787070515394211,
                "rejected_mean_error": 2.0872284207979837,
                "gap_rejected_minus_accepted": 1.2085213692585626
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.189623904228211,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0308451056480408,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019783587853113,
                "rejected_mean_error": 3.27176251411438,
                "gap_rejected_minus_accepted": 1.9697841553290685
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5148810148239136,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0764620199799537,
                "rejected_mean_error": 2.5123867752552034,
                "gap_rejected_minus_accepted": 1.4359247552752497
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0852706134319305,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8663601452112197,
                "rejected_mean_error": 2.103779148419698,
                "gap_rejected_minus_accepted": 1.2374190032084784
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9894908057478152,
            "spearman": 0.9813386346921679,
            "auroc_top30_bad": 0.9936373333333334,
            "mae": 0.12357072302292688,
            "mse": 0.027962984276384578,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8757001948591162,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11632608109712601
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21204409217834472
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5863362670540809
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0190185184876124
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
            "pearson": 0.9939800954575827,
            "spearman": 0.9923469303980356,
            "auroc_top30_worst": 0.9991161904761905,
            "pairwise_seed_ranking": 0.9316,
            "predicted_best_mean_error": 1.9922189506292343,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11226205408573176,
            "gap_to_oracle": 0.003323720932006724,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6290866849422455
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8697797960768907
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2247833899974823
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5491266703999627
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.155322170257569,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.842582990937763,
                "rejected_mean_error": 4.215736318588257,
                "gap_rejected_minus_accepted": 2.3731533276504937
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8578444719314575,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5480422452966838,
                "rejected_mean_error": 3.672068117525631,
                "gap_rejected_minus_accepted": 2.1240258722289473
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7653266787528992,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2247833899974823,
                "rejected_mean_error": 2.935013257408142,
                "gap_rejected_minus_accepted": 1.7102298674106597
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.191152811050415,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8715827966840884,
                "rejected_mean_error": 2.483529871148768,
                "gap_rejected_minus_accepted": 1.6119470744646796
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.247730731964111,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.86610019048055,
                "rejected_mean_error": 4.249908332824707,
                "gap_rejected_minus_accepted": 2.383808142344157
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8900545239448547,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5549441582378856,
                "rejected_mean_error": 3.7356459299723306,
                "gap_rejected_minus_accepted": 2.1807017717344452
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.770713448524475,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2239435138702393,
                "rejected_mean_error": 2.9850184955596926,
                "gap_rejected_minus_accepted": 1.7610749816894533
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2007423043251038,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8699968901891557,
                "rejected_mean_error": 2.5203767224429123,
                "gap_rejected_minus_accepted": 1.6503798322537566
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9895882160745282,
            "spearman": 0.9817832731956343,
            "auroc_top30_bad": 0.9785158095238093,
            "mae": 0.10457355165911954,
            "mse": 0.02189049842226755,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7452210610225624,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05032630205154419
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18631536808013915
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6304591631293297
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0433196672677993
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
            "pearson": 0.9865866826571804,
            "spearman": 0.9719445672605231,
            "auroc_top30_worst": 0.9605302857142857,
            "pairwise_seed_ranking": 0.8892,
            "predicted_best_mean_error": 1.5871435611248017,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06999958133697493,
            "gap_to_oracle": 0.007246039628982626,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.41270843148231506
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.654130835372668
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0352291417121888
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3127444819219585
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5122108459472656,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4588860567410786,
                "rejected_mean_error": 3.3397901973724364,
                "gap_rejected_minus_accepted": 1.8809041406313578
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9704459607601166,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3120838244035125,
                "rejected_mean_error": 2.6495145208919393,
                "gap_rejected_minus_accepted": 1.3374306964884268
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6369484066963196,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0352291417121888,
                "rejected_mean_error": 2.25872379989624,
                "gap_rejected_minus_accepted": 1.2234946581840513
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.103342205286026,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6554482084112807,
                "rejected_mean_error": 1.9781913546131666,
                "gap_rejected_minus_accepted": 1.322743146201886
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6376805305480953,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9759304821491241,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3071811164126677,
                "rejected_mean_error": 2.695919315020243,
                "gap_rejected_minus_accepted": 1.3887381986075755
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6468369960784912,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.028483922481537,
                "rejected_mean_error": 2.2858023624420167,
                "gap_rejected_minus_accepted": 1.2573184399604798
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1018109023571014,
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
            "pearson": 0.9845461796405803,
            "spearman": 0.9779342307437044,
            "auroc_top30_bad": 0.9815580952380952,
            "mae": 0.09907663846229707,
            "mse": 0.02193186675000583,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6843284421874073,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08147265124320983
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2170080942630768
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7849834965705872
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1382616738001505
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
            "pearson": 0.9640175696851452,
            "spearman": 0.953938377944562,
            "auroc_top30_worst": 0.9626209523809524,
            "pairwise_seed_ranking": 0.9016,
            "predicted_best_mean_error": 1.597697630405426,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06405349755287171,
            "gap_to_oracle": 0.005673698425292972,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8435965540409088
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1035943681804032
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3612111498355866
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5212697828057478
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0857530355453493,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5967821295261384,
                "rejected_mean_error": 2.2270938024520874,
                "gap_rejected_minus_accepted": 0.630311672925949
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8999208211898804,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5208652233555833,
                "rejected_mean_error": 2.0757696700934023,
                "gap_rejected_minus_accepted": 0.554904446737819
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6990406513214111,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3612111498355866,
                "rejected_mean_error": 1.95841544380188,
                "gap_rejected_minus_accepted": 0.5972042939662934
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.367743581533432,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.104566616848254,
                "rejected_mean_error": 1.8452905762539094,
                "gap_rejected_minus_accepted": 0.7407239594056554
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0970173358917235,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6005810602506,
                "rejected_mean_error": 2.212281737327576,
                "gap_rejected_minus_accepted": 0.6117006770769757
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9073096811771393,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5259210263344056,
                "rejected_mean_error": 2.0649293661117554,
                "gap_rejected_minus_accepted": 0.5390083397773497
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.709216594696045,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.37254336977005,
                "rejected_mean_error": 1.9509588861465454,
                "gap_rejected_minus_accepted": 0.5784155163764955
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3660530745983124,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.114140146308475,
                "rejected_mean_error": 1.8462403891558317,
                "gap_rejected_minus_accepted": 0.7321002428473566
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
      "best_epoch": 159,
      "best_calib_loss": 0.014067614451050758,
      "train_time_sec": 79.7535810470581,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999555010397817,
            "spearman": 0.9981740075152484,
            "auroc_top30_bad": 0.999483,
            "mae": 0.023613839205162367,
            "mse": 0.001029423391355619,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8105320386307517,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.000802094005048275
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19978616260886192
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.618822159549594
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9865269007662932
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
            "pearson": 0.9995720724365306,
            "spearman": 0.9987352232053787,
            "auroc_top30_worst": 0.9994737142857142,
            "pairwise_seed_ranking": 0.9709,
            "predicted_best_mean_error": 1.702712462067604,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09171193554997448,
            "gap_to_oracle": 0.001118414342403229,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.723219484269619
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.87944788377285
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0842320474505425
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3052601686080296
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1550370454788212,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.489949363331,
                "rejected_mean_error": 4.4414365148544315,
                "gap_rejected_minus_accepted": 2.9514871515234313
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0215800404548645,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3052601686080296,
                "rejected_mean_error": 3.2246118081092834,
                "gap_rejected_minus_accepted": 1.9193516395012538
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5211421251296997,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0842320474505425,
                "rejected_mean_error": 2.4859641095161438,
                "gap_rejected_minus_accepted": 1.4017320620656013
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0888850688934326,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.87944788377285,
                "rejected_mean_error": 2.086981476720174,
                "gap_rejected_minus_accepted": 1.2075335929473243
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2232322692871103,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917422084344758,
                "rejected_mean_error": 4.518564100265503,
                "gap_rejected_minus_accepted": 3.0268218918310272
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.043227791786194,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020201389392216,
                "rejected_mean_error": 3.271637173652649,
                "gap_rejected_minus_accepted": 1.9696170347134272
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5175332427024841,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.077002615749836,
                "rejected_mean_error": 2.511846179485321,
                "gap_rejected_minus_accepted": 1.434843563735485
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0784672796726227,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8667609325647354,
                "rejected_mean_error": 2.103645552635193,
                "gap_rejected_minus_accepted": 1.2368846200704575
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9889145774533797,
            "spearman": 0.9761226058355842,
            "auroc_top30_bad": 0.9929142857142856,
            "mae": 0.1317659015104269,
            "mse": 0.031668399901418794,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.895960258258356,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1339868425130844
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22029650633335113
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5863369330048561
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0190875779867172
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
            "pearson": 0.9934324460588293,
            "spearman": 0.9908063767080812,
            "auroc_top30_worst": 0.999640380952381,
            "pairwise_seed_ranking": 0.9176,
            "predicted_best_mean_error": 1.992849951148033,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11163105356693293,
            "gap_to_oracle": 0.003954721450805554,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6432915580272675
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8714317728120548
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2263725694179535
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5462473913995443
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.093720388412476,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8429894541369545,
                "rejected_mean_error": 4.212078149795532,
                "gap_rejected_minus_accepted": 2.369088695658578
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.856682300567627,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5451901868351496,
                "rejected_mean_error": 3.6806060688945053,
                "gap_rejected_minus_accepted": 2.1354158820593554
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7762218117713928,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2263725694179535,
                "rejected_mean_error": 2.933424077987671,
                "gap_rejected_minus_accepted": 1.7070515085697175
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1816305220127106,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8733402474429279,
                "rejected_mean_error": 2.482942803819508,
                "gap_rejected_minus_accepted": 1.60960255637658
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.169033002853394,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.86610019048055,
                "rejected_mean_error": 4.249908332824707,
                "gap_rejected_minus_accepted": 2.383808142344157
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.907556176185608,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7972399592399597,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.225216073989868,
                "rejected_mean_error": 2.9837459354400635,
                "gap_rejected_minus_accepted": 1.7585298614501954
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.167603313922882,
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
            "pearson": 0.9881778274077833,
            "spearman": 0.9829319932832647,
            "auroc_top30_bad": 0.9805508571428572,
            "mae": 0.10778827144539428,
            "mse": 0.025789851292991942,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7497291918018265,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.049734837353229526
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1873660170316696
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6277636341452598
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.042395436056455
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
            "pearson": 0.9850757519545777,
            "spearman": 0.9809191936762841,
            "auroc_top30_worst": 0.9699321904761905,
            "pairwise_seed_ranking": 0.9036,
            "predicted_best_mean_error": 1.585554615497589,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.0715885269641876,
            "gap_to_oracle": 0.005657094001769947,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4006874866485596
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6542577802752837
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0271748660087585
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3102193607577384
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.550842022895813,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4607482425371805,
                "rejected_mean_error": 3.3230305252075194,
                "gap_rejected_minus_accepted": 1.862282282670339
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9573598504066467,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3095719746235468,
                "rejected_mean_error": 2.6570340200734974,
                "gap_rejected_minus_accepted": 1.3474620454499506
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6032302975654602,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0271748660087585,
                "rejected_mean_error": 2.2667780755996705,
                "gap_rejected_minus_accepted": 1.239603209590912
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0345117151737213,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6558472700774098,
                "rejected_mean_error": 1.978058050129177,
                "gap_rejected_minus_accepted": 1.322210780051767
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6708156347274774,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.466823774708642,
                "rejected_mean_error": 3.37001745223999,
                "gap_rejected_minus_accepted": 1.9031936775313483
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9679987728595734,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3034668360801942,
                "rejected_mean_error": 2.7069442423563155,
                "gap_rejected_minus_accepted": 1.4034774062761213
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6165956258773804,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0192103962898253,
                "rejected_mean_error": 2.295075888633728,
                "gap_rejected_minus_accepted": 1.2758654923439028
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0063768178224564,
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
            "pearson": 0.9774314065506408,
            "spearman": 0.9748924158705855,
            "auroc_top30_bad": 0.9794316190476191,
            "mae": 0.12156975120141505,
            "mse": 0.030145070992947318,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6852022972256435,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08588309878110886
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2341860565662384
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.783721914100647
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1393802216211955
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
            "pearson": 0.9595497632310704,
            "spearman": 0.9558927855953829,
            "auroc_top30_worst": 0.9613653333333333,
            "pairwise_seed_ranking": 0.9032,
            "predicted_best_mean_error": 1.598305567741394,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06344556021690373,
            "gap_to_oracle": 0.006281635761260951,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8426655390262604
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1007648569842179
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3599498028278352
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5219886366810118
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0543628454208376,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5995180862479739,
                "rejected_mean_error": 2.2024701919555665,
                "gap_rejected_minus_accepted": 0.6029521057075926
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8587974309921265,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5216311069092094,
                "rejected_mean_error": 2.073476913257148,
                "gap_rejected_minus_accepted": 0.5518458063479386
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6350388526916504,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3599498028278352,
                "rejected_mean_error": 1.9596767908096313,
                "gap_rejected_minus_accepted": 0.5997269879817961
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2718859910964966,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1021264396346033,
                "rejected_mean_error": 1.8461057048215428,
                "gap_rejected_minus_accepted": 0.7439792651869395
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.042729640007019,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6082943606376647,
                "rejected_mean_error": 2.1428620338439943,
                "gap_rejected_minus_accepted": 0.5345676732063296
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.848165214061737,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5288453232795798,
                "rejected_mean_error": 2.0562493100998895,
                "gap_rejected_minus_accepted": 0.5274039868203098
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6500157713890076,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3700443568229674,
                "rejected_mean_error": 1.953457899093628,
                "gap_rejected_minus_accepted": 0.5834135422706606
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2827799022197723,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1101071238517761,
                "rejected_mean_error": 1.847599107951404,
                "gap_rejected_minus_accepted": 0.7374919840996279
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
      "best_epoch": 155,
      "best_calib_loss": 0.01262399461120367,
      "train_time_sec": 54.91450071334839,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998791484600434,
            "spearman": 0.9991515366033845,
            "auroc_top30_bad": 0.9998957142857142,
            "mae": 0.010410380596497725,
            "mse": 0.00027736973159994455,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8078579464312606,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0010667296200990678
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19961392292380334
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185258854597807
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9863074967046579
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
            "pearson": 0.9999221522162636,
            "spearman": 0.9998505679300158,
            "auroc_top30_worst": 0.9999457142857143,
            "pairwise_seed_ranking": 0.9794,
            "predicted_best_mean_error": 1.7019701916575432,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09245420596003529,
            "gap_to_oracle": 0.00037614393234242094,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7207642428278923
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8787518800497055
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0837317072272301
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051094699780146
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.158308935165407,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899519003166093,
                "rejected_mean_error": 4.441413681983947,
                "gap_rejected_minus_accepted": 2.951461781667338
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.020226299762726,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051094699780146,
                "rejected_mean_error": 3.2250639039993287,
                "gap_rejected_minus_accepted": 1.9199544340213142
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5111088156700134,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0837317072272301,
                "rejected_mean_error": 2.486464449739456,
                "gap_rejected_minus_accepted": 1.402732742512226
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.088998556137085,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8787518800497055,
                "rejected_mean_error": 2.0872134779612224,
                "gap_rejected_minus_accepted": 1.208461597911517
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.216133165359498,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.023063898086548,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019743714729946,
                "rejected_mean_error": 3.2717744760513305,
                "gap_rejected_minus_accepted": 1.969800104578336
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5093213319778442,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.07637689524889,
                "rejected_mean_error": 2.512471899986267,
                "gap_rejected_minus_accepted": 1.436095004737377
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.086247444152832,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8664352694749832,
                "rejected_mean_error": 2.103754106998444,
                "gap_rejected_minus_accepted": 1.2373188375234605
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9896437181694695,
            "spearman": 0.9810817547530543,
            "auroc_top30_bad": 0.9903702857142858,
            "mae": 0.12238430025946764,
            "mse": 0.027387052335429256,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.872283686384745,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09392910778522491
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2080508544921875
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5895655057549477
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0198223607142767
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
            "pearson": 0.9926937207451791,
            "spearman": 0.9880245667813286,
            "auroc_top30_worst": 0.999768380952381,
            "pairwise_seed_ranking": 0.9192,
            "predicted_best_mean_error": 1.9931605002880097,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11132050442695629,
            "gap_to_oracle": 0.004265270590782189,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6369843108654022
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.871335609887655
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.229242538022995
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5477837899536975
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.065869379043579,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8417427118884193,
                "rejected_mean_error": 4.223298830032348,
                "gap_rejected_minus_accepted": 2.381556118143929
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8342848420143127,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5467037720448689,
                "rejected_mean_error": 3.676074984736336,
                "gap_rejected_minus_accepted": 2.129371212691467
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7251821160316467,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.229242538022995,
                "rejected_mean_error": 2.9305541093826295,
                "gap_rejected_minus_accepted": 1.7013115713596345
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1854917109012604,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8730048115451496,
                "rejected_mean_error": 2.483054854444913,
                "gap_rejected_minus_accepted": 1.6100500428997635
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.149142742156982,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8656373437245686,
                "rejected_mean_error": 4.25407395362854,
                "gap_rejected_minus_accepted": 2.3884366099039713
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8856208324432373,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7260790467262268,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2288121156692504,
                "rejected_mean_error": 2.980149893760681,
                "gap_rejected_minus_accepted": 1.7513377780914305
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1827104687690735,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8699968901891557,
                "rejected_mean_error": 2.5203767224429123,
                "gap_rejected_minus_accepted": 1.6503798322537566
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9896248949085271,
            "spearman": 0.982877348089465,
            "auroc_top30_bad": 0.9813828571428571,
            "mae": 0.10684708983242526,
            "mse": 0.02202977620626859,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7426655416846021,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.039186789333820346
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18287564916610718
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.629356075322628
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0432323464314144
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
            "pearson": 0.9886084932976039,
            "spearman": 0.976443974940144,
            "auroc_top30_worst": 0.9667382857142857,
            "pairwise_seed_ranking": 0.894,
            "predicted_best_mean_error": 1.5858905178308487,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07125262463092796,
            "gap_to_oracle": 0.005992996335029588,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4199915041923523
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6551320147820008
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.031578915309906
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3115383335140978
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.536531591415406,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.458648711575402,
                "rejected_mean_error": 3.3419263038635254,
                "gap_rejected_minus_accepted": 1.8832775922881233
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9567182958126068,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3109681740514496,
                "rejected_mean_error": 2.6528543431918843,
                "gap_rejected_minus_accepted": 1.3418861691404347
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6123037338256836,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.031578915309906,
                "rejected_mean_error": 2.262374026298523,
                "gap_rejected_minus_accepted": 1.2307951109886168
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.064741462469101,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6565348759245949,
                "rejected_mean_error": 1.9778283589550372,
                "gap_rejected_minus_accepted": 1.3212934830304421
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.668885374069214,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4643141012721592,
                "rejected_mean_error": 3.392604513168335,
                "gap_rejected_minus_accepted": 1.9282904118961757
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9821245968341827,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3052493337003943,
                "rejected_mean_error": 2.7016533367217535,
                "gap_rejected_minus_accepted": 1.3964040030213591
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6123037338256836,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0250220322608947,
                "rejected_mean_error": 2.2892642526626585,
                "gap_rejected_minus_accepted": 1.2642422204017638
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0301926732063293,
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
            "pearson": 0.979931425323654,
            "spearman": 0.9700581760946869,
            "auroc_top30_bad": 0.9694049523809524,
            "mae": 0.1288404880238857,
            "mse": 0.029263396978640208,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.673104316187615,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07453907310962676
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21747236671447753
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7845401526451111
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1427394588470459
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
            "pearson": 0.9387051197654234,
            "spearman": 0.9308291018426252,
            "auroc_top30_worst": 0.9323062857142856,
            "pairwise_seed_ranking": 0.8944,
            "predicted_best_mean_error": 1.5978588726520537,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06389225530624398,
            "gap_to_oracle": 0.005834940671920696,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.845735365152359
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.099637037763993
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3627352798938752
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5272587792260814
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0527884244918826,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6076341793537139,
                "rejected_mean_error": 2.129425354003906,
                "gap_rejected_minus_accepted": 0.5217911746501922
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8469517529010773,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5266536944004108,
                "rejected_mean_error": 2.0584412439943502,
                "gap_rejected_minus_accepted": 0.5317875495939395
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.644457459449768,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3627352798938752,
                "rejected_mean_error": 1.9568913137435913,
                "gap_rejected_minus_accepted": 0.594156033849716
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.316959708929062,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1008347113863728,
                "rejected_mean_error": 1.8465371999567575,
                "gap_rejected_minus_accepted": 0.7457024885703847
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0784849882125855,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6146351875199212,
                "rejected_mean_error": 2.0857945919036864,
                "gap_rejected_minus_accepted": 0.47115940438376525
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.838644653558731,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5377130970597905,
                "rejected_mean_error": 2.0299275053872003,
                "gap_rejected_minus_accepted": 0.4922144083274098
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6576674580574036,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.376958330631256,
                "rejected_mean_error": 1.9465439252853394,
                "gap_rejected_minus_accepted": 0.5695855946540833
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3099783062934875,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1094066349286882,
                "rejected_mean_error": 1.8478351015458132,
                "gap_rejected_minus_accepted": 0.738428466617125
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
      "best_epoch": 135,
      "best_calib_loss": 0.012069527059793472,
      "train_time_sec": 72.41339540481567,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994251964896026,
            "spearman": 0.9982770022324593,
            "auroc_top30_bad": 0.9995473333333333,
            "mae": 0.03677401252813674,
            "mse": 0.0027969223716951576,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7888077250326603,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0005033980682492257
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1997947622001171
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6187343414753675
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.986596307784319
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
            "pearson": 0.9993927621251801,
            "spearman": 0.9984597384503158,
            "auroc_top30_worst": 0.9995739047619048,
            "pairwise_seed_ranking": 0.971,
            "predicted_best_mean_error": 1.7022076347470283,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09221676287055014,
            "gap_to_oracle": 0.0006135870218275663,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7227556242346763
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8799423769712448
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.084267324054241
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.305269383295377
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0807826042175295,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4900044362743696,
                "rejected_mean_error": 4.4409408583641055,
                "gap_rejected_minus_accepted": 2.950936422089736
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9851531088352203,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.305269383295377,
                "rejected_mean_error": 3.2245841640472412,
                "gap_rejected_minus_accepted": 1.9193147807518642
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4923877120018005,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.084267324054241,
                "rejected_mean_error": 2.485928832912445,
                "gap_rejected_minus_accepted": 1.401661508858204
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.090968132019043,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8799423769712448,
                "rejected_mean_error": 2.0868166456540425,
                "gap_rejected_minus_accepted": 1.2068742686827978
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.125840425491334,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917173154155414,
                "rejected_mean_error": 4.518788137435913,
                "gap_rejected_minus_accepted": 3.027070822020372
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9935959577560425,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3022210016647975,
                "rejected_mean_error": 3.2710345854759217,
                "gap_rejected_minus_accepted": 1.9688135838111243
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4939396977424622,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.077191191494465,
                "rejected_mean_error": 2.511657603740692,
                "gap_rejected_minus_accepted": 1.4344664122462272
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0811196267604828,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8677919417619705,
                "rejected_mean_error": 2.103301882902781,
                "gap_rejected_minus_accepted": 1.2355099411408106
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9896030162800945,
            "spearman": 0.9807480563588091,
            "auroc_top30_bad": 0.9916228571428571,
            "mae": 0.11840215243054304,
            "mse": 0.027403011351429505,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8573800188936217,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10672509169578552
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20878552358150482
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5879368700623512
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0198455661535264
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
            "pearson": 0.9926740270761636,
            "spearman": 0.9898963514216651,
            "auroc_top30_worst": 0.9989699047619048,
            "pairwise_seed_ranking": 0.9356,
            "predicted_best_mean_error": 1.9915317159891128,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11294928872585319,
            "gap_to_oracle": 0.002636486291885287,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6241096613407136
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8736873283409156
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2239678384304047
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5498248258315679
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.998205709457398,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8416408649815454,
                "rejected_mean_error": 4.224215452194214,
                "gap_rejected_minus_accepted": 2.3825745872126682
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7235679626464844,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5485456563301758,
                "rejected_mean_error": 3.670561101109075,
                "gap_rejected_minus_accepted": 2.1220154447788993
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.761897325515747,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2239678384304047,
                "rejected_mean_error": 2.9358288089752196,
                "gap_rejected_minus_accepted": 1.711860970544815
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2175110876560211,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8751935752245564,
                "rejected_mean_error": 2.4823237092670536,
                "gap_rejected_minus_accepted": 1.6071301340424973
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.093797397613526,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.865179386138916,
                "rejected_mean_error": 4.258195571899414,
                "gap_rejected_minus_accepted": 2.393016185760498
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8264439702033997,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548626369333522,
                "rejected_mean_error": 3.7358879059080095,
                "gap_rejected_minus_accepted": 2.181025268974657
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7756287455558777,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2222022066116334,
                "rejected_mean_error": 2.9867598028182982,
                "gap_rejected_minus_accepted": 1.7645575962066649
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2104641199111938,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8748412851303343,
                "rejected_mean_error": 2.518744653558986,
                "gap_rejected_minus_accepted": 1.6439033684286515
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9884203534784407,
            "spearman": 0.9838049820845405,
            "auroc_top30_bad": 0.982272,
            "mae": 0.11348322035966112,
            "mse": 0.028814705167704856,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7258351270082773,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.044718791007995605
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1871248580932617
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6284143639922142
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0440370297988255
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
            "pearson": 0.9889802738413478,
            "spearman": 0.985210387206648,
            "auroc_top30_worst": 0.9767801904761904,
            "pairwise_seed_ranking": 0.9068,
            "predicted_best_mean_error": 1.5836495233774186,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07349361908435803,
            "gap_to_oracle": 0.0037520018815995204,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.41459683299064637
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6542092907505158
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0265525729179383
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3088901211330886
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4631984233856206,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4586588728692798,
                "rejected_mean_error": 3.341834852218628,
                "gap_rejected_minus_accepted": 1.8831759793493483
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9502620995044708,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3082408913298884,
                "rejected_mean_error": 2.6610187646299126,
                "gap_rejected_minus_accepted": 1.3527778733000242
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6671792268753052,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0265525729179383,
                "rejected_mean_error": 2.267400368690491,
                "gap_rejected_minus_accepted": 1.2408477957725526
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.07161146402359,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6554119703106986,
                "rejected_mean_error": 1.9782034597630944,
                "gap_rejected_minus_accepted": 1.3227914894523958
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5619178533554074,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4643141012721592,
                "rejected_mean_error": 3.392604513168335,
                "gap_rejected_minus_accepted": 1.9282904118961757
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9853668510913849,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3047812389817468,
                "rejected_mean_error": 2.7030427607278975,
                "gap_rejected_minus_accepted": 1.3982615217461507
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6811946034431458,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0155783772468567,
                "rejected_mean_error": 2.2987079076766967,
                "gap_rejected_minus_accepted": 1.28312953042984
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0740890502929688,
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
            "pearson": 0.985161346345961,
            "spearman": 0.9814154911897841,
            "auroc_top30_bad": 0.9846590476190475,
            "mae": 0.1069276764662236,
            "mse": 0.02312563736698093,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6755698614921553,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06828480976819992
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21906010863780975
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7835373859405518
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1369481147130331
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
            "pearson": 0.9683213853936996,
            "spearman": 0.9654737576152049,
            "auroc_top30_worst": 0.9688655238095238,
            "pairwise_seed_ranking": 0.9164,
            "predicted_best_mean_error": 1.5979434244632722,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06380770349502551,
            "gap_to_oracle": 0.005919492483139166,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8479501287937165
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1038177778514533
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.359040568590164
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5184989508344675
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.035455393791199,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5965594869454702,
                "rejected_mean_error": 2.2290975856781006,
                "gap_rejected_minus_accepted": 0.6325380987326303
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.864418625831604,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5182161298416468,
                "rejected_mean_error": 2.083700023520107,
                "gap_rejected_minus_accepted": 0.5654838936784603
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6791381239891052,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.359040568590164,
                "rejected_mean_error": 1.9605860250473022,
                "gap_rejected_minus_accepted": 0.6015454564571381
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.385777324438095,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1052270325037619,
                "rejected_mean_error": 1.8450699678225604,
                "gap_rejected_minus_accepted": 0.7398429353187985
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0373135566711427,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6039567091729905,
                "rejected_mean_error": 2.181900897026062,
                "gap_rejected_minus_accepted": 0.5779441878530716
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.872032880783081,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5253398058248713,
                "rejected_mean_error": 2.066654576195611,
                "gap_rejected_minus_accepted": 0.5413147703707397
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6786546111106873,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3685750136375427,
                "rejected_mean_error": 1.9549272422790527,
                "gap_rejected_minus_accepted": 0.5863522286415099
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3914632201194763,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1141011819006905,
                "rejected_mean_error": 1.8462535162023044,
                "gap_rejected_minus_accepted": 0.7321523343016139
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
      "best_epoch": 118,
      "best_calib_loss": 0.013318771496415138,
      "train_time_sec": 72.4622757434845,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993809341168225,
            "spearman": 0.9984841427005932,
            "auroc_top30_bad": 0.9995783333333333,
            "mae": 0.026686226934854573,
            "mse": 0.0015323665948058227,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8116352312691549,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0017157780826091767
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19981655861735345
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186371680229902
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9865825472493966
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
            "pearson": 0.9994905943142653,
            "spearman": 0.9993176509806735,
            "auroc_top30_worst": 0.9998443809523809,
            "pairwise_seed_ranking": 0.9666,
            "predicted_best_mean_error": 1.702293020606041,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09213137701153751,
            "gap_to_oracle": 0.0006989728808401985,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7225973321795464
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8790934690237046
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0839053357958794
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3052228112777073
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0960042238235475,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899505086408722,
                "rejected_mean_error": 4.441426207065582,
                "gap_rejected_minus_accepted": 2.9514756984247104
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0419737100601196,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3052228112777073,
                "rejected_mean_error": 3.2247238801002505,
                "gap_rejected_minus_accepted": 1.9195010688225431
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5326489210128784,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0839053357958794,
                "rejected_mean_error": 2.486290821170807,
                "gap_rejected_minus_accepted": 1.4023854853749274
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.097766637802124,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8790934690237046,
                "rejected_mean_error": 2.0870996149698895,
                "gap_rejected_minus_accepted": 1.208006145946185
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.144466638565064,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491642521388001,
                "rejected_mean_error": 4.519461283683777,
                "gap_rejected_minus_accepted": 3.0278187622957757
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0441054105758667,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3021080279747645,
                "rejected_mean_error": 3.2713735065460203,
                "gap_rejected_minus_accepted": 1.9692654785712558
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5333327651023865,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0764494736790657,
                "rejected_mean_error": 2.5123993215560914,
                "gap_rejected_minus_accepted": 1.4359498478770256
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.091037541627884,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8669740329980851,
                "rejected_mean_error": 2.1035745191574096,
                "gap_rejected_minus_accepted": 1.2366004861593245
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9876850078040129,
            "spearman": 0.9764417085796728,
            "auroc_top30_bad": 0.9884731428571429,
            "mae": 0.12408373354731271,
            "mse": 0.03260336764740877,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8785722224903117,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12612900608778
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21044866020679473
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5917522578835487
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0195731563329697
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
            "pearson": 0.9890465543451469,
            "spearman": 0.9811043923868114,
            "auroc_top30_worst": 0.9992137142857143,
            "pairwise_seed_ranking": 0.9232,
            "predicted_best_mean_error": 1.9933270494937896,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11115395522117644,
            "gap_to_oracle": 0.004431819796562042,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6649528634548187
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.888312600266475
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.233164691877365
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5482075540686466
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.108349466323853,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8421628187762367,
                "rejected_mean_error": 4.219517868041992,
                "gap_rejected_minus_accepted": 2.377355049265755
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7350661158561707,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5469236318876802,
                "rejected_mean_error": 3.6754168100631275,
                "gap_rejected_minus_accepted": 2.1284931781754475
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7777915000915527,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.233164691877365,
                "rejected_mean_error": 2.926631955528259,
                "gap_rejected_minus_accepted": 1.693467263650894
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2004692554473877,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8897869814508639,
                "rejected_mean_error": 2.4774488574539966,
                "gap_rejected_minus_accepted": 1.5876618760031327
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.180731248855591,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.865179386138916,
                "rejected_mean_error": 4.258195571899414,
                "gap_rejected_minus_accepted": 2.393016185760498
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8340813517570496,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.555659858938207,
                "rejected_mean_error": 3.73352154852852,
                "gap_rejected_minus_accepted": 2.177861689590313
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7962002158164978,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2337229375839234,
                "rejected_mean_error": 2.9752390718460084,
                "gap_rejected_minus_accepted": 1.741516134262085
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2106806337833405,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8804594505400885,
                "rejected_mean_error": 2.5168519026455396,
                "gap_rejected_minus_accepted": 1.6363924521054511
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9875668891539333,
            "spearman": 0.9800652040830921,
            "auroc_top30_bad": 0.9786285714285714,
            "mae": 0.1094815494096619,
            "mse": 0.025338186683721706,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7438063011764873,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05851904988288879
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19267294054031373
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6292314292311668
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0428768773635229
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
            "pearson": 0.9880670433778385,
            "spearman": 0.9745699861567912,
            "auroc_top30_worst": 0.9646445714285714,
            "pairwise_seed_ranking": 0.8984,
            "predicted_best_mean_error": 1.585169580101967,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07197356235980967,
            "gap_to_oracle": 0.005272058606147878,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.41100375962257385
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.657651360027301
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0321176657676696
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.309520851765106
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.417683982849122,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.458699286195967,
                "rejected_mean_error": 3.3414711322784423,
                "gap_rejected_minus_accepted": 1.8827718460824754
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9331676661968231,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3085051780703738,
                "rejected_mean_error": 2.660227593141623,
                "gap_rejected_minus_accepted": 1.351722415071249
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.667254626750946,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0321176657676696,
                "rejected_mean_error": 2.261835275840759,
                "gap_rejected_minus_accepted": 1.2297176100730896
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.082397609949112,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6590764120744821,
                "rejected_mean_error": 1.9769793719593973,
                "gap_rejected_minus_accepted": 1.3179029598849152
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.472262406349182,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4641851909955343,
                "rejected_mean_error": 3.393764705657959,
                "gap_rejected_minus_accepted": 1.9295795146624248
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.940413236618042,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3030816683157243,
                "rejected_mean_error": 2.708087518101647,
                "gap_rejected_minus_accepted": 1.4050058497859226
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6804784536361694,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0259178671836853,
                "rejected_mean_error": 2.288368417739868,
                "gap_rejected_minus_accepted": 1.262450550556183
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0923761427402496,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6485171753262716,
                "rejected_mean_error": 1.9969476126732035,
                "gap_rejected_minus_accepted": 1.348430437346932
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9835487034861627,
            "spearman": 0.9772426429015088,
            "auroc_top30_bad": 0.9819771428571428,
            "mae": 0.09889201394345284,
            "mse": 0.022182849545707258,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6940151224343617,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0652169508934021
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22928196980953217
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7844646059989929
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1383525149027507
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
            "pearson": 0.9625141958426335,
            "spearman": 0.9517595052540834,
            "auroc_top30_worst": 0.9585584761904762,
            "pairwise_seed_ranking": 0.9032,
            "predicted_best_mean_error": 1.5981191936731338,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.0636319342851639,
            "gap_to_oracle": 0.006095261693000786,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.845850087404251
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1020673544934163
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3635907257556916
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.521495000798819
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0329688787460327,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.59611683011055,
                "rejected_mean_error": 2.2330814971923827,
                "gap_rejected_minus_accepted": 0.6369646670818327
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.877922922372818,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5207683331747575,
                "rejected_mean_error": 2.0760597215292935,
                "gap_rejected_minus_accepted": 0.5552913883545361
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6980702877044678,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3635907257556916,
                "rejected_mean_error": 1.9560358678817749,
                "gap_rejected_minus_accepted": 0.5924451421260832
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3440519571304321,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1030700055364602,
                "rejected_mean_error": 1.8457905115160134,
                "gap_rejected_minus_accepted": 0.7427205059795532
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.043301248550415,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6052217210663688,
                "rejected_mean_error": 2.170515789985657,
                "gap_rejected_minus_accepted": 0.565294068919288
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8763851523399353,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5289251342176753,
                "rejected_mean_error": 2.056012410966177,
                "gap_rejected_minus_accepted": 0.5270872767485018
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7076503038406372,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3754616541862488,
                "rejected_mean_error": 1.9480406017303467,
                "gap_rejected_minus_accepted": 0.5725789475440979
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.334114819765091,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.11358119097967,
                "rejected_mean_error": 1.8464287003093862,
                "gap_rejected_minus_accepted": 0.7328475093297162
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
      "best_epoch": 137,
      "best_calib_loss": 0.010646096430718899,
      "train_time_sec": 80.74156665802002,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994163829767574,
            "spearman": 0.9979778393797791,
            "auroc_top30_bad": 0.9995421428571429,
            "mae": 0.025582703052050057,
            "mse": 0.001315664586132583,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8126329611059955,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0025167659372091295
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20016478294730186
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6188416568249464
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.986491812847058
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
            "pearson": 0.9996155501336061,
            "spearman": 0.9986740777309313,
            "auroc_top30_worst": 0.9997678095238095,
            "pairwise_seed_ranking": 0.9678,
            "predicted_best_mean_error": 1.7026836692094802,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09174072840809822,
            "gap_to_oracle": 0.0010896214842794905,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7231368815302849
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8797649760007858
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0841057233691216
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051655321677527
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.143169164657594,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.489944330420759,
                "rejected_mean_error": 4.4414818110466,
                "gap_rejected_minus_accepted": 2.9515374806258414
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0301396250724792,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051655321677527,
                "rejected_mean_error": 3.224895717430115,
                "gap_rejected_minus_accepted": 1.9197301852623623
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.522339940071106,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0841057233691216,
                "rejected_mean_error": 2.486090433597565,
                "gap_rejected_minus_accepted": 1.4019847102284433
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0960156917572021,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8797649760007858,
                "rejected_mean_error": 2.086875779310862,
                "gap_rejected_minus_accepted": 1.2071108033100764
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1890490055084233,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491642521388001,
                "rejected_mean_error": 4.519461283683777,
                "gap_rejected_minus_accepted": 3.0278187622957757
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.04233455657959,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019809724887212,
                "rejected_mean_error": 3.2717546730041502,
                "gap_rejected_minus_accepted": 1.969773700515429
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5218555927276611,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0766184177994729,
                "rejected_mean_error": 2.5122303774356842,
                "gap_rejected_minus_accepted": 1.4356119596362114
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0946883261203766,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8668848496675491,
                "rejected_mean_error": 2.103604246934255,
                "gap_rejected_minus_accepted": 1.236719397266706
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9915635813555059,
            "spearman": 0.9827320563984187,
            "auroc_top30_bad": 0.9938826666666666,
            "mae": 0.10858502209741637,
            "mse": 0.024173240795847057,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9039464986254642,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08460860109329224
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20644035425186158
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5854156823754311
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.018926142414411
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
            "pearson": 0.9953538631567931,
            "spearman": 0.993428914066505,
            "auroc_top30_worst": 0.9997927619047619,
            "pairwise_seed_ranking": 0.9212,
            "predicted_best_mean_error": 1.9922943348884583,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11218666982650771,
            "gap_to_oracle": 0.003399105191230767,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6542842490673065
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8704379035685307
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.222099425840378
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.547839206005973
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.114444398880005,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8420283750693003,
                "rejected_mean_error": 4.220727861404419,
                "gap_rejected_minus_accepted": 2.378699486335119
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8210538625717163,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.546625742503902,
                "rejected_mean_error": 3.67630857476792,
                "gap_rejected_minus_accepted": 2.129682832264018
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7870768308639526,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.222099425840378,
                "rejected_mean_error": 2.9376972215652466,
                "gap_rejected_minus_accepted": 1.7155977957248687
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1635541021823883,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.871119106444307,
                "rejected_mean_error": 2.4836847644732627,
                "gap_rejected_minus_accepted": 1.6125656580289558
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.194782304763794,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8655182372199164,
                "rejected_mean_error": 4.25514591217041,
                "gap_rejected_minus_accepted": 2.3896276749504937
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8642173409461975,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548626369333522,
                "rejected_mean_error": 3.7358879059080095,
                "gap_rejected_minus_accepted": 2.181025268974657
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8033206462860107,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2192690563201904,
                "rejected_mean_error": 2.989692953109741,
                "gap_rejected_minus_accepted": 1.7704238967895507
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1752477586269379,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8705015901535277,
                "rejected_mean_error": 2.5202066898345947,
                "gap_rejected_minus_accepted": 1.649705099681067
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.98873012169579,
            "spearman": 0.9845858684889941,
            "auroc_top30_bad": 0.9875596190476191,
            "mae": 0.1084307786531659,
            "mse": 0.025343434230057513,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7458335291743351,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06546006971597672
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1894753047466278
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6266890144705772
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.041301732214292
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
            "pearson": 0.9882026140059881,
            "spearman": 0.9865904226498706,
            "auroc_top30_worst": 0.9830247619047618,
            "pairwise_seed_ranking": 0.9032,
            "predicted_best_mean_error": 1.5860222512483597,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07112089121341691,
            "gap_to_oracle": 0.006124729752540636,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4110642609596252
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6534313809795257
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0252712861061095
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3079015467085564
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5546480894088752,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4597268793847826,
                "rejected_mean_error": 3.332222793579102,
                "gap_rejected_minus_accepted": 1.8724959141943192
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9462704956531525,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3072209885560588,
                "rejected_mean_error": 2.66407195600077,
                "gap_rejected_minus_accepted": 1.3568509674447111
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6137772798538208,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0252712861061095,
                "rejected_mean_error": 2.2686816555023195,
                "gap_rejected_minus_accepted": 1.24341036939621
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.023036539554596,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6550775044642317,
                "rejected_mean_error": 1.97831518634788,
                "gap_rejected_minus_accepted": 1.3232376818836484
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7125058889389035,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4643141012721592,
                "rejected_mean_error": 3.392604513168335,
                "gap_rejected_minus_accepted": 1.9282904118961757
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9363943040370941,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3019195128889645,
                "rejected_mean_error": 2.7115370905588545,
                "gap_rejected_minus_accepted": 1.40961757766989
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6246932744979858,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0145145134925841,
                "rejected_mean_error": 2.299771771430969,
                "gap_rejected_minus_accepted": 1.285257257938385
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0206057727336884,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6442655022182162,
                "rejected_mean_error": 1.9983799945224414,
                "gap_rejected_minus_accepted": 1.3541144923042252
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9806701784700668,
            "spearman": 0.9754215816517815,
            "auroc_top30_bad": 0.9801980952380952,
            "mae": 0.10809405225078153,
            "mse": 0.025172945109034246,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6946363779499666,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09832633924484253
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22700154783725737
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7875600583076477
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.138325389480591
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
            "pearson": 0.9610923249210501,
            "spearman": 0.948845648334642,
            "auroc_top30_worst": 0.9623893333333333,
            "pairwise_seed_ranking": 0.8998,
            "predicted_best_mean_error": 1.5983725271224976,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06337860083580016,
            "gap_to_oracle": 0.0063485951423645215,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8432425425052643
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1020469498366883
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3645957268238067
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5208374377824605
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1325587272644047,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.59658558011055,
                "rejected_mean_error": 2.228862747192383,
                "gap_rejected_minus_accepted": 0.632277167081833
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9145176112651825,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5202761418091704,
                "rejected_mean_error": 2.077533150633303,
                "gap_rejected_minus_accepted": 0.5572570088241326
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.69416081905365,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3645957268238067,
                "rejected_mean_error": 1.9550308668136596,
                "gap_rejected_minus_accepted": 0.5904351399898529
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3264120221138,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1031479227085845,
                "rejected_mean_error": 1.8457644836879719,
                "gap_rejected_minus_accepted": 0.7426165609793873
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.142145347595215,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6009573170873854,
                "rejected_mean_error": 2.2088954257965088,
                "gap_rejected_minus_accepted": 0.6079381087091233
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9212502837181091,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5259956609119067,
                "rejected_mean_error": 2.064707831730918,
                "gap_rejected_minus_accepted": 0.5387121708190115
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7075291872024536,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3766458745002748,
                "rejected_mean_error": 1.946856381416321,
                "gap_rejected_minus_accepted": 0.5702105069160461
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3359732925891876,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1101071238517761,
                "rejected_mean_error": 1.847599107951404,
                "gap_rejected_minus_accepted": 0.7374919840996279
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
      "best_epoch": 142,
      "best_calib_loss": 0.012427901849150658,
      "train_time_sec": 56.226547718048096,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998151951957576,
            "spearman": 0.9990246632696366,
            "auroc_top30_bad": 0.9997995476190477,
            "mae": 0.023030174210178667,
            "mse": 0.0009097823954821669,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7964425964845041,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0003629552125930786
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19962511867880822
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185528732270003
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9864027237554391
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
            "pearson": 0.9998439595476917,
            "spearman": 0.9995477826698898,
            "auroc_top30_worst": 0.9998792380952382,
            "pairwise_seed_ranking": 0.9695,
            "predicted_best_mean_error": 1.7024955899715424,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09192880764603606,
            "gap_to_oracle": 0.0009015422463416467,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.722087089240551
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8789711218595505
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0837686618685722
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051321231126785
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1265239000320437,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899265274935298,
                "rejected_mean_error": 4.441642037391663,
                "gap_rejected_minus_accepted": 2.951715509898133
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0052844882011414,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051321231126785,
                "rejected_mean_error": 3.224995944595337,
                "gap_rejected_minus_accepted": 1.9198638214826584
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4985443353652954,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0837686618685722,
                "rejected_mean_error": 2.486427495098114,
                "gap_rejected_minus_accepted": 1.4026588332295418
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0813040137290955,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8789711218595505,
                "rejected_mean_error": 2.0871403973579405,
                "gap_rejected_minus_accepted": 1.2081692754983901
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.179234790802002,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0107603073120117,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020091573794683,
                "rejected_mean_error": 3.271670118331909,
                "gap_rejected_minus_accepted": 1.9696609609524407
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4873427152633667,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0763838449120522,
                "rejected_mean_error": 2.5124649503231047,
                "gap_rejected_minus_accepted": 1.4360811054110525
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0790491998195648,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.86644231903553,
                "rejected_mean_error": 2.103751757144928,
                "gap_rejected_minus_accepted": 1.2373094381093979
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.990779106402979,
            "spearman": 0.9832823396897493,
            "auroc_top30_bad": 0.992096380952381,
            "mae": 0.12206158088441006,
            "mse": 0.026477468133828876,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9067489813256822,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11017599219083786
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20308414072990416
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5849662644982337
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0201520491043727
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
            "pearson": 0.9925518407333535,
            "spearman": 0.9929728630866325,
            "auroc_top30_worst": 0.999079619047619,
            "pairwise_seed_ranking": 0.9148,
            "predicted_best_mean_error": 1.993210987687111,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.1112700170278551,
            "gap_to_oracle": 0.004315757989883373,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6223053982257843
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8675889455928252
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.222382186460495
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.551888667539493
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.24249176979065,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.841695894320806,
                "rejected_mean_error": 4.223720188140869,
                "gap_rejected_minus_accepted": 2.3820242938200633
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.775203824043274,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5508040080011973,
                "rejected_mean_error": 3.663800476458126,
                "gap_rejected_minus_accepted": 2.1129964684569287
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.856170892715454,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.222382186460495,
                "rejected_mean_error": 2.9374144609451296,
                "gap_rejected_minus_accepted": 1.7150322744846347
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2476355135440826,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8688866043814455,
                "rejected_mean_error": 2.4844305202317214,
                "gap_rejected_minus_accepted": 1.6155439158502758
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.339526653289795,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.864833976957533,
                "rejected_mean_error": 4.2613042545318605,
                "gap_rejected_minus_accepted": 2.3964702775743274
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8763771057128906,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5576011254825695,
                "rejected_mean_error": 3.7277593764047774,
                "gap_rejected_minus_accepted": 2.170158250922208
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8957906365394592,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2224604558944703,
                "rejected_mean_error": 2.9865015535354615,
                "gap_rejected_minus_accepted": 1.7640410976409913
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2654241621494293,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8700367723192487,
                "rejected_mean_error": 2.520363286217266,
                "gap_rejected_minus_accepted": 1.6503265138980172
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9891784330681266,
            "spearman": 0.9808379963262129,
            "auroc_top30_bad": 0.979064380952381,
            "mae": 0.10252290233578533,
            "mse": 0.01942917600543733,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7658220658163165,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.041324282705783845
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1845772939682007
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6319913090109825
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0433865815718968
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
            "pearson": 0.9853358102880421,
            "spearman": 0.9714902058817317,
            "auroc_top30_worst": 0.9658057142857144,
            "pairwise_seed_ranking": 0.8968,
            "predicted_best_mean_error": 1.5880804467201233,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06906269574165336,
            "gap_to_oracle": 0.008182925224304194,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.40766511344909667
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6557604139431928
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0385980410575866
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3100874674981082
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6157530069351216,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4584742743704053,
                "rejected_mean_error": 3.343496238708496,
                "gap_rejected_minus_accepted": 1.8850219643380908
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0526058673858643,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3093050993748383,
                "rejected_mean_error": 2.6578329405464682,
                "gap_rejected_minus_accepted": 1.34852784117163
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.731151282787323,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0385980410575866,
                "rejected_mean_error": 2.2553549005508424,
                "gap_rejected_minus_accepted": 1.2167568594932558
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.118640661239624,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6571689966006782,
                "rejected_mean_error": 1.9776165342254597,
                "gap_rejected_minus_accepted": 1.3204475376247815
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.709132051467895,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4637714997927347,
                "rejected_mean_error": 3.397487926483154,
                "gap_rejected_minus_accepted": 1.9337164266904194
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0723235607147217,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3054159921120831,
                "rejected_mean_error": 2.7011586522299145,
                "gap_rejected_minus_accepted": 1.3957426601178313
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.758687436580658,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0298415684700013,
                "rejected_mean_error": 2.284444716453552,
                "gap_rejected_minus_accepted": 1.2546031479835509
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0952715575695038,
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
            "pearson": 0.9855248283694664,
            "spearman": 0.9742120867708014,
            "auroc_top30_bad": 0.9761234285714285,
            "mae": 0.09839477500570938,
            "mse": 0.01969213103979768,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7022932793210459,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08312162846326827
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2173803524494171
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7857213364601136
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1394150775909424
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
            "pearson": 0.9588520180994622,
            "spearman": 0.9389228915048363,
            "auroc_top30_worst": 0.949799619047619,
            "pairwise_seed_ranking": 0.892,
            "predicted_best_mean_error": 1.5983784811496735,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.0633726468086242,
            "gap_to_oracle": 0.00635454916954048,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8490813066959381
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1019671690196564
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3659184381961822
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5241175478518898
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1119556188583375,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5966529053846994,
                "rejected_mean_error": 2.2282568197250368,
                "gap_rejected_minus_accepted": 0.6316039143403374
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9181406497955322,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.523894547302924,
                "rejected_mean_error": 2.0667010549539193,
                "gap_rejected_minus_accepted": 0.5428065076509954
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7368836998939514,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3659184381961822,
                "rejected_mean_error": 1.9537081554412843,
                "gap_rejected_minus_accepted": 0.5877897172451021
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4695678651332855,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1028955467402364,
                "rejected_mean_error": 1.8458487885738768,
                "gap_rejected_minus_accepted": 0.7429532418336404
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.13558669090271,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6043596800168356,
                "rejected_mean_error": 2.1782741594314574,
                "gap_rejected_minus_accepted": 0.5739144794146218
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.913895606994629,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5282122601162305,
                "rejected_mean_error": 2.0581284023466564,
                "gap_rejected_minus_accepted": 0.5299161422304259
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7383914589881897,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3787611594200135,
                "rejected_mean_error": 1.9447410964965821,
                "gap_rejected_minus_accepted": 0.5659799370765686
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4995992183685303,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1110458667316134,
                "rejected_mean_error": 1.8472828469811913,
                "gap_rejected_minus_accepted": 0.7362369802495778
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
      "best_calib_loss": 0.013030100613832474,
      "train_time_sec": 56.42836618423462,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999828765922317,
            "spearman": 0.9990376524339762,
            "auroc_top30_bad": 0.9998581428571429,
            "mae": 0.017623231865512207,
            "mse": 0.0006672325523688666,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8000510772490518,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00019051821529865264
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1996788996875286
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185615236729384
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.98635498671333
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
            "pearson": 0.9997820776683864,
            "spearman": 0.9995025345800894,
            "auroc_top30_worst": 0.999868380952381,
            "pairwise_seed_ranking": 0.9689,
            "predicted_best_mean_error": 1.7025209807157518,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09190341690182668,
            "gap_to_oracle": 0.0009269329905510215,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7221561936736107
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8789745609998703
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.083841710269451
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051370938539506
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.120740962028504,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.489947269750966,
                "rejected_mean_error": 4.441455357074737,
                "gap_rejected_minus_accepted": 2.9515080873237713
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9958927929401398,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051370938539506,
                "rejected_mean_error": 3.224981032371521,
                "gap_rejected_minus_accepted": 1.9198439385175705
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.491639494895935,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.083841710269451,
                "rejected_mean_error": 2.486354446697235,
                "gap_rejected_minus_accepted": 1.402512736427784
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0774067640304565,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8789745609998703,
                "rejected_mean_error": 2.087139250977834,
                "gap_rejected_minus_accepted": 1.208164689977964
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.177073121070862,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.997833013534546,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019762820005416,
                "rejected_mean_error": 3.271768744468689,
                "gap_rejected_minus_accepted": 1.9697924624681475
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4952847957611084,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0765085473656655,
                "rejected_mean_error": 2.5123402478694916,
                "gap_rejected_minus_accepted": 1.4358317005038261
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.062663495540619,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8667286311388016,
                "rejected_mean_error": 2.103656319777171,
                "gap_rejected_minus_accepted": 1.2369276886383693
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.99016747344871,
            "spearman": 0.9839896819128198,
            "auroc_top30_bad": 0.9923832380952381,
            "mae": 0.1246657043427229,
            "mse": 0.028268571949103084,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9055334668775337,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07091456019878388
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2005058251142502
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5858312985062599
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0189474560817082
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
            "pearson": 0.9916514155704491,
            "spearman": 0.9910620532877141,
            "auroc_top30_worst": 0.9991588571428571,
            "pairwise_seed_ranking": 0.9284,
            "predicted_best_mean_error": 1.9925192894935608,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11196171522140519,
            "gap_to_oracle": 0.00362405979633329,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6262247369289399
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8668433503271677
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.22667496676445
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5523692088277101
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.230039024353028,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8415573924117619,
                "rejected_mean_error": 4.224966705322266,
                "gap_rejected_minus_accepted": 2.383409312910504
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.770632803440094,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5507475651379201,
                "rejected_mean_error": 3.663969444390684,
                "gap_rejected_minus_accepted": 2.113221879252764
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7953163385391235,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.22667496676445,
                "rejected_mean_error": 2.9331216806411744,
                "gap_rejected_minus_accepted": 1.7064467138767243
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2198578417301178,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8686060919738806,
                "rejected_mean_error": 2.4845242239495096,
                "gap_rejected_minus_accepted": 1.6159181319756288
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.294408464431763,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.864661266538832,
                "rejected_mean_error": 4.2628586483001705,
                "gap_rejected_minus_accepted": 2.3981973817613387
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.856270670890808,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5584959894578088,
                "rejected_mean_error": 3.7251031928592258,
                "gap_rejected_minus_accepted": 2.166607203401417
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8050827980041504,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2288757400512695,
                "rejected_mean_error": 2.980086269378662,
                "gap_rejected_minus_accepted": 1.7512105293273925
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.251103013753891,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8679434117816743,
                "rejected_mean_error": 2.5210685360240426,
                "gap_rejected_minus_accepted": 1.6531251242423681
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9912091029338931,
            "spearman": 0.9850189433869293,
            "auroc_top30_bad": 0.9858666666666667,
            "mae": 0.08508591056577862,
            "mse": 0.015049094306143488,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7816296933609187,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.042336971819400784
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1863655070781708
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6306939487814903
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0415288114150365
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
            "pearson": 0.9880193315720709,
            "spearman": 0.9771644699932609,
            "auroc_top30_worst": 0.9713219047619048,
            "pairwise_seed_ranking": 0.8988,
            "predicted_best_mean_error": 1.5880137555599212,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06912938690185544,
            "gap_to_oracle": 0.008116234064102112,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.42729075503349306
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6557141565359556
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0346164969444276
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3091359849550577
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.639935183525086,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.458654379579756,
                "rejected_mean_error": 3.3418752918243406,
                "gap_rejected_minus_accepted": 1.8832209122445847
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.989613801240921,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.308306258859604,
                "rejected_mean_error": 2.660823079724662,
                "gap_rejected_minus_accepted": 1.3525168208650582
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6877749562263489,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0346164969444276,
                "rejected_mean_error": 2.2593364446640014,
                "gap_rejected_minus_accepted": 1.2247199477195738
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.093347191810608,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6570965794328684,
                "rejected_mean_error": 1.9776407248055285,
                "gap_rejected_minus_accepted": 1.32054414537266
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.752732038497925,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4640148658222623,
                "rejected_mean_error": 3.395297632217407,
                "gap_rejected_minus_accepted": 1.9312827663951448
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.002233147621155,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3053038735440707,
                "rejected_mean_error": 2.701491448614332,
                "gap_rejected_minus_accepted": 1.3961875750702615
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7054396867752075,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0266126942634584,
                "rejected_mean_error": 2.2876735906600953,
                "gap_rejected_minus_accepted": 1.261060896396637
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0623320639133453,
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
            "pearson": 0.9838767733869199,
            "spearman": 0.976382210841634,
            "auroc_top30_bad": 0.9800342857142856,
            "mae": 0.10326678625643253,
            "mse": 0.022437844742950228,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7040834417452579,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06260176491737365
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2274225089788437
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7864957997322083
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1385560762405396
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
            "pearson": 0.9602833004447016,
            "spearman": 0.9461919440588443,
            "auroc_top30_worst": 0.9640380952380952,
            "pairwise_seed_ranking": 0.8936,
            "predicted_best_mean_error": 1.597915964603424,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06383516335487371,
            "gap_to_oracle": 0.005892032623290966,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8538018763065338
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.103716082011278
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3643279163837432
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5201857252987718
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.119883680343628,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5941942922009362,
                "rejected_mean_error": 2.250384338378906,
                "gap_rejected_minus_accepted": 0.6561900461779699
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9683522880077362,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5197989374812664,
                "rejected_mean_error": 2.0789617143880825,
                "gap_rejected_minus_accepted": 0.5591627769068162
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7260261178016663,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3643279163837432,
                "rejected_mean_error": 1.955298677253723,
                "gap_rejected_minus_accepted": 0.5909707608699799
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4563176035881042,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.104995970623181,
                "rejected_mean_error": 1.8451471528477705,
                "gap_rejected_minus_accepted": 0.7401511822245896
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.120860457420349,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5998626854684619,
                "rejected_mean_error": 2.2187471103668215,
                "gap_rejected_minus_accepted": 0.6188844248983596
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9640149474143982,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5279139340880084,
                "rejected_mean_error": 2.05901390976376,
                "gap_rejected_minus_accepted": 0.5310999756757517
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7443289756774902,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3743622364997863,
                "rejected_mean_error": 1.9491400194168091,
                "gap_rejected_minus_accepted": 0.5747777829170229
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4762423038482666,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1126631564564176,
                "rejected_mean_error": 1.8467379846674874,
                "gap_rejected_minus_accepted": 0.7340748282110698
              }
            ]
          }
        }
      }
    }
  ]
}
```
