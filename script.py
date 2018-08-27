from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import csv
import json


cabal = 'http://www.nigeria70.com/nigerian_news_paper/archives/tech_cabal'

def getUrls(archive):
    
    archives = []
    soups = BeautifulSoup(urlopen(archive), 'html.parser')
    getData = soups.find('div', attrs={'class': 'news_story_right_column'})
    
    for a in getData.find_all('a', attrs={'href': re.compile("/nigerian_news_paper/archives/")}):
        archives.append(a['href'])
    print('done with getting archives')
    return archives

getUrls(cabal)

def getHeadline(websiteArr):

    #     for item in websiteArr:
    #         page = urlopen(item)
    #         soup = BeautifulSoup(page, 'html.parser')
    #         div = soup.find('div', attrs={'class': 'holder'})
    #         result = div.find_all(string=re.compile(r'\b(?:%s)\b' % '|'.join(names)))
    #         headlines[item[-7:]] = result
    textItem = []
    for item in websiteArr:
        page = urlopen(item)
        soup = BeautifulSoup(page, 'html.parser')
        div = soup.find('div', attrs={'class': 'holder'})
        for tag in div.find_all(href=re.compile("/nigerian_news_paper"), string=True):
            textItem.append(tag.text)
        headlines[item[-7:]] = textItem
        print('added' + ' ' + item)
        print('done adding to headline')


