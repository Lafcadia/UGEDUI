from curses.ascii import isdigit
import os, requests, json, sys
from pydub import AudioSegment
from curses.ascii import isdigit
from sre_compile import isstring
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB
from selenium import webdriver

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; \
    en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
apath = os.path.abspath('.')

def IDTester(ID, ignorance=True):
    try:
        if isdigit(ID) == False and ignorance == False:
            #print(f'ID:{ID}出现错误，请检查是否正确。')
            return 0
        if isdigit(ID) == False and ignorance == True:
            ID = str(ID)
            raise IDError
        if isstring(ID) == False:
            ID = str(ID)
    except:
        print(f'ID:{ID}出现错误，请检查是否正确。')
    return ID

class TemplateError(Exception):
    def __init__(self, err):
        print("程序出现了错误: "+err)
        Exception().__init__(self, err)
        
class FanMangError(TemplateError):
    def __init__(self, code):
        err = '网易云音乐出现了系统繁忙，请在几分钟之后重启程序。错误码: %s' % code
        super().__init__(self, err)

class NotExist404(TemplateError):
    def __init__(self):
        err = '您输入的ID指向不存在的音乐。'
        super().__init__(self, err)

class VIPMusicError(TemplateError):
    def __init__(self):
        err = '请使用网易云音乐APP下载VIP音乐。'
        super().__init__(err)

class IDError(TemplateError):
    def __init__(self):
        err = '错误的ID'
        super().__init__(self, err)

def trans_any_audio_types(filepath, input_audio_type, output_audio_type):
    song = AudioSegment.from_file(filepath, input_audio_type)
    filename = filepath.split(".")[0]
    song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")

def setSongInfo(songfilepath, songtitle, songartist, songalbum, songpicpath):
    audio = ID3(songfilepath)
    img = open(songpicpath,'rb')
    audio.update_to_v23() #把可能存在的旧版本升级为2.3
    audio['APIC'] = APIC( #插入专辑图片
                    encoding=3,
                    mime='image/jpeg',
                    type=3, 
                    desc=u'Cover',
                    data=img.read()
                )
    audio['TIT2'] = TIT2( #插入歌名
                    encoding=3,
                    text=[songtitle]
                )
    audio['TPE1'] = TPE1( #插入第一演奏家、歌手、等
                    encoding=3,
                    text=[songartist]
                )
    audio['TALB'] = TALB( #插入专辑名称
                    encoding=3,
                    text=[songalbum]
                )
    audio.save() #记得要保存
    img.close()
    
def wyydownloader(ID):
    '''
    利用官方API实现。
    ID是一个字符串，是网易云音乐的歌曲ID，
    ignorance是一个是否被错误打断的boolean，若为True则忽视VIP歌曲无法下载错误并给予反馈。
    '''
    try:
        ID = IDTester(ID)
        data = requests.get('http://music.163.com/api/song/detail/?id='+ID+'&ids=%5B'+ID+'%5D', headers=headers)
        if data.content == r'{"songs":[],"equalizers":{},"code":200}':
            raise NotExist404
        n = json.loads(data.content)
        name = n['songs'][0]['name']
        creator = n['songs'][0]['artists'][0]['name']
        chunk_size = 1024
        response = requests.get('http://music.163.com/song/media/outer/url?id=%s.mp3' % ID, headers=headers)
        file_size = response.headers.get('Content-Length')
        if file_size is not None:
            file_size = int(file_size)
        with open(f'{name} - {creator}.mp3', mode='wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    except:
        print(ID,"下载失败")

def get_music_info(key_word):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    url = 'https://music.163.com/#/search/m/?s={}'.format(key_word)
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    data_all = driver.find_elements_by_xpath('.//div[@class="item f-cb h-flag  "]')
    data_all += driver.find_elements_by_xpath('.//div[@class="item f-cb h-flag even "]')
    id_, name, author = [], [], []
    for data in data_all:
        id_.append(data.find_element_by_xpath('.//div[@class="td w0"]//a').get_attribute('href').split('=')[1])
        name.append(data.find_element_by_xpath('.//div[@class="td w0"]//b').get_attribute('title'))
        author.append(data.find_element_by_xpath('.//div[@class="td w1"]//a').text)
    return list(zip(name,author,id_))