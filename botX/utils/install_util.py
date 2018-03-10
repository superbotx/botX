import sys
import os
import json
from .exception_util import *
from ..configs.config import *
from ..configs.params import *

def process_argv(argv):
    if len(argv) == 1:
        raise CreateProjectError('Too few arguments received', get_help())
    action_type = argv[1]
    if action_type not in allowed_actions:
        raise CreateProjectError('Invalid action code', get_help())
    payload = argv[2:]
    return action_type, payload

def execute_action(action_type, payload):
    if action_type == 'create':
        create_project(payload)
    elif action_type == 'version':
        print_version(payload)
    else:
        raise CreateProjectError('Invalid action code', get_help())

def get_help():
    msg = 'Important argument missing\n\n'
    msg += '==> botX create [project name]\n'
    msg += 'The above command will create a new project in current directory\n\n'
    msg += '==> botX add [module type] [github download url]\n'
    msg += 'The above command add module to the project\n'
    msg += 'module type: botX (botX module) / external (ros module)\n\n'
    msg += '==> botX remove [module type] [module name]\n'
    msg += 'The above command remove added module\n'
    msg += 'module type: botX (botX module) / external (ros module)\n\n'
    return msg

def print_version(payload):
    print(VERSION)

def process_create_payload(payload):
    if len(payload) == 0:
        raise CreateProjectError('No project name found', get_help())
    if len(payload) > 1:
        raise CreateProjectError('Too many information', 'Only project name needed')
    project_name = payload[0]
    return project_name

def create_project_dir(project_name):
    if os.path.exists(project_name):
        raise CreateProjectError(project_name + ' already existed in this directory', 'Use another project name or delete the existing one')
    os.makedirs(project_name)

def create_botX_json_file(project_name):
    template_cpy = botX_json_template.copy()
    template_cpy['name'] = project_name
    with open(project_name + '/botX.json', 'w') as outfile:
        json.dump(template_cpy, outfile)

def install_template(dest_filename, template_name):
    template_path = os.path.join(os.path.dirname(__file__), 'templates/' + template_name + '.py')
    with open(template_path, 'r') as template_file:
        with open(dest_filename, 'w') as dest_file:
            dest_file.write(template_file.read())

def create_project(payload):
    project_name = process_create_payload(payload)
    create_project_dir(project_name)
    os.makedirs(project_name + '/botX_modules')
    os.makedirs(project_name + '/external_modules')
    install_template(project_name + '/test.py', 'test')
