# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout
from TabBar.TabBar import TabBar
from TabPane.TabPane import TabPane
from NewYearCountDown.NewYearCountDown import NewYearCountDown
from PyQt5.Qt import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import QPoint, QTimer, QRect


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        tabs = (
            ("欢迎", "Welcome"),
            ("Covid19 概览", "Covid19GeneralView"),
            ("Covid19 图表", "Covid19Charts"),
            ("Covid19 地图", "Covid19Map"),
            ("碰撞老鼠", "CollidingMice"),
            )

        self.tabBar = TabBar(tabs, self)
        self.tabBar.setMinimumWidth(200)
        self.tabPane = TabPane(tabs, self)

        mainHLayout = QHBoxLayout()
        mainHLayout.setContentsMargins(0, 0, 0, 0)
        mainHLayout.setSpacing(10)
        mainHLayout.addWidget(self.tabBar)
        mainHLayout.addWidget(self.tabPane, 1)

        centralWidget = QFrame(self)
        centralWidget.setLayout(mainHLayout)
        self.setCentralWidget(centralWidget)
        self.tabBar.changeTab.connect(self.tabPane.setCurrentIndex)
        self.setStyleSheet("background:white")
        self.setMinimumSize(1440, 900)

        #春节倒计时
        QTimer.singleShot(5000, self.__popupDialog)

    #春节倒计时进入动画
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

    #春节倒计时退出动画
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


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
