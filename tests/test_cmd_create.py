from .botX.utils.install_util import *
from .botX.utils.exception_util import *
import shutil

def exec_command(argv):
    action_type, payload = process_argv(argv)
    execute_action(action_type, payload)

def test_commands():
    exec_command(['botX', 'create', 'test_proj'])
    shutil.rmtree('test_proj')
