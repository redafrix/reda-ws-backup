# DynamicVLA Fresh Setup Report

Fresh isolated setup for official DynamicVLA data collection in Isaac Sim.

## Start
Thu Jun 11 11:03:01 AM CEST 2026
ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test
/home/redafrix/tests/internship/isaac_dynamicVLA-test

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  253G   34G  89% /

## Isaac Sim detection
CHECK /home/redafrix/isaacsim
drwxrwxr-x 21 redafrix redafrix 4096 Oct 31  2025 /home/redafrix/isaacsim
CHECK /home/redafrix/.local/share/ov/pkg/isaac-sim-*
CHECK /home/redafrix/Downloads/isaacsim

## Isaac Sim symlink
lrwxrwxrwx 1 redafrix redafrix 23 Jun 11 11:03 /home/redafrix/tests/internship/isaac_dynamicVLA-test/isaacsim -> /home/redafrix/isaacsim
/home/redafrix/tests/internship/isaac_dynamicVLA-test/isaacsim/kit/python/bin/python3
3.10.15 (tags/v3.10.15-dirty:ffee63f, Oct  8 2024, 18:53:10) [GCC 7.3.1 20180303 (Red Hat 7.3.1-5)]

## Isaac Lab status
0f00ca2b4b2d54d5f90006a92abb1b00a72b2f20
v2.2.1
lrwxrwxrwx 1 redafrix redafrix 62 Jun 11 11:06 _isaac_sim -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/isaacsim

