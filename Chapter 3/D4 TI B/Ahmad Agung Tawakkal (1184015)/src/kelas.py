# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:46:08 2019

@author: Ahmad Agung Tawakkal
"""


class Bapak(object):
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat

    def berjalan(self):
        print("Berjalan ke depan")

    def berlari(self):
        print("Berlari dengan cepat")


# class Anak turunan dari class Bapak
class Anak(Bapak):
    pass


b = Bapak("Wiragan", 170, 68)
print()
print("Nama:", b.nama)
print("Tinggi:", b.tinggi, "cm")
print("Berat:", b.berat, "kg")
b.berjalan()
b.berlari()

# objek dari class Anak memiliki seluruh yang dimiliki class Bapak
a = Anak("Mustofa", 140, 32)
print()
print("Nama:", a.nama)
print("Tinggi:", a.tinggi, "cm")
print("Berat:", a.berat, "kg")
a.berjalan()
a.berlari()