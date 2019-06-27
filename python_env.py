#!/usr/bin/env python

import sys
import json
import platform
from distutils.sysconfig import get_python_lib
from pip._internal.operations.freeze import freeze
import subprocess
import yaml

# Version Python
pver = platform.python_version()

# Virtual environment
t = sys.prefix.split('/')
pvirt = t[len(t) - 1]

# Python executable location
pexec = sys.executable

# Pip location (each python version has its own version of pip)
piploc = subprocess.getoutput('which pip')

# PYTHONPATH
ppath = sys.path

# Installed packages: name, version
instpack = []
for requirements in freeze(local_only=True):
    instpack.append(requirements)

# Site-packages location
sploc = get_python_lib()

print('Python version: ' + pver)
print('Python virtual environment name: ' + pvirt)
print('Python executable location: ' + pexec)
print('Pip location: ' + piploc)
print('PYTHONPATH: ' + ', '.join(ppath))
print('Installed packages: ' + ', '.join(instpack))
print('Site-packages location: ' + str(sploc))

format = input('Input json or yaml:')

if format == "json":
    f = open('pythoninfo.' + format, 'w')
    prints = json.dumps({
        'Python version:': pver,
        'Python virtual environment name:': pvirt,
        'Python executable location:': pexec,
        'Pip location:': piploc,
        'PYTHONPATH:': ppath,
        'Site-packages location:': sploc,
        'Installed packages': instpack
    }, indent=4)
    f.write(prints)
    f.close()
elif format == "yaml":
    prints = dict(
        Python_version=pver,
        Python_virtual_environment=pvirt,
        Python_executable_location=pexec,
        Pip_location=piploc,
        PYTHONPATH=ppath,
        Site_packages_location=sploc,
        Installed_packages=instpack,
    )
    with open('pythoninfo.yml', 'w') as outfile:
        yaml.dump(prints, outfile, default_flow_style=False)
