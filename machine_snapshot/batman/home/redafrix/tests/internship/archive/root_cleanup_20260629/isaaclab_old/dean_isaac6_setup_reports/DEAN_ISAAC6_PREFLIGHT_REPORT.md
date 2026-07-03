# DEAN_ISAAC6_PREFLIGHT_REPORT

Preflight compatibility audit for remote computer **Dean** (static hostname **Batman**).

## Machine Details
* **Hostname**: Batman
* **User**: dean
* **SSH Route**: dean
* **Audit Date**: 2026-06-17
* **Current Activity/Busy Status**: IDLE (no active simulations, training runs, or dockers)

## Operating System Compatibility
* **Ubuntu Version**: Ubuntu 22.04.5 LTS (Jammy Jellyfish)
* **Kernel**: Linux 6.8.0-111-generic (x86_64)
* **Architecture**: x86_64
* **GLIBC**: 2.35
* **OS Verdict**: **PASS** (Ubuntu 22.04 and GLIBC 2.35 are fully supported by Isaac Sim 6.0.0)
* **Virtualization**: None (bare-metal)
* **Secure Boot**: SecureBoot disabled

## CPU and Memory
* **CPU Model**: 11th Gen Intel(R) Core(TM) i9-11900 @ 2.50GHz
* **Physical Cores**: 8
* **Threads**: 16
* **AVX2 Support**: YES
* **RAM**: 31Gi (32 GB total)
* **Swap**: 2.0Gi (swapon size: 2.0G, used: 162M)
* **CPU/RAM Verdict**: **PASS_MINIMUM** (Meets the physical core requirement and AVX2 requirements, but RAM is at the minimum threshold of 32 GB)

## GPU & Driver Compatibility
* **GPU Model**: NVIDIA RTX A5000 (GA102GL)
* **VRAM**: 24564 MiB (~24 GB)
* **Driver Version**: 580.95.05
* **Driver Requirement Comparison**: **PASS_RECOMMENDED** (RTX A5000, VRAM >= 16 GB, driver version 580.95.05 is newer than the 580.95.05 requirement for Isaac Sim 6.0)
* **Compute Capability**: 8.6
* **Current GPU Workloads**: None (only Xorg using 4 MiB)
* **GPU Verdict**: **PASS_RECOMMENDED**

## Graphics Runtime
* **Vulkan Status**: READY (ICD configs for intel, radeon, lvp, and nvidia present; nvidia_icd.json verified; Vulkan libraries mapped in ldconfig)
* **NVIDIA Libraries**: `libGLX_nvidia.so.0`, `libcuda.so.1` present in ldconfig
* **Display/Headless Status**: HEADLESS (DISPLAY/WAYLAND_DISPLAY are unset)

## Storage
* **Installation Filesystem**: `/dev/sda2` (`ext4`, mounted on `/`)
* **Disk Type**: SSD (SATA controller interface)
* **Free Space Before**: 38 GB
* **Free Space After**: 38 GB (Purged pip and shader cache files, but reclaimed space was negligible under 1MB as APT cleanup failed due to passwordless sudo limits and Conda/UV caches were missing)
* **Space Reclaimed**: ~0 GB
* **Storage Verdict**: **BLOCKED** (Free space is only 38 GB, which is below the minimum required 80 GB and recommended 120 GB for isolated installation)
* **Inode Availability**: 27M free inodes (11% used)
* **Home Quota**: None set
* **/tmp Free Space**: 38 GB (Shares the root filesystem `/dev/sda2`)
* **/dev/shm Size**: 16 GB total (27M used)

## Existing Software
* **Python Versions**: Python 3.10.12 (system Python). Python 3.12 is **MISSING**.
* **Environment Managers**: None (conda, uv, micromamba, and mamba are **MISSING**).
* **Existing Isaac Installations**: None found in `/home/dean`, `/opt`, or `/usr/local`.
* **CUDA Toolkit**: CUDA 13.0 (present in `/usr/local/cuda-13.0` and symlinked to `/usr/local/cuda`).
* **Development Tools**:
  * `git`: git version 2.34.1
  * `git-lfs`: git-lfs/3.0.2
  * `curl`: curl 7.81.0
  * `wget`: GNU Wget 1.21.2
  * `unzip`: Available
  * `tar`: tar (GNU tar) 1.34
  * `rsync`: rsync version 3.2.7
  * `gcc`: 11
  * `g++`: 11
  * `make`: GNU Make 4.3
  * `cmake`: cmake version 3.22.1
  * `ninja`: **MISSING**
  * `pkg-config`: Available
  * `vulkaninfo`: **MISSING**
  * `glxinfo`: **MISSING**

## Connectivity
* **GitHub**: SUCCESS (200 OK)
* **NVIDIA PyPI**: SUCCESS (200 OK)
* **NVIDIA Documentation**: SUCCESS (200 OK)
* **Project Master SHA**: `b1e3ff35d2cea67a15bca15cf0ac598b6eefa233`
* **Isaac Lab release/3.0.0-beta2 SHA**: `28a37cecdd433c22d9eabd6a5954add9f13a8951`

## Safety Confirmation
* **driver_modified**: NO
* **CUDA_modified**: NO
* **kernel_modified**: NO
* **existing_envs_modified**: NO
* **existing_projects_modified**: NO
* **experiments_stopped**: NO
* **reboot_performed**: NO

## Final Verdict
**NOT_READY**

### Blockers:
1. **Inadequate Disk Space**: Root filesystem (`/dev/sda2`) has only 38 GB of free space. A minimum of 80 GB is required, and 120 GB is recommended to support downloading, extracting, and running Isaac Sim 6.0.0 along with Isaac Lab.
2. **Missing Python 3.12**: Isaac Lab `release/3.0.0-beta2` requires Python 3.12, but it is not installed on the system.
3. **Missing Environment Manager**: Neither Conda nor `uv` is installed, preventing clean environment isolation.

## Safe Cleanup Candidates (REQUIRES_USER_APPROVAL)
The following candidate paths can be cleaned to reclaim up to 13.97 GB of space:
1. `/home/dean/tmp_transfer/chunks` - **2.30 GB** - Contains temporary chunks `chunk_aa` through `chunk_ae` from a manual file transfer in May. Safe to delete.
2. `/home/dean/deploy_packages/simvla_modified_risk_topk8_h10_20260608.zip` - **2.65 GB** - Zip archive of a backup/deployment package. Can be removed if the unzipped directory is sufficient or backed up elsewhere.
3. `/home/dean/deploy_packages/simvla_modified_risk_topk8_h10_20260608/checkpoints/simvla_modified_ckpt_60000/model.safetensors` - **3.02 GB** - Duplicate model checkpoint weights inside deploy packages.
4. `/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000/model.safetensors` - **3.02 GB** - SimVLA model checkpoint. Recommend confirmation before deleting.
5. `/home/dean/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO/model.safetensors` - **3.02 GB** - Original model checkpoint weights. Recommend verification.

*Note: Freeing up space from `/home/redafrix` (which currently uses 242 GB on the same root partition) would also resolve the storage blocker.*

## Planned Next Action
1. Ask user for approval to clean up the safe candidate files (or clean `/home/redafrix`).
2. Install `uv` via curl standalone installer or `miniconda` locally in `/home/dean/.local` to manage environments.
3. Set up an isolated Python 3.12 virtual environment using the installed manager.
4. Clone the project master and Isaac Lab `release/3.0.0-beta2` inside `/home/dean/isaac6_master_workspace/`.
5. Install Isaac Sim 6.0.0 wheel inside the virtual environment and compile Isaac Lab.
