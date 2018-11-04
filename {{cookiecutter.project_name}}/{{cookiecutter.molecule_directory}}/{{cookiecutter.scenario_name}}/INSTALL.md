{% if cookiecutter.driver_name == 'docker' %}
{% raw -%}
# Install

## Requirements

* Docker Engine
* docker-py

## Install

```bash
sudo pip install docker-py
```
{%- endraw %}
{% elif cookiecutter.driver_name == 'vagrant' %}
{% raw -%}
# Install

## Requirements

* Vagrant
* Virtualbox, Parallels, VMware Fusion, VMware Workstation or VMware Desktop
* python-vagrant

## Install

```
sudo pip install python-vagrant
```
{%- endraw %}
{% endif %}
