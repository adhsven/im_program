from bs4 import BeautifulSoup
import requests

def scrape_topics(topiclink):
    #topiclink = 'https://www.photovoltaikforum.com/thread/185804-frage-zu-stringplan/'
    html_text = requests.get(topiclink).text

    soup = BeautifulSoup(html_text, 'lxml')

    posts = soup.find_all('div', class_='messageContent')
    #post_texte = posts.find_all('div',class_='messageText')
    for post in posts:
        try:
            post_text = post.find('div',class_='messageText')
        except:
            post_text = 'no text found'
        print(post_text.text)

