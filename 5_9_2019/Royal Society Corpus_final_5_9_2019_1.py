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
   # return name 
    return "text"

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
            
def split_text_chunks(lines):
    
    storage = []
    
    for line in lines:
        storage.append(line)
        if "</text>" in line:
            yield "".join(storage)
            storage = []
                
def get_text_iter(file):
    """
    Opens a file, parses the html, 
    extracts anything enclosed in the <text> tag, and closes the file.
    """
    
    with open(file) as raw_xml: 
        for text_xml in split_text_chunks(raw_xml):           
            text = bs4.BeautifulSoup(text_xml, "lxml").find_all("text") # list
            if text: # if the text-list is not empty
                yield text[0] # yields first item/text tag in the list
            
if __name__ == "__main__": # meaning: if running script directly as a stand-alone script do this work
    test_file = "Royal_Society_Corpus_v2.0.2_final.vrt"
    print(os.getcwd())
           
    for text_tag in get_text_iter(test_file):
        text_dict = get_article(text_tag)
        write_metadata_row(text_dict)
        write_text_file(text_dict)
    
# unicode    FileNotFoundError: [Errno 2] No such file or directory: 'csvfiles\\1737-Abb\\#xE9;-Nolet-J.-T.-Desaguliers-New-Experiments-upon-9fd02508ab578c543f9a49d9b5fdb31f5d7589d9.csv'

                                # TMT: comma in filename
                                
                                # hashes!