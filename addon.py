from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

URL1 = "http://podcastfeeds.nbcnews.com/audio/podcast/why-is-this-happening.xml"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/0e/41/9a/39/0e419a39-8b77-4fe4-b948-93852db63118/4548cbd9d993aa7f75a56a6e9d03e290551b3fae7b2e8fa05d694611f504fecbe0aa37243ec306c1bcf35bf14f57a24148e9efc305106273722c6514f23d913c.jpeg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://content.production.cdn.art19.com/images/0e/41/9a/39/0e419a39-8b77-4fe4-b948-93852db63118/4548cbd9d993aa7f75a56a6e9d03e290551b3fae7b2e8fa05d694611f504fecbe0aa37243ec306c1bcf35bf14f57a24148e9efc305106273722c6514f23d913c.jpeg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes():
    soup = mainaddon.get_soup(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes1():
    soup = mainaddon.get_soup(URL1)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
