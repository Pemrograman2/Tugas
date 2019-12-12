# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:37:07 2019

@author: ASUS
"""

npm=int(input("input NPM : "))
DuaDigitTerakhir=abs(npm)%100
for i in range(DuaDigitTerakhir):
    print("Halo, ", npm, " Apa Kabar ?")