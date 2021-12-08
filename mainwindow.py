# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout
from TabBar.TabBar import TabBar
from TabPane.TabPane import TabPane


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        tabs = (
            ("欢迎", "Welcome"),
            ("Covid19 概览", "Covid19GeneralView"),
            ("Covid19 图表", "Covid19Charts"),
            ("Covid19 地图", "Covid19Map"),
            ("碰撞老鼠(PySide2 示例)", "CollidingMice"),
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


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
