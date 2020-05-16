# -*- coding: utf-8 -*-

##PANDAS
#veri temizleme ve veri analizi modülü
#iki veri yapısına sahiptir. series ve dataframe
#numpy dizilerinde bulunan elemanlar aynı veri tipinde olurken pandas
#birden fazla farklı veri tipine sahip olabilir.
#seriler numpy dizilerine benzer

import numpy as np
import pandas as pd


#serimizi oluşturduk
sayılar=[0,1,2,3,4,5,6,7,8,9]
seriler=pd.Series(data=sayılar)

print(seriler.sum())

print(seriler.min())

print(seriler.max())

print(seriler.mean())

print(seriler.median())

print(seriler.var())

print(seriler.std())

sayılar2=[9,8,7,6,5,4,3,2,1,0]
seriler2=pd.Series(data=sayılar2)

print(seriler+seriler2)
print(seriler+5)
print(seriler2-seriler)
print(seriler*seriler2)
print(seriler*3)
print(seriler2*3)

#seriler=pd.Series(data,index)
#data sabit değer alabilir
#data liste aalbilir.
#data numpy dizisi alabilir.
#data dictionary(sözlük) degeri alabilir.

sayılar=[0,1,2,3,4,5,6,7,8,9]
numpy_array=np.array(sayılar)#nesne oluşturma
print(numpy_array)

#pandasta seri oluştur
seriler=pd.Series(data=sayılar)
print(seriler)

my_index=['a','b','c','d','e','f','g','h','i','j']
seriler=pd.Series(data=sayılar, index=my_index ,dtype=float)
print(seriler)

#sözlük veri tipini data olarak kullanalım
sözlük={'a':0,'b':1,'c':2,'d':3} #key ve value degerleri
seriler=pd.Series(data=sözlük)
print(seriler)

#pandas serilerinin boyutunu ögrenme
print(seriler.ndim)
#veri tipi ögrenme
print(seriler.dtype)
#satır ve sutun sayısı ögrenme
print(seriler.shape)

 





