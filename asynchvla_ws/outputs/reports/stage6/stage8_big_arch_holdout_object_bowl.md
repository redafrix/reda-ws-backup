# Stage 6 Experiments: holdout_object_bowl

```json
{
  "split": "holdout_object_bowl",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 103,
      "best_calib_loss": 0.09109630435705185,
      "train_time_sec": 22.339964151382446,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8758989310199532,
            "spearman": 0.8295583768786965,
            "auroc_top30_bad": 0.9057603571428572,
            "mae": 0.19286654993146657,
            "mse": 0.2005319508556488,
            "expert_lt_perturb_large": 0.986,
            "expert_lt_other_task": 0.573,
            "expert_lt_simvla_seed0": 0.977,
            "same_context_pred_std": 0.7241888346826466,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4676465109288693
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.49752523937821386
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6730616976767778
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9533292764604092
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
            "pearson": 0.9978478587780855,
            "spearman": 0.9969847170632437,
            "auroc_top30_worst": 0.9990314285714286,
            "pairwise_seed_ranking": 0.8783,
            "predicted_best_mean_error": 1.5354993950128555,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08010893300175681,
            "gap_to_oracle": 0.006640160828828678,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6709973827004433
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8094825779676438
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0110101581931115
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2418051582256953
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7318841934204103,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4057661659651333,
                "rejected_mean_error": 3.4558923783302307,
                "gap_rejected_minus_accepted": 2.0501262123650976
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9666448831558228,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2418051582256953,
                "rejected_mean_error": 2.717699674129486,
                "gap_rejected_minus_accepted": 1.4758945159037908
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.420054852962494,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0110101581931115,
                "rejected_mean_error": 2.2105474162101744,
                "gap_rejected_minus_accepted": 1.199537258017063
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0284923613071442,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8094825779676438,
                "rejected_mean_error": 1.877877523612976,
                "gap_rejected_minus_accepted": 1.0683949456453323
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7476591348648074,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106468056639037,
                "rejected_mean_error": 3.46026202917099,
                "gap_rejected_minus_accepted": 2.049615223507086
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9837388396263123,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2436153630018234,
                "rejected_mean_error": 2.7315872230529785,
                "gap_rejected_minus_accepted": 1.4879718600511551
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4318518042564392,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0045208070874214,
                "rejected_mean_error": 2.226695848941803,
                "gap_rejected_minus_accepted": 1.2221750418543815
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0311076045036316,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8018290807008743,
                "rejected_mean_error": 1.8868680771191915,
                "gap_rejected_minus_accepted": 1.0850389964183171
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.5361001767551101,
            "spearman": 0.5014863759581027,
            "auroc_top30_bad": 0.6668125714285713,
            "mae": 0.46651372636556626,
            "mse": 0.5370381428909928,
            "expert_lt_perturb_large": 0.968,
            "expert_lt_other_task": 0.472,
            "expert_lt_simvla_seed0": 0.956,
            "same_context_pred_std": 0.6573061998023361,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5983043714761734
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7967463047027588
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9398364935278892
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1662936970790228
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
            "pearson": 0.44130095639197164,
            "spearman": 0.5000787676664114,
            "auroc_top30_worst": 0.7343055238095237,
            "pairwise_seed_ranking": 0.744,
            "predicted_best_mean_error": 1.4866766386032104,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.04211718511581419,
            "gap_to_oracle": 0.023833616495132492,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9675145244598389
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.171105570709094
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3413044914245607
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4698027778408929
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.110751986503601,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.522193906095293,
                "rejected_mean_error": 1.665238461971283,
                "gap_rejected_minus_accepted": 0.14304455587599008
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.829653948545456,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4694327246417613,
                "rejected_mean_error": 1.7372667383842957,
                "gap_rejected_minus_accepted": 0.26783401374253435
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.548096776008606,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3413044914245607,
                "rejected_mean_error": 1.7316922319412231,
                "gap_rejected_minus_accepted": 0.3903877405166625
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2692965269088745,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1704552906770676,
                "rejected_mean_error": 1.6587731548790743,
                "gap_rejected_minus_accepted": 0.48831786420200674
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1109950304031373,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5131148121092055,
                "rejected_mean_error": 1.6699049282073974,
                "gap_rejected_minus_accepted": 0.15679011609819193
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8205818235874176,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.468755492552079,
                "rejected_mean_error": 1.707002838452657,
                "gap_rejected_minus_accepted": 0.23824734590057806
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5645779371261597,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3279557056427003,
                "rejected_mean_error": 1.7296319417953492,
                "gap_rejected_minus_accepted": 0.4016762361526489
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2514347732067108,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1643937807234506,
                "rejected_mean_error": 1.6515596136052342,
                "gap_rejected_minus_accepted": 0.4871658328817836
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.5232269379695613,
            "spearman": 0.45680327696202355,
            "auroc_top30_bad": 0.6178262857142858,
            "mae": 0.6015528596818447,
            "mse": 0.69284135940407,
            "expert_lt_perturb_large": 0.936,
            "expert_lt_other_task": 0.488,
            "expert_lt_simvla_seed0": 0.908,
            "same_context_pred_std": 0.6430207954696481,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5660231556892396
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5585778404951096
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0607199452996254
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3177699805339178
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
            "pearson": 0.2270222054042029,
            "spearman": 0.1307415067785644,
            "auroc_top30_worst": 0.44211809523809525,
            "pairwise_seed_ranking": 0.71,
            "predicted_best_mean_error": 1.752852373957634,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.05429620742797847,
            "gap_to_oracle": 0.02896557378768927,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.4810246903896331
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.5964239083994658
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.8190983769416809
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7992873444740198
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.685227417945862,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7458021105660333,
                "rejected_mean_error": 2.312376879692078,
                "gap_rejected_minus_accepted": 0.5665747691260445
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8460036218166351,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.799842676459916,
                "rejected_mean_error": 1.8102935990586448,
                "gap_rejected_minus_accepted": 0.010450922598728818
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.467463493347168,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.8190983769416809,
                "rejected_mean_error": 1.7858207980155945,
                "gap_rejected_minus_accepted": -0.033277578926086404
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.188632756471634,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.594550931510834,
                "rejected_mean_error": 1.8719103978499532,
                "gap_rejected_minus_accepted": 0.27735946633911923
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.641921520233154,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7481526039706337,
                "rejected_mean_error": 2.3381123781204223,
                "gap_rejected_minus_accepted": 0.5899597741497886
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8692361414432526,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.8008172733579728,
                "rejected_mean_error": 1.8259415115628923,
                "gap_rejected_minus_accepted": 0.02512423820491949
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4718735814094543,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8300679590702056,
                "rejected_mean_error": 1.7842292037010192,
                "gap_rejected_minus_accepted": -0.04583875536918636
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1904844641685486,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.6460808586506617,
                "rejected_mean_error": 1.8614120387776012,
                "gap_rejected_minus_accepted": 0.21533118012693953
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6377790021971961,
            "spearman": 0.6018308562917524,
            "auroc_top30_bad": 0.7998182857142857,
            "mae": 0.46394342351555823,
            "mse": 0.47619979396382806,
            "expert_lt_perturb_large": 0.972,
            "expert_lt_other_task": 0.544,
            "expert_lt_simvla_seed0": 0.968,
            "same_context_pred_std": 0.7055648481706964,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6838217886090279
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7158139274120331
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8362569177269935
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0304947882811228
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
            "pearson": 0.6849275958567042,
            "spearman": 0.5876953480290228,
            "auroc_top30_worst": 0.8650575238095238,
            "pairwise_seed_ranking": 0.762,
            "predicted_best_mean_error": 1.5672489000558854,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.05207337820529934,
            "gap_to_oracle": 0.01610563981533053,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7313745572566986
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1371454452283871
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2907001401424407
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4189953973997376
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.47136836051941,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.517520294798745,
                "rejected_mean_error": 2.572420692920685,
                "gap_rejected_minus_accepted": 1.05490039812194
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9132300317287445,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.419733886307815,
                "rejected_mean_error": 2.2315407884768406,
                "gap_rejected_minus_accepted": 0.8118069021690255
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6583545207977295,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2907001401424407,
                "rejected_mean_error": 1.9553205290794373,
                "gap_rejected_minus_accepted": 0.6646203889369966
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3339709639549255,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1381254680811788,
                "rejected_mean_error": 1.7849836144655975,
                "gap_rejected_minus_accepted": 0.6468581463844187
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.497754669189453,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5170027671919928,
                "rejected_mean_error": 2.540197877883911,
                "gap_rejected_minus_accepted": 1.0231951106919182
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9241746962070465,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.399800219637825,
                "rejected_mean_error": 2.270919499889253,
                "gap_rejected_minus_accepted": 0.8711192802514278
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6587049961090088,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2577567167282104,
                "rejected_mean_error": 1.980887839794159,
                "gap_rejected_minus_accepted": 0.7231311230659485
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3282816410064697,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0773312298078386,
                "rejected_mean_error": 1.8019181929807613,
                "gap_rejected_minus_accepted": 0.7245869631729227
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
      "best_epoch": 155,
      "best_calib_loss": 0.023372100666165352,
      "train_time_sec": 28.42845129966736,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993640986082482,
            "spearman": 0.9982538345034893,
            "auroc_top30_bad": 0.9993678571428571,
            "mae": 0.022531041043765434,
            "mse": 0.0010182914685120243,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7418759014023019,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.005968358725309372
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19778646628856658
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5742076643705368
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9269622966448466
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
            "pearson": 0.9994821265810744,
            "spearman": 0.9990232660089304,
            "auroc_top30_worst": 0.9995542857142856,
            "pairwise_seed_ranking": 0.9402,
            "predicted_best_mean_error": 1.5304192120432853,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08518911597132695,
            "gap_to_oracle": 0.0015599778592585434,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6654182786345482
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8073461615800858
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0102137178778647
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2414430283466975
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.75691478252411,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056698287526765,
                "rejected_mean_error": 3.4567594132423403,
                "gap_rejected_minus_accepted": 2.051089584489664
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9638230502605438,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2414430283466975,
                "rejected_mean_error": 2.7187860637664794,
                "gap_rejected_minus_accepted": 1.4773430354197818
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4043540954589844,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0102137178778647,
                "rejected_mean_error": 2.211343856525421,
                "gap_rejected_minus_accepted": 1.2011301386475564
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0214552879333496,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8073461615800858,
                "rejected_mean_error": 1.8785896624088287,
                "gap_rejected_minus_accepted": 1.0712435008287429
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8040873527526857,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106084573600026,
                "rejected_mean_error": 3.4606071639060976,
                "gap_rejected_minus_accepted": 2.049998706546095
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9749624133110046,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2432007658084234,
                "rejected_mean_error": 2.7328310146331787,
                "gap_rejected_minus_accepted": 1.4896302488247553
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4180578589439392,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0040836127400399,
                "rejected_mean_error": 2.2271330432891845,
                "gap_rejected_minus_accepted": 1.2230494305491446
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0197247564792633,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7995144659280777,
                "rejected_mean_error": 1.8876396153767903,
                "gap_rejected_minus_accepted": 1.0881251494487125
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9579187428654956,
            "spearman": 0.9487608195974387,
            "auroc_top30_bad": 0.9503504761904762,
            "mae": 0.1809961963887792,
            "mse": 0.05825581850893243,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.59805448646329,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11983353674411773
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.25739653360843656
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6968115191817283
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0497123452742894
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
            "pearson": 0.9114909849488542,
            "spearman": 0.905807412356744,
            "auroc_top30_worst": 0.9256685714285714,
            "pairwise_seed_ranking": 0.8328,
            "predicted_best_mean_error": 1.4719017395973206,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.05689208412170399,
            "gap_to_oracle": 0.009058717489242696,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8984169239997863
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.023272532492112
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1914547550201415
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3785188450996302
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.104375743865967,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4609257541232639,
                "rejected_mean_error": 2.2166518297195434,
                "gap_rejected_minus_accepted": 0.7557260755962796
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8644803762435913,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3775892505778065,
                "rejected_mean_error": 2.012210301316965,
                "gap_rejected_minus_accepted": 0.6346210507391588
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5773473978042603,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1914547550201415,
                "rejected_mean_error": 1.881541968345642,
                "gap_rejected_minus_accepted": 0.6900872133255005
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.298188328742981,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0231603669663207,
                "rejected_mean_error": 1.7079762617322907,
                "gap_rejected_minus_accepted": 0.6848158947659699
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.134317326545715,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4546510728200277,
                "rejected_mean_error": 2.1960785818099975,
                "gap_rejected_minus_accepted": 0.7414275089899698
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8647615015506744,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.366511731224264,
                "rejected_mean_error": 2.010488288743155,
                "gap_rejected_minus_accepted": 0.6439765575188912
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.574423611164093,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1823094758987427,
                "rejected_mean_error": 1.8752781715393065,
                "gap_rejected_minus_accepted": 0.6929686956405638
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2927489280700684,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0033398535516527,
                "rejected_mean_error": 1.7058184232941285,
                "gap_rejected_minus_accepted": 0.7024785697424758
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9530908625581838,
            "spearman": 0.9539856362843097,
            "auroc_top30_bad": 0.9694727619047618,
            "mae": 0.20491311087049544,
            "mse": 0.08653784960611849,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.956,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6849278659602971,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11637561684846878
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2582807027101517
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7125379114985466
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0608128600358964
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
            "pearson": 0.952845770422674,
            "spearman": 0.9384230476947507,
            "auroc_top30_worst": 0.9898300952380953,
            "pairwise_seed_ranking": 0.8796,
            "predicted_best_mean_error": 1.7291489502191544,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.07799963116645814,
            "gap_to_oracle": 0.005262150049209602,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0006689376831055
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1589877678033633
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2947572153091431
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4565846257880806
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6795577287673953,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.66362050014072,
                "rejected_mean_error": 3.0520113735198975,
                "gap_rejected_minus_accepted": 1.3883908733791774
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3964913487434387,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4560140611776802,
                "rejected_mean_error": 2.8395824569482775,
                "gap_rejected_minus_accepted": 1.3835683957705973
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6864639520645142,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2947572153091431,
                "rejected_mean_error": 2.3101619596481324,
                "gap_rejected_minus_accepted": 1.0154047443389893
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4673353731632233,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.159764067814373,
                "rejected_mean_error": 2.0171486991701157,
                "gap_rejected_minus_accepted": 0.8573846313557427
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6916813611984254,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.667436159849167,
                "rejected_mean_error": 3.064560375213623,
                "gap_rejected_minus_accepted": 1.397124215364456
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.436154782772064,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4545739422188724,
                "rejected_mean_error": 2.8536796531979998,
                "gap_rejected_minus_accepted": 1.3991057109791274
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6772741079330444,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2927669599056244,
                "rejected_mean_error": 2.3215302028656004,
                "gap_rejected_minus_accepted": 1.028763242959976
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.457425832748413,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1515452365080516,
                "rejected_mean_error": 2.0280202965047907,
                "gap_rejected_minus_accepted": 0.876475059996739
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9654326522593747,
            "spearman": 0.9599424574312095,
            "auroc_top30_bad": 0.9715253333333334,
            "mae": 0.18064756927381967,
            "mse": 0.0570798320780558,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6431375714495317,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11955378252267837
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23481983869075776
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6039435782432556
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9481127212524414
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
            "pearson": 0.9655805191312925,
            "spearman": 0.9533493830076052,
            "auroc_top30_worst": 0.9888579047619048,
            "pairwise_seed_ranking": 0.89,
            "predicted_best_mean_error": 1.5567494105100632,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06257286775112147,
            "gap_to_oracle": 0.005606150269508392,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5951800501346588
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8931921415795119
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1239292383670807
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3151174184165275
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.804318976402283,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4751220796638065,
                "rejected_mean_error": 2.954004629135132,
                "gap_rejected_minus_accepted": 1.4788825494713254
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1957440972328186,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3146860683804007,
                "rejected_mean_error": 2.54601301019565,
                "gap_rejected_minus_accepted": 1.2313269418152493
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.696453869342804,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1239292383670807,
                "rejected_mean_error": 2.1220914308547973,
                "gap_rejected_minus_accepted": 0.9981621924877166
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2821004688739777,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8949271479544167,
                "rejected_mean_error": 1.866222754486597,
                "gap_rejected_minus_accepted": 0.9712956065321803
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7896108388900758,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4686131861474778,
                "rejected_mean_error": 2.975704107284546,
                "gap_rejected_minus_accepted": 1.5070909211370682
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1933408975601196,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3002102716083832,
                "rejected_mean_error": 2.5665277583258495,
                "gap_rejected_minus_accepted": 1.2663174867174662
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6632678508758545,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1123952116966247,
                "rejected_mean_error": 2.1262493448257445,
                "gap_rejected_minus_accepted": 1.0138541331291198
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2852958142757416,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8677735962564983,
                "rejected_mean_error": 1.872517823535491,
                "gap_rejected_minus_accepted": 1.0047442272789926
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
      "best_epoch": 145,
      "best_calib_loss": 0.005790023598819971,
      "train_time_sec": 66.81144452095032,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997899317707364,
            "spearman": 0.999101021383978,
            "auroc_top30_bad": 0.9998792857142856,
            "mae": 0.013325643174862489,
            "mse": 0.00034130699049039976,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7426209366691018,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0004389982670545578
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19773876986503602
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5739621668100358
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9267034301916758
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
            "pearson": 0.9997494557680048,
            "spearman": 0.9996126610085063,
            "auroc_top30_worst": 0.9999333333333333,
            "pairwise_seed_ranking": 0.9632,
            "predicted_best_mean_error": 1.5298499281406404,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08575839987397194,
            "gap_to_oracle": 0.000990693956613553,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6653445045351982
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8069355354070663
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0100626212477684
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2412889313936233
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7336942911148103,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056614204711384,
                "rejected_mean_error": 3.456835087776184,
                "gap_rejected_minus_accepted": 2.0511736673050454
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.968848556280136,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2412889313936233,
                "rejected_mean_error": 2.719248354625702,
                "gap_rejected_minus_accepted": 1.4779594232320787
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.411128580570221,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0100626212477684,
                "rejected_mean_error": 2.2114949531555177,
                "gap_rejected_minus_accepted": 1.2014323319077493
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.025757521390915,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8069355354070663,
                "rejected_mean_error": 1.8787265377998352,
                "gap_rejected_minus_accepted": 1.0717910023927688
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.775678038597107,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.410628084242344,
                "rejected_mean_error": 3.460430521965027,
                "gap_rejected_minus_accepted": 2.0498024377226827
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.98420912027359,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2430162887970606,
                "rejected_mean_error": 2.7333844456672667,
                "gap_rejected_minus_accepted": 1.490368156870206
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4177842140197754,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.003780542910099,
                "rejected_mean_error": 2.227436113119125,
                "gap_rejected_minus_accepted": 1.2236555702090262
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0255109667778015,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7987997950315475,
                "rejected_mean_error": 1.887877839008967,
                "gap_rejected_minus_accepted": 1.0890780439774195
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9897847053914238,
            "spearman": 0.9868703586974794,
            "auroc_top30_bad": 0.9894232380952381,
            "mae": 0.07696146207060665,
            "mse": 0.012509118600654207,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7028340648376818,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04815576243400574
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2281100177049637
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6789940522551536
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0343381548802058
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
            "pearson": 0.9824033639508305,
            "spearman": 0.9814002384641527,
            "auroc_top30_worst": 0.9886567619047619,
            "pairwise_seed_ranking": 0.89,
            "predicted_best_mean_error": 1.4693671131134034,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.059426710605621214,
            "gap_to_oracle": 0.006524091005325472,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8786913919448852
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9777626486924978
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1693513980865478
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3582817645215277
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1077397584915163,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4555616466734145,
                "rejected_mean_error": 2.2649287967681886,
                "gap_rejected_minus_accepted": 0.8093671500947741
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.93086838722229,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3577692077406698,
                "rejected_mean_error": 2.0715437841872437,
                "gap_rejected_minus_accepted": 0.7137745764465739
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5363957285881042,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1693513980865478,
                "rejected_mean_error": 1.9036453252792358,
                "gap_rejected_minus_accepted": 0.734293927192688
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1733140647411346,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9782195114099179,
                "rejected_mean_error": 1.722988521912818,
                "gap_rejected_minus_accepted": 0.7447690105029001
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.105724024772644,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4486772955788507,
                "rejected_mean_error": 2.249842576980591,
                "gap_rejected_minus_accepted": 0.8011652814017403
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9307244718074799,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3477918744724702,
                "rejected_mean_error": 2.066053577831813,
                "gap_rejected_minus_accepted": 0.718261703359343
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5266752243041992,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1577787742614747,
                "rejected_mean_error": 1.8998088731765748,
                "gap_rejected_minus_accepted": 0.7420300989151001
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2045786380767822,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9598667772989424,
                "rejected_mean_error": 1.7204644329407637,
                "gap_rejected_minus_accepted": 0.7605976556418212
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9700096487519745,
            "spearman": 0.9767500485633891,
            "auroc_top30_bad": 0.9851215238095238,
            "mae": 0.15261654602512717,
            "mse": 0.05850399300641072,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7089990026327864,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08214588356018067
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2044758495092392
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6927486904025077
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0511652836402257
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
            "pearson": 0.9334194434204657,
            "spearman": 0.9675861276071217,
            "auroc_top30_worst": 0.9824152380952381,
            "pairwise_seed_ranking": 0.924,
            "predicted_best_mean_error": 1.7262624462842941,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08088613510131837,
            "gap_to_oracle": 0.0023756461143493723,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9451961126327515
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.111170049279164
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2990404754638671
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4601152187217272
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2138318777084356,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6537522532145181,
                "rejected_mean_error": 3.1408255958557127,
                "gap_rejected_minus_accepted": 1.4870733426411946
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.904569685459137,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4595755172004823,
                "rejected_mean_error": 2.828920845787365,
                "gap_rejected_minus_accepted": 1.3693453285868828
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6465439200401306,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2990404754638671,
                "rejected_mean_error": 2.3058786994934084,
                "gap_rejected_minus_accepted": 1.0068382240295413
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3853531181812286,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1123700869350006,
                "rejected_mean_error": 2.032980413167174,
                "gap_rejected_minus_accepted": 0.9206103262321734
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.222471070289612,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.654941863881217,
                "rejected_mean_error": 3.177009038925171,
                "gap_rejected_minus_accepted": 1.522067175043954
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9361867010593414,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4575991131723884,
                "rejected_mean_error": 2.8447001775105796,
                "gap_rejected_minus_accepted": 1.3871010643381911
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6404139399528503,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2948709075450897,
                "rejected_mean_error": 2.3194262552261353,
                "gap_rejected_minus_accepted": 1.0245553476810456
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.390651524066925,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1131214012229254,
                "rejected_mean_error": 2.0409652249698333,
                "gap_rejected_minus_accepted": 0.927843823746908
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.990681200165547,
            "spearman": 0.9900802689956604,
            "auroc_top30_bad": 0.9962011428571429,
            "mae": 0.08181677217483521,
            "mse": 0.014892762305854186,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7407712997610206,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04944271320104599
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19849177341461183
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.588513161277771
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9331578113555908
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
            "pearson": 0.9842078951455294,
            "spearman": 0.98754689046201,
            "auroc_top30_worst": 0.9972053333333333,
            "pairwise_seed_ranking": 0.9252,
            "predicted_best_mean_error": 1.5551206340789796,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06420164418220509,
            "gap_to_oracle": 0.00397737383842478,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5684206440448761
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8680824680397143
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1162967613697052
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.311404806369149
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6511842489242556,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4771300409369998,
                "rejected_mean_error": 2.9359329776763916,
                "gap_rejected_minus_accepted": 1.4588029367393918
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0197887420654297,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.310525345477885,
                "rejected_mean_error": 2.5584685928143633,
                "gap_rejected_minus_accepted": 1.2479432473364784
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5451071858406067,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1162967613697052,
                "rejected_mean_error": 2.129723907852173,
                "gap_rejected_minus_accepted": 1.0134271464824676
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2821696996688843,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8694796502209319,
                "rejected_mean_error": 1.8747233593858292,
                "gap_rejected_minus_accepted": 1.0052437091648974
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6280009269714353,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4691338721911114,
                "rejected_mean_error": 2.971017932891846,
                "gap_rejected_minus_accepted": 1.5018840607007344
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.011791706085205,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2979737759273957,
                "rejected_mean_error": 2.573166245505923,
                "gap_rejected_minus_accepted": 1.2751924695785275
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.575015664100647,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1036189541816712,
                "rejected_mean_error": 2.1350256023406984,
                "gap_rejected_minus_accepted": 1.0314066481590272
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2742173373699188,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.856193689126817,
                "rejected_mean_error": 1.8764190756700894,
                "gap_rejected_minus_accepted": 1.0202253865432724
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
      "best_epoch": 101,
      "best_calib_loss": 0.010531432926654816,
      "train_time_sec": 70.0245726108551,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996553003180718,
            "spearman": 0.9987727037079236,
            "auroc_top30_bad": 0.9996494761904762,
            "mae": 0.017888050055825225,
            "mse": 0.0006031599390583425,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7395825127182356,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.001206660494208336
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19771282260417938
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5740197159528733
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9267608301003774
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
            "pearson": 0.9995753022677857,
            "spearman": 0.9993063048841856,
            "auroc_top30_worst": 0.9996053333333333,
            "pairwise_seed_ranking": 0.9631,
            "predicted_best_mean_error": 1.5300064297020435,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08560189831256881,
            "gap_to_oracle": 0.0011471955180166749,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6652590875029564
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8071887591600418
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0101971409678459
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.241317932597796
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7626330375671406,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056868469119073,
                "rejected_mean_error": 3.456606249809265,
                "gap_rejected_minus_accepted": 2.0509194028973576
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9654632210731506,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.241317932597796,
                "rejected_mean_error": 2.7191613510131836,
                "gap_rejected_minus_accepted": 1.4778434184153875
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4022518992424011,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0101971409678459,
                "rejected_mean_error": 2.21136043343544,
                "gap_rejected_minus_accepted": 1.2011632924675941
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.024032473564148,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8071887591600418,
                "rejected_mean_error": 1.8786421298821767,
                "gap_rejected_minus_accepted": 1.0714533707221348
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8003406047821047,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106561736596954,
                "rejected_mean_error": 3.4601777172088624,
                "gap_rejected_minus_accepted": 2.049521543549167
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9849151372909546,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2431224934657414,
                "rejected_mean_error": 2.733065831661224,
                "gap_rejected_minus_accepted": 1.4899433381954827
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4124895930290222,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0037828736901284,
                "rejected_mean_error": 2.227433782339096,
                "gap_rejected_minus_accepted": 1.2236509086489678
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.008464515209198,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7990222312211991,
                "rejected_mean_error": 1.8878036936124165,
                "gap_rejected_minus_accepted": 1.0887814623912173
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9789276369849125,
            "spearman": 0.9803397234388249,
            "auroc_top30_bad": 0.9876822857142856,
            "mae": 0.1065498894635738,
            "mse": 0.024925089936247244,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6650005853985486,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07429023557901382
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23890427038669587
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6817690382361412
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0343966258605322
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
            "pearson": 0.9665472114584953,
            "spearman": 0.9739909629382164,
            "auroc_top30_worst": 0.9848655238095239,
            "pairwise_seed_ranking": 0.8836,
            "predicted_best_mean_error": 1.4669427459239959,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06185107779502874,
            "gap_to_oracle": 0.004099723815917944,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8917465205192566
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.981206863354414
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.17246729927063
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3603090068170511
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.063353157043457,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4595523453818426,
                "rejected_mean_error": 2.229012508392334,
                "gap_rejected_minus_accepted": 0.7694601630104914
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.874321311712265,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3594815331563879,
                "rejected_mean_error": 2.0664177493165474,
                "gap_rejected_minus_accepted": 0.7069362161601596
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4677807688713074,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.17246729927063,
                "rejected_mean_error": 1.9005294240951538,
                "gap_rejected_minus_accepted": 0.7280621248245238
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.108772486448288,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.982250925451041,
                "rejected_mean_error": 1.7216418489193586,
                "gap_rejected_minus_accepted": 0.7393909234683176
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0919973373413088,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.455781651602851,
                "rejected_mean_error": 2.1859033727645873,
                "gap_rejected_minus_accepted": 0.7301217211617363
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8607540428638458,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3508383953635068,
                "rejected_mean_error": 2.0570107301076255,
                "gap_rejected_minus_accepted": 0.7061723347441187
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4862261414527893,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1608103427886962,
                "rejected_mean_error": 1.896777304649353,
                "gap_rejected_minus_accepted": 0.7359669618606568
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.115404337644577,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9621805766272167,
                "rejected_mean_error": 1.7196849176590456,
                "gap_rejected_minus_accepted": 0.757504341031829
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9532381930549942,
            "spearman": 0.9624150990552462,
            "auroc_top30_bad": 0.9863299047619049,
            "mae": 0.18698257064181403,
            "mse": 0.09911894395497997,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6696867284767707,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10510318195819855
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2250068620443344
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.698948037803173
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0794228307644527
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
            "pearson": 0.8926645404881446,
            "spearman": 0.9436373962479336,
            "auroc_top30_worst": 0.9760975238095237,
            "pairwise_seed_ranking": 0.9208,
            "predicted_best_mean_error": 1.7270328220129012,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08011575937271131,
            "gap_to_oracle": 0.0031460218429564257,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9494120836257934
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1247697873757436
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2886864727020264
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5081926387256142
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.036100745201111,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6637239507039387,
                "rejected_mean_error": 3.0510803184509276,
                "gap_rejected_minus_accepted": 1.387356367746989
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.835922509431839,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5078072250207435,
                "rejected_mean_error": 2.684533912152909,
                "gap_rejected_minus_accepted": 1.1767266871321653
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.550746202468872,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2886864727020264,
                "rejected_mean_error": 2.316232702255249,
                "gap_rejected_minus_accepted": 1.0275462295532225
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3039998412132263,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1260934314027,
                "rejected_mean_error": 2.0283962009810588,
                "gap_rejected_minus_accepted": 0.9023027695783588
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.048179292678833,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6656186038917966,
                "rejected_mean_error": 3.080918378829956,
                "gap_rejected_minus_accepted": 1.4152997749381593
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8365300595760345,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5102529664409352,
                "rejected_mean_error": 2.688410168602353,
                "gap_rejected_minus_accepted": 1.178157202161418
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5438552498817444,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2855286729335784,
                "rejected_mean_error": 2.3287684898376466,
                "gap_rejected_minus_accepted": 1.0432398169040682
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3113706409931183,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1418345253618936,
                "rejected_mean_error": 2.0312918195112504,
                "gap_rejected_minus_accepted": 0.8894572941493568
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9871888199172916,
            "spearman": 0.984228915708229,
            "auroc_top30_bad": 0.9965699047619048,
            "mae": 0.09254505128665623,
            "mse": 0.021612407507541054,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7046501418748381,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05832511937618256
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2061720395565033
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5971004796981811
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9326345630009969
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
            "pearson": 0.9792427610626702,
            "spearman": 0.9610760086246456,
            "auroc_top30_worst": 0.9982262857142857,
            "pairwise_seed_ranking": 0.9052,
            "predicted_best_mean_error": 1.5554855345487595,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.0638367437124252,
            "gap_to_oracle": 0.004342274308204663,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6248284466266633
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8949806469564254
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1264508388996124
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3100117194944862
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.50242156982422,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4750022193325891,
                "rejected_mean_error": 2.9550833721160887,
                "gap_rejected_minus_accepted": 1.4800811527834996
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9273009896278381,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3093181876833437,
                "rejected_mean_error": 2.562082352729651,
                "gap_rejected_minus_accepted": 1.2527641650463073
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4103643298149109,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1264508388996124,
                "rejected_mean_error": 2.1195698303222654,
                "gap_rejected_minus_accepted": 0.993118991422653
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1856141984462738,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8958431391860731,
                "rejected_mean_error": 1.8659167723569188,
                "gap_rejected_minus_accepted": 0.9700736331708457
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4668972253799435,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4676686607466805,
                "rejected_mean_error": 2.9842048358917235,
                "gap_rejected_minus_accepted": 1.516536175145043
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9537169933319092,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2983499672961107,
                "rejected_mean_error": 2.572049613982912,
                "gap_rejected_minus_accepted": 1.2736996466868011
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.440359354019165,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.113684443950653,
                "rejected_mean_error": 2.124960112571716,
                "gap_rejected_minus_accepted": 1.011275668621063
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1746870577335358,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8864087708412655,
                "rejected_mean_error": 1.8662396631138847,
                "gap_rejected_minus_accepted": 0.9798308922726192
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
      "best_epoch": 139,
      "best_calib_loss": 0.008582995273172855,
      "train_time_sec": 79.24749255180359,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999110932526736,
            "spearman": 0.997707567113261,
            "auroc_top30_bad": 0.9993140476190475,
            "mae": 0.02821011659888427,
            "mse": 0.001556795829010586,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7482882152226209,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0019659763276576995
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19831783335208894
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5744777120113372
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.927071285311381
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
            "pearson": 0.9989935190275707,
            "spearman": 0.9980833100033323,
            "auroc_top30_worst": 0.9994767619047619,
            "pairwise_seed_ranking": 0.9663,
            "predicted_best_mean_error": 1.5305646212100983,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08504370680451401,
            "gap_to_oracle": 0.001705387026071481,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6679006133675576
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8077039134263992
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0104709687113762
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2415910261392593
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7908371210098273,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056619959606065,
                "rejected_mean_error": 3.4568299083709717,
                "gap_rejected_minus_accepted": 2.0511679124103654
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0038154125213623,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2415910261392593,
                "rejected_mean_error": 2.718342070388794,
                "gap_rejected_minus_accepted": 1.4767510442495348
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4207124710083008,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0104709687113762,
                "rejected_mean_error": 2.21108660569191,
                "gap_rejected_minus_accepted": 1.2006156369805336
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0182011425495148,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8077039134263992,
                "rejected_mean_error": 1.8784704117933908,
                "gap_rejected_minus_accepted": 1.0707664983669916
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8257747888565063,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106695878836844,
                "rejected_mean_error": 3.4600569891929625,
                "gap_rejected_minus_accepted": 2.049387401309278
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0186256170272827,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2434931157827378,
                "rejected_mean_error": 2.7319539647102355,
                "gap_rejected_minus_accepted": 1.4884608489274977
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4440205693244934,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0042474001049995,
                "rejected_mean_error": 2.226969255924225,
                "gap_rejected_minus_accepted": 1.2227218558192254
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0130582749843597,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7995720599889755,
                "rejected_mean_error": 1.887620417356491,
                "gap_rejected_minus_accepted": 1.0880483573675155
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9832278540569128,
            "spearman": 0.9815626160571214,
            "auroc_top30_bad": 0.9866400000000001,
            "mae": 0.09377242792195829,
            "mse": 0.019581840468817547,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6880171043038869,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05156395572423935
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2323892591714859
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6811256654143334
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0364578589359918
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
            "pearson": 0.9676985514685796,
            "spearman": 0.9723777256817445,
            "auroc_top30_worst": 0.9835398095238096,
            "pairwise_seed_ranking": 0.8868,
            "predicted_best_mean_error": 1.4678558585643768,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06093796515464778,
            "gap_to_oracle": 0.005012836456298908,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8799239983558654
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9792480999842669
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1709126817703248
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.361995000320711
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0703838348388675,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4618110048505994,
                "rejected_mean_error": 2.2086845731735227,
                "gap_rejected_minus_accepted": 0.7468735683229233
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8957422077655792,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3612543432282536,
                "rejected_mean_error": 2.0611106469608345,
                "gap_rejected_minus_accepted": 0.6998563037325809
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4871841669082642,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1709126817703248,
                "rejected_mean_error": 1.902084041595459,
                "gap_rejected_minus_accepted": 0.7311713598251341
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1265004575252533,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9797631875394632,
                "rejected_mean_error": 1.722472864891956,
                "gap_rejected_minus_accepted": 0.7427096773524928
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0938039779663087,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4568461275100708,
                "rejected_mean_error": 2.1763230895996095,
                "gap_rejected_minus_accepted": 0.7194769620895387
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9009613692760468,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3543508148448353,
                "rejected_mean_error": 2.0465849770439997,
                "gap_rejected_minus_accepted": 0.6922341621991643
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.487206220626831,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.159846767425537,
                "rejected_mean_error": 1.8977408800125122,
                "gap_rejected_minus_accepted": 0.7378941125869751
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1365202367305756,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.961644380811661,
                "rejected_mean_error": 1.719865561169099,
                "gap_rejected_minus_accepted": 0.7582211803574379
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9790954328323358,
            "spearman": 0.985428724711408,
            "auroc_top30_bad": 0.9943062857142858,
            "mae": 0.13819745344630718,
            "mse": 0.05077773790408368,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7099986298790283,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.080491763651371
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20724891650676727
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6926900255084038
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0496439567486444
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
            "pearson": 0.9669519293686831,
            "spearman": 0.984839346177895,
            "auroc_top30_worst": 0.9936182857142857,
            "pairwise_seed_ranking": 0.9288,
            "predicted_best_mean_error": 1.7260233465433121,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08112523484230039,
            "gap_to_oracle": 0.002136546373367354,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9383669700622559
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1100103656450908
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.285603903388977
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4606324645247795
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.29764301776886,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6497348200480144,
                "rejected_mean_error": 3.176982494354248,
                "gap_rejected_minus_accepted": 1.5272476743062335
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.001523733139038,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4600801579853004,
                "rejected_mean_error": 2.8274101479746663,
                "gap_rejected_minus_accepted": 1.3673299899893658
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5503363609313965,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.285603903388977,
                "rejected_mean_error": 2.3193152715682985,
                "gap_rejected_minus_accepted": 1.0337113681793215
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3130857646465302,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1105983820967018,
                "rejected_mean_error": 2.0335722419978968,
                "gap_rejected_minus_accepted": 0.922973859901195
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.299665117263794,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6506941613886092,
                "rejected_mean_error": 3.2152383613586424,
                "gap_rejected_minus_accepted": 1.5645441999700331
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0647026896476746,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4616600815306373,
                "rejected_mean_error": 2.832646192066253,
                "gap_rejected_minus_accepted": 1.3709861105356158
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5213780403137207,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2828318831920624,
                "rejected_mean_error": 2.3314652795791626,
                "gap_rejected_minus_accepted": 1.0486333963871002
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3045208752155304,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1097028042588915,
                "rejected_mean_error": 2.042116944802636,
                "gap_rejected_minus_accepted": 0.9324141405437447
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9915727803954946,
            "spearman": 0.9893549878814613,
            "auroc_top30_bad": 0.9957668571428572,
            "mae": 0.07983599621463182,
            "mse": 0.01413693827614287,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7079354266066354,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0711267671585083
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20183606328964232
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5891161389350891
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9327539920806884
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
            "pearson": 0.993254161175894,
            "spearman": 0.9876272540334428,
            "auroc_top30_worst": 0.9958857142857143,
            "pairwise_seed_ranking": 0.914,
            "predicted_best_mean_error": 1.5540538580417633,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06526842021942136,
            "gap_to_oracle": 0.002910597801208503,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5708653185367584
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8741886631991619
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.115807512140274
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.309413496015677
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5725396156311042,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4739072348541684,
                "rejected_mean_error": 2.964938232421875,
                "gap_rejected_minus_accepted": 1.4910309975677067
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.962790161371231,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3086257346348167,
                "rejected_mean_error": 2.5641552872551134,
                "gap_rejected_minus_accepted": 1.2555295526202968
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4362226128578186,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.115807512140274,
                "rejected_mean_error": 2.130213157081604,
                "gap_rejected_minus_accepted": 1.0144056449413301
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1672692000865936,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8752573992307193,
                "rejected_mean_error": 1.8727933322352814,
                "gap_rejected_minus_accepted": 0.9975359330045621
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5262868642807006,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4671877535184223,
                "rejected_mean_error": 2.988533000946045,
                "gap_rejected_minus_accepted": 1.5213452474276226
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9865899980068207,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2975750890645115,
                "rejected_mean_error": 2.5743496493687705,
                "gap_rejected_minus_accepted": 1.276774560304259
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.462584137916565,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.103007565021515,
                "rejected_mean_error": 2.1356369915008546,
                "gap_rejected_minus_accepted": 1.0326294264793396
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1692690253257751,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8519670121253483,
                "rejected_mean_error": 1.877843036371119,
                "gap_rejected_minus_accepted": 1.0258760242457705
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
      "best_epoch": 149,
      "best_calib_loss": 0.010129471309483051,
      "train_time_sec": 54.895349740982056,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996127110760124,
            "spearman": 0.9990338248206498,
            "auroc_top30_bad": 0.9996071428571429,
            "mae": 0.022556027980790715,
            "mse": 0.0013577539772770318,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7551381438742463,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19752738604545594
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5740060228109359
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9267746155579885
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
            "pearson": 0.9995008435787895,
            "spearman": 0.9994991236759407,
            "auroc_top30_worst": 0.9995470476190477,
            "pairwise_seed_ranking": 0.9743,
            "predicted_best_mean_error": 1.5293331331908704,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08627519482374191,
            "gap_to_oracle": 0.0004738990068435811,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6649441390633583
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8069544941663742
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0100729184508324
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.241400483059883
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.816012024879456,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.405700731297334,
                "rejected_mean_error": 3.4564812903404234,
                "gap_rejected_minus_accepted": 2.0507805590430896
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.00386905670166,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.241400483059883,
                "rejected_mean_error": 2.7189136996269228,
                "gap_rejected_minus_accepted": 1.4775132165670397
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4282180666923523,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0100729184508324,
                "rejected_mean_error": 2.2114846559524537,
                "gap_rejected_minus_accepted": 1.2014117375016213
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0370199978351593,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8069544941663742,
                "rejected_mean_error": 1.8787202182133993,
                "gap_rejected_minus_accepted": 1.071765724047025
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.854158806800842,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106278595990605,
                "rejected_mean_error": 3.4604325437545778,
                "gap_rejected_minus_accepted": 2.049804684155517
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0204252004623413,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2432756227254869,
                "rejected_mean_error": 2.7326064438819886,
                "gap_rejected_minus_accepted": 1.4893308211565017
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.433297038078308,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0037654088139534,
                "rejected_mean_error": 2.227451247215271,
                "gap_rejected_minus_accepted": 1.2236858384013178
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0265713036060333,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7989317737817764,
                "rejected_mean_error": 1.8878338460922242,
                "gap_rejected_minus_accepted": 1.0889020723104479
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9803881906662136,
            "spearman": 0.9801227113204322,
            "auroc_top30_bad": 0.9866979047619047,
            "mae": 0.10611192557099057,
            "mse": 0.02274382363456453,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6827363425125027,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05454333317279816
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23245474746227265
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6832774696707725
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0355317873239518
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
            "pearson": 0.9648173154079172,
            "spearman": 0.9705144643292574,
            "auroc_top30_worst": 0.9853988571428571,
            "pairwise_seed_ranking": 0.8936,
            "predicted_best_mean_error": 1.4674907071590424,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06130311655998222,
            "gap_to_oracle": 0.004647685050964467,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8896615610122681
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9815090753329105
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1741475917816162
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3603744267909004
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0537783384323123,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.461014502843221,
                "rejected_mean_error": 2.215853091239929,
                "gap_rejected_minus_accepted": 0.7548385883967079
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9014921188354492,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3598513178280858,
                "rejected_mean_error": 2.0653107581428065,
                "gap_rejected_minus_accepted": 0.7054594403147207
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.514738142490387,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1741475917816162,
                "rejected_mean_error": 1.8988491315841676,
                "gap_rejected_minus_accepted": 0.7247015398025514
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0976263284683228,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9819678338571859,
                "rejected_mean_error": 1.7217364142009772,
                "gap_rejected_minus_accepted": 0.7397685803437913
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0609220266342163,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4587864536709256,
                "rejected_mean_error": 2.1588601541519163,
                "gap_rejected_minus_accepted": 0.7000737004809907
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8998740017414093,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3514234356701693,
                "rejected_mean_error": 2.055274181895786,
                "gap_rejected_minus_accepted": 0.7038507462256165
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5186108350753784,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.166452000617981,
                "rejected_mean_error": 1.8911356468200684,
                "gap_rejected_minus_accepted": 0.7246836462020874
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0904732942581177,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9606306193366884,
                "rejected_mean_error": 1.720207095783662,
                "gap_rejected_minus_accepted": 0.7595764764469736
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9560183640961044,
            "spearman": 0.9605268573854442,
            "auroc_top30_bad": 0.9808167619047619,
            "mae": 0.17669101746213856,
            "mse": 0.09620883140172007,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6750956778378652,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08805509483814239
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20301661326885223
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6952711902499199
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0909510976076127
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
            "pearson": 0.8941920294588181,
            "spearman": 0.9451435312278601,
            "auroc_top30_worst": 0.9615451428571429,
            "pairwise_seed_ranking": 0.9268,
            "predicted_best_mean_error": 1.7263466814756394,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08080189990997311,
            "gap_to_oracle": 0.0024598813056946334,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.947066177368164
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1133083070699985
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2880731872558593
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5271186998912267
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0523460865020757,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6825943633185492,
                "rejected_mean_error": 2.8812466049194336,
                "gap_rejected_minus_accepted": 1.1986522416008845
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8434218764305115,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5258125034951096,
                "rejected_mean_error": 2.6306331264325222,
                "gap_rejected_minus_accepted": 1.1048206229374127
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5092540383338928,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2880731872558593,
                "rejected_mean_error": 2.316845987701416,
                "gap_rejected_minus_accepted": 1.0287728004455567
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.302640289068222,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1143529373235976,
                "rejected_mean_error": 2.0323180522582827,
                "gap_rejected_minus_accepted": 0.917965114934685
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0867158651351927,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6916366798347897,
                "rejected_mean_error": 2.8467556953430178,
                "gap_rejected_minus_accepted": 1.155119015508228
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8509288728237152,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5319917194027315,
                "rejected_mean_error": 2.6238840288586087,
                "gap_rejected_minus_accepted": 1.0918923094558772
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4921942353248596,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2880925233364104,
                "rejected_mean_error": 2.3262046394348146,
                "gap_rejected_minus_accepted": 1.0381121160984041
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.331531047821045,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1111862673645927,
                "rejected_mean_error": 2.0416171684622126,
                "gap_rejected_minus_accepted": 0.93043090109762
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9916079939711231,
            "spearman": 0.9903732555063715,
            "auroc_top30_bad": 0.9971291428571428,
            "mae": 0.07807244449204809,
            "mse": 0.012607869310249757,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7086381235939926,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05213700467348099
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20415115168094636
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5892783325195312
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.932704376411438
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
            "pearson": 0.992487180236895,
            "spearman": 0.9862025824016528,
            "auroc_top30_worst": 0.9990217142857143,
            "pairwise_seed_ranking": 0.9112,
            "predicted_best_mean_error": 1.554455027103424,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.0648672511577606,
            "gap_to_oracle": 0.00331176686286927,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5717464802265168
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8769546954486614
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1155642570972442
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3092600071925853
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6111643075942994,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4759765623145633,
                "rejected_mean_error": 2.94631428527832,
                "gap_rejected_minus_accepted": 1.4703377229637569
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02970689535141,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3084194151607114,
                "rejected_mean_error": 2.5647729273421316,
                "gap_rejected_minus_accepted": 1.2563535121814202
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.458724558353424,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1155642570972442,
                "rejected_mean_error": 2.1304564121246337,
                "gap_rejected_minus_accepted": 1.0148921550273895
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.192491054534912,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8781015755840764,
                "rejected_mean_error": 1.8718432498461663,
                "gap_rejected_minus_accepted": 0.9937416742620899
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5978870391845703,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4680864887767369,
                "rejected_mean_error": 2.980444383621216,
                "gap_rejected_minus_accepted": 1.5123578948444791
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0603156685829163,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2969628524652776,
                "rejected_mean_error": 2.576166923083956,
                "gap_rejected_minus_accepted": 1.2792040706186785
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4719560146331787,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1028687977790832,
                "rejected_mean_error": 2.135775758743286,
                "gap_rejected_minus_accepted": 1.032906960964203
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1928390562534332,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8576705654462179,
                "rejected_mean_error": 1.8759215184074034,
                "gap_rejected_minus_accepted": 1.0182509529611856
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
      "best_epoch": 126,
      "best_calib_loss": 0.007662668824195862,
      "train_time_sec": 73.73391890525818,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9988332436042123,
            "spearman": 0.997686563331551,
            "auroc_top30_bad": 0.999261,
            "mae": 0.030307231628851787,
            "mse": 0.0021293715406625305,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7514177786012919,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.005818067401647567
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1989334442138672
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5743143851280212
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9271281951109568
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
            "pearson": 0.9992248197940137,
            "spearman": 0.9987928096477122,
            "auroc_top30_worst": 0.9996236190476191,
            "pairwise_seed_ranking": 0.9624,
            "predicted_best_mean_error": 1.5304666743278503,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08514165368676196,
            "gap_to_oracle": 0.0016074401438235242,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6666111285090447
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8074041142702103
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0102925216078757
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2415410708347956
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.811926579475403,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.405717816001839,
                "rejected_mean_error": 3.456327527999878,
                "gap_rejected_minus_accepted": 2.050609711998039
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.006883442401886,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2415410708347956,
                "rejected_mean_error": 2.718491936302185,
                "gap_rejected_minus_accepted": 1.4769508654673893
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.402176856994629,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0102925216078757,
                "rejected_mean_error": 2.2112650527954103,
                "gap_rejected_minus_accepted": 1.2009725311875346
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0168966352939606,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8074041142702103,
                "rejected_mean_error": 1.8785703448454538,
                "gap_rejected_minus_accepted": 1.0711662305752436
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8328824520111087,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106747157375017,
                "rejected_mean_error": 3.460010838508606,
                "gap_rejected_minus_accepted": 2.0493361227711047
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.023771643638611,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2433639113505681,
                "rejected_mean_error": 2.7323415780067446,
                "gap_rejected_minus_accepted": 1.4889776666561765
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4083675146102905,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0038893938660622,
                "rejected_mean_error": 2.227327262163162,
                "gap_rejected_minus_accepted": 1.2234378682970999
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.009827047586441,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7992210220098496,
                "rejected_mean_error": 1.8877374300161998,
                "gap_rejected_minus_accepted": 1.0885164080063503
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9858048042720445,
            "spearman": 0.9840846165745443,
            "auroc_top30_bad": 0.9872792380952382,
            "mae": 0.0902867803311532,
            "mse": 0.016626005157427893,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.692931040544836,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06401712727546692
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2329997491121292
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6798915155768395
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.03501281645298
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
            "pearson": 0.9739857842783205,
            "spearman": 0.9769670938669401,
            "auroc_top30_worst": 0.9833508571428572,
            "pairwise_seed_ranking": 0.8988,
            "predicted_best_mean_error": 1.4679815065860748,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06081231713294977,
            "gap_to_oracle": 0.0051384844779969185,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8996955018043518
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9798404597319089
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1701703962326049
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3621096377179567
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0413830757141116,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4560450171364678,
                "rejected_mean_error": 2.260578462600708,
                "gap_rejected_minus_accepted": 0.8045334454642403
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8860304951667786,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3614546196692272,
                "rejected_mean_error": 2.0605110973595813,
                "gap_rejected_minus_accepted": 0.6990564776903541
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.507343828678131,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1701703962326049,
                "rejected_mean_error": 1.9028263271331787,
                "gap_rejected_minus_accepted": 0.7326559309005738
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.13307324051857,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9807515369055751,
                "rejected_mean_error": 1.7221427119019954,
                "gap_rejected_minus_accepted": 0.7413911749964203
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.043693470954895,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4500861766603257,
                "rejected_mean_error": 2.2371626472473145,
                "gap_rejected_minus_accepted": 0.7870764705869888
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8795159459114075,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3535315556959673,
                "rejected_mean_error": 2.0490167462636553,
                "gap_rejected_minus_accepted": 0.695485190567688
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.524743139743805,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.158768922805786,
                "rejected_mean_error": 1.8988187246322632,
                "gap_rejected_minus_accepted": 0.7400498018264772
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1324274241924286,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.963473810089959,
                "rejected_mean_error": 1.7192492293801538,
                "gap_rejected_minus_accepted": 0.7557754192901948
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9680945611076098,
            "spearman": 0.9739730297139003,
            "auroc_top30_bad": 0.9914003809523809,
            "mae": 0.16568721339425338,
            "mse": 0.07143766183297669,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6999111735783472,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06977847808599472
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20464706752300263
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7008447848200798
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0623649192094804
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
            "pearson": 0.927119818428935,
            "spearman": 0.949057403044738,
            "auroc_top30_worst": 0.9900129523809524,
            "pairwise_seed_ranking": 0.9256,
            "predicted_best_mean_error": 1.726383434176445,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.0807651472091675,
            "gap_to_oracle": 0.0024966340065002424,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9496271305084228
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1337851152206078
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2901043781280517
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4841465946199544
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1561723947525024,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6570915637546115,
                "rejected_mean_error": 3.110771800994873,
                "gap_rejected_minus_accepted": 1.4536802372402613
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8959831595420837,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4836109975867744,
                "rejected_mean_error": 2.7569679859728096,
                "gap_rejected_minus_accepted": 1.2733569883860352
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.574958324432373,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2901043781280517,
                "rejected_mean_error": 2.3148147968292236,
                "gap_rejected_minus_accepted": 1.024710418701172
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3075262010097504,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1345298320721513,
                "rejected_mean_error": 2.0255780650050306,
                "gap_rejected_minus_accepted": 0.8910482329328793
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1774603128433228,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6588545299900903,
                "rejected_mean_error": 3.1417950439453124,
                "gap_rejected_minus_accepted": 1.482940513955222
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9020406305789948,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4834225443913975,
                "rejected_mean_error": 2.768049675320822,
                "gap_rejected_minus_accepted": 1.2846271309294244
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5540712475776672,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.286879019498825,
                "rejected_mean_error": 2.3274181432724,
                "gap_rejected_minus_accepted": 1.0405391237735748
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3048442900180817,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.140865584687581,
                "rejected_mean_error": 2.031618254069976,
                "gap_rejected_minus_accepted": 0.8907526693823951
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9914560453521271,
            "spearman": 0.9888870229528939,
            "auroc_top30_bad": 0.9965432380952381,
            "mae": 0.07866562921819416,
            "mse": 0.013174875877347194,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7174460815029108,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05729325878620148
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19984138746261595
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5912194067001343
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9330171932856242
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
            "pearson": 0.9901046560737334,
            "spearman": 0.9832156503140164,
            "auroc_top30_worst": 0.9980190476190476,
            "pairwise_seed_ranking": 0.9148,
            "predicted_best_mean_error": 1.5549472348690032,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06437504339218147,
            "gap_to_oracle": 0.003803974628448392,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5746821935176849
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8782223204198556
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1171264046192169
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3101245465118494
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5345100164413457,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4751933295196957,
                "rejected_mean_error": 2.953363380432129,
                "gap_rejected_minus_accepted": 1.4781700509124331
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0140392184257507,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3093830155270332,
                "rejected_mean_error": 2.5618882834340058,
                "gap_rejected_minus_accepted": 1.2525052679069726
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4819809198379517,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1171264046192169,
                "rejected_mean_error": 2.128894264602661,
                "gap_rejected_minus_accepted": 1.011767859983444
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2143707275390625,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8797647295097193,
                "rejected_mean_error": 1.8712876818859463,
                "gap_rejected_minus_accepted": 0.991522952376227
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5104912519454956,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4676686607466805,
                "rejected_mean_error": 2.9842048358917235,
                "gap_rejected_minus_accepted": 1.516536175145043
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0177019834518433,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2973129318997185,
                "rejected_mean_error": 2.5751277984134733,
                "gap_rejected_minus_accepted": 1.2778148665137548
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4901132583618164,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1041666378974915,
                "rejected_mean_error": 2.134477918624878,
                "gap_rejected_minus_accepted": 1.0303112807273864
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2046834826469421,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8655096604710534,
                "rejected_mean_error": 1.8732805398696246,
                "gap_rejected_minus_accepted": 1.0077708793985711
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
      "best_epoch": 122,
      "best_calib_loss": 0.010442988947033882,
      "train_time_sec": 72.98385238647461,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998253033119996,
            "spearman": 0.9991025340895388,
            "auroc_top30_bad": 0.999859619047619,
            "mae": 0.012903642124736143,
            "mse": 0.00032051740564874884,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7396196092871498,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0001479109823703766
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19771964349746704
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5738941936254501
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9267172776381175
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
            "pearson": 0.9997719507088609,
            "spearman": 0.9995933058477225,
            "auroc_top30_worst": 0.9999226666666666,
            "pairwise_seed_ranking": 0.9649,
            "predicted_best_mean_error": 1.5299388646781444,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08566946333646785,
            "gap_to_oracle": 0.0010796304941176338,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6649090139269829
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8069776463270187
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0100496419787406
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.24129659845829
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.756028294563295,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056633697814411,
                "rejected_mean_error": 3.4568175439834596,
                "gap_rejected_minus_accepted": 2.0511541742020185
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9641478955745697,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.24129659845829,
                "rejected_mean_error": 2.7192253534317015,
                "gap_rejected_minus_accepted": 1.4779287549734115
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4016762375831604,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0100496419787406,
                "rejected_mean_error": 2.2115079324245452,
                "gap_rejected_minus_accepted": 1.2014582904458047
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0260616540908813,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8069776463270187,
                "rejected_mean_error": 1.8787125008265178,
                "gap_rejected_minus_accepted": 1.071734854499499
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7864868640899663,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106002229120995,
                "rejected_mean_error": 3.4606812739372255,
                "gap_rejected_minus_accepted": 2.050081051025126
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.984834760427475,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.243071423570315,
                "rejected_mean_error": 2.7332190413475037,
                "gap_rejected_minus_accepted": 1.4901476177771886
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4138615727424622,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0038019052147866,
                "rejected_mean_error": 2.2274147508144377,
                "gap_rejected_minus_accepted": 1.2236128455996511
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0192444920539856,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7988403466939926,
                "rejected_mean_error": 1.8878643217881521,
                "gap_rejected_minus_accepted": 1.0890239750941595
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9787977730918519,
            "spearman": 0.9804556691879345,
            "auroc_top30_bad": 0.9888579047619048,
            "mae": 0.10589754834028427,
            "mse": 0.02496242477832021,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6672108693043745,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07101554811000824
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2531499418735504
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6825606304526329
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0349776574691136
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
            "pearson": 0.9696403396533279,
            "spearman": 0.975449623199759,
            "auroc_top30_worst": 0.9874590476190476,
            "pairwise_seed_ranking": 0.8852,
            "predicted_best_mean_error": 1.4685028495788575,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06029097414016715,
            "gap_to_oracle": 0.005659827470779533,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.893850914478302
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9802522101463416
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1744015987396241
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3588522743822924
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.038059520721436,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.458104856385125,
                "rejected_mean_error": 2.242039909362793,
                "gap_rejected_minus_accepted": 0.7839350529776681
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8517602682113647,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3584296265686588,
                "rejected_mean_error": 2.0695667476318897,
                "gap_rejected_minus_accepted": 0.7111371210632309
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5009449124336243,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1744015987396241,
                "rejected_mean_error": 1.8985951246261596,
                "gap_rejected_minus_accepted": 0.7241935258865355
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.108552634716034,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9813582284001116,
                "rejected_mean_error": 1.7219400497485378,
                "gap_rejected_minus_accepted": 0.7405818213484262
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.059128427505493,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4527242856555516,
                "rejected_mean_error": 2.2134196662902834,
                "gap_rejected_minus_accepted": 0.7606953806347319
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8424351811408997,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3509731509468772,
                "rejected_mean_error": 2.0566107413125416,
                "gap_rejected_minus_accepted": 0.7056375903656644
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5112507343292236,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1631740789413452,
                "rejected_mean_error": 1.894413568496704,
                "gap_rejected_minus_accepted": 0.7312394895553589
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1045903265476227,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9629164953080435,
                "rejected_mean_error": 1.7194369878360931,
                "gap_rejected_minus_accepted": 0.7565204925280496
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9583662899678682,
            "spearman": 0.9684882983673674,
            "auroc_top30_bad": 0.9864449523809524,
            "mae": 0.18256579850963825,
            "mse": 0.09364150937000286,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6642935207574221,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09418868643045425
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20477486817836763
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6958403809428215
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.068798913693428
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
            "pearson": 0.9136433802293513,
            "spearman": 0.9604721390541692,
            "auroc_top30_worst": 0.9814156190476191,
            "pairwise_seed_ranking": 0.9364,
            "predicted_best_mean_error": 1.725467794775963,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08168078660964961,
            "gap_to_oracle": 0.0015809946060181268,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9388075561523438
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1116102777230434
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2909067909240723
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.48800665877267
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0374808311462407,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.662517757627699,
                "rejected_mean_error": 3.061936056137085,
                "gap_rejected_minus_accepted": 1.399418298509386
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8268047273159027,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.487612088309281,
                "rejected_mean_error": 2.7449902798801946,
                "gap_rejected_minus_accepted": 1.2573781915709137
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5330888628959656,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2909067909240723,
                "rejected_mean_error": 2.314012384033203,
                "gap_rejected_minus_accepted": 1.0231055931091306
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.317006140947342,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1122602361459701,
                "rejected_mean_error": 2.0330171082546515,
                "gap_rejected_minus_accepted": 0.9207568721086814
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0450985193252564,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6696168569723766,
                "rejected_mean_error": 3.044934101104736,
                "gap_rejected_minus_accepted": 1.3753172441323596
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8403430581092834,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4906562348419332,
                "rejected_mean_error": 2.7465782449358986,
                "gap_rejected_minus_accepted": 1.2559220100939654
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5319072008132935,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2855149085521698,
                "rejected_mean_error": 2.328782254219055,
                "gap_rejected_minus_accepted": 1.0432673456668853
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3266828656196594,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1092813577916887,
                "rejected_mean_error": 2.0422589294413194,
                "gap_rejected_minus_accepted": 0.9329775716496307
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9912463514189949,
            "spearman": 0.9894281607442361,
            "auroc_top30_bad": 0.9970598095238095,
            "mae": 0.07755533275961288,
            "mse": 0.013177879555255621,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7055212070451239,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06396523720026016
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2066047213077545
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5894775335311889
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9325225414276123
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
            "pearson": 0.9913145018681218,
            "spearman": 0.9856525711696457,
            "auroc_top30_worst": 0.9983024761904762,
            "pairwise_seed_ranking": 0.9144,
            "predicted_best_mean_error": 1.5553031142950058,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.0640191639661789,
            "gap_to_oracle": 0.004159854054450962,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5725646178722381
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.878595611701409
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1160050520420075
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3092209731401412
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5051079273223875,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4756052886380089,
                "rejected_mean_error": 2.9496557483673094,
                "gap_rejected_minus_accepted": 1.4740504597293005
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9773251712322235,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3084299760605254,
                "rejected_mean_error": 2.564741312124478,
                "gap_rejected_minus_accepted": 1.2563113360639526
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4720197319984436,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1160050520420075,
                "rejected_mean_error": 2.1300156171798705,
                "gap_rejected_minus_accepted": 1.014010565137863
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2395301163196564,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.880103697887244,
                "rejected_mean_error": 1.8711744512539663,
                "gap_rejected_minus_accepted": 0.9910707533667223
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.474336767196655,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4680864887767369,
                "rejected_mean_error": 2.980444383621216,
                "gap_rejected_minus_accepted": 1.5123578948444791
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.005971908569336,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2969628524652776,
                "rejected_mean_error": 2.576166923083956,
                "gap_rejected_minus_accepted": 1.2792040706186785
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5068459510803223,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1025902009010315,
                "rejected_mean_error": 2.136054355621338,
                "gap_rejected_minus_accepted": 1.0334641547203063
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.241780012845993,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8640404589592464,
                "rejected_mean_error": 1.8737755115019445,
                "gap_rejected_minus_accepted": 1.0097350525426982
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
      "best_epoch": 154,
      "best_calib_loss": 0.009245580993592739,
      "train_time_sec": 79.73485159873962,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994196316814649,
            "spearman": 0.9983280443083822,
            "auroc_top30_bad": 0.9995250952380952,
            "mae": 0.025960809756152958,
            "mse": 0.0012422003802234048,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7538756359298768,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00032417865097522734
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19792789256572724
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5743056021928787
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9269457426389058
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
            "pearson": 0.9993621231362615,
            "spearman": 0.9986724841308674,
            "auroc_top30_worst": 0.9995424761904762,
            "pairwise_seed_ranking": 0.9648,
            "predicted_best_mean_error": 1.5303198700845242,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.0852884579300881,
            "gap_to_oracle": 0.0014606359004973868,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6671142174601555
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8080599930524826
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0103131028532981
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2414993916749955
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.802946591377258,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056613642043538,
                "rejected_mean_error": 3.456835594177246,
                "gap_rejected_minus_accepted": 2.051174229972892
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.997688889503479,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2414993916749955,
                "rejected_mean_error": 2.7186169737815855,
                "gap_rejected_minus_accepted": 1.47711758210659
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4265658855438232,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0103131028532981,
                "rejected_mean_error": 2.2112444715499877,
                "gap_rejected_minus_accepted": 1.2009313686966896
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0503826141357422,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8080599930524826,
                "rejected_mean_error": 1.8783517185846965,
                "gap_rejected_minus_accepted": 1.070291725532214
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8273230314254763,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106334669391314,
                "rejected_mean_error": 3.4603820776939394,
                "gap_rejected_minus_accepted": 2.0497486107548077
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.014214277267456,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.243176325360934,
                "rejected_mean_error": 2.732904335975647,
                "gap_rejected_minus_accepted": 1.4897280106147128
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4427474737167358,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.003960019171238,
                "rejected_mean_error": 2.2272566368579865,
                "gap_rejected_minus_accepted": 1.2232966176867486
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0418711304664612,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7991871050596238,
                "rejected_mean_error": 1.887748735666275,
                "gap_rejected_minus_accepted": 1.0885616306066512
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.981947255862517,
            "spearman": 0.9799754592854758,
            "auroc_top30_bad": 0.9836822857142857,
            "mae": 0.10070291295026254,
            "mse": 0.021188525759511394,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6812530177985461,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05567706996202469
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23728462035655976
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6799829577803612
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0361112980127334
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
            "pearson": 0.9647637059625218,
            "spearman": 0.9700694356924389,
            "auroc_top30_worst": 0.9752015238095239,
            "pairwise_seed_ranking": 0.8896,
            "predicted_best_mean_error": 1.4677321257591247,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06106169795989991,
            "gap_to_oracle": 0.004889103651046778,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8959568438529968
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9807662188242643
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1690783304214478
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3623042007499158
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0509227752685546,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4614726314544677,
                "rejected_mean_error": 2.2117299337387086,
                "gap_rejected_minus_accepted": 0.7502573022842409
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.888065755367279,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3617336601177936,
                "rejected_mean_error": 2.0596757590199433,
                "gap_rejected_minus_accepted": 0.6979420989021496
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4673975110054016,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1690783304214478,
                "rejected_mean_error": 1.903918392944336,
                "gap_rejected_minus_accepted": 0.7348400625228881
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1039230525493622,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9812408110585076,
                "rejected_mean_error": 1.7219792724037375,
                "gap_rejected_minus_accepted": 0.7407384613452299
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0493258953094484,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.453962050014072,
                "rejected_mean_error": 2.2022797870635986,
                "gap_rejected_minus_accepted": 0.7483177370495266
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.903681218624115,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3518715708013525,
                "rejected_mean_error": 2.0539440030143377,
                "gap_rejected_minus_accepted": 0.7020724322129852
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4698521494865417,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1567682781219482,
                "rejected_mean_error": 1.900819369316101,
                "gap_rejected_minus_accepted": 0.7440510911941529
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.109372764825821,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9612947456420414,
                "rejected_mean_error": 1.7199833526968318,
                "gap_rejected_minus_accepted": 0.7586886070547904
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9722635505053241,
            "spearman": 0.9786067543882996,
            "auroc_top30_bad": 0.9924114285714286,
            "mae": 0.15277102648435356,
            "mse": 0.0633372281295369,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7078860288074657,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06754635161161422
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2036785975217819
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6952037658572197
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0554168327887854
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
            "pearson": 0.9420272832936578,
            "spearman": 0.9706151706977093,
            "auroc_top30_worst": 0.9914514285714287,
            "pairwise_seed_ranking": 0.9336,
            "predicted_best_mean_error": 1.725870134472847,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08127844691276542,
            "gap_to_oracle": 0.0019833343029023176,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9419475450515747
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1166052852685635
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2885045782089233
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4732788806276789
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.165147042274475,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.651732872221205,
                "rejected_mean_error": 3.159000024795532,
                "gap_rejected_minus_accepted": 1.507267152574327
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9345579147338867,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.472786792441646,
                "rejected_mean_error": 2.7893714371580667,
                "gap_rejected_minus_accepted": 1.3165846447164207
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5423418879508972,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2885045782089233,
                "rejected_mean_error": 2.316414596748352,
                "gap_rejected_minus_accepted": 1.0279100185394288
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3054249584674835,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1177281282199458,
                "rejected_mean_error": 2.0311905872096627,
                "gap_rejected_minus_accepted": 0.9134624589897169
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1945410490036013,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6529732533295949,
                "rejected_mean_error": 3.1947265338897703,
                "gap_rejected_minus_accepted": 1.5417532805601755
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9538094997406006,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4834225443913975,
                "rejected_mean_error": 2.768049675320822,
                "gap_rejected_minus_accepted": 1.2846271309294244
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5370802879333496,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2842750871181488,
                "rejected_mean_error": 2.3300220756530763,
                "gap_rejected_minus_accepted": 1.0457469885349275
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3185964226722717,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1173353739201077,
                "rejected_mean_error": 2.0395455443285364,
                "gap_rejected_minus_accepted": 0.9222101704084287
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9909362237692282,
            "spearman": 0.9894546396550532,
            "auroc_top30_bad": 0.9968754285714285,
            "mae": 0.08634739200487238,
            "mse": 0.015304480217359653,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7041616152312277,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07489339804649353
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20124424166679383
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5893602269172669
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9330349081675211
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
            "pearson": 0.991614948919964,
            "spearman": 0.988359477990066,
            "auroc_top30_worst": 0.9975771428571428,
            "pairwise_seed_ranking": 0.9172,
            "predicted_best_mean_error": 1.5539994344711303,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06532284379005437,
            "gap_to_oracle": 0.0028561742305754922,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5727696440219879
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8686039658884207
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1170358597278596
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.309372405285266
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5372313499450687,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4752140812608932,
                "rejected_mean_error": 2.9531766147613525,
                "gap_rejected_minus_accepted": 1.4779625335004594
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9544748663902283,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3085404455407326,
                "rejected_mean_error": 2.564410609559129,
                "gap_rejected_minus_accepted": 1.2558701640183965
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4304583072662354,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1170358597278596,
                "rejected_mean_error": 2.1289848094940185,
                "gap_rejected_minus_accepted": 1.011948949766159
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1475543677806854,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8698109674948854,
                "rejected_mean_error": 1.8746126845653945,
                "gap_rejected_minus_accepted": 1.0048017170705092
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5307830810546874,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4684279624621073,
                "rejected_mean_error": 2.9773711204528808,
                "gap_rejected_minus_accepted": 1.5089431579907735
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9777188003063202,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2975750890645115,
                "rejected_mean_error": 2.5743496493687705,
                "gap_rejected_minus_accepted": 1.276774560304259
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4379682540893555,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1041717581748962,
                "rejected_mean_error": 2.134472798347473,
                "gap_rejected_minus_accepted": 1.030301040172577
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1423437893390656,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8496206951519799,
                "rejected_mean_error": 1.8786335067953017,
                "gap_rejected_minus_accepted": 1.0290128116433217
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
      "best_epoch": 110,
      "best_calib_loss": 0.007756560575217009,
      "train_time_sec": 56.40331530570984,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9995852257251332,
            "spearman": 0.9986917586995485,
            "auroc_top30_bad": 0.9997524761904762,
            "mae": 0.024915797876100987,
            "mse": 0.001171267371608163,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.997,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7323939739401635,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0042601535916328434
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19775410676002503
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5740261389255523
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.926801818005244
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
            "pearson": 0.9995797593943395,
            "spearman": 0.9992504885140193,
            "auroc_top30_worst": 0.9997323809523809,
            "pairwise_seed_ranking": 0.9555,
            "predicted_best_mean_error": 1.530591365724802,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08501696228981026,
            "gap_to_oracle": 0.001732131540775228,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6664534595608711
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8072160672426224
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0101375191092492
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2413526337544123
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.733267498016359,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.405698852399985,
                "rejected_mean_error": 3.456498200416565,
                "gap_rejected_minus_accepted": 2.05079934801658
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9405213296413422,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2413526337544123,
                "rejected_mean_error": 2.719057247543335,
                "gap_rejected_minus_accepted": 1.4777046137889227
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3833246231079102,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0101375191092492,
                "rejected_mean_error": 2.211420055294037,
                "gap_rejected_minus_accepted": 1.2012825361847876
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0119349658489227,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8072160672426224,
                "rejected_mean_error": 1.8786330271879832,
                "gap_rejected_minus_accepted": 1.0714169599453607
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7689993619918822,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4107513972454602,
                "rejected_mean_error": 3.459320704936981,
                "gap_rejected_minus_accepted": 2.048569307691521
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.955145537853241,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2431681161324184,
                "rejected_mean_error": 2.7329289636611938,
                "gap_rejected_minus_accepted": 1.4897608475287754
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.38791161775589,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0037608090043069,
                "rejected_mean_error": 2.2274558470249177,
                "gap_rejected_minus_accepted": 1.2236950380206109
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.005995362997055,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.799192277789116,
                "rejected_mean_error": 1.887747011423111,
                "gap_rejected_minus_accepted": 1.0885547336339951
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9860970339603466,
            "spearman": 0.9836740044310854,
            "auroc_top30_bad": 0.9854026666666666,
            "mae": 0.08965613712277264,
            "mse": 0.01731181003682353,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.69985497149977,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05956549340486526
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22739833772182463
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6809741438269615
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.034622305639585
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
            "pearson": 0.9768709410343468,
            "spearman": 0.9777098962280961,
            "auroc_top30_worst": 0.984152380952381,
            "pairwise_seed_ranking": 0.876,
            "predicted_best_mean_error": 1.4679616293907165,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06083219432830811,
            "gap_to_oracle": 0.0051186072826385765,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.884094777584076
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.976284283093917
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1706053951263429
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3624802294062144
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.09094557762146,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4562279647191365,
                "rejected_mean_error": 2.2589319343566894,
                "gap_rejected_minus_accepted": 0.8027039696375529
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9202437698841095,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3618074131368192,
                "rejected_mean_error": 2.059454971228164,
                "gap_rejected_minus_accepted": 0.6976475580913446
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.560439109802246,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1706053951263429,
                "rejected_mean_error": 1.902391328239441,
                "gap_rejected_minus_accepted": 0.731785933113098
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1995046138763428,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9767785194201972,
                "rejected_mean_error": 1.7234698778282744,
                "gap_rejected_minus_accepted": 0.7466913584080772
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.089193773269653,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4502976968553332,
                "rejected_mean_error": 2.2352589654922483,
                "gap_rejected_minus_accepted": 0.7849612686369152
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9179746508598328,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3530387508677926,
                "rejected_mean_error": 2.0504795161504594,
                "gap_rejected_minus_accepted": 0.6974407652826669
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5685369968414307,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1596392517089844,
                "rejected_mean_error": 1.897948395729065,
                "gap_rejected_minus_accepted": 0.7383091440200806
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2020330429077148,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.95643959537385,
                "rejected_mean_error": 1.7216190450331743,
                "gap_rejected_minus_accepted": 0.7651794496593243
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9794050089599238,
            "spearman": 0.9818045030838839,
            "auroc_top30_bad": 0.991248761904762,
            "mae": 0.1322450709696859,
            "mse": 0.03702154230001738,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7302413710593783,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09882877188920974
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22134888231754302
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.697229974257946
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0485192534049352
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
            "pearson": 0.984117355477496,
            "spearman": 0.9707728934226518,
            "auroc_top30_worst": 0.9956510476190477,
            "pairwise_seed_ranking": 0.9164,
            "predicted_best_mean_error": 1.726940250515938,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.0802083308696746,
            "gap_to_oracle": 0.003053450345993136,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9420561637878418
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1151550389253175
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.291123602294922
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4559292855547434
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6888532400131235,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.646002908706665,
                "rejected_mean_error": 3.2105696964263917,
                "gap_rejected_minus_accepted": 1.5645667877197267
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1176788806915283,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4554026189201543,
                "rejected_mean_error": 2.8414128767415736,
                "gap_rejected_minus_accepted": 1.3860102578214193
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6156338453292847,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.291123602294922,
                "rejected_mean_error": 2.3137955726623534,
                "gap_rejected_minus_accepted": 1.0226719703674314
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3109454810619354,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1159527080889327,
                "rejected_mean_error": 2.0317836571146866,
                "gap_rejected_minus_accepted": 0.9158309490257539
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6859249114990233,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6474531172381508,
                "rejected_mean_error": 3.2444077587127684,
                "gap_rejected_minus_accepted": 1.5969546414746176
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1301676630973816,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4545739422188724,
                "rejected_mean_error": 2.8536796531979998,
                "gap_rejected_minus_accepted": 1.3991057109791274
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6147716045379639,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2858546092510224,
                "rejected_mean_error": 2.3284425535202025,
                "gap_rejected_minus_accepted": 1.0425879442691801
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3176309764385223,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1162269035029033,
                "rejected_mean_error": 2.039918986233798,
                "gap_rejected_minus_accepted": 0.9236920827308945
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9894878438069119,
            "spearman": 0.9881422947977676,
            "auroc_top30_bad": 0.9947748571428572,
            "mae": 0.08635315794576891,
            "mse": 0.01594222223419817,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7411010910116995,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05347767090797424
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20811645965576173
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5896727292060852
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9347614702224731
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
            "pearson": 0.9858736117362285,
            "spearman": 0.9838660238502553,
            "auroc_top30_worst": 0.994816,
            "pairwise_seed_ranking": 0.9088,
            "predicted_best_mean_error": 1.5549326417446137,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06438963651657104,
            "gap_to_oracle": 0.003789381504058831,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5705491602420807
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8707189816886034
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1179692575931548
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3113547783734194
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5409107685089114,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4766729734473758,
                "rejected_mean_error": 2.940046585083008,
                "gap_rejected_minus_accepted": 1.4633736116356322
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0311641693115234,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3104671433552098,
                "rejected_mean_error": 2.558642827283841,
                "gap_rejected_minus_accepted": 1.248175683928631
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5363712906837463,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1179692575931548,
                "rejected_mean_error": 2.1280514116287232,
                "gap_rejected_minus_accepted": 1.0100821540355684
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2654704749584198,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8719071916307504,
                "rejected_mean_error": 1.8739124517430619,
                "gap_rejected_minus_accepted": 1.0020052601123115
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.526404786109924,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4680441996786329,
                "rejected_mean_error": 2.9808249855041504,
                "gap_rejected_minus_accepted": 1.5127807858255176
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0415082573890686,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2977390496488561,
                "rejected_mean_error": 2.573862972713652,
                "gap_rejected_minus_accepted": 1.2761239230647958
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5675815343856812,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1062972798347472,
                "rejected_mean_error": 2.132347276687622,
                "gap_rejected_minus_accepted": 1.0260499968528747
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.262456089258194,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8564057870516701,
                "rejected_mean_error": 1.8763476202194704,
                "gap_rejected_minus_accepted": 1.0199418331678003
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
      "best_epoch": 61,
      "best_calib_loss": 0.009612605907022953,
      "train_time_sec": 56.25807046890259,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9988924601289428,
            "spearman": 0.997897751173871,
            "auroc_top30_bad": 0.9996035238095239,
            "mae": 0.03866597846397199,
            "mse": 0.0026503338745853676,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7275817018021974,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.007864635720849037
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19862471590042113
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5744439825892449
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.926918066740036
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
            "pearson": 0.9988611121994844,
            "spearman": 0.9981394194135765,
            "auroc_top30_worst": 0.999779238095238,
            "pairwise_seed_ranking": 0.9411,
            "predicted_best_mean_error": 1.5325889553427696,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08301937267184267,
            "gap_to_oracle": 0.003729721158742816,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6681936747431755
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8081188112974167
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0108239249110222
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.241471092470487
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.706383299827576,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4057557686368625,
                "rejected_mean_error": 3.455985954284668,
                "gap_rejected_minus_accepted": 2.0502301856478056
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9473133087158203,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.241471092470487,
                "rejected_mean_error": 2.718701871395111,
                "gap_rejected_minus_accepted": 1.477230778924624
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3857126832008362,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0108239249110222,
                "rejected_mean_error": 2.210733649492264,
                "gap_rejected_minus_accepted": 1.1999097245812416
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.009895145893097,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8081188112974167,
                "rejected_mean_error": 1.8783321125030517,
                "gap_rejected_minus_accepted": 1.070213301205635
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7397298574447633,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106613770127296,
                "rejected_mean_error": 3.4601308870315552,
                "gap_rejected_minus_accepted": 2.0494695100188256
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9647412598133087,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2432810162305832,
                "rejected_mean_error": 2.732590263366699,
                "gap_rejected_minus_accepted": 1.489309247136116
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3942500352859497,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0043410602211953,
                "rejected_mean_error": 2.2268755958080293,
                "gap_rejected_minus_accepted": 1.222534535586834
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0092770457267761,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7991434782743454,
                "rejected_mean_error": 1.8877632779280344,
                "gap_rejected_minus_accepted": 1.088619799653689
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9814381997175465,
            "spearman": 0.9808542835781818,
            "auroc_top30_bad": 0.9803900952380952,
            "mae": 0.10003474958310835,
            "mse": 0.022469248842239966,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6801036481492722,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06977384752035141
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2283931003332138
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6803138439536095
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0359617271025976
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
            "pearson": 0.9721170838695918,
            "spearman": 0.9699690058041638,
            "auroc_top30_worst": 0.970057142857143,
            "pairwise_seed_ranking": 0.8668,
            "predicted_best_mean_error": 1.468292219877243,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.060501603841781604,
            "gap_to_oracle": 0.005449197769165082,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8809968695640564
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9778124388211813
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1700174669265746
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3668160538937746
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1120230913162232,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4565980275472006,
                "rejected_mean_error": 2.255601368904114,
                "gap_rejected_minus_accepted": 0.7990033413569133
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8883546590805054,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3663484551481657,
                "rejected_mean_error": 2.045860861437008,
                "gap_rejected_minus_accepted": 0.6795124062888425
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5174065232276917,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1700174669265746,
                "rejected_mean_error": 1.902979256439209,
                "gap_rejected_minus_accepted": 0.7329617895126344
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1986353397369385,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9781948137588014,
                "rejected_mean_error": 1.722996772035336,
                "gap_rejected_minus_accepted": 0.7448019582765347
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.120182728767395,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.450433439678616,
                "rejected_mean_error": 2.2340372800827026,
                "gap_rejected_minus_accepted": 0.7836038404040866
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8853757083415985,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3564845119568116,
                "rejected_mean_error": 2.0402516221243236,
                "gap_rejected_minus_accepted": 0.683767110167512
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5180625915527344,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.157304838180542,
                "rejected_mean_error": 1.9002828092575073,
                "gap_rejected_minus_accepted": 0.7429779710769653
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2171729803085327,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9609309434890747,
                "rejected_mean_error": 1.7201059170585264,
                "gap_rejected_minus_accepted": 0.7591749735694517
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9610699620973948,
            "spearman": 0.9731467394750566,
            "auroc_top30_bad": 0.985968,
            "mae": 0.18481184096513317,
            "mse": 0.07565992714730096,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.68014524170944,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08883577573299407
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2342649625301361
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6989965991854667
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.051112407231331
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
            "pearson": 0.9537591168222899,
            "spearman": 0.944953159266022,
            "auroc_top30_worst": 0.9851428571428571,
            "pairwise_seed_ranking": 0.908,
            "predicted_best_mean_error": 1.7258373426198959,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08131123876571666,
            "gap_to_oracle": 0.001950542449951076,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9488591060638428
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1284590695913022
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3018993724822998
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.459938204364736
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.27847101688385,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6493465987311469,
                "rejected_mean_error": 3.1804764862060546,
                "gap_rejected_minus_accepted": 1.5311298874749077
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.913430005311966,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4593809021193547,
                "rejected_mean_error": 2.8295034474839036,
                "gap_rejected_minus_accepted": 1.370122545364549
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.637293815612793,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3018993724822998,
                "rejected_mean_error": 2.3030198024749757,
                "gap_rejected_minus_accepted": 1.001120429992676
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3113211691379547,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1294348159918008,
                "rejected_mean_error": 2.02728002875439,
                "gap_rejected_minus_accepted": 0.8978452127625893
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.258165717124939,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6505905033482446,
                "rejected_mean_error": 3.216171283721924,
                "gap_rejected_minus_accepted": 1.5655807803736792
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9281805753707886,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4575991131723884,
                "rejected_mean_error": 2.8447001775105796,
                "gap_rejected_minus_accepted": 1.3871010643381911
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6422035694122314,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2935491473674774,
                "rejected_mean_error": 2.3207480154037476,
                "gap_rejected_minus_accepted": 1.0271988680362703
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.316723257303238,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1256612913003043,
                "rejected_mean_error": 2.036740556120235,
                "gap_rejected_minus_accepted": 0.9110792648199308
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9862339098706677,
            "spearman": 0.985352558417978,
            "auroc_top30_bad": 0.9943908571428571,
            "mae": 0.1015106462949887,
            "mse": 0.020058393852405595,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7284505836894802,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07533407080173492
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20385226504802703
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5905833376884461
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9349830034255981
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
            "pearson": 0.9809611826799787,
            "spearman": 0.9815306756676324,
            "auroc_top30_worst": 0.9956236190476191,
            "pairwise_seed_ranking": 0.898,
            "predicted_best_mean_error": 1.5562084066867827,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06311387157440196,
            "gap_to_oracle": 0.005065146446227908,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5780566341876984
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8687894605100155
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1201065067768097
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3119846076917039
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.519515085220337,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4771356722778743,
                "rejected_mean_error": 2.9358822956085207,
                "gap_rejected_minus_accepted": 1.4587466233306463
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.990700751543045,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3111010951764301,
                "rejected_mean_error": 2.556745022630539,
                "gap_rejected_minus_accepted": 1.245643927454109
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5097257494926453,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1201065067768097,
                "rejected_mean_error": 2.1259141624450684,
                "gap_rejected_minus_accepted": 1.0058076556682587
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2497420012950897,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8703194880447449,
                "rejected_mean_error": 1.874442815907864,
                "gap_rejected_minus_accepted": 1.0041233278631192
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5373291015625,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4691338721911114,
                "rejected_mean_error": 2.971017932891846,
                "gap_rejected_minus_accepted": 1.5018840607007344
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0251250863075256,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.299702818699699,
                "rejected_mean_error": 2.5680340074357533,
                "gap_rejected_minus_accepted": 1.2683311887360542
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5350207090377808,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1070566992759705,
                "rejected_mean_error": 2.131587857246399,
                "gap_rejected_minus_accepted": 1.0245311579704284
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2499068677425385,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8536804450882806,
                "rejected_mean_error": 1.87726578355473,
                "gap_rejected_minus_accepted": 1.0235853384664493
              }
            ]
          }
        }
      }
    }
  ]
}
```
