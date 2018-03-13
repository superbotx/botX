PROJECT_NAME = 'botX'

PROJECT_DESCRIPTION = 'A easier way to build robots'

VERSION = 'pre-alpha developer version, really really unstable and buggy, prepare youself'

API_DOC = [
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
        'description': 'This command adds module to the project'
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
        'description': 'This command installs all the modules'
    },
    'version': {
        'name': 'version',
        'command': 'botX version',
        'arguments': {},
        'description': 'This command indicates the version of botX'
    }
]
