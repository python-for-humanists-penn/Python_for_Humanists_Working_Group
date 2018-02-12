# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:48:28 2018

@author: florian
"""

# Homework assignment:
    # go to https://www.gutenberg.org/
    # Search for a work (can be your favorite text, for example)
    # Open the text file UTF-8
    # copy and paste the text (without the top and bottom parts) into word, and create a .txt file
    # bring the text file to next week's session
    # we will be working with string commands next week (Monday, February 12)

# ASSIGNMENT: Write a function that, when you give it a file name, will read that file into a variable, and print out the first two lines of the file in all CAPS!"

import os # importing this library enables us to run 'pwd' and 'cd' commands (= to look where we are, and to go where we want to go) - we need to know/be/go where we saved our .txt file 

os.getcwd() # running this allows us to find our current location (= we search for the folder in which Python is saved/located on our computer)

# result (as displayed in the IPython console): 
    # os.getcwd()
    # Out[3]: 'C:\\Users\\florian' # There you are, Python!
    
# now, we need to (1) either save the .txt file there, or (2) save it somewhere else, and tell Python to 'go there' (= change the working directory)

# I decided to save the .txt somewhere else, and to 'go' there:

os.chdir("C:\\Users\\florian\\Desktop") # two backslashes ("\\")! - a single backslash "is used to escape characters" in Python (see https://docs.python.org/2.0/ref/strings.html)

os.chdir("C:\\Users\\florian\\Desktop\\Penn_DH_2017\\Python for Humanists\\Python for Humanists Working Group\\2_11_2018") 

# now, I am in the folder where I previously saved "Kleist" (as a .txt file)

f = open ('Kleist', "r") # This opens "KLeist" in Python # if we run it again, we 'open' the file again, and can start looking for line 1, 2 etc. - using the "line = f.readline()" command again and again etc. - all over again

line = f.readline() # running it once shows "Das Bettelweib von Locarno" = the first line (the title) of "Kleist" / Kleist.txt

print(line) # prints "Das Bettelweib von Locarno"

line = f.readline() # I run it five times:

print(line) # prints the fifth line "einem Marchese gehÃ¶riges SchloÃŸ, das man jetzt, wenn man vom St."

# helpful until here: http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

# I do not want to run the command again and again - what can I do?

f = open ('Kleist', "r") # running this allows Python to go back to the text, to start all over again. I found another function: "lines = f.readlines()"! Where is the difference between "line =" and "lines ="? 

lines = f.readlines() # this creates a list of the lines (plural!)/separates the entire text into lines

print(lines) # this prints out all the lines = the entire novella/Kleist/Kleist.txt, split into lines

lines[0] # selects the first line of our list of lines = the title: "Das Bettelweib von Locarno"

lines[1] and lines[2] # = empty lines in my text file

lines[3] # the first line of the actual text
lines[4] # the second line of the actual text

lines[3].upper()  # converts all letters of the text's first line into uppercase letters
lines[4].upper()  # converts all letters of the text's second line into uppercase letters

print(lines[3].upper()+lines[4].upper()) # this prints the first two lines of the actual text (= lines 3 and 4 of the file) in all CAPS!

     # now, we need to write/define a function that combines all of what we have done!
     
def CAPS():
    import os
    import codecs # Python would not read German special letters (ä, ö, ü, ß) in my .txt. Importing this library solved that issue.
    os.chdir("C:\\Users\\florian\\Desktop\\Penn_DH_2017\\Python for Humanists\\Python for Humanists Working Group\\2_11_2018")
    f = codecs.open('Kleist', 'r', 'utf-8') # see my "import codecs" comment)
    lines = f.readlines()
    print(lines[3].upper()+lines[4].upper())
    
CAPS() # do not indent it, otherwise it is still part of the function
    
# done!    

# use help(open) to find information on 'r'
    
    
# meeting 2_12_2018:

# raw string: r'My cat\'s tail' # prints the sentence with the "\" 
# r, f etc. = "flags"
# index: "what goes in sqaure brackets" # in my example: "lines[3]"

                                    
                                                             
                                                               
# Homework assignment: please see Sasha's notes! 



    
  







