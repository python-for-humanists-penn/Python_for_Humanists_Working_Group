#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:24:59 2019

@author: jdummer
"""

import yaml

yml_lines = []

with open('2019-01-08-oleanna.md', encoding='utf8') as file:
    for line in file:
        if line.strip() == "---":
            break
    for line in file:
        if line.strip() == "---":
            break
        else:
            yml_lines.append(line)

yml_string = "".join(yml_lines)
print(yaml.load(yml_string))
