# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 10:38:14 2018

@author: florian
"""

#==============================================================================
# Notes on our meeting on March 12, 2018:
#     
# Jacob introduced us to "ScanTailor" (http://scantailor.org/), an image cleaning tool that you may want to use to polish your image files before you work with pytesseract. Check it out!
#                                     
# Using pytesseract in Python:
# 
# First, go to https://github.com/madmaze/pytesseract, and follow the "INSTALLATION" instructions
# 
# If you want tesseract to recognize languages other than English, make sure to download the appropriate language "training data:" https://github.com/tesseract-ocr/tesseract/wiki. Save the file(s) to your "Tesseract_OCR" folder / the folder that includes tesseract.
# 
#                                                                                                                                                                                                  Use the command line interface (cmd) to run "pip install pytesseract." Pip is a Python installer that enables us to work with tesseract in Python. Before you run the command, make sure to go to the folder that includes tesseract (use the "cd" command).
#                                                                                                                                 
# You can learn more about pip here:                                                                                                                                                                                                
#                                                                                                                                                                                                 https://packaging.python.org/tutorials/installing-packages/#use-pip-for-installing
#                                                                                                                                                                                                  and here:
#                                                                                                                                                                                                https://en.wikipedia.org/wiki/Pip_(package_manager)
#                                                                                                                                                                                                
#                                                                                                                                                                                                Now, follow the instructions in the "USAGE" / "Quickstart" section on https://github.com/madmaze/pytesseract:                                                                                                                                                                                                                                  
# 
# "try:
#     import Image
# except ImportError:
#     from PIL import Image
# import pytesseract
# 
# pytesseract.pytesseract.tesseract_cmd = '<full_path_to_your_tesseract_executable>'
# # Include the above line, if you don't have tesseract executable in your PATH
# # Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
# 
# # Simple image to string
# print(pytesseract.image_to_string(Image.open('test.png')))"
# 
# etc.
# 
# You may get this error message if you use a computer than runs on Windows 7: "OSError: [WinError 6] The handle is invalid"
#                                                                                       
# (We plan to discuss that error next week.)
#==============================================================================















