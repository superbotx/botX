PROJECT_NAME = 'botX'

BADGES = [
    '[![CircleCI](https://circleci.com/gh/superbotx/botX.svg?style=svg)](https://circleci.com/gh/superbotx/botX)',
    '[![codebeat badge](https://codebeat.co/badges/ec88afd6-002a-43e2-83f0-c5003c45eeb2)](https://codebeat.co/projects/github-com-superbotx-botx-master)'
]

PROJECT_DESCRIPTION = 'A easier way to build robots'

VERSION = 'pre-alpha developer version, really really unstable and buggy, prepare youself'

INSTALLATION = [
    '### Install from source code',
    '> If you want to help me improve',
    'You can install by cloning the repo and do a local installation',
    '`git clone https://github.com/superbotx/botX.git`',
    '`cd botX`',
    '`python setup.py build` (optional)',
    '`python setup.py install`',
    '### Install from pip',
    'You can also install from github by',
    '`pip install git+https://github.com/superbotx/botX.git`'
]

API_DOC = {
    'create': {
        'name': 'create',
        'command': 'botX create [project name]',
        'arguments': {
            'project_name': 'The name of the project which will be the name of the directory as well'
        },
        'description': 'This command creates a new project in current directory'
    },
    'add': {
        'name': 'add',
        'command': 'botX add [module type] [github download url]',
        'arguments': {
            'module_type': 'The type of module which can be either botX or external',
            'github download url': 'The download url is different from git url'
        },
        'description': 'This command adds module to the project. If you do not have\
         permission to cfg file, do `chmod +x /path/to/cfg/file`'
    },
    'remove': {
        'name': 'remove',
        'command': 'botX remove [module type] [module name]',
        'arguments': {
            'module_type': 'The type of module which can be either botX or external',
            'module name': 'The name of the module which can be found in botX list'
        },
        'description': 'This command removes module from the project'
    },
    'update': {
        'name': 'update',
        'command': 'botX update [module_type] [module_name]',
        'arguments': {
            'module_type': 'The type of module which can be either botX or external',
            'module name': 'The name of the module which can be found in botX list'
        },
        'description': 'This command updates module in the project'
    },
    'install': {
        'name': 'install',
        'command': 'botX install',
        'arguments': {},
        'description': 'This command installs all the modules. If you do not have permission\
         to cfg file, do `chmod +x /path/to/cfg/file'
    },
    'version': {
        'name': 'version',
        'command': 'botX version',
        'arguments': {},
        'description': 'This command indicates the version of botX'
    },
    'source': {
        'name': 'source',
        'command': 'botX source [file_path]',
        'arguments': {
            'file_path': 'The path to the source file, relative path from project root or absolute path if outside project'
        },
        'description': '[still under construction] This command adds source to the record'
    },
    'rebuild': {
        'name': 'rebuild',
        'command': 'botX rebuild',
        'arguments': {},
        'description': 'This command will rebuild external modules without re-downloading. \
        If you do not have permission to cfg file, do `chmod +x /path/to/cfg/file'
    }
}

DOC_STRUCT = [
    {
        'title': 'Getting Started',
        'docs': ['home', 'installation']
    },
    {
        'title': 'Command Line Interface',
        'docs': [command_name for command_name in API_DOC]
    }
]
