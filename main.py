from you_get import common
from ui.ui_form import Ui_MainWindow
import sys, os
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6 import QtCore
from pyperclip import copy
from webbrowser import open
from requests import get
from backup_engine import netease, QQMusic, kuwo
from backup_engine.batches import NeteaseMulti, kuwoMulti
from multiprocessing import Process as P
import multiprocessing as m

headers = {'User-Agent': "Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
message = "这是一个远古版本，有很多的bug，但是勉强还是能运行的。"

os.chdir(os.path.join(os.path.expanduser('~'),"Desktop"))

# 如果没有安装ffmpeg，这里会给你一个包让你安装。
try:
    os.system("ffmpeg")
except:
    pass

def custom_outer(url):
    if "163" in url:
        if "playlist" in url:
            IDs = NeteaseMulti.getID(url)
            print("e")
            for ID in IDs:
                netease.wyydownloader(ID)
                print(ID)
        else:
            print("f")
            netease.wyydownloader(ID)
    elif 'kuwo' in url:
        if "playlist" in url:
            urls = kuwoMulti.getUrls(url)
            for url in urls:
                get(kuwo.getLink(url),headers=headers)
        else:
            netease.wyydownloader(ID)

def customdownload(url, dir, merge, bool1, q): # 适配多进程
    try:
        if bool1:
            common.any_download(url,output_dir=dir,merge=merge)
        else:
            common.any_download_playlist(url,output_dir=dir,merge=merge)
    except:
        q.put(-1)

class TheMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.openInBrowser.clicked.connect(self.browseIt)
        self.ui.Copyer.clicked.connect(self.copying)
        self.ui.pushtoMotrix.clicked.connect(self.Motrix)
        self.ui.downloader.clicked.connect(self.downloadInside)
        self.ui.obtainer.clicked.connect(self.obtain)

    def browseIt(self):
        for i in self.ui.linksObtained.toPlainText().split("\n"):
            open(i,2)
    
    def copying(self):
        copy(self.ui.linksObtained.toPlainText())
        QMessageBox.information(self,"已复制!","已复制!",QMessageBox.Ok)

    def downloadInside(self):
        urls = []
        url = self.ui.theInput.toPlainText()
        if len(url.split("\n"))>=2:
            urls = url.split("\n")
        def download(url):
            try:
                try:
                    q = m.Queue()
                    p = P(target=customdownload,args=(url,".","True",True,q))
                    p.start(); p.join(); a = q.get()
                    if a == -1:
                        p1 = P(target=customdownload,args=(url,".","True",False,q))
                        p1.start(); p1.join(); a = q.get()
                        if a == -1:   
                            QMessageBox.information(self,"您要下载的链接有可能You-Get引擎不支持下载","尝试使用我自主研发的Beta版本的备用引擎。",QMessageBox.Ok)
                            p2 = P(target=custom_outer,args=([url]))
                            p2.start(); p2.join()
                            return
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        if urls:
            for url in urls:
                QMessageBox.information(self,url+"已在后台下载",url+"已在后台下载",QMessageBox.Ok)
                download(url)
        else:
            QMessageBox.information(self,url+"已在后台下载",url+"已在后台下载",QMessageBox.Ok)
            download(url)

    def obtain(self):
        QMessageBox.information(self,"下个版本会出的","下个版本会出的",QMessageBox.Ok)
    
    def Motrix(self):
        QMessageBox.information(self,"下个版本会出的","下个版本会出的",QMessageBox.Ok)
    
if __name__ == "__main__":
    m.freeze_support()
    app = QApplication(sys.argv)
    window = TheMainWindow()
    window.show()
    sys.exit(app.exec())

