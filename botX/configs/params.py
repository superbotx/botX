allowed_actions = set(['version', 'create', 'add', 'remove', 'update', 'install'])

valid_module_types = set(['botX', 'external'])

git_prefix = 'https://github.com/'

botX_json_template = {
    'name': 'placeholder',
    'version': '0.0.1',
    'botX_modules': {},
    'external_modules': {},
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

help_doc = [
    'Important argument missing\n\n',
    '==> botX create [project name]\n',
    'The above command will create a new project in current directory\n\n',
    '==> botX add [module type] [github download url]\n',
    'The above command add module to the project\n',
    'module type: botX (botX module) / external (ros module)\n\n',
    '==> botX remove [module type] [module name]\n',
    'The above command remove added module\n',
    'module type: botX (botX module) / external (ros module)\n\n',
    '==> botX update [module_type] [module_name]\n',
    'The above command update the module\n',
    'module type: botX (botX module) / external (ros module)\n\n',
    '==> botX install\n',
    'The above command will install all the modules when you first clone the project\n\n'
]
