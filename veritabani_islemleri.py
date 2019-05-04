# -*- coding: utf-8 -*-
import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="veritabani"#eğer yeni database oluşturmayacaksan bağlan
)

cursor = mydb.cursor()

#%%Tabloların oluşturulması

cursor.execute("drop table if exists tedarikci")
cursor.execute("drop table if exists tedarikci_hammadde")
cursor.execute("drop table if exists uretici")
cursor.execute("drop table if exists stok_hammadde")
cursor.execute("drop table if exists stok_urun")
cursor.execute("drop table if exists bilesenler")
cursor.execute("drop table if exists musteri")
cursor.execute("drop table if exists musteri_urun")

cursor.execute("create table tedarikci          (id varchar(10), konum varchar(30), firma_adi varchar(20), primary key(id))")
cursor.execute("create table tedarikci_hammadde (id varchar(10),tedarikci_id varchar(10) ,miktar int,uretim_tarihi varchar(10),raf_omru int,satis_fiyati int, primary key(id))")
cursor.execute("create table uretici            (firma_adi varchar(20),konum varchar(30))")
cursor.execute("create table stok_hammadde      (id varchar(10),hammadde_ismi varchar(10),alis_maliyeti int,stok_miktar int, primary key(id))")
cursor.execute("create table stok_urun          (id varchar(10),kimyasal_urun varchar(20),uretim_tarihi varchar(10),raf_omru int,iscilik_maliyeti int, toplam_maliyet int,satis_fiyati int, primary key(id))")
cursor.execute("create table musteri            (musteri_id varchar(10),musteriAdi varchar(20),adres varchar(50))")
cursor.execute("create table musteri_urun       (musteri_id varchar(10),urun varchar(20))")
cursor.execute("create table bilesenler         (stok_urun_id varchar(10),bilesen1 varchar(10),bilesen2 varchar(10),bilesen3 varchar(10))")

cursor.execute("insert into tedarikci(id,konum,firma_adi) values ('1','konum1','firma1')")
cursor.execute("insert into tedarikci(id,konum,firma_adi) values ('2','konum2','firma2')")
cursor.execute("insert into tedarikci(id,konum,firma_adi) values ('3','konum3','firma3')")

cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('1','1',2,'01012019',2,300)")
cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('2','1',8,'01012019',3,200)")
cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('3','1',3,'01012019',5,400)")
cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('4','2',5,'01012019',7,150)")
cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('5','2',7,'01012019',2,300)")
cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('6','2',8,'01012019',1,250)")
cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('7','3',2,'01012019',3,450)")
cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('8','3',8,'01012019',4,150)")
cursor.execute("insert into tedarikci_hammadde(id,tedarikci_id,miktar,uretim_tarihi,raf_omru,satis_fiyati) values ('9','3',1,'01012019',6,200)")

cursor.execute("insert into uretici(firma_adi,konum) values ('Uretici','Istanbul')")

cursor.execute("insert into stok_hammadde(id,hammadde_ismi,alis_maliyeti,stok_miktar) values (1,'C',300,10)")

cursor.execute("insert into stok_urun(id,kimyasal_urun,uretim_tarihi,raf_omru,iscilik_maliyeti,toplam_maliyet,satis_fiyati) values ('1','CO2','01012019',3,100,400,500)")
cursor.execute("insert into stok_urun(id,kimyasal_urun,uretim_tarihi,raf_omru,iscilik_maliyeti,toplam_maliyet,satis_fiyati) values ('2','H2O','01012019',4,250,600,750)")
cursor.execute("insert into stok_urun(id,kimyasal_urun,uretim_tarihi,raf_omru,iscilik_maliyeti,toplam_maliyet,satis_fiyati) values ('3','NH3','01012019',2,150,500,625)")

cursor.execute("insert into bilesenler(stok_urun_id,bilesen1,bilesen2,bilesen3) values ('1','C','2O',null)")
cursor.execute("insert into bilesenler(stok_urun_id,bilesen1,bilesen2,bilesen3) values ('2','2H','O',null)")
cursor.execute("insert into bilesenler(stok_urun_id,bilesen1,bilesen2,bilesen3) values ('3','N','3H',null)")

cursor.execute("insert into musteri(musteri_id,musteriAdi,adres) values ('1','musteri1','xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')")
cursor.execute("insert into musteri(musteri_id,musteriAdi,adres) values ('2','musteri2','yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')")
cursor.execute("insert into musteri(musteri_id,musteriAdi,adres) values ('3','musteri3','zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')")

cursor.execute("insert into musteri_urun(musteri_id,urun) values ('1','CO2')")
cursor.execute("insert into musteri_urun(musteri_id,urun) values ('1','H2O')")
cursor.execute("insert into musteri_urun(musteri_id,urun) values ('1','NH3')")
cursor.execute("insert into musteri_urun(musteri_id,urun) values ('2','CO2')")
cursor.execute("insert into musteri_urun(musteri_id,urun) values ('2','H2O')")
cursor.execute("insert into musteri_urun(musteri_id,urun) values ('2','NH3')")
cursor.execute("insert into musteri_urun(musteri_id,urun) values ('3','CO2')")
cursor.execute("insert into musteri_urun(musteri_id,urun) values ('3','H2O')")
cursor.execute("insert into musteri_urun(musteri_id,urun) values ('3','NH3')")

cursor = mydb.cursor(buffered=True)

cursor.execute("select * from tedarikci")
tedarikci_tablo = cursor.fetchall()
for i in tedarikci_tablo:
    print(i)

cursor.execute("select * from tedarikci_hammadde")
tedarikci_hammadde_tablo = cursor.fetchall()

for i in tedarikci_hammadde_tablo:
    print(i)

cursor.execute("select * from uretici")
uretici_tablo = cursor.fetchall()
for i in uretici_tablo:
    print(i)

cursor.execute("select * from stok_hammadde")
stok_hammadde_tablo = cursor.fetchall()
for i in stok_hammadde_tablo:
    print(i)

cursor.execute("select * from stok_urun")
stok_urun_tablo = cursor.fetchall()
for i in stok_urun_tablo:
    print(i)

cursor.execute("select * from musteri")
musteri_tablo = cursor.fetchall()
for i in musteri_tablo:
    print(i)

cursor.execute("select * from musteri_urun")
musteri_urun_tablo = cursor.fetchall()
for i in musteri_urun_tablo:
    print(i)

cursor.execute("select * from bilesenler")
bilesen_tablo = cursor.fetchall()
for i in bilesen_tablo:
    print(i)


#sonuc = cursor.fetchall()

