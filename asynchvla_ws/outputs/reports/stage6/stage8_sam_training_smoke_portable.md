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
      "best_epoch": 10,
      "best_calib_loss": 0.08401035517454147,
      "train_time_sec": 7.889516830444336,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8571597413600974,
            "spearman": 0.7698787487953159,
            "auroc_top30_bad": 0.8310796666666667,
            "mae": 0.2893482741095126,
            "mse": 0.3028060664377107,
            "expert_lt_perturb_large": 0.982,
            "expert_lt_other_task": 0.504,
            "expert_lt_simvla_seed0": 0.973,
            "same_context_pred_std": 0.7988355049102727,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5462527184486389
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5491057269066573
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7502460416331888
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0158796352773904
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
            "pearson": 0.9921190539712736,
            "spearman": 0.9868787993702072,
            "auroc_top30_worst": 0.9935481904761905,
            "pairwise_seed_ranking": 0.7579,
            "predicted_best_mean_error": 1.6444395095407962,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.062010840564966196,
            "gap_to_oracle": 0.02129298862814899,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.56523338586092
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7380418196678161
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0181357365846635
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.252732683356603
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.296836400032044,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4537241577704747,
                "rejected_mean_error": 3.9099050278663636,
                "gap_rejected_minus_accepted": 2.456180870095889
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.010197341442108,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.252732683356603,
                "rejected_mean_error": 3.0391709290504454,
                "gap_rejected_minus_accepted": 1.7864382456938424
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5391284823417664,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0181357365846635,
                "rejected_mean_error": 2.380548752975464,
                "gap_rejected_minus_accepted": 1.3624130163908004
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0496065318584442,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7380418196678161,
                "rejected_mean_error": 2.0197757198174795,
                "gap_rejected_minus_accepted": 1.2817339001496633
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.283091259002686,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.456136974030071,
                "rejected_mean_error": 3.9592707347869873,
                "gap_rejected_minus_accepted": 2.503133760756916
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0520323514938354,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2513310752709708,
                "rejected_mean_error": 3.0718081746101378,
                "gap_rejected_minus_accepted": 1.820477099339167
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.542681872844696,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0140731762647628,
                "rejected_mean_error": 2.3988275239467622,
                "gap_rejected_minus_accepted": 1.3847543476819995
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0487392842769623,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7297787175178528,
                "rejected_mean_error": 2.032007560968399,
                "gap_rejected_minus_accepted": 1.3022288434505462
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6988990041627217,
            "spearman": 0.6811473135901737,
            "auroc_top30_bad": 0.8017725714285715,
            "mae": 0.4349919084846973,
            "mse": 0.45804865462038624,
            "expert_lt_perturb_large": 0.968,
            "expert_lt_other_task": 0.488,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.71497884197557,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7213238927721978
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5994368885755539
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.841639460682869
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.100901253382365
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
            "pearson": 0.8318831320308153,
            "spearman": 0.8375434183317878,
            "auroc_top30_worst": 0.9427657142857143,
            "pairwise_seed_ranking": 0.694,
            "predicted_best_mean_error": 1.6772335144281387,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.050762105345726116,
            "gap_to_oracle": 0.028161259889602608,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7617534425258636
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.003278855043344
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2368286891460418
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4805273935675367
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.382857584953309,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6082661490175458,
                "rejected_mean_error": 2.802245040893555,
                "gap_rejected_minus_accepted": 1.193978891876009
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0025405883789062,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4788059411906382,
                "rejected_mean_error": 2.4726481816639154,
                "gap_rejected_minus_accepted": 0.9938422404732772
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6856328845024109,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2368286891460418,
                "rejected_mean_error": 2.2184993872642518,
                "gap_rejected_minus_accepted": 0.98167069811821
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2649605870246887,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0056154066190932,
                "rejected_mean_error": 1.9688606461949385,
                "gap_rejected_minus_accepted": 0.9632452395758453
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.403554582595825,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6089453856150309,
                "rejected_mean_error": 2.7994477272033693,
                "gap_rejected_minus_accepted": 1.1905023415883385
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0375689268112183,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4784141339082768,
                "rejected_mean_error": 2.4688168555971175,
                "gap_rejected_minus_accepted": 0.9904027216888407
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.695874810218811,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2293028054237365,
                "rejected_mean_error": 2.226688434123993,
                "gap_rejected_minus_accepted": 0.9973856287002565
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.296197921037674,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9897570761423262,
                "rejected_mean_error": 1.9767070007834204,
                "gap_rejected_minus_accepted": 0.9869499246410942
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6101689054509969,
            "spearman": 0.5259201007847942,
            "auroc_top30_bad": 0.7131127619047618,
            "mae": 0.5334053195893764,
            "mse": 0.5749854107527909,
            "expert_lt_perturb_large": 0.976,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.952,
            "same_context_pred_std": 0.7215243752132258,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8327663811445236
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7089614599943161
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8743547301292419
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.014812728468577
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
            "pearson": 0.713486918562976,
            "spearman": 0.5801046102379913,
            "auroc_top30_worst": 0.8533455238095238,
            "pairwise_seed_ranking": 0.6574,
            "predicted_best_mean_error": 1.4378702297210693,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.04418897902965546,
            "gap_to_oracle": 0.03641371345520006,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8276298274993896
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.039964611713703
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0986097345352173
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1964671315033553
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6471772909164444,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2854642821682825,
                "rejected_mean_error": 3.1398124160766603,
                "gap_rejected_minus_accepted": 1.8543481339083778
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0441941022872925,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.196276649657792,
                "rejected_mean_error": 2.293011657250956,
                "gap_rejected_minus_accepted": 1.096735007593164
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6834166646003723,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0986097345352173,
                "rejected_mean_error": 1.843188456583023,
                "gap_rejected_minus_accepted": 0.7445787220478057
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.997553750872612,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0401137499763562,
                "rejected_mean_error": 1.614800710465636,
                "gap_rejected_minus_accepted": 0.5746869604892797
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6271718740463257,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2937463647789424,
                "rejected_mean_error": 3.176874804496765,
                "gap_rejected_minus_accepted": 1.8831284397178225
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0541833639144897,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1953007717502309,
                "rejected_mean_error": 2.3332310773077465,
                "gap_rejected_minus_accepted": 1.1379303055575156
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6838791966438293,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0902666516304016,
                "rejected_mean_error": 1.873851765871048,
                "gap_rejected_minus_accepted": 0.7835851142406465
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0072027742862701,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0497531597576444,
                "rejected_mean_error": 1.6277024231173776,
                "gap_rejected_minus_accepted": 0.5779492633597332
              }
            ]
          }
        }
      }
    }
  ]
}
```
