# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi
from PyQt5.QtCore import QFile, QIODevice, QPoint, QTimer, QRect
from Welcome.NewYearCountDown.NewYearCountDown import NewYearCountDown
from PyQt5.Qt import QPropertyAnimation, QEasingCurve


class Welcome(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('Welcome/Welcome.ui', self)
        self.textEdit.setMarkdown(self.__readMeReader("README.md"))
        QTimer.singleShot(5000, self.__popupDialog)

    def __popupDialog(self):
        self.__newYearCountDown = NewYearCountDown(self)
        self.__newYearCountDown.show()
        animationEnter = QPropertyAnimation(self.__newYearCountDown, b'pos', self)
        animationEnter.setDuration(2000)
        finishX = (self.width() - self.__newYearCountDown.width()) / 2
        finishY = (self.height() - self.__newYearCountDown.height()) / 2
        animationEnter.setStartValue(QPoint(finishX, 0))
        animationEnter.setEndValue(QPoint(finishX, finishY))
        animationEnter.setEasingCurve(QEasingCurve.OutBounce)
        animationEnter.start()

        animationEnter.finished.connect(self.__closeDialog)

    def __closeDialog(self):
        animationLeave = QPropertyAnimation(self.__newYearCountDown, b'pos', self)
        animationLeave.setDuration(2000)
        finishX = (self.width() - self.__newYearCountDown.width()) / 2
        finishY = (self.height() - self.__newYearCountDown.height()) / 2
        animationLeave.setStartValue(QPoint(finishX, finishY))
        animationLeave.setEndValue(QPoint(self.width(), finishY))
        animationLeave.setEasingCurve(QEasingCurve.InBack)
        animationLeave.start()

        animationLeave.finished.connect(self.__newYearCountDown.close)

    def __readMeReader(self, path):
        readMeFile = QFile(path)
        if not readMeFile.open(QIODevice.ReadOnly | QIODevice.Text):
            return ""

        return str(readMeFile.readAll(), encoding='utf-8')
