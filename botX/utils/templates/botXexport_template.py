"""
All the tasks or APIs you developed that you want to reuse need to be exported
here as a dictionary named botXexport. An example is shown below.

example:

from my_task_file import my_task
from my_api_file import my_api

botXexport = {
    'my_task': {
        'module': my_task,
        'type': 'task',
        'inputs': [],
        'outputs': [],
        'requirements': ['camera', 'arm'],
        'description': 'just a example task'
    },
    'my_api': {
        'module': my_api,
        'type': 'api',
        'inputs': [],
        'outputs': [],
        'requirements': ['camera', 'arm'],
        'description': 'just a example api'
    }
}

The module attribute is important and all the rest are for automatic
documentation generation.

Modify the following variable to your needs
"""
botXexport = {}
