#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import *


class ComBox(QWidget):
	def __init__(self, parent=None):
		self.selected_data = ''
		super(ComBox, self).__init__(parent)
		self.create_win()
		
	def create_win(self):
		self.setWindowTitle("测试窗口")
		self.resize(500, 400)
		layout = QVBoxLayout()
		self.select = QComboBox()
		
		dates = ["请选择", "2022-12", "2022-11", "2022-10", "2022-09"]
		self.select.addItems(dates)
		self.select.currentIndexChanged.connect(self.selected)
		layout.addWidget(QLabel("选择日期"))
		layout.addWidget(self.select)
		
		# 复选框
		self.rb_task = QRadioButton('任务')
		self.rb_version = QRadioButton("版本")
		self.rb_shot = QRadioButton("镜头")
		self.rb_task.setChecked(True)
		
		layout.addWidget(QLabel("选择类型"))
		layout.addWidget(self.rb_task)
		layout.addWidget(self.rb_version)
		layout.addWidget(self.rb_shot)
		
		self.label1 = QLabel("")
		layout.addWidget(self.label1)
		
		self.button1 = QPushButton("生成", self)
		self.button1.clicked.connect(self.clickButton)
		layout.addWidget(self.button1)
		self.setLayout(layout)
		
		
	def clickButton(self):
		print('被点击了')
		print(self.selected_data)
		if self.rb_version.isChecked():
			self.checked = '版本'
		elif self.rb_task.isChecked():
			self.checked = '任务'
		elif self.rb_shot.isChecked():
			self.checked = '镜头'
		self.label1.setText('{}类型为[{}]'.format(self.select.currentText()), self.checked)

	def selected(self):
		self.selected_data = self.select.currentText()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	comBox = ComBox()
	comBox.show()
	sys.exit(app.exec())