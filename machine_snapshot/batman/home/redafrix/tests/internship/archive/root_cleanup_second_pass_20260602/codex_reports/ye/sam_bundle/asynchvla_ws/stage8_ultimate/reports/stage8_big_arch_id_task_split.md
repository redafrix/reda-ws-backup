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
      "best_epoch": 28,
      "best_calib_loss": 0.08353704959154129,
      "train_time_sec": 23.418039083480835,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8830683593931586,
            "spearman": 0.8096384418112618,
            "auroc_top30_bad": 0.8805209047619047,
            "mae": 0.21374803010374308,
            "mse": 0.2376222477478974,
            "expert_lt_perturb_large": 0.978,
            "expert_lt_other_task": 0.523,
            "expert_lt_simvla_seed0": 0.972,
            "same_context_pred_std": 0.8004326387507137,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5660789822787047
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5515451875478029
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6932491966053843
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0077330787072578
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
            "pearson": 0.9973708336441208,
            "spearman": 0.9957803494468087,
            "auroc_top30_worst": 0.9979653333333334,
            "pairwise_seed_ranking": 0.8152,
            "predicted_best_mean_error": 1.6354229668676854,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.071027383238077,
            "gap_to_oracle": 0.012276445955038184,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5213771655559539
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7336785264492035
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0134824068784714
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2511311346848806
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1822374105453495,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.453270788470904,
                "rejected_mean_error": 3.9139853515625,
                "gap_rejected_minus_accepted": 2.460714563091596
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.989556223154068,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2511311346848806,
                "rejected_mean_error": 3.043975575065613,
                "gap_rejected_minus_accepted": 1.7928444403807324
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5215008854866028,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0134824068784714,
                "rejected_mean_error": 2.385202082681656,
                "gap_rejected_minus_accepted": 1.3717196758031844
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.070545643568039,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7336785264492035,
                "rejected_mean_error": 2.0212301508903505,
                "gap_rejected_minus_accepted": 1.287551624441147
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1843145847320558,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4560400054852167,
                "rejected_mean_error": 3.9601434516906737,
                "gap_rejected_minus_accepted": 2.504103446205457
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0111076831817627,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2503445324103037,
                "rejected_mean_error": 3.0747678031921386,
                "gap_rejected_minus_accepted": 1.8244232707818349
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5395570993423462,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.00910287630558,
                "rejected_mean_error": 2.4037978239059448,
                "gap_rejected_minus_accepted": 1.3946949476003647
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.078672707080841,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.722154629945755,
                "rejected_mean_error": 2.0345489234924314,
                "gap_rejected_minus_accepted": 1.3123942935466766
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6862049712070502,
            "spearman": 0.6674446421154432,
            "auroc_top30_bad": 0.791048761904762,
            "mae": 0.43295974904298784,
            "mse": 0.45775645971810447,
            "expert_lt_perturb_large": 0.96,
            "expert_lt_other_task": 0.504,
            "expert_lt_simvla_seed0": 0.98,
            "same_context_pred_std": 0.6922041340874271,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.691235700905323
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6890079723119735
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8339331175327301
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1072490923404694
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
            "pearson": 0.8507752849415893,
            "spearman": 0.8549222495502399,
            "auroc_top30_worst": 0.9275428571428571,
            "pairwise_seed_ranking": 0.7468,
            "predicted_best_mean_error": 1.6683055411577226,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.059690078616142284,
            "gap_to_oracle": 0.01923328661918644,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6963181321620941
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9650729097043856
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2236629955768585
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4799150266944727
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.393196463584901,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.611724110947715,
                "rejected_mean_error": 2.771123383522034,
                "gap_rejected_minus_accepted": 1.159399272574319
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0345650911331177,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.478208718743879,
                "rejected_mean_error": 2.4744360328863224,
                "gap_rejected_minus_accepted": 0.9962273141424434
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6718928813934326,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2236629955768585,
                "rejected_mean_error": 2.231665080833435,
                "gap_rejected_minus_accepted": 1.0080020852565765
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3065439462661743,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9667057660631478,
                "rejected_mean_error": 1.9818582102226983,
                "gap_rejected_minus_accepted": 1.0151524441595505
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4269627571105956,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6113808086183337,
                "rejected_mean_error": 2.777528920173645,
                "gap_rejected_minus_accepted": 1.1661481115553114
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.067512035369873,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4829066080205582,
                "rejected_mean_error": 2.4554820514860607,
                "gap_rejected_minus_accepted": 0.9725754434655025
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7024273872375488,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2160941743850708,
                "rejected_mean_error": 2.239897065162659,
                "gap_rejected_minus_accepted": 1.023802890777588
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3224554657936096,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9614686369895935,
                "rejected_mean_error": 1.9862373305514534,
                "gap_rejected_minus_accepted": 1.0247686935618598
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.5803464181143918,
            "spearman": 0.48512183428674893,
            "auroc_top30_bad": 0.6863920000000001,
            "mae": 0.5587364189386368,
            "mse": 0.616598929600005,
            "expert_lt_perturb_large": 0.952,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.912,
            "same_context_pred_std": 0.7103576594091839,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8330867750048637
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8257586310625076
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8835727532982827
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.026462279399236
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
            "pearson": 0.7271563575512432,
            "spearman": 0.6095877058481319,
            "auroc_top30_worst": 0.8455100952380953,
            "pairwise_seed_ranking": 0.6952,
            "predicted_best_mean_error": 1.4311861625909805,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.050873046159744195,
            "gap_to_oracle": 0.029729646325111325,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8860468935966491
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0244058742164037
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0773885248184205
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1913630742825934
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.855527758598328,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2880487634076012,
                "rejected_mean_error": 3.1165520849227906,
                "gap_rejected_minus_accepted": 1.8285033215151894
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.179007589817047,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1912857706607851,
                "rejected_mean_error": 2.3079524036413566,
                "gap_rejected_minus_accepted": 1.1166666329805714
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6328482627868652,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0773885248184205,
                "rejected_mean_error": 1.86440966629982,
                "gap_rejected_minus_accepted": 0.7870211414813995
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1066633462905884,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.023807713113273,
                "rejected_mean_error": 1.6202476576781706,
                "gap_rejected_minus_accepted": 0.5964399445648976
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8300402164459224,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2978756023777855,
                "rejected_mean_error": 3.1397116661071776,
                "gap_rejected_minus_accepted": 1.841836063729392
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1847274899482727,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1929037059373397,
                "rejected_mean_error": 2.340346177419027,
                "gap_rejected_minus_accepted": 1.147442471481687
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6018927693367004,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0704596898555756,
                "rejected_mean_error": 1.893658727645874,
                "gap_rejected_minus_accepted": 0.8231990377902985
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1061921417713165,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.021013140205353,
                "rejected_mean_error": 1.6373848895975613,
                "gap_rejected_minus_accepted": 0.6163717493922083
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
      "best_epoch": 157,
      "best_calib_loss": 0.032904718071222305,
      "train_time_sec": 28.10075044631958,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9991141078724833,
            "spearman": 0.9978118720037189,
            "auroc_top30_bad": 0.9988666190476191,
            "mae": 0.03287917335240636,
            "mse": 0.0019999034068424876,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7918380209530471,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.015469730570912362
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1865229263037443
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5935609845027328
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9738839950631062
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
            "pearson": 0.999560220516666,
            "spearman": 0.9991360132373368,
            "auroc_top30_worst": 0.9993262857142857,
            "pairwise_seed_ranking": 0.9447,
            "predicted_best_mean_error": 1.6244110118746757,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08203933823108667,
            "gap_to_oracle": 0.0012644909620285194,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5163893079757691
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7320289161205292
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0111763860940932
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2504395240942636
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1095823764801027,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4531286081870396,
                "rejected_mean_error": 3.915264974117279,
                "gap_rejected_minus_accepted": 2.462136365930239
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9715822041034698,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2504395240942636,
                "rejected_mean_error": 3.0460504068374634,
                "gap_rejected_minus_accepted": 1.7956108827431998
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4936766028404236,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0111763860940932,
                "rejected_mean_error": 2.387508103466034,
                "gap_rejected_minus_accepted": 1.3763317173719407
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0642539858818054,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7320289161205292,
                "rejected_mean_error": 2.0217800209999086,
                "gap_rejected_minus_accepted": 1.2897511048793793
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1780084371566772,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455658050444391,
                "rejected_mean_error": 3.9635810470581054,
                "gap_rejected_minus_accepted": 2.5079229966137144
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9764693975448608,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2494942821661632,
                "rejected_mean_error": 3.0773185539245604,
                "gap_rejected_minus_accepted": 1.8278242717583972
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4963377714157104,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0082113794088363,
                "rejected_mean_error": 2.4046893208026887,
                "gap_rejected_minus_accepted": 1.3964779413938524
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0750292241573334,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7211759068965912,
                "rejected_mean_error": 2.0348751645088194,
                "gap_rejected_minus_accepted": 1.3136992576122282
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9438319750026015,
            "spearman": 0.9470027309222481,
            "auroc_top30_bad": 0.9610674285714286,
            "mae": 0.2217511086821556,
            "mse": 0.09968759574625412,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.622780469608728,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1139019457101822
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.27818588366508484
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6614184177279472
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0374809400479
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
            "pearson": 0.964239758037619,
            "spearman": 0.9639738587992697,
            "auroc_top30_worst": 0.9854872380952381,
            "pairwise_seed_ranking": 0.8596,
            "predicted_best_mean_error": 1.657794580578804,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07020103919506093,
            "gap_to_oracle": 0.008722326040267792,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6398595130443573
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8956598474238163
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1673556963443756
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.421894685831914
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.587044429779053,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.59051722518603,
                "rejected_mean_error": 2.9619853553771973,
                "gap_rejected_minus_accepted": 1.3714681301911673
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2678322196006775,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4213535137148525,
                "rejected_mean_error": 2.644638355928488,
                "gap_rejected_minus_accepted": 1.2232848422136355
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7838332653045654,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1673556963443756,
                "rejected_mean_error": 2.287972380065918,
                "gap_rejected_minus_accepted": 1.1206166837215426
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4119995832443237,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8970525469452428,
                "rejected_mean_error": 2.005125507537431,
                "gap_rejected_minus_accepted": 1.108072960592188
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5815751552581787,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.590305174721612,
                "rejected_mean_error": 2.9672096252441404,
                "gap_rejected_minus_accepted": 1.3769044505225285
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2892873883247375,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4106942491735366,
                "rejected_mean_error": 2.6698266721907116,
                "gap_rejected_minus_accepted": 1.259132423017175
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8091667294502258,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1540298748016358,
                "rejected_mean_error": 2.3019613647460937,
                "gap_rejected_minus_accepted": 1.147931489944458
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4143083095550537,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8880613294858781,
                "rejected_mean_error": 2.010968134683721,
                "gap_rejected_minus_accepted": 1.122906805197843
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9514936185408472,
            "spearman": 0.9356305314528254,
            "auroc_top30_bad": 0.9752464761904762,
            "mae": 0.22736680070459842,
            "mse": 0.09210517208562545,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.5811711108805526,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10611709028482437
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24595865106582643
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6101648000836373
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9042672709862392
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
            "pearson": 0.9575230642755892,
            "spearman": 0.8509150564576362,
            "auroc_top30_worst": 0.9919725714285714,
            "pairwise_seed_ranking": 0.8132,
            "predicted_best_mean_error": 1.4138181321620942,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.06824107658863054,
            "gap_to_oracle": 0.012361615896224976,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7673534517288207
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9073219890586841
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9854670563220977
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1231013302927586
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.604078340530396,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2638040748437245,
                "rejected_mean_error": 3.3347542819976805,
                "gap_rejected_minus_accepted": 2.070950207153956
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8281162679195404,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.122324493963156,
                "rejected_mean_error": 2.5143955865987953,
                "gap_rejected_minus_accepted": 1.3920710926356392
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3948237299919128,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9854670563220977,
                "rejected_mean_error": 1.9563311347961425,
                "gap_rejected_minus_accepted": 0.9708640784740448
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1715022921562195,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9084266388949495,
                "rejected_mean_error": 1.6587901082975252,
                "gap_rejected_minus_accepted": 0.7503634694025757
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6119109869003294,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2739171005619896,
                "rejected_mean_error": 3.3553381824493407,
                "gap_rejected_minus_accepted": 2.081421081887351
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.852811485528946,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1289176123346236,
                "rejected_mean_error": 2.5302731536683583,
                "gap_rejected_minus_accepted": 1.4013555413337346
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4006051421165466,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9878865692615509,
                "rejected_mean_error": 1.9762318482398986,
                "gap_rejected_minus_accepted": 0.9883452789783477
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1759948134422302,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9490641118988158,
                "rejected_mean_error": 1.661624401807785,
                "gap_rejected_minus_accepted": 0.7125602899089692
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
      "best_epoch": 152,
      "best_calib_loss": 0.007645517122000456,
      "train_time_sec": 67.05087471008301,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999871920402169,
            "spearman": 0.9991905758562779,
            "auroc_top30_bad": 0.9998347142857144,
            "mae": 0.012007926811114886,
            "mse": 0.0002716062713327685,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8038865393335706,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18612690839469434
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5933922650203108
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9735740840345621
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
            "pearson": 0.9998156973551803,
            "spearman": 0.9996866024434415,
            "auroc_top30_worst": 0.9997742857142857,
            "pairwise_seed_ranking": 0.9686,
            "predicted_best_mean_error": 1.6236388112306595,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08281153887510295,
            "gap_to_oracle": 0.000492290318012234,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5153094996213913
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7315261429309845
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0107260788679122
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2502856007417043
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1423783779144294,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530218033393225,
                "rejected_mean_error": 3.9162262177467344,
                "gap_rejected_minus_accepted": 2.4632044144074117
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9972178637981415,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2502856007417043,
                "rejected_mean_error": 3.0465121768951415,
                "gap_rejected_minus_accepted": 1.7962265761534373
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5035640597343445,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0107260788679122,
                "rejected_mean_error": 2.387958410692215,
                "gap_rejected_minus_accepted": 1.377232331824303
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0665443539619446,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7315261429309845,
                "rejected_mean_error": 2.02194761206309,
                "gap_rejected_minus_accepted": 1.2904214691321054
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2161102533340458,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455667041738828,
                "rejected_mean_error": 3.9635001254081725,
                "gap_rejected_minus_accepted": 2.5078330836693445
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9979968667030334,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2494719579219817,
                "rejected_mean_error": 3.0773855266571046,
                "gap_rejected_minus_accepted": 1.827913568735123
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4968349933624268,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0075980890989304,
                "rejected_mean_error": 2.4053026111125946,
                "gap_rejected_minus_accepted": 1.3977045220136641
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.079772174358368,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.720922813653946,
                "rejected_mean_error": 2.034959528923035,
                "gap_rejected_minus_accepted": 1.314036715269089
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9896033909323676,
            "spearman": 0.9898842410711987,
            "auroc_top30_bad": 0.9950544761904762,
            "mae": 0.08424902662225067,
            "mse": 0.016781842388546773,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7264538694243613,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06247150546312332
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20112320053577423
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6405897822260856
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0243904790798823
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
            "pearson": 0.9871437322589706,
            "spearman": 0.9918692033722903,
            "auroc_top30_worst": 0.9978514285714285,
            "pairwise_seed_ranking": 0.9148,
            "predicted_best_mean_error": 1.6545968103408812,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.0733988094329836,
            "gap_to_oracle": 0.005524555802345121,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.643000116109848
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.861648616213829
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1526082373142243
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4100091786844644
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6140357494354247,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5909410914580027,
                "rejected_mean_error": 2.958170558929443,
                "gap_rejected_minus_accepted": 1.3672294674714405
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2092560529708862,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4090853698289254,
                "rejected_mean_error": 2.6813643968905123,
                "gap_rejected_minus_accepted": 1.272279027061587
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.612770676612854,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1526082373142243,
                "rejected_mean_error": 2.3027198390960693,
                "gap_rejected_minus_accepted": 1.150111601781845
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1830648183822632,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8633815858501215,
                "rejected_mean_error": 2.016373117807199,
                "gap_rejected_minus_accepted": 1.1529915319570774
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6610772609710693,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.58886761241489,
                "rejected_mean_error": 2.9801476860046385,
                "gap_rejected_minus_accepted": 1.3912800735897486
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.205460488796234,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.400630133674744,
                "rejected_mean_error": 2.699699522956969,
                "gap_rejected_minus_accepted": 1.2990693892822252
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5926604270935059,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.138495611190796,
                "rejected_mean_error": 2.3174956283569337,
                "gap_rejected_minus_accepted": 1.1790000171661377
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1962977945804596,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8575173654253521,
                "rejected_mean_error": 2.0212583471747005,
                "gap_rejected_minus_accepted": 1.1637409817493485
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9821349801586061,
            "spearman": 0.9840025727138041,
            "auroc_top30_bad": 0.9954887619047619,
            "mae": 0.10649241703590379,
            "mse": 0.026705677598057854,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7067160065133397,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06306297832727432
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2283026615858078
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5658823887467385
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.890110333832105
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
            "pearson": 0.9778044568827537,
            "spearman": 0.9835988211192456,
            "auroc_top30_worst": 0.9978758095238096,
            "pairwise_seed_ranking": 0.8944,
            "predicted_best_mean_error": 1.4129741425514222,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.06908506619930255,
            "gap_to_oracle": 0.011517626285552973,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6354199907779694
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7855495895521764
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9396657425403595
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1155613746279593
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.612334847450259,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2651411374674904,
                "rejected_mean_error": 3.3227207183837892,
                "gap_rejected_minus_accepted": 2.0575795809162987
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8414638042449951,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1148306629128493,
                "rejected_mean_error": 2.5368291958452414,
                "gap_rejected_minus_accepted": 1.421998532932392
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2512670755386353,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9396657425403595,
                "rejected_mean_error": 2.0021324485778806,
                "gap_rejected_minus_accepted": 1.062466706037521
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9105205535888672,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7862227653352597,
                "rejected_mean_error": 1.699611679721413,
                "gap_rejected_minus_accepted": 0.9133889143861532
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6331775426864623,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2756635611587102,
                "rejected_mean_error": 3.3396200370788574,
                "gap_rejected_minus_accepted": 2.063956475920147
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8669959902763367,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1200414110313763,
                "rejected_mean_error": 2.5566199734097435,
                "gap_rejected_minus_accepted": 1.4365785623783671
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2526606321334839,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9371308076381684,
                "rejected_mean_error": 2.0269876098632813,
                "gap_rejected_minus_accepted": 1.089856802225113
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8930967748165131,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7864102328580523,
                "rejected_mean_error": 1.7164222327145664,
                "gap_rejected_minus_accepted": 0.9300119998565141
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
      "best_calib_loss": 0.009226866997778416,
      "train_time_sec": 70.03449273109436,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9989171793197897,
            "spearman": 0.9979204893100034,
            "auroc_top30_bad": 0.9982400238095239,
            "mae": 0.035452336108206875,
            "mse": 0.0023783997316281025,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.806959258314414,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.001455836646258831
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18657567937076092
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.593670518027246
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9745073609103759
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
            "pearson": 0.9986408191641198,
            "spearman": 0.9984210070087642,
            "auroc_top30_worst": 0.9979409523809524,
            "pairwise_seed_ranking": 0.9606,
            "predicted_best_mean_error": 1.623803539276123,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08264681082963943,
            "gap_to_oracle": 0.0006570183634757587,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5162946312427521
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7321689774990082
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0113965739011765
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.250998063103358
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.174201321601868,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4532861988941828,
                "rejected_mean_error": 3.9138466577529907,
                "gap_rejected_minus_accepted": 2.460560458858808
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.04338937997818,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.250998063103358,
                "rejected_mean_error": 3.0443747898101807,
                "gap_rejected_minus_accepted": 1.7933767267068228
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.528528094291687,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0113965739011765,
                "rejected_mean_error": 2.3872879156589506,
                "gap_rejected_minus_accepted": 1.375891341757774
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.087841510772705,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7321689774990082,
                "rejected_mean_error": 2.021733333873749,
                "gap_rejected_minus_accepted": 1.2895643563747408
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.231596970558167,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4557856515381071,
                "rejected_mean_error": 3.9624326372146608,
                "gap_rejected_minus_accepted": 2.5066469856765536
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.050140082836151,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2503084936936697,
                "rejected_mean_error": 3.074875919342041,
                "gap_rejected_minus_accepted": 1.8245674256483715
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5284136533737183,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0081880704164505,
                "rejected_mean_error": 2.4047126297950743,
                "gap_rejected_minus_accepted": 1.3965245593786237
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0974797010421753,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7212976324558258,
                "rejected_mean_error": 2.0348345893224082,
                "gap_rejected_minus_accepted": 1.3135369568665825
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9869479307720846,
            "spearman": 0.9857962596879704,
            "auroc_top30_bad": 0.9929409523809524,
            "mae": 0.09749919540930824,
            "mse": 0.02054465668183269,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7266027293274382,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09148514741659164
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20876045696735382
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6431456738352775
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0273565417528152
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
            "pearson": 0.9873665870064552,
            "spearman": 0.9887711078215091,
            "auroc_top30_worst": 0.9965622857142857,
            "pairwise_seed_ranking": 0.8972,
            "predicted_best_mean_error": 1.653724242568016,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07427137720584875,
            "gap_to_oracle": 0.00465198802947997,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.642349191904068
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8672045649817357
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1513666157245637
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4106747945552187
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6046555280685424,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5911630108356476,
                "rejected_mean_error": 2.9561732845306397,
                "gap_rejected_minus_accepted": 1.365010273694992
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2244399189949036,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4098279487934031,
                "rejected_mean_error": 2.6791414049105904,
                "gap_rejected_minus_accepted": 1.2693134561171873
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6652622818946838,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1513666157245637,
                "rejected_mean_error": 2.30396146068573,
                "gap_rejected_minus_accepted": 1.1525948449611665
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1625953316688538,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8682213778884266,
                "rejected_mean_error": 2.014756410328021,
                "gap_rejected_minus_accepted": 1.1465350324395946
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6327692747116087,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.588214512930976,
                "rejected_mean_error": 2.986025581359863,
                "gap_rejected_minus_accepted": 1.3978110684288871
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.245279312133789,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4013903625508681,
                "rejected_mean_error": 2.6974429705786327,
                "gap_rejected_minus_accepted": 1.2960526080277646
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6640300154685974,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.138772247314453,
                "rejected_mean_error": 2.3172189922332764,
                "gap_rejected_minus_accepted": 1.1784467449188234
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1687840521335602,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8579079234410846,
                "rejected_mean_error": 2.021126768805764,
                "gap_rejected_minus_accepted": 1.1632188453646797
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9760923822304407,
            "spearman": 0.9708325830974881,
            "auroc_top30_bad": 0.9928502857142857,
            "mae": 0.13561264915994597,
            "mse": 0.03622009301441382,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6595589755397825,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06520443868637085
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24364002611637114
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5736838588356972
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8929951252698898
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
            "pearson": 0.9747167547085629,
            "spearman": 0.9443759300965954,
            "auroc_top30_worst": 0.988672,
            "pairwise_seed_ranking": 0.8956,
            "predicted_best_mean_error": 1.409247909784317,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07281129896640781,
            "gap_to_oracle": 0.007791393518447709,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6515626528263092
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8038015143038371
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9625280645847321
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.11786740652915
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.406862354278565,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2638120481967925,
                "rejected_mean_error": 3.3346825218200684,
                "gap_rejected_minus_accepted": 2.070870473623276
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7419057786464691,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1172689521643497,
                "rejected_mean_error": 2.5295299082137523,
                "gap_rejected_minus_accepted": 1.4122609560494026
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2569398880004883,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9625280645847321,
                "rejected_mean_error": 1.9792701265335082,
                "gap_rejected_minus_accepted": 1.0167420619487761
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8829197138547897,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8038783497132432,
                "rejected_mean_error": 1.6937139231469105,
                "gap_rejected_minus_accepted": 0.8898355734336673
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3916825056076045,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7767671346664429,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1214716292638829,
                "rejected_mean_error": 2.552374722465636,
                "gap_rejected_minus_accepted": 1.4309030932017532
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.249160349369049,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9635963675975799,
                "rejected_mean_error": 2.0005220499038696,
                "gap_rejected_minus_accepted": 1.0369256823062898
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8704338222742081,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7976149495631929,
                "rejected_mean_error": 1.7126473816320857,
                "gap_rejected_minus_accepted": 0.9150324320688928
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
      "best_epoch": 97,
      "best_calib_loss": 0.009789085015654564,
      "train_time_sec": 79.38504815101624,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9995177385484858,
            "spearman": 0.9983550576266811,
            "auroc_top30_bad": 0.9994923333333334,
            "mae": 0.029852837550124606,
            "mse": 0.00164863289608791,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8167156594907763,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0016765107735991478
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18668121351897715
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5936702498301863
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9738823337306579
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
            "pearson": 0.9995298940065008,
            "spearman": 0.9989522527900396,
            "auroc_top30_worst": 0.9995742857142857,
            "pairwise_seed_ranking": 0.9657,
            "predicted_best_mean_error": 1.6242732445895671,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08217710551619528,
            "gap_to_oracle": 0.0011267236769199052,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5169358414411545
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7322036667346954
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.011316412472725
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2503715126196544
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.195465779304505,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4531072339084414,
                "rejected_mean_error": 3.915457342624664,
                "gap_rejected_minus_accepted": 2.4623501087162225
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0356032848358154,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2503715126196544,
                "rejected_mean_error": 3.0462544412612913,
                "gap_rejected_minus_accepted": 1.795882928641637
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5188467502593994,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.011316412472725,
                "rejected_mean_error": 2.387368077087402,
                "gap_rejected_minus_accepted": 1.3760516646146772
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.072332739830017,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7322036667346954,
                "rejected_mean_error": 2.0217217707951862,
                "gap_rejected_minus_accepted": 1.2895181040604908
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2672101974487306,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4556599781910577,
                "rejected_mean_error": 3.9635636973381043,
                "gap_rejected_minus_accepted": 2.5079037191470466
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0357571840286255,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2494570724964142,
                "rejected_mean_error": 3.0774301829338073,
                "gap_rejected_minus_accepted": 1.827973110437393
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.510015606880188,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0080228852033615,
                "rejected_mean_error": 2.4048778150081636,
                "gap_rejected_minus_accepted": 1.396854929804802
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.099683701992035,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7213511850833892,
                "rejected_mean_error": 2.0348167384465534,
                "gap_rejected_minus_accepted": 1.313465553363164
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9864894039369847,
            "spearman": 0.9847675512557537,
            "auroc_top30_bad": 0.992695619047619,
            "mae": 0.10282399460355837,
            "mse": 0.02190410757295704,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7394784938671914,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09792014980316162
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2189753700733185
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6409797577738762
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0268364495515823
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
            "pearson": 0.9875284829981508,
            "spearman": 0.9902358506469446,
            "auroc_top30_worst": 0.993767619047619,
            "pairwise_seed_ranking": 0.8952,
            "predicted_best_mean_error": 1.6539518882036208,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07404373157024402,
            "gap_to_oracle": 0.004879633665084704,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6594695909023285
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8615663048739617
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1525438568592072
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4118363790229949
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6369655847549445,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5902683098316193,
                "rejected_mean_error": 2.9642255935668946,
                "gap_rejected_minus_accepted": 1.3739572837352754
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.128864109516144,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.411044378704297,
                "rejected_mean_error": 2.675499887892994,
                "gap_rejected_minus_accepted": 1.264455509188697
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6680079698562622,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1525438568592072,
                "rejected_mean_error": 2.3027842195510866,
                "gap_rejected_minus_accepted": 1.1502403626918793
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0860419869422913,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8632288433301943,
                "rejected_mean_error": 2.016424140655371,
                "gap_rejected_minus_accepted": 1.1531952973251767
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6693623542785643,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5898986848195393,
                "rejected_mean_error": 2.970868034362793,
                "gap_rejected_minus_accepted": 1.3809693495432536
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.14632648229599,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4029590344046527,
                "rejected_mean_error": 2.6927867541237482,
                "gap_rejected_minus_accepted": 1.2898277197190955
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6605957746505737,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1395062294006348,
                "rejected_mean_error": 2.316485010147095,
                "gap_rejected_minus_accepted": 1.17697878074646
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.103155493736267,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8577907388172452,
                "rejected_mean_error": 2.0211662481175385,
                "gap_rejected_minus_accepted": 1.1633755093002933
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9752665022653907,
            "spearman": 0.9712017038244742,
            "auroc_top30_bad": 0.9936380952380953,
            "mae": 0.146064041496159,
            "mse": 0.04254759227130985,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6559055630059026,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0684629482626915
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2543505226612091
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5721339122891426
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8907621298551559
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
            "pearson": 0.9790323906926639,
            "spearman": 0.9558456672292273,
            "auroc_top30_worst": 0.9903146666666667,
            "pairwise_seed_ranking": 0.8988,
            "predicted_best_mean_error": 1.4079224126338958,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07413679611682888,
            "gap_to_oracle": 0.006465896368026636,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.667359213590622
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7971276429792246
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9582826147556305
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1167736363881178
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2280238389968874,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2640160179403093,
                "rejected_mean_error": 3.332846794128418,
                "gap_rejected_minus_accepted": 2.0688307761881086
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6477997601032257,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1161212929094104,
                "rejected_mean_error": 2.532965552692596,
                "gap_rejected_minus_accepted": 1.4168442597831856
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1832417845726013,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9582826147556305,
                "rejected_mean_error": 1.9835155763626098,
                "gap_rejected_minus_accepted": 1.0252329616069793
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8060821443796158,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7976798755101884,
                "rejected_mean_error": 1.6957844913705564,
                "gap_rejected_minus_accepted": 0.898104615860368
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2431714773178095,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6985724568367004,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.120664961675909,
                "rejected_mean_error": 2.5547691167347013,
                "gap_rejected_minus_accepted": 1.4341041550587923
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1764620542526245,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9573097932338714,
                "rejected_mean_error": 2.006808624267578,
                "gap_rejected_minus_accepted": 1.0494988310337066
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.7809758484363556,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7964239465811896,
                "rejected_mean_error": 1.7130486286260227,
                "gap_rejected_minus_accepted": 0.916624682044833
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
      "best_epoch": 101,
      "best_calib_loss": 0.01400796975940466,
      "train_time_sec": 54.255532026290894,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997212108470799,
            "spearman": 0.999024672388209,
            "auroc_top30_bad": 0.9996809047619047,
            "mae": 0.018272315553011047,
            "mse": 0.0006432171396372211,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8104998751086423,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0010136950686573981
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18610658573806285
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.593409107862413
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9736380082199971
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
            "pearson": 0.9996559466886966,
            "spearman": 0.9995958799678156,
            "auroc_top30_worst": 0.9996910476190476,
            "pairwise_seed_ranking": 0.9661,
            "predicted_best_mean_error": 1.6236885356009005,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08276181450486186,
            "gap_to_oracle": 0.0005420146882533228,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5151197135448455
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7316059932231903
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0107123984575273
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2503319336414338
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.144525170326234,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4531935401625102,
                "rejected_mean_error": 3.914680586338043,
                "gap_rejected_minus_accepted": 2.4614870461755327
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.021813154220581,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2503319336414338,
                "rejected_mean_error": 3.0463731781959535,
                "gap_rejected_minus_accepted": 1.7960412445545197
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5182018280029297,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0107123984575273,
                "rejected_mean_error": 2.3879720911026,
                "gap_rejected_minus_accepted": 1.3772596926450729
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.072452872991562,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7316059932231903,
                "rejected_mean_error": 2.0219209952990216,
                "gap_rejected_minus_accepted": 1.2903150020758312
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2082858562469485,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455667041738828,
                "rejected_mean_error": 3.9635001254081725,
                "gap_rejected_minus_accepted": 2.5078330836693445
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02381694316864,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2495146524906158,
                "rejected_mean_error": 3.0772574429512023,
                "gap_rejected_minus_accepted": 1.8277427904605865
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.508854866027832,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0076015485525132,
                "rejected_mean_error": 2.405299151659012,
                "gap_rejected_minus_accepted": 1.3976976031064987
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.086543709039688,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7209845321178436,
                "rejected_mean_error": 2.0349389561017355,
                "gap_rejected_minus_accepted": 1.3139544239838918
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9806640947353658,
            "spearman": 0.9815089766785193,
            "auroc_top30_bad": 0.9901043809523808,
            "mae": 0.12577313774209525,
            "mse": 0.03181947320244622,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.715251704255134,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09006093919277192
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22044187326431275
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6437696829676628
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.027795531074206
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
            "pearson": 0.9751165147354341,
            "spearman": 0.983773771631214,
            "auroc_top30_worst": 0.9942095238095239,
            "pairwise_seed_ranking": 0.8816,
            "predicted_best_mean_error": 1.6537143949270248,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07428122484684008,
            "gap_to_oracle": 0.004642140388488647,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6420357291698455
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8726157848842633
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1527469519138336
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.414963924204871
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.603629398345948,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5956960003376006,
                "rejected_mean_error": 2.9153763790130616,
                "gap_rejected_minus_accepted": 1.319680378675461
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1716806888580322,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4139119353912684,
                "rejected_mean_error": 2.666915540878003,
                "gap_rejected_minus_accepted": 1.2530036054867348
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6314139366149902,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1527469519138336,
                "rejected_mean_error": 2.30258112449646,
                "gap_rejected_minus_accepted": 1.1498341725826262
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0936672389507294,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8735117349571313,
                "rejected_mean_error": 2.0129891939326057,
                "gap_rejected_minus_accepted": 1.1394774589754744
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.662910413742065,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5932713370853,
                "rejected_mean_error": 2.9405141639709473,
                "gap_rejected_minus_accepted": 1.3472428268856473
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1866548657417297,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4048624051445946,
                "rejected_mean_error": 2.6871370663718572,
                "gap_rejected_minus_accepted": 1.2822746612272626
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6397801637649536,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1394738025665283,
                "rejected_mean_error": 2.316517436981201,
                "gap_rejected_minus_accepted": 1.1770436344146729
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0859487056732178,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8667658889104449,
                "rejected_mean_error": 2.018142534449776,
                "gap_rejected_minus_accepted": 1.1513766455393313
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9745281209482561,
            "spearman": 0.971937778434422,
            "auroc_top30_bad": 0.9939306666666667,
            "mae": 0.1403028904682189,
            "mse": 0.0432945498260945,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6468341602236992,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08679972070455551
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2492199059486389
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5723434058785438
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8909775134483974
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
            "pearson": 0.9719195382183345,
            "spearman": 0.9525147569374446,
            "auroc_top30_worst": 0.984935619047619,
            "pairwise_seed_ranking": 0.896,
            "predicted_best_mean_error": 1.408620932340622,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.0734382764101027,
            "gap_to_oracle": 0.007164416074752822,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6759936392307282
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8005761304535927
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9582875685214997
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1160894866500581
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.313233900070194,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2640571556356217,
                "rejected_mean_error": 3.3324765548706057,
                "gap_rejected_minus_accepted": 2.068419399234984
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.691474437713623,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.115501390227386,
                "rejected_mean_error": 2.5348212996991677,
                "gap_rejected_minus_accepted": 1.4193199094717817
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1893375515937805,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9582875685214997,
                "rejected_mean_error": 1.9835106225967407,
                "gap_rejected_minus_accepted": 1.0252230540752412
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.826199010014534,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8016686655652409,
                "rejected_mean_error": 1.694452056699018,
                "gap_rejected_minus_accepted": 0.8927833911337771
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3047566413879395,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2739171005619896,
                "rejected_mean_error": 3.3553381824493407,
                "gap_rejected_minus_accepted": 2.081421081887351
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7306749522686005,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1200003819988373,
                "rejected_mean_error": 2.556741757998391,
                "gap_rejected_minus_accepted": 1.4367413759995535
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1819422245025635,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9546499335765839,
                "rejected_mean_error": 2.0094684839248655,
                "gap_rejected_minus_accepted": 1.0548185503482816
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8151718378067017,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8034135448554206,
                "rejected_mean_error": 1.7106938441806936,
                "gap_rejected_minus_accepted": 0.907280299325273
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
      "best_epoch": 120,
      "best_calib_loss": 0.00966167263686657,
      "train_time_sec": 71.94945788383484,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996341360960825,
            "spearman": 0.9987225977192022,
            "auroc_top30_bad": 0.9995303333333333,
            "mae": 0.020503594325621,
            "mse": 0.0008221561462708547,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.808212512706687,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.004943621166050434
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18632128129899503
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5934230547770858
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.973770017789801
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
            "pearson": 0.9998006354870753,
            "spearman": 0.9996488721859296,
            "auroc_top30_worst": 0.9997272380952381,
            "pairwise_seed_ranking": 0.9624,
            "predicted_best_mean_error": 1.6237852367460728,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08266511335968962,
            "gap_to_oracle": 0.0006387158334255627,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.515267342209816
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7316534506320953
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0108181451559066
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2502843025684356
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.130971288681031,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530566426515579,
                "rejected_mean_error": 3.915912663936615,
                "gap_rejected_minus_accepted": 2.462856021285057
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9977779388427734,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2502843025684356,
                "rejected_mean_error": 3.0465160714149473,
                "gap_rejected_minus_accepted": 1.7962317688465117
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5141563415527344,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0108181451559066,
                "rejected_mean_error": 2.3878663444042205,
                "gap_rejected_minus_accepted": 1.377048199248314
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0740760266780853,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7316534506320953,
                "rejected_mean_error": 2.02190517616272,
                "gap_rejected_minus_accepted": 1.2902517255306245
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.212978887557983,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4556959566142824,
                "rejected_mean_error": 3.963239891529083,
                "gap_rejected_minus_accepted": 2.5075439349148008
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9951319992542267,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2495200556914012,
                "rejected_mean_error": 3.0772412333488464,
                "gap_rejected_minus_accepted": 1.8277211776574451
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5134795904159546,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0076140776872635,
                "rejected_mean_error": 2.4052866225242613,
                "gap_rejected_minus_accepted": 1.3976725448369978
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.097602665424347,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7209514400959015,
                "rejected_mean_error": 2.034949986775716,
                "gap_rejected_minus_accepted": 1.3139985466798145
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9863555206063814,
            "spearman": 0.9863161869961741,
            "auroc_top30_bad": 0.9932632380952381,
            "mae": 0.10189065024523629,
            "mse": 0.02156582017483712,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7361425014332185,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08557249814271926
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2116845317840576
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.640647610270977
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0263626271486281
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
            "pearson": 0.9818554122404285,
            "spearman": 0.9895180958195814,
            "auroc_top30_worst": 0.9974918095238094,
            "pairwise_seed_ranking": 0.886,
            "predicted_best_mean_error": 1.6551704624891281,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07282515728473671,
            "gap_to_oracle": 0.006098207950592016,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6640973260402679
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8642593355706105
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1528623398303985
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4116771789565523
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.626628684997559,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.592766445716222,
                "rejected_mean_error": 2.9417423706054686,
                "gap_rejected_minus_accepted": 1.3489759248892466
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.186968982219696,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4106436823131945,
                "rejected_mean_error": 2.6766994167059757,
                "gap_rejected_minus_accepted": 1.2660557343927812
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.686763346195221,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1528623398303985,
                "rejected_mean_error": 2.302465736579895,
                "gap_rejected_minus_accepted": 1.1496033967494965
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1279204487800598,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8654837243663617,
                "rejected_mean_error": 2.0156709093167153,
                "gap_rejected_minus_accepted": 1.1501871849503535
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6800180196762087,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5915453455183242,
                "rejected_mean_error": 2.9560480880737305,
                "gap_rejected_minus_accepted": 1.3645027425554064
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.209083080291748,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4013886604717072,
                "rejected_mean_error": 2.6974480227818565,
                "gap_rejected_minus_accepted": 1.2960593623101493
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6775781512260437,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1411641626358031,
                "rejected_mean_error": 2.3148270769119264,
                "gap_rejected_minus_accepted": 1.1736629142761232
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1434053480625153,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8501879885083153,
                "rejected_mean_error": 2.0237276024996915,
                "gap_rejected_minus_accepted": 1.1735396139913763
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9763119178456293,
            "spearman": 0.9738005452746029,
            "auroc_top30_bad": 0.993207619047619,
            "mae": 0.1336918188716149,
            "mse": 0.03751515308196641,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6667919845295891,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07448551529645919
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23412627992630006
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5741785317063332
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8919998696088791
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
            "pearson": 0.9709210740344085,
            "spearman": 0.9456004669442989,
            "auroc_top30_worst": 0.9856579047619047,
            "pairwise_seed_ranking": 0.9036,
            "predicted_best_mean_error": 1.409995508670807,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.0720637000799178,
            "gap_to_oracle": 0.008538992404937717,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6659913442134857
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8102349544373842
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9622490341663361
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1176206356744522
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.374992012977601,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2647044016785092,
                "rejected_mean_error": 3.326651340484619,
                "gap_rejected_minus_accepted": 2.06194693880611
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7018021643161774,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1168722166513811,
                "rejected_mean_error": 2.530717579701457,
                "gap_rejected_minus_accepted": 1.413845363050076
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2463129758834839,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9622490341663361,
                "rejected_mean_error": 1.9795491569519044,
                "gap_rejected_minus_accepted": 1.0173001227855683
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.882590189576149,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8105371277362775,
                "rejected_mean_error": 1.6914895928147762,
                "gap_rejected_minus_accepted": 0.8809524650784987
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3970812082290647,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7425609827041626,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1213308430929234,
                "rejected_mean_error": 2.552792611576262,
                "gap_rejected_minus_accepted": 1.4314617684833384
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2451310753822327,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9630948207378387,
                "rejected_mean_error": 2.001023596763611,
                "gap_rejected_minus_accepted": 1.0379287760257723
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8716553002595901,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8108151228654952,
                "rejected_mean_error": 1.7082002644232888,
                "gap_rejected_minus_accepted": 0.8973851415577936
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
      "best_epoch": 152,
      "best_calib_loss": 0.007764136418700218,
      "train_time_sec": 71.57329416275024,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993024091372986,
            "spearman": 0.9982896976878993,
            "auroc_top30_bad": 0.9990185714285714,
            "mae": 0.030255876121938172,
            "mse": 0.0019514130341983479,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8124801461815802,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0005237236097455025
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18668957239091397
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5935980155333876
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9738478495190541
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
            "pearson": 0.999521434489489,
            "spearman": 0.99915053030996,
            "auroc_top30_worst": 0.9995794285714286,
            "pairwise_seed_ranking": 0.9621,
            "predicted_best_mean_error": 1.623567803442478,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08288254666328432,
            "gap_to_oracle": 0.00042128252983086867,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5162517006397247
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7319662191867828
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0109682664155961
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2504463288466137
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.181209444999695,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530747558938133,
                "rejected_mean_error": 3.915749644756317,
                "gap_rejected_minus_accepted": 2.462674888862504
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.00746887922287,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2504463288466137,
                "rejected_mean_error": 3.0460299925804137,
                "gap_rejected_minus_accepted": 1.7955836637338
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4902645945549011,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0109682664155961,
                "rejected_mean_error": 2.3877162231445315,
                "gap_rejected_minus_accepted": 1.3767479567289354
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0498577058315277,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7319662191867828,
                "rejected_mean_error": 2.021800919977824,
                "gap_rejected_minus_accepted": 1.2898347007910411
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2325719118118292,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4556599781910577,
                "rejected_mean_error": 3.9635636973381043,
                "gap_rejected_minus_accepted": 2.5079037191470466
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.001620829105377,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2495744647185008,
                "rejected_mean_error": 3.0770780062675476,
                "gap_rejected_minus_accepted": 1.8275035415490468
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4821166396141052,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.007869720339775,
                "rejected_mean_error": 2.40503097987175,
                "gap_rejected_minus_accepted": 1.397161259531975
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0575225949287415,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7213490536212921,
                "rejected_mean_error": 2.0348174489339192,
                "gap_rejected_minus_accepted": 1.3134683953126272
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9888618994808864,
            "spearman": 0.987547367408672,
            "auroc_top30_bad": 0.9929135238095239,
            "mae": 0.0900363068592681,
            "mse": 0.017091154328410577,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7415296307875224,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.061716150522232054
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20677284727096557
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6418037517428398
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0262393771409988
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
            "pearson": 0.9888214235802381,
            "spearman": 0.9908388231928469,
            "auroc_top30_worst": 0.9955565714285715,
            "pairwise_seed_ranking": 0.9048,
            "predicted_best_mean_error": 1.653414428114891,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07458119165897381,
            "gap_to_oracle": 0.004342173576354913,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6459548709392547
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.861168417124412
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1517324373722075
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.412487709604855
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.681938624382019,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5914745796256595,
                "rejected_mean_error": 2.9533691654205323,
                "gap_rejected_minus_accepted": 1.3618945857948728
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1937639117240906,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4115145724572902,
                "rejected_mean_error": 2.6740923110669415,
                "gap_rejected_minus_accepted": 1.2625777386096513
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6566023230552673,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1517324373722075,
                "rejected_mean_error": 2.303595639038086,
                "gap_rejected_minus_accepted": 1.1518632016658785
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1431758105754852,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8625046994549017,
                "rejected_mean_error": 2.016666037168676,
                "gap_rejected_minus_accepted": 1.1541613377137743
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.723632264137268,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.59129576365153,
                "rejected_mean_error": 2.958294324874878,
                "gap_rejected_minus_accepted": 1.3669985612233482
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2064666748046875,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4037708012177983,
                "rejected_mean_error": 2.6903772240593318,
                "gap_rejected_minus_accepted": 1.2866064228415335
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6624996662139893,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1394206228256225,
                "rejected_mean_error": 2.3165706167221067,
                "gap_rejected_minus_accepted": 1.1771499938964842
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1662191152572632,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8488670265863812,
                "rejected_mean_error": 2.024172632452001,
                "gap_rejected_minus_accepted": 1.1753056058656197
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9756284547073895,
            "spearman": 0.9722056668210934,
            "auroc_top30_bad": 0.9929942857142857,
            "mae": 0.13120539120269387,
            "mse": 0.0361739284394823,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.665579451924022,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05904148209095001
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24476922051906586
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5747494372010231
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8916070695956548
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
            "pearson": 0.9781053126685256,
            "spearman": 0.9574412158983783,
            "auroc_top30_worst": 0.9905859047619048,
            "pairwise_seed_ranking": 0.912,
            "predicted_best_mean_error": 1.4106847448348998,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07137446391582492,
            "gap_to_oracle": 0.009228228569030605,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6430295321941376
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7946945987641811
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9559759178638458
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1179642916551784
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4600239992141733,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2639896647400326,
                "rejected_mean_error": 3.333083972930908,
                "gap_rejected_minus_accepted": 2.0690943081908753
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6840794682502747,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1172076213385278,
                "rejected_mean_error": 2.5297135088009575,
                "gap_rejected_minus_accepted": 1.4125058874624297
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2049006223678589,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9559759178638458,
                "rejected_mean_error": 1.9858222732543944,
                "gap_rejected_minus_accepted": 1.0298463553905486
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8811864256858826,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7952210544206845,
                "rejected_mean_error": 1.6966058478284163,
                "gap_rejected_minus_accepted": 0.9013847934077318
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.464022588729858,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2739171005619896,
                "rejected_mean_error": 3.3553381824493407,
                "gap_rejected_minus_accepted": 2.081421081887351
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7138153314590454,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1213629556530937,
                "rejected_mean_error": 2.552697293342106,
                "gap_rejected_minus_accepted": 1.4313343376890122
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2046308517456055,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9543208816051483,
                "rejected_mean_error": 2.0097975358963014,
                "gap_rejected_minus_accepted": 1.0554766542911531
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8845682293176651,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7908699280685849,
                "rejected_mean_error": 1.714919768552729,
                "gap_rejected_minus_accepted": 0.9240498404841442
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
      "best_epoch": 71,
      "best_calib_loss": 0.009745396673679352,
      "train_time_sec": 79.42787981033325,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9992750709296812,
            "spearman": 0.9979376305139208,
            "auroc_top30_bad": 0.9990001904761904,
            "mae": 0.03668380542848536,
            "mse": 0.002530652987876023,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8174488538190101,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0018402262106537819
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18699609011113644
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5937795588120818
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9742025303115447
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
            "pearson": 0.9994451522647797,
            "spearman": 0.9988950684437231,
            "auroc_top30_worst": 0.9994849523809524,
            "pairwise_seed_ranking": 0.9578,
            "predicted_best_mean_error": 1.6240730576515199,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08237729245424252,
            "gap_to_oracle": 0.0009265367388726631,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5159299033880234
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7321433397769928
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0113094767332078
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.250449556875229
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.213438987731934,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4531345363855361,
                "rejected_mean_error": 3.9152116203308105,
                "gap_rejected_minus_accepted": 2.4620770839452746
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0514872074127197,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.250449556875229,
                "rejected_mean_error": 3.046020308494568,
                "gap_rejected_minus_accepted": 1.795570751619339
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5269203782081604,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0113094767332078,
                "rejected_mean_error": 2.3873750128269196,
                "gap_rejected_minus_accepted": 1.3760655360937117
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0699879825115204,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7321433397769928,
                "rejected_mean_error": 2.021741879781087,
                "gap_rejected_minus_accepted": 1.2895985400040944
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.3057550191879272,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455658050444391,
                "rejected_mean_error": 3.9635810470581054,
                "gap_rejected_minus_accepted": 2.5079229966137144
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.048338294029236,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2496545374393464,
                "rejected_mean_error": 3.076837788105011,
                "gap_rejected_minus_accepted": 1.8271832506656644
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5253798961639404,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0081745022535324,
                "rejected_mean_error": 2.4047261979579924,
                "gap_rejected_minus_accepted": 1.39655169570446
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.082923948764801,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7209588916301727,
                "rejected_mean_error": 2.034947502930959,
                "gap_rejected_minus_accepted": 1.3139886113007861
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9870201156128241,
            "spearman": 0.9848766107438184,
            "auroc_top30_bad": 0.9915001904761904,
            "mae": 0.10352500487778639,
            "mse": 0.021483769019301987,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7429320210312063,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09947541117668152
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2142851181268692
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.640446685397625
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0271892138719558
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
            "pearson": 0.9888917446082663,
            "spearman": 0.9905174364911595,
            "auroc_top30_worst": 0.9943344761904762,
            "pairwise_seed_ranking": 0.904,
            "predicted_best_mean_error": 1.6517903281450272,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.0762052916288376,
            "gap_to_oracle": 0.0027180736064911226,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6600532901287078
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8636423159295168
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.151412252664566
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4112565953657825
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.610196566581727,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5899239064587487,
                "rejected_mean_error": 2.9673252239227295,
                "gap_rejected_minus_accepted": 1.3774013174639808
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.258961021900177,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4103051683882384,
                "rejected_mean_error": 2.677712795452569,
                "gap_rejected_minus_accepted": 1.2674076270643304
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6450021862983704,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.151412252664566,
                "rejected_mean_error": 2.3039158237457276,
                "gap_rejected_minus_accepted": 1.1525035710811615
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0580819249153137,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8649131243411725,
                "rejected_mean_error": 2.0158615153016504,
                "gap_rejected_minus_accepted": 1.1509483909604779
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6369736194610596,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.586507355372111,
                "rejected_mean_error": 3.0013899993896485,
                "gap_rejected_minus_accepted": 1.4148826440175375
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2979267835617065,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4014148673909232,
                "rejected_mean_error": 2.697370233989897,
                "gap_rejected_minus_accepted": 1.2959553665989738
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6501726508140564,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1382761898040772,
                "rejected_mean_error": 2.3177150497436525,
                "gap_rejected_minus_accepted": 1.1794388599395753
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0915563106536865,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8547374029008169,
                "rejected_mean_error": 2.0221949120893834,
                "gap_rejected_minus_accepted": 1.1674575091885666
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9706475744946711,
            "spearman": 0.9646357269145528,
            "auroc_top30_bad": 0.993576380952381,
            "mae": 0.15697662130575926,
            "mse": 0.049108447362189174,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6539149215209761,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07669254755973816
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2786109666109085
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5733051709294319
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8903185045957566
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
            "pearson": 0.9739379495541343,
            "spearman": 0.940937315415882,
            "auroc_top30_worst": 0.991527619047619,
            "pairwise_seed_ranking": 0.892,
            "predicted_best_mean_error": 1.4081771042346953,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07388210451602939,
            "gap_to_oracle": 0.0067205879688261305,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7267535221576691
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8221045716259724
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.957856443452835
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1165375918277036
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.273048973083499,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2638040748437245,
                "rejected_mean_error": 3.3347542819976805,
                "gap_rejected_minus_accepted": 2.070950207153956
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6505819261074066,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1160588147736918,
                "rejected_mean_error": 2.5331525878784373,
                "gap_rejected_minus_accepted": 1.4170937731047455
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.162556529045105,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.957856443452835,
                "rejected_mean_error": 1.9839417476654053,
                "gap_rejected_minus_accepted": 1.0260853042125704
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8009574115276337,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8222520379022288,
                "rejected_mean_error": 1.6875762877113154,
                "gap_rejected_minus_accepted": 0.8653242498090866
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.296254158020019,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6808080077171326,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.119757845918125,
                "rejected_mean_error": 2.5574616666824097,
                "gap_rejected_minus_accepted": 1.4377038207642847
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1556163430213928,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9581328008174896,
                "rejected_mean_error": 2.00598561668396,
                "gap_rejected_minus_accepted": 1.0478528158664702
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.7960206866264343,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8138330129403917,
                "rejected_mean_error": 1.707183542098591,
                "gap_rejected_minus_accepted": 0.8933505291581993
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
      "best_epoch": 158,
      "best_calib_loss": 0.009893719106912613,
      "train_time_sec": 57.87524628639221,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994347633861232,
            "spearman": 0.9983593167748093,
            "auroc_top30_bad": 0.9994525238095238,
            "mae": 0.024838449663249777,
            "mse": 0.0012064348989092965,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.798893648089482,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.005145016081631183
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1866398664444685
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5935504021272063
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9738823190758625
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
            "pearson": 0.9996171549279392,
            "spearman": 0.9991988355679149,
            "auroc_top30_worst": 0.999679619047619,
            "pairwise_seed_ranking": 0.9621,
            "predicted_best_mean_error": 1.6239451380670071,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08250521203875527,
            "gap_to_oracle": 0.0007986171543599152,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5160553984642029
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7319897078037262
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0113920642137528
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2503527264753977
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1573142528533937,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530555628273223,
                "rejected_mean_error": 3.9159223823547364,
                "gap_rejected_minus_accepted": 2.462866819527414
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0003411769866943,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2503527264753977,
                "rejected_mean_error": 3.0463107996940613,
                "gap_rejected_minus_accepted": 1.7959580732186635
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4913983941078186,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0113920642137528,
                "rejected_mean_error": 2.3872924253463745,
                "gap_rejected_minus_accepted": 1.3759003611326217
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0458717048168182,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7319897078037262,
                "rejected_mean_error": 2.021793090438843,
                "gap_rejected_minus_accepted": 1.2898033826351165
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1909701108932502,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4556599781910577,
                "rejected_mean_error": 3.9635636973381043,
                "gap_rejected_minus_accepted": 2.5079037191470466
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0074710845947266,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2495055329799651,
                "rejected_mean_error": 3.077284801483154,
                "gap_rejected_minus_accepted": 1.827779268503189
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4892714023590088,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0083864732980727,
                "rejected_mean_error": 2.4045142269134523,
                "gap_rejected_minus_accepted": 1.3961277536153796
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0491148829460144,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7211205203533173,
                "rejected_mean_error": 2.034893626689911,
                "gap_rejected_minus_accepted": 1.3137731063365936
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9853258286315572,
            "spearman": 0.9869570015336014,
            "auroc_top30_bad": 0.9932975238095239,
            "mae": 0.10178711389955133,
            "mse": 0.022432652788638274,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7513225329385325,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06600236195325851
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2066073275566101
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6406624974131584
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0266058283408483
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
            "pearson": 0.9719006056355282,
            "spearman": 0.9859466600618625,
            "auroc_top30_worst": 0.9939169523809523,
            "pairwise_seed_ranking": 0.8752,
            "predicted_best_mean_error": 1.6550867387056352,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07290888106822968,
            "gap_to_oracle": 0.006014484167099043,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6550457193851471
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8629279026809411
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.155040238046646
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4137487608804378
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.651603412628174,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.59752578663826,
                "rejected_mean_error": 2.8989083023071287,
                "gap_rejected_minus_accepted": 1.3013825156688688
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.19760400056839,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4128670340350242,
                "rejected_mean_error": 2.6700435682607533,
                "gap_rejected_minus_accepted": 1.257176534225729
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.663617491722107,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.155040238046646,
                "rejected_mean_error": 2.3002878383636474,
                "gap_rejected_minus_accepted": 1.1452476003170013
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1740597784519196,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8642335948281394,
                "rejected_mean_error": 2.0160885086181706,
                "gap_rejected_minus_accepted": 1.1518549137900311
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7070786714553834,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5977706665462919,
                "rejected_mean_error": 2.9000201988220216,
                "gap_rejected_minus_accepted": 1.3022495322757297
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2343889474868774,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4075949345043,
                "rejected_mean_error": 2.6790262252565413,
                "gap_rejected_minus_accepted": 1.2714312907522414
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.654850423336029,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1420534896850585,
                "rejected_mean_error": 2.3139377498626708,
                "gap_rejected_minus_accepted": 1.1718842601776123
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.193112075328827,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8539449563102116,
                "rejected_mean_error": 2.0224618860744537,
                "gap_rejected_minus_accepted": 1.168516929764242
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9795214221811973,
            "spearman": 0.9769196179392206,
            "auroc_top30_bad": 0.9932297142857143,
            "mae": 0.12565654108813032,
            "mse": 0.03149935567844698,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7300163597409336,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06088515305519104
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22855274221897126
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5718951465249061
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8921710713148117
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
            "pearson": 0.971388033080967,
            "spearman": 0.9501706781252341,
            "auroc_top30_worst": 0.9911497142857143,
            "pairwise_seed_ranking": 0.9052,
            "predicted_best_mean_error": 1.407231952190399,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07482725656032563,
            "gap_to_oracle": 0.0057754359245298925,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6776100175380707
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8093698728734102
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9568640944957734
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1165525597105148
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7105206727981574,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.265161886241701,
                "rejected_mean_error": 3.3225339794158937,
                "gap_rejected_minus_accepted": 2.057372093174193
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8225466907024384,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1159527020940405,
                "rejected_mean_error": 2.5334702478811,
                "gap_rejected_minus_accepted": 1.4175175457870595
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2772700190544128,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9568640944957734,
                "rejected_mean_error": 1.9849340966224671,
                "gap_rejected_minus_accepted": 1.0280700021266937
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9223212003707886,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8094395062984369,
                "rejected_mean_error": 1.6918562475746952,
                "gap_rejected_minus_accepted": 0.8824167412762584
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.715247321128845,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2756635611587102,
                "rejected_mean_error": 3.3396200370788574,
                "gap_rejected_minus_accepted": 2.063956475920147
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8646855652332306,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1198156337368297,
                "rejected_mean_error": 2.557290137760223,
                "gap_rejected_minus_accepted": 1.4374745040233932
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2707756161689758,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9568644597530365,
                "rejected_mean_error": 2.007253957748413,
                "gap_rejected_minus_accepted": 1.0503894979953765
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9408262521028519,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.805547496156087,
                "rejected_mean_error": 1.7099749194109504,
                "gap_rejected_minus_accepted": 0.9044274232548634
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
      "best_epoch": 90,
      "best_calib_loss": 0.010857883840799332,
      "train_time_sec": 55.861074447631836,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993577763256718,
            "spearman": 0.9979878835582009,
            "auroc_top30_bad": 0.9996405714285714,
            "mae": 0.026123508927389048,
            "mse": 0.0015724975987810499,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8034454512842136,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.012390733294188976
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18681347353160382
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5934354116067291
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9737132987250884
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
            "pearson": 0.9996730673868244,
            "spearman": 0.9995156008525891,
            "auroc_top30_worst": 0.9998266666666668,
            "pairwise_seed_ranking": 0.9416,
            "predicted_best_mean_error": 1.6251148081421851,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08133554196357728,
            "gap_to_oracle": 0.0019682872295379017,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5156173812150955
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7316870347499848
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0108219910383225
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2503235094547271
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.138808655738831,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530340563588673,
                "rejected_mean_error": 3.9161159405708315,
                "gap_rejected_minus_accepted": 2.463081884211964
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9888735115528107,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2503235094547271,
                "rejected_mean_error": 3.046398450756073,
                "gap_rejected_minus_accepted": 1.7960749413013457
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4917343258857727,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0108219910383225,
                "rejected_mean_error": 2.387862498521805,
                "gap_rejected_minus_accepted": 1.3770405074834824
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0417125225067139,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7316870347499848,
                "rejected_mean_error": 2.0218939814567567,
                "gap_rejected_minus_accepted": 1.290206946706772
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1855518817901616,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4556599781910577,
                "rejected_mean_error": 3.9635636973381043,
                "gap_rejected_minus_accepted": 2.5079037191470466
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.01079785823822,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2494437228043873,
                "rejected_mean_error": 3.0774702320098877,
                "gap_rejected_minus_accepted": 1.8280265092055004
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.486984670162201,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0076692324876786,
                "rejected_mean_error": 2.4052314677238464,
                "gap_rejected_minus_accepted": 1.3975622352361678
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0585167109966278,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7209845321178436,
                "rejected_mean_error": 2.0349389561017355,
                "gap_rejected_minus_accepted": 1.3139544239838918
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9844929527595006,
            "spearman": 0.9845066236634147,
            "auroc_top30_bad": 0.9910933333333334,
            "mae": 0.10931404269724153,
            "mse": 0.023636120535808897,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7480644086617336,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07577173978090286
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20568597717285156
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6438095611453056
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0295859256664912
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
            "pearson": 0.9778446783021439,
            "spearman": 0.9862335727574868,
            "auroc_top30_worst": 0.9925424761904762,
            "pairwise_seed_ranking": 0.8852,
            "predicted_best_mean_error": 1.6540159145593643,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07397970521450059,
            "gap_to_oracle": 0.004943660020828133,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6452393743991852
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8671943840499108
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1537775074481964
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4122042924419904
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6297984361648563,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5955261125829485,
                "rejected_mean_error": 2.916905368804932,
                "gap_rejected_minus_accepted": 1.3213792562219833
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.164651036262512,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.411336720085195,
                "rejected_mean_error": 2.6746247317463445,
                "gap_rejected_minus_accepted": 1.2632880116611496
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6724545359611511,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1537775074481964,
                "rejected_mean_error": 2.301550568962097,
                "gap_rejected_minus_accepted": 1.1477730615139008
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2264658510684967,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8679565595933043,
                "rejected_mean_error": 2.0148448715087826,
                "gap_rejected_minus_accepted": 1.1468883119154782
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.679239296913147,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5966050508287217,
                "rejected_mean_error": 2.9105107402801513,
                "gap_rejected_minus_accepted": 1.3139056894514296
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1806581616401672,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4049308631509383,
                "rejected_mean_error": 2.6869338656228687,
                "gap_rejected_minus_accepted": 1.2820030024719304
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.660021960735321,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.140884419441223,
                "rejected_mean_error": 2.3151068201065064,
                "gap_rejected_minus_accepted": 1.1742224006652833
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2295357882976532,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8581862430723887,
                "rejected_mean_error": 2.02103300336848,
                "gap_rejected_minus_accepted": 1.162846760296091
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9837991126536805,
            "spearman": 0.981607045196043,
            "auroc_top30_bad": 0.994432,
            "mae": 0.10935625629373825,
            "mse": 0.02458611871406036,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7138354899708172,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05522933328151703
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22170994243621825
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5696085421681404
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8907316405057907
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
            "pearson": 0.9846068869302866,
            "spearman": 0.9755075427248274,
            "auroc_top30_worst": 0.9961843809523809,
            "pairwise_seed_ranking": 0.8988,
            "predicted_best_mean_error": 1.4071803982257842,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.0748788105249405,
            "gap_to_oracle": 0.005723881959915023,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6370211374759674
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7853466775745918
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9483241400241852
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1158690329617276
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.573760747909547,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.265161886241701,
                "rejected_mean_error": 3.3225339794158937,
                "gap_rejected_minus_accepted": 2.057372093174193
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7826521694660187,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1151260522093818,
                "rejected_mean_error": 2.5359449154271867,
                "gap_rejected_minus_accepted": 1.420818863217805
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2920565009117126,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9483241400241852,
                "rejected_mean_error": 1.9934740510940552,
                "gap_rejected_minus_accepted": 1.04514991106987
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0002281963825226,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7859716966700631,
                "rejected_mean_error": 1.6996955479094669,
                "gap_rejected_minus_accepted": 0.9137238512394038
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.576159572601318,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2756635611587102,
                "rejected_mean_error": 3.3396200370788574,
                "gap_rejected_minus_accepted": 2.063956475920147
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.809531807899475,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1195587925413713,
                "rejected_mean_error": 2.5580525076578535,
                "gap_rejected_minus_accepted": 1.4384937151164823
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2855310440063477,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9476160895824433,
                "rejected_mean_error": 2.016502327919006,
                "gap_rejected_minus_accepted": 1.068886238336563
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9941196739673615,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7786497828506288,
                "rejected_mean_error": 1.7190367158721476,
                "gap_rejected_minus_accepted": 0.9403869330215188
              }
            ]
          }
        }
      }
    }
  ]
}
```
