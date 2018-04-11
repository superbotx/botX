import os
from ..configs.config import *

def get_installation_page():
    content = []
    content.append('---\n')
    content.append('title: ' + 'Installation' + '\n')
    content.append('permalink: /docs/installation' + '/\n')
    content.append('---\n\n')
    for s in INSTALLATION:
        content.append(s + '\n\n')
    str_content = ''.join(s for s in content)
    return str_content

def get_example_page(filename):
    content = []
    title = filename.split('/')[-1].split('.')[0].replace('example_', '').replace('_', ' ').capitalize()
    link = 'permalink: /docs/' + filename.split('/')[-1].split('.')[0]
    with open(filename, 'r') as example_file:
        content.append('---\n')
        content.append('title: ' + title + '\n')
        content.append(link + '/\n')
        content.append('---\n\n')
        content.append('```python\n')
        content.append(example_file.read())
        content.append('```\n')
    str_content = ''.join(s for s in content)
    return str_content

def get_command_pages():
    output = {}
    for API_name, API_elt in API_DOC.items():
        content = []
        content.append('---\n')
        content.append('title: ' + API_elt['name'].capitalize() + '\n')
        content.append('permalink: /docs/' + API_elt['name'] + '/\n')
        content.append('---\n\n')
        content.append('Command name: ' + API_elt['name'] + '\n\n')
        content.append(API_elt['description'] + '\n\n')
        content.append('Example: `' + API_elt['command'] + '`\n\n')
        if len(API_elt['arguments']) == 0:
            content.append('No available arguments\n\n')
        else:
            content.append('Available arguments: \n\n')
        for API_arg, API_arg_des in API_elt['arguments'].items():
            content.append('* ' + API_arg + ': ' + API_arg_des + '\n\n')
        content.append('\n')
        str_content = ''.join(s for s in content)
        doc_filename = API_name + '.md'
        output[doc_filename] = str_content
    return output

def get_readme_content():
    content = []
    content.append('# ' + PROJECT_NAME + '\n\n')
    content.append(' '.join(badge for badge in BADGES) + '\n\n')
    content.append(PROJECT_DESCRIPTION + '\n\n')
    content.append('Current version: ' + VERSION + '\n\n')
    content.append('## How to install?\n\n')
    for s in INSTALLATION:
        content.append(s + '\n\n')
    content.append('## API documentation: \n\n')
    for API_name, API_elt in API_DOC.items():
        content.append('### Command name: ' + API_elt['name'] + '\n\n')
        content.append('Example: `' + API_elt['command'] + '`\n\n')
        content.append('Available arguments: \n\n')
        if not API_elt['arguments']:
            content.append('None\n\n')
        else:
            for API_arg, API_arg_des in API_elt['arguments'].items():
                content.append('* ' + API_arg + ': ' + API_arg_des + '\n\n')
    return ''.join(s for s in content)

def get_help():
    content = []
    content.append(PROJECT_NAME + '\n')
    content.append(PROJECT_DESCRIPTION + '\n')
    content.append('Current version: ' + VERSION + '\n\n')
    content.append('Command ocumentation: \n\n')
    for API_name, API_elt in API_DOC.items():
        content.append('Command name: ' + API_elt['name'] + '\n')
        content.append('Example: `' + API_elt['command'] + '`\n')
        content.append('Available arguments: \n')
        for API_arg, API_arg_des in API_elt['arguments'].items():
            content.append('--' + API_arg + ': ' + API_arg_des + '\n')
        content.append('\n')
    return ''.join(s for s in content)
