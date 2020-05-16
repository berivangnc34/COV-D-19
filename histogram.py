# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:24:47 2020

@author: Windows10
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")

türkiye=df[df["Country/Region"]=="Turkey"]
italya=df[df["Country/Region"]=="Italy"]
ispanya=df[df["Country/Region"]=="Spain"]

#bins=bar sayısı
plt.hist(italya.Deaths,bins=7,color="grey")
plt.xlabel("Ölüm Sayısı")
plt.ylabel("deger aralıgı")
plt.title("İtalya Coronavirüs analizi")


plt.hist(ispanya.Deaths,bins=7,color="pink")
plt.xlabel("Ölüm Sayısı")
plt.ylabel("deger aralıgı")
plt.title("İspanya Coronavirüs analizi")


plt.show()