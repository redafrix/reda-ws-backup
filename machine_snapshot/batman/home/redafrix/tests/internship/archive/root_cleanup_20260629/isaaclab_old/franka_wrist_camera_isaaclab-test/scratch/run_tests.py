import sys
import os

# Add src to python path so that franka_wrist_camera_scene can be imported
repo_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "../franka_wrist_camera_isaaclab/src"))
sys.path.insert(0, repo_src)

# Filter out ROS humble paths which cause dependency conflicts
sys.path = [p for p in sys.path if not p.startswith('/opt/ros/')]
import pytest
sys.exit(pytest.main(['-v']))
