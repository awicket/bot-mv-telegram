from modules.tools import GetJson
import random

def Reddits(key):
    r = 'https://www.reddit.com'
    urls = {}
    urls['asians_gif'] = '/r/asian_gifs/.json?limit=100'
    urls['anal'] = '/r/anal/.json?limit=100'
    urls['asianhotties'] = '/r/asianhotties/.json?limit=100'
    urls['AsiansGoneWild'] = '/r/AsiansGoneWild/.json?limit=100'
    urls['RealGirls'] = '/r/RealGirls/.json?limit=100'
    urls['wallpapers'] = '/r/wallpapers/.json?limit=100'
    if key in urls.keys():
        url = r+urls[key]
    r = GetJson(url)
    try:
        npost = len(r['data']['children'])
        xpost = random.randint(1,npost)
        tits = r['data']['children'][xpost]['data']['url']
        return tits
    except KeyError and TypeError:
        return "Some Error"