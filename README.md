# botX

| System | Status |
| ------------- |:-------------:|
| CircleCI | [![CircleCI](https://circleci.com/gh/superbotx/botX.svg?style=svg)](https://circleci.com/gh/superbotx/botX) |
| CodeBeat | [![codebeat badge](https://codebeat.co/badges/ec88afd6-002a-43e2-83f0-c5003c45eeb2)](https://codebeat.co/projects/github-com-superbotx-botx-master) |
| Codecov | [![codecov](https://codecov.io/gh/superbotx/botX/branch/master/graph/badge.svg)](https://codecov.io/gh/superbotx/botX) |

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

### Command name: version

Example: `botX version`

Available arguments:

None

### Command name: add

Example: `botX add [module type] [github download url]`

Available arguments:

* module_type: The type of module which can be either botX or external

* github download url: The download url is different from git url

### Command name: source

Example: `botX source [file_path]`

Available arguments:

* file_path: The path to the source file, relative path from project root or absolute path if outside project

### Command name: update

Example: `botX update [module_type] [module_name]`

Available arguments:

* module_type: The type of module which can be either botX or external

* module name: The name of the module which can be found in botX list

### Command name: install

Example: `botX install`

Available arguments:

None

### Command name: create

Example: `botX create [project name]`

Available arguments:

* project_name: The name of the project which will be the name of the directory as well

### Command name: rebuild

Example: `botX rebuild`

Available arguments:

None

### Command name: remove

Example: `botX remove [module type] [module name]`

Available arguments:

* module_type: The type of module which can be either botX or external

* module name: The name of the module which can be found in botX list
