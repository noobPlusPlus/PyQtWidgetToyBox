# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QFrame
from PyQt5.uic import loadUi
from PyQt5.QtCore import QFile, QIODevice, QDate, Qt


class NewYearCountDown(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('NewYearCountDown/NewYearCountDown.ui', self)
        self.setAttribute(Qt.WA_DeleteOnClose,True)

        yearDayList = [QDate(2022, 2, 1),
         QDate(2023, 1, 22),
         QDate(2024, 2, 10),
         QDate(2025, 1, 29),
         QDate(2026, 2, 17),
         QDate(2027, 2, 6),
         QDate(2028, 1, 26),
         QDate(2099, 1, 26),
         ]

        today = QDate.currentDate()
        self.dateLabel.setText(today.toString("- yyyy年M月d日 -"))

        for yearDay in yearDayList:
            daysTo = today.daysTo(yearDay)
            if daysTo >= 0:
                self.countDownLabel.setText(str(daysTo))
                break
        
