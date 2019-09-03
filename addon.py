from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://revolutionspodcast.libsyn.com/rss"

@plugin.route('/')
def main_menu():
    items = [
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/3/4/5/f/345fbd6a253649c0/RevolutionsLogo_V2.jpg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/3/4/5/f/345fbd6a253649c0/RevolutionsLogo_V2.jpg"},
   ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
