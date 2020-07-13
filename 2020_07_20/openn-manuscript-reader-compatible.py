#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:33:00 2020
@author: davidnelson
most recently updated Mon July 13
"""

# test using LJS465, collection ID 0001
# download images and metadata X
# run via wget using subprocess run() to get images X
# $ wget -nd -np -r -A_web.jpg -A.xml -P openn/ljs225 \
#       http://openn.library.upenn.edu/Data/0001/ljs225/
# getting TEI: use requests? or just wget
# using wget - will need to save and read, parse with bs4
# using requests - will save as memory
# user can provide input to pick what manuscript they want
# identify relevant metadata for creating ebook
# plug into EbookLib to make ebook
# Profit!
# https://pypi.org/project/EbookLib/

# import subprocess
from bs4 import BeautifulSoup as soup
from ebooklib import epub
import os
import requests
import re
import shutil
import PySimpleGUI as sg


pwd = os.getcwd()
try:
    os.mkdir('ebook-temp')
except FileExistsError:
    pass
os.chdir('ebook-temp')


# Use pysimplegui to get user input from pop-up windows

sg.theme('DarkAmber')   # Add a touch of color
    
layout = [[sg.Text('Please enter the collection ID for the manuscript from Openn: ')],      
                 [sg.InputText()],  
                 [sg.Text('Please enter the manuscript call number from Openn:')],      
                 [sg.InputText()],
                 [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
                 [sg.Submit(), sg.Cancel()]]      
window = sg.Window('Window Title', layout)    
event, values = window.read()    
window.close()
repo_num = values[0]  
ms_name = values[1]
save_location = values[2]  

# command = ['wget', '-nd', '-np', '-r', '-A', '_web.jpg', '-A.xml', '-P',
#           ms_name,
#           f'http://openn.library.upenn.edu/Data/{repo_num}/{ms_name}/']

# subprocess.run(command)

# with open(f'{ms_name}/{ms_name}_TEI.xml') as f:
#    soup = soup(f, 'xml')  # specify 'xml' so it parses data correctly

# minimum metadata required for epub: identifier, title, language

with open(f'{ms_name}_TEI.xml', 'wb') as f:
    f.write(requests.get(f'http://openn.library.upenn.edu/Data/{repo_num}/{ms_name}/data/{ms_name}_TEI.xml').content)
print('Getting TEI...')

with open(f'{ms_name}_TEI.xml') as f:
    soup = soup(f, 'xml')  # specify 'xml' so it parses data correctly

img_details = soup.find_all('graphic')
img_names = []
for img in img_details:
    if '_web.jpg' in img.get('url'):
        img_names.append(img.get('url')[4:])

print('Getting images...')

for img in img_names:
    with open(f'{img}', 'wb') as f:
        f.write(requests.get(f'http://openn.library.upenn.edu/Data/{repo_num}/{ms_name}/data/web/{img}').content)

print('Images saved.')

book = epub.EpubBook()

# get bibid, if it exists
bibid = soup.find('altIdentifier', attrs={'type': 'bibid'})
print(bibid)
if bibid is None:
    call_number = soup.find('idno', attrs={'type': 'call-number'})
    identifier = 'openn' + call_number.string
else:
    identifier = 'openn' + bibid.idno.string

print('Preparing book metadata...')

book.set_identifier(identifier)

ms_item = soup.find_all('msItem')  

ms_title = ms_item[0].title.string

book.set_title(ms_title)

ms_lang = soup.textLang['mainLang']

book.set_language(ms_lang)

ms_authors = ms_item[0].find_all('author')
print(ms_authors)

authors = []
for i in ms_authors:
    if i.persName: 
        author = i.find('persName').string
    else:
        author = i.find('name').string
        # vernac = i.find('persName', attrs={'type': 'vernacular'})
        # vernac_auth = vernac.string
        # author = f'{author} ({vernac_auth})'
    book.add_author(author)
    authors.append(author)
        
title_author = '<p>' + ', '.join(authors) + '</p>'

# get list of images

# image_list = []
# file_list = os.listdir(ms_name)
# for f in file_list:
#    if 'REF' in f:
#        continue
#    elif f.endswith('jpg'):
#        image_list.append(f)

# image_list.sort()
# print(image_list)

# first image is cover 

book.set_cover(f'{img_names[0]}', open(f'{img_names[0]}', 'rb').read())

# var_holder = {}

# for i in range(10):
#    var_holder['my_var_' + str(i)] = "iterationNumber=="+str(i)

# locals().update(var_holder)
# license, repository, summary

institution = soup.find('institution').string
repository = soup.find('repository').string

if institution is not None:
    repo_info = '<p>' + institution + ', ' + repository + '</p>'
else:
    repo_info = f'<p>{repository}</p>'    


summary = soup.find('summary').string
if summary is None:
    summary = ''
    
licences = []
ms_licence = soup.find_all('licence')
for licence in ms_licence:
    licence_string = licence.string
    licence_string = '<p>' + licence_string + '</p>'
    licences.append(licence_string)

# create list of decoNotes pulled from TEI
deco_notes = soup.find_all('decoNote')
print(deco_notes)
# the first decoNote is a summmary (doesn't have a n)
# create a deco_dict with keys that are the n attribute in decoNote from the
# TEI and values that are the text within decoNote in the TEI
deco_dict = {}

for entry in deco_notes:
  deco_n = entry.get('n')
  deco_dict[deco_n] = entry.string

print(deco_dict) 

# create html content for the title page
title_licence = ''.join(licences)
title_page = epub.EpubHtml(title='Title Page', file_name='title-page.xhtml')
if deco_dict != {}:
    title_content = '<html><head></head><body>' + f'<h1>{ms_title}</h1>' + title_author + repo_info + '<p>' + summary + '</p>' + '<p>Decoration notes: ' + deco_dict[None] + '</p>' + title_licence + '</body></html>'
else:
    title_content = '<html><head></head><body>' + f'<h1>{ms_title}</h1>' + title_author + repo_info + '<p>' + summary + '</p>' + title_licence + '</body></html>'
title_page.content = title_content
book.add_item(title_page)
 

vis_page = soup.find_all('surface')

image_html = []
x = 0
for i in img_names:
    image_src = f'<figure><img src="{i}">'
    caption = vis_page[x].get('n')
    if deco_notes:
    # find the deco_note where deco_note[n] is the same as vis_page[n] 
        if caption in deco_dict:
            image_info = image_src + '<figcaption>' + caption + ': ' + deco_dict[caption] + '</figcaption></figure>'
        else: 
            image_info = image_src + '<figcaption>' + caption + '</figcaption></figure>'
    else: 
        image_info = image_src + '<figcaption>' + caption + '</figcaption></figure>'
    image_html.append(image_info)
    x = x + 1

image_content = '<html><head></head><body>' + ''.join(image_html) + '</body></html>'

images = epub.EpubHtml(title='images', file_name='images.xhtml')
images.content = image_content

book.add_item(images)

image_holder = {}

n = 0
for image in img_names:
    image_holder[f'book_image_{n}'] = epub.EpubImage()
            # media_type='image/jpeg',
            # content=open(image, 'rb').read())
    # file_name = f'image{n}'
    # ei = epub.EpubImage()
    # ei.file_name = f'{image}'
    # ei.media_type = 'image/jpeg'
    # ei.content = open(f'{image}', 'rb').read()
    # book.add_item(ei)
    n = n + 1

image_id = re.search(r'\d+', image_src).group()

book.spine = ['nav', title_page, images]

locals().update(image_holder)

for i in list(locals()):
    if i.startswith('book_image'):
        image_num = re.search(r'\d+', i).group().zfill(4)
        locals()[i].file_name = f'{image_id}_{image_num}_web.jpg'
        locals()[i].media_type = 'image/jpeg'
        locals()[i].content = open(f'{image_id}_{image_num}_web.jpg', 'rb').read()
        book.add_item(locals()[i])
        # book.spine.append(locals()[i])
        # print('I added it to the spine')
# for item in image_holder.keys():
#    book.add_item(item)
#    spine_info.append(item)
#    item.content = f'<html><head></head><body><img src="{ms_name}/{image}"></body></html>'


# find more robust ereader to see if multiple authors can be set

# create chapter
# c1 = epub.EpubHtml(title='Intro', file_name='chap_01.xhtml', lang='hr')
# c1.content=u'<h1>Intro heading</h1><p>Zaba je skocila u baru.</p>'

# add chapter
# book.add_item(c1)

# book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
#             (epub.Section('Simple book'),
#             (c1, ))
#            )

# add default NCX and Nav file
print('I got to line 150!')
book.add_item(epub.EpubNcx())  # required element
book.add_item(epub.EpubNav())  # required element

# define CSS style
style = 'body {background-color: Tomato;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

# add CSS file
book.add_item(nav_css)

# basic spine
print('I got to line 162!')
# book.spine = ['nav', images]

print("I'm making your book now! So friendly!")

os.chdir(pwd)

epub.write_epub(f'{save_location}/{ms_name}.epub', book, {})

shutil.rmtree('ebook-temp')
