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
        self.tabs.addTab(self.tab3,"Üretici <=> Müşteri")
        
        # tab1
        self.tab1.layout = QVBoxLayout(self)
        self.tabloMenu = QComboBox()
        self.tabloMenu.addItems(["Tedarikçi","Tedarikçi Hammadde","Stok Hammade","Stok Ürün","Müşteri","Boş","Formüller","Uzaklıklar"])
        self.tab1.layout.addWidget(self.tabloMenu)
        self.tableWidget = QTableWidget()
        tedarikci_tablo = vti.getTedarikciTablo()
        self.tableWidget.setRowCount(len(tedarikci_tablo))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Id","Ülke","Şehir","Firma Adı"])
        i = 0
        for j in tedarikci_tablo:
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
        
        self.pushButton3 = QPushButton("Yeni Kimyasal Formül Ekle")
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
            tedarikci_tablo = vti.getTedarikciTablo()
            self.tableWidget.setRowCount(len(tedarikci_tablo))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Id","Ülke","Şehir","Firma Adı"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in tedarikci_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(satir[3]))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
        
        elif i == 1:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            tedarikci_hammadde_tablo = vti.getTedarikciHammaddeTablo()
            self.tableWidget.setRowCount(len(tedarikci_hammadde_tablo))
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setHorizontalHeaderLabels(["Id", "Hammadde","Tedarikçi Id", "Miktar", "Üretim Tarihi", "Raf Ömrü", "Satış Fiyatı"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in tedarikci_hammadde_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(str(satir[3])))
                self.tableWidget.setItem(satirIndex,4,QTableWidgetItem(str(satir[4])))
                self.tableWidget.setItem(satirIndex,5,QTableWidgetItem(str(satir[5])))
                self.tableWidget.setItem(satirIndex,6,QTableWidgetItem(str(satir[6])))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)

        elif i == 2:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            stok_hammadde_tablo = vti.getStokHammaddeTablo()
            self.tableWidget.setRowCount(len(stok_hammadde_tablo))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Id", "Hammadde İsmi", "Alış Maliyeti", "Stok Miktarı"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in stok_hammadde_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(str(satir[2])))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(str(satir[3])))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 3:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            stok_urun_tablo = vti.getStokUrunTablo()
            self.tableWidget.setRowCount(len(stok_urun_tablo))
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setHorizontalHeaderLabels(["Id","Kimyasal Ürun","Üretim Tarihi","Raf Ömru","İşçilik Maliyeti","Toplam Maliyet","Satış Fiyati"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in stok_urun_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(str(satir[2])))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(str(satir[3])))
                self.tableWidget.setItem(satirIndex,4,QTableWidgetItem(str(satir[4])))
                self.tableWidget.setItem(satirIndex,5,QTableWidgetItem(str(satir[5])))
                self.tableWidget.setItem(satirIndex,6,QTableWidgetItem(str(satir[6])))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 4:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            musteri_tablo = vti.getMusteriTablo()
            self.tableWidget.setRowCount(len(musteri_tablo))
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["Müşteri Id", "Müşteri Adı", "Adres"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in musteri_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
            
        elif i == 5:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
#            musteri_urun_tablo = vti.getMusteriUrunTablo()
#            self.tableWidget.setRowCount(len(musteri_urun_tablo))
#            self.tableWidget.setColumnCount(2)
#            self.tableWidget.setHorizontalHeaderLabels(["Müşteri Id", "Ürün"])
#            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
#            satirIndex = 0
#            for satir in musteri_urun_tablo:
#                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
#                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
#                satirIndex += 1
            self.tab1.layout.addWidget(self.tableWidget)
        
        elif i == 6:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            formul_tablo = vti.getFormulTablo()
            self.tableWidget.setRowCount(len(formul_tablo))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Formül", "Bileşen 1", "Bileşen 2","Bileşen 3"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in formul_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(satir[3]))
                satirIndex += 1         
            self.tab1.layout.addWidget(self.tableWidget)
        elif i == 7:
            self.tab1.layout.removeWidget(self.tableWidget)
            self.tableWidget = QTableWidget()
            ulasim_tablo = vti.getUlasimTablo()
            self.tableWidget.setRowCount(len(ulasim_tablo))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["Id", "Ülke", "Şehir","Uzaklık"])
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#tablo değiştirilemez
            satirIndex = 0
            for satir in ulasim_tablo:
                self.tableWidget.setItem(satirIndex,0,QTableWidgetItem(satir[0]))
                self.tableWidget.setItem(satirIndex,1,QTableWidgetItem(satir[1]))
                self.tableWidget.setItem(satirIndex,2,QTableWidgetItem(satir[2]))
                self.tableWidget.setItem(satirIndex,3,QTableWidgetItem(str(satir[3])))
                satirIndex += 1         
            self.tab1.layout.addWidget(self.tableWidget)

