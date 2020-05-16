# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:17:51 2020

@author: Windows10
"""

import numpy as np

python_list=[0,2,3,5,5,5]
#np kütüphanesinden dizi şeklinde array olacagı için gösterimi bu şekildedir.
numpy_array=np.array([1,3,3,4,5,6,7,7,8,9])

print(python_list)
print(numpy_array)

#boyutunu öğrenmek için yapılan işlem
print(numpy_array.ndim)

#2boyutlu dizi oluşturma
numpy_array2=np.array([[3,4,33,4,5,6,5]])
print(numpy_array2)
print(numpy_array2.ndim)

#boyutu göstermke için
print(numpy_array.shape)
print(numpy_array2.shape)

#boyut degerini degistirmek icin
print(numpy_array.reshape(2,3))


#arange kullanımı (baslangıc,bitis,artıs)
print(np.arange(0,15,3))
print(np.arange(5))

#[satır.sutun]

numpy_array=numpy_array.reshape(5,2)
print(numpy_array)
print(numpy_array[0])
print(numpy_array[0:4])

print(numpy_array[:,0])

#diziyi tersten yazma
print(numpy_array[::-1])

#sıfır matris olşuturma
print(np.zeros((6,6)))

#birlerden oluşan matris için
print(np.ones((5,6,8)))

#birim matris oluşturma
#sütun sayısı belirtilmez satır sayısı belirtilir.
print(np.eye(6))

#dizilerde birleştirme işlemi için
#satır bazlı birleştirme
print(np.concatenate([numpy_array,numpy_array],axis=0))

#sütun bazlı birleştirme
print(np.concatenate([numpy_array,numpy_array],axis=1))




























