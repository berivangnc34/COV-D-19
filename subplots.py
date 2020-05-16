# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:13:24 2020

@author: Windows10
"""

#SUBPLOT İLE İKİ GRAFİGİ ÜST ÜSTE YAZDIRABİLİRSİN
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")


ispanya=df[df["Country/Region"]=="Spain"]
türkiye=df[df["Country/Region"]=="Turkey"]
italya=df[df["Country/Region"]=="Italy"]
çin=df[df["Country/Region"]=="China"]
almanya=df[df["Country/Region"]=="Germany"]

#SUBPLOT OLUŞTURMA
#ilk parametre kaç subplot olacagıdır.
#ikinci parametre nerede yer alacagı
#üçüncü ise 1.grafik demek

df.plot(subplots=True)

plt.subplot(2,1,1)
plt.plot(ispanya.Deaths,ispanya.Recovered,color="green",label="İapanyada ölen ve iyileşen hasta sayısı")
plt.xlabel("ispanyada ölüm oranı")
plt.ylabel("ispanyada iyileşme")



plt.subplot(2,1,2)
plt.plot(italya.Deaths,italya.Recovered,color="grey",label="İtalyada ölen ve iyileşen hasta sayısı")
plt.xlabel("italyada ölüm oranı")
plt.ylabel("italyada iyileşme ")

plt.show()

plt.subplot(5,1,3)
plt.plot(türkiye.Deaths,türkiye.Recovered,color="purple",label="Türkiyede ölen ve iyileşen hasta sayısı")
plt.xlabel("Türkiyede ölüm oranı")
plt.ylabel("Türkiyede iyileşme")


plt.subplot(5,1,4)
plt.plot(çin.Deaths,çin.Recovered,color="purple",label="Çinde ölen ve iyileşen hasta sayısı")
plt.xlabel("Çinde ölüm oranı")
plt.ylabel("Çinde iyileşme")




plt.subplot(5,1,5)
plt.plot(almanya.Deaths,almanya.Recovered,color="purple",label="Almanyada ölen ve iyileşen hasta sayısı")
plt.xlabel("Almanyada ölüm oranı")
plt.ylabel("Almanyada iyileşme")
"""







