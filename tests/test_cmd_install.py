from .botX.utils.install_util import *
from .botX.utils.exception_util import *
import os
import shutil

def exec_command(argv):
    action_type, payload = process_argv(argv)
    execute_action(action_type, payload)

def test_commands():
    exec_command(['botX', 'create', 'test_proj'])
    os.chdir('test_proj')
    exec_command(['botX', 'add', 'external', 'https://github.com/ros-planning/moveit_msgs.git'])
    shutil.rmtree('external_modules/src/moveit_msgs')
    exec_command(['botX', 'install'])
    os.chdir('..')
    shutil.rmtree('test_proj')
