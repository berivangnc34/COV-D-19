# -*- coding: utf-8 -*-

import numpy as np
numpy_array=np.array([1,2,3,4,5,6,7,8,9])
numpy_array=numpy_array.reshape(3,3)
print(numpy_array)

#dizisde maksimum eleman bulma
print(numpy_array.max())

#dizide minimum elemanı bulma
print(numpy_array.min())

#dizide toplama işlemi
print(numpy_array.sum())

#satırları toplama
print(numpy_array.sum(axis=1))

#sütunların toplamı
print(numpy_array.sum(axis=0))

#dizinin ortalamasını bulma
print(numpy_array.mean())
print(np.median(numpy_array))
#dizinin varyansı hesaplama
print(numpy_array.var())
#stabdart sapma hesaplama
print(numpy_array.std())

#ikinci dizi olşuturma
numpy_array2=np.array([2,5,3,6,7,4,9,8,4])
#3e 3lük matris haline getirmek için reshape kullanılır.
numpy_array2=numpy_array2.reshape(3,3)

#matrislerarası toplama işlemi
print(np.add(numpy_array,numpy_array2))
#çıkarma işlemi
print(np.subtract(numpy_array2,numpy_array))
#matrisler arası çarpma işlemi,normal çarpma işlemi yapılır.
print(np.multiply(numpy_array,numpy_array2))

#trigonometrik işlemler
print(np.sin(numpy_array))
print("-------------------")
print(np.cos(numpy_array))
print("-------------------")
print(np.sqrt(numpy_array))
print("-------------------")
print(np.exp(numpy_array))
print("-------------------")
print(np.log(numpy_array))
print("-------------------")
print(numpy_array.T)
print("------------------- TRANSPOZ ALMA")
print(numpy_array2.T)

#BOOLEAN DEGER SORGULAMA

boolean_array=numpy_array>=6
print(boolean_array)
print("-------------------")
print(numpy_array[boolean_array])


