tabs: terminal type 'dumb' cannot reset tabs
tabs: terminal type 'dumb' cannot reset tabs
isaaclab python validation:
[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
isaaclab python ok 3.10.15 (tags/v3.10.15-dirty:ffee63f, Oct  8 2024, 18:53:10) [GCC 7.3.1 20180303 (Red Hat 7.3.1-5)]

[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
OK shapely
OK zmq
OK h5py
OK numpy
missing: []
[INFO] Using python from: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/python.sh
Requirement already satisfied: shapely in /home/redafrix/.local/lib/python3.10/site-packages (2.1.2)
Requirement already satisfied: pyzmq in /home/redafrix/.local/lib/python3.10/site-packages (27.1.0)
Requirement already satisfied: h5py in /home/redafrix/isaacsim/kit/python/lib/python3.10/site-packages (3.15.1)
Requirement already satisfied: numpy>=1.21 in /home/redafrix/isaacsim/extscache/omni.kit.pip_archive-0.0.0+d02c707b.lx64.cp310/pip_prebundle (from shapely) (1.26.0)

[notice] A new release of pip is available: 24.0+nv1 -> 26.1.2
[notice] To update, run: /home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/_isaac_sim/kit/python/bin/python3 -m pip install --upgrade pip
## DynamicVLA status
origin	https://github.com/hzxie/DynamicVLA.git (fetch)
origin	https://github.com/hzxie/DynamicVLA.git (push)
a27a06d2ca74d0e987a5e552e01013073e93cfd8

## README asset section
32-               Hong, Fangzhou and 
33-               Diao, Haiwen and 
34-               Liu, Ziwei},
35-  journal   = {arXiv preprint arXiv:2601.22153},
36-  year      = {2026}
37-}
38-```
39-
40-## Dataset and Pretrained Models 🛢️
41-
42:### DOM Dataset
43-
44-- [DOM Training Set](https://huggingface.co/datasets/hzxie/DOM) – for training DynamicVLA
45:- [DOM Testing Set](https://gateway.infinitescript.com/?f=DOM-Test) – for benchmarking; includes test configurations and a subset of 3D scenes
46:- [DOM 3D Objects](https://gateway.infinitescript.com/?f=DOM-3D-Objects) – assets for data generation and benchmarking
47:- [DOM 3D Scenes](https://gateway.infinitescript.com/?f=DOM-3D-Scenes) – full scene assets for data generation
48-
49-### Pretrained Models
50-
51-- [DynamicVLA  (trained on DOM)](https://huggingface.co/hzxie/dynamic-vla-DOM)
52-
53-
54-## Installation 📥
55-
56-We recommend using **conda** to create two separate environments:
57-
58-- one for **model training & inference**
59-- one for **Isaac Lab simulation & evaluation**
60-
61-### PyTorch Environment
62-
63-- Install **Python 3.10** and **PyTorch 2.7.1** *(Other versions should work, but are not fully tested)*
64-- Install dependencies:
65-
66-```bash
67-pip install -r requirements.txt
68-```
69-
70-### Isaac Lab Environment
71-
72-- Install **Python 3.10** *(Other versions should work, but are not fully tested)*
73-- Install **Isaac Sim 4.5.0** and **Isaac Lab 2.2.1**
74-  Follow the official guide: https://isaac-sim.github.io/IsaacLab/v2.2.0/source/setup/installation/index.html
75-- Install additional dependencies:
76-
77-```bash
78-pip install shapely pyzmq h5py
79-```
80-
81-## Benchmarking Your Policy 🏅
82-
83:### Prepare scenes and objects
84-
85:Download [DOM Testing Set](#dom-dataset) (including a subset of DOM 3D scenes) and [DOM 3D Objects](#dom-dataset).
86-
87-```
88-PROJECT_ROOT/
89:├── objects/           # Put DOM 3D Objects here
90:├── scenes/            # Put DOM 3D Scenes here
91-|   └── textures       # Put the textures of 3D scenes here
92-|   └── *.usd          # Put the USD files of 3D scenes here
93:├── tests/             # Put DOM Testing Set here
94-|   └── *.json
95:|── test-envs.txt      # The list of test environments (included in DOM Testing Set)
96-├── datasets/          # Generated simulated datasets will be stored here
97-└── dynamic-vla/       # git clone https://github.com/hzxie/DynamicVLA dynamic-vla
98-    └── runs           # Create folder for evaluation and checkpoints output
99-```
100-
101-### Run Policy Evaluation Server
102-
103-> ⚠️ This step requires the **Isaac Lab environment**
104-
105-From the `PROJECT_ROOT/dynamic-vla` directory, run:
106-
107-```bash
108-python3 simulations/evaluate.py \
109-    --scene_dir ../scenes \
110-    --output_dir ../output/evaluation \
111:    --env_cfg ../test-envs.txt \
112-    --enable_cameras --headless -n 20 --save
113-```
114-
115-**Arguments:**
116-
117:- `test-envs.txt` are provided by [DOM Testing Set](#dom-dataset)
118-- `-n 20`: run 20 trials per environment
119-- `--save`: save evaluation videos to `output_dir`
120-- `--headless`: run without GUI
121-- `--enable_cameras`: enable visual observations
122-
123-### Run Policy Inference
124-
125-> ⚠️ This step requires the **PyTorch environment**
126-
127-From the `PROJECT_ROOT/dynamic-vla` directory, run:
128-
129-```bash
130-python3 scripts/inference.py \
131-    -p /path/to/vla-checkpoint \
132-    -r euler -d -s
133-```
134-
135-**Arguments:**
136-
137-- `-p`: path to the trained model checkpoint
138-- `-r euler`: use Euler angles for rotation representation
139-- `-d`: enable **delta actions** *(actions are relative to current state)*
140-- `-s`: enable **contiguous inference** *(if supported by the model)*
141-
142:## Simulated Dataset Generation 🧪
143-
144-> ⚠️ This step requires the **Isaac Lab environment**
145-
146-### IsaacSim Simulation
147-
148-From the `PROJECT_ROOT/dynamic-vla` directory, you can generate synthetic data using:
149-
150-```bash
151:python3 simulations/simulate.py \  
152-        --headless  --enable_cameras  --seed 42  --save  --task place
153-```
154-
155-Example configuration file: `simulations/configs/sim_cfg.yaml`
156-
157-**Arguments:**
158-
159--   `--task` : task type to simulate. Options: `pick`, `place`, `long-horizon`.
160--   `--robot`: robot type used in simulation _(default: `franka`, also supports `piper`)_.
161--   `--headless`: run simulation without GUI.
162--   `--enable_cameras`: include visual observations in the output dataset.
163--   `--debug`: enable debug mode and render trajectories as `.mp4` videos.
164--   `--seed`: random seed for simulation _(automatically increments for each run if specified)_.
165--   `-n`, `--n_simulations`: number of simulation episodes to generate *(default: `10,000`)*.
166--   `--save`: save generated simulation data in HDF5 format.
167-
168-### Trajectory Replay
169-
170-After data generation, convert the trajectories into a format compatible with VLA training:
171-
172-```bash
173-python3 scripts/translate_dataset_seq.py \
174-        --dataset_dir ../datasets --output_dir ../datasets-tr \
175-        --enable_cameras --headless --save
176-```
177-
178-**Arguments:**
179-
180--   `--dataset_dir`: directory containing the raw simulation datasets.
181--   `--output_dir`: directory to store the processed trajectories.
182--   `--enable_cameras`: include visual observations in the output dataset.
183--   `--headless`: run simulation without GUI.
184--   `--save`: save generated simulation data in HDF5 format.
185-
186-### Convert LeRobot Dataset
187-
188-We provide a script to convert the generated `.h5` files into the LeRobot dataset *(v2.1 format)*, using **Euler angles** as the rotation representation:
189-
190-```bash
191-python3 scripts/create_lerobot_dataset.py \  
192-        --dataset_dir ../datasets-tr --repo hzxie/DOM --rotation euler
193-```
194-
195-This will create lerobot dataset using all the hdf5 datasets in the default output directory.
196-
197-## Training 👩🏽‍💻
198-
199-> ⚠️ This step requires the **PyTorch environment**
200-
201-From the `PROJECT_ROOT/dynamic-vla` directory, run:
202-
203-```bash
204-torchrun --nnodes=1  --nproc_per_node=8  --standalone run.py \  
205-  -c configs/dynamicvla.yaml \  
206-  -p /path/to/pretrained/model
207-  -d hzxie/DOM
208-```
209-
210-**Arguments:**
211-
212--   `--nnodes`: number of compute nodes (machines) used for distributed training
213--   `--nproc_per_node`: number of GPUs per node
214--   `-c`: path to the training config file
215--   `-p`: path to the pretrained model checkpoint *(optional)*
216--   `-d`: name of the LeRobot dataset *(v2.1 format)*
217-
218-### Checkpoint Evaluation
219-
220-> ⚠️ This step requires the **PyTorch environment**
221-

## simulate.py relevant args
38:def get_object_metadata(object_dir, target_categories=[]):
41:    object_sizes = _get_object_sizes(args.object_dir, target_categories)
53:    metadata_file = os.path.join(object_dir, "metadata.json")
67:def _get_object_sizes(object_dir, target_categories=None):
69:    categories = sorted([f for f in os.listdir(object_dir)])
75:            f for f in os.listdir(os.path.join(object_dir, c)) if f.endswith(".usd")
78:            usd_path = os.path.join(object_dir, c, o)
100:def get_env_cfg(sim_cfg, task, robot, object_metadata, scene_dir):
108:        entry_point="isaaclab.envs:ManagerBasedRLEnv",
110:            "env_cfg_entry_point": "configs.env_cfg:EnvCfg",
112:        disable_env_checker=True,
114:    env_cfg = isaaclab_tasks.utils.parse_cfg.parse_env_cfg(
117:        num_envs=sim_cfg["num_envs"],
122:    scenes = [f for f in os.listdir(scene_dir) if f.endswith(".usd")]
126:        usd_file = os.path.join(scene_dir, scene)
128:        env_cfg.scene = configs.scene_cfg.set_house_asset(
129:            env_cfg.scene, os.path.join(scene_dir, usd_file)
144:    env_cfg = configs.env_cfg.set_robot(robot, env_cfg, robot_pose)
147:        env_cfg.scene = _set_up_scene_cameras(env_cfg.scene, sim_cfg, robot)
155:    env_cfg.scene = configs.scene_cfg.set_light_asset(env_cfg.scene, **light_cfg)
166:    env_cfg.scene = _set_up_scene_objects(env_cfg.scene, object_states["objects"])
169:        env_cfg.scene = _set_up_scene_containers(
170:            env_cfg.scene, object_states["containers"]
176:        objects = [key for key in vars(env_cfg.scene) if key.startswith("object")]
182:            os.path.basename(getattr(env_cfg.scene, o).spawn.usd_path),
189:    env_cfg.episode_length_s = sim_cfg["tasks"][task]["episode_length"]
200:    if hasattr(env_cfg.scene, "container"):
202:            os.path.basename(env_cfg.scene.container.spawn.usd_path),
208:    env_cfg.events = configs.event_cfg.get_event_cfg(
211:    env_cfg.terminations = configs.termination_cfg.get_termination_cfg(
229:    return env_cfg, object_tags, objects, object_sizes
470:    object_direction = random_position - object_position
472:        object_direction
473:        / np.linalg.norm(object_direction)
657:def set_object_material(target_object, n_envs=1):
663:        materials, torch.arange(n_envs)
674:    env_origins=None,
685:                ee_state.target_pos_w[..., 0, :] - env_origins, robot_quat
699:                object_state.root_pos_w - env_origins, robot_quat
715:                container_state.root_pos_w - env_origins, robot_quat
794:def get_next_object(scene_objects, scene, env_idx=None):
795:    next_object = []  # next object index for each environment
796:    n_envs = len(scene_objects)
797:    for i in range(n_envs):
798:        if len(scene_objects[i]) == 0 or (env_idx is not None and i != env_idx):
807:        fastest_index = torch.argmax(speed, dim=0).item()
808:        next_object.append(fastest_index)
810:    return next_object if env_idx is None else next_object[env_idx]
813:def get_env_states(states, n_envs=1):
827:    env_states = [{} for _ in range(n_envs)]
830:        for eid in range(n_envs):
846:                if k not in env_states[eid]:
847:                    env_states[eid][k] = []
849:                env_states[eid][k].append(value)
856:                        if cam_key not in env_states[eid]:
857:                            env_states[eid][cam_key] = []
859:                        env_states[eid][cam_key].append(v[eid])
861:    return env_states
864:def simulate(sim_cfg, task, robot, scene_dir, object_metadata, seed):
867:    # Create a new environment
868:    env_cfg, object_tags, objects, object_sizes = get_env_cfg(
873:        scene_dir,
884:    env = gym.make("Robot-Env-Cfg-v0", cfg=env_cfg, seed=seed)
885:    # Reset environment at start
886:    env.reset(seed=seed)
889:    if "container" in env.unwrapped.scene.keys():
890:        container_data = env.unwrapped.scene["container"].data
892:            os.path.basename(env_cfg.scene.container.spawn.usd_path),
894:            env.unwrapped.device,
912:            "dt": env_cfg.sim.dt * env_cfg.decimation,
913:            "num_envs": env.unwrapped.num_envs,
914:            "device": env.unwrapped.device,
920:        env.unwrapped.scene["object"],
921:        n_envs=env.unwrapped.num_envs,
925:    env_states = []
926:    term_mgr = env.env.termination_manager
929:    scene_objects = [copy.deepcopy(objects) for _ in range(env.unwrapped.num_envs)]
930:    curr_object_idx = get_next_object(scene_objects, env.unwrapped.scene)
935:            env.step(torch.from_numpy(env.action_space.sample()))
940:            env.unwrapped.scene["ee_frame"].data,
941:            env.unwrapped.scene.state["articulation"]["robot"]["joint_position"],
942:            [env.unwrapped.scene[co].data for co in curr_object][0],  # TODO: remove [0]
946:            env.unwrapped.scene["robot"].data.root_pos_w,
947:            env.unwrapped.scene["robot"].data.root_quat_w,
948:            env.unwrapped.device,
958:                for env_idx, op in enumerate(object_placed):
959:                    if not op or len(scene_objects[env_idx]) < 2:
962:                    scene_objects[env_idx].remove(curr_object[env_idx])
963:                    curr_object_idx[env_idx] = get_next_object(
964:                        scene_objects, env.unwrapped.scene, env_idx
966:                    _curr_object = curr_object[env_idx]
967:                    _next_object = scene_objects[env_idx][curr_object_idx[env_idx]]
968:                    curr_object[env_idx] = _next_object
971:                        % (env_idx, _curr_object, _next_object)
978:            env.unwrapped.scene.sensors, ["rgb", "depth", "seg"]
980:        env.step(next_state["action"])
981:        env_states.append(
991:    env_states = get_env_states(env_states, env.unwrapped.num_envs)
992:    env.close()
997:        env_cfg,
1001:            for env_id, es in enumerate(env_states)
1002:            if is_done[env_id].item() or sim_cfg["debug"]
1017:def is_object_direction_changed(scene_cfg, object_velocity, n_steps=25):
1083:    env_state, state_keys=["sm_state", "ee_pos", "object_pos", "object_vel"]
1089:    for st_key, frames in env_state.items():
1123:        raise ValueError("No camera frames found in the environment state.")
1139:                {k: env_state[k][frame_idx] for k in state_keys if k in env_state},
1222:            "num_envs": args.num_envs,
1230:        args.object_dir, object_categories + container_categories
1232:    # Perform simulations in the environment
1233:    n_simulations = 0
1235:    while n_simulations < args.n_simulations:
1242:            env_cfg, object_tags, env_states = simulate(
1246:                args.scene_dir,
1253:            n_simulations += 1
1257:        for es in env_states:
1261:            env_cfg = env_cfg.to_dict()
1262:            if is_object_stopped(env_cfg["scene"], es["object_vel"]):
1264:            if is_object_direction_changed(env_cfg["scene"], es["object_vel"]):
1271:                args.task, args.robot, seed, env_cfg["scene"]
1281:                    env_cfg["seed"] = seed
1282:                    env_cfg["instruction"] = {"task": args.task, **object_tags}
1283:                    json.dump(get_object_without_numpy(env_cfg), fp, indent=2)
1300:        n_simulations += 1
1308:    SHARED_PARAMETERS = ["num_envs", "save"]
1312:    parser.add_argument(
1318:    parser.add_argument(
1319:        "--num_envs", type=int, default=1, help="Number of environments to simulate."
1321:    parser.add_argument(
1322:        "--save",
1331:    parser.add_argument("--robot", default="franka")
1332:    parser.add_argument(
1333:        "--scene_dir", default=os.path.join(PROJECT_HOME, os.pardir, "scenes")
1335:    parser.add_argument(
1336:        "--object_dir", default=os.path.join(PROJECT_HOME, os.pardir, "objects")
1338:    parser.add_argument(
1341:    parser.add_argument("--task", default="pick")
1342:    parser.add_argument(
1347:    parser.add_argument("--debug", action="store_true", default=False)
1348:    parser.add_argument("--disable_sm", action="store_true", default=False)
1349:    parser.add_argument("--path_tracing", action="store_true", default=False)
1350:    parser.add_argument("--seed", type=int, default=None)
1351:    parser.add_argument("-n", "--n_simulations", type=int, default=10_000)

## Old object candidates
drwxrwxr-x 24 redafrix redafrix 4096 Apr  5 20:31 /home/redafrix/isaac_franka_env_probe/assets_staging/objects
-rw-rw-r-- 1 redafrix redafrix 184M Apr  5 14:32 /home/redafrix/isaac_franka_env_probe/downloads/DOM_Assets.zip


## Objects final check
lrwxrwxrwx 1 redafrix redafrix 76 Jun 11 11:06 /home/redafrix/tests/internship/isaac_dynamicVLA-test/objects -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/objects
object USD count:
211
metadata:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/metadata.json
sample:
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/tangerine/tangerine00.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/tangerine/tangerine05.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/tangerine/tangerine06.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/tangerine/tangerine03.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/tangerine/tangerine04.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/kiwi/kiwi05.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/kiwi/kiwi07.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/kiwi/kiwi00.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/beer/beer19.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/beer/beer13.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/beer/beer01.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/beer/beer05.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/beer/beer07.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/beer/beer09.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/beer/beer03.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/beer/beer00.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple22.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple12.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple00.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple04.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple03.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple13.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple02.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple10.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple07.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple11.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple09.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple01.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple18.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple20.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple06.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple08.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple19.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple05.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple15.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/apple/apple14.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/placemat/placemat03.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/placemat/placemat00.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/placemat/placemat02.usd
/home/redafrix/tests/internship/isaac_dynamicVLA-test/objects/placemat/placemat01.usd

## Locate DOM-Test candidates
### /home/redafrix/tests/internship/isaac_dynamicVLA-test/downloads

### /home/redafrix/Downloads
2026-04-30 13:12 | 17067 bytes | /home/redafrix/Downloads/sci-fi-motivation-letter.zip
2026-04-30 14:59 | 6276 bytes | /home/redafrix/Downloads/image.png.html
2026-04-30 15:31 | 19086 bytes | /home/redafrix/Downloads/sci-fi-motivation-letter (1).zip
2026-04-30 16:43 | 19086 bytes | /home/redafrix/Downloads/sci-fi-motivation-letter2.zip
2026-05-02 20:40 | 146279 bytes | /home/redafrix/Downloads/La.Traque.dans.le.Sang.S01.MULTI.VFF.1080p.WEB.DV.HDR.EAC3.5.1.H265-R3MiX.torrent
2026-05-02 21:30 | 107334970 bytes | /home/redafrix/Downloads/discord-0.0.135.deb
2026-05-03 14:52 | 13304 bytes | /home/redafrix/Downloads/ai_studio_code (1).txt
2026-05-03 16:57 | 133344 bytes | /home/redafrix/Downloads/Mars - A SIGNER.pdf
2026-05-03 16:57 | 133593 bytes | /home/redafrix/Downloads/Avril - A SIGNER.pdf
2026-05-03 16:57 | 135213 bytes | /home/redafrix/Downloads/Avril - A SIGNER (1).pdf
2026-05-03 16:57 | 386528 bytes | /home/redafrix/Downloads/Fwd STAGE Gana et Reda - Attestation de présence.zip
2026-05-03 17:00 | 144666 bytes | /home/redafrix/Downloads/Avril - A SIGNER(signer par Reda) .pdf
2026-05-05 12:11 | 33441939 bytes | /home/redafrix/Downloads/ckpt-60000.zip
2026-05-07 15:22 | 2746 bytes | /home/redafrix/Downloads/REMOTE_CONTROL_GUIDE.txt
2026-05-07 21:19 | 2179140 bytes | /home/redafrix/Downloads/discord-1.0.137.deb
2026-05-10 14:41 | 3901798 bytes | /home/redafrix/Downloads/Gemini_Generated_Image_6tkt2d6tkt2d6tkt.png
2026-05-10 17:14 | 117397 bytes | /home/redafrix/Downloads/La.Traque.dans.le.Sang.S02.MULTI.VFF.1080p.WEB.DV.HDR.EAC3.5.1.H265-R3MiX.torrent
2026-05-11 14:01 | 24003 bytes | /home/redafrix/Downloads/avis_echeance-20260511-140105.924_62.pdf
2026-05-11 17:02 | 238767 bytes | /home/redafrix/Downloads/v8_balanced_comparison.png
2026-05-12 09:46 | 5415778 bytes | /home/redafrix/Downloads/phase2_tdqc_k8_best_ckpt_ood_bundle_20260512.zip
2026-05-12 10:13 | 5428873 bytes | /home/redafrix/Downloads/phase2_tdqc_k8_best_ckpt_ood_bundle_20260512 (1).zip
2026-05-13 09:56 | 16299860 bytes | /home/redafrix/Downloads/2604.16677v1.pdf
2026-05-13 12:18 | 2080306672 bytes | /home/redafrix/Downloads/ckpt-50000.zip
2026-05-15 20:19 | 2179498 bytes | /home/redafrix/Downloads/discord-1.0.138.deb
2026-05-19 16:15 | 474169 bytes | /home/redafrix/Downloads/Isaac_Sim_Beginner_Help_Guide.pdf
2026-05-19 18:50 | 2179500 bytes | /home/redafrix/Downloads/discord-1.0.139.deb
2026-05-20 15:34 | 9758730 bytes | /home/redafrix/Downloads/2510.09459v2.pdf
2026-05-28 15:06 | 937994 bytes | /home/redafrix/Downloads/ilovepdf_merged.pdf
2026-06-01 10:15 | 13851 bytes | /home/redafrix/Downloads/Texte collé(2).txt
2026-06-01 10:21 | 87454 bytes | /home/redafrix/Downloads/cv_fr (1).pdf
2026-06-01 10:22 | 85856 bytes | /home/redafrix/Downloads/cv_en.pdf
2026-06-01 11:32 | 32542 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_base_EN.pdf
2026-06-01 11:32 | 33200 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_base_FR.pdf
2026-06-01 11:46 | 44947 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_base_EN_lettre_en.pdf
2026-06-01 11:46 | 45214 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_base_FR_lettre_fr.pdf
2026-06-01 12:06 | 63264 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_sci_fi_letter_base_v2_final_EN.pdf
2026-06-01 12:06 | 63861 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_sci_fi_letter_base_v2_final_FR.pdf
2026-06-01 12:20 | 77070 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_sci_fi_letter_base_v3_1_FR_EN.pdf
2026-06-01 13:58 | 69362 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_Mistral_AI_Research_Engineer_Robotics_EN.pdf
2026-06-01 13:58 | 77697 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Mistral_AI_Research_Engineer_Robotics_EN.pdf
2026-06-01 14:06 | 77697 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Mistral_AI_Research_Engineer_Robotics_EN (1).pdf
2026-06-01 14:13 | 77697 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Mistral_AI_Research_Engineer_Robotics_EN (2).pdf
2026-06-01 14:14 | 80853 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Mistral_AI_Research_Engineer_Robotics_FR.pdf
2026-06-01 14:25 | 77697 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Mistral_AI_Research_Engineer_Robotics_EN (3).pdf
2026-06-01 14:27 | 77697 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Mistral_AI_Research_Engineer_Robotics_EN (4).pdf
2026-06-01 14:33 | 81153 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Mistral_AI_EN_FULL_PAGE_FINAL.pdf
2026-06-01 14:48 | 69697 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Robeaute_Surgical_Robotics_FULL_PAGE_FINAL_EN.pdf
2026-06-01 14:48 | 81918 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Robeaute_EN_FULL_PAGE_FINAL.pdf
2026-06-01 15:05 | 70186 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Robeaute_System_VV_BALANCED_FINAL_EN.pdf
2026-06-01 15:06 | 80655 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Robeaute_System_VV_EN_BALANCED_FINAL.pdf
2026-06-01 15:07 | 70186 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Robeaute_System_VV_BALANCED_FINAL_EN (1).pdf
2026-06-01 15:38 | 27819 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Wandercraft_Systems_Engineer_Robotics_Safety_Functional_Safety_EN_BALANCED_FINAL.pdf
2026-06-01 15:38 | 69455 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Wandercraft_Systems_Engineer_Robotics_Safety_Functional_Safety_FINAL_EN.pdf
2026-06-01 15:38 | 928689 bytes | /home/redafrix/Downloads/wandercraft_systems_engineer_robotics_safety_application_pack_BALANCED_FINAL.zip
2026-06-01 15:40 | 27792 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Iris_Lab_Robotics_Engineer_Drone_Tracking_and_AI_Computer_Vision_EN_BALANCED_FINAL.pdf
2026-06-01 15:40 | 69675 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Iris_Lab_Robotics_Engineer_Drone_Tracking_and_AI_Computer_Vision_FINAL_EN.pdf
2026-06-01 15:50 | 68893 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Harmattan_AI_Automation_Software_Engineer_APPROVED_STYLE_FINAL_EN.pdf
2026-06-01 15:50 | 80495 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Harmattan_AI_Automation_Software_Engineer_EN_APPROVED_STYLE_FINAL.pdf
2026-06-01 16:01 | 69092 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Harmattan_AI_Software_Engineer_Validation_APPROVED_STYLE_FINAL_EN.pdf
2026-06-01 16:01 | 80532 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Harmattan_AI_Software_Engineer_Validation_EN_APPROVED_STYLE_FINAL.pdf
2026-06-01 16:18 | 69664 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Harmattan_AI_Computer_Vision_Engineer_Lausanne_APPROVED_STYLE_FINAL_EN.pdf
2026-06-01 16:18 | 79968 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Harmattan_AI_Computer_Vision_Engineer_Lausanne_EN_APPROVED_STYLE_FINAL.pdf
2026-06-01 16:24 | 64272 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Harmattan_AI_Computer_Vision_Engineer_Paris_APPROVED_STYLE_FINAL_EN.pdf
2026-06-01 16:24 | 79986 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Harmattan_AI_Computer_Vision_Engineer_Paris_EN_APPROVED_STYLE_FINAL.pdf
2026-06-01 16:29 | 79986 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Harmattan_AI_Computer_Vision_Engineer_Paris_EN_APPROVED_STYLE_FINAL (1).pdf
2026-06-01 16:29 | 80040 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Harmattan_AI_Computer_Vision_Engineer_VIO_Lausanne_EN_APPROVED_STYLE_FINAL.pdf
2026-06-01 16:36 | 80614 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Harmattan_AI_Physics_Simulation_Engineer_Paris_EN_APPROVED_STYLE_FINAL.pdf
2026-06-01 16:52 | 5843 bytes | /home/redafrix/Downloads/Texte collé(16).txt
2026-06-01 20:18 | 2177818 bytes | /home/redafrix/Downloads/discord-1.0.141.deb
2026-06-03 09:18 | 135007 bytes | /home/redafrix/Downloads/Reda_Mai_A SIGNER.pdf
2026-06-03 09:20 | 144947 bytes | /home/redafrix/Downloads/Reda_Mai_SIGNER_par_Reda.pdf
2026-06-03 11:38 | 172284 bytes | /home/redafrix/Downloads/WhatsApp Image 2026-06-03 at 11.38.29.jpeg
2026-06-03 16:39 | 71062 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_SII_Ingenieur_Controle_Commande_Robotique_FR_APPROVED_STYLE_FINAL.pdf
2026-06-03 16:39 | 80707 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_SII_Ingenieur_Controle_Commande_Robotique_FR_APPROVED_STYLE_FINAL.pdf
2026-06-03 16:45 | 70784 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_CS_Sopra_Steria_Ingenieur_Logiciel_Robotique_FR_APPROVED_STYLE_FINAL.pdf
2026-06-03 16:45 | 81008 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_CS_Sopra_Steria_Ingenieur_Logiciel_Robotique_FR_APPROVED_STYLE_FINAL.pdf
2026-06-03 19:37 | 47585 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_ALTEN_Robotique_Vision_IA_Developpement_FR_APPROVED_STYLE_FINAL.pdf
2026-06-03 19:37 | 81188 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_ALTEN_Robotique_Vision_IA_Developpement_FR_APPROVED_STYLE_FINAL (1).pdf
2026-06-03 19:37 | 81188 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_ALTEN_Robotique_Vision_IA_Developpement_FR_APPROVED_STYLE_FINAL.pdf
2026-06-03 20:15 | 70422 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_ALTEN_Robotique_Vision_IA_Developpement_FR_SCI_FI_APPROVED_FINAL.pdf
2026-06-04 11:29 | 3591610 bytes | /home/redafrix/Downloads/postulation_pipeline_FULL_REPRODUCIBLE_v24.zip
2026-06-04 11:29 | 69930 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_Akkodis_Developpeur_IA_Generative_FR_SCI_FI_APPROVED_FINAL.pdf
2026-06-04 11:29 | 81050 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Akkodis_Developpeur_IA_Generative_FR_APPROVED_STYLE_FINAL.pdf
2026-06-04 11:30 | 3598456 bytes | /home/redafrix/Downloads/postulation_pipeline_current_clean_v24.zip
2026-06-04 11:49 | 70009 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_Viveris_CPP_Qt_Robotique_Drone_FR_SCI_FI_APPROVED_FINAL.pdf
2026-06-04 11:49 | 81014 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Viveris_CPP_Qt_Robotique_Drone_FR_APPROVED_STYLE_FINAL.pdf
2026-06-04 13:45 | 70156 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_ADENTIS_Ingenieur_Robotique_FR_SCI_FI_APPROVED_FINAL.pdf
2026-06-04 13:45 | 80807 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_ADENTIS_Ingenieur_Robotique_FR_APPROVED_STYLE_FINAL.pdf
2026-06-04 13:54 | 80192 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Developpeur_CPP_ROS_Embarque_FR_APPROVED_STYLE_FINAL.pdf
2026-06-04 13:59 | 79959 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Fortil_Ingenieur_Roboticien_FR_APPROVED_STYLE_FINAL.pdf
2026-06-04 14:03 | 79959 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Fortil_Ingenieur_Roboticien_FR_APPROVED_STYLE_FINAL (1).pdf
2026-06-04 14:38 | 80303 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Parrot_Python_Automatisation_Tests_Drones_FR_APPROVED_STYLE_FINAL.pdf
2026-06-04 14:44 | 79375 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Parrot_Autonomie_Drone_Vision_Navigation_FR_APPROVED_STYLE_FINAL.pdf
2026-06-04 15:01 | 79940 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Parrot_Tests_Validation_Fonctionnelle_FR_APPROVED_STYLE_FINAL.pdf
2026-06-05 14:51 | 285028 bytes | /home/redafrix/Downloads/libero_goal_object_exact_trials0to9_40to49_eval_seed0_20260605.json
2026-06-05 14:51 | 35908 bytes | /home/redafrix/Downloads/libero_goal_object_exact_trials0to9_40to49_eval_seed0_20260605.csv
2026-06-05 15:20 | 192518 bytes | /home/redafrix/Downloads/libero_goal_object_reproduction_bundle_20260605.zip
2026-06-08 19:22 | 10622375 bytes | /home/redafrix/Downloads/v_FINAL_PFE.pdf
2026-06-10 14:03 | 7525 bytes | /home/redafrix/Downloads/LIBERO_GOAL_OBJECT_OOD_STEP9_FORENSIC_AUDIT_THRESH_0.5_20260610.md
2026-06-10 14:13 | 3591610 bytes | /home/redafrix/Downloads/postulation_pipeline_FULL_REPRODUCIBLE_v24 (1).zip
2026-06-10 16:25 | 80041 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_NAVER_AI_Research_Prototyping_EN_APPROVED_STYLE_FINAL.pdf
2026-06-10 16:27 | 69809 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_NAVER_AI_Research_Prototyping_EN_SCI_FI_APPROVED_FINAL.pdf
2026-06-10 16:33 | 80946 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_NAVER_AI_Research_Prototyping_FR_APPROVED_STYLE_FINAL.pdf
2026-06-10 16:43 | 70070 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_TEKEVER_Computer_Vision_Robotics_FR_SCI_FI_APPROVED_FINAL.pdf
2026-06-10 16:43 | 79765 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_TEKEVER_Computer_Vision_Robotics_FR_APPROVED_STYLE_FINAL.pdf
2026-06-10 16:58 | 69725 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_TEKEVER_Navigation_Research_Engineer_FR_SCI_FI_APPROVED_FINAL.pdf
2026-06-10 16:58 | 80899 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_TEKEVER_Navigation_Research_Engineer_FR_APPROVED_STYLE_FINAL.pdf
2026-06-10 18:28 | 70849 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_MARSO_Robotics_Deployment_Engineer_FR_SCI_FI_APPROVED_FINAL.pdf
2026-06-10 18:28 | 81867 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_MARSO_Robotics_Deployment_Engineer_FR_APPROVED_STYLE_FINAL.pdf
2026-06-10 18:51 | 70691 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Lettre_MARSO_Robotics_Software_Engineer_FR_SCI_FI_APPROVED_FINAL.pdf
2026-06-10 18:51 | 82554 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_MARSO_Robotics_Software_Engineer_FR_APPROVED_STYLE_FINAL.pdf
2026-06-10 19:01 | 70006 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_Dioxycle_Junior_Automation_Electrical_Engineer_EN_SCI_FI_APPROVED_FINAL.pdf
2026-06-10 19:01 | 81708 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_Dioxycle_Junior_Automation_Electrical_Engineer_EN_APPROVED_STYLE_FINAL.pdf
2026-06-10 19:59 | 69908 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_SMAROBIX_Runtime_Systems_Engineer_EN_SCI_FI_APPROVED_FINAL.pdf
2026-06-10 19:59 | 82041 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_SMAROBIX_Runtime_Systems_Engineer_EN_APPROVED_STYLE_FINAL.pdf
2026-06-10 20:36 | 137538 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_DGS_Junior_Robotics_Engineer_EN_APPROVED_STYLE_FINAL.pdf
2026-06-10 20:36 | 69626 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_DGS_Junior_Robotics_Engineer_EN_SCI_FI_APPROVED_FINAL.pdf
2026-06-10 21:04 | 138946 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_CV_AI_Robotics_Systems_Engineer_Singapore_EN_APPROVED_STYLE_FINAL.pdf
2026-06-10 21:04 | 69495 bytes | /home/redafrix/Downloads/Reda_OULD_OULHADJ_Letter_AI_Robotics_Systems_Engineer_Singapore_EN_SCI_FI_APPROVED_FINAL.pdf
2026-06-11 10:55 | 1581527028 bytes | /home/redafrix/Downloads/DOM-Test.zip

### old project downloads
2026-04-05 14:32 | 192584117 bytes | /home/redafrix/isaac_franka_env_probe/downloads/DOM_Assets.zip
2026-06-06 17:54 | 737 bytes | /home/redafrix/isaac_franka_env_probe/downloads/DOM-3D-Objects.download
2026-06-06 17:54 | 737 bytes | /home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.download
2026-06-06 17:54 | 737 bytes | /home/redafrix/isaac_franka_env_probe/downloads/index.html?f=DOM-3D-Objects
2026-06-06 17:54 | 737 bytes | /home/redafrix/isaac_franka_env_probe/downloads/index.html?f=DOM-Test
2026-06-10 18:38 | 737 bytes | /home/redafrix/isaac_franka_env_probe/downloads/?f=DOM-Test
2026-06-11 10:57 | 1581527028 bytes | /home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.zip
2026-06-11 10:57 | 61 bytes | /home/redafrix/isaac_franka_env_probe/downloads/chosen_dom_test_path.txt

## DOM-Test archive candidates
score=18 size=1.473GB path=/home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.zip
score=18 size=1.473GB path=/home/redafrix/Downloads/DOM-Test.zip
score=10 size=0.029GB path=/home/redafrix/Downloads/testtt.pdf
score=10 size=0.004GB path=/home/redafrix/Downloads/test_2.pdf
score=10 size=0.002GB path=/home/redafrix/Downloads/Follow @uraharago 🌙for more Aizen soske is the greatest manipulator ever. ⚡Follow for more- @ur.mp4
score=3 size=1.937GB path=/home/redafrix/Downloads/ckpt-50000.zip
score=3 size=0.323GB path=/home/redafrix/Downloads/phase2_tdqc_raw_pro_4000_20260428_171248.zip
score=3 size=0.061GB path=/home/redafrix/Downloads/phillips-head-screwdriver-1.snapshot.5.zip
score=3 size=0.061GB path=/home/redafrix/Downloads/phillips-head-screwdriver-1.snapshot.5 (1).zip
score=3 size=0.053GB path=/home/redafrix/Downloads/phase2_tdqc_20260427_1.zip
score=3 size=0.053GB path=/home/redafrix/Downloads/Supports de cours-20260121.zip
score=3 size=0.045GB path=/home/redafrix/Downloads/projet_groupe_10.zip
score=3 size=0.036GB path=/home/redafrix/Downloads/lounas-portfolio-master.zip
score=3 size=0.036GB path=/home/redafrix/Downloads/reda-portfolio-master.zip
score=3 size=0.032GB path=/home/redafrix/Downloads/robot_modeling_png_pages.zip
score=3 size=0.031GB path=/home/redafrix/Downloads/ckpt-60000.zip
score=3 size=0.022GB path=/home/redafrix/Downloads/screwdriver-332.snapshot.1.zip
score=3 size=0.016GB path=/home/redafrix/Downloads/M1_project-table.zip
score=3 size=0.016GB path=/home/redafrix/Downloads/Diapos 2025-2026-20251230.zip
score=3 size=0.016GB path=/home/redafrix/Downloads/Diapos 2025-2026-20251229 (1).zip
score=3 size=0.013GB path=/home/redafrix/Downloads/Diapos 2025-2026-20251230 (1).zip
score=3 size=0.013GB path=/home/redafrix/Downloads/Diapos 2025-2026-20251229.zip
score=3 size=0.010GB path=/home/redafrix/Downloads/screwdriver-334.snapshot.4.zip
score=3 size=0.009GB path=/home/redafrix/Downloads/Diapos RL 2025-2026-20260102.zip
score=3 size=0.008GB path=/home/redafrix/Downloads/Diapos 2025-26-20260304.zip
score=3 size=0.007GB path=/home/redafrix/Downloads/M1_project-bcr_with_fr3.zip
score=3 size=0.006GB path=/home/redafrix/Downloads/presenation internship 2/internship_first_presentation.zip
score=3 size=0.006GB path=/home/redafrix/Downloads/presenation internship 2/dcdc/internship_first_presentation.zip
score=3 size=0.006GB path=/home/redafrix/Downloads/internship_first_presentation.zip
score=3 size=0.005GB path=/home/redafrix/Downloads/phase2_tdqc_k8_best_ckpt_ood_bundle_20260512 (1).zip
score=3 size=0.005GB path=/home/redafrix/Downloads/phase2_tdqc_k8_best_ckpt_ood_bundle_20260512.zip
score=3 size=0.005GB path=/home/redafrix/Downloads/tvtunes_7893.zip
score=3 size=0.004GB path=/home/redafrix/Downloads/Session Pratique-20251230.zip
score=3 size=0.004GB path=/home/redafrix/Downloads/Session Pratique-20251106.zip
score=3 size=0.004GB path=/home/redafrix/Downloads/Consignes Groupe 10-20260103.zip
score=3 size=0.004GB path=/home/redafrix/Downloads/Consignes Groupe 10-20251230.zip
score=3 size=0.003GB path=/home/redafrix/Downloads/postulation_pipeline_current_clean_v24.zip
score=3 size=0.003GB path=/home/redafrix/Downloads/postulation_pipeline_FULL_REPRODUCIBLE_v24.zip
score=3 size=0.003GB path=/home/redafrix/Downloads/postulation_pipeline_FULL_REPRODUCIBLE_v24 (1).zip
score=3 size=0.002GB path=/home/redafrix/Downloads/utserver.tar.gz
score=3 size=0.001GB path=/home/redafrix/Downloads/studentCV1P1.zip
score=3 size=0.001GB path=/home/redafrix/Downloads/presenation internship 2.zip
score=0 size=0.179GB path=/home/redafrix/isaac_franka_env_probe/downloads/DOM_Assets.zip
score=0 size=0.164GB path=/home/redafrix/Downloads/cursor_2.6.13_amd64.deb
score=0 size=0.128GB path=/home/redafrix/Downloads/tor-browser-linux-x86_64-15.0.5.tar.xz
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.128.deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.127.deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.127 (1).deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.129.deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.129 (1).deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.135.deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.132.deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.130.deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.130 (1).deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.131.deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.133.deb
score=0 size=0.100GB path=/home/redafrix/Downloads/discord-0.0.134.deb
score=0 size=0.075GB path=/home/redafrix/Downloads/Slides2025_s1_sans_animations.pdf
score=0 size=0.075GB path=/home/redafrix/Downloads/Slides2025_s1_sans_animations (2).pdf
score=0 size=0.075GB path=/home/redafrix/Downloads/Slides2025_s1_sans_animations (1).pdf
score=0 size=0.054GB path=/home/redafrix/Downloads/kling_20260216_Motion_Control__1538_0.mp4
score=0 size=0.048GB path=/home/redafrix/Downloads/2512.05927v2.pdf
score=0 size=0.038GB path=/home/redafrix/Downloads/2025-12-07 16-27-39.mkv
score=0 size=0.037GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Uncertainty-Aware Robotic World Model Makes Offline MBRL Work on Real Robots.pdf
score=0 size=0.035GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Flow Matching with Uncertainty Quantification and Guidance.pdf
score=0 size=0.035GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/V-JEPA 2.1 - Unlocking Dense Features in Video Self-Supervised Learning.pdf
score=0 size=0.035GB path=/home/redafrix/Downloads/2603.14482v2.pdf
score=0 size=0.035GB path=/home/redafrix/Downloads/2603.14482v2 (1).pdf
score=0 size=0.031GB path=/home/redafrix/Downloads/Robust Ladder Climbing with a Quadrupedal Robot.mp4
score=0 size=0.029GB path=/home/redafrix/Downloads/2403.13431v1.pdf
score=0 size=0.029GB path=/home/redafrix/Downloads/2403.13431.pdf
score=0 size=0.027GB path=/home/redafrix/Downloads/quadruped_presentation_20251210.pdf
score=0 size=0.024GB path=/home/redafrix/Downloads/.org.chromium.Chromium.j5TOVA
score=0 size=0.023GB path=/home/redafrix/Downloads/Slides2025_s1_sans_animations (1)_compressed.pdf
score=0 size=0.022GB path=/home/redafrix/Downloads/fddebe55-38c0-41a2-9d54-18a0cc99a1ef.ogg
score=0 size=0.022GB path=/home/redafrix/Downloads/Slides_Notes_Combined_9up_compressed.pdf
score=0 size=0.021GB path=/home/redafrix/Downloads/Slides_Notes_Combined_9up_compressed (1).pdf
score=0 size=0.021GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/SRPO - Self-Referential Policy Optimization for Vision-Language-Action Models.pdf
score=0 size=0.020GB path=/home/redafrix/Downloads/supplementary_video.mp4
score=0 size=0.020GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Confidence Calibration in Vision-Language-Action Models.pdf
score=0 size=0.019GB path=/home/redafrix/Downloads/2506.09985v1.pdf
score=0 size=0.015GB path=/home/redafrix/Downloads/2604.16677v1.pdf
score=0 size=0.014GB path=/home/redafrix/Downloads/1000_steps_4up_grid.mp4
score=0 size=0.014GB path=/home/redafrix/Downloads/hf_20260226_211825_25a02e2d-1d31-48d2-9443-54a1045df582.mp4
score=0 size=0.014GB path=/home/redafrix/Downloads/2510.10903v1.pdf
score=0 size=0.014GB path=/home/redafrix/Downloads/1000_steps_working_3views-2026-02-04_14.09.34_3x3_grid.mp4
score=0 size=0.014GB path=/home/redafrix/Downloads/anydesk_7.1.2-1_amd64.deb
score=0 size=0.013GB path=/home/redafrix/Downloads/Scientific_Poster_Reda_Ouldoulhadj.pdf
score=0 size=0.013GB path=/home/redafrix/Downloads/Scientific_Poster_Reda_Ouldoulhadj (1).pdf
score=0 size=0.012GB path=/home/redafrix/Downloads/presenation ct.pdf
score=0 size=0.011GB path=/home/redafrix/Downloads/presenation ct (2).pdf
score=0 size=0.011GB path=/home/redafrix/Downloads/presenation ct (1).pdf
score=0 size=0.011GB path=/home/redafrix/Downloads/Présenation Group 10.pdf
score=0 size=0.011GB path=/home/redafrix/Downloads/Project_report_Gana_Reda.pdf
score=0 size=0.011GB path=/home/redafrix/Downloads/Project_report_Gana_Reda (1).pdf
score=0 size=0.011GB path=/home/redafrix/Downloads/main-4-30.pdf
score=0 size=0.011GB path=/home/redafrix/Downloads/main2-4-30.pdf
score=0 size=0.010GB path=/home/redafrix/Downloads/2604.20472v1.pdf
score=0 size=0.010GB path=/home/redafrix/Downloads/2_CNN_2025.pdf
score=0 size=0.010GB path=/home/redafrix/Downloads/2_CNN_2025 (1).pdf
score=0 size=0.010GB path=/home/redafrix/Downloads/v_FINAL_PFE.pdf
score=0 size=0.010GB path=/home/redafrix/Downloads/robotique_humanoide_sans_animations-1.pdf
score=0 size=0.010GB path=/home/redafrix/Downloads/robotique_humanoide_sans_animations-1 (2).pdf
score=0 size=0.010GB path=/home/redafrix/Downloads/robotique_humanoide_sans_animations-1 (1).pdf
score=0 size=0.010GB path=/home/redafrix/Downloads/moveit2_UR5/src/ur5_moveit_config/config/ur5/ur5.usd
score=0 size=0.010GB path=/home/redafrix/Downloads/2512.24497v2.pdf
score=0 size=0.009GB path=/home/redafrix/Downloads/Gemini_Generated_Image_480nmx480nmx480n.png
score=0 size=0.009GB path=/home/redafrix/Downloads/dreamina-2026-03-08-4913-Cinematic, high-impact motion transition....mp4
score=0 size=0.009GB path=/home/redafrix/Downloads/2510.09459v2.pdf
score=0 size=0.009GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling.pdf
score=0 size=0.009GB path=/home/redafrix/Downloads/Gemini_Generated_Image_dpxn05dpxn05dpxn.png
score=0 size=0.009GB path=/home/redafrix/Downloads/A king never gives up 🏆📈👑animemotivation #recordofragnarok #animeinspiration #qinshihuang #mo.mp4
score=0 size=0.009GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/When to Act, Ask, or Learn - Uncertainty-Aware Policy Steering.pdf
score=0 size=0.008GB path=/home/redafrix/Downloads/Gemini_Generated_Image_7bov6a7bov6a7bov.png
score=0 size=0.008GB path=/home/redafrix/Downloads/1_Detection_segmentation.pdf
score=0 size=0.008GB path=/home/redafrix/Downloads/Gemini_Generated_Image_9lv2al9lv2al9lv2.png
score=0 size=0.008GB path=/home/redafrix/Downloads/Gemini_Generated_Image_eyo862eyo862eyo8.png
score=0 size=0.008GB path=/home/redafrix/Downloads/Gemini_Generated_Image_geud09geud09geud.png
score=0 size=0.008GB path=/home/redafrix/Downloads/hf_20260215_215452_9ccf1a0e-6288-4b6c-aec7-0cc6d4cb4f5b.mp4
score=0 size=0.008GB path=/home/redafrix/Downloads/tinyvla_lora_first_attempt (online-video-cutter.com).mp4
score=0 size=0.008GB path=/home/redafrix/Downloads/poly.pdf
score=0 size=0.008GB path=/home/redafrix/Downloads/1000_steps_working_3views-2026-02-04_14.09.34_3x3_grid_plus_smolVLA.mp4
score=0 size=0.008GB path=/home/redafrix/Downloads/smolVLA_4000_steps_sucess_rate_85%.mp4
score=0 size=0.008GB path=/home/redafrix/Downloads/Gemini_Generated_Image_b7otyhb7otyhb7ot.png
score=0 size=0.008GB path=/home/redafrix/Downloads/Gemini_Generated_Image_13i9nq13i9nq13i9.png
score=0 size=0.008GB path=/home/redafrix/Downloads/Gemini_Generated_Image_pkkdzppkkdzppkkd.png
score=0 size=0.008GB path=/home/redafrix/Downloads/Gemini_Generated_Image_ma4e19ma4e19ma4e.png
score=0 size=0.008GB path=/home/redafrix/Downloads/yazuwi_san_background.png
score=0 size=0.007GB path=/home/redafrix/Downloads/Gemini_Generated_Image_pkz3qopkz3qopkz3.png
score=0 size=0.007GB path=/home/redafrix/Downloads/pipi.mp4
score=0 size=0.007GB path=/home/redafrix/Downloads/episode_000024.hdf5
score=0 size=0.007GB path=/home/redafrix/Downloads/Gemini_Generated_Image_4eyw0x4eyw0x4eyw.png
score=0 size=0.007GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots.pdf
score=0 size=0.007GB path=/home/redafrix/Downloads/yazuwi_san_background_2.png
score=0 size=0.007GB path=/home/redafrix/Downloads/Gemini_Generated_Image_nhvimznhvimznhvi.png
score=0 size=0.007GB path=/home/redafrix/Downloads/CommandeBSAdapt2026.pdf
score=0 size=0.007GB path=/home/redafrix/Downloads/Gemini_Generated_Image_ceq9acceq9acceq9.png
score=0 size=0.007GB path=/home/redafrix/Downloads/1000_steps_merged_4x (online-video-cutter.com).mp4
score=0 size=0.007GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Diff-DAgger - Uncertainty Estimation with Diffusion Policy for Robotic Manipulation.pdf
score=0 size=0.007GB path=/home/redafrix/Downloads/Gemini_Generated_Image_umwmn7umwmn7umwm.png
score=0 size=0.007GB path=/home/redafrix/Downloads/Gemini_Generated_Image_g85hlkg85hlkg85h.png
score=0 size=0.007GB path=/home/redafrix/Downloads/Gemini_Generated_Image_q5eawsq5eawsq5ea (1).png
score=0 size=0.007GB path=/home/redafrix/Downloads/M1_project-bcr_with_fr3/src/fr3/fr3_description/meshes/robot_arms/fr3/visual/link0.dae
score=0 size=0.007GB path=/home/redafrix/Downloads/Gemini_Generated_Image_q5eawsq5eawsq5ea.png
score=0 size=0.006GB path=/home/redafrix/Downloads/yazuwi_san_pfp.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_pgutm2pgutm2pgut.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_s401dys401dys401.png
score=0 size=0.006GB path=/home/redafrix/Downloads/nnnn.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_v8ihn6v8ihn6v8ih.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_v8ihn6v8ihn6v8ih (2).png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_v8ihn6v8ihn6v8ih (1).png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_xcvg4qxcvg4qxcvg.png
score=0 size=0.006GB path=/home/redafrix/Downloads/3_RNN_Transformers_2025.pdf
score=0 size=0.006GB path=/home/redafrix/Downloads/3_RNN_Transformers_2025 (1).pdf
score=0 size=0.006GB path=/home/redafrix/Downloads/smolVLA_4000_steps_sucess_rate_80%.mp4
score=0 size=0.006GB path=/home/redafrix/Downloads/𝗦𝗵𝗮𝗱𝗼𝘄 𝗕𝗼𝘅𝗶𝗻𝗴 🥊 Anyone wanting to improve their boxing should be using shadow boxin.mp4
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_h5t5t5h5t5t5h5t5.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_unyek2unyek2unye.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_b8b0d2b8b0d2b8b0.png
score=0 size=0.006GB path=/home/redafrix/Downloads/2409.17731v2_copy.pdf
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_3yw1kj3yw1kj3yw1.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_m8us75m8us75m8us.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_1vik1u1vik1u1vik.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_dwamjsdwamjsdwam.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_ohbm9sohbm9sohbm.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_ylqcviylqcviylqc.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_xougs5xougs5xoug (1).png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_1ytto41ytto41ytt.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_kyxaehkyxaehkyxa.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_xougs5xougs5xoug.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_85wzml85wzml85wz.png
score=0 size=0.006GB path=/home/redafrix/Downloads/yazuwi_san_end_scene.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_80ddmv80ddmv80dd.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_hu0l46hu0l46hu0l.png
score=0 size=0.006GB path=/home/redafrix/Downloads/Gemini_Generated_Image_xevav9xevav9xeva.png
score=0 size=0.006GB path=/home/redafrix/Downloads/𝗦𝗵𝗮𝗱𝗼𝘄 𝗕𝗼𝘅𝗶𝗻𝗴 🥊 Anyone wanting to improve their boxing should be using shadow boxin_15s-plus-29s.mp4
score=0 size=0.006GB path=/home/redafrix/Downloads/kling_20260216_Motion_Control__1497_0.mp4
score=0 size=0.005GB path=/home/redafrix/Downloads/1_ML_intro_2025.pdf
score=0 size=0.005GB path=/home/redafrix/Downloads/1_ML_intro_2025 (1).pdf
score=0 size=0.005GB path=/home/redafrix/Downloads/hf_20260306_215012_0f43ade7-52f6-4b08-a0ca-369b08a8157d.mp4
score=0 size=0.005GB path=/home/redafrix/Downloads/Gemini_Generated_Image_n323htn323htn323.png
score=0 size=0.005GB path=/home/redafrix/Downloads/3_ML_supervised_learning_classification.pdf
score=0 size=0.005GB path=/home/redafrix/Downloads/2603.19312v2.pdf
score=0 size=0.005GB path=/home/redafrix/Downloads/Risk_Calibrated_Robot_Control.pdf
score=0 size=0.005GB path=/home/redafrix/Downloads/Gemini_Generated_Image_7ef4pd7ef4pd7ef4.png
score=0 size=0.005GB path=/home/redafrix/Downloads/Gemini_Generated_Image_lwj36rlwj36rlwj3.png
score=0 size=0.005GB path=/home/redafrix/Downloads/a reviser/contact_sheets/3_GeoDiff_contact.png
score=0 size=0.005GB path=/home/redafrix/Downloads/Gemini_Generated_Image_kfhqk3kfhqk3kfhq.png
score=0 size=0.005GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models.pdf
score=0 size=0.005GB path=/home/redafrix/Downloads/first_zero_shot_vla attempt.mp4
score=0 size=0.005GB path=/home/redafrix/Downloads/first_zero_shot_vla attempt (1).mp4
score=0 size=0.005GB path=/home/redafrix/Downloads/UE Gestion Projet 2025.pptx
score=0 size=0.005GB path=/home/redafrix/Downloads/Quadruped_Presentation.pdf
score=0 size=0.005GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/SimVLA - A Simple VLA Baseline for Robotic Manipulation.pdf
score=0 size=0.005GB path=/home/redafrix/Downloads/M1_project-bcr_with_fr3/src/fr3/fr3_description/meshes/robot_arms/fr3/visual/link6.dae
score=0 size=0.005GB path=/home/redafrix/Downloads/presenation internship 2/internship_first_presentation/presentation-internship-hybrid-vla-jepa/.git/objects/pack/pack-83915ebf1618f17581dee16220fab06a02ef85c0.pack
score=0 size=0.005GB path=/home/redafrix/Downloads/presenation internship 2/dcdc/internship_first_presentation/presentation-internship-hybrid-vla-jepa/.git/objects/pack/pack-83915ebf1618f17581dee16220fab06a02ef85c0.pack
score=0 size=0.005GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/LUMOS - Language-Conditioned Imitation Learning with World Models.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/2409.12514v5.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/part3_1_RL_2025-2026.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/part3_1_RL_2025-2026 (2).pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/part3_1_RL_2025-2026 (1).pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/s10462-023-10562-9.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/grok-video-a5b1b2d6-5b6c-4f3f-b068-3c6bda8ef3d6.mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/dreamina-2026-03-08-9791-A smooth, powerful cinematic transition ....mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/This one is soo catchy📈No Batidao🎶......#nobatidão #trend#viral #dance #instagramreels.mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/M1_project-bcr_with_fr3/src/fr3/fr3_description/meshes/robot_arms/fr3/visual/link7.dae
score=0 size=0.004GB path=/home/redafrix/Downloads/2_ML_param_nonparam.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/2_ML_param_nonparam (1).pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/Untitled Project.mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/tinyvla_lora_1000_steps_wrench_2x (online-video-cutter.com).mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/πRL - Online RL Fine-tuning for Flow-based Vision-Language-Action Models.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/Risk-Aware Navigation for Mobile Robots in Unknown M2 PAR.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/grok-video-a5b1b2d6-5b6c-4f3f-b068-3c6bda8ef3d6 (1).mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/a reviser/contact_sheets/1_Lyapunov_contact.png
score=0 size=0.004GB path=/home/redafrix/Downloads/ChatGPT Image 7 mars 2026, 00_09_23.png
score=0 size=0.004GB path=/home/redafrix/Downloads/SnapInsta.to_AQNJGjmHbqgScoWZMQtfxsTveyVkHAzSmNkNK8pjw5vjq3BDztcwcu4TxMKXz3dSoDg5MzLtwxYQgLHbGW4eeUBOonfzg3wFlRwfBOo.mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/King of kings 👑-#アニメ #qinshihuang #recordofragnarok #anime #animeedits.mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/hhhhhhhhhhhhh.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/c+++++.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/TP Cobotique 1 - Pick and Place (1) (1).pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/Gemini_Generated_Image_6tkt2d6tkt2d6tkt.png
score=0 size=0.004GB path=/home/redafrix/Downloads/VLA_survey.pdf
score=0 size=0.004GB path=/home/redafrix/Downloads/1000_steps_merged_4x (online-video-cutter.com) (1).mp4
score=0 size=0.004GB path=/home/redafrix/Downloads/0c0e8e50ec4dafd291049060b809ba4a-1763224405789-2jzc9d.mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/NAHHHH WHAT ... #memes #reels #epstein #doj #whatyousaying_trimmed_cut.mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/NAHHHH WHAT ... #memes #reels #epstein #doj #whatyousaying_trimmed.mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/a reviser/contact_sheets/Simulations_LinExacte_contact.png
score=0 size=0.003GB path=/home/redafrix/Downloads/Slides_Notes_Mixed_Format_compressed.pdf
score=0 size=0.003GB path=/home/redafrix/Downloads/pi0.pdf
score=0 size=0.003GB path=/home/redafrix/Downloads/Gemini_Generated_Image_t847ezt847ezt847.png
score=0 size=0.003GB path=/home/redafrix/Downloads/yazuwi_san_pfp (1) (1).png
score=0 size=0.003GB path=/home/redafrix/Downloads/TP_ROS_UR3e.pdf
score=0 size=0.003GB path=/home/redafrix/Downloads/Post filming 😛 dc- @river.novin#explorepage #dance #dancer #trend #trending #nohands_trimmed.mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/vidu-video-3034712618479801.mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/english presentation.pdf
score=0 size=0.003GB path=/home/redafrix/Downloads/M1_project-bcr_with_fr3/src/fr3/fr3_description/meshes/robot_arms/fr3/visual/link5.dae
score=0 size=0.003GB path=/home/redafrix/Downloads/tinyvla_lora_500_steps_wrench_2x (online-video-cutter.com).mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/yazuwi_san_video.mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/download.mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/video_ref.mp4
score=0 size=0.003GB path=/home/redafrix/Downloads/moveit2_UR5/src/robot_description/robotiq_meshes/visual/robotiq_85_base_link.dae
score=0 size=0.003GB path=/home/redafrix/Downloads/moveit2_UR5/src/robot_description/meshes/ur5/visual/robotiq_85_base_link.dae
score=0 size=0.002GB path=/home/redafrix/Downloads/nobatidao_05-14.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/tinyvla_lora_1000_steps_wrench_2x (online-video-cutter.com) (1).mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/yazuwi_san_background_compressed.png
score=0 size=0.002GB path=/home/redafrix/Downloads/M1_project-bcr_with_fr3/src/fr3/fr3_description/meshes/robot_arms/fr3/visual/link4.dae
score=0 size=0.002GB path=/home/redafrix/Downloads/Post filming 😛 dc- @river.novin#explorepage #dance #dancer #trend #trending #nohands.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/Gemini_Generated_Image_my3fw6my3fw6my3f.png
score=0 size=0.002GB path=/home/redafrix/Downloads/Automatic Navigation Map Generation.pptx
score=0 size=0.002GB path=/home/redafrix/Downloads/grok-video-cb85a168-b471-4cec-acf5-105c47854f6a.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/part3_3_RL_2025-2026_policy_gradient.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/part3_3_RL_2025-2026_policy_gradient (1).pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/M1_project-bcr_with_fr3/src/fr3/fr3_description/meshes/robot_arms/fr3/visual/link3.dae
score=0 size=0.002GB path=/home/redafrix/Downloads/part3_2_RL_2025-2026_DQN.pdf.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/part3_2_RL_2025-2026_DQN.pdf (3).pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/part3_2_RL_2025-2026_DQN.pdf (2).pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/part3_2_RL_2025-2026_DQN.pdf (1).pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/a reviser/contact_sheets/2_introLE_contact.png
score=0 size=0.002GB path=/home/redafrix/Downloads/yazuwi_san_background_2_compressed.png
score=0 size=0.002GB path=/home/redafrix/Downloads/ChatGPT Image 13 janv. 2026, 19_14_32.png
score=0 size=0.002GB path=/home/redafrix/Downloads/a reviser/contact_sheets/Simulations_LinTangente_Lyapunov_contact.png
score=0 size=0.002GB path=/home/redafrix/Downloads/grok-video-6515796b-c3e9-4a1e-a773-c023da4493fa (1).mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/nobatidao_05-13.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/Robust Ladder Climbing.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/a reviser/contact_sheets/td_3_GeoDiff_contact.png
score=0 size=0.002GB path=/home/redafrix/Downloads/a reviser/contact_sheets/0_modelisationRobotsMobiles_contact.png
score=0 size=0.002GB path=/home/redafrix/Downloads/yazuwi_san_end_scene.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/1000_steps_working_3views-2026-02-04_14.09.34_trim_4x.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/discord-1.0.139.deb
score=0 size=0.002GB path=/home/redafrix/Downloads/discord-1.0.138.deb
score=0 size=0.002GB path=/home/redafrix/Downloads/discord-1.0.137.deb
score=0 size=0.002GB path=/home/redafrix/Downloads/discord-1.0.141.deb
score=0 size=0.002GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/ProbeFlow - Training-Free Adaptive Flow Matching for Vision-Language-Action Models.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/magic_merged_with_nahhh_audio.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/cour_PMR.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/Face_Scan_Video_Generation.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/Commandeprédictive.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/Internship-at-Axter.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/tinyvla_lora_500_steps_wrench_2x (online-video-cutter.com) (2).mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/tinyvla_lora_500_steps_wrench_2x (online-video-cutter.com) (1).mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/02177310384693700000000000000000000ffffc0a8ac5de61e35.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/moveit2_UR5/src/robot_description/meshes/ur5/visual/upperarm.dae
score=0 size=0.002GB path=/home/redafrix/Downloads/yazuwi_san_pfp_compressed.png
score=0 size=0.002GB path=/home/redafrix/Downloads/yazuwi_san_pfp (2).png
score=0 size=0.002GB path=/home/redafrix/Downloads/UE Gestion Projet 2025.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/moveit2_UR5/src/robot_description/robotiq_meshes/collision/robotiq_85_base_link.stl
score=0 size=0.002GB path=/home/redafrix/Downloads/moveit2_UR5/src/robot_description/meshes/ur5/collision/robotiq_85_base_link.stl
score=0 size=0.002GB path=/home/redafrix/Downloads/1000_steps_merged_4x (online-video-cutter.com) (2).mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/magic_merged.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/𝗦𝗵𝗮𝗱𝗼𝘄 𝗕𝗼𝘅𝗶𝗻𝗴 🥊 Anyone wanting to improve their boxing should be using shadow boxin_31s-39s.mp4
score=0 size=0.002GB path=/home/redafrix/Downloads/master_PAR_Projet_SLIM_2026.pdf
score=0 size=0.002GB path=/home/redafrix/Downloads/Robust Ladder Climbing with a Quadrupedal Robot.pptx
score=0 size=0.001GB path=/home/redafrix/Downloads/1000_steps_working_3views-2026-02-04_14.09.34_trim_4x (1).mp4
score=0 size=0.001GB path=/home/redafrix/Downloads/grok-video-6515796b-c3e9-4a1e-a773-c023da4493fa.mp4
score=0 size=0.001GB path=/home/redafrix/Downloads/presenation internship 2/.git/objects/2d/df73b2b21e0ebafc030098a47bdb1209f0bffa
score=0 size=0.001GB path=/home/redafrix/Downloads/presenation internship 2/.git/objects/ee/e2c7c7d635a88c391e52b33b31189d35bc2aab
score=0 size=0.001GB path=/home/redafrix/Downloads/Untitled diagram-2026-04-10-133332.png
score=0 size=0.001GB path=/home/redafrix/Downloads/Untitled diagram-2026-04-10-133332 (1).png
score=0 size=0.001GB path=/home/redafrix/Downloads/yazuwi_san_pfp (1).png
score=0 size=0.001GB path=/home/redafrix/Downloads/local-repo-converted (5).txt
score=0 size=0.001GB path=/home/redafrix/Downloads/𝗦𝗵𝗮𝗱𝗼𝘄 𝗕𝗼𝘅𝗶𝗻𝗴 🥊 Anyone wanting to improve their boxing should be using shadow boxin_32s-39s.mp4
score=0 size=0.001GB path=/home/redafrix/Downloads/local-repo-converted (17).txt
score=0 size=0.001GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Shifting Uncertainty to Critical Moments - Towards Reliable Uncertainty Quantification for VLA Model.pdf
score=0 size=0.001GB path=/home/redafrix/Downloads/moveit2_UR5/src/robot_description/meshes/ur5/visual/forearm.dae
score=0 size=0.001GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Policy-Guided World Model Planning for Language-Conditioned Visual Navigation.pdf
score=0 size=0.001GB path=/home/redafrix/Downloads/presentation (1).pdf
score=0 size=0.001GB path=/home/redafrix/Downloads/1000_steps_merged_4x (online-video-cutter.com) (3).mp4
score=0 size=0.001GB path=/home/redafrix/Downloads/Record (online-voice-recorder.com).mp3
score=0 size=0.001GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/ReinFlow - Fine-tuning Flow Matching Policy with Online Reinforcement Learning.pdf
score=0 size=0.001GB path=/home/redafrix/Downloads/Chosen Architecture Draft Referenced PDFs/Uncertainty-Aware Deployment of Pre-trained Language-Conditioned Imitation Learning Policies.pdf
score=0 size=0.001GB path=/home/redafrix/Downloads/Partie3_GeometrieMultiVues.pdf
score=0 size=0.001GB path=/home/redafrix/Downloads/5697388a-decc-4edd-bafc-ef73fcb2c5c0.png
score=0 size=0.001GB path=/home/redafrix/Downloads/presentation.pdf
score=0 size=0.001GB path=/home/redafrix/Downloads/A-king-never-gives-up-___animemotivation-_recordofragnarok-_animeinspiration-_qinshihuang-_mo.mp3
score=0 size=0.001GB path=/home/redafrix/Downloads/conversation.txt
score=0 size=0.001GB path=/home/redafrix/Downloads/ryomen_sukuna_a0b1c2d3_fish.mp3
score=0 size=0.001GB path=/home/redafrix/Downloads/1000_steps_working_3views-2026-02-04_13.50.29_trim_4x (1).mp4
score=0 size=0.001GB path=/home/redafrix/Downloads/𝗦𝗵𝗮𝗱𝗼𝘄 𝗕𝗼𝘅𝗶𝗻𝗴 🥊 Anyone wanting to improve their boxing should be using shadow boxin_34s-39s.mp4
score=0 size=0.001GB path=/home/redafrix/Downloads/Partie 1 - ModeleStenopeCalibrage.pdf
score=-8 size=0.009GB path=/home/redafrix/Downloads/objectVLA.pdf
BEST_GUESS_DOM_TEST_ARCHIVE: /home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.zip

## Selected DOM-Test archive
/home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.zip
-rw-rw-r-- 1 redafrix redafrix 1.5G Jun 11 10:57 /home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.zip
/home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.zip: Zip archive data, at least v2.0 to extract, compression method=store

## First 300 archive entries
Archive:  /home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-04-23 20:22   scenes/
  8036917  2026-04-23 16:40   scenes/0106f9d2-5779-457b-9b8b-72942373d42e.usd
  5918590  2026-04-23 16:40   scenes/0398338b-d4c2-42f0-a1c3-c43ce0f23f7c.usd
  6259056  2026-04-23 16:40   scenes/04dcc229-3353-4d90-a058-080acbcc4d59.usd
  4462487  2026-04-23 16:40   scenes/058205e1-6ec4-4342-a609-1ecce3551c3b.usd
  3678204  2026-04-23 16:40   scenes/07da426f-2064-4f8a-bee2-a7d1e2741ec5.usd
  3674695  2026-04-23 16:40   scenes/106438c4-a1de-4c81-9740-74c214025a50.usd
  5062186  2026-04-23 16:40   scenes/10c73ad0-214c-4bf7-a4e8-1c154a77b7ed.usd
  3349345  2026-04-23 16:40   scenes/14f8c7f2-d61d-4a6f-86a6-2086a2157bf4.usd
  2237311  2026-04-23 16:40   scenes/1738bb5e-a0d6-4820-ad10-f3c4bf9533e9.usd
  8990434  2026-04-23 16:40   scenes/191931a4-ae27-44eb-a639-d8ee3de85a0b.usd
  3963700  2026-04-23 16:40   scenes/1a2853ed-7b80-419a-9707-7107959afeff.usd
  8951490  2026-04-23 16:40   scenes/1a8dbd8d-0025-4373-8b94-ee9dd9fa7295.usd
  5400008  2026-04-23 16:40   scenes/1cd0db41-bcd9-4af7-a0be-cce5de62cc35.usd
  9006826  2026-04-23 16:40   scenes/1d076f8c-e01d-4a2e-96f9-7676001a0d8c.usd
  7402099  2026-04-23 16:40   scenes/21465c7c-7ddc-4b9c-9c12-feebdbf9cd1e.usd
  6667477  2026-04-23 16:40   scenes/2311eda9-dcda-45fb-89c3-0c068ed74b9c.usd
 10254632  2026-04-23 16:40   scenes/2d728150-ecd3-4648-b584-68de8e9f9a89.usd
  3462361  2026-04-23 16:40   scenes/2e4fd266-4688-4343-896d-61b28ad746f0.usd
 12212290  2026-04-23 16:40   scenes/2f7b66ba-455d-4ee4-8212-3072b100e189.usd
  4816174  2026-04-23 16:40   scenes/338025eb-9da6-4d7a-9226-269351c76269.usd
  7941610  2026-04-23 16:40   scenes/36672c0e-419c-476e-83c0-5b04654d3690.usd
  7545548  2026-04-23 16:40   scenes/38e3cf4a-a67b-42d8-b467-2d1a3e5407a8.usd
  6688048  2026-04-23 16:40   scenes/3da510a3-8db8-425e-bd0c-99e5a12af2ca.usd
  7370875  2026-04-23 16:40   scenes/427248f1-b9be-41b9-bca5-ae3277b73e47.usd
  5651430  2026-04-23 16:40   scenes/42dac4e2-8940-4ea3-9039-030961b73776.usd
  6112125  2026-04-23 16:40   scenes/42fa9f8e-56c4-4ac8-95ac-29452eb2726a.usd
 15701834  2026-04-23 16:40   scenes/43f1271f-d362-49c1-9ebc-cf9f8c82ea81.usd
  8415615  2026-04-23 16:40   scenes/45dddc0b-2505-4dcd-b07e-f0ff4e5c90d4.usd
  6478006  2026-04-23 16:40   scenes/45fb7506-342f-4dc6-b2c3-2e041fe69faa.usd
  4536977  2026-04-23 16:40   scenes/47664f37-b639-45fd-a436-20fa2ab72ec7.usd
  6362805  2026-04-23 16:40   scenes/502565a4-cf3d-4679-9d4e-e75310597922.usd
 13886777  2026-04-23 16:40   scenes/58064c7d-8e8b-4149-9b3a-672cf22d4733.usd
 12901640  2026-04-23 16:40   scenes/5a5372e5-d820-434d-885d-710887b2b0ee.usd
 13008056  2026-04-23 16:40   scenes/5a6650a5-b713-4d8f-9c82-5fc49a5f6ea3.usd
  7445550  2026-04-23 16:40   scenes/5bb3120d-3ad7-4456-b332-5bc1d60dd53c.usd
 10999662  2026-04-23 16:40   scenes/5e2a38d6-75b9-4f91-a688-a2f3141230bd.usd
   268837  2026-04-23 16:40   scenes/620d9fb6-afad-4c3d-8517-4386a0f8d3d6.usd
  5645345  2026-04-23 16:40   scenes/6a8ad1d5-8c81-49bf-a752-fbe9448ff3b1.usd
  4096469  2026-04-23 16:40   scenes/6e356720-39a8-4843-874d-a71efc4fb1ff.usd
 10806209  2026-04-23 16:40   scenes/6ea55a54-e0ba-46be-be97-1453b19c010d.usd
  5185060  2026-04-23 16:40   scenes/73579a31-0878-40be-a445-ce768de6ddae.usd
  6953422  2026-04-23 16:40   scenes/73d4b873-78d5-47dc-a0b1-81d96baa7f4a.usd
  5606343  2026-04-23 16:40   scenes/7f56f3b3-faf3-44bb-89bf-e4f300718ce5.usd
  5335202  2026-04-23 16:40   scenes/862269d5-f301-4857-90ea-df3b2d848997.usd
  8046027  2026-04-23 16:40   scenes/865efbe7-e24e-4080-9c8e-dc6c52180ea6.usd
  3485875  2026-04-23 16:40   scenes/89cba9bf-de9b-44a3-90c4-cdfd777e3d95.usd
  4269142  2026-04-23 16:40   scenes/8cd5b2fd-c93f-4c67-9d58-1618296bf571.usd
 12143700  2026-04-23 16:40   scenes/90b7eea6-8bb6-48aa-9981-690ca4de4938.usd
  5874665  2026-04-23 16:40   scenes/91efeb20-7892-46d5-8846-35a2c8773e73.usd
 12012935  2026-04-23 16:40   scenes/92c1c4c2-73f3-4688-b0e8-493c94f7fbe4.usd
  8987051  2026-04-23 16:40   scenes/9819d7d9-5d08-48aa-b496-45bb26b0f5a3.usd
  6784371  2026-04-23 16:40   scenes/98d50a8c-8f9c-40c7-b306-2b282a3ade70.usd
  1331324  2026-04-23 16:40   scenes/9956c823-3aa0-4ff9-bd56-64d7f27e7bd8.usd
 10524991  2026-04-23 16:40   scenes/9f283b51-0327-43d5-9ec0-44d867530f4e.usd
 17471861  2026-04-23 16:40   scenes/9fa47876-dc0b-4cb1-b5dc-93ca194b1d87.usd
  5081376  2026-04-23 16:40   scenes/9faff3f5-2f29-4312-bf2f-712557fe9fe7.usd
 13712709  2026-04-23 16:40   scenes/a9efa7e9-ca08-4e7b-84cb-a1cbe3a71211.usd
 12440369  2026-04-23 16:40   scenes/aa2174af-a1ed-403f-b46d-bb44f315c181.usd
  8193199  2026-04-23 16:40   scenes/ab48b02d-9678-4949-83fe-0af34dad0bde.usd
  7042651  2026-04-23 16:40   scenes/aee07a67-c3a3-4382-955c-82bb53a70c36.usd
  9821683  2026-04-23 16:40   scenes/b4551582-1fbb-4320-bac8-74655b3babd1.usd
 11852665  2026-04-23 16:40   scenes/bba8c5f2-10f0-4917-b26b-82fb076a97b4.usd
  9908631  2026-04-23 16:40   scenes/c1117917-ddde-4d13-86e0-d8306e0c655f.usd
  5130342  2026-04-23 16:40   scenes/c1b3e945-cefc-4e73-89fc-099bb5352bac.usd
  3093073  2026-04-23 16:40   scenes/c49b0591-97b2-45e7-b0fd-0ac5968240ac.usd
  6182637  2026-04-23 16:40   scenes/c720579b-1608-48cc-8b29-79ad02aa2739.usd
  4799221  2026-04-23 16:40   scenes/c99f6564-2c07-4733-86c5-7d1712c3deac.usd
  7294869  2026-04-23 16:40   scenes/cdfbf2d9-fbd9-4e14-b2c9-a2ff8f6601f3.usd
  7440137  2026-04-23 16:40   scenes/cf496159-b747-4b04-ae6d-ed8317108bb5.usd
  4444275  2026-04-23 16:40   scenes/d0615bd5-c5af-474b-a2bf-c434fcfaf74c.usd
  5486497  2026-04-23 16:40   scenes/d6784049-e7e4-4a1e-818f-955c1c5bd871.usd
 12128341  2026-04-23 16:40   scenes/d6c3ddf7-9807-40d5-8523-4a2b871c2419.usd
  7292681  2026-04-23 16:40   scenes/d94ae128-dd50-42bc-9214-10a404f07b3f.usd
 12082217  2026-04-23 16:40   scenes/da9d58e5-d9bd-4d3e-8ac0-10e224cb505a.usd
  3916842  2026-04-23 16:40   scenes/e249a0e2-e0ef-4af4-81ab-945e6973e53f.usd
  6981685  2026-04-23 16:40   scenes/e68032b2-11be-476a-b4b3-cf9a601db316.usd
  8586747  2026-04-23 16:40   scenes/e8d819e4-bfb3-406e-a683-0ea452650633.usd
  7414336  2026-04-23 16:40   scenes/eb254b92-dba1-4c7a-91d8-dd32bc39d279.usd
  6628786  2026-04-23 16:40   scenes/ee4ca189-a9b5-4049-a0ee-9f78402ab039.usd
  2000013  2026-04-23 16:40   scenes/f98c8dff-7392-45b8-abf5-81c3ca5eb064.usd
  9777459  2026-04-23 16:40   scenes/ffa247bb-94fc-4f11-abb5-5681b09d1d81.usd
        0  2026-04-23 20:36   scenes/texture/
    42035  2026-04-23 20:36   scenes/texture/00221545-8e2c-4266-bb42-f08c4e8d2382.png
   290158  2026-04-23 20:36   scenes/texture/0033e020-460c-4990-a2d2-cfe223a2f5a0.png
   564040  2026-04-23 20:36   scenes/texture/003a85cc-1a58-4b93-8b5c-11ad960aded5.png
   901564  2026-04-23 20:36   scenes/texture/006a08bb-914c-49b9-93ed-4de256ae74c2.png
   907263  2026-04-23 20:36   scenes/texture/00acb313-c507-4372-addf-508755c6e98b.png
  1022837  2026-04-23 20:36   scenes/texture/0115036f-8abc-4cc5-99a3-d8607500d213.png
  1632744  2026-04-23 20:36   scenes/texture/0128706c-a595-405b-a9ce-47d89847bf28.png
    60690  2026-04-23 20:36   scenes/texture/013207f3-b388-4335-b2b1-a91dd49be349.png
   507511  2026-04-23 20:36   scenes/texture/0157cd98-fa1d-4009-b7d6-85fbc44a6eba.png
    17701  2026-04-23 20:36   scenes/texture/01dfc00c-638a-4890-8788-ccd35e567602.png
   538683  2026-04-23 20:36   scenes/texture/01fe3767-6f21-49cf-b8da-e16b53267dc8.png
   862753  2026-04-23 20:36   scenes/texture/0220bd66-882a-4f00-9009-f5788caeab72.png
  1281662  2026-04-23 20:36   scenes/texture/023dd6cc-ca41-4f4c-82f8-67737acd2675.png
   137304  2026-04-23 20:36   scenes/texture/026b3a27-85f5-4061-9991-7d6182ad8861.png
   789699  2026-04-23 20:36   scenes/texture/02c42ff4-8c7b-4eb1-97e2-b40ed18b02eb.png
   814852  2026-04-23 20:36   scenes/texture/02dabe94-29fe-4f44-a7b0-8d12b6281806.png
  2423403  2026-04-23 20:36   scenes/texture/0311b280-2ba9-47ff-a09a-af573deb74ab.png
    67171  2026-04-23 20:36   scenes/texture/033280d4-d766-4edf-b499-6c1c1c402c50.png
   837964  2026-04-23 20:36   scenes/texture/03375fab-55d8-48da-85dc-4d3876da4f67.png
   524248  2026-04-23 20:36   scenes/texture/0353b780-27c1-42eb-8544-212c32c1afb3.png
  1044235  2026-04-23 20:36   scenes/texture/04039de7-100a-4be6-b17e-1f7bd6fe37f7.png
  1152103  2026-04-23 20:36   scenes/texture/042badc0-128e-4abe-8ce8-5fe3e538b4fc.png
   597842  2026-04-23 20:36   scenes/texture/045d681b-c15f-4e25-b86d-9a759766af24.png
  1466103  2026-04-23 20:36   scenes/texture/04753da7-1d93-4857-8b7f-51c50fe95568.png
   310230  2026-04-23 20:36   scenes/texture/04b83a73-5a05-4a96-b25b-7f0160bec071.png
  1260308  2026-04-23 20:36   scenes/texture/04bb0dd5-b86a-42bf-93c9-b5710faa9e57.png
  1027283  2026-04-23 20:36   scenes/texture/04c083bf-1bde-4e6a-a707-ac890b6ce79e.png
   656681  2026-04-23 20:36   scenes/texture/04d7bef7-8628-48c5-a62f-3762e54f7914.png
   979519  2026-04-23 20:36   scenes/texture/04de61d6-79b0-42d9-9695-161b818317ce.png
    95598  2026-04-23 20:36   scenes/texture/05101287-941c-4442-af2e-0eef69f136b6.png
   987101  2026-04-23 20:36   scenes/texture/05291d86-5851-4077-b7a5-7ce7130e7306.png
   846688  2026-04-23 20:36   scenes/texture/055f37b8-af39-4baa-8c31-ea11a449be94.png
   986668  2026-04-23 20:36   scenes/texture/056dd1f4-327c-433b-bd62-5a160ef809b3.png
    47353  2026-04-23 20:36   scenes/texture/05940431-6b68-4a02-8d56-f4aa23e5d98b.png
  1064270  2026-04-23 20:36   scenes/texture/05ae8b65-0d7a-4563-82cb-15d17866d9d9.png
  1054874  2026-04-23 20:36   scenes/texture/05c2ba89-d3ef-47d9-b272-149712dd9b1e.png
  1584663  2026-04-23 20:36   scenes/texture/05d628ef-e510-4f6a-8862-ade7405dd3f4.png
   431431  2026-04-23 20:36   scenes/texture/05faf43b-c747-468c-a863-4a00b8761b9d.png
    58357  2026-04-23 20:36   scenes/texture/0629cbd0-8721-437d-a34a-952a9e2b2f5f.png
   971291  2026-04-23 20:36   scenes/texture/062d9bec-df16-4fd6-98ad-57ebc1b71753.png
   562720  2026-04-23 20:36   scenes/texture/06638f22-d2e9-4223-affc-9547dc4c633c.png
   520777  2026-04-23 20:36   scenes/texture/0672476a-38c2-4f15-a2d4-ff0a06caf9a6.png
   705153  2026-04-23 20:36   scenes/texture/068bc916-69aa-4153-ac1f-8cb0a00e4cde.png
   970989  2026-04-23 20:36   scenes/texture/06a02e7c-af9d-42b9-a112-b0c7357c1bd7.png
   680436  2026-04-23 20:36   scenes/texture/06a11496-dadc-469d-86ec-1c15fe15fa1e.png
  1232086  2026-04-23 20:36   scenes/texture/06bb1295-131b-471a-8e97-66251b0f79fd.png
   995865  2026-04-23 20:36   scenes/texture/06ccac96-3ca8-4bd0-aee2-64f1b495f485.png
    54248  2026-04-23 20:36   scenes/texture/06d5595f-679e-423c-b011-9619edaaac60.png
  1598658  2026-04-23 20:36   scenes/texture/06dfd96e-44c4-402b-896a-c895cd537929.png
    66281  2026-04-23 20:36   scenes/texture/06fa510a-de04-45f5-b54b-d1ddacc27a4b.png
  1148317  2026-04-23 20:36   scenes/texture/074ef4d4-cb22-4a0e-a611-3a579b9b21a2.png
   836563  2026-04-23 20:36   scenes/texture/07624dbf-6451-4973-bfce-3a343cb80f38.png
  1855171  2026-04-23 20:36   scenes/texture/079cca6e-c638-459b-9008-813b69145117.png
   725640  2026-04-23 20:36   scenes/texture/07ce940a-2a2a-4bfb-bc31-e23bc38f6ddf.png
   290813  2026-04-23 20:36   scenes/texture/07d9fb2b-9d82-4ced-a712-19071abd9f21.png
   955929  2026-04-23 20:36   scenes/texture/08011234-d5e0-4eb0-bd6b-bed34868ca89.png
   687520  2026-04-23 20:36   scenes/texture/08033850-ac78-475d-a588-54a9ae21d711.png
   838910  2026-04-23 20:36   scenes/texture/08389a32-693e-41f5-86ca-2fbe14d49a3b.png
   828595  2026-04-23 20:36   scenes/texture/0855306f-0728-4914-9245-9ab7fcac9478.png
   953902  2026-04-23 20:36   scenes/texture/087ab7ae-de84-47fd-b420-3dfa3ddd9bc4.png
   795319  2026-04-23 20:36   scenes/texture/0893af5b-1c13-4996-b1ad-78329f5c2fd2.png
   808096  2026-04-23 20:36   scenes/texture/08bd9700-ae85-4722-8a3c-bf394a31799f.png
   184874  2026-04-23 20:36   scenes/texture/0911a15e-85ba-450a-950f-d4251bae7aa1.png
   830524  2026-04-23 20:36   scenes/texture/094e1cb8-4a48-446e-a88c-ddee36aba955.png
   500916  2026-04-23 20:36   scenes/texture/094ed7df-1568-457a-aa01-478b98bc896a.png
   297155  2026-04-23 20:36   scenes/texture/097169f3-ed0c-4b51-8e6c-cfe70989a202.png
  1918791  2026-04-23 20:36   scenes/texture/09926e0a-8894-42f8-9662-58ff6a20a626.png
   276910  2026-04-23 20:36   scenes/texture/09abc58f-e1ae-4f8f-a7fa-136c6f8b3ebb.png
   943747  2026-04-23 20:36   scenes/texture/09d273b4-c8cc-4f51-8cec-68f8838d6bb0.png
   104126  2026-04-23 20:36   scenes/texture/09fdda8c-7df0-4af6-ac68-aee7cbead3fb.png
   933580  2026-04-23 20:36   scenes/texture/0a42986e-556c-4afa-9973-86f93de5fa76.png
   575706  2026-04-23 20:36   scenes/texture/0ad663fa-87da-47b0-a522-478bd75ed23d.png
  1543105  2026-04-23 20:36   scenes/texture/0ad6bfc2-37db-4427-8e3a-f61b6b402f41.png
  2680421  2026-04-23 20:36   scenes/texture/0ad968e0-8164-44f8-b033-83f117c59c1e.png
   891047  2026-04-23 20:36   scenes/texture/0b0946c0-3835-4207-978b-c5f93b8c6c71.png
   677405  2026-04-23 20:36   scenes/texture/0b233069-9e14-48d1-9c13-1c80311b8e24.png
   675988  2026-04-23 20:36   scenes/texture/0b36f29a-b271-4c3c-862e-f1168c5a5cad.png
  1359173  2026-04-23 20:36   scenes/texture/0b37c900-4ecc-42e5-9899-b71aef429431.png
   923865  2026-04-23 20:36   scenes/texture/0b8fd0fd-4f20-4d3a-bf70-e20f52b13c12.png
   947540  2026-04-23 20:36   scenes/texture/0bc089e6-ce36-45ae-9a4a-cf13f96c0d37.png
   847277  2026-04-23 20:36   scenes/texture/0bca869d-b715-4795-b911-9de38f642f22.png
  1227014  2026-04-23 20:36   scenes/texture/0c0c2842-496f-4679-9b8b-f28c0903e438.png
  1130502  2026-04-23 20:36   scenes/texture/0c2f5f5b-6ff7-4d35-bec3-39e6458c7c8c.png
   727863  2026-04-23 20:36   scenes/texture/0c5273c1-3bb5-4e1b-9145-03931ec12545.png
   438227  2026-04-23 20:36   scenes/texture/0c64b5e0-2f99-4c17-bd22-345131e20f72.png
  1127562  2026-04-23 20:36   scenes/texture/0c7c35ff-8fda-44f7-9e5a-cf75ed3e50fa.png
  1845505  2026-04-23 20:36   scenes/texture/0cac4c9c-ef2c-4a90-8944-6e94b5b8b757.png
   470968  2026-04-23 20:36   scenes/texture/0cd14fb8-c9bf-48be-99d3-ccdf38a7f017.png
   961554  2026-04-23 20:36   scenes/texture/0d1c2c39-5c57-4c75-b477-603123dc0b40.png
    70565  2026-04-23 20:36   scenes/texture/0d7421d4-2656-435b-9eb1-8884b4b3dcb3.png
  1440259  2026-04-23 20:36   scenes/texture/0d8ad8d3-d1d5-45b1-a7fc-71c3bc5eaaf1.png
   340830  2026-04-23 20:36   scenes/texture/0d9d29e3-9033-47f3-8b81-a37c278e6ac6.png
   612479  2026-04-23 20:36   scenes/texture/0dcad060-ffe6-4eae-893f-bd6932263950.png
  1137299  2026-04-23 20:36   scenes/texture/0ddbb652-14e3-4e01-8fd5-aae213910ac2.png
  1447608  2026-04-23 20:36   scenes/texture/0df8ebe6-1dc4-45d6-83fb-fd5150a54bf8.png
    52901  2026-04-23 20:36   scenes/texture/0e2091bc-7a97-46b6-98f0-d960a6903042.png
  1421385  2026-04-23 20:36   scenes/texture/0e29e910-61d9-4261-8942-a1728d211847.png
  1239054  2026-04-23 20:36   scenes/texture/0e2b963d-66ab-49e3-8cf0-f90fd919bce4.png
   462810  2026-04-23 20:36   scenes/texture/0e4c4d43-c3fe-4df6-80d1-01cad2dcac84.png
   909234  2026-04-23 20:36   scenes/texture/0e62bdf5-42b7-4d1e-8acf-791daba32178.png
   872158  2026-04-23 20:36   scenes/texture/0e90ef50-aced-4b4c-97b1-cd7ced5724f5.png
   584738  2026-04-23 20:36   scenes/texture/0ea10ffb-60a0-48d7-9c79-f272bfd5ac77.png
   272509  2026-04-23 20:36   scenes/texture/0ea8993b-3e43-49bd-8158-0163a20f1409.png
  1105486  2026-04-23 20:36   scenes/texture/0eb963f7-bc2e-460a-9018-b5ba97149980.png
  1459619  2026-04-23 20:36   scenes/texture/0ec63027-468c-4bf0-854b-5376b9a64856.png
   901588  2026-04-23 20:36   scenes/texture/0eda6797-989e-426e-8f96-4e1c6c85aff5.png
   561431  2026-04-23 20:36   scenes/texture/0f0f8391-056f-439a-8c68-d1c132cd672b.png
  3391239  2026-04-23 20:36   scenes/texture/0f1d9021-594f-4413-ba81-092ae228b4d8.png
   590666  2026-04-23 20:36   scenes/texture/0f2d04fd-dfbc-443e-87e8-4df92160cc45.png
    78886  2026-04-23 20:36   scenes/texture/0f78b360-17e1-4812-9710-6a53a486de16.png
   724099  2026-04-23 20:36   scenes/texture/0f95f670-3100-4cbd-85bd-e2d2167dd450.png
  2563344  2026-04-23 20:36   scenes/texture/0fa21aa5-d88f-428e-a603-16b1bc04692f.png
  1131600  2026-04-23 20:36   scenes/texture/0fb25207-a5bf-45cc-8b52-cce170f682da.png
  1255589  2026-04-23 20:36   scenes/texture/0fc7452c-650b-4ae1-9190-11949e669499.png
  1329466  2026-04-23 20:36   scenes/texture/0ff2235c-d954-4b07-935a-5e4dd2c583a2.png
   381063  2026-04-23 20:36   scenes/texture/102c7436-d583-4de3-bfd6-1409f3ab9f52.png
   249257  2026-04-23 20:36   scenes/texture/1064988b-1363-45f6-96c9-f429e47e510a.png
   324688  2026-04-23 20:36   scenes/texture/10821dd8-229a-480c-b6fd-68b4d7d20bc0.png
    66545  2026-04-23 20:36   scenes/texture/111226c4-e22a-4cea-9675-7d460a020ff3.png
   767992  2026-04-23 20:36   scenes/texture/1125b207-30eb-41f8-9164-05630e87f80d.png
  1161645  2026-04-23 20:36   scenes/texture/113b1fbf-cc94-48a2-b387-9d82c30442c6.png
   768910  2026-04-23 20:36   scenes/texture/11710d4f-b5a6-4f42-9149-e6d5c898bdf4.png
   950414  2026-04-23 20:36   scenes/texture/11789dc3-bcf2-4d2a-90aa-ecd0e9a55cf1.png
  1407910  2026-04-23 20:36   scenes/texture/1189d1b7-81f3-469c-8e1d-fe1db897ed04.png
   611173  2026-04-23 20:36   scenes/texture/11aeb77c-8486-43ca-8da0-e152841f2e75.png
   886255  2026-04-23 20:36   scenes/texture/11e48b3a-7f5a-4964-a56b-20b5313c1de8.png
   972194  2026-04-23 20:36   scenes/texture/122b69db-88d0-4927-ba01-15dc17194c78.png
  1283587  2026-04-23 20:36   scenes/texture/122e2399-d839-416b-b50a-4eedf8b98510.png
   639615  2026-04-23 20:36   scenes/texture/126908c4-e8aa-456b-b459-7b3b0527de6f.png
   624078  2026-04-23 20:36   scenes/texture/12c73c31-4b45-42c9-ab98-268efb9768af.png
   852001  2026-04-23 20:36   scenes/texture/12cdb4e6-4b67-4d54-aac9-a2813fcf0155.png
   968625  2026-04-23 20:36   scenes/texture/12d2f66e-5d6f-49c4-9285-82b85931e0f5.png
  1182626  2026-04-23 20:36   scenes/texture/12d840b9-5eba-41d8-976d-d93fd0ae8d85.png
   494588  2026-04-23 20:36   scenes/texture/13031c58-7951-4044-8bc8-9e47cb42742c.png
   999655  2026-04-23 20:36   scenes/texture/131f323a-5470-40fa-93ca-30f58ae7f001.png
   505807  2026-04-23 20:36   scenes/texture/13256e16-3b76-4fa3-ad28-3f476ad0e338.png
   603038  2026-04-23 20:36   scenes/texture/134b2e64-dd23-4cf8-9ff8-39f4b7de45c2.png
   883851  2026-04-23 20:36   scenes/texture/137b2dda-9f69-4e1a-a576-ea00e62ed75e.png
   347609  2026-04-23 20:36   scenes/texture/1456d6b1-e19f-485a-be95-a0f79ecf2051.png
  1460839  2026-04-23 20:36   scenes/texture/145d3f20-5dc7-4813-8421-c62c0b42b75e.png
   628650  2026-04-23 20:36   scenes/texture/14723db0-4389-45db-9420-f02b9d226c2a.png
   425678  2026-04-23 20:36   scenes/texture/14a8635b-e6ef-4561-88d9-6c21f09eda27.png
  2589546  2026-04-23 20:36   scenes/texture/15b01c22-d271-42e7-8596-d158310d1294.png
   761967  2026-04-23 20:36   scenes/texture/15da01af-9578-4043-880f-2ab9107ef76a.png
   183109  2026-04-23 20:36   scenes/texture/162e1aed-6e96-4503-ba3c-adfe8b07b429.png
   795382  2026-04-23 20:36   scenes/texture/1690e7fb-5340-429b-b3c8-0ab7c20455ae.png
   800187  2026-04-23 20:36   scenes/texture/16bee8d2-7d9f-48c7-9f2c-4b71c4d7081a.png
   877595  2026-04-23 20:36   scenes/texture/172f65bb-736d-47e5-8b8f-6ded1d701a44.png
   800081  2026-04-23 20:36   scenes/texture/1731bda3-d883-47fd-8224-3f0ef38e82e7.png
   211460  2026-04-23 20:36   scenes/texture/173eb984-a4e8-4907-9353-4ecc1977237f.png
  1113216  2026-04-23 20:36   scenes/texture/1791e0c9-15fc-4fa9-80df-e73332ed6ce0.png
   586446  2026-04-23 20:36   scenes/texture/17b89600-f089-4e90-bec6-799298457ed4.png
  1415766  2026-04-23 20:36   scenes/texture/181085d9-8598-45dd-8108-c9aa2f4bd2ee.png
   539554  2026-04-23 20:36   scenes/texture/1848ca4a-cfff-48e7-9d8f-092cbcce7a8d.png
  1982462  2026-04-23 20:36   scenes/texture/189c8998-ae86-4b0a-841d-d8fd6818f8e2.png
  1024561  2026-04-23 20:36   scenes/texture/19035101-21a1-4495-ae95-90d8d1ccd108.png
  1406760  2026-04-23 20:36   scenes/texture/1919418e-3329-4c71-85e4-b00c54aa2c7e.png
  1118949  2026-04-23 20:36   scenes/texture/192ac441-48b7-4559-bc02-7c532171b531.png
   607743  2026-04-23 20:36   scenes/texture/196b2b95-2b39-4fb1-8fd4-14b5a2ab5ff8.png
   926658  2026-04-23 20:36   scenes/texture/1978275c-8e55-49e4-aa8e-ba0c4800d40b.png
   446169  2026-04-23 20:36   scenes/texture/1a1c11a4-9c90-403c-b7cf-70ee73b58cdd.png
   104610  2026-04-23 20:36   scenes/texture/1a4af735-398a-483b-ad94-68baeb0517bd.png
   130203  2026-04-23 20:36   scenes/texture/1a55111c-d745-475c-b3fb-884f7bb102db.png
    99322  2026-04-23 20:36   scenes/texture/1a7259e3-969e-4eda-b2ea-1312c55965f4.png
   632831  2026-04-23 20:36   scenes/texture/1a9c2d94-d577-4246-9829-75e26ad1cfe3.png
  1430470  2026-04-23 20:36   scenes/texture/1abab334-35fc-4dec-a8fb-bbe6b46866ba.png
   633044  2026-04-23 20:36   scenes/texture/1af90188-a986-4823-ba28-98ea51939a60.png
   960797  2026-04-23 20:36   scenes/texture/1b30b6c7-b465-49d8-87e6-dd2314e53ad2.png
   864096  2026-04-23 20:36   scenes/texture/1b51dd12-0f5e-4d3d-bf6f-1e9e73dc14cb.png
   544177  2026-04-23 20:36   scenes/texture/1b55ec50-ccbe-491d-9b32-6a538b95b2f8.png
   925534  2026-04-23 20:36   scenes/texture/1b75a261-6622-41e6-8225-1a41e6a04050.png
  1092894  2026-04-23 20:36   scenes/texture/1b99f254-0d54-437f-a715-8d8351d99afa.png
   124132  2026-04-23 20:36   scenes/texture/1b9d62ed-554b-4542-b225-265338db3514.png
   712313  2026-04-23 20:36   scenes/texture/1bac3fe5-bd4c-415f-8944-e43b8ddfd219.png
   748396  2026-04-23 20:36   scenes/texture/1bc9f0a1-e74d-447a-a651-95a3dc301171.png
  1393981  2026-04-23 20:36   scenes/texture/1c0371f2-be63-4a4e-bbc5-14909fc06f7e.png
   420979  2026-04-23 20:36   scenes/texture/1c1c88dd-39bf-4a6b-9b46-e2699b3a98eb.png
  1268550  2026-04-23 20:36   scenes/texture/1c2a2b53-fed2-49f7-b0ae-f40028fd1c44.png
   659938  2026-04-23 20:36   scenes/texture/1c648cfd-6eca-4a84-af58-b62a3a4d173a.png
  1032958  2026-04-23 20:36   scenes/texture/1d24fd7b-4ed9-474e-8155-ce0d9def78b7.png
   256043  2026-04-23 20:36   scenes/texture/1d4497dc-d858-4ef9-a807-3fa7b10a23b7.png
   245254  2026-04-23 20:36   scenes/texture/1d920ba1-6a64-4834-b9f9-737fb7660bcc.png
  1116219  2026-04-23 20:36   scenes/texture/1da4d744-9c9c-4173-a98a-fa71b5ebd6d0.png
  1584612  2026-04-23 20:36   scenes/texture/1da59a58-7627-4954-9950-4b5dbace0186.png
  1210857  2026-04-23 20:36   scenes/texture/1daf21ae-dcd0-4c8c-b657-521574440b4e.png
   792004  2026-04-23 20:36   scenes/texture/1db58710-b23b-452f-a817-1e170fb12a08.png
   626484  2026-04-23 20:36   scenes/texture/1db692a8-a183-44dc-ab4d-dcba5e0f9369.png
  1113722  2026-04-23 20:36   scenes/texture/1e527594-16ee-4d5e-97b3-3aa6930d03f5.png
  1102799  2026-04-23 20:36   scenes/texture/1e66214b-4c7f-4ce7-9a37-c41dcd7eb98b.png
  1301964  2026-04-23 20:36   scenes/texture/1e81f176-e7fd-4580-8697-aeff753062fa.png
   965468  2026-04-23 20:36   scenes/texture/1e85357c-97cc-4d7a-9c76-1eb285807849.png
   859377  2026-04-23 20:36   scenes/texture/1ea4a9a2-e029-4cb1-9fcd-fb7a8f0edce5.png
   410739  2026-04-23 20:36   scenes/texture/1ea566c6-6d1f-4aaf-b2b3-d1c8301ef13d.png
  1069592  2026-04-23 20:36   scenes/texture/1ead30d0-b899-4318-b72e-9aedfaffe9f7.png
  1176518  2026-04-23 20:36   scenes/texture/1ecf937a-58e9-4516-b9c9-dfbf6535950c.png
   814918  2026-04-23 20:36   scenes/texture/1ef668a9-12e0-447b-9bbc-8ae484ba8c58.png
  1241437  2026-04-23 20:36   scenes/texture/1f286ffd-7bb7-47a3-b722-d2b30098782d.png
  1048565  2026-04-23 20:36   scenes/texture/1f44b15a-8c3d-409d-80f1-20dc77cb9778.png
  1212079  2026-04-23 20:36   scenes/texture/1f5410a5-1b98-4ccb-974c-7eb6be918d84.png
   887798  2026-04-23 20:36   scenes/texture/1f7889f6-3b63-4668-8f58-1a4917793c23.png
  1448891  2026-04-23 20:36   scenes/texture/1fabeadc-efd8-4b75-a865-3da667a63d6f.png
   204064  2026-04-23 20:36   scenes/texture/1fbe850a-8237-428a-86e0-c9a903c67364.png
  1432289  2026-04-23 20:36   scenes/texture/1ff04aec-2aa8-417a-a19b-6e5e6ae1bf1d.png
   866319  2026-04-23 20:36   scenes/texture/2046863b-b103-395e-bc9b-91cf5ad009c9.png
   636782  2026-04-23 20:36   scenes/texture/2054aeaa-9ba8-43e9-b88a-a571d7adbbaa.png
   112736  2026-04-23 20:36   scenes/texture/206f88c4-68b7-4ecf-ba15-8bf296209515.png
   130354  2026-04-23 20:36   scenes/texture/20b9a2fa-2146-4a2e-9652-86a64e415479.png
   782450  2026-04-23 20:36   scenes/texture/20e62a42-7efa-48cc-8afc-daa96a1b80f4.png
  1107575  2026-04-23 20:36   scenes/texture/20f171c7-21ae-4876-bb79-6ec3fabc2ade.png
   471185  2026-04-23 20:36   scenes/texture/210bbebc-d2f0-4334-877c-ceedf9e5cfa5.png
   682814  2026-04-23 20:36   scenes/texture/210e365e-f949-4075-a7c4-4a7cc43178bc.png
   939176  2026-04-23 20:36   scenes/texture/2138ef44-a995-43ae-a69e-89c68b79c10d.png
   128477  2026-04-23 20:36   scenes/texture/215f41e9-f851-40f1-b2a2-d9daacaae1b9.png
   779527  2026-04-23 20:36   scenes/texture/216f7336-4e3e-4665-940a-d33ca4afb0fd.png

## DOM-Test content counts
total_entries: 1558
usd_or_usda_count: 81
json_count: 90
test_envs_txt_count: 1

test-envs paths:
- test-envs.txt

USD sample:
- scenes/0106f9d2-5779-457b-9b8b-72942373d42e.usd
- scenes/0398338b-d4c2-42f0-a1c3-c43ce0f23f7c.usd
- scenes/04dcc229-3353-4d90-a058-080acbcc4d59.usd
- scenes/058205e1-6ec4-4342-a609-1ecce3551c3b.usd
- scenes/07da426f-2064-4f8a-bee2-a7d1e2741ec5.usd
- scenes/106438c4-a1de-4c81-9740-74c214025a50.usd
- scenes/10c73ad0-214c-4bf7-a4e8-1c154a77b7ed.usd
- scenes/14f8c7f2-d61d-4a6f-86a6-2086a2157bf4.usd
- scenes/1738bb5e-a0d6-4820-ad10-f3c4bf9533e9.usd
- scenes/191931a4-ae27-44eb-a639-d8ee3de85a0b.usd
- scenes/1a2853ed-7b80-419a-9707-7107959afeff.usd
- scenes/1a8dbd8d-0025-4373-8b94-ee9dd9fa7295.usd
- scenes/1cd0db41-bcd9-4af7-a0be-cce5de62cc35.usd
- scenes/1d076f8c-e01d-4a2e-96f9-7676001a0d8c.usd
- scenes/21465c7c-7ddc-4b9c-9c12-feebdbf9cd1e.usd
- scenes/2311eda9-dcda-45fb-89c3-0c068ed74b9c.usd
- scenes/2d728150-ecd3-4648-b584-68de8e9f9a89.usd
- scenes/2e4fd266-4688-4343-896d-61b28ad746f0.usd
- scenes/2f7b66ba-455d-4ee4-8212-3072b100e189.usd
- scenes/338025eb-9da6-4d7a-9226-269351c76269.usd
- scenes/36672c0e-419c-476e-83c0-5b04654d3690.usd
- scenes/38e3cf4a-a67b-42d8-b467-2d1a3e5407a8.usd
- scenes/3da510a3-8db8-425e-bd0c-99e5a12af2ca.usd
- scenes/427248f1-b9be-41b9-bca5-ae3277b73e47.usd
- scenes/42dac4e2-8940-4ea3-9039-030961b73776.usd
- scenes/42fa9f8e-56c4-4ac8-95ac-29452eb2726a.usd
- scenes/43f1271f-d362-49c1-9ebc-cf9f8c82ea81.usd
- scenes/45dddc0b-2505-4dcd-b07e-f0ff4e5c90d4.usd
- scenes/45fb7506-342f-4dc6-b2c3-2e041fe69faa.usd
- scenes/47664f37-b639-45fd-a436-20fa2ab72ec7.usd
- scenes/502565a4-cf3d-4679-9d4e-e75310597922.usd
- scenes/58064c7d-8e8b-4149-9b3a-672cf22d4733.usd
- scenes/5a5372e5-d820-434d-885d-710887b2b0ee.usd
- scenes/5a6650a5-b713-4d8f-9c82-5fc49a5f6ea3.usd
- scenes/5bb3120d-3ad7-4456-b332-5bc1d60dd53c.usd
- scenes/5e2a38d6-75b9-4f91-a688-a2f3141230bd.usd
- scenes/620d9fb6-afad-4c3d-8517-4386a0f8d3d6.usd
- scenes/6a8ad1d5-8c81-49bf-a752-fbe9448ff3b1.usd
- scenes/6e356720-39a8-4843-874d-a71efc4fb1ff.usd
- scenes/6ea55a54-e0ba-46be-be97-1453b19c010d.usd
- scenes/73579a31-0878-40be-a445-ce768de6ddae.usd
- scenes/73d4b873-78d5-47dc-a0b1-81d96baa7f4a.usd
- scenes/7f56f3b3-faf3-44bb-89bf-e4f300718ce5.usd
- scenes/862269d5-f301-4857-90ea-df3b2d848997.usd
- scenes/865efbe7-e24e-4080-9c8e-dc6c52180ea6.usd
- scenes/89cba9bf-de9b-44a3-90c4-cdfd777e3d95.usd
- scenes/8cd5b2fd-c93f-4c67-9d58-1618296bf571.usd
- scenes/90b7eea6-8bb6-48aa-9981-690ca4de4938.usd
- scenes/91efeb20-7892-46d5-8846-35a2c8773e73.usd
- scenes/92c1c4c2-73f3-4688-b0e8-493c94f7fbe4.usd
- scenes/9819d7d9-5d08-48aa-b496-45bb26b0f5a3.usd
- scenes/98d50a8c-8f9c-40c7-b306-2b282a3ade70.usd
- scenes/9956c823-3aa0-4ff9-bd56-64d7f27e7bd8.usd
- scenes/9f283b51-0327-43d5-9ec0-44d867530f4e.usd
- scenes/9fa47876-dc0b-4cb1-b5dc-93ca194b1d87.usd
- scenes/9faff3f5-2f29-4312-bf2f-712557fe9fe7.usd
- scenes/a9efa7e9-ca08-4e7b-84cb-a1cbe3a71211.usd
- scenes/aa2174af-a1ed-403f-b46d-bb44f315c181.usd
- scenes/ab48b02d-9678-4949-83fe-0af34dad0bde.usd
- scenes/aee07a67-c3a3-4382-955c-82bb53a70c36.usd
- scenes/b4551582-1fbb-4320-bac8-74655b3babd1.usd
- scenes/bba8c5f2-10f0-4917-b26b-82fb076a97b4.usd
- scenes/c1117917-ddde-4d13-86e0-d8306e0c655f.usd
- scenes/c1b3e945-cefc-4e73-89fc-099bb5352bac.usd
- scenes/c49b0591-97b2-45e7-b0fd-0ac5968240ac.usd
- scenes/c720579b-1608-48cc-8b29-79ad02aa2739.usd
- scenes/c99f6564-2c07-4733-86c5-7d1712c3deac.usd
- scenes/cdfbf2d9-fbd9-4e14-b2c9-a2ff8f6601f3.usd
- scenes/cf496159-b747-4b04-ae6d-ed8317108bb5.usd
- scenes/d0615bd5-c5af-474b-a2bf-c434fcfaf74c.usd
- scenes/d6784049-e7e4-4a1e-818f-955c1c5bd871.usd
- scenes/d6c3ddf7-9807-40d5-8523-4a2b871c2419.usd
- scenes/d94ae128-dd50-42bc-9214-10a404f07b3f.usd
- scenes/da9d58e5-d9bd-4d3e-8ac0-10e224cb505a.usd
- scenes/e249a0e2-e0ef-4af4-81ab-945e6973e53f.usd
- scenes/e68032b2-11be-476a-b4b3-cf9a601db316.usd
- scenes/e8d819e4-bfb3-406e-a683-0ea452650633.usd
- scenes/eb254b92-dba1-4c7a-91d8-dd32bc39d279.usd
- scenes/ee4ca189-a9b5-4049-a0ee-9f78402ab039.usd
- scenes/f98c8dff-7392-45b8-abf5-81c3ca5eb064.usd

JSON sample:
- tests/1-1_place_franka_apple13d_O02_01048988_09b0.json
- tests/1-1_place_franka_avocado05d_O02_01048620_1690.json
- tests/1-1_place_franka_beer07d_O02_01048625_91e1.json
- tests/1-1_place_franka_can13d_O02_01048658_e9a1.json
- tests/1-1_place_franka_cup03d_O02_01622004_d37b.json
- tests/1-1_place_franka_dbottle04d_O02_01049070_38b7.json
- tests/1-1_place_franka_egg04d_O02_01048656_a3f0.json
- tests/1-1_place_franka_lemon03d_O02_01621718_2818.json
- tests/1-1_place_franka_potato18d_O02_01049048_9fb2.json
- tests/1-1_place_franka_wbottle11d_O02_01049082_d8a4.json
- tests/1-2_place_franka_apple12d_O04_01150235_caaa.json
- tests/1-2_place_franka_avocado06d_O03_01050247_9766.json
- tests/1-2_place_franka_beer07d_O04_01150287_1270.json
- tests/1-2_place_franka_egg13d_O02_01049028_9e3d.json
- tests/1-2_place_franka_fcan04d_O05_01250045_e0a8.json
- tests/1-2_place_franka_lemon03d_O03_01050300_20ba.json
- tests/1-2_place_franka_orange12d_O04_01150190_df9e.json
- tests/1-2_place_franka_peach02d_O03_01050238_9c43.json
- tests/1-2_place_franka_potato17d_O04_01150021_c37f.json
- tests/1-2_place_franka_tangerine06d_O03_01050375_2503.json
- tests/1-3_long-horizon_franka_apple19d_O03_01051606_af73.json
- tests/1-3_long-horizon_franka_avocado05d_O04_01051722_1abe.json
- tests/1-3_long-horizon_franka_egg04d_O04_01060705_f5f0.json
- tests/1-3_long-horizon_franka_fcan03d_O03_01051534_43f0.json
- tests/1-3_long-horizon_franka_fcan11d_O03_01060604_0679.json
- tests/1-3_long-horizon_franka_kiwi05d_O04_01051742_a2d5.json
- tests/1-3_long-horizon_franka_lemon06d_O03_01060576_5305.json
- tests/1-3_long-horizon_franka_lemon06d_O04_01051735_6ace.json
- tests/1-3_long-horizon_franka_lime02d_O03_01051568_4973.json
- tests/1-3_long-horizon_franka_tomato03d_O04_01051726_3e60.json
- tests/2-1_place_franka_avocado01d_O03_01050191_8482.json
- tests/2-1_place_franka_beer09d_O03_01150509_472f.json
- tests/2-1_place_franka_can11d_O05_01250064_1b1f.json
- tests/2-1_place_franka_cup03d_O03_01050304_5362.json
- tests/2-1_place_franka_dbottle02d_O03_01050315_2e40.json
- tests/2-1_place_franka_fcan11d_O03_01050130_dc3e.json
- tests/2-1_place_franka_lemon04d_O03_01150557_bdac.json
- tests/2-1_place_franka_orange03d_O05_01250241_af42.json
- tests/2-1_place_franka_peach01d_O03_01050401_66e6.json
- tests/2-1_place_franka_wbottle12d_O03_01150548_418c.json
- tests/2-2_place_franka_apple08d_O03_01050789_b41d.json
- tests/2-2_place_franka_can12d_O03_01050529_5ba6.json
- tests/2-2_place_franka_cup02d_O03_01050695_f467.json
- tests/2-2_place_franka_egg00d_O03_01250873_b050.json
- tests/2-2_place_franka_fcan04d_O03_01050627_1701.json
- tests/2-2_place_franka_kiwi00d_O04_01625759_b82c.json
- tests/2-2_place_franka_lemon14d_O03_01250807_bea5.json
- tests/2-2_place_franka_orange09d_O03_01250680_6e99.json
- tests/2-2_place_franka_potato02d_O04_01624132_ad86.json
- tests/2-2_place_franka_tangerine00d_O04_01626714_9924.json
- tests/2-3_place_franka_apple20d_O03_01050837_f264.json
- tests/2-3_place_franka_can13d_O03_01250594_6053.json
- tests/2-3_place_franka_cup02d_O03_01050695_f467.json
- tests/2-3_place_franka_egg07d_O03_01250883_c3cf.json
- tests/2-3_place_franka_fcan17d_O03_01250504_6336.json
- tests/2-3_place_franka_kiwi00d_O04_01625057_98b5.json
- tests/2-3_place_franka_lemon15d_O03_01250782_dee9.json
- tests/2-3_place_franka_orange09d_O03_01250729_3add.json
- tests/2-3_place_franka_peach01d_O04_01623186_ebff.json
- tests/2-3_place_franka_tangerine05d_O04_01626203_bc6c.json
- tests/3-1_place_franka_apple99d_O02_01610325_2a43.json
- tests/3-1_place_franka_apple99d_O02_01610841_d1f1.json
- tests/3-1_place_franka_can99d_O02_01080044_571c.json
- tests/3-1_place_franka_can99d_O02_01610785_5f89.json
- tests/3-1_place_franka_cup99d_O02_01610039_9412.json
- tests/3-1_place_franka_cup99d_O02_01610356_a52b.json
- tests/3-1_place_franka_dbottle99d_O02_01610074_1745.json
- tests/3-1_place_franka_dbottle99d_O02_01611366_b510.json
- tests/3-1_place_franka_peach99d_O02_01610119_2f43.json
- tests/3-1_place_franka_peach99d_O02_01610473_4c0d.json
- tests/3-2_place_franka_apple00d_O02_01641303_47a0.json
- tests/3-2_place_franka_avocado08d_O02_01641061_076c.json
- tests/3-2_place_franka_beer05d_O02_01641571_0bce.json
- tests/3-2_place_franka_can00d_O02_01641329_c06f.json
- tests/3-2_place_franka_cup04d_O02_01630239_6853.json
- tests/3-2_place_franka_egg13d_O02_01641323_e5d6.json
- tests/3-2_place_franka_fcan04d_O02_01641409_e758.json
- tests/3-2_place_franka_kiwi07d_O02_01630549_eac1.json
- tests/3-2_place_franka_lemon02d_O02_01641197_3c18.json
- tests/3-2_place_franka_orange13d_O02_01186003_bbfe.json

# DOM-TEST CONTENT VERDICT
contains_scene_usd: YES
contains_test_json: YES
contains_test_envs_txt: YES
contains_textures: YES
ready_to_extract_dom_test: YES
recommended_next_step: extract DOM-Test; it appears to include tests and scenes
Extracting DOM-Test into /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test
Archive:  /home/redafrix/isaac_franka_env_probe/downloads/DOM-Test.zip
   creating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/0106f9d2-5779-457b-9b8b-72942373d42e.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/0398338b-d4c2-42f0-a1c3-c43ce0f23f7c.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/04dcc229-3353-4d90-a058-080acbcc4d59.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/058205e1-6ec4-4342-a609-1ecce3551c3b.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/07da426f-2064-4f8a-bee2-a7d1e2741ec5.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/106438c4-a1de-4c81-9740-74c214025a50.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/10c73ad0-214c-4bf7-a4e8-1c154a77b7ed.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/14f8c7f2-d61d-4a6f-86a6-2086a2157bf4.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/1738bb5e-a0d6-4820-ad10-f3c4bf9533e9.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/191931a4-ae27-44eb-a639-d8ee3de85a0b.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/1a2853ed-7b80-419a-9707-7107959afeff.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/1a8dbd8d-0025-4373-8b94-ee9dd9fa7295.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/1cd0db41-bcd9-4af7-a0be-cce5de62cc35.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/1d076f8c-e01d-4a2e-96f9-7676001a0d8c.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/21465c7c-7ddc-4b9c-9c12-feebdbf9cd1e.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/2311eda9-dcda-45fb-89c3-0c068ed74b9c.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/2d728150-ecd3-4648-b584-68de8e9f9a89.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/2e4fd266-4688-4343-896d-61b28ad746f0.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/2f7b66ba-455d-4ee4-8212-3072b100e189.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/338025eb-9da6-4d7a-9226-269351c76269.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/36672c0e-419c-476e-83c0-5b04654d3690.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/38e3cf4a-a67b-42d8-b467-2d1a3e5407a8.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/3da510a3-8db8-425e-bd0c-99e5a12af2ca.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/427248f1-b9be-41b9-bca5-ae3277b73e47.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/42dac4e2-8940-4ea3-9039-030961b73776.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/42fa9f8e-56c4-4ac8-95ac-29452eb2726a.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/43f1271f-d362-49c1-9ebc-cf9f8c82ea81.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/45dddc0b-2505-4dcd-b07e-f0ff4e5c90d4.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/45fb7506-342f-4dc6-b2c3-2e041fe69faa.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/47664f37-b639-45fd-a436-20fa2ab72ec7.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/502565a4-cf3d-4679-9d4e-e75310597922.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/58064c7d-8e8b-4149-9b3a-672cf22d4733.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/5a5372e5-d820-434d-885d-710887b2b0ee.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/5a6650a5-b713-4d8f-9c82-5fc49a5f6ea3.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/5bb3120d-3ad7-4456-b332-5bc1d60dd53c.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/5e2a38d6-75b9-4f91-a688-a2f3141230bd.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/620d9fb6-afad-4c3d-8517-4386a0f8d3d6.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/6a8ad1d5-8c81-49bf-a752-fbe9448ff3b1.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/6e356720-39a8-4843-874d-a71efc4fb1ff.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/6ea55a54-e0ba-46be-be97-1453b19c010d.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/73579a31-0878-40be-a445-ce768de6ddae.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/73d4b873-78d5-47dc-a0b1-81d96baa7f4a.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/7f56f3b3-faf3-44bb-89bf-e4f300718ce5.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/862269d5-f301-4857-90ea-df3b2d848997.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/865efbe7-e24e-4080-9c8e-dc6c52180ea6.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/89cba9bf-de9b-44a3-90c4-cdfd777e3d95.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/8cd5b2fd-c93f-4c67-9d58-1618296bf571.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/90b7eea6-8bb6-48aa-9981-690ca4de4938.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/91efeb20-7892-46d5-8846-35a2c8773e73.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/92c1c4c2-73f3-4688-b0e8-493c94f7fbe4.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/9819d7d9-5d08-48aa-b496-45bb26b0f5a3.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/98d50a8c-8f9c-40c7-b306-2b282a3ade70.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/9956c823-3aa0-4ff9-bd56-64d7f27e7bd8.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/9f283b51-0327-43d5-9ec0-44d867530f4e.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/9fa47876-dc0b-4cb1-b5dc-93ca194b1d87.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/9faff3f5-2f29-4312-bf2f-712557fe9fe7.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/a9efa7e9-ca08-4e7b-84cb-a1cbe3a71211.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/aa2174af-a1ed-403f-b46d-bb44f315c181.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/ab48b02d-9678-4949-83fe-0af34dad0bde.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/aee07a67-c3a3-4382-955c-82bb53a70c36.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/b4551582-1fbb-4320-bac8-74655b3babd1.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/bba8c5f2-10f0-4917-b26b-82fb076a97b4.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/c1117917-ddde-4d13-86e0-d8306e0c655f.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/c1b3e945-cefc-4e73-89fc-099bb5352bac.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/c49b0591-97b2-45e7-b0fd-0ac5968240ac.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/c720579b-1608-48cc-8b29-79ad02aa2739.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/c99f6564-2c07-4733-86c5-7d1712c3deac.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/cdfbf2d9-fbd9-4e14-b2c9-a2ff8f6601f3.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/cf496159-b747-4b04-ae6d-ed8317108bb5.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/d0615bd5-c5af-474b-a2bf-c434fcfaf74c.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/d6784049-e7e4-4a1e-818f-955c1c5bd871.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/d6c3ddf7-9807-40d5-8523-4a2b871c2419.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/d94ae128-dd50-42bc-9214-10a404f07b3f.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/da9d58e5-d9bd-4d3e-8ac0-10e224cb505a.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/e249a0e2-e0ef-4af4-81ab-945e6973e53f.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/e68032b2-11be-476a-b4b3-cf9a601db316.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/e8d819e4-bfb3-406e-a683-0ea452650633.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/eb254b92-dba1-4c7a-91d8-dd32bc39d279.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/ee4ca189-a9b5-4049-a0ee-9f78402ab039.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/f98c8dff-7392-45b8-abf5-81c3ca5eb064.usd  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/ffa247bb-94fc-4f11-abb5-5681b09d1d81.usd  
   creating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/00221545-8e2c-4266-bb42-f08c4e8d2382.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0033e020-460c-4990-a2d2-cfe223a2f5a0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/003a85cc-1a58-4b93-8b5c-11ad960aded5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/006a08bb-914c-49b9-93ed-4de256ae74c2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/00acb313-c507-4372-addf-508755c6e98b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0115036f-8abc-4cc5-99a3-d8607500d213.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0128706c-a595-405b-a9ce-47d89847bf28.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/013207f3-b388-4335-b2b1-a91dd49be349.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0157cd98-fa1d-4009-b7d6-85fbc44a6eba.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/01dfc00c-638a-4890-8788-ccd35e567602.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/01fe3767-6f21-49cf-b8da-e16b53267dc8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0220bd66-882a-4f00-9009-f5788caeab72.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/023dd6cc-ca41-4f4c-82f8-67737acd2675.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/026b3a27-85f5-4061-9991-7d6182ad8861.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/02c42ff4-8c7b-4eb1-97e2-b40ed18b02eb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/02dabe94-29fe-4f44-a7b0-8d12b6281806.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0311b280-2ba9-47ff-a09a-af573deb74ab.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/033280d4-d766-4edf-b499-6c1c1c402c50.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/03375fab-55d8-48da-85dc-4d3876da4f67.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0353b780-27c1-42eb-8544-212c32c1afb3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/04039de7-100a-4be6-b17e-1f7bd6fe37f7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/042badc0-128e-4abe-8ce8-5fe3e538b4fc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/045d681b-c15f-4e25-b86d-9a759766af24.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/04753da7-1d93-4857-8b7f-51c50fe95568.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/04b83a73-5a05-4a96-b25b-7f0160bec071.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/04bb0dd5-b86a-42bf-93c9-b5710faa9e57.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/04c083bf-1bde-4e6a-a707-ac890b6ce79e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/04d7bef7-8628-48c5-a62f-3762e54f7914.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/04de61d6-79b0-42d9-9695-161b818317ce.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/05101287-941c-4442-af2e-0eef69f136b6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/05291d86-5851-4077-b7a5-7ce7130e7306.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/055f37b8-af39-4baa-8c31-ea11a449be94.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/056dd1f4-327c-433b-bd62-5a160ef809b3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/05940431-6b68-4a02-8d56-f4aa23e5d98b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/05ae8b65-0d7a-4563-82cb-15d17866d9d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/05c2ba89-d3ef-47d9-b272-149712dd9b1e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/05d628ef-e510-4f6a-8862-ade7405dd3f4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/05faf43b-c747-468c-a863-4a00b8761b9d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0629cbd0-8721-437d-a34a-952a9e2b2f5f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/062d9bec-df16-4fd6-98ad-57ebc1b71753.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/06638f22-d2e9-4223-affc-9547dc4c633c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0672476a-38c2-4f15-a2d4-ff0a06caf9a6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/068bc916-69aa-4153-ac1f-8cb0a00e4cde.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/06a02e7c-af9d-42b9-a112-b0c7357c1bd7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/06a11496-dadc-469d-86ec-1c15fe15fa1e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/06bb1295-131b-471a-8e97-66251b0f79fd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/06ccac96-3ca8-4bd0-aee2-64f1b495f485.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/06d5595f-679e-423c-b011-9619edaaac60.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/06dfd96e-44c4-402b-896a-c895cd537929.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/06fa510a-de04-45f5-b54b-d1ddacc27a4b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/074ef4d4-cb22-4a0e-a611-3a579b9b21a2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/07624dbf-6451-4973-bfce-3a343cb80f38.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/079cca6e-c638-459b-9008-813b69145117.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/07ce940a-2a2a-4bfb-bc31-e23bc38f6ddf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/07d9fb2b-9d82-4ced-a712-19071abd9f21.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/08011234-d5e0-4eb0-bd6b-bed34868ca89.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/08033850-ac78-475d-a588-54a9ae21d711.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/08389a32-693e-41f5-86ca-2fbe14d49a3b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0855306f-0728-4914-9245-9ab7fcac9478.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/087ab7ae-de84-47fd-b420-3dfa3ddd9bc4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0893af5b-1c13-4996-b1ad-78329f5c2fd2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/08bd9700-ae85-4722-8a3c-bf394a31799f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0911a15e-85ba-450a-950f-d4251bae7aa1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/094e1cb8-4a48-446e-a88c-ddee36aba955.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/094ed7df-1568-457a-aa01-478b98bc896a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/097169f3-ed0c-4b51-8e6c-cfe70989a202.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/09926e0a-8894-42f8-9662-58ff6a20a626.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/09abc58f-e1ae-4f8f-a7fa-136c6f8b3ebb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/09d273b4-c8cc-4f51-8cec-68f8838d6bb0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/09fdda8c-7df0-4af6-ac68-aee7cbead3fb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0a42986e-556c-4afa-9973-86f93de5fa76.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0ad663fa-87da-47b0-a522-478bd75ed23d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0ad6bfc2-37db-4427-8e3a-f61b6b402f41.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0ad968e0-8164-44f8-b033-83f117c59c1e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0b0946c0-3835-4207-978b-c5f93b8c6c71.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0b233069-9e14-48d1-9c13-1c80311b8e24.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0b36f29a-b271-4c3c-862e-f1168c5a5cad.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0b37c900-4ecc-42e5-9899-b71aef429431.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0b8fd0fd-4f20-4d3a-bf70-e20f52b13c12.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0bc089e6-ce36-45ae-9a4a-cf13f96c0d37.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0bca869d-b715-4795-b911-9de38f642f22.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0c0c2842-496f-4679-9b8b-f28c0903e438.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0c2f5f5b-6ff7-4d35-bec3-39e6458c7c8c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0c5273c1-3bb5-4e1b-9145-03931ec12545.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0c64b5e0-2f99-4c17-bd22-345131e20f72.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0c7c35ff-8fda-44f7-9e5a-cf75ed3e50fa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0cac4c9c-ef2c-4a90-8944-6e94b5b8b757.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0cd14fb8-c9bf-48be-99d3-ccdf38a7f017.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0d1c2c39-5c57-4c75-b477-603123dc0b40.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0d7421d4-2656-435b-9eb1-8884b4b3dcb3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0d8ad8d3-d1d5-45b1-a7fc-71c3bc5eaaf1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0d9d29e3-9033-47f3-8b81-a37c278e6ac6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0dcad060-ffe6-4eae-893f-bd6932263950.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0ddbb652-14e3-4e01-8fd5-aae213910ac2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0df8ebe6-1dc4-45d6-83fb-fd5150a54bf8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0e2091bc-7a97-46b6-98f0-d960a6903042.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0e29e910-61d9-4261-8942-a1728d211847.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0e2b963d-66ab-49e3-8cf0-f90fd919bce4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0e4c4d43-c3fe-4df6-80d1-01cad2dcac84.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0e62bdf5-42b7-4d1e-8acf-791daba32178.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0e90ef50-aced-4b4c-97b1-cd7ced5724f5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0ea10ffb-60a0-48d7-9c79-f272bfd5ac77.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0ea8993b-3e43-49bd-8158-0163a20f1409.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0eb963f7-bc2e-460a-9018-b5ba97149980.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0ec63027-468c-4bf0-854b-5376b9a64856.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0eda6797-989e-426e-8f96-4e1c6c85aff5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0f0f8391-056f-439a-8c68-d1c132cd672b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0f1d9021-594f-4413-ba81-092ae228b4d8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0f2d04fd-dfbc-443e-87e8-4df92160cc45.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0f78b360-17e1-4812-9710-6a53a486de16.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0f95f670-3100-4cbd-85bd-e2d2167dd450.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0fa21aa5-d88f-428e-a603-16b1bc04692f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0fb25207-a5bf-45cc-8b52-cce170f682da.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0fc7452c-650b-4ae1-9190-11949e669499.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/0ff2235c-d954-4b07-935a-5e4dd2c583a2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/102c7436-d583-4de3-bfd6-1409f3ab9f52.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1064988b-1363-45f6-96c9-f429e47e510a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/10821dd8-229a-480c-b6fd-68b4d7d20bc0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/111226c4-e22a-4cea-9675-7d460a020ff3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1125b207-30eb-41f8-9164-05630e87f80d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/113b1fbf-cc94-48a2-b387-9d82c30442c6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/11710d4f-b5a6-4f42-9149-e6d5c898bdf4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/11789dc3-bcf2-4d2a-90aa-ecd0e9a55cf1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1189d1b7-81f3-469c-8e1d-fe1db897ed04.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/11aeb77c-8486-43ca-8da0-e152841f2e75.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/11e48b3a-7f5a-4964-a56b-20b5313c1de8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/122b69db-88d0-4927-ba01-15dc17194c78.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/122e2399-d839-416b-b50a-4eedf8b98510.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/126908c4-e8aa-456b-b459-7b3b0527de6f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/12c73c31-4b45-42c9-ab98-268efb9768af.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/12cdb4e6-4b67-4d54-aac9-a2813fcf0155.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/12d2f66e-5d6f-49c4-9285-82b85931e0f5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/12d840b9-5eba-41d8-976d-d93fd0ae8d85.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/13031c58-7951-4044-8bc8-9e47cb42742c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/131f323a-5470-40fa-93ca-30f58ae7f001.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/13256e16-3b76-4fa3-ad28-3f476ad0e338.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/134b2e64-dd23-4cf8-9ff8-39f4b7de45c2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/137b2dda-9f69-4e1a-a576-ea00e62ed75e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1456d6b1-e19f-485a-be95-a0f79ecf2051.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/145d3f20-5dc7-4813-8421-c62c0b42b75e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/14723db0-4389-45db-9420-f02b9d226c2a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/14a8635b-e6ef-4561-88d9-6c21f09eda27.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/15b01c22-d271-42e7-8596-d158310d1294.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/15da01af-9578-4043-880f-2ab9107ef76a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/162e1aed-6e96-4503-ba3c-adfe8b07b429.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1690e7fb-5340-429b-b3c8-0ab7c20455ae.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/16bee8d2-7d9f-48c7-9f2c-4b71c4d7081a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/172f65bb-736d-47e5-8b8f-6ded1d701a44.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1731bda3-d883-47fd-8224-3f0ef38e82e7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/173eb984-a4e8-4907-9353-4ecc1977237f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1791e0c9-15fc-4fa9-80df-e73332ed6ce0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/17b89600-f089-4e90-bec6-799298457ed4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/181085d9-8598-45dd-8108-c9aa2f4bd2ee.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1848ca4a-cfff-48e7-9d8f-092cbcce7a8d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/189c8998-ae86-4b0a-841d-d8fd6818f8e2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/19035101-21a1-4495-ae95-90d8d1ccd108.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1919418e-3329-4c71-85e4-b00c54aa2c7e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/192ac441-48b7-4559-bc02-7c532171b531.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/196b2b95-2b39-4fb1-8fd4-14b5a2ab5ff8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1978275c-8e55-49e4-aa8e-ba0c4800d40b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1a1c11a4-9c90-403c-b7cf-70ee73b58cdd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1a4af735-398a-483b-ad94-68baeb0517bd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1a55111c-d745-475c-b3fb-884f7bb102db.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1a7259e3-969e-4eda-b2ea-1312c55965f4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1a9c2d94-d577-4246-9829-75e26ad1cfe3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1abab334-35fc-4dec-a8fb-bbe6b46866ba.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1af90188-a986-4823-ba28-98ea51939a60.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1b30b6c7-b465-49d8-87e6-dd2314e53ad2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1b51dd12-0f5e-4d3d-bf6f-1e9e73dc14cb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1b55ec50-ccbe-491d-9b32-6a538b95b2f8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1b75a261-6622-41e6-8225-1a41e6a04050.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1b99f254-0d54-437f-a715-8d8351d99afa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1b9d62ed-554b-4542-b225-265338db3514.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1bac3fe5-bd4c-415f-8944-e43b8ddfd219.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1bc9f0a1-e74d-447a-a651-95a3dc301171.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1c0371f2-be63-4a4e-bbc5-14909fc06f7e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1c1c88dd-39bf-4a6b-9b46-e2699b3a98eb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1c2a2b53-fed2-49f7-b0ae-f40028fd1c44.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1c648cfd-6eca-4a84-af58-b62a3a4d173a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1d24fd7b-4ed9-474e-8155-ce0d9def78b7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1d4497dc-d858-4ef9-a807-3fa7b10a23b7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1d920ba1-6a64-4834-b9f9-737fb7660bcc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1da4d744-9c9c-4173-a98a-fa71b5ebd6d0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1da59a58-7627-4954-9950-4b5dbace0186.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1daf21ae-dcd0-4c8c-b657-521574440b4e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1db58710-b23b-452f-a817-1e170fb12a08.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1db692a8-a183-44dc-ab4d-dcba5e0f9369.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1e527594-16ee-4d5e-97b3-3aa6930d03f5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1e66214b-4c7f-4ce7-9a37-c41dcd7eb98b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1e81f176-e7fd-4580-8697-aeff753062fa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1e85357c-97cc-4d7a-9c76-1eb285807849.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1ea4a9a2-e029-4cb1-9fcd-fb7a8f0edce5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1ea566c6-6d1f-4aaf-b2b3-d1c8301ef13d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1ead30d0-b899-4318-b72e-9aedfaffe9f7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1ecf937a-58e9-4516-b9c9-dfbf6535950c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1ef668a9-12e0-447b-9bbc-8ae484ba8c58.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1f286ffd-7bb7-47a3-b722-d2b30098782d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1f44b15a-8c3d-409d-80f1-20dc77cb9778.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1f5410a5-1b98-4ccb-974c-7eb6be918d84.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1f7889f6-3b63-4668-8f58-1a4917793c23.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1fabeadc-efd8-4b75-a865-3da667a63d6f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1fbe850a-8237-428a-86e0-c9a903c67364.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/1ff04aec-2aa8-417a-a19b-6e5e6ae1bf1d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2046863b-b103-395e-bc9b-91cf5ad009c9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2054aeaa-9ba8-43e9-b88a-a571d7adbbaa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/206f88c4-68b7-4ecf-ba15-8bf296209515.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/20b9a2fa-2146-4a2e-9652-86a64e415479.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/20e62a42-7efa-48cc-8afc-daa96a1b80f4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/20f171c7-21ae-4876-bb79-6ec3fabc2ade.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/210bbebc-d2f0-4334-877c-ceedf9e5cfa5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/210e365e-f949-4075-a7c4-4a7cc43178bc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2138ef44-a995-43ae-a69e-89c68b79c10d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/215f41e9-f851-40f1-b2a2-d9daacaae1b9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/216f7336-4e3e-4665-940a-d33ca4afb0fd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/21f34649-749e-4481-aef4-abf73263c950.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2220bef3-61ba-42d6-881e-2f3df67f83a3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/22280199-72eb-48d7-bbd0-1760bf6a94c7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2250c149-cae7-47b1-b2f6-061f171b3198.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/226446d4-031a-469f-8c9d-6a635847bb5d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/226745c3-3118-4501-b90c-8f7f8a89331a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/229a9614-f7bd-4e78-ae14-5b36c827cf88.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/22a234bc-ae89-42ea-b091-847019bea405.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/22b5726c-451b-42e6-8825-b90cd1cdbc35.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/22c239f7-1cd5-4e8d-a792-9a6d6bad3bf0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/22da2ff5-6dd3-4c99-b179-b075a35eb3eb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/235b23eb-1a3b-4545-bb44-a549b45e13cf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2364f982-e6ae-4752-bd43-d683b666975b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/237836b2-7d7d-4469-9672-dff828358828.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/238c3d4e-2c08-4d8d-82c4-b06326568e27.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/240750b2-2a9f-4eb8-b61f-40505cd8936a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2439e21f-2c7d-4fea-ad39-d21539945f13.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/245bf1c1-0c77-4285-b511-cf1599ba7c80.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/248774ec-da30-4b29-a9c8-1aa5668ec462.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/24ae86f8-6a16-49a3-b0e9-f35bfe9dfb3f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/24bc76e9-7b52-48ea-92d5-e7cf72b9cf43.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/24e0fbde-6fb9-4312-8e48-2b01531e46c2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/24e81447-5e7a-4d34-8c36-562ccac837f7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2502cec2-3444-4046-b2c8-8afda329d115.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/250acddd-7d4d-4f22-8fb6-603ac07c8c39.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/252c2950-6bad-4bf7-a557-76b1a08f7394.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/25606e3d-1684-42f6-95d2-d0b7f0cdba5a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/25d25b90-1efe-4b21-918d-fa7a4b3844c9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/26098b5a-1e15-4c51-9312-cb6b4d83015d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/260eb3ca-ddb5-43b5-b2ed-3dd8e4c51e61.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2622fde2-c4aa-4863-89b9-77673b524b62.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/26514721-8967-4ae2-ab37-b70bfede2873.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/269b409e-c8bb-4737-8546-0a47ae202cf0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/26afb29f-d893-44dc-b311-53fdf34cf832.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/26ceb30c-01a5-448f-9714-85759b08abd4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/26d34ba7-1d4b-48c9-a7f2-05032289870d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/26ec6b73-48a6-441c-b005-61a2fba2e4eb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/26fed367-1189-49af-ae0c-e218cdf80bf0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/27195304-e542-4ad0-90e8-69c9eb662834.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/27498740-3ec5-425a-aaa3-9f4703765e5f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/277ccdab-ecc1-4e27-bb04-e971e7d538c7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/27a67254-913a-43b1-8292-ca73c8998f91.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/27fa631e-8f81-4712-9f20-2e2eac0b1168.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/280daff8-2fa7-4043-a7ea-b56785a535c3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28449ed2-369d-4733-8419-4d64b0d5a05d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/286d18bd-dfd1-4713-ba8c-9bb470c06e8e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28746bea-d522-4135-bef3-14fadc523f40.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/288ac6f4-47ef-418d-87d0-6cc1365a98f4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28a8fde0-22ef-4175-9370-12ba922348aa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28b7ed8a-0382-4fe5-82fe-8fbfd34a9c08.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28ca9bd1-e10a-4c41-a580-9654e8a6d06b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28d2dfc7-6f31-4eae-9a5c-ea61533004ee.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28d3a35a-0ccd-42a8-9052-24322cd7b8ed.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28db412b-c62b-4c83-ae16-c0ce86d93491.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28dd3ca2-3e58-38ef-980d-0f2f7a795cc3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28ef3e6f-d5b0-4354-804b-b84cdaf687f8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/28f855f2-fadb-4d8d-917c-44d90ce964bb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2913731c-740b-4f22-adb2-c94660c4189e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2924c470-d123-48de-bbc4-af3ec50872ff.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2946a5e8-d81d-4768-ae28-f27ba8886410.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/297e7696-b4ee-4db7-85a2-6f8e6a7ce75c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/297ecba4-d2a9-408f-b52b-fa6277611011.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/29a5968a-f8d6-46e0-a700-c3d24470597a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/29ed0e9c-02ae-4404-a8dd-f6f178dc79b4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2a7fd249-5ac6-4e46-a12f-dce1cdefd840.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2ac26da2-fa72-4e83-8c1c-542792d997c0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2ac67c87-c768-470d-91d6-cc018259f6fc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2adca377-c11f-41f1-a27c-20d1b622d329.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2ae6ab10-1876-4f27-b80b-e85dda03d5ab.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2b537d6a-b6b9-40d6-89e2-991c418ef53f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2b6ddc8c-780c-4b2b-9195-609279aad321.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2b89a816-0e9d-467f-add2-73c7c1ae3dd9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2bba3e93-a195-4af7-949d-ab8b3e9c64c9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2bcd3a77-71d3-4353-9812-7ade8d6ca625.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2bcec827-4fb0-4861-a75a-17d1ac733de2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2c0d595f-c2f4-4bf6-b81e-af86475d0d21.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2c12b4a1-a364-4653-aee1-fe96c466a98c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2c5e4742-bfa2-46f7-9387-9c8985d68104.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2c8ea0e4-ec79-424c-a67a-69ecc4dab48c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2c98bcbe-0286-4264-8ae7-4a4d33d00dfc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2cb60a2d-315b-4fcb-89f0-59e8c05c07d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2cff958d-5385-4554-9ddc-597a56a49886.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2d22eef5-ddbd-47f9-9125-69d4678bfeb5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2d60ca8e-19c3-4a11-a397-53609c3eed67.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2d8e7040-14d8-4aba-84ee-356a1eae11e8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2e5104c3-4b7f-451a-afaf-6d272e77ae2f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2e5d4548-f77e-495a-8d5d-02daaa4eb97e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2e5ed04f-68fb-4145-a4b6-d284756b6baa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2ead01d0-6b1b-42d2-b7c6-58bd1fef297e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2eb772de-68d9-4437-8ba9-124989fbd7ce.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2ec84a37-8444-4362-9369-c56451e4ae1a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2eccafc6-954a-43e7-9c41-ab8fdaeac04c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2f3408e8-e143-48b3-9f38-65808d091301.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2f8be13a-50da-4754-9026-4037f8fb0c45.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/2fe8d64a-5ea2-4901-b7dd-04a26c568014.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/300c9220-a845-47b7-8050-207265fb44c5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/301f56f3-1f87-406f-a2df-cebd939d48fb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3071bdcb-4ce9-456b-8180-f39e52a59b65.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/307dec24-4beb-4d07-8b06-d2c715a7b1a5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/30926db2-c1b3-4f71-9800-e363d36a51d0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/30d524b6-ad13-440f-a1ac-6d564213c2f7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/30f80fbb-ca6f-406d-a578-05818474be48.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/30f9385f-e431-44ac-8735-056448902493.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3104c91a-9eed-4c61-a279-3c2b28ae2e77.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3124954e-9fdd-4935-8cba-c4c3c2790dac.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/315e89f4-775f-44b0-88c7-3ff00cd42320.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3243d433-3501-455a-9062-141cb965c319.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/32475a7e-a379-4f2b-9666-1ae76cb94b98.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/32773307-6d99-44f7-b717-f89619d98868.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/328026c4-f745-40a8-ab1d-8433330ec839.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/32adb74e-d807-4c90-848f-d11bc719687e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/32f14e25-b2c7-45e9-976f-4743ae0efd30.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3336af2e-3b1f-4ac6-9f77-5531f7a4a761.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/336479f3-1ddb-4d73-960c-6f96a7b8f070.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/33c25d3a-2758-4fde-936d-a4665a606318.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/340637d9-d7d8-4bbb-a8b2-8b40e5453af0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3407b527-0a61-4360-b4b0-917d905f82aa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/344d4e0b-bc1a-4bdf-9ba4-4ab6ef5577f7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/34656753-d3cb-42dd-9d70-37bde2c5c139.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/34c75d65-9192-4a9d-933f-37d8069fba11.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/34e5b695-1212-4cf3-9d9e-50314061a036.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/34e88056-8de1-43ea-b59f-d193e6874fc6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/35258d4e-b8b4-4c1a-a15a-98f08d4db444.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/354ce96d-d417-4228-9488-ed38d22d3167.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/35b9551e-9267-4297-b42d-1f8dd1cab089.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/361d8d34-5dae-4e60-b153-d6580ec7373a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/362671bf-ebc0-49cd-a3d6-a91b5d62ecb3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/36df9d95-c1a4-47e7-8e68-7d1e4b9ea4ca.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/37261dcc-f6eb-4b5d-9365-68a9496e89f0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3738505e-b1f9-4004-8f9c-97b4671a5109.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/37c1c3e6-600a-45bb-9ae6-9c8a8845745d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/37c8590a-f99b-471b-835d-7457da2aeb4b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3804111f-592c-4b84-aa3c-5e1f47ee4ff9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3818dfe8-0127-44f8-af3b-6d6742a24f30.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3822e68e-4089-4795-acf1-7af53e09cc06.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3853e55a-8057-4db9-a704-573e05710dc5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3882182e-1382-4d4b-b280-ca9d76d990de.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/38dc6b77-bf8c-47ba-8c68-356c8c672c31.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3949e862-ec8a-4108-8811-f295c45966a9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3968ef34-111b-447c-b194-a1ce0281fd45.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/39d28bb3-4248-4fa1-9ce1-1bee8bd3214c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3a0f0662-7dfd-4e71-b390-e96575e2cdec.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3a1a0273-f07d-4067-bdfc-5b8e897cd6b2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3a412bbe-1de1-412e-bb31-d544c5e2eeb0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3a5ede7d-a24f-4a13-b44e-83914fb4c796.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3a78e14c-171d-451f-b4ad-41936568aba7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3a9b2124-e5a8-4ebf-97c6-b4da63d2e5f5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3aed8cb0-da5d-4f31-ae74-4b68faaa29be.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3b24e2fc-2f7f-49b3-bf76-81b226a74046.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3b4b35bb-23c3-4f75-856c-5eb219124141.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3b92b678-a005-40aa-af39-8d5ec22dd0d1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3bfeed24-ef65-45ec-b93f-3d1815947b02.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3c52cc2f-a786-438d-bea6-92cdafacefbc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3c9038e7-2fa2-4e2c-8952-d50b7646f088.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3cc05e45-1d67-425a-a99c-3e8cfe4f533a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3d135fd7-0f66-4d70-ba63-abaa83c76bfb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3d1547bf-41c5-40d9-9065-f346e295cf76.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3d5ed2e0-dfc4-445b-954e-ba743d5d0608.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3d751664-e48a-4742-9557-6c3d19cd241c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3d798477-2a40-4da2-a6fb-91cc638ff2a1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3d855406-9af8-4932-b592-22cd48415d54.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3da11e21-92d3-4543-b342-105c324c39c8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3dd4bce8-4f46-4947-8783-e85fbde6a487.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3e545b9b-5d2e-476b-934c-7e7e58b8e3ae.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3e601900-792a-4a63-afd5-4087b7c02d0f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3eade32b-1859-4ecb-a38a-885d7f6d33ce.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3ee0376a-5f95-4076-8ef5-e81a8eeb4e32.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3f308c49-1bfb-4770-8571-a147581f65cc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3f341df8-c46e-4d07-8f3c-d3bb2daa6410.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3f3e9fe3-3db0-407b-9956-57025c5b7e6d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3f409efd-8c48-41c0-b930-b0e915ffbeec.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3f4d9136-8cc9-4b63-a04b-98e2141f964f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/3f85a8b1-ccdc-47e9-87ab-480c3166d668.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4048fcf9-1937-4a23-af7d-6982626ec2f1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/40799068-9192-4e25-8744-6ce5f388930c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/409e7d25-c45c-4127-a303-e6f24c55192d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/40c3ae30-f7fb-412a-bf7a-a20fd94ed601.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/40f62301-945f-4c0d-8995-f5dea1a89f30.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/41d26271-f158-4d78-b3d2-2dfb349fe61b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/41d9d404-8b73-4d6c-9bb2-d059d745c1f0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/41dce00c-6a26-4480-a569-4ab8e6e74d67.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/41f95e55-3ce3-4ba9-9153-fa9a9f904229.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/42061aa6-19bd-44f8-95db-e91d3fc90d54.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/421924eb-840e-4d1d-9277-8ae938cbefc0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/421f8a79-16e8-4064-8a49-3b2507f76f6e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/428825d5-0253-4c71-9fe7-5ff834c8264d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/428836db-fb61-4207-9af8-468b1a286029.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/42936f41-3c98-48f4-80d7-f97fcc41d084.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/42aa16a7-4d7f-43c0-a163-825e10197c1c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/43065d31-4404-4eb9-95e9-85bf6f5d4522.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/432c231c-52c4-4f1d-9210-d066d87560e5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/43330772-33f1-4e38-993d-3306cb7ff268.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/436ce948-4578-4ef5-bed9-f929c3ecfa91.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/436dded5-ebdb-4dfa-8210-89d137b4005d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4379f5d9-10e6-4a37-8195-b6ca38ee5dd9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/43ba505f-1e4e-41ce-aabe-b45823c6b350.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/43cb86ce-5ccb-468a-afd1-0b901fc858c8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/43e87cfa-50da-4ffa-835c-bb39a7d05cb5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/441e1921-ed75-4191-ad0f-397b884d1021.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4483a0f8-e95b-4dc3-8796-03e2a55d5fcf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4486a0c5-0c5c-4788-a77f-3c9bdc3204a7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/448eeb65-841d-4c9f-9893-3f5b87d3bad0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/449c28c5-9a78-4c1a-a56c-c01b129b7b1d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/449c4927-93df-4465-a43a-fffa5442cbbc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/44c0faa6-9d85-45f7-bf87-cf583e6ad88a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/44d7529c-c2c6-44c9-a0f5-5759e210a957.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/44f10265-9efc-4bb0-9566-ca74c42cbe07.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4544119b-81f7-423e-a4e6-90dbcd9db806.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4583b13d-357a-4464-b917-e77450aa09f4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/45a08422-657e-4626-bcbe-c845e74ec809.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/45ac0c68-6109-45b5-98dc-456f579113c0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/45d36d0a-d5f4-4d0d-b577-fd52821e67e8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/45ee620d-f213-4f6a-a1c9-89f1a738c8fa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/460e6208-bd39-48e6-87ef-c9e15c240671.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/46328a86-4e81-443a-b36c-2abb5cb6f798.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4644c440-8fd7-4044-9909-e848c3af29ba.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/466388a7-42f4-4469-95f9-4d89cf0bd16f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/46efcafc-0622-4a48-880e-451e28e15008.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/47743ba1-1b3a-4b2a-8698-caf384221bca.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/47a11128-1de8-4624-aa37-226979c7a248.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/47d40cd4-1ae6-4dbb-87f4-cf0f715eeff8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/47d7e740-92fd-4687-8977-c1baa6cea843.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/47ffbe6b-d081-4f8d-801e-ba0fb6153a01.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/48261cc3-38e4-4cf5-af61-a16ae090eaef.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/482a093c-bce5-4d5f-a293-a9deb9a95892.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/484680bb-f5f9-4dc9-b40e-22844b32c83f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/485fa040-ac8e-4396-a3d1-36de9eefef8f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/486e87d6-3e65-4d79-8863-cb12ead2dc88.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/487092ac-5c24-48bc-a957-95be07cd9be5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/48837580-2014-4595-ae78-e655724d88d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/488f239b-81f3-403c-b32d-7d80f1bce848.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4890e48b-62ec-45a7-80eb-d9111b9619e7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4891137b-a48b-4961-a69c-9629a6f165d5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4893d1b2-647b-4f0f-9bca-3123fb28c881.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/489e32eb-2e28-46a4-b2ff-a1688a83333f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/48b31960-ad7e-4a99-b890-f1ffe19d48a8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/48b6a0f4-8455-4c28-9144-2d90b08711b2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/48fe0333-9c9a-47d2-938a-b093a29af8d1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/497cd032-1332-4d2f-8d96-9bbcf4ff1657.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/49a97a90-4584-4e80-a5de-4e4c8e05a795.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4a44ab0c-af72-49e6-8813-e36f746977dd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4a4ea2f0-361f-4cfb-9c07-5605286acd58.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4a584aa5-909b-4193-b1ea-3a63f6eb4faf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4a6aea75-8b07-426e-aaef-8f4a1841d513.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4a6c8766-5641-4d4d-914b-822e409441a4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4a9a12ad-e06e-4885-b58c-647868e9f821.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4b0d7eb3-a00e-4211-bac0-a21513cc55c6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4b443401-cc13-4d2e-b7bb-2aeea7eabe04.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4b584db8-5099-4709-a7da-7be121ca2892.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4b613fb2-4e15-4b2f-8b8c-f1a9302cc4f1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4b6de243-ba0f-4185-81ea-18d549bd2357.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4b804799-5936-46e3-854c-b809590fc158.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4b82d587-f110-41ab-a8cf-49e33db9bd37.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4ba82cdf-553e-4548-9763-9e0e24d4105f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4bc0b1d1-ce6a-4b7b-8eeb-4da336ea53a7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4bdb8763-e976-43a0-ab37-23bb156cd742.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4c0af339-2f2e-407c-8c4b-67fb1421efef.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4c1bc225-0287-481b-80b3-c5f30c6d6ed9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4c6a57d3-fa56-45a8-96d1-9bf767e8ba82.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4c72d8a1-e3ba-401b-9031-0a7d06583b19.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4c9c11ff-f385-4be3-bba4-ccb70ecba2df.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4cb0cff6-41e7-487c-8476-9253a21f88f4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4cbdaa10-169b-441b-bab5-732300455dab.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4cde752e-623f-4072-a3d0-1517aafd4cc6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4cdec8cf-d12f-4c7d-9dc7-b23604b7c369.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4cf03f39-f074-4297-8b88-607687b18118.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4d10c966-115e-46aa-a4b1-0585539e84ba.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4d24044b-8ed0-4623-8bf2-fce87aaa3766.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4d3da550-b2a6-417c-a1d6-7c6a4d145a39.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4d48203c-9e9b-4765-b44c-9f8387932370.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4d4d646d-db1a-44e9-a33d-bcd531324e42.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4d571177-0b55-498c-9457-6bd8f600973a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4d698773-946c-4d46-8b2a-3aec6b9e74f3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4da192f1-bd83-4705-9b64-d28b51914450.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4da220f3-080c-4ed7-801e-12c264f90c6b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4dbe1f83-38f7-4370-bd61-cac43a016126.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4dd15ac0-c18b-43d7-81d4-44ec40d8ea3c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4ddf942a-a9db-4b0f-86f9-87f94881f88f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4e086af8-0900-4c6d-b535-08c7a936a981.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4e1c07c2-5511-4018-b809-b51695a10f4a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4e1f8c18-bedf-43e0-a74f-bb2588be2c9d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4e8edd2f-7bd3-4b43-86fa-1aba40c9d302.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4e90c984-635f-4e05-9695-cacae33724b9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4e996f6c-ea8f-4f0b-88d6-b724fd671d73.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4ed52d2c-6da1-49ea-af40-bf49b8ff67dc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4efa29ba-9633-4dfa-bae3-76dde466850c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4f501ce5-28ab-4d40-9547-5be1311dc29f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4f6da8fa-e161-4292-8fba-e6f8b1c2e4dd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/4fff0d90-6b23-4321-b9a0-ed974b23ee97.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5029425c-701f-4cbd-bd71-2db071fcd19f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/50472b93-8644-450b-bc4b-4470d7a11421.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/506d43c6-854f-45ae-aa86-809e0512fa2a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/50c338dc-2d1a-4ed5-8435-5352759293d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/50ca90b4-ca3f-4b10-8754-18d0d0fcdbf0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/50e050e8-ba69-4eef-b76f-120369aca884.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/50e6b76e-6c76-46d1-b8cb-5d1af3e98984.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/510d41a1-4327-4f49-ac6b-2c738b4a026e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5177c343-8247-4db1-a0d9-40347ffc5102.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/51d8f810-d983-4ab4-a460-0f3c4c8efa30.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/51ec86f8-de27-4189-9d2f-aee0f93611b3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/51ee76e1-6037-4535-a8b9-9d989882aab8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/51ef1baf-47f2-4be4-9186-fffff7d5f2a9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5206872c-1674-430c-8d34-e46d5843fe07.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5225ced7-7ee3-4b5f-98fe-127a94e9a2d4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/522af54c-7156-4289-a59f-aef8cb000d83.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5248bb82-aece-4429-9b83-3940578043e1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/52824459-a268-4a34-8416-6478f7c2aded.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/52b650c3-c865-4dbe-be0e-e538320bccbf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/52f2b488-ac2a-4273-9ee8-4b8c17537536.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/53173a08-901c-4486-8eba-b9ed7b9ae6ae.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/53365527-4dcd-4a00-bd60-da1713269cad.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/538ea008-47bf-4643-bec9-dbe982cede2e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/53cad1d0-9969-4258-9889-900d8967430a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/53cfd3bb-3df5-4726-a8e8-41507bc87881.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/53eaf7fe-a4f0-47b8-8e8d-8892794398bf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5407bb09-6234-4026-86f1-da39bc57affe.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/54268bbc-8c70-42b8-97c4-3c0d2229528c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/544b5284-24ab-4085-9527-62325c3915d2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5465f348-7abf-403e-a689-31fc649b75be.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5474896c-d215-486b-8c86-5344072c7c38.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5496da12-d91e-474b-954e-a9411e832aef.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/54aac193-b73b-4c2d-aaa7-ba78c974318f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/54b8a506-111a-4fff-a37d-51bb136bc87d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/55393b72-abf5-4e46-9450-9ec5113137e9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/553eb677-6660-4280-b1a1-d233dc9e4bcd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5546cfbc-bf92-453e-b8c7-9bcf9489e458.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/55653e8b-300a-4b21-bc1c-6588324c9fc7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/55a8c415-70bb-4874-aa05-de73f4e976db.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/55ba0859-3d39-4a04-a1f8-e934087ab599.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5631b63c-24b2-4074-857b-425794858ca9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/566772d2-93d2-468d-88f3-bb76cb106d8c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5698039e-91f4-4e52-b39c-f6a79c03b9c2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/56b1b9fd-78a1-40d7-b20b-97b5c70f289e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5729adbd-d618-4aab-83db-6ccaf02c4c4c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/57666a38-d501-4619-bfc8-09840a8d28d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5789d421-98ce-408f-9a8f-30cf5be3c783.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/57955f74-652d-44a0-822d-7e3427a77bdc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/57bc4eec-bff8-48f7-b034-f9611a3cfa37.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/57f08c70-969f-4320-9fc4-fb83447094e8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/57f7e7c0-8ca3-4eee-b127-5a44c76a9a61.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/57fcf466-f39b-4bc9-8f0c-13db9c9a0675.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5842c4d2-f2da-473e-91dc-48395b63f382.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/58611f22-e2b7-479a-8ff4-186926c28a2e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/58961b54-d044-474a-9498-80a6f31cf10b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/58cf0970-4674-4057-a1d8-0240a9c610eb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/58fabe3e-ceb0-4886-a702-45a948d0af2e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5921e731-07e7-42be-9b2b-b7e7025de569.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5949e07c-612d-4f06-826f-5150b5435890.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/594a44b8-da84-45b3-b448-8ad6d355290f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/59f44afe-59ca-4281-9a2e-753322f2542e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5a04bc49-3476-4d7e-9538-d000162fa449.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5a72093d-b9e5-4823-906b-331ced5e08d7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5a9f88fe-7fc2-41e0-95b7-25401e2bcde7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5ac8f833-5342-41dc-8906-974efdfe81aa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5ad97bd1-0f41-4d4d-b6f0-c8580a8353c9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5aea9c82-6c98-4d98-98b9-eb6908acbe41.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5aef8099-7b21-4248-85e1-6bd781b26478.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5b03414c-a131-4c05-9824-1322521f9c3a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5b1ecc1e-41db-4212-92d0-acc52af7392c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5b31a753-516f-4dc8-aa72-937fc6126c95.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5b3eb52a-e3ed-4f13-bcb7-2564bf39d34b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5b655957-9943-41f5-85df-a0b5beba545a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5b846a5c-a500-4d93-bc5c-db8b98d91bd9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5b8ba1e5-30b8-448f-97e6-50a6741500f3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5c6a1cd0-5f6b-42b3-96ef-fc1e4ef7d067.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5ce0286c-a161-4473-82c0-febd82bc2233.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5ce0fea7-afe8-4836-be0e-948f041aaa83.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5d231b48-1c50-4ca3-977c-8f9aa5912a32.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5dc65c0e-fcca-4386-80bd-cdc8cf3aaeae.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5dd34946-e294-4dd4-90fb-715417f123ff.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5dd46e7e-7425-475b-88c6-736b17fda9c6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5e42db5e-3361-468b-8d82-d9c35a286b21.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5eea8819-77a2-46e9-9a98-8c9bfaf6e4c7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5ef10029-a87b-4fc5-8b53-99f05731fc00.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5f5949dd-e1db-4dcd-9328-cfa5d3e0b224.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5f72fed8-7f98-4c85-a10a-80cf908e720a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5f75f67e-b806-48c8-b324-27703dbb013e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5f86cea2-bb34-4b39-9c62-2505417ac7c7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5fa11d54-53f7-4b9e-9d8f-07012eba4e90.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5fc13bc0-a4ec-4d58-b82c-fc9e36ebe244.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/5fd84e6a-b92d-4373-92f6-ba7d7aa562a6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/601a73ea-3962-435c-a902-40aec8a11c56.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6063cc59-ff2c-4c3a-a58b-f6aad91157f9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/60b72399-743b-49b9-b31f-6b37e77d8f46.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/60d66fea-b63a-43f0-b85c-748a3adc0391.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/611473e7-176a-4678-9ae4-b8184cdf8039.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/611dcd46-d08f-48d2-a935-c90e83be6914.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6121172c-95e6-4f95-b5e2-709369a26f8a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/612aa8ec-7df1-443b-a081-d62add5e0c14.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6183e4e1-f674-4048-a669-c7b310cf1530.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/619a822d-dd10-49d2-8ede-94aaa700984c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/61f6269f-d4fb-496f-b18e-c565316b6a41.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/622824d9-83a1-4b15-a75b-0f4c708a7e3c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/62319141-32fa-4353-b2ff-ec31ca232e3e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/625e44d4-fcdc-47ba-b3c1-4c55298b1b80.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/62748645-320e-48c5-865e-ee4a60349472.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6289a052-b4a7-417a-b687-b22fddc14663.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6289d90b-2b9f-4e68-bbfc-2314eeeb1dd4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/62ce5421-bc66-46ef-b797-a809ca70d250.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/63083cb5-29b7-4693-b8a8-d37f77a3b35d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/631651e4-7cf4-4c0b-9b98-8657ce077ee7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6321e604-9437-4090-ba2c-af5567201483.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6346eb3b-8049-44c0-9706-1161fa480542.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/63600695-59a6-4faa-8d60-78545571d34f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/63703299-e4c2-4156-8df3-180a070141c9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/638408fa-2023-4cce-9dcf-a378e28312d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/63c2f8e2-08fb-41cb-bbcb-7e11ef5574ee.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/641767c4-11cc-4a5c-ad87-e392ce092ee5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/64184c4a-d0f6-4502-badc-6fcaf1ee71b0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/644b7f76-eb3e-49c8-ad9c-810fc403ea52.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/64548939-41e3-425b-b358-0d0e916a516d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/646cc2d8-cf72-4d53-ac0c-ca11f20af175.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/647d9600-d011-409f-af3a-68afe22dd8cd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6486b048-5518-4561-a3df-5449b3dae62b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/648885b4-928f-4e9a-8417-a60707dd2614.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/64baf4f3-af6a-43ad-a2d9-2c6734d32bb2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/64c7b51f-5d88-4771-b8cd-5533c64dcbb1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/64daf139-bf01-3270-8280-81f9a4c63b97.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/64e15b3e-dc58-40cd-81fb-9c1804efba9d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/64eff51e-441e-4ce6-8a73-55c2b80ca3b2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/650c4656-afae-4bf8-871d-3cd63f52d38a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/650fec0d-8577-4afd-b42a-47bf8132e31c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/651e9c46-e4a8-455d-9f69-be7f4ce3a422.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/652fadac-5ee4-4a5f-afad-b3df8568f6b4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/653efc24-a5c5-4f94-86d9-1256dcf4bc28.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6598ec73-86cd-40f0-b5ca-724aee528c93.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/65af4bae-9bdc-42aa-8128-63147895a6af.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6615bbd5-025d-45a2-9489-fed57d044001.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/662e3cde-ccc6-408b-9cd8-1c6b7fbd0bdf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/663606ea-7234-49aa-a361-a0e2d5555675.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/66373c84-4872-433b-a949-c4e5ba43e363.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6652b96a-6894-4cdb-8a8a-543ddb2110a7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/66abd0f6-acc6-4f2b-80f5-867210ccb2ee.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/67b419b2-41df-4b94-a8b6-440455819427.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/67d97e73-4eac-4ae9-9ff2-db1127dd5d03.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/67f94294-ce00-4106-92c5-603858b5a73d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/68501be9-0dcb-44b6-988b-ac1677cb2a35.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6863834d-718a-4e93-be23-aa2fb45b6b51.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/686acd03-2e85-4290-9a19-d40196209a57.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/689463e0-f435-424a-bf21-9f7d8c876632.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/68a8d4a1-713b-4cfe-a841-bded448a740f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/68b5092e-274b-429f-9527-4ffdb446a0fb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6940c2c0-6685-4a46-a941-d8e9bfe160d4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/69acc8df-eaac-4453-9729-12f25673b9fe.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/69c544a9-6dc0-4ce3-a6b3-e987a6f37a7a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/69e270b3-9354-4f92-a397-08099b189d3e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6a0b1a22-b45e-4dd0-869c-8ccea4fa6950.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6aa24c17-8976-44be-b3ec-e66c430512f0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6ad1eaaa-4724-45c6-8ed6-24d85ec20bb5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6ad4145e-3017-4519-8089-a5b0f6605de5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6af44d96-2d68-4ac7-9724-0b838523cfa3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6bb592ac-81c2-4df6-8f2e-ee2c42de67cc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6c185b06-6b95-45d0-bad2-fea9895e1e5a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6c265549-4946-41d2-96b0-0e0bd3d2089f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6c2fd22a-75d5-4f18-bf23-d80347bb4f53.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6c861441-b3f2-4aff-b2cc-79232245a4dd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6cd57992-84f9-4ff8-9526-a2a937f5acd5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6cefa84c-81f8-424a-8da2-9965c1cc742d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6d254375-63cd-4610-93ef-ea801fc30934.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6d4046a6-e65c-4e8c-aaaa-8a59bb494aa3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6d8b1aae-c4f8-3b6e-93e5-d5df230ab180.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6d9b2c0d-0aab-4a55-9ca5-24b8f6d87eda.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6d9c44c4-a8b6-4297-9a16-fd65d9dd096d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6da8d4a0-97c9-40a8-960b-6825fa3221a9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6e16ad24-712f-4d40-abe6-93ecdf10bcb9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6e7d323a-de8d-424c-bcd9-384c7540b55b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6e8a91c8-ce26-493d-87f4-df89ae7c3407.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6e98b8e8-6feb-479a-a122-5523b9620819.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f02d910-2ab0-4540-897d-3510e3274b2b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f08f24b-b56d-4424-9878-3aaa85d27c76.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f2cc2ba-6d8d-4a20-8707-4b2d12edf23c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f3f7829-e4a6-470f-b59b-98e97921de1d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f671575-096f-493d-899d-c990b38db2a1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f6dc04a-1a6c-40aa-a3e6-0f62fa8afb0a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f6fa6cb-11d1-4213-8a1e-3d6bb602f82e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f8e2463-f7e2-4807-b12d-ab29878c5439.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6f9f4aee-dc7b-4749-a98a-67fd52cd55b6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6fe28e4b-da6c-4b5a-bc39-6eaff0322b34.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/6fff9bdc-20b4-40e6-a37d-ca372cddb1e4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/70540c4f-9d4d-44f4-bc4d-fc835d5dca2c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/709bb15d-00a9-4da6-9f92-e18e9391a525.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/70b30bb6-d938-4874-9aff-a7298c604d21.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/70bfd2f5-3ab1-4876-9d2e-9a7d151bc657.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/70e6bdde-3c7e-4561-b775-c0fdf72d837d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/710163bd-fdf3-4ca6-8b8f-1ebf70cc1d9c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/713059bb-b8b8-408a-9374-038df1deb3e2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7191996d-fa91-41f5-876b-4c3075fddd3f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/71c4791c-25f1-4fa7-ba4c-0287c9dd81ad.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/71c821a0-41bd-425f-9311-c689a7d1528f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/71cae2e2-a584-4adc-88da-e0d67c85ca60.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/71eb55bb-b50f-436e-aba5-a25504574d49.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/71f48ed3-c9a2-4775-81f1-0561356178ad.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/725b5283-33c2-44c2-a0f8-628e3621e9a0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/725c06eb-411e-4f33-bf85-12c8abc37a0d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7295403f-5ae8-4e04-b687-8e3779ac41b7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/729cb450-34d4-4ab0-ac94-e7279f07c31e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/72a8fbb3-35f9-42f6-b46a-41677383bd8e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/72c699a6-53c6-4b0d-b430-e14f2e15ff91.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/72db2b25-9bf3-4c97-9fe7-dfd96dbb833d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/72ef43f5-ea82-43b4-81c9-11f713843d8e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/73728248-41b4-4c99-a172-abd2ff1a35a2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/73d76c19-2e12-4efd-a0f3-7ffe054b881d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/73dfcc36-ab85-45e8-9063-bc1c4bba7aac.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/73e85e57-b389-494b-81dc-5827c238cb1b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7400940b-2129-43d9-ab09-74c3d83adc97.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/743266c4-7096-41e7-b812-82310c4ee393.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/74345089-2a96-44e0-9da1-b640fb6f7f5d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7445b1b0-ce5d-4dac-9665-6e1211d7d454.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/74d854cd-c006-4164-ab00-39549af4a140.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/75373602-61ce-45df-8a9f-de721e3e47de.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/753e1cc6-dcf4-48c2-8ec7-c971580d08d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/758b7302-a6c5-4281-9939-2eebaa6ed2b9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7599c6c3-3472-4237-8ee5-7b77f3934fa4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/75fdbd17-c029-4a56-bafa-17a78cf0a8d5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/763759f2-5537-4ea5-9f54-27cc2d9708e4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7642c1ce-55aa-4cda-9238-31b1cafc7989.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/767fb808-cc4d-43ab-aadb-54a324570ecd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/768c0f66-5062-4bbc-9140-d8fbd2346c63.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7694f6ff-467e-4bf0-92b2-161cfdb13118.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/76d0a744-becf-4852-83c8-25d793d438c5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/76d1b15e-667e-4b7a-b6dc-74bf7626350c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/771e1e7a-b1e6-4e9d-a17e-a4bfb9b81e4e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/771f29ec-7a0a-4593-9f1a-6a31d281fbd0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/77348b64-e8f9-421c-8986-e3dbede8b470.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7734a9f8-3617-4962-9e92-2314c9feebe5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/785a503d-21b0-4aad-9c6c-9b3b5d965b07.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/790d23da-e07b-4885-b80d-be1c28b54858.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/792e64e0-70f3-4c39-a77b-48a514a68fbd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/793417c0-aea5-45b7-9d08-908f24535abe.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/798bde9b-6bbc-43eb-9456-9e0227fc0d1f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/79b5982a-1302-4080-9cab-306c8e3e337e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/79e5cd95-d841-48f3-98ae-2e71e2089896.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7a0ff9f9-85e9-4bde-93ca-c2c929233258.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7a1d1b3b-4c78-4edc-8a11-c9a3f962e97f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7a2d6a8d-6929-4d68-a070-75bd3f614026.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7a4091f8-71ff-4897-a703-a57af1d1f318.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7a55553d-97b2-337d-b244-00599c86a5e3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7a5f2dc8-4afc-4533-b62d-6f5d5d418663.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7a6bb036-06d5-4f58-ae34-453640a0a0af.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7a750748-9fa2-44f8-8b0c-6814de92a2c4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7aa42079-a9b0-449c-8c49-6d8da1ec5b3b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7aa60c7c-a8e7-42e8-8235-7c0bf0572eb4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7abbb840-1187-45ef-a42f-9912f1ec85d3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7acf98b8-349b-4b03-86a5-5fda22cf7818.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7b523483-9417-42aa-bcc5-fd8cfd4eb9ed.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7bb1794d-3a37-4455-a801-abe31de2ce8c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7bf721bf-8839-4343-95c5-b6e852805ad1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7c418d2e-974e-4a2e-b286-ad5043eb7d95.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7cbd1940-e203-4bb5-bb6f-d89ce943018e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7d2d82d0-ad8a-4fef-9288-8e763a29f50f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7d4713d9-c632-4b6f-8c3d-cf1c7b16113d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7d9ed100-9897-4d06-8f1d-00fc9260ff9d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7d9ee706-7c45-4b22-a4d2-1b33c6ccd9e8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7dc5ad07-64d6-461a-822c-e36c142cd96c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7dce7d7b-1243-44cc-94a6-aaf3ab155f0f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7de1987b-c150-489b-baa7-0cf57f0dcf3f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7de9ffd6-f4c4-4c35-b7aa-a5a1cb7e285c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7e259fdb-ecdc-4498-bdd3-b95c1218fb89.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7e33d9d3-6387-4705-a679-012a80197e67.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7e7f1f8e-812f-402b-b5fc-406719e9ec43.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7ea9aaf2-ed80-4b8a-a174-a7c6b7685e2d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7eaaa405-12bf-4800-9931-940e3be49943.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7ec7761b-f803-4062-ac46-05d7eb771020.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7ed123e8-b232-4e10-8c0a-cdd67c8d47aa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7f065772-c89d-42d2-94cc-062ff234920e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7f352274-2488-4fec-a1d4-a157191c1ccd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7fb021fa-9d67-4193-9b65-e6895d1dc071.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7fe838b9-c3a8-4f7f-9b08-012f6ba079ac.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/7fe87256-e9b8-4599-982b-61e732d9226c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/80229416-b3cd-4db0-83ee-61c6645a04cd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8076578e-eacb-4865-8d1e-4b977bbe8a61.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/808eee53-1193-4903-a12b-6cd9ad837af7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/80b9751a-956c-4c30-b712-39c6f9c0d09c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/80bad779-5430-494a-8f69-b5b74eec3c19.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/80c66afe-a38e-43cc-b423-5d86f3fc4b41.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8132d666-3252-44f9-9cc5-c0c5bf3377ad.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8142ffc9-be64-44b6-8d23-267c54f41bbb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8144792f-4d0a-4f19-b724-a302a87bebb7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8164e0ef-5dba-4ca0-888b-54706c212df0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/818ff115-688a-4b02-ad78-9a30539eb018.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81a16e8f-3b69-447f-9290-0b2d3e2f46c7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81af1feb-181f-4047-9b6a-214757293820.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81b63911-a15d-421d-b400-bea2e1e094c0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81b888c5-1b37-4ed3-abec-e67cc3b03156.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81bfea92-9a56-38eb-8bb2-ffa5b572fbc1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81c358ca-dd9f-4d4d-8e96-664752f15204.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81d1ecd3-9a1c-4ee2-be0e-de9c6c121ed3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81e4fc44-062b-427f-affe-6339a7289307.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/81fa58e1-f96f-4daf-a3a4-8f8ce70f6e98.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/82044272-791c-47e8-aa8a-c91545aa0c9f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/827a7bf0-21fe-342d-ba2a-a29246d30d43.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/833ebdfc-650b-4470-bca9-55ccb1861f32.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8352b20f-d22e-4c35-8277-cb1da2a7b84c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/835f1b5d-cb60-4164-a1cd-927bad7f3dbd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/835fd00a-3a2b-4fb1-a8fc-8e68df742cd5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/83db09d8-0c4c-4b13-8909-404bdf4ea3ec.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/83f72371-11c5-4edd-89b9-95b2388888d0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/84e42153-bfb5-4f05-8e28-84e4772351ae.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8531e316-2cc7-4917-89f7-c6697f6513da.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/85502557-96e1-4840-83b8-6aad2298d6c7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8573432c-da1d-4cbb-8732-f1a799c84bf2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/85bf43f9-8086-422c-87b3-69d0ead9d4bc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/85c56fb2-ff7a-47d4-84a2-199e61d6159f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8601deed-5a31-422c-8bc4-fa0c10c288f4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8616658e-3dd5-4215-9940-f540664634e8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/86205f15-d65f-4dd7-af0f-08b77a32097c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/863747ea-4502-49d3-bd2d-98e2551b586a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8693a47d-21a4-4b98-a1b4-5e901f379b8f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/86b7eb6e-e2a3-4985-90c3-970a71db4fbe.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/86c99c80-ffde-3e4a-b530-716ea61ea8dd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/873ee523-5780-45b4-a964-fc59a5674f61.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/874d4496-7e8a-4cbd-9fed-35bb923ff0ae.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/877293a1-df79-4a77-a420-495fdb1e4933.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/879812cc-973d-4c7c-ad38-76262208230a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/88433761-5eb0-4d1e-bb75-1fe1eecf319b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8860dfa2-5713-405a-bed1-04dd55a5dd69.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/889d46f4-c6fd-4f2f-87d4-54c9bdc34f6c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/88bab778-aa61-4ae3-9fac-b7ff21d7a626.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/88d53250-c1ec-41a9-95a1-3ace49c016c8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/88f28693-5929-4fd6-ae61-e64c7f82e9ff.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8931999e-b92f-41cb-8f30-819557715be5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/89dec671-d278-4685-8ffa-aaf60a839cef.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/89eb27f1-dac4-45e2-93fa-4dc0f44e9793.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8a2f8f91-8d42-4431-9424-9bd341d653f8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8aa5e2ce-e86c-443a-85e6-56a3fd956b36.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8b089f0a-3600-4932-845c-74c8c680cf7f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8b0dad02-3ca9-4b41-a8b4-f476f27b25e8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8b18b3dd-4d69-4776-9361-a709d7116d4f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8b55bdba-2598-4b46-90a0-eea534a19a66.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8b847a09-1736-476f-8aba-ba6da836c998.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8b8cdbde-57e3-432a-a46a-89a77f8e6294.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8b8e6917-51bf-43f5-a2ed-44822c0ad710.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8b907d74-e97e-46fa-a9a7-ed3e96c81ea5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8bba3d84-9d53-4dc6-ad3e-dfac6907b177.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8bce5a0f-7695-4b4e-9cd1-98529f41c16a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8bcfbbc3-fb54-46d6-b9f6-8029c2fbb3b1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8bf54b30-9829-441a-9a79-f17648f0966b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8c14a633-3a0d-4fba-abae-0687b9e5a840.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8c2cded0-a94a-4c7b-b5be-d8e31a408732.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8c88bf88-c253-4a3e-b3a3-53d96a47e873.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8cf0f886-0ee9-4f2d-8462-38783e39a9b8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8d36ee59-4316-4ec5-9aab-b03242410ffb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8d47cb7b-eff9-46e1-924c-2e33eed6f20c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8d4810de-1c7b-4ace-b9b3-edf23619b063.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8dd376c8-f393-4eee-98cb-2c61d559a139.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8e2509fd-0407-4aea-af54-eb1e13e83737.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8e58fb02-90a0-42af-8f99-2ec9556061e4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8e83a9f4-f23e-4852-adab-62c3278671a6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8f4810fb-e4cc-419b-85c3-6f1b6e7cd88e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8f4f873e-6974-4126-8c16-ab7d85204903.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/8fe26c63-f744-4dbf-9149-ed8147275bed.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9009bf15-6028-49e1-a037-cb1b2f20e7bd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/90510de5-90ed-4cf2-b81a-f0d8295f2a1c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/90619437-788f-4bf9-894e-5523634d2d6d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/906eae3a-3643-4c3f-8287-e2073bcdb53e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9088a23a-0ab5-45a3-9207-1c81550b5d68.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/908ee318-f4d3-48b1-8498-f4cb8627aac0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9090ae7e-815a-412c-8610-0233ae8b4db5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/90a2df4e-5e45-4b20-8d77-7e3c4b42be12.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/91241816-4526-4352-a559-44c06aac505d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9129c153-38a4-4b23-97c8-90b3b9fc4e06.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/91529269-ea9c-4809-9629-8e60a957b34e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/919025e6-660c-4583-a892-ec3709bee55e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/91c70914-7c69-4383-b4f8-4860ffe4bcd6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/91e45e60-ee09-497c-a348-dcf9fb314f2e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/925bc907-2909-43e4-a988-261bf098e3be.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9270ae91-dd5b-452e-ad61-03b5760bf025.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/929bcf93-c9d4-4933-ae6d-8a73308b8ba8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/93a7847f-b482-44c9-8bf4-0417d174f4a7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/93e52a11-6fa9-467e-8da1-95b53e3286bb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/93e8be7d-0f5d-423f-be8d-3e54cf1fbaed.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/941e3c41-5fef-4be4-8934-ccf60fee9721.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/94ea3c29-2066-43b4-a900-80b286410a0f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/94f69cc1-d4a1-45f0-bfae-672cfbd57fac.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9553f42e-253a-40f1-9148-30f7f71937de.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/95625d50-3350-480b-add8-dd1001fdd612.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/957eeddc-24c0-4d57-b8e4-7a5ab3d7bd85.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9582f63c-7e72-44c6-9373-3e229f9ff7ef.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9603344b-99b8-43db-abf0-73c7eaf0ea5f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/967011ed-753f-4eb2-8505-feefe3f33f88.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/96c1a40e-a679-4645-955a-aa88244c7ecf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/972f278d-f277-4b92-a6ec-6fc99ed7e92e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/973e5393-a935-443b-b7a2-10a29752ce24.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/978dc980-b198-472f-b04c-cdacf7d0e968.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/979f2e7d-12b7-40f4-a57c-388907f78b27.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/97c76356-1d93-4887-ab6e-0e9334e6cf3e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/97c76c43-bb65-4f05-9f16-d67695f8f397.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/97dc7e5b-68bc-4e1f-ac9b-b5de5e69819d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/97f12f67-508b-4cdb-8e0c-ea0e20cc0805.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9814a26d-3cb1-411b-a11e-95a40986c273.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/986a7091-335d-4ad8-9844-1252049970c6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/98a95640-f085-4208-8297-db47551e4272.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/98d79c07-d61d-4849-9a96-78c9c1ab0466.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/98e10094-bd8d-49b7-a01f-c5050f7ddf4d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/98e118f7-edd2-47ec-9912-3a2954477cdb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/990ec0bb-377d-40e3-9798-2dde29ab853e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/99a1b7c8-b3fe-47f4-851f-0bab93344121.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9a30c6cd-408e-4d05-be43-0b40addbe29b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9a88b82f-bc7c-4282-ae71-c91d58c07708.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9a967b96-b40c-486a-ba68-e6183fd07575.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9a9a3f9d-e59c-4597-8882-26e0c803146a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9a9b1caa-8346-4844-8c11-09674e43f87a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9aaa05f2-d0d8-4511-9b53-bdcb3082e96d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9b07bdb0-5645-4588-b202-9ef637971c46.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9b139b95-4c82-4574-a575-805325525c25.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9b4ce4b4-50ef-4f6d-8b7e-1f326cc72e3d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9b5bbf71-3ba0-40b0-86e7-b295b23a5e86.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9b686bf7-b0b9-4d4e-a160-fee03ebc0df1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9bab8067-6b18-4b4c-b980-92b690005387.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9c2e6c40-74b3-40b9-84bf-5de7cbfec0ff.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9c3a1b9d-e217-4bda-b6e8-50e637807803.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9c4424b3-ed58-4cf8-b1b5-7c75dcf54286.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9c535c3b-7700-4ee9-bd00-2e81212090c4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9c587f60-5d5c-4e8b-893a-232728564717.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9c62fb18-f0b7-4ba4-abca-bc60d19b2a42.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9cba2ff3-4b9f-49ed-b5f7-c526ad7a4e24.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9cc6d87d-e891-4930-b8f2-ab463777b5bd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9d3ca979-5a5e-4ed1-a45d-e8d4ca9b4dc3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9dd3b6d3-9234-4395-a21f-b7514402ea17.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9df2949c-074e-4b18-b779-b88a074f9590.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9df43bc8-7d25-4ea0-a1da-46e5d73e9080.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9e0dfc29-e55e-4db2-a58d-f91595be12db.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9e62de1c-9e8b-4e39-bc9f-29bef87bb4b5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9eae7ebd-8faf-401a-804c-ef4408ab7552.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9f637598-a8d1-42ac-9bca-8dec361ecbb2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9f7d8df8-5f33-4a45-95b2-03c8692847c2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9fb1e141-de8a-4b4b-8db8-abaa38eacb9a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/9ff76d8d-af20-493d-a17c-a4aaaa94114a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a08373a6-e9bc-44c1-877f-1c078a9eb841.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a08867ac-8370-4645-915a-58f23d263b97.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a0b67c64-15a4-4969-91a6-89e365d87d12.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a0f9ef23-e4ef-43bd-be1c-6589f3770210.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a12acfc1-6929-488a-966f-01ab7e6e7555.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a13d7035-8c1e-4e8e-8ff7-4445788bee4b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a18d65b3-1273-48da-a4a1-2a2f3c24cf8a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a2270562-ddf0-44c8-8e20-2351a22be3e6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a288ee17-88c3-4e3e-92ec-b2d550ddb121.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a29f69f7-9df2-4038-bb61-122c9f6f907d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a2a8b471-48b3-4dd9-9ffd-dcf66d72dd58.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a2ac585a-4a8e-442a-8824-bf759e6ccdbb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a2d6e01c-cac3-4706-bedf-59368d6638f2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a2e681fa-e610-4f99-ae95-415d06220c8b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a2f74171-bbf0-459f-b441-aaedae789746.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a306b4cb-fab4-476b-b435-c86b7755427e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a32fbc3e-32e7-44a9-b947-306c42d3a34d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a337b429-eee0-4aad-a325-ec8248688d1c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a3f3de2c-0654-49ea-a1ac-9404322b9d32.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a3f6781b-630a-4326-b176-f666cc2eecdb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a418959a-2e3c-41eb-b1b5-15156f0838e2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a41dc8ba-827b-4f3a-98d9-ad5f1f7618a0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a42bd7a8-76f2-443b-98d7-e31c9123cfbe.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a43462dc-5a0a-4dbb-9201-a5bb9cf2db4e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a454de07-1d86-4590-95f5-93e6eceabba3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a474c86d-ab78-46c9-ae20-8693a48fb396.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a4876bad-812f-492c-9c0e-35293918aa31.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a493bbf0-3f37-4a72-8d1a-db8797f9eb1a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a4ba9f47-84a2-4b9c-b219-9d2ac0889649.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a4eb53e3-82d6-4be4-a0fe-f46827556022.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a585fa24-e819-4809-954f-f0bd3162ee88.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a5e064f6-2ea1-4465-9fac-5d694f3a7176.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a61d62b3-f40c-4099-b55f-0ca94c30e1aa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a6740956-d396-4a32-8339-60d811de1a53.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a68002c4-ac82-46e7-8946-0ee9f600e529.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a6836878-bae7-4da6-ae1f-d8fc6cda4703.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a6a1c4ec-a9e1-4135-bb78-8311278f3969.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a6ccdbb9-f0ac-4931-8a56-9e186cb3ba8c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a6d45771-8bf5-4c80-b7d5-df3f3231069a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a706a607-7e31-45e0-86f0-08573486871f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a712f91c-50a1-4269-bb61-03540f07db3a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a7621218-bd3a-48ab-9694-9f307bb4ba1e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a777eb62-7b38-4a0a-b0a2-cbbc9f9dbf3d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a86e27f5-9af8-45d5-ac87-6f67572002a0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a8715d51-381f-4fd5-b744-ba8d96a60497.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a89237bd-9f82-4c6f-88b1-5f7d8340ca88.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a8affecd-7ecb-49ac-998a-fad79a84fd5f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a91293b9-db48-42c1-91ab-f84a674ad63f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a975e5f0-d61d-4fed-ae91-84688aef8437.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a97f9900-b489-498b-8973-cb1a69690d35.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a99959a8-7d64-4433-968d-34e923fdf1c2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/a9e662be-94ad-43bd-a135-9862e1defc1f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/aa12068b-9f9a-4fb3-8fcd-b70f22249e9d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/aa6d228c-fc58-4e80-b1c2-ecb2e6fb25f8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/aac51183-f0f0-4246-9342-bf1682044fc5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/aafe7bca-8478-45b3-8a51-2799e2c04911.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ab48c542-dfb3-4617-96de-478ba09d1e29.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ab52b1ff-be0d-452f-ab2e-aeaaf55c6efa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ab6497d1-7887-4a9c-b457-0f8e7b60be1e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ab705d5e-935f-4dc9-b428-38d9ce379807.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ab7e9c56-b5b2-4dd8-ae70-fb293448d95f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/abc27de3-9f43-441a-a6a6-ec16ef13c6af.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/abfcc76a-d50c-48a0-bbe9-54e953797687.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ac4d4119-b468-4843-81e0-30c7693f30e7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ac7d2819-cae6-4551-b03b-21e973a5e166.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ad019f8c-2c85-48ae-90b8-4287ec72e9df.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ad37faea-9ed2-412f-a856-e4a4584c5e24.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ad798efb-579a-4768-8f2d-13a96a0303d1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ad7a4df3-d162-4fc7-924d-b76f2014d184.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ada48d55-60be-46e3-8649-befd587e0a51.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/adc07286-349b-4ff6-8902-c57e9e6ca77d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ae2a8a90-84b2-4d01-b8bb-943f0e0f112d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ae511bec-d70d-4347-b7d0-9836d9a37f60.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ae8020c8-8084-40f4-baac-af8ae542aaaf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/aec967ca-9327-45f4-aa03-3f432ae9003b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/aee0ea02-44f0-40ef-9ee6-6cc5c472da9e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/aef5f7e8-7353-4655-8fb8-1e7d605a606a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/af132cf6-232e-4772-96ac-a75a18a21382.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/af64b95f-8309-4ea3-ba49-e144dfeb86c7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/af8f84de-bb38-49e0-9e39-ffd0511dd65b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/af9e4300-62e6-4c4a-b4d6-1bfc9eeeeee2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/afb47456-1325-4e40-9d0a-df10b9596f5f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/afba1a29-9cd3-4f7d-8771-1d78883ca7d5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/afc53d20-f500-41ab-9c72-594588cf8a1d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/afcf6dfd-730f-4ba1-b8c2-158804fb6886.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b0537ad1-162e-4887-b638-c0c2302035ae.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b07444ff-5d5d-4493-8616-c1eabe6a840b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b0793c95-053a-44cb-b516-4a0f9a583f9d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b0a8e58a-bc9b-4720-88ed-3b99d53c6659.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b1141445-55a4-4dc6-92df-f60c66b74712.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b12b8162-efa4-4444-93a0-0aba7b8bcd2e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b130163c-7c15-4f9b-9294-5c81fd23e968.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b1833d8e-5de3-4f85-9eb6-42b4767c53af.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b2110fad-744b-4297-90b9-093fe5482d7c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b24b1afd-b058-479d-a227-1b433b71d695.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b2547f60-2576-4001-8cf7-831fedeed1ce.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b274aeae-e7c2-4b02-86a9-65248ac1e6d4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b29b8ea2-c7b3-4c3d-8b8a-a6b99ca190f7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b2c8bb99-b0c4-4bd1-8b5b-8358001a1e9d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b2e5a495-3ff6-4344-8394-299a42891da7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b3097f98-d093-42fd-b7b0-12143f9f666f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b31cc2af-6549-4422-8f96-ec5cd8f0f92c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b328cfe4-5621-493f-994f-24740d65dcde.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b338f1a0-d6a6-4786-b83b-7272ff085b85.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b33deb5a-4a01-4e2b-be82-3f4a5ea98fac.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b399d411-411d-4428-9c2b-6de9e4d83c7b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b3e45859-0476-42df-bc84-b8625b12b929.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b43ae585-3c79-4ea0-bde1-a14f99a067d0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b44e175e-11ce-42dc-834c-95a5b5a3e17d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b4a4c789-bc17-4d91-9496-22a4ebbfc655.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b4e96b08-b603-4021-8730-13a70cbb10d0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b5a7f2a5-0e51-4bb2-a6ae-1ebc9f8c6313.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b5e6468a-1f25-40e4-b38c-7e6969fc2605.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b627ee54-6ccf-496f-8a81-931938e5e4ec.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b63725db-7394-48f4-bb99-5707bd346d88.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b6eed575-7905-41b5-bd6a-66c6a538f125.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b734950d-92f3-4955-8d06-232dfc9c56c6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b78cf8d6-eb50-4977-b4ca-e05c68acf253.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b7e70ae7-a3b8-4623-bf64-0293c473b859.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b7f84357-1c82-40a7-bd6d-7817ec95b913.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b837e50b-2a7d-4b3c-b321-495f261acd2d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b86ebe56-e858-4ae2-bf0e-331120c1a2fe.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b8cdfe23-59f9-43d5-9d4f-d8f3bd406b62.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b9237c75-6b5b-4c0f-a776-5ab036c5fb22.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b98b384e-3fd6-4af6-9b6d-b4c1f1441460.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b9dca0d1-6166-4ac2-a048-3051c19b362c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/b9f96f80-07ac-445c-893b-fa02173345a0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/baa3522b-8136-47e2-b401-b413906edeb0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/badee8ce-ba11-484c-91df-c3b10a27619f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bb0a025a-2bee-4a6e-96d3-9559d8a56e3e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bb14e327-3e81-413c-a6f0-dc0e27319436.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bb2babab-9064-4bee-90a1-ce4681d6cb1d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bb6bcfe0-60c4-4e01-b416-ec4bae39c99c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bb77b52c-806a-440c-bef2-dd11a69bce25.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bb9598e5-69bc-46e9-90c6-c6fb93f96ed1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bc16ac37-00f0-4646-8e47-56de6044ac1e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bc3a9226-7734-40ae-817a-0ebb54a78a50.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bcc47f55-1dce-4693-a652-ac106f8d72dd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bcd6a9a4-acfd-4bf0-8344-ad4cbfe0b189.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bcdd266c-ded7-47b0-962e-aba98f16afa5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bcf190c8-288a-46c6-a178-c08dae003eed.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bd0a76e1-c4b6-4135-bc08-6f9c21ef0973.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bd2a6793-4c84-49a6-9311-3cc71701dccc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bd480c30-db5e-4361-983b-a8373f8441ef.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bd68e830-18a3-4b11-bab5-0065a5531d83.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bdb14156-5e8c-4f35-a064-be724505d5aa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bdb254be-2557-4999-abaf-9d5e2f093ae8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bdc51f04-3186-4772-a0f6-3d063c2f3467.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/be222e30-10a6-4e3c-85ee-8144f581482a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/be5b3d10-d630-4c86-ae25-6a79d5fc9c09.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bef42425-94cf-4583-9b0e-7d71e8137ca8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bf5a12c3-549b-42cb-9ce3-f9af050c6d9e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bfc1cd6d-3638-4cd2-9506-61fa2a144a91.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/bfd12459-d957-4422-a455-a32a5c2e798a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c038d3cf-722c-45d9-88db-45ede34c5cb9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c0756420-7f61-4f93-83ca-b44e99075bef.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c0760695-7800-45bb-86b6-8062360f52e6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c076b732-888a-4061-b775-684471031596.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c08c72b6-d175-4d0f-a248-b7326b81db78.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c0965a35-9ab9-45da-8034-f1dce40c961f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c1221b18-80ba-42ad-af16-0abf3eef03b8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c15f137c-e3fe-4427-b214-322bd762a0fd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c1a085ef-ff8f-45c2-b19e-1b472056a59c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c1e28f8b-0f3c-41c9-8367-54cd52db5df9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c1ec8df3-e322-4f39-a807-ac5d91808915.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c1ee0255-52ba-4cfd-b3bf-c20906fac5b0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c1f688a0-3014-480d-9067-4aec2021456b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c20b7c71-59b4-4377-ae94-90fb68365a24.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c2455922-3285-443f-886c-73a06874423d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c252f1e2-c013-4393-9929-7396caef8214.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c27111fa-87fd-49d9-ad0b-36ec05055e85.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c28de481-41bc-4957-809f-251d66997a31.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c2be36fa-91ee-44e6-9235-e044981d1746.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c2d7281e-a0ae-4b33-8a62-2fde4583a787.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c2fca76d-7e53-423f-a35c-98b4a4c32dfb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c38e9641-3409-4d36-97a2-509b6b9b62a9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c390f121-819e-4405-896a-1e60a357edcb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c3b9b3bd-eed1-4910-9d00-b8908bbee469.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c3c80594-d649-44f4-b92c-ffff3096b493.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c3ea770e-01f1-4563-a95c-87b05fdce81c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c430f507-2b43-44f5-9f4f-2244900cb4ff.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c46211a7-2f21-4bed-95ed-30d39ad2a59d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c49a5bcf-1419-4b1d-90e8-71335389e550.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c4f6373f-946f-4115-95d9-9d8f55f09e4e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c4fda120-f3eb-413f-a7ba-5cff189e4e89.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c5815d12-3168-46be-9a43-e16ea492a08d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c5960c63-aaaf-4999-8520-6612317eae37.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c5b6b7c1-55f8-470a-9fb8-83e5f5bec1a7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c5c90a50-8774-4f1b-9a41-751d21025814.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c5d2b55c-30c1-4da3-928d-abc49b9936d4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c5f652d5-9962-455f-bce3-d0afbe690ed7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c6477eff-05e1-4022-9c94-7f773fc0a1f5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c65033bc-8b5b-4608-b6f3-2c2853e8e670.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c6b5cd1a-3e5e-4499-8d75-69562e7826a0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c6cb7406-f11a-401c-9010-4ceb76dd889f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c6e032a3-cd3d-4bb2-b4f9-caab2f27a9d0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c6fb58e0-e5b5-4118-9b22-76696095bff0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c83adaa6-3842-4a61-94b2-3e9841166c40.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c894d593-ad87-445a-b795-9a1a7e4294b3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c899366c-4578-432d-8c65-bef87b826be6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c8a4c36a-45ec-4ae0-adb4-a6bdc6b89533.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c8c4ce87-381e-41f1-94cf-64661dc5dc18.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c8d25dfa-8d2e-453a-9df6-3f94cfa6493b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c900392e-ad30-4389-ac10-4a96d67948a1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c922708e-0db4-4ad3-a225-04a7a2a7500a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c93297f5-50a4-4f80-8bfb-085f61af44a2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c94c58ed-23fe-43a6-a80e-92186f15ede0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/c9d93142-6292-41f5-90ca-cd68d31cdcec.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ca051e8c-0402-4400-b02e-6aa3fc6b89f9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ca1f9be7-a10f-4ff3-b4c2-5e16f3946502.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ca3a9ff5-7638-4147-9a59-b8bf0885ace1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cac6fe2d-1ce5-431b-abd3-68317007808b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cb62c10c-ccf5-41fb-a165-45f62d8e08df.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cbcdcac7-0bd7-4068-a94b-6c5fb52639b7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cd150ee7-5b6e-478a-a3be-057ca7a3180f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cd16c6e6-5ff2-4a5b-a3e6-e4b9c39b6389.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cdb53cce-9109-4b96-94f9-155fdafc489d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cdb92528-cf52-4fdd-b3cd-1c368f7d9284.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ce2ff684-6d76-409d-82fc-75a204afe64c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cea558f7-86d4-45ea-95ff-9dffa08d49c0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ced09dfa-1635-4781-83f9-de75f83bc279.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cede2c1a-8176-438d-84e8-7952434327b7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cf11a369-e0de-4ea3-80c6-913e1ed3288a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cf1b305a-818f-417e-bfa9-0dba25edff8f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cf32cb38-e1c7-42df-85c8-707290e3185c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cf3811e5-6b86-47ee-a495-451388f676fb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cf499ab3-a6b1-470c-b2c8-a0712d6593e2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cf756389-1436-43d4-9f21-dab8c3802554.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/cfa158a1-24a3-4f00-a999-ef7c64aa4f44.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d01666f1-788b-46d5-9502-fa796496820c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d0681e95-d3a1-4461-8f6e-dff29ce7da47.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d12201e8-4ad6-4833-b225-e788a51f561c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d2232ce3-668a-4511-826d-36d66dacc98c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d241f2cb-c38e-4d11-b9bf-afe32c6bb674.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d254f79b-17e1-4afe-ab30-40d32041facd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d271f860-bff8-459a-8ba0-defdf223c4db.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d2ad56bd-bd6b-4329-a62f-1ee78106556d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d2e2c46f-9624-4071-bde3-f02c7696bdc5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d358cff2-1039-4836-bb26-b74a51ad207a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d3601408-ac22-4172-a551-8b003e579bee.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d36ed0a4-986c-4f35-9505-0c86b2f43532.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d3822e74-0975-40e8-afcd-941b36163c1c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d3eb636c-fd8e-4fcb-a102-49812171f23a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d41427e4-173b-490f-9ec7-e0bc1cb087d8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d4304ec9-abb2-4743-8af7-540307849267.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d44be608-465a-46dc-b45f-0e092c4bb8ad.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d4585471-281f-4cd5-b094-2091dbc20107.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d45bf008-06bf-4bf6-a658-14b25636d58d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d53ffa68-36ce-4241-b9c6-760d132e8a5d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d547fc89-31f7-408c-aa99-30bb4ff9bdfc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d5663f07-64a0-495e-a020-f3a85818d71a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d5dd7553-d4f7-44b2-bf12-9d452e47eb06.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d6740fcc-1946-4bff-9efa-677f452e2e53.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d77eeaec-ba82-47ec-b69e-b5123b6d2f60.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d7b7be7a-5ed6-419e-8d47-cfa909735db7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d7d1fd31-8fb4-4fdd-8a71-73723d8f8bb8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d7dbc1d7-3c46-4658-8ef1-c57610426886.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d83053c4-c025-4551-a02a-2ac028472c9a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d8633416-c410-435e-8816-d96e548473bb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d864c4f8-a679-411a-adc4-10354d300e44.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d8a112aa-b508-466a-bab9-3e9315d24012.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d8d6b164-38bb-49f1-8f6c-85e234c7514f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d8f18019-7b99-492e-88aa-2be0613dc92b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d91fe08a-8df0-42fa-8902-3fcc781af206.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d951b096-e345-4ecf-9ec0-e9d5229a193c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d998827d-171a-4dc4-9f3e-b5d32365e104.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/d9b14683-501d-4690-9232-f1e59aca3b7c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/da0fde27-343e-40ef-bb9e-e88cfddce815.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/da34f6fe-6160-4df4-9bd1-8ee0d309a396.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/da3c9afa-cd04-48f9-a2d6-3b6703c7ad3a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/da63b5a1-d4b5-469d-b25d-db5a22c800eb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/da8570b9-119e-4a21-a23b-ca8b94000c30.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/dab5ae00-0024-4e5d-a362-13e81efbf170.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/daeed374-84ed-4a16-ba18-71c5c79b6034.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/db06f39b-2088-48fd-a143-9dc4a8e2b44f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/db6f6739-0a6e-436b-b6b6-9c470d21ee87.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/db9ad90c-3da7-4dfd-91a5-4b0f35207b2b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/dba1acda-119c-4568-a24e-14cc17623ede.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/dc270f56-2ec4-48a3-a437-346647ed9799.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/dd577dff-09c1-472c-a578-8415767e983f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/dd6632d8-6a8a-452b-b5a7-05aa1caaa67b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ddeaac35-bfba-4cdf-96fe-c3ea9436a386.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/de2bbb3c-d07a-4384-86e2-e09a35484fde.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/de5d2f45-3cb5-4835-92e1-73e171558979.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/de5d892b-107c-4525-885e-53585305b655.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/de61b6bd-123c-41e4-b59e-da89bb2f200c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/de91c842-f703-4d14-a095-8a5c3f570fc2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/de9d6511-cfcc-4894-82f9-8fe2f6d062d3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/deef724e-97ff-4e08-bb11-b2ccd3c6f86a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/df4cc201-17da-43bb-8346-b020da57e6ce.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/df5706b1-53b9-43af-ba30-76c6401fd327.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/dfa244cb-7980-40e5-82cc-c9e29a543802.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/dfc72e00-60bf-4003-8841-b94d3eed5677.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e0010317-e54b-4310-9d9c-81c7d0383789.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e00349c0-02d1-4d62-9299-1b32299dcc35.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e02cad87-efc1-4bd2-986d-0f021dfd6dae.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e03bd3e5-8600-4495-80e2-bf2671c5973d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e0414d6c-1472-442f-b417-ebca71c83918.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e0d0379b-0835-482f-836a-5803975ade24.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e0ee334f-2d46-49d5-8d76-270715ec8cbf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e12245bf-0d10-4eee-87a0-ce75ea0ed8bb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e12f66cb-4bf5-4f9e-92dd-1cc9407f85c8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e1571151-263d-4e01-b760-50b292a243c3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e184fa13-9c76-4048-a06b-47b396a09fe2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e1d3de98-9eaf-4c02-b0cd-b1dbd03c745e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e1e408a3-7668-40fb-a008-776cefdc30ef.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e1f69b2f-5ff5-45f1-ba2b-da94a87230df.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e1ffad37-d420-4a79-a034-0a8e2ac787cd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e27534df-1e29-4a43-9f43-23e026d84c8e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e2d8ec53-224a-46a5-9269-06b72b160ae2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e38d5d57-429f-42f3-b1d5-f6ac48563e53.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e3d33704-98af-4bb2-afde-fa8079694aff.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e40258de-5c0c-4ce7-8b85-2953d498ac77.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e40f2a24-f9cf-48c0-89bc-b71b795c3d5c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e44318ac-6453-499e-a90e-1324258f1bce.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e44f4796-3c49-41d9-8eae-2d8fdcf6f44e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e45091f7-8083-490d-97c7-15e20c9004bd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e4644a2d-24ef-4697-99b2-842be257bd2d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e46831f6-4411-4848-a6c0-4d05dad8a905.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e4accb44-ea51-425a-ae27-3dac83db46b4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e4e3e639-5dfc-4a6f-950b-a2ae741af1af.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e6385a7a-7758-4546-a8b6-155c38ded9ed.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e658314b-1d41-4592-afce-1216b76642b6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e65f8f9c-c145-43be-8098-9febbd02ea06.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e68b1384-ad17-41d5-9e5a-d3c998b209a6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e6a4a044-6ee4-4901-89fe-5ab8b4bc8af9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e6c859db-475c-4257-abf3-8f4f379737d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e6cea7d6-0701-417d-b52d-9759ec66e1bd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e6e2fcd9-6cea-4d72-8c9f-e98f68bcba5c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e7276bfe-8ee9-43d3-b927-1075e9c88f45.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e736b2f5-97bd-45cf-8406-20ef69f13f82.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e7a194e7-45c6-4713-9016-55c542691f9c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e7b2d2f7-3f82-40d8-b88a-cc33fe3e7d28.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e7d832ce-83d1-4211-af05-15647bcc59fe.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e811f6b0-d002-4b76-8c17-3d99e93a98f8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e81221b1-1a69-428e-8b49-05e876d0d1f7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e8f868af-e2d8-47a4-add8-81d2bf522ea4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e90089af-65c7-4dc1-9b01-834420fe1807.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e914e4f7-9047-44e6-9a8a-19b64427ad37.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e91abdc9-0772-442a-b2cc-3f0eba36350a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e94bb5c7-9122-47c3-8b30-0c6bc52041bc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e95fb414-c5ce-4432-82ad-930371e41ee7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e9b6f54f-1d29-47bf-ba38-db51856d3aa5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/e9bd517b-849a-4d61-a78d-9a05285d1b32.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ea0be776-bedd-48cc-b929-e1f79e4e847e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ea4e5b6b-b3ed-4dd1-9da3-68ed85a10f3d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eb056d82-3318-44f6-96f6-6e49090468a0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eb369a6a-230d-4231-8cee-0f54201ae975.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eb42fd74-2ca7-44fa-bcb6-6b9982145489.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eb8ce439-cb02-4f7d-984b-9393cbe0822e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eb95db5a-76f3-49af-957c-b82056cff8f5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ebcb383f-0a48-4714-9dac-b39e05a6a903.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ec008c96-5096-4125-83cb-89c997576bf5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ec331d41-6b14-4d93-a52a-240d91ba93cc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ec7533e4-557a-4f24-8200-a26e977363be.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ec8593e3-11b8-4b77-b5fb-2f32d5abf03b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ecde40bf-2179-4bc9-8a58-1a5d666f0944.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eceec9a5-be0c-47a9-a168-a541a3eee215.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ed2fb23c-d84d-4bde-bfef-b852d6c84223.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ed3217e9-adaa-4e05-b7cb-d1e2a9b7bbf1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ed64ae66-3294-43a6-b94a-6912e770f5ed.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eda429d5-f2ad-4a16-a24b-473541d0fd73.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/edafe9da-56cc-400b-a101-f5bafbe4cea5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ee10ac88-e99c-41bd-8579-ee0626924007.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ee321758-50bb-4ccc-ad26-28d0096f4f7d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ee4a3e45-7cc5-476b-aa55-a71726fa7ea0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ee520469-b2d9-4552-b207-e674cd30a402.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ee70905c-37a8-4661-93cc-92f23e9453a5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ee7ce223-8224-451a-96d5-ddbeeda0687b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ee8e9ae9-a5bc-4125-89b9-4bc0511c95b1.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eeacf700-56a4-4245-8720-25deaa2ad398.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eed7aea0-aa17-48f4-bf86-fb696c2847aa.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/eeecca29-8bd8-4050-b6f4-b96ee8cbdf50.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ef14301a-3bad-4e12-9407-fc8253bbb374.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ef292341-44b2-4ff5-989f-1cf78ffaf7f0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ef3867e2-995e-4490-b3c3-260c75d8f80b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ef913336-6fb7-43aa-9520-271e477a25d5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/efd57f9b-c5e6-43c2-b6ce-be8b3ad405ff.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/efe1857b-d46a-47bd-b92f-0dc81a4eb620.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/efee4898-cecb-4ed5-938f-239931c5886c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f04245d9-b314-48a9-856d-93a98aa985d9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f07659e7-cb2e-4a07-9fbd-397b33b9360b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f07de825-d870-4cb1-b73d-540480a28da8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f0a5837f-18c8-4565-a386-e009a18782cf.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f0e405d5-66e9-40b4-b1e7-54e1bf5ae757.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f1a57686-c24d-450c-a758-23e5d2e805cc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f1fba920-4996-4310-aa1a-a0c03ba80845.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f2e08623-4743-47d7-91b7-4c015aa1fdc0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f2ecc636-3b30-4f45-96f0-5bd3fcd85a1f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f32fb422-a6ea-4bbc-b0f7-6df331725485.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f350c1ba-8040-4750-9e6e-f45cfbf916a4.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f380e8b1-0f97-4966-bceb-d730fa53f01c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f3d56c09-fb27-4ae9-a9ec-f75be5a893bb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f3fceff6-41e9-4994-b79d-faad21aa0fda.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f409f4f8-68c8-4a25-bcc7-d631f22066b2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f43310eb-270b-49ec-aef9-11103921b224.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f44dc1ee-3b57-41bf-86d5-4f6d025fccd8.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f44fe630-f6f9-42de-b105-28682786d77d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f477a2be-bab2-41f9-85e7-9da2cd00678e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f5c8c735-859a-43a7-9c11-00da41d2e73d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f63b0dbf-ce94-4ab5-92fd-a2a1abca4298.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f6e9071f-09fd-4603-ad76-028356d07024.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f780034a-fde5-47dd-a4ab-079fda0e0502.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f783bc85-89dd-465f-bc92-6bfb7c2f83c7.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f7dce3bd-31e7-44ac-ba84-c5098c46f6fb.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f8426088-824c-424e-8cad-71e2adfc1ed2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f87cd562-016f-4da4-a08f-13debf311708.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f8c3c03e-c471-4823-8588-1216d68e7e90.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f8d8856a-5d51-45e9-9fa8-49c074994101.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f8df44d6-9c0b-4f19-a0fc-4821bb569712.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f91f6539-4cc0-42a0-ab17-751b26e5b886.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f92e4a5d-691a-4555-a4e7-e09aa1dfd80e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f9bc5ca8-180a-4a0c-8cf1-e85b20864fa3.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/f9d7691a-e8d5-45fa-a279-ec7224afa8d0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fa3cf32d-dfae-4f29-80cd-14b67320532b.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fa806a59-4b25-480e-9502-35d15427ac14.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fa892aee-16e1-4410-b8e1-1196e89e4455.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fa9229b4-7d48-40f2-adef-ceccab8697f5.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fadafd96-5405-47db-bbf2-201fd3a9ccb0.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fb17ffa2-7ee0-4c65-a86f-c3c9b6c61c2c.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fb2c12f1-6169-41d3-b739-e5a48aea86c9.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fb2ecc58-2c2c-4110-8418-b0291667704a.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fb71b194-f607-4271-b8e4-8c82c7e606af.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fc0b2119-a86e-4162-9a13-e67411cfaeff.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fc21d53d-30db-4a3c-a717-82359d2170e6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fc6b1d8f-e38e-4bd8-914e-4e019105765e.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fc7315a5-d20f-45fe-8f8e-309f38ea44ac.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fc7eb06e-b6ac-4dfa-8a2f-ab378b3eb177.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fc93abbf-984c-432a-abb7-7f1ce951955f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fcb7b0b7-e74f-4397-907c-37cd2fe9efbc.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fcd7f3ae-0c21-4230-94e4-3a0e12ebcc78.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fdd65db5-a110-43d3-a9a8-2805169bd572.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fe3372be-1f4b-48cd-a15d-4bdf3e052386.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fe8f3664-81a2-4378-8125-b7ec392315d2.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ff1bff16-7d44-40ef-84e8-1120d0ad0dab.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ff453a14-c904-48bc-8b79-410a55694cbd.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ff62d9c3-1813-406a-88c2-427eaaee4578.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ff88f589-1b08-408c-a61b-5b860dbf512f.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ffc2d6b6-17a4-43ef-a7e2-e85e63e74a1d.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/ffd71c3f-5625-4090-a8d7-a3caba1af504.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes/texture/fffd4028-7f01-46c7-96d2-36c3f51b5ba6.png  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/test-envs.txt  
   creating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_apple13d_O02_01048988_09b0.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_avocado05d_O02_01048620_1690.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_beer07d_O02_01048625_91e1.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_can13d_O02_01048658_e9a1.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_cup03d_O02_01622004_d37b.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_dbottle04d_O02_01049070_38b7.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_egg04d_O02_01048656_a3f0.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_lemon03d_O02_01621718_2818.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_potato18d_O02_01049048_9fb2.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-1_place_franka_wbottle11d_O02_01049082_d8a4.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_apple12d_O04_01150235_caaa.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_avocado06d_O03_01050247_9766.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_beer07d_O04_01150287_1270.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_egg13d_O02_01049028_9e3d.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_fcan04d_O05_01250045_e0a8.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_lemon03d_O03_01050300_20ba.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_orange12d_O04_01150190_df9e.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_peach02d_O03_01050238_9c43.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_potato17d_O04_01150021_c37f.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-2_place_franka_tangerine06d_O03_01050375_2503.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_apple19d_O03_01051606_af73.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_avocado05d_O04_01051722_1abe.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_egg04d_O04_01060705_f5f0.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_fcan03d_O03_01051534_43f0.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_fcan11d_O03_01060604_0679.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_kiwi05d_O04_01051742_a2d5.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_lemon06d_O03_01060576_5305.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_lemon06d_O04_01051735_6ace.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_lime02d_O03_01051568_4973.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/1-3_long-horizon_franka_tomato03d_O04_01051726_3e60.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_avocado01d_O03_01050191_8482.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_beer09d_O03_01150509_472f.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_can11d_O05_01250064_1b1f.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_cup03d_O03_01050304_5362.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_dbottle02d_O03_01050315_2e40.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_fcan11d_O03_01050130_dc3e.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_lemon04d_O03_01150557_bdac.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_orange03d_O05_01250241_af42.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_peach01d_O03_01050401_66e6.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-1_place_franka_wbottle12d_O03_01150548_418c.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_apple08d_O03_01050789_b41d.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_can12d_O03_01050529_5ba6.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_cup02d_O03_01050695_f467.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_egg00d_O03_01250873_b050.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_fcan04d_O03_01050627_1701.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_kiwi00d_O04_01625759_b82c.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_lemon14d_O03_01250807_bea5.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_orange09d_O03_01250680_6e99.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_potato02d_O04_01624132_ad86.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-2_place_franka_tangerine00d_O04_01626714_9924.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_apple20d_O03_01050837_f264.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_can13d_O03_01250594_6053.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_cup02d_O03_01050695_f467.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_egg07d_O03_01250883_c3cf.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_fcan17d_O03_01250504_6336.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_kiwi00d_O04_01625057_98b5.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_lemon15d_O03_01250782_dee9.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_orange09d_O03_01250729_3add.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_peach01d_O04_01623186_ebff.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/2-3_place_franka_tangerine05d_O04_01626203_bc6c.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_apple99d_O02_01610325_2a43.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_apple99d_O02_01610841_d1f1.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_can99d_O02_01080044_571c.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_can99d_O02_01610785_5f89.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_cup99d_O02_01610039_9412.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_cup99d_O02_01610356_a52b.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_dbottle99d_O02_01610074_1745.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_dbottle99d_O02_01611366_b510.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_peach99d_O02_01610119_2f43.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-1_place_franka_peach99d_O02_01610473_4c0d.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_apple00d_O02_01641303_47a0.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_avocado08d_O02_01641061_076c.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_beer05d_O02_01641571_0bce.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_can00d_O02_01641329_c06f.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_cup04d_O02_01630239_6853.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_egg13d_O02_01641323_e5d6.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_fcan04d_O02_01641409_e758.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_kiwi07d_O02_01630549_eac1.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_lemon02d_O02_01641197_3c18.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-2_place_franka_orange13d_O02_01186003_bbfe.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_apple20d_O02_01660153_2a7c.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_avocado01d_O02_01650109_8032.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_beer13d_O02_01660041_2302.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_can12d_O02_01186110_5554.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_cup03d_O02_01650032_d3a8.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_egg12d_O02_01650248_8fcb.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_fcan08d_O02_01660185_f657.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_kiwi05d_O02_01660135_cbfe.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_onion04d_O02_01660011_e345.json  
  inflating: /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests/3-3_place_franka_potato00d_O02_01660238_33f5.json  
## Mapping extracted DOM-Test content
usd_files 81
json_files 90
test_envs_files ['/home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/test-envs.txt']
chosen_scene_dir /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes
chosen_tests_dir /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests
LINK /home/redafrix/tests/internship/isaac_dynamicVLA-test/tests -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests
LINK /home/redafrix/tests/internship/isaac_dynamicVLA-test/test-envs.txt -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/test-envs.txt
LINK /home/redafrix/tests/internship/isaac_dynamicVLA-test/scenes -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes

## Final expected structure
lrwxrwxrwx  1 redafrix redafrix   23 Jun 11 11:03 isaacsim -> /home/redafrix/isaacsim
lrwxrwxrwx  1 redafrix redafrix   76 Jun 11 11:06 objects -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/objects
lrwxrwxrwx  1 redafrix redafrix   84 Jun 11 11:07 scenes -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/scenes
lrwxrwxrwx  1 redafrix redafrix   91 Jun 11 11:07 test-envs.txt -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/test-envs.txt
lrwxrwxrwx  1 redafrix redafrix   83 Jun 11 11:07 tests -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/tests

dynamic-vla:
total 48
drwxrwxr-x 2 redafrix redafrix 4096 Jun 11 11:06 configs
drwxrwxr-x 2 redafrix redafrix 4096 Jun 11 11:06 core
-rw-rw-r-- 1 redafrix redafrix 1718 Jun 11 11:06 LICENSE
drwxrwxr-x 3 redafrix redafrix 4096 Jun 11 11:06 policies
-rw-rw-r-- 1 redafrix redafrix 8654 Jun 11 11:06 README.md
-rw-rw-r-- 1 redafrix redafrix  202 Jun 11 11:06 requirements.txt
-rw-rw-r-- 1 redafrix redafrix 3646 Jun 11 11:06 run.py
drwxrwxr-x 2 redafrix redafrix 4096 Jun 11 11:06 scripts
drwxrwxr-x 5 redafrix redafrix 4096 Jun 11 11:06 simulations
drwxrwxr-x 2 redafrix redafrix 4096 Jun 11 11:06 utils

IsaacLab:
total 136
drwxrwxr-x 4 redafrix redafrix  4096 Jun 11 11:06 apps
-rw-rw-r-- 1 redafrix redafrix  1490 Jun 11 11:06 CITATION.cff
-rw-rw-r-- 1 redafrix redafrix  1770 Jun 11 11:06 CONTRIBUTING.md
-rw-rw-r-- 1 redafrix redafrix  2608 Jun 11 11:06 CONTRIBUTORS.md
drwxrwxr-x 6 redafrix redafrix  4096 Jun 11 11:06 docker
drwxrwxr-x 6 redafrix redafrix  4096 Jun 11 11:06 docs
-rw-rw-r-- 1 redafrix redafrix   285 Jun 11 11:06 environment.yml
-rw-rw-r-- 1 redafrix redafrix 24001 Jun 11 11:06 isaaclab.bat
-rwxrwxr-x 1 redafrix redafrix 22640 Jun 11 11:06 isaaclab.sh
lrwxrwxrwx 1 redafrix redafrix    62 Jun 11 11:06 _isaac_sim -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/isaacsim
-rw-rw-r-- 1 redafrix redafrix  1630 Jun 11 11:06 LICENSE
-rw-rw-r-- 1 redafrix redafrix 10142 Jun 11 11:06 LICENSE-mimic
-rw-rw-r-- 1 redafrix redafrix  2462 Jun 11 11:06 pyproject.toml
-rw-rw-r-- 1 redafrix redafrix    68 Jun 11 11:06 pytest.ini
-rw-rw-r-- 1 redafrix redafrix  9003 Jun 11 11:06 README.md
drwxrwxr-x 9 redafrix redafrix  4096 Jun 11 11:06 scripts
-rw-rw-r-- 1 redafrix redafrix  1708 Jun 11 11:06 SECURITY.md
drwxrwxr-x 7 redafrix redafrix  4096 Jun 11 11:06 source
drwxrwxr-x 3 redafrix redafrix  4096 Jun 11 11:06 tools
-rw-rw-r-- 1 redafrix redafrix     6 Jun 11 11:06 VERSION

object USD count:
211

scene USD count:
81

test JSON count:
90

test-envs.txt:
lrwxrwxrwx 1 redafrix redafrix 91 Jun 11 11:07 test-envs.txt -> /home/redafrix/tests/internship/isaac_dynamicVLA-test/assets_staging/dom_test/test-envs.txt
../tests/1-1_place_franka_avocado05d_O02_01048620_1690.json
../tests/1-1_place_franka_beer07d_O02_01048625_91e1.json
../tests/1-1_place_franka_can13d_O02_01048658_e9a1.json
../tests/1-1_place_franka_dbottle04d_O02_01049070_38b7.json
../tests/1-1_place_franka_potato18d_O02_01049048_9fb2.json
../tests/1-1_place_franka_wbottle11d_O02_01049082_d8a4.json
../tests/1-1_place_franka_apple13d_O02_01048988_09b0.json
../tests/1-1_place_franka_egg04d_O02_01048656_a3f0.json
../tests/1-1_place_franka_cup03d_O02_01622004_d37b.json
../tests/1-1_place_franka_lemon03d_O02_01621718_2818.json
../tests/1-2_place_franka_potato17d_O04_01150021_c37f.json
../tests/1-2_place_franka_tangerine06d_O03_01050375_2503.json
../tests/1-2_place_franka_fcan04d_O05_01250045_e0a8.json
../tests/1-2_place_franka_orange12d_O04_01150190_df9e.json
../tests/1-2_place_franka_peach02d_O03_01050238_9c43.json
../tests/1-2_place_franka_egg13d_O02_01049028_9e3d.json
../tests/1-2_place_franka_beer07d_O04_01150287_1270.json
../tests/1-2_place_franka_avocado06d_O03_01050247_9766.json
../tests/1-2_place_franka_lemon03d_O03_01050300_20ba.json
../tests/1-2_place_franka_apple12d_O04_01150235_caaa.json
../tests/1-3_long-horizon_franka_apple19d_O03_01051606_af73.json
../tests/1-3_long-horizon_franka_fcan03d_O03_01051534_43f0.json
../tests/1-3_long-horizon_franka_fcan11d_O03_01060604_0679.json
../tests/1-3_long-horizon_franka_lemon06d_O03_01060576_5305.json
../tests/1-3_long-horizon_franka_lime02d_O03_01051568_4973.json
../tests/1-3_long-horizon_franka_avocado05d_O04_01051722_1abe.json
../tests/1-3_long-horizon_franka_egg04d_O04_01060705_f5f0.json
../tests/1-3_long-horizon_franka_kiwi05d_O04_01051742_a2d5.json
../tests/1-3_long-horizon_franka_lemon06d_O04_01051735_6ace.json
../tests/1-3_long-horizon_franka_tomato03d_O04_01051726_3e60.json
../tests/2-1_place_franka_beer09d_O03_01150509_472f.json
../tests/2-1_place_franka_wbottle12d_O03_01150548_418c.json
../tests/2-1_place_franka_cup03d_O03_01050304_5362.json
../tests/2-1_place_franka_dbottle02d_O03_01050315_2e40.json
../tests/2-1_place_franka_avocado01d_O03_01050191_8482.json
../tests/2-1_place_franka_fcan11d_O03_01050130_dc3e.json
../tests/2-1_place_franka_lemon04d_O03_01150557_bdac.json
../tests/2-1_place_franka_can11d_O05_01250064_1b1f.json
../tests/2-1_place_franka_peach01d_O03_01050401_66e6.json
../tests/2-1_place_franka_orange03d_O05_01250241_af42.json

Disk after extraction:
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  255G   32G  90% /


## simulate.py result
exit_status=0
log=/home/redafrix/tests/internship/isaac_dynamicVLA-test/logs/simulate_place_franka_dom_test_n1.log

Important lines:
[DEBUG] 2026-06-11 11:07:40,372 Using selector: EpollSelector
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'any' as 'Any'
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'bool' as 'Bool' and array 'BoolArray
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'bundle' as 'Bundle'
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'colord[3]' as 'Color3d' and array 'Color3dArray
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'colorf[3]' as 'Color3f' and array 'Color3fArray
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'colorh[3]' as 'Color3h' and array 'Color3hArray
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'colord[4]' as 'Color4d' and array 'Color4dArray
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'colorf[4]' as 'Color4f' and array 'Color4fArray
[DEBUG] 2026-06-11 11:07:44,935 Defining data type 'colorh[4]' as 'Color4h' and array 'Color4hArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'double' as 'Double' and array 'DoubleArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'double[2]' as 'Double2' and array 'Double2Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'double[3]' as 'Double3' and array 'Double3Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'double[4]' as 'Double4' and array 'Double4Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'execution' as 'Execution'
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'float' as 'Float' and array 'FloatArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'float[2]' as 'Float2' and array 'Float2Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'float[3]' as 'Float3' and array 'Float3Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'float[4]' as 'Float4' and array 'Float4Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'frame[4]' as 'Frame' and array 'FrameArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'half' as 'Half' and array 'HalfArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'half[2]' as 'Half2' and array 'Half2Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'half[3]' as 'Half3' and array 'Half3Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'half[4]' as 'Half4' and array 'Half4Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'int' as 'Int' and array 'IntArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'int[2]' as 'Int2' and array 'Int2Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'int[3]' as 'Int3' and array 'Int3Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'int[4]' as 'Int4' and array 'Int4Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'int64' as 'Int64' and array 'Int64Array
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'matrixd[2]' as 'Matrix2d' and array 'Matrix2dArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'matrixd[3]' as 'Matrix3d' and array 'Matrix3dArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'matrixd[4]' as 'Matrix4d' and array 'Matrix4dArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'normald[3]' as 'Normal3d' and array 'Normal3dArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'normalf[3]' as 'Normal3f' and array 'Normal3fArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'normalh[3]' as 'Normal3h' and array 'Normal3hArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'objectId' as 'ObjectId' and array 'ObjectIdArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'path' as 'Path'
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'pointd[3]' as 'Point3d' and array 'Point3dArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'pointf[3]' as 'Point3f' and array 'Point3fArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'pointh[3]' as 'Point3h' and array 'Point3hArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'quatd[4]' as 'Quatd' and array 'QuatdArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'quatf[4]' as 'Quatf' and array 'QuatfArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'quath[4]' as 'Quath' and array 'QuathArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'string' as 'String'
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'target' as 'Target'
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'texcoordd[2]' as 'TexCoord2d' and array 'TexCoord2dArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'texcoordf[2]' as 'TexCoord2f' and array 'TexCoord2fArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'texcoordh[2]' as 'TexCoord2h' and array 'TexCoord2hArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'texcoordd[3]' as 'TexCoord3d' and array 'TexCoord3dArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'texcoordf[3]' as 'TexCoord3f' and array 'TexCoord3fArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'texcoordh[3]' as 'TexCoord3h' and array 'TexCoord3hArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'timecode' as 'Timecode' and array 'TimecodeArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'token' as 'Token' and array 'TokenArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'uchar' as 'UChar' and array 'UCharArray
[DEBUG] 2026-06-11 11:07:44,936 Defining data type 'uint' as 'UInt' and array 'UIntArray
[DEBUG] 2026-06-11 11:07:44,937 Defining data type 'uint64' as 'UInt64' and array 'UInt64Array
[DEBUG] 2026-06-11 11:07:44,937 Defining data type 'vectord[3]' as 'Vector3d' and array 'Vector3dArray
[DEBUG] 2026-06-11 11:07:44,937 Defining data type 'vectorf[3]' as 'Vector3f' and array 'Vector3fArray
[DEBUG] 2026-06-11 11:07:44,937 Defining data type 'vectorh[3]' as 'Vector3h' and array 'Vector3hArray
2026-06-11 09:07:40 [2ms] [Warning] [omni.ext.plugin] [ext: rendering_modes] Extensions config 'extension.toml' doesn't exist '/home/redafrix/isaac_franka_env_probe/IsaacLab/apps/isaacsim_4_5/rendering_modes' or '/home/redafrix/isaac_franka_env_probe/IsaacLab/apps/isaacsim_4_5/rendering_modes/config'
2026-06-11 09:07:46 [6,267ms] [Warning] [omni.kit.menu.utils.app_menu] add_menu_items: menu [<MenuItemDescription name:'New'>, <MenuItemDescription name:'Open'>, <MenuItemDescription name:'Re-open with New Edit Layer'>, <MenuItemDescription name:'Save'>, <MenuItemDescription name:'Save With[DEBUG] 2026-06-11 11:07:46,767 matplotlib data path: /home/redafrix/isaacsim/exts/omni.isaac.core_archive/pip_prebundle/matplotlib/mpl-data
[DEBUG] 2026-06-11 11:07:46,775 CONFIGDIR=/home/redafrix/.config/matplotlib
[DEBUG] 2026-06-11 11:07:46,777 interactive is False
[DEBUG] 2026-06-11 11:07:46,777 platform is linux
[DEBUG] 2026-06-11 11:07:46,908 CACHEDIR=/home/redafrix/.cache/matplotlib
[DEBUG] 2026-06-11 11:07:46,909 Using fontManager instance from /home/redafrix/.cache/matplotlib/fontlist-v330.json
2026-06-11 09:07:48 [8,377ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults/sceneDb/ambientLightIntensity'
2026-06-11 09:07:48 [8,501ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 7508933632
2026-06-11 09:07:48 [8,501ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid false, within: false
2026-06-11 09:07:48 [8,501ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : decrement: 167690, decrement size: 7433845248
2026-06-11 09:07:48 [8,501ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : New limit 9574251 (slope: 447, intercept: 13179904)
2026-06-11 09:07:48 [8,501ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 4287216384
2026-06-11 09:07:48 [8,501ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid true, within: true
2026-06-11 09:07:59 [19,004ms] [Warning] [carb] Client rtx.scenedb.plugin has acquired [carb::settings::ISettings v1.0] 100 times. Consider accessing this interface with carb::getCachedInterface() (Performance warning)
2026-06-11 09:12:06 [266,715ms] [[WARNING] 2026-06-11 11:12:08,006 Metadata found for unknown object tray00.usd.
[WARNING] 2026-06-11 11:12:08,006 Metadata found for unknown object tray01.usd.
[WARNING] 2026-06-11 11:12:08,006 Metadata found for unknown object tray02.usd.
[WARNING] 2026-06-11 11:12:08,006 Metadata found for unknown object tray03.usd.
[INFO] 2026-06-11 11:12:08,034 Loading scene from /home/redafrix/tests/internship/isaac_dynamicVLA-test/dynamic-vla/../scenes/5a6650a5-b713-4d8f-9c82-5fc49a5f6ea3.usd
[DEBUG] 2026-06-11 11:12:09,033 [Table_00142] Anchor [-0.7256415   1.90135005  0.75305414] collides with Chair_00143
[DEBUG] 2026-06-11 11:12:09,034 [Table_00142] Anchor [0.0794015  1.90135005 0.75305414] collides with Chair_00145
[DEBUG] 2026-06-11 11:12:09,100 [Coffee_Table_00241] Camera side_cam of [-4.37227299 -3.15412997  0.43178865] collides with Wardrobe_00236
[DEBUG] 2026-06-11 11:12:09,101 [Coffee_Table_00241] Camera side_cam of [-4.11851    -3.68324502  0.43178865] collides with Sofa_00240
[INFO] 2026-06-11 11:12:10,182 Using target object: tomato02.usd
[INFO] 2026-06-11 11:12:10,183 Using container object: bowl11.usd
[DEBUG] 2026-06-11 11:12:10,215 Object tags: {'objects': ['red tomato', 'red round tomato', 'round tomato', 'tomato'], 'containers': ['bowl with cyan patterns', 'ceramic bowl with cyan patterns', 'bowl', 'deep bowl', 'ceramic bowl', 'ceramic deep bowl with cyan patterns', 'deep bowl with cyan patterns', 'ceramic deep bowl']}
2026-06-11 09:12:08 [267,992ms] [Warning] [root] Metadata found for unknown object tray00.usd.
2026-06-11 09:12:08 [267,992ms] [Warning] [root] Metadata found for unknown object tray01.usd.
2026-06-11 09:12:08 [267,992ms] [Warning] [root] Metadata found for unknown object tray02.usd.
2026-06-11 09:12:08 [267,992ms] [Warning] [root] Metadata found for unknown object tray03.usd.
		Discovered list of instanced prim paths: ['/World/envs/env_0/Robot/panda_link0/visuals', '/World/envs/env_0/Robot/panda_link0/collisions', '/World/envs/env_0/Robot/panda_link1/visuals', '/World/envs/env_0/Robot/panda_link1/collisions', '/World/envs/env_0/Robot/panda_link2/visuals', '/World/envs/env_0/Robot/panda_link2/collisions', '/World/envs/env_0/Robot/panda_link3/visuals', '/World/envs/env_0/Robot/panda_link3/collisions', '/World/envs/env_0/Robot/panda_link4/vi[INFO] 2026-06-11 11:12:40,734 Saving episode place_franka_tomato02d_O02_00000042_e954 with 204 frames.
[DEBUG] 2026-06-11 11:12:49,173 {'objects': ['red tomato', 'red round tomato', 'round tomato', 'tomato'], 'containers': ['bowl with cyan patterns', 'ceramic bowl with cyan patterns', 'bowl', 'deep bowl', 'ceramic bowl', 'ceramic deep bowl with cyan patterns', 'deep bowl with cyan patterns', 'ceramic deep bowl']}
2026-06-11 09:12:14 [274,013ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:12:14 [274,051ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:12:14 [274,072ms] [Warning] [isaaclab.sensors.camera.camera] Isaac Sim 4.5 introduced a bug in Camera and TiledCamera when outputting instance and semantic segmentation outputs for instanceable assets. As a workaround, the instanceable flag on assets will be disabled in the current workflow and may lead to longer load times and increased memory usage.
2026-06-11 09:12:18 [278,928ms] [Warning] [rtx.postprocessing.plugin] DLSS increasing input dimensions: Render resolution of (278, 209) is below minimal input resolution of 300.

# FINAL SUMMARY
- workspace: /home/redafrix/tests/internship/isaac_dynamicVLA-test
- Isaac Sim symlink: /home/redafrix/isaacsim
- Isaac Lab exists: yes
- DynamicVLA exists: yes
- object USD count: 211
- scene USD count: 81
- test JSON count: 90
- test-envs.txt size: 91
- simulate log exists: yes

## Output files
./assets_staging/dom_test/tests/1-1_place_franka_apple13d_O02_01048988_09b0.json | 37116 bytes
./assets_staging/dom_test/tests/1-1_place_franka_avocado05d_O02_01048620_1690.json | 36968 bytes
./assets_staging/dom_test/tests/1-1_place_franka_beer07d_O02_01048625_91e1.json | 37026 bytes
./assets_staging/dom_test/tests/1-1_place_franka_can13d_O02_01048658_e9a1.json | 36968 bytes
./assets_staging/dom_test/tests/1-1_place_franka_cup03d_O02_01622004_d37b.json | 37125 bytes
./assets_staging/dom_test/tests/1-1_place_franka_dbottle04d_O02_01049070_38b7.json | 37064 bytes
./assets_staging/dom_test/tests/1-1_place_franka_egg04d_O02_01048656_a3f0.json | 36947 bytes
./assets_staging/dom_test/tests/1-1_place_franka_lemon03d_O02_01621718_2818.json | 36930 bytes
./assets_staging/dom_test/tests/1-1_place_franka_potato18d_O02_01049048_9fb2.json | 36990 bytes
./assets_staging/dom_test/tests/1-1_place_franka_wbottle11d_O02_01049082_d8a4.json | 37699 bytes
./assets_staging/dom_test/tests/1-2_place_franka_apple12d_O04_01150235_caaa.json | 41483 bytes
./assets_staging/dom_test/tests/1-2_place_franka_avocado06d_O03_01050247_9766.json | 39255 bytes
./assets_staging/dom_test/tests/1-2_place_franka_beer07d_O04_01150287_1270.json | 41684 bytes
./assets_staging/dom_test/tests/1-2_place_franka_egg13d_O02_01049028_9e3d.json | 36849 bytes
./assets_staging/dom_test/tests/1-2_place_franka_fcan04d_O05_01250045_e0a8.json | 43792 bytes
./assets_staging/dom_test/tests/1-2_place_franka_lemon03d_O03_01050300_20ba.json | 39262 bytes
./assets_staging/dom_test/tests/1-2_place_franka_orange12d_O04_01150190_df9e.json | 41780 bytes
./assets_staging/dom_test/tests/1-2_place_franka_peach02d_O03_01050238_9c43.json | 39228 bytes
./assets_staging/dom_test/tests/1-2_place_franka_potato17d_O04_01150021_c37f.json | 41545 bytes
./assets_staging/dom_test/tests/1-2_place_franka_tangerine06d_O03_01050375_2503.json | 39409 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_apple19d_O03_01051606_af73.json | 39480 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_avocado05d_O04_01051722_1abe.json | 41964 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_egg04d_O04_01060705_f5f0.json | 42013 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_fcan03d_O03_01051534_43f0.json | 39463 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_fcan11d_O03_01060604_0679.json | 39445 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_kiwi05d_O04_01051742_a2d5.json | 41904 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_lemon06d_O03_01060576_5305.json | 39431 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_lemon06d_O04_01051735_6ace.json | 41939 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_lime02d_O03_01051568_4973.json | 39387 bytes
./assets_staging/dom_test/tests/1-3_long-horizon_franka_tomato03d_O04_01051726_3e60.json | 41935 bytes
./assets_staging/dom_test/tests/2-1_place_franka_avocado01d_O03_01050191_8482.json | 39255 bytes
./assets_staging/dom_test/tests/2-1_place_franka_beer09d_O03_01150509_472f.json | 39246 bytes
./assets_staging/dom_test/tests/2-1_place_franka_can11d_O05_01250064_1b1f.json | 43897 bytes
./assets_staging/dom_test/tests/2-1_place_franka_cup03d_O03_01050304_5362.json | 39588 bytes
./assets_staging/dom_test/tests/2-1_place_franka_dbottle02d_O03_01050315_2e40.json | 39588 bytes
./assets_staging/dom_test/tests/2-1_place_franka_fcan11d_O03_01050130_dc3e.json | 39229 bytes
./assets_staging/dom_test/tests/2-1_place_franka_lemon04d_O03_01150557_bdac.json | 39087 bytes
./assets_staging/dom_test/tests/2-1_place_franka_orange03d_O05_01250241_af42.json | 43738 bytes
./assets_staging/dom_test/tests/2-1_place_franka_peach01d_O03_01050401_66e6.json | 39185 bytes
./assets_staging/dom_test/tests/2-1_place_franka_wbottle12d_O03_01150548_418c.json | 39181 bytes
./assets_staging/dom_test/tests/2-2_place_franka_apple08d_O03_01050789_b41d.json | 39209 bytes
./assets_staging/dom_test/tests/2-2_place_franka_can12d_O03_01050529_5ba6.json | 39387 bytes
./assets_staging/dom_test/tests/2-2_place_franka_cup02d_O03_01050695_f467.json | 39188 bytes
./assets_staging/dom_test/tests/2-2_place_franka_egg00d_O03_01250873_b050.json | 39310 bytes
./assets_staging/dom_test/tests/2-2_place_franka_fcan04d_O03_01050627_1701.json | 39289 bytes
./assets_staging/dom_test/tests/2-2_place_franka_kiwi00d_O04_01625759_b82c.json | 41633 bytes
./assets_staging/dom_test/tests/2-2_place_franka_lemon14d_O03_01250807_bea5.json | 39243 bytes
./assets_staging/dom_test/tests/2-2_place_franka_orange09d_O03_01250680_6e99.json | 39317 bytes
./assets_staging/dom_test/tests/2-2_place_franka_potato02d_O04_01624132_ad86.json | 41603 bytes
./assets_staging/dom_test/tests/2-2_place_franka_tangerine00d_O04_01626714_9924.json | 41586 bytes
./assets_staging/dom_test/tests/2-3_place_franka_apple20d_O03_01050837_f264.json | 39195 bytes
./assets_staging/dom_test/tests/2-3_place_franka_can13d_O03_01250594_6053.json | 39177 bytes
./assets_staging/dom_test/tests/2-3_place_franka_cup02d_O03_01050695_f467.json | 39174 bytes
./assets_staging/dom_test/tests/2-3_place_franka_egg07d_O03_01250883_c3cf.json | 39199 bytes
./assets_staging/dom_test/tests/2-3_place_franka_fcan17d_O03_01250504_6336.json | 39419 bytes
./assets_staging/dom_test/tests/2-3_place_franka_kiwi00d_O04_01625057_98b5.json | 41584 bytes
./assets_staging/dom_test/tests/2-3_place_franka_lemon15d_O03_01250782_dee9.json | 39226 bytes
./assets_staging/dom_test/tests/2-3_place_franka_orange09d_O03_01250729_3add.json | 39185 bytes
./assets_staging/dom_test/tests/2-3_place_franka_peach01d_O04_01623186_ebff.json | 41695 bytes
./assets_staging/dom_test/tests/2-3_place_franka_tangerine05d_O04_01626203_bc6c.json | 41565 bytes
./assets_staging/dom_test/tests/3-1_place_franka_apple99d_O02_01610325_2a43.json | 36948 bytes
./assets_staging/dom_test/tests/3-1_place_franka_apple99d_O02_01610841_d1f1.json | 36972 bytes
./assets_staging/dom_test/tests/3-1_place_franka_can99d_O02_01080044_571c.json | 37078 bytes
./assets_staging/dom_test/tests/3-1_place_franka_can99d_O02_01610785_5f89.json | 37066 bytes
./assets_staging/dom_test/tests/3-1_place_franka_cup99d_O02_01610039_9412.json | 36883 bytes
./assets_staging/dom_test/tests/3-1_place_franka_cup99d_O02_01610356_a52b.json | 36928 bytes
./assets_staging/dom_test/tests/3-1_place_franka_dbottle99d_O02_01610074_1745.json | 36911 bytes
./assets_staging/dom_test/tests/3-1_place_franka_dbottle99d_O02_01611366_b510.json | 36945 bytes
./assets_staging/dom_test/tests/3-1_place_franka_peach99d_O02_01610119_2f43.json | 36922 bytes
./assets_staging/dom_test/tests/3-1_place_franka_peach99d_O02_01610473_4c0d.json | 36974 bytes
./assets_staging/dom_test/tests/3-2_place_franka_apple00d_O02_01641303_47a0.json | 36988 bytes
./assets_staging/dom_test/tests/3-2_place_franka_avocado08d_O02_01641061_076c.json | 37064 bytes
./assets_staging/dom_test/tests/3-2_place_franka_beer05d_O02_01641571_0bce.json | 37091 bytes
./assets_staging/dom_test/tests/3-2_place_franka_can00d_O02_01641329_c06f.json | 36997 bytes
./assets_staging/dom_test/tests/3-2_place_franka_cup04d_O02_01630239_6853.json | 37127 bytes
./assets_staging/dom_test/tests/3-2_place_franka_egg13d_O02_01641323_e5d6.json | 36931 bytes
./assets_staging/dom_test/tests/3-2_place_franka_fcan04d_O02_01641409_e758.json | 37070 bytes
./assets_staging/dom_test/tests/3-2_place_franka_kiwi07d_O02_01630549_eac1.json | 36962 bytes
./assets_staging/dom_test/tests/3-2_place_franka_lemon02d_O02_01641197_3c18.json | 36905 bytes
./assets_staging/dom_test/tests/3-2_place_franka_orange13d_O02_01186003_bbfe.json | 36874 bytes
./assets_staging/dom_test/tests/3-3_place_franka_apple20d_O02_01660153_2a7c.json | 37838 bytes
./assets_staging/dom_test/tests/3-3_place_franka_avocado01d_O02_01650109_8032.json | 37852 bytes
./assets_staging/dom_test/tests/3-3_place_franka_beer13d_O02_01660041_2302.json | 37938 bytes
./assets_staging/dom_test/tests/3-3_place_franka_can12d_O02_01186110_5554.json | 37764 bytes
./assets_staging/dom_test/tests/3-3_place_franka_cup03d_O02_01650032_d3a8.json | 37965 bytes
./assets_staging/dom_test/tests/3-3_place_franka_egg12d_O02_01650248_8fcb.json | 37785 bytes
./assets_staging/dom_test/tests/3-3_place_franka_fcan08d_O02_01660185_f657.json | 37875 bytes
./assets_staging/dom_test/tests/3-3_place_franka_kiwi05d_O02_01660135_cbfe.json | 37797 bytes
./assets_staging/dom_test/tests/3-3_place_franka_onion04d_O02_01660011_e345.json | 38021 bytes
./assets_staging/dom_test/tests/3-3_place_franka_potato00d_O02_01660238_33f5.json | 37815 bytes
./assets_staging/objects/metadata.json | 36654 bytes
./datasets/place_franka_tomato02d_O02_00000042_e954.h5 | 114687874 bytes
./datasets/place_franka_tomato02d_O02_00000042_e954.json | 37328 bytes
./datasets/place_franka_tomato02d_O02_00000042_e954.mp4 | 1164912 bytes
./IsaacLab/.github/workflows/license-exceptions.json | 6769 bytes
./IsaacLab/scripts/tools/cosmos/transfer1_templates.json | 16698 bytes
./IsaacLab/source/isaaclab/test/controllers/test_configs/pink_ik_gr1_test_configs.json | 3014 bytes
./IsaacLab/tools/template/templates/external/.vscode/extensions.json | 290 bytes
./IsaacLab/tools/template/templates/external/.vscode/tasks.json | 1093 bytes
./IsaacLab/tools/template/templates/external/.vscode/tools/launch.template.json | 4004 bytes
./IsaacLab/tools/template/templates/external/.vscode/tools/settings.template.json | 2376 bytes
./IsaacLab/.vscode/extensions.json | 309 bytes
./IsaacLab/.vscode/tasks.json | 921 bytes
./IsaacLab/.vscode/tools/launch.template.json | 1906 bytes
./IsaacLab/.vscode/tools/settings.template.json | 2546 bytes
./logs/simulate_place_franka_dom_test_n1.log | 245160 bytes

## Disk final
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  256G   31G  90% /
