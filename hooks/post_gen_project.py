#!/usr/bin/env python
import os
import shutil

PROJECT_TYPE = '{{ cookiecutter.project_type }}'

paths_to_delete_if_playbook = ['defaults',
        '{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/playbook.yml']
paths_to_delete_if_role = ['group_vars']

if PROJECT_TYPE == 'role':
    paths_to_delete = paths_to_delete_if_role
elif PROJECT_TYPE == 'playbook':
    paths_to_delete = paths_to_delete_if_playbook
else:
    raise Exception('Invalid project_type')

if '{{cookiecutter.driver_name}}' != 'docker':
    paths_to_delete.extend([
            '{{cookiecutter.molecule_directory}}/{{cookiecutter.scenario_name}}/Dockerfile.j2'])

def delete_resource(resource):
    if os.path.isfile(resource):
        print "removing file: {}".format(resource)
        os.remove(resource)
    elif os.path.isdir(resource):
        print "removing directory: {}".format(resource)
        shutil.rmtree(resource)

for path in paths_to_delete:
    delete_resource(path)
