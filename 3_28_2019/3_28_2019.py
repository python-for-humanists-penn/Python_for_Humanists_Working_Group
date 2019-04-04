# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:17:30 2019

@author: florian
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 7 13:56:10 2019
@ author: emily
"""

import bs4
import csv
with open("test_1.vrt") as input_file: # when the block ends/when it unindents, close file
    raw_html = input_file.read()
parsed_html = bs4.BeautifulSoup(raw_html, "lxml")
#text_tag = parsed_html.find_all("text")
text_tags = parsed_html.find_all("text")

## we want: journal, title, volume, year, + get the CSV itself
## write a function that takes text object, processes it, and returns data

def get_article(text):
    data = {}
    data["author"] = text["author"]
    data["title"] = text["title"]
    data["journal"] = text["journal"]
    data["volume"] = text["volume"]
    data["year"] = text["year"]
    data["text"] = column_one(text.get_text())

    return data
## run that function

def column_one(text):
     #creates an empty list_of_words
     # create in for-loop: takes text in format
     #split string into lines
     #take each line and split it into its constituent fields
     #take the first field from each line
     #append it to a list
     list_of_words = []
     lines = text.splitlines()

     for line in lines:
         fields = line.split("\t") #"\t" signifies tab character, instead of comma-separated
         item1 = fields[0]
         list_of_words.append(item1)

     return " ".join(list_of_words)

max_list_of_words = []

for text_tag in text_tags:
    output = get_article(text_tag)
    max_list_of_words.append(output)

print((max_list_of_words), file = open("output.txt", "w"))

#output = get_article(text_tag)
#print(output)
#text_tag.attrs


#change find to find_all
#create a for loop that looks at find_all, loops over that output, and then appends this structured dictionary into the empty dictionary

#print(output)
#print(output['text'][0:500])



#print(list_of_words)

#column_one(output['text'])
#print(column_one(output['text']))

#csvData = column_one(output)
#with open('test.csv', 'wb') as csvFile:
#    writer = csv.writer(csvFile)
#    writer.writerows(csvData)
#csvFile.close()
## get that CSV with the first column of the data
#text_tag.get_text()

## we'll cover how to run it on every text in the sample
## and then we'll talk about how to break that up into usable chunks of data

#print(list_of_words[0])
## get that CSV with the first column of the data
#text_tag.get_text()

## we'll cover how to run it on every text in the sample
## and then we'll talk about how to break that up into usable chunks of data




#==============================================================================
# 3_21_2019
# 
# Our roadmap:
#     1. assign file names (year, full name of author, first              
#     three words of title, sequential number - all separated               by hyphens)
#     2. save files
#     3. modify each of the dictionaries to add a file name
#     4. save all of the dictionaries to a csv file
# 
# Today: 1.: write a function that takes one of our dictionaries that has been output by the function above (line 60), and returns a file name for that dictionary
#==============================================================================

def file_name(data):
    parts = []
    parts.append(data['year']) # get = method = ()
    parts.extend(data['author'].split()) # position: default value (defined by individual function)
    parts.extend(data['title'].split()[0:3]) # expression #.extend joins lists together
    name = '-'.join(parts) # join always accepts a sequence
    return name

corpus = []

for text_tag in text_tags:
    output = get_article(text_tag)
    print(file_name(output))
    corpus.append(output)
    
with open("metadata.csv", "w", newline="") as metadata: # Python closes after with-block
    sequence = 0
    fieldnames = ['author', 'title', 'year', 'filename']
    writer = csv.DictWriter(metadata, fieldnames=fieldnames) # _=_ passing an argument
    writer.writeheader()
    for text_dict in corpus:   
        filenametxt = file_name(text_dict) 
        sequence = sequence + 1
        filenametxt = filenametxt + '-' + str(sequence) + '.txt'
        text_dict['filename'] = filenametxt                                      
        writer.writerow({fn: text_dict[fn] for fn in fieldnames})        
        
# next week: create for-loop that saves files      
    






# for loop that looks at each item in the list






# writer = csv.writer(file-object) # takes lists
# fieldnames = ['author', 'title', 'year']
# writer = csv.DictWriter(file-object, fieldnames = [])

# print((corpus), file = open("output.txt", "w"))


# 





# Create a for-loop that adds sequential numbers to the file names as well as file extensions.
    
# Use this function in a for-loop to modify the dictionary: add file names to our 'data'-dictionary / append them to the output; then create a separate for-loop to save each of the text files. 

# save all of the dictionaries to a csv file




















