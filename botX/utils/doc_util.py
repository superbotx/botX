from ..configs.config import *

def get_readme_content():
    content = []
    content.append('# ' + PROJECT_NAME + '\n\n')
    content.append(PROJECT_DESCRIPTION + '\n\n')
    content.append('Current version: ' + VERSION + '\n\n')
    content.append('## API documentation: \n\n')
    for API_name, API_elt in API_DOC.items():
        content.append('### API name: ' + API_elt['name'] + '\n\n')
        content.append('Example: `' + API_elt['command'] + '`\n\n')
        content.append('Available arguments: \n\n')
        for API_arg, API_arg_des in API_elt['arguments'].items():
            content.append('* ' + API_arg + ': ' + API_arg_des + '\n\n')
    return ''.join(s for s in content)
