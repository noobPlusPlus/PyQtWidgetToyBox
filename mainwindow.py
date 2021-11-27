# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout
from TabBar.TabBar import TabBar
from TabPane.TabPane import TabPane


class MainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        tabs = (
            ("欢迎", "Welcome"),
            ("Covid19 图表", "Covid19Charts"),
#            ("Covid19 地图", "Covid19Map"),
            )

        self.tabBar = TabBar(tabs, self)
        self.tabPane = TabPane(tabs, self)

        mainHLayout = QHBoxLayout(self)
        mainHLayout.setContentsMargins(0, 0, 0, 0)
        mainHLayout.setSpacing(10)
        mainHLayout.addWidget(self.tabBar)
        mainHLayout.addWidget(self.tabPane, 1)
        self.setLayout(mainHLayout)
        self.tabBar.changeTab.connect(self.tabPane.setCurrentIndex)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
