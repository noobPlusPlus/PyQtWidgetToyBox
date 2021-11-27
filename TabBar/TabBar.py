# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame, QButtonGroup, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from QSSReader.QSSReader import QSSReader


class TabBar(QFrame):
    changeTab = pyqtSignal(int)

    def __init__(self, buttonNameTuple, parent=None):
        super().__init__(parent)
        if len(buttonNameTuple) == 0:
            return

        mainVLayout = QVBoxLayout(self)
        mainVLayout.setContentsMargins(0, 0, 0, 0)
        mainVLayout.setSpacing(0)
        self.buttonGroup = QButtonGroup(self)
        for i in range(len(buttonNameTuple)):
            button = QPushButton(buttonNameTuple[i][0], self)
            button.setCheckable(True)
            mainVLayout.addWidget(button)
            self.buttonGroup.addButton(button, len(self.buttonGroup.buttons()))

        self.setLayout(mainVLayout)
        self.buttonGroup.buttonClicked.connect(self.onButtonClicked)
        self.setStyleSheet(QSSReader("./TabBar/TabBar.css"))
        self.buttonGroup.button(0).click()

    def onButtonClicked(self, button):
        self.changeTab.emit(self.buttonGroup.id(button))
