# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, Qt
from Covid19HttpHelper.Covid19HttpHelper import Covid19HttpHelper
from QSSReader.QSSReader import QSSReader


class Covid19GeneralViewItem(QFrame):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        titleLabel = QLabel(title, self)
        titleLabel.setObjectName("title")
        titleLabel.setAlignment(Qt.AlignHCenter)
        self.__totalLabel = QLabel("0", self)
        self.__totalLabel.setProperty("labelType", "total")
        self.__totalLabel.setAlignment(Qt.AlignHCenter)
        increaseTitleLabel = QLabel("较昨日", self)
        increaseTitleLabel.setObjectName("increaseTitle")
        self.__increaseLabel = QLabel("0", self)
        self.__increaseLabel.setProperty("labelType", "increase")

        increaseHLayout = QHBoxLayout()
        increaseHLayout.setContentsMargins(0, 0, 0, 0)
        increaseHLayout.setSpacing(6)
        increaseHLayout.addStretch(1)
        increaseHLayout.addWidget(increaseTitleLabel)
        increaseHLayout.addWidget(self.__increaseLabel)
        increaseHLayout.addStretch(1)

        mainVLayout = QVBoxLayout()
        mainVLayout.setContentsMargins(0, 0, 0, 0)
        mainVLayout.setSpacing(6)
        mainVLayout.addWidget(titleLabel, 0, alignment=Qt.AlignHCenter)
        mainVLayout.addWidget(self.__totalLabel, 0, alignment=Qt.AlignHCenter)
        mainVLayout.addLayout(increaseHLayout)

        self.setLayout(mainVLayout)

    def setData(self, total, increase):
        self.__totalLabel.setText(str(total))
        increaseString = ("+" if increase >= 0 else "") + str(increase)
        self.__increaseLabel.setText(increaseString)


class Covid19GeneralView(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__itemList = []
        itemInfoList = [("境外输入", "input"),
                        ("无症状感染者", "noSymptom"),
                        ("现有确诊", "storeConfirm"),
                        ("累计确诊", "totalConfirm"),
                        ("累计死亡", "totalDead"),
                        ("累计治愈", "totalHeal")]

        mainGridLayout = QGridLayout()
        mainGridLayout.setContentsMargins(0, 0, 0, 0)
        mainGridLayout.setHorizontalSpacing(20)
        mainGridLayout.setVerticalSpacing(20)
        for i in range(len(itemInfoList)):
            itemInfo = itemInfoList[i]
            item = Covid19GeneralViewItem(itemInfo[0], self)
            item.setObjectName(itemInfo[1])
            self.__itemList.append(item)
            mainGridLayout.addWidget(item, i / 3, i % 3)

        centerFrame = QFrame(self)
        centerFrame.setLayout(mainGridLayout)

        mainHLayout = QHBoxLayout()
        mainHLayout.setContentsMargins(0, 0, 0, 0)
        mainHLayout.addStretch(1)
        mainHLayout.addWidget(centerFrame, 0, alignment=Qt.AlignCenter)
        mainHLayout.addStretch(1)
        self.setLayout(mainHLayout)
        self.setStyleSheet(QSSReader("./Covid19GeneralView/Covid19GeneralView.css"))
        QTimer.singleShot(1000, self.__requestData)

    def __requestData(self):
        h = Covid19HttpHelper(self)
        datas = h.getGeneralView()
        if len(datas) == 0:
            return

        for i in range(len(datas)):
            self.__itemList[i].setData(datas[i][0], datas[i][1])
