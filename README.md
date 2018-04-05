# botX

A easier way to build robots

Current version: pre-alpha developer version, really really unstable and buggy, prepare youself

## How to install?

### Install from source code

> If you want to help me improve

You can install by cloning the repo and do a local installation

`git clone https://github.com/superbotx/botX.git`

`cd botX`

`python setup.py build` (optional)

`python setup.py install`

### Install from pip

You can also install from github by

`pip install git+https://github.com/superbotx/botX.git`

## API documentation: 

### Command name: source

Example: `botX source [file_path]`

Available arguments: 

* file_path: The path to the source file, relative path from project root or absolute path if outside project

### Command name: remove

Example: `botX remove [module type] [module name]`

Available arguments: 

* module name: The name of the module which can be found in botX list

* module_type: The type of module which can be either botX or external

### Command name: update

Example: `botX update [module_type] [module_name]`

Available arguments: 

* module name: The name of the module which can be found in botX list

* module_type: The type of module which can be either botX or external

### Command name: create

Example: `botX create [project name]`

Available arguments: 

* project_name: The name of the project which will be the name of the directory as well

### Command name: install

Example: `botX install`

Available arguments: 

### Command name: rebuild

Example: `botX rebuild`

Available arguments: 

### Command name: version

Example: `botX version`

Available arguments: 

### Command name: add

Example: `botX add [module type] [github download url]`

Available arguments: 

* github download url: The download url is different from git url

* module_type: The type of module which can be either botX or external

