# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:51:25 2019

@author: Asus
"""

lib = __import__('3lib')

npm = "1184041"

lib.printNPM(npm)
lib.printNPMDuaDigitBelakang(npm)
lib.printNPMTigaDigitBelakang(npm)
lib.printNPMDigitKetigaBelakang(npm)
lib.printNPMSatuSatu(npm)
lib.printNPMPenjumlahan(npm)
lib.printNPMPerkalian(npm)
lib.printNPMGenap(npm)
lib.printNPMGanjil(npm)
lib.printNPMPrima(npm)
print()

from kelas3lib import kelas3lib

npm = "1184041"

k3lib = kelas3lib(npm)

k3lib.printNPM()
k3lib.printNPMDuaDijit()
k3lib.printNPMTigaDijit()
k3lib.printNPMDigitKetiga()
k3lib.printNPMSatuPersatu()
k3lib.printNPMPenjumlahan()
k3lib.printNPMPerkalian()
k3lib.printNPMDijitGenap()
k3lib.printNPMDijitGanjil()
k3lib.printNPMDijitPrima()