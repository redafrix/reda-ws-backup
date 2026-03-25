<video controls="" aria-label="PointWorld teaser"><source src="https://point-world.github.io/media/teaser-720p.mp4" type="video/mp4"></video>

## PointWorld is a large pre-trained 3D world model that predicts full-scene 3D point flow from partially observable RGB-D captures and robot actions (represented as 3D point flow).

## Abstract

Humans anticipate, from a glance and a contemplated action of their bodies, how the 3D world will respond, a capability that is equally vital for robotic manipulation. We introduce PointWorld, a large pre-trained 3D world model that unifies state and action in a shared 3D space as 3D point flows: given one or few RGB-D images and a sequence of low-level robot action commands, PointWorld forecasts per-pixel displacements in 3D that respond to the given actions. By representing actions as 3D point flows instead of embodiment-specific action spaces (e.g., joint positions), this formulation directly conditions on physical geometries of robots while seamlessly integrating learning across embodiments. To train our 3D world model, we curate a large-scale dataset spanning real and simulated robotic manipulation in open-world environments, enabled by recent advances in 3D vision and simulated environments, totaling about 2M trajectories and 500 hours across a single-arm Franka and a bimanual humanoid. Through rigorous, large-scale empirical studies of backbones, action representations, learning objectives, partial observability, data mixtures, domain transfers, and scaling, we distill design principles for large-scale 3D world modeling. With a real-time (0.1s) inference speed, PointWorld can be efficiently integrated in the model-predictive control (MPC) framework for manipulation. We demonstrate that a single pre-trained checkpoint enables a real-world Franka robot to perform rigid-body pushing, deformable and articulated object manipulation, and tool use, without requiring any demonstrations or post-training and all from a single image captured in-the-wild.

## Walkthrough Video

![](https://www.youtube.com/watch?v=XPOsCwrYdk0)

## Interactive Results

Pick a scene below to view its RGB-D observations along with model predictions and corresponding ground-truth (played at 1/8× speed for clarity). All samples are unseen during training.

- **Single Checkpoint:** All predictions come from a single pre-trained PointWorld model.
- **Inputs:** Static Calibrated RGB-D Captures (t=0), Robot Point Flow (t=0...T).
- **Outputs:** Full-Scene 3D Point Flow (t=0...T) over the 1 m × 1 m × 1 m workspace in front of the robot.

DROID (real)

BEHAVIOR (simulated)

**NOTE:** The model operates on voxel-downsampled (1.5 cm) point clouds. For visual clarity, we upsample the predictions and and the ground truth by applying the same displacement to all points within each voxel. The green color in ground truth visualization indicate the points that are inaccurate due to occlusion (from 2D trackers used to provide annotations). Note that these points are not used to supervise the model, hence it's often observed that the model predicts better than the ground truth for occluded point flows after training.

## Custom 3D Annotations of Real-World Robotics Dataset

To scale up 3D world modeling, we built a custom annotation pipeline with recent advances in 3D computer vision— [Foundation Stereo](https://nvlabs.github.io/FoundationStereo/), [VGGT](https://vgg-t.github.io/), and [Co-Tracker3](https://cotracker3.github.io/) —to recover high-fidelity metric depth and camera poses aligned to the robot base (shown as a transparent overlay in each visualization). The same pipeline can be applied to other datasets so long as time-aligned stereo RGB, robot joint configurations, and sufficient robot visibility are recorded. Both code and annotations will be open-sourced.

Across DROID we annotate roughly 42K episodes (all cameras in each episode), yielding about 400K unique 1-second dense flow trajectories for both scene and robot. This results in the largest real-world dataset for 3D dynamics learning to the best of our knowledge. Below we visualize our annotations alongside the annotations from DROID, which rely on sensor depth and [post-processed extrinsics](https://huggingface.co/KarlP/droid/blob/main/cam2base_extrinsic_superset.json).

## Real-World Experiments

Integrated within a model-predictive control framework, a single pretrained PointWorld model enables diverse manipulation skills without task-specific data or training.

 <video controls=""><source src="https://point-world.github.io/media/videos/book.mp4" type="video/mp4"> </video><video controls=""><source src="https://point-world.github.io/media/videos/tissuebox.mp4" type="video/mp4"> </video><video controls=""><source src="https://point-world.github.io/media/videos/scarf.mp4" type="video/mp4"> </video><video controls=""><source src="https://point-world.github.io/media/videos/pillow.mp4" type="video/mp4"> </video><video controls=""><source src="https://point-world.github.io/media/videos/drawer.mp4" type="video/mp4"> </video><video controls=""><source src="https://point-world.github.io/media/videos/microwave.mp4" type="video/mp4"> </video><video controls=""><source src="https://point-world.github.io/media/videos/duster.mp4" type="video/mp4"> </video><video controls=""><source src="https://point-world.github.io/media/videos/broom.mp4" type="video/mp4"></video>