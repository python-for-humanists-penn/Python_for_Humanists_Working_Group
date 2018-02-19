# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:11:03 2018

@author: florian
"""

"""
Activity - Using what we just learned, first, write a method 
that prints the first 500 characters from your text.

Then, break those 500 characters into a list of lines.

"""

# solution:
    
def first_500_characters():
        import os
        import codecs
        os.chdir("C:\\Users\\florian\\Desktop\\Penn_DH_2017\\Python for Humanists\\Python for Humanists Working Group\\2_11_2018")
        f = codecs.open('Kleist', 'r', 'utf-8')
        characters = f.read()
        print(characters[:500])
         
first_500_characters()
    
characters[:500].splitlines()


# ctrl + 4 = commenting out:
    

#==============================================================================
# text
# text
#==============================================================================


 
