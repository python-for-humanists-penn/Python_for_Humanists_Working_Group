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
parsed_html = bs4.BeautifulSoup(raw_html)
text_tag = parsed_html.find('text')

def get_article(text):
    data = {}
    
    data['title'] = text['title']
    data['journal'] = text['journal']
    data['volume'] = text['volume']
    data['year'] = text['year']
    
    return data
    
get_article(text_tag)

text_tag.attrs 

# text_tag.get_text()



#==============================================================================
# In preparation for next week: add content to line 33ff., mirroring lines 29-32. You can see the content of our text object if you execute lines 20-38. Execute lines 20-36 to get your current selection (lines 29-32).

                                                                                                                                                                                                           # Execute our code by marking it, and (1) pressing Shift+Enter OR (2) copying it to your IPython console, and pressing Enter twice.
                                                                                                                                                                                                          
#==============================================================================
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
# If you have questions about BeautifulSoup, google "BeautifulSoup" to access the BeautifulSoup documentation.

                                                                                                                                                                                                        # Next week: Move output of get_text as an output to the dictionary.



