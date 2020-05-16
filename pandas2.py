# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:25:09 2020

@author: Windows10
"""

import pandas as pd


#dataframe
#veriyi daha kolay işlememizi sağlar
#dataframede farklı türden data parametreleri alır.
#onunla ilgili örnekler çözeceğiz
#veri=pd.Dataframe(data,index)

sözlük1=dict(a=5,b=2,c=8,d=7)
sözlük2=dict(a=1,b=3,c=5,d=8)
data1=dict(ilk=sözlük1,ikinci=sözlük2)
df1=pd.DataFrame(data1)
print(df1)

#dataframeleri serilerden seçerek oluşturma
s1=pd.Series([1,2,3,4,5])
s2=pd.Series(['a','b','c','d','e'])
data2=dict(ilk=s1,ikinci=s2)
df2=pd.DataFrame(data2)
print(df2)





sayılar=[0,1,2,3,4,5,6,7,8,9]
seriler=pd.Series(data=sayılar)

#pandasta indekste şart işlemi
print(seriler[seriler>5] )  
print(seriler[seriler>seriler.mean()])

print(seriler[seriler==4])
print(seriler[seriler<=5])
