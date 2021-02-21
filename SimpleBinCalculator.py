# This is simple binary calculator
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore

date = QDate.currentDate()

def switch_func(value):
    return {
        '+': bin(int(a) + int(b)),
        '-': bin(int(a) - int(b)),
        '*': bin(int(a) * int(b)),
        '/': bin(int(a) // int(b))
    }.get(value)

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
        self.show()

    def timeApp(self):
        lbTime = QLabel(date.toString(Qt.DefaultLocaleShortDate),self)
        lbTime.move(10,10)
        lbTime.setGeometry(10,10,150,50)
        lbTime.setFont(QFont('Roboco Mono', 14))




if __name__ == '__main__':
    a = input("Wprowadź pierwszą liczbę: ")
    b = input("Wprowadź drugą liczbę: ")
    c = input("Wprowadź znak: ")
    print(switch_func(c))
    app = QApplication(sys.argv)
    ma = MyApp()
    sys.exit(app.exec_())


