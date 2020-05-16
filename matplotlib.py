# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:54:12 2020

@author: Windows10
"""
#VERİ GÖRSELLEŞTİRME
#veri görselleştirme dagınık verileri kolay
#anlaşılır hale getirir. 
#öncelikle doğru grafik türü seçilmelidir.
#renk  uyumuna dikkat edilmeli
#dikkat dagıtıcı veri olmamamlı
#verilerin yerleştirilmesi doğru yapılmalıdır.

"matplotlib"
#verilerin 2 boyutlu görselleştirilmesi

import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")

#veri setini tabloya aktarma
df.plot()
#tabloları yazdırma
plt.show()

"sno degerini grafikten silelim."
df=df.drop("SNo",axis=1)
df.plot()
plt.show()



türkiye=df[df["Country/Region"]=="Turkey"]
print(türkiye.columns)
#ilk deger x ekseni
#ikinci deger y ekseni
#grafigin rengi
#çizgilerin ne anlama geldigi
plt.plot(türkiye.Deaths,türkiye.Recovered,color="pink",label="Türkiyede Ölen Ve Kurtulan Hasta Sayıları")
plt.xlabel("Ölüm Sayısı")
plt.ylabel("Kurtulan Sayısı")
plt.title("TÜRKİYE CORONAVİRÜS ANALİZİ")
#LABELİN KONUMUNU BELİRLEME
plt.legend()
plt.show()



italya=df[df["Country/Region"]=="Italy"]
plt.plot(italya.Deaths,italya.Recovered,color="orange",label="italyada Ölen Ve Kurtulan Hasta Sayıları")
plt.xlabel("Ölüm Sayısı")
plt.ylabel("Kurtulan İnsan Sayısı")
plt.title("İTALYA CORONAVİRÜS ANALİZİ")
plt.legend()
plt.show()


ispanya=df[df["Country/Region"]=="Spain"]
plt.plot(ispanya.Deaths,ispanya.Recovered,color="blue",label="ispanyada ölen ve kurtulan insan sayısı")
plt.xlabel("Ölüm Sayısı")
plt.ylabel("Kurtulan İnsan Sayısı")
plt.title("İSPANYA CORONAVİRÜS ANALİZİ")
plt.legend()
plt.show()

#GRAFİGİ DİKDÖRTGEN PARÇALARA BÖLME ve NOKTASAL HALE GETİRME
ispanya.plot(grid=True,linestyle=":",color="blue")
plt.show()

 


























