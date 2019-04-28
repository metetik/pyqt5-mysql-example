import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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
        
        # tab1
        self.tab1.layout = QVBoxLayout(self)
        self.tabloMenu = QComboBox()
        self.tabloMenu.addItems(["tablo1","tablo2","tablo3","tablo4","tablo5","tablo6","tablo7",])
        self.tab1.layout.addWidget(self.tabloMenu)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["tablo1a", "b", "c"])
        self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))
        self.tab1.layout.addWidget(self.tableWidget)
        
        self.tabloMenu.currentIndexChanged.connect(self.fun)
        
        self.tab1.setLayout(self.tab1.layout)
        
        # tab2
        self.tab2.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("tab2 button")
        self.tab2.layout.addWidget(self.pushButton1)
        self.tab2.setLayout(self.tab2.layout)
        
        # tab3
        self.tab3.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("tab3 button")
        self.tab3.layout.addWidget(self.pushButton1)
        self.tab3.setLayout(self.tab3.layout)
        
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    def fun(self,i):
        if i == 0:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(5)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["tablo1a", "b", "c"])
            self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
            self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
            self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))
            self.tab1.layout.addWidget(self.tableWidget)
        
        elif i == 1:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(5)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["tablo2a", "b", "c"])
            self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
            self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
            self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))
            self.tab1.layout.addWidget(self.tableWidget)
        elif i == 2:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(5)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["tablo3a", "b", "c"])
            self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
            self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
            self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 3:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(5)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["tablo4a", "b", "c"])
            self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
            self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
            self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))
            self.tab1.layout.addWidget(self.tableWidget)
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 4:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(5)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["tablo5a", "b", "c"])
            self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
            self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
            self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))
            self.tab1.layout.addWidget(self.tableWidget)
        elif i == 5:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(5)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["tablo6a", "b", "c"])
            self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
            self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
            self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 6:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(5)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["tablo7a", "b", "c"])
            self.tableWidget.setItem(0,0,QTableWidgetItem("Id"))
            self.tableWidget.setItem(0,1,QTableWidgetItem("İsim"))
            self.tableWidget.setItem(0,2,QTableWidgetItem("Soyisim"))            
            self.tab1.layout.addWidget(self.tableWidget)
#    @pyqtSlot()
#    def on_click(self):
#        print("\n")
#        for currentQTableWidgetItem in self.tableWidget.selectedItems():
#            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
