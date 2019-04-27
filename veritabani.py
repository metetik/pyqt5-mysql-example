# -*- coding: utf-8 -*-
#import and connect

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSql
import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="db1"#eğer yeni database oluşturmayacaksan bağlan
)

print(mydb)

#%%Create db

mycursor = mydb.cursor()

#mycursor.execute("create database db1")

for x in mycursor:
    print(x)

#%%
#mycursor.execute("create table tablo1(id int,isim varchar(20),soyisim varchar(20))")

#%%
mycursor.execute("insert into tablo1 values(1,'isim1','soyisim1')")
mycursor.execute("insert into tablo1 values(2,'isim2','soyisim2')")
mycursor.execute("insert into tablo1 values(3,'isim1','soyisim3')")
mycursor.execute("insert into tablo1 values(4,'isim1','soyisim4')")
mycursor.execute("insert into tablo1 values(5,'isim1','soyisim5')")

#%%
mycursor.execute("SELECT * FROM tablo1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
#%%
type(myresult)  

for i in range(5):
    j = str(i)
    print(myresult[i],"->",j)

