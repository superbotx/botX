import sys
import os
import json
import zipfile
import subprocess
import shutil
import platform
if sys.version_info[0] < 3:
    import urllib as urllib_alias
else:
    import urllib.request as urllib_alias
from .doc_util import *
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

def check_current_dir():
    current_folder = os.listdir('.')
    if 'botX.json' not in current_folder:
        raise CreateProjectError('botX.json not found', 'Need to execute in project directory')

def execute_action(action_type, payload):
    if action_type == 'create':
        create_project(payload)
    elif action_type == 'version':
        print_version(payload)
    elif action_type == 'add':
        check_current_dir()
        add_module(payload)
    elif action_type == 'remove':
        check_current_dir()
        remove_module(payload)
    elif action_type == 'update':
        check_current_dir()
        update_module(payload)
    elif action_type == 'install':
        check_current_dir()
        install_all()
    elif action_type == 'rebuild':
        check_current_dir()
        catkin_make('external_modules')
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

def process_remove_payload(payload):
    if len(payload) != 2:
        raise CreateProjectError('Invalid remove arguments', get_help())
    module_type = payload[0]
    if module_type not in valid_module_types:
        raise CreateProjectError(module_type + ' is not a valid module type', 'botX and external allowed')
    module_name = payload[1]
    return module_type, module_name

def read_botX_json(filename):
    botX_meta = None
    with open(filename, 'r') as botX_json_file:
        botX_meta = json.loads(botX_json_file.read())
    return botX_meta

def get_zip_roots(namelist):
    roots = []
    for name in namelist:
        elts = name.split('/')
        roots.append(elts[0] + '/')
    roots = list(set(roots))
    return roots

def download_module(module_type, git_url, git_proj):
    module_data = urllib_alias.urlopen(git_url)
    create_if_not_exist('tmp')
    module_filename = 'tmp/' + git_proj + '.zip'
    target_path = None
    if module_type == 'botX':
        target_path = 'botX_modules'
    elif module_type == 'external':
        target_path = 'external_modules/src'
    else:
        raise CreateProjectError(module_type + ' is not valid', get_help())
    with open(module_filename, 'wb') as module_file:
        module_file.write(module_data.read())
    unzip_filename = None
    with zipfile.ZipFile(module_filename) as module_zip:
        zip_roots = get_zip_roots(module_zip.namelist())
        if len(zip_roots) != 1:
            raise CreateProjectError('Only one project allowed, ' + str(len(zip_roots)) + ' detected', 'Check repo')
        unzip_filename = zip_roots[0]
        if module_type == 'botX':
            module_zip.extractall(target_path)
        elif module_type == 'external':
            module_zip.extractall(target_path)
        else:
            raise CreateProjectError(module_type + ' is not valid', get_help())
    os.rename(target_path + '/' + unzip_filename, target_path + '/' + git_proj)

def add_module_to_json(module_type, git_url, git_proj):
    botX_meta = None
    with open('botX.json', 'r') as botX_file:
        botX_meta = json.loads(botX_file.read())
    with open('botX.json', 'w') as botX_file:
        meta_info = {'url': git_url, 'name': git_proj}
        entry_point = None
        if module_type == 'botX':
            entry_point = 'botX_modules'
        elif module_type == 'external':
            entry_point = 'external_modules'
        else:
            raise CreateProjectError(module_type + ' is not valid', get_help())
        botX_meta[entry_point][git_proj] = meta_info
        json.dump(botX_meta, botX_file, indent=4)

def install_modules(module_type, module_dict):
    for module_id, module_info in module_dict.items():
        module_name = module_info['name']
        module_url = module_info['url']
        download_module(module_type, module_url, module_name)

def install_missing_modules(module_type, my_dict, require_dict, recompile=True):
    install_dict = {}
    for require_module_name, require_module_info in require_dict.items():
        if require_module_name not in my_dict:
            install_dict[require_module_name] = require_module_info
    if install_dict:
        install_modules(module_type, install_dict)
    if module_type == 'external' and install_dict and recompile:
        catkin_make('external_modules')

def add_botX_module_dependency(module_name):
    required_botX_json = read_botX_json('botX_modules/' + module_name + '/botX.json')
    project_botX_json = read_botX_json('botX.json')
    required_botX_dict = required_botX_json['botX_modules']
    required_external_dict = required_botX_json['external_modules']
    project_botX_dict = project_botX_json['botX_modules']
    project_external_dict = project_botX_json['external_modules']
    install_missing_modules('botX', project_botX_dict, required_botX_dict)
    install_missing_modules('external', project_external_dict, required_external_dict)

