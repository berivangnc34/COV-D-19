# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:00:00 2020

@author: Windows10
"""

import pandas as pd

#veri setini okuma
df=pd.read_csv("covid_19_data.csv")
print(df)

#sadece virüsün görüldügü şehirleri yazmak istersek
first=df["Province/State"]
print(first)

#aynı anda birden fazla sütuna ulaşmak istersek
second=df[["Province/State","Country/Region"]]
print(second)

"ilk parametre ulaşılmak istenen satır"
"ikinci parametre ulaşılmak istenen sütun"
#log(satir,sütun)
#log istenilen satır ve sütuna ulaşılmasını sağlar
c1=df.loc[1]
print(c1)

#belirli bir satır aralıgına ulaşmak istersek
c2=df.loc[1:55]
print(c2)

#belirtilmiş olan sütunlardaki satırları alalım
c3=df.loc[:,"Province/State"]
print(c3)

#iki sütun degeri alarak tüm satırları yazma
#iki sütun alınacagı için iki tane köşeli parantez kullan 
c4=df.loc[:,["Province/State","Country/Region"]]
print(c4)

"belirli satır aralıklarını alma"
c5=df.loc[3:48,["Province/State","Country/Region"]]
print(c5)

"istenilen indeks degerine göre satırın hepsini yazma"
c6=df.iloc[5]
print(c6)

"şart oluşturma"
c7=df[df.Deaths<10]
print(c7)

c8=df[df.Recovered<50]
print(c8)









