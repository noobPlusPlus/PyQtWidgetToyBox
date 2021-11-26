# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
