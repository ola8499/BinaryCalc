# This is a simple binary calculator
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from functools import partial


date = QDate.currentDate()



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.setLayout(layout)
        self.timeApp()
        self.mainApp()

    def mainApp(self):
        self.setGeometry(100,100,400,600)
        self.setWindowTitle('Binary Calculator')
        self.setWindowIcon(QtGui.QIcon('calculator.png'))
        self.buttons()
        self.textBox()
        self.show()

    def timeApp(self):
        lbTime = QLabel(date.toString(Qt.DefaultLocaleShortDate),self)
        lbTime.move(10,10)
        lbTime.setGeometry(10,10,150,50)
        lbTime.setFont(QFont('Roboco Mono', 14))

    def buttons(self):

        self.butt_plus=QPushButton(self)
        self.butt_plus.setText("+")
        self.butt_plus.move(50,200)
        self.butt_plus.clicked.connect(self.click_plus)
        self.butt_plus.setFont(QFont('Roboco Mono', 11))

        self.butt_minus = QPushButton(self)
        self.butt_minus.setText("-")
        self.butt_minus.move(170, 200)
        self.butt_minus.clicked.connect(self.click_minus)
        self.butt_minus.setFont(QFont('Roboco Mono', 11))

        self.butt_multi = QPushButton(self)
        self.butt_multi.setText("*")
        self.butt_multi.move(50, 260)
        self.butt_multi.clicked.connect(self.click_multi)
        self.butt_multi.setFont(QFont('Roboco Mono', 11))

        self.butt_div = QPushButton(self)
        self.butt_div.setText("/")
        self.butt_div.move(170, 260)
        self.butt_div.clicked.connect(self.click_div)
        self.butt_div.setFont(QFont('Roboco Mono', 11))

        self.butt_eql = QPushButton(self)
        self.butt_eql.setText("=")
        self.butt_eql.move(170, 320)
        self.butt_eql.clicked.connect(self.click_eql)
        self.butt_eql.setFont(QFont('Roboco Mono', 11))

        self.butt_clean = QPushButton(self)
        self.butt_clean.setText("C")
        self.butt_clean.move(50, 320)
        self.butt_clean.clicked.connect(self.click_clean)
        self.butt_clean.setFont(QFont('Roboco Mono', 11))

    def textBox(self):
        self.txtbx = QLineEdit(self)
        self.txtbx.move(50, 120)
        self.txtbx.resize(220, 30)
        self.txtbx.setFont(QFont('Roboco Mono',11))

        self.txtbx_result = QLineEdit(self)
        self.txtbx_result.move(50, 380)
        self.txtbx_result.resize(220, 30)
        self.txtbx_result.setReadOnly(True)
        self.txtbx_result.setFont(QFont('Roboco Mono', 11))



    @pyqtSlot()
    def click_plus(self):
        text = self.txtbx.text()
        self.txtbx.setText(text+" + ")


    @pyqtSlot()
    def click_minus(self):
        text = self.txtbx.text()
        self.txtbx.setText(text + " - ")

    @pyqtSlot()
    def click_multi(self):
        text = self.txtbx.text()
        self.txtbx.setText(text + " * ")

    @pyqtSlot()
    def click_div(self):
        text = self.txtbx.text()
        self.txtbx.setText(text + " / ")

    @pyqtSlot()
    def click_eql(self):
        result = self.txtbx.text()
        try:
            ans = eval(result)
            ans = bin(ans)[2:].zfill(8)
            self.txtbx_result.setText(str(ans))
        except:
            self.txtbx_result.setText("Math error")


    @pyqtSlot()
    def click_clean(self):
        text = self.txtbx.text()
        self.txtbx.setText(text[:len(text) - 1])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = MyApp()

    sys.exit(app.exec_())


