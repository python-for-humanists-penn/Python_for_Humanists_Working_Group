# -*- coding: utf-8 -*-
"""
Created on Thu Feb 7 13:56:10 2019
@ author: emily

"""

import bs4
import csv
with open("test_1.vrt") as input_file:
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
