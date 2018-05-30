# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:06:58 2018

@author: florian
"""

#==============================================================================
# Royal Society Corpus: https://fedora.clarin-d.uni-saarland.de/rsc/
# 
# Goal: Limit the size of the data passed to Beautiful Soup
#  
# 1. Create a for-loop that reads lines from the big file
#     a. remember line - a good way to remember each line as it comes in is to use the append method #         of a list, beginning with an empty list         
#     b. check if line is a closing text tag: <\text>    
#         i. if it is, save metadata + text into a single file with unique name - to do this, we'll 
#         want to use Beautiful Soup, which accepts strings, but we have a list of strings, so:
#         ".join(list_of_strings) 
#         ii. clear previous remembered lines        
#     c. continue until we run out of lines
# 
#         
# 
# Homework activity:
# 
# For our meeting on the 12th (we will not be meeting on the 5th because of HILT): 
#     1. use the head command to create a smaller test file from Royal..... . vrt:
#         head -n 1,000,000 Royal.... .vrt > test.vrt
#     2. Write a script that does the looping, remembering and joining part of 1. (see above)
#         (optimal: print out the first 1000 characters of each joined string)
#     3. We will do the Beautiful Soup part for the following week (June 19)        
#==============================================================================


