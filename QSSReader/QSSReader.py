# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QFile, QIODevice


def QSSReader(path):
    qssFile = QFile(path)
    if not qssFile.open(QIODevice.ReadOnly | QIODevice.Text):
        return ""

    return str(qssFile.readAll(), encoding='utf-8')
