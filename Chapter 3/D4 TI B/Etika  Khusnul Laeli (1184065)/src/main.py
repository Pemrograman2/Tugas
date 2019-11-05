# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:48:46 2019

@author: ANIF
"""
#main.py
import kalkulator

a=100
b=50

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

from Ngitung import Ngitung

a=100
b=50

hitung = Ngitung(a,b)

hasil1 = hitung.Penambahan()
hasil2 = hitung.Pengurangan()
hasil3 = hitung.Perkalian()
hasil4 = hitung.Pembagian()

lib = __import__('3lib')

npm = "1184065"

lib.printNPM(npm)
lib.perulangan(npm)
lib.printNPMTigaDigit(npm)
lib.printdigit_ketiga(npm)
lib.satupersatu(npm)
lib.printpenjumlahan(npm)
lib.printperkalian(npm)
lib.printNPMDigitGenap(npm)
lib.printNPMDigitGanjil(npm)
lib.printNPMDigitPrima(npm)
print()
from kelas3lib import kelas3lib

npm = "1184065"
k3lib = kelas3lib(npm)
k3lib.printNPM()
k3lib.perulangan()
k3lib.printNPMTigaDigit(npm)
k3lib.printdigit_ketiga(npm)
k3lib.satupersatu(npm)
k3lib.printpenjumlahan(npm)
k3lib.printperkalian(npm)
k3lib.printNPMDigitGenap(npm)
k3lib.printNPMDigitGanjil(npm)
k3lib.printNPMDigitPrima(npm)