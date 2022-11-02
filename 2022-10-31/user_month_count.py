#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from tron_py.common.model import Table
import time, pandas as pd

time_array = time.localtime(time.time())
year = str(time_array[0])


class CreateExcel:
    def __init__(self, date):
        self.date = date
        print(date)


class ComboxSelect(QWidget):
    def __init__(self, parent=None):
        super(ComboxSelect, self).__init__(parent)
        self.setWindowTitle("选择日期")
        self.resize(360, 180)
        layout = QVBoxLayout()
        self.lbl = QLabel("")
        self.cb = QComboBox()
        dates = ['请选择']
        for i in range(1, 13):
            if i < 10:
                i = '0{}'.format(i)
            ym = "{}-{}".format(year, i)
            dates.append(ym)
        self.cb.addItems(dates)
        self.cb.currentIndexChanged.connect(self.selectionchange)
        layout.addWidget(self.cb)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def selectionchange(self):
        self.lbl.setText('正在生成{}的表格'.format(self.cb.currentText()))
        self.lbl.adjustSize()
        select_str = self.cb.currentText()
        CreateExcel(select_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxSelect = ComboxSelect()
    comboxSelect.show()
    sys.exit(app.exec())
