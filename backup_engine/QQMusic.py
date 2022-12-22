from requests import get
from json import loads

def getLink(url):
    ID = url.split("/")[-1]
    music_info = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module": "CDN.SrfCdnDispatchServer", "method":" "'