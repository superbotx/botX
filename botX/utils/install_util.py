import sys
import os
import json
import zipfile
import urllib.request as urllib2
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
    elif action_type == 'add':
        add_module(payload)
    elif action_type == 'remove':
        remove_module(payload)
    else:
        raise CreateProjectError('Invalid action code', get_help())

def process_add_payload(payload):
    if len(payload) != 2:
        raise CreateProjectError('Invalid add arguments', get_help())
    module_type = payload[0]
    if module_type not in valid_module_types:
        raise CreateProjectError(module_type + ' is not a valid module type', 'botX and external allowed')
    git_url = payload[1]
    url_prefix = git_url[:len(git_prefix)]
    git_info = git_url[len(git_prefix):]
    if url_prefix != git_prefix:
        raise CreateProjectError(git_url + ' is not a valid url', 'Only github download url allowed')
    git_elts = git_info.split('/')
    git_usr = git_elts[0]
    git_proj = git_elts[1]
    git_dir = git_elts[2]
    git_file = git_elts[3]
    if git_dir != 'archive' or '.zip' not in git_file:
        raise CreateProjectError(git_url + ' is not download url', 'Only github download url allowed')
    return module_type, git_url, git_proj

def download_module(git_url, git_proj):
    module_data = urllib2.urlopen(git_url)
    create_if_not_exist('tmp')
    module_filename = 'tmp/' + git_proj + '.zip'
    with open(module_filename, 'wb') as module_file:
        module_file.write(module_data.read())

def add_module(payload):
    module_type, git_url, git_proj = process_add_payload(payload)
    download_module(git_url, git_proj)

def remove_module(payload):
    print('not implemented')

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

def create_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)

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

def create_git_ignore(project_name):
    git_ignore_path = project_name + '/.gitignore'
    ignore_list = git_ignore_list.copy()
    with open(git_ignore_path, 'w') as git_ignore_file:
        for ignore_item in ignore_list:
            git_ignore_file.write(ignore_item + '\n')

def create_init_file(dest_dir):
    with open(dest_dir + '/__init__.py', 'w') as init_file:
        pass

def create_project(payload):
    project_name = process_create_payload(payload)
    create_project_dir(project_name)
    create_botX_json_file(project_name)
    create_git_ignore(project_name)
    os.makedirs(project_name + '/botX_modules')
    create_init_file(project_name + '/botX_modules')
    os.makedirs(project_name + '/external_modules')
    os.makedirs(project_name + '/botXsrc')
    create_init_file(project_name + '/botXsrc')
    install_template(project_name + '/botXsrc/botXexport.py', 'botXexport_template')
    install_template(project_name + '/botXapp.py', 'botXapp_template')
