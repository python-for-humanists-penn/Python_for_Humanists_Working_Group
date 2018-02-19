#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:24:38 2018

@author: davidnelson
"""

# First, we need to print the first 500 characters by line

doeblin = open('/Users/davidnelson/Desktop/Döblin_Ermordung.txt', 'r')

content = doeblin.read(500).splitlines()

print(content)

# If you use readlines, it includes /n

# Alternative solution:

doeblin = open('/Users/davidnelson/Desktop/Döblin_Ermordung.txt', 'r')

content = doeblin.read(500)

list_of_lines = content.split('\n')

print(list_of_lines)
