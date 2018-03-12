allowed_actions = set(['version', 'create', 'add', 'remove'])

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
