from requests import get
from json import loads

headers = {'User-Agent': "Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}

def getLink(url):
    ID = url.split("/")[-1]
    a = loads(get("https://kuwo.cn/api/v1/www/music/playUrl?mid=%s" % ID,headers=headers).content.decode(encoding='utf-8'))["data"]
    links = a['data']['url']
    return links