# -*- coding: utf-8 -*-
"""
Excercises taken from 'Automate the Boring Stuff with Python' by Al Sweigart

Chapters 8 and 6

Sasha Renninger

2018.02.11
"""

# ------------------------Homework-----------------------------

oz = open('C:\\Users\\sashafr\\Documents\\docs\\plpython\\wizardofoz.txt')
content = oz.read()
print(content)

# ---------------------String Literals-------------------------

# How do we create a string?

my_string = 'Hello World!'

print(my_string)

# How do we create a string that contains quotes?

my_quote_string = 'My cat\'s tail'

print (my_quote_string)

# ------------------Escape Characters-------------------------

# What if I need to use both single quotes and double quotes in my string?

my_quote_filled_string ='My cat\'s tail'

print (my_quote_filled_string)

""" 
Some handy escape characters:
\'    Single quote
\"    Double quote
\t    Tab
\n    New Line
\\    Backslash
"""

playing_with_escape_characters = r"Hello there!\nHow are you?\nI\'m doing fine."

print(playing_with_escape_characters)

# ----------------------Raw Strings------------------------------

# What if I want to print or use my string with the escaped characters in it?

my_raw_string = rf'That is Carol\'s cat {playing_with_escape_characters}'

print(my_raw_string)

# This is not very exciting right now, but it will be SUPER impt for regular expressions!!!!!

# ------------------------Multiline Strings-----------------------------

# How can I print a multiline string without typing the newline (\n) character?

my_multiline_string = """Hello
World!"""

print(my_multiline_string)

# -----------------------Indexing and Slicing---------------------------

# What is the length of my string?

my_string = "Hello World!"

length_of_my_string = len(my_string)

print(length_of_my_string)

# Have someone write the string on the board

# Add indexes for each character

# What character is at index 1?

char_at_index_1 = my_string[1]

print(char_at_index_1)

# What is the index of 'H' in my string? 

# What is the index of '!'?

loc_of_exclamation_point = my_string[-1]

print(loc_of_exclamation_point)

# What if I only wanted to print "Hello" (this is called slicing)

hello = 

print(hello)

slice_from_the_beginning = my_string[:5]

print(slice_from_the_beginning)

slice_from_the_end = my_string[6:]

print(slice_from_the_end)

# Slicing doesn't modify the original string

print(my_string)

# ----------------Testing In and Not In----------------------

hello_check = 'Hello' in my_string
print(hello_check)

HELLO_check = 'HELLO' in my_string
print(HELLO_check)

dog_check = 'dog' in my_string
print(dog_check)

dog_double_check = 'dog' not in my_string
print(dog_double_check)

# -------------------Changing Case----------------------------

screaming_string = my_string.upper()
print(screaming_string)

# What if I want to change my original string instead of creating a new one?





my_string = my_string.lower()
print(my_string)

# Note that nothing changes in the string except for the alphabetic letters

# When would you need to use upper and lower?

# Activity: Ask user 'How are you?' and if they respond 'great' REGARDLESS OF CASE, return one respond. For everything else, return a different response



def activity1():
    print('How are you?')
    feeling = input()
    if feeling.lower() == 'great':
        print('I feel great too.')
    else:
        print('I hope the rest of your day is good.')
        
# How can I check if a string is upper or lower case?

my_string = "Hello World!"
lower_check = my_string.islower()
print(lower_check)

upper_check = my_string.isupper()
print(upper_check)

# How do I make my whole string upper case again?

upper_my_string = 
print(upper_my_string.isupper())

# ----------------------Chaining Methods-------------------

crazy_string = "Hello World".upper().lower().upper()
print(crazy_string)

"""
Some other useful string check methods:

isalpha()        returns True if only letters and is not blank
isalnum()        returns True if only letters and numbers and not blank
isdecimal()      returns True if only numbers and not blank
isspace()        returns True if only spaces, tabs, and newlines and not blank
istitle()        returns True if only words that start with an upper case letter and the rest are lower case
"""
       
print('hello'.isalpha())

print('hello123'.isalpha())

print('hello123'.isalnum())

print('hello'.isalnum())

print('123'.isdecimal())

print('     '.isspace())

print('This Is Title Case'.istitle())
    
print('This Is Title Case 123'.istitle())

print('This Is title Case'.istitle())

print('This IS Title Case'.istitle())

# -------------------Startswith and Endswith--------------------------

print('Hello World!'.startswith('Hello'))

print('Hello World!'.endswith('dog'))

print('Hello World!'.endswith('world!'))

# ------------------Join and Split----------------------------------

# What if I have a list of strings and want to turn them into a single string?

oh_my = ', '.join(['lions', 'tigers', 'bears'])
print(oh_my)

silly_string = 'aaaaahh!!!'.join(['lions', 'tigers', 'bears'])
print(silly_string)

# What about the opposite? What if I have one string and I want to turn it into a list of strings?
me = 'My name is Sasha'

split_me = me.split(' ')
print(split_me)

split_on_s = me.split('s')
print(split_on_s)

"""
Activity - Using what we just learned, first, write a method 
that prints the first 500 characters from your text.

Then, break those 500 characters into a list of lines.

"""