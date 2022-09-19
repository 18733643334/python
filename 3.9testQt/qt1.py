#!/usr/bin/env python3


from PyQt5.QtWidgets import QPushButton, QApplication, QWidget
import sys



class WinForm(QWidget):
	def __init__(self, parent = None):
		super(WinForm, self).__init__(parent)
		self.setGeometry(300, 300, 350, 350)
		self.setWindowTitle('按钮操作')
		quit = QPushButton('close', self) # 设置按钮的名称
		quit.setGeometry(10, 10, 60, 35) # 设置按钮位置及大小
		quit.setStyleSheet("background-color:read") # 设置背景颜色
		quit.clicked.connect(self.close)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	app.exec_()