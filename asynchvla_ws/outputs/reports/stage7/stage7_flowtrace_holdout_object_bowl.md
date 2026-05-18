# Stage 7 Flow-trace Experiments: holdout_object_bowl

```json
{
  "split": "holdout_object_bowl",
  "variants": [
    {
      "variant": "context_gated_action_no_flow",
      "feature_mode": "M3_gated_base",
      "with_flow": false,
      "model_kind": "gated",
      "input_dim": 1456,
      "best_epoch": 86,
      "best_calib_loss": 0.017830021679401398,
      "train_time_sec": 19.174774169921875,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9994281262555701,
            "spearman": 0.998156340634525,
            "auroc_top30_bad": 0.9999908571428571,
            "mae": 0.03234243450313806,
            "mse": 0.0014905414731862087,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.678301826056345,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0024364603757858275
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18050320925712585
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.45930401084423067
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7646819809118907
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.141449211704731
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9998279551911571,
            "spearman": 0.9996135482966712,
            "auroc_top30_worst": 0.9995032380952381,
            "pairwise_seed_ranking": 0.9316,
            "predicted_best_mean_error": 1.5006200901269913,
            "seed0_mean_error": 1.5777591111660003,
            "random_seed_mean_error": 1.5666084773540496,
            "oracle_best_mean_error": 1.4992612565755845,
            "improvement_over_seed0": 0.07713902103900905,
            "gap_to_oracle": 0.0013588335514067573,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5289492557048797
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7219897284148595
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.97684586186409
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.204882688010171
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5630589366197587
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3397864818573013,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.335151430050532,
                "rejected_mean_error": 3.614226495742798,
                "gap_rejected_minus_accepted": 2.2790750656922656
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7783371806144714,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2042519504576126,
                "rejected_mean_error": 2.6371871987089945,
                "gap_rejected_minus_accepted": 1.432935248251382
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.438952922821045,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.97684586186409,
                "rejected_mean_error": 2.149272011375427,
                "gap_rejected_minus_accepted": 1.1724261495113373
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0112681686878204,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7230284736750606,
                "rejected_mean_error": 1.843666764689866,
                "gap_rejected_minus_accepted": 1.1206382910148052
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3697735071182247,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3472341163953145,
                "rejected_mean_error": 3.6524840641021727,
                "gap_rejected_minus_accepted": 2.305249947706858
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7853184342384338,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2135769361480673,
                "rejected_mean_error": 2.6587442973303417,
                "gap_rejected_minus_accepted": 1.4451673611822744
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4527775049209595,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.982014808177948,
                "rejected_mean_error": 2.1735034141540526,
                "gap_rejected_minus_accepted": 1.1914886059761045
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.010767936706543,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.722355238028935,
                "rejected_mean_error": 1.865943303720199,
                "gap_rejected_minus_accepted": 1.1435880656912638
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9628183320512039,
            "spearman": 0.9669567017753302,
            "auroc_top30_bad": 0.9955059523809524,
            "mae": 0.1530695614157594,
            "mse": 0.03853331909283531,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.8875,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6575570679155728,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.18152926135808228
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2066859185695648
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.46174844205379484
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.6795704617102941
              },
              {
                "coverage": 1.0,
                "mean_true_error": 0.9519133406877518
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9052962379990864,
            "spearman": 0.9149798436240225,
            "auroc_top30_worst": 0.9369047619047619,
            "pairwise_seed_ranking": 0.87375,
            "predicted_best_mean_error": 1.174049586057663,
            "seed0_mean_error": 1.2502248018980027,
            "random_seed_mean_error": 1.233658631145954,
            "oracle_best_mean_error": 1.1669989094138145,
            "improvement_over_seed0": 0.0761752158403397,
            "gap_to_oracle": 0.007050676643848508,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8426492005586624
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8777417874336243
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9248840734362602
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0689619431893032
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.229582890123129
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8078650951385498,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.1581985246804025,
                "rejected_mean_error": 1.872042179107666,
                "gap_rejected_minus_accepted": 0.7138436544272635
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6907899379730225,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.0689619431893032,
                "rejected_mean_error": 1.7114457309246063,
                "gap_rejected_minus_accepted": 0.6424837877353031
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2962759137153625,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 0.9248840734362602,
                "rejected_mean_error": 1.5342817068099976,
                "gap_rejected_minus_accepted": 0.6093976333737374
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0634958446025848,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.8777417874336243,
                "rejected_mean_error": 1.346863257686297,
                "gap_rejected_minus_accepted": 0.4691214702526728
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8275800347328186,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.1708674612972472,
                "rejected_mean_error": 1.964440867304802,
                "gap_rejected_minus_accepted": 0.7935734060075548
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7183736860752106,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.0890730977058412,
                "rejected_mean_error": 1.7336799144744872,
                "gap_rejected_minus_accepted": 0.6446068167686461
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3062827587127686,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 0.9386888265609741,
                "rejected_mean_error": 1.561760777235031,
                "gap_rejected_minus_accepted": 0.623071950674057
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.097747027873993,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.8824297457933425,
                "rejected_mean_error": 1.3728231539328892,
                "gap_rejected_minus_accepted": 0.4903934081395467
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9539550275143862,
            "spearman": 0.9421399833629484,
            "auroc_top30_bad": 0.9404538690476191,
            "mae": 0.283320798574714,
            "mse": 0.1942136359135474,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9875,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7267341770931104,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.14293844662606717
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22166174300014974
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5348515013232827
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9277853610366583
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.403959329444915
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9504612986616094,
            "spearman": 0.8293039956499727,
            "auroc_top30_worst": 0.9668749999999999,
            "pairwise_seed_ranking": 0.89375,
            "predicted_best_mean_error": 2.0658317506313324,
            "seed0_mean_error": 2.1668263889849184,
            "random_seed_mean_error": 2.1269816286861896,
            "oracle_best_mean_error": 2.0627124555408956,
            "improvement_over_seed0": 0.10099463835358602,
            "gap_to_oracle": 0.0031192950904368466,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9732168316841125
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.293505014181137
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4990794706344603
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5901146332422893
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.131755758523941
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8151443004608154,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9307319515281254,
                "rejected_mean_error": 3.940970021486282,
                "gap_rejected_minus_accepted": 2.010238069958157
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0374359488487244,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5901146332422893,
                "rejected_mean_error": 3.7566791343688966,
                "gap_rejected_minus_accepted": 2.166564501126607
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.634285569190979,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.4990794706344603,
                "rejected_mean_error": 2.7644320464134218,
                "gap_rejected_minus_accepted": 1.2653525757789614
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.464018166065216,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.293505014181137,
                "rejected_mean_error": 2.4111726733048755,
                "gap_rejected_minus_accepted": 1.1176676591237384
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8223996162414555,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.963608527349101,
                "rejected_mean_error": 3.9957871437072754,
                "gap_rejected_minus_accepted": 2.0321786163581743
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0563091039657593,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6146415005127588,
                "rejected_mean_error": 3.8233810544013975,
                "gap_rejected_minus_accepted": 2.2087395538886385
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6534671187400818,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5252366647124291,
                "rejected_mean_error": 2.808416113257408,
                "gap_rejected_minus_accepted": 1.283179448544979
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.490345150232315,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.3425533860921859,
                "rejected_mean_error": 2.4415840566158296,
                "gap_rejected_minus_accepted": 1.0990306705236437
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.960718084588084,
            "spearman": 0.9568083063193163,
            "auroc_top30_bad": 0.9892336309523809,
            "mae": 0.15713878021400887,
            "mse": 0.05626904567817201,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9125,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6695589705078745,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.15689200144261123
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21312879659235479
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4500569463893771
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8285141327728828
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1658278352580964
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9214997763479946,
            "spearman": 0.900179813623835,
            "auroc_top30_worst": 0.9348511904761905,
            "pairwise_seed_ranking": 0.8925,
            "predicted_best_mean_error": 1.5764772288501263,
            "seed0_mean_error": 1.6129030644893647,
            "random_seed_mean_error": 1.6272749602794647,
            "oracle_best_mean_error": 1.5712506547570229,
            "improvement_over_seed0": 0.0364258356392384,
            "gap_to_oracle": 0.005226574093103453,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5575404532253743
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7628587195277214
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0721120147407055
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3923587722579638
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6329095786064862
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2148515701293947,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.552144376354085,
                "rejected_mean_error": 2.3597963988780974,
                "gap_rejected_minus_accepted": 0.8076520225240125
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0296135544776917,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.3923587722579638,
                "rejected_mean_error": 2.3545619976520538,
                "gap_rejected_minus_accepted": 0.96220322539409
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5013288855552673,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.0721120147407055,
                "rejected_mean_error": 2.193707142472267,
                "gap_rejected_minus_accepted": 1.1215951277315617
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2087709307670593,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.7628587195277214,
                "rejected_mean_error": 1.9229265316327413,
                "gap_rejected_minus_accepted": 1.1600678121050199
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.211539626121521,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.5305138031641643,
                "rejected_mean_error": 2.354406416416168,
                "gap_rejected_minus_accepted": 0.8238926132520039
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.030797004699707,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.3697185536225638,
                "rejected_mean_error": 2.3424565970897673,
                "gap_rejected_minus_accepted": 0.9727380434672035
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.487679362297058,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.0437951505184173,
                "rejected_mean_error": 2.182010978460312,
                "gap_rejected_minus_accepted": 1.1382158279418946
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2082968950271606,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.7227217674255371,
                "rejected_mean_error": 1.9096301635106405,
                "gap_rejected_minus_accepted": 1.1869083960851035
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
      "best_epoch": 98,
      "best_calib_loss": 0.010830237530171871,
      "train_time_sec": 17.163788318634033,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9993678533661464,
            "spearman": 0.9982312725218517,
            "auroc_top30_bad": 0.9999398095238096,
            "mae": 0.029552872898615898,
            "mse": 0.0012751304896460316,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6832534111002052,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0012191847562789918
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1803288637161255
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.459110519528389
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7647437448660532
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.141449211704731
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9997317230519605,
            "spearman": 0.999442824859408,
            "auroc_top30_worst": 0.9991923809523809,
            "pairwise_seed_ranking": 0.9232,
            "predicted_best_mean_error": 1.5009219123125077,
            "seed0_mean_error": 1.5777591111660003,
            "random_seed_mean_error": 1.5666084773540496,
            "oracle_best_mean_error": 1.4992612565755845,
            "improvement_over_seed0": 0.0768371988534926,
            "gap_to_oracle": 0.0016606557369232,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5288519670963288
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7222050368212737
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9768912008762359
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2050099239738257
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5630589366197587
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.363928914070132,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3352642177210914,
                "rejected_mean_error": 3.6132114067077636,
                "gap_rejected_minus_accepted": 2.2779471889866723
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7701073586940765,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2043307581031844,
                "rejected_mean_error": 2.6369512793355097,
                "gap_rejected_minus_accepted": 1.4326205212323253
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4315993189811707,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9768912008762359,
                "rejected_mean_error": 2.149226672363281,
                "gap_rejected_minus_accepted": 1.1723354714870453
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0095932483673096,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7232120655024775,
                "rejected_mean_error": 1.8436054367902057,
                "gap_rejected_minus_accepted": 1.120393371287728
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3936943054199213,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3472341163953145,
                "rejected_mean_error": 3.6524840641021727,
                "gap_rejected_minus_accepted": 2.305249947706858
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7872961163520813,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2135203901459188,
                "rejected_mean_error": 2.658912140225607,
                "gap_rejected_minus_accepted": 1.4453917500796882
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4479960203170776,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9821837267875672,
                "rejected_mean_error": 2.1733344955444336,
                "gap_rejected_minus_accepted": 1.1911507687568665
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0122044086456299,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7216928241744874,
                "rejected_mean_error": 1.8661664698850662,
                "gap_rejected_minus_accepted": 1.1444736457105789
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9741467192668019,
            "spearman": 0.9682656865300807,
            "auroc_top30_bad": 0.9988616071428572,
            "mae": 0.11773391962866299,
            "mse": 0.02263376504533809,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.95,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6081121451912458,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10185661725699902
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2083751780539751
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4680627727508545
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.6728132021427154
              },
              {
                "coverage": 1.0,
                "mean_true_error": 0.9519133406877518
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9525490201861022,
            "spearman": 0.9004608778804867,
            "auroc_top30_worst": 0.979107142857143,
            "pairwise_seed_ranking": 0.8625,
            "predicted_best_mean_error": 1.1712918713688851,
            "seed0_mean_error": 1.2502248018980027,
            "random_seed_mean_error": 1.233658631145954,
            "oracle_best_mean_error": 1.1669989094138145,
            "improvement_over_seed0": 0.07893293052911754,
            "gap_to_oracle": 0.004292961955070673,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8876729026436806
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9018026775121689
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.924608110487461
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0534868425130843
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.229582890123129
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8370830178260806,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.1523852376474275,
                "rejected_mean_error": 1.9243617624044418,
                "gap_rejected_minus_accepted": 0.7719765247570143
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.587119460105896,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.0534868425130843,
                "rejected_mean_error": 1.7578710329532623,
                "gap_rejected_minus_accepted": 0.704384190440178
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.1595576405525208,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 0.924608110487461,
                "rejected_mean_error": 1.5345576697587966,
                "gap_rejected_minus_accepted": 0.6099495592713355
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9610429853200912,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.9018026775121689,
                "rejected_mean_error": 1.338842960993449,
                "gap_rejected_minus_accepted": 0.43704028348128
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8541744470596315,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.1708674612972472,
                "rejected_mean_error": 1.964440867304802,
                "gap_rejected_minus_accepted": 0.7935734060075548
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.5916026532649994,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.0692574977874756,
                "rejected_mean_error": 1.7931267142295837,
                "gap_rejected_minus_accepted": 0.7238692164421081
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.173105537891388,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 0.9386888265609741,
                "rejected_mean_error": 1.561760777235031,
                "gap_rejected_minus_accepted": 0.623071950674057
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9708804041147232,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.9268260568380355,
                "rejected_mean_error": 1.3580243835846584,
                "gap_rejected_minus_accepted": 0.43119832674662284
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.965779601141908,
            "spearman": 0.964698174292507,
            "auroc_top30_bad": 0.9611755952380954,
            "mae": 0.24377152442582883,
            "mse": 0.16257189821981105,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.975,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7358894791965017,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1306272491812706
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20519897736608983
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5233193308487535
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9196255715936422
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.403959329444915
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9641479203157203,
            "spearman": 0.9189349933437083,
            "auroc_top30_worst": 0.9800297619047618,
            "pairwise_seed_ranking": 0.865,
            "predicted_best_mean_error": 2.065905809402466,
            "seed0_mean_error": 2.1668263889849184,
            "random_seed_mean_error": 2.1269816286861896,
            "oracle_best_mean_error": 2.0627124555408956,
            "improvement_over_seed0": 0.1009205795824526,
            "gap_to_oracle": 0.0031933538615702695,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9650085479021072
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2201042199134826
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4491202598810196
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5901146332422893
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.131755758523941
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8782462596893312,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.929055956337187,
                "rejected_mean_error": 3.9560539782047273,
                "gap_rejected_minus_accepted": 2.0269980218675405
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0703037679195404,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5901146332422893,
                "rejected_mean_error": 3.7566791343688966,
                "gap_rejected_minus_accepted": 2.166564501126607
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6256354451179504,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.4491202598810196,
                "rejected_mean_error": 2.8143912571668626,
                "gap_rejected_minus_accepted": 1.365270997285843
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.467406004667282,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.2201042199134826,
                "rejected_mean_error": 2.4356396047274274,
                "gap_rejected_minus_accepted": 1.2155353848139447
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.880955171585083,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.963608527349101,
                "rejected_mean_error": 3.9957871437072754,
                "gap_rejected_minus_accepted": 2.0321786163581743
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1181661188602448,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6146415005127588,
                "rejected_mean_error": 3.8233810544013975,
                "gap_rejected_minus_accepted": 2.2087395538886385
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6253615021705627,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.4707116559147835,
                "rejected_mean_error": 2.862941122055054,
                "gap_rejected_minus_accepted": 1.3922294661402703
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4927857518196106,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.2820520669221878,
                "rejected_mean_error": 2.461751163005829,
                "gap_rejected_minus_accepted": 1.179699096083641
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9610596557891987,
            "spearman": 0.9600434018057283,
            "auroc_top30_bad": 0.9941592261904761,
            "mae": 0.16192708599905017,
            "mse": 0.056105191189784236,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.95,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6466892974185596,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.13962850719690323
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22607751481235028
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4505929970368743
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8120395009467999
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1658278352580964
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9319724996585704,
            "spearman": 0.9147670297939362,
            "auroc_top30_worst": 0.9442559523809524,
            "pairwise_seed_ranking": 0.8725,
            "predicted_best_mean_error": 1.5831013828516007,
            "seed0_mean_error": 1.6129030644893647,
            "random_seed_mean_error": 1.6272749602794647,
            "oracle_best_mean_error": 1.5712506547570229,
            "improvement_over_seed0": 0.029801681637763977,
            "gap_to_oracle": 0.011850728094577878,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5636658050119877
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7655198368430137
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0681334565579892
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3887709274888038
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6329095786064862
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.220386910438538,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.5542137363718616,
                "rejected_mean_error": 2.341172158718109,
                "gap_rejected_minus_accepted": 0.7869584223462476
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.981753945350647,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.3887709274888038,
                "rejected_mean_error": 2.3653255319595337,
                "gap_rejected_minus_accepted": 0.9765546044707298
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5178797245025635,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.0681334565579892,
                "rejected_mean_error": 2.1976857006549837,
                "gap_rejected_minus_accepted": 1.1295522440969945
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2361875772476196,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.7655198368430137,
                "rejected_mean_error": 1.9220394925276438,
                "gap_rejected_minus_accepted": 1.15651965568463
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2307972431182863,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.5305138031641643,
                "rejected_mean_error": 2.354406416416168,
                "gap_rejected_minus_accepted": 0.8238926132520039
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9656732082366943,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.3697185536225638,
                "rejected_mean_error": 2.3424565970897673,
                "gap_rejected_minus_accepted": 0.9727380434672035
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4798027276992798,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.0452502340078353,
                "rejected_mean_error": 2.180555894970894,
                "gap_rejected_minus_accepted": 1.1353056609630585
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1814104318618774,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.7227217674255371,
                "rejected_mean_error": 1.9096301635106405,
                "gap_rejected_minus_accepted": 1.1869083960851035
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
      "best_epoch": 35,
      "best_calib_loss": 0.03906617313623428,
      "train_time_sec": 7.0677430629730225,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9697033399461678,
            "spearman": 0.9218786446867724,
            "auroc_top30_bad": 0.9994857142857143,
            "mae": 0.12870068367123605,
            "mse": 0.04744314678826943,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.492,
            "expert_lt_simvla_seed0": 0.964,
            "same_context_pred_std": 0.6704274565822504,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3391294646859169
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.35816513414382933
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4665949073553085
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7653474935054779
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.141449211704731
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.99848446953077,
            "spearman": 0.9965704415810828,
            "auroc_top30_worst": 0.9966872380952381,
            "pairwise_seed_ranking": 0.8296,
            "predicted_best_mean_error": 1.5041366764307023,
            "seed0_mean_error": 1.5777591111660003,
            "random_seed_mean_error": 1.5666084773540496,
            "oracle_best_mean_error": 1.4992612565755845,
            "improvement_over_seed0": 0.07362243473529806,
            "gap_to_oracle": 0.004875419855117746,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5306829459667206
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7246947511075399
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9778485189914703
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2057629193641992
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5630589366197587
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3695710420608536,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3352646038532257,
                "rejected_mean_error": 3.613207931518555,
                "gap_rejected_minus_accepted": 2.277943327665329
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7861180901527405,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2051450300687405,
                "rejected_mean_error": 2.6345136664545956,
                "gap_rejected_minus_accepted": 1.429368636385855
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4314144253730774,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9778485189914703,
                "rejected_mean_error": 2.148269354248047,
                "gap_rejected_minus_accepted": 1.1704208352565766
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0187714993953705,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7256663398811231,
                "rejected_mean_error": 1.842785599137574,
                "gap_rejected_minus_accepted": 1.1171192592564507
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.394351315498352,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3472341163953145,
                "rejected_mean_error": 3.6524840641021727,
                "gap_rejected_minus_accepted": 2.305249947706858
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7955684959888458,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.215015622702512,
                "rejected_mean_error": 2.6544739102560375,
                "gap_rejected_minus_accepted": 1.4394582875535256
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4338901042938232,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9825630288124084,
                "rejected_mean_error": 2.1729551935195923,
                "gap_rejected_minus_accepted": 1.190392164707184
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0216813385486603,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7264099773906526,
                "rejected_mean_error": 1.8645772685341657,
                "gap_rejected_minus_accepted": 1.138167291143513
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9063815430770452,
            "spearman": 0.9078038804994151,
            "auroc_top30_bad": 0.9809672619047619,
            "mae": 0.254786144439131,
            "mse": 0.09503345773781025,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6197660514342982,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.2994850631803274
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3210056191682816
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4664359310269356
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.6923835003376007
              },
              {
                "coverage": 1.0,
                "mean_true_error": 0.9519133406877518
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8052497187082763,
            "spearman": 0.8416781354883468,
            "auroc_top30_worst": 0.8885416666666667,
            "pairwise_seed_ranking": 0.8325,
            "predicted_best_mean_error": 1.1729803808033465,
            "seed0_mean_error": 1.2502248018980027,
            "random_seed_mean_error": 1.233658631145954,
            "oracle_best_mean_error": 1.1669989094138145,
            "improvement_over_seed0": 0.07724442109465612,
            "gap_to_oracle": 0.005981471389532089,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8745002314448357
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8881441879272461
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9632702657580375
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.086845220128695
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.229582890123129
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9617758870124817,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.1726852859059969,
                "rejected_mean_error": 1.7416613280773163,
                "gap_rejected_minus_accepted": 0.5689760421713195
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7843681871891022,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.086845220128695,
                "rejected_mean_error": 1.65779590010643,
                "gap_rejected_minus_accepted": 0.5709506799777349
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4547926783561707,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 0.9632702657580375,
                "rejected_mean_error": 1.4958955144882202,
                "gap_rejected_minus_accepted": 0.5326252487301827
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.270137369632721,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.8881441879272461,
                "rejected_mean_error": 1.3433957908550898,
                "gap_rejected_minus_accepted": 0.4552516029278436
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0073944330215454,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.190123705400361,
                "rejected_mean_error": 1.7911346703767776,
                "gap_rejected_minus_accepted": 0.6010109649764166
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8210662007331848,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.097074520587921,
                "rejected_mean_error": 1.7096756458282472,
                "gap_rejected_minus_accepted": 0.6126011252403261
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4894497394561768,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 0.9692134112119675,
                "rejected_mean_error": 1.5312361925840379,
                "gap_rejected_minus_accepted": 0.5620227813720704
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2913326621055603,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.8880544483661652,
                "rejected_mean_error": 1.3709482530752817,
                "gap_rejected_minus_accepted": 0.48289380470911647
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8926208312097598,
            "spearman": 0.9033993562628536,
            "auroc_top30_bad": 0.9559970238095237,
            "mae": 0.35022666785866025,
            "mse": 0.34192234373140823,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.9875,
            "same_context_pred_std": 0.7334227015764702,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3512652629986405
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.33918986685574054
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5387913382425904
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9306205622603496
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.403959329444915
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8725665317838543,
            "spearman": 0.7990639941499633,
            "auroc_top30_worst": 0.974375,
            "pairwise_seed_ranking": 0.795,
            "predicted_best_mean_error": 2.0768592044711114,
            "seed0_mean_error": 2.1668263889849184,
            "random_seed_mean_error": 2.1269816286861896,
            "oracle_best_mean_error": 2.0627124555408956,
            "improvement_over_seed0": 0.08996718451380703,
            "gap_to_oracle": 0.014146748930215836,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0224420428276062
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.285914032459259
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5154414564371108
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5901146332422893
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.131755758523941
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3923043966293336,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9632993227905697,
                "rejected_mean_error": 3.6478636801242827,
                "gap_rejected_minus_accepted": 1.684564357333713
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0180440843105316,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5901146332422893,
                "rejected_mean_error": 3.7566791343688966,
                "gap_rejected_minus_accepted": 2.166564501126607
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.732969343662262,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.5154414564371108,
                "rejected_mean_error": 2.7480700606107713,
                "gap_rejected_minus_accepted": 1.2326286041736605
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6189698278903961,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.285914032459259,
                "rejected_mean_error": 2.413703000545502,
                "gap_rejected_minus_accepted": 1.1277889680862427
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4084927082061767,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9892541906899877,
                "rejected_mean_error": 3.7649761736392975,
                "gap_rejected_minus_accepted": 1.7757219829493098
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02975794672966,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6146415005127588,
                "rejected_mean_error": 3.8233810544013975,
                "gap_rejected_minus_accepted": 2.2087395538886385
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7513501644134521,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5614009216427802,
                "rejected_mean_error": 2.772251856327057,
                "gap_rejected_minus_accepted": 1.2108509346842768
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6614484786987305,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.3375588089227677,
                "rejected_mean_error": 2.443248915672302,
                "gap_rejected_minus_accepted": 1.1056901067495344
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9280245790108366,
            "spearman": 0.8949372802250153,
            "auroc_top30_bad": 0.9898660714285714,
            "mae": 0.24206533327698707,
            "mse": 0.09940820043196584,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.4875,
            "expert_lt_simvla_seed0": 0.875,
            "same_context_pred_std": 0.6187693447156761,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.36599631160497664
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.359296937212348
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.45141863998025655
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8138456546018521
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1658278352580964
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9086508996706677,
            "spearman": 0.9228412052575328,
            "auroc_top30_worst": 0.9142261904761906,
            "pairwise_seed_ranking": 0.72125,
            "predicted_best_mean_error": 1.5881915844976902,
            "seed0_mean_error": 1.6129030644893647,
            "random_seed_mean_error": 1.6272749602794647,
            "oracle_best_mean_error": 1.5712506547570229,
            "improvement_over_seed0": 0.024711479991674556,
            "gap_to_oracle": 0.0169409297406673,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5582830063998699
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7724278423190117
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0763573782145976
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3840358061591784
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6329095786064862
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.059138369560242,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.5380291176338992,
                "rejected_mean_error": 2.486833727359772,
                "gap_rejected_minus_accepted": 0.9488046097258727
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9381200075149536,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.3840358061591784,
                "rejected_mean_error": 2.37953089594841,
                "gap_rejected_minus_accepted": 0.9954950897892316
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.678294062614441,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.0763573782145976,
                "rejected_mean_error": 2.189461778998375,
                "gap_rejected_minus_accepted": 1.1131044007837771
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3152810335159302,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.7724278423190117,
                "rejected_mean_error": 1.9197368240356445,
                "gap_rejected_minus_accepted": 1.1473089817166326
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0690656900405884,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.5212794840335846,
                "rejected_mean_error": 2.437515288591385,
                "gap_rejected_minus_accepted": 0.9162358045578003
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.935314267873764,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.36596626440684,
                "rejected_mean_error": 2.3537134647369387,
                "gap_rejected_minus_accepted": 0.9877472003300987
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6718435883522034,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.0461225241422654,
                "rejected_mean_error": 2.179683604836464,
                "gap_rejected_minus_accepted": 1.1335610806941985
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3006140887737274,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.7291600465774536,
                "rejected_mean_error": 1.9074840704600016,
                "gap_rejected_minus_accepted": 1.1783240238825479
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
      "best_epoch": 100,
      "best_calib_loss": 0.02029343880712986,
      "train_time_sec": 21.900947093963623,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9993484022405437,
            "spearman": 0.9981273635143195,
            "auroc_top30_bad": 0.9998674285714286,
            "mae": 0.026832721185125412,
            "mse": 0.0012287745293826603,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6877428332150878,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0019261423945426941
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18135146512985229
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.45935902502536774
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.764745349264145
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.141449211704731
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9995808850820902,
            "spearman": 0.9991266544170588,
            "auroc_top30_worst": 0.9994971428571429,
            "pairwise_seed_ranking": 0.9156,
            "predicted_best_mean_error": 1.50136689722538,
            "seed0_mean_error": 1.5777591111660003,
            "random_seed_mean_error": 1.5666084773540496,
            "oracle_best_mean_error": 1.4992612565755845,
            "improvement_over_seed0": 0.07639221394062035,
            "gap_to_oracle": 0.0021056406497954594,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5288392302989959
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7228666657629685
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9769027452945709
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.204950919188162
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5630589366197587
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.393052268028261,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.335280748711692,
                "rejected_mean_error": 3.6130626277923583,
                "gap_rejected_minus_accepted": 2.277781879080666
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.794983983039856,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2043153208182487,
                "rejected_mean_error": 2.6369974925495185,
                "gap_rejected_minus_accepted": 1.4326821717312699
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4447823762893677,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9769027452945709,
                "rejected_mean_error": 2.149215127944946,
                "gap_rejected_minus_accepted": 1.1723123826503752
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0104148089885712,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7238916690928486,
                "rejected_mean_error": 1.8433784187285343,
                "gap_rejected_minus_accepted": 1.1194867496356857
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4331597089767447,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3472341163953145,
                "rejected_mean_error": 3.6524840641021727,
                "gap_rejected_minus_accepted": 2.305249947706858
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8078396320343018,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2136785419867,
                "rejected_mean_error": 2.658442705396622,
                "gap_rejected_minus_accepted": 1.444764163409922
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4698653817176819,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9822196526527405,
                "rejected_mean_error": 2.17329856967926,
                "gap_rejected_minus_accepted": 1.1910789170265197
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0143759846687317,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7216928241744874,
                "rejected_mean_error": 1.8661664698850662,
                "gap_rejected_minus_accepted": 1.1444736457105789
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9544165080830781,
            "spearman": 0.9693006019793202,
            "auroc_top30_bad": 0.9996428571428572,
            "mae": 0.167633092610726,
            "mse": 0.045146799073776264,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6445414522295818,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.13644420113414527
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2162255083024502
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4632705746591091
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.6726637291908264
              },
              {
                "coverage": 1.0,
                "mean_true_error": 0.9519133406877518
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9487821982871325,
            "spearman": 0.9271136069600434,
            "auroc_top30_worst": 0.9874999999999999,
            "pairwise_seed_ranking": 0.8525,
            "predicted_best_mean_error": 1.1765738718211651,
            "seed0_mean_error": 1.2502248018980027,
            "random_seed_mean_error": 1.233658631145954,
            "oracle_best_mean_error": 1.1669989094138145,
            "improvement_over_seed0": 0.07365093007683754,
            "gap_to_oracle": 0.009574962407350673,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8376407876610756
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8833066862821579
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9262335821986198
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0543183682362238
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.229582890123129
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8470296025276187,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.1546339179078737,
                "rejected_mean_error": 1.904123640060425,
                "gap_rejected_minus_accepted": 0.7494897221525512
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.620796799659729,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.0543183682362238,
                "rejected_mean_error": 1.755376455783844,
                "gap_rejected_minus_accepted": 0.7010580875476202
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.305639624595642,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 0.9262335821986198,
                "rejected_mean_error": 1.532932198047638,
                "gap_rejected_minus_accepted": 0.6066986158490182
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1510484218597412,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.8833066862821579,
                "rejected_mean_error": 1.3450082914034525,
                "gap_rejected_minus_accepted": 0.46170160512129454
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9122637867927554,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.1731625182761087,
                "rejected_mean_error": 1.9437853544950485,
                "gap_rejected_minus_accepted": 0.7706228362189398
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6396999061107635,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.0688516775767007,
                "rejected_mean_error": 1.794344174861908,
                "gap_rejected_minus_accepted": 0.7254924972852073
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.352263331413269,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 0.9416278094053269,
                "rejected_mean_error": 1.5588217943906784,
                "gap_rejected_minus_accepted": 0.6171939849853515
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1673624813556671,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.9030029028654099,
                "rejected_mean_error": 1.3659654349088668,
                "gap_rejected_minus_accepted": 0.46296253204345694
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9410418369247282,
            "spearman": 0.9235181498520716,
            "auroc_top30_bad": 0.9314508928571429,
            "mae": 0.32116851413304204,
            "mse": 0.22810035875578868,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.975,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6661188840387154,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.15102374628186227
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.25396299742162226
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5538377780094743
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9180999859422445
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.403959329444915
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9396115326159382,
            "spearman": 0.8000026250164063,
            "auroc_top30_worst": 0.9592559523809524,
            "pairwise_seed_ranking": 0.81125,
            "predicted_best_mean_error": 2.0683467514812945,
            "seed0_mean_error": 2.1668263889849184,
            "random_seed_mean_error": 2.1269816286861896,
            "oracle_best_mean_error": 2.0627124555408956,
            "improvement_over_seed0": 0.09847963750362387,
            "gap_to_oracle": 0.005634295940398992,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9782350271940231
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3336721646785736
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5011818724870682
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5901146332422893
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.131755758523941
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.84965410232544,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9320084075133006,
                "rejected_mean_error": 3.929481917619705,
                "gap_rejected_minus_accepted": 1.9974735101064045
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9869034886360168,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5901146332422893,
                "rejected_mean_error": 3.7566791343688966,
                "gap_rejected_minus_accepted": 2.166564501126607
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6085036396980286,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.5011818724870682,
                "rejected_mean_error": 2.762329644560814,
                "gap_rejected_minus_accepted": 1.2611477720737456
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4103985726833344,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.3336721646785736,
                "rejected_mean_error": 2.3977836231390635,
                "gap_rejected_minus_accepted": 1.0641114584604898
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8883172512054442,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.963608527349101,
                "rejected_mean_error": 3.9957871437072754,
                "gap_rejected_minus_accepted": 2.0321786163581743
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0465494990348816,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6146415005127588,
                "rejected_mean_error": 3.8233810544013975,
                "gap_rejected_minus_accepted": 2.2087395538886385
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6320585012435913,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5255227580666542,
                "rejected_mean_error": 2.808130019903183,
                "gap_rejected_minus_accepted": 1.2826072618365287
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4278553128242493,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.39651919901371,
                "rejected_mean_error": 2.4235954523086547,
                "gap_rejected_minus_accepted": 1.0270762532949447
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9403629553226437,
            "spearman": 0.9437344980676504,
            "auroc_top30_bad": 0.9965997023809523,
            "mae": 0.19250338943419978,
            "mse": 0.08278374051958849,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.5876724487804722,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1264416677877307
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2784937082976103
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.45897482242435217
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8079579103738069
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1658278352580964
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.939835127667132,
            "spearman": 0.9311484446777791,
            "auroc_top30_worst": 0.9520238095238096,
            "pairwise_seed_ranking": 0.7825,
            "predicted_best_mean_error": 1.5891088508069515,
            "seed0_mean_error": 1.6129030644893647,
            "random_seed_mean_error": 1.6272749602794647,
            "oracle_best_mean_error": 1.5712506547570229,
            "improvement_over_seed0": 0.02379421368241319,
            "gap_to_oracle": 0.017858196049928665,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5621286876499653
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7647406527400017
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.066329134553671
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.388951731423537
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6329095786064862
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2513612270355225,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.5424568983415763,
                "rejected_mean_error": 2.446983700990677,
                "gap_rejected_minus_accepted": 0.9045268026491007
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8817180395126343,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.388951731423537,
                "rejected_mean_error": 2.3647831201553347,
                "gap_rejected_minus_accepted": 0.9758313887317978
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3858714699745178,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.066329134553671,
                "rejected_mean_error": 2.199490022659302,
                "gap_rejected_minus_accepted": 1.133160888105631
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1713480055332184,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.7647406527400017,
                "rejected_mean_error": 1.922299220561981,
                "gap_rejected_minus_accepted": 1.1575585678219795
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2578129053115843,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.526286608643002,
                "rejected_mean_error": 2.3924511671066284,
                "gap_rejected_minus_accepted": 0.8661645584636264
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8992521464824677,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.3697185536225638,
                "rejected_mean_error": 2.3424565970897673,
                "gap_rejected_minus_accepted": 0.9727380434672035
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.39163076877594,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.0399240374565124,
                "rejected_mean_error": 2.185882091522217,
                "gap_rejected_minus_accepted": 1.1459580540657044
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1483023166656494,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.7231807231903076,
                "rejected_mean_error": 1.909477178255717,
                "gap_rejected_minus_accepted": 1.1862964550654094
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
      "best_epoch": 22,
      "best_calib_loss": 0.05024978518486023,
      "train_time_sec": 4.624361038208008,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8223159455927291,
            "spearman": 0.6568815292281581,
            "auroc_top30_bad": 0.7663222857142857,
            "mae": 0.3188358234405518,
            "mse": 0.2718193752632541,
            "expert_lt_perturb_large": 0.5,
            "expert_lt_other_task": 0.502,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.557640592388112,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7286284668445587
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7261161407709121
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7192745476007462
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8067249032497406
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.141449211704731
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9929211206149832,
            "spearman": 0.9835083506613446,
            "auroc_top30_worst": 0.9873249523809524,
            "pairwise_seed_ranking": 0.7568,
            "predicted_best_mean_error": 1.5154329040050507,
            "seed0_mean_error": 1.5777591111660003,
            "random_seed_mean_error": 1.5666084773540496,
            "oracle_best_mean_error": 1.4992612565755845,
            "improvement_over_seed0": 0.06232620716094961,
            "gap_to_oracle": 0.016171647429466196,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5390111000537873
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7301962959269682
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9804957361698151
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2109207981494443
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5630589366197587
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3311959505081177,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3352759309609732,
                "rejected_mean_error": 3.613105987548828,
                "gap_rejected_minus_accepted": 2.277830056587855
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.838173270225525,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2099662421543544,
                "rejected_mean_error": 2.6200808366647546,
                "gap_rejected_minus_accepted": 1.4101145945104
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4850725531578064,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9804957361698151,
                "rejected_mean_error": 2.145622137069702,
                "gap_rejected_minus_accepted": 1.165126400899887
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.106252133846283,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.731096124782349,
                "rejected_mean_error": 1.840971807596396,
                "gap_rejected_minus_accepted": 1.1098756828140468
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4128941297531123,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3476255467202929,
                "rejected_mean_error": 3.648961191177368,
                "gap_rejected_minus_accepted": 2.301335644457075
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8605705201625824,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2223572007475052,
                "rejected_mean_error": 2.63268224209074,
                "gap_rejected_minus_accepted": 1.4103250413432347
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5140535831451416,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9861677174568176,
                "rejected_mean_error": 2.169350504875183,
                "gap_rejected_minus_accepted": 1.1831827874183656
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0970993041992188,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7308246247352116,
                "rejected_mean_error": 1.8630899809261057,
                "gap_rejected_minus_accepted": 1.132265356190894
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.6102014351106578,
            "spearman": 0.6219224615227192,
            "auroc_top30_bad": 0.7621874999999998,
            "mae": 0.28299605518579485,
            "mse": 0.2532145744282306,
            "expert_lt_perturb_large": 0.50625,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.3790900991923789,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5984220301732421
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6752486886829138
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6742437912523747
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7581668440500895
              },
              {
                "coverage": 1.0,
                "mean_true_error": 0.9519133406877518
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9728578835136564,
            "spearman": 0.9067881049256558,
            "auroc_top30_worst": 0.9953273809523809,
            "pairwise_seed_ranking": 0.7475,
            "predicted_best_mean_error": 1.183459209650755,
            "seed0_mean_error": 1.2502248018980027,
            "random_seed_mean_error": 1.233658631145954,
            "oracle_best_mean_error": 1.1669989094138145,
            "improvement_over_seed0": 0.06676559224724765,
            "gap_to_oracle": 0.01646030023694056,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8773849323391915
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9020002591609955
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9260129496455193
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0493939338127771
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.229582890123129
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8320497870445251,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.1521212476823064,
                "rejected_mean_error": 1.9267376720905305,
                "gap_rejected_minus_accepted": 0.7746164244082241
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.5087752044200897,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.0493939338127771,
                "rejected_mean_error": 1.770149759054184,
                "gap_rejected_minus_accepted": 0.7207558252414068
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.0726997256278992,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 0.9260129496455193,
                "rejected_mean_error": 1.5331528306007385,
                "gap_rejected_minus_accepted": 0.6071398809552192
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9223887622356415,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.9020002591609955,
                "rejected_mean_error": 1.33877710044384,
                "gap_rejected_minus_accepted": 0.43677684128284455
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.844603443145752,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.1708674612972472,
                "rejected_mean_error": 1.964440867304802,
                "gap_rejected_minus_accepted": 0.7935734060075548
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.5256486535072327,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.065460846821467,
                "rejected_mean_error": 1.8045166671276092,
                "gap_rejected_minus_accepted": 0.7390558203061421
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.0726997256278992,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 0.9391761511564255,
                "rejected_mean_error": 1.5612734526395797,
                "gap_rejected_minus_accepted": 0.6220973014831542
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9319237470626831,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.9258069306612015,
                "rejected_mean_error": 1.3583640923102698,
                "gap_rejected_minus_accepted": 0.4325571616490683
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.898421799448824,
            "spearman": 0.7747176160764152,
            "auroc_top30_bad": 0.8724925595238096,
            "mae": 0.31913376091048123,
            "mse": 0.2713899168743354,
            "expert_lt_perturb_large": 0.50625,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7814735192395612,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6415561765432358
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6669128389656543
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6761629003658891
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9221678527444601
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.403959329444915
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.994437312405151,
            "spearman": 0.9784994281214258,
            "auroc_top30_worst": 0.9854464285714286,
            "pairwise_seed_ranking": 0.73875,
            "predicted_best_mean_error": 2.0883348792791367,
            "seed0_mean_error": 2.1668263889849184,
            "random_seed_mean_error": 2.1269816286861896,
            "oracle_best_mean_error": 2.0627124555408956,
            "improvement_over_seed0": 0.07849150970578167,
            "gap_to_oracle": 0.025622423738241196,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9710582554340362
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.208493436574936
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4141777575016021
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5909612313906352
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.131755758523941
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.6296287298202516,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9108555628193749,
                "rejected_mean_error": 4.119857519865036,
                "gap_rejected_minus_accepted": 2.209001957045661
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.103716790676117,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5909612313906352,
                "rejected_mean_error": 3.7541393399238587,
                "gap_rejected_minus_accepted": 2.1631781085332236
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8403112292289734,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.4141777575016021,
                "rejected_mean_error": 2.8493337595462798,
                "gap_rejected_minus_accepted": 1.4351560020446776
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3706980049610138,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.208493436574936,
                "rejected_mean_error": 2.439509865840276,
                "gap_rejected_minus_accepted": 1.23101642926534
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.6701403856277466,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9441997450258997,
                "rejected_mean_error": 4.170466184616089,
                "gap_rejected_minus_accepted": 2.226266439590189
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.093406021595001,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6146415005127588,
                "rejected_mean_error": 3.8233810544013975,
                "gap_rejected_minus_accepted": 2.2087395538886385
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8731289505958557,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.43996070176363,
                "rejected_mean_error": 2.8936920762062073,
                "gap_rejected_minus_accepted": 1.4537313744425773
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.365043729543686,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.255463543534279,
                "rejected_mean_error": 2.4706140041351317,
                "gap_rejected_minus_accepted": 1.2151504606008527
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.7936877518787526,
            "spearman": 0.7389308335558021,
            "auroc_top30_bad": 0.7936272321428571,
            "mae": 0.34088492011651395,
            "mse": 0.27406240611365623,
            "expert_lt_perturb_large": 0.50625,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.975,
            "same_context_pred_std": 0.537489206557136,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6963858101516962
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7390985970199108
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6951104886457324
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8222507084161044
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1658278352580964
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9784782504566722,
            "spearman": 0.9829006431290194,
            "auroc_top30_worst": 0.9981547619047619,
            "pairwise_seed_ranking": 0.765,
            "predicted_best_mean_error": 1.5873849906027317,
            "seed0_mean_error": 1.6129030644893647,
            "random_seed_mean_error": 1.6272749602794647,
            "oracle_best_mean_error": 1.5712506547570229,
            "improvement_over_seed0": 0.025518073886632964,
            "gap_to_oracle": 0.01613433584570889,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5653391100466252
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.76599534958601
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0692599414288997
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3497825653354327
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6329095786064862
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.177949857711792,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.526319536815087,
                "rejected_mean_error": 2.5922199547290803,
                "gap_rejected_minus_accepted": 1.0659004179139933
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0379186272621155,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.3497825653354327,
                "rejected_mean_error": 2.4822906184196474,
                "gap_rejected_minus_accepted": 1.1325080530842146
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5815469026565552,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.0692599414288997,
                "rejected_mean_error": 2.196559215784073,
                "gap_rejected_minus_accepted": 1.1272992743551733
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2306053936481476,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 0.76599534958601,
                "rejected_mean_error": 1.9218809882799783,
                "gap_rejected_minus_accepted": 1.1558856386939684
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.156067991256714,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.5099570784303877,
                "rejected_mean_error": 2.539416939020157,
                "gap_rejected_minus_accepted": 1.0294598605897691
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0083819031715393,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.3340360164642333,
                "rejected_mean_error": 2.4495042085647585,
                "gap_rejected_minus_accepted": 1.1154681921005252
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6085954904556274,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.045968198776245,
                "rejected_mean_error": 2.179837930202484,
                "gap_rejected_minus_accepted": 1.133869731426239
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2516122460365295,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 0.7231807231903076,
                "rejected_mean_error": 1.909477178255717,
                "gap_rejected_minus_accepted": 1.1862964550654094
              }
            ]
          }
        }
      }
    }
  ]
}
```
