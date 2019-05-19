# -*- coding: utf-8 -*-
#database'e bağlanma
import mysql.connector
import sys
import re

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="veritabani"#eğer yeni database oluşturmayacaksan bağlan
)

cursor = mydb.cursor()

#%%Tabloların oluşturulması
def tabloOlustur():
    cursor = mydb.cursor()
    
    cursor.execute("drop table if exists tedarikci")
    cursor.execute("drop table if exists tedarikci_hammadde")
    cursor.execute("drop table if exists stok_hammadde")
    cursor.execute("drop table if exists stok_urun")
    cursor.execute("drop table if exists formuller")
    cursor.execute("drop table if exists musteri")
    cursor.execute("drop table if exists ulasim")
    cursor.execute("drop table if exists siparisler")
    cursor.execute("drop view if exists tedarikci_fiyat")
    
    cursor.execute("create table tedarikci          (id int, ulke varchar(20), sehir varchar(20), firma_adi varchar(20), primary key(id))")
    cursor.execute("create table tedarikci_hammadde (id int, hammadde varchar(5),tedarikci_id int ,miktar int,uretim_tarihi varchar(10),raf_omru int,satis_fiyati int, primary key(id))")
    cursor.execute("create table stok_hammadde      (id int,hammadde_ismi varchar(10),alis_maliyeti int,stok_miktar int, primary key(id))")
    cursor.execute("create table stok_urun          (id int,kimyasal_urun varchar(20),miktar int,uretim_tarihi varchar(10),raf_omru int,iscilik_maliyeti int, toplam_maliyet int,satis_fiyati int, primary key(id))")
    cursor.execute("create table musteri            (musteri_id int,musteri_adi varchar(20),adres varchar(50))")
    cursor.execute("create table formuller          (id int,formul varchar(10),bilesen1 varchar(10),bilesen2 varchar(10),bilesen3 varchar(10))")
    cursor.execute("create table ulasim             (id int,ulke varchar(20),sehir varchar(20),uzaklik int)")
    cursor.execute("create table siparisler         (id int,musteri_id int,siparis_tarihi varchar(10),urun varchar(10),miktar int)")
    
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (1,'Turkiye','Ankara','ANK1')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (2,'Turkiye','Eskisehir','ESK1')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (3,'Turkiye','Gaziantep','GAZ1')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (4,'Turkiye','Istanbul','IST1')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (5,'Turkiye','Istanbul','IST2')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (6,'Turkiye','Istanbul','IST3')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (7,'Ingiltere','Londra','LON1')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (8,'Almanya','Berlin','BER1')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (9,'Almanya','Berlin','BER2')")
    cursor.execute("insert into tedarikci(id,ulke,sehir,firma_adi) values (10,'Bosna Hersek','Saraybosna','SB1')")

    
    
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (1,'N',1,100,'01012019',2,8)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (2,'H',1,300,'01012019',3,9)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (3,'C',1,150,'01012019',5,10)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (4,'O',1,400,'01012019',7,11)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (5,'S',1,200,'01012019',2,12)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (6,'Cl',1,250,'01012019',1,13)")
    
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (7,'N',2,10,'01012019',3,1)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (8,'H',2,15,'01012019',4,2)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (9,'C',2,20,'01012019',6,3)")
    
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (10,'N',3,150,'01012019',2,3)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (11,'H',3,200,'01012019',2,4)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (12,'C',3,200,'01012019',3,5)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (13,'S',3,200,'01012019',5,6)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (14,'Cl',3,200,'01012019',7,7)")
    
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (15,'N',4,1000,'01012019',2,10)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (16,'H',4,3000,'01012019',1,11)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (17,'C',4,2000,'01012019',3,12)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (18,'O',4,1000,'01012019',4,13)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (19,'S',4,1000,'01012019',6,14)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (20,'Cl',4,1000,'01012019',2,14)")
      
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (21,'N',5,50,'01012019',3,7)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (22,'C',5,50,'01012019',5,8)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (23,'O',5,50,'01012019',7,9)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (24,'H',5,50,'01012019',2,10)")

    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (25,'N',6,30,'01012019',2,5)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (26,'H',6,30,'01012019',1,6)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (27,'C',6,30,'01012019',3,7)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (28,'O',6,30,'01012019',4,7)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (29,'S',6,30,'01012019',6,8)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (30,'Cl',6,40,'01012019',2,8)")
    
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (31,'N',7,1000,'01012019',2,20)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (32,'H',7,1000,'01012019',3,25)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (33,'C',7,1000,'01012019',5,30)")
    
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (34,'N',8,500,'01012019',7,7)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (35,'H',8,1000,'01012019',2,8)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (36,'O',8,2000,'01012019',1,9)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (37,'S',8,600,'01012019',3,10)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (38,'C',8,1000,'01012019',4,11)")

    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (39,'N',9,100,'01012019',6,3)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (40,'H',9,300,'01012019',2,4)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (41,'C',9,200,'01012019',3,5)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (42,'O',9,300,'01012019',5,6)")    
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (43,'S',9,100,'01012019',7,7)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (44,'Cl',9,100,'01012019',2,8)")
    
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (45,'N',10,10,'01012019',1,1)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (46,'C',10,5,'01012019',3,2)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (47,'O',10,5,'01012019',4,3)")
    cursor.execute("insert into tedarikci_hammadde(id,hammadde,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values (48,'S',10,10,'01012019',6,4)")
    
    
    
    
    
    cursor.execute("insert into stok_hammadde(id,hammadde_ismi,alis_maliyeti,stok_miktar) values (1,'C',160,10)")
    cursor.execute("insert into stok_hammadde(id,hammadde_ismi,alis_maliyeti,stok_miktar) values (2,'H',140,20)")
    cursor.execute("insert into stok_hammadde(id,hammadde_ismi,alis_maliyeti,stok_miktar) values (3,'O',320,15)")
    
    cursor.execute("insert into stok_urun(id,kimyasal_urun,miktar,uretim_tarihi,raf_omru,iscilik_maliyeti,toplam_maliyet,satis_fiyati) values (1,'CO2',10,'01012019',3,1,400,400)")
    cursor.execute("insert into stok_urun(id,kimyasal_urun,miktar,uretim_tarihi,raf_omru,iscilik_maliyeti,toplam_maliyet,satis_fiyati) values (2,'H2O',15,'01012019',4,1,600,750)")
    cursor.execute("insert into stok_urun(id,kimyasal_urun,miktar,uretim_tarihi,raf_omru,iscilik_maliyeti,toplam_maliyet,satis_fiyati) values (3,'NH3',20,'01012019',2,1,500,625)")
    
    cursor.execute("insert into formuller(formul,bilesen1,bilesen2,bilesen3) values ('NH3','N','3H',null)")
    cursor.execute("insert into formuller(formul,bilesen1,bilesen2,bilesen3) values ('CO2','C','2O',null)")
    cursor.execute("insert into formuller(formul,bilesen1,bilesen2,bilesen3) values ('SO2','S','2O',null)")
    cursor.execute("insert into formuller(formul,bilesen1,bilesen2,bilesen3) values ('C6H12O6','6C','12H','6O')")
    cursor.execute("insert into formuller(formul,bilesen1,bilesen2,bilesen3) values ('HCl','H','Cl',null)")
    
    cursor.execute("insert into musteri(musteri_id,musteri_adi,adres) values (1,'musteri1','Japonya,Tokyo')")
    cursor.execute("insert into musteri(musteri_id,musteri_adi,adres) values (2,'musteri2','Guney Afrika,Cape Town')")
    cursor.execute("insert into musteri(musteri_id,musteri_adi,adres) values (3,'musteri3','Ingiltere,Londra')")
    cursor.execute("insert into musteri(musteri_id,musteri_adi,adres) values (4,'musteri4','Turkiye,Ankara')")
    
    cursor.execute("insert into ulasim(id,ulke,sehir,uzaklik) values (1,'Turkiye','Ankara',342)")
    cursor.execute("insert into ulasim(id,ulke,sehir,uzaklik) values (2,'Turkiye','Eskisehir',214)")
    cursor.execute("insert into ulasim(id,ulke,sehir,uzaklik) values (3,'Turkiye','Gaziantep',1000)")
    cursor.execute("insert into ulasim(id,ulke,sehir,uzaklik) values (4,'Turkiye','Istanbul',111)")
    cursor.execute("insert into ulasim(id,ulke,sehir,uzaklik) values (5,'Ingiltere','Londra',2582)")
    cursor.execute("insert into ulasim(id,ulke,sehir,uzaklik) values (6,'Almanya','Berlin',1809)")
    cursor.execute("insert into ulasim(id,ulke,sehir,uzaklik) values (7,'Bosna Hersek','Saraybosna',1008)")
    