class pencere1(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hammade Satın Al")
        self.setFixedSize(400,300)
        
        self.label1 = QLabel(self)
        self.label1.setText("Hammadde : ")
        self.label1.move(75,50)
        self.line1 = QLineEdit(self)
        self.line1.move(175,50)
        
        self.label2 = QLabel(self)
        self.label2.setText("Adet : ")
        self.label2.move(75,90)
        self.line2 = QLineEdit(self)
        self.line2.move(175,90)
        
        self.label3 = QLabel(self)
        self.label3.setGeometry(80,160,180,30)
        
        self.tedarikci_menu = QComboBox(self)
        self.tedarikci_menu.setGeometry(65,190,250,25)
        self.tedarikci_menu.setVisible(False)

        self.buton1 = QPushButton(self)
        self.buton1.setText("Firmalari Listele")
        self.buton1.setGeometry(150,130,100,30)
        
        self.buton2 = QPushButton(self)
        self.buton2.setText("Tamam")
        self.buton2.setGeometry(150,230,100,30)
        self.buton2.setVisible(False)
        
        self.buton1.clicked.connect(self.tiklandi1)
        
    def tiklandi1(self):
        self.hammadde = self.line1.text()
        self.miktar = self.line2.text()
        
        tedarikci_liste = vti.tedarikci_listele(self.hammadde,self.miktar)
        
        self.tedarikci_menu.addItems(tedarikci_liste)
        self.tedarikci_menu.setVisible(True)
        self.label3.setText("Firma\t\tUlaşım Maliyeti\tToplam Maliyet")
        self.buton2.setVisible(True)
        self.buton2.clicked.connect(self.tiklandi2)
    
    def tiklandi2(self):
        index = self.tedarikci_menu.currentIndex()

        print(index)
        
        vti.hammadde_satisi(index,self.miktar,self.hammadde)
        
        self.close()

        
class pencere2(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kimyasal Ürün Üret")
        self.setFixedSize(450,450)
        
        self.label1 = QLabel(self)
        self.label1.setText("Üretilecek Kimyasal Ürün : ")
        self.label1.setGeometry(75,50,175,30)
    
        urun_liste = vti.kimyasal_urun_liste()
        self.urun_combo = QComboBox(self)
        self.urun_combo.addItems(urun_liste)
        self.urun_combo.move(225,50)
        
        self.label2 = QLabel(self)
        self.label2.setText("Miktar : ")
        self.label2.setGeometry(80,90,50,25)
        
        self.line1 = QLineEdit(self)
        self.line1.setGeometry(225,90,50,25)
        self.line1.textChanged.connect(self.miktar_al)
        
        self.label3 = QLabel(self)
        self.label3.setText("Hammadde")
        self.label3.move(75,115)
        
        self.label4 = QLabel(self)
        self.label4.setText("Miktar")
        self.label4.move(150,115)
        
        self.label5 = QLabel(self)
        self.label5.setText("Stok")
        self.label5.move(250,115)
        
        self.label6 = QLabel(self)
        self.label6.setText("C")
        self.label6.move(90,140)
        
        self.label7 = QLabel(self)
        self.label7.setText("H")
        self.label7.move(90,165)
        
        self.label8 = QLabel(self)
        self.label8.setText("O")
        self.label8.move(90,190)
        
        self.label9 = QLabel(self)
        self.label9.setText("N")
        self.label9.move(90,215)
        
        self.label10 = QLabel(self)
        self.label10.setText("S")
        self.label10.move(90,240)
        
        self.label11 = QLabel(self)
        self.label11.setText("Cl")
        self.label11.move(90,265)
          
        self.label12 = QLabel(self)
        self.label12.move(155,140)
   
        self.label13 = QLabel(self)
        self.label13.move(155,165)
        
        self.label14 = QLabel(self)
        self.label14.move(155,190)
              
        self.label15 = QLabel(self)
        self.label15.move(155,215)
        
        self.label16 = QLabel(self)
        self.label16.move(155,240)
        
        self.label17 = QLabel(self)
        self.label17.move(155,265)

        self.label18 = QLabel(self)
        self.label18.setGeometry(80,300,150,25)
        self.label18.setText("İşçilik Maliyeti : ")
        
        self.label19 = QLabel(self)
        self.label19.setGeometry(80,325,150,25)
        self.label19.setText("Hammaddelerin Maliyeti : ")
        
        self.label20 = QLabel(self)
        self.label20.setGeometry(80,350,150,25)
        self.label20.setText("Toplam Maliyet : ")
        
        self.label21 = QLabel(self)
        self.label21.move(250,295)
        
        self.label22 = QLabel(self)
        self.label22.move(250,320)
       
        self.label23 = QLabel(self)
        self.label23.move(250,345)
        
        self.label24 = QLabel(self)
        self.label24.move(10,10)
        self.label24.setText("Tarih : "+vti.tarih[0:2]+"."+vti.tarih[2:4]+"."+vti.tarih[4:8])
        
        self.label25 = QLabel(self)
        self.label25.move(80,375)
        self.label25.setText("Raf Ömrü : ")
        
        self.line2 = QLineEdit(self)
        self.line2.setGeometry(240,377,50,25)
        
        self.c_combo = QComboBox(self)
        self.c_combo.setGeometry(200,145,150,20)
        
        self.h_combo = QComboBox(self)
        self.h_combo.setGeometry(200,170,150,20)

        self.o_combo = QComboBox(self)
        self.o_combo.setGeometry(200,195,150,20)

        self.n_combo = QComboBox(self)
        self.n_combo.setGeometry(200,220,150,20)
        
        self.s_combo = QComboBox(self)
        self.s_combo.setGeometry(200,245,150,20)
        
        self.cl_combo = QComboBox(self)
        self.cl_combo.setGeometry(200,270,150,20)
        
        self.buton = QPushButton(self)
        self.buton.setText("Tamam")
        self.buton.setGeometry(175,415,80,25)
        self.buton.setEnabled(False)
        self.buton.clicked.connect(self.tamam)
            
    def miktar_al(self):
        miktar = int(self.line1.text())
        
        urun = self.urun_combo.currentText()
        
        elementler = vti.element_miktarlar(urun)
        
        self.c_miktar = int(elementler["C"])*miktar
        self.h_miktar = int(elementler["H"])*miktar
        self.o_miktar = int(elementler["O"])*miktar
        self.n_miktar = int(elementler["N"])*miktar
        self.s_miktar = int(elementler["S"])*miktar
        self.cl_miktar = int(elementler["Cl"])*miktar
    
        self.label12.setText(str(self.c_miktar))
        self.label13.setText(str(self.h_miktar))
        self.label14.setText(str(self.o_miktar))
        self.label15.setText(str(self.n_miktar))       
        self.label16.setText(str(self.s_miktar))
        self.label17.setText(str(self.cl_miktar))
        
        self.c_stok = vti.c_stok_liste(self.c_miktar)
        self.h_stok = vti.h_stok_liste(self.h_miktar)
        self.o_stok = vti.o_stok_liste(self.o_miktar)
        self.n_stok = vti.n_stok_liste(self.n_miktar)
        self.s_stok = vti.n_stok_liste(self.s_miktar)
        self.cl_stok = vti.n_stok_liste(self.cl_miktar)
        
        self.c_combo.clear()
        self.c_combo.addItems(self.c_stok)
        
        self.h_combo.clear()
        self.h_combo.addItems(self.h_stok)
        
        self.o_combo.clear()
        self.o_combo.addItems(self.o_stok)
        
        self.n_combo.clear()
        self.n_combo.addItems(self.n_stok)
        
        self.s_combo.clear()
        self.s_combo.addItems(self.s_stok)
        
        self.cl_combo.clear()
        self.cl_combo.addItems(self.cl_stok)
        
        if self.uretilebiliyor_mu():
            hammadde_toplam = 0
            
            self.buton.setEnabled(True)
            
            self.iscilik = vti.imk
            
            if self.c_miktar != 0:
                hammadde_toplam += int(self.c_combo.currentText().split(" | ")[2])*self.c_miktar/int(self.c_combo.currentText().split(" | ")[3])
            if self.h_miktar != 0:
                hammadde_toplam += int(self.h_combo.currentText().split(" | ")[2])*self.h_miktar/int(self.h_combo.currentText().split(" | ")[3])
            if self.o_miktar != 0:
                hammadde_toplam += int(self.o_combo.currentText().split(" | ")[2])*self.o_miktar/int(self.o_combo.currentText().split(" | ")[3])
            if self.n_miktar != 0:
                hammadde_toplam += int(self.n_combo.currentText().split(" | ")[2])*self.n_miktar/int(self.n_combo.currentText().split(" | ")[3])
            if self.s_miktar != 0:
                hammadde_toplam += int(self.s_combo.currentText().split(" | ")[2])*self.s_miktar/int(self.s_combo.currentText().split(" | ")[3])
            if self.cl_miktar != 0:
                hammadde_toplam += int(self.cl_combo.currentText().split(" | ")[2])*self.cl_miktar/int(self.cl_combo.currentText().split(" | ")[3])
                
            self.label21.setText(str(self.iscilik*miktar))
            self.label22.setText(str(int(hammadde_toplam)))
            self.label23.setText(str(int(self.iscilik*miktar + hammadde_toplam)))
            
        else:
            self.label21.clear()
            self.label22.clear()
            self.label23.clear()           
            self.buton.setEnabled(False)
            
    def uretilebiliyor_mu(self):
        if self.label12.text() != "0" and len(self.c_stok) == 0 :
            return False
        elif self.label13.text() != "0" and len(self.h_stok) == 0 :
            return False
        elif self.label14.text() != "0" and len(self.o_stok) == 0 :
            return False
        elif self.label15.text() != "0" and len(self.n_stok) == 0 :
            return False
        elif self.label16.text() != "0" and len(self.n_stok) == 0 :
            return False
        elif self.label17.text() != "0" and len(self.n_stok) == 0 :
            return False
        else:
            return True
    
    def tamam(self):
        hammadde_miktarlar = [self.c_miktar,self.h_miktar,self.o_miktar,self.n_miktar,self.s_miktar,self.cl_miktar]
        
        secilen_hammaddeler = [self.c_combo.currentText(),self.h_combo.currentText(),self.o_combo.currentText(),self.n_combo.currentText(),self.s_combo.currentText(),self.cl_combo.currentText()]
        
        toplam_maliyet = self.label19.text()
        
        raf_omru = int(self.line2.text())
        
        vti.kimyasal_uret(hammadde_miktarlar,secilen_hammaddeler,raf_omru,self.iscilik,toplam_maliyet)
        
        self.close()
        
class pencere3(QMainWindow):                          
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni Kimyasal Formul Ekle")
        self.setFixedSize(400,300)
        
        self.label1 = QLabel(self)
        self.label1.setText("Formul : ")
        self.label1.move(75,50)
        self.line1 = QLineEdit(self)
        self.line1.move(175,50)

        self.label2 = QLabel(self)
        self.label2.setText("Bileşen 1")
        self.label2.move(75,90)
        self.line2 = QLineEdit(self)
        self.line2.move(175,90)
        
        self.label3 = QLabel(self)
        self.label3.setText("Bileşen 2 : ")
        self.label3.move(75,130)
        self.line3 = QLineEdit(self)
        self.line3.move(175,130)
        
        self.label4 = QLabel(self)
        self.label4.setText("Bileşen 3 : ")
        self.label4.move(75,170)
        self.line4 = QLineEdit(self)
        self.line4.move(175,170)
  
        self.buton = QPushButton(self)
        self.buton.setText("Tamam")
        self.buton.setGeometry(160,250,80,25)
   
        self.buton.clicked.connect(self.tiklandi)
    
    def tiklandi(self):
        formul = self.line1.text()
        bilesen1 = self.line2.text()
        bilesen2 = self.line3.text()
        bilesen3 = self.line4.text()
        
        vti.formul_ekle(formul,bilesen1,bilesen2,bilesen3)
        self.close()
        
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
        tedarikci_id = self.line1.text()
        tedarikci_firma_adi = self.line2.text()
        tedarikci_ulke = self.line3.text()
        tedarikci_sehir = self.line4.text()
        
        vti.yeni_tedarikci(tedarikci_id,tedarikci_firma_adi,tedarikci_ulke,tedarikci_sehir)
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
        self.label3.setText("Adres : ")
        self.label3.move(75,130)
        self.line3 = QLineEdit(self)
        self.line3.move(175,130)

        self.buton = QPushButton(self)
        self.buton.setText("Tamam")
        self.buton.setGeometry(150,210,80,30)
   
        self.buton.clicked.connect(self.tiklandi)
    
    def tiklandi(self):
        musteri_id = self.line1.text()
        musteri_adi = self.line2.text()
        musteri_adres = self.line3.text()
        
        vti.yeni_musteri(musteri_id,musteri_adi,musteri_adres)
        self.close()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
