# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:21:20 2020
@author: rnelson2
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
    
    imgurl = requests.get(url)
    res.raise_for_status()
    
    with open(f'{comicnumber}.jpg', 'wb') as img:
        img.write(imgurl.content)


for i in range(1):
    save_comic(i + 1)
