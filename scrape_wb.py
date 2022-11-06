# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:33:57 2022

@author: Sven
"""

from bs4 import BeautifulSoup
import requests

#source = requests.get('https://coreyms.com/').text
#soup = BeautifulSoup(source, 'lxml')

#soup.prettify())

#article = soup.find('article')
#print(article.prettify())
#header = article.h2.a.text
#print(header)
# summary = article.find('div', class_='entry-content').p.text
# print(summary)

#vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

#vid_id = vid_src.split('/')[4]
#vid_id = vid_id.split('?')[0]
#print(vid_id)

#yt_link = f'https://youtube.com/watch?v={vid_id}'
#print(yt_link)


source = requests.get('https://www.photovoltaikforum.com/core/search-result/13083397/?highlight=versicherung').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())
tabelle = soup.find('ol',class_='tabularList')
#post = soup.find('li',class_='tabularListRow mobileLinkShadowContainer')
#print(post)
#post = tab.find('li', class_='columnSubject').text
post =  tabelle.tabularListRow.mobileLinkShadowContainer
print(post)

#for postlink in tab.find_all('a'):
    # link = postlink.get('href')
    # print(postlink.text)
    # print(link)