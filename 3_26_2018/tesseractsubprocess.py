#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 16:23:59 2018

@author: davidnelson
"""

# This script uses tesseract without pytesseract for machines that have trouble
# running pytesseract. It will write a new text file with the output.

import os
from subprocess import Popen

poem_names = os.listdir()

for name in poem_names:
    # select relevant files
    if name.startswith('blumenstrausse_1912') and name.endswith('.png'):
        print(f'Processing {name}...')
        filename = name.replace('.png', '') # delete extension; on my computer
            # bash will automatically add the '.txt' extension, but if yours 
            # doesn't, add '.txt' for the new file name
        # now create a list where each item is what you would put on the 
        # command line
        command = ['tesseract', name, '-l', 'deu', filename]
        proc = Popen(command)
