import requests
import re
from bs4 import BeautifulSoup

def get_soup(url1):
    page = requests.get(url1)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup))
    return soup
get_soup("http://podcastfeeds.nbcnews.com/audio/podcast/why-is-this-happening.xml")

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=9):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://content.production.cdn.art19.com/images/0e/41/9a/39/0e419a39-8b77-4fe4-b948-93852db63118/4548cbd9d993aa7f75a56a6e9d03e290551b3fae7b2e8fa05d694611f504fecbe0aa37243ec306c1bcf35bf14f57a24148e9efc305106273722c6514f23d913c.jpeg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://content.production.cdn.art19.com/images/0e/41/9a/39/0e419a39-8b77-4fe4-b948-93852db63118/4548cbd9d993aa7f75a56a6e9d03e290551b3fae7b2e8fa05d694611f504fecbe0aa37243ec306c1bcf35bf14f57a24148e9efc305106273722c6514f23d913c.jpeg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items