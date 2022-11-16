from bs4 import BeautifulSoup
import requests
from scrape_topics import scrape_topics

html_text = requests.get('https://www.photovoltaikforum.com/board/10-versicherungen/').text
soup = BeautifulSoup(html_text, 'lxml')
newposts = soup.find_all('ol', class_='tabularListColumns messageGroup wbbThread jsClipboardObject new')


for newpost in newposts:
    newbeitrag = newpost.find('li', class_='columnSubject')
    newtitel = newbeitrag.h3.a.text
    newlink = newbeitrag.h3.a.get('href')
    try:
        post_inhalt = scrape_topics(newlink)
    except:
        post_inhalt = 'empty'
    html_post = requests.get(newlink).text
    try:
        newantworten = newbeitrag.find('span', class_='badge messageGroupCounterMobile').text
    except:
        newantworten = 'no answer found'

    print(f"topic: {newtitel}")
    print(f"number of answers: {newantworten}")
    print(f"link: {newlink}")
    print("***\n")
    print(post_inhalt)
    print("\n***\n")

oldposts = soup.find_all('ol', class_='tabularListColumns messageGroup wbbThread jsClipboardObject')

for oldpost in oldposts:
    oldbeitrag = oldpost.find('li', class_='columnSubject')
    oldtitel = oldbeitrag.h3.a.text
    oldlink = oldbeitrag.h3.a.get('href')

    try:
        post_inhalt = scrape_topics(oldlink)
    except:
        post_inhalt = 'empty'
    html_post = requests.get(oldlink).text
    try:
        oldantworten = oldbeitrag.find('span', class_='badge messageGroupCounterMobile').text
    except:
        oldantworten = 'no answer found'

    print(f"topic: {oldtitel}")
    print(f"number of answers: {oldantworten}")
    print(f"link: {oldlink}")
    print("***\n")
    print(post_inhalt)
    print("\n***\n")


'''
    try:
        oldantworten = oldbeitrag.find('span', class_='badge messageGroupCounterMobile').text
    except:
        oldantworten = 'no answer found'

    print(f"topic: {oldtitel}")
    print(f"number of answers: {oldantworten}")
    print(f"link: {oldlink}")
    print("\n")
    '''



