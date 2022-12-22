from requests import get
from json import loads
from selenium import webdriver
import cloudmusic

headers = {'User-Agent': "Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}

def getID(url):
    IDlist = []
    ID = url.split("id=")[-1]
    playlist = cloudmusic.getPlaylist(ID)
    for x in playlist:
        IDlist.append(x.id)
    return IDlist

