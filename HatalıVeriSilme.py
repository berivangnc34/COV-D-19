# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:28:52 2020

@author: Windows10
"""


import pandas as pd

df=pd.read_csv("covid_19_data.csv")

#sıralama yapmak için
#azalan şekilde sıralama oldugu için false
#ölüm oranları azalan şekilde sıralanmıştır
a1=df.sort_values(by='Deaths',ascending=False).head(20)
print(a1)

#silme işlemi yapma
df.drop(23651)
print(a1)

"drop ile silinme tam anlamıyla gerçekleşmiyor"
"bu yüzden atama işlemi gerçekleştirdik"
df=df.drop(23651)
print(df.sort_values(by='Deaths',ascending=False).head(20))

"sütunları silme işlemi"
df=df.drop("SNo",axis=1)
print(df.sort_values(by='Deaths',ascending=False).head(20))

#datasetteki verileri gruplandırma
#ortalamadaki ilk 10 veri ve otalama ölü sayısı
print(df.groupby("Province/State")["Deaths"].mean().head(10))

#en yüksek ölüm oranları
print(df.groupby("Province/State")["Deaths"].max().head(10))

print(df.groupby(["Province/State","Country/Region"])["Deaths"].max().head(10))



#eksik verilerle çalışma 
#öncelikle hangi sütunda kaç tane null deger var onu bul
print(df.isnull().sum())

#null degerlerini silmeyip o sütunun ortalamasını almak daha saglıklı
#bunu uygulayalım
df["Province/State"].fillna(method="ffill",inplace=True) #ffill null degerden önceki degeri yazar.
print(df.isnull().sum())








