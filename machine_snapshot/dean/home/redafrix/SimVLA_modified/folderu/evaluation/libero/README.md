# Evaluation on LIBERO

## 1. Environment Setup

Set up LIBERO following the [official instructions](https://github.com/Lifelong-Robot-Learning/LIBERO).

```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

## 2. Start Server

```bash
conda activate simvla
CUDA_VISIBLE_DEVICES=1 python serve_smolvlm_libero.py \
    --checkpoint YuankaiLuo/SimVLA-LIBERO \
    --norm_stats ../../norm_stats/libero_norm.json \
    --port 8102
```

or 

```
conda activate simvla
CUDA_VISIBLE_DEVICES=1 python serve_smolvlm_libero.py \
    --checkpoint ../../runs/simvla_libero_large/ckpt-150000 \
    --norm_stats ../../norm_stats/libero_norm.json \
    --port 8102
```

## 3. Run Evaluation

Quick evaluation on selected tasks:

Full evaluation on all task suites:

```bash
conda activate libero
bash run_eval_all.sh 8102 10 "eval_simvla_150k" "0 1 2 3"
bash run_eval_all.sh 8102 50 "eval_simvla_150k" "0 1 2 3"
```

## 4. Zero-Shot LIBERO-PRO

LIBERO-PRO is a separate benchmark repo built on top of LIBERO.

Official sources:

- https://github.com/Zxy-MLlab/LIBERO-PRO
- https://huggingface.co/papers/2510.03827

This repo now includes a thin bridge for zero-shot evaluation against a local LIBERO-PRO checkout.

### Start the SimVLA server

```bash
cd evaluation/libero
conda activate simvla
CUDA_VISIBLE_DEVICES=0 python serve_smolvlm_libero.py \
    --checkpoint ../../runs/simvla_libero_uncertainty/ckpt-60000 \
    --norm_stats ../../norm_stats/libero_norm.json \
    --port 8102
```

### Run a LIBERO-PRO suite

Assumes a local checkout at `/home/redafrix/LIBERO-PRO`. Override `LIBERO_PRO_ROOT` if needed.

```bash
cd evaluation/libero
conda activate libero
LIBERO_PRO_ROOT=/home/redafrix/LIBERO-PRO \
TASK_SUITE=libero_10_temp \
NUM_TRIALS=10 \
./run_libero_pro_eval.sh
```

### Run one task only with uncertainty logging

```bash
cd evaluation/libero
conda activate libero
LIBERO_PRO_ROOT=/home/redafrix/LIBERO-PRO \
TASK_SUITE=libero_10_temp \
TASK_ID=8 \
NUM_TRIALS=50 \
UNCERTAINTY_LOG=./eval_libero_pro/libero_10_temp_task8.jsonl \
./run_libero_pro_eval.sh
```

Notes:

- `TASK_SUITE` can be a standard LIBERO suite or a LIBERO-PRO suite such as `libero_10_temp`, `libero_10_lan`, or similar names registered by the LIBERO-PRO checkout.
- The wrapper only handles client-side integration. You still need the LIBERO-PRO repo and its required `bddl_files` and `init_files` prepared according to the official README.
