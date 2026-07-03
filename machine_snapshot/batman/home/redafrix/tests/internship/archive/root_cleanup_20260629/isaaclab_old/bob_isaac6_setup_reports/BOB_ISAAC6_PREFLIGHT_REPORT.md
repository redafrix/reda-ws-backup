# BOB_ISAAC6_PREFLIGHT_REPORT

Preflight compatibility audit for remote computer **Bob** (static hostname **PCROBOTUBUNTU02**).

## Machine Details
* **Hostname**: PCROBOTUBUNTU02
* **User**: rootalkhatib
* **SSH Route**: pcrobot
* **Audit Date**: 2026-06-17
* **Current Activity/Busy Status**: BUSY (Active python OpenVLA data collection script `collect_openvla_oft_goal_object_pro_risk_data_round_robin_bob.py` utilizing 109% CPU and 9GB VRAM, active python experiment `marathon_c_50.py --idea 22`, active tmux sessions `ood_production_aggressive_fixed_100ep_20260609`, `openvla_goal_object_pro_risk_data_10000ep_20260616`, etc.)

## Operating System Compatibility
* **Ubuntu Version**: Ubuntu 22.04.5 LTS (Jammy Jellyfish)
* **Kernel**: Linux 6.8.0-111-generic (x86_64)
* **Architecture**: x86_64
* **GLIBC**: 2.35
* **OS Verdict**: **PASS** (Ubuntu 22.04 and GLIBC 2.35 are fully supported by Isaac Sim 6.0.0)
* **Virtualization**: None (bare-metal)
* **Secure Boot**: SecureBoot disabled

## CPU and Memory
* **CPU Model**: Intel(R) Xeon(R) w3-2423 (6 physical cores, 12 threads)
* **Physical Cores**: 6
* **Threads**: 12
* **AVX2 Support**: YES (AVX, AVX2, and AVX-512 are present in flags)
* **RAM**: 30Gi (32 GB total)
* **Swap**: 2.0Gi (swapon size: 2.0G, used: 2.0G - SWAP IS FULLY UTILIZED)
* **CPU/RAM Verdict**: **PASS_MINIMUM** (Meets the physical core requirement and AVX2 requirements, but RAM is at the minimum threshold of 32 GB, and swap is heavily saturated)

## GPU & Driver Compatibility
* **GPU Model**: NVIDIA GeForce RTX 4070 Ti SUPER
* **VRAM**: 16376 MiB (~16 GB)
* **Driver Version**: 570.211.01
* **Driver Requirement Comparison**: **BLOCKED** (RTX 4070 Ti SUPER has enough VRAM, but driver version 570.211.01 is older than the required 580.95.05 for Isaac Sim 6.0)
* **Compute Capability**: 8.9
* **Current GPU Workloads**: YES (Active compute process PID 4059685 using 9056 MiB VRAM; other PID 848267 using 3158 MiB VRAM)
* **GPU Verdict**: **BLOCKED** (Driver needs upgrading to >= 580.95.05, and active compute tasks occupy most of the VRAM)

## Graphics Runtime
* **Vulkan Status**: READY (ICD configs for intel, radeon, lvp, and nvidia present; Vulkan libraries mapped in ldconfig)
* **NVIDIA Libraries**: `libGLX_nvidia.so.0`, `libcuda.so.1` present in ldconfig
* **Display/Headless Status**: HEADLESS (DISPLAY/WAYLAND_DISPLAY are unset)

## Storage
* **Installation Filesystem**: `/dev/nvme0n1p2` (`ext4`, mounted on `/`)
* **Disk Type**: NVMe KIOXIA 512GB SSD
* **Free Space Before**: 350 GB
* **Free Space After**: 350 GB (Conservative cache cleanup was deferred due to active workload dependencies to avoid corrupting running tasks)
* **Space Reclaimed**: 0 GB (deferred)
* **Storage Verdict**: **PASS_RECOMMENDED** (Free space is 350 GB, which easily exceeds the 120 GB recommended size)
* **Inode Availability**: 30M free inodes (3% used)
* **Home Quota**: None set
* **/tmp Free Space**: 350 GB (Shares the root filesystem `/dev/nvme0n1p2`)
* **/dev/shm Size**: 16 GB total (76K used)

## Existing Software
* **Python Versions**: Python 3.10.12 (system Python). Python 3.12 is **MISSING**.
* **Environment Managers**: None (conda, uv, micromamba, and mamba are **MISSING**).
* **Existing Isaac Installations**: None found in `/home/rootalkhatib`, `/opt`, or `/usr/local`.
* **CUDA Toolkit**: **MISSING** (nvcc compiler not found; no `/usr/local/cuda` directories present).
* **Development Tools**:
  * `git`: git version 2.34.1
  * `git-lfs`: **MISSING**
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
1. **Active Workloads**: The system is actively running Python OpenVLA data collection and experiment scripts utilizing 100%+ CPU and 9GB of VRAM. Purges/workload changes must not be performed while busy.
2. **Outdated NVIDIA Driver**: Driver version `570.211.01` is older than the required `580.95.05` for Isaac Sim 6.0.
3. **Missing CUDA Toolkit**: No CUDA toolkit/compiler is installed.
4. **Missing Python 3.12**: Python 3.12 is not installed.
5. **Missing Environment Manager**: Neither Conda nor `uv` is installed.
6. **Missing Development Tools**: `git-lfs`, `ninja` are missing.

## Safe Cleanup Candidates (REQUIRES_USER_APPROVAL)
Since free space is 350 GB, cleanup is not strictly necessary for storage reasons. However, the following is identified as a candidate for future cleanup:
1. `/home/rootalkhatib/.cache/pip` - **13.00 GB** - Large pip package download cache. Can be cleaned once the active workloads are idle.

*Note: Protect `/media/rootalkhatib/My Passport` (external drive) which is used as data collection targets.*

## Planned Next Action
1. Wait for active workloads to finish.
2. Upgrade the NVIDIA driver to version `580.95.05` or newer.
3. Install the matching CUDA 12.8 / 13.0 Toolkit.
4. Install `uv` or `miniconda` locally under `/home/rootalkhatib/.local` to manage virtual environments.
5. Create an isolated Python 3.12 environment, clone the repositories under `/home/rootalkhatib/isaac6_master_workspace/`, and proceed with installation.
