#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:35:18 2020

@author: jdummer
"""
import subprocess
from ebooklib import epub
from bs4 import BeautifulSoup as soup

# download images and metadata
# use run() to run wget from command line

repo_num = input('Please enter the repository number for the manuscript: ')
ms_name = input('Please give the call number of the manuscript from OPenn: ')

command = ['/usr/local/bin/wget', '-nd', '-np', '-r', '-A', '_web.jpg',
           '-A.xml', '-P', ms_name,
           f'http://openn.library.upenn.edu/Data/{repo_num}/{ms_name}/']

subprocess.run(command)

# use BeautifulSoup to parse xml and create soup object

with open(f'{ms_name}/{ms_name}_TEI.xml') as fp:
    soup = soup(fp, 'xml')

# create epub book
book = epub.EpubBook()

'''minimum metadata required for epub: identifier, title, language
identifier: idno type="call number"
if bibid exists: take: openn + bibid
if not: take: openn + call number'''

'''parse beautifulSoup object to find bibid or call_number and create
identifier, then add to ebook'''

bibid = soup.find('altIdentifier', attrs={'type': 'bibid'})
if bibid is None:
    call_number = soup.find('idno', attrs={'type': 'call-number'})
    identifier = 'openn' + call_number.idno.string
else:
    identifier = 'openn' + bibid.idno.string

book.set_identifier(identifier)

# parse bs to find title and add to ebook

'''ask Doug about title tag and how its used in OPenn, this code assumes that
title is the first <title> tage in first <msItem> tag'''

ms_item = soup.find('msItem')
ms_title = ms_item.title.string
print(ms_title)

book.set_title(ms_title)

# parse bs to find language and add to ebook
# right now uses ISO code from OPenn and assumes ebooklib will accept it
ms_lang = soup.textLang['mainLang']

book.set_language(ms_lang)

# for next time, work on getting images and other metadata
