# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QProcess, Qt
from PyQt5.QtWidgets import QFrame, QPushButton, QVBoxLayout


class ScreenShotWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        pushButton = QPushButton("截图", self)
        pushButton.setFixedSize(60, 30)
        mainVLayout = QVBoxLayout()
        mainVLayout.addWidget(pushButton, 0, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
        self.setLayout(mainVLayout)

        QProcess.startDetached("Snipaste/Snipaste.exe")
        pushButton.clicked.connect(self.__onScreenShot)

    def __onScreenShot(self):
        QProcess.startDetached("Snipaste/Snipaste.exe" + " snip")