tabloOlustur()

#%%üretici bilgileri
ureticiAdi = "Uretici"
ureticiUlke = "Turkiye"
ureticiSehir = "Istanbul"

yimk = 1 #yurtici ulaşım maliyeti katsayısı
ydmk = 1.5 #yurtdışı ulaşım maliyeti katsayısı

imk= 1 #işçilik maliyeti katsayısı

tarih = "01012019"

kar_katsayisi = 20
#%% fonksiyonlar
def getTedarikciTablo():
    cursor.execute("select * from tedarikci")
    
    tedarikci_tablo = cursor.fetchall()

    return tedarikci_tablo

def getTedarikciHammaddeTablo():
    cursor.execute("select * from tedarikci_hammadde")
    
    tedarikci_hammadde_tablo = cursor.fetchall()

    return tedarikci_hammadde_tablo

def getStokHammaddeTablo():
    cursor.execute("select * from stok_hammadde")
    stok_hammadde_tablo = cursor.fetchall()

    return stok_hammadde_tablo

def getStokUrunTablo():
    cursor.execute("select * from stok_urun")
    stok_urun_tablo = cursor.fetchall()

    return stok_urun_tablo

def getMusteriTablo():
    cursor.execute("select * from musteri")
    musteri_tablo = cursor.fetchall()

    return musteri_tablo


