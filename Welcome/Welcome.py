# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi
from PyQt5.QtCore import QFile, QIODevice


class Welcome(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('Welcome/Welcome.ui', self)
        self.textEdit.setMarkdown(self.__readMeReader("README.md"))

    def __readMeReader(self, path):
        readMeFile = QFile(path)
        if not readMeFile.open(QIODevice.ReadOnly | QIODevice.Text):
            return ""

        return str(readMeFile.readAll(), encoding='utf-8')
