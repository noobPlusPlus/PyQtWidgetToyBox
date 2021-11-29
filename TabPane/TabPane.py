# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame, QStackedLayout
#from Welcome.Welcome import Welcome
#from Covid19Charts.Covid19Charts import Covid19Charts
#from Covid19Map.Covid19Map import Covid19Map
#from Covid19GeneralView.Covid19GeneralView import Covid19GeneralView


class TabPane(QFrame):
    def __init__(self, buttonNameTuple, parent=None):
        super().__init__(parent)
        self.mainStackedLayout = QStackedLayout(self)
        self.mainStackedLayout.setContentsMargins(0, 0, 0, 0)
        for i in range(len(buttonNameTuple)):
            page = self.__pageFactory(buttonNameTuple[i][1])
            self.mainStackedLayout.addWidget(page)

        self.setLayout(self.mainStackedLayout)

    def setCurrentIndex(self, index):
        self.mainStackedLayout.setCurrentIndex(index)

    def __pageFactory(self, name):
        page = __import__(name + "." + name, fromlist=[name])
        # 实例化，获取方法
        pageClass = getattr(page, name)
        return pageClass(self)

        # python 反射不会用
#        if name == 'Welcome':
#            return Welcome(self)
#        elif name == 'Covid19Charts':
#            return Covid19Charts(self)
#        elif name == 'Covid19Map':
#            return Covid19Map(self)
#        elif name == 'Covid19GeneralView':
#            return Covid19GeneralView(self)
