# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:09:30 2020

@author: Windows10
"""

#Farklı grafiklerin bir grafik halinde gösterimi

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")


türkiye=df[df["Country/Region"]=="Turkey"]
italya=df[df["Country/Region"]=="Italy"]
ispanya=df[df["Country/Region"]=="Spain"]
almanya=df[df["Country/Region"]=="Germany"]
kanada=df[df["Country/Region"]=="Canada"]

plt.scatter(türkiye.Deaths,türkiye.Recovered,color="blue",label="türkiyede ölen ve kurtulan hasta sayıları")
plt.scatter(italya.Deaths,italya.Recovered,color="yellow",label="italyada ölen ve kurtulan hasta sayıları")
plt.scatter(ispanya.Deaths,ispanya.Recovered,color="pink",label="ispanyada ölen ve kurtulan hasta sayıları")
plt.scatter(almanya.Deaths,almanya.Recovered,color="purple",label="Almanyada ölen ve kurtulan hasta sayıları")
plt.scatter(kanada.Deaths,kanada.Recovered,color="orange",label="Kanadada ölen ve kurtulan hasta sayıları")

plt.xlabel("Ölü Sayısı")
plt.ylabel("Kurtulan Sayısı")
plt.title("Dünyadaki coronavirüs analizi")
plt.legend()
plt.show()