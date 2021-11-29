# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QUrl, QObject, pyqtSignal, pyqtSlot
from Covid19HttpHelper.Covid19HttpHelper import Covid19HttpHelper


class ChartsWebClass(QObject):
    setData = pyqtSignal(str, str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def setDatas(self, datas):
        self.setData.emit(datas[0], datas[1], datas[2])

    @pyqtSlot()
    def pageLoadFinished(self):
        h = Covid19HttpHelper(self)
        datas = h.getChartsData()
        self.setDatas(datas)


class Covid19Charts(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        webView = QWebEngineView(self)
        settings = webView.settings()
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, False)
        engineProfile = webView.page().profile()
        engineProfile.clearHttpCache()
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
