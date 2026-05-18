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
      "best_epoch": 14,
      "best_calib_loss": 0.09294075518846512,
      "train_time_sec": 11.517884254455566,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8575629996678241,
            "spearman": 0.8052591233236601,
            "auroc_top30_bad": 0.893127738095238,
            "mae": 0.23569052840694785,
            "mse": 0.22521408979916974,
            "expert_lt_perturb_large": 0.987,
            "expert_lt_other_task": 0.501,
            "expert_lt_simvla_seed0": 0.978,
            "same_context_pred_std": 0.6964208970400078,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4783627574443817
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5266363224089146
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6886591502785683
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9556863846004009
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
            "pearson": 0.9938073209979778,
            "spearman": 0.9890203019845485,
            "auroc_top30_worst": 0.9963382857142856,
            "pairwise_seed_ranking": 0.7758,
            "predicted_best_mean_error": 1.5453800049722195,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.07022832304239279,
            "gap_to_oracle": 0.016520770788192696,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6818114988207817
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8181055158376693
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0142136981844903
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2428584992011389
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.732161855697633,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.406349954466025,
                "rejected_mean_error": 3.450638281822205,
                "gap_rejected_minus_accepted": 2.04428832735618
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9424995183944702,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2428584992011389,
                "rejected_mean_error": 2.7145396512031557,
                "gap_rejected_minus_accepted": 1.4716811520020168
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4326094388961792,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0142136981844903,
                "rejected_mean_error": 2.2073438762187956,
                "gap_rejected_minus_accepted": 1.1931301780343053
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.086909532546997,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8181055158376693,
                "rejected_mean_error": 1.8750032109896342,
                "gap_rejected_minus_accepted": 1.0568976951519649
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.718175101280213,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4117145182357893,
                "rejected_mean_error": 3.4506526160240174,
                "gap_rejected_minus_accepted": 2.038938097788228
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.971927523612976,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.244862311244011,
                "rejected_mean_error": 2.727846378326416,
                "gap_rejected_minus_accepted": 1.482984067082405
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4387332201004028,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0077112367749215,
                "rejected_mean_error": 2.223505419254303,
                "gap_rejected_minus_accepted": 1.2157941824793816
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0891426801681519,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8140612343549728,
                "rejected_mean_error": 1.8827906925678253,
                "gap_rejected_minus_accepted": 1.0687294582128524
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.5273583174203786,
            "spearman": 0.4794971451164368,
            "auroc_top30_bad": 0.6557619047619048,
            "mae": 0.47654644829034803,
            "mse": 0.5246175202627351,
            "expert_lt_perturb_large": 0.972,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.968,
            "same_context_pred_std": 0.6305508834018185,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5223716715574265
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7887582639217376
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9456541944384574
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1789559818983077
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
            "pearson": 0.430320282384764,
            "spearman": 0.4498270270892974,
            "auroc_top30_worst": 0.7111253333333333,
            "pairwise_seed_ranking": 0.7016,
            "predicted_best_mean_error": 1.491066266298294,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.03772755742073053,
            "gap_to_oracle": 0.028223244190216157,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9349137449264526
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1543043464040146
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3788413235664367
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.49116817313725
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.130832052230835,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.526471169842614,
                "rejected_mean_error": 1.626743088245392,
                "gap_rejected_minus_accepted": 0.10027191840277783
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8758064806461334,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4908551195260682,
                "rejected_mean_error": 1.6731364380437346,
                "gap_rejected_minus_accepted": 0.18228131851766638
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.580760419368744,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3788413235664367,
                "rejected_mean_error": 1.6941553997993468,
                "gap_rejected_minus_accepted": 0.3153140762329101
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.351045846939087,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1561406848910518,
                "rejected_mean_error": 1.663554874848149,
                "gap_rejected_minus_accepted": 0.5074141899570972
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.132810926437378,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5146567376454672,
                "rejected_mean_error": 1.6560275983810424,
                "gap_rejected_minus_accepted": 0.14137086073557525
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9016230702400208,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.484100527941862,
                "rejected_mean_error": 1.6614548762639363,
                "gap_rejected_minus_accepted": 0.1773543483220743
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5858524441719055,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3743509907722473,
                "rejected_mean_error": 1.683236656665802,
                "gap_rejected_minus_accepted": 0.3088856658935546
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3461579978466034,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1209688404249767,
                "rejected_mean_error": 1.6661894063261105,
                "gap_rejected_minus_accepted": 0.5452205659011338
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.3882590821797509,
            "spearman": 0.32691720698932264,
            "auroc_top30_bad": 0.5401828571428571,
            "mae": 0.6883894992232322,
            "mse": 0.8817506885098887,
            "expert_lt_perturb_large": 0.928,
            "expert_lt_other_task": 0.504,
            "expert_lt_simvla_seed0": 0.804,
            "same_context_pred_std": 0.643956977606795,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4868811802864075
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7358328689098358
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2061746242880822
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3377290196816127
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
            "pearson": -0.00044710439992198814,
            "spearman": -0.1634323759467849,
            "auroc_top30_worst": 0.3002788571428571,
            "pairwise_seed_ranking": 0.6728,
            "predicted_best_mean_error": 1.7635456284284592,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.04360295295715333,
            "gap_to_oracle": 0.03965882825851441,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.8808742549419404
              },
              {
                "coverage": 0.25,
                "mean_true_error": 2.343646932297792
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.876109552669525
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8065391488548026
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7344855308532727,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7469135505888198,
                "rejected_mean_error": 2.3023739194869997,
                "gap_rejected_minus_accepted": 0.5554603688981798
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9265385866165161,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.8070556410730458,
                "rejected_mean_error": 1.7887007944500104,
                "gap_rejected_minus_accepted": -0.018354846623035437
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5329932570457458,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.876109552669525,
                "rejected_mean_error": 1.7288096222877503,
                "gap_rejected_minus_accepted": -0.1472999303817748
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.083938479423523,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 2.3456955506397894,
                "rejected_mean_error": 1.6209944258250193,
                "gap_rejected_minus_accepted": -0.7247011248147701
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.66684501171112,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7481526039706337,
                "rejected_mean_error": 2.3381123781204223,
                "gap_rejected_minus_accepted": 0.5899597741497886
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9128975570201874,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.8117556117753932,
                "rejected_mean_error": 1.7934737451492795,
                "gap_rejected_minus_accepted": -0.018281866626113752
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5514943599700928,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8871739308834077,
                "rejected_mean_error": 1.7271232318878174,
                "gap_rejected_minus_accepted": -0.16005069899559032
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0435656607151031,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 2.307261209166239,
                "rejected_mean_error": 1.638661439406043,
                "gap_rejected_minus_accepted": -0.668599769760196
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6078745462753552,
            "spearman": 0.58710421049417,
            "auroc_top30_bad": 0.7867950476190476,
            "mae": 0.4990412243068218,
            "mse": 0.49637915293220414,
            "expert_lt_perturb_large": 0.968,
            "expert_lt_other_task": 0.524,
            "expert_lt_simvla_seed0": 0.92,
            "same_context_pred_std": 0.6780914165989115,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6680240783691406
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6061161405086517
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8663659070134163
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0632014576911926
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
            "pearson": 0.657896173959372,
            "spearman": 0.5692898721855183,
            "auroc_top30_worst": 0.8518491428571429,
            "pairwise_seed_ranking": 0.7344,
            "predicted_best_mean_error": 1.5696335773468018,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.04968870091438293,
            "gap_to_oracle": 0.018490317106246934,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7252398989200592
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1321765424158328
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3089682215213776
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4053824067052239
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.300009894371033,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5176568603250715,
                "rejected_mean_error": 2.5711916031837463,
                "gap_rejected_minus_accepted": 1.0535347428586748
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0373146533966064,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.404557031876504,
                "rejected_mean_error": 2.2769743750651426,
                "gap_rejected_minus_accepted": 0.8724173431886386
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.756106436252594,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3089682215213776,
                "rejected_mean_error": 1.9370524477005004,
                "gap_rejected_minus_accepted": 0.6280842261791229
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4680699110031128,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1346191555356826,
                "rejected_mean_error": 1.7861548800224174,
                "gap_rejected_minus_accepted": 0.6515357244867348
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3074378252029417,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4980728952089946,
                "rejected_mean_error": 2.710566725730896,
                "gap_rejected_minus_accepted": 1.2124938305219013
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.068475127220154,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3801637562838467,
                "rejected_mean_error": 2.329205510162172,
                "gap_rejected_minus_accepted": 0.9490417538783253
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7619138956069946,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.290178345680237,
                "rejected_mean_error": 1.9484662108421327,
                "gap_rejected_minus_accepted": 0.6582878651618957
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4418484270572662,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0744056162380038,
                "rejected_mean_error": 1.8029038274989408,
                "gap_rejected_minus_accepted": 0.7284982112609371
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
      "best_epoch": 67,
      "best_calib_loss": 0.027394931763410568,
      "train_time_sec": 14.448170900344849,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9978075836027575,
            "spearman": 0.9963131983871599,
            "auroc_top30_bad": 0.9984924285714285,
            "mae": 0.04732378007825464,
            "mse": 0.0037672657679466925,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7365508502098697,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04095915700495243
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1987576021671295
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5743540410757065
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9273827073256175
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
            "pearson": 0.9988251832638935,
            "spearman": 0.9980419694495377,
            "auroc_top30_worst": 0.9987024761904763,
            "pairwise_seed_ranking": 0.9123,
            "predicted_best_mean_error": 1.5325768420994281,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08303148591518417,
            "gap_to_oracle": 0.003717607915401322,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6674591290354729
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8079724783182144
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0105431289076805
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.241749489235878
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7463833808898928,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4057531334757805,
                "rejected_mean_error": 3.4560096707344057,
                "gap_rejected_minus_accepted": 2.0502565372586252
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9353728294372559,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.241749489235878,
                "rejected_mean_error": 2.717866681098938,
                "gap_rejected_minus_accepted": 1.47611719186306
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4016616940498352,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0105431289076805,
                "rejected_mean_error": 2.2110144454956053,
                "gap_rejected_minus_accepted": 1.2004713165879248
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0137713551521301,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8079724783182144,
                "rejected_mean_error": 1.8783808901627859,
                "gap_rejected_minus_accepted": 1.0704084118445714
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7694200038909913,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106759033269352,
                "rejected_mean_error": 3.460000150203705,
                "gap_rejected_minus_accepted": 2.04932424687677
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9593108892440796,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2434973446925481,
                "rejected_mean_error": 2.7319412779808045,
                "gap_rejected_minus_accepted": 1.4884439332882564
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.400734782218933,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0041387591958046,
                "rejected_mean_error": 2.22707789683342,
                "gap_rejected_minus_accepted": 1.2229391376376153
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.01592156291008,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7996499010324478,
                "rejected_mean_error": 1.8875944703420002,
                "gap_rejected_minus_accepted": 1.0879445693095524
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9354756425425153,
            "spearman": 0.9313223983325222,
            "auroc_top30_bad": 0.9417683809523811,
            "mae": 0.1982980613157153,
            "mse": 0.07739619608878855,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.948,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6032685540404482,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11221746039390564
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2999288831710815
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.70923505474329
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0492566940546035
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
            "pearson": 0.8692564483648322,
            "spearman": 0.8611193683963958,
            "auroc_top30_worst": 0.9052312380952381,
            "pairwise_seed_ranking": 0.8148,
            "predicted_best_mean_error": 1.477442724943161,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.051351098775863635,
            "gap_to_oracle": 0.01459970283508305,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9229984288215637
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0371270130077999
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2136320344924927
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3813937235234388
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0967674970626833,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.461576362186008,
                "rejected_mean_error": 2.2107963571548463,
                "gap_rejected_minus_accepted": 0.7492199949688383
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.826757401227951,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3807571593318195,
                "rejected_mean_error": 2.0027268172833868,
                "gap_rejected_minus_accepted": 0.6219696579515672
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5424827933311462,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2136320344924927,
                "rejected_mean_error": 1.859364688873291,
                "gap_rejected_minus_accepted": 0.6457326543807984
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2797262966632843,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0378980670874112,
                "rejected_mean_error": 1.7030532092905604,
                "gap_rejected_minus_accepted": 0.6651551422031492
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0979671716690063,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4562899006737604,
                "rejected_mean_error": 2.181329131126404,
                "gap_rejected_minus_accepted": 0.7250392304526434
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8370651006698608,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.37093088907354,
                "rejected_mean_error": 1.9973711059207009,
                "gap_rejected_minus_accepted": 0.6264402168471608
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5407328009605408,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.204837067604065,
                "rejected_mean_error": 1.8527505798339843,
                "gap_rejected_minus_accepted": 0.6479135122299193
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2504287362098694,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0170034624281383,
                "rejected_mean_error": 1.7012151753838687,
                "gap_rejected_minus_accepted": 0.6842117129557304
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9350053581197448,
            "spearman": 0.9429996431343848,
            "auroc_top30_bad": 0.9653196190476191,
            "mae": 0.250747633472085,
            "mse": 0.12215676177400307,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6536390742736592,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11567442381381988
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.29417941846847534
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7216335328936577
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.058471568353971
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
            "pearson": 0.9395823993957678,
            "spearman": 0.9160042531867222,
            "auroc_top30_worst": 0.9877881904761905,
            "pairwise_seed_ranking": 0.842,
            "predicted_best_mean_error": 1.7308507021665573,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.07629787921905518,
            "gap_to_oracle": 0.006963901996612565,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0472445154190064
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.165566977017965
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3124252708435058
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.456816210929773
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.671954941749573,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.656593971464369,
                "rejected_mean_error": 3.1152501316070556,
                "gap_rejected_minus_accepted": 1.4586561601426866
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.419646203517914,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4562458934753402,
                "rejected_mean_error": 2.838888441411832,
                "gap_rejected_minus_accepted": 1.3826425479364917
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7307794094085693,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3124252708435058,
                "rejected_mean_error": 2.2924939041137695,
                "gap_rejected_minus_accepted": 0.9800686332702637
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4984720349311829,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1659330647593489,
                "rejected_mean_error": 2.015087977671954,
                "gap_rejected_minus_accepted": 0.849154912912605
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6692819595336914,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6548357559574975,
                "rejected_mean_error": 3.1779640102386475,
                "gap_rejected_minus_accepted": 1.52312825428115
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.440624237060547,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4545739422188724,
                "rejected_mean_error": 2.8536796531979998,
                "gap_rejected_minus_accepted": 1.3991057109791274
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7194841504096985,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3042151486873628,
                "rejected_mean_error": 2.3100820140838625,
                "gap_rejected_minus_accepted": 1.0058668653964997
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.500964343547821,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1645411882135603,
                "rejected_mean_error": 2.0236419812243254,
                "gap_rejected_minus_accepted": 0.859100793010765
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9478585512596417,
            "spearman": 0.9445235678354501,
            "auroc_top30_bad": 0.962320761904762,
            "mae": 0.2186111081548035,
            "mse": 0.08531474349399154,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6293566288173733,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1269857068657875
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.26331394333839414
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6114150351285934
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9505829755783081
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
            "pearson": 0.9613625244669624,
            "spearman": 0.9434142521691214,
            "auroc_top30_worst": 0.9916617142857144,
            "pairwise_seed_ranking": 0.8724,
            "predicted_best_mean_error": 1.5573115348815918,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06201074337959289,
            "gap_to_oracle": 0.006168274641036975,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6264992587566376
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9312860871163698
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1239117893695831
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.311396789099616
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7315343379974366,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.475135314544042,
                "rejected_mean_error": 2.953885515213013,
                "gap_rejected_minus_accepted": 1.4787502006689708
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2209523916244507,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3109614682744637,
                "rejected_mean_error": 2.557163011151762,
                "gap_rejected_minus_accepted": 1.2462015428772981
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6925190687179565,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1239117893695831,
                "rejected_mean_error": 2.122108879852295,
                "gap_rejected_minus_accepted": 0.9981970904827118
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2875370681285858,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9321274457457728,
                "rejected_mean_error": 1.8537961875616296,
                "gap_rejected_minus_accepted": 0.9216687418158568
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7160826206207274,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4670894095632765,
                "rejected_mean_error": 2.9894180965423582,
                "gap_rejected_minus_accepted": 1.5223286869790817
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2229577898979187,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2970597058693993,
                "rejected_mean_error": 2.5758794375828336,
                "gap_rejected_minus_accepted": 1.2788197317134342
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6575849652290344,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1128667855262757,
                "rejected_mean_error": 2.125777770996094,
                "gap_rejected_minus_accepted": 1.0129109854698182
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.290791928768158,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.909395262362465,
                "rejected_mean_error": 1.858495550997117,
                "gap_rejected_minus_accepted": 0.949100288634652
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
      "best_epoch": 70,
      "best_calib_loss": 0.006694100797176361,
      "train_time_sec": 35.17915153503418,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996726790245349,
            "spearman": 0.9987638062170063,
            "auroc_top30_bad": 0.9997703333333334,
            "mae": 0.02168004155983217,
            "mse": 0.0007696761887844434,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7366862221599536,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00047208963334560396
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19778824577331544
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5739945960760117
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9267414147377014
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
            "pearson": 0.9996211137677866,
            "spearman": 0.9994099816723991,
            "auroc_top30_worst": 0.9999173333333333,
            "pairwise_seed_ranking": 0.9525,
            "predicted_best_mean_error": 1.5306339201033115,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08497440791130084,
            "gap_to_oracle": 0.0017746859192846465,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6661121190190316
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8071833005666733
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.010111699473858
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2413145092566809
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7535242080688476,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056603148447142,
                "rejected_mean_error": 3.4568450384140013,
                "gap_rejected_minus_accepted": 2.0511847235692873
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.956998497247696,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2413145092566809,
                "rejected_mean_error": 2.7191716210365295,
                "gap_rejected_minus_accepted": 1.4778571117798487
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3891035914421082,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.010111699473858,
                "rejected_mean_error": 2.211445874929428,
                "gap_rejected_minus_accepted": 1.20133417545557
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0058632791042328,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8071833005666733,
                "rejected_mean_error": 1.8786439494132996,
                "gap_rejected_minus_accepted": 1.0714606488466263
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7914886713027953,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106119764182303,
                "rejected_mean_error": 3.4605754923820498,
                "gap_rejected_minus_accepted": 2.049963515963819
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.974058985710144,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.24300752389431,
                "rejected_mean_error": 2.733410740375519,
                "gap_rejected_minus_accepted": 1.4904032164812089
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3944340944290161,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0038486118912697,
                "rejected_mean_error": 2.227368044137955,
                "gap_rejected_minus_accepted": 1.2235194322466851
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9982530772686005,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7987657254934311,
                "rejected_mean_error": 1.8878891955216726,
                "gap_rejected_minus_accepted": 1.0891234700282415
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9878910500134591,
            "spearman": 0.9845639643496997,
            "auroc_top30_bad": 0.9868335238095239,
            "mae": 0.08523042771052569,
            "mse": 0.014183009032573983,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7056369397260385,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04892170852422714
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22525068085193634
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6792801681876183
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0348482067982356
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
            "pearson": 0.9767628080312402,
            "spearman": 0.9782726455504933,
            "auroc_top30_worst": 0.9860632380952381,
            "pairwise_seed_ranking": 0.8896,
            "predicted_best_mean_error": 1.470212511062622,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.05858131265640254,
            "gap_to_oracle": 0.0073694889545441455,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8770282530784607
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9777975869484437
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.169911709213257
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.359986284394254
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.096766543388367,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.458859046406216,
                "rejected_mean_error": 2.2352521991729737,
                "gap_rejected_minus_accepted": 0.7763931527667576
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9078397452831268,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3594508785575532,
                "rejected_mean_error": 2.0665095172370203,
                "gap_rejected_minus_accepted": 0.707058638679467
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5421288013458252,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.169911709213257,
                "rejected_mean_error": 1.9030850141525268,
                "gap_rejected_minus_accepted": 0.7331733049392699
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.141396403312683,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9782816636295745,
                "rejected_mean_error": 1.7229677602855475,
                "gap_rejected_minus_accepted": 0.7446860966559731
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.11706485748291,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4538903257581923,
                "rejected_mean_error": 2.202925305366516,
                "gap_rejected_minus_accepted": 0.7490349796083238
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9067752957344055,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3512565018658969,
                "rejected_mean_error": 2.055769683822753,
                "gap_rejected_minus_accepted": 0.704513181956856
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5467024445533752,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1571773328781128,
                "rejected_mean_error": 1.9004103145599365,
                "gap_rejected_minus_accepted": 0.7432329816818237
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1645146608352661,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9611913722658915,
                "rejected_mean_error": 1.720018179021417,
                "gap_rejected_minus_accepted": 0.7588268067555256
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9663336247836651,
            "spearman": 0.9743825855176665,
            "auroc_top30_bad": 0.9844899047619048,
            "mae": 0.16137306782519445,
            "mse": 0.06499782999889342,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7042592350020916,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0794628911614418
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21541832716464995
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6948135347247124
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0515818995078405
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
            "pearson": 0.9311517536876666,
            "spearman": 0.9625550976992627,
            "auroc_top30_worst": 0.9784685714285715,
            "pairwise_seed_ranking": 0.9136,
            "predicted_best_mean_error": 1.7260646203756331,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08108396100997939,
            "gap_to_oracle": 0.0021778202056883522,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9461087350845336
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1134620018494434
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3028906061172485
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4611440025158782
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1942459106445313,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6510383565690783,
                "rejected_mean_error": 3.165250665664673,
                "gap_rejected_minus_accepted": 1.5142123090955948
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8813167214393616,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4608885824616715,
                "rejected_mean_error": 2.824990040197159,
                "gap_rejected_minus_accepted": 1.3641014577354875
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6250633597373962,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3028906061172485,
                "rejected_mean_error": 2.302028568840027,
                "gap_rejected_minus_accepted": 0.9991379627227785
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3681565821170807,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1140214970317512,
                "rejected_mean_error": 2.032428768172208,
                "gap_rejected_minus_accepted": 0.9184072711404567
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.181921935081482,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6511795032024383,
                "rejected_mean_error": 3.2108702850341797,
                "gap_rejected_minus_accepted": 1.5596907818317414
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8963002264499664,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4597867464317995,
                "rejected_mean_error": 2.8382067264072477,
                "gap_rejected_minus_accepted": 1.3784199799754482
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6317350268363953,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2963652198314666,
                "rejected_mean_error": 2.3179319429397585,
                "gap_rejected_minus_accepted": 1.0215667231082919
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3650125861167908,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1125982332797277,
                "rejected_mean_error": 2.0411414794105895,
                "gap_rejected_minus_accepted": 0.9285432461308618
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9881110645943968,
            "spearman": 0.9856251946518929,
            "auroc_top30_bad": 0.9957371428571429,
            "mae": 0.09467224430404604,
            "mse": 0.019450660085699546,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.952,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7602985682004697,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0929322669506073
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19863458104133605
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5893852776527405
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9341900427500407
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
            "pearson": 0.9806330270128658,
            "spearman": 0.9820676923313233,
            "auroc_top30_worst": 0.9953493333333333,
            "pairwise_seed_ranking": 0.9268,
            "predicted_best_mean_error": 1.5548980807065964,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06442419755458828,
            "gap_to_oracle": 0.0037548204660415863,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5697726953029633
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.870784293478116
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1175191538333893
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3122358021260834
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6619315147399902,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4771119389269087,
                "rejected_mean_error": 2.936095895767212,
                "gap_rejected_minus_accepted": 1.4589839568403031
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.054430603981018,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.311413907604004,
                "rejected_mean_error": 2.5558085841492724,
                "gap_rejected_minus_accepted": 1.2443946765452685
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.568527102470398,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1175191538333893,
                "rejected_mean_error": 2.1285015153884888,
                "gap_rejected_minus_accepted": 1.0109823615550995
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2681873440742493,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8717448422893549,
                "rejected_mean_error": 1.8739666837002196,
                "gap_rejected_minus_accepted": 1.0022218414108646
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.643825578689575,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4691338721911114,
                "rejected_mean_error": 2.971017932891846,
                "gap_rejected_minus_accepted": 1.5018840607007344
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0632710456848145,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2984497531212587,
                "rejected_mean_error": 2.5717534243114413,
                "gap_rejected_minus_accepted": 1.2733036711901826
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5819151401519775,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1042517943382264,
                "rejected_mean_error": 2.134392762184143,
                "gap_rejected_minus_accepted": 1.0301409678459166
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.272029459476471,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.85269215088042,
                "rejected_mean_error": 1.8775987382878594,
                "gap_rejected_minus_accepted": 1.0249065874074392
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
      "best_epoch": 80,
      "best_calib_loss": 0.010227088816463947,
      "train_time_sec": 41.1669340133667,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9984259369308672,
            "spearman": 0.9972891661424303,
            "auroc_top30_bad": 0.9984587142857143,
            "mae": 0.04472106186172641,
            "mse": 0.0036570473041040996,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7541087058215126,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.002457388922572136
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1982763353586197
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5743537674903869
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9273555032412211
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
            "pearson": 0.99828171771905,
            "spearman": 0.9977731631749264,
            "auroc_top30_worst": 0.9989485714285714,
            "pairwise_seed_ranking": 0.9579,
            "predicted_best_mean_error": 1.531189804136753,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.0844185238778592,
            "gap_to_oracle": 0.0023305699527262913,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6689263922572136
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8083421442747116
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0107754069209098
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2416202474514644
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8268623828887955,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4059831616282463,
                "rejected_mean_error": 3.4539394173622133,
                "gap_rejected_minus_accepted": 2.047956255733967
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.012967884540558,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2416202474514644,
                "rejected_mean_error": 2.718254406452179,
                "gap_rejected_minus_accepted": 1.4766341590007146
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4652818441390991,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0107754069209098,
                "rejected_mean_error": 2.210782167482376,
                "gap_rejected_minus_accepted": 1.2000067605614662
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0869021713733673,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8083421442747116,
                "rejected_mean_error": 1.8782576681772867,
                "gap_rejected_minus_accepted": 1.069915523902575
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.871448016166687,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4108302337924639,
                "rejected_mean_error": 3.4586111760139464,
                "gap_rejected_minus_accepted": 2.0477809422214825
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0382333397865295,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2432629491885503,
                "rejected_mean_error": 2.7326444644927976,
                "gap_rejected_minus_accepted": 1.4893815153042473
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4813365936279297,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0045410016179084,
                "rejected_mean_error": 2.226675654411316,
                "gap_rejected_minus_accepted": 1.2221346527934076
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.081200748682022,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7995164660215378,
                "rejected_mean_error": 1.8876389486789704,
                "gap_rejected_minus_accepted": 1.0881224826574325
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9798580223863723,
            "spearman": 0.9787075353027952,
            "auroc_top30_bad": 0.9821234285714286,
            "mae": 0.10343070031947263,
            "mse": 0.023696529486986608,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6691738019371344,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08633015084266663
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23453484904766084
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6803041328787803
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.037886202009519
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
            "pearson": 0.9692896190380039,
            "spearman": 0.9704272563374442,
            "auroc_top30_worst": 0.9749394285714286,
            "pairwise_seed_ranking": 0.8688,
            "predicted_best_mean_error": 1.4709899129867554,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.057803910732269204,
            "gap_to_oracle": 0.008146890878677482,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8757073388099671
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9765791977063204
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1702512851715088
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3632041980971152
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0629832744598393,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4607746716605292,
                "rejected_mean_error": 2.2180115718841553,
                "gap_rejected_minus_accepted": 0.7572369002236261
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8633719682693481,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3625723867813322,
                "rejected_mean_error": 2.0571649383051325,
                "gap_rejected_minus_accepted": 0.6945925515238003
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.484406054019928,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1702512851715088,
                "rejected_mean_error": 1.902745438194275,
                "gap_rejected_minus_accepted": 0.7324941530227662
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1428968012332916,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9770965404784717,
                "rejected_mean_error": 1.7233636445398646,
                "gap_rejected_minus_accepted": 0.7462671040613928
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1038554191589354,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4555650483237372,
                "rejected_mean_error": 2.1878528022766113,
                "gap_rejected_minus_accepted": 0.732287753952874
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8598284125328064,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3543232252253568,
                "rejected_mean_error": 2.046666870041499,
                "gap_rejected_minus_accepted": 0.6923436448161422
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.474894106388092,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1610021991729735,
                "rejected_mean_error": 1.8965854482650757,
                "gap_rejected_minus_accepted": 0.7355832490921022
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1672492623329163,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9558139301481701,
                "rejected_mean_error": 1.721829830643965,
                "gap_rejected_minus_accepted": 0.7660159004957949
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9684371608000356,
            "spearman": 0.9758861205511946,
            "auroc_top30_bad": 0.9927283809523809,
            "mae": 0.16594320527737144,
            "mse": 0.06838231160561908,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6889069858039352,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10582249593734741
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2071314268350601
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6998841503977775
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0555452300945918
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
            "pearson": 0.9423296704460893,
            "spearman": 0.960953798242431,
            "auroc_top30_worst": 0.9928594285714285,
            "pairwise_seed_ranking": 0.9112,
            "predicted_best_mean_error": 1.72602408015728,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08112450122833259,
            "gap_to_oracle": 0.00213727998733515,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9455920510292053
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1205497903701587
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2894320224761964
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.475633161154383
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2092643260955813,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6514585603078207,
                "rejected_mean_error": 3.1614688320159914,
                "gap_rejected_minus_accepted": 1.5100102717081707
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9677390456199646,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4751057769852742,
                "rejected_mean_error": 2.7824293013197927,
                "gap_rejected_minus_accepted": 1.3073235243345185
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.598414957523346,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2894320224761964,
                "rejected_mean_error": 2.315487152481079,
                "gap_rejected_minus_accepted": 1.0260551300048826
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.340323805809021,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1210916049945088,
                "rejected_mean_error": 2.0300670352027916,
                "gap_rejected_minus_accepted": 0.9089754302082829
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.222753167152405,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6520909731917912,
                "rejected_mean_error": 3.202667055130005,
                "gap_rejected_minus_accepted": 1.5505760819382137
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9887507855892181,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4747022637390197,
                "rejected_mean_error": 2.7939336829715304,
                "gap_rejected_minus_accepted": 1.3192314192325107
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5935041904449463,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2849766690731048,
                "rejected_mean_error": 2.32932049369812,
                "gap_rejected_minus_accepted": 1.0443438246250154
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3640099167823792,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1259666298116957,
                "rejected_mean_error": 2.036637688065595,
                "gap_rejected_minus_accepted": 0.9106710582538993
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9886735502721062,
            "spearman": 0.9875903848308653,
            "auroc_top30_bad": 0.9947405714285714,
            "mae": 0.09083148834713757,
            "mse": 0.016995523002194278,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7211684310141199,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06505098062753677
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20547047016620637
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5911277003765106
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9334138923009236
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
            "pearson": 0.9874688694014211,
            "spearman": 0.980952747588502,
            "auroc_top30_worst": 0.994471619047619,
            "pairwise_seed_ranking": 0.8986,
            "predicted_best_mean_error": 1.556008264541626,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06331401371955869,
            "gap_to_oracle": 0.004865004301071174,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5687942097187042
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8792096354449407
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1187333145618439
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.311279975942203
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6689645528793338,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4740936154524484,
                "rejected_mean_error": 2.9632608070373534,
                "gap_rejected_minus_accepted": 1.489167191584905
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9652146697044373,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.310395135855344,
                "rejected_mean_error": 2.5588583896716184,
                "gap_rejected_minus_accepted": 1.2484632538162743
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4677813053131104,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1187333145618439,
                "rejected_mean_error": 2.127287354660034,
                "gap_rejected_minus_accepted": 1.0085540400981903
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1839520037174225,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8802406689800775,
                "rejected_mean_error": 1.8711286967693805,
                "gap_rejected_minus_accepted": 0.9908880277893031
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6511335611343383,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.468049295478397,
                "rejected_mean_error": 2.9807791233062746,
                "gap_rejected_minus_accepted": 1.5127298278278776
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.021542966365814,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2978753090542268,
                "rejected_mean_error": 2.5734585201929487,
                "gap_rejected_minus_accepted": 1.275583211138722
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.49612158536911,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1042146325111388,
                "rejected_mean_error": 2.1344299240112306,
                "gap_rejected_minus_accepted": 1.0302152915000917
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1953760087490082,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8602504134178162,
                "rejected_mean_error": 1.8750523717645655,
                "gap_rejected_minus_accepted": 1.0148019583467494
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
      "best_epoch": 73,
      "best_calib_loss": 0.00978445541113615,
      "train_time_sec": 28.98829197883606,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9995686345783128,
            "spearman": 0.9986522559728672,
            "auroc_top30_bad": 0.9997379523809524,
            "mae": 0.02322118246042528,
            "mse": 0.0009803912299336441,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7548713196977335,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.000771246537566185
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19771181406974792
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5740747690439224
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9267941413561503
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
            "pearson": 0.999462396604037,
            "spearman": 0.999192679135707,
            "auroc_top30_worst": 0.999756380952381,
            "pairwise_seed_ranking": 0.965,
            "predicted_best_mean_error": 1.5295823648273945,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08602596318721778,
            "gap_to_oracle": 0.0007231306433677087,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.665651480615139
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8073573663473129
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0101901267886162
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.241464035153389
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.782564043998719,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.405698768582609,
                "rejected_mean_error": 3.4564989547729494,
                "gap_rejected_minus_accepted": 2.05080018619034
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9986866414546967,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.241464035153389,
                "rejected_mean_error": 2.718723043346405,
                "gap_rejected_minus_accepted": 1.477259008193016
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.418415606021881,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0101901267886162,
                "rejected_mean_error": 2.21136744761467,
                "gap_rejected_minus_accepted": 1.2011773208260537
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.021041214466095,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8073573663473129,
                "rejected_mean_error": 1.8785859274864196,
                "gap_rejected_minus_accepted": 1.0712285611391068
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8060496330261233,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106121353639496,
                "rejected_mean_error": 3.460574061870575,
                "gap_rejected_minus_accepted": 2.049961926506626
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0219537019729614,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2433005539973576,
                "rejected_mean_error": 2.7325316500663757,
                "gap_rejected_minus_accepted": 1.489231096069018
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4359108209609985,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0039730091691017,
                "rejected_mean_error": 2.227243646860123,
                "gap_rejected_minus_accepted": 1.2232706376910212
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0217444896697998,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.79907676923275,
                "rejected_mean_error": 1.887785514275233,
                "gap_rejected_minus_accepted": 1.0887087450424828
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9810240915334292,
            "spearman": 0.9779815409399558,
            "auroc_top30_bad": 0.9846598095238095,
            "mae": 0.1013928020201552,
            "mse": 0.02209244374568646,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6912945670638826,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06240195673704147
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23044718663692473
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6835527471899986
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.037597828189532
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
            "pearson": 0.9598863362287096,
            "spearman": 0.9668157862501033,
            "auroc_top30_worst": 0.9808335238095238,
            "pairwise_seed_ranking": 0.8848,
            "predicted_best_mean_error": 1.467567363023758,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.061226460695266605,
            "gap_to_oracle": 0.004724340915680081,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8852447443008423
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9827767025965911
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.174432741355896
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3629618757315027
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0229754209518434,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4620665600034926,
                "rejected_mean_error": 2.2063845767974852,
                "gap_rejected_minus_accepted": 0.7443180167939927
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.875991016626358,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3624804695489694,
                "rejected_mean_error": 2.057440102671663,
                "gap_rejected_minus_accepted": 0.6949596331226935
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.503730297088623,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.174432741355896,
                "rejected_mean_error": 1.8985639820098876,
                "gap_rejected_minus_accepted": 0.7241312406539917
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1201944649219513,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.98414638743233,
                "rejected_mean_error": 1.7210086796555981,
                "gap_rejected_minus_accepted": 0.7368622922232682
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0554884672164917,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4586297432581583,
                "rejected_mean_error": 2.1602705478668214,
                "gap_rejected_minus_accepted": 0.7016408046086631
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.877954751253128,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3546148277221517,
                "rejected_mean_error": 2.045801319773235,
                "gap_rejected_minus_accepted": 0.6911864920510833
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5063663125038147,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1645937309265137,
                "rejected_mean_error": 1.8929939165115357,
                "gap_rejected_minus_accepted": 0.728400185585022
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1296999752521515,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9665274468679277,
                "rejected_mean_error": 1.7182204640485386,
                "gap_rejected_minus_accepted": 0.7516930171806109
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9417868036137598,
            "spearman": 0.947233203598662,
            "auroc_top30_bad": 0.9689584761904763,
            "mae": 0.20377563252466044,
            "mse": 0.1224046242858472,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6633485443624743,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08833798146247863
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2058722358942032
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6990195559382438
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0974695575634639
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
            "pearson": 0.862222392594018,
            "spearman": 0.919879810995079,
            "auroc_top30_worst": 0.9471847619047619,
            "pairwise_seed_ranking": 0.9216,
            "predicted_best_mean_error": 1.726196113705635,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08095246767997755,
            "gap_to_oracle": 0.002309313535690194,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.948137743473053
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.131574660157546
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2897469676971436
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5293777160553028
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9407693266868595,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6896132352617053,
                "rejected_mean_error": 2.8180767574310304,
                "gap_rejected_minus_accepted": 1.128463522169325
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7411214709281921,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.528989290733093,
                "rejected_mean_error": 2.6211230636785587,
                "gap_rejected_minus_accepted": 1.0921337729454657
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5108987092971802,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2897469676971436,
                "rejected_mean_error": 2.3151722072601317,
                "gap_rejected_minus_accepted": 1.0254252395629881
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2749402821063995,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1324444605519597,
                "rejected_mean_error": 2.026274672567272,
                "gap_rejected_minus_accepted": 0.8938302120153123
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9237117052078248,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.700865148305893,
                "rejected_mean_error": 2.763699479103088,
                "gap_rejected_minus_accepted": 1.0628343307971952
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7382679879665375,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5343160481057703,
                "rejected_mean_error": 2.616984830962287,
                "gap_rejected_minus_accepted": 1.0826687828565167
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5074147582054138,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2851136138439179,
                "rejected_mean_error": 2.329183548927307,
                "gap_rejected_minus_accepted": 1.0440699350833893
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.28121417760849,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1354275142389632,
                "rejected_mean_error": 2.0334503312799384,
                "gap_rejected_minus_accepted": 0.8980228170409752
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9906630217269204,
            "spearman": 0.9887638735999795,
            "auroc_top30_bad": 0.9963923809523809,
            "mae": 0.08576159557341516,
            "mse": 0.014287567651450967,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.70934029391342,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06369187384843826
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20231114349365234
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5895319175720215
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9331718332290649
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
            "pearson": 0.9899889966652631,
            "spearman": 0.9826241363354474,
            "auroc_top30_worst": 0.998208,
            "pairwise_seed_ranking": 0.9004,
            "predicted_best_mean_error": 1.5550851006507873,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06423717761039738,
            "gap_to_oracle": 0.003941840410232489,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5787940394878387
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8802131705750258
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.118167498064041
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3091002827577753
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5422756433486944,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4759065772427453,
                "rejected_mean_error": 2.9469441509246828,
                "gap_rejected_minus_accepted": 1.4710375736819374
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.982741355895996,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3083576586419516,
                "rejected_mean_error": 2.5649578022880677,
                "gap_rejected_minus_accepted": 1.256600143646116
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4199575781822205,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.118167498064041,
                "rejected_mean_error": 2.127853171157837,
                "gap_rejected_minus_accepted": 1.0096856730937958
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.203484207391739,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8812974608553865,
                "rejected_mean_error": 1.8707756809134874,
                "gap_rejected_minus_accepted": 0.9894782200581009
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.531618785858154,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4680864887767369,
                "rejected_mean_error": 2.980444383621216,
                "gap_rejected_minus_accepted": 1.5123578948444791
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.006528317928314,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2973129318997185,
                "rejected_mean_error": 2.5751277984134733,
                "gap_rejected_minus_accepted": 1.2778148665137548
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4211626648902893,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.105522690296173,
                "rejected_mean_error": 2.133121866226196,
                "gap_rejected_minus_accepted": 1.0275991759300231
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.220739483833313,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8585539100662111,
                "rejected_mean_error": 1.8756239210220582,
                "gap_rejected_minus_accepted": 1.0170700109558473
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
      "best_epoch": 78,
      "best_calib_loss": 0.010253392159938812,
      "train_time_sec": 38.49017786979675,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993551197779109,
            "spearman": 0.9982164509806951,
            "auroc_top30_bad": 0.9994311904761904,
            "mae": 0.02580584731543753,
            "mse": 0.0012246366467615255,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7509655101804066,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0014819620400667191
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19788526377677917
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.574156036901474
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9269173621654511
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
            "pearson": 0.9993951143689671,
            "spearman": 0.9990075302882774,
            "auroc_top30_worst": 0.9997662857142857,
            "pairwise_seed_ranking": 0.9571,
            "predicted_best_mean_error": 1.5304311681687832,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08517715984582908,
            "gap_to_oracle": 0.0015719339847564129,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.666193558871746
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8071956357717514
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0101808164000512
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2414625150601069
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.806353831291199,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056982675857015,
                "rejected_mean_error": 3.456503463745117,
                "gap_rejected_minus_accepted": 2.0508051961594154
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0031793117523193,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2414625150601069,
                "rejected_mean_error": 2.718727603626251,
                "gap_rejected_minus_accepted": 1.4772650885661442
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4265474677085876,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0101808164000512,
                "rejected_mean_error": 2.211376758003235,
                "gap_rejected_minus_accepted": 1.2011959416031837
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0307502746582031,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8071956357717514,
                "rejected_mean_error": 1.8786398376782736,
                "gap_rejected_minus_accepted": 1.0714442019065222
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8569738149642947,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.410647800134288,
                "rejected_mean_error": 3.4602530789375305,
                "gap_rejected_minus_accepted": 2.0496052788032424
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.021320939064026,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2431739561160406,
                "rejected_mean_error": 2.7329114437103272,
                "gap_rejected_minus_accepted": 1.4897374875942866
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4424781203269958,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0039055796265601,
                "rejected_mean_error": 2.227311076402664,
                "gap_rejected_minus_accepted": 1.2234054967761039
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0227940380573273,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.799005828499794,
                "rejected_mean_error": 1.8878091611862182,
                "gap_rejected_minus_accepted": 1.0888033326864242
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.980338216747606,
            "spearman": 0.9789143928371125,
            "auroc_top30_bad": 0.9818106666666667,
            "mae": 0.10785682360689938,
            "mse": 0.02282447867767916,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6821776932548405,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06444836527109146
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24260664761066436
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6829957406401634
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0353408364216488
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
            "pearson": 0.9627878329212007,
            "spearman": 0.9651134347710125,
            "auroc_top30_worst": 0.971623619047619,
            "pairwise_seed_ranking": 0.8752,
            "predicted_best_mean_error": 1.4691934731006622,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.05960035061836244,
            "gap_to_oracle": 0.0063504509925842445,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9022692122459411
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9803940031008843
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1727946578979491
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3649078884612778
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0837643146514893,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4562991536458334,
                "rejected_mean_error": 2.2582912340164185,
                "gap_rejected_minus_accepted": 0.8019920803705851
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8788982927799225,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3644291008549285,
                "rejected_mean_error": 2.051606660072034,
                "gap_rejected_minus_accepted": 0.6871775592171054
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5112284421920776,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1727946578979491,
                "rejected_mean_error": 1.9002020654678344,
                "gap_rejected_minus_accepted": 0.7274074075698853
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1415267288684845,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9807792422108756,
                "rejected_mean_error": 1.722133457088165,
                "gap_rejected_minus_accepted": 0.7413542148772894
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1019038200378417,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.451066051589118,
                "rejected_mean_error": 2.2283437728881834,
                "gap_rejected_minus_accepted": 0.7772777212990654
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.892567217350006,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3528092391988173,
                "rejected_mean_error": 2.051160765072656,
                "gap_rejected_minus_accepted": 0.6983515258738389
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5212501883506775,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1650213556289672,
                "rejected_mean_error": 1.892566291809082,
                "gap_rejected_minus_accepted": 0.7275449361801147
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1326202750205994,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9657094951659914,
                "rejected_mean_error": 1.718496030664699,
                "gap_rejected_minus_accepted": 0.7527865354987077
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9574793079459434,
            "spearman": 0.9676669780388604,
            "auroc_top30_bad": 0.986534857142857,
            "mae": 0.17711442866375965,
            "mse": 0.08411275985611068,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6843358770426275,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0818032033443451
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2055902492284775
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6978818145632744
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0731327266613642
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
            "pearson": 0.9059739635154592,
            "spearman": 0.9504133970005741,
            "auroc_top30_worst": 0.9809097142857143,
            "pairwise_seed_ranking": 0.9328,
            "predicted_best_mean_error": 1.7255368875265122,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08161169385910028,
            "gap_to_oracle": 0.0016500873565674645,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9500796203613281
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1217503043321462
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2884738052368163
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.49586511624139
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0942437171936037,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6635984355078803,
                "rejected_mean_error": 3.0522099552154542,
                "gap_rejected_minus_accepted": 1.388611519707574
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9025118052959442,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4954346494715394,
                "rejected_mean_error": 2.721572580809791,
                "gap_rejected_minus_accepted": 1.2261379313382517
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5880241990089417,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2884738052368163,
                "rejected_mean_error": 2.316445369720459,
                "gap_rejected_minus_accepted": 1.0279715644836427
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3159105479717255,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1229370234492488,
                "rejected_mean_error": 2.0294505827200453,
                "gap_rejected_minus_accepted": 0.9065135592707965
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.099875831604004,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6685937594042883,
                "rejected_mean_error": 3.0541419792175293,
                "gap_rejected_minus_accepted": 1.385548219813241
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9057296812534332,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4925080861318558,
                "rejected_mean_error": 2.74108147999597,
                "gap_rejected_minus_accepted": 1.2485733938641141
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5758902430534363,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2857714745998383,
                "rejected_mean_error": 2.3285256881713865,
                "gap_rejected_minus_accepted": 1.0427542135715482
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.318602979183197,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1187850724137018,
                "rejected_mean_error": 2.0390571432317643,
                "gap_rejected_minus_accepted": 0.9202720708180625
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9894412723001483,
            "spearman": 0.9866722818759615,
            "auroc_top30_bad": 0.9966689523809524,
            "mae": 0.08732497166398291,
            "mse": 0.01606431421359389,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.720804015075031,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08356718736886978
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20137693519592284
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5914780010223388
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9330295758565267
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
            "pearson": 0.9891691638150206,
            "spearman": 0.9793186683639479,
            "auroc_top30_worst": 0.9975070476190475,
            "pairwise_seed_ranking": 0.902,
            "predicted_best_mean_error": 1.5565832848548888,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06273899340629585,
            "gap_to_oracle": 0.005440024614334016,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5735238773822784
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8822364777517624
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.119698953294754
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3108467874305842
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.545097017288208,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.475772482580609,
                "rejected_mean_error": 2.948151002883911,
                "gap_rejected_minus_accepted": 1.4723785203033022
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9975406229496002,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3102030815475143,
                "rejected_mean_error": 2.5594333254110317,
                "gap_rejected_minus_accepted": 1.2492302438635174
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4716719388961792,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.119698953294754,
                "rejected_mean_error": 2.126321715927124,
                "gap_rejected_minus_accepted": 1.00662276263237
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2315489947795868,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8836447256632125,
                "rejected_mean_error": 1.8699915892540964,
                "gap_rejected_minus_accepted": 0.9863468635908839
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.538710379600525,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4688920924398634,
                "rejected_mean_error": 2.973193950653076,
                "gap_rejected_minus_accepted": 1.5043018582132126
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.023986339569092,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2980622406949334,
                "rejected_mean_error": 2.572903659608629,
                "gap_rejected_minus_accepted": 1.2748414189136958
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4923189282417297,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1091023983955384,
                "rejected_mean_error": 2.129542158126831,
                "gap_rejected_minus_accepted": 1.0204397597312926
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.240119308233261,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8629184062518771,
                "rejected_mean_error": 1.8741535292589728,
                "gap_rejected_minus_accepted": 1.0112351230070957
              }
            ]
          }
        }
      }
    }
  ]
}
```