def module_exist(module_type, module_name):
    botX_meta = read_botX_json('botX.json')
    module_cat = None
    if module_type == 'botX':
        module_cat = 'botX_modules'
    elif module_type == 'external':
        module_cat = 'external_modules'
    else:
        raise CreateProjectError(module_type + ' is not valid', get_help())
    module_dict = botX_meta[module_cat]
    if module_name in module_dict:
        return True
    else:
        return False

def add_module(payload, recompile=True):
    module_type, git_url, git_proj = process_add_payload(payload)
    if module_exist(module_type, git_proj):
        raise CreateProjectError(git_proj + ' already exist', 'Remove first or use botX update')
    download_module(module_type, git_url, git_proj)
    if module_type == 'botX':
        add_botX_module_dependency(git_proj)
    if module_type == 'external' and recompile:
        catkin_make('external_modules')
    add_module_to_json(module_type, git_url, git_proj)

def remove_module_from_json(module_type, module_name):
    json_attr = None
    if module_type == 'botX':
        json_attr = 'botX_modules'
    elif module_type == 'external':
        json_attr = 'external_modules'
    else:
        raise CreateProjectError(module_type + ' is not valid', get_help())
    botX_json = read_botX_json('botX.json')
    del botX_json[json_attr][module_name]
    with open('botX.json', 'w') as output_file:
        json.dump(botX_json, output_file, indent=4)

def remove_module_files(module_type, module_name):
    module_path = None
    if module_type == 'botX':
        module_path = 'botX_modules/' + module_name
    elif module_type == 'external':
        module_path = 'external_modules/src/' + module_name
    else:
        raise CreateProjectError(module_type + ' is not valid', get_help())
    shutil.rmtree(module_path)

def remove_module(payload, recompile=True):
    module_type, module_name = process_remove_payload(payload)
    if not module_exist(module_type, module_name):
        raise CreateProjectError(module_name + ' does not exist', 'Check the name again')
    remove_module_files(module_type, module_name)
    remove_module_from_json(module_type, module_name)
    if module_type == 'external' and recompile:
        catkin_make('external_modules')

def remove_all_file(root):
    for filename in os.listdir(root):
        full_path = os.path.join(root, filename)
        if os.path.isfile(full_path):
            os.remove(full_path)
        else:
            shutil.rmtree(full_path)

def install_all():
    create_if_not_exist('botX_modules')
    create_if_not_exist('external_modules')
    create_if_not_exist('external_modules/src')
    botX_meta = read_botX_json('botX.json')
    botX_modules = botX_meta['botX_modules']
    external_modules = botX_meta['external_modules']
    remove_all_file('botX_modules')
    remove_all_file('external_modules')
    os.makedirs('external_modules/src')
    install_missing_modules('botX', {}, botX_modules, False)
    install_missing_modules('external', {}, external_modules, False)
    catkin_make('external_modules')

def update_module(payload):
    remove_module(payload, False)
    add_module(payload)

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
        json.dump(template_cpy, outfile, indent=4)

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

def init_project_git(project_name):
    wd = os.getcwd()
    os.chdir(project_name)
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'commit', '-m', '\"init\"'])
    os.chdir(wd)

def chmod_cfg_files(path):
    for k in os.listdir(path):
        full_path = os.path.join(path, k)
        if '.cfg' in full_path:
                print('calling chmod on ', full_path)
                subprocess.call(['chmod','+x',full_path])
        else:
            try:
                chmod_cfg_files(full_path)
            except:
                print('cannot open ', full_path)

def catkin_make(path):
    os_name = platform.system()
    if os_name != 'Linux':
        print(os_name + ' is not supported', 'Use a Linux machine (Ubuntu 16.04 suggested)')
        return
    print('makding all cfg files executable ...')
    chmod_cfg_files(os.path.join(path, 'src'))
    print('starting catkin_make ...')
    subprocess.call(['catkin_make', '--directory', path])
    print('building finished')

def create_project(payload):
    project_name = process_create_payload(payload)
    create_project_dir(project_name)
    create_botX_json_file(project_name)
    create_git_ignore(project_name)
    os.makedirs(project_name + '/botX_modules')
    create_init_file(project_name + '/botX_modules')
    os.makedirs(project_name + '/external_modules')
    os.makedirs(project_name + '/external_modules/src')
    os.makedirs(project_name + '/botXsrc')
    create_init_file(project_name + '/botXsrc')
    install_template(project_name + '/botXsrc/botXexport.py', 'botXexport_template')
    install_template(project_name + '/botXapp.py', 'botXapp_template')
    init_project_git(project_name)
    catkin_make(project_name + '/external_modules')
