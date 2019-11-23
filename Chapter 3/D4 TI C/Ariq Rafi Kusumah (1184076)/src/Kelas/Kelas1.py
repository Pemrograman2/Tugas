# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:48:49 2019

@author: Asus
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