from .botX.application import external_command_pool

def test_trivial_command():
    command = 'ls -A'
    external_command_pool.start_command(command)
