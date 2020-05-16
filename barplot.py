# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:33:29 2020

@author: Windows10
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")

"""
amerika=df[df["Country/Region"]=="UK"]
italya=df[df["Country/Region"]=="Italy"]
ispanya=df[df["Country/Region"]=="Spain"]


plt.bar(italya.Deaths,italya.Recovered)
plt.show()


sayı=np.array([1,2,3,4,5,6,7,8,9])
karesi=sayı**2


plt.bar(sayı,karesi)
plt.xlabel("Sayı degeri")
plt.ylabel("Sayının Karesi")
plt.title("sayıların karesini alma")

plt.show()
"""


ülke=["türkiye","abd","almanya","italya","ispanya","fransa","güney kore","japonya","uk","çin","hindistan"]
oran=[40,34.7,29.2,12.5,11.6,10.6,9.7,7.3,6.6,3.6,2.3]
plt.xlabel("Ülkeler")
plt.ylabel("Oranlar")
plt.title("YOGUN BAKIM YATAK SAYISI" )#100bin kişi başına düşen

plt.bar(ülke,oran,color="grey")
plt.show()
