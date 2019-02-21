# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:56:10 2019

@author: florian
"""

#==============================================================================
# Python for Humanists Working Group, 2_7_2019
#==============================================================================


# Work with the Royal Society Corpus: https://fedora.clarin-d.uni-saarland.de/rsc/

# Goals: we want to access and extract information from our text object - like journal, title, volume, year, for example - AND also get the csv itself.

# We need to write a function that takes our text object, processes it, and returns data.


import bs4 
with open('test_1.vrt') as input_file: # you can find the 'test_1.vrt' in our GitHub repository ('royal_society_corpus_sample.vrt')
    raw_html = input_file.read()
parsed_html = bs4.BeautifulSoup(raw_html, "lxml")
text_tag = parsed_html.find('text')

def get_article(text): # simplifying!
    data = {}
    
    data['title'] = text['title']
    data['journal'] = text['journal']
    data['volume'] = text['volume']
    data['year'] = text['year']
    data['text'] = text_tag.get_text()
    
    return data
    
output = get_article(text_tag)

print(output)

text_tag.attrs 



# text_tag.get_text()

print(output['text'][0:1000]) # column structure

# normalized word (first column)




# Goal: Write a function that...

# takes text in format
# splits string into lines
# takes each line and splits it into its constituent fields
# takes first field from each line
# appends it to a list


# string processing command: lines = s.splitlines() # each lines as individual string: "['a', 'b', 'c']"

# fields = s.split('\t') '\' = signifies tab-character # output: "['a', 'b', 'c']"

# to get an item from a list: field[0]
# append item to a new list: new_list = []

# create a for-loop, looping over X; each time, it is going to grab a new item, and append it to a new list

def column_one(text):
    
    for first_column in text:
        list_of_words = []
        lines = str(text).splitlines()
        field = str(lines).split('\t')
        field_zero = field[0]
        list_of_words.append(field_zero)
        
    return list_of_words
    
column_one(output)

print(list_of_)

# save output from column 1 to csv:

print(column_one(output), file = open('test_1.csv', 'w'))







