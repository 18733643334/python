#~/www/cgtron_pipeline/venv
import sys
from PyQt6.QtWidgets import *


class ComBox(QWidget):
    def __init__(self, parent=None):
        super(ComBox, self).__init__(parent)
        self.setWindowTitle("测试窗口")
        self.resize(500, 400)
        layout = QVBoxLayout()
        self.select = QComboBox()

        dates = ["213", "4235", "436", "7657"]
        self.select.addItems(dates)
        layout.addWidget(self.select)

        self.button1 = QPushButton("生成", self)
        self.button1.clicked.connect(self.clickButton)
        layout.addWidget(self.button1)
        self.setLayout(layout)

    def clickButton(self):
        print('被点击了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    comBox = ComBox()
    comBox.show()
    sys.exit(app.exec())
