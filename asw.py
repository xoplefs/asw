# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:21:20 2020
@author: rnelson2

This is the start of a project that I first thought of just under 5 years ago,
on May 27, 2005, just a few days before the final A Softer World comic.

The spirit of the idea is to look for any sort of pattern in how sentences are
broken up between panels in A Softer World comics, relative to the structure
of the sentences. Because I had often found the breaks to be counter-intuitive,
I might expect a high occurence of the breaks being within major syntactic
constituents/phrases, rather than at their boundaries.

***As a start to this project, this code downloads and saves all ASW comics.***

Next steps would be:

Use OCR to extract the text from all of the comics, using the comic panels as 
a basis to annotate the breaks.

Use NLPT and perhaps statistical packages to look for patterns, if any, within
those break.

"""

import bs4 #beautifulsoup4
import requests

def save_comic(n):
    
    comicnumber = n
    res = requests.get(f'https://www.asofterworld.com/index.php?id={comicnumber}')
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    comic = soup.select("#comicimg > img")
    
    url = comic[0].get('src')
    title = comic[0].get('title')
    filename = url.split('/')[-1]
    print(title)
    print(filename)
    
    imgurl = requests.get(url)
    res.raise_for_status()
    
    with open(f'comics/{comicnumber:04d}_{filename}', 'wb') as img:
        img.write(imgurl.content)

for i in range(1,5):
    save_comic(i)

