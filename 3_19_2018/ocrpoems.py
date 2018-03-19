#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:41:55 2018

@author: davidnelson
"""

# This script will create a dictionary of poems by extracting text from image
# files. Set your directory to the folder you want to use.

try:    # From the pytesseract documentation at 
        # https://github.com/madmaze/pytesseract 
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os

poem_names = os.listdir() # Gets a list of names

poems = {} # blank dictionary

for name in poem_names:
    if name.startswith('blumenstrausse_1912'): # to get just the relevant files
        print(f'Processing {name}...')
        poems[name] = pytesseract.image_to_string(Image.open(name), lang='deu')
    else:
        print(f'Nope, not {name}!')

print(poems['blumenstrausse_1912_4.png']) # to print a single poem

# Here's the checklist we created before writing this script:

# take all the files and open them and perform OCR
# for every tesseract output, store it in something

# [X] get a list of files in the directory
# [X] get just the relevant files
# [X] create a blank dictionary
# [X] open up a for loop
# [X] open each file
# [X] use tesseract to get a string
# [X] save it to a dictionary where the key is the file name and the value 
#       is the text