def getFormulTablo():
    cursor.execute("select * from formuller")
    formul_tablo = cursor.fetchall()

    return formul_tablo

def getUlasimTablo():
    cursor.execute("select * from ulasim")
    ulasim_tablo = cursor.fetchall()

    return ulasim_tablo

def getSiparisTablo():
    cursor.execute("select * from siparisler")
    siparis_tablo = cursor.fetchall()

    return siparis_tablo


#############################################

def yeni_tedarikci(tedarikci_id,tedarikci_firma_adi,tedarikci_ulke,tedarikci_sehir):
    sorgu = "insert into tedarikci(id,ulke,sehir,firma_adi) values ("+tedarikci_id+",'"+tedarikci_ulke+"','"+tedarikci_sehir+"','"+tedarikci_firma_adi+"')"
    
    cursor.execute(sorgu)

def yeni_musteri(musteri_id,musteri_adi,musteri_adres):
    sorgu = "insert into musteri(musteri_id,musteri_adi,adres) values ("+musteri_id+",'"+musteri_adi+"','"+musteri_adres+"')"

    cursor.execute(sorgu)

def formul_ekle(formul,bilesen1,bilesen2,bilesen3):
    sorgu = "insert into formuller(formul,bilesen1,bilesen2,bilesen3) values ('"+formul+"','"+bilesen1+"','"+bilesen2+"','"+bilesen3+"')"

    cursor.execute(sorgu)
    
def tedarikci_listele(hammadde,miktar):
    sorgu1 = "drop view if exists tedarikci_fiyat"
    
    sorgu2 = "create view tedarikci_fiyat as select t.firma_adi,u.uzaklik,th.satis_fiyati*"+miktar+"+floor(if(u.ulke = 'Turkiye',u.uzaklik*"+str(yimk)+",u.uzaklik*"+str(ydmk)+")) as toplam\
            from tedarikci as t,tedarikci_hammadde as th,ulasim as u\
            where th.hammadde = '"+hammadde+"' and th.miktar >= "+miktar+"\
            and t.id = th.tedarikci_id and u.sehir = t.sehir\
            order by toplam asc"
    
    sorgu3 = "select * from tedarikci_fiyat"
    
    cursor.execute(sorgu1)
    
    cursor.execute(sorgu2)
    
    cursor.execute(sorgu3)
    
    sonuc = cursor.fetchall()
    
    tedarikci_liste = []
    
    for j in sonuc:
        tedarikci_liste.append(j[0]+" "*15+str(j[1])+" "*25+str(j[2]))
        
