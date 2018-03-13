allowed_actions = set(['version', 'create', 'add', 'remove', 'update', 'install'])

valid_module_types = set(['botX', 'external'])

git_prefix = 'https://github.com/'

botX_json_template = {
    'name': 'placeholder',
    'version': '0.0.1',
    'botX_modules': {},
    'external_modules': {},
    'scripts': {
        'moveit-install': 'sudo apt-get install ros-kinetic-moveit',
        'moveit-source': 'source /opt/ros/kinetic/setup.bash'
    }
}

git_ignore_list = [
    'botX_modules/*',
    'external_modules/*',
    '.DS_Store',
    '*.pyc',
    '__pycache__',
    '!botX_modules/__init__.py',
    'tmp/*'
]
