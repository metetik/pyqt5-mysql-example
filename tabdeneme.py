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
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Id","Ülke","Şehir","Firma Adı"])
        i = 0
        for j in vti.tedarikci_tablo:
            self.tableWidget.setItem(i,0,QTableWidgetItem(j[0]))
            self.tableWidget.setItem(i,1,QTableWidgetItem(j[1]))
            self.tableWidget.setItem(i,2,QTableWidgetItem(j[2]))
            self.tableWidget.setItem(i,3,QTableWidgetItem(j[3]))
            i+=1
        self.tab1.layout.addWidget(self.tableWidget)
        self.tabloMenu.currentIndexChanged.connect(self.tablolar)
        self.tab1.setLayout(self.tab1.layout)
        
        # tab2
        self.tab2.layout = QVBoxLayout(self)
        self.tab2_butonlar1 = QHBoxLayout(self)
        self.tab2_butonlar2 = QHBoxLayout(self)
        
        self.pushButton1 = QPushButton("Hammadde Satın Al")
        self.tab2_butonlar1.addWidget(self.pushButton1)
        self.pushButton1.clicked.connect(self.pencere1_ac)
        self.pushButton2 = QPushButton("Kimyasal Ürün Üret")
        self.tab2_butonlar1.addWidget(self.pushButton2)
        self.pushButton2.clicked.connect(self.pencere2_ac)
        
        self.pushButton3 = QPushButton("Yeni Kimyasal Ürün Ekle")
        self.tab2_butonlar2.addWidget(self.pushButton3)
        self.pushButton3.clicked.connect(self.pencere3_ac)
        self.pushButton4 = QPushButton("Yeni Tedarikçi")
        self.tab2_butonlar2.addWidget(self.pushButton4)
        self.pushButton4.clicked.connect(self.pencere4_ac)
        
        self.bilgi_kutusu = QLabel("Bilgi kutusu1")
        
        
        self.tab2.layout.addLayout(self.tab2_butonlar1)
        self.tab2.layout.addLayout(self.tab2_butonlar2)
        self.tab2.layout.addWidget(self.bilgi_kutusu)
        self.tab2.setLayout(self.tab2.layout)
        
        # tab3
        self.tab3.layout = QVBoxLayout(self)
        self.tab3_butonlar1 = QHBoxLayout(self)
        self.tab3_butonlar2 = QHBoxLayout(self)
        
        self.pushButton5 = QPushButton("Kimyasal Ürün Sat")
        self.tab3_butonlar1.addWidget(self.pushButton5)
        self.pushButton5.clicked.connect(self.pencere5_ac)
        self.pushButton6 = QPushButton("Kimyasal Ürün Sipariş Et")
        self.tab3_butonlar1.addWidget(self.pushButton6)
        self.pushButton6.clicked.connect(self.pencere6_ac)
        
        self.pushButton7 = QPushButton("Satışları Göster")
        self.tab3_butonlar2.addWidget(self.pushButton7)
        self.pushButton7.clicked.connect(self.pencere7_ac)
        self.pushButton8 = QPushButton("Yeni Müşteri")
        self.tab3_butonlar2.addWidget(self.pushButton8)
        self.pushButton8.clicked.connect(self.pencere8_ac)
        
        self.bilgi_kutusu = QLabel("Bilgi kutusu2")
        
        self.tab3.layout.addLayout(self.tab3_butonlar1)
        self.tab3.layout.addLayout(self.tab3_butonlar2)
        self.tab3.layout.addWidget(self.bilgi_kutusu)
        self.tab3.setLayout(self.tab3.layout)
        
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    
    def pencere1_ac(self):
        self.p1 = pencere1()
        self.p1.show()
    def pencere2_ac(self):
        self.p2 = pencere2()
        self.p2.show()
    def pencere3_ac(self):
        self.p3 = pencere3()
        self.p3.show()
    def pencere4_ac(self):
        self.p4 = pencere4()
        self.p4.show()
    def pencere5_ac(self):
        self.p5 = pencere5()
        self.p5.show()
    def pencere6_ac(self):
        self.p6 = pencere6()
        self.p6.show()
    def pencere7_ac(self):
        self.p7 = pencere7()
        self.p7.show()
    def pencere8_ac(self):
        self.p8 = pencere8()
        self.p8.show()
        
        
    def tablolar(self,i):
        if i == 0:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(len(vti.tedarikci_tablo))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Id","Ülke","Şehir","Firma Adı"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.tedarikci_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(satir[3]))
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
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["Firma Adı", "Ülke", "Şehir"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.uretici_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
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
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.stok_urun_tablo:
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
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Müşteri Id", "Müşteri Adı", "Ülke", "Şehir"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.musteri_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(satir[3]))
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
            self.tableWidget.setHorizontalHeaderLabels(["Stok Ürün", "Bileşen 1", "Bileşen 2","Bileşen 3"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in vti.bilesen_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(satir[3]))
                satirIndex += 1         
            self.tab1.layout.addWidget(self.tableWidget)

class pencere1(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hammade Satın Al")
        
class pencere2(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kimyasal Ürün Üret")
class pencere3(QMainWindow):                          
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni Kimyasal Ürün Ekle")
class pencere4(QMainWindow):                           
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Yeni Tedarikçi")
        self.setFixedSize(400,300)
        
        self.label1 = QLabel(self)
        self.label1.setText("Tedarikçi Id : ")
        self.label1.move(75,50)
        self.line1 = QLineEdit(self)
        self.line1.move(175,50)
        
        self.label2 = QLabel(self)
        self.label2.setText("Tedarikçi Firma Adı : ")
        self.label2.move(75,90)
        self.line2 = QLineEdit(self)
        self.line2.move(175,90)
        
        self.label3 = QLabel(self)
        self.label3.setText("Ülke : ")
        self.label3.move(75,130)
        self.line3 = QLineEdit(self)
        self.line3.move(175,130)
        
        self.label4 = QLabel(self)
        self.label4.setText("Şehir : ")
        self.label4.move(75,170)
        self.line4 = QLineEdit(self)
        self.line4.move(175,170)
  
        self.buton = QPushButton(self)
        self.buton.setText("Tamam")
        self.buton.setGeometry(150,210,80,30)
   
        self.buton.clicked.connect(self.tiklandi)
    
    def tiklandi(self):
        self.tedarikci_id = self.line1.text()
        self.tedarikci_firma_adi = self.line2.text()
        self.tedarikci_ulke = self.line3.text()
        self.tedarikci_sehir = self.line4.text()
        
        vti.yeni_tedarikci(self.tedarikci_id,self.tedarikci_firma_adi,self.tedarikci_ulke,self.tedarikci_sehir)
        self.close()
        
class pencere5(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kimyasal Ürün Sat")        
class pencere6(QMainWindow):                          
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kimyasal Ürün Sipariş Et")        
class pencere7(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Satışları Göster")        
class pencere8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni Müşteri Ekle")
        self.setFixedSize(400,300)
        
        self.label1 = QLabel(self)
        self.label1.setText("Müşteri Id : ")
        self.label1.move(75,50)
        self.line1 = QLineEdit(self)
        self.line1.move(175,50)
        
        self.label2 = QLabel(self)
        self.label2.setText("Müşteri Adı : ")
        self.label2.move(75,90)
        self.line2 = QLineEdit(self)
        self.line2.move(175,90)
        
        self.label3 = QLabel(self)
        self.label3.setText("Ülke : ")
        self.label3.move(75,130)
        self.line3 = QLineEdit(self)
        self.line3.move(175,130)
        
        self.label4 = QLabel(self)
        self.label4.setText("Şehir : ")
        self.label4.move(75,170)
        self.line4 = QLineEdit(self)
        self.line4.move(175,170)
  
        self.buton = QPushButton(self)
        self.buton.setText("Tamam")
        self.buton.setGeometry(150,210,80,30)
   
        self.buton.clicked.connect(self.tiklandi)
    
    def tiklandi(self):
        self.musteri_id = self.line1.text()
        self.musteri_adi = self.line2.text()
        self.musteri_ulke = self.line3.text()
        self.musteri_sehir = self.line4.text()
        
        vti.yeni_musteri(self.musteri_id,self.musteri_adi,self.musteri_ulke,self.musteri_sehir)
        self.close()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