#        print(tedarikci_liste)
        
        print(j)

    
    return tedarikci_liste

def hammadde_satisi(index,miktar,hammadde):
    sorgu1 = "select * from tedarikci_fiyat limit 1 offset "+str(index)
    cursor.execute(sorgu1)
    sonuc = cursor.fetchall()[0]
    firma_adi = sonuc[0]
    fiyat = sonuc[2]
    
    print("firma ad : "+firma_adi)
    print("hammadde : "+hammadde)
    print(sonuc)
    
    
    sorgu2 = "select id from tedarikci where firma_adi = '"+firma_adi+"'"
    cursor.execute(sorgu2)
    firma_id = cursor.fetchall()[0][0]
    print("firma id : "+str(firma_id))
    
    sorgu3 = "select miktar from tedarikci_hammadde where tedarikci_id = "+str(firma_id)+" and hammadde = '"+hammadde+"'"
    cursor.execute(sorgu3)
    tedarikci_miktar = cursor.fetchall()[0][0]
    print("tedarikci miktar : "+str(tedarikci_miktar))
    
    sorgu4 = "select max(id) from stok_hammadde"
    cursor.execute(sorgu4)
    son_id = cursor.fetchall()[0][0]
    
    sorgu5 = "update tedarikci_hammadde set miktar = "+str(int(tedarikci_miktar)-int(miktar))+" where tedarikci_id = "+str(firma_id)+" and hammadde = '"+hammadde+"'"
    cursor.execute(sorgu5)
    
    sorgu6 = "insert into stok_hammadde(id,hammadde_ismi,alis_maliyeti,stok_miktar) values ("+str(int(son_id)+1)+",'"+hammadde+"',"+str(fiyat)+","+miktar+")" 
    cursor.execute(sorgu6)
    
def kimyasal_urun_liste():
    sorgu = "select formul from formuller"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        sonuc1.append(i[0])
        
    return sonuc1

def element_miktarlar(urun):
    sorgu = "select bilesen1,bilesen2,bilesen3 from formuller where formul = '"+urun+"'"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()

    sonuc1 = list(sonuc[0])
    
    print(sonuc1)
    
    elementler = {"C":0,"H":0,"O":0,"N":0,"S":0,"Cl":0}

    for i in sonuc1:
        if i == None or i == "":
            continue
        
        element = re.findall(r"([A-Z-a-z].|[A-Z-a-z])", i)[0]

        sayi = re.findall(r"([0-9]+[0-9]|[0-9])", i)
        
        if len(sayi) == 0:
            sayi = 1
        
        else:
            sayi = sayi[0]
        
        print(element)
        
        print(sayi)
        
        elementler[element] = sayi
        
    print(elementler)
        
    return elementler

def c_stok_liste(c_miktar):
    if c_miktar == 0:
        return []
    
    sorgu = "select * from stok_hammadde where stok_miktar >= "+str(c_miktar)+" and hammadde_ismi = 'C'"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    print(sonuc)
    
    sonuc1 = []
    
    for i in sonuc:
        row = str(i[0])+" | "+i[1]+" | "+str(i[2])+" | "+str(i[3])
        
        sonuc1.append(row)
    
    return sonuc1

def h_stok_liste(h_miktar):
    if h_miktar == 0:
        return []
    
    sorgu = "select * from stok_hammadde where stok_miktar >= "+str(h_miktar)+" and hammadde_ismi = 'H'"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        row = str(i[0])+" | "+i[1]+" | "+str(i[2])+" | "+str(i[3])
        
        sonuc1.append(row)
    
    return sonuc1

def o_stok_liste(o_miktar):
    if o_miktar == 0:
        return []
    
    sorgu = "select * from stok_hammadde where stok_miktar >= "+str(o_miktar)+" and hammadde_ismi = 'O'"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        row = str(i[0])+" | "+i[1]+" | "+str(i[2])+" | "+str(i[3])
        
        sonuc1.append(row)
    
    return sonuc1

