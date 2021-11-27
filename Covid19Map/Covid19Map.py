﻿# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame, QApplication, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QUrl, QObject, pyqtSignal


class MapWebClass(QObject):
    changeTab = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)


class Covid19Map(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        webView = QWebEngineView(self)
        print(QApplication.applicationDirPath())
        webView.load(QUrl.fromLocalFile("/Covid19Map/map.html"))
        webView.show()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(webView)
        self.setLayout(layout)

        webChannel = QWebChannel(self)
        webObject = MapWebClass(self)
        webChannel.registerObject("webObject", webObject)
        webView.page().setWebChannel(webChannel)
