# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:06:04 2019

@author: Dell
"""

npm=int(input("input NPM : "))
DuaDigitTerakhir=abs(npm)%100
for i in range(DuaDigitTerakhir):
    print("Hallo, ", npm, " Apa Kabar ?")