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

headers = {'User-Agent': "Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
message = "这是一个远古版本，有很多的bug，但是勉强还是能运行的。"

# 如果没有安装ffmpeg，这里会给你一个包让你安装。
try:
    os.system("ffmpeg")
except:
    pass

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
                    common.any_download(url,output_dir=".",merge=True)
                    print("a")
                except Exception as e:
                    print(e)
                    try:
                        common.any_download_playlist(url,output_dir=".",merge=True)
                        print("b")
                    except:
                        QMessageBox.information(self,"您要下载的链接有可能You-Get引擎不支持下载","尝试使用我自主研发的Beta版本的备用引擎。",QMessageBox.Ok)
                        print("c")
                        if "163" in url:
                            print("d")
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
                        return
            except Exception as e:
                print(e)
        if urls:
            for url in urls:
                download(url)
                QMessageBox.information(self,url+"的下载任务已完成",url+"的下载任务已完成",QMessageBox.Ok)
        else:
            download(url)
            QMessageBox.information(self,url+"的下载任务已完成",url+"的下载任务已完成",QMessageBox.Ok)

    def obtain(self):
        QMessageBox.information(self,"下个版本会出的","下个版本会出的",QMessageBox.Ok)
    
    def Motrix(self):
        QMessageBox.information(self,"下个版本会出的","下个版本会出的",QMessageBox.Ok)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TheMainWindow()
    window.show()
    sys.exit(app.exec())    