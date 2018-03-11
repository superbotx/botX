import os
import json
import importlib
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
    import_name = 'botX_modules.' + module_name + '.botXexport'
    target_module = importlib.import_module(import_name)
    target_dict = getattr(target_module, 'botXexport')
    return target_dict
