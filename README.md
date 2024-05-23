# Ansible

Ansible is a radically simple IT automation system. It handles
configuration management, application deployment, cloud provisioning,
ad-hoc task execution, network automation, and multi-node orchestration. Ansible makes complex
changes like zero-downtime rolling updates with load balancers easy. More information on the Ansible [website](https://ansible.com/).

## Changes for Custom Facts
- lib/ansible/module_utils/facts/default_collectors.py
- lib/ansible/module_utils/facts/other/personal.py
- test/units/module_utils/facts/test_ansible_collector.py
- test/units/module_utils/facts/test_collectors.py