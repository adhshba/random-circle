import sys

from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAbstractButton, QRadioButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QCheckBox, QMainWindow, QButtonGroup
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Окружности')
        self.pushButton = QPushButton('Pисовать', self)
        self.pushButton.resize(80, 50)
        self.pushButton.move(375, 550)
        self.flag = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()


    def draw(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        for _ in range(10):
            x = randint(0, 100)
            qp.drawEllipse(randint(0, 800), randint(0, 600), x, x)

    def paint(self):
        self.flag = True
        self.repaint()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())