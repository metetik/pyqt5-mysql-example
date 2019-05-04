import sys
import veritabani_islemleri as vti
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Deneme")
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.setGeometry(200,200,600,450)
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
        self.tabloMenu.addItems(["Tedarikçi","Tedarikçi Hammadde","Üretici","Stok Hammade","Stok Ürün","Müşteri","Müşteri Ürün","Bileşenler"])
        self.tab1.layout.addWidget(self.tabloMenu)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(vti.tedarikci_tablo))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Id","Konum","Firma Adı"])
        i = 0
        for j in vti.tedarikci_tablo:
            self.tableWidget.setItem(i,0,QTableWidgetItem(j[0]))
            self.tableWidget.setItem(i,1,QTableWidgetItem(j[1]))
            self.tableWidget.setItem(i,2,QTableWidgetItem(j[2]))
            i+=1
        self.tab1.layout.addWidget(self.tableWidget)
        self.tabloMenu.currentIndexChanged.connect(self.tablolar)
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
        
    def tablolar(self,i):
        if i == 0:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.tedarikci_tablo))
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["Id","Konum","Firma Adı"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.tedarikci_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
        
        elif i == 1:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.tedarikci_hammadde_tablo))
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(["Id", "Tedarikçi Id", "Miktar", "Üretim Tarihi", "Raf Ömrü", "Satış Fiyatı"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.tedarikci_hammadde_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(str(satir[2])))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(satir[3]))
                self.tableWidget.setItem(satirIndex,4,QTableWidgetItem(str(satir[4])))
                self.tableWidget.setItem(satirIndex,5,QTableWidgetItem(str(satir[5])))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
        elif i == 2:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.uretici_tablo))
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Firma Adı", "Konum"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.uretici_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 3:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.stok_hammadde_tablo))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Id", "Hammadde İsmi", "Alış Maliyeti", "Stok Miktarı"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.stok_hammadde_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(str(satir[2])))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(str(satir[3])))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 4:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.stok_urun_tablo))
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setHorizontalHeaderLabels(["Id","Kimyasal Ürun","Üretim Tarihi","Raf Ömru","İşçilik Maliyeti","Toplam Maliyet","Satış Fiyati"])
            satirIndex = 0
            for satir in vti.stok_hammadde_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(str(satir[2])))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(str(satir[3])))
                self.tableWidget.setItem(satirIndex,4,QTableWidgetItem(str(satir[4])))
                self.tableWidget.setItem(satirIndex,5,QTableWidgetItem(str(satir[5])))
                self.tableWidget.setItem(satirIndex,6,QTableWidgetItem(str(satir[6])))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
        elif i == 5:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.musteri_tablo))
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["Müşteri Id", "Müşteri Adı", "Adres"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.musteri_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 6:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.musteri_urun_tablo))
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Müşteri Id", "Ürün"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.musteri_urun_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
        
        elif i == 7:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.bilesen_tablo))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Stok Ürün", "Bileşen 1", "Bileşen 2","Bileşen3"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.bilesen_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[3]))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(satir[3]))
                satirIndex += 1         
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
    
