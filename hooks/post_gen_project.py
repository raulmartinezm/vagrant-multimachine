#!/usr/bin/env python
import os
from collections import OrderedDict


folders = OrderedDict()

folders['ansible']= [
    'templates',
    'defaults',
    'group_vars',
    'host_vars',
    'roles',
    'templates',
    'files'
]

provisioning_method = '{{ cookiecutter.provisioning }}'

def create_ansible_folders():
    for folder in folders['ansible']:
        try:
            os.mkdir(folder)
            open(folder + '/.empty', 'a').close()
        except OSError:
            pass

if __name__ == '__main__':
    if provisioning_method == 'ansible':
        create_ansible_folders()
