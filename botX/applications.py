from __future__ import print_function

import os
import json
import importlib
import subprocess
import uuid
from .utils.exception_util import *

def botXimport(module_name):
    current_files = set(os.listdir('.'))
    if 'botX.json' not in current_files:
        raise CreateProjectError('botX.json not found in current directory', 'Start from project root directory => python botXapp.py')
    botX_meta = None
    with open('botX.json', 'r') as botX_meta_file:
        botX_meta = json.loads(botX_meta_file.read())
    botX_modules = botX_meta['botX_modules']
    if module_name not in botX_modules:
        raise CreateProjectError(module_name + ' not found', 'Install module by => botX add botX ' + module_name)
    import_name = 'botX_modules.' + module_name + '.botXsrc.botXexport'
    target_module = importlib.import_module(import_name)
    target_dict = getattr(target_module, 'botXexport')
    return target_dict

def get_str_uuid():
    uuid_code = uuid.uuid1()
    uuid_str = str(uuid_code)
    return uuid_code

class ExternalCommandPool():

    def __init__(self):
        self.proc_dict = {}

    def start_command(self, command):
        current_env = os.environ
        commands = command.split(' ')
        proc = subprocess.Popen(args=commands, env=current_env)
        proc_id = get_str_uuid()
        self.proc_dict[proc_id] = proc
        return proc_id

    def end_command(self, proc_id):
        if proc_id not in self.proc_dict:
            print(proc_id, ' does not exist')
            return
        self.proc_dict[proc_id].terminate()
        del self.proc_dict[proc_id]

external_command_pool = ExternalCommandPool()
