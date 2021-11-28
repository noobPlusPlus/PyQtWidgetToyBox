# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QUrl, QObject, pyqtSignal, QTimer
from Covid19HttpHelper.Covid19HttpHelper import Covid19HttpHelper


class ChartsWebClass(QObject):
    setData = pyqtSignal(str, str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def setDatas(self, datas):
        self.setData.emit(datas[0], datas[1], datas[2])


class Covid19Charts(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        webView = QWebEngineView(self)
        webView.load(QUrl.fromLocalFile("/Covid19Charts/charts.html"))
        webView.show()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(webView)
        self.setLayout(layout)

        webChannel = QWebChannel(self)
        self.__webObject = ChartsWebClass(self)
        webChannel.registerObject("webObject", self.__webObject)
        webView.page().setWebChannel(webChannel)

        QTimer.singleShot(1000, self.__requestData)

    def __requestData(self):
        h = Covid19HttpHelper(self)
        datas = h.getChartsData()
        self.__webObject.setDatas(datas)