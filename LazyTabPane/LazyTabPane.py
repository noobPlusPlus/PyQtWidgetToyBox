# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame, QStackedLayout


class LazyTabPane(QFrame):
    def __init__(self, firstPageName, parent=None):
        super().__init__(parent)
        self.__mainStackedLayout = QStackedLayout(self)
        self.__mainStackedLayout.setContentsMargins(0, 0, 0, 0)
        self.__pageDict = {};
        self.__addWidget(firstPageName)  
        self.setLayout(self.__mainStackedLayout)

    def setCurrentPage(self, pageName):
        pageIndex = self.__pageDict.get(pageName, -1)
        if pageIndex == -1:
            self.__addWidget(pageName)
            pageIndex = self.__pageDict.get(pageName)

        self.__mainStackedLayout.setCurrentIndex(pageIndex)

    def __pageFactory(self, name):
        page = __import__(name + "." + name, fromlist=[name])
        # 实例化，获取方法
        pageClass = getattr(page, name)
        return pageClass(self)

    def __addWidget(self, pageName):
        page = self.__pageFactory(pageName)
        self.__pageDict[pageName] = self.__mainStackedLayout.count();
        self.__mainStackedLayout.addWidget(page)   
