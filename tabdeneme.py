#%%
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Deneme")
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.setGeometry(400,200,800,600)
        self.show()
    
class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1,"Tablolar")
        self.tabs.addTab(self.tab2,"Tedarikçi <=> Üretici")
        self.tabs.addTab(self.tab3,"Üretici <=> Satıcı")
        
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("tab1 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
        
        self.tab2.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("tab2 button")
        self.tab2.layout.addWidget(self.pushButton1)
        self.tab2.setLayout(self.tab2.layout)
        
        self.tab3.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("tab3 button")
        self.tab3.layout.addWidget(self.pushButton1)
        self.tab3.setLayout(self.tab3.layout)
        
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
## -*- coding: utf-8 -*-
#
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
#from PyQt5 import QtSql
#import sys
#
#class MainWindow(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.setUI()
#    
#    def pencere(self):
#        #ortalamak için sağ ve sol boşluklar
#        sol_bosluk = QWidget()
#        sol_bosluk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#        sag_bosluk = QWidget()
#        sag_bosluk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#        
#        toolbar = self.addToolBar("Tablo")
#
#        toolbar.addWidget(sol_bosluk)
#        menu1 = QPushButton("Tedarikçi <-> Üretici")
#        toolbar.addWidget(menu1)
#        toolbar.addWidget(QLabel("\t"))
#        menu2 = QPushButton("Üretici <-> Müşteri")
#        toolbar.addWidget(menu2)
#        toolbar.addWidget(QLabel("\t"))
#        menu3 = QPushButton("Tablo")
#        toolbar.addWidget(menu3)
#        toolbar.addWidget(sag_bosluk)
# 
#        menu2.clicked.connect(self.pencere2)
#        menu3.clicked.connect(self.pencere3)
#        
#    def pencere2(self):
#        #ortalamak için sağ ve sol boşluklar
#        sol_bosluk = QWidget()
#        sol_bosluk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#        sag_bosluk = QWidget()
#        sag_bosluk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#        
#        toolbar = self.addToolBar("Tablo")
#
#        toolbar.addWidget(sol_bosluk)
#        menu1 = QPushButton("Tedarikçi <-> Üretici2")
#        toolbar.addWidget(menu1)
#        toolbar.addWidget(QLabel("\t"))
#        menu2 = QPushButton("Üretici <-> Müşteri")
#        toolbar.addWidget(menu2)
#        toolbar.addWidget(QLabel("\t"))
#        menu3 = QPushButton("Tablo")
#        toolbar.addWidget(menu3)
#        toolbar.addWidget(sag_bosluk)
#        
#        menu1.clicked.connect(pencere1)
#        menu3.clicked.connect(pencere3)
#        
#        self.deleteItemsOfLayout(toolbar)
#    def pencere3(self):
#        #ortalamak için sağ ve sol boşluklar
#        sol_bosluk = QWidget()
#        sol_bosluk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#        sag_bosluk = QWidget()
#        sag_bosluk.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#        
#        toolbar = self.addToolBar("Tablo")
#
#        toolbar.addWidget(sol_bosluk)
#        menu1 = QPushButton("Tedarikçi <-> Üretici3")
#        toolbar.addWidget(menu1)
#        toolbar.addWidget(QLabel("\t"))
#        menu2 = QPushButton("Üretici <-> Müşteri")
#        toolbar.addWidget(menu2)
#        toolbar.addWidget(QLabel("\t"))
#        menu3 = QPushButton("Tablo")
#        toolbar.addWidget(menu3)
#        toolbar.addWidget(sag_bosluk)
#        
#        menu1.clicked.connect(pencere1)
#        menu2.clicked.connect(pencere2)
#        
#        self.deleteItemsOfLayout(toolbar)
#        
#    def deleteItemsOfLayout(layout):
#         if layout is not None:
#             while layout.count():
#                 item = layout.takeAt(0)
#                 widget = item.widget()
#                 if widget is not None:
#                     widget.setParent(None)
#                 else:
#                     deleteItemsOfLayout(item.layout())
#    def setUI(self):
#        self.setWindowTitle("Tab Deneme")
#        self.pencere1()
#        self.show()
#def main():
#    app = QApplication(sys.argv)
#    mainWindow = MainWindow()
#    sys.exit(app.exec())
#    
#if __name__ == "__main__":
#    main()
