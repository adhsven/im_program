import csv

from requests_html import HTMLSession

s = HTMLSession()

def get_post_links(page):
    url = f'https://www.photovoltaikforum.com/board/10-versicherungen/?pageNo={page}'
    linklist=[]
    r=s.get(url)
    posts = r.html.find('ol.tabularList li.tabularListRow')

    for post in posts:
        linklist.append(post.find('a',first=True).attrs['href'])
    return linklist

def get_title_and_content(testlink):
    r = s.get(testlink)
    title= r.html.find('h1.contentTitle',first=True).text.strip()
    issues_and_answers = r.html.find('div.messageText p')
    content = []
    for issue in issues_and_answers:
        content.append(issue.text.strip())
    topic = {
        'title': title,
        'conversation': content
    }
    return topic

def save_csv(topics):
    keys = topics[0].keys()

    with open('forum.csv','w') as f:
        dict_writer = csv.DictWriter(f,keys)
        dict_writer.writeheader()
        dict_writer.writerows(topics)



for idx_page in range(1,3):
    links = get_post_links(idx_page)
    topics = []
    for link in links:
        topics.append(get_title_and_content(link))
    #save_csv(topics)
    print(topics)