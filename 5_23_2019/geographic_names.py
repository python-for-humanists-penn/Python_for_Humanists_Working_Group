#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:00:42 2019

@author: jdummer
"""
values = []

with open('place_names.txt', encoding="latin-1") as places:
    for line in places:
        if line.strip():
            for value in line.split("|"):
                values.append(value.strip())

values.sort()

unique_values = set(values)
# print(unique_values)
values = list(unique_values)
values.sort()

with open('geographic_names.txt', 'w+') as names:
    for name in values:
        names.write("%s\r\n" % (name))
