# Ansible cookiecutter template

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for
[ansible](https://www.ansible.com/) roles or playbooks. Including
[molecule](https://github.com/ansible/molecule) for testing.

Uses **debian stretch** by default for testing.

## Compatibility

The following setups are supported:

* Drivers:
  * [docker](https://www.docker.com/)
  * [vagrant](https://www.vagrantup.com/)
    * [virtualbox](https://www.virtualbox.org/)
* Verifiers:
  * [testinfra](https://github.com/philpep/testinfra)

## Variables

### Common

* `project_name`: Name of the role or playbook.
* `project_type`: Type of project, role or playbook.
* `molecule_directory`: Directory name for the **molecule** files.
* `dependency_name`: Dependencies engine for molecule.
* `dependency_enabled`: Boolean to enable the molecule dependencies engine.
* `driver_name`: Driver name.
* `lint_name`: YAML lint checker.
* `provisioner_name`: Ansible.
* `provisioner_lint_name`: Ansible lint checker.
* `scenario_name`: Name for the molecule scenario.
* `verifier_name`: Molecule verifier.
* `verifier_directory`: Name of the testing directory inside molecule.
* `verifier_lint_name`: Verifier lint checker.

### Vagrant Specific

* `provider_name`: Vagrant provider.
* `static_ip`: Static IP for the virtual machine.

## Usage

`cookiecutter ansible_cookiecutter` or `cookiecutter [repo url]`.

## License

License for the original [molecule](https://github.com/ansible/molecule)
configuration files: MIT.

Following modifications: GPLv3

## Author Information

m0wer (at) autistici.org
