# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 01:59:39 2019

@author: ASUS
"""

npm=int(input("input NPM : "))
DuaDigitTerakhir=abs(npm)%100
for i in range(DuaDigitTerakhir):
    print("Halo, ", npm, " Apa Kabar ?")