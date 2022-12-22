# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(678, 360)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.preload = QLabel(self.centralwidget)
        self.preload.setObjectName(u"preload")
        self.preload.setGeometry(QRect(20, 20, 181, 171))
        font = QFont()
        font.setFamilies([u"Yuanti SC"])
        font.setPointSize(66)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.preload.setFont(font)
        self.preload.setAlignment(Qt.AlignCenter)
        self.theInput = QPlainTextEdit(self.centralwidget)
        self.theInput.setObjectName(u"theInput")
        self.theInput.setGeometry(QRect(10, 200, 221, 141))
        self.obtainer = QPushButton(self.centralwidget)
        self.obtainer.setObjectName(u"obtainer")
        self.obtainer.setGeometry(QRect(240, 30, 191, 51))
        self.downloader = QPushButton(self.centralwidget)
        self.downloader.setObjectName(u"downloader")
        self.downloader.setGeometry(QRect(240, 80, 191, 51))
        self.pushtoMotrix = QPushButton(self.centralwidget)
        self.pushtoMotrix.setObjectName(u"pushtoMotrix")
        self.pushtoMotrix.setGeometry(QRect(440, 30, 101, 51))
        self.Copyer = QPushButton(self.centralwidget)
        self.Copyer.setObjectName(u"Copyer")
        self.Copyer.setGeometry(QRect(440, 80, 101, 51))
        self.openInBrowser = QPushButton(self.centralwidget)
        self.openInBrowser.setObjectName(u"openInBrowser")
        self.openInBrowser.setGeometry(QRect(550, 30, 111, 101))
        self.linksObtained = QPlainTextEdit(self.centralwidget)
        self.linksObtained.setObjectName(u"linksObtained")
        self.linksObtained.setGeometry(QRect(240, 140, 421, 201))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UGEDUI(\u6709\u4e2a\u5806)", None))
        self.preload.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.theInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740(\u5206\u884c)", None))
        self.obtainer.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u76f4\u94fe", None))
        self.downloader.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6587\u4ef6(\u4e0d\u7a33\u5b9a)", None))
        self.pushtoMotrix.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5230Motrix", None))
        self.Copyer.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u5230\u526a\u8d34\u677f", None))
        self.openInBrowser.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6d4f\u89c8\u5668\u6253\u5f00", None))
        self.linksObtained.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u7684\u76f4\u94fe(\u5206\u884c)", None))
    # retranslateUi

