# -*- coding: utf-8 -*-


import pandas as pd

#dataesti okuma
df=pd.read_csv("covid_19_data.csv")
print(df)

#verilerin satır ve sutun sayısını ögrenme
print(df.shape)
#sütundaki değerleri ögrenme
print(df.columns)
#sütunların veri türlerini ögrenme
print(df.dtypes)

#varsayılan olarak ilk 5 satır yazdırma
print(df.head())
#diger kullanımı
print(df.head(10))#ilk 10 satırı yazar.

#veri setindeki en son 5 degere ulaşma
print(df.tail())

#veri seti hakkında genel bilgilere erişme
print(df.info())

#boş olan degerleri tespit etme
print(df.isnull().sum())

#sütunları analiz etme işlemi
'string olmayan degerleri alır'
print(df.describe())

'stringlerin analizi için farklı bir yol kullanılır.'

print(df["Province/State" ].describe())

'sayısal olmayan bütün sütun degerlerine ulşamak istersek'
'yukarıdaki işlem zor olur'
'farklı bir yöntem uygularız'
a=(df.describe(include=["O"]))
print(a)

#her bir degerin kaç defa yazıldıgını 
#ögrenmek için
'veritabanına yazılma miktarlar'
b=(df["Country/Region"].value_counts())
print(b)

#şarta göre verileri listeleme
print(df[df["Province/State"]=="New York"])

















