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
      "best_epoch": 61,
      "best_calib_loss": 0.042708870023489,
      "train_time_sec": 11.252354621887207,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9785918677427081,
            "spearman": 0.9408957307559901,
            "auroc_top30_bad": 0.9989543571428571,
            "mae": 0.11828310875073075,
            "mse": 0.04699167641669102,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.489,
            "expert_lt_simvla_seed0": 0.959,
            "same_context_pred_std": 0.7968694865391877,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.29690339663624765
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.31790577175021173
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.48305346571058033
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8230925616095464
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
            "pearson": 0.998929604836511,
            "spearman": 0.9980005480879741,
            "auroc_top30_worst": 0.9986188571428571,
            "pairwise_seed_ranking": 0.8553,
            "predicted_best_mean_error": 1.7791846675872802,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07084104371070876,
            "gap_to_oracle": 0.005545554339885683,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6055604446530342
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8416513303995132
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1154436503529548
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3621052876551947
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.5483646631240853,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.568217608961794,
                "rejected_mean_error": 4.288577872753144,
                "gap_rejected_minus_accepted": 2.7203602637913495
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1550203561782837,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3621052876551947,
                "rejected_mean_error": 3.2746986783981322,
                "gap_rejected_minus_accepted": 1.9125933907429375
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6444513201713562,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1154436503529548,
                "rejected_mean_error": 2.5650636203289032,
                "gap_rejected_minus_accepted": 1.4496199699759484
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.153622716665268,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8416513303995132,
                "rejected_mean_error": 2.173121070321401,
                "gap_rejected_minus_accepted": 1.3314697399218876
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.6171094655990603,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.167488932609558,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3728836727142335,
                "rejected_mean_error": 3.2814518270492554,
                "gap_rejected_minus_accepted": 1.908568154335022
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.674760103225708,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1225378592014312,
                "rejected_mean_error": 2.5775135633945463,
                "gap_rejected_minus_accepted": 1.454975704193115
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1741490066051483,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8456106810569763,
                "rejected_mean_error": 2.1848307213783262,
                "gap_rejected_minus_accepted": 1.33922004032135
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9028648410159291,
            "spearman": 0.8941816544060176,
            "auroc_top30_bad": 0.9783710476190477,
            "mae": 0.2571976719498634,
            "mse": 0.13338012524440587,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.964,
            "same_context_pred_std": 0.7039820285855061,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.27938096451759337
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2898549556732178
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4468613500237465
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7913778501590093
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
            "pearson": 0.7747215841414515,
            "spearman": 0.8313045816989324,
            "auroc_top30_worst": 0.9292556190476191,
            "pairwise_seed_ranking": 0.8016,
            "predicted_best_mean_error": 1.5705375810861588,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.08821465826034536,
            "gap_to_oracle": 0.011404420614242516,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.63719708943367
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9371230958554989
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.162106794834137
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3846399139747945
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.313226628303528,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.574299118783739,
                "rejected_mean_error": 2.195220299720764,
                "gap_rejected_minus_accepted": 0.6209211809370252
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.018332302570343,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3837720618812863,
                "rejected_mean_error": 2.3926345818339825,
                "gap_rejected_minus_accepted": 1.0088625199526962
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.667097270488739,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.162106794834137,
                "rejected_mean_error": 2.110675678920746,
                "gap_rejected_minus_accepted": 0.9485688840866089
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2328872680664062,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.938007218483538,
                "rejected_mean_error": 1.8696828033206556,
                "gap_rejected_minus_accepted": 0.9316755848371177
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3784024238586423,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5995766858259837,
                "rejected_mean_error": 2.191332221031189,
                "gap_rejected_minus_accepted": 0.5917555352052053
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.039981961250305,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4068467197889951,
                "rejected_mean_error": 2.4064717973981584,
                "gap_rejected_minus_accepted": 0.9996250776091633
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7023524641990662,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1744524309635163,
                "rejected_mean_error": 2.1430520477294923,
                "gap_rejected_minus_accepted": 0.9685996167659761
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2626740634441376,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9435593045893169,
                "rejected_mean_error": 1.899699591697856,
                "gap_rejected_minus_accepted": 0.9561402871085392
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8267780360966538,
            "spearman": 0.8148499284438661,
            "auroc_top30_bad": 0.9149097142857143,
            "mae": 0.3287113126784563,
            "mse": 0.22341938079748583,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.488,
            "expert_lt_simvla_seed0": 0.948,
            "same_context_pred_std": 0.6542397912395874,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.44313042974472044
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.4612065442919731
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.634639479392767
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.005062174061934
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
            "pearson": 0.6107752622961349,
            "spearman": 0.6566030349944847,
            "auroc_top30_worst": 0.809408,
            "pairwise_seed_ranking": 0.7616,
            "predicted_best_mean_error": 1.7676162035465242,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.07598468232154842,
            "gap_to_oracle": 0.027765485286712854,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2188368673324586
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3758236765861511
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5444750946044923
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6686175761700692
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.066221809387207,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7559205482270983,
                "rejected_mean_error": 2.310755837917328,
                "gap_rejected_minus_accepted": 0.5548352896902295
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8887851238250732,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6682943178215557,
                "rejected_mean_error": 2.239818915962792,
                "gap_rejected_minus_accepted": 0.5715245981412362
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6247625350952148,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.5444750946044923,
                "rejected_mean_error": 2.07833305978775,
                "gap_rejected_minus_accepted": 0.5338579651832578
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.324768602848053,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.3758067524852082,
                "rejected_mean_error": 1.956913108823139,
                "gap_rejected_minus_accepted": 0.5811063563379308
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.104437565803528,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7771770885255602,
                "rejected_mean_error": 2.441415061950684,
                "gap_rejected_minus_accepted": 0.6642379734251236
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9087336361408234,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.679529844120862,
                "rejected_mean_error": 2.3306054066097928,
                "gap_rejected_minus_accepted": 0.6510755624889308
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6562851071357727,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5536101770401,
                "rejected_mean_error": 2.133591594696045,
                "gap_rejected_minus_accepted": 0.5799814176559448
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3638636469841003,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.3758373222653828,
                "rejected_mean_error": 2.0011896800229896,
                "gap_rejected_minus_accepted": 0.6253523577576068
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.7645924352197622,
            "spearman": 0.7633385837389995,
            "auroc_top30_bad": 0.8593380952380952,
            "mae": 0.4369719463866204,
            "mse": 0.32695931289638647,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.495,
            "expert_lt_simvla_seed0": 0.96,
            "same_context_pred_std": 0.6054353230167959,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4562195382267237
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.45228518060594797
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7949196201451123
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0855072754447659
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
            "pearson": 0.4105061083753797,
            "spearman": 0.4499073372570592,
            "auroc_top30_worst": 0.767747619047619,
            "pairwise_seed_ranking": 0.7075,
            "predicted_best_mean_error": 1.8851516875624656,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.04107837587594987,
            "gap_to_oracle": 0.02185030043125158,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.8863669073581695
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.7372561612129211
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.778692656517029
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8234567718505859
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.069823431968689,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8795900795194838,
                "rejected_mean_error": 2.231306254863739,
                "gap_rejected_minus_accepted": 0.35171617534425526
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9190280139446259,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8234567718505859,
                "rejected_mean_error": 2.188676472663879,
                "gap_rejected_minus_accepted": 0.36521970081329336
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4225564002990723,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.778692656517029,
                "rejected_mean_error": 2.0508307375907897,
                "gap_rejected_minus_accepted": 0.2721380810737608
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0505734384059906,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.7372561612129211,
                "rejected_mean_error": 1.9739302090009054,
                "gap_rejected_minus_accepted": 0.2366740477879843
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.067994165420532,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8965779536300236,
                "rejected_mean_error": 2.1930990517139435,
                "gap_rejected_minus_accepted": 0.2965210980839199
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9359078705310822,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8373638319969177,
                "rejected_mean_error": 2.192828757762909,
                "gap_rejected_minus_accepted": 0.3554649257659912
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4718773365020752,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.7909198606014252,
                "rejected_mean_error": 2.061540266275406,
                "gap_rejected_minus_accepted": 0.27062040567398093
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.057366818189621,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.7532806420326232,
                "rejected_mean_error": 1.9838798705736795,
                "gap_rejected_minus_accepted": 0.2305992285410563
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
      "best_epoch": 80,
      "best_calib_loss": 0.016199545934796333,
      "train_time_sec": 14.179060459136963,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9991927650744352,
            "spearman": 0.997840201068935,
            "auroc_top30_bad": 0.999468619047619,
            "mae": 0.033593001875944904,
            "mse": 0.0019178174517863911,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8012351275030942,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.007135039009153843
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17296551284492015
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4752140534862876
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8230078407118718
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
            "pearson": 0.9994006301629402,
            "spearman": 0.9991446288297849,
            "auroc_top30_worst": 0.9994744761904761,
            "pairwise_seed_ranking": 0.913,
            "predicted_best_mean_error": 1.775698792219162,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07432691907882694,
            "gap_to_oracle": 0.002059678971767509,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6047334839701652
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8409131698846817
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1148148594498635
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3617550705353418
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4416501283645635,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681385049621264,
                "rejected_mean_error": 4.289289808750152,
                "gap_rejected_minus_accepted": 2.7211513037880257
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.119139313697815,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3617550705353418,
                "rejected_mean_error": 3.2757493297576903,
                "gap_rejected_minus_accepted": 1.9139942592223484
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6178120970726013,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1148148594498635,
                "rejected_mean_error": 2.5656924112319945,
                "gap_rejected_minus_accepted": 1.450877551782131
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1267563998699188,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8409131698846817,
                "rejected_mean_error": 2.173367123826345,
                "gap_rejected_minus_accepted": 1.3324539539416633
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.431089472770691,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.57722972896364,
                "rejected_mean_error": 4.305189552307129,
                "gap_rejected_minus_accepted": 2.727959823343489
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.133366823196411,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3726710872650147,
                "rejected_mean_error": 3.2820895833969117,
                "gap_rejected_minus_accepted": 1.909418496131897
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6314061284065247,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1214297564029694,
                "rejected_mean_error": 2.5786216661930084,
                "gap_rejected_minus_accepted": 1.457191909790039
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1410291492938995,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8440425248146057,
                "rejected_mean_error": 2.1853534401257835,
                "gap_rejected_minus_accepted": 1.3413109153111777
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9714832914778857,
            "spearman": 0.9762600861026899,
            "auroc_top30_bad": 0.9937798095238095,
            "mae": 0.14003313137544318,
            "mse": 0.04094333297139959,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.968,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6918895346143349,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06369068735837936
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17660840694904328
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4098791843533516
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7781215458949406
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
            "pearson": 0.9389328434966566,
            "spearman": 0.9683590740218074,
            "auroc_top30_worst": 0.9915306666666667,
            "pairwise_seed_ranking": 0.9108,
            "predicted_best_mean_error": 1.563228112220764,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.0955241271257401,
            "gap_to_oracle": 0.004094951748847775,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4974269061088562
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.788666923267719
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0977652170181273
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3505361780428937
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.474877882003784,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5285091167026097,
                "rejected_mean_error": 2.6073303184509276,
                "gap_rejected_minus_accepted": 1.0788212017483179
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.118119478225708,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.349684703948022,
                "rejected_mean_error": 2.4946788450399526,
                "gap_rejected_minus_accepted": 1.1449941410919307
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5955020785331726,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0977652170181273,
                "rejected_mean_error": 2.1750172567367554,
                "gap_rejected_minus_accepted": 1.077252039718628
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1861034631729126,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7893789917135391,
                "rejected_mean_error": 1.9193312931595135,
                "gap_rejected_minus_accepted": 1.1299523014459742
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4954174757003784,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5515284507804448,
                "rejected_mean_error": 2.62376633644104,
                "gap_rejected_minus_accepted": 1.0722378856605954
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1315106749534607,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3647512128965102,
                "rejected_mean_error": 2.5314219527774386,
                "gap_rejected_minus_accepted": 1.1666707398809284
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.61833256483078,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1178691313266753,
                "rejected_mean_error": 2.199635347366333,
                "gap_rejected_minus_accepted": 1.0817662160396575
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2142391800880432,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.800006048546897,
                "rejected_mean_error": 1.9480624533592061,
                "gap_rejected_minus_accepted": 1.148056404812309
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9634650908821137,
            "spearman": 0.9576305483130657,
            "auroc_top30_bad": 0.9759318095238095,
            "mae": 0.16453122231066228,
            "mse": 0.05189375545114588,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.6564218907473521,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0873999803364277
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19968060513734817
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5888763225495816
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9696079151113828
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
            "pearson": 0.9275070448395326,
            "spearman": 0.9348902898777771,
            "auroc_top30_worst": 0.9626300952380953,
            "pairwise_seed_ranking": 0.882,
            "predicted_best_mean_error": 1.746764581680298,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.09683630418777467,
            "gap_to_oracle": 0.00691386342048661,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9118931694030762
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2063561574770854
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4508112533569335
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6249939703356737
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2214797735214233,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7327651488516065,
                "rejected_mean_error": 2.519154432296753,
                "gap_rejected_minus_accepted": 0.7863892834451465
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.95327228307724,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6244913403863204,
                "rejected_mean_error": 2.3709479570388794,
                "gap_rejected_minus_accepted": 0.746456616652559
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7056385278701782,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4508112533569335,
                "rejected_mean_error": 2.1719969010353086,
                "gap_rejected_minus_accepted": 0.7211856476783751
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.450898826122284,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.2071060555430646,
                "rejected_mean_error": 2.013266703426011,
                "gap_rejected_minus_accepted": 0.8061606478829464
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.251624274253845,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7559691826502482,
                "rejected_mean_error": 2.632286214828491,
                "gap_rejected_minus_accepted": 0.876317032178243
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9699656665325165,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6332041975011162,
                "rejected_mean_error": 2.468111691020784,
                "gap_rejected_minus_accepted": 0.8349074935196679
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7169107794761658,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.459865511894226,
                "rejected_mean_error": 2.227336259841919,
                "gap_rejected_minus_accepted": 0.7674707479476928
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4773904085159302,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2129251692030165,
                "rejected_mean_error": 2.0560745230333053,
                "gap_rejected_minus_accepted": 0.8431493538302888
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9727928697890436,
            "spearman": 0.9531698490784635,
            "auroc_top30_bad": 0.9529380952380953,
            "mae": 0.18878096270008246,
            "mse": 0.05697810001200229,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.995,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6465766508969566,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08675839120522141
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.190742608346045
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6747503162659705
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0624326721057296
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
            "pearson": 0.8749374387332451,
            "spearman": 0.8825629745629745,
            "auroc_top30_worst": 0.9572809523809525,
            "pairwise_seed_ranking": 0.8715,
            "predicted_best_mean_error": 1.8681413140892982,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.05808874934911734,
            "gap_to_oracle": 0.0048399269580841064,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.420948475599289
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.51396284866333
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6485292596817016
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7682143756548563
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1498655319213866,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8536316967010498,
                "rejected_mean_error": 2.464931700229645,
                "gap_rejected_minus_accepted": 0.6113000035285951
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8952171504497528,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7682143756548563,
                "rejected_mean_error": 2.354403661251068,
                "gap_rejected_minus_accepted": 0.5861892855962119
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6755387783050537,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6485292596817016,
                "rejected_mean_error": 2.180994134426117,
                "gap_rejected_minus_accepted": 0.5324648747444154
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4744142591953278,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.51396284866333,
                "rejected_mean_error": 2.0483613131841025,
                "gap_rejected_minus_accepted": 0.5343984645207724
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.145141291618347,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8658952593803406,
                "rejected_mean_error": 2.4692432999610903,
                "gap_rejected_minus_accepted": 0.6033480405807496
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.907660186290741,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7792473483085631,
                "rejected_mean_error": 2.3671782088279723,
                "gap_rejected_minus_accepted": 0.5879308605194091
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6849393844604492,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.661164685487747,
                "rejected_mean_error": 2.1912954413890837,
                "gap_rejected_minus_accepted": 0.5301307559013366
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4964033961296082,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5179999017715453,
                "rejected_mean_error": 2.062306783994039,
                "gap_rejected_minus_accepted": 0.5443068822224937
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
      "best_epoch": 78,
      "best_calib_loss": 0.00922413356602192,
      "train_time_sec": 34.80931901931763,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997641479565641,
            "spearman": 0.9989268619267572,
            "auroc_top30_bad": 0.9998392380952381,
            "mae": 0.01881738333045505,
            "mse": 0.0007000270840525452,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7965928020664896,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0005118973702192307
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17255428595244884
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47506957986205817
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8225349433094263
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
            "pearson": 0.9997579296667365,
            "spearman": 0.9998048546481941,
            "auroc_top30_worst": 0.9999198095238095,
            "pairwise_seed_ranking": 0.9532,
            "predicted_best_mean_error": 1.7742156014740467,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07581010982394232,
            "gap_to_oracle": 0.0005764882266521276,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6038524212241173
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8401909522294998
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1144175255894662
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.361621087495486
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4255178689956676,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681292934219042,
                "rejected_mean_error": 4.289372712612152,
                "gap_rejected_minus_accepted": 2.7212434191902473
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.108215868473053,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.361621087495486,
                "rejected_mean_error": 3.276151278877258,
                "gap_rejected_minus_accepted": 1.9145301913817723
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6181873679161072,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1144175255894662,
                "rejected_mean_error": 2.566089745092392,
                "gap_rejected_minus_accepted": 1.451672219502926
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1321427822113037,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8401909522294998,
                "rejected_mean_error": 2.173607863044739,
                "gap_rejected_minus_accepted": 1.333416910815239
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.3825411796569833,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.134982943534851,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3725075308481853,
                "rejected_mean_error": 3.2825802526473997,
                "gap_rejected_minus_accepted": 1.9100727217992144
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.650318682193756,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.121159267425537,
                "rejected_mean_error": 2.5788921551704407,
                "gap_rejected_minus_accepted": 1.4577328877449036
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.145195484161377,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8436733469963074,
                "rejected_mean_error": 2.1854764993985496,
                "gap_rejected_minus_accepted": 1.3418031524022422
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9848027143146112,
            "spearman": 0.9873826424881212,
            "auroc_top30_bad": 0.9973965714285715,
            "mae": 0.09280485459882766,
            "mse": 0.02172768862379239,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7272020231821337,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05818270206451416
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16417884776592254
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4025640545964241
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7751104462067286
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
            "pearson": 0.9654963923194224,
            "spearman": 0.9869334301013954,
            "auroc_top30_worst": 0.9939961904761905,
            "pairwise_seed_ranking": 0.9388,
            "predicted_best_mean_error": 1.5599303587675095,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09882188057899466,
            "gap_to_oracle": 0.0007971982955932155,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46511230516433716
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7502187484732041
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0914653871536255
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3465260338427416
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5470976352691657,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5135126152038574,
                "rejected_mean_error": 2.7422988319396975,
                "gap_rejected_minus_accepted": 1.22878621673584
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.080787181854248,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3457583691547113,
                "rejected_mean_error": 2.5064327610186496,
                "gap_rejected_minus_accepted": 1.1606743918639384
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.662714421749115,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0914653871536255,
                "rejected_mean_error": 2.1813170866012572,
                "gap_rejected_minus_accepted": 1.0898516994476317
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1098701059818268,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7512874532812319,
                "rejected_mean_error": 1.9320555744074452,
                "gap_rejected_minus_accepted": 1.1807681211262133
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5671860218048095,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5304330678780873,
                "rejected_mean_error": 2.813624782562256,
                "gap_rejected_minus_accepted": 1.2831917146841685
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.098213315010071,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3633799943375715,
                "rejected_mean_error": 2.535492077706352,
                "gap_rejected_minus_accepted": 1.1721120833687806
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6787967681884766,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.11210355591774,
                "rejected_mean_error": 2.2054009227752687,
                "gap_rejected_minus_accepted": 1.0932973668575288
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1369667947292328,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7624138068585169,
                "rejected_mean_error": 1.9607272192756122,
                "gap_rejected_minus_accepted": 1.1983134124170953
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9855289703951402,
            "spearman": 0.9856328237245761,
            "auroc_top30_bad": 0.9900860952380953,
            "mae": 0.09110901346895844,
            "mse": 0.020125125196691133,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7068078277480199,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04319105112552643
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1744463928580284
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5721073920667171
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9599435892383258
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
            "pearson": 0.9524634924354436,
            "spearman": 0.9753821420307581,
            "auroc_top30_worst": 0.9770087619047618,
            "pairwise_seed_ranking": 0.9336,
            "predicted_best_mean_error": 1.7420140650272369,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.1015868208408357,
            "gap_to_oracle": 0.002163346767425578,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8721643424034119
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1817388758063316
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4368013283729553
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6132450985120559
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2751375198364263,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7245807701216804,
                "rejected_mean_error": 2.592813840866089,
                "gap_rejected_minus_accepted": 0.8682330707444084
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0090808272361755,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6125679534552828,
                "rejected_mean_error": 2.4066419300560753,
                "gap_rejected_minus_accepted": 0.7940739766007925
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7884730696678162,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4368013283729553,
                "rejected_mean_error": 2.186006826019287,
                "gap_rejected_minus_accepted": 0.7492054976463318
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5022497475147247,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1828200857098492,
                "rejected_mean_error": 2.021379305942336,
                "gap_rejected_minus_accepted": 0.8385592202324867
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3772403478622435,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7490210655000475,
                "rejected_mean_error": 2.694819269180298,
                "gap_rejected_minus_accepted": 0.9457982036802504
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0289787650108337,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6236376972759472,
                "rejected_mean_error": 2.496507493276445,
                "gap_rejected_minus_accepted": 0.8728697960004976
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8181908130645752,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4468697690963745,
                "rejected_mean_error": 2.2403320026397706,
                "gap_rejected_minus_accepted": 0.7934622335433961
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5448409020900726,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1901155502077132,
                "rejected_mean_error": 2.0637590470798512,
                "gap_rejected_minus_accepted": 0.873643496872138
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9898643240421033,
            "spearman": 0.9723180501931636,
            "auroc_top30_bad": 0.9658,
            "mae": 0.09907551642716862,
            "mse": 0.017333816886367922,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7166156117986069,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.043977168146520855
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16944510502368212
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6618387693203985
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0581919903780024
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
            "pearson": 0.9527810418987473,
            "spearman": 0.9204121644121644,
            "auroc_top30_worst": 0.9657190476190477,
            "pairwise_seed_ranking": 0.917,
            "predicted_best_mean_error": 1.8648668828606605,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06136318057775503,
            "gap_to_oracle": 0.00156549572944642,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2947825002670288
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4488819861412048
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.659000018119812
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.765569986184438
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.215623617172241,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8440360188484193,
                "rejected_mean_error": 2.5512928009033202,
                "gap_rejected_minus_accepted": 0.707256782054901
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0206016898155212,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.765569986184438,
                "rejected_mean_error": 2.362336829662323,
                "gap_rejected_minus_accepted": 0.5967668434778848
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.837638795375824,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.659000018119812,
                "rejected_mean_error": 2.1705233759880067,
                "gap_rejected_minus_accepted": 0.5115233578681948
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6369534134864807,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4488819861412048,
                "rejected_mean_error": 2.0700549340248107,
                "gap_rejected_minus_accepted": 0.6211729478836059
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2260414361953735,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8553364290131462,
                "rejected_mean_error": 2.564272773265839,
                "gap_rejected_minus_accepted": 0.7089363442526926
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0386186838150024,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7717185123761494,
                "rejected_mean_error": 2.389764716625214,
                "gap_rejected_minus_accepted": 0.6180462042490644
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.843848466873169,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.665837494134903,
                "rejected_mean_error": 2.186622632741928,
                "gap_rejected_minus_accepted": 0.520785138607025
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6643955707550049,
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
    }
  ]
}
```
