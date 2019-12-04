# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:54:25 2019

@author: GL503GE
"""

class angAnggota:
   
   angJumlah = 0

   def __init__(self, nama, uang):
      self.nama = nama
      self.uang = uang
      angAnggota.angJumlah += 1
   
   def displayJumlah(self):
     print ("Total angAnggota %d" % angAnggota.angJumlah)

   def displayAnggota(self):
      print ("Nama : ", self.nama,  ", Uang: ", self.uang)



ang1 = angAnggota("budi", 2000)

ang2 = angAnggota("bedu", 5000)
ang1.displayAnggota()
ang2.displayAnggota()
print ("Total Anggota %d" % angAnggota.angJumlah)