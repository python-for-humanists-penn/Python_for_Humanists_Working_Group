# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 11:05:45 2018

@author: florian
"""

import requests, os, bs4

url = 'http://xkcd.com'              
os.makedirs('xkcd', exist_ok=True)   
while not url.endswith('#'):
    print(f'Downloading page {url}...')  
    res = requests.get(url)      
    res.raise_for_status()       
   
    soup = bs4.BeautifulSoup(res.text)
    
    comicElem = soup.select('#comic img')   
    if comicElem == []:
         print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            print(f'Downloading image {comicUrl}...')
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        comicNum = url.split("/")[-2]    
        imageFile = open(os.path.join('xkcd', comicNum + "-" + os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

         
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')

#==============================================================================
# Assignment: 
#     
#  Documenting/styling: Make this code comprehensible! Fix the code analysis warnings, and comment on each line of code: why do we need it, what does it do etc. 

#  Reminder: This code was taken from chapter 11 of "Automate the Boring Stuff with Python" [https://automatetheboringstuff.com/chapter11/], Project: Downloading All XKCD Comics. We slightly modified it during today's (4/30/2018) session.

#==============================================================================