def n_stok_liste(n_miktar):
    if n_miktar == 0:
        return []
    
    sorgu = "select * from stok_hammadde where stok_miktar >= "+str(n_miktar)+" and hammadde_ismi = 'N'"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        row = str(i[0])+" | "+i[1]+" | "+str(i[2])+" | "+str(i[3])
        
        sonuc1.append(row)
    
    return sonuc1

def s_stok_liste(n_miktar):
    if n_miktar == 0:
        return []
    
    sorgu = "select * from stok_hammadde where stok_miktar >= "+str(n_miktar)+" and hammadde_ismi = 'S'"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        row = str(i[0])+" | "+i[1]+" | "+str(i[2])+" | "+str(i[3])
        
        sonuc1.append(row)
    
    return sonuc1
def cl_stok_liste(n_miktar):
    if n_miktar == 0:
        return []
    
    sorgu = "select * from stok_hammadde where stok_miktar >= "+str(n_miktar)+" and hammadde_ismi = 'Cl'"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        row = str(i[0])+" | "+i[1]+" | "+str(i[2])+" | "+str(i[3])
        
        sonuc1.append(row)
    
    return sonuc1

def kimyasal_uret(urun,miktar,hammadde_miktarlar,secilen_hammaddeler,raf_omru,iscilik_maliyeti,toplam_maliyet):
    c_miktar,h_miktar,o_miktar,n_miktar,s_miktar,cl_miktar = hammadde_miktarlar
    
    print(secilen_hammaddeler)
    
    if c_miktar != 0:
        c_stok = secilen_hammaddeler[0]
        
        c_id,c,c_stok_maliyet,c_stok_miktar = c_stok.split(" | ")
        
        sorgu1 = "update stok_hammadde set stok_miktar = "+str(int(c_stok_miktar) - c_miktar)+" where id = '"+str(c_id)+"'"
        
        cursor.execute(sorgu1)
        
        sorgu2 = "update stok_hammadde set alis_maliyeti = "+str(int(c_stok_maliyet) - int(c_stok_maliyet)*c_miktar/int(c_stok_miktar))+" where id = '"+str(c_id)+"'"
        
        cursor.execute(sorgu2)
        
    if h_miktar != 0:
        h_stok = secilen_hammaddeler[1]    
        
        h_id,h,h_stok_maliyet,h_stok_miktar = h_stok.split(" | ")
        
        sorgu1 = "update stok_hammadde set stok_miktar = "+str(int(h_stok_miktar) - h_miktar)+" where id = '"+str(h_id)+"'"
        
        cursor.execute(sorgu1)
        
        sorgu2 = "update stok_hammadde set alis_maliyeti = "+str(int(h_stok_maliyet) - int(h_stok_maliyet)*h_miktar/int(h_stok_miktar))+" where id = '"+str(h_id)+"'"
        
        cursor.execute(sorgu2)
        
    if o_miktar != 0:
        o_stok = secilen_hammaddeler[2]    

        o_id,o,o_stok_maliyet,o_stok_miktar = o_stok.split(" | ")
        
        sorgu1 = "update stok_hammadde set stok_miktar = "+str(int(o_stok_miktar) - o_miktar)+" where id = '"+str(o_id)+"'"
        
        cursor.execute(sorgu1)
        
        sorgu2 = "update stok_hammadde set alis_maliyeti = "+str(int(o_stok_maliyet) - int(o_stok_maliyet)*o_miktar/int(o_stok_miktar))+" where id = '"+str(o_id)+"'"
        
        cursor.execute(sorgu2)
        
    if n_miktar != 0:
        n_stok = secilen_hammaddeler[3]    
     
        n_id,n,n_stok_maliyet,n_stok_miktar = n_stok.split(" | ")
        
        sorgu1 = "update stok_hammadde set stok_miktar = "+str(int(n_stok_miktar) - n_miktar)+" where id = '"+str(n_id)+"'"
        
        cursor.execute(sorgu1)
        
        sorgu2 = "update stok_hammadde set alis_maliyeti = "+str(int(n_stok_maliyet) - int(n_stok_maliyet)*n_miktar/int(n_stok_miktar))+"where id = '"+str(n_id)+"'"
        
        cursor.execute(sorgu2)                            
    
    if s_miktar != 0:
        s_stok = secilen_hammaddeler[4]    
     
        s_id,s,s_stok_maliyet,s_stok_miktar = s_stok.split(" | ")
        
        sorgu1 = "update stok_hammadde set stok_miktar = "+str(int(s_stok_miktar) - s_miktar)+" where id = '"+str(s_id)+"'"
        
        cursor.execute(sorgu1)
        
        sorgu2 = "update stok_hammadde set alis_maliyeti = "+str(int(s_stok_maliyet) - int(s_stok_maliyet)*s_miktar/int(s_stok_miktar))+"where id = '"+str(s_id)+"'"
        
        cursor.execute(sorgu2)     
    
    if cl_miktar != 0:
        cl_stok = secilen_hammaddeler[5]    
     
        cl_id,cl,cl_stok_maliyet,cl_stok_miktar = cl_stok.split(" | ")
        
        sorgu1 = "update stok_hammadde set stok_miktar = "+str(int(cl_stok_miktar) - cl_miktar)+" where id = '"+str(cl_id)+"'"
        
        cursor.execute(sorgu1)
        
        sorgu2 = "update stok_hammadde set alis_maliyeti = "+str(int(cl_stok_maliyet) - int(cl_stok_maliyet)*n_miktar/int(cl_stok_miktar))+"where id = '"+str(cl_id)+"'"
        
        cursor.execute(sorgu2)
    
    sorgu1 = "select max(id) from stok_hammadde"
    
    cursor.execute(sorgu1)

    son_id = cursor.fetchall()[0][0]
    
    sorgu2 = "insert into stok_urun(id,kimyasal_urun,miktar,uretim_tarihi,raf_omru,iscilik_maliyeti,toplam_maliyet,satis_fiyati) values \
    ("+str(son_id+1)+",'"+urun+"',"+str(miktar)+",'"+tarih+"',"+str(raf_omru)+","+str(iscilik_maliyeti)+","+toplam_maliyet+","+str(int(toplam_maliyet)+int(toplam_maliyet)*kar_katsayisi/100)+")"
    
    cursor.execute(sorgu2)
    
    #(id int,kimyasal_urun varchar(20),miktar int,uretim_tarihi varchar(10),raf_omru int,iscilik_maliyeti int, toplam_maliyet int,satis_fiyati int, primary key(id))

