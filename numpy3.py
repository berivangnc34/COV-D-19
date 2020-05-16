# -*- coding: utf-8 -*-

import numpy as np

a=np.floor(np.random.random((3,4)))
print(a)
a=np.floor(10*np.random.random((3,4)))
print(a)

#oluşmuş olan diziyi tek satır içinde yazma
print(a.ravel())
print("-------------")
print(a.reshape(6,2))
print("-------------")
print(a.T)

#sıralama yapma
print(a.ravel(order="C"))
print(a.ravel(order="F"))
print(a.ravel(order="A"))
print(a.ravel(order="K"))


#numpy stack yapısı
a=np.floor(10*np.random.random((3,3)))
print(a)
b=np.floor(10*np.random.random((3,3)))
print(b)


#OLUŞMUŞ OLAN MATRİSSLERİ BİRARAYA GETİRME
print(np.stack(((a,b))))
#yatay birleştirme
print(np.vstack((a,b)))
#dikey birleştirme
print(np.hstack((a,b)))

a=np.arange(12)
b=a
print(b is a)
#b objesinde yapılan degisiklikler a objesinide etkiledi
b.shape=4,3
print(a.shape)

#farklı arrayler aynı dataya bakacak
#aynı verilere sahip olacak 
c=a.view()
print(c is a) #atama işlemi yapılmadıgı için false döner
print(c.base is a) #aynı verileri barındırdıgı için true döner

#veriler cyemi ait onun kontrolü
print(c.flags.owndata)

#c objesinin satır ve sütun degerleri
#cdeki degisiklik a degerine uyarlanmamıştır.
c.shape=6,2
print(a.shape)

#cde yapılan degisiklik a degerine uyarlandı.
#aynı verileri taşıyorlar çünkü
c[4,1]=1453
print(a)

#adaki verileri kopyalayalım
#kopyalama oldugu için d degerinde yapılan 
#degisiklikler a degerine geçmez.
d=a.copy()
print(d is a)
print(d.base is a)

#indeksleme
d[1,1]=571
print(a.shape)


























