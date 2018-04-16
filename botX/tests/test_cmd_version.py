from ..utils.install_util import *
from ..utils.exception_util import *
import os

def exec_command(argv):
    action_type, payload = process_argv(argv)
    execute_action(action_type, payload)

def test_commands():
    exec_command(['botX', 'version'])