def musteriler():
    sorgu = "select musteri_adi from musteri"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        sonuc1.append(i[0]) 

    return sonuc1

def urunler():
    sorgu = "select formul from formuller"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        sonuc1.append(i[0])  
    
    return sonuc1

def siparis_ekle(musteri,urun,miktar):
    sorgu = "select max(id) from siparisler"
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()[0][0]
    
    if sonuc == None:
        sonuc = 0
   
    sorgu1 = "select musteri_id from musteri where musteri_adi = '"+musteri+"'"
    
    cursor.execute(sorgu1)
    
    musteri_id = cursor.fetchall()[0][0]
    
    sorgu1 = "insert into siparisler(id,musteri_id,siparis_tarihi,urun,miktar )\
    values ("+str(int(sonuc)+1)+","+str(musteri_id)+",'"+tarih+"','"+urun+"',"+str(miktar)+")"
    
    cursor.execute(sorgu1)
    
def stok_urunler(urun,miktar):
    sorgu = "select * from stok_urun where kimyasal_urun = '"+urun+"' and miktar >= "+miktar
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        row = str(i[0])+"   "+i[1]+"   "+str(i[2])+"   "+str(i[6])
        
        sonuc1.append(row)
   
    return sonuc1

def siparis_bul(urun,miktar):  
    sorgu = "select * from siparisler where urun = '"+urun+"' and miktar = "+miktar
    
    cursor.execute(sorgu)
    
    sonuc = cursor.fetchall()
    
    sonuc1 = []
    
    for i in sonuc:
        row = str(i[0])+"   "+i[3]+"   "+str(i[4])
        
        sonuc1.append(row)
    
    return sonuc1

def siparis_sil(siparis_id):
    sorgu = "delete from siparisler where id = "+str(siparis_id)
    
    cursor.execute(sorgu)
    