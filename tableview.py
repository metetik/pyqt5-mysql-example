# -*- coding: utf-8 -*-
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.title = "PyQt5 Table"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400
        
        self.initWindow()
    
    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        
        self.creatingTables()
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)
        
        self.show()
        
    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["a", "b", "c"])
        self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

#%%
