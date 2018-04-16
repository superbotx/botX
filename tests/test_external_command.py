from .botX.applications import external_command_pool
import time

def test_trivial_command():
    command = 'ls -A'
    external_command_pool.start_command(command)

def test_ros_command():
    command = 'roscore'
    proc_id = external_command_pool.start_command(command)
    time.sleep(1)
    external_command_pool.end_command(proc_id)
    external_command_pool.end_command('some random pid')
