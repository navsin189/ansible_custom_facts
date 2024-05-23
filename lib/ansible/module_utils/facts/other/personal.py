from __future__ import annotations

import os

import ansible.module_utils.compat.typing as t

from ansible.module_utils.facts.collector import BaseFactCollector

file_path = '/home/naveen/Desktop/git_repos/host.txt'

class NaveenFactCollector(BaseFactCollector):
    name = 'personal'
    _fact_ids = set()  # type: t.Set[str]

    def collect(self, module=None, collected_facts=None):
        personal_facts = {}
        personal_facts['personal'] = {}
        if not os.path.exists(file_path):
            return personal_facts

        with open(file_path) as fd:
            content = fd.read()
        content = content.strip().split('\n')
        for line in content:
            if ('[' or ']') in line:
                continue
            content = line.strip().split(' ')
        for comp in content:
            key,value = comp.strip().split('=')
            personal_facts['personal'][key] = value

        return personal_facts
