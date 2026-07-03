# Stage 6 Experiments: holdout_object_cabinet

```json
{
  "split": "holdout_object_cabinet",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 105,
      "best_calib_loss": 0.06071188300848007,
      "train_time_sec": 22.364398956298828,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9684906310456575,
            "spearman": 0.9352498122604679,
            "auroc_top30_bad": 0.9989171666666667,
            "mae": 0.1103844786286354,
            "mse": 0.040852215665852246,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.554,
            "expert_lt_simvla_seed0": 0.966,
            "same_context_pred_std": 0.6606756605847486,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.29554826686903835
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.30630984675735234
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4460833202622831
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7571471024607619
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9984191761988079,
            "spearman": 0.9981173924765601,
            "auroc_top30_worst": 0.9984554285714285,
            "pairwise_seed_ranking": 0.89,
            "predicted_best_mean_error": 1.4547757540643216,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07070215937495217,
            "gap_to_oracle": 0.004516689121723205,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4975948743224144
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7052852321386337
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9819395141243935
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2103576409101486
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.334727954864502,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3521496859192847,
                "rejected_mean_error": 2.957267252445221,
                "gap_rejected_minus_accepted": 1.6051175665259363
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.893943578004837,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2103576409101486,
                "rejected_mean_error": 2.4195728475570677,
                "gap_rejected_minus_accepted": 1.209215206646919
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4895806908607483,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9819395141243935,
                "rejected_mean_error": 2.043383371019363,
                "gap_rejected_minus_accepted": 1.0614438568949698
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.028133600950241,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7052852321386337,
                "rejected_mean_error": 1.7817868460496267,
                "gap_rejected_minus_accepted": 1.076501613910993
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3747501134872437,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.3643075228399701,
                "rejected_mean_error": 2.976011428833008,
                "gap_rejected_minus_accepted": 1.6117039059930378
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9140629470348358,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.221426321585973,
                "rejected_mean_error": 2.437632688999176,
                "gap_rejected_minus_accepted": 1.216206367413203
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4971882700920105,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9886464523077011,
                "rejected_mean_error": 2.0623093745708467,
                "gap_rejected_minus_accepted": 1.0736629222631455
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0489332973957062,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7081097030639648,
                "rejected_mean_error": 1.7979339835643768,
                "gap_rejected_minus_accepted": 1.089824280500412
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8663395612315545,
            "spearman": 0.8254227876471163,
            "auroc_top30_bad": 0.9450209523809524,
            "mae": 0.34088376666903497,
            "mse": 0.21788027643794772,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.96,
            "same_context_pred_std": 0.6155576228815341,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4394340584278107
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.407685088121891
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5551384315252305
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9037184384822845
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.8412282746947253,
            "spearman": 0.7264086292535228,
            "auroc_top30_worst": 0.8470918095238095,
            "pairwise_seed_ranking": 0.7184,
            "predicted_best_mean_error": 1.6468343914747239,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.04589539909362794,
            "gap_to_oracle": 0.021163292407989642,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7142169902324677
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9807405615082154
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2789845984458923
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4297280039614453
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.942119586467743,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5300845238367717,
                "rejected_mean_error": 3.0891300745010377,
                "gap_rejected_minus_accepted": 1.559045550664266
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.604168713092804,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.429226921996541,
                "rejected_mean_error": 2.4546348968633827,
                "gap_rejected_minus_accepted": 1.0254079748668417
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3489649295806885,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2789845984458923,
                "rejected_mean_error": 2.092993559360504,
                "gap_rejected_minus_accepted": 0.8140089609146117
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0757369697093964,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9816454685153291,
                "rejected_mean_error": 1.921271416204589,
                "gap_rejected_minus_accepted": 0.9396259476892599
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9461408019065858,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.536321429014206,
                "rejected_mean_error": 3.100405044555664,
                "gap_rejected_minus_accepted": 1.564083615541458
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.600580245256424,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4320256937952602,
                "rejected_mean_error": 2.466565760355147,
                "gap_rejected_minus_accepted": 1.0345400665598867
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3758743405342102,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2683655240535736,
                "rejected_mean_error": 2.11709405708313,
                "gap_rejected_minus_accepted": 0.8487285330295564
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0910847783088684,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0088514860660311,
                "rejected_mean_error": 1.9231272942242137,
                "gap_rejected_minus_accepted": 0.9142758081581825
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8357856879233512,
            "spearman": 0.837414850977305,
            "auroc_top30_bad": 0.9237939047619047,
            "mae": 0.3782711798220873,
            "mse": 0.36352528639458564,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.976,
            "same_context_pred_std": 0.6505692217461986,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4250144647359848
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.38470397636890413
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6141653649389743
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9529812630057335
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.7085707093444862,
            "spearman": 0.687298179646835,
            "auroc_top30_worst": 0.7662201904761905,
            "pairwise_seed_ranking": 0.7444,
            "predicted_best_mean_error": 1.918130925655365,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.06321586644649524,
            "gap_to_oracle": 0.026084524869918857,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.1076081042289734
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3341223343442647
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.486926008605957
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.586743636299044
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3992277145385743,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.786539473109775,
                "rejected_mean_error": 3.510092948913574,
                "gap_rejected_minus_accepted": 1.7235534758037991
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9165480732917786,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5863974674534262,
                "rejected_mean_error": 3.0740067056192757,
                "gap_rejected_minus_accepted": 1.4876092381658494
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5903317332267761,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.486926008605957,
                "rejected_mean_error": 2.430863632774353,
                "gap_rejected_minus_accepted": 0.9439376241683959
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.228214591741562,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.335051659768382,
                "rejected_mean_error": 2.167286399525283,
                "gap_rejected_minus_accepted": 0.832234739756901
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.443587231636047,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.828616638051139,
                "rejected_mean_error": 3.3559181785583494,
                "gap_rejected_minus_accepted": 1.5273015405072103
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9186467230319977,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5974243565357942,
                "rejected_mean_error": 3.120926084972563,
                "gap_rejected_minus_accepted": 1.523501728436769
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6192886233329773,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4960489900112153,
                "rejected_mean_error": 2.466644594192505,
                "gap_rejected_minus_accepted": 0.9705956041812898
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2329211235046387,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.3465126350758567,
                "rejected_mean_error": 2.1952214011534013,
                "gap_rejected_minus_accepted": 0.8487087660775445
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.892705651411671,
            "spearman": 0.8601851942548924,
            "auroc_top30_bad": 0.9451413333333334,
            "mae": 0.27715325111746786,
            "mse": 0.16182260475184038,
            "expert_lt_perturb_large": 0.988,
            "expert_lt_other_task": 0.536,
            "expert_lt_simvla_seed0": 0.94,
            "same_context_pred_std": 0.7146057141497009,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.39563687932491304
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3741994610071182
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.532571820795536
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9035110752105713
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.875778406807751,
            "spearman": 0.8340531817300363,
            "auroc_top30_worst": 0.8875245714285714,
            "pairwise_seed_ranking": 0.7236,
            "predicted_best_mean_error": 1.6872633810043336,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.019326713681220964,
            "gap_to_oracle": 0.025414445042610367,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6539229567050934
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9915555261839659
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2798973593235017
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4848266353548716
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7618243932724003,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.564564442343182,
                "rejected_mean_error": 3.108600171089172,
                "gap_rejected_minus_accepted": 1.5440357287459903
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9887828826904297,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4843887138074083,
                "rejected_mean_error": 2.4212070101747116,
                "gap_rejected_minus_accepted": 0.9368182963673033
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6893338561058044,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2798973593235017,
                "rejected_mean_error": 2.1580386711120605,
                "gap_rejected_minus_accepted": 0.8781413117885588
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2746038138866425,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9922695035180344,
                "rejected_mean_error": 1.9617178915913356,
                "gap_rejected_minus_accepted": 0.9694483880733011
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7210004806518553,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5578719998730552,
                "rejected_mean_error": 3.045052947998047,
                "gap_rejected_minus_accepted": 1.4871809481249916
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9174821972846985,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4792021074715782,
                "rejected_mean_error": 2.381535390066722,
                "gap_rejected_minus_accepted": 0.9023332825951438
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.690678596496582,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2729532988071441,
                "rejected_mean_error": 2.140226890563965,
                "gap_rejected_minus_accepted": 0.8672735917568208
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2756222486495972,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.960691138392403,
                "rejected_mean_error": 1.9578822564313756,
                "gap_rejected_minus_accepted": 0.9971911180389725
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
      "best_epoch": 102,
      "best_calib_loss": 0.011359547264873981,
      "train_time_sec": 28.513244152069092,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993210002002813,
            "spearman": 0.998399954585096,
            "auroc_top30_bad": 0.9997647142857143,
            "mae": 0.02548789338076531,
            "mse": 0.0012678737920337436,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6895790319887319,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0029896394871175287
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1657737279817462
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.43709097620472315
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7567799874559045
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9993069682351047,
            "spearman": 0.9992330296172846,
            "auroc_top30_worst": 0.9993137142857144,
            "pairwise_seed_ranking": 0.9364,
            "predicted_best_mean_error": 1.4515037670433522,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07397414639592159,
            "gap_to_oracle": 0.0012447021007537806,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4956251249909401
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7047637901544571
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9815479459881783
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2101435708125432
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.346195650100709,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520845792624685,
                "rejected_mean_error": 2.9578532123565675,
                "gap_rejected_minus_accepted": 1.605768633094099
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8922161757946014,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2101435708125432,
                "rejected_mean_error": 2.420215057849884,
                "gap_rejected_minus_accepted": 1.210071487037341
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5003167986869812,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9815479459881783,
                "rejected_mean_error": 2.0437749391555786,
                "gap_rejected_minus_accepted": 1.0622269931674002
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.036671221256256,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7047637901544571,
                "rejected_mean_error": 1.7819606600443523,
                "gap_rejected_minus_accepted": 1.077196869889895
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.375652694702149,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.364366340438525,
                "rejected_mean_error": 2.9754820704460143,
                "gap_rejected_minus_accepted": 1.6111157300074894
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.906328409910202,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.221353582461675,
                "rejected_mean_error": 2.4378509063720704,
                "gap_rejected_minus_accepted": 1.2164973239103953
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5151693224906921,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9885251237154007,
                "rejected_mean_error": 2.062430703163147,
                "gap_rejected_minus_accepted": 1.0739055794477461
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0460799634456635,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7071686074733734,
                "rejected_mean_error": 1.798247682094574,
                "gap_rejected_minus_accepted": 1.0910790746212007
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.986026523165369,
            "spearman": 0.9767173201505078,
            "auroc_top30_bad": 0.9892518095238095,
            "mae": 0.12105674822065048,
            "mse": 0.023163786083627774,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6889967251523191,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08967788082361221
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1846938401937485
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5019319560527802
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8571031278928121
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9822094982583651,
            "spearman": 0.9639766051690274,
            "auroc_top30_worst": 0.9782826666666665,
            "pairwise_seed_ranking": 0.8692,
            "predicted_best_mean_error": 1.6310806934833526,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.061649097084999216,
            "gap_to_oracle": 0.0054095944166183685,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5249710025787353
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8567532090804516
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1557149042129518
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3779702594539505
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.294772148132324,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.497445727666219,
                "rejected_mean_error": 3.3828792400360106,
                "gap_rejected_minus_accepted": 1.8854335123697916
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.919629544019699,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3773268498122502,
                "rejected_mean_error": 2.6100034835620427,
                "gap_rejected_minus_accepted": 1.2326766337497925
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.612553894519806,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1557149042129518,
                "rejected_mean_error": 2.216263253593445,
                "gap_rejected_minus_accepted": 1.0605483493804932
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3197221457958221,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8587688737022229,
                "rejected_mean_error": 1.9623177066811122,
                "gap_rejected_minus_accepted": 1.1035488329788894
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2925321578979494,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5017610029379527,
                "rejected_mean_error": 3.4114488792419433,
                "gap_rejected_minus_accepted": 1.9096878763039906
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9246450364589691,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3824535568448948,
                "rejected_mean_error": 2.613708452572898,
                "gap_rejected_minus_accepted": 1.2312548957280034
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.609095573425293,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.153469806432724,
                "rejected_mean_error": 2.2319897747039796,
                "gap_rejected_minus_accepted": 1.0785199682712556
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3112807869911194,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.853590045183424,
                "rejected_mean_error": 1.9754346245750387,
                "gap_rejected_minus_accepted": 1.1218445793916147
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9686746482784154,
            "spearman": 0.9770491465727345,
            "auroc_top30_bad": 0.9830133333333334,
            "mae": 0.1818053490905324,
            "mse": 0.09527274759733712,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.731746112469048,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08355238515138626
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18029418247938156
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5135461212694645
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9121187078197797
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9539697638090151,
            "spearman": 0.9739581908212422,
            "auroc_top30_worst": 0.9757622857142858,
            "pairwise_seed_ranking": 0.902,
            "predicted_best_mean_error": 1.8950671384334563,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.08627965366840384,
            "gap_to_oracle": 0.003020737648010252,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6603542995452881
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9910916342185094
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3085622945785522
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5468447383787078
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.735994124412537,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.739303410742018,
                "rejected_mean_error": 3.9352175102233886,
                "gap_rejected_minus_accepted": 2.195914099481371
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.115672528743744,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5463804766106377,
                "rejected_mean_error": 3.1938019785256433,
                "gap_rejected_minus_accepted": 1.6474215019150056
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8324667811393738,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3085622945785522,
                "rejected_mean_error": 2.6092273468017577,
                "gap_rejected_minus_accepted": 1.3006650522232055
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4368805885314941,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9920704821809031,
                "rejected_mean_error": 2.2818574865955936,
                "gap_rejected_minus_accepted": 1.2897870044146904
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7726531505584715,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7585853977998098,
                "rejected_mean_error": 3.9861993408203125,
                "gap_rejected_minus_accepted": 2.2276139430205024
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.121115565299988,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.566712370371436,
                "rejected_mean_error": 3.2120870597778803,
                "gap_rejected_minus_accepted": 1.6453746894064443
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.855105459690094,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.320835688352585,
                "rejected_mean_error": 2.6418578958511354,
                "gap_rejected_minus_accepted": 1.3210222074985505
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4640116393566132,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9984033046260713,
                "rejected_mean_error": 2.3124988761177674,
                "gap_rejected_minus_accepted": 1.3140955714916962
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9789558935528206,
            "spearman": 0.9720654229912977,
            "auroc_top30_bad": 0.9796914285714285,
            "mae": 0.13456584909444208,
            "mse": 0.030585201571821385,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7015081674699911,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07853940910100937
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19748353226184845
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5084206244111061
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8681205741008122
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9605198032910093,
            "spearman": 0.9393159066341804,
            "auroc_top30_worst": 0.9492053333333333,
            "pairwise_seed_ranking": 0.8904,
            "predicted_best_mean_error": 1.6670402847528458,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.039549809932708735,
            "gap_to_oracle": 0.005191348791122596,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6550129382610321
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9783064227264661
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2321609129428863
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4376815376060603
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4645076990127563,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5598347563478683,
                "rejected_mean_error": 3.1511673450469972,
                "gap_rejected_minus_accepted": 1.591332588699129
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.989875316619873,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.43730126478756,
                "rejected_mean_error": 2.5621684789657593,
                "gap_rejected_minus_accepted": 1.1248672141781992
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6714375615119934,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2321609129428863,
                "rejected_mean_error": 2.2057751174926756,
                "gap_rejected_minus_accepted": 0.9736142045497893
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.30574369430542,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9791985697830066,
                "rejected_mean_error": 1.966084169349141,
                "gap_rejected_minus_accepted": 0.9868855995661345
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4154017210006713,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.550651095840666,
                "rejected_mean_error": 3.1100410842895507,
                "gap_rejected_minus_accepted": 1.5593899884488847
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9846936166286469,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4192523645525947,
                "rejected_mean_error": 2.5594814523818,
                "gap_rejected_minus_accepted": 1.1402290878292052
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6688688397407532,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2226707842350006,
                "rejected_mean_error": 2.1905094051361083,
                "gap_rejected_minus_accepted": 0.9678386209011076
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.289705514907837,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9600271010209643,
                "rejected_mean_error": 1.9581059695565126,
                "gap_rejected_minus_accepted": 0.9980788685355483
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
      "best_epoch": 138,
      "best_calib_loss": 0.00525642791762948,
      "train_time_sec": 68.26777839660645,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998649169840359,
            "spearman": 0.9992418508066282,
            "auroc_top30_bad": 0.9999609761904762,
            "mae": 0.01010789472591132,
            "mse": 0.0002062471851091554,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6809490166626716,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00048593005537986755
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16558881744593382
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.43691856357082726
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7565144015406569
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998720975126982,
            "spearman": 0.999867229138686,
            "auroc_top30_worst": 0.9998939047619048,
            "pairwise_seed_ranking": 0.9667,
            "predicted_best_mean_error": 1.4507749670743941,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07470294636487962,
            "gap_to_oracle": 0.0005159021317957535,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4948592979311943
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.704318025135994
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9812624284863471
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2099583992083867
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3163262128829962,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520122395157814,
                "rejected_mean_error": 2.9585042700767517,
                "gap_rejected_minus_accepted": 1.6064920305609702
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.872488558292389,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2099583992083867,
                "rejected_mean_error": 2.4207705726623536,
                "gap_rejected_minus_accepted": 1.210812173453967
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4771305918693542,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9812624284863471,
                "rejected_mean_error": 2.0440604566574097,
                "gap_rejected_minus_accepted": 1.0627980281710625
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0238028168678284,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.704318025135994,
                "rejected_mean_error": 1.7821092483838399,
                "gap_rejected_minus_accepted": 1.077791223247846
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.362243223190308,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.364134051601092,
                "rejected_mean_error": 2.9775726699829104,
                "gap_rejected_minus_accepted": 1.6134386183818183
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8807488083839417,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.221133905172348,
                "rejected_mean_error": 2.4385099382400512,
                "gap_rejected_minus_accepted": 1.2173760330677033
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.483307659626007,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9883355726003646,
                "rejected_mean_error": 2.062620254278183,
                "gap_rejected_minus_accepted": 1.0742846816778182
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.046505182981491,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7067827084064484,
                "rejected_mean_error": 1.7983763151168823,
                "gap_rejected_minus_accepted": 1.091593606710434
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9933024197347521,
            "spearman": 0.9897211691388675,
            "auroc_top30_bad": 0.9956228571428571,
            "mae": 0.06959960764441639,
            "mse": 0.011069927705364552,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7147358311241624,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03974488735198975
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17376172568798065
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.493228693151474
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8528364034334819
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9907845968234477,
            "spearman": 0.9900838234136471,
            "auroc_top30_worst": 0.9904822857142856,
            "pairwise_seed_ranking": 0.9088,
            "predicted_best_mean_error": 1.6279734123945235,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.06475637817382829,
            "gap_to_oracle": 0.002302313327789296,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.521760624408722
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8298107286294302
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1484090810775758
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.373151074086171
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.338925957679749,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5001030107074314,
                "rejected_mean_error": 3.3589636926651,
                "gap_rejected_minus_accepted": 1.8588606819576687
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9093174040317535,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3725184011357572,
                "rejected_mean_error": 2.6243981046798512,
                "gap_rejected_minus_accepted": 1.251879703544094
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6172387599945068,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1484090810775758,
                "rejected_mean_error": 2.223569076728821,
                "gap_rejected_minus_accepted": 1.0751599956512452
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2486039102077484,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8310694347936124,
                "rejected_mean_error": 1.9715705608736362,
                "gap_rejected_minus_accepted": 1.1405011260800237
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3322134494781492,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5069407482941946,
                "rejected_mean_error": 3.3648311710357666,
                "gap_rejected_minus_accepted": 1.857890422741572
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9228534400463104,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3764052102591264,
                "rejected_mean_error": 2.631661481327481,
                "gap_rejected_minus_accepted": 1.2552562710683544
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6097870469093323,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.147644879102707,
                "rejected_mean_error": 2.2378147020339965,
                "gap_rejected_minus_accepted": 1.0901698229312895
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2570009231567383,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8274502427805037,
                "rejected_mean_error": 1.9842410820690706,
                "gap_rejected_minus_accepted": 1.1567908392885669
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.968297430381208,
            "spearman": 0.9844750678187434,
            "auroc_top30_bad": 0.9914582857142856,
            "mae": 0.139158561594598,
            "mse": 0.08504788750139271,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7542036530453735,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05302609279751778
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17717309764623643
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5110620354235172
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9050817943930626
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9469625580926451,
            "spearman": 0.9922502422081552,
            "auroc_top30_worst": 0.9982384761904761,
            "pairwise_seed_ranking": 0.9208,
            "predicted_best_mean_error": 1.8933125283718109,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.0880342637300493,
            "gap_to_oracle": 0.0012661275863647958,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6514002680778503
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9854783155979254
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3003811447143554
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5235837412033
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.804422640800476,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7552513700061374,
                "rejected_mean_error": 3.7916858768463135,
                "gap_rejected_minus_accepted": 2.036434506840176
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.223560929298401,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5227733990425998,
                "rejected_mean_error": 3.264472367283635,
                "gap_rejected_minus_accepted": 1.7416989682410353
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8424330949783325,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3003811447143554,
                "rejected_mean_error": 2.6174084966659548,
                "gap_rejected_minus_accepted": 1.3170273519515994
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.447150856256485,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9863598716144745,
                "rejected_mean_error": 2.2837650864966523,
                "gap_rejected_minus_accepted": 1.2974052148821777
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.84121310710907,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7770260173744625,
                "rejected_mean_error": 3.8202337646484374,
                "gap_rejected_minus_accepted": 2.043207747273975
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2783287167549133,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.540639381198322,
                "rejected_mean_error": 3.289478313355219,
                "gap_rejected_minus_accepted": 1.748838932156897
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8769004940986633,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3131129186153412,
                "rejected_mean_error": 2.649580665588379,
                "gap_rejected_minus_accepted": 1.3364677469730377
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.479519248008728,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9923824275296832,
                "rejected_mean_error": 2.3145272999523794,
                "gap_rejected_minus_accepted": 1.322144872422696
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9880663621476145,
            "spearman": 0.9861724397366588,
            "auroc_top30_bad": 0.987648,
            "mae": 0.09159811140596867,
            "mse": 0.02219091193196674,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.948,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7747059816235287,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.024194218575954437
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18047306358814239
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5002861907601357
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8639551212708155
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9728243424723826,
            "spearman": 0.9707384931446357,
            "auroc_top30_worst": 0.9597348571428571,
            "pairwise_seed_ranking": 0.9212,
            "predicted_best_mean_error": 1.6629005460739135,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.043689548611641094,
            "gap_to_oracle": 0.0010516101121902377,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6300264613628388
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9504945588608583
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2210610590457915
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4309458886700144
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.708483886718752,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5593121089140574,
                "rejected_mean_error": 3.155871171951294,
                "gap_rejected_minus_accepted": 1.5965590630372366
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0713319182395935,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4304194904887688,
                "rejected_mean_error": 2.582769828863418,
                "gap_rejected_minus_accepted": 1.1523503383746494
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7429388761520386,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2210610590457915,
                "rejected_mean_error": 2.2168749713897706,
                "gap_rejected_minus_accepted": 0.9958139123439791
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3559585809707642,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9514407727855463,
                "rejected_mean_error": 1.9753565177591785,
                "gap_rejected_minus_accepted": 1.0239157449736322
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6486923217773435,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5499693193700579,
                "rejected_mean_error": 3.1161770725250246,
                "gap_rejected_minus_accepted": 1.5662077531549667
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0531294345855713,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4220915339528557,
                "rejected_mean_error": 2.55105407654293,
                "gap_rejected_minus_accepted": 1.1289625425900742
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7485305666923523,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.209979192018509,
                "rejected_mean_error": 2.2032009973526,
                "gap_rejected_minus_accepted": 0.9932218053340909
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3567019999027252,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9297307488464174,
                "rejected_mean_error": 1.968312762000344,
                "gap_rejected_minus_accepted": 1.0385820131539267
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
      "best_epoch": 141,
      "best_calib_loss": 0.006518299225717783,
      "train_time_sec": 70.3377914428711,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998958824961918,
            "spearman": 0.9992708525744229,
            "auroc_top30_bad": 0.9999778571428571,
            "mae": 0.01419788523113093,
            "mse": 0.00035007163179786525,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6853258449488104,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0007534039989113807
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16556137501448392
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.43689617818817494
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7565111584121982
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998574594178185,
            "spearman": 0.9998265259290529,
            "auroc_top30_worst": 0.9998885714285715,
            "pairwise_seed_ranking": 0.969,
            "predicted_best_mean_error": 1.450632246941328,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07484566649794577,
            "gap_to_oracle": 0.00037318199872959923,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.49503311747312545
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7042978602647781
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9812608019471168
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.209947597638766
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.334014773368836,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520030976997481,
                "rejected_mean_error": 2.958586546421051,
                "gap_rejected_minus_accepted": 1.6065834487213029
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8868891894817352,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.209947597638766,
                "rejected_mean_error": 2.4208029773712156,
                "gap_rejected_minus_accepted": 1.2108553797324497
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4922738671302795,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9812608019471168,
                "rejected_mean_error": 2.04406208319664,
                "gap_rejected_minus_accepted": 1.062801281249523
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0417066514492035,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7042978602647781,
                "rejected_mean_error": 1.7821159700075786,
                "gap_rejected_minus_accepted": 1.0778181097428003
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3900821924209597,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.3641470387909147,
                "rejected_mean_error": 2.977455785274506,
                "gap_rejected_minus_accepted": 1.6133087464835911
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9070726037025452,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2211054747104644,
                "rejected_mean_error": 2.438595229625702,
                "gap_rejected_minus_accepted": 1.2174897549152375
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4998666048049927,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9882957895994187,
                "rejected_mean_error": 2.062660037279129,
                "gap_rejected_minus_accepted": 1.0743642476797102
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.056639850139618,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7069192826747894,
                "rejected_mean_error": 1.7983307903607686,
                "gap_rejected_minus_accepted": 1.0914115076859792
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9910892614980622,
            "spearman": 0.9850892449699019,
            "auroc_top30_bad": 0.9951504761904761,
            "mae": 0.08067448458633153,
            "mse": 0.014036705564249727,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7100536864965625,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06425963923335075
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19172486491203308
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4942492887020111
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8526447303454081
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9935101430127411,
            "spearman": 0.98842415591946,
            "auroc_top30_worst": 0.9904060952380952,
            "pairwise_seed_ranking": 0.9224,
            "predicted_best_mean_error": 1.6276050354242324,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.06512475514411942,
            "gap_to_oracle": 0.0019339363574981672,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.525758930683136
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8333915873215749
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1503170057296752
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3732594762529646
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.405942606925965,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4981754586961535,
                "rejected_mean_error": 3.3763116607666017,
                "gap_rejected_minus_accepted": 1.8781362020704482
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9447226822376251,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.372627866560774,
                "rejected_mean_error": 2.6240704078643846,
                "gap_rejected_minus_accepted": 1.2514425413036105
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6279471516609192,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1503170057296752,
                "rejected_mean_error": 2.221661152076721,
                "gap_rejected_minus_accepted": 1.071344146347046
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2085091173648834,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8349980420578783,
                "rejected_mean_error": 1.9702582299518483,
                "gap_rejected_minus_accepted": 1.1352601878939699
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.413068389892578,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5027562606334686,
                "rejected_mean_error": 3.4024915599823,
                "gap_rejected_minus_accepted": 1.8997352993488315
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9507665932178497,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3767149803791454,
                "rejected_mean_error": 2.630742004939488,
                "gap_rejected_minus_accepted": 1.2540270245603427
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.619011402130127,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1481982553005219,
                "rejected_mean_error": 2.2372613258361818,
                "gap_rejected_minus_accepted": 1.0890630705356599
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2135323584079742,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.827614159338058,
                "rejected_mean_error": 1.9841858588437984,
                "gap_rejected_minus_accepted": 1.1565716995057405
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9736679115240259,
            "spearman": 0.9797148757030317,
            "auroc_top30_bad": 0.9930598095238096,
            "mae": 0.1422154159320764,
            "mse": 0.06518380316604357,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7630909545076742,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08451550379395485
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18219297136068344
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.512617345482111
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.904487050028642
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9665493946589535,
            "spearman": 0.99219618726156,
            "auroc_top30_worst": 0.9980007619047618,
            "pairwise_seed_ranking": 0.9316,
            "predicted_best_mean_error": 1.8929926537275314,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.0883541383743287,
            "gap_to_oracle": 0.0009462529420853905,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6589753232002258
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.983846956338638
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3021084533691407
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5233138554385985
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9303127765655517,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7404170971976387,
                "rejected_mean_error": 3.925194332122803,
                "gap_rejected_minus_accepted": 2.184777234925164
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2695725560188293,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5225394938773253,
                "rejected_mean_error": 3.265172588177763,
                "gap_rejected_minus_accepted": 1.7426330943004378
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.863027811050415,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3021084533691407,
                "rejected_mean_error": 2.6156811880111692,
                "gap_rejected_minus_accepted": 1.3135727346420285
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4140654802322388,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9849579079082599,
                "rejected_mean_error": 2.2842334052160176,
                "gap_rejected_minus_accepted": 1.2992754973077578
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.950084662437439,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7596449066532982,
                "rejected_mean_error": 3.976663761138916,
                "gap_rejected_minus_accepted": 2.2170188544856178
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3424354195594788,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5408730275809446,
                "rejected_mean_error": 3.2887847915528314,
                "gap_rejected_minus_accepted": 1.7479117639718869
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8897443413734436,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3153199813365937,
                "rejected_mean_error": 2.6473736028671264,
                "gap_rejected_minus_accepted": 1.3320536215305327
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4467597901821136,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9910634145850227,
                "rejected_mean_error": 2.314971673297372,
                "gap_rejected_minus_accepted": 1.3239082587123492
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9904628022464843,
            "spearman": 0.9889836885784407,
            "auroc_top30_bad": 0.9917539047619048,
            "mae": 0.08066859090466641,
            "mse": 0.014062713362962912,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7367114888180548,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03593872618675232
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.183222371840477
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5012143716454506
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8601474260091782
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9814288958778253,
            "spearman": 0.978421742093915,
            "auroc_top30_worst": 0.9762102857142856,
            "pairwise_seed_ranking": 0.9208,
            "predicted_best_mean_error": 1.6631279175281524,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.04346217715740219,
            "gap_to_oracle": 0.0012789815664291382,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6315135447978973
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9511812143027782
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.219931449174881
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.426675814078815
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.482539701461793,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.559700943549474,
                "rejected_mean_error": 3.152371660232544,
                "gap_rejected_minus_accepted": 1.5926707166830698
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9981809556484222,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.426303303769711,
                "rejected_mean_error": 2.5950920875080095,
                "gap_rejected_minus_accepted": 1.1687887837382984
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.656771957874298,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.219931449174881,
                "rejected_mean_error": 2.218004581260681,
                "gap_rejected_minus_accepted": 0.9980731320858001
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.336903601884842,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.952873827645573,
                "rejected_mean_error": 1.9748778132008131,
                "gap_rejected_minus_accepted": 1.02200398555524
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.442061352729797,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5512216420968374,
                "rejected_mean_error": 3.1049061679840086,
                "gap_rejected_minus_accepted": 1.5536845258871712
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9534966051578522,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.415588495724979,
                "rejected_mean_error": 2.570356745568533,
                "gap_rejected_minus_accepted": 1.154768249843554
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6629835367202759,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2074053366184234,
                "rejected_mean_error": 2.2057748527526857,
                "gap_rejected_minus_accepted": 0.9983695161342623
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3232362568378448,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.929971824089686,
                "rejected_mean_error": 1.9682315441376386,
                "gap_rejected_minus_accepted": 1.0382597200479524
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
      "best_epoch": 156,
      "best_calib_loss": 0.006852820515632629,
      "train_time_sec": 79.66387844085693,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993392624712105,
            "spearman": 0.9983449350219021,
            "auroc_top30_bad": 0.9997091904761906,
            "mae": 0.02585596663827673,
            "mse": 0.001240280800688952,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6863654978393456,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0007449966110289097
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16579245020598174
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4372461166761816
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7567771648660302
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9992949470232451,
            "spearman": 0.9990673166666482,
            "auroc_top30_worst": 0.9993988571428571,
            "pairwise_seed_ranking": 0.9658,
            "predicted_best_mean_error": 1.4507691868841648,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07470872655510896,
            "gap_to_oracle": 0.0005101219415664104,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4957888368964195
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7048681395292282
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9820673000454903
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2101672717809677
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.34254333972931,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520921141372786,
                "rejected_mean_error": 2.9577853984832765,
                "gap_rejected_minus_accepted": 1.605693284345998
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.904915988445282,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2101672717809677,
                "rejected_mean_error": 2.4201439549446104,
                "gap_rejected_minus_accepted": 1.2099766831636427
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.495562493801117,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9820673000454903,
                "rejected_mean_error": 2.0432555850982665,
                "gap_rejected_minus_accepted": 1.0611882850527763
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0427219569683075,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7048681395292282,
                "rejected_mean_error": 1.7819258769194286,
                "gap_rejected_minus_accepted": 1.0770577373902004
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.383027720451355,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.3642535295089087,
                "rejected_mean_error": 2.976497368812561,
                "gap_rejected_minus_accepted": 1.6122438393036524
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9329076707363129,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2211535597642262,
                "rejected_mean_error": 2.4384509744644167,
                "gap_rejected_minus_accepted": 1.2172974147001905
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.511841595172882,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9889259415864945,
                "rejected_mean_error": 2.0620298852920533,
                "gap_rejected_minus_accepted": 1.0731039437055587
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0693979561328888,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7077222683429718,
                "rejected_mean_error": 1.7980631284713746,
                "gap_rejected_minus_accepted": 1.0903408601284028
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9909498420144534,
            "spearman": 0.9829260442368,
            "auroc_top30_bad": 0.9949257142857143,
            "mae": 0.08358384411875595,
            "mse": 0.014408394212713012,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7173109129321414,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0668990306854248
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1965133267402649
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.49457653574943544
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8526103194872539
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9923309376579843,
            "spearman": 0.9874678724274385,
            "auroc_top30_worst": 0.9947550476190475,
            "pairwise_seed_ranking": 0.9184,
            "predicted_best_mean_error": 1.6282817871570587,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.06444800341129309,
            "gap_to_oracle": 0.0026106880903244978,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5282003479003906
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8343157730041406
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.151373903465271
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3721487346742707
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.449990606307985,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.496612630844116,
                "rejected_mean_error": 3.3903771114349364,
                "gap_rejected_minus_accepted": 1.8937644805908203
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9696819484233856,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3715203538648346,
                "rejected_mean_error": 2.6273858691937626,
                "gap_rejected_minus_accepted": 1.255865515328928
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.658076524734497,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.151373903465271,
                "rejected_mean_error": 2.2206042543411253,
                "gap_rejected_minus_accepted": 1.0692303508758543
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1940483748912811,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8360529269654149,
                "rejected_mean_error": 1.9699058511086691,
                "gap_rejected_minus_accepted": 1.1338529241432542
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4716371059417725,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5033108762900034,
                "rejected_mean_error": 3.3975000190734863,
                "gap_rejected_minus_accepted": 1.894189142783483
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9990310966968536,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3749261570168052,
                "rejected_mean_error": 2.6360516869832598,
                "gap_rejected_minus_accepted": 1.2611255299664546
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6613061428070068,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1499372298717498,
                "rejected_mean_error": 2.2355223512649536,
                "gap_rejected_minus_accepted": 1.0855851213932037
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2105628550052643,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8300008504163652,
                "rejected_mean_error": 1.9833817864484329,
                "gap_rejected_minus_accepted": 1.1533809360320677
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9745251433130282,
            "spearman": 0.9770144351913334,
            "auroc_top30_bad": 0.9917043809523809,
            "mae": 0.13407073262699995,
            "mse": 0.05913207995307755,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7686432539331374,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07291134205460549
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18640977779626847
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5132525092661381
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9039115805029869
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9685997182807147,
            "spearman": 0.9908662131623766,
            "auroc_top30_worst": 0.9990064761904762,
            "pairwise_seed_ranking": 0.9268,
            "predicted_best_mean_error": 1.8933253655433655,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.08802142655849465,
            "gap_to_oracle": 0.001278964757919443,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.654772469997406
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9820851091391001
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.303203673553467
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5233105816312436
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.030132007598877,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.742881691508823,
                "rejected_mean_error": 3.9030129833221436,
                "gap_rejected_minus_accepted": 2.160131291813321
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.311797559261322,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.522518432127628,
                "rejected_mean_error": 3.2652356388469856,
                "gap_rejected_minus_accepted": 1.7427172067193577
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8223347067832947,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.303203673553467,
                "rejected_mean_error": 2.614585967826843,
                "gap_rejected_minus_accepted": 1.3113822942733762
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3437926769256592,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9835898937127842,
                "rejected_mean_error": 2.2846903832770464,
                "gap_rejected_minus_accepted": 1.3011004895642624
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0797499895095823,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7608780149618786,
                "rejected_mean_error": 3.965565786361694,
                "gap_rejected_minus_accepted": 2.204687771399816
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3924644589424133,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5408077212897213,
                "rejected_mean_error": 3.2889786372109064,
                "gap_rejected_minus_accepted": 1.7481709159211851
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8431735634803772,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.31755632853508,
                "rejected_mean_error": 2.64513725566864,
                "gap_rejected_minus_accepted": 1.3275809271335601
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4093059599399567,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9888334004651933,
                "rejected_mean_error": 2.31572296147678,
                "gap_rejected_minus_accepted": 1.3268895610115867
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.991779680580928,
            "spearman": 0.9885240344949882,
            "auroc_top30_bad": 0.9953729523809524,
            "mae": 0.0790939780552595,
            "mse": 0.012456128245906578,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7401634432379812,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0635581745505333
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19175069074630738
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5016558242440223
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8584544948975246
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9910464501042484,
            "spearman": 0.9892055564835562,
            "auroc_top30_worst": 0.9918598095238095,
            "pairwise_seed_ranking": 0.9312,
            "predicted_best_mean_error": 1.6631661858558655,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.04342390882968905,
            "gap_to_oracle": 0.0013172498941422806,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6320593020915986
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9509964433427041
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2184916023731232
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.419672323728421
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.47199981212616,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5567236352761586,
                "rejected_mean_error": 3.1791674346923826,
                "gap_rejected_minus_accepted": 1.622443799416224
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0509005188941956,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4189764031287573,
                "rejected_mean_error": 2.6170259721743796,
                "gap_rejected_minus_accepted": 1.1980495690456223
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6793898344039917,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2184916023731232,
                "rejected_mean_error": 2.219444428062439,
                "gap_rejected_minus_accepted": 1.0009528256893159
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2992816269397736,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9519846893537539,
                "rejected_mean_error": 1.9751748252449322,
                "gap_rejected_minus_accepted": 1.0231901358911784
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.435299301147461,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5485859501361847,
                "rejected_mean_error": 3.128627395629883,
                "gap_rejected_minus_accepted": 1.5800414454936982
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.016373038291931,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4070276865028442,
                "rejected_mean_error": 2.595767401513599,
                "gap_rejected_minus_accepted": 1.188739715010755
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6767053604125977,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2078509562015534,
                "rejected_mean_error": 2.2053292331695555,
                "gap_rejected_minus_accepted": 0.9974782769680022
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.292383760213852,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9287586973773109,
                "rejected_mean_error": 1.968640244580845,
                "gap_rejected_minus_accepted": 1.0398815472035343
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
      "best_epoch": 129,
      "best_calib_loss": 0.006208803970366716,
      "train_time_sec": 54.87902641296387,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998478512617053,
            "spearman": 0.9992686424880783,
            "auroc_top30_bad": 0.9999021904761904,
            "mae": 0.01350622609263487,
            "mse": 0.0003849363480004626,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6856437745360078,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0005495213866233826
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16555016872137784
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4369066394470632
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7565391715303064
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9997389967009193,
            "spearman": 0.9997107103244147,
            "auroc_top30_worst": 0.9997685714285715,
            "pairwise_seed_ranking": 0.9705,
            "predicted_best_mean_error": 1.4505101909935474,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07496772244572636,
            "gap_to_oracle": 0.0002511260509490132,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.49486239844560626
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7043048860788346
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9813463080048561
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.210028754591942
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3438100576400758,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520545677675142,
                "rejected_mean_error": 2.9581233158111573,
                "gap_rejected_minus_accepted": 1.606068748043643
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8962375223636627,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.210028754591942,
                "rejected_mean_error": 2.420559506511688,
                "gap_rejected_minus_accepted": 1.2105307519197461
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4908756613731384,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9813463080048561,
                "rejected_mean_error": 2.043976577138901,
                "gap_rejected_minus_accepted": 1.0626302691340448
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0308711528778076,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7043048860788346,
                "rejected_mean_error": 1.7821136280695598,
                "gap_rejected_minus_accepted": 1.0778087419907252
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3755828142166138,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.3641494197977915,
                "rejected_mean_error": 2.977434356212616,
                "gap_rejected_minus_accepted": 1.6132849364148245
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9025441110134125,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2211388250192006,
                "rejected_mean_error": 2.4384951786994935,
                "gap_rejected_minus_accepted": 1.217356353680293
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.49894779920578,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9882847143411636,
                "rejected_mean_error": 2.062671112537384,
                "gap_rejected_minus_accepted": 1.0743863981962205
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0510669648647308,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7067895233631134,
                "rejected_mean_error": 1.7983740434646607,
                "gap_rejected_minus_accepted": 1.0915845201015473
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9920852769593682,
            "spearman": 0.9872657921559612,
            "auroc_top30_bad": 0.9954460952380952,
            "mae": 0.08139367800596092,
            "mse": 0.01292502451884333,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6960493807368128,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.042051878809928896
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1877810158252716
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.495216793012619
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8524103232383728
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9937616313064079,
            "spearman": 0.9896083389493371,
            "auroc_top30_worst": 0.9954864761904761,
            "pairwise_seed_ranking": 0.9284,
            "predicted_best_mean_error": 1.6278117126226426,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.06491807794570925,
            "gap_to_oracle": 0.002140613555908333,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.527761146068573
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8362679519714453
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1503182010650634
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3716652084515293
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4148057460784926,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4967983133527967,
                "rejected_mean_error": 3.3887059688568115,
                "gap_rejected_minus_accepted": 1.8919076555040149
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9364479780197144,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3710885424496906,
                "rejected_mean_error": 2.6286785442608234,
                "gap_rejected_minus_accepted": 1.2575900018111328
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.621084988117218,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1503182010650634,
                "rejected_mean_error": 2.221659956741333,
                "gap_rejected_minus_accepted": 1.0713417556762697
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1833781898021698,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8378879490751809,
                "rejected_mean_error": 1.9692928714711486,
                "gap_rejected_minus_accepted": 1.1314049223959677
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4311193227767944,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5014479211966196,
                "rejected_mean_error": 3.4142666149139402,
                "gap_rejected_minus_accepted": 1.9128186937173206
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9592090845108032,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3747038342417244,
                "rejected_mean_error": 2.636711597442627,
                "gap_rejected_minus_accepted": 1.2620077632009026
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6321690678596497,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.148459184408188,
                "rejected_mean_error": 2.2370003967285155,
                "gap_rejected_minus_accepted": 1.0885412123203275
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1921404600143433,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8336631319825611,
                "rejected_mean_error": 1.9821479696640993,
                "gap_rejected_minus_accepted": 1.1484848376815382
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9692537373341668,
            "spearman": 0.9815979154136635,
            "auroc_top30_bad": 0.9945775238095238,
            "mae": 0.14584903393103865,
            "mse": 0.0767125743853458,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7607776540523278,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08213137033581734
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18211269456148146
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5111397950708866
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9042656779964765
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9562791157429993,
            "spearman": 0.9925131625684241,
            "auroc_top30_worst": 0.9981287619047619,
            "pairwise_seed_ranking": 0.9204,
            "predicted_best_mean_error": 1.8937462126016618,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.0876005795001984,
            "gap_to_oracle": 0.0016998118162157017,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6624988451004028
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9847916995103543
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3007952297210694
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5236090621206044
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.841688370704651,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7506802793078953,
                "rejected_mean_error": 3.832825693130493,
                "gap_rejected_minus_accepted": 2.082145413822598
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.238414704799652,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5228460223086997,
                "rejected_mean_error": 3.264254961531764,
                "gap_rejected_minus_accepted": 1.7414089392230645
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8447955250740051,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3007952297210694,
                "rejected_mean_error": 2.6169944116592405,
                "gap_rejected_minus_accepted": 1.316199181938171
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4201380908489227,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9858288509777179,
                "rejected_mean_error": 2.2839424711917484,
                "gap_rejected_minus_accepted": 1.2981136202140307
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.861394000053406,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.765603844192293,
                "rejected_mean_error": 3.9230333232879637,
                "gap_rejected_minus_accepted": 2.1574294790956707
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.311886429786682,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5410664360472226,
                "rejected_mean_error": 3.288210706105308,
                "gap_rejected_minus_accepted": 1.7471442700580853
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8787175416946411,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.313997960805893,
                "rejected_mean_error": 2.648695623397827,
                "gap_rejected_minus_accepted": 1.3346976625919342
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.436304360628128,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9919637417982495,
                "rejected_mean_error": 2.314668354503611,
                "gap_rejected_minus_accepted": 1.3227046127053614
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.992056709169562,
            "spearman": 0.9905275799314243,
            "auroc_top30_bad": 0.9939672380952381,
            "mae": 0.07581815647030307,
            "mse": 0.011624241627116323,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7261525554480535,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04599476736783981
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18369882266521453
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5011203333497047
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8586406463384628
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9859628005331004,
            "spearman": 0.9846914769225453,
            "auroc_top30_worst": 0.9885714285714285,
            "pairwise_seed_ranking": 0.908,
            "predicted_best_mean_error": 1.664106567621231,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.04248352706432357,
            "gap_to_oracle": 0.002257631659507764,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6332965028285981
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9525671288944207
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2197952810764312
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4215912454481572
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4187309503555308,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5594419586658477,
                "rejected_mean_error": 3.1547025241851805,
                "gap_rejected_minus_accepted": 1.5952605655193328
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9872552156448364,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.421169250631027,
                "rejected_mean_error": 2.6104614414726965,
                "gap_rejected_minus_accepted": 1.1892921908416696
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.676885962486267,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2197952810764312,
                "rejected_mean_error": 2.2181407493591307,
                "gap_rejected_minus_accepted": 0.9983454682826995
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.325992614030838,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9535298390319934,
                "rejected_mean_error": 1.974658675992756,
                "gap_rejected_minus_accepted": 1.0211288369607625
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.36596360206604,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5499383069409265,
                "rejected_mean_error": 3.116456184387207,
                "gap_rejected_minus_accepted": 1.5665178774462807
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9638852179050446,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4101853442383323,
                "rejected_mean_error": 2.5863946714098494,
                "gap_rejected_minus_accepted": 1.176209327171517
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6717225313186646,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2065998594760894,
                "rejected_mean_error": 2.2065803298950195,
                "gap_rejected_minus_accepted": 0.9999804704189301
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3250043392181396,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9292037643137432,
                "rejected_mean_error": 1.9684903022439721,
                "gap_rejected_minus_accepted": 1.039286537930229
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
      "best_epoch": 94,
      "best_calib_loss": 0.006880063563585281,
      "train_time_sec": 72.6251175403595,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997982116607828,
            "spearman": 0.9990139969520085,
            "auroc_top30_bad": 0.9998983809523809,
            "mae": 0.023490343294327157,
            "mse": 0.0009382242906249109,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6934769507887238,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0008351264260709286
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16570331339091063
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4369583909653127
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7565533815955122
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9997838464188209,
            "spearman": 0.9997180224287142,
            "auroc_top30_worst": 0.9997470476190476,
            "pairwise_seed_ranking": 0.9639,
            "predicted_best_mean_error": 1.4507332746386528,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07474463880062099,
            "gap_to_oracle": 0.000474209696054384,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4949456245303154
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7044574078798294
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9813777850270271
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.209973947819074
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.360462665557862,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520066883365314,
                "rejected_mean_error": 2.9585542306900026,
                "gap_rejected_minus_accepted": 1.6065475423534712
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9157566130161285,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.209973947819074,
                "rejected_mean_error": 2.420723926830292,
                "gap_rejected_minus_accepted": 1.2107499790112177
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5118884444236755,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9813777850270271,
                "rejected_mean_error": 2.04394510011673,
                "gap_rejected_minus_accepted": 1.0625673150897028
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0433281064033508,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7044574078798294,
                "rejected_mean_error": 1.782062787469228,
                "gap_rejected_minus_accepted": 1.0776053795893987
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3993435859680177,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.3640916144185595,
                "rejected_mean_error": 2.977954604625702,
                "gap_rejected_minus_accepted": 1.6138629902071424
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9296884536743164,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.221132358789444,
                "rejected_mean_error": 2.4385145773887635,
                "gap_rejected_minus_accepted": 1.2173822185993195
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.517701506614685,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9883865798711777,
                "rejected_mean_error": 2.06256924700737,
                "gap_rejected_minus_accepted": 1.0741826671361923
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0562153160572052,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7068761441707611,
                "rejected_mean_error": 1.7983451698621113,
                "gap_rejected_minus_accepted": 1.0914690256913504
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9905513345728976,
            "spearman": 0.98407997128291,
            "auroc_top30_bad": 0.9949980952380952,
            "mae": 0.08458937379385043,
            "mse": 0.014834319484483669,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7029864206753118,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0659950003027916
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18941900351047516
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.49500669655799867
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8526584204673767
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9925234314325521,
            "spearman": 0.9857175194352126,
            "auroc_top30_worst": 0.9884617142857143,
            "pairwise_seed_ranking": 0.9204,
            "predicted_best_mean_error": 1.6275571073293686,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.06517268323898318,
            "gap_to_oracle": 0.0018860082626344088,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5228214282989502
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8356237648389279
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.15087299785614
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.374211582674909
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4604521274566653,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4975847250620524,
                "rejected_mean_error": 3.3816282634735106,
                "gap_rejected_minus_accepted": 1.8840435384114582
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9378316402435303,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.373658176292859,
                "rejected_mean_error": 2.620986062116897,
                "gap_rejected_minus_accepted": 1.2473278858240382
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6282203197479248,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.15087299785614,
                "rejected_mean_error": 2.2211051599502563,
                "gap_rejected_minus_accepted": 1.0702321620941162
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2095883786678314,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8374525731363998,
                "rejected_mean_error": 1.9694383065499517,
                "gap_rejected_minus_accepted": 1.131985733413552
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4692036628723146,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.501817346016566,
                "rejected_mean_error": 3.410941791534424,
                "gap_rejected_minus_accepted": 1.909124445517858
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9703079164028168,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.377740794165249,
                "rejected_mean_error": 2.627697129098196,
                "gap_rejected_minus_accepted": 1.249956334932947
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6358709931373596,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1502362954616547,
                "rejected_mean_error": 2.235223285675049,
                "gap_rejected_minus_accepted": 1.0849869902133942
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2127761244773865,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8328892101371099,
                "rejected_mean_error": 1.9824087026922461,
                "gap_rejected_minus_accepted": 1.1495194925551362
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9745039839788225,
            "spearman": 0.9809637827459324,
            "auroc_top30_bad": 0.9947207619047618,
            "mae": 0.13622739852338714,
            "mse": 0.062037613798355554,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7722499035447054,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08216992393136024
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18235607854127883
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5121003663599492
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9039756872534752
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9708650845821287,
            "spearman": 0.9945263068968365,
            "auroc_top30_worst": 0.9989363809523809,
            "pairwise_seed_ranking": 0.9276,
            "predicted_best_mean_error": 1.8936827894449233,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.08766400265693686,
            "gap_to_oracle": 0.0016363886594772392,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6527838625907898
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9819061759954844
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3007954238891601
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5234988146245099
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9769812583923345,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7406657016542222,
                "rejected_mean_error": 3.92295689201355,
                "gap_rejected_minus_accepted": 2.1822911903593276
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.283531367778778,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.522735657152524,
                "rejected_mean_error": 3.2645853517916255,
                "gap_rejected_minus_accepted": 1.7418496946391016
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8642207980155945,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3007954238891601,
                "rejected_mean_error": 2.61699421749115,
                "gap_rejected_minus_accepted": 1.3161987936019899
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4302814602851868,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9829881027483711,
                "rejected_mean_error": 2.284891408433782,
                "gap_rejected_minus_accepted": 1.3019033056854108
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0244840145111085,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7597288819154104,
                "rejected_mean_error": 3.975907983779907,
                "gap_rejected_minus_accepted": 2.2161791018644967
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.362407863140106,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5408730275809446,
                "rejected_mean_error": 3.2887847915528314,
                "gap_rejected_minus_accepted": 1.7479117639718869
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8895636796951294,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3137334811687469,
                "rejected_mean_error": 2.648960103034973,
                "gap_rejected_minus_accepted": 1.3352266218662263
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4725299179553986,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9888121509362781,
                "rejected_mean_error": 2.3157301204089813,
                "gap_rejected_minus_accepted": 1.3269179694727034
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9895591344903828,
            "spearman": 0.9868455832804827,
            "auroc_top30_bad": 0.9889432380952381,
            "mae": 0.09214470929748761,
            "mse": 0.017050871496499028,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7543168429160161,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03793375730514526
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18368590581417082
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5014749242424965
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8619230097214381
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9793655922846672,
            "spearman": 0.9724671823789969,
            "auroc_top30_worst": 0.9712274285714285,
            "pairwise_seed_ranking": 0.9164,
            "predicted_best_mean_error": 1.6632664108276367,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.04332368385791785,
            "gap_to_oracle": 0.0014174748659134817,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6297017891407013
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9560956336939946
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2213967928409577
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4268907875712238
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.558357763290406,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5592431268956926,
                "rejected_mean_error": 3.156492010116577,
                "gap_rejected_minus_accepted": 1.5972488832208844
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0791388154029846,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4263845599766347,
                "rejected_mean_error": 2.5948488380962287,
                "gap_rejected_minus_accepted": 1.168464278119594
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7246678471565247,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2213967928409577,
                "rejected_mean_error": 2.2165392375946045,
                "gap_rejected_minus_accepted": 0.9951424447536468
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.352799415588379,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9569972918246882,
                "rejected_mean_error": 1.9735003913352176,
                "gap_rejected_minus_accepted": 1.0165030995105293
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.512914896011352,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5499383069409265,
                "rejected_mean_error": 3.116456184387207,
                "gap_rejected_minus_accepted": 1.5665178774462807
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.050297796726227,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.414465470906885,
                "rejected_mean_error": 2.573690168441288,
                "gap_rejected_minus_accepted": 1.1592246975344032
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7167723178863525,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2093376896381378,
                "rejected_mean_error": 2.2038424997329713,
                "gap_rejected_minus_accepted": 0.9945048100948335
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3530222475528717,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.932400274371344,
                "rejected_mean_error": 1.9674134031336574,
                "gap_rejected_minus_accepted": 1.0350131287623134
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
      "best_epoch": 149,
      "best_calib_loss": 0.0069025917910039425,
      "train_time_sec": 72.87074613571167,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997793213662218,
            "spearman": 0.99913481029995,
            "auroc_top30_bad": 0.9998453333333333,
            "mae": 0.017397015040151655,
            "mse": 0.0006295197901356252,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6896609411808896,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0003732055649161339
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16562760079354047
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4369650061748922
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7565345593387882
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9996871019203467,
            "spearman": 0.9996087192483302,
            "auroc_top30_worst": 0.9997405714285714,
            "pairwise_seed_ranking": 0.9669,
            "predicted_best_mean_error": 1.4506246736347674,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07485323980450631,
            "gap_to_oracle": 0.00036560869216906156,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.49500595790147783
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7043645185709
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9813887297272682
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2099879190524419
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.337590861320496,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520370508366162,
                "rejected_mean_error": 2.9582809681892397,
                "gap_rejected_minus_accepted": 1.6062439173526235
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8974968492984772,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2099879190524419,
                "rejected_mean_error": 2.420682013130188,
                "gap_rejected_minus_accepted": 1.210694094077746
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.497678816318512,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9813887297272682,
                "rejected_mean_error": 2.0439341554164887,
                "gap_rejected_minus_accepted": 1.0625454256892204
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.046875387430191,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7043645185709,
                "rejected_mean_error": 1.7820937505722045,
                "gap_rejected_minus_accepted": 1.0777292320013045
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3839929580688475,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.364116338690122,
                "rejected_mean_error": 2.9777320861816405,
                "gap_rejected_minus_accepted": 1.6136157474915185
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.916516751050949,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2211701231797536,
                "rejected_mean_error": 2.4384012842178344,
                "gap_rejected_minus_accepted": 1.2172311610380808
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5042197108268738,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9883895984888077,
                "rejected_mean_error": 2.06256622838974,
                "gap_rejected_minus_accepted": 1.0741766299009323
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0620617866516113,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7069769937992096,
                "rejected_mean_error": 1.7983115533192953,
                "gap_rejected_minus_accepted": 1.0913345595200856
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9906440568154213,
            "spearman": 0.9839958354954957,
            "auroc_top30_bad": 0.9954651428571428,
            "mae": 0.08341511784300114,
            "mse": 0.0147087569718932,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.71101919257883,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06163361185789108
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19017729303836822
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4943624318599701
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.852766374429067
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9920212265302065,
            "spearman": 0.9863390038649625,
            "auroc_top30_worst": 0.9902384761904762,
            "pairwise_seed_ranking": 0.924,
            "predicted_best_mean_error": 1.6273050805330276,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.06542471003532424,
            "gap_to_oracle": 0.0016339814662933438,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5231308183670044
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8334450194468865
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1497664892196655
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3743888907341053
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3966006994247437,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4985554826524523,
                "rejected_mean_error": 3.372891445159912,
                "gap_rejected_minus_accepted": 1.8743359625074598
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9608165919780731,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3736996767742276,
                "rejected_mean_error": 2.620861825851587,
                "gap_rejected_minus_accepted": 1.2471621490773592
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6306618452072144,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1497664892196655,
                "rejected_mean_error": 2.222211668586731,
                "gap_rejected_minus_accepted": 1.0724451793670655
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2048158049583435,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8349600980837886,
                "rejected_mean_error": 1.9702709049399914,
                "gap_rejected_minus_accepted": 1.1353108068562028
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.386486625671387,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5044825944635603,
                "rejected_mean_error": 3.3869545555114744,
                "gap_rejected_minus_accepted": 1.8824719610479141
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.973363995552063,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.378664434115517,
                "rejected_mean_error": 2.6249555311505754,
                "gap_rejected_minus_accepted": 1.2462910970350585
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.631354033946991,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1479500224590302,
                "rejected_mean_error": 2.237509558677673,
                "gap_rejected_minus_accepted": 1.089559536218643
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.223567545413971,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8317677742905087,
                "rejected_mean_error": 1.9827865126298712,
                "gap_rejected_minus_accepted": 1.1510187383393624
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9697682740066107,
            "spearman": 0.980735020296919,
            "auroc_top30_bad": 0.9930483809523809,
            "mae": 0.14193291352992718,
            "mse": 0.07393459361858547,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7651795282544556,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06874265393614769
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18113396743535995
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5118293314039707
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9048742164333662
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9585297618915798,
            "spearman": 0.9927862558521235,
            "auroc_top30_worst": 0.9982902857142857,
            "pairwise_seed_ranking": 0.922,
            "predicted_best_mean_error": 1.8934864550828934,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.08786033701896678,
            "gap_to_oracle": 0.001440054297447313,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6562636218070984
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9830296326142091
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3005121942520141
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5247311222273658
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8766854286193846,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7422206411361694,
                "rejected_mean_error": 3.9089624366760254,
                "gap_rejected_minus_accepted": 2.1667417955398562
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3304449319839478,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5239977155958193,
                "rejected_mean_error": 3.2608072407329427,
                "gap_rejected_minus_accepted": 1.7368095251371234
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8548029661178589,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3005121942520141,
                "rejected_mean_error": 2.617277447128296,
                "gap_rejected_minus_accepted": 1.3167652528762817
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.411040335893631,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9845487275443519,
                "rejected_mean_error": 2.284370089798625,
                "gap_rejected_minus_accepted": 1.2998213622542731
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9050955533981324,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7595737614896563,
                "rejected_mean_error": 3.977304067611694,
                "gap_rejected_minus_accepted": 2.217730306122038
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.4243290424346924,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5430794423595469,
                "rejected_mean_error": 3.2822355921306308,
                "gap_rejected_minus_accepted": 1.739156149771084
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.89369398355484,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3139182631969453,
                "rejected_mean_error": 2.648775321006775,
                "gap_rejected_minus_accepted": 1.3348570578098298
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.436570256948471,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9900284925150493,
                "rejected_mean_error": 2.3153203368824435,
                "gap_rejected_minus_accepted": 1.3252918443673942
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9891512708914741,
            "spearman": 0.987187814200995,
            "auroc_top30_bad": 0.9916769523809523,
            "mae": 0.09253860160519785,
            "mse": 0.017489368351430973,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7566879634223027,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.051975796461105346
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18570901622772218
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5006807698845863
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.860681501809756
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9803626732717389,
            "spearman": 0.9790234289747747,
            "auroc_top30_worst": 0.9780662857142858,
            "pairwise_seed_ranking": 0.9196,
            "predicted_best_mean_error": 1.6633551614284516,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.043234933257102925,
            "gap_to_oracle": 0.0015062254667284058,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6314710366725922
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9509197367498508
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.219789205789566
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4236282364709545
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.58777780532837,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.559999251180225,
                "rejected_mean_error": 3.149686891555786,
                "gap_rejected_minus_accepted": 1.589687640375561
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0474520921707153,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.423278272756263,
                "rejected_mean_error": 2.6041478512767022,
                "gap_rejected_minus_accepted": 1.1808695785204393
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7321289777755737,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.219789205789566,
                "rejected_mean_error": 2.218146824645996,
                "gap_rejected_minus_accepted": 0.9983576188564298
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.360211342573166,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9524096019161395,
                "rejected_mean_error": 1.9750328854028545,
                "gap_rejected_minus_accepted": 1.0226232834867148
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.539710187911987,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5512216420968374,
                "rejected_mean_error": 3.1049061679840086,
                "gap_rejected_minus_accepted": 1.5536845258871712
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02300888299942,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4134050411655303,
                "rejected_mean_error": 2.576837793229118,
                "gap_rejected_minus_accepted": 1.1634327520635879
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7298895120620728,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2060679018497467,
                "rejected_mean_error": 2.2071122875213622,
                "gap_rejected_minus_accepted": 1.0010443856716156
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.338378518819809,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9289946220223866,
                "rejected_mean_error": 1.9685607619464078,
                "gap_rejected_minus_accepted": 1.0395661399240212
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
      "best_epoch": 155,
      "best_calib_loss": 0.007287731394171715,
      "train_time_sec": 80.02474021911621,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994458699101281,
            "spearman": 0.9985098156444142,
            "auroc_top30_bad": 0.9996783809523809,
            "mae": 0.025837567768646114,
            "mse": 0.001205334489583509,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6914698511755316,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0011641218438744544
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16586379390209913
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4371537979029119
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.756707631692787
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9992357800089323,
            "spearman": 0.9989720745348338,
            "auroc_top30_worst": 0.9994321904761905,
            "pairwise_seed_ranking": 0.9717,
            "predicted_best_mean_error": 1.4508271445333958,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07465076890587796,
            "gap_to_oracle": 0.0005680795907974101,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.495783663213253
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7048280920743942
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9818843713879585
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.210183699043592
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.338944602012636,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3521721408168474,
                "rejected_mean_error": 2.9570651583671568,
                "gap_rejected_minus_accepted": 1.6048930175503093
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9052019119262695,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.210183699043592,
                "rejected_mean_error": 2.420094673156738,
                "gap_rejected_minus_accepted": 1.2099109741131462
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4995868802070618,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.9818843713879585,
                "rejected_mean_error": 2.0434385137557984,
                "gap_rejected_minus_accepted": 1.0615541423678398
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0402640104293823,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7048280920743942,
                "rejected_mean_error": 1.7819392260710398,
                "gap_rejected_minus_accepted": 1.0771111339966457
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.383758616447449,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.3643397618002362,
                "rejected_mean_error": 2.975721278190613,
                "gap_rejected_minus_accepted": 1.6113815163903766
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9193591177463531,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2213735271294912,
                "rejected_mean_error": 2.437791072368622,
                "gap_rejected_minus_accepted": 1.2164175452391308
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5102233290672302,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9888732146024704,
                "rejected_mean_error": 2.062082612276077,
                "gap_rejected_minus_accepted": 1.0732093976736068
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.057370901107788,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7070885722637177,
                "rejected_mean_error": 1.7982743604977927,
                "gap_rejected_minus_accepted": 1.091185788234075
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9902486695127614,
            "spearman": 0.9828398791461667,
            "auroc_top30_bad": 0.9942377142857142,
            "mae": 0.08575572671089904,
            "mse": 0.015543532211899332,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7167399480208607,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06768259713053704
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19822211833000183
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4948671484470367
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8527645026842753
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.993441819471389,
            "spearman": 0.9866054693155004,
            "auroc_top30_worst": 0.9943314285714286,
            "pairwise_seed_ranking": 0.934,
            "predicted_best_mean_error": 1.627398313164711,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.06533147740364087,
            "gap_to_oracle": 0.0017272140979767148,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5227181553840637
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8307731785835364
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1530010263442994
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.371575407000747
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4575510740280153,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4965477036370172,
                "rejected_mean_error": 3.390961456298828,
                "gap_rejected_minus_accepted": 1.8944137526618108
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.944541871547699,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3708974825279945,
                "rejected_mean_error": 2.6292505031957414,
                "gap_rejected_minus_accepted": 1.258353020667747
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6563238501548767,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1530010263442994,
                "rejected_mean_error": 2.218977131462097,
                "gap_rejected_minus_accepted": 1.0659761051177976
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1568397283554077,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8317889051315502,
                "rejected_mean_error": 1.9713302255312941,
                "gap_rejected_minus_accepted": 1.139541320399744
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.456664276123047,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5013947602113087,
                "rejected_mean_error": 3.4147450637817385,
                "gap_rejected_minus_accepted": 1.9133503035704298
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9675379395484924,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3758249338616662,
                "rejected_mean_error": 2.6333838890469266,
                "gap_rejected_minus_accepted": 1.2575589551852604
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6685909032821655,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1524788081645965,
                "rejected_mean_error": 2.2329807729721067,
                "gap_rejected_minus_accepted": 1.0805019648075103
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1757401823997498,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8305172026157379,
                "rejected_mean_error": 1.9832078282208365,
                "gap_rejected_minus_accepted": 1.1526906256050986
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9787115749831656,
            "spearman": 0.9794502815679049,
            "auroc_top30_bad": 0.9943032380952381,
            "mae": 0.13383579461398332,
            "mse": 0.05580949947957433,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7550268202646641,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08953573867678642
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18630442801713942
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5126446776926518
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9040049054185549
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9741142960891639,
            "spearman": 0.9925942987369761,
            "auroc_top30_worst": 0.9989973333333334,
            "pairwise_seed_ranking": 0.9192,
            "predicted_best_mean_error": 1.8930460364818573,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.08830075562000284,
            "gap_to_oracle": 0.0009996356964112607,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6527863392829895
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9822279237783872
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3034168392181396
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5239965423846296
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.014442038536073,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7401184678607517,
                "rejected_mean_error": 3.927881996154785,
                "gap_rejected_minus_accepted": 2.1877635282940333
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.270951986312866,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5232339161055575,
                "rejected_mean_error": 3.2630937586958035,
                "gap_rejected_minus_accepted": 1.739859842590246
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8100183010101318,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3034168392181396,
                "rejected_mean_error": 2.6143728021621704,
                "gap_rejected_minus_accepted": 1.3109559629440308
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3744338750839233,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9835243320312744,
                "rejected_mean_error": 2.284712283817401,
                "gap_rejected_minus_accepted": 1.3011879517861265
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.023504114151001,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7592811148696477,
                "rejected_mean_error": 3.9799378871917725,
                "gap_rejected_minus_accepted": 2.220656772322125
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3576128482818604,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.541340178825001,
                "rejected_mean_error": 3.287398168018886,
                "gap_rejected_minus_accepted": 1.746057989193885
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8388664722442627,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.315726799726486,
                "rejected_mean_error": 2.6469667844772338,
                "gap_rejected_minus_accepted": 1.3312399847507477
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4086439609527588,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9917471669022999,
                "rejected_mean_error": 2.3147413182386103,
                "gap_rejected_minus_accepted": 1.3229941513363104
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9900641742946725,
            "spearman": 0.9885983099894854,
            "auroc_top30_bad": 0.995232,
            "mae": 0.08889979656100332,
            "mse": 0.015296042475730954,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7264778359195774,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05941245639324188
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19217551980018616
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.502246021425724
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8586797003825506
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9881067039923412,
            "spearman": 0.9881610205190533,
            "auroc_top30_worst": 0.9918811428571428,
            "pairwise_seed_ranking": 0.9336,
            "predicted_best_mean_error": 1.6636277945041658,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.0429623001813888,
            "gap_to_oracle": 0.0017788585424425296,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6327185008525849
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9516505565589819
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2182245150089264
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4211891014248068
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.423691558837891,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5594912004735735,
                "rejected_mean_error": 3.1542593479156493,
                "gap_rejected_minus_accepted": 1.5947681474420758
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.970757782459259,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4204216676753256,
                "rejected_mean_error": 2.612699413451905,
                "gap_rejected_minus_accepted": 1.1922777457765792
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5877083539962769,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2182245150089264,
                "rejected_mean_error": 2.219711515426636,
                "gap_rejected_minus_accepted": 1.0014870004177094
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2716293931007385,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9528434883100918,
                "rejected_mean_error": 1.9748879478987915,
                "gap_rejected_minus_accepted": 1.0220444595886997
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.388872718811035,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5507535596688589,
                "rejected_mean_error": 3.1091189098358156,
                "gap_rejected_minus_accepted": 1.5583653501669568
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9326839447021484,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4086092546343165,
                "rejected_mean_error": 2.5910729056312922,
                "gap_rejected_minus_accepted": 1.1824636509969757
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.588461995124817,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2064202225208283,
                "rejected_mean_error": 2.2067599668502806,
                "gap_rejected_minus_accepted": 1.0003397443294524
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.263240784406662,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.931374457620439,
                "rejected_mean_error": 1.967758999151342,
                "gap_rejected_minus_accepted": 1.036384541530903
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
      "best_epoch": 152,
      "best_calib_loss": 0.005908412393182516,
      "train_time_sec": 56.46102833747864,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9995303363237487,
            "spearman": 0.9983918722958688,
            "auroc_top30_bad": 0.999834380952381,
            "mae": 0.016620836509601212,
            "mse": 0.000629751030177521,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.993,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6795276244068922,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00520139791443944
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1659194980427623
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.43700244266018273
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7565924454465508
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9997182115839934,
            "spearman": 0.9996489297379488,
            "auroc_top30_worst": 0.9998066666666667,
            "pairwise_seed_ranking": 0.9596,
            "predicted_best_mean_error": 1.4509227604568005,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07455515298247328,
            "gap_to_oracle": 0.0006636955142020895,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4949012491106987
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7044041915178298
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.981341366493702
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2100208105484644
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.33286030292511,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520240348246362,
                "rejected_mean_error": 2.958398112297058,
                "gap_rejected_minus_accepted": 1.606374077472422
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.879670113325119,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2100208105484644,
                "rejected_mean_error": 2.4205833386421203,
                "gap_rejected_minus_accepted": 1.2105625280936558
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.489537537097931,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.981341366493702,
                "rejected_mean_error": 2.043981518650055,
                "gap_rejected_minus_accepted": 1.0626401521563529
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0369854867458344,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7044041915178298,
                "rejected_mean_error": 1.7820805262565613,
                "gap_rejected_minus_accepted": 1.0776763347387315
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3794219970703128,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.3641281258397633,
                "rejected_mean_error": 2.9776260018348695,
                "gap_rejected_minus_accepted": 1.6134978759951062
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8832237124443054,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2211563913822174,
                "rejected_mean_error": 2.438442479610443,
                "gap_rejected_minus_accepted": 1.2172860882282257
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5029369592666626,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9883924590349198,
                "rejected_mean_error": 2.062563367843628,
                "gap_rejected_minus_accepted": 1.0741709088087081
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.053897887468338,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7068565089702606,
                "rejected_mean_error": 1.798351714928945,
                "gap_rejected_minus_accepted": 1.0914952059586844
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9922204631228841,
            "spearman": 0.9874809282641579,
            "auroc_top30_bad": 0.996839619047619,
            "mae": 0.07496725715380162,
            "mse": 0.012460932823546489,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7079594467747955,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06755479514598846
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18189256217479705
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.49285067734718324
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8520511938412985
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.993753336177286,
            "spearman": 0.9925963953896931,
            "auroc_top30_worst": 0.993609142857143,
            "pairwise_seed_ranking": 0.918,
            "predicted_best_mean_error": 1.6287874742746353,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.0639423162937165,
            "gap_to_oracle": 0.00311637520790109,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5224728665351868
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8278858883258624
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1484128368377686
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3720130619209712
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.292537307739258,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4971002303229437,
                "rejected_mean_error": 3.3859887161254885,
                "gap_rejected_minus_accepted": 1.8888884858025448
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9579477608203888,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3713737069733496,
                "rejected_mean_error": 2.6278248728273774,
                "gap_rejected_minus_accepted": 1.2564511658540278
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6641578078269958,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1484128368377686,
                "rejected_mean_error": 2.223565320968628,
                "gap_rejected_minus_accepted": 1.0751524841308593
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1985767781734467,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8290412669745497,
                "rejected_mean_error": 1.972248059835607,
                "gap_rejected_minus_accepted": 1.1432067928610572
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3093791007995605,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5027562606334686,
                "rejected_mean_error": 3.4024915599823,
                "gap_rejected_minus_accepted": 1.8997352993488315
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.969219297170639,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3759405407357344,
                "rejected_mean_error": 2.6330407384842163,
                "gap_rejected_minus_accepted": 1.257100197748482
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6771353483200073,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1480159394741059,
                "rejected_mean_error": 2.2374436416625976,
                "gap_rejected_minus_accepted": 1.0894277021884917
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.212260514497757,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8248652593484,
                "rejected_mean_error": 1.985111958840314,
                "gap_rejected_minus_accepted": 1.160246699491914
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9620449372567754,
            "spearman": 0.979106954932582,
            "auroc_top30_bad": 0.9916670476190477,
            "mae": 0.15172991469185798,
            "mse": 0.08033745234606417,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.792177191820683,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.066342741638422
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18220084651708604
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5137220642149448
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9047371466040611
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.93126180225316,
            "spearman": 0.9825260165926507,
            "auroc_top30_worst": 0.9981775238095237,
            "pairwise_seed_ranking": 0.9004,
            "predicted_best_mean_error": 1.8935811142921448,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.08776567780971534,
            "gap_to_oracle": 0.0015347135066987594,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6483764996528626
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.98216036038521
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3039640478134156
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5236991274077247
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0724592685699466,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7858108186721802,
                "rejected_mean_error": 3.5166508388519286,
                "gap_rejected_minus_accepted": 1.7308400201797485
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.271080732345581,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5229646193943003,
                "rejected_mean_error": 3.263899928083816,
                "gap_rejected_minus_accepted": 1.7409353086895156
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.842319369316101,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3039640478134156,
                "rejected_mean_error": 2.6138255935668946,
                "gap_rejected_minus_accepted": 1.309861545753479
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.472957581281662,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9837533860160901,
                "rejected_mean_error": 2.2846357695193786,
                "gap_rejected_minus_accepted": 1.3008823835032886
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.097425317764282,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.807609270811081,
                "rejected_mean_error": 3.544984483718872,
                "gap_rejected_minus_accepted": 1.737375212907791
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3391517996788025,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.540380666440821,
                "rejected_mean_error": 3.290246244460817,
                "gap_rejected_minus_accepted": 1.749865578019996
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8741187453269958,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3178745515346526,
                "rejected_mean_error": 2.6448190326690675,
                "gap_rejected_minus_accepted": 1.3269444811344149
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.525475263595581,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9895998348319341,
                "rejected_mean_error": 2.3154647509681987,
                "gap_rejected_minus_accepted": 1.3258649161362646
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9925599982269098,
            "spearman": 0.9895858791219425,
            "auroc_top30_bad": 0.9926788571428572,
            "mae": 0.073218410626892,
            "mse": 0.011928897762761336,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.744768978153602,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.039786694288253786
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18405677831172942
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5006848889946938
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8592275612274806
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9892968167676737,
            "spearman": 0.9849034327701972,
            "auroc_top30_worst": 0.9856152380952381,
            "pairwise_seed_ranking": 0.9204,
            "predicted_best_mean_error": 1.6666872457265853,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.03990284895896923,
            "gap_to_oracle": 0.004838309764862103,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6307881863117218
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9499087009865504
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.218788730287552
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4215078568979622
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4711743116378786,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5587729540136126,
                "rejected_mean_error": 3.1607235660552977,
                "gap_rejected_minus_accepted": 1.601950612041685
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9920338988304138,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4209097256464536,
                "rejected_mean_error": 2.611238358119806,
                "gap_rejected_minus_accepted": 1.1903286324733524
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6749106049537659,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.218788730287552,
                "rejected_mean_error": 2.2191473001480104,
                "gap_rejected_minus_accepted": 1.0003585698604585
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3348358869552612,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9513618623296293,
                "rejected_mean_error": 1.9753828773885298,
                "gap_rejected_minus_accepted": 1.0240210150589006
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.443476128578186,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5499693193700579,
                "rejected_mean_error": 3.1161770725250246,
                "gap_rejected_minus_accepted": 1.5662077531549667
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9718400537967682,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4105395093002422,
                "rejected_mean_error": 2.5853434195594183,
                "gap_rejected_minus_accepted": 1.174803910259176
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6769755482673645,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2070349056720733,
                "rejected_mean_error": 2.2061452836990356,
                "gap_rejected_minus_accepted": 0.9991103780269623
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3242737352848053,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9291889407331981,
                "rejected_mean_error": 1.9684952962844766,
                "gap_rejected_minus_accepted": 1.0393063555512785
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
      "best_epoch": 160,
      "best_calib_loss": 0.0060186018235981464,
      "train_time_sec": 56.49719429016113,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998576908052076,
            "spearman": 0.9992142155652844,
            "auroc_top30_bad": 0.9999657619047619,
            "mae": 0.011298369025764986,
            "mse": 0.0002560558829734388,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.997,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6813752546391354,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0016042251884937286
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16558829735964536
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4369065905235708
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7565216158643365
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.108668715305254
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998962218802985,
            "spearman": 0.9998825756033002,
            "auroc_top30_worst": 0.9999177142857143,
            "pairwise_seed_ranking": 0.971,
            "predicted_best_mean_error": 1.4506119091808796,
            "seed0_mean_error": 1.5254779134392737,
            "random_seed_mean_error": 1.5131405942738057,
            "oracle_best_mean_error": 1.4502590649425984,
            "improvement_over_seed0": 0.07486600425839418,
            "gap_to_oracle": 0.0003528442382811914,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.49486994224786757
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7042719531297684
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.981241736805439
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.209947544614474
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5126614425718785
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.318413639068604,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3520023826559384,
                "rejected_mean_error": 2.9585929818153383,
                "gap_rejected_minus_accepted": 1.6065905991593998
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8907373547554016,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.209947544614474,
                "rejected_mean_error": 2.420803136444092,
                "gap_rejected_minus_accepted": 1.2108555918296178
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4904157519340515,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 0.981241736805439,
                "rejected_mean_error": 2.044081148338318,
                "gap_rejected_minus_accepted": 1.0628394115328788
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.037552535533905,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7042719531297684,
                "rejected_mean_error": 1.7821246057192484,
                "gap_rejected_minus_accepted": 1.0778526525894798
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3556104421615602,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.364116338690122,
                "rejected_mean_error": 2.9777320861816405,
                "gap_rejected_minus_accepted": 1.6136157474915185
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9063142240047455,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.221094091018041,
                "rejected_mean_error": 2.4386293807029724,
                "gap_rejected_minus_accepted": 1.2175352896849314
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4950370788574219,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 0.9882646969556809,
                "rejected_mean_error": 2.0626911299228667,
                "gap_rejected_minus_accepted": 1.074426432967186
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0583027005195618,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7067713038921356,
                "rejected_mean_error": 1.7983801166216533,
                "gap_rejected_minus_accepted": 1.0916088127295178
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9921412764691244,
            "spearman": 0.9876779479786325,
            "auroc_top30_bad": 0.996560761904762,
            "mae": 0.07865999116413296,
            "mse": 0.012418283243645018,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7149617157658713,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04962554383277893
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18396957552433013
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.49421222252845765
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.852934161345164
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2122082696199417
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9914913415386108,
            "spearman": 0.9898413011464329,
            "auroc_top30_worst": 0.9910247619047619,
            "pairwise_seed_ranking": 0.932,
            "predicted_best_mean_error": 1.6270627871751786,
            "seed0_mean_error": 1.6927297905683518,
            "random_seed_mean_error": 1.6863511270284652,
            "oracle_best_mean_error": 1.6256710990667342,
            "improvement_over_seed0": 0.06566700339317322,
            "gap_to_oracle": 0.0013916881084443666,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5300978803634644
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8320876264419311
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.148222364616394
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3733021609310403
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6859890789031982
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.296770930290222,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.498157841152615,
                "rejected_mean_error": 3.376470218658447,
                "gap_rejected_minus_accepted": 1.8783123775058321
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9514279067516327,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3727343653665662,
                "rejected_mean_error": 2.6237515919505596,
                "gap_rejected_minus_accepted": 1.2510172265839934
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6247547268867493,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.148222364616394,
                "rejected_mean_error": 2.2237557931900023,
                "gap_rejected_minus_accepted": 1.0755334285736082
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.220009833574295,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8338187060797938,
                "rejected_mean_error": 1.9706521810309736,
                "gap_rejected_minus_accepted": 1.13683347495118
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2978134632110594,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.503912573787901,
                "rejected_mean_error": 3.392084741592407,
                "gap_rejected_minus_accepted": 1.888172167804506
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9583621621131897,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3778008495103866,
                "rejected_mean_error": 2.6275188695816767,
                "gap_rejected_minus_accepted": 1.24971802007129
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6331686973571777,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1468820474147796,
                "rejected_mean_error": 2.238577533721924,
                "gap_rejected_minus_accepted": 1.0916954863071442
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.221950650215149,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8322884180243053,
                "rejected_mean_error": 1.9826111085912124,
                "gap_rejected_minus_accepted": 1.150322690566907
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9713765586016485,
            "spearman": 0.9814993522448598,
            "auroc_top30_bad": 0.989959619047619,
            "mae": 0.1490738726930693,
            "mse": 0.06962418887043009,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7741595000068701,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07421798571944237
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1775721624970436
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5115703125059604
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9051319099783898
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.339590658262372
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9603345368092183,
            "spearman": 0.9883557547236831,
            "auroc_top30_worst": 0.9971596190476191,
            "pairwise_seed_ranking": 0.9244,
            "predicted_best_mean_error": 1.8945041358470918,
            "seed0_mean_error": 1.9813467921018602,
            "random_seed_mean_error": 1.9611121064424515,
            "oracle_best_mean_error": 1.892046400785446,
            "improvement_over_seed0": 0.08684265625476839,
            "gap_to_oracle": 0.002457735061645705,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6515363664627075
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9836386289352026
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3051851146697997
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5238101707338525
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.958894820690155
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9191421747207644,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7493850865893894,
                "rejected_mean_error": 3.844482427597046,
                "gap_rejected_minus_accepted": 2.0950973410076568
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2738640904426575,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5229555788264075,
                "rejected_mean_error": 3.263926992020287,
                "gap_rejected_minus_accepted": 1.7409714131938794
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8405749797821045,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3051851146697997,
                "rejected_mean_error": 2.6126045267105105,
                "gap_rejected_minus_accepted": 1.3074194120407108
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4927245676517487,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.984923180299826,
                "rejected_mean_error": 2.2842450057938617,
                "gap_rejected_minus_accepted": 1.2993218254940357
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9471031188964845,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7684283276398978,
                "rejected_mean_error": 3.8976129722595214,
                "gap_rejected_minus_accepted": 2.129184644619624
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.31948983669281,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.540380666440821,
                "rejected_mean_error": 3.290246244460817,
                "gap_rejected_minus_accepted": 1.749865578019996
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8659449219703674,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3171836726665498,
                "rejected_mean_error": 2.6455099115371703,
                "gap_rejected_minus_accepted": 1.3283262388706205
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5350694954395294,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9893244424509624,
                "rejected_mean_error": 2.315557530219542,
                "gap_rejected_minus_accepted": 1.3262330877685797
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9920463388588816,
            "spearman": 0.9896603809056476,
            "auroc_top30_bad": 0.9928487619047619,
            "mae": 0.08469656410105526,
            "mse": 0.016725907733384927,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7656429041881057,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.036481639802455904
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18312409150600434
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.500768935739994
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8592930129766464
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2155965617477893
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9871580179396355,
            "spearman": 0.9820601536384984,
            "auroc_top30_worst": 0.9801813333333332,
            "pairwise_seed_ranking": 0.92,
            "predicted_best_mean_error": 1.663095700621605,
            "seed0_mean_error": 1.7065900946855546,
            "random_seed_mean_error": 1.7170267285108567,
            "oracle_best_mean_error": 1.6618489359617232,
            "improvement_over_seed0": 0.043494394063949615,
            "gap_to_oracle": 0.0012467646598817161,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6299283993244171
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9511126983815279
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2195077093601228
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.425036364685752
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.718968015217781
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5645970821380617,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5595795494980282,
                "rejected_mean_error": 3.1534642066955567,
                "gap_rejected_minus_accepted": 1.5938846571975285
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0455920100212097,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4245434364934104,
                "rejected_mean_error": 2.6003604441785964,
                "gap_rejected_minus_accepted": 1.175817007685186
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7131460905075073,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2195077093601228,
                "rejected_mean_error": 2.2184283210754394,
                "gap_rejected_minus_accepted": 0.9989206117153167
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3773536682128906,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9526208563924978,
                "rejected_mean_error": 1.9749623169385,
                "gap_rejected_minus_accepted": 1.0223414605460022
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.515483522415161,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5509547860092587,
                "rejected_mean_error": 3.1073078727722168,
                "gap_rejected_minus_accepted": 1.556353086762958
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.022468686103821,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.414260789831692,
                "rejected_mean_error": 2.574297713854956,
                "gap_rejected_minus_accepted": 1.1600369240232642
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7199349999427795,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2079210255146027,
                "rejected_mean_error": 2.2052591638565064,
                "gap_rejected_minus_accepted": 0.9973381383419038
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3787857294082642,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9286135875043415,
                "rejected_mean_error": 1.9686891318642519,
                "gap_rejected_minus_accepted": 1.0400755443599103
              }
            ]
          }
        }
      }
    }
  ]
}
```
