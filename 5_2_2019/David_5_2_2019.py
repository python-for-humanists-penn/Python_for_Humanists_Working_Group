# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:13:54 2019

@author: florian
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 7 13:56:10 2019
@author: florian
@author: emily
@tidied-up-by: david
"""


#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------

import bs4
import csv
import os
import hashlib




#-------------------------------------------------------------------------------
# Definitions
#-------------------------------------------------------------------------------

def get_text_tags(file):
    """
    Opens a file, parses the html, 
    extracts anything enclosed in the <text> tag, and closes the file.
    """
    
    with open(file) as input_file: 
        raw_html = input_file.read()
        parsed_html = bs4.BeautifulSoup(raw_html, "lxml")
        text_tags = parsed_html.find_all("text")
    return text_tags




def get_article(text):
    """
    For a given in-memory sequence of texts,
    use BS4-parsed tags to create a library
    containing author, title, journal, 
    volume, year, and text.
    """
    
    data = {}
    data["author"] = text["author"]
    data["title"] = text["title"]
    data["journal"] = text["journal"]
    data["volume"] = text["volume"]
    data["year"] = text["year"]
    data["text"] = column_one(text.get_text())
    
    return data


def column_one(text):
    """
    For a given in-memory sequence of texts,
    return the first column of the embedded csv formatted as a string.
    """
     #creates an empty list_of_words
    list_of_words = []     
    #split string into lines
    lines = text.splitlines()
    # create in for-loop: takes text in format
    for line in lines:
        #take each line and split it into its constituent fields
        fields = line.split("\t") #"\t" signifies tab character, instead of comma-separated
        #take the first field from each line    
        item1 = fields[0]
        #append it to a list
        list_of_words.append(item1)

    return " ".join(list_of_words)

def file_name(data):
    """
    Returns a file name consisting of year, author name, 
    and the first three words of the title of a given work.
    """
    parts = []
    parts.append(data['year']) # get = method = ()
    parts.extend(data['author'].split()) # position: default value (defined by individual function)
    parts.extend(data['title'].split()[0:3]) # expression #.extend joins lists together
    name = '-'.join(parts) # join always accepts a sequence
    name = name.replace('|', '-') # replace the 'pipe'-character with a hyphen
    return name

def build_corpus(text_tags):
    """
    Returns a list of libraries defined using get_article
    """
    corpus = []
    for text_tag in text_tags:
        output = get_article(text_tag)
        corpus.append(output)
    return corpus
    
def write_metadata_csv(corpus):
    """
    For a corpus as created in build_corpus,
    create a csv file with the collected metadata
    """
    with open("metadata.csv", "w", newline="") as metadata: # Python closes after with-block
        sequence = 0
        fieldnames = ['filename', 'author', 'title', 'year']
        writer = csv.DictWriter(metadata, fieldnames=fieldnames) # _=_ passing an argument
        writer.writeheader()
        for text_dict in corpus:   
            filenametxt = file_name(text_dict) # preliminary filename
            sequence = sequence + 1
            filenametxt = filenametxt + '-' + str(sequence) + '.txt'
            text_dict['filename'] = filenametxt                                      
            writer.writerow({fn: text_dict[fn] for fn in fieldnames})        

def write_text_files(corpus):
    """
    For a corpus as created in build_corpus,
    
    """
    if not os.path.exists('textfiles'):
        os.mkdir('textfiles')

    for text_dict in corpus:
        filenametxt = text_dict['filename']
        filenametxt = os.path.join('textfiles', filenametxt)
        with open(filenametxt, "w") as textfile:
            textfile.write(text_dict['text'])   # text-key = includes the text :)
    
def write_metadata_row(text_dict):
    """
    For a corpus as created in build_corpus,
    create a csv file with the collected metadata
    """
    if not os.path.exists('csvfiles'):
        os.mkdir('csvfiles')
    
    filenamebase = file_name(text_dict) # preliminary filename
    hash_id = hashlib.sha1(text_dict["text"].encode('utf-8')).hexdigest()
    filenametxt = filenamebase + '-' + str(hash_id) + '.txt'
    filenamecsv = filenamebase + '-' + str(hash_id) + '.csv'
    text_dict['filename'] = filenametxt
    fieldnames = ['filename', 'author', 'title', 'year']
    
    filenamecsv = os.path.join('csvfiles', filenamecsv)
                               
    with open(filenamecsv, "w", newline="") as metadata: # Python closes after with-block
        writer = csv.DictWriter(metadata, fieldnames=fieldnames) # _=_ passing an argument
        writer.writerow({fn: text_dict[fn] for fn in fieldnames})        

def write_text_file(text_dict):
    """
    For a corpus as created in build_corpus,
    
    """
    if not os.path.exists('textfiles'):
        os.mkdir('textfiles')

    filenametxt = text_dict['filename']
    filenametxt = os.path.join('textfiles', filenametxt)
    with open(filenametxt, "w") as textfile:
        textfile.write(text_dict['text'])   # text-key = includes the text :)    


#-------------------------------------------------------------------------------
# Globals
#-------------------------------------------------------------------------------

test_file = "test_1.vrt"

#-------------------------------------------------------------------------------
# Calls
#-------------------------------------------------------------------------------
        
print(os.getcwd())
text_tags = get_text_tags(test_file)
corpus = build_corpus(text_tags)
# write_metadata_csv(corpus)
# write_text_files(corpus)
write_metadata_row(corpus[0])
write_text_file(corpus[0])

#-------------------------------------------------------------------------------
# Experimental Stuff
#-------------------------------------------------------------------------------

"""
The code below is intended as a replacement for the get_text_tags function 
above, because get_text_tags above eats too much memory, so we're going to
try to do it in chunks.
"""


from lxml import etree


def parse_text_chunk(string):  
    
    """
    Parses xml files in chunks, yielding a generator element that, when
    iterated, returns the content of an <s> tag every time it reads the end
    of an <s> tag. (For the moment. Later we want it to be a text tag.)
    
    (I made a few tweaks to this function. Ultimately, I suspected we would 
    like to take a string as the input for this function, 
    rather than the parser, and instead include the "parser =" statement 
    in the definition of the function, so I implemented this below.
    I also pulled the parser.feed line in, and substituted our 
    chunk of text below with a variable, which I've unimaginatively 
    called string. This way we can then focus on writing another function
    that feeds strings into this. -- DCS)
    
    (We also need to figure out how and when to clear what's in the parser 
    -- DCS)
    """
    parser = etree.XMLPullParser(events=('end',))
    parser.feed(string)    
    for action, element in parser.read_events():
        if element.tag == 'text':
            yield etree.tostring(element, pretty_print=True)
            
def get_text_iter(file):
    """
    Opens a file, parses the html, 
    extracts anything enclosed in the <text> tag, and closes the file.
    """
    
    with open(file) as input_file: 
        raw_html = input_file.read()
        for text_xml in parse_text_chunk(raw_html):           
            yield bs4.BeautifulSoup(text_xml, "lxml")
            
for text_tag in get_text_iter(test_file):
    text_dict = get_article(text_tag)
    write_metadata_row(text_dict)
    write_text_file(text_dict)
    

#-------------------------------------------------------------------------------
# Experimental Stuff: globals and calls
#-------------------------------------------------------------------------------

string ='''<s no="s_0001" avs="2.808" surprisal="1.512" avs50="2.007" avs10="1.805">
An	DT	an	An	8.36	6.63	6.55	5.86
<normalised orig="Accompt" auto="true">
Account	NP	Account	Accompt	1.96	0.94	1.16	1.18
</normalised>
of	IN	of	of	0.05	0.29	0.06	0.10
some	DT	some	some	3.06	0.41	2.66	2.04
Books	NPS	Books	Books	2.64	0.62	0.90	0.88
.	SENT	.	.	0.78	0.19	0.72	0.77
</s>'''

parse_text_chunk(string) # for-loop: s-tags
# start: text



"""
Here were some thoughts that occurred to me as I was thinking about the
overall work needing to be done in the project, as it relates to memory.
It seems like what we need to do is:
    1: Read and parse the content of the first <text> tag (what we're working on now)
    2: Write the metadata into a library
    3: Write from that library into the .csv
    4: Write the text for that tag into an appropriate .txt file
    5: Wipe everything from the memory except the "cursor position" in the .vrt file
    6: Repeat steps 1-4 for the each following <text> tag until
       we hit the end of the document.
Given that, I think we won't end up needing to put the dictionaries 
into a corpus as in lines 93-101 above.
""" 