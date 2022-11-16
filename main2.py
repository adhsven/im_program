import csv
import pandas as pd
from requests_html import HTMLSession


#s = HTMLSession()

def get_post_links(page):
    s = HTMLSession()
    url = f'https://www.photovoltaikforum.com/board/10-versicherungen/?pageNo={page}'
    linklist=[]
    r=s.get(url)
    posts = r.html.find('ol.tabularList li.tabularListRow')

    for post in posts:
        linklist.append(post.find('a',first=True).attrs['href'])
    return linklist

def get_title(testlink):
    s = HTMLSession()
    r = s.get(testlink)
    title = r.html.find('h1.contentTitle',first=True).text.strip()
    return title

def get_content(testlink):
    s = HTMLSession()
    r = s.get(testlink)
    issues_and_answers = r.html.find('div.messageText p')
    content = []
    for issue in issues_and_answers:
        content.append(issue.text.strip())
    return content



#main
df = pd.DataFrame(
    columns=['URL','Topic','Content']
)
for idx_page in range(1,41):
    print(f'scraping page {idx_page}...')
    linklist_page = get_post_links(idx_page)
    for idx_link in linklist_page:
        #current_url = linklist_page(idx_link)
        current_title = get_title(idx_link)
        current_content = get_content(idx_link)

        dict = {'URL': idx_link,
                'Topic': current_title,
                'Content': current_content}
        df = df.append(dict, ignore_index=True)

df.to_csv('firsttry.csv',index=False)





